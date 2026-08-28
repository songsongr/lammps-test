::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::: {#fix-neighbor-swap-command .section}
[]{#index-0}

# fix neighbor/swap command[](#fix-neighbor-swap-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID neighbor/swap N X seed T R0 voro-ID keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- neighbor/swap = style name of this fix command

- N = invoke this fix every N steps

- X = number of swaps to attempt every N steps

- seed = random \# seed (positive integer)

- T = scaling temperature of the MC swaps (temperature units)

- R0 = scaling swap probability of the MC swaps (distance units)

- voro-ID = valid voronoi compute id (compute voronoi/atom)

- one or more keyword/value pairs may be appended to args

- keywords *types* and *diff* are mutually exclusive, but one must be specified

- keyword = *types* or *diff* or *ke* or *region* or *rates*

  ``` literal-block
  types values = two or more atom types (Integers in range [1,Ntypes] or type labels)
  diff values = one atom type
  ke value = yes or no
    yes = kinetic energy is conserved after atom swaps
    no = no conservation of kinetic energy after atom swaps
  region value = region-ID
    region-ID = ID of region to use as an exchange/move volume
  rates values = V1 V2 . . . Vntypes values to conduct variable diffusion for different atom types (unitless)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute voroN all voronoi/atom neighbors yes
    fix mc all neighbor/swap 10 160 15238 1000.0 3.0 voroN diff 2
    fix myFix all neighbor/swap 100 1 12345 298.0 3.0 voroN region my_swap_region types 5 6
    fix kmc all neighbor/swap 1 100 345 1.0 3.0 voroN diff 3 rates 3 1 6
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 22Jul2025.]{.versionmodified .added}
:::

This fix performs Monte-Carlo (MC) evaluations to enable kinetic Monte Carlo (kMC)-type behavior during MD simulation by allowing neighboring atoms to swap their positions. In contrast to the [[fix atom/swap]{.doc}]fix_atom_swap.md){.reference .internal} command which swaps pairs of atoms anywhere in the simulation domain, the restriction of the MC swapping to neighbors enables a hybrid MD/kMC-like simulation.

Neighboring atoms are defined by using a Voronoi tesselation performed by the [[compute voronoi/atom]{.doc}]compute_voronoi_atom.md){.reference .internal} command. Two atoms are neighbors if their Voronoi cells share a common face (3d) or edge (2d).

The selection of a swap neighbor is made using a distance-based criterion for weighting the selection probability of each swap, in the same manner as kMC selects a next event using relative probabilities. The acceptance or rejection of each swap is determined via the Metropolis criterion after evaluating the change in system energy due to the swap.

A detailed explanation of the original implementation of this algorithm can be found in [[(Tavenner 2023)]{.std .std-ref}](#tavennermdkmc){.reference .internal} where it was used to simulated accelerated diffusion in an MD context.

Simulating inherently kinetically-limited behaviors which rely on rare events (such as atomic diffusion in a solid) is challenging for traditional MD since its relatively short timescale will not naturally sample many events. This fix addresses this challenge by allowing rare neighbor hopping events to be sampled in a kMC-like fashion at a much faster rate (set by the specified *N* and *X* parameters). This enables the processes of atomic diffusion to be approximated during an MD simulation, effectively decoupling the MD atomic vibrational timescale and the atomic hopping (kMC event) timescale.

The algorithm implemented by this fix is as follows:

> ::: {}
> - The MD simulation is paused every *N* steps
>
> - A Voronoi tesselation is performed for the current atom configuration.
>
> - Then *X* atom swaps are attempted, one after the other.
>
> - For each swap, an atom *I* is selected randomly from the list of atom types specified by either the *types* or *diff* keywords.
>
> - One of *I*'s Voronoi neighbors *J* is selected using the distance-weighted probability for each neighbor detailed below.
>
> - The *I,J* atom IDs are communicated to all processors so that a global energy evaluation can be performed for the post-swap state of the system.
>
> - The swap is accepted or rejected based on the Metropolis criterion using the energy change of the system and the specified temperature *T*.
> :::

::: {.admonition .note}
Note

To run an MC-only simulation (no MD), you should define no time-integration fix, set the [[thermo]{.doc}]thermo.md){.reference .internal} command to 1, set *N* to 1, and set *X* small enough to see the MC evolution of the system. But if *X* is too small, the overhead at the start and stop of MC moves each timestep will slow down the simulation.
:::

Here are a few comments on the computational cost of the swapping algorithm.

> ::: {}
> 1.  The cost of a global energy evaluation is similar to that of an MD timestep.
>
> 2.  Similar to other MC algorithms in LAMMPS, improved parallel efficiency is achieved with a smaller number of atoms per processor than would typically be used in an standard MD simulation. This is because the per-energy evaluation cost increases relative to the balance of MD/MC steps as indicated by 1., but the communication cost remains relatively constant for a given number of MD steps.
>
> 3.  The MC portion of the simulation will run dramatically slower if the pair style uses different cutoffs for different atom types (or type pairs). This is because each atom swap then requires a rebuild of the neighbor list to ensure the post-swap global energy can be computed correctly.
> :::

Limitations are imposed on selection of *I,J* atom pairs to avoid swapping of atoms which are outside of a reasonable cutoff (e.g. due to a Voronoi tesselation near free surfaces) though the use of a distance-weighted probability scaling.

------------------------------------------------------------------------

This section gives more details on other arguments and keywords.

The random number generator (RNG) used by all the processors for MC operations is initialized with the specified *seed*.

The distance-based probability is weighted by the specified *R0* which sets the radius [\\(r_0\\)]{.math .notranslate .nohighlight} in this formula

::: {.math .notranslate .nohighlight}
\\\[p\_{ij} = e\^{(\\frac{r\_{ij}}{r_0})\^2}\\\]
:::

where [\\(p\_{ij}\\)]{.math .notranslate .nohighlight} is the probability of selecting atom [\\(j\\)]{.math .notranslate .nohighlight} to swap with atom [\\(i\\)]{.math .notranslate .nohighlight}. Typically, a value for *R0* around the average nearest-neighbor spacing is appropriate. Since this is simply a probability weighting, the swapping behavior is not very sensitive to the exact value of *R0*.

The required *voro-ID* value is the compute-ID of a [[compute voronoi/atom]{.doc}]compute_voronoi_atom.md){.reference .internal} command like this:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute compute-ID group-ID voronoi/atom neighbors yes
:::
::::

It must return per-atom list of valid neighbor IDs as in the [[compute voronoi/atom]{.doc}]compute_voronoi_atom.md){.reference .internal} command.

The keyword *types* takes two or more atom types as its values. Only atoms *I* of the first atom type will be selected. Only atoms *J* of the remaining atom types will be considered as potential swap partners.

The keyword *diff* take a single atom type as its value. Only atoms *I* of the that atom type will be selected. Atoms *J* of all remaining atom types will be considered as potential swap partners. This includes the atom type specified with the *diff* keyword to account for self-diffusive hops between two atoms of the same type.

Note that the *neighbors yes* option must be enabled for use with this fix. The group-ID should include all the atoms which this fix will potentially select. I.e. the group-ID used in the voronoi compute should include the same atoms as that indicated by the *types* keyword. If the *diff* keyword is used, the group-ID should include atoms of all types in the simulation.

The keyword *ke* takes *yes* (default) or *no* as its value. It two atoms are swapped with different masses, then a value of *yes* will rescale their respective velocities to conserve the kinetic energy of the system. A value of *no* will perform no rescaling, so that kinetic energy is not conserved. See the restriction on this keyword below.

The *region* keyword takes a *region-ID* as its value. If specified, then only atoms *I* and *J* within the geometric region will be considered as swap partners. See the [[region]{.doc}]region.md){.reference .internal} command for details. This means the group-ID for the [[compute voronoi/atom]{.doc}]compute_voronoi_atom.md){.reference .internal} command also need only contain atoms within the region.

The keyword *rates* can modify the swap rate based on the type of atom *J*. Ntype values must be specified, where Ntype = the number of atom types in the system. Each value is used to scale the probability weighting given by the equation above. In the third example command above, a simulation has 3 atoms types. Atom *I\*s of type 1 are eligible for swapping. Swaps may occur with atom \*J\*s of all 3 types. Assuming all \*J* atoms are equidistant from an atom *I*, *J* atoms of type 1 will be 3x more likely to be selected as a swap partner than atoms of type 2. And *J* atoms of type 3 will be 6.5x more likely to be selected than atoms of type 2. If the *rates* keyword is not used, all atom types will be treated with the same probability during selection of swap attempts.
::::::::

------------------------------------------------------------------------

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

Fix *neighbor/swap* supports the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix will pass geometry information about atoms involved in a swap to *dump image* so that these atoms can be highlighted in the visualization as additional spheres. For how long those additional spheres will be shown depends on the value of the *vizsteps* setting (default is 1000) which can be changed by using the [[fix_modify command]{.doc}]fix_modify.md){.reference .internal}. If an atom is involved in multiple swaps, the check on showing the additional graphics depends on the timestep of its last swap.

The color of the additional spheres is by default that of the atom type *before* the swap when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

The *fflag1* setting of *dump image fix* has no effect.

The *fflag2* setting allows you to set the radius of the added spheres, since the radius is set to zero internally.
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the state of the fix to [[binary restart files]{.doc}]restart.md){.reference .internal}. This includes information about the random number generator seed, the next timestep for MC exchanges, and the number of exchange attempts and successes. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix computes a global vector of length 2, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The vector values are the following global cumulative quantities:

> ::: {}
> 1.  swap attempts
>
> 2.  swap accepts
> :::

The vector values calculated by this fix are "intensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info. Also this fix requires that the [[VORONOI package]{.std .std-ref}]Packages_details.md#pkg-voronoi){.reference .internal} is installed, otherwise the fix will not be compiled.

The [[compute voronoi/atom]{.doc}]compute_voronoi_atom.md){.reference .internal} command referenced by the required voro-ID must return neighboring atoms as illustrated in the examples above.

If this fix is used with systems that do not have per-type masses (e.g. atom style sphere), the *ke* keyword must be set to *off* since the implemented algorithm will not be able to re-scale velocities properly.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[compute voronoi/atom]{.doc}]compute_voronoi_atom.md){.reference .internal} [[delete_atoms]{.doc}]delete_atoms.md){.reference .internal}, [[fix gcmc]{.doc}]fix_gcmc.md){.reference .internal}, [[fix atom/swap]{.doc}]fix_atom_swap.md){.reference .internal}, [[fix mol/swap]{.doc}]fix_mol_swap.md){.reference .internal}, [[fix sgcmc]{.doc}]fix_sgcmc.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *ke* = yes and *rates* = 1 for all atom types.

------------------------------------------------------------------------

**(Tavenner 2023)** J Tavenner, M Mendelev, J Lawson, Computational

:   Materials Science, 218, 111929 (2023).
:::
:::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

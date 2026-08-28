:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-widom-command .section}
[]{#index-0}

# fix widom command[](#fix-widom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID widom N M type seed T keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- widom = style name of this fix command

- N = invoke this fix every N steps

- M = number of Widom insertions to attempt every N steps

- type = atom type (1-Ntypes or type label) for inserted atoms (must be 0 if mol keyword used)

- seed = random \# seed (positive integer)

- T = temperature of the system (temperature units)

- zero or more keyword/value pairs may be appended to args

  ``` literal-block
  keyword = mol, region, full_energy, charge, intra_energy
    mol value = template-ID
      template-ID = ID of molecule template specified in a separate molecule command
    region value = region-ID
      region-ID = ID of region where Widom insertions are allowed
    full_energy = compute the entire system energy when performing Widom insertions
    charge value = charge of inserted atoms (charge units)
    intra_energy value = intramolecular energy (energy units)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 2 gas widom 1 50000 1 19494 2.0
    fix 3 water widom 1000 100 0 29494 300.0 mol h2omol full_energy

    labelmap atom 1 Li
    fix 2 ion widom 1 50000 Li 19494 2.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix performs Widom insertions of atoms or molecules at the given temperature as discussed in [[(Frenkel)]{.std .std-ref}](#frenkel1){.reference .internal}. Specific uses include computation of Henry constants of small molecules in microporous materials or amorphous systems.

Every N timesteps the fix attempts M number of Widom insertions of atoms or molecules.

If the *mol* keyword is used, only molecule insertions are performed. Conversely, if the *mol* keyword is not used, only atom insertions are performed.

This command may optionally use the *region* keyword to define an insertion volume. The specified region must have been previously defined with a [[region]{.doc}]region.md){.reference .internal} command. It must be defined with side = *in*. Insertion attempts occur only within the specified region. For non-rectangular regions, random trial points are generated within the rectangular bounding box until a point is found that lies inside the region. If no valid point is generated after 1000 trials, no insertion is performed. If an attempted insertion places the atom or molecule center-of-mass outside the specified region, a new attempted insertion is generated. This process is repeated until the atom or molecule center-of-mass is inside the specified region.

Note that neighbor lists are re-built every timestep that this fix is invoked, so you should not set N to be too small. See the [[neighbor]{.doc}]neighbor.md){.reference .internal} command for details.

When an atom or molecule is to be inserted, its coordinates are chosen at a random position within the current simulation cell or region. Relative coordinates for atoms in a molecule are taken from the template molecule provided by the user. The center of mass of the molecule is placed at the insertion point. The orientation of the molecule is chosen at random by rotating about this point.

Individual atoms are inserted, unless the *mol* keyword is used. It specifies a *template-ID* previously defined using the [[molecule]{.doc}]molecule.md){.reference .internal} command, which reads a file that defines the molecule. The coordinates, atom types, charges, etc., as well as any bonding and special neighbor information for the molecule can be specified in the molecule file. See the [[molecule]{.doc}]molecule.md){.reference .internal} command for details. The only settings required to be in this file are the coordinates and types of atoms in the molecule.

Note that fix widom does not use configurational bias MC or any other kind of sampling of intramolecular degrees of freedom. Inserted molecules can have different orientations, but they will all have the same intramolecular configuration, which was specified in the molecule command input.

For atoms, inserted particles have the specified atom type. For molecules, they use the same atom types as in the template molecule supplied by the user.

The excess chemical potential mu_ex is defined as:

::: {.math .notranslate .nohighlight}
\\\[\\mu\_{ex} = -kT \\ln(\<\\exp(-(U\_{N+1}-U\_{N})/{k_B T})\>)\\\]
:::

where [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant, [\\(T\\)]{.math .notranslate .nohighlight} is the user-specified temperature, [\\(U_N\\)]{.math .notranslate .nohighlight} and [\\(U\_{N+1}\\)]{.math .notranslate .nohighlight} is the potential energy of the system with [\\(N\\)]{.math .notranslate .nohighlight} and [\\(N+1\\)]{.math .notranslate .nohighlight} particles.

The *full_energy* option means that the fix calculates the total potential energy of the entire simulated system, instead of just the energy of the part that is changed. By default, this option is off, in which case only partial energies are computed to determine the energy difference due to the proposed change.

The *full_energy* option is needed for systems with complicated potential energy calculations, including the following:

- long-range electrostatics (kspace)

- many-body pair styles

- hybrid pair styles

- eam pair styles

- tail corrections

- need to include potential energy contributions from other fixes

In these cases, LAMMPS will automatically apply the *full_energy* keyword and issue a warning message.

When the *mol* keyword is used, the *full_energy* option also includes the intramolecular energy of inserted and deleted molecules, whereas this energy is not included when *full_energy* is not used. If this is not desired, the *intra_energy* keyword can be used to define an amount of energy that is subtracted from the final energy when a molecule is inserted, and subtracted from the initial energy when a molecule is deleted. For molecules that have a non-zero intramolecular energy, this will ensure roughly the same behavior whether or not the *full_energy* option is used.

Some fixes have an associated potential energy. Examples of such fixes include: [[efield]{.doc}]fix_efield.md){.reference .internal}, [[gravity]{.doc}]fix_gravity.md){.reference .internal}, [[addforce]{.doc}]fix_addforce.md){.reference .internal}, [[restrain]{.doc}]fix_restrain.md){.reference .internal}, and [[wall fixes]{.doc}]fix_wall.md){.reference .internal}. For that energy to be included in the total potential energy of the system (the quantity used when performing Widom insertions), you MUST enable the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for that fix. The doc pages for individual [[fix]{.doc}]fix.md){.reference .internal} commands specify if this should be done.

Use the *charge* option to insert atoms with a user-specified point charge. Note that doing so will cause the system to become non-neutral. LAMMPS issues a warning when using long-range electrostatics (kspace) with non-neutral systems. See the [[compute group/group]{.doc}]compute_group_group.md){.reference .internal} documentation for more details about simulating non-neutral systems with kspace on.
::::

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the state of the fix to [[binary restart files]{.doc}]restart.md){.reference .internal}. This includes information about the random number generator seed, the next timestep for Widom insertions etc. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

::: {.admonition .note}
Note

For this to work correctly, the timestep must **not** be changed after reading the restart with [[reset_timestep]{.doc}]reset_timestep.md){.reference .internal}. The fix will try to detect it and stop with an error.
:::

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix computes a global vector of length 3, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The vector values are the following global cumulative quantities:

> ::: {}
> 1.  average excess chemical potential on each timestep
>
> 2.  average difference in potential energy on each timestep
>
> 3.  volume of the insertion region
> :::

The vector values calculated by this fix are "intensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

Do not set "neigh_modify once yes" or else this fix will never be called. Reneighboring is **required**.

This fix style requires an [[atom style]{.doc}]atom_style.md){.reference .internal} with per atom type masses.

Can be run in parallel, but some aspects of the insertion procedure will not scale well in parallel. Only usable for 3D simulations.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix gcmc]{.doc}]fix_gcmc.md){.reference .internal} [[fix atom/swap]{.doc}]fix_atom_swap.md){.reference .internal}, [[neighbor]{.doc}]neighbor.md){.reference .internal}, [[fix deposit]{.doc}]fix_deposit.md){.reference .internal}, [[fix evaporate]{.doc}]fix_evaporate.md){.reference .internal},
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are mol = no, intra_energy = 0.0 and full_energy = no, except for the situations where full_energy is required, as listed above.

------------------------------------------------------------------------

**(Frenkel)** Frenkel and Smit, Understanding Molecular Simulation, Academic Press, London, 2002.
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

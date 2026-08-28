:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-atom-swap-command .section}
[]{#index-0}

# fix atom/swap command[](#fix-atom-swap-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID atom/swap N X seed T keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- atom/swap = style name of this fix command

- N = invoke this fix every N steps

- X = number of swaps to attempt every N steps

- seed = random \# seed (positive integer)

- T = scaling temperature of the MC swaps (temperature units)

- one or more keyword/value pairs may be appended to args

- keyword = *types* or *mu* or *ke* or *semi-grand* or *region*

  ``` literal-block
  types values = two or more atom types (1-Ntypes or type label)
  mu values = chemical potential of swap types (energy units)
  ke value = no or yes
    no = no conservation of kinetic energy after atom swaps
    yes = kinetic energy is conserved after atom swaps
  semi-grand value = no or yes
    no = particle type counts and fractions conserved
    yes = semi-grand canonical ensemble, particle fractions not conserved
  region value = region-ID
    region-ID = ID of region to use as an exchange/move volume
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 2 all atom/swap 1 1 29494 300.0 ke no types 1 2
    fix myFix all atom/swap 100 1 12345 298.0 region my_swap_region types 5 6
    fix SGMC all atom/swap 1 100 345 1.0 semi-grand yes types 1 2 3 mu 0.0 4.3 -5.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix performs Monte Carlo swaps of atoms of one given atom type with atoms of the other given atom types. The specified scaling temperature *T* is used in the Metropolis criterion dictating swap probabilities.

Perform *X* swaps of atoms of one type with atoms of another type according to a Monte Carlo probability. Swap candidates must be in the fix group, must be in the region (if specified), and must be of one of the listed types. Swaps are attempted between candidates that are chosen randomly with equal probability among the candidate atoms. Swaps are not attempted between atoms of the same type since nothing would happen.

All atoms in the simulation domain can also be moved using regular time integration displacements (e.g., via [[fix nvt]{.doc}]fix_nh.md){.reference .internal}), resulting in a hybrid MC+MD simulation, where \$X\$ MC swap attempts are made once every \$N\$ MD steps. A smaller-than-usual timestep size may be needed when running such a hybrid simulation, especially if the swapped atoms are not well equilibrated.

::: {.admonition .note}
Note

To run an MC-only simulation (no MD), you should define no time-integration fix, set the [[thermo]{.doc}]thermo.md){.reference .internal} command to 1, set *N* to 1, and set *X* small enough to see the MC evolution of the system. But if *X* is too small, the overhead at the start and stop of MC moves each timestep will slow down the simulation.
:::

The *types* keyword is required. At least two atom types must be specified. If not using *semi-grand*, exactly two atom types are required.

The *ke* keyword can be set to *no* to turn off kinetic energy conservation for swaps. The default is *yes*, which means that swapped atoms have their velocities scaled by the ratio of the masses of the swapped atom types. This ensures that the kinetic energy of each atom is the same after the swap as it was before the swap, even though the atom masses have changed.

The *semi-grand* keyword can be set to *yes* to switch to the semi-grand canonical ensemble as discussed in [[(Sadigh)]{.std .std-ref}](#sadigh){.reference .internal}. This means that the total number of each particle type does not need to be conserved. The default is *no*, which means that the only kind of swap allowed exchanges an atom of one type with an atom of a different given type. In other words, the relative mole fractions of the swapped atoms remains constant. Whereas in the semi-grand canonical ensemble, the composition of the system can change. Note that when using *semi-grand*, atoms in the fix group whose type is not listed in the *types* keyword are ineligible for attempted conversion. An attempt is made to switch the selected atom (if eligible) to one of the other listed types with equal probability. Acceptance of each attempt depends upon the Metropolis criterion.

The *mu* keyword allows users to specify chemical potentials. This is required and allowed only when using *semi-grand*. All chemical potentials are absolute, so there is one for each swap type listed following the *types* keyword. In semi-grand canonical ensemble simulations the chemical composition of the system is controlled by the difference in these values. So shifting all values by a constant amount will have no effect on the simulation.

This command may optionally use the *region* keyword to define swap volume. The specified region must have been previously defined with a [[region]{.doc}]region.md){.reference .internal} command. It must be defined with side = *in*. Swap attempts occur only between atoms that are both within the specified region. Swaps are not otherwise attempted.

You should ensure you do not swap atoms belonging to a molecule, or LAMMPS will eventually generate an error when it tries to find those atoms. LAMMPS will warn you if any of the atoms eligible for swapping have a non-zero molecule ID, but does not check for this at the time of swapping.

If not using *semi-grand* this fix checks to ensure all atoms of the given types have the same atomic charge. LAMMPS does not enforce this in general, but it is needed for this fix to simplify the swapping procedure. Successful swaps will swap the atom type and charge of the swapped atoms. Conversely, when using *semi-grand*, it is assumed that all the atom types involved in switches have the same charge. Otherwise, charge would not be conserved. As a consequence, no checks on atomic charges are performed, and successful switches update the atom type but not the atom charge. While it is possible to use *semi-grand* with groups of atoms that have different charges, these charges will not be changed when the atom types change. The same applies for systems with per-atom masses: non *semi-grand* will swap atom masses, but the masses have to be the same each for the atom types. When using *semi-grand* no per-atom masses are changed.

Since this fix computes total potential energies before and after proposed swaps, even complicated potential energy calculations are acceptable, including the following:

- long-range electrostatics ([\\(k\\)]{.math .notranslate .nohighlight}-space)

- many body pair styles

- hybrid pair styles (with restrictions)

- EAM pair styles

- triclinic systems

Some fixes have an associated potential energy. Examples of such fixes include: [[efield]{.doc}]fix_efield.md){.reference .internal}, [[gravity]{.doc}]fix_gravity.md){.reference .internal}, [[addforce]{.doc}]fix_addforce.md){.reference .internal}, [[langevin]{.doc}]fix_langevin.md){.reference .internal}, [[restrain]{.doc}]fix_restrain.md){.reference .internal}, [[temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal}, [[temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, and [[wall fixes]{.doc}]fix_wall.md){.reference .internal}. For that energy to be included in the total potential energy of the system (the quantity used when performing GCMC moves), you **must** enable the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for that fix. The doc pages for individual [[fix]{.doc}]fix.md){.reference .internal} commands specify if this should be done.
::::

------------------------------------------------------------------------

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

Fix *atom/swap* supports the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix will pass geometry information about atoms involved in a swap to *dump image* so that these atoms can be highlighted in the visualization as additional spheres. For how long those additional spheres will be shown depends on the value of the *vizsteps* setting (default is 1000) which can be changed by using the [[fix_modify command]{.doc}]fix_modify.md){.reference .internal}. If an atom is involved in multiple swaps, the check on showing the additional graphics depends on the timestep of its last swap.

The color of the additional spheres is by default that of the atom type *before* the swap when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

The *fflag1* setting of *dump image fix* has no effect.

The *fflag2* setting allows you to set the radius of the added spheres, since the radius is set to zero internally.
::::

------------------------------------------------------------------------

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the state of the fix to [[binary restart files]{.doc}]restart.md){.reference .internal}. This includes information about the random number generator seed, the next timestep for MC exchanges, the number of exchange attempts and successes, etc. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

::: {.admonition .note}
Note

For this to work correctly, the timestep must **not** be changed after reading the restart with [[reset_timestep]{.doc}]reset_timestep.md){.reference .internal}. The fix will try to detect it and stop with an error.
:::

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix computes a global vector of length 2, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The vector values are the following global cumulative quantities:

> ::: {}
> 1.  swap attempts
>
> 2.  swap accepts
> :::

The vector values calculated by this fix are "intensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

When this fix is used with a [[hybrid pair style]{.doc}]pair_hybrid.md){.reference .internal} system, only swaps between atom types of the same sub-style (or combination of sub-styles) are permitted.

This fix can be used with systems that have per-atom masses (e.g. atom style sphere) provided all atoms of the types handled by this fix have the same mass per type. The fix will check for that. In case both, per-type and per-atom masses are present, a warning is printed.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[neighbor]{.doc}]neighbor.md){.reference .internal}, [[fix deposit]{.doc}]fix_deposit.md){.reference .internal}, [[fix evaporate]{.doc}]fix_evaporate.md){.reference .internal}, [[delete_atoms]{.doc}]delete_atoms.md){.reference .internal}, [[fix gcmc]{.doc}]fix_gcmc.md){.reference .internal}, [[fix mol/swap]{.doc}]fix_mol_swap.md){.reference .internal}, [[fix sgcmc]{.doc}]fix_sgcmc.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *ke* = yes, *semi-grand* = no, *mu* = 0.0 for all atom types.

------------------------------------------------------------------------

**(Sadigh)** B Sadigh, P Erhart, A Stukowski, A Caro, E Martinez, and L Zepeda-Ruiz, Phys. Rev. B, 85, 184203 (2012).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

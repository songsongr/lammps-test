::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::: {#input-script-structure .section}
# [6.3. ]{.section-number}Input script structure[](#input-script-structure "Link to this heading"){.headerlink}

This page describes the structure of a typical LAMMPS input script. The examples directory in the LAMMPS distribution contains many sample input scripts; it is discussed on the [[Examples]{.doc}]Examples.md){.reference .internal} doc page.

A LAMMPS input script typically has 4 parts:

1.  [[Initialization]{.std .std-ref}](#init){.reference .internal}

2.  [[System definition]{.std .std-ref}](#system){.reference .internal}

3.  [[Simulation settings]{.std .std-ref}](#settings){.reference .internal}

4.  [[Run a simulation]{.std .std-ref}](#run){.reference .internal}

The last 2 parts can be repeated as many times as desired. I.e. run a simulation, change some settings, run some more, etc. Each of the 4 parts is now described in more detail. Remember that almost all commands need only be used if a non-default value is desired.

::: {#initialization .section}
[]{#init}

## [6.3.1. ]{.section-number}Initialization[](#initialization "Link to this heading"){.headerlink}

Set parameters that need to be defined before atoms are created or read-in from a file.

The relevant commands are [[units]{.doc}]units.md){.reference .internal}, [[dimension]{.doc}]dimension.md){.reference .internal}, [[newton]{.doc}]newton.md){.reference .internal}, [[processors]{.doc}]processors.md){.reference .internal}, [[boundary]{.doc}]boundary.md){.reference .internal}, [[atom_style]{.doc}]atom_style.md){.reference .internal}, [[atom_modify]{.doc}]atom_modify.md){.reference .internal}.

If force-field parameters appear in the files that will be read, these commands tell LAMMPS what kinds of force fields are being used: [[pair_style]{.doc}]pair_style.md){.reference .internal}, [[bond_style]{.doc}]bond_style.md){.reference .internal}, [[angle_style]{.doc}]angle_style.md){.reference .internal}, [[dihedral_style]{.doc}]dihedral_style.md){.reference .internal}, [[improper_style]{.doc}]improper_style.md){.reference .internal}.
:::

::: {#system-definition .section}
[]{#system}

## [6.3.2. ]{.section-number}System definition[](#system-definition "Link to this heading"){.headerlink}

There are 3 ways to define the simulation cell and reserve space for force field info and fill it with atoms in LAMMPS. Read them in from (1) a data file or (2) a restart file via the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, respectively. These files can also contain molecular topology information. Or (3) create a simulation cell and fill it with atoms on a lattice (with no molecular topology), using these commands: [[lattice]{.doc}]lattice.md){.reference .internal}, [[region]{.doc}]region.md){.reference .internal}, [[create_box]{.doc}]create_box.md){.reference .internal}, [[create_atoms]{.doc}]create_atoms.md){.reference .internal} or [[read_dump]{.doc}]read_dump.md){.reference .internal}.

The entire set of atoms can be duplicated to make a larger simulation using the [[replicate]{.doc}]replicate.md){.reference .internal} command.
:::

::: {#simulation-settings .section}
[]{#settings}

## [6.3.3. ]{.section-number}Simulation settings[](#simulation-settings "Link to this heading"){.headerlink}

Once atoms and molecular topology are defined, a variety of settings can be specified: force field coefficients, simulation parameters, output options, and more.

Force field coefficients are set by these commands (they can also be set in the read-in files): [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}, [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}, [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal}, [[kspace_style]{.doc}]kspace_style.md){.reference .internal}, [[dielectric]{.doc}]dielectric.md){.reference .internal}, [[special_bonds]{.doc}]special_bonds.md){.reference .internal}.

Various simulation parameters are set by these commands: [[neighbor]{.doc}]neighbor.md){.reference .internal}, [[neigh_modify]{.doc}]neigh_modify.md){.reference .internal}, [[group]{.doc}]group.md){.reference .internal}, [[timestep]{.doc}]timestep.md){.reference .internal}, [[reset_timestep]{.doc}]reset_timestep.md){.reference .internal}, [[run_style]{.doc}]run_style.md){.reference .internal}, [[min_style]{.doc}]min_style.md){.reference .internal}, [[min_modify]{.doc}]min_modify.md){.reference .internal}.

Fixes impose a variety of boundary conditions, time integration, and diagnostic options. The [[fix]{.doc}]fix.md){.reference .internal} command comes in many flavors.

Various computations can be specified for execution during a simulation using the [[compute]{.doc}]compute.md){.reference .internal}, [[compute_modify]{.doc}]compute_modify.md){.reference .internal}, and [[variable]{.doc}]variable.md){.reference .internal} commands.

Output options are set by the [[thermo]{.doc}]thermo.md){.reference .internal}, [[dump]{.doc}]dump.md){.reference .internal}, and [[restart]{.doc}]restart.md){.reference .internal} commands.
:::

::: {#run-a-simulation .section}
[]{#run}

## [6.3.4. ]{.section-number}Run a simulation[](#run-a-simulation "Link to this heading"){.headerlink}

A molecular dynamics simulation is run using the [[run]{.doc}]run.md){.reference .internal} command. Energy minimization (molecular statics) is performed using the [[minimize]{.doc}]minimize.md){.reference .internal} command. A parallel tempering (replica-exchange) simulation can be run using the [[temper]{.doc}]temper.md){.reference .internal} command.
:::
:::::::
::::::::
:::::::::

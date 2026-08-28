:::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::: {#fix-gcmc-command .section}
[]{#index-0}

# fix gcmc command[](#fix-gcmc-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID gcmc N X M type seed T mu displace keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- gcmc = style name of this fix command

- N = invoke this fix every N steps

- X = average number of GCMC exchanges to attempt every N steps

- M = average number of MC moves to attempt every N steps

- type = atom type (1-Ntypes or type label) for inserted atoms (must be 0 if mol keyword used)

- seed = random \# seed (positive integer)

- T = temperature of the ideal gas reservoir (temperature units)

- mu = chemical potential of the ideal gas reservoir (energy units)

- displace = maximum Monte Carlo translation distance (length units)

- zero or more keyword/value pairs may be appended to args

  ``` literal-block
  keyword = mol or mcmoves or rigid or shake or region or maxangle or pressure or fugacity_coeff or full_energy or charge or group or grouptype or intra_energy or tfac_insert or overlap_cutoff or max or min
    mol value = template-ID
      template-ID = ID of molecule template specified in a separate molecule command
    mcmoves values = Patomtrans Pmoltrans Pmolrotate
      Patomtrans = proportion of atom translation MC moves
      Pmoltrans = proportion of molecule translation MC moves
      Pmolrotate = proportion of molecule rotation MC moves
    rigid value = fix-ID
      fix-ID = ID of fix rigid/small command
    shake value = fix-ID
      fix-ID = ID of fix shake command
    region value = region-ID
      region-ID = ID of region where GCMC exchanges and MC moves are allowed
    maxangle value = maximum molecular rotation angle (degrees)
    pressure value = pressure of the gas reservoir (pressure units)
    fugacity_coeff value = fugacity coefficient of the gas reservoir (unitless)
    full_energy = compute the entire system energy when performing GCMC exchanges and MC moves
    charge value = charge of inserted atoms (charge units)
    group value = group-ID
      group-ID = group-ID for inserted atoms (string)
    grouptype values = type group-ID
      type = atom type (1-Ntypes or type label)
      group-ID = group-ID for inserted atoms (string)
    intra_energy value = intramolecular energy (energy units)
    tfac_insert value = scale up/down temperature of inserted atoms (unitless)
    overlap_cutoff value = maximum pair distance for overlap rejection (distance units)
    max value = Maximum number of atoms allowed in the fix group (and region)
    min value = Minimum number of atoms allowed in the fix group (and region)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 2 gas gcmc 10 1000 1000 2 29494 298.0 -0.5 0.01
    fix 3 water gcmc 10 100 100 0 3456543 3.0 -2.5 0.1 mol my_one_water maxangle 180 full_energy
    fix 4 my_gas gcmc 1 10 10 1 123456543 300.0 -12.5 1.0 region disk

    labelmap atom 1 Li
    fix 2 ion gcmc 10 1000 1000 Li 29494 298.0 -0.5 0.01
:::
::::
:::::

:::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix performs grand canonical Monte Carlo (GCMC) exchanges of atoms or molecules with an imaginary ideal gas reservoir at the specified *T* and chemical potential ([\\(\\mu\\)]{.math .notranslate .nohighlight}) as discussed in [[(Frenkel)]{.std .std-ref}](#frenkel2){.reference .internal}. It also attempts Monte Carlo (MC) moves (translations and molecule rotations) within the simulation cell or region. If used with the [[fix nvt]{.doc}]fix_nh.md){.reference .internal} command, simulations in the grand canonical ensemble (muVT, constant chemical potential, constant volume, and constant temperature) can be performed. Specific uses include computing isotherms in microporous materials, or computing vapor-liquid coexistence curves.

Every *N* timesteps the fix attempts both GCMC exchanges (insertions or deletions) and MC moves of gas atoms or molecules. On those timesteps, the average number of attempted GCMC exchanges is *X*, while the average number of attempted MC moves is *M*. For GCMC exchanges of either molecular or atomic gasses, these exchanges can be either deletions or insertions, with equal probability.

::: {.admonition .note}
Note

To run an MC-only simulation (no MD), you should define no time-integration fix, set the [[thermo]{.doc}]thermo.md){.reference .internal} command to 1, set *N* to 1, and set *X+M* small enough to see the MC evolution of the system. But if *X+M* is too small, the overhead at the start and stop of MC moves each timestep will slow down the simulation.
:::

The possible choices for MC moves are translation of an atom, translation of a molecule, and rotation of a molecule. The relative amounts of each are determined by the optional *mcmoves* keyword (see below). The default behavior is as follows. If the *mol* keyword is used, only molecule translations and molecule rotations are performed with equal probability. Conversely, if the *mol* keyword is not used, only atom translations are performed. *M* should typically be chosen to be approximately equal to the expected number of gas atoms or molecules of the given type within the simulation cell or region, which will result in roughly one MC move per atom or molecule per MC cycle.

All inserted particles are always added to two groups: the default group "all" and the fix group specified in the fix command. In addition, particles are also added to any groups specified by the *group* and *grouptype* keywords. If inserted particles are individual atoms, they are assigned the atom type given by the type argument. If they are molecules, the type argument has no effect and must be set to zero. Instead, the type of each atom in the inserted molecule is specified in the file read by the [[molecule]{.doc}]molecule.md){.reference .internal} command.

::: {.admonition .note}
Note

Care should be taken to apply *fix gcmc* to a group that contains *only* those atoms and molecules that you wish to manipulate using Monte Carlo. Hence it is generally not a good idea to specify the default group "all" in the fix command, although it is allowed.
:::

This fix cannot be used to perform GCMC insertions of gas atoms or molecules other than the exchanged type, but GCMC deletions, and MC translations, and rotations can be performed on any atom/molecule in the fix group. All atoms in the simulation cell can be moved using regular time integration translations, e.g. via [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, resulting in a hybrid GCMC+MD simulation. A smaller-than-usual timestep size may be needed when running such a hybrid simulation, especially if the inserted molecules are not well equilibrated.

This command may optionally use the *region* keyword to define an exchange and move volume. The specified region must have been previously defined with a [[region]{.doc}]region.md){.reference .internal} command. It must be defined with side = *in*. Insertion attempts occur only within the specified region. For non-rectangular regions, random trial points are generated within the rectangular bounding box until a point is found that lies inside the region. If no valid point is generated after 1000 trials, no insertion is performed, but it is counted as an attempted insertion. Move and deletion attempt candidates are selected from gas atoms or molecules within the region. If there are no candidates, no move or deletion is performed, but it is counted as an attempt move or deletion. If an attempted move places the atom or molecule center-of-mass outside the specified region, a new attempted move is generated. This process is repeated until the atom or molecule center-of-mass is inside the specified region.

If used with [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, the temperature of the imaginary reservoir, *T*, should be set to be equivalent to the target temperature used in fix nvt. Otherwise, the imaginary reservoir will not be in thermal equilibrium with the simulation cell. Also, it is important that the temperature used by *fix nvt* is dynamically updated, which can be achieved as follows:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute mdtemp mdatoms temp
    compute_modify mdtemp dynamic/dof yes
    fix mdnvt mdatoms nvt temp 300.0 300.0 10.0
    fix_modify mdnvt temp mdtemp
:::
::::

Note that neighbor lists are re-built every timestep that this fix is invoked, so you should not set *N* to be too small. However, periodic rebuilds are necessary in order to avoid dangerous rebuilds and missed interactions. Specifically, avoid performing so many MC translations per timestep that atoms can move beyond the neighbor list skin distance. See the [[neighbor]{.doc}]neighbor.md){.reference .internal} command for details.

When an atom or molecule is to be inserted, its coordinates are chosen at a random position within the current simulation cell or region, and new atom velocities are randomly chosen from the specified temperature distribution given by *T*. The effective temperature for new atom velocities can be increased or decreased using the optional keyword *tfac_insert* (see below). Relative coordinates for atoms in a molecule are taken from the template molecule provided by the user. The center of mass of the molecule is placed at the insertion point. The orientation of the molecule is chosen at random by rotating about this point.

Individual atoms are inserted, unless the *mol* keyword is used. It specifies a *template-ID* previously defined using the [[molecule]{.doc}]molecule.md){.reference .internal} command, which reads a file that defines the molecule. The coordinates, atom types, charges, etc., as well as any bonding and special neighbor information for the molecule can be specified in the molecule file. See the [[molecule]{.doc}]molecule.md){.reference .internal} command for details. The only settings required to be in this file are the coordinates and types of atoms in the molecule.

When not using the *mol* keyword, you should ensure you do not delete atoms that are bonded to other atoms, or LAMMPS will soon generate an error when it tries to find bonded neighbors. LAMMPS will warn you if any of the atoms eligible for deletion have a non-zero molecule ID, but does not check for this at the time of deletion.

If you wish to insert molecules using the *mol* keyword that will be treated as rigid bodies, use the *rigid* keyword, specifying as its value the ID of a separate [[fix rigid/small]{.doc}]fix_rigid.md){.reference .internal} command which also appears in your input script.

::: {.admonition .note}
Note

If you wish the new rigid molecules (and other rigid molecules) to be thermostatted correctly via [[fix rigid/small/nvt]{.doc}]fix_rigid.md){.reference .internal} or [[fix rigid/small/npt]{.doc}]fix_rigid.md){.reference .internal}, then you need to use the [[fix_modify dynamic/dof yes]{.doc}]fix_modify.md){.reference .internal} command for the rigid fix. This is to inform that fix that the molecule count will vary dynamically.
:::

If you wish to insert molecules via the *mol* keyword, that will have their bonds or angles constrained via SHAKE, use the *shake* keyword, specifying as its value the ID of a separate [[fix shake]{.doc}]fix_shake.md){.reference .internal} command which also appears in your input script.

Optionally, users may specify the relative amounts of different MC moves using the *mcmoves* keyword. The values *Patomtrans*, *Pmoltrans*, *Pmolrotate* specify the average proportion of atom translations, molecule translations, and molecule rotations, respectively. The values must be non-negative integers or real numbers, with at least one non-zero value. For example, (10,30,0) would result in 25% of the MC moves being atomic translations, 75% molecular translations, and no molecular rotations.

Optionally, users may specify the maximum rotation angle for molecular rotations using the *maxangle* keyword and specifying the angle in degrees. Rotations are performed by generating a random point on the unit sphere and a random rotation angle on the range \[0,maxangle). The molecule is then rotated by that angle about an axis passing through the molecule center of mass. The axis is parallel to the unit vector defined by the point on the unit sphere. The same procedure is used for randomly rotating molecules when they are inserted, except that the maximum angle is 360 degrees.

Note that *fix gcmc* does not use configurational bias MC or any other kind of sampling of intramolecular degrees of freedom. Inserted molecules can have different orientations, but they will all have the same intramolecular configuration, which was specified in the molecule command input.

For atomic gasses, inserted atoms have the specified atom type, but deleted atoms are any atoms that have been inserted or that already belong to the fix group. For molecular gasses, exchanged molecules use the same atom types as in the template molecule supplied by the user. In both cases, exchanged atoms/molecules are assigned to two groups: the default group "all" and the fix group (which can also be "all").

The chemical potential is a user-specified input parameter defined as:

::: {.math .notranslate .nohighlight}
\\\[\\mu = \\mu\^{id} + \\mu\^{ex}\\\]
:::

The second term [\\(\\mu\^{ex}\\)]{.math .notranslate .nohighlight} is the excess chemical potential due to energetic interactions and is formally zero for the fictitious gas reservoir but is non-zero for interacting systems. So, while the chemical potential of the reservoir and the simulation cell are equal, [\\(\\mu\^{ex}\\)]{.math .notranslate .nohighlight} is not, and as a result, the densities of the two are generally quite different. The first term [\\(\\mu\^{id}\\)]{.math .notranslate .nohighlight} is the ideal gas contribution to the chemical potential. [\\(\\mu\^{id}\\)]{.math .notranslate .nohighlight} can be related to the density or pressure of the fictitious gas reservoir by:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mu\^{id} = & k T \\ln{\\rho \\Lambda\^3} \\\\ = & k T \\ln{\\frac{\\phi P \\Lambda\^3}{k_B T}}\\end{split}\\\]
:::

where [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant, *T* is the user-specified temperature, [\\(\\rho\\)]{.math .notranslate .nohighlight} is the number density, *P* is the pressure, and [\\(\\phi\\)]{.math .notranslate .nohighlight} is the fugacity coefficient. The constant [\\(\\Lambda\\)]{.math .notranslate .nohighlight} is required for dimensional consistency. For all unit styles except *lj* it is defined as the thermal de Broglie wavelength

::: {.math .notranslate .nohighlight}
\\\[\\Lambda = \\sqrt{ \\frac{h\^2}{2 \\pi m k_B T}}\\\]
:::

where *h* is Planck's constant, and *m* is the mass of the exchanged atom or molecule. For unit style *lj*, [\\(\\Lambda\\)]{.math .notranslate .nohighlight} is simply set to unity. Note that prior to March 2017, [\\(\\Lambda\\)]{.math .notranslate .nohighlight} for unit style *lj* was calculated using the above formula with *h* set to the rather specific value of 0.18292026. Chemical potential under the old definition can be converted to an equivalent value under the new definition by subtracting [\\(3 k T \\ln(\\Lambda\_{old})\\)]{.math .notranslate .nohighlight}.

As an alternative to specifying mu directly, the ideal gas reservoir can be defined by its pressure *P* using the *pressure* keyword, in which case the user-specified chemical potential is ignored. The user may also specify the fugacity coefficient [\\(\\phi\\)]{.math .notranslate .nohighlight} using the *fugacity_coeff* keyword, which defaults to unity.

The *full_energy* option means that the fix calculates the total potential energy of the entire simulated system, instead of just the energy of the part that is changed. The total system energy before and after the proposed GCMC exchange or MC move is then used in the Metropolis criterion to determine whether or not to accept the proposed change. By default, this option is off, in which case only partial energies are computed to determine the energy difference due to the proposed change.

The *full_energy* option is needed for systems with complicated potential energy calculations, including the following:

- long-range electrostatics (kspace)

- many-body pair styles

- hybrid pair styles

- eam pair styles

- tail corrections

- need to include potential energy contributions from other fixes

In these cases, LAMMPS will automatically apply the *full_energy* keyword and issue a warning message.

When the *mol* keyword is used, the *full_energy* option also includes the intramolecular energy of inserted and deleted molecules, whereas this energy is not included when *full_energy* is not used. If this is not desired, the *intra_energy* keyword can be used to define an amount of energy that is subtracted from the final energy when a molecule is inserted, and subtracted from the initial energy when a molecule is deleted. For molecules that have a non-zero intramolecular energy, this will ensure roughly the same behavior whether or not the *full_energy* option is used.

Inserted atoms and molecules are assigned random velocities based on the specified temperature *T*. Because the relative velocity of all atoms in the molecule is zero, this may result in inserted molecules that are systematically too cold. In addition, the intramolecular potential energy of the inserted molecule may cause the kinetic energy of the molecule to quickly increase or decrease after insertion. The *tfac_insert* keyword allows the user to counteract these effects by changing the temperature used to assign velocities to inserted atoms and molecules by a constant factor. For a particular application, some experimentation may be required to find a value of *tfac_insert* that results in inserted molecules that equilibrate quickly to the correct temperature.

Some fixes have an associated potential energy. Examples of such fixes include: [[efield]{.doc}]fix_efield.md){.reference .internal}, [[gravity]{.doc}]fix_gravity.md){.reference .internal}, [[addforce]{.doc}]fix_addforce.md){.reference .internal}, [[langevin]{.doc}]fix_langevin.md){.reference .internal}, [[restrain]{.doc}]fix_restrain.md){.reference .internal}, [[temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal}, [[temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, and [[wall fixes]{.doc}]fix_wall.md){.reference .internal}. For that energy to be included in the total potential energy of the system (the quantity used when performing GCMC exchange and MC moves), you MUST enable the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for that fix. The doc pages for individual [[fix]{.doc}]fix.md){.reference .internal} commands specify if this should be done.

Use the *charge* option to insert atoms with a user-specified point charge. Note that doing so will cause the system to become non-neutral. LAMMPS issues a warning when using long-range electrostatics (kspace) with non-neutral systems. See the [[compute group/group]{.doc}]compute_group_group.md){.reference .internal} documentation for more details about simulating non-neutral systems with kspace on.

Use of this fix typically will cause the number of atoms to fluctuate, therefore, you will want to use the [[compute_modify dynamic/dof]{.doc}]compute_modify.md){.reference .internal} command to ensure that the current number of atoms is used as a normalizing factor each time temperature is computed. A simple example of this is:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute_modify thermo_temp dynamic/dof yes
:::
::::

A more complicated example is listed earlier on this page in the context of NVT dynamics.

::: {.admonition .note}
Note

If the density of the cell is initially very small or zero, and increases to a much larger density after a period of equilibration, then certain quantities that are only calculated once at the start (kspace parameters) may no longer be accurate. The solution is to start a new simulation after the equilibrium density has been reached.
:::

With some pair_styles, such as [[Buckingham]{.doc}]pair_buck.md){.reference .internal}, [[Born-Mayer-Huggins]{.doc}]pair_born.md){.reference .internal} and [[ReaxFF]{.doc}]pair_reaxff.md){.reference .internal}, two atoms placed close to each other may have an arbitrary large, negative potential energy due to the functional form of the potential. While these unphysical configurations are inaccessible to typical dynamical trajectories, they can be generated by Monte Carlo moves. The *overlap_cutoff* keyword suppresses these moves by effectively assigning an infinite positive energy to all new configurations that place any pair of atoms closer than the specified overlap cutoff distance.

The *max* and *min* keywords allow for the restriction of the number of atoms in the fix group (and region in case the *region* keyword is used). They automatically reject all insertion or deletion moves that would take the system beyond the set boundaries. Should the system already be beyond the boundary, only moves that bring the system closer to the bounds may be accepted.

The *group* keyword adds all inserted atoms to the [[group]{.doc}]group.md){.reference .internal} of the group-ID value. The *grouptype* keyword adds all inserted atoms of the specified type to the [[group]{.doc}]group.md){.reference .internal} of the group-ID value.
::::::::::::::

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the state of the fix to [[binary restart files]{.doc}]restart.md){.reference .internal}. This includes information about the random number generator seed, the next timestep for MC exchanges, the number of MC step attempts and successes etc. This ensures that the sequence of Monte Carlo moves generated after reading from a restart file are exactly the same as those that are generated in the original run. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

::: {.admonition .note}
Note

For this to work correctly, the timestep must **not** be changed after reading the restart with [[reset_timestep]{.doc}]reset_timestep.md){.reference .internal}. The fix will try to detect it and stop with an error.
:::

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix computes a global vector of length 8, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The vector values are the following global cumulative quantities:

> ::: {}
> 1.  translation attempts
>
> 2.  translation successes
>
> 3.  insertion attempts
>
> 4.  insertion successes
>
> 5.  deletion attempts
>
> 6.  deletion successes
>
> 7.  rotation attempts
>
> 8.  rotation successes
> :::

The vector values calculated by this fix are "intensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

This fix style requires an [[atom style]{.doc}]atom_style.md){.reference .internal} with per atom type masses.

Do not set "neigh_modify once yes" or else this fix will never be called. Reneighboring is **required**.

This fix style is only usable for 3D simulations.

This fix can be run in parallel, but aspects of the GCMC part will not scale well in parallel. Currently, molecule translations and rotations are not supported with more than one MPI process. It is still possible to do parallel molecule exchange without translation and rotation moves by setting MC moves to zero and/or by using the *mcmoves* keyword with *Pmoltrans* = *Pmolrotate* = 0 .

When using *fix gcmc* in combination with [[fix shake]{.doc}]fix_shake.md){.reference .internal} or [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}, only GCMC exchange moves are supported, so the argument *M* must be zero.

When using *fix gcmc* in combination with [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}, deletion of the last remaining molecule is not allowed for technical reasons, and so the molecule count will never drop below 1, regardless of the specified chemical potential.

Note that very lengthy simulations involving insertions/deletions of billions of gas molecules may run out of atom or molecule IDs and trigger an error, so it is better to run multiple shorter-duration simulations. The [[reset_atoms]{.doc}]reset_atoms.md){.reference .internal} command can be used to "compress" the atom and molecule IDs between runs. Likewise, very large molecules have not been tested and may turn out to be problematic.

Use of multiple *fix gcmc* commands in the same input script can be problematic if using a template molecule. The issue is that the user-referenced template molecule in the second *fix gcmc* command may no longer exist since it might have been deleted by the first *fix gcmc* command. An existing template molecule will need to be referenced by the user for each subsequent *fix gcmc* command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix atom/swap]{.doc}]fix_atom_swap.md){.reference .internal}, [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[neighbor]{.doc}]neighbor.md){.reference .internal}, [[fix deposit]{.doc}]fix_deposit.md){.reference .internal}, [[fix evaporate]{.doc}]fix_evaporate.md){.reference .internal}, [[delete_atoms]{.doc}]delete_atoms.md){.reference .internal}
:::

::: {#defaults .section}
## Defaults[](#defaults "Link to this heading"){.headerlink}

The option defaults are mol = no, maxangle = 10, overlap_cutoff = 0.0, fugacity_coeff = 1.0, intra_energy = 0.0, tfac_insert = 1.0. (Patomtrans, Pmoltrans, Pmolrotate) = (1, 0, 0) for mol = no and (0, 1, 1) for mol = yes. full_energy = no, except for the situations where full_energy is required, as listed above.

------------------------------------------------------------------------

**(Frenkel)** Frenkel and Smit, Understanding Molecular Simulation, Academic Press, London, 2002.
:::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-gjf-command .section}
[]{#index-0}

# fix gjf command[](#fix-gjf-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID gjf Tstart Tstop damp seed keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- gjf = style name of this fix command

- Tstart,Tstop = desired temperature at start/end of run (temperature units)

- Tstart can be a variable (see below)

- damp = damping parameter (time units)

- seed = random number seed to use for white noise (positive integer)

- zero or more keyword/value pairs may be appended

- keyword = *vel* or *method*

  ``` literal-block
  vel value = vfull or vhalf
    vfull = use on-site velocity
    vhalf = use half-step velocity
  method value = 1-8
    1-8 = choose one of the many GJ formulations
    7   = requires input of additional scalar between 0 and 1
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 3 boundary gjf 10.0 10.0 1.0 699483
    fix 1 all gjf 10.0 100.0 100.0 48279 vel vfull method 4
    fix 2 all gjf 10.0 10.0 1.0 26488 method 7 0.95
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 12Jun2025.]{.versionmodified .added}
:::

Apply a Langevin thermostat as described in [[(Gronbech-Jensen-2020)]{.std .std-ref}](#gronbech-jensen-2020){.reference .internal} to a group of atoms which models an interaction with a background implicit solvent. As described in the papers cited below, the GJ methods provide exact diffusion, drift, and Boltzmann sampling for linear systems for any time step within the stability limit. The purpose of this set of methods is therefore to significantly improve statistical accuracy at longer time steps compared to other thermostats.

The current implementation provides the user with the option to output the velocity in one of two forms: *vfull* or *vhalf*. The option *vhalf* outputs the 2GJ half-step velocity given in [[Gronbech Jensen/Gronbech-Jensen]{.std .std-ref}](#gronbech-jensen-2019){.reference .internal}; for linear systems, this velocity is shown to not have any statistical errors for any stable time step. The option *vfull* outputs the on-site velocity given in [[Gronbech-Jensen/Farago]{.std .std-ref}](#gronbech-jensen-farago){.reference .internal}; this velocity is shown to be systematically lower than the target temperature by a small amount, which grows quadratically with the timestep. An overview of statistically correct Boltzmann and Maxwell-Boltzmann sampling of true on-site and true half-step velocities is given in [[Gronbech-Jensen-2020]{.std .std-ref}](#gronbech-jensen-2020){.reference .internal}.

This fix allows the use of several GJ methods as listed in [[Gronbech-Jensen-2020]{.std .std-ref}](#gronbech-jensen-2020){.reference .internal}. The GJ-VII method is described in [[Finkelstein]{.std .std-ref}](#finkelstein){.reference .internal} and GJ-VIII is described in [[Gronbech-Jensen-2024]{.std .std-ref}](#gronbech-jensen-2024){.reference .internal}. The implementation follows the splitting form provided in Eqs. (24) and (25) in [[Gronbech-Jensen-2024]{.std .std-ref}](#gronbech-jensen-2024){.reference .internal}, including the application of Gaussian noise values, per the description in [[Gronbech-Jensen-2023]{.std .std-ref}](#gronbech-jensen-2023){.reference .internal}.

::: {.admonition .note}
Note

Unlike the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} command which performs force modifications only, this fix performs thermostatting and time integration. Thus you no longer need a separate time integration fix, like [[fix nve]{.doc}]fix_nve.md){.reference .internal}.
:::

See the [[Howto thermostat]{.doc}]Howto_thermostat.md){.reference .internal} page for a discussion of different ways to compute temperature and perform thermostatting.

The desired temperature at each timestep is a ramped value during the run from *Tstart* to *Tstop*.

*Tstart* can be specified as an equal-style or atom-style [[variable]{.doc}]variable.md){.reference .internal}. In this case, the *Tstop* setting is ignored. If the value is a variable, it should be specified as v_name, where name is the variable name. In this case, the variable will be evaluated each timestep, and its value used to determine the target temperature.

Equal-style variables can specify formulas with various mathematical functions, and include [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command keywords for the simulation box parameters and timestep and elapsed time. Thus it is easy to specify a time-dependent temperature.

Atom-style variables can specify the same formulas as equal-style variables but can also include per-atom values, such as atom coordinates. Thus it is easy to specify a spatially-dependent temperature with optional time-dependence as well.

Like other fixes that perform thermostatting, this fix can be used with [[compute commands]{.doc}]compute.md){.reference .internal} that remove a "bias" from the atom velocities. E.g. to apply the thermostat only to atoms within a spatial [[region]{.doc}]region.md){.reference .internal}, or to remove the center-of-mass velocity from a group of atoms, or to remove the x-component of velocity from the calculation.

This is not done by default, but only if the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command is used to assign a temperature compute to this fix that includes such a bias term. See the doc pages for individual [[compute temp commands]{.doc}]compute.md){.reference .internal} to determine which ones include a bias.

The *damp* parameter is specified in time units and determines how rapidly the temperature is relaxed. For example, a value of 100.0 means to relax the temperature in a timespan of (roughly) 100 time units ([\\(\\tau\\)]{.math .notranslate .nohighlight} or fs or ps - see the [[units]{.doc}]units.md){.reference .internal} command). The damp factor can be thought of as inversely related to the viscosity of the solvent. I.e. a small relaxation time implies a high-viscosity solvent and vice versa. See the discussion about [\\(\\gamma\\)]{.math .notranslate .nohighlight} and viscosity in the documentation for the [[fix viscous]{.doc}]fix_viscous.md){.reference .internal} command for more details.

The random \# *seed* must be a positive integer. A Marsaglia random number generator is used. Each processor uses the input seed to generate its own unique seed and its own stream of random numbers. Thus the dynamics of the system will not be identical on two runs on different numbers of processors.

------------------------------------------------------------------------

The keyword/value option pairs are used in the following ways.

The keyword *vel* determines which velocity is used to determine quantities of interest in the simulation.

The keyword *method* selects one of the eight GJ-methods implemented in LAMMPS.
:::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. Because the state of the random number generator is not saved in restart files, this means you cannot do "exact" restarts with this fix, where the simulation continues on the same as if no restart had taken place. However, in a statistical sense, a restarted simulation should produce the same behavior. Additionally, the GJ methods implement noise exclusively within each time step (unlike the BBK thermostat of the fix-langevin). The restart is done with either vfull or vhalf velocity output for as long as the choice of vfull/vhalf is the same for the simulation as it is in the restart file.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* option is supported by this fix. You can use it to assign a temperature [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its thermostatting procedure, as described above. For consistency, the group used by this fix and by the compute should be the same.

This fix can ramp its target temperature over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is not compatible with run_style respa. It is not compatible with accelerated packages such as KOKKOS.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, [[fix nvt]{.doc}]fix_nh.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are vel = vhalf, method = 1.

------------------------------------------------------------------------

**(Gronbech-Jensen-2020)** Gronbech-Jensen, Mol Phys 118, e1662506 (2020).

**(Gronbech Jensen/Gronbech-Jensen)** Gronbech Jensen and Gronbech-Jensen, Mol Phys, 117, 2511 (2019)

**(Gronbech-Jensen/Farago)** Gronbech-Jensen and Farago, Mol Phys, 111, 983 (2013).

**(Finkelstein)** Finkelstein, Cheng, Fiorin, Seibold, Gronbech-Jensen, J. Chem. Phys., 155, 18 (2021)

**(Gronbech-Jensen-2024)** Gronbech-Jensen, J. Stat. Phys. 191, 137 (2024).

**(Gronbech-Jensen-2023)** Gronbech-Jensen, J. Stat. Phys. 190, 96 (2023).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

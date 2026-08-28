:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-temp-rescale-command .section}
[]{#index-1}[]{#index-0}

# fix temp/rescale command[](#fix-temp-rescale-command "Link to this heading"){.headerlink}

Accelerator Variants: *temp/rescale/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID temp/rescale N Tstart Tstop window fraction
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- temp/rescale = style name of this fix command

- N = perform rescaling every N steps

- Tstart,Tstop = desired temperature at start/end of run (temperature units)

  :::: {.highlight-none .notranslate}
  ::: highlight
      Tstart can be a variable (see below)
  :::
  ::::

- window = only rescale if temperature is outside this window (temperature units)

- fraction = rescale to target temperature by this fraction
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 3 flow temp/rescale 100 1.0 1.1 0.02 0.5
    fix 3 boundary temp/rescale 1 1.0 1.5 0.05 1.0
    fix 3 boundary temp/rescale 1 1.0 1.5 0.05 1.0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Reset the temperature of a group of atoms by explicitly rescaling their velocities.

The rescaling is applied to only the translational degrees of freedom for the particles, which is an important consideration if finite-size particles which have rotational degrees of freedom are being thermostatted with this fix. The translational degrees of freedom can also have a bias velocity removed from them before thermostatting takes place; see the description below.

Rescaling is performed every N timesteps. The target temperature is a ramped value between the *Tstart* and *Tstop* temperatures at the beginning and end of the run.

::: {.admonition .note}
Note

This thermostat will generate an error if the current temperature is zero at the end of a timestep it is invoked on. It cannot rescale a zero temperature.
:::

*Tstart* can be specified as an equal-style [[variable]{.doc}]variable.md){.reference .internal}. In this case, the *Tstop* setting is ignored. If the value is a variable, it should be specified as v_name, where name is the variable name. In this case, the variable will be evaluated each timestep, and its value used to determine the target temperature.

Equal-style variables can specify formulas with various mathematical functions, and include [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command keywords for the simulation box parameters and timestep and elapsed time. Thus it is easy to specify a time-dependent temperature.

Rescaling is only performed if the difference between the current and desired temperatures is greater than the *window* value. The amount of rescaling that is applied is a *fraction* (from 0.0 to 1.0) of the difference between the actual and desired temperature. E.g. if *fraction* = 1.0, the temperature is reset to exactly the desired value.

::: {.admonition .note}
Note

Unlike the [[fix nvt]{.doc}]fix_nh.md){.reference .internal} command which performs Nose/Hoover thermostatting AND time integration, this fix does NOT perform time integration. It only modifies velocities to effect thermostatting. Thus you must use a separate time integration fix, like [[fix nve]{.doc}]fix_nve.md){.reference .internal} to actually update the positions of atoms using the modified velocities. Likewise, this fix should not normally be used on atoms that also have their temperature controlled by another fix - e.g. by [[fix nvt]{.doc}]fix_nh.md){.reference .internal} or [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} commands.
:::

See the [[Howto thermostat]{.doc}]Howto_thermostat.md){.reference .internal} page for a discussion of different ways to compute temperature and perform thermostatting.

This fix computes a temperature each timestep. To do this, the fix creates its own compute of style "temp", as if one of this command had been issued:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute fix-ID_temp group-ID temp
:::
::::

See the [[compute temp]{.doc}]compute_temp.md){.reference .internal} for details. Note that the ID of the new compute is the fix-ID + underscore + "temp", and the group for the new compute is the same as the fix group.

Note that this is NOT the compute used by thermodynamic output (see the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command) with ID = *thermo_temp*. This means you can change the attributes of this fix's temperature (e.g. its degrees-of-freedom) via the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command or print this temperature during thermodynamic output via the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command using the appropriate compute-ID. It also means that changing attributes of *thermo_temp* will have no effect on this fix.

Like other fixes that perform thermostatting, this fix can be used with [[compute commands]{.doc}]compute.md){.reference .internal} that remove a "bias" from the atom velocities. E.g. to apply the thermostat only to atoms within a spatial [[region]{.doc}]region.md){.reference .internal}, or to remove the center-of-mass velocity from a group of atoms, or to remove the x-component of velocity from the calculation.

This is not done by default, but only if the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command is used to assign a temperature compute to this fix that includes such a bias term. See the doc pages for individual [[compute temp commands]{.doc}]compute.md){.reference .internal} to determine which ones include a bias. In this case, the thermostat works in the following manner: bias is removed from each atom, thermostatting is performed on the remaining thermal degrees of freedom, and the bias is added back in.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the cumulative global energy change to [[binary restart files]{.doc}]restart.md){.reference .internal}. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the fix continues in an uninterrupted fashion.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* option is supported by this fix. You can use it to assign a temperature [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its thermostatting procedure, as described above. For consistency, the group used by this fix and by the compute should be the same.

The cumulative energy change in the system imposed by this fix is included in the [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} keywords *ecouple* and *econserve*. See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} doc page for details.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the same cumulative energy change due to this fix described in the previous paragraph. The scalar value calculated by this fix is "extensive".

This fix can ramp its target temperature over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix_modify]{.doc}]fix_modify.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#fix-modify-command .section}
[]{#index-0}

# fix_modify command[](#fix-modify-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix_modify fix-ID keyword value ...
:::
::::

- fix-ID = ID of the fix to modify

- one or more keyword/value pairs may be appended

- keyword = *bodyforces* or *dynamic/dof* or *energy* or *pad* or *press* or *respa* or *temp* or *virial* or *kick*

  ``` literal-block
  bodyforces value = early or late
    early/late = compute rigid-body forces/torques early or late in the timestep
  dynamic/dof value = yes or no
    yes/no = do or do not re-compute the number of degrees of freedom (DOF) contributing to the temperature
  energy value = yes or no
  pad    arg = Nchar = # of characters to convert timestep to
  press value = compute ID that calculates a pressure
  respa value = 1 to max respa level or 0 (for outermost level)
  temp value = compute ID that calculates a temperature
  virial value = yes or no
  vizsteps value = number of MD steps that generated graphics objects should remain visible for fixes that support it
  kick value = yes or no
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix_modify 3 temp myTemp press myPress
    fix_modify 1 energy yes
    fix_modify tether respa 2
    fix_modify myrxns vizsteps 100
:::
::::
:::::

:::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Modify one or more parameters of a previously defined fix. Only specific fix styles support specific parameters. See the doc pages for individual fix commands for info on which ones support which fix_modify parameters.

The *temp* keyword is used to determine how a fix computes temperature. The specified compute ID must have been previously defined by the user via the [[compute]{.doc}]compute.md){.reference .internal} command and it must be a style of compute that calculates a temperature. All fixes that compute temperatures define their own compute by default, as described in their documentation. Thus this option allows the user to override the default method for computing T.

The *press* keyword is used to determine how a fix computes pressure. The specified compute ID must have been previously defined by the user via the [[compute]{.doc}]compute.md){.reference .internal} command and it must be a style of compute that calculates a pressure. All fixes that compute pressures define their own compute by default, as described in their documentation. Thus this option allows the user to override the default method for computing P.

The *energy* keyword can be used with fixes that support it, which is explained at the bottom of their doc page. *Energy yes* will add a contribution to the potential energy of the system. More specifically, the fix's global or per-atom energy is included in the calculation performed by the [[compute pe]{.doc}]compute_pe.md){.reference .internal} or [[compute pe/atom]{.doc}]compute_pe_atom.md){.reference .internal} commands. The former is what is used the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command for output of any quantity that includes the global potential energy of the system. Note that the [[compute pe]{.doc}]compute_pe.md){.reference .internal} and [[compute pe/atom]{.doc}]compute_pe_atom.md){.reference .internal} commands also have an option to include or exclude the contribution from fixes. For fixes that tally a global energy, it can also be printed with thermodynamic output by using the keyword f_ID in the thermo_style custom command, where ID is the fix-ID of the appropriate fix.

::: {.admonition .note}
Note

If you are performing an [[energy minimization]{.doc}]minimize.md){.reference .internal} with one of these fixes and want the energy and forces it produces to be part of the optimization criteria, you must specify the *energy yes* setting.
:::

::: {.admonition .note}
Note

For most fixes that support the *energy* keyword, the default setting is *no*. For a few it is *yes*, when a user would expect that to be the case. The page of each fix gives the default.
:::

The *virial* keyword can be used with fixes that support it, which is explained at the bottom of their doc page. *Virial yes* will add a contribution to the virial of the system. More specifically, the fix's global or per-atom virial is included in the calculation performed by the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} or [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} commands. The former is what is used the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command for output of any quantity that includes the global pressure of the system. Note that the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} and [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} commands also have an option to include or exclude the contribution from fixes.

::: {.admonition .note}
Note

If you are performing an [[energy minimization]{.doc}]minimize.md){.reference .internal} with [[box relaxation]{.doc}]fix_box_relax.md){.reference .internal} and one of these fixes and want the virial contribution of the fix to be part of the optimization criteria, you must specify the *virial yes* setting.
:::

::: {.admonition .note}
Note

For most fixes that support the *virial* keyword, the default setting is *no*. For a few it is *yes*, when a user would expect that to be the case. The page of each fix gives the default.
:::

For fixes that set or modify forces, it may be possible to select at which [[r-RESPA]{.doc}]run_style.md){.reference .internal} level the fix operates via the *respa* keyword. The RESPA level at which the fix is active can be selected. This is a number ranging from 1 to the number of levels. If the RESPA level is larger than the current maximum, the outermost level will be used, which is also the default setting. This default can be restored using a value of *0* for the RESPA level. The affected fix has to be enabled to support this feature; if not, *fix_modify* will report an error. Active fixes with a custom RESPA level setting are reported with their specified level at the beginning of a r-RESPA run.

The *dynamic/dof* keyword determines whether the number of atoms N in the fix group and their associated degrees of freedom are re-computed each time a temperature is computed. Only fix styles that calculate their own internal temperature use this option. Currently this is only the [[fix rigid/nvt/small]{.doc}]fix_rigid.md){.reference .internal} and [[fix rigid/npt/small]{.doc}]fix_rigid.md){.reference .internal} commands for the purpose of thermostatting rigid body translation and rotation. By default, N and their DOF are assumed to be constant. If you are adding atoms or molecules to the system (see the [[fix pour]{.doc}]fix_pour.md){.reference .internal}, [[fix deposit]{.doc}]fix_deposit.md){.reference .internal}, and [[fix gcmc]{.doc}]fix_gcmc.md){.reference .internal} commands) or expect atoms or molecules to be lost (e.g. due to exiting the simulation box or via [[fix evaporate]{.doc}]fix_evaporate.md){.reference .internal}), then this option should be used to ensure the temperature is correctly normalized.

::: {.admonition .note}
Note

Other thermostatting fixes, such as [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, do not use the *dynamic/dof* keyword because they use a temperature compute to calculate temperature. See the [[compute_modify dynamic/dof]{.doc}]compute_modify.md){.reference .internal} command for a similar way to ensure correct temperature normalization for those thermostats.
:::

The *bodyforces* keyword determines whether the forces and torques acting on rigid bodies are computed *early* at the post-force stage of each timestep (right after per-atom forces have been computed and communicated among processors), or *late* at the final-integrate stage of each timestep (after any other fixes have finished their post-force tasks). Only the rigid-body integration fixes use this option, which includes [[fix rigid]{.doc}]fix_rigid.md){.reference .internal} and [[fix rigid/small]{.doc}]fix_rigid.md){.reference .internal}, and their variants.

The default is *late*. If there are other fixes that add forces to individual atoms, then the rigid-body constraints will include these forces when time-integrating the rigid bodies. If *early* is specified, then new fixes can be written that use or modify the per-body force and torque, before time-integration of the rigid bodies occurs. Note however this has the side effect, that fixes such as [[fix addforce]{.doc}]fix_addforce.md){.reference .internal}, [[fix setforce]{.doc}]fix_setforce.md){.reference .internal}, [[fix spring]{.doc}]fix_spring.md){.reference .internal}, which add forces to individual atoms will have no effect on the motion of the rigid bodies if they are specified in the input script after the fix rigid command. LAMMPS will give a warning if that is the case.

::: versionadded
[Added in version 2Apr2025.]{.versionmodified .added}
:::

The *pad* keyword only applies when a fix produces a file and the output filename is specified with a wildcard "\*" character which becomes the timestep. If *pad* is 0, which is the default, the timestep is converted into a string of unpadded length (e.g., 100 or 12000 or 2000000). When *pad* is specified with *Nchar* [\\(\>\\)]{.math .notranslate .nohighlight} 0, the string is padded with leading zeroes so they are all the same length = *Nchar*. For example, pad 7 would yield 0000100, 0012000, 2000000. This can be useful so that post-processing programs can easily read the files in ascending timestep order. Please see the documentation of the individual fix styles if this keyword is supported.

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

The *vizsteps* keyword only applies when a fix produces event based graphics objects, e.g. atoms that were involved in a reaction or a Monte Carlo swap, move, or insert. It determines for how many time steps the graphics objects will remain visible in the corresponding [[dump image output]{.doc}]dump_image.md){.reference .internal}.

The *kick* keyword can only be used with [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal} and [[fix nvt/sllod/eff]{.doc}]fix_nvt_sllod_eff.md){.reference .internal}. If *kick* is *yes* and velocity is stored in the laboratory frame, the velocity profile consistent with [[fix deform]{.doc}]fix_deform.md){.reference .internal} will be superimposed at the start of the next run. If velocity is stored in the peculiar frame, the *kick* flag is ignored.
::::::::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix]{.doc}]fix.md){.reference .internal}, [[compute temp]{.doc}]compute_temp.md){.reference .internal}, [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}, [[thermo_style]{.doc}]thermo_style.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are temp = ID defined by fix, press = ID defined by fix, energy = no, virial = different for each fix style, respa = 0, bodyforce = late.
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-addtorque-atom-command .section}
[]{#index-0}

# fix addtorque/atom command[](#fix-addtorque-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID addtorque/atom tx ty tz keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- addtorque/atom = style name of this fix command

- tx,ty,tz = torque component values (torque units) .. parsed-literal:

  :::: {.highlight-none .notranslate}
  ::: highlight
      any of tx,ty,tz can be a variable (see below)
  :::
  ::::

- zero or more keyword/value pairs may be appended to args

- keyword = *every* or *region*

  ``` literal-block
  every value = Nevery
    Nevery = add torque every this many time steps
  region value = region-ID
    region-ID = ID of region atoms must be in to have added torque
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix kick flow addtorque/atom 1.0 0.0 0.0
    fix kick flow addtorque/atom 1.0 0.0 v_oscillate
    fix ff boundary addtorque/atom 0.0 0.0 v_push
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 10Dec2025.]{.versionmodified .added}
:::

This fix is intended to add a peratom torque of each individual finite-sized atom in the group to the specified values. Unlike [[fix addtorque/group]{.doc}]fix_addtorque_group.md){.reference .internal}, it does not apply a collective torque to a set of point particles.

Add [\\((t_x,t_y,t_z)\\)]{.math .notranslate .nohighlight} to the corresponding component of the torque for each atom in the group. Any of the three quantities defining the torque components, namely [\\(t_x\\)]{.math .notranslate .nohighlight}, [\\(t_y\\)]{.math .notranslate .nohighlight}, and [\\(t_z\\)]{.math .notranslate .nohighlight}, can be specified as an equal-style or atom-style [[variable]{.doc}]variable.md){.reference .internal}. If the value is a variable, it should be specified as v_name, where name is the variable name. In this case, the variable will be evaluated each time step, and its value(s) will be used to determine the torque component(s).

Equal-style variables can specify formulas with various mathematical functions and include [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command keywords for the simulation box parameters, time step, and elapsed time. Thus, it is easy to specify a time-dependent torque field.

Atom-style variables can specify the same formulas as equal-style variables but can also include per-atom values, such as atom coordinates. Thus, it is easy to specify a spatially-dependent torque field with optional time-dependence as well.

If the *every* keyword is used, the *Nevery* setting determines how often the torques are applied. The default value is 1, for every time step.

If the *region* keyword is used, the atom must also be in the specified geometric [[region]{.doc}]region.md){.reference .internal} in order to have torque added to it.
::::

------------------------------------------------------------------------

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is adding its torques. Default is the outermost level.

This fix computes a global three-vector of torques which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The vector is the total torque on the group of atoms before the torques on individual atoms are changed by the fix. The vector values calculated by this fix are "extensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The torques due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command. You should not specify torque components with a variable that has time-dependence for use with a minimizer, since the minimizer increments the time step as the iteration count during the minimization.

::: {.admonition .note}
Note

This fix is not (currently) designed to be used with rigid fixes. While it will apply additional torques to all of the atoms in a rigid body as described above, there is not always an easy mapping between these peratom torques and the torque experienced by the body.
:::
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Fix *addtorque/atom* is part of the GRANULAR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix settorque/atom]{.doc}]fix_settorque_atom.md){.reference .internal}, [[fix addforce]{.doc}]fix_addforce.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option default for the every keyword is every = 1.
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

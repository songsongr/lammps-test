:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-add-heat-command .section}
[]{#index-0}

# fix add/heat command[](#fix-add-heat-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID add/heat style args keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- add/heat = style name of this fix command

- style = *constant* or *linear* or *quartic*

  ``` literal-block
  constant args = rate
    rate = rate of heat flow (energy/time units)
  linear args = Ttarget k
    Ttarget = target temperature (temperature units)
    k = prefactor (energy/(time*temperature) units)
  quartic args = Ttarget k
    Ttarget = target temperature (temperature units)
    k = prefactor (energy/(time*temperature^4) units)
  ```

- zero or more keyword/value pairs may be appended to args

- keyword = *overwrite*

  ``` literal-block
  overwrite value = yes or no
    yes = sets current heat flow of particle
    no = adds to current heat flow of particle
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all add/heat constant v_heat
    fix 1 all add/heat linear 10.0 1.0 overwrite yes
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix adds heat to particles with the temperature attribute every timestep at a given rate. Note that this is an internal temperature of a particle intended for use with non-atomistic models like the discrete element method.

For the *constant* style, heat is added at the specified rate. For the *linear* style, heat is added at a rate of [\\(k (T\_{target} - T)\\)]{.math .notranslate .nohighlight} where [\\(k\\)]{.math .notranslate .nohighlight} is the specified prefactor, [\\(T\_{target}\\)]{.math .notranslate .nohighlight} is the specified target temperature, and [\\(T\\)]{.math .notranslate .nohighlight} is the temperature of the atom. This may be more representative of a conductive process. For the *quartic* style, heat is added at a rate of [\\(k (T\_{target}\^4 - T\^4)\\)]{.math .notranslate .nohighlight}, akin to radiative heat transfer.

The rate or temperature can be can be specified as an equal-style or atom-style [[variable]{.doc}]variable.md){.reference .internal}. If the value is a variable, it should be specified as v_name, where name is the variable name. In this case, the variable will be evaluated each time step, and its value will be used to determine the rate of heat added.

Equal-style variables can specify formulas with various mathematical functions and include [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command keywords for the simulation box parameters, time step, and elapsed time to specify time-dependent heating.

Atom-style variables can specify the same formulas as equal-style variables but can also include per-atom values, such as atom coordinates to specify spatially-dependent heating.

If the *overwrite* keyword is set to *yes*, this fix will set the total heat flow on a particle every timestep, overwriting contributions from pair styles or other fixes. If *overwrite* is *no*, this fix will add heat on top of other contributions.
:::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the GRANULAR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This fix requires that atoms store temperature and heat flow as defined by the [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal} command or included in certain atom styles, such as atom_style rheo/thermal.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix heat/flow]{.doc}]fix_heat_flow.md){.reference .internal}, [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal}, [[fix rheo/thermal]{.doc}]fix_rheo_thermal.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default for the *overwrite* keyword is *no*
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

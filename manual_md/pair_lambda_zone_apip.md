::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#pair-style-lambda-zone-apip-command .section}
[]{#index-0}

# pair_style lambda/zone/apip command[](#pair-style-lambda-zone-apip-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lambda/zone/apip cutoff
:::
::::

- lambda/zone/apip = style name of this pair style

- cutoff = global cutoff (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lambda/zone/apip 12.0
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This pair_style calculates [\\(\\lambda\_{\\text{min},i}\\)]{.math .notranslate .nohighlight}, which is required for [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}. The meaning of [\\(\\lambda\_{\\text{min},i}\\)]{.math .notranslate .nohighlight} is documented in [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, as this pair_style is for use with [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal} only.

This pair_style requires only the global cutoff as argument. The remaining quantities, that are required to calculate [\\(\\lambda\_{\\text{min},i}\\)]{.math .notranslate .nohighlight} are extracted from [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal} and, thus, do not need to be passed to this pair_style as arguments.

::: {.admonition .warning}
Warning

The cutoff given as argument to this pair style is only relevant for the neighbor list creation. The radii, which define [\\(r\_{\\lambda,\\text{hi}}\\)]{.math .notranslate .nohighlight} and [\\(r\_{\\lambda,\\text{lo}}\\)]{.math .notranslate .nohighlight} are defined by [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}.
:::

The computation of [\\(\\lambda\_{\\text{min},i}\\)]{.math .notranslate .nohighlight} is done by this pair_style instead of by [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, as this computation takes time and this pair_style can be included in the load-balancing via [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal}.

A code example for the calculation of the switching parameter for an adaptive-precision interatomic potential (APIP) is given in the following: The adaptive-precision potential is created by combining [[pair_style eam/fs/apip]{.doc}]pair_eam_apip.md){.reference .internal} and [[pair_style pace/precise/apip]{.doc}]pair_pace_apip.md){.reference .internal}. The input, from which the switching parameter is calculated, is provided by [[pair lambda/input/csp/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}. The switching parameter is calculated by [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, whereas the spatial transition zone of the switching parameter is calculated by this pair style.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay eam/fs/apip pace/precise/apip lambda/input/csp/apip fcc cutoff 5.0 lambda/zone/apip 12.0
    pair_coeff * * eam/fs/apip Cu.eam.fs Cu
    pair_coeff * * pace/precise/apip Cu_precise.yace Cu
    pair_coeff * * lambda/input/csp/apip
    pair_coeff * * lambda/zone/apip
    fix 2 all lambda/apip 3.0 3.5 time_averaged_zone 4.0 12.0 110 110 min_delta_lambda 0.01
:::
::::
::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

The cutoff distance for this pair style can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style writes no information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands need to be specified in an input script that reads a restart file.

This pair style does not support the use of the *inner*, *middle*, and *outer* keywords of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the APIP package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal} [[pair_style lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}, [[pair_style eam/apip]{.doc}]pair_eam_apip.md){.reference .internal}, [[pair_style pace/apip]{.doc}]pair_pace_apip.md){.reference .internal}, [[fix lambda_thermostat/apip]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal},
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

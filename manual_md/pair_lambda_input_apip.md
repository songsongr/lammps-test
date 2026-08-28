:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::: {#pair-style-lambda-input-apip-command .section}
[]{#index-1}[]{#index-0}

# pair_style lambda/input/apip command[](#pair-style-lambda-input-apip-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lambda/input/apip cutoff
:::
::::

- lambda/input/apip = style name of this pair style

- cutoff = global cutoff (distance units)
:::::
::::::

:::::::::::::::: {#pair-style-lambda-input-csp-apip-command .section}
# pair_style lambda/input/csp/apip command[](#pair-style-lambda-input-csp-apip-command "Link to this heading"){.headerlink}

::::: {#id1 .section}
## Syntax[](#id1 "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lambda/input/csp/apip lattice keyword args
:::
::::

- lambda/input/csp/apip = style name of this pair style

- lattice = *fcc* or *bcc* or integer

  ``` literal-block
  fcc = use 12 nearest neighbors to calculate the CSP like in a perfect fcc lattice
  bcc = use 8 nearest neighbors to calculate the CSP like in a perfect bcc lattice
  integer = use N nearest neighbors to calculate the CSP
  ```

- zero or more keyword/args pairs may be appended

- keyword = *cutoff* or *N_buffer*

  ``` literal-block
  cutoff args = cutoff
    cutoff = distance in which neighboring atoms are considered (> 0)
  N_buffer args = N_buffer
    N_buffer = number of additional neighbors, which are included in the j-j+N/2 calculation
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lambda/input/csp/apip fcc
    pair_style lambda/input/csp/apip fcc cutoff 5.0
    pair_style lambda/input/csp/apip bcc cutoff 5.0 N_buffer 2
    pair_style lambda/input/csp/apip 14
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This pair_styles calculates [\\(\\lambda_i\^\\text{input}(t)\\)]{.math .notranslate .nohighlight}, which is required for [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}.

The pair_style lambda_input sets [\\(\\lambda_i\^\\text{input}(t) = 0\\)]{.math .notranslate .nohighlight}.

The pair_style lambda_input/csp calculates [\\(\\lambda_i\^\\text{input}(t) = \\text{CSP}\_i(t)\\)]{.math .notranslate .nohighlight}. The centro-symmetry parameter (CSP) [[(Kelchner)]{.std .std-ref}](#kelchner-2){.reference .internal} is described in [[compute centro/atom]{.doc}]compute_centro_atom.md){.reference .internal}.

The lattice argument is described in [[compute centro/atom]{.doc}]compute_centro_atom.md){.reference .internal} and determines the number of neighboring atoms that are used to compute the CSP. The *N_buffer* argument allows to include more neighboring atoms in the calculation of the contributions from the pair j,j+N/2 to the CSP as discussed in [[(Immel)]{.std .std-ref}](#immel2025-6){.reference .internal}.

The computation of [\\(\\lambda_i\^\\text{input}(t)\\)]{.math .notranslate .nohighlight} is done by this pair_style instead of by [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, as this computation takes time and this pair_style can be included in the load-balancing via [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal}.

A code example for the calculation of the switching parameter for an adaptive- precision potential is given in the following: The adaptive-precision potential is created by combining [[pair_style eam/fs/apip]{.doc}]pair_eam_apip.md){.reference .internal} and [[pair_style pace/precise/apip]{.doc}]pair_pace_apip.md){.reference .internal}. The input, from which the switching parameter is calculated, is provided by this pair_style. The switching parameter is calculated by [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, whereas the spatial transition zone of the switching parameter is calculated by [[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal}.

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
:::::

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

[[compute centro/atom]{.doc}]compute_centro_atom.md){.reference .internal}, [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, [[fix lambda_thermostat/apip]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal}, [[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal}, [[pair_style eam/apip]{.doc}]pair_eam_apip.md){.reference .internal}, [[pair_style pace/apip]{.doc}]pair_pace_apip.md){.reference .internal}, [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

N_buffer=0, cutoff=5.0

------------------------------------------------------------------------

**(Kelchner)** Kelchner, Plimpton, Hamilton, Phys Rev B, 58, 11085 (1998).

**(Immel)** Immel, Drautz and Sutmann, J Chem Phys, 162, 114119 (2025)
:::
::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-pace-apip-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style pace/apip command[](#pair-style-pace-apip-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-pace-fast-apip-command .section}
# pair_style pace/fast/apip command[](#pair-style-pace-fast-apip-command "Link to this heading"){.headerlink}
:::

::::::::::::::: {#pair-style-pace-precise-apip-command .section}
# pair_style pace/precise/apip command[](#pair-style-pace-precise-apip-command "Link to this heading"){.headerlink}

Constant precision variant: *pace*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style pace/apip ... keyword values ...
    pair_style pace/fast/apip ... keyword values ...
    pair_style pace/precise/apip ... keyword values ...
:::
::::

- one or more keyword/value pairs may be appended

  ``` literal-block
  keyword = keywords of pair pace
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay pace/fast/apip pace/precise/apip lambda/input/csp/apip fcc cutoff 5.0 lambda/zone/apip 12.0
    pair_coeff * * pace/fast/apip Cu_fast.yace Cu
    pair_coeff * * pace/precise/apip Cu_precise.yace Cu
    pair_coeff * * lambda/input/csp/apip
    pair_coeff * * lambda/zone/apip

    pair_style hybrid/overlay eam/fs/apip pace/precise/apip lambda/input/csp/apip fcc cutoff 5.0 lambda/zone/apip 12.0
    pair_coeff * * eam/fs/apip Cu.eam.fs Cu
    pair_coeff * * pace/precise/apip Cu_precise.yace Cu
    pair_coeff * * lambda/input/csp/apip
    pair_coeff * * lambda/zone/apip
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Pair style [[pace]{.doc}]pair_pace.md){.reference .internal} computes interactions using the Atomic Cluster Expansion (ACE), which is a general expansion of the atomic energy in multi-body basis functions [[(Drautz19)]{.std .std-ref}](#drautz2019-2){.reference .internal}. The *pace* pair style provides an efficient implementation that is described in this paper [[(Lysogorskiy21)]{.std .std-ref}](#lysogorskiy20211-2){.reference .internal}.

The potential energy [\\(E_i\\)]{.math .notranslate .nohighlight} of an atom [\\(i\\)]{.math .notranslate .nohighlight} of an adaptive-precision interatomic potential (APIP) according to [[(Immel25)]{.std .std-ref}](#immel2025-7){.reference .internal} is given by

::: {.math .notranslate .nohighlight}
\\\[E_i\^\\text{APIP} = \\lambda_i E_i\^\\text{(fast)} + (1-\\lambda_i) E_i\^\\text{(precise)}\\,,\\\]
:::

whereas the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} is computed dynamically during a simulation by [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal} or set prior to a simulation via [[set]{.doc}]set.md){.reference .internal}.

The pair style *pace/precise/apip* computes the potential energy [\\((1-\\lambda_i) E_i\^\\text{(pace)}\\)]{.math .notranslate .nohighlight} and the corresponding force and should be combined with a fast potential that computes the potential energy [\\(\\lambda_i E_i\^\\text{(fast)}\\)]{.math .notranslate .nohighlight} and the corresponding force via [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}.

The pair style *pace/fast/apip* computes the potential energy [\\(\\lambda_i E_i\^\\text{(pace)}\\)]{.math .notranslate .nohighlight} and the corresponding force and should be combined with a precise potential that computes the potential energy [\\((1-\\lambda_i) E_i\^\\text{(precise)}\\)]{.math .notranslate .nohighlight} and the corresponding force via [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}.

The pair_styles *pace/fast/apip* and *pace/precise/apip* commands may be followed by the optional keywords of [[pair_style pace]{.doc}]pair_pace.md){.reference .internal}, which are described [[here]{.doc}]pair_pace.md){.reference .internal}.
::::

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, where types I and J correspond to two different element types, mixing is performed by LAMMPS with user-specifiable parameters as described above. You never need to specify a pair_coeff command with I != J arguments for this style.

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

These pair styles do not write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the APIP package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style pace]{.doc}]pair_pace.md){.reference .internal}, [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, [[fix lambda_thermostat/apip]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal}, [[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal}, [[pair_style lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}, [[pair_style eam/apip]{.doc}]pair_eam_apip.md){.reference .internal}, [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

See [[pair_style pace]{.doc}]pair_pace.md){.reference .internal}.

------------------------------------------------------------------------

**(Drautz19)** Drautz, Phys Rev B, 99, 014104 (2019).

**(Lysogorskiy21)** Lysogorskiy, van der Oord, Bochkarev, Menon, Rinaldi, Hammerschmidt, Mrovec, Thompson, Csanyi, Ortner, Drautz, npj Comp Mat, 7, 97 (2021).

**(Immel25)** Immel, Drautz and Sutmann, J Chem Phys, 162, 114119 (2025)
:::
:::::::::::::::
::::::::::::::::::
:::::::::::::::::::

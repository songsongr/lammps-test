::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-eam-apip-command .section}
[]{#index-1}[]{#index-0}

# pair_style eam/apip command[](#pair-style-eam-apip-command "Link to this heading"){.headerlink}

Constant precision variant: *eam*
:::

:::::::::::::::: {#pair-style-eam-fs-apip-command .section}
# pair_style eam/fs/apip command[](#pair-style-eam-fs-apip-command "Link to this heading"){.headerlink}

Constant precision variant: *eam/fs*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style eam/apip
    pair_style eam/fs/apip
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay eam/fs/apip pace/precise/apip lambda/input/csp/apip fcc cutoff 5.0 lambda/zone/apip 12.0
    pair_coeff * * eam/fs/apip Cu.eam.fs Cu
    pair_coeff * * pace/precise/apip Cu_precise.yace Cu
    pair_coeff * * lambda/input/csp/apip
    pair_coeff * * lambda/zone/apip
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *eam* computes pairwise interactions for metals and metal alloys using embedded-atom method (EAM) potentials [[(Daw)]{.std .std-ref}](#daw2){.reference .internal}. The total energy [\\(E_i\\)]{.math .notranslate .nohighlight} of an atom [\\(i\\)]{.math .notranslate .nohighlight} is given by

::: {.math .notranslate .nohighlight}
\\\[E_i\^\\text{EAM} = F\_\\alpha \\left(\\sum\_{j \\neq i}\\ \\rho\_\\beta (r\_{ij})\\right) + \\frac{1}{2} \\sum\_{j \\neq i} \\phi\_{\\alpha\\beta} (r\_{ij})\\\]
:::

where [\\(F\\)]{.math .notranslate .nohighlight} is the embedding energy which is a function of the atomic electron density [\\(\\rho\\)]{.math .notranslate .nohighlight}, [\\(\\phi\\)]{.math .notranslate .nohighlight} is a pair potential interaction, and [\\(\\alpha\\)]{.math .notranslate .nohighlight} and [\\(\\beta\\)]{.math .notranslate .nohighlight} are the element types of atoms [\\(i\\)]{.math .notranslate .nohighlight} and [\\(j\\)]{.math .notranslate .nohighlight}. The multi-body nature of the EAM potential is a result of the embedding energy term. Both summations in the formula are over all neighbors [\\(j\\)]{.math .notranslate .nohighlight} of atom [\\(i\\)]{.math .notranslate .nohighlight} within the cutoff distance. EAM is documented in detail in [[pair_style eam]{.doc}]pair_eam.md){.reference .internal}.

The potential energy [\\(E_i\\)]{.math .notranslate .nohighlight} of an atom [\\(i\\)]{.math .notranslate .nohighlight} of an adaptive-precision interatomic potential (APIP) according to [[(Immel)]{.std .std-ref}](#immel2025-5){.reference .internal} is given by

::: {.math .notranslate .nohighlight}
\\\[E_i\^\\text{APIP} = \\lambda_i E_i\^\\text{(fast)} + (1-\\lambda_i) E_i\^\\text{(precise)}\\,,\\\]
:::

whereas the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} is computed dynamically during a simulation by [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal} or set prior to a simulation via [[set]{.doc}]set.md){.reference .internal}.

The pair style *eam/fs/apip* computes the potential energy [\\(\\lambda_i E_i\^\\text{EAM}\\)]{.math .notranslate .nohighlight} and the corresponding force and should be combined with a precise potential like [[pair_style pace/precise/apip]{.doc}]pair_pace_apip.md){.reference .internal} that computes the potential energy [\\((1-\\lambda_i) E_i\^\\text{(precise)}\\)]{.math .notranslate .nohighlight} and the corresponding force via [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}.
:::::

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, where types I and J correspond to two different element types, mixing is performed by LAMMPS as described above with the individual styles. You never need to specify a pair_coeff command with I != J arguments for the eam/apip styles.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

The eam/apip pair styles do not write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in tabulated potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

The eam/apip pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the APIP package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style eam]{.doc}]pair_eam.md){.reference .internal}, [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, [[fix lambda_thermostat/apip]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal}, [[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal}, [[pair_style lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}, [[pair_style pace/apip]{.doc}]pair_pace_apip.md){.reference .internal}, [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Immel)** Immel, Drautz and Sutmann, J Chem Phys, 162, 114119 (2025)

**(Daw)** Daw, Baskes, Phys Rev Lett, 50, 1285 (1983). Daw, Baskes, Phys Rev B, 29, 6443 (1984).
:::
::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

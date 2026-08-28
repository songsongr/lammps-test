::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#pair-style-dispersion-d3-command .section}
[]{#index-0}

# pair_style dispersion/d3 command[](#pair-style-dispersion-d3-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dispersion/d3 damping functional cutoff cn_cutoff
:::
::::

- damping = damping function: *original*, *zerom*, *bj*, or *bjm*

- functional = XC functional form: *pbe*, *pbe0*, ... (see list below)

- cutoff = global cutoff (distance units)

- cn_cutoff = coordination number cutoff (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dispersion/d3 original pbe 30.0 20.0
    pair_coeff * * C
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4Feb2025.]{.versionmodified .added}
:::

Style *dispersion/d3* computes the dispersion energy-correction used in the DFT-D3 method of Grimme [[(Grimme1)]{.std .std-ref}](#grimme1){.reference .internal}. It would typically be used with a machine learning (ML) potential that was trained with results from plain DFT calculations without the dispersion correction through pair_style hybrid/overlay. ML potentials are often combined *a posteriori* with dispersion energy-correction schemes (see *e.g.* [[(Qamar)]{.std .std-ref}](#qamar){.reference .internal} and [[(Batatia)]{.std .std-ref}](#batatia){.reference .internal}).

The energy contribution [\\(E_i\\)]{.math .notranslate .nohighlight} for an atom [\\(i\\)]{.math .notranslate .nohighlight} is given by:

::: {.math .notranslate .nohighlight}
\\\[E_i = \\frac{1}{2} \\sum\_{j \\neq i} \\big( s_6 \\frac{C\_{6,ij}}{r\^6\_{ij}} f_6\^{damp}(r\_{ij}) + s_8 \\frac{C\_{8,ij}}{r\^8\_{ij}} f_8\^{damp}(r\_{ij}) \\big)\\\]
:::

where [\\(C_n\\)]{.math .notranslate .nohighlight} is the averaged, geometry-dependent nth-order dispersion coefficient for atom pair [\\(ij\\)]{.math .notranslate .nohighlight}, [\\(r\_{ij}\\)]{.math .notranslate .nohighlight} their inter-nuclear distance, [\\(s_n\\)]{.math .notranslate .nohighlight} are XC functional-dependent scaling factor, and [\\(f_n\^{damp}\\)]{.math .notranslate .nohighlight} are damping functions.

::: {.admonition .note}
Note

It is currently *not* possible to calculate three-body dispersion contributions, according to, for example, the Axilrod-Teller-Muto model.
:::

::: versionchanged
[Changed in version 2Apr2025: ]{.versionmodified .changed}renamed *zero* keyword to *original* to avoid conflicts with [[pair style zero]{.doc}]pair_zero.md){.reference .internal} when used as [[hybrid sub-style]{.doc}]pair_hybrid.md){.reference .internal}.
:::

Available damping functions are the original "zero-damping" (*original*) [[(Grimme1)]{.std .std-ref}](#grimme1){.reference .internal}, Becke-Johnson damping (*bj*) [[(Grimme2)]{.std .std-ref}](#grimme2){.reference .internal}, and their revised forms (*zerom* and *bjm*, respectively) [[(Sherrill)]{.std .std-ref}](#sherrill){.reference .internal}.

Available XC functional scaling factors are listed in the table below, and depend on the selected damping function.

+-----------------------------------+------------------------------------------------------------------------------+
| Damping function                  | XC functional                                                                |
+===================================+==============================================================================+
| ::: line                          | ::: line                                                                     |
| \                                 | slater-dirac-exchange, b-lyp, b-p, b97-d, revpbe, pbe, pbesol, rpw86-pbe,    |
| :::                               | :::                                                                          |
|                                   |                                                                              |
| ::: line                          | ::: line                                                                     |
| \                                 | rpbe, tpss, b3-lyp, pbe0, hse06, revpbe38, pw6b95, tpss0, b2-plyp, pwpb95,   |
| :::                               | :::                                                                          |
|                                   |                                                                              |
| ::: line                          | ::: line                                                                     |
| original                          | b2gp-plyp, ptpss, hf, mpwlyp, bpbe, bh-lyp, tpssh, pwb6k, b1b95, bop, o-lyp, |
| :::                               | :::                                                                          |
|                                   |                                                                              |
| ::: line                          | ::: line                                                                     |
| \                                 | o-pbe, ssb, revssb, otpss, b3pw91, revpbe0, pbe38, mpw1b95, mpwb1k, bmk,     |
| :::                               | :::                                                                          |
|                                   |                                                                              |
| ::: line                          | ::: line                                                                     |
| \                                 | cam-b3lyp, lc-wpbe, m05, m052x, m06l, m06, m062x, m06hf, hcth120             |
| :::                               | :::                                                                          |
+-----------------------------------+------------------------------------------------------------------------------+
| zerom                             | b2-plyp, b3-lyp, b97-d, b-lyp, b-p, pbe, pbe0, lc-wpbe                       |
+-----------------------------------+------------------------------------------------------------------------------+
| ::: line                          | ::: line                                                                     |
| \                                 | b-p, b-lyp, revpbe, rpbe, b97-d, pbe, rpw86-pbe, b3-lyp, tpss, hf, tpss0,    |
| :::                               | :::                                                                          |
|                                   |                                                                              |
| ::: line                          | ::: line                                                                     |
| \                                 | pbe0, hse06, revpbe38, pw6b95, b2-plyp, dsd-blyp, dsd-blyp-fc, bop, mpwlyp,  |
| :::                               | :::                                                                          |
|                                   |                                                                              |
| ::: line                          | ::: line                                                                     |
| bj                                | o-lyp, pbesol, bpbe, opbe, ssb, revssb, otpss, b3pw91, bh-lyp, revpbe0,      |
| :::                               | :::                                                                          |
|                                   |                                                                              |
| ::: line                          | ::: line                                                                     |
| \                                 | tpssh, mpw1b95, pwb6k, b1b95, bmk, cam-b3lyp, lc-wpbe, b2gp-plyp, ptpss,     |
| :::                               | :::                                                                          |
|                                   |                                                                              |
| ::: line                          | ::: line                                                                     |
| \                                 | pwpb95, hf/mixed, hf/sv, hf/minis, b3lyp/6-31gd, hcth120, pw1pw, pwgga,      |
| :::                               | :::                                                                          |
|                                   |                                                                              |
| ::: line                          | ::: line                                                                     |
| \                                 | hsesol, hf3c, hf3cv, pbeh3c, pbeh-3c, mn15                                   |
| :::                               | :::                                                                          |
+-----------------------------------+------------------------------------------------------------------------------+
| bjm                               | b2-plyp, b3-lyp, b97-d, b-lyp, b-p, pbe, pbe0, lc-wpbe                       |
+-----------------------------------+------------------------------------------------------------------------------+

This style is primarily supposed to be used combined with a machine-learned interatomic potential trained on a DFT dataset (the selected XC functional should be chosen accordingly) via the [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal} command.
:::::::

::: {#coefficients .section}
## Coefficients[](#coefficients "Link to this heading"){.headerlink}

All the required coefficients are already stored internally (in the [`src/EXTRA-PAIR/d3_parameters.h`{.docutils .literal .notranslate}]{.pre} file). The only information to provide are the chemical symbols of the atoms. The number of chemical symbols given must be equal to the number of atom types used and must match their ordering as atom types.
:::

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support mixing since all parameters are explicit for each pair of atom types.

This pair style does not support the [[pair_modify command]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Style *dispersion/d3* is part of the EXTRA-PAIR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The compiled in parameters require the use of [[metal units]{.doc}]units.md){.reference .internal}.

It is currently *not* possible to calculate three-body dispersion contributions according to, for example, the Axilrod-Teller-Muto model.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Grimme1)** S. Grimme, J. Antony, S. Ehrlich, and H. Krieg, J. Chem. Phys. 132, 154104 (2010).

**(Qamar)** M. Qamar, M. Mrovec, T. Lysogorskiy, A. Bochkarev, and R. Drautz, J. Chem. Theory Comput. 19, 5151 (2023).

**(Batatia)** I. Batatia, *et al.*, arXiv:2401.0096 (2023).

**(Grimme2)** S. Grimme, S. Ehrlich and L. Goerigk, J. Comput. Chem. 32, 1456 (2011).

**(Sherrill)** D. G. A. Smith, L. A. Burns, K. Patkowski, and C. D. Sherrill, J. Phys. Chem. Lett., 7, 2197, (2016).
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

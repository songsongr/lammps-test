:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-coul-shield-command .section}
[]{#index-0}

# pair_style coul/shield command[](#pair-style-coul-shield-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style coul/shield cutoff tap_flag
:::
::::

- cutoff = global cutoff (distance units)

- tap_flag = 0/1 to turn off/on the taper function
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style coul/shield 16.0 1
    pair_coeff 1 2 0.70
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *coul/shield* computes a Coulomb interaction for boron and nitrogen atoms located in different layers of hexagonal boron nitride. This potential is designed be used in combination with the pair style [[ilp/graphene/hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}

::: {.admonition .note}
Note

This potential is intended for electrostatic interactions between two different layers of hexagonal boron nitride. Therefore, to avoid interaction within the same layers, each layer should have a separate molecule id and is recommended to use the "full" atom style, so that charge and molecule ID information is included.
:::

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} V\_{ij} \\\\ V\_{ij} = & \\mathrm{Tap}(r\_{ij})\\frac{\\kappa q_i q_j}{\\sqrt\[3\]{r\_{ij}\^3+(1/\\lambda\_{ij})\^3}}\\\\ \\mathrm{Tap}(r\_{ij}) = & 20\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^7 - 70\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^6 + 84\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^5 - 35\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^4 + 1\\end{split}\\\]
:::

Where Tap([\\(r\_{ij}\\)]{.math .notranslate .nohighlight}) is the taper function which provides a continuous cutoff (up to third derivative) for inter-atomic separations larger than [\\(r_c\\)]{.math .notranslate .nohighlight} [[(Leven1)]{.std .std-ref}](#leven3){.reference .internal}, [[(Leven2)]{.std .std-ref}](#leven4){.reference .internal} and [[(Maaravi)]{.std .std-ref}](#maaravi1){.reference .internal}. Here [\\(\\lambda\\)]{.math .notranslate .nohighlight} is the shielding parameter that eliminates the short-range singularity of the classical mono-polar electrostatic interaction expression [[(Maaravi)]{.std .std-ref}](#maaravi1){.reference .internal}.

The shielding parameter [\\(\\lambda\\)]{.math .notranslate .nohighlight} (1/distance units) must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

The global cutoff ([\\(r_c\\)]{.math .notranslate .nohighlight}) specified in the pair_style command is used.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support parameter mixing. Coefficients must be given explicitly for each type of particle pairs.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} *table* option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} *tail* option for adding long-range tail corrections to energy and pressure.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the INTERLAYER package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} [[pair_style ilp/graphene/hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

tap_flag = 1

------------------------------------------------------------------------

**(Leven1)** I. Leven, I. Azuri, L. Kronik and O. Hod, J. Chem. Phys. 140, 104106 (2014).

**(Leven2)** I. Leven et al, J. Chem.Theory Comput. 12, 2896-905 (2016).

**(Maaravi)** T. Maaravi et al, J. Phys. Chem. C 121, 22826-22835 (2017).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-born-gauss-command .section}
[]{#index-0}

# pair_style born/gauss command[](#pair-style-born-gauss-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style born/gauss cutoff
:::
::::

- born/gauss = name of the pair style

- cutoff = global cutoff (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style born/gauss 10.0
    pair_coeff 1 1 8.2464e13 12.48 0.042644277 0.44 3.56
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 28Mar2023.]{.versionmodified .added}
:::

Pair style *born/gauss* computes pairwise interactions from a combination of a Born-Mayer repulsive term and a Gaussian attractive term according to [[(Bomont)]{.std .std-ref}](#bomont){.reference .internal}:

::: {.math .notranslate .nohighlight}
\\\[E = A_0 \\exp \\left( -\\alpha r \\right) - A_1 \\exp\\left\[ -\\beta \\left(r - r_0 \\right)\^2 \\right\] \\qquad r \< r_c\\\]
:::

[\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(A_0\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (1/distance units)

- [\\(A_1\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\beta\\)]{.math .notranslate .nohighlight} (1/(distance units)\^2)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance units)

- cutoff (distance units)

The last coefficient is optional. If not specified, the global cutoff is used.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

This pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table options are not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is only enabled if LAMMPS was built with the EXTRA-PAIR package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style born]{.doc}]pair_born.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Bomont)** Bomont, Bretonnet, J. Chem. Phys. 124, 054504 (2006)
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

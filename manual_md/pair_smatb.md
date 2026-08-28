:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-smatb-command .section}
[]{#index-1}[]{#index-0}

# pair_style smatb command[](#pair-style-smatb-command "Link to this heading"){.headerlink}
:::

::::::::::::::::::: {#pair-style-smatb-single-command .section}
# pair_style smatb/single command[](#pair-style-smatb-single-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *smatb* or *smatb/single*

- args = none
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style smatb
    pair_coeff 1 1 2.88 10.35 4.178 0.210 1.818 4.07293506 4.9883063257983666

    pair_style smatb/single
    pair_coeff 1 1 2.88 10.35 4.178 0.210 1.818 4.07293506 4.9883063257983666
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

The *smatb* and *smatb/single* styles compute the Second Moment Approximation to the Tight Binding [[(Cyrot)]{.std .std-ref}](#cyrot){.reference .internal}, [[(Gupta)]{.std .std-ref}](#gupta){.reference .internal}, [[(Rosato)]{.std .std-ref}](#rosato){.reference .internal}, given by

::: {.math .notranslate .nohighlight}
\\\[E\_{i} = \\sum\_{j,R\_{ij}\\leq R\_{c}} \\alpha(R\_{ij}) - \\sqrt{\\sum\_{j,R\_{ij}\\leq R\_{c}}\\Xi\^2(R\_{ij})}\\\]
:::

[\\(R\_{ij}\\)]{.math .notranslate .nohighlight} is the distance between the atom [\\(i\\)]{.math .notranslate .nohighlight} and [\\(j\\)]{.math .notranslate .nohighlight}. And the two functions [\\(\\alpha\\left(r\\right)\\)]{.math .notranslate .nohighlight} and [\\(\\Xi\\left(r\\right)\\)]{.math .notranslate .nohighlight} are:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\alpha\\left(r\\right)=\\left\\lbrace\\begin{array}{ll} A e\^{-p \\left(\\frac{r}{R\_{0}}-1\\right)} & r \< R\_{sc}\\\\ a_3\\left(r-R\_{c}\\right)\^3+a_4\\left(r-R\_{c}\\right)\^4 +a_5\\left(r-R\_{c}\\right)\^5& R\_{sc} \< r \< R\_{c} \\end{array} \\right.\\end{split}\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\Xi\\left(r\\right)=\\left\\lbrace\\begin{array}{ll} \\xi e\^{-q \\left(\\frac{r}{R\_{0}}-1\\right)} & r \< R\_{sc}\\\\ x_3\\left(r-R\_{c}\\right)\^3+x_4\\left(r-R\_{c}\\right)\^4 +x_5\\left(r-R\_{c}\\right)\^5& R\_{sc} \< r \< R\_{c} \\end{array} \\right.\\end{split}\\\]
:::

The polynomial coefficients [\\(a_3\\)]{.math .notranslate .nohighlight}, [\\(a_4\\)]{.math .notranslate .nohighlight}, [\\(a_5\\)]{.math .notranslate .nohighlight}, [\\(x_3\\)]{.math .notranslate .nohighlight}, [\\(x_4\\)]{.math .notranslate .nohighlight}, [\\(x_5\\)]{.math .notranslate .nohighlight} are computed by LAMMPS: the two exponential terms and their first and second derivatives are smoothly reduced to zero, from the inner cutoff [\\(R\_{sc}\\)]{.math .notranslate .nohighlight} to the outer cutoff [\\(R\_{c}\\)]{.math .notranslate .nohighlight}.

The *smatb/single* style is an optimization when using only a single atom type.
:::::::

::: {#coefficients .section}
## Coefficients[](#coefficients "Link to this heading"){.headerlink}

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(R\_{0}\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(p\\)]{.math .notranslate .nohighlight} (dimensionless)

- [\\(q\\)]{.math .notranslate .nohighlight} (dimensionless)

- [\\(A\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\xi\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(R\_{cs}\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(R\_{c}\\)]{.math .notranslate .nohighlight} (distance units)

Note that: [\\(R\_{0}\\)]{.math .notranslate .nohighlight} is the nearest neighbor distance, usually coincides with the diameter of the atoms

See the [[run_style]{.doc}]run_style.md){.reference .internal} command for details.
:::

------------------------------------------------------------------------

::: {#mixing-info .section}
## Mixing info[](#mixing-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J the coefficients are not automatically mixed.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the SMTBQ package and are only enabled if LAMMPS is built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

These pair styles require the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

- [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Cyrot)** Cyrot-Lackmann and Ducastelle, Phys Rev. B, 4, 2406-2412 (1971).

**(Gupta)** Gupta ,Phys Rev. B, 23, 6265-6270 (1981).

**(Rosato)** Rosato and Guillope and Legrand, Philosophical Magazine A, 59.2, 321-336 (1989).
:::
:::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

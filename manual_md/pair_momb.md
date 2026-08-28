:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#pair-style-momb-command .section}
[]{#index-0}

# pair_style momb command[](#pair-style-momb-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style momb cutoff s6 d
:::
::::

- cutoff = global cutoff (distance units)

- s6 = global scaling factor of the exchange-correlation functional used (unitless)

- d = damping scaling factor of Grimme's method (unitless)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style momb 12.0 0.75 20.0
    pair_style hybrid/overlay eam/fs lj/charmm/coul/long 10.0 12.0 momb 12.0 0.75 20.0 morse 5.5

    pair_coeff 1 2 momb 0.0 1.0 1.0 10.2847 2.361
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *momb* computes pairwise van der Waals (vdW) and short-range interactions using the Morse potential and [[(Grimme)]{.std .std-ref}](#grimme){.reference .internal} method implemented in the Many-Body Metal-Organic (MOMB) force field described comprehensively in [[(Fichthorn)]{.std .std-ref}](#fichthorn){.reference .internal} and [[(Zhou)]{.std .std-ref}](#zhou5){.reference .internal}. Grimme's method is widely used to correct for dispersion in density functional theory calculations.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split} E & = D_0 \[\\exp\^{-2 \\alpha (r-r_0)} - 2\\exp\^{-\\alpha (r-r_0)}\] - s_6 \\frac{C_6}{r\^6} f\_{damp}(r,R_r) \\\\ f\_{damp}(r,R_r) & = \\frac{1}{1 + \\exp\^{-d(r/R_r - 1)}}\\end{split}\\\]
:::

For the *momb* pair style, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} as described below:

- [\\(D_0\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (1/distance units)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(C_6\\)]{.math .notranslate .nohighlight} (energy\*distance\^6 units)

- [\\(R_r\\)]{.math .notranslate .nohighlight} (distance units, typically sum of atomic vdW radii)
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This style is part of the EXTRA-PAIR package. It is only enabled if LAMMPS is built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page on for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style morse]{.doc}]pair_morse.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Grimme)** Grimme, J Comput Chem, 27(15), 1787-1799 (2006).

**(Fichthorn)** Fichthorn, Balankura, Qi, CrystEngComm, 18(29), 5410-5417 (2016).

**(Zhou)** Zhou, Saidi, Fichthorn, J Phys Chem C, 118(6), 3366-3374 (2014).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

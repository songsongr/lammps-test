:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#bond-style-mm3-command .section}
[]{#index-0}

# bond_style mm3 command[](#bond-style-mm3-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style mm3
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style mm3
    bond_coeff 1 100.0 107.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *mm3* bond style uses the potential that is anharmonic in the bond as defined in [[(Allinger)]{.std .std-ref}](#mm3-allinger1989){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[E = K (r - r_0)\^2 \\left\[ 1 - 2.55(r-r_0) + \\frac{7}{12} 2.55\^2(r-r_0)\^2 \\right\]\\\]
:::

where [\\(r_0\\)]{.math .notranslate .nohighlight} is the equilibrium value of the bond, and [\\(K\\)]{.math .notranslate .nohighlight} is a prefactor. The anharmonic prefactors have units [\\(\\AA\^{-n}\\)]{.math .notranslate .nohighlight}: [\\(-2.55 \\AA\^{-1}\\)]{.math .notranslate .nohighlight} and [\\(\\frac{7}{12} 2.55\^2 \\AA\^{-2}\\)]{.math .notranslate .nohighlight}. The code takes care of the necessary unit conversion for these factors internally. Note that the MM3 papers contain an error in Eq (1): [\\(\\frac{7}{12} 2.55\\)]{.math .notranslate .nohighlight} should be replaced with [\\(\\frac{7}{12} 2.55\^2\\)]{.math .notranslate .nohighlight}

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the YAFF package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Allinger)** Allinger, Yuh, Lii, JACS, 111(23), 8551-8566 (1989),
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

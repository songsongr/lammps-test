:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#bond-style-gaussian-command .section}
[]{#index-0}

# bond_style gaussian command[](#bond-style-gaussian-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style gaussian
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style gaussian
    bond_coeff 1 300.0 2 0.0128 0.375 3.37 0.0730 0.148 3.63
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *gaussian* bond style uses the potential:

::: {.math .notranslate .nohighlight}
\\\[E = -k_B T ln\\left(\\sum\_{i=1}\^{n} \\frac{A_i}{w_i \\sqrt{\\pi/2}} exp\\left( \\frac{-2(r-r\_{i})\^2}{w_i\^2}\\right)\\right)\\\]
:::

This analytical form is a suitable potential for obtaining mesoscale effective force fields which can reproduce target atomistic distributions [[(Milano)]{.std .std-ref}](#milano0){.reference .internal}

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(T\\)]{.math .notranslate .nohighlight} temperature at which the potential was derived

- [\\(n\\)]{.math .notranslate .nohighlight} (integer \>=1)

- [\\(A_1\\)]{.math .notranslate .nohighlight} (\> 0, distance)

- [\\(w_1\\)]{.math .notranslate .nohighlight} (\> 0, distance)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (\>= 0, distance)

- ...

- [\\(A_n\\)]{.math .notranslate .nohighlight} (\> 0, distance)

- [\\(w_n\\)]{.math .notranslate .nohighlight} (\> 0, distance)

- [\\(r_n\\)]{.math .notranslate .nohighlight} (\>= 0, distance)
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Milano)** G. Milano, S. Goudeau, F. Mueller-Plathe, J. Polym. Sci. B Polym. Phys. 43, 871 (2005).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

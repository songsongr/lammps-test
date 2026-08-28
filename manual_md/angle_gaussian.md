:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-gaussian-command .section}
[]{#index-0}

# angle_style gaussian command[](#angle-style-gaussian-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style gaussian
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style gaussian
    angle_coeff 1 300.0 2 0.0128 0.375 80.0 0.0730 0.148 123.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *gaussian* angle style uses the potential:

::: {.math .notranslate .nohighlight}
\\\[E = -k_B T ln\\left(\\sum\_{i=1}\^{n} \\frac{A_i}{w_i \\sqrt{\\pi/2}} exp\\left( \\frac{-2(\\theta-\\theta\_{i})\^2}{w_i\^2}\\right) \\right)\\\]
:::

This analytical form is a suitable potential for obtaining mesoscale effective force fields which can reproduce target atomistic distributions [[(Milano)]{.std .std-ref}](#milano1){.reference .internal}.

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(T\\)]{.math .notranslate .nohighlight} temperature at which the potential was derived

- [\\(n\\)]{.math .notranslate .nohighlight} (integer \>=1)

- [\\(A_1\\)]{.math .notranslate .nohighlight} (\> 0, radians)

- [\\(w_1\\)]{.math .notranslate .nohighlight} (\> 0, radians)

- [\\(\\theta_1\\)]{.math .notranslate .nohighlight} (degrees)

- ...

- [\\(A_n\\)]{.math .notranslate .nohighlight} (\> 0, radians)

- [\\(w_n\\)]{.math .notranslate .nohighlight} (\> 0, radians)

- [\\(\\theta_n\\)]{.math .notranslate .nohighlight} (degrees)
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This angle style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}
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

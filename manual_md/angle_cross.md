:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-cross-command .section}
[]{#index-0}

# angle_style cross command[](#angle-style-cross-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cross
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cross
    angle_coeff 1 200.0 100.0 100.0 1.25 1.25 107.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *cross* angle style uses a potential that couples the bond stretches of a bend with the angle stretch of that bend:

::: {.math .notranslate .nohighlight}
\\\[E = K\_{SS} \\left(r\_{12}-r\_{12,0}\\right)\\left(r\_{32}-r\_{32,0}\\right) + K\_{BS0}\\left(r\_{12}-r\_{12,0}\\right)\\left(\\theta-\\theta_0\\right) + K\_{BS1}\\left(r\_{32}-r\_{32,0}\\right)\\left(\\theta-\\theta_0\\right)\\\]
:::

where [\\(r\_{12,0}\\)]{.math .notranslate .nohighlight} is the rest value of the bond length between atom 1 and 2, [\\(r\_{32,0}\\)]{.math .notranslate .nohighlight} is the rest value of the bond length between atom 3 and 2, and [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is the rest value of the angle. [\\(K\_{SS}\\)]{.math .notranslate .nohighlight} is the force constant of the bond stretch-bond stretch term and [\\(K\_{BS0}\\)]{.math .notranslate .nohighlight} and [\\(K\_{BS1}\\)]{.math .notranslate .nohighlight} are the force constants of the bond stretch-angle stretch terms.

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\_{SS}\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(K\_{BS0}\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(K\_{BS1}\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(r\_{12,0}\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r\_{32,0}\\)]{.math .notranslate .nohighlight} (distance)

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

[\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence the [\\(K\_{BS0}\\)]{.math .notranslate .nohighlight} and [\\(K\_{BS1}\\)]{.math .notranslate .nohighlight} are effectively energy/distance per radian.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This angle style can only be used if LAMMPS was built with the YAFF package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

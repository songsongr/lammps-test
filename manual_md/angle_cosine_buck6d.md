:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-cosine-buck6d-command .section}
[]{#index-0}

# angle_style cosine/buck6d command[](#angle-style-cosine-buck6d-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cosine/buck6d
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cosine/buck6d
    angle_coeff 1  cosine/buck6d  1.978350  4  180.000000
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *cosine/buck6d* angle style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = K \\left\[ 1 + \\cos(n\\theta - \\theta_0)\\right\]\\\]
:::

where [\\(K\\)]{.math .notranslate .nohighlight} is the energy constant, [\\(n\\)]{.math .notranslate .nohighlight} is the periodic multiplicity and [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is the equilibrium angle.

The coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands in the following order:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(n\\)]{.math .notranslate .nohighlight}

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

[\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally.

Additional to the cosine term the *cosine/buck6d* angle style computes the short range (vdW) interaction belonging to the [[pair_style buck6d]{.doc}]pair_buck6d_coul_gauss.md){.reference .internal} between the end atoms of the angle. For this reason this angle style only works in combination with the [[pair_style buck6d]{.doc}]pair_buck6d_coul_gauss.md){.reference .internal} styles and needs the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} 1-3 interactions to be weighted 0.0 to prevent double counting.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

*cosine/buck6d* can only be used in combination with the [[pair_style buck6d]{.doc}]pair_buck6d_coul_gauss.md){.reference .internal} style and with a [[special_bonds]{.doc}]special_bonds.md){.reference .internal} 0.0 weighting of 1-3 interactions.

This angle style can only be used if LAMMPS was built with the MOFFF package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
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

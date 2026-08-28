:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-mm3-command .section}
[]{#index-0}

# angle_style mm3 command[](#angle-style-mm3-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style mm3
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style mm3
    angle_coeff 1 100.0 107.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *mm3* angle style uses the potential that is anharmonic in the angle as defined in [[(Allinger)]{.std .std-ref}]bond_mm3.md#mm3-allinger1989){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[E = K (\\theta - \\theta_0)\^2 \\left\[ 1 - 0.014(\\theta - \\theta_0) + 5.6(10)\^{-5} (\\theta - \\theta_0)\^2 - 7.0(10)\^{-7} (\\theta - \\theta_0)\^3 + 9(10)\^{-10} (\\theta - \\theta_0)\^4 \\right\]\\\]
:::

where [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is the equilibrium value of the angle, and [\\(K\\)]{.math .notranslate .nohighlight} is a prefactor. The anharmonic prefactors have units [\\(\\deg\^{-n}\\)]{.math .notranslate .nohighlight}, for example [\\(-0.014 \\deg\^{-1}\\)]{.math .notranslate .nohighlight}, [\\(5.6 \\cdot 10\^{-5} \\deg\^{-2}\\)]{.math .notranslate .nohighlight}, ...

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

[\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence [\\(K\\)]{.math .notranslate .nohighlight} is effectively energy per radian\^2.
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

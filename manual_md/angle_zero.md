::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#angle-style-zero-command .section}
[]{#index-0}

# angle_style zero command[](#angle-style-zero-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style zero keyword
:::
::::

- zero or more keywords may be appended

- keyword = *nocoeff*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style zero
    angle_style zero nocoeff
    angle_coeff *
    angle_coeff * 120.0
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Using an angle style of zero means angle forces and energies are not computed, but the geometry of angle triplets is still accessible to other commands.

As an example, the [[compute angle/local]{.doc}]compute_angle_local.md){.reference .internal} command can be used to compute the theta values for the list of triplets of angle atoms listed in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command. If no angle style is defined, this command cannot be used.

The optional *nocoeff* flag allows to read data files with AngleCoeff section for any angle style. Similarly, any [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} commands will only be checked for the angle type number and the rest ignored.

Note that the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command must be used for all angle types. If specified, there can be only one value, which is going to be used to assign an equilibrium angle, e.g. for use with [[fix shake]{.doc}]fix_shake.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_style none]{.doc}]angle_none.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

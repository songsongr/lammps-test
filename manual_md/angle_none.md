::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#angle-style-none-command .section}
[]{#index-0}

# angle_style none command[](#angle-style-none-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style none
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style none
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Using an angle style of none means angle forces and energies are not computed, even if triplets of angle atoms were listed in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command.

See the [[angle_style zero]{.doc}]angle_zero.md){.reference .internal} command for a way to calculate angle statistics, but compute no angle interactions.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_style zero]{.doc}]angle_zero.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#dielectric-command .section}
[]{#index-0}

# dielectric command[](#dielectric-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dielectric value
:::
::::

- value = dielectric constant
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dielectric 2.0
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set the dielectric constant for Coulombic interactions (pairwise and long-range) to this value. The constant is unitless, since it is used to reduce the strength of the interactions. The value is used in the denominator of the formulas for Coulombic interactions (e.g., a value of 4.0 reduces the Coulombic interactions to 25% of their default strength). See the [[pair_style]{.doc}]pair_style.md){.reference .internal} command for more details.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style]{.doc}]pair_style.md){.reference .internal}
:::

::::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dielectric 1.0
:::
::::
:::::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

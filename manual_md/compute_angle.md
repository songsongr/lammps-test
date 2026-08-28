:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-angle-command .section}
[]{#index-0}

# compute angle command[](#compute-angle-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID angle
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- angle = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all angle
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that extracts the angle energy calculated by each of the angle sub-styles used in the [[angle_style hybrid]{.doc}]angle_hybrid.md){.reference .internal} command. These values are made accessible for output or further processing by other commands. The group specified for this command is ignored.

This compute is useful when using [[angle_style hybrid]{.doc}]angle_hybrid.md){.reference .internal} if you want to know the portion of the total energy contributed by one or more of the hybrid sub-styles.
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector of length *N*, where *N* is the number of sub_styles defined by the [[angle_style hybrid]{.doc}]angle_style.md){.reference .internal} command, which can be accessed by indices 1 through *N*. These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The vector values are "extensive" and will be in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute pe]{.doc}]compute_pe.md){.reference .internal}, [[compute pair]{.doc}]compute_pair.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

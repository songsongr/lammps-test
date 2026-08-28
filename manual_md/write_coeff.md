::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#write-coeff-command .section}
[]{#index-0}

# write_coeff command[](#write-coeff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    write_coeff file
:::
::::

- file = name of data file to write out
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    write_coeff polymer.coeff
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Write a text format file with the currently defined force field coefficients in a way, that it can be read by LAMMPS with the [[include]{.doc}]include.md){.reference .internal} command. In combination with the nocoeff option of [[write_data]{.doc}]write_data.md){.reference .internal} this can be used to move the Coeffs sections from a data file into a separate file.

::: {.admonition .note}
Note

The write_coeff command is not yet fully implemented as some pair styles do not output their coefficient information. This means you will need to add/copy this information manually.
:::
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[read_data]{.doc}]read_data.md){.reference .internal}, [[write_restart]{.doc}]write_restart.md){.reference .internal}, [[write_data]{.doc}]write_data.md){.reference .internal}
:::
:::::::::::::
::::::::::::::
:::::::::::::::

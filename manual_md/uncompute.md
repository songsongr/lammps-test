::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#uncompute-command .section}
[]{#index-0}

# uncompute command[](#uncompute-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    uncompute compute-ID
:::
::::

- compute-ID = ID of a previously defined compute
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    uncompute 2
    uncompute lower-boundary
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Delete a compute that was previously defined with a [[compute]{.doc}]compute.md){.reference .internal} command. This also wipes out any additional changes made to the compute via the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute]{.doc}]compute.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

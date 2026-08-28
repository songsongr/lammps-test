::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#unfix-command .section}
[]{#index-0}

# unfix command[](#unfix-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    unfix fix-ID
:::
::::

- fix-ID = ID of a previously defined fix
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    unfix 2
    unfix lower-boundary
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Delete a fix that was previously defined with a [[fix]{.doc}]fix.md){.reference .internal} command. This also wipes out any additional changes made to the fix via the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix]{.doc}]fix.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

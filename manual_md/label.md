::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#label-command .section}
[]{#index-0}

# label command[](#label-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    label ID
:::
::::

- ID = string used as label name
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    label xyz
    label loop
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Label this line of the input script with the chosen ID. Unless a jump command was used previously, this does nothing. But if a [[jump]{.doc}]jump.md){.reference .internal} command was used with a label argument to begin invoking this script file, then all commands in the script prior to this line will be ignored. I.e. execution of the script will begin at this line. This is useful for looping over a section of the input script as discussed in the [[jump]{.doc}]jump.md){.reference .internal} command.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[jump]{.doc}]jump.md){.reference .internal}, [[next]{.doc}]next.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

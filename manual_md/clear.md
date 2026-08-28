::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#clear-command .section}
[]{#index-0}

# clear command[](#clear-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    clear
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # (commands for 1st simulation)
    clear
    # (commands for 2nd simulation)
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command deletes all atoms, restores all settings to their default values, and frees all memory allocated by LAMMPS. Once a clear command has been executed, it is almost as if LAMMPS is completely reset, with some exceptions noted below. The command thus allows to run multiple jobs sequentially from a single input script, often with a loop.

The following settings are not affected by a clear command:

> ::: {}
> - working directory ([[shell]{.doc}]shell.md){.reference .internal} command)
>
> - log file status ([[log]{.doc}]log.md){.reference .internal} command)
>
> - echo status ([[echo]{.doc}]echo.md){.reference .internal} command)
>
> - input script variables except for *atomfile* style variables ([[variable]{.doc}]variable.md){.reference .internal} command).
> :::
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[label]{.doc}]label.md){.reference .internal}, [[jump]{.doc}]jump.md){.reference .internal}, [[next]{.doc}]next.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

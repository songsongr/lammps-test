::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#thermo-command .section}
[]{#index-0}

# thermo command[](#thermo-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    thermo N
:::
::::

- N = output thermodynamics every N timesteps

- N can be a variable (see below)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    thermo 100
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Compute and print thermodynamic info (e.g. temperature, energy, pressure) on timesteps that are a multiple of N and at the beginning and end of a simulation. A value of 0 will only print thermodynamics at the beginning and end.

The content and format of what is printed is controlled by the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} and [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} commands.

Instead of a numeric value, N can be specified as an [[equal-style variable]{.doc}]variable.md){.reference .internal}, which should be specified as v_name, where name is the variable name. In this case, the variable is evaluated at the beginning of a run to determine the next timestep at which thermodynamic info will be written out. On that timestep, the variable will be evaluated again to determine the next timestep, etc. Thus the variable should return timestep values. See the stagger() and logfreq() and stride() math functions for [[equal-style variables]{.doc}]variable.md){.reference .internal}, as examples of useful functions to use in this context. Other similar math functions could easily be added as options for [[equal-style variables]{.doc}]variable.md){.reference .internal}.

For example, the following commands will output thermodynamic info at timesteps 0, 10, 20, 30, 100, 200, 300, 1000, 2000, *etc*:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable        s equal logfreq(10,3,10)
    thermo          v_s
:::
::::
:::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[thermo_style]{.doc}]thermo_style.md){.reference .internal}, [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal}
:::

::::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    thermo 0
:::
::::
:::::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

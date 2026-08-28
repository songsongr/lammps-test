::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#timestep-command .section}
[]{#index-0}

# timestep command[](#timestep-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    timestep dt
:::
::::

- dt = timestep size (time units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    timestep 2.0
    timestep 0.003
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set the timestep size for subsequent molecular dynamics simulations. See the [[units]{.doc}]units.md){.reference .internal} command for the time units associated with each choice of units that LAMMPS supports.

The default value for the timestep size also depends on the choice of units for the simulation; see the default values below.

When the [[run style]{.doc}]run_style.md){.reference .internal} is *respa*, dt is the timestep for the outer loop (largest) timestep.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix dt/reset]{.doc}]fix_dt_reset.md){.reference .internal}, [[run]{.doc}]run.md){.reference .internal}, [[run_style]{.doc}]run_style.md){.reference .internal} respa, [[units]{.doc}]units.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

  ------------------------------------------------------------- ------------------------------------------------ ------------------------------------------------------
  choice of [[units]{.doc}]units.md){.reference .internal}   time units                                       default timestep size
  lj                                                            [\\(\\tau\\)]{.math .notranslate .nohighlight}   0.005 [\\(\\tau\\)]{.math .notranslate .nohighlight}
  real                                                          fs                                               1.0 fs
  metal                                                         ps                                               0.001 ps
  si                                                            s                                                1.0e-8 s (10 ns)
  cgs                                                           s                                                1.0e-8 s (10 ns)
  electron                                                      fs                                               0.001 fs
  micro                                                         [\\(\\mu\\)]{.math .notranslate .nohighlight}s   2.0 [\\(\\mu\\)]{.math .notranslate .nohighlight}s
  nano                                                          ns                                               0.00045 ns
  ------------------------------------------------------------- ------------------------------------------------ ------------------------------------------------------
:::
:::::::::::::
::::::::::::::
:::::::::::::::

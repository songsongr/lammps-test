::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-lb-momentum-command .section}
[]{#index-0}

# fix lb/momentum command[](#fix-lb-momentum-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID lb/momentum nevery keyword values ...
:::
::::

- ID, group-ID are documented in the [[fix]{.doc}]fix.md){.reference .internal} command

- lb/momentum = style name of this fix command

- nevery = adjust the momentum every this many timesteps

- zero or more keyword/value pairs may be appended

- keyword = *linear*

  ``` literal-block
  linear values = xflag yflag zflag
    xflag,yflag,zflag = 0/1 to exclude/include each dimension.
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 sphere lb/momentum
    fix 1 all lb/momentum linear 1 1 0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix is based on the [[fix momentum]{.doc}]fix_momentum.md){.reference .internal} command, and was created to be used in place of that command, when a lattice-Boltzmann fluid is present.

Zero the total linear momentum of the system, including both the atoms specified by group-ID and the lattice-Boltzmann fluid every nevery timesteps. If there are no atoms specified by group-ID only the fluid momentum is affected. This is accomplished by adjusting the particle velocities and the fluid velocities at each lattice site.

::: {.admonition .note}
Note

This fix only considers the linear momentum of the system.
:::

By default, the subtraction is performed for each dimension. This can be changed by specifying the keyword *linear*, along with a set of three flags set to 0/1 in order to exclude/ include the corresponding dimension.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Can only be used if a lattice-Boltzmann fluid has been created via the [[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal} command, and must come after this command.

This fix is part of the LATBOLTZ package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix momentum]{.doc}]fix_momentum.md){.reference .internal}, [[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

Zeros the total system linear momentum in each dimension.
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

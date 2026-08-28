:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-lb-viscous-command .section}
[]{#index-0}

# fix lb/viscous command[](#fix-lb-viscous-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID lb/viscous
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- lb/viscous = style name of this fix command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 flow lb/viscous
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix is similar to the [[fix viscous]{.doc}]fix_viscous.md){.reference .internal} command, and is to be used in place of that command when a lattice-Boltzmann fluid is present using the [[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal}. This should be used in conjunction with one of the built-in LAMMPS integrators, such as [[fix NVE]{.doc}]fix_nve.md){.reference .internal} or [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}.

This fix adds a viscous force to each atom to cause it move with the same velocity as the fluid (an equal and opposite force is applied to the fluid via [[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal}). When [[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal} is called with the noise option, the atoms will also experience random forces which will thermalize them to the same temperature as the fluid. In this way, the combination of this fix with [[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal} and a LAMMPS integrator like [[fix NVE]{.doc}]fix_nve.md){.reference .internal} is analogous to [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} except here the fluid is explicit. The temperature of the particles can be monitored via the scalar output of [[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal}.

------------------------------------------------------------------------

For details of this fix, as well as descriptions and results of several test runs, see [[Denniston et al.]{.std .std-ref}](#fluid-denniston2){.reference .internal}. Please include a citation to this paper if this fix is used in work contributing to published research.
:::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

As described in the [[fix viscous]{.doc}]fix_viscous.md){.reference .internal} documentation:

"No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The forces due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command. This fix should only be used with damped dynamics minimizers that allow for non-conservative forces. See the [[min_style]{.doc}]min_style.md){.reference .internal} command for details."
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the LATBOLTZ package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Can only be used if a lattice-Boltzmann fluid has been created via the [[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal} command, and must come after this command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Denniston et al.)** Denniston, C., Afrasiabian, N., Cole-Andre, M.G., Mackay, F. E., Ollila, S.T.T., and Whitehead, T., LAMMPS lb/fluid fix version 2: Improved Hydrodynamic Forces Implemented into LAMMPS through a lattice-Boltzmann fluid, Computer Physics Communications 275 (2022) [108318](https://doi.org/10.1016/j.cpc.2022.108318){.reference .external} .
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

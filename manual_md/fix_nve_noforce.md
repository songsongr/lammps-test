:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-nve-noforce-command .section}
[]{#index-0}

# fix nve/noforce command[](#fix-nve-noforce-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nve
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nve/noforce = style name of this fix command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 3 wall nve/noforce
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform updates of position, but not velocity for atoms in the group each timestep. In other words, the force on the atoms is ignored and their velocity is not updated. The atom velocities are used to update their positions.

This can be useful for wall atoms, when you set their velocities, and want the wall to move (or stay stationary) in a prescribed fashion.

This can also be accomplished via the [[fix setforce]{.doc}]fix_setforce.md){.reference .internal} command, but with fix nve/noforce, the forces on the wall atoms are unchanged, and can thus be printed by the [[dump]{.doc}]dump.md){.reference .internal} command or queried with an equal-style [[variable]{.doc}]variable.md){.reference .internal} that uses the fcm() group function to compute the total force on the group of atoms.
:::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nve]{.doc}]fix_nve.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

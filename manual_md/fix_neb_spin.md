:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-neb-spin-command .section}
[]{#index-0}

# fix neb/spin command[](#fix-neb-spin-command "Link to this heading"){.headerlink}

::::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID neb/spin Kspring
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- neb/spin = style name of this fix command

:::: {.highlight-none .notranslate}
::: highlight
    Kspring = spring constant for parallel nudging force
    (force/distance units or force units, see parallel keyword)
:::
::::
:::::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 active neb/spin 1.0
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Add nudging forces to spins in the group for a multi-replica simulation run via the [[neb/spin]{.doc}]neb_spin.md){.reference .internal} command to perform a geodesic nudged elastic band (GNEB) calculation for finding the transition state. Hi-level explanations of GNEB are given with the [[neb/spin]{.doc}]neb_spin.md){.reference .internal} command and on the [[Howto replica]{.doc}]Howto_replica.md){.reference .internal} doc page. The fix neb/spin command must be used with the "neb/spin" command and defines how inter-replica nudging forces are computed. A GNEB calculation is divided in two stages. In the first stage n replicas are relaxed toward a MEP until convergence. In the second stage, the climbing image scheme is enabled, so that the replica having the highest energy relaxes toward the saddle point (i.e. the point of highest energy along the MEP), and a second relaxation is performed.

The nudging forces are calculated as explained in [[(Bessarab)]{.std .std-ref}](#bessarabb){.reference .internal}). See this reference for more explanation about their expression.
:::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The forces due to this fix are imposed during an energy minimization, as invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command via the [[neb/spin]{.doc}]neb_spin.md){.reference .internal} command.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command can only be used if LAMMPS was built with the SPIN package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[neb_spin]{.doc}]neb_spin.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Bessarab)** Bessarab, Uzdin, Jonsson, Comp Phys Comm, 196, 335-347 (2015).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

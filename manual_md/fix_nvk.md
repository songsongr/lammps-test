:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-nvk-command .section}
[]{#index-0}

# fix nvk command[](#fix-nvk-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nvk
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nvk = style name of this fix command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nvk
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform constant kinetic energy integration using the Gaussian thermostat to update position and velocity for atoms in the group each timestep. V is volume; K is kinetic energy. This creates a system trajectory consistent with the isokinetic ensemble.

The equations of motion used are those of Minary et al in [[(Minary)]{.std .std-ref}](#nvk-minary){.reference .internal}, a variant of those initially given by Zhang in [[(Zhang)]{.std .std-ref}](#nvk-zhang){.reference .internal}.

The kinetic energy will be held constant at its value given when fix nvk is initiated. If a different kinetic energy is desired, the [[velocity]{.doc}]velocity.md){.reference .internal} command should be used to change the kinetic energy prior to this fix.
:::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The Gaussian thermostat only works when it is applied to all atoms in the simulation box. Therefore, the group must be set to all.

This fix has not yet been implemented to work with the RESPA integrator.

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Minary)** Minary, Martyna, and Tuckerman, J Chem Phys, 18, 2510 (2003).

**(Zhang)** Zhang, J Chem Phys, 106, 6102 (1997).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

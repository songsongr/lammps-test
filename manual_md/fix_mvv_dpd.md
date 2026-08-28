:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#fix-mvv-dpd-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# fix mvv/dpd command[](#fix-mvv-dpd-command "Link to this heading"){.headerlink}
:::

::: {#fix-mvv-edpd-command .section}
# fix mvv/edpd command[](#fix-mvv-edpd-command "Link to this heading"){.headerlink}
:::

:::::::::::::::: {#fix-mvv-tdpd-command .section}
# fix mvv/tdpd command[](#fix-mvv-tdpd-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID mvv/dpd lambda

    fix ID group-ID mvv/edpd lambda

    fix ID group-ID mvv/tdpd lambda
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- mvv/dpd, mvv/edpd, mvv/tdpd = style name of this fix command

- lambda = (optional) relaxation parameter (unitless)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all mvv/dpd
    fix 1 all mvv/dpd 0.5
    fix 1 all mvv/edpd
    fix 1 all mvv/edpd 0.5
    fix 1 all mvv/tdpd
    fix 1 all mvv/tdpd 0.5
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform time integration using the modified velocity-Verlet (MVV) algorithm to update position and velocity (fix mvv/dpd), or position, velocity and temperature (fix mvv/edpd), or position, velocity and concentration (fix mvv/tdpd) for particles in the group each timestep.

The modified velocity-Verlet (MVV) algorithm aims to improve the stability of the time integrator by using an extrapolated version of the velocity for the force evaluation:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}v(t+\\frac{\\Delta t}{2}) = & v(t) + \\frac{\\Delta t}{2}\\cdot a(t) \\\\ r(t+\\Delta t) = & r(t) + \\Delta t\\cdot v(t+\\frac{\\Delta t}{2}) \\\\ a(t+\\Delta t) = & \\frac{1}{m}\\cdot F\\left\[ r(t+\\Delta t), v(t) +\\lambda \\cdot \\Delta t\\cdot a(t)\\right\] \\\\ v(t+\\Delta t) = & v(t+\\frac{\\Delta t}{2}) + \\frac{\\Delta t}{2}\\cdot a(t+\\Delta t)\\end{split}\\\]
:::

where the parameter [\\(\\lambda\\)]{.math .notranslate .nohighlight} depends on the specific choice of DPD parameters, and needs to be tuned on a case-by-case basis. Specification of a *lambda* value is optional. If specified, the setting must be from 0.0 to 1.0. If not specified, a default value of 0.5 is used, which effectively reproduces the standard velocity-Verlet (VV) scheme. For more details, see [[Groot]{.std .std-ref}](#groot2){.reference .internal}.

Fix *mvv/dpd* updates the position and velocity of each atom. It can be used with the [[pair_style mdpd]{.doc}]pair_mesodpd.md){.reference .internal} command or other pair styles such as [[pair dpd]{.doc}]pair_dpd.md){.reference .internal}.

Fix *mvv/edpd* updates the per-atom temperature, in addition to position and velocity, and must be used with the [[pair_style edpd]{.doc}]pair_mesodpd.md){.reference .internal} command.

Fix *mvv/tdpd* updates the per-atom chemical concentration, in addition to position and velocity, and must be used with the [[pair_style tdpd]{.doc}]pair_mesodpd.md){.reference .internal} command.
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

:::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These fixes are part of the DPD-MESO package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

::: versionchanged
[Changed in version 29Aug2024.]{.versionmodified .changed}
:::

This fix is incompatible with deformation controls that remap velocity, for instance the *remap v* option of [[fix deform]{.doc}]fix_deform.md){.reference .internal}.
::::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style mdpd]{.doc}]pair_mesodpd.md){.reference .internal}, [[pair_style edpd]{.doc}]pair_mesodpd.md){.reference .internal}, [[pair_style tdpd]{.doc}]pair_mesodpd.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default value for the optional *lambda* parameter is 0.5.

------------------------------------------------------------------------

**(Groot)** Groot and Warren, J Chem Phys, 107: 4423-4435 (1997). DOI: 10.1063/1.474784
:::
::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

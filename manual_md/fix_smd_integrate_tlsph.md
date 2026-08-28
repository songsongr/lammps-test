::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-smd-integrate-tlsph-command .section}
[]{#index-0}

# fix smd/integrate_tlsph command[](#fix-smd-integrate-tlsph-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID smd/integrate_tlsph keyword values
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- smd/integrate_tlsph = style name of this fix command

- zero or more keyword/value pairs may be appended

- keyword = *limit_velocity*

``` literal-block
limit_velocity value = max_vel
  max_vel = maximum allowed velocity
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all smd/integrate_tlsph
    fix 1 all smd/integrate_tlsph limit_velocity 1000
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The fix performs explicit time integration for particles which interact according with the Total-Lagrangian SPH pair style.

See [this PDF guide](PDF/MACHDYN_LAMMPS_userguide.pdf){.reference .external} to using Smooth Mach Dynamics in LAMMPS.

The *limit_velocity* keyword will control the velocity, scaling the norm of the velocity vector to max_vel in case it exceeds this velocity limit.
:::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

Currently, no part of MACHDYN supports restarting nor minimization. This fix has no outputs.
:::

:::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MACHDYN package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

::: versionchanged
[Changed in version 29Aug2024.]{.versionmodified .changed}
:::

This fix is incompatible with deformation controls that remap velocity, for instance the *remap v* option of [[fix deform]{.doc}]fix_deform.md){.reference .internal}.
::::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[smd/integrate_ulsph]{.doc}]fix_smd_integrate_ulsph.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

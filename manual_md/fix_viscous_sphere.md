::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-viscous-sphere-command .section}
[]{#index-0}

# fix viscous/sphere command[](#fix-viscous-sphere-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID viscous/sphere gamma keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- viscous/sphere = style name of this fix command

- gamma = damping coefficient (torque/angular velocity units)

- zero or more keyword/value pairs may be appended

  ``` literal-block
  keyword = scale
    scale values = type ratio or v_name
      type = atom type (1-N)
      ratio = factor to scale the damping coefficients by
      v_name = reference to atom style variable name
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 flow viscous/sphere 0.1
    fix 1 damp viscous/sphere 0.5 scale 3 2.5
    fix 1 damp viscous/sphere 0.5 scale v_radscale
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Add a viscous damping torque to finite-size spherical particles in the group that is proportional to the angular velocity of the atom. In granular simulations this can be useful for draining the rotational kinetic energy from the system in a controlled fashion. If used without additional thermostatting (to add kinetic energy to the system), it has the effect of slowly (or rapidly) freezing the system; hence it can also be used as a simple energy minimization technique.

The damping torque [\\(T_i\\)]{.math .notranslate .nohighlight} is given by [\\(T_i = - \\gamma \\omega_i\\)]{.math .notranslate .nohighlight}. The larger the coefficient, the faster the rotational kinetic energy is reduced.

If the optional keyword *scale* is used, [\\(\\gamma\\)]{.math .notranslate .nohighlight} can be scaled up or down by the specified factor for atoms. This factor can be set for different atom types and thus the *scale* keyword used multiple times followed by the atom type and the associated scale factor. Alternately the scaling factor can be computed for each atom (e.g. based on its radius) by using an [[atom-style variable]{.doc}]variable.md){.reference .internal}.

::: {.admonition .note}
Note

You should specify gamma in torque/angular velocity units. This is not the same as mass/time units, at least for some of the LAMMPS [[units]{.doc}]units.md){.reference .internal} options like "real" or "metal" that are not self-consistent.
:::

In the current implementation, rather than have the user specify a viscosity, [\\(\\gamma\\)]{.math .notranslate .nohighlight} is specified directly in torque/angular velocity units. If needed, [\\(\\gamma\\)]{.math .notranslate .nohighlight} can be adjusted for atoms of different sizes (i.e. [\\(\\sigma\\)]{.math .notranslate .nohighlight}) by using the *scale* keyword.
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is modifying torques. Default is the outermost level.

The torques due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command. This fix should only be used with damped dynamics minimizers that allow for non-conservative forces. See the [[min_style]{.doc}]min_style.md){.reference .internal} command for details.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This fix requires that atoms store torque and angular velocity (omega) and a radius as defined by the [[atom_style sphere]{.doc}]atom_style.md){.reference .internal} command.

All particles in the group must be finite-size spheres. They cannot be point particles.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix viscous]{.doc}]fix_viscous.md){.reference .internal}, [[fix damping/cundall]{.doc}]fix_damping_cundall.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

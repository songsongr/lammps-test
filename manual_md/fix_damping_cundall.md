::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#fix-damping-cundall-command .section}
[]{#index-0}

# fix damping/cundall command[](#fix-damping-cundall-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID damping/cundall gamma_l gamma_a keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- damping/cundall = style name of this fix command

- gamma_l = linear damping coefficient (dimensionless)

- gamma_a = angular damping coefficient (dimensionless)

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
    fix 1 all damping/cundall 0.8 0.8
    fix 1 all damping/cundall 0.8 0.5 scale 3 2.5
    fix a all damping/cundall 0.8 0.5 scale v_radscale
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Add damping force and torque to finite-size spherical particles in the group following the model of [[Cundall, 1987]{.std .std-ref}](#cundall1987){.reference .internal}, as implemented in other granular physics code (e.g., [[Yade-DEM]{.std .std-ref}](#yadedem){.reference .internal}, [[PFC]{.std .std-ref}](#pfc){.reference .internal}).

The damping is constructed to always have negative mechanical power with respect to the current velocity/angular velocity to ensure dissipation of kinetic energy. If used without additional thermostatting (to add kinetic energy to the system), it has the effect of slowly (or rapidly) freezing the system; hence it can also be used as a simple energy minimization technique.

The magnitude of the damping force/torque [\\(F_d\\)]{.math .notranslate .nohighlight}/[\\(T_d\\)]{.math .notranslate .nohighlight} is a fraction [\\(\\gamma \\in \[0;1\]\\)]{.math .notranslate .nohighlight} of the current force/torque [\\(F\\)]{.math .notranslate .nohighlight}/[\\(T\\)]{.math .notranslate .nohighlight} on the particle. Damping is applied component-by-component in each direction [\\(k\\in\\{x, y, z\\}\\)]{.math .notranslate .nohighlight}:

::: {.math .notranslate .nohighlight}
\\\[{F_d}\_k = - \\gamma_l \\, F_k \\, \\mathrm{sign}(F_k v_k)\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[{T_d}\_k = - \\gamma_a \\, T_k \\, \\mathrm{sign}(T_k \\omega_k)\\\]
:::

The larger the coefficients, the faster the kinetic energy is reduced.

If the optional keyword *scale* is used, [\\(\\gamma_l\\)]{.math .notranslate .nohighlight} and [\\(\\gamma_a\\)]{.math .notranslate .nohighlight} can be scaled up or down by the specified factor for atoms. This factor can be set for different atom types and thus the *scale* keyword used multiple times followed by the atom type and the associated scale factor. Alternately the scaling factor can be computed for each atom (e.g. based on its radius) by using an [[atom-style variable]{.doc}]variable.md){.reference .internal}.

::: {.admonition .note}
Note

The damping force/torque is computed based on the force/torque at the moment this fix is invoked. Any force/torque added after this fix, e.g., by [[fix addforce]{.doc}]fix_addforce.md){.reference .internal} or [[fix addtorque/group]{.doc}]fix_addtorque_group.md){.reference .internal} will not be damped. When performing simulations with gravity, invoking [[fix gravity]{.doc}]fix_gravity.md){.reference .internal} after this fix will maintain the specified gravitational acceleration.
:::

::: {.admonition .note}
Note

This scheme is dependent on the coordinates system and does not correspond to realistic physical processes. It is constructed for numerical convenience and efficacy.
:::

This non-viscous damping presents the following advantages:

1.  damping is independent of velocity, equally damping regions with distinct natural frequencies,

2.  damping affects acceleration and vanishes for steady uniform motion of the particles,

3.  damping parameter [\\(\\gamma\\)]{.math .notranslate .nohighlight} is dimensionless and does not require scaling.
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is modifying forces/torques. Default is the outermost level.

The forces/torques due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command. This fix should only be used with damped dynamics minimizers that allow for non-conservative forces. See the [[min_style]{.doc}]min_style.md){.reference .internal} command for details.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the GRANULAR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This fix requires that atoms store torque and a radius as defined by the [[atom_style sphere]{.doc}]atom_style.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix viscous]{.doc}]fix_viscous.md){.reference .internal}, [[fix viscous/sphere]{.doc}]fix_viscous_sphere.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::

::: {#references .section}
## References[](#references "Link to this heading"){.headerlink}

**(Cundall, 1987)** Cundall, P. A. Distinct Element Models of Rock and Soil Structure, in Analytical and Computational Methods in Engineering Rock Mechanics, Ch. 4, pp. 129-163. E. T. Brown, ed. London: Allen & Unwin., 1987.

**(PFC)** PFC Particle Flow Code 6.0 Documentation. Itasca Consulting Group.

**(Yade-DEM)** V. Smilauer et al. (2021), Yade Documentation 3rd ed. The Yade Project. DOI:10.5281/zenodo.5705394 (https://yade-dem.org/doc/)
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

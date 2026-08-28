:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-nve-sphere-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# fix nve/sphere command[](#fix-nve-sphere-command "Link to this heading"){.headerlink}

Accelerator Variants: *nve/sphere/omp*, *nve/sphere/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nve/sphere
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nve/sphere = style name of this fix command

- zero or more keyword/value pairs may be appended

- keyword = *update* or *disc*

  ``` literal-block
  update value = dipole or dipole/dlm
    dipole = update orientation of dipole moment during integration
    dipole/dlm = use DLM integrator to update dipole orientation
  disc value = none = treat particles as 2d discs, not spheres
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nve/sphere
    fix 1 all nve/sphere update dipole
    fix 1 all nve/sphere disc
    fix 1 all nve/sphere update dipole/dlm
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform constant NVE integration to update position, velocity, and angular velocity for finite-size spherical particles in the group each timestep. V is volume; E is energy. This creates a system trajectory consistent with the microcanonical ensemble.

This fix differs from the [[fix nve]{.doc}]fix_nve.md){.reference .internal} command, which assumes point particles and only updates their position and velocity.

If the *update* keyword is used with the *dipole* value, then the orientation of the dipole moment of each particle is also updated during the time integration. This option should be used for models where a dipole moment is assigned to finite-size particles, e.g. spheroids via use of the [[atom_style hybrid sphere dipole]{.doc}]atom_style.md){.reference .internal} command.

The default dipole orientation integrator can be changed to the Dullweber-Leimkuhler-McLachlan integration scheme [[(Dullweber)]{.std .std-ref}]fix_nh.md#nh-dullweber){.reference .internal} when using *update* with the value *dipole/dlm*. This integrator is symplectic and time-reversible, giving better energy conservation and allows slightly longer timesteps at only a small additional computational cost.

If the *disc* keyword is used, then each particle is treated as a 2d disc (circle) instead of as a sphere. This is only possible for 2d simulations, as defined by the [[dimension]{.doc}]dimension.md){.reference .internal} keyword. The only difference between discs and spheres in this context is their moment of inertia, as used in the time integration.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix requires that atoms store torque and angular velocity (omega) and a radius as defined by the [[atom_style sphere]{.doc}]atom_style.md){.reference .internal} command. If the *dipole* keyword is used, then they must also store a dipole moment as defined by the [[atom_style dipole]{.doc}]atom_style.md){.reference .internal} command.

All particles in the group must be finite-size spheres. They cannot be point particles.

Use of the *disc* keyword is only allowed for 2d simulations, as defined by the [[dimension]{.doc}]dimension.md){.reference .internal} keyword.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nve]{.doc}]fix_nve.md){.reference .internal}, [[fix nve/asphere]{.doc}]fix_nve_asphere.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Dullweber)** Dullweber, Leimkuhler and McLachlan, J Chem Phys, 107, 5840 (1997).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

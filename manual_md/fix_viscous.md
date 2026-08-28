::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-viscous-command .section}
[]{#index-1}[]{#index-0}

# fix viscous command[](#fix-viscous-command "Link to this heading"){.headerlink}

Accelerator Variants: *viscous/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID viscous gamma keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- viscous = style name of this fix command

- gamma = damping coefficient (force/velocity units)

- zero or more keyword/value pairs may be appended

  ``` literal-block
  keyword = scale
    scale values = type ratio
      type = atom type (1-N)
      ratio = factor to scale the damping coefficient by
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 flow viscous 0.1
    fix 1 damp viscous 0.5 scale 3 2.5
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Add a viscous damping force to atoms in the group that is proportional to the velocity of the atom. The added force can be thought of as a frictional interaction with implicit solvent, i.e. the no-slip Stokes drag on a spherical particle. In granular simulations this can be useful for draining the kinetic energy from the system in a controlled fashion. If used without additional thermostatting (to add kinetic energy to the system), it has the effect of slowly (or rapidly) freezing the system; hence it can also be used as a simple energy minimization technique.

The damping force [\\(F_i\\)]{.math .notranslate .nohighlight} is given by [\\(F_i = - \\gamma v_i\\)]{.math .notranslate .nohighlight}. The larger the coefficient, the faster the kinetic energy is reduced. If the optional keyword *scale* is used, [\\(\\gamma\\)]{.math .notranslate .nohighlight} can scaled up or down by the specified factor for atoms of that type. It can be used multiple times to adjust [\\(\\gamma\\)]{.math .notranslate .nohighlight} for several atom types.

::: {.admonition .note}
Note

You should specify gamma in force/velocity units. This is not the same as mass/time units, at least for some of the LAMMPS [[units]{.doc}]units.md){.reference .internal} options like "real" or "metal" that are not self-consistent.
:::

In a Brownian dynamics context, [\\(\\gamma = \\frac{k_B T}{D}\\)]{.math .notranslate .nohighlight}, where [\\(k_B =\\)]{.math .notranslate .nohighlight} Boltzmann's constant, [\\(T\\)]{.math .notranslate .nohighlight} = temperature, and *D* = particle diffusion coefficient. *D* can be written as [\\(\\frac{k_B T}{3 \\pi \\eta d}\\)]{.math .notranslate .nohighlight}, where [\\(\\eta =\\)]{.math .notranslate .nohighlight} dynamic viscosity of the frictional fluid and d = diameter of particle. This means [\\(\\gamma = 3 \\pi \\eta d\\)]{.math .notranslate .nohighlight}, and thus is proportional to the viscosity of the fluid and the particle diameter.

In the current implementation, rather than have the user specify a viscosity, [\\(\\gamma\\)]{.math .notranslate .nohighlight} is specified directly in force/velocity units. If needed, [\\(\\gamma\\)]{.math .notranslate .nohighlight} can be adjusted for atoms of different sizes (i.e. [\\(\\sigma\\)]{.math .notranslate .nohighlight}) by using the *scale* keyword.

Note that Brownian dynamics models also typically include a randomized force term to thermostat the system at a chosen temperature. The [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} command does this. It has the same viscous damping term as fix viscous and adds a random force to each atom. The random force term is proportional to the square root of the chosen thermostatting temperature. Thus if you use fix langevin with a target [\\(T = 0\\)]{.math .notranslate .nohighlight}, its random force term is zero, and you are essentially performing the same operation as fix viscous. Also note that the gamma of fix viscous is related to the damping parameter of [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, however the former is specified in units of force/velocity and the latter in units of time, so that it can more easily be used as a thermostat.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is modifying forces. Default is the outermost level.

The forces due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command. This fix should only be used with damped dynamics minimizers that allow for non-conservative forces. See the [[min_style]{.doc}]min_style.md){.reference .internal} command for details.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, [[fix viscous/sphere]{.doc}]fix_viscous_sphere.md){.reference .internal}, [[fix damping/cundall]{.doc}]fix_damping_cundall.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

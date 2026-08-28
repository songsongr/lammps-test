:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-lambda-thermostat-apip-command .section}
[]{#index-0}

# fix lambda_thermostat/apip command[](#fix-lambda-thermostat-apip-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID lambda_thermostat/apip keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- lambda_thermostat/apip = style name of this fix command

- zero or more keyword/value pairs may be appended

- keyword = *seed* or *store_atomic_forces* or *N_rescaling*

  ``` literal-block
  seed value = integer
    integer = integer that is used as seed for the random number generator (> 0)
  store_atomic_forces value = nevery
    nevery = provide per-atom output every this many steps
  N_rescaling value = groupsize
    groupsize = rescale this many neighboring atoms (> 1)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 2 all lambda_thermostat/apip
    fix 2 all lambda_thermostat/apip N_rescaling 100
    fix 2 all lambda_thermostat/apip seed 42
    fix 2 all lambda_thermostat/apip seed 42 store_atomic_forces 1000
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command applies the local thermostat described in [[(Immel)]{.std .std-ref}](#immel2025-4){.reference .internal} to conserve the energy when the switching parameters of an [[adaptive-precision interatomic potential]{.doc}]Howto_apip.md){.reference .internal} (APIP) are updated while the gradient of the switching parameter is neglected in the force calculation.

::: {.admonition .warning}
Warning

The temperature change caused by this fix is only the means to the end of conserving the energy. Thus, this fix is not a classical thermostat, that ensures a given temperature in the system. All available thermostats are listed [[here]{.doc}]Howto_thermostat.md){.reference .internal}.
:::

The potential energy [\\(E_i\\)]{.math .notranslate .nohighlight} of an atom [\\(i\\)]{.math .notranslate .nohighlight} is given by the formula from [[(Immel)]{.std .std-ref}](#immel2025-4){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[E_i = \\lambda_i E_i\^\\text{(fast)} + (1-\\lambda_i) E_i\^\\text{(precise)},\\\]
:::

whereas [\\(E_i\^\\text{(fast)}\\)]{.math .notranslate .nohighlight} is the potential energy of atom [\\(i\\)]{.math .notranslate .nohighlight} according to a fast interatomic potential like EAM, [\\(E_i\^\\text{(precise)}\\)]{.math .notranslate .nohighlight} is the potential energy according to a precise interatomic potential such as ACE and [\\(\\lambda_i\\in\[0,1\]\\)]{.math .notranslate .nohighlight} is the switching parameter that decides which potential energy is used. This potential energy and the corresponding forces are conservative when the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} is constant in time for all atoms [\\(i\\)]{.math .notranslate .nohighlight}.

For a conservative force calculation and dynamic switching parameters, the atomic force on an atom is given by [\\(F_i = -\\nabla_i \\sum_j E_j\\)]{.math .notranslate .nohighlight} and includes the derivative of the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight}. The force contribution of this gradient of the switching function can cause large forces which are not similar to the forces of the fast or the precise interatomic potential as discussed in [[(Immel)]{.std .std-ref}](#immel2025-4){.reference .internal}. Thus, one can neglect the gradient of the switching parameter in the force calculation and compensate for the violation of energy conservation by the application of the local thermostat implemented in this fix. One can compute the violation of the energy conservation [\\(\\Delta H_i\\)]{.math .notranslate .nohighlight} for all atoms [\\(i\\)]{.math .notranslate .nohighlight} as discussed in [[(Immel)]{.std .std-ref}](#immel2025-4){.reference .internal}. To locally correct this energy violation [\\(\\Delta H_i\\)]{.math .notranslate .nohighlight}, one can rescale the velocity of atom [\\(i\\)]{.math .notranslate .nohighlight} and of neighboring atoms. The rescaling is done relative to the center-of-mass velocity of the group and, thus, conserves the momentum.

::: {.admonition .note}
Note

This local thermostat provides the NVE ensemble rather than the NVT ensemble as the energy [\\(\\Delta H_i\\)]{.math .notranslate .nohighlight} determines the rescaling factor rather than a temperature.
:::

Velocities [\\(v\\)]{.math .notranslate .nohighlight} are updated by the integrator according to [\\(\\Delta v_i = (F_i/m_i)\\Delta t\\)]{.math .notranslate .nohighlight}, whereas m denotes the mass of atom [\\(i\\)]{.math .notranslate .nohighlight} and [\\(\\Delta t\\)]{.math .notranslate .nohighlight} is the time step. One can interpret the velocity difference [\\(\\Delta v\\)]{.math .notranslate .nohighlight} caused by the rescaling as the application of an additional force which is given by [\\(F\^\\text{lt}\_i = (v\^\\text{unscaled}\_i - v\^\\text{rescaled}\_i) m_i / \\Delta t\\)]{.math .notranslate .nohighlight} [[(Immel)]{.std .std-ref}](#immel2025-4){.reference .internal}. This additional force is computed when the *store_atomic_forces* option is used.

The local thermostat is not appropriate for simulations at a temperature of 0K.

::: {.admonition .note}
Note

The maximum decrease of the kinetic energy is achieved with a rescaling factor of 0, i.e., the relative velocity of the group of rescaled atoms is set to zero. One cannot decrease the energy further. Thus, the local thermostat can fail, which is, however, reported by the returned vector.
:::
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

If the *store_atomic_forces* option is used, this fix produces every *nevery* time steps a per-atom array that contains the theoretical force applied by the local thermostat in all three spatial dimensions in the first three components. [\\(\\Delta H_i\\)]{.math .notranslate .nohighlight} is the fourth component of the per-atom array. The per-atom array can only be accessed on timesteps that are multiples of *nevery*.

Furthermore, this fix computes a global vector of length 6 with information about the rescaling:

> ::: {}
> 1.  number of atoms whose energy changed due to the last [\\(\\lambda\\)]{.math .notranslate .nohighlight} update
>
> 2.  contribution of the potential energy to the last computed [\\(\\Delta H\\)]{.math .notranslate .nohighlight}
>
> 3.  contribution of the kinetic energy to the last computed [\\(\\Delta H\\)]{.math .notranslate .nohighlight}
>
> 4.  sum over all atoms of the absolute energy change caused by the last rescaling step
>
> 5.  energy change that could not be compensated accumulated over all timesteps
>
> 6.  number of atoms whose energy change could not be compensated accumulated over all timesteps
> :::

The vector and the per-atom vector can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the APIP package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}, [[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal}, [[pair_style lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}, [[pair_style eam/apip]{.doc}]pair_eam_apip.md){.reference .internal}, [[pair_style pace/apip]{.doc}]pair_pace_apip.md){.reference .internal}, [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

seed = 42, N_rescaling = 200, *store_atomic_forces* is not used

------------------------------------------------------------------------

**(Immel)** Immel, Drautz and Sutmann, J Chem Phys, 162, 114119 (2025)
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

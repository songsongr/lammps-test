::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-ffl-command .section}
[]{#index-0}

# fix ffl command[](#fix-ffl-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID id-group ffl tau Tstart Tstop seed [flip-type]
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- ffl = style name of this fix command

- tau = thermostat parameter (positive real)

- Tstart, Tstop = temperature ramp during the run

- seed = random number seed to use for generating noise (positive integer)

- one more value may be appended

  :::: {.highlight-none .notranslate}
  ::: highlight
      flip-type  = determines the flipping type, can be chosen between rescale - no_flip - hard - soft, if no flip type is given, rescale will be chosen by default
  :::
  ::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 3 boundary ffl 10 300 300 31415
    fix 1 all ffl 100 500 500 9265 soft
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply a Fast-Forward Langevin Equation (FFL) thermostat as described in [[(Hijazi)]{.std .std-ref}](#hijazi){.reference .internal}. Contrary to [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, this fix performs both thermostatting and evolution of the Hamiltonian equations of motion, so it should not be used together with [[fix nve]{.doc}]fix_nve.md){.reference .internal} -- at least not on the same atom groups.

The time-evolution of a single particle undergoing Langevin dynamics is described by the equations

::: {.math .notranslate .nohighlight}
\\\[\\frac {dq}{dt} = \\frac{p}{m},\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[\\frac {dp}{dt} = -\\gamma p + W + F,\\\]
:::

where [\\(F\\)]{.math .notranslate .nohighlight} is the physical force, [\\(\\gamma\\)]{.math .notranslate .nohighlight} is the friction coefficient, and [\\(W\\)]{.math .notranslate .nohighlight} is a Gaussian random force.

The friction coefficient is the inverse of the thermostat parameter : [\\(\\gamma = 1/\\tau\\)]{.math .notranslate .nohighlight}, with [\\(\\tau\\)]{.math .notranslate .nohighlight} the thermostat parameter *tau*. The thermostat parameter is given in the time units, [\\(\\gamma\\)]{.math .notranslate .nohighlight} is in inverse time units.

Equilibrium sampling a temperature T is obtained by specifying the target value as the *Tstart* and *Tstop* arguments, so that the internal constants depending on the temperature are computed automatically.

The random number *seed* must be a positive integer. A Marsaglia random number generator is used. Each processor uses the input seed to generate its own unique seed and its own stream of random numbers. Thus the dynamics of the system will not be identical on two runs on different numbers of processors.

The flipping type *flip-type* can be chosen between 4 types described in [[(Hijazi)]{.std .std-ref}](#hijazi){.reference .internal}. The flipping operation occurs during the thermostatting step and it flips the momenta of the atoms. If no_flip is chosen, no flip will be executed and the integration will be the same as a standard Langevin thermostat [[(Bussi)]{.std .std-ref}](#bussi3){.reference .internal}. The other flipping types are : rescale - hard - soft.
:::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

The instantaneous values of the extended variables are written to [[binary restart files]{.doc}]restart.md){.reference .internal}. Because the state of the random number generator is not saved in restart files, this means you cannot do "exact" restarts with this fix, where the simulation continues on the same as if no restart had taken place. However, in a statistical sense, a restarted simulation should produce the same behavior. Note however that you should use a different seed each time you restart, otherwise the same sequence of random numbers will be used each time, which might lead to stochastic synchronization and subtle artifacts in the sampling.

The cumulative energy change in the system imposed by this fix is included in the [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} keywords *ecouple* and *econserve*. See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} doc page for details.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the same cumulative energy change due to this fix described in the previous paragraph. The scalar value calculated by this fix is "extensive".

This fix can ramp its target temperature over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

In order to perform constant-pressure simulations please use [[fix press/berendsen]{.doc}]fix_press_berendsen.md){.reference .internal}, rather than [[fix npt]{.doc}]fix_nh.md){.reference .internal}, to avoid duplicate integration of the equations of motion.

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, [[fix viscous]{.doc}]fix_viscous.md){.reference .internal}, [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[pair_style dpd/tstat]{.doc}]pair_dpd.md){.reference .internal}, [[fix gld]{.doc}]fix_gld.md){.reference .internal}, [[fix gle]{.doc}]fix_gle.md){.reference .internal}

------------------------------------------------------------------------

[]{#hijazi}**(Hijazi)** M. Hijazi, D. M. Wilkins, M. Ceriotti, J. Chem. Phys. 148, 184109 (2018)

**(Bussi)** G. Bussi, M. Parrinello, Phs. Rev. E 75, 056707 (2007)
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

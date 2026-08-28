::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#fix-ti-spring-command .section}
[]{#index-0}

# fix ti/spring command[](#fix-ti-spring-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID ti/spring k t_s t_eq keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- ti/spring = style name of this fix command

- k = spring constant (force/distance units)

- t_eq = number of steps for the equilibration procedure

- t_s = number of steps for the switching procedure

- zero or more keyword/value pairs may be appended to args

- keyword = *function*

  ``` literal-block
  function value = function-ID
    function-ID = ID of the switching function (1 or 2)
  ```
:::::

::::: {#example .section}
## Example[](#example "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all ti/spring 50.0 2000 1000 function 2
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix allows you to compute the free energy of crystalline solids by performing a nonequilibrium thermodynamic integration between the solid of interest and an Einstein crystal. A detailed explanation of how to use this command and choose its parameters for optimal performance and accuracy is given in the paper by [[Freitas]{.std .std-ref}](#freitas1){.reference .internal}. The paper also presents a short summary of the theory of nonequilibrium thermodynamic integration.

The thermodynamic integration procedure is performed by rescaling the force on each atom. Given an atomic configuration the force (F) on each atom is given by

::: {.math .notranslate .nohighlight}
\\\[F = \\left( 1-\\lambda \\right) F\_{\\text{solid}} + \\lambda F\_{\\text{harm}}\\\]
:::

where F_solid is the force that acts on an atom due to an interatomic potential (*e.g.* EAM potential), F_harm is the force due to the Einstein crystal harmonic spring, and lambda is the coupling parameter of the thermodynamic integration. An Einstein crystal is a solid where each atom is attached to its equilibrium position by a harmonic spring with spring constant *k*. With this fix a spring force is applied independently to each atom in the group defined by the fix to tether it to its initial position. The initial position of each atom is its position at the time the fix command was issued.

The fix acts as follows: during the first *t_eq* steps after the fix is defined the value of lambda is zero. This is the period to equilibrate the system in the lambda = 0 state. After this the value of lambda changes dynamically during the simulation from 0 to 1 according to the function defined using the keyword *function* (described below), this switching from lambda from 0 to 1 is done in *t_s* steps. Then comes the second equilibration period of *t_eq* to equilibrate the system in the lambda = 1 state. After that, the switching back to the lambda = 0 state is made using *t_s* timesteps and following the same switching function. After this period the value of lambda is kept equal to zero and the fix has no other effect on the dynamics of the system.

The processes described above is known as nonequilibrium thermodynamic integration and is has been shown ([[Freitas]{.std .std-ref}](#freitas1){.reference .internal}) to present a much superior efficiency when compared to standard equilibrium methods. The reason why the switching it is made in both directions (potential to Einstein crystal and back) is to eliminate the dissipated heat due to the nonequilibrium process. Further details about nonequilibrium thermodynamic integration and its implementation in LAMMPS is available in [[Freitas]{.std .std-ref}](#freitas1){.reference .internal}.

The *function* keyword allows the use of two different lambda paths. Option *1* results in a constant rate of change of lambda with time:

::: {.math .notranslate .nohighlight}
\\\[\\lambda(\\tau) = \\tau\\\]
:::

where [\\(\\tau\\)]{.math .notranslate .nohighlight} is the scaled time variable *t/t_s*. The option *2* performs the lambda switching at a rate defined by the following switching function

::: {.math .notranslate .nohighlight}
\\\[\\lambda(\\tau) = \\tau\^5 \\left( 70 \\tau\^4 - 315 \\tau\^3 + 540 \\tau\^2 - 420 \\tau + 126 \\right)\\\]
:::

This function has zero slope as lambda approaches its extreme values (0 and 1), according to [[de Koning]{.std .std-ref}](#dekoning96){.reference .internal} this results in smaller fluctuations on the integral to be computed on the thermodynamic integration. The use of option *2* is recommended since it results in better accuracy and less dissipation without any increase in computational resources cost.

::: {.admonition .note}
Note

As described in [[Freitas]{.std .std-ref}](#freitas1){.reference .internal}, it is important to keep the center-of-mass fixed during the thermodynamic integration. A nonzero total velocity will result in divergences during the integration due to the fact that the atoms are 'attached' to their equilibrium positions by the Einstein crystal. Check the option *zero* of [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} and [[velocity]{.doc}]velocity.md){.reference .internal}. The use of the Nose-Hoover thermostat ([[fix nvt]{.doc}]fix_nh.md){.reference .internal}) is *NOT* recommended due to its well documented issues with the canonical sampling of harmonic degrees of freedom (notice that the *chain* option will *NOT* solve this problem). The Langevin thermostat ([[fix langevin]{.doc}]fix_langevin.md){.reference .internal}) correctly thermostats the system and we advise its usage with ti/spring command.
:::
:::::::

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the original coordinates of tethered atoms to [[binary restart files]{.doc}]restart.md){.reference .internal}, so that the spring effect will be the same in a restarted simulation. See the [[read restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the energy stored in the per-atom springs to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}.

This fix computes a global scalar and a global vector quantities which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is an energy which is the sum of the spring energy for each atom, where the per-atom energy is [\\(0.5 \\cdot k \\cdot r\^2\\)]{.math .notranslate .nohighlight}. The vector stores 2 values. The first value is the coupling parameter lambda. The second value is the derivative of lambda with respect to the integer timestep *s*, i.e. [\\(\\frac{d \\lambda}{d s}\\)]{.math .notranslate .nohighlight}. In order to obtain [\\(\\frac{d \\lambda}{d t}\\)]{.math .notranslate .nohighlight}, where t is simulation time, this 2nd value needs to be divided by the timestep size (e.g. 0.5 fs). The scalar and vector values calculated by this fix are "extensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The forces due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command.

::: {.admonition .note}
Note

If you want the per-atom spring energy to be included in the total potential energy of the system (the quantity being minimized), you MUST enable the [[fix modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for this fix.
:::
::::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix spring]{.doc}]fix_spring.md){.reference .internal}, [[fix adapt]{.doc}]fix_adapt.md){.reference .internal}
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The keyword default is function = 1.

------------------------------------------------------------------------

**(Freitas)** Freitas, Asta, and de Koning, Computational Materials Science, 112, 333 (2016).

**(de Koning)** de Koning and Antonelli, Phys Rev E, 53, 465 (1996).
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

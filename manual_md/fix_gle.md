::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-gle-command .section}
[]{#index-0}

# fix gle command[](#fix-gle-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID id-group gle Ns Tstart Tstop seed Amatrix [noneq Cmatrix] [every stride]
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- gle = style name of this fix command

- Ns = number of additional fictitious momenta

- Tstart, Tstop = temperature ramp during the run

- Amatrix = file to read the drift matrix A from

- seed = random number seed to use for generating noise (positive integer)

- zero or more keyword/value pairs may be appended

  ``` literal-block
  keyword = noneq or every
    noneq Cmatrix  = file to read the non-equilibrium covariance matrix from
    every stride   = apply the GLE once every time steps. Reduces the accuracy
        of the integration of the GLE, but has *no effect* on the accuracy of equilibrium
        sampling. It might change sampling properties when used together with noneq.
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 3 boundary gle 6 300 300 31415 smart.A
    fix 1 all gle 6 300 300 31415 qt-300k.A noneq qt-300k.C
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply a Generalized Langevin Equation (GLE) thermostat as described in [[(Ceriotti)]{.std .std-ref}](#ceriotti){.reference .internal}. The formalism allows one to obtain a number of different effects ranging from efficient sampling of all vibrational modes in the system to inexpensive (approximate) modelling of nuclear quantum effects. Contrary to [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, this fix performs both thermostatting and evolution of the Hamiltonian equations of motion, so it should not be used together with [[fix nve]{.doc}]fix_nve.md){.reference .internal} -- at least not on the same atom groups.

Each degree of freedom in the thermostatted group is supplemented with Ns additional degrees of freedom s, and the equations of motion become

:::: {.highlight-none .notranslate}
::: highlight
    dq/dt=p/m
    d(p,s)/dt=(F,0) - A(p,s) + B dW/dt
:::
::::

where F is the physical force, A is the drift matrix (that generalizes the friction in Langevin dynamics), B is the diffusion term and dW/dt un-correlated Gaussian random forces. The A matrix couples the physical (q,p) dynamics with that of the additional degrees of freedom, and makes it possible to obtain effectively a history-dependent noise and friction kernel.

The drift matrix should be given as an external file *Afile*, as a (Ns+1 x Ns+1) matrix in inverse time units. Matrices that are optimal for a given application and the system of choice can be obtained from [[(GLE4MD)]{.std .std-ref}](#gle4md){.reference .internal}.

Equilibrium sampling a temperature T is obtained by specifying the target value as the *Tstart* and *Tstop* arguments, so that the diffusion matrix that gives canonical sampling for a given A is computed automatically. However, the GLE framework also allow for non-equilibrium sampling, that can be used for instance to model inexpensively zero-point energy effects [[(Ceriotti2)]{.std .std-ref}](#ceriotti2){.reference .internal}. This is achieved specifying the *noneq* keyword followed by the name of the file that contains the static covariance matrix for the non-equilibrium dynamics. Please note, that the covariance matrix is expected to be given in **temperature units**.

Since integrating GLE dynamics can be costly when used together with simple potentials, one can use the *every* optional keyword to apply the Langevin terms only once every several MD steps, in a multiple time-step fashion. This should be used with care when doing non-equilibrium sampling, but should have no effect on equilibrium averages when using canonical sampling.

The random number *seed* must be a positive integer. A Marsaglia random number generator is used. Each processor uses the input seed to generate its own unique seed and its own stream of random numbers. Thus the dynamics of the system will not be identical on two runs on different numbers of processors.

Note also that the Generalized Langevin Dynamics scheme that is implemented by the [[fix gld]{.doc}]fix_gld.md){.reference .internal} scheme is closely related to the present one. In fact, it should be always possible to cast the Prony series form of the memory kernel used by GLD into an appropriate input matrix for [[fix gle]{.doc}](#){.reference .internal}. While the GLE scheme is more general, the form used by [[fix gld]{.doc}]fix_gld.md){.reference .internal} can be more directly related to the representation of an implicit solvent environment.
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

The GLE thermostat in its current implementation should not be used with rigid bodies, SHAKE or RATTLE. It is expected that all the thermostatted degrees of freedom are fully flexible, and the sampled ensemble will not be correct otherwise.

In order to perform constant-pressure simulations please use [[fix press/berendsen]{.doc}]fix_press_berendsen.md){.reference .internal}, rather than [[fix npt]{.doc}]fix_nh.md){.reference .internal}, to avoid duplicate integration of the equations of motion.

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, [[fix viscous]{.doc}]fix_viscous.md){.reference .internal}, [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[pair_style dpd/tstat]{.doc}]pair_dpd.md){.reference .internal}, [[fix gld]{.doc}]fix_gld.md){.reference .internal}

------------------------------------------------------------------------

**(Ceriotti)** Ceriotti, Bussi and Parrinello, J Chem Theory Comput 6, 1170-80 (2010)

**(GLE4MD)** [https://gle4md.org/](https://gle4md.org/){.reference .external}

**(Ceriotti2)** Ceriotti, Bussi and Parrinello, Phys Rev Lett 103, 030603 (2009)
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-tfmc-command .section}
[]{#index-0}

# fix tfmc command[](#fix-tfmc-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID tfmc Delta Temp seed keyword value
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- tfmc = style name of this fix command

- Delta = maximal displacement length (distance units)

- Temp = imposed temperature of the system

- seed = random number seed (positive integer)

- zero or more keyword/arg pairs may be appended

- keyword = *com* or *rot*

  ``` literal-block
  com args = xflag yflag zflag
    xflag,yflag,zflag = 0/1 to exclude/include each dimension
  rot args = none
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all tfmc 0.1 1000.0 159345
    fix 1 all tfmc 0.05 600.0 658943 com 1 1 0
    fix 1 all tfmc 0.1 750.0 387068 com 1 1 1 rot
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform uniform-acceptance force-bias Monte Carlo (fbMC) simulations, using the time-stamped force-bias Monte Carlo (tfMC) algorithm described in [[(Mees)]{.std .std-ref}](#mees){.reference .internal} and [[(Bal)]{.std .std-ref}](#bal){.reference .internal}.

One successful use case of force-bias Monte Carlo methods is that they can be used to extend the time scale of atomistic simulations, in particular when long time scale relaxation effects must be considered; some interesting examples are given in the review by [[(Neyts)]{.std .std-ref}](#neyts){.reference .internal}. An example of a typical use case would be the modelling of chemical vapor deposition (CVD) processes on a surface, in which impacts by gas-phase species can be performed using MD, but subsequent relaxation of the surface is too slow to be done using MD only. Using tfMC can allow for a much faster relaxation of the surface, so that higher fluxes can be used, effectively extending the time scale of the simulation. (Such an alternating simulation approach could be set up using a [[loop]{.doc}]jump.md){.reference .internal}.)

The initial version of tfMC algorithm in [[(Mees)]{.std .std-ref}](#mees){.reference .internal} contained an estimation of the effective time scale of such a simulation, but it was later shown that the speed-up one can gain from a tfMC simulation is system- and process-dependent, ranging from none to several orders of magnitude. In general, solid-state processes such as (re)crystallization or growth can be accelerated by up to two or three orders of magnitude, whereas diffusion in the liquid phase is not accelerated at all. The observed pseudodynamics when using the tfMC method is not the actual dynamics one would obtain using MD, but the relative importance of processes can match the actual relative dynamics of the system quite well, provided *Delta* is chosen with care. Thus, the system's equilibrium is reached faster than in MD, along a path that is generally roughly similar to a typical MD simulation (but not necessarily so). See [[(Bal)]{.std .std-ref}](#bal){.reference .internal} for details.

Each step, all atoms in the selected group are displaced using the stochastic tfMC algorithm, which is designed to sample the canonical (NVT) ensemble at the temperature *Temp*. Although tfMC is a Monte Carlo algorithm and thus strictly speaking does not perform time integration, it is similar in the sense that it uses the forces on all atoms in order to update their positions. Therefore, it is implemented as a time integration fix, and no other fixes of this type (such as [[fix nve]{.doc}]fix_nve.md){.reference .internal}) should be used at the same time. Because velocities do not play a role in this kind of Monte Carlo simulations, instantaneous temperatures as calculated by [[temperature computes]{.doc}]compute_temp.md){.reference .internal} or [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} have no meaning: the only relevant temperature is the sampling temperature *Temp*. Similarly, performing tfMC simulations does not require setting a [[timestep]{.doc}]timestep.md){.reference .internal} and the [[simulated time]{.doc}]thermo_style.md){.reference .internal} as calculated by LAMMPS is meaningless.

The critical parameter determining the success of a tfMC simulation is *Delta*, the maximal displacement length of the lightest element in the system: the larger it is, the longer the effective time scale of the simulation will be (there is an approximately quadratic dependence). However, *Delta* must also be chosen sufficiently small in order to comply with detailed balance; in general values between 5 and 10 % of the nearest neighbor distance are found to be a good choice. For a more extensive discussion with specific examples, please refer to [[(Bal)]{.std .std-ref}](#bal){.reference .internal}, which also describes how the code calculates element-specific maximal displacements from *Delta*, based on the fourth root of their mass.

Because of the uncorrelated movements of the atoms, the center-of-mass of the fix group will not necessarily be stationary, just like its orientation. When the *com* keyword is used, all atom positions will be shifted (after every tfMC iteration) in order to fix the position of the center-of-mass along the included directions, by setting the corresponding flag to 1. The *rot* keyword does the same for the rotational component of the tfMC displacements after every iteration.

::: {.admonition .note}
Note

the *com* and *rot* keywords should not be used if an external force is acting on the specified fix group, along the included directions. This can be either a true external force (e.g. through [[fix wall]{.doc}]fix_wall.md){.reference .internal}) or forces due to the interaction with atoms not included in the fix group. This is because in such cases, translations or rotations of the fix group could be induced by these external forces, and removing them will lead to a violation of detailed balance.
:::
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

This fix is not compatible with [[fix shake]{.doc}]fix_shake.md){.reference .internal}.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix gcmc]{.doc}]fix_gcmc.md){.reference .internal}, [[fix nvt]{.doc}]fix_nh.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option default is com = 0 0 0

------------------------------------------------------------------------

**(Bal)** K. M Bal and E. C. Neyts, J. Chem. Phys. 141, 204104 (2014).

**(Mees)** M. J. Mees, G. Pourtois, E. C. Neyts, B. J. Thijsse, and A. Stesmans, Phys. Rev. B 85, 134301 (2012).

**(Neyts)** E. C. Neyts and A. Bogaerts, Theor. Chem. Acc. 132, 1320 (2013).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

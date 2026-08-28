::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#fix-tgnvt-drude-command .section}
[]{#index-1}[]{#index-0}

# fix tgnvt/drude command[](#fix-tgnvt-drude-command "Link to this heading"){.headerlink}
:::

:::::::::::::::::::::::: {#fix-tgnpt-drude-command .section}
# fix tgnpt/drude command[](#fix-tgnpt-drude-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID style_name keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- style_name = *tgnvt/drude* or *tgnpt/drude*

- one or more keyword/values pairs may be appended

  ``` literal-block
  keyword = temp iso or aniso or tri or x or y or z or xy or yz or xz or couple or tchain or pchain or mtk or tloop or ploop or nreset or scalexy or scaleyz or scalexz or flip or fixedpoint
    temp values = Tstart Tstop Tdamp Tdrude Tdamp_drude
      Tstart, Tstop = external temperature at start/end of run (temperature units)
      Tdamp = temperature damping parameter (time units)
      Tdrude = desired temperature of Drude oscillators (temperature units)
      Tdamp_drude = temperature damping parameter for Drude oscillators (time units)
    iso or aniso or tri values = Pstart Pstop Pdamp
      Pstart,Pstop = scalar external pressure at start/end of run (pressure units)
      Pdamp = pressure damping parameter (time units)
    x or y or z or xy or yz or xz values = Pstart Pstop Pdamp
      Pstart,Pstop = external stress tensor component at start/end of run (pressure units)
      Pdamp = stress damping parameter (time units)
    couple = none or xyz or xy or yz or xz
    tchain value = N
      N = length of thermostat chain (1 = single thermostat)
    pchain value = N
      N length of thermostat chain on barostat (0 = no thermostat)
    mtk value = yes or no = add in MTK adjustment term or not
    tloop value = M
      M = number of sub-cycles to perform on thermostat
    ploop value = M
      M = number of sub-cycles to perform on barostat thermostat
    nreset value = reset reference cell every this many timesteps
    scalexy value = yes or no = scale xy with ly
    scaleyz value = yes or no = scale yz with lz
    scalexz value = yes or no = scale xz with lz
    flip value = yes or no = allow or disallow box flips when it becomes highly skewed
    fixedpoint values = x y z
      x,y,z = perform barostat dilation/contraction around this point (distance units)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    comm_modify vel yes
    fix 1 all tgnvt/drude temp 300.0 300.0 100.0 1.0 20.0
    fix 1 water tgnpt/drude temp 300.0 300.0 100.0 1.0 20.0 iso 0.0 0.0 1000.0
    fix 2 jello tgnpt/drude temp 300.0 300.0 100.0 1.0 20.0 tri 5.0 5.0 1000.0
    fix 2 ice tgnpt/drude temp 250.0 250.0 100.0 1.0 20.0 x 1.0 1.0 0.5 y 2.0 2.0 0.5 z 3.0 3.0 0.5 yz 0.1 0.1 0.5 xz 0.2 0.2 0.5 xy 0.3 0.3 0.5 nreset 1000
:::
::::

Example input scripts available: examples/PACKAGES/drude
:::::

:::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

These commands are variants of the Nose-Hoover fix styles [[fix nvt]{.doc}]fix_nh.md){.reference .internal} and [[fix npt]{.doc}]fix_nh.md){.reference .internal} for thermalized Drude polarizable models. They apply temperature-grouped Nose-Hoover thermostat (TGNH) proposed by [[(Son)]{.std .std-ref}](#tgnh-son){.reference .internal}. When there are fast vibrational modes with frequencies close to Drude oscillators (e.g. double bonds or out-of-plane torsions), this thermostat can provide better kinetic energy equipartitioning.

The difference between TGNH and the original Nose-Hoover thermostat is that, TGNH separates the kinetic energy of the group into three contributions: molecular center of mass (COM) motion, motion of COM of atom-Drude pairs or non-polarizable atoms relative to molecular COM, and relative motion of atom-Drude pairs. An independent Nose-Hoover chain is applied to each type of motion. The temperatures for these three types of motion are denoted as molecular translational temperature ([\\(T\_\\mathrm{M}\\)]{.math .notranslate .nohighlight}), real atomic temperature ([\\(T\_\\mathrm{R}\\)]{.math .notranslate .nohighlight}) and Drude temperature ([\\(T\_\\mathrm{D}\\)]{.math .notranslate .nohighlight}), which are defined in terms of their associated degrees of freedom (DOF):

::: {.math .notranslate .nohighlight}
\\\[T\_\\mathrm{M}=\\frac{\\Sigma\_{i}\^{N\_\\mathrm{mol}} M_i V_i\^2}{3 \\left ( N\_\\mathrm{mol} - \\frac{N\_\\mathrm{mol}}{N\_\\mathrm{mol,sys}} \\right ) k\_\\mathrm{B}}\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[T\_\\mathrm{R}=\\frac{\\Sigma\_{i}\^{N\_\\mathrm{real}} m_i (v_i-v\_{M,i})\^2}{(N\_\\mathrm{DOF} - 3 N\_\\mathrm{mol} + 3 \\frac{N\_\\mathrm{mol}}{N\_\\mathrm{mol,sys}} - 3 N\_\\mathrm{drude}) k\_\\mathrm{B}}\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[T\_\\mathrm{D}=\\frac{\\Sigma\_{i}\^{N\_\\mathrm{drude}} m_i\^{\\prime} v_i\^{\\prime 2}}{3 N\_\\mathrm{drude} k\_\\mathrm{B}}\\\]
:::

Here [\\(N\_\\mathrm{mol}\\)]{.math .notranslate .nohighlight} and [\\(N\_\\mathrm{mol,sys}\\)]{.math .notranslate .nohighlight} are the numbers of molecules in the group and in the whole system, respectively. [\\(N\_\\mathrm{real}\\)]{.math .notranslate .nohighlight} is the number of atom-Drude pairs and non-polarizable atoms in the group. [\\(N\_\\mathrm{drude}\\)]{.math .notranslate .nohighlight} is the number of Drude particles in the group. [\\(N\_\\mathrm{DOF}\\)]{.math .notranslate .nohighlight} is the DOF of the group. [\\(M_i\\)]{.math .notranslate .nohighlight} and [\\(V_i\\)]{.math .notranslate .nohighlight} are the mass and the COM velocity of the i-th molecule. [\\(m_i\\)]{.math .notranslate .nohighlight} is the mass of the i-th atom-Drude pair or non-polarizable atom. [\\(v_i\\)]{.math .notranslate .nohighlight} is the velocity of COM of i-th atom-Drude pair or non-polarizable atom. [\\(v\_{M,i}\\)]{.math .notranslate .nohighlight} is the COM velocity of the molecule the i-th atom-Drude pair or non-polarizable atom belongs to. [\\(m_i\^\\prime\\)]{.math .notranslate .nohighlight} and [\\(v_i\^\\prime\\)]{.math .notranslate .nohighlight} are the reduced mass and the relative velocity of the i-th atom-Drude pair.

::: {.admonition .note}
Note

These fixes require that each atom knows whether it is a Drude particle or not. You must therefore use the [[fix drude]{.doc}]fix_drude.md){.reference .internal} command to specify the Drude status of each atom type.

Because the TGNH thermostat thermostats the molecular COM motion, all atoms belonging to the same molecule must be in the same group. That is, these fixes can not be applied to a subset of a molecule.

For this fix to act correctly, ghost atoms need to know their velocity. You must use the [[comm_modify]{.doc}]comm_modify.md){.reference .internal} command to enable this.

These fixes assume that the translational DOF of the whole system is removed. It is therefore recommended to invoke [[fix momentum]{.doc}]fix_momentum.md){.reference .internal} command so that the [\\(T\_\\mathrm{M}\\)]{.math .notranslate .nohighlight} is calculated correctly.
:::

------------------------------------------------------------------------

The thermostat parameters are specified using the *temp* keyword. The thermostat is applied to only the translational DOF for the particles. The translational DOF can also have a bias velocity removed before thermostatting takes place; see the description below. The desired temperature for molecular and real atomic motion is a ramped value during the run from *Tstart* to *Tstop*. The *Tdamp* parameter is specified in time units and determines how rapidly the temperature is relaxed. For example, a value of 10.0 means to relax the temperature in a timespan of (roughly) 10 time units (e.g. [\\(\\tau\\)]{.math .notranslate .nohighlight} or fs or ps - see the [[units]{.doc}]units.md){.reference .internal} command). The parameter *Tdrude* is the desired temperature for Drude motion at each timestep. Similar to *Tdamp*, the *Tdamp_drude* parameter determines the relaxation speed for Drude motion. Fix group are the only ones whose velocities and positions are updated by the velocity/position update portion of the integration. Other thermostat-related keywords are *tchain* and *tloop*, which are detailed in [[fix nvt]{.doc}]fix_nh.md){.reference .internal}.

::: {.admonition .note}
Note

A Nose-Hoover thermostat will not work well for arbitrary values of *Tdamp*. If *Tdamp* is too small, the temperature can fluctuate wildly; if it is too large, the temperature will take a very long time to equilibrate. A good choice for many models is a *Tdamp* of around 100 timesteps. A smaller *Tdamp_drude* value would be required to maintain Drude motion at low temperature.
:::

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nvt temp 300.0 300.0 $(100.0*dt) 1.0 $(20.0*dt)
:::
::::

------------------------------------------------------------------------

The barostat parameters for fix style *tgnpt/drude* is specified using one or more of the *iso*, *aniso*, *tri*, *x*, *y*, *z*, *xy*, *xz*, *yz*, and *couple* keywords. These keywords give you the ability to specify all 6 components of an external stress tensor, and to couple various of these components together so that the dimensions they represent are varied together during a constant-pressure simulation. Other barostat-related keywords are *pchain*, *mtk*, *ploop*, *nreset*, *scalexy*, *scaleyz*, *scalexz*, *flip*and *fixedpoint*. The meaning of barostat parameters are detailed in [[fix npt]{.doc}]fix_nh.md){.reference .internal}.

Regardless of what atoms are in the fix group (the only atoms which are time integrated), a global pressure or stress tensor is computed for all atoms. Similarly, when the size of the simulation box is changed, all atoms are re-scaled to new positions.

::: {.admonition .note}
Note

Unlike the [[fix temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal} command which performs thermostatting but NO time integration, these fixes perform thermostatting/barostatting AND time integration. Thus you should not use any other time integration fix, such as [[fix nve]{.doc}]fix_nve.md){.reference .internal} on atoms to which this fix is applied. Likewise, these fixes should not be used on atoms that also have their temperature controlled by another fix - e.g. by [[fix langevin/drude]{.doc}]fix_langevin_drude.md){.reference .internal} command.
:::

See the [[Howto thermostat]{.doc}]Howto_thermostat.md){.reference .internal} and [[Howto barostat]{.doc}]Howto_barostat.md){.reference .internal} doc pages for a discussion of different ways to compute temperature and perform thermostatting and barostatting.

------------------------------------------------------------------------

Like other fixes that perform thermostatting, this fix can be used with [[compute commands]{.doc}]compute.md){.reference .internal} that remove a "bias" from the atom velocities. E.g. to apply the thermostat only to atoms within a spatial [[region]{.doc}]region.md){.reference .internal}, or to remove the center-of-mass velocity from a group of atoms, or to remove the x-component of velocity from the calculation.

This is not done by default, but only if the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command is used to assign a temperature compute to this fix that includes such a bias term. See the doc pages for individual [[compute temp commands]{.doc}]compute.md){.reference .internal} to determine which ones include a bias. In this case, the thermostat works in the following manner: bias is removed from each atom, thermostatting is performed on the remaining thermal degrees of freedom, and the bias is added back in.

::: {.admonition .note}
Note

However, not all temperature compute commands are valid to be used with these fixes. Precisely, only temperature compute that does not modify the DOF of the group can be used. E.g. [[compute temp/ramp]{.doc}]compute_temp_ramp.md){.reference .internal} and [[compute viscosity/cos]{.doc}]compute_viscosity_cos.md){.reference .internal} compute the kinetic energy after remove a velocity gradient without affecting the DOF of the group, then they can be invoked in this way. In contrast, [[compute temp/partial]{.doc}]compute_temp_partial.md){.reference .internal} may remove the DOF at one or more dimensions, therefore it cannot be used with these fixes.
:::
::::::::::::

------------------------------------------------------------------------

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

These fixes writes the state of all the thermostat and barostat variables to [[binary restart files]{.doc}]restart.md){.reference .internal}. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* and *press* options are supported by these fixes. You can use them to assign a [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its thermostatting or barostatting procedure, as described above. If you do this, note that the kinetic energy derived from the compute temperature should be consistent with the virial term computed using all atoms for the pressure. LAMMPS will warn you if you choose to compute temperature on a subset of atoms.

::: {.admonition .note}
Note

If both the *temp* and *press* keywords are used in a single thermo_modify command (or in two separate commands), then the order in which the keywords are specified is important. Note that a [[pressure compute]{.doc}]compute_pressure.md){.reference .internal} defines its own temperature compute as an argument when it is specified. The *temp* keyword will override this (for the pressure compute being used by fix npt), but only if the *temp* keyword comes after the *press* keyword. If the *temp* keyword comes before the *press* keyword, then the new pressure compute specified by the *press* keyword will be unaffected by the *temp* setting.
:::

The cumulative energy change in the system imposed by these fixes, due to thermostatting and/or barostatting, are included in the [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} keywords *ecouple* and *econserve*. See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} page for details.

These fixes compute a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the same cumulative energy change due to this fix described in the previous paragraph. The scalar value calculated by this fix is "extensive".

These fixes also compute a global vector of quantities, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The vector values are "intensive". The vector stores the three temperatures [\\(T\_\\mathrm{M}\\)]{.math .notranslate .nohighlight}, [\\(T\_\\mathrm{R}\\)]{.math .notranslate .nohighlight} and [\\(T\_\\mathrm{D}\\)]{.math .notranslate .nohighlight}.

These fixes can ramp their external temperature and pressure over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

These fixes are not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These fixes are only available when LAMMPS was built with the DRUDE package. These fixes cannot be used with dynamic groups as defined by the [[group]{.doc}]group.md){.reference .internal} command. These fixes cannot be used in 2D simulations.

*X*, *y*, *z* cannot be barostatted if the associated dimension is not periodic. *Xy*, *xz*, and *yz* can only be barostatted if the simulation domain is triclinic and the second dimension in the keyword (*y* dimension in *xy*) is periodic. The [[create_box]{.doc}]create_box.md){.reference .internal}, [[read data]{.doc}]read_data.md){.reference .internal}, and [[read_restart]{.doc}]read_restart.md){.reference .internal} commands specify whether the simulation box is orthogonal or non-orthogonal (triclinic) and explain the meaning of the xy,xz,yz tilt factors.

For the *temp* keyword, the final *Tstop* cannot be 0.0 since it would make the external T = 0.0 at some timestep during the simulation which is not allowed in the Nose/Hoover formulation.

The *scaleyz yes*, *scalexz yes*, and *scalexy yes* options can only be used if the second dimension in the keyword is periodic, and if the tilt factor is not coupled to the barostat via keywords *tri*, *yz*, *xz*, and *xy*.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix drude]{.doc}]fix_drude.md){.reference .internal}, [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix_npt]{.doc}]fix_nh.md){.reference .internal}, [[fix_modify]{.doc}]fix_modify.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The keyword defaults are tchain = 3, pchain = 3, mtk = yes, tloop = 1, ploop = 1, nreset = 0, couple = none, flip = yes, scaleyz = scalexz = scalexy = yes if periodic in second dimension and not coupled to barostat, otherwise no.

------------------------------------------------------------------------

**(Son)** Son, McDaniel, Cui and Yethiraj, J Phys Chem Lett, 10, 7523 (2019).
:::
::::::::::::::::::::::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::

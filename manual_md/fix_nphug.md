:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-nphug-command .section}
[]{#index-1}[]{#index-0}

# fix nphug command[](#fix-nphug-command "Link to this heading"){.headerlink}

Accelerator Variants: *nphug/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nphug keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

  ``` literal-block
  one or more keyword value pairs may be appended
  keyword = temp or iso or aniso or tri or x or y or z or couple or tchain or pchain or mtk or tloop or ploop or nreset or drag or dilate or scaleyz or scalexz or scalexy
    temp values = Value1 Value2 Tdamp
      Value1, Value2 = Nose-Hoover target temperatures, ignored by Hugoniostat
      Tdamp = temperature damping parameter (time units)
    iso or aniso or tri values = Pstart Pstop Pdamp
      Pstart,Pstop = scalar external pressures, must be equal (pressure units)
      Pdamp = pressure damping parameter (time units)
    x or y or z or xy or yz or xz values = Pstart Pstop Pdamp
      Pstart,Pstop = external stress tensor components, must be equal (pressure units)
      Pdamp = stress damping parameter (time units)
    couple = none or xyz or xy or yz or xz
    tchain value = length of thermostat chain (1 = single thermostat)
    pchain values = length of thermostat chain on barostat (0 = no thermostat)
    mtk value = yes or no = add in MTK adjustment term or not
    tloop value = number of sub-cycles to perform on thermostat
    ploop value = number of sub-cycles to perform on barostat thermostat
    nreset value = reset reference cell every this many timesteps
    drag value = drag factor added to barostat/thermostat (0.0 = no drag)
    dilate value = all or partial
    scaleyz value = yes or no = scale yz with lz
    scalexz value = yes or no = scale xz with lz
    scalexy value = yes or no = scale xy with ly
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix myhug all nphug temp 1.0 1.0 10.0 z 40.0 40.0 70.0
    fix myhug all nphug temp 1.0 1.0 10.0 iso 40.0 40.0 70.0 drag 200.0 tchain 1 pchain 0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command is a variant of the Nose-Hoover [[fix npt]{.doc}]fix_nh.md){.reference .internal} fix style. It performs time integration of the Hugoniostat equations of motion developed by Ravelo et al. [[(Ravelo)]{.std .std-ref}](#ravelo1){.reference .internal}. These equations compress the system to a state with average axial stress or pressure equal to the specified target value and that satisfies the Rankine-Hugoniot (RH) jump conditions for steady shocks.

The compression can be performed either hydrostatically (using keyword *iso*, *aniso*, or *tri*) or uniaxially (using keywords *x*, *y*, or *z*). In the hydrostatic case, the cell dimensions change dynamically so that the average axial stress in all three directions converges towards the specified target value. In the uniaxial case, the chosen cell dimension changes dynamically so that the average axial stress in that direction converges towards the target value. The other two cell dimensions are kept fixed (zero lateral strain).

This leads to the following additional restrictions on the keywords:

- One and only one of the following keywords should be used: *iso*, *aniso*, *tri*, *x*, *y*, *z*

- The specified initial and final target pressures must be the same.

- The keywords *xy*, *xz*, *yz* may not be used.

- The only admissible value for the couple keyword is *xyz*, which has the same effect as keyword *iso*

- The *temp* keyword must be used to specify the time constant for kinetic energy relaxation, but initial and final target temperature values are ignored.

Essentially, a Hugoniostat simulation is an NPT simulation in which the user-specified target temperature is replaced with a time-dependent target temperature Tt obtained from the following equation:

::: {.math .notranslate .nohighlight}
\\\[T_t - T = \\frac{\\left(\\frac{1}{2}\\left(P + P_0\\right)\\left(V_0 - V\\right) + E_0 - E\\right)}{N\_{dof} k_B } = \\Delta\\\]
:::

where [\\(T\\)]{.math .notranslate .nohighlight} and [\\(T_t\\)]{.math .notranslate .nohighlight} are the instantaneous and target temperatures, *P* and [\\(P_0\\)]{.math .notranslate .nohighlight} are the instantaneous and reference pressures or axial stresses, depending on whether hydrostatic or uniaxial compression is being performed, *V* and [\\(V_0\\)]{.math .notranslate .nohighlight} are the instantaneous and reference volumes, *E* and [\\(E_0\\)]{.math .notranslate .nohighlight} are the instantaneous and reference internal energy (potential plus kinetic), [\\(N\_{dof}\\)]{.math .notranslate .nohighlight} is the number of degrees of freedom used in the definition of temperature, and [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant. [\\(\\Delta\\)]{.math .notranslate .nohighlight} is the negative deviation of the instantaneous temperature from the target temperature. When the system reaches a stable equilibrium, the value of [\\(\\Delta\\)]{.math .notranslate .nohighlight} should fluctuate about zero.

The values of [\\(E_0\\)]{.math .notranslate .nohighlight}, [\\(V_0\\)]{.math .notranslate .nohighlight}, and [\\(P_0\\)]{.math .notranslate .nohighlight} are the instantaneous values at the start of the simulation. These can be overridden using the fix_modify keywords *e0*, *v0*, and *p0* described below.

------------------------------------------------------------------------

::: {.admonition .note}
Note

Unlike the [[fix temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal} command which performs thermostatting but NO time integration, this fix performs thermostatting/barostatting AND time integration. Thus you should not use any other time integration fix, such as [[fix nve]{.doc}]fix_nve.md){.reference .internal} on atoms to which this fix is applied. Likewise, this fix should not be used on atoms that have their temperature controlled by another fix - e.g. by [[fix langevin]{.doc}]fix_nh.md){.reference .internal} or [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal} commands.
:::

------------------------------------------------------------------------

This fix computes a temperature and pressure at each timestep. To do this, the fix creates its own computes of style "temp" and "pressure", as if one of these two sets of commands had been issued:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute fix-ID_temp group-ID temp
    compute fix-ID_press group-ID pressure fix-ID_temp

    compute fix-ID_temp all temp
    compute fix-ID_press all pressure fix-ID_temp
:::
::::

See the [[compute temp]{.doc}]compute_temp.md){.reference .internal} and [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} commands for details. Note that the IDs of the new computes are the fix-ID + underscore + "temp" or fix_ID + underscore + "press". The group for the new computes is "all" since pressure is computed for the entire system.

Note that these are NOT the computes used by thermodynamic output (see the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command) with ID = *thermo_temp* and *thermo_press*. This means you can change the attributes of this fix's temperature or pressure via the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command or print this temperature or pressure during thermodynamic output via the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command using the appropriate compute-ID. It also means that changing attributes of *thermo_temp* or *thermo_press* will have no effect on this fix.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the values of [\\(E_0\\)]{.math .notranslate .nohighlight}, [\\(V_0\\)]{.math .notranslate .nohighlight}, and [\\(P_0\\)]{.math .notranslate .nohighlight}, as well as the state of all the thermostat and barostat variables to [[binary restart files]{.doc}]restart.md){.reference .internal}. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *e0*, *v0* and *p0* keywords can be used to define the values of [\\(E_0\\)]{.math .notranslate .nohighlight}, [\\(V_0\\)]{.math .notranslate .nohighlight}, and [\\(P_0\\)]{.math .notranslate .nohighlight}. Note the the values for *e0* and *v0* are extensive, and so must correspond to the total energy and volume of the entire system, not energy and volume per atom. If any of these quantities are not specified, then the instantaneous value in the system at the start of the simulation is used.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* and *press* options are supported by this fix. You can use them to assign a [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its thermostatting or barostatting procedure, as described above. If you do this, note that the kinetic energy derived from the compute temperature should be consistent with the virial term computed using all atoms for the pressure. LAMMPS will warn you if you choose to compute temperature on a subset of atoms.

The cumulative energy change in the system imposed by this fix is included in the [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} keywords *ecouple* and *econserve*. See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} doc page for details. Note that this energy is \*not\* included in the definition of internal energy E when calculating the value of Delta in the above equation.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the same cumulative energy change due to this fix described in the previous paragraph. The scalar value calculated by this fix is "extensive".

This fix also computes a global vector of quantities, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar The vector values are "intensive".

The vector stores three quantities unique to this fix ([\\(\\Delta\\)]{.math .notranslate .nohighlight}, Us, and up), followed by all the internal Nose/Hoover thermostat and barostat variables defined for [[fix npt]{.doc}]fix_nh.md){.reference .internal}. Delta is the deviation of the temperature from the target temperature, given by the above equation. Us and up are the shock and particle velocity corresponding to a steady shock calculated from the RH conditions. They have units of distance/time.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix style is part of the SHOCK package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

All the usual restrictions for [[fix npt]{.doc}]fix_nh.md){.reference .internal} apply, plus the additional ones mentioned above.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix msst]{.doc}]fix_msst.md){.reference .internal}, [[fix npt]{.doc}]fix_nh.md){.reference .internal}, [[fix_modify]{.doc}]fix_modify.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The keyword defaults are the same as those for [[fix npt]{.doc}]fix_nh.md){.reference .internal}

------------------------------------------------------------------------

**(Ravelo)** Ravelo, Holian, Germann and Lomdahl, Phys Rev B, 70, 014103 (2004).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-npt-body-command .section}
[]{#index-0}

# fix npt/body command[](#fix-npt-body-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID npt/body keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- npt/body = style name of this fix command

- additional thermostat and barostat related keyword/value pairs from the [[fix npt]{.doc}]fix_nh.md){.reference .internal} command can be appended
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all npt/body temp 300.0 300.0 100.0 iso 0.0 0.0 1000.0
    fix 2 all npt/body temp 300.0 300.0 100.0 x 5.0 5.0 1000.0
    fix 2 all npt/body temp 300.0 300.0 100.0 x 5.0 5.0 1000.0 drag 0.2
    fix 2 water npt/body temp 300.0 300.0 100.0 aniso 0.0 0.0 1000.0 dilate partial
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform constant NPT integration to update position, velocity, orientation, and angular velocity each timestep for body particles in the group using a Nose/Hoover temperature thermostat and Nose/Hoover pressure barostat. P is pressure; T is temperature. This creates a system trajectory consistent with the isothermal-isobaric ensemble.

This fix differs from the [[fix npt]{.doc}]fix_nh.md){.reference .internal} command, which assumes point particles and only updates their position and velocity.

The thermostat is applied to both the translational and rotational degrees of freedom for the body particles, assuming a compute is used which calculates a temperature that includes the rotational degrees of freedom (see below). The translational degrees of freedom can also have a bias velocity removed from them before thermostatting takes place; see the description below.

Additional parameters affecting the thermostat and barostat are specified by keywords and values documented with the [[fix npt]{.doc}]fix_nh.md){.reference .internal} command. See, for example, discussion of the *temp*, *iso*, *aniso*, and *dilate* keywords.

The particles in the fix group are the only ones whose velocities and positions are updated by the velocity/position update portion of the NPT integration.

Regardless of what particles are in the fix group, a global pressure is computed for all particles. Similarly, when the size of the simulation box is changed, all particles are re-scaled to new positions, unless the keyword *dilate* is specified with a value of *partial*, in which case only the particles in the fix group are re-scaled. The latter can be useful for leaving the coordinates of particles in a solid substrate unchanged and controlling the pressure of a surrounding fluid.

------------------------------------------------------------------------

This fix computes a temperature and pressure each timestep. To do this, the fix creates its own computes of style "temp/body" and "pressure", as if these commands had been issued:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute fix-ID_temp all temp/body
    compute fix-ID_press all pressure fix-ID_temp
:::
::::

See the [[compute temp/body]{.doc}]compute_temp_body.md){.reference .internal} and [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} commands for details. Note that the IDs of the new computes are the fix-ID + underscore + "temp" or fix_ID + underscore + "press", and the group for the new computes is "all" since pressure is computed for the entire system.

Note that these are NOT the computes used by thermodynamic output (see the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command) with ID = *thermo_temp* and *thermo_press*. This means you can change the attributes of this fix's temperature or pressure via the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command or print this temperature or pressure during thermodynamic output via the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command using the appropriate compute-ID. It also means that changing attributes of *thermo_temp* or *thermo_press* will have no effect on this fix.

Like other fixes that perform thermostatting, this fix can be used with [[compute commands]{.doc}]compute.md){.reference .internal} that remove a "bias" from the atom velocities. E.g. to apply the thermostat only to atoms within a spatial [[region]{.doc}]region.md){.reference .internal}, or to remove the center-of-mass velocity from a group of atoms, or to remove the x-component of velocity from the calculation.

This is not done by default, but only if the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command is used to assign a temperature compute to this fix that includes such a bias term. See the doc pages for individual [[compute temp commands]{.doc}]compute.md){.reference .internal} to determine which ones include a bias. In this case, the thermostat works in the following manner: bias is removed from each atom, thermostatting is performed on the remaining thermal degrees of freedom, and the bias is added back in.
:::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the state of the Nose/Hoover thermostat and barostat to [[binary restart files]{.doc}]restart.md){.reference .internal}. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* and *press* options are supported by this fix. You can use them to assign a [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its thermostatting or barostatting procedure. If you do this, note that the kinetic energy derived from the compute temperature should be consistent with the virial term computed using all atoms for the pressure. LAMMPS will warn you if you choose to compute temperature on a subset of atoms.

The cumulative energy change in the system imposed by this fix is included in the [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} keywords *ecouple* and *econserve*. See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} doc page for details.

This fix computes the same global scalar and global vector of quantities as does the [[fix npt]{.doc}]fix_nh.md){.reference .internal} command.

This fix can ramp its target temperature and pressure over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the BODY package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This fix requires that atoms store torque and angular momentum and a quaternion as defined by the [[atom_style body]{.doc}]atom_style.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix npt]{.doc}]fix_nh.md){.reference .internal}, [[fix nve_body]{.doc}]fix_nve_body.md){.reference .internal}, [[fix nvt_body]{.doc}]fix_nvt_body.md){.reference .internal}, [[fix_modify]{.doc}]fix_modify.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

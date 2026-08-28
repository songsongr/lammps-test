:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#barostats .section}
# [10.2.5. ]{.section-number}Barostats[](#barostats "Link to this heading"){.headerlink}

Barostatting means controlling the pressure in an MD simulation. [[Thermostatting]{.doc}]Howto_thermostat.md){.reference .internal} means controlling the temperature of the particles. Since the pressure includes a kinetic component due to particle velocities, both these operations require calculation of the temperature. Typically a target temperature (T) and/or pressure (P) is specified by the user, and the thermostat or barostat attempts to equilibrate the system to the requested T and/or P.

Barostatting in LAMMPS is performed by [[fixes]{.doc}]fix.md){.reference .internal}. Three barostatting methods are currently available: Nose-Hoover (npt and nph), Berendsen, and various linear controllers in deform/pressure:

- [[fix npt]{.doc}]fix_nh.md){.reference .internal}

- [[fix npt/sphere]{.doc}]fix_npt_sphere.md){.reference .internal}

- [[fix npt/asphere]{.doc}]fix_npt_asphere.md){.reference .internal}

- [[fix nph]{.doc}]fix_nh.md){.reference .internal}

- [[fix press/berendsen]{.doc}]fix_press_berendsen.md){.reference .internal}

- [[fix deform/pressure]{.doc}]fix_deform_pressure.md){.reference .internal}

The [[fix npt]{.doc}]fix_nh.md){.reference .internal} commands include a Nose-Hoover thermostat and barostat. [[Fix nph]{.doc}]fix_nh.md){.reference .internal} is just a Nose/Hoover barostat; it does no thermostatting. The fixes [[nph]{.doc}]fix_nh.md){.reference .internal}, [[press/berendsen]{.doc}]fix_press_berendsen.md){.reference .internal}, and [[deform/pressure]{.doc}]fix_deform_pressure.md){.reference .internal} can be used in conjunction with any of the thermostatting fixes.

As with the [[thermostats]{.doc}]Howto_thermostat.md){.reference .internal}, [[fix npt]{.doc}]fix_nh.md){.reference .internal} and [[fix nph]{.doc}]fix_nh.md){.reference .internal} only use translational motion of the particles in computing T and P and performing thermo/barostatting. [[Fix npt/sphere]{.doc}]fix_npt_sphere.md){.reference .internal} and [[fix npt/asphere]{.doc}]fix_npt_asphere.md){.reference .internal} thermo/barostat using not only translation velocities but also rotational velocities for spherical and aspherical particles.

All of the barostatting fixes use the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} compute to calculate a current pressure. By default, this compute is created with a simple [[compute temp]{.doc}]compute_temp.md){.reference .internal} (see the last argument of the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} command), which is used to calculated the kinetic component of the pressure. The barostatting fixes can also use temperature computes that remove bias for the purpose of computing the kinetic component which contributes to the current pressure. See the doc pages for the individual fixes and for the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command for instructions on how to assign a temperature or pressure compute to a barostatting fix.

::: {.admonition .note}
Note

As with the thermostats, the Nose/Hoover methods ([[fix npt]{.doc}]fix_nh.md){.reference .internal} and [[fix nph]{.doc}]fix_nh.md){.reference .internal}) perform time integration. [[Fix press/berendsen]{.doc}]fix_press_berendsen.md){.reference .internal} and [[fix deform/pressure]{.doc}]fix_deform_pressure.md){.reference .internal} do NOT, so they should be used with one of the constant NVE fixes or with one of the NVT fixes.
:::

Thermodynamic output, which can be setup via the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command, often includes pressure values. As explained on the page for the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command, the default pressure is setup by the thermo command itself. It is NOT the pressure associated with any barostatting fix you have defined or with any compute you have defined that calculates a pressure. The doc pages for the barostatting fixes explain the ID of the pressure compute they create. Thus if you want to view these pressures, you need to specify them explicitly via the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command. Or you can use the [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} command to re-define what pressure compute is used for default thermodynamic output.
::::
:::::
::::::

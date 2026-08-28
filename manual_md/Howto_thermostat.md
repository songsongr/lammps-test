::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#thermostats .section}
# [10.2.4. ]{.section-number}Thermostats[](#thermostats "Link to this heading"){.headerlink}

Thermostatting means controlling the temperature of particles in an MD simulation. [[Barostatting]{.doc}]Howto_barostat.md){.reference .internal} means controlling the pressure. Since the pressure includes a kinetic component due to particle velocities, both these operations require calculation of the temperature. Typically a target temperature (T) and/or pressure (P) is specified by the user, and the thermostat or barostat attempts to equilibrate the system to the requested T and/or P.

Thermostatting in LAMMPS is performed by [[fixes]{.doc}]fix.md){.reference .internal}, or in one case by a pair style. Several thermostatting fixes are available: Nose-Hoover (nvt), Berendsen, CSVR, Langevin, and direct rescaling (temp/rescale). Dissipative particle dynamics (DPD) thermostatting can be invoked via the *dpd/tstat* pair style:

- [[fix nvt]{.doc}]fix_nh.md){.reference .internal}

- [[fix nvt/sphere]{.doc}]fix_nvt_sphere.md){.reference .internal}

- [[fix nvt/asphere]{.doc}]fix_nvt_asphere.md){.reference .internal}

- [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal}

- [[fix temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal}

- [[fix temp/csvr]{.doc}]fix_temp_csvr.md){.reference .internal}

- [[fix ffl]{.doc}]fix_ffl.md){.reference .internal}

- [[fix gjf]{.doc}]fix_gjf.md){.reference .internal}

- [[fix gld]{.doc}]fix_gld.md){.reference .internal}

- [[fix gle]{.doc}]fix_gle.md){.reference .internal}

- [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}

- [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}

- [[pair_style dpd/tstat]{.doc}]pair_dpd.md){.reference .internal}

- [[pair_style dpd/ext/tstat]{.doc}]pair_dpd_ext.md){.reference .internal}

[[Fix nvt]{.doc}]fix_nh.md){.reference .internal} only thermostats the translational velocity of particles. [[Fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal} also does this, except that it subtracts out a velocity bias due to a deforming box and integrates the SLLOD equations of motion. See the [[Howto nemd]{.doc}]Howto_nemd.md){.reference .internal} page for further details. [[Fix nvt/sphere]{.doc}]fix_nvt_sphere.md){.reference .internal} and [[fix nvt/asphere]{.doc}]fix_nvt_asphere.md){.reference .internal} thermostat not only translation velocities but also rotational velocities for spherical and aspherical particles.

::: {.admonition .note}
Note

A recent (2017) book by [[(Daivis and Todd)]{.std .std-ref}](#daivis-thermostat){.reference .internal} discusses use of the SLLOD method and non-equilibrium MD (NEMD) thermostatting generally, for both simple and complex fluids, e.g. molecular systems. The latter can be tricky to do correctly.
:::

DPD thermostatting alters pairwise interactions in a manner analogous to the per-particle thermostatting of [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}.

Any of the thermostatting fixes can be instructed to use custom temperature computes that remove bias which has two effects: first, the current calculated temperature, which is compared to the requested target temperature, is calculated with the velocity bias removed; second, the thermostat adjusts only the thermal temperature component of the particle's velocities, which are the velocities with the bias removed. The removed bias is then added back to the adjusted velocities. See the doc pages for the individual fixes and for the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command for instructions on how to assign a temperature compute to a thermostatting fix.

For example, you can apply a thermostat only to atoms in a spatial region by using it in conjunction with [[compute temp/region]{.doc}]compute_temp_region.md){.reference .internal}. Or you can apply a thermostat to only the x and z components of velocity by using it with [[compute temp/partial]{.doc}]compute_temp_partial.md){.reference .internal}. Of you could thermostat only the thermal temperature of a streaming flow of particles without affecting the streaming velocity, by using [[compute temp/profile]{.doc}]compute_temp_profile.md){.reference .internal}.

Below is a list of custom temperature computes that can be used like that:

- [[compute temp/asphere command]{.doc}]compute_temp_asphere.md){.reference .internal}

- [[compute temp/body command]{.doc}]compute_temp_body.md){.reference .internal}

- [[compute temp/chunk command]{.doc}]compute_temp_chunk.md){.reference .internal}

- [[compute temp/com command]{.doc}]compute_temp_com.md){.reference .internal}

- [[compute temp/deform command]{.doc}]compute_temp_deform.md){.reference .internal}

- [[compute temp/partial command]{.doc}]compute_temp_partial.md){.reference .internal}

- [[compute temp/profile command]{.doc}]compute_temp_profile.md){.reference .internal}

- [[compute temp/ramp command]{.doc}]compute_temp_ramp.md){.reference .internal}

- [[compute temp/region command]{.doc}]compute_temp_region.md){.reference .internal}

- [[compute temp/rotate command]{.doc}]compute_temp_rotate.md){.reference .internal}

- [[compute temp/sphere command]{.doc}]compute_temp_sphere.md){.reference .internal}

::: {.admonition .note}
Note

Not all thermostat fixes perform time integration, meaning they update the velocities and positions of particles due to forces and velocities respectively. The other thermostat fixes only adjust velocities; they do NOT perform time integration updates. Thus, they should be used in conjunction with a constant NVE integration fix such as these:
:::

- [[fix nve]{.doc}]fix_nve.md){.reference .internal}

- [[fix nve/sphere]{.doc}]fix_nve_sphere.md){.reference .internal}

- [[fix nve/asphere]{.doc}]fix_nve_asphere.md){.reference .internal}

Thermodynamic output, which can be setup via the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command, often includes temperature values. As explained on the page for the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command, the default temperature is setup by the thermo command itself. It is NOT the temperature associated with any thermostatting fix you have defined or with any compute you have defined that calculates a temperature. The doc pages for the thermostatting fixes explain the ID of the temperature compute they create. Thus if you want to view these temperatures, you need to specify them explicitly via the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command. Or you can use the [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} command to re-define what temperature compute is used for default thermodynamic output.

------------------------------------------------------------------------

**(Daivis and Todd)** Daivis and Todd, Nonequilibrium Molecular Dynamics (book), Cambridge University Press, [https://doi.org/10.1017/9781139017848](https://doi.org/10.1017/9781139017848){.reference .external}, (2017).
:::::
::::::
:::::::

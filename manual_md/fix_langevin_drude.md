::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::::: {#fix-langevin-drude-command .section}
[]{#index-0}

# fix langevin/drude command[](#fix-langevin-drude-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID langevin/drude Tcom damp_com seed_com Tdrude damp_drude seed_drude keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- langevin/drude = style name of this fix command

- Tcom = desired temperature of the centers of mass (temperature units)

- damp_com = damping parameter for the thermostat on centers of mass (time units)

- seed_com = random number seed to use for white noise of the thermostat on centers of mass (positive integer)

- Tdrude = desired temperature of the Drude oscillators (temperature units)

- damp_drude = damping parameter for the thermostat on Drude oscillators (time units)

- seed_drude = random number seed to use for white noise of the thermostat on Drude oscillators (positive integer)

- zero or more keyword/value pairs may be appended

- keyword = *zero*

  ``` literal-block
  zero value = no or yes
    no = do not set total random force on centers of mass to zero
    yes = set total random force on centers of mass to zero
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 3 all langevin/drude 300.0 100.0 19377 1.0 20.0 83451
    fix 1 all langevin/drude 298.15 100.0 19377 5.0 10.0 83451 zero yes
:::
::::

Example input scripts available: examples/PACKAGES/drude
:::::

:::::::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply two Langevin thermostats as described in [[(Jiang1)]{.std .std-ref}](#jiang1){.reference .internal} for thermalizing the reduced degrees of freedom of Drude oscillators. This link describes how to use the [[thermalized Drude oscillator model]{.doc}]Howto_drude.md){.reference .internal} in LAMMPS and polarizable models in LAMMPS are discussed on the [[Howto polarizable]{.doc}]Howto_polarizable.md){.reference .internal} doc page.

Drude oscillators are a way to simulate polarizables atoms, by splitting them into a core and a Drude particle bound by a harmonic bond. The thermalization works by transforming the particles degrees of freedom by these equations. In these equations upper case denotes atomic or center of mass values and lower case denotes Drude particle or dipole values. Primes denote the transformed (reduced) values, while bare letters denote the original values.

Velocities:

::: {.math .notranslate .nohighlight}
\\\[V\' = \\frac {M\\, V + m\\, v} {M\'}\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[v\' = v - V\\\]
:::

Masses:

::: {.math .notranslate .nohighlight}
\\\[M\' = M + m\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[m\' = \\frac {M\\, m } {M\'}\\\]
:::

The Langevin forces are computed as

::: {.math .notranslate .nohighlight}
\\\[F\' = - \\frac {M\'} {\\mathtt{damp_com}}\\, V\' + F_r\'\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[f\' = - \\frac {m\'} {\\mathtt{damp_drude}}\\, v\' + f_r\'\\\]
:::

[\\(F_r\'\\)]{.math .notranslate .nohighlight} is a random force proportional to [\\(\\sqrt { \\frac {2\\, k_B \\mathtt{Tcom}\\, m\'} {\\mathrm dt\\, \\mathtt{damp_com} } }\\)]{.math .notranslate .nohighlight}. [\\(f_r\'\\)]{.math .notranslate .nohighlight} is a random force proportional to [\\(\\sqrt { \\frac {2\\, k_B \\mathtt{Tdrude}\\, m\'} {\\mathrm dt\\, \\mathtt{damp_drude} } }\\)]{.math .notranslate .nohighlight}. Then the real forces acting on the particles are computed from the inverse transform:

::: {.math .notranslate .nohighlight}
\\\[F = \\frac M {M\'}\\, F\' - f\'\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[f = \\frac m {M\'}\\, F\' + f\'\\\]
:::

This fix also thermostats non-polarizable atoms in the group at temperature *Tcom*, as if they had a massless Drude partner. The Drude particles themselves need not be in the group. The center of mass and the dipole are thermostatted iff the core atom is in the group.

Note that the thermostat effect of this fix is applied to only the translational degrees of freedom of the particles, which is an important consideration if finite-size particles, which have rotational degrees of freedom, are being thermostatted. The translational degrees of freedom can also have a bias velocity removed from them before thermostatting takes place; see the description below.

::: {.admonition .note}
Note

Like the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} command, this fix does NOT perform time integration. It only modifies forces to effect thermostatting. Thus you must use a separate time integration fix, like [[fix nve]{.doc}]fix_nve.md){.reference .internal} or [[fix nph]{.doc}]fix_nh.md){.reference .internal} to actually update the velocities and positions of atoms using the modified forces. Likewise, this fix should not normally be used on atoms that also have their temperature controlled by another fix - e.g. by [[fix nvt]{.doc}]fix_nh.md){.reference .internal} or [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal} commands.
:::

See the [[Howto thermostat]{.doc}]Howto_thermostat.md){.reference .internal} page for a discussion of different ways to compute temperature and perform thermostatting.

------------------------------------------------------------------------

This fix requires each atom know whether it is a Drude particle or not. You must therefore use the [[fix drude]{.doc}]fix_drude.md){.reference .internal} command to specify the Drude status of each atom type.

::: {.admonition .note}
Note

only the Drude core atoms need to be in the group specified for this fix. A Drude electron will be transformed together with its cores even if it is not itself in the group. It is safe to include Drude electrons or non-polarizable atoms in the group. The non-polarizable atoms will simply be thermostatted as if they had a massless Drude partner (electron).
:::

::: {.admonition .note}
Note

Ghost atoms need to know their velocity for this fix to act correctly. You must use the [[comm_modify]{.doc}]comm_modify.md){.reference .internal} command to enable this, e.g.
:::

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    comm_modify vel yes
:::
::::

------------------------------------------------------------------------

*Tcom* is the target temperature of the centers of mass, which would be used to thermostat the non-polarizable atoms. *Tdrude* is the (normally low) target temperature of the core-Drude particle pairs (dipoles). *Tcom* and *Tdrude* can be specified as an equal-style [[variable]{.doc}]variable.md){.reference .internal}. If the value is a variable, it should be specified as v_name, where name is the variable name. In this case, the variable will be evaluated each timestep, and its value used to determine the target temperature.

Equal-style variables can specify formulas with various mathematical functions, and include [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command keywords for the simulation box parameters and timestep and elapsed time. Thus it is easy to specify a time-dependent temperature.

Like other fixes that perform thermostatting, this fix can be used with [[compute commands]{.doc}]compute.md){.reference .internal} that remove a "bias" from the atom velocities. E.g. to apply the thermostat only to atoms within a spatial [[region]{.doc}]region.md){.reference .internal}, or to remove the center-of-mass velocity from a group of atoms, or to remove the x-component of velocity from the calculation.

This is not done by default, but only if the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command is used to assign a temperature compute to this fix that includes such a bias term. See the doc pages for individual [[compute temp commands]{.doc}]compute.md){.reference .internal} to determine which ones include a bias. In this case, the thermostat works in the following manner: bias is removed from each atom, thermostatting is performed on the remaining thermal degrees of freedom, and the bias is added back in.

Note: The temperature thermostatting the core-Drude particle pairs should be chosen low enough, so as to mimic as closely as possible the self-consistent minimization. It must however be high enough, so that the dipoles can follow the local electric field exerted by the neighboring atoms. The optimal value probably depends on the temperature of the centers of mass and on the mass of the Drude particles.

*damp_com* is the characteristic time for reaching thermal equilibrium of the centers of mass. For example, a value of 100.0 means to relax the temperature of the centers of mass in a timespan of (roughly) 100 time units (tau or fs or ps - see the [[units]{.doc}]units.md){.reference .internal} command). *damp_drude* is the characteristic time for reaching thermal equilibrium of the dipoles. It is typically a few timesteps.

The number *seed_com* and *seed_drude* are positive integers. They set the seeds of the Marsaglia random number generators used for generating the random forces on centers of mass and on the dipoles. Each processor uses the input seed to generate its own unique seed and its own stream of random numbers. Thus the dynamics of the system will not be identical on two runs on different numbers of processors.

The keyword *zero* can be used to eliminate drift due to the thermostat on centers of mass. Because the random forces on different centers of mass are independent, they do not sum exactly to zero. As a result, this fix applies a small random force to the entire system, and the momentum of the total center of mass of the system undergoes a slow random walk. If the keyword *zero* is set to *yes*, the total random force on the centers of mass is set exactly to zero by subtracting off an equal part of it from each center of mass in the group. As a result, the total center of mass of a system with zero initial momentum will not drift over time.

The actual temperatures of cores and Drude particles, in center-of-mass and relative coordinates, respectively, can be calculated using the [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal} command.

------------------------------------------------------------------------

Usage example for rigid bodies in the NPT ensemble:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    comm_modify vel yes
    fix TEMP all langevin/drude 300. 100. 1256 1. 20. 13977 zero yes
    fix NPH ATOMS rigid/nph/small molecule iso 1. 1. 500.
    fix NVE DRUDES nve
    compute TDRUDE all temp/drude
    thermo_style custom step cpu etotal ke pe ebond ecoul elong press vol temp c_TDRUDE[1] c_TDRUDE[2]
:::
::::

Comments:

- Drude particles should not be in the rigid group, otherwise the Drude oscillators will be frozen and the system will lose its polarizability.

- *zero yes* avoids a drift of the center of mass of the system, but is a bit slower.

- Use two different random seeds to avoid unphysical correlations.

- Temperature is controlled by the fix *langevin/drude*, so the time-integration fixes do not thermostat. Don't forget to time-integrate both cores and Drude particles.

- Pressure is time-integrated only once by using *nve* for Drude particles and *nph* for atoms/cores (or vice versa). Do not use *nph* for both.

- The temperatures of cores and Drude particles are calculated by [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal}

- Contrary to the alternative thermostatting using Nose-Hoover thermostat fix *npt* and [[fix drude/transform]{.doc}]fix_drude_transform.md){.reference .internal}, the *fix_modify* command is not required here, because the fix *nph* computes the global pressure even if its group is *ATOMS*. This is what we want. If we thermostatted *ATOMS* using *npt*, the pressure should be the global one, but the temperature should be only that of the cores. That's why the command *fix_modify* should be called in that case.
::::::::::::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. Because the state of the random number generator is not saved in restart files, this means you cannot do "exact" restarts with this fix, where the simulation continues on the same as if no restart had taken place. However, in a statistical sense, a restarted simulation should produce the same behavior.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* option is supported by this fix. You can use it to assign a temperature [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its thermostatting procedure, as described above. For consistency, the group used by the compute should include the group of this fix and the Drude particles.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, [[fix drude]{.doc}]fix_drude.md){.reference .internal}, [[fix drude/transform]{.doc}]fix_drude_transform.md){.reference .internal}, [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal}, [[pair_style thole]{.doc}]pair_thole.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are zero = no.

------------------------------------------------------------------------

**(Jiang1)** Jiang, Hardy, Phillips, MacKerell, Schulten, and Roux, J Phys Chem Lett, 2, 87-92 (2011).
:::
:::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::

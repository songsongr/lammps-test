:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-qtb-command .section}
[]{#index-0}

# fix qtb command[](#fix-qtb-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID qtb keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- qtb = style name of this fix

- zero or more keyword/value pairs may be appended

- keyword = *temp* or *damp* or *seed* or *f_max* or *N_f*

  ``` literal-block
  temp value = target quantum temperature (temperature units)
  damp value = damping parameter (time units) inverse of friction gamma
  seed value = random number seed (positive integer)
  f_max value = upper cutoff frequency of the vibration spectrum (1/time units)
  N_f value = number of frequency bins (positive integer)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # (liquid methane modeled with the REAX force field, real units)
    fix 1 all nve
    fix 1 all qtb temp 110 damp 200 seed 35082 f_max 0.3 N_f 100
    # (quartz modeled with the BKS force field, metal units)
    fix 2 all nph iso 1.01325 1.01325 1
    fix 2 all qtb temp 300 damp 1 seed 47508 f_max 120.0 N_f 100
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command performs the quantum thermal bath scheme proposed by [[(Dammak)]{.std .std-ref}](#dammak){.reference .internal} to include self-consistent quantum nuclear effects, when used in conjunction with the [[fix nve]{.doc}]fix_nve.md){.reference .internal} or [[fix nph]{.doc}]fix_nh.md){.reference .internal} commands.

Classical molecular dynamics simulation does not include any quantum nuclear effect. Quantum treatment of the vibrational modes will introduce zero point energy into the system, alter the energy power spectrum and bias the heat capacity from the classical limit. Missing all the quantum nuclear effects, classical MD cannot model systems at temperatures lower than their classical limits. This effect is especially important for materials with a large population of hydrogen atoms and thus higher classical limits.

The equation of motion implemented by this command follows a Langevin form:

::: {.math .notranslate .nohighlight}
\\\[m_i a_i = f_i + R_i - m_i\\gamma v_i\\\]
:::

Here [\\(m_i, a_i, f_i, R_i, \\gamma, \\textrm{and} v_i\\)]{.math .notranslate .nohighlight} represent in this order mass, acceleration, force exerted by all other atoms, random force, frictional coefficient (the inverse of damping parameter damp), and velocity. The random force [\\(R_i\\)]{.math .notranslate .nohighlight} is "colored" so that any vibrational mode with frequency [\\(\\omega\\)]{.math .notranslate .nohighlight} will have a temperature-sensitive energy [\\(\\theta(\\omega,T)\\)]{.math .notranslate .nohighlight} which resembles the energy expectation for a quantum harmonic oscillator with the same natural frequency:

::: {.math .notranslate .nohighlight}
\\\[\\theta(\\omega T) = \\frac{\\hbar}{2} + \\hbar\\omega \\left\[\\exp(\\frac{\\hbar\\omega}{k_B T})-1 \\right\]\^{-1}\\\]
:::

To efficiently generate the random forces, we employ the method of [[(Barrat)]{.std .std-ref}](#barrat){.reference .internal}, that circumvents the need to generate all random forces for all times before the simulation. The memory requirement of this approach is less demanding and independent of the simulation duration. Since the total random force [\\(R\_{tot}\\)]{.math .notranslate .nohighlight} does not necessarily vanish for a finite number of atoms, [\\(R_i\\)]{.math .notranslate .nohighlight} is replaced by [\\(R_i - \\frac{R\_{tot}}{N\_{tot}}\\)]{.math .notranslate .nohighlight} to avoid collective motion of the system.

The *temp* parameter sets the target quantum temperature. LAMMPS will still have an output temperature in its thermo style. That is the instantaneous classical temperature [\\(T\^{cl}\\)]{.math .notranslate .nohighlight} derived from the atom velocities at thermal equilibrium. A non-zero [\\(T\^{cl}\\)]{.math .notranslate .nohighlight} will be present even when the quantum temperature approaches zero. This is associated with zero-point energy at low temperatures.

::: {.math .notranslate .nohighlight}
\\\[T\^{cl} = \\sum \\frac{m_i v_i\^2}{3 N k_B}\\\]
:::

The *damp* parameter is specified in time units, and it equals the inverse of the frictional coefficient [\\(\\gamma\\)]{.math .notranslate .nohighlight}. [\\(\\gamma\\)]{.math .notranslate .nohighlight} should be as small as possible but slightly larger than the timescale of anharmonic coupling in the system which is about 10 ps to 100 ps. When [\\(\\gamma\\)]{.math .notranslate .nohighlight} is too large, it gives an energy spectrum that differs from the desired Bose-Einstein spectrum. When [\\(\\gamma\\)]{.math .notranslate .nohighlight} is too small, the quantum thermal bath coupling to the system will be less significant than anharmonic effects, reducing to a classical limit. We find that setting [\\(\\gamma\\)]{.math .notranslate .nohighlight} between 5 THz and 1 THz could be appropriate depending on the system.

The random number *seed* is a positive integer used to initiate a Marsaglia random number generator. Each processor uses the input seed to generate its own unique seed and its own stream of random numbers. Thus the dynamics of the system will not be identical on two runs on different numbers of processors.

The *f_max* parameter truncate the noise frequency domain so that vibrational modes with frequencies higher than *f_max* will not be modulated. If we denote [\\(\\Delta t\\)]{.math .notranslate .nohighlight} as the time interval for the MD integration, *f_max* is always reset by the code to make [\\(\\alpha = (int)(2\\)]{.math .notranslate .nohighlight} *f_max* [\\(\\Delta t)\^{-1}\\)]{.math .notranslate .nohighlight} a positive integer and print out relative information. An appropriate value for the cutoff frequency *f_max* would be around 2\~3 [\\(f_D\\)]{.math .notranslate .nohighlight}, where [\\(f_D\\)]{.math .notranslate .nohighlight} is the Debye frequency.

The *N_f* parameter is the frequency grid size, the number of points from 0 to *f_max* in the frequency domain that will be sampled. 3\*2*N_f* per-atom random numbers are required in the random force generation and there could be as many atoms as in the whole simulation that can migrate into every individual processor. A larger *N_f* provides a more accurate sampling of the spectrum while consumes more memory. With fixed *f_max* and [\\(\\gamma\\)]{.math .notranslate .nohighlight}, *N_f* should be big enough to converge the classical temperature [\\(T\^{cl}\\)]{.math .notranslate .nohighlight} as a function of target quantum bath temperature. Memory usage per processor could be from 10 to 100 MBytes.

::: {.admonition .note}
Note

Unlike the [[fix nvt]{.doc}]fix_nh.md){.reference .internal} command which performs Nose/Hoover thermostatting AND time integration, this fix does NOT perform time integration. It only modifies forces to a colored thermostat. Thus you must use a separate time integration fix, like [[fix nve]{.doc}]fix_nve.md){.reference .internal} or [[fix nph]{.doc}]fix_nh.md){.reference .internal} to actually update the velocities and positions of atoms (as shown in the examples). Likewise, this fix should not normally be used with other fixes or commands that also specify system temperatures , e.g. [[fix nvt]{.doc}]fix_nh.md){.reference .internal} and [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}.
:::
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. Because the state of the random number generator is not saved in restart files, this means you cannot do "exact" restarts with this fix. However, in a statistical sense, a restarted simulation should produce similar behaviors of the system.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix style is part of the QTB package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

------------------------------------------------------------------------

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nve]{.doc}]fix_nve.md){.reference .internal}, [[fix nph]{.doc}]fix_nh.md){.reference .internal}, [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, [[fix qbmsst]{.doc}]fix_qbmsst.md){.reference .internal}
:::

------------------------------------------------------------------------

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The keyword defaults are temp = 300, damp = 1, seed = 880302, f_max=200.0 and N_f = 100.

------------------------------------------------------------------------

**(Dammak)** Dammak, Chalopin, Laroche, Hayoun, and Greffet, Phys Rev Lett, 103, 190601 (2009).

**(Barrat)** Barrat and Rodney, J. Stat. Phys, 144, 679 (2011).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

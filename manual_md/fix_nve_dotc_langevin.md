::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-nve-dotc-langevin-command .section}
[]{#index-0}

# fix nve/dotc/langevin command[](#fix-nve-dotc-langevin-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nve/dotc/langevin Tstart Tstop damp seed keyword value
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nve/dotc/langevin = style name of this fix command

- Tstart,Tstop = desired temperature at start/end of run (temperature units)

- damp = damping parameter (time units)

- seed = random number seed to use for white noise (positive integer)

- keyword = *angmom*

  ``` literal-block
  angmom value = factor
    factor = do thermostat rotational degrees of freedom via the angular momentum and apply numeric scale factor as discussed below
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nve/dotc/langevin 1.0 1.0 0.03 457145 angmom 10
    fix 1 all nve/dotc/langevin 0.1 0.1 78.9375 457145 angmom 10
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply a rigid-body Langevin-type integrator of the kind "Langevin C" as described in [[(Davidchack)]{.std .std-ref}](#davidchack5){.reference .internal} to a group of atoms, which models an interaction with an implicit background solvent. This command performs Brownian dynamics (BD) via a technique that splits the integration into a deterministic Hamiltonian part and the Ornstein-Uhlenbeck process for noise and damping. The quaternion degrees of freedom are updated though an evolution operator which performs a rotation in quaternion space, preserves the quaternion norm and is akin to [[(Miller)]{.std .std-ref}](#miller5){.reference .internal}.

In terms of syntax this command has been closely modelled on the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} and its *angmom* option. But it combines the [[fix nve]{.doc}]fix_nve.md){.reference .internal} and the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} in one single command. The main feature is improved stability over the standard integrator, permitting slightly larger timestep sizes.

::: {.admonition .note}
Note

Unlike the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} this command performs also time integration of the translational and quaternion degrees of freedom.
:::

The total force on each atom will have the form:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}F = & F_c + F_f + F_r \\\\ F_f = & - \\frac{m}{\\mathrm{damp}} v \\\\ F_r \\propto & \\sqrt{\\frac{k_B T m}{dt\~\\mathrm{damp}}}\\end{split}\\\]
:::

[\\(F_c\\)]{.math .notranslate .nohighlight} is the conservative force computed via the usual inter-particle interactions ([[pair_style]{.doc}]pair_style.md){.reference .internal}, [[bond_style]{.doc}]bond_style.md){.reference .internal}, etc). The [\\(F_f\\)]{.math .notranslate .nohighlight} and [\\(F_r\\)]{.math .notranslate .nohighlight} terms are implicitly taken into account by this fix on a per-particle basis.

[\\(F_f\\)]{.math .notranslate .nohighlight} is a frictional drag or viscous damping term proportional to the particle's velocity. The proportionality constant for each atom is computed as [\\(\\frac{m}{\\mathrm{damp}}\\)]{.math .notranslate .nohighlight}, where *m* is the mass of the particle and damp is the damping factor specified by the user.

[\\(F_r\\)]{.math .notranslate .nohighlight} is a force due to solvent atoms at a temperature [\\(T\\)]{.math .notranslate .nohighlight} randomly bumping into the particle. As derived from the fluctuation/dissipation theorem, its magnitude as shown above is proportional to [\\(\\sqrt{\\frac{k_B T m}{dt\~\\mathrm{damp}}}\\)]{.math .notranslate .nohighlight}, where [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant, [\\(T\\)]{.math .notranslate .nohighlight} is the desired temperature, *m* is the mass of the particle, *dt* is the timestep size, and damp is the damping factor. Random numbers are used to randomize the direction and magnitude of this force as described in [[(Dunweg)]{.std .std-ref}](#dunweg5){.reference .internal}, where a uniform random number is used (instead of a Gaussian random number) for speed.

------------------------------------------------------------------------

*Tstart* and *Tstop* have to be constant values, i.e. they cannot be variables. If used together with the oxDNA force field for coarse-grained simulation of DNA please note that T = 0.1 in oxDNA units corresponds to T = 300 K.

The *damp* parameter is specified in time units and determines how rapidly the temperature is relaxed. For example, a value of 0.03 means to relax the temperature in a timespan of (roughly) 0.03 time units [\\(\\tau\\)]{.math .notranslate .nohighlight} (see the [[units]{.doc}]units.md){.reference .internal} command). The damp factor can be thought of as inversely related to the viscosity of the solvent, i.e. a small relaxation time implies a high-viscosity solvent and vice versa. See the discussion about gamma and viscosity in the documentation for the [[fix viscous]{.doc}]fix_viscous.md){.reference .internal} command for more details. Note that the value 78.9375 in the second example above corresponds to a diffusion constant, which is about an order of magnitude larger than realistic ones. This has been used to sample configurations faster in Brownian dynamics simulations.

The random \# *seed* must be a positive integer. A Marsaglia random number generator is used. Each processor uses the input seed to generate its own unique seed and its own stream of random numbers. Thus the dynamics of the system will not be identical on two runs on different numbers of processors.

The keyword/value option has to be used in the following way:

This fix has to be used together with the *angmom* keyword. The particles are always considered to have a finite size. The keyword *angmom* enables thermostatting of the rotational degrees of freedom in addition to the usual translational degrees of freedom.

The scale factor after the *angmom* keyword gives the ratio of the rotational to the translational friction coefficient.

An example input file can be found in examples/PACKAGES/cgdna/examples/duplex2/. Further details of the implementation and stability of the integrators are contained in [[(Henrich)]{.std .std-ref}](#henrich5){.reference .internal}. The preprint version of the article can be found [here](PDF/CG-DNA.pdf){.reference .external}.
:::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles can only be used if LAMMPS was built with the [[CG-DNA]{.std .std-ref}]Packages_details.md#pkg-cg-dna){.reference .internal} package and the MOLECULE and ASPHERE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nve]{.doc}]fix_nve.md){.reference .internal}, [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, [[fix nve/dot]{.doc}]fix_nve_dot.md){.reference .internal}, [[bond_style oxdna/fene]{.doc}]bond_oxdna.md){.reference .internal}, [[bond_style oxdna2/fene]{.doc}]bond_oxdna.md){.reference .internal}, [[pair_style oxdna/excv]{.doc}]pair_oxdna.md){.reference .internal}, [[pair_style oxdna2/excv]{.doc}]pair_oxdna2.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Davidchack)** R.L Davidchack, T.E. Ouldridge, M.V. Tretyakov. J. Chem. Phys. 142, 144114 (2015).

**(Miller)** T. F. Miller III, M. Eleftheriou, P. Pattnaik, A. Ndirango, G. J. Martyna, J. Chem. Phys., 116, 8649-8659 (2002).

**(Dunweg)** B. Dunweg, W. Paul, Int. J. Mod. Phys. C, 2, 817-27 (1991).

**(Henrich)** O. Henrich, Y. A. Gutierrez-Fosado, T. Curk, T. E. Ouldridge, Eur. Phys. J. E 41, 57 (2018).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

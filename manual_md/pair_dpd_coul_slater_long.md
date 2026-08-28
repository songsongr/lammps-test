::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#pair-style-dpd-coul-slater-long-command .section}
[]{#index-1}[]{#index-0}

# pair_style dpd/coul/slater/long command[](#pair-style-dpd-coul-slater-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *dpd/coul/slater/long/gpu*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dpd/coul/slater/long T cutoff_DPD seed lambda cutoff_coul
:::
::::

- T = temperature (temperature units)

- cutoff_DPD = global cutoff for DPD interactions (distance units)

- seed = random \# seed (positive integer)

- lambda = decay length of the charge (distance units)

- cutoff_coul = global cutoff for Coulombic interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dpd/coul/slater/long 1.0 2.5 34387 0.25 3.0

    pair_coeff 1 1 78.0 4.5          # not charged by default
    pair_coeff 2 2 78.0 4.5 yes
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 27June2024.]{.versionmodified .added}
:::

Style *dpd/coul/slater/long* computes a force field for dissipative particle dynamics (DPD) following the exposition in [[(Groot)]{.std .std-ref}](#groot5){.reference .internal}. It also allows for the use of charged particles in the model by adding a long-range Coulombic term to the DPD interactions. The short-range portion of the Coulombics is calculated by this pair style. The long-range Coulombics are computed by use of the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command, e.g. using the Ewald or PPPM styles.

Coulombic forces in mesoscopic models such as DPD employ potentials without explicit excluded-volume interactions. The goal is to prevent artificial ionic pair formation by including a charge distribution in the Coulomb potential, following the formulation in [[(Melchor1)]{.std .std-ref}](#melchor1){.reference .internal}.

::: {.admonition .note}
Note

This pair style is effectively the combination of the [[pair_style dpd]{.doc}]pair_dpd.md){.reference .internal} and [[pair_style coul/slater/long]{.doc}]pair_coul_slater.md){.reference .internal} commands, but should be more efficient (especially on GPUs) than using [[pair_style hybrid/overlay dpd coul/slater/long]{.doc}]pair_hybrid.md){.reference .internal}. That is particularly true for the GPU package version of the pair style since this version is compatible with computing neighbor lists on the GPU instead of the CPU as is required for hybrid styles.
:::

In the charged DPD model, the force on bead I due to bead J is given as a sum of 4 terms:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\vec{f} = & (F\^C + F\^D + F\^R + F\^E) \\hat{r\_{ij}} \\\\ F\^C = & A w(r) \\qquad \\qquad \\qquad \\qquad \\qquad r \< r\_{DPD} \\\\ F\^D = & - \\gamma w\^2(r) (\\hat{r\_{ij}} \\bullet \\vec{v}\_{ij}) \\qquad \\qquad r \< r\_{DPD} \\\\ F\^R = & \\sigma w(r) \\alpha (\\Delta t)\^{-1/2} \\qquad \\qquad \\qquad r \< r\_{DPD} \\\\ w(r) = & 1 - \\frac{r}{r\_{DPD}} \\\\ F\^E = & \\frac{C q_iq_j}{\\epsilon r\^2} \\left( 1- exp\\left( \\frac{2r\_{ij}}{\\lambda} \\right) \\left( 1 + \\frac{2r\_{ij}}{\\lambda} \\left( 1 + \\frac{r\_{ij}}{\\lambda} \\right)\\right) \\right)\\end{split}\\\]
:::

where [\\(F\^C\\)]{.math .notranslate .nohighlight} is a conservative force, [\\(F\^D\\)]{.math .notranslate .nohighlight} is a dissipative force, [\\(F\^R\\)]{.math .notranslate .nohighlight} is a random force, and [\\(F\^E\\)]{.math .notranslate .nohighlight} is an electrostatic force. [\\(\\hat{r\_{ij}}\\)]{.math .notranslate .nohighlight} is a unit vector in the direction [\\(r_i - r_j\\)]{.math .notranslate .nohighlight}, [\\(\\vec{v}\_{ij}\\)]{.math .notranslate .nohighlight} is the vector difference in velocities of the two atoms [\\(\\vec{v}\_i - \\vec{v}\_j\\)]{.math .notranslate .nohighlight}, [\\(\\alpha\\)]{.math .notranslate .nohighlight} is a Gaussian random number with zero mean and unit variance, *dt* is the timestep size, and [\\(w(r)\\)]{.math .notranslate .nohighlight} is a weighting factor that varies between 0 and 1.

[\\(\\sigma\\)]{.math .notranslate .nohighlight} is set equal to [\\(\\sqrt{2 k_B T \\gamma}\\)]{.math .notranslate .nohighlight}, where [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant and *T* is the temperature parameter in the pair_style command.

[\\(r\_{DPD}\\)]{.math .notranslate .nohighlight} is the pairwise cutoff for the first 3 DPD terms in the formula as specified by *cutoff_DPD*. For the [\\(F\^E\\)]{.math .notranslate .nohighlight} term, pairwise interactions within the specified *cutoff_coul* distance are computed directly; interactions beyond that distance are computed in reciprocal space. *C* is the same Coulomb conversion factor used in the Coulombic formulas described on the [[pair_coul]{.doc}]pair_coul.md){.reference .internal} doc page.

The following parameters must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- A (force units)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

- is_charged (optional boolean, default = no)

The *is_charged* parameter is optional and can be specified as *yes* or *no*. *Yes* should be used for interactions between two types of charged particles. *No* is the default and should be used for interactions between two types of particles when one or both are uncharged.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file. Note that the user-specified random number seed is stored in the restart file, so when a simulation is restarted, each processor will re-initialize its random number generator the same way it did initially. This means the random forces will be random, but will not be the same as they would have been if the original simulation had continued past the restart time.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This style is part of the DPD-BASIC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The default frequency for rebuilding neighbor lists is every 10 steps (see the [[neigh_modify]{.doc}]neigh_modify.md){.reference .internal} command). This may be too infrequent since particles move rapidly and can overlap by large amounts. If this setting yields a non-zero number of "dangerous" reneighborings (printed at the end of a simulation), you should experiment with forcing reneighboring more often and see if system energies/trajectories change.

This pair style requires use of the [[comm_modify vel yes]{.doc}]comm_modify.md){.reference .internal} command so that velocities are stored by ghost atoms.

This pair style also requires use of a long-range solvers from the KSPACE package.

This pair style will not restart exactly when using the [[read_restart]{.doc}]read_restart.md){.reference .internal} command, though they should provide statistically similar results. This is because the forces they compute depend on atom velocities. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for more details.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style dpd]{.doc}]pair_dpd.md){.reference .internal}, [[pair_style coul/slater/long]{.doc}]pair_coul_slater.md){.reference .internal},
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

For the pair_coeff command, the default is is_charged = no.

------------------------------------------------------------------------

**(Groot)** Groot and Warren, J Chem Phys, 107, 4423-35 (1997).

**(Melchor)** Gonzalez-Melchor, Mayoral, Velazquez, and Alejandre, J Chem Phys, 125, 224107 (2006).
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

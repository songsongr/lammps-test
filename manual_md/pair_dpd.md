::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-dpd-command .section}
[]{#index-8}[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style dpd command[](#pair-style-dpd-command "Link to this heading"){.headerlink}

Accelerator Variants: *dpd/gpu*, *dpd/intel*, *dpd/kk*, *dpd/omp*
:::

:::::::::::::::::: {#pair-style-dpd-tstat-command .section}
# pair_style dpd/tstat command[](#pair-style-dpd-tstat-command "Link to this heading"){.headerlink}

Accelerator Variants: *dpd/tstat/gpu*, *dpd/tstat/kk*, *dpd/tstat/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dpd T cutoff seed
    pair_style dpd/tstat Tstart Tstop cutoff seed
:::
::::

- T = temperature (temperature units) (dpd only)

- Tstart,Tstop = desired temperature at start/end of run (temperature units) (dpd/tstat only)

- cutoff = global cutoff for DPD interactions (distance units)

- seed = random \# seed (positive integer)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dpd 1.0 2.5 34387
    pair_coeff * * 3.0 1.0
    pair_coeff 1 1 3.0 1.0 1.0

    pair_style hybrid/overlay lj/cut 2.5 dpd/tstat 1.0 1.0 2.5 34387
    pair_coeff * * lj/cut 1.0 1.0
    pair_coeff * * dpd/tstat 1.0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *dpd* computes a force field for dissipative particle dynamics (DPD) following the exposition in [[(Groot)]{.std .std-ref}](#groot1){.reference .internal}.

Style *dpd/tstat* invokes a DPD thermostat on pairwise interactions, which is equivalent to the non-conservative portion of the DPD force field. This pairwise thermostat can be used in conjunction with any [[pair style]{.doc}]pair_style.md){.reference .internal}, and instead of per-particle thermostats like [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} or ensemble thermostats like Nose Hoover as implemented by [[fix nvt]{.doc}]fix_nh.md){.reference .internal}. To use *dpd/tstat* as a thermostat for another pair style, use the [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} command to compute both the desired pair interaction and the thermostat for each pair of particles.

For style *dpd*, the force on atom I due to atom J is given as a sum of 3 terms

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\vec{f} = & (F\^C + F\^D + F\^R) \\hat{r\_{ij}} \\qquad \\qquad r \< r_c \\\\ F\^C = & A w(r) \\\\ F\^D = & - \\gamma w\^2(r) (\\hat{r\_{ij}} \\bullet \\vec{v}\_{ij}) \\\\ F\^R = & \\sigma w(r) \\alpha (\\Delta t)\^{-1/2} \\\\ w(r) = & 1 - \\frac{r}{r_c}\\end{split}\\\]
:::

where [\\(F\^C\\)]{.math .notranslate .nohighlight} is a conservative force, [\\(F\^D\\)]{.math .notranslate .nohighlight} is a dissipative force, and [\\(F\^R\\)]{.math .notranslate .nohighlight} is a random force. [\\(\\hat{r\_{ij}}\\)]{.math .notranslate .nohighlight} is a unit vector in the direction [\\(r_i - r_j\\)]{.math .notranslate .nohighlight}, [\\(\\vec{v}\_{ij}\\)]{.math .notranslate .nohighlight} is the vector difference in velocities of the two atoms [\\(\\vec{v}\_i - \\vec{v}\_j\\)]{.math .notranslate .nohighlight}, [\\(\\alpha\\)]{.math .notranslate .nohighlight} is a Gaussian random number with zero mean and unit variance, *dt* is the timestep size, and [\\(w(r)\\)]{.math .notranslate .nohighlight} is a weighting factor that varies between 0 and 1. [\\(r_c\\)]{.math .notranslate .nohighlight} is the pairwise cutoff. [\\(\\sigma\\)]{.math .notranslate .nohighlight} is set equal to [\\(\\sqrt{2 k_B T \\gamma}\\)]{.math .notranslate .nohighlight}, where [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant and *T* is the temperature parameter in the pair_style command.

For style *dpd/tstat*, the force on atom I due to atom J is the same as the above equation, except that the conservative [\\(F\^C\\)]{.math .notranslate .nohighlight} term is dropped. Also, during the run, *T* is set each timestep to a ramped value from *Tstart* to *Tstop*.

For style *dpd*, the pairwise energy associated with style *dpd* is only due to the conservative force term [\\(F\^C\\)]{.math .notranslate .nohighlight}, and is shifted to be zero at the cutoff distance [\\(r_c\\)]{.math .notranslate .nohighlight}. The pairwise virial is calculated using all 3 terms. For style *dpd/tstat* there is no pairwise energy, but the last two terms of the formula make a contribution to the virial.

For style *dpd*, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- A (force units)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

- cutoff (distance units)

The cutoff coefficient is optional. If not specified, the global DPD cutoff is used. Note that sigma is set equal to sqrt(2 T gamma), where T is the temperature set by the [[pair_style]{.doc}]pair_style.md){.reference .internal} command so it does not need to be specified.

For style *dpd/tstat*, the coefficients defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command are:

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

- cutoff (distance units)

The cutoff coefficient is optional.

Styles with a *gpu* suffix are implemented based on the work of [[(Afshar)]{.std .std-ref}](#afshar){.reference .internal} and [[(Phillips)]{.std .std-ref}](#phillips){.reference .internal}.

::: {.admonition .note}
Note

If you are modeling DPD polymer chains, you may want to use the [[pair_style srp]{.doc}]pair_srp.md){.reference .internal} command in conjunction with these pair styles. It is a soft segmental repulsive potential (SRP) that can prevent DPD polymer chains from crossing each other.
:::

::: {.admonition .note}
Note

The virial calculation for pressure when using these pair styles includes all the components of force listed above, including the random force. Since the random force depends on random numbers, everything that changes the order of atoms in the neighbor list (e.g. different number of MPI ranks or a different neighbor list skin distance) will also change the sequence in which the random numbers are applied and thus the individual forces and therefore also the virial/pressure.
:::

::: {.admonition .note}
Note

For more consistent time integration and force computation you may consider using [[fix mvv/dpd]{.doc}]fix_mvv_dpd.md){.reference .internal} instead of [[fix nve]{.doc}]fix_nve.md){.reference .internal}.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

These pair styles do not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction. Note that as discussed above, the energy due to the conservative [\\(F\^C\\)]{.math .notranslate .nohighlight} term is already shifted to be 0.0 at the cutoff distance [\\(r_c\\)]{.math .notranslate .nohighlight}.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for these pair styles.

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

These pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file. Note that the user-specified random number seed is stored in the restart file, so when a simulation is restarted, each processor will re-initialize its random number generator the same way it did initially. This means the random forces will be random, but will not be the same as they would have been if the original simulation had continued past the restart time.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.

The *dpd/tstat* style can ramp its target temperature over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These styles are part of the DPD-BASIC package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The default frequency for rebuilding neighbor lists is every 10 steps (see the [[neigh_modify]{.doc}]neigh_modify.md){.reference .internal} command). This may be too infrequent for style *dpd* simulations since particles move rapidly and can overlap by large amounts. If this setting yields a non-zero number of "dangerous" reneighborings (printed at the end of a simulation), you should experiment with forcing reneighboring more often and see if system energies/trajectories change.

These pair styles requires you to use the [[comm_modify vel yes]{.doc}]comm_modify.md){.reference .internal} command so that velocities are stored by ghost atoms.

These pair styles will not restart exactly when using the [[read_restart]{.doc}]read_restart.md){.reference .internal} command, though they should provide statistically similar results. This is because the forces they compute depend on atom velocities. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for more details.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style dpd/ext]{.doc}]pair_dpd_ext.md){.reference .internal}, [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, [[pair_style srp]{.doc}]pair_srp.md){.reference .internal}, [[fix mvv/dpd]{.doc}]fix_mvv_dpd.md){.reference .internal}.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Groot)** Groot and Warren, J Chem Phys, 107, 4423-35 (1997).

**(Afshar)** Afshar, F. Schmid, A. Pishevar, S. Worley, Comput Phys Comm, 184, 1119-1128 (2013).

**(Phillips)** C. L. Phillips, J. A. Anderson, S. C. Glotzer, Comput Phys Comm, 230, 7191-7201 (2011).
:::
::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

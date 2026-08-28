::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-dpd-ext-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style dpd/ext command[](#pair-style-dpd-ext-command "Link to this heading"){.headerlink}

Accelerator Variants: dpd/ext/kk dpd/ext/omp
:::

:::::::::::::::: {#pair-style-dpd-ext-tstat-command .section}
# pair_style dpd/ext/tstat command[](#pair-style-dpd-ext-tstat-command "Link to this heading"){.headerlink}

Accelerator Variants: dpd/ext/tstat/kk dpd/ext/tstat/omp

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dpd/ext T cutoff seed
    pair_style dpd/ext/tstat Tstart Tstop cutoff seed
:::
::::

- T = temperature (temperature units)

- Tstart,Tstop = desired temperature at start/end of run (temperature units)

- cutoff = global cutoff for DPD interactions (distance units)

- seed = random \# seed (positive integer)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dpd/ext 1.0 2.5 34387
    pair_coeff 1 1 25.0 4.5 4.5 0.5 0.5 1.2
    pair_coeff 1 2 40.0 4.5 4.5 0.5 0.5 1.2

    pair_style hybrid/overlay lj/cut 2.5 dpd/ext/tstat 1.0 1.0 2.5 34387
    pair_coeff * * lj/cut 1.0 1.0
    pair_coeff * * 4.5 4.5 0.5 0.5 1.2
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The style *dpd/ext* computes an extended force field for dissipative particle dynamics (DPD) following the exposition in [[(Groot)]{.std .std-ref}](#groot){.reference .internal}, [[(Junghans)]{.std .std-ref}](#junghans){.reference .internal}.

Style *dpd/ext/tstat* invokes an extended DPD thermostat on pairwise interactions, equivalent to the non-conservative portion of the extended DPD force field. To use *dpd/ext/tstat* as a thermostat for another pair style, use the [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} command to compute both the desired pair interaction and the thermostat for each pair of particles.

For the style *dpd/ext*, the force on atom I due to atom J is given as a sum of 3 terms

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathbf{f} = & f\^C + f\^D + f\^R \\qquad \\qquad r \< r_c \\\\ f\^C = & A\_{ij} w(r) \\hat{\\mathbf{r}}\_{ij} \\\\ f\^D = & - \\gamma\_{\\parallel} w\_{\\parallel}\^2(r) (\\hat{\\mathbf{r}}\_{ij} \\cdot \\mathbf{v}\_{ij}) \\hat{\\mathbf{r}}\_{ij} - \\gamma\_{\\perp} w\_{\\perp}\^2 (r) ( \\mathbf{I} - \\hat{\\mathbf{r}}\_{ij} \\hat{\\mathbf{r}}\_{ij}\^\\mathrm{T} ) \\mathbf{v}\_{ij} \\\\ f\^R = & \\sigma\_{\\parallel} w\_{\\parallel}(r) \\frac{\\alpha}{\\sqrt{\\Delta t}} \\hat{\\mathbf{r}}\_{ij} + \\sigma\_{\\perp} w\_{\\perp} (r) ( \\mathbf{I} - \\hat{\\mathbf{r}}\_{ij} \\hat{\\mathbf{r}}\_{ij}\^\\mathrm{T} ) \\frac{\\mathbf{\\xi}\_{ij}}{\\sqrt{\\Delta t}}\\\\ w(r) = & 1 - r/r_c \\\\\\end{split}\\\]
:::

where [\\(\\mathbf{f}\^C\\)]{.math .notranslate .nohighlight} is a conservative force, [\\(\\mathbf{f}\^D\\)]{.math .notranslate .nohighlight} is a dissipative force, and [\\(\\mathbf{f}\^R\\)]{.math .notranslate .nohighlight} is a random force. [\\(A\_{ij}\\)]{.math .notranslate .nohighlight} is the maximum repulsion between the two atoms, [\\(\\hat{\\mathbf{r}}\_{ij}\\)]{.math .notranslate .nohighlight} is a unit vector in the direction [\\(\\mathbf{r}\_i - \\mathbf{r}\_j\\)]{.math .notranslate .nohighlight}, [\\(\\mathbf{v}\_{ij} = \\mathbf{v}\_i - \\mathbf{v}\_j\\)]{.math .notranslate .nohighlight} is the vector difference in velocities of the two atoms, [\\(\\alpha\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{\\xi}\_{ij}\\)]{.math .notranslate .nohighlight} are Gaussian random numbers with zero mean and unit variance, [\\(\\Delta t\\)]{.math .notranslate .nohighlight} is the timestep, [\\(w (r) = 1 - r / r_c\\)]{.math .notranslate .nohighlight} is a weight function for the conservative interactions that varies between 0 and 1, [\\(r_c\\)]{.math .notranslate .nohighlight} is the corresponding cutoff, [\\(w\_{\\alpha} ( r ) = ( 1 - r / \\bar{r}\_c )\^{s\_{\\alpha}}\\)]{.math .notranslate .nohighlight}, [\\(\\alpha \\equiv ( \\parallel, \\perp )\\)]{.math .notranslate .nohighlight}, are weight functions with coefficients [\\(s\_\\alpha\\)]{.math .notranslate .nohighlight} that vary between 0 and 1, [\\(\\bar{r}\_c\\)]{.math .notranslate .nohighlight} is the corresponding cutoff, [\\(\\mathbf{I}\\)]{.math .notranslate .nohighlight} is the unit matrix, [\\(\\sigma\_{\\alpha} = \\sqrt{2 k_B T \\gamma\_{\\alpha}}\\)]{.math .notranslate .nohighlight}, where [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant and [\\(T\\)]{.math .notranslate .nohighlight} is the temperature in the pair_style command.

For the style *dpd/ext/tstat*, the force on atom I due to atom J is the same as the above equation, except that the conservative [\\(\\mathbf{f}\^C\\)]{.math .notranslate .nohighlight} term is dropped. Also, during the run, T is set each timestep to a ramped value from Tstart to Tstop.

For the style *dpd/ext*, the pairwise energy associated with style *dpd/ext* is only due to the conservative force term [\\(\\mathbf{f}\^C\\)]{.math .notranslate .nohighlight}, and is shifted to be zero at the cutoff distance [\\(r_c\\)]{.math .notranslate .nohighlight}. The pairwise virial is calculated using all three terms. There is no pairwise energy for style *dpd/ext/tstat*, but the last two terms of the formula contribute the virial.

For the style *dpd/ext/tstat*, the force on atom I due to atom J is the same as the above equation, except that the conservative [\\(\\mathbf{f}\^C\\)]{.math .notranslate .nohighlight} term is dropped. Also, during the run, T is set each timestep to a ramped value from Tstart to Tstop.

For the style *dpd/ext*, the pairwise energy associated with style *dpd/ext* is only due to the conservative force term [\\(\\mathbf{f}\^C\\)]{.math .notranslate .nohighlight}, and is shifted to be zero at the cutoff distance [\\(r_c\\)]{.math .notranslate .nohighlight}. The pairwise virial is calculated using all three terms. There is no pairwise energy for style *dpd/ext/tstat*, but the last two terms of the formula contribute the virial.

For the style *dpd/ext*, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above:

- A (force units)

- [\\(\\gamma\_{\\parallel}\\)]{.math .notranslate .nohighlight} (force/velocity units)

- [\\(\\gamma\_{\\perp}\\)]{.math .notranslate .nohighlight} (force/velocity units)

- [\\(s\_{\\parallel}\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(s\_{\\perp}\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(r_c\\)]{.math .notranslate .nohighlight} (distance units)

The last coefficient is optional. If not specified, the global DPD cutoff is used. Note that [\\(\\sigma\\)]{.math .notranslate .nohighlight}'s are set equal to [\\(\\sqrt{2 k_B T \\gamma}\\)]{.math .notranslate .nohighlight}, where [\\(T\\)]{.math .notranslate .nohighlight} is the temperature set by the [[pair_style]{.doc}]pair_style.md){.reference .internal} command so it does not need to be specified.

For the style *dpd/ext/tstat*, the coefficients defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command are:

- [\\(\\gamma\_{\\parallel}\\)]{.math .notranslate .nohighlight} (force/velocity units)

- [\\(\\gamma\_{\\perp}\\)]{.math .notranslate .nohighlight} (force/velocity units)

- [\\(s\_{\\parallel}\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(s\_{\\perp}\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(r_c\\)]{.math .notranslate .nohighlight} (distance units)

The last coefficient is optional.

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

------------------------------------------------------------------------

**Mixing, shift, table, tail correction, restart, rRESPA info**:

The style *dpd/ext* does not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

The pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction. Note that as discussed above, the energy due to the conservative [\\(\\mathbf{f}\^C\\)]{.math .notranslate .nohighlight} term is already shifted to be zero at the cutoff distance [\\(r_c\\)]{.math .notranslate .nohighlight}.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for the style *dpd/ext*.

The style *dpd/ext* does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

The pair styles can only be used via the pair keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, and *outer*keywords.

The style *dpd/ext/tstat* can ramp its target temperature over multiple runs, using the start and stop keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.
:::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These styles are part of the DPD-BASIC package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The default frequency for rebuilding neighbor lists is every 10 steps (see the [[neigh_modify]{.doc}]neigh_modify.md){.reference .internal} command). This may be too infrequent for style *dpd/ext* simulations since particles move rapidly and can overlap by large amounts. If this setting yields a non-zero number of say{dangerous} reneighborings (printed at the end of a simulation), you should experiment with forcing reneighboring more often and see if system energies/trajectories change.

The pair styles require to use the [[comm_modify vel yes]{.doc}]comm_modify.md){.reference .internal} command so that velocities are stored by ghost atoms.

The pair styles will not restart exactly when using the [[read_restart]{.doc}]read_restart.md){.reference .internal} command, though they should provide statistically similar results. This is because the forces they compute depend on atom velocities. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for more details.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style dpd]{.doc}]pair_dpd.md){.reference .internal}, [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, [[pair_style srp]{.doc}]pair_srp.md){.reference .internal}, [[fix mvv/dpd]{.doc}]fix_mvv_dpd.md){.reference .internal}.

**Default:** none

------------------------------------------------------------------------

**(Groot)** Groot and Warren, J Chem Phys, 107, 4423-35 (1997).

**(Junghans)** Junghans, Praprotnik and Kremer, Soft Matter 4, 156, 1119-1128 (2008).
:::
::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

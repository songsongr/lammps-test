::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-dpd-fdt-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style dpd/fdt command[](#pair-style-dpd-fdt-command "Link to this heading"){.headerlink}
:::

:::::::::::::::: {#pair-style-dpd-fdt-energy-command .section}
# pair_style dpd/fdt/energy command[](#pair-style-dpd-fdt-energy-command "Link to this heading"){.headerlink}

Accelerator Variants: *dpd/fdt/energy/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *dpd/fdt* or *dpd/fdt/energy*

- args = list of arguments for a particular style

``` literal-block
dpd/fdt args = T cutoff seed
  T = temperature (temperature units)
  cutoff = global cutoff for DPD interactions (distance units)
  seed = random # seed (positive integer)
dpd/fdt/energy args = cutoff seed
  cutoff = global cutoff for DPD interactions (distance units)
  seed = random # seed (positive integer)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dpd/fdt 300.0 2.5 34387
    pair_coeff * * 3.0 1.0 2.5

    pair_style dpd/fdt/energy 2.5 34387
    pair_coeff * * 3.0 1.0 0.1 2.5
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Styles *dpd/fdt* and *dpd/fdt/energy* compute the force for dissipative particle dynamics (DPD) simulations. The *dpd/fdt* style is used to perform DPD simulations under isothermal and isobaric conditions, while the *dpd/fdt/energy* style is used to perform DPD simulations under isoenergetic and isoenthalpic conditions (see [[(Lisal)]{.std .std-ref}](#lisal3){.reference .internal}). For DPD simulations in general, the force on atom I due to atom J is given as a sum of 3 terms

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\vec{f} = & (F\^C + F\^D + F\^R) \\hat{r\_{ij}} \\qquad \\qquad r \< r_c \\\\ F\^C = & A w(r) \\\\ F\^D = & - \\gamma w\^2(r) (\\hat{r\_{ij}} \\bullet \\vec{v}\_{ij}) \\\\ F\^R = & \\sigma w(r) \\alpha (\\Delta t)\^{-1/2} \\\\ w(r) = & 1 - \\frac{r}{r_c}\\end{split}\\\]
:::

where [\\(F\^C\\)]{.math .notranslate .nohighlight} is a conservative force, [\\(F\^D\\)]{.math .notranslate .nohighlight} is a dissipative force, and [\\(F\^R\\)]{.math .notranslate .nohighlight} is a random force. [\\(\\hat{r\_{ij}}\\)]{.math .notranslate .nohighlight} is a unit vector in the direction [\\(r_i - r_j\\)]{.math .notranslate .nohighlight}, [\\(\\vec{v}\_{ij}\\)]{.math .notranslate .nohighlight} is the vector difference in velocities of the two atoms, [\\(\\vec{v}\_i - \\vec{v}\_j\\)]{.math .notranslate .nohighlight}, [\\(\\alpha\\)]{.math .notranslate .nohighlight} is a Gaussian random number with zero mean and unit variance, *dt* is the timestep size, and [\\(w(r)\\)]{.math .notranslate .nohighlight} is a weighting factor that varies between 0 and 1, [\\(r_c\\)]{.math .notranslate .nohighlight} is the pairwise cutoff. Note that alternative definitions of the weighting function exist, but would have to be implemented as a separate pair style command.

For style *dpd/fdt*, the fluctuation-dissipation theorem defines [\\(\\gamma\\)]{.math .notranslate .nohighlight} to be set equal to [\\(\\sigma\^2/(2 T)\\)]{.math .notranslate .nohighlight}, where *T* is the set point temperature specified as a pair style parameter in the above examples. The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- A (force units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (force\*time\^(1/2) units)

- cutoff (distance units)

The last coefficient is optional. If not specified, the global DPD cutoff is used.

Style *dpd/fdt/energy* is used to perform DPD simulations under isoenergetic and isoenthalpic conditions. The fluctuation-dissipation theorem defines [\\(\\gamma\\)]{.math .notranslate .nohighlight} to be set equal to [\\(\\sigma\^2/(2 \\theta)\\)]{.math .notranslate .nohighlight}, where [\\(\\theta\\)]{.math .notranslate .nohighlight} is the average internal temperature for the pair. The particle internal temperature is related to the particle internal energy through a mesoparticle equation of state (see [[fix eos]{.doc}]fix.md){.reference .internal}). The differential internal conductive and mechanical energies are computed within style *dpd/fdt/energy* as:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}du\_{i}\^{cond} = & \\kappa\_{ij}(\\frac{1}{\\theta\_{i}}-\\frac{1}{\\theta\_{j}})\\omega\_{ij}\^{2} + \\alpha\_{ij}\\omega\_{ij}\\zeta\_{ij}\^{q}(\\Delta{t})\^{-1/2} \\\\ du\_{i}\^{mech} = & -\\frac{1}{2}\\gamma\_{ij}\\omega\_{ij}\^{2}(\\frac{\\vec{r}\_{ij}}{r\_{ij}}\\bullet\\vec{v}\_{ij})\^{2} - \\frac{\\sigma\^{2}\_{ij}}{4}(\\frac{1}{m\_{i}}+\\frac{1}{m\_{j}})\\omega\_{ij}\^{2} - \\frac{1}{2}\\sigma\_{ij}\\omega\_{ij}(\\frac{\\vec{r}\_{ij}}{r\_{ij}}\\bullet\\vec{v}\_{ij})\\zeta\_{ij}(\\Delta{t})\^{-1/2}\\end{split}\\\]
:::

where

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\alpha\_{ij}\^{2} = & 2k\_{B}\\kappa\_{ij} \\\\ \\sigma\^{2}\_{ij} = & 2\\gamma\_{ij}k\_{B}\\Theta\_{ij} \\\\ \\Theta\_{ij}\^{-1} = & \\frac{1}{2}(\\frac{1}{\\theta\_{i}}+\\frac{1}{\\theta\_{j}})\\end{split}\\\]
:::

[\\(\\zeta_ij\^q\\)]{.math .notranslate .nohighlight} is a second Gaussian random number with zero mean and unit variance that is used to compute the internal conductive energy. The fluctuation-dissipation theorem defines [\\(alpha\^2\\)]{.math .notranslate .nohighlight} to be set equal to [\\(2k_B\\kappa\\)]{.math .notranslate .nohighlight}, where [\\(\\kappa\\)]{.math .notranslate .nohighlight} is the mesoparticle thermal conductivity parameter. The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- A (force units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (force\*time\^(1/2) units)

- [\\(\\kappa\\)]{.math .notranslate .nohighlight} (energy\*temperature/time units)

- cutoff (distance units)

The last coefficient is optional. If not specified, the global DPD cutoff is used.

The pairwise energy associated with styles *dpd/fdt* and *dpd/fdt/energy* is only due to the conservative force term [\\(F\^C\\)]{.math .notranslate .nohighlight}, and is shifted to be zero at the cutoff distance [\\(r_c\\)]{.math .notranslate .nohighlight}. The pairwise virial is calculated using only the conservative term.

The forces computed through the *dpd/fdt* and *dpd/fdt/energy* styles can be integrated with the velocity-Verlet integration scheme or the Shardlow splitting integration scheme described by [[(Lisal)]{.std .std-ref}](#lisal3){.reference .internal}. In the cases when these pair styles are combined with the [[fix shardlow]{.doc}]fix_shardlow.md){.reference .internal}, these pair styles differ from the other dpd styles in that the dissipative and random forces are split from the force calculation and are not computed within the pair style. Thus, only the conservative force is computed by the pair style, while the stochastic integration of the dissipative and random forces are handled through the Shardlow splitting algorithm approach. The Shardlow splitting algorithm is advantageous, especially when performing DPD under isoenergetic conditions, as it allows significantly larger timesteps to be taken.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These commands are part of the DPD-REACT package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Pair styles *dpd/fdt* and *dpd/fdt/energy* require use of the [[comm_modify vel yes]{.doc}]comm_modify.md){.reference .internal} option so that velocities are stored by ghost atoms.

Pair style *dpd/fdt/energy* requires [[atom_style dpd]{.doc}]atom_style.md){.reference .internal} to be used in order to properly account for the particle internal energies and temperatures.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix shardlow]{.doc}]fix_shardlow.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Lisal)** M. Lisal, J.K. Brennan, J. Bonet Avalos, J. Chem. Phys., 135, 204105 (2011).
:::
::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

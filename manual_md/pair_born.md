::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-born-command .section}
[]{#index-11}[]{#index-10}[]{#index-9}[]{#index-8}[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style born command[](#pair-style-born-command "Link to this heading"){.headerlink}

Accelerator Variants: *born/omp*, *born/gpu*
:::

::: {#pair-style-born-coul-long-command .section}
# pair_style born/coul/long command[](#pair-style-born-coul-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *born/coul/long/gpu*, *born/coul/long/omp*
:::

::: {#pair-style-born-coul-msm-command .section}
# pair_style born/coul/msm command[](#pair-style-born-coul-msm-command "Link to this heading"){.headerlink}

Accelerator Variants: *born/coul/msm/omp*
:::

::: {#pair-style-born-coul-wolf-command .section}
# pair_style born/coul/wolf command[](#pair-style-born-coul-wolf-command "Link to this heading"){.headerlink}

Accelerator Variants: *born/coul/wolf/gpu*, *born/coul/wolf/omp*
:::

::::::::::::::: {#pair-style-born-coul-dsf-command .section}
# pair_style born/coul/dsf command[](#pair-style-born-coul-dsf-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *born* or *born/coul/long* or *born/coul/msm* or *born/coul/wolf*

- args = list of arguments for a particular style

``` literal-block
born args = cutoff
  cutoff = global cutoff for non-Coulombic interactions (distance units)
born/coul/long args = cutoff (cutoff2)
  cutoff = global cutoff for non-Coulombic (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
born/coul/msm args = cutoff (cutoff2)
  cutoff = global cutoff for non-Coulombic (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
born/coul/wolf args = alpha cutoff (cutoff2)
  alpha = damping parameter (inverse distance units)
  cutoff = global cutoff for non-Coulombic (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
born/coul/dsf args = alpha cutoff (cutoff2)
  alpha = damping parameter (inverse distance units)
  cutoff = global cutoff for non-Coulombic (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style born 10.0
    pair_coeff * * 6.08 0.317 2.340 24.18 11.51
    pair_coeff 1 1 6.08 0.317 2.340 24.18 11.51

    pair_style born/coul/long 10.0
    pair_style born/coul/long 10.0 8.
    pair_coeff * * 6.08 0.317 2.340 24.18 11.51
    pair_coeff 1 1 6.08 0.317 2.340 24.18 11.51

    pair_style born/coul/msm 10.0
    pair_style born/coul/msm 10.0 8.0
    pair_coeff * * 6.08 0.317 2.340 24.18 11.51
    pair_coeff 1 1 6.08 0.317 2.340 24.18 11.51

    pair_style born/coul/wolf 0.25 10.0
    pair_style born/coul/wolf 0.25 10.0 9.0
    pair_coeff * * 6.08 0.317 2.340 24.18 11.51
    pair_coeff 1 1 6.08 0.317 2.340 24.18 11.51

    pair_style born/coul/dsf 0.1 10.0 12.0
    pair_coeff * *   0.0 1.00 0.00 0.00 0.00
    pair_coeff 1 1 480.0 0.25 0.00 1.05 0.50
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *born* style computes the Born-Mayer-Huggins or Tosi/Fumi potential described in [[(Fumi and Tosi)]{.std .std-ref}](#fumitosi){.reference .internal}, given by

::: {.math .notranslate .nohighlight}
\\\[E = A \\exp \\left(\\frac{\\sigma - r}{\\rho} \\right) - \\frac{C}{r\^6} + \\frac{D}{r\^8} \\qquad r \< r_c\\\]
:::

where [\\(\\sigma\\)]{.math .notranslate .nohighlight} is an interaction-dependent length parameter, [\\(\\rho\\)]{.math .notranslate .nohighlight} is an ionic-pair dependent length parameter, and [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff.

The styles with *coul/long* or *coul/msm* add a Coulombic term as described for the [[lj/cut]{.doc}]pair_lj.md){.reference .internal} pair styles. An additional damping factor is applied to the Coulombic term so it can be used in conjunction with the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command and its *ewald* or *pppm* of *msm* option. The Coulombic cutoff specified for this style means that pairwise interactions within this distance are computed directly; interactions outside that distance are computed in reciprocal space.

If one cutoff is specified for the *born/coul/long* and *born/coul/msm* style, it is used for both the A,C,D and Coulombic terms. If two cutoffs are specified, the first is used as the cutoff for the A,C,D terms, and the second is the cutoff for the Coulombic term.

The *born/coul/wolf* style adds a Coulombic term as described for the Wolf potential in the [[coul/wolf]{.doc}]pair_coul.md){.reference .internal} pair style.

The *born/coul/dsf* style computes the Coulomb contribution with the damped shifted force model as in the [[coul/dsf]{.doc}]pair_coul.md){.reference .internal} style.

Note that these potentials are related to the [[Buckingham potential]{.doc}]pair_buck.md){.reference .internal}.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- A (energy units)

- [\\(\\rho\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- C (energy units \* distance units\^6)

- D (energy units \* distance units\^8)

- cutoff (distance units)

The second coefficient, rho, must be greater than zero.

The last coefficient is optional. If not specified, the global A,C,D cutoff specified in the pair_style command is used.

For *born/coul/long*, *born/coul/wolf* and *born/coul/dsf* no Coulombic cutoff can be specified for an individual I,J type pair. All type pairs use the same global Coulombic cutoff specified in the pair_style command.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

These pair styles do not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

These styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the exp(), 1/r\^6, and 1/r\^8 portion of the pair interaction.

The *born/coul/long* pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option to tabulate the short-range portion of the long-range Coulombic interaction.

These styles support the pair_modify tail option for adding long-range tail corrections to energy and pressure.

Thess styles writes thei information to binary [[restart]{.doc}]restart.md){.reference .internal} files, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *born/coul/long* style is part of the KSPACE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The *born/coul/dsf* and *born/coul/wolf* pair styles are part of the EXTRA-PAIR package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style buck]{.doc}]pair_buck.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

Fumi and Tosi, J Phys Chem Solids, 25, 31 (1964), Fumi and Tosi, J Phys Chem Solids, 25, 45 (1964).
:::
:::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

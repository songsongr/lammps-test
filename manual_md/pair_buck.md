::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-buck-command .section}
[]{#index-16}[]{#index-15}[]{#index-14}[]{#index-13}[]{#index-12}[]{#index-11}[]{#index-10}[]{#index-9}[]{#index-8}[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style buck command[](#pair-style-buck-command "Link to this heading"){.headerlink}

Accelerator Variants: *buck/gpu*, *buck/intel*, *buck/kk*, *buck/omp*
:::

::: {#pair-style-buck-coul-cut-command .section}
# pair_style buck/coul/cut command[](#pair-style-buck-coul-cut-command "Link to this heading"){.headerlink}

Accelerator Variants: *buck/coul/cut/gpu*, *buck/coul/cut/intel*, *buck/coul/cut/kk*, *buck/coul/cut/omp*
:::

::: {#pair-style-buck-coul-long-command .section}
# pair_style buck/coul/long command[](#pair-style-buck-coul-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *buck/coul/long/gpu*, *buck/coul/long/intel*, *buck/coul/long/kk*, *buck/coul/long/omp*
:::

:::::::::::::::: {#pair-style-buck-coul-msm-command .section}
# pair_style buck/coul/msm command[](#pair-style-buck-coul-msm-command "Link to this heading"){.headerlink}

Accelerator Variants: *buck/coul/msm/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *buck* or *buck/coul/cut* or *buck/coul/long* or *buck/coul/msm*

- args = list of arguments for a particular style

``` literal-block
buck args = cutoff
  cutoff = global cutoff for Buckingham interactions (distance units)
buck/coul/cut args = cutoff (cutoff2)
  cutoff = global cutoff for Buckingham (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
buck/coul/long args = cutoff (cutoff2)
  cutoff = global cutoff for Buckingham (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
buck/coul/msm args = cutoff (cutoff2)
  cutoff = global cutoff for Buckingham (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style buck 2.5
    pair_coeff * * 100.0 1.5 200.0
    pair_coeff * * 100.0 1.5 200.0 3.0

    pair_style buck/coul/cut 10.0
    pair_style buck/coul/cut 10.0 8.0
    pair_coeff * * 100.0 1.5 200.0
    pair_coeff 1 1 100.0 1.5 200.0 9.0
    pair_coeff 1 1 100.0 1.5 200.0 9.0 8.0

    pair_style buck/coul/long 10.0
    pair_style buck/coul/long 10.0 8.0
    pair_coeff * * 100.0 1.5 200.0
    pair_coeff 1 1 100.0 1.5 200.0 9.0

    pair_style buck/coul/msm 10.0
    pair_style buck/coul/msm 10.0 8.0
    pair_coeff * * 100.0 1.5 200.0
    pair_coeff 1 1 100.0 1.5 200.0 9.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *buck* style computes a Buckingham potential (exp/6 instead of Lennard-Jones 12/6) given by

::: {.math .notranslate .nohighlight}
\\\[E = A e\^{-r / \\rho} - \\frac{C}{r\^6} \\qquad r \< r_c\\\]
:::

where [\\(\\rho\\)]{.math .notranslate .nohighlight} is an ionic-pair dependent length parameter, and [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff on both terms.

The styles with *coul/cut* or *coul/long* or *coul/msm* add a Coulombic term as described for the [[lj/cut]{.doc}]pair_lj.md){.reference .internal} pair styles. For *buck/coul/long* and *buc/coul/msm*, an additional damping factor is applied to the Coulombic term so it can be used in conjunction with the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command and its *ewald* or *pppm* or *msm* option. The Coulombic cutoff specified for this style means that pairwise interactions within this distance are computed directly; interactions outside that distance are computed in reciprocal space.

If one cutoff is specified for the *born/coul/cut* and *born/coul/long* and *born/coul/msm* styles, it is used for both the A,C and Coulombic terms. If two cutoffs are specified, the first is used as the cutoff for the A,C terms, and the second is the cutoff for the Coulombic term.

Note that these potentials are related to the [[Born-Mayer-Huggins potential]{.doc}]pair_born.md){.reference .internal}.

::: {.admonition .note}
Note

For all these pair styles, the terms with A and C are always cutoff. The additional Coulombic term can be cutoff or long-range (no cutoff) depending on whether the style name includes coul/cut or coul/long or coul/msm. If you wish the C/r\^6 term to be long-range (no cutoff), then see the [[pair_style buck/long/coul/long]{.doc}]pair_buck_long.md){.reference .internal} command.
:::

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- A (energy units)

- [\\(\\rho\\)]{.math .notranslate .nohighlight} (distance units)

- C (energy-distance\^6 units)

- cutoff (distance units)

- cutoff2 (distance units)

The second coefficient, [\\(\\rho\\)]{.math .notranslate .nohighlight}, must be greater than zero. The coefficients A, [\\(\\rho\\)]{.math .notranslate .nohighlight}, and C can be written as analytical expressions of [\\(\\epsilon\\)]{.math .notranslate .nohighlight} and [\\(\\sigma\\)]{.math .notranslate .nohighlight}, in analogy to the Lennard-Jones potential [[(Khrapak)]{.std .std-ref}](#khrapak){.reference .internal}.

The latter 2 coefficients are optional. If not specified, the global A,C and Coulombic cutoffs are used. If only one cutoff is specified, it is used as the cutoff for both A,C and Coulombic interactions for this type pair. If both coefficients are specified, they are used as the A,C and Coulombic cutoffs for this type pair. You cannot specify 2 cutoffs for style *buck*, since it has no Coulombic terms. For *buck/coul/long* only the LJ cutoff can be specified since a Coulombic cutoff cannot be specified for an individual I,J type pair. All type pairs use the same global Coulombic cutoff specified in the pair_style command.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

These pair styles do not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

These styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the exp() and 1/r\^6 portion of the pair interaction.

The *buck/coul/long* pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option to tabulate the short-range portion of the long-range Coulombic interaction.

These styles support the pair_modify tail option for adding long-range tail corrections to energy and pressure for the A,C terms in the pair interaction.

These styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *buck/coul/long* style is part of the KSPACE package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style born]{.doc}]pair_born.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

**(Khrapak)** Khrapak, Chaudhuri, and Morfill, J Chem Phys, 134, 054120 (2011).
:::
::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

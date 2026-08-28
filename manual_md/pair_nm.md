::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-nm-cut-command .section}
[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style nm/cut command[](#pair-style-nm-cut-command "Link to this heading"){.headerlink}

Accelerator Variants: *nm/cut/omp*
:::

::: {#pair-style-nm-cut-split-command .section}
# pair_style nm/cut/split command[](#pair-style-nm-cut-split-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-nm-cut-coul-cut-command .section}
# pair_style nm/cut/coul/cut command[](#pair-style-nm-cut-coul-cut-command "Link to this heading"){.headerlink}

Accelerator Variants: *nm/cut/coul/cut/omp*
:::

:::::::::::::::: {#pair-style-nm-cut-coul-long-command .section}
# pair_style nm/cut/coul/long command[](#pair-style-nm-cut-coul-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *nm/cut/coul/long/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *nm/cut* or *nm/cut/split* or *nm/cut/coul/cut* or *nm/cut/coul/long*

- args = list of arguments for a particular style

  ``` literal-block
  nm/cut args = cutoff
    cutoff = global cutoff for Pair interactions (distance units)
  nm/cut/split args = cutoff
    cutoff = global cutoff for Pair interactions (distance units)
  nm/cut/coul/cut args = cutoff (cutoff2)
    cutoff = global cutoff for Pair (and Coulombic if only 1 arg) (distance units)
    cutoff2 = global cutoff for Coulombic (optional) (distance units)
  nm/cut/coul/long args = cutoff (cutoff2)
    cutoff = global cutoff for Pair (and Coulombic if only 1 arg) (distance units)
    cutoff2 = global cutoff for Coulombic (optional) (distance units)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style nm/cut 12.0
    pair_coeff * * 0.01 5.4 8.0 7.0
    pair_coeff 1 1 0.01 4.4 7.0 6.0

    pair_style nm/cut/split 1.12246
    pair_coeff 1 1 1.0 1.1246 12 6
    pair_coeff * * 1.0 1.1246 11 6

    pair_style nm/cut/coul/cut 12.0 15.0
    pair_coeff * * 0.01 5.4 8.0 7.0
    pair_coeff 1 1 0.01 4.4 7.0 6.0

    pair_style nm/cut/coul/long 12.0 15.0
    pair_coeff * * 0.01 5.4 8.0 7.0
    pair_coeff 1 1 0.01 4.4 7.0 6.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *nm* computes site-site interactions based on the N-M potential by [[Clarke]{.std .std-ref}](#clarke){.reference .internal}, mainly used for ionic liquids. A site can represent a single atom or a united-atom site. The energy of an interaction has the following form:

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{E_0}{(n-m)} \\left\[ m \\left(\\frac{r_0}{r}\\right)\^n - n \\left(\\frac{r_0}{r}\\right)\^m \\right\] \\qquad r \< r_c\\\]
:::

where [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff and [\\(r_0\\)]{.math .notranslate .nohighlight} is the minimum of the potential. Please note that this differs from the convention used for other Lennard-Jones potentials in LAMMPS where [\\(\\sigma\\)]{.math .notranslate .nohighlight} represents the location where the energy is zero.

Style *nm/cut/split* applies the standard LJ (12-6) potential above [\\(r_0 = 2\^\\frac{1}{6}\\sigma\\)]{.math .notranslate .nohighlight}. Style *nm/cut/split* is employed in polymer equilibration protocols that combine core-softening approaches with topology-changing moves [[Dietz]{.std .std-ref}](#dietz){.reference .internal}.

Style *nm/cut/coul/cut* adds a Coulombic pairwise interaction given by

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{C q_i q_j}{\\epsilon r} \\qquad r \< r_c\\\]
:::

where [\\(C\\)]{.math .notranslate .nohighlight} is an energy-conversion constant, [\\(q_i\\)]{.math .notranslate .nohighlight} and [\\(q_j\\)]{.math .notranslate .nohighlight} are the charges on the two atoms, and epsilon is the dielectric constant which can be set by the [[dielectric]{.doc}]dielectric.md){.reference .internal} command. If one cutoff is specified in the pair_style command, it is used for both the N-M and Coulombic terms. If two cutoffs are specified, they are used as cutoffs for the N-M and Coulombic terms respectively.

Styles *nm/cut/coul/long* compute the same Coulombic interactions as style *nm/cut/coul/cut* except that an additional damping factor is applied to the Coulombic term so it can be used in conjunction with the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command and its *ewald* or *pppm* option. The Coulombic cutoff specified for this style means that pairwise interactions within this distance are computed directly; interactions outside that distance are computed in reciprocal space.

For all of the *nm* pair styles, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

- [\\(E_0\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(n\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(m\\)]{.math .notranslate .nohighlight} (unitless)

- cutoff1 (distance units)

- cutoff2 (distance units)

The latter 2 coefficients are optional. If not specified, the global N-M and Coulombic cutoffs specified in the pair_style command are used. If only one cutoff is specified, it is used as the cutoff for both N-M and Coulombic interactions for this type pair. If both coefficients are specified, they are used as the N-M and Coulombic cutoffs for this type pair. You cannot specify 2 cutoffs for style *nm*, since it has no Coulombic terms.

For *nm/cut/coul/long* only the N-M cutoff can be specified since a Coulombic cutoff cannot be specified for an individual I,J type pair. All type pairs use the same global Coulombic cutoff specified in the pair_style command.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

These pair styles do not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

All of the *nm* pair styles supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The *nm/cut/coul/long* pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option since they can tabulate the short-range portion of the long-range Coulombic interaction.

All of the *nm* pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding a long-range tail correction to the energy and pressure for the N-M portion of the pair interaction.

All of the *nm* pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

All of the *nm* pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the EXTRA-PAIR package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair style lj/cut]{.doc}]pair_lj.md){.reference .internal}, [[bond style fene/nm]{.doc}]bond_fene.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Clarke)** Clarke and Smith, J Chem Phys, 84, 2290 (1986).

**(Dietz)** Dietz and Hoy, J. Chem Phys, 156, 014103 (2022).
:::
::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-pedone-command .section}
[]{#index-1}[]{#index-0}

# pair_style pedone command[](#pair-style-pedone-command "Link to this heading"){.headerlink}

Accelerator Variants: *pedone/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = pedone\*

- args = list of arguments for a particular style

``` literal-block
pedone args = cutoff
  cutoff = global cutoff for Pedone interactions (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay pedone 15.0 coul/long 15.0
    kspace_style pppm 1.0e-5

    pair_coeff * * coul/long
    pair_coeff 1 2 pedone 0.030211 2.241334 2.923245 5.0
    pair_coeff 2 2 pedone 0.042395 1.379316 3.618701 22.0
:::
::::

Used in input scripts:

> ::::: {}
> :::: {.highlight-none .notranslate}
> ::: highlight
>     examples/PACKAGES/pedone/in.pedone.relax
>     examples/PACKAGES/pedone/in.pedone.melt
> :::
> ::::
> :::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 17Apr2024.]{.versionmodified .added}
:::

Pair style *pedone* computes the **non-Coulomb** interactions of the Pedone (or PMMCS) potential [[(Pedone)]{.std .std-ref}](#pedone){.reference .internal} which combines Coulomb interactions, Morse potential, and repulsive [\\(r\^{-12}\\)]{.math .notranslate .nohighlight} Lennard-Jones terms (see below). The *pedone* pair style is meant to be used in addition to a [[Coulomb pair style]{.doc}]pair_coul.md){.reference .internal} via pair style [[hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} (see example above). Using *coul/long* or *could/dsf* (for solids) is recommended.

The full Pedone potential function from [[(Pedone)]{.std .std-ref}](#pedone){.reference .internal} for each pair of atoms is:

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{C q_i q_j}{\\epsilon r} + D_0 \\left\[ e\^{- 2 \\alpha (r - r_0)} - 2 e\^{- \\alpha (r - r_0)} \\right\] + \\frac{B_0}{r\^{12}} \\qquad r \< r_c\\\]
:::

[\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff and [\\(C\\)]{.math .notranslate .nohighlight} is a conversion factor that is specific to the choice of [[units]{.doc}]units.md){.reference .internal} so that the entire Coulomb term is in energy units with [\\(q_i\\)]{.math .notranslate .nohighlight} and [\\(q_j\\)]{.math .notranslate .nohighlight} as the assigned charges in multiples of the elementary charge.

The following coefficients must be defined for the selected pairs of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the example above:

- [\\(D_0\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (1/distance units)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(C_0\\)]{.math .notranslate .nohighlight} (energy units)

- cutoff (distance units)

The last coefficient is optional. If not specified, the global *pedone* cutoff is used.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support mixing.

This pair style support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands does not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, or *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *pedone* pair style is only enabled if LAMMPS was built with the EXTRA-PAIR package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style]{.doc}]pair_style.md){.reference .internal}, [[pair style coul/long and coul/dsf]{.doc}]pair_coul.md){.reference .internal}, [[pair style morse]{.doc}]pair_morse.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Pedone)** A. Pedone, G. Malavasi, M. C. Menziani, A. N. Cormack, and U. Segre, J. Phys. Chem. B, 110, 11780 (2006)
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

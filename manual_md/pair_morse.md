::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-morse-command .section}
[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style morse command[](#pair-style-morse-command "Link to this heading"){.headerlink}

Accelerator Variants: *morse/gpu*, *morse/omp*, *morse/opt*, *morse/kk*
:::

:::::::::::::::: {#pair-style-morse-smooth-linear-command .section}
# pair_style morse/smooth/linear command[](#pair-style-morse-smooth-linear-command "Link to this heading"){.headerlink}

Accelerator Variants: *morse/smooth/linear/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *morse* or *morse/smooth/linear* or *morse/soft*

- args = list of arguments for a particular style

``` literal-block
morse args = cutoff
  cutoff = global cutoff for Morse interactions (distance units)
morse/smooth/linear args = cutoff
  cutoff = global cutoff for Morse interactions (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style morse 2.5
    pair_style morse/smooth/linear 2.5
    pair_coeff * * 100.0 2.0 1.5
    pair_coeff 1 1 100.0 2.0 1.5 3.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *morse* computes pairwise interactions with the formula

::: {.math .notranslate .nohighlight}
\\\[E = D_0 \\left\[ e\^{- 2 \\alpha (r - r_0)} - 2 e\^{- \\alpha (r - r_0)} \\right\] \\qquad r \< r_c\\\]
:::

[\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(D_0\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (1/distance units)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance units)

- cutoff (distance units)

The last coefficient is optional. If not specified, the global morse cutoff is used.

------------------------------------------------------------------------

The *morse/smooth/linear* variant is similar to the lj/smooth/linear variant in that it adds to the potential a shift and a linear term so that both, potential energy and force, go to zero at the cut-off:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\phi\\left(r\\right) & = D_0 \\left\[ e\^{- 2 \\alpha (r - r_0)} - 2 e\^{- \\alpha (r - r_0)} \\right\] \\qquad r \< r_c \\\\ E\\left(r\\right) & = \\phi\\left(r\\right) - \\phi\\left(r_c\\right) - \\left(r - r_c\\right) \\left.\\frac{d\\phi}{d r} \\right\|\_{r=r_c} \\qquad r \< r_c\\end{split}\\\]
:::

The syntax of the pair_style and pair_coeff commands are the same for the *morse* and *morse/smooth/linear* styles.

------------------------------------------------------------------------

A version of the *morse* style with a soft core, *morse/soft*, suitable for use in free energy calculations, is part of the FEP package and is documented with the [[pair_style \*/soft]{.doc}]pair_fep_soft.md){.reference .internal} styles. The version with soft core is only available if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

None of these pair styles support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

All of these pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table options are not relevant for the Morse pair styles.

None of these pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

All of these pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *morse/smooth/linear* pair style is only enabled if LAMMPS was built with the EXTRA-PAIR package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style \*/soft]{.doc}]pair_fep_soft.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

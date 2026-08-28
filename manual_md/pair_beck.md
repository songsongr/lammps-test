::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#pair-style-beck-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style beck command[](#pair-style-beck-command "Link to this heading"){.headerlink}

Accelerator Variants: *beck/gpu*, *beck/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style beck Rc
:::
::::

- Rc = cutoff for interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style beck 8.0
    pair_coeff * * 399.671876712 0.0000867636112694 0.675 4.390 0.0003746
    pair_coeff 1 1 399.671876712 0.0000867636112694 0.675 4.390 0.0003746 6.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *beck* computes interactions based on the potential by [[(Beck)]{.std .std-ref}](#beck){.reference .internal}, originally designed for simulation of Helium. It includes truncation at a cutoff distance [\\(r_c\\)]{.math .notranslate .nohighlight}.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E(r) &= A \\exp\\left\[-\\alpha r - \\beta r\^6\\right\] - \\frac{B}{\\left(r\^2+a\^2\\right)\^3} \\left(1+\\frac{2.709+3a\^2}{r\^2+a\^2}\\right) \\qquad r \< r_c \\\\\\end{split}\\\]
:::

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

- [\\(A\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(B\\)]{.math .notranslate .nohighlight} (energy-distance\^6 units)

- [\\(a\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (1/distance units)

- [\\(\\beta\\)]{.math .notranslate .nohighlight} (1/distance\^6 units)

- cutoff (distance units)

The last coefficient is optional. If not specified, the global cutoff [\\(r_c\\)]{.math .notranslate .nohighlight} is used.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, coefficients must be specified. No default mixing rules are used.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the EXTRA-PAIR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Beck)** Beck, Molecular Physics, 14, 311 (1968).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-lj-expand-command .section}
[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style lj/expand command[](#pair-style-lj-expand-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/expand/gpu*, *lj/expand/kk*, *lj/expand/omp*
:::

::::::::::::::: {#pair-style-lj-expand-coul-long-command .section}
# pair_style lj/expand/coul/long command[](#pair-style-lj-expand-coul-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/expand/coul/long/gpu*, *lj/expand/coul/long/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/expand cutoff
:::
::::

- cutoff = global cutoff for lj/expand interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/expand 2.5
    pair_coeff * * 1.0 1.0 0.5
    pair_coeff 1 1 1.0 1.0 -0.2 2.0

    pair_style lj/expand/coul/long 2.5
    pair_style lj/expand/coul/long 2.5 4.0
    pair_coeff * * 1.0 1.0 0.5
    pair_coeff 1 1 1.0 1.0 -0.2 3.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *lj/expand* computes a LJ interaction with a distance shifted by delta which can be useful when particles are of different sizes, since it is different that using different sigma values in a standard LJ formula:

::: {.math .notranslate .nohighlight}
\\\[E = 4 \\epsilon \\left\[ \\left(\\frac{\\sigma}{r - \\Delta}\\right)\^{12} - \\left(\\frac{\\sigma}{r - \\Delta}\\right)\^6 \\right\] \\qquad r \< r_c + \\Delta\\\]
:::

[\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff which does not include the [\\(\\Delta\\)]{.math .notranslate .nohighlight} distance. I.e. the actual force cutoff is the sum of [\\(r_c + \\Delta\\)]{.math .notranslate .nohighlight}.

For all of the *lj/expand* pair styles, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(\\Delta\\)]{.math .notranslate .nohighlight} (distance units)

- cutoff (distance units)

The [\\(\\Delta\\)]{.math .notranslate .nohighlight} values can be positive or negative. The last coefficient is optional. If not specified, the global LJ cutoff is used.

For *lj/expand/coul/long* only the LJ cutoff can be specified since a Coulombic cutoff cannot be specified for an individual I,J type pair. All type pairs use the same global Coulombic cutoff specified in the pair_style command.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon, sigma, and shift coefficients and cutoff distance for this pair style can be mixed. Shift is always mixed via an *arithmetic* rule. The other coefficients are mixed according to the pair_modify mix value. The default mix value is *geometric*. See the "pair_modify" command for details.

This pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding a long-range tail correction to the energy and pressure of the pair interaction.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
:::::::::::::::::
::::::::::::::::::

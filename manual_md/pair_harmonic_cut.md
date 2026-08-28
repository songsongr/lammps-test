:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-harmonic-cut-command .section}
[]{#index-1}[]{#index-0}

# pair_style harmonic/cut command[](#pair-style-harmonic-cut-command "Link to this heading"){.headerlink}

Accelerator Variants: *harmonic/cut/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style
:::
::::

- style = *harmonic/cut*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style harmonic/cut
    pair_coeff * * 0.2 2.0
    pair_coeff 1 1 0.5 2.5
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 17Feb2022.]{.versionmodified .added}
:::

Style *harmonic/cut* computes pairwise repulsive-only harmonic interactions with the formula

::: {.math .notranslate .nohighlight}
\\\[E = k (r_c - r)\^2 \\qquad r \< r_c\\\]
:::

where [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff. Note that the usual 1/2 factor is included in [\\(k\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(k\\)]{.math .notranslate .nohighlight} (energy/distance\^2 units)

- [\\(r_c\\)]{.math .notranslate .nohighlight} (distance units)

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the [\\(k\\)]{.math .notranslate .nohighlight} and [\\(r_c\\)]{.math .notranslate .nohighlight} coefficients can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

Since the potential is zero at and beyond the cutoff parameter by construction, there is no need to support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift or tail options for the energy and pressure of the pair interaction.

These pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *harmonic/cut* pair style is only enabled if LAMMPS was built with the EXTRA-PAIR package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

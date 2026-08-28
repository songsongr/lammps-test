:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-coul-cut-dielectric-command .section}
[]{#index-9}[]{#index-8}[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style coul/cut/dielectric command[](#pair-style-coul-cut-dielectric-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-coul-long-dielectric-command .section}
# pair_style coul/long/dielectric command[](#pair-style-coul-long-dielectric-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-lj-cut-coul-cut-dielectric-command .section}
# pair_style lj/cut/coul/cut/dielectric command[](#pair-style-lj-cut-coul-cut-dielectric-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/cut/coul/cut/dielectric/omp*
:::

::: {#pair-style-lj-cut-coul-debye-dielectric-command .section}
# pair_style lj/cut/coul/debye/dielectric command[](#pair-style-lj-cut-coul-debye-dielectric-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/cut/coul/debye/dielectric/omp*
:::

::: {#pair-style-lj-cut-coul-long-dielectric-command .section}
# pair_style lj/cut/coul/long/dielectric command[](#pair-style-lj-cut-coul-long-dielectric-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/cut/coul/long/dielectric/omp*
:::

::: {#pair-style-lj-cut-coul-msm-dielectric-command .section}
# pair_style lj/cut/coul/msm/dielectric command[](#pair-style-lj-cut-coul-msm-dielectric-command "Link to this heading"){.headerlink}
:::

:::::::::::::: {#pair-style-lj-long-coul-long-dielectric-command .section}
# pair_style lj/long/coul/long/dielectric command[](#pair-style-lj-long-coul-long-dielectric-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *lj/cut/coul/cut/dielectric* or *lj/cut/coul/long/dielectric* or *lj/cut/coul/msm/dielectric* or *lj/long/coul/msm/dielectric*

- args = list of arguments for a particular style
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style coul/cut/dielectric 10.0
    pair_coeff * *
    pair_coeff 1 1 9.0

    pair_style lj/cut/coul/cut/dielectric 10.0
    pair_style lj/cut/coul/cut/dielectric 10.0 8.0
    pair_coeff * * 100.0 3.0
    pair_coeff 1 1 100.0 3.5 9.0

    pair_style lj/cut/coul/long/dielectric 10.0
    pair_style lj/cut/coul/long/dielectric 10.0 8.0
    pair_coeff * * 100.0 3.0
    pair_coeff 1 1 100.0 3.5 9.0
:::
::::

Used in input scripts:

> ::::: {}
> :::: {.highlight-none .notranslate}
> ::: highlight
>     examples/PACKAGES/dielectric/in.confined
>     examples/PACKAGES/dielectric/in.nopbc
> :::
> ::::
> :::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

All these pair styles are derived from the corresponding pair styles without the *dielectric* suffix. In addition to computing atom forces and energies, these pair styles compute the electric field vector at each atom, which are intended to be used by the [[fix polarize]{.doc}]fix_polarize.md){.reference .internal} commands to compute induced charges at interfaces between two regions of different dielectric constant.

These pair styles should be used with [[atom_style dielectric]{.doc}]atom_style.md){.reference .internal}.

The styles lj/cut/coul/long/dielectric, lj/cut/coul/msm/dielectric, and lj/long/coul/long/dielectric should be used with their kspace style counterparts, namely, pppm/dielectric, pppm/disp/dielectric, and msm/dielectric, respectively.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon and sigma coefficients and cutoff distances for this pair style can be mixed. The default mix algorithm is *geometric*. See the [[pair_modify]{.doc}]pair_modify.md){.reference .internal}" command for details.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

These pair styles write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These styles are part of the DIELECTRIC package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix polarize]{.doc}]fix_polarize.md){.reference .internal}, [[read_data]{.doc}]read_data.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

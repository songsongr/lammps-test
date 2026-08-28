::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-coul-slater-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style coul/slater command[](#pair-style-coul-slater-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-coul-slater-cut-command .section}
# pair_style coul/slater/cut command[](#pair-style-coul-slater-cut-command "Link to this heading"){.headerlink}
:::

::::::::::::::: {#pair-style-coul-slater-long-command .section}
# pair_style coul/slater/long command[](#pair-style-coul-slater-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *coul/slater/long/gpu*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style coul/slater/cut lambda cutoff
    pair_style coul/slater/long lambda cutoff
:::
::::

lambda = decay length of the charge (distance units) cutoff = cutoff (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style coul/slater/cut 1.0 3.5
    pair_coeff * *
    pair_coeff 2 2 2.5

    pair_style coul/slater/long 1.0 12.0
    pair_coeff * *
    pair_coeff 1 1 5.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Styles *coul/slater/\** compute electrostatic interactions in mesoscopic models which employ potentials without explicit excluded-volume interactions. The goal is to prevent artificial ionic pair formation by including a charge distribution in the Coulomb potential, following the formulation of [[(Melchor)]{.std .std-ref}](#melchor){.reference .internal}:

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{Cq_iq_j}{\\epsilon r} \\left( 1- \\left( 1 + \\frac{r\_{ij}}{\\lambda} exp\\left( -2r\_{ij}/\\lambda \\right) \\right) \\right) \\qquad r \< r_c\\\]
:::

where [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff distance and [\\(\\lambda\\)]{.math .notranslate .nohighlight} is the decay length of the charge. C is the same Coulomb conversion factor as in the pair_styles coul/cut and coul/long. In this way the Coulomb interaction between ions is corrected at small distances r. For the *coul/slater/cut* style, the potential energy for distances larger than the cutoff is zero, while for the *coul/slater/long*, the long-range interactions are computed either by the Ewald or the PPPM technique.

Phenomena that can be captured at a mesoscopic level using this type of electrostatic interactions include the formation of polyelectrolyte-surfactant aggregates, charge stabilization of colloidal suspensions, and the formation of complexes driven by charged species in biological systems. [[(Vaiwala)]{.std .std-ref}](#vaiwala){.reference .internal}.

The cutoff distance is optional. If it is not used, the default global value specified in the pair_style command is used. For each pair of atom types, a specific cutoff distance can be defined via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(r_c\\)]{.math .notranslate .nohighlight} (distance units)

The global decay length of the charge ([\\(\\lambda\\)]{.math .notranslate .nohighlight}) specified in the pair_style command is used for all pairs.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the cutoff distance for the *coul/slater* styles can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift and table options are not relevant for these pair styles.

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

These pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *coul/slater/long* style requires the long-range solvers included in the KSPACE package.

These styles are part of the EXTRA-PAIR package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style, hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[kspace_style]{.doc}]kspace_style.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Melchor)** Gonzalez-Melchor, Mayoral, Velazquez, and Alejandre, J Chem Phys, 125, 224107 (2006).

**(Vaiwala)** Vaiwala, Jadhav, and Thaokar, J Chem Phys, 146, 124904 (2017).
:::
:::::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-lj-cut-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style lj/cut command[](#pair-style-lj-cut-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/cut/gpu*, *lj/cut/intel*, *lj/cut/kk*, *lj/cut/opt*, *lj/cut/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *lj/cut*

- args = list of arguments for a particular style

``` literal-block
lj/cut args = cutoff
  cutoff = global cutoff for Lennard Jones interactions (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/cut 2.5
    pair_coeff * * 1 1
    pair_coeff 1 1 1 1.1 2.8
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *lj/cut* styles compute the standard 12/6 Lennard-Jones potential, given by

::: {.math .notranslate .nohighlight}
\\\[E = 4 \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - \\left(\\frac{\\sigma}{r}\\right)\^6 \\right\] \\qquad r \< r_c\\\]
:::

[\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff.

See the [[lj/cut/coul]{.doc}]pair_lj_cut_coul.md){.reference .internal} styles to add a Coulombic pairwise interaction and the [[lj/cut/tip4p]{.doc}]pair_lj_cut_tip4p.md){.reference .internal} styles to add the TIP4P water model.
::::

:::: {#coefficients .section}
## Coefficients[](#coefficients "Link to this heading"){.headerlink}

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- LJ cutoff (distance units)

The last coefficient is optional. If not specified, the global LJ cutoff specified in the pair_style command is used.

Note that [\\(\\sigma\\)]{.math .notranslate .nohighlight} is defined in the LJ formula as the zero-crossing distance for the potential, *not* as the energy minimum at [\\(r_0 = 2\^{\\frac{1}{6}} \\sigma\\)]{.math .notranslate .nohighlight}. The *same* potential function becomes:

::: {.math .notranslate .nohighlight}
\\\[E = \\epsilon \\left\[ \\left(\\frac{r_0}{r}\\right)\^{12} - 2 \\left(\\frac{r_0}{r}\\right)\^6 \\right\] \\qquad r \< r_c\\\]
:::

When using the minimum as reference width. In the literature both formulations are used, but the describe the same potential, only the [\\(\\sigma\\)]{.math .notranslate .nohighlight} value must be computed by [\\(\\sigma = r_0 / 2\^{\\frac{1}{6}}\\)]{.math .notranslate .nohighlight} for use with LAMMPS, if this latter formulation is used.

------------------------------------------------------------------------

A version of these styles with a soft core, *lj/cut/soft*, suitable for use in free energy calculations, is part of the FEP package and is documented with the [[pair_style \*/soft]{.doc}]pair_fep_soft.md){.reference .internal} styles.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon and sigma coefficients and cutoff distance for all of the lj/cut pair styles can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

All of the *lj/cut* pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the Lennard-Jones portion of the pair interaction.

All of the *lj/cut* pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding a long-range tail correction to the energy and pressure for the Lennard-Jones portion of the pair interaction.

All of the *lj/cut* pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

The *lj/cut* pair styles support the use of the *inner*, *middle*, and *outer* keywords of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command, meaning the pairwise forces can be partitioned by distance at different levels of the rRESPA hierarchy. The other styles only support the *pair* keyword of run_style respa. See the [[run_style]{.doc}]run_style.md){.reference .internal} command for details.
:::

------------------------------------------------------------------------

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

- [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}

- [[pair_style lj/cut/coul/cut]{.doc}]pair_lj_cut_coul.md){.reference .internal}

- [[pair_style lj/cut/coul/debye]{.doc}]pair_lj_cut_coul.md){.reference .internal}

- [[pair_style lj/cut/coul/dsf]{.doc}]pair_lj_cut_coul.md){.reference .internal}

- [[pair_style lj/cut/coul/long]{.doc}]pair_lj_cut_coul.md){.reference .internal}

- [[pair_style lj/cut/coul/msm]{.doc}]pair_lj_cut_coul.md){.reference .internal}

- [[pair_style lj/cut/coul/wolf]{.doc}]pair_lj_cut_coul.md){.reference .internal}

- [[pair_style lj/cut/tip4p/cut]{.doc}]pair_lj_cut_tip4p.md){.reference .internal}

- [[pair_style lj/cut/tip4p/long]{.doc}]pair_lj_cut_tip4p.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

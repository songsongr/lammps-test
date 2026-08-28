::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-lj-class2-command .section}
[]{#index-10}[]{#index-9}[]{#index-8}[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style lj/class2 command[](#pair-style-lj-class2-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/class2/gpu*, *lj/class2/kk*, *lj/class2/omp*
:::

::: {#pair-style-lj-class2-coul-cut-command .section}
# pair_style lj/class2/coul/cut command[](#pair-style-lj-class2-coul-cut-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/class2/coul/cut/kk*, *lj/class2/coul/cut/omp*
:::

::::::::::::::: {#pair-style-lj-class2-coul-long-command .section}
# pair_style lj/class2/coul/long command[](#pair-style-lj-class2-coul-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/class2/coul/long/gpu*, *lj/class2/coul/long/kk*, *lj/class2/coul/long/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *lj/class2* or *lj/class2/coul/cut* or *lj/class2/coul/long*

- args = list of arguments for a particular style

``` literal-block
lj/class2 args = cutoff
  cutoff = global cutoff for class 2 interactions (distance units)
lj/class2/coul/cut args = cutoff (cutoff2)
  cutoff = global cutoff for class 2 (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
lj/class2/coul/long args = cutoff (cutoff2)
  cutoff = global cutoff for class 2 (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/class2 10.0
    pair_coeff * * 100.0 2.5
    pair_coeff 1 2* 100.0 2.5 9.0

    pair_style lj/class2/coul/cut 10.0
    pair_style lj/class2/coul/cut 10.0 8.0
    pair_coeff * * 100.0 3.0
    pair_coeff 1 1 100.0 3.5 9.0
    pair_coeff 1 1 100.0 3.5 9.0 9.0

    pair_style lj/class2/coul/long 10.0
    pair_style lj/class2/coul/long 10.0 8.0
    pair_coeff * * 100.0 3.0
    pair_coeff 1 1 100.0 3.5 9.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *lj/class2* styles compute a 6/9 Lennard-Jones potential given by

::: {.math .notranslate .nohighlight}
\\\[E = \\epsilon \\left\[ 2 \\left(\\frac{\\sigma}{r}\\right)\^9 - 3 \\left(\\frac{\\sigma}{r}\\right)\^6 \\right\] \\qquad r \< r_c\\\]
:::

[\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff.

The *lj/class2/coul/cut* and *lj/class2/coul/long* styles add a Coulombic term as described for the [[lj/cut]{.doc}]pair_lj.md){.reference .internal} pair styles.

See [[(Sun)]{.std .std-ref}](#pair-sun){.reference .internal} for a description of the COMPASS class2 force field.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- cutoff1 (distance units)

- cutoff2 (distance units)

The latter 2 coefficients are optional. If not specified, the global class 2 and Coulombic cutoffs are used. If only one cutoff is specified, it is used as the cutoff for both class 2 and Coulombic interactions for this type pair. If both coefficients are specified, they are used as the class 2 and Coulombic cutoffs for this type pair. You cannot specify 2 cutoffs for style *lj/class2*, since it has no Coulombic terms.

For *lj/class2/coul/long* only the class 2 cutoff can be specified since a Coulombic cutoff cannot be specified for an individual I,J type pair. All type pairs use the same global Coulombic cutoff specified in the pair_style command.

------------------------------------------------------------------------

If the pair_coeff command is not used to define coefficients for a particular I != J type pair, the mixing rule for [\\(\\epsilon\\)]{.math .notranslate .nohighlight} and [\\(\\sigma\\)]{.math .notranslate .nohighlight} for all class2 potentials is to use the *sixthpower* formulas documented by the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} command. The [[pair_modify mix]{.doc}]pair_modify.md){.reference .internal} setting is thus ignored for class2 potentials for epsilon and sigma. However it is still followed for mixing the cutoff distance.

------------------------------------------------------------------------

A version of these styles with a soft core, *lj/cut/soft*, suitable for use in free energy calculations, is part of the FEP package and is documented with the [[pair_style \*/soft]{.doc}]pair_fep_soft.md){.reference .internal} styles. The version with soft core is only available if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon and sigma coefficients and cutoff distance for all of the lj/class2 pair styles can be mixed. Epsilon and sigma are always mixed with the value *sixthpower*. The cutoff distance is mixed by whatever option is set by the pair_modify command (default = geometric). See the "pair_modify" command for details.

All of the lj/class2 pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the Lennard-Jones portion of the pair interaction.

The *lj/class2/coul/long* pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option since a tabulation capability has not yet been added to this potential.

All of the lj/class2 pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding a long-range tail correction to the energy and pressure of the Lennard-Jones portion of the pair interaction.

All of the lj/class2 pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

Only the *lj/class2* and *lj/class2/coul/long* pair styles support the use of the *inner*, *middle*, and *outer* keywords of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command, meaning the pairwise forces can be partitioned by distance at different levels of the rRESPA hierarchy. The other styles only support the *pair* keyword of run_style respa. See the [[run_style]{.doc}]run_style.md){.reference .internal} command for details.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These styles are part of the CLASS2 package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style \*/soft]{.doc}]pair_fep_soft.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Sun)** Sun, J Phys Chem B 102, 7338-7364 (1998).
:::
:::::::::::::::
::::::::::::::::::
:::::::::::::::::::

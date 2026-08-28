::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-lj-spica-command .section}
[]{#index-9}[]{#index-8}[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style lj/spica command[](#pair-style-lj-spica-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/spica/gpu*, *lj/spica/kk*, *lj/spica/omp*
:::

::: {#pair-style-lj-spica-coul-long-command .section}
# pair_style lj/spica/coul/long command[](#pair-style-lj-spica-coul-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/spica/coul/long/gpu*, *lj/spica/coul/long/omp*, *lj/spica/coul/long/kk*
:::

::::::::::::::: {#pair-style-lj-spica-coul-msm-command .section}
# pair_style lj/spica/coul/msm command[](#pair-style-lj-spica-coul-msm-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/spica/coul/msm/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *lj/spica* or *lj/spica/coul/long*

- args = list of arguments for a particular style

``` literal-block
lj/spica args = cutoff
  cutoff = global cutoff for Lennard Jones interactions (distance units)
lj/spica/coul/long args = cutoff (cutoff2)
  cutoff = global cutoff for LJ (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/spica 2.5
    pair_coeff 1 1 lj12_6 1 1.1 2.8

    pair_style lj/spica/coul/long 10.0
    pair_style lj/spica/coul/long 10.0 12.0
    pair_coeff 1 1 lj9_6 100.0 3.5 12.0

    pair_style lj/spica/coul/msm 10.0
    pair_style lj/spica/coul/msm 10.0 12.0
    pair_coeff 1 1 lj9_6 100.0 3.5 12.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *lj/spica* styles compute a 9/6, 12/4, 12/5, or 12/6 Lennard-Jones potential, given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{27}{4} \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{9} - \\left(\\frac{\\sigma}{r}\\right)\^6 \\right\] \\qquad r \< r_c \\\\ E = & \\frac{3\\sqrt{3}}{2} \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - \\left(\\frac{\\sigma}{r}\\right)\^4 \\right\] \\qquad r \< r_c \\\\ E = & \\frac{12}{7}\\left(\\frac{12}{5}\\right)\^{\\left(\\frac{5}{7}\\right)} \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - \\left(\\frac{\\sigma}{r}\\right)\^5 \\right\] \\qquad r \< r_c \\\\ E = & 4 \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - \\left(\\frac{\\sigma}{r}\\right)\^6 \\right\] \\qquad r \< r_c\\end{split}\\\]
:::

as required for the SPICA (formerly called SDK) and the pSPICA Coarse-grained MD parameterization discussed in [[(Shinoda)]{.std .std-ref}](#shinoda3){.reference .internal}, [[(DeVane)]{.std .std-ref}](#devane){.reference .internal}, [[(Seo)]{.std .std-ref}](#seo){.reference .internal}, and [[(Miyazaki)]{.std .std-ref}](#miyazaki){.reference .internal}. [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff. Summary information on these force fields can be found at [https://www.spica-ff.org](https://www.spica-ff.org){.reference .external}

Style *lj/spica/coul/long* computes the adds Coulombic interactions with an additional damping factor applied so it can be used in conjunction with the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command and its *ewald* or *pppm* or *pppm/cg* option. The Coulombic cutoff specified for this style means that pairwise interactions within this distance are computed directly; interactions outside that distance are computed in reciprocal space.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- cg_type (lj9_6, lj12_4, lj12_5, or lj12_6)

- epsilon (energy units)

- sigma (distance units)

- cutoff1 (distance units)

Note that sigma is defined in the LJ formula as the zero-crossing distance for the potential, not as the energy minimum. The prefactors are chosen so that the potential minimum is at -epsilon.

The latter 2 coefficients are optional. If not specified, the global LJ and Coulombic cutoffs specified in the pair_style command are used. If only one cutoff is specified, it is used as the cutoff for both LJ and Coulombic interactions for this type pair. If both coefficients are specified, they are used as the LJ and Coulombic cutoffs for this type pair.

For *lj/spica/coul/long* and *lj/spica/coul/msm* only the LJ cutoff can be specified since a Coulombic cutoff cannot be specified for an individual I,J type pair. All type pairs use the same global Coulombic cutoff specified in the pair_style command.

The original implementation of the above styles are style *lj/sdk*, *lj/sdk/coul/long*, and *lj/sdk/coul/msm*, and available for backward compatibility.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon and sigma coefficients and cutoff distance for all of the lj/spica pair styles *cannot* be mixed, since different pairs may have different exponents. So all parameters for all pairs have to be specified explicitly through the "pair_coeff" command. Defining then in a data file is also not supported, due to limitations of that file format.

All of the lj/spica pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the Lennard-Jones portion of the pair interaction.

The *lj/spica/coul/long* pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option since they can tabulate the short-range portion of the long-range Coulombic interaction.

All of the lj/spica pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

The lj/spica and lj/cut/coul/long pair styles do not support the use of the *inner*, *middle*, and *outer* keywords of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

All of the lj/spica pair styles are part of the CG-SPICA package. The *lj/spica/coul/long* style also requires the KSPACE package to be built (which is enabled by default). They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[angle_style spica]{.doc}]angle_spica.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Shinoda)** Shinoda, DeVane, Klein, Mol Sim, 33, 27-36 (2007).

**(DeVane)** Shinoda, DeVane, Klein, Soft Matter, 4, 2453-2462 (2008).

**(Seo)** Seo, Shinoda, J Chem Theory Comput, 15, 762-774 (2019).

**(Miyazaki)** Miyazaki, Okazaki, Shinoda, J Chem Theory Comput, 16, 782-793 (2020).
:::
:::::::::::::::
::::::::::::::::::
:::::::::::::::::::

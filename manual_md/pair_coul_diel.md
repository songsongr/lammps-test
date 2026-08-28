::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#pair-style-coul-diel-command .section}
[]{#index-1}[]{#index-0}

# pair_style coul/diel command[](#pair-style-coul-diel-command "Link to this heading"){.headerlink}

Accelerator Variants: *coul/diel/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style coul/diel cutoff
:::
::::

cutoff = global cutoff (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style coul/diel 3.5
    pair_coeff 1 4 78. 1.375 0.112
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *coul/diel* computes a Coulomb correction for implicit solvent ion interactions in which the dielectric permittivity is distance dependent. The dielectric permittivity [\\(\\epsilon_D(r)\\)]{.math .notranslate .nohighlight} connects to limiting regimes: One limit is defined by a small dielectric permittivity (close to vacuum) at or close to contact separation between the ions. At larger separations the dielectric permittivity reaches a bulk value used in the regular Coulomb interaction coul/long or coul/cut. The transition is modeled by a hyperbolic function which is incorporated in the Coulomb correction term for small ion separations as follows

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{Cq_iq_j}{\\epsilon r} \\left( \\frac{\\epsilon}{\\epsilon_D(r)}-1\\right) \\qquad r \< r_c \\\\ \\epsilon_D(r) = & \\frac{5.2+\\epsilon}{2} + \\frac{\\epsilon-5.2}{2}\\tanh\\left(\\frac{r-r\_{me}}{\\sigma_e}\\right)\\end{split}\\\]
:::

where [\\(r\_{me}\\)]{.math .notranslate .nohighlight} is the inflection point of [\\(\\epsilon_D(r)\\)]{.math .notranslate .nohighlight} and [\\(\\sigma_e\\)]{.math .notranslate .nohighlight} is a slope defining length scale. C is the same Coulomb conversion factor as in the pair_styles coul/cut, coul/long, and coul/debye. In this way the Coulomb interaction between ions is corrected at small distances r. The lower limit of [\\(\\epsilon_D(r \\to 0) = 5.2\\)]{.math .notranslate .nohighlight} due to dielectric saturation [[(Stiles)]{.std .std-ref}](#stiles){.reference .internal} while the Coulomb interaction reaches its bulk limit by setting [\\(\\epsilon_D(r \\to \\infty) = \\epsilon\\)]{.math .notranslate .nohighlight}, the bulk value of the solvent which is 78 for water at 298K.

Examples of the use of this type of Coulomb interaction include implicit solvent simulations of salt ions [[(Lenart)]{.std .std-ref}](#lenart1){.reference .internal} and of ionic surfactants [[(Jusufi)]{.std .std-ref}](#jusufi1){.reference .internal}. Note that this potential is only reasonable for implicit solvent simulations and in combination with coul/cut or coul/long. It is also usually combined with gauss/cut, see [[(Lenart)]{.std .std-ref}](#lenart1){.reference .internal} or [[(Jusufi)]{.std .std-ref}](#jusufi1){.reference .internal}.

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (no units)

- [\\(r\_{me}\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(\\sigma_e\\)]{.math .notranslate .nohighlight} (distance units)

The global cutoff ([\\(r_c\\)]{.math .notranslate .nohighlight}) specified in the pair_style command is used.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support parameter mixing. Coefficients must be given explicitly for each type of particle pairs.

This pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the Gauss-potential portion of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This style is part of the EXTRA-PAIR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} [[pair_style gauss/cut]{.doc}]pair_gauss.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Stiles)** Stiles, Hubbard, and Kayser, J Chem Phys, 77, 6189 (1982).

**(Lenart)** Lenart, Jusufi, and Panagiotopoulos, J Chem Phys, 126, 044509 (2007).

**(Jusufi)** Jusufi, Hynninen, and Panagiotopoulos, J Phys Chem B, 112, 13783 (2008).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

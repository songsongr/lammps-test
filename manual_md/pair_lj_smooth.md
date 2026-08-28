:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-lj-smooth-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style lj/smooth command[](#pair-style-lj-smooth-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/smooth/gpu*, *lj/smooth/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/smooth Rin Rc
:::
::::

- Rin = inner cutoff beyond which force smoothing will be applied (distance units)

- Rc = outer cutoff for lj/smooth interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/smooth 8.0 10.0
    pair_coeff * * 10.0 1.5
    pair_coeff 1 1 20.0 1.3 7.0 9.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *lj/smooth* computes a LJ interaction with a force smoothing applied between the inner and outer cutoff.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = 4 \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - \\left(\\frac{\\sigma}{r}\\right)\^6 \\right\] \\qquad r \< r\_{in} \\\\ F & = C_1 + C_2 (r - r\_{in}) + C_3 (r - r\_{in})\^2 + C_4 (r - r\_{in})\^3 \\qquad r\_{in} \< r \< r_c\\end{split}\\\]
:::

The polynomial coefficients C1, C2, C3, C4 are computed by LAMMPS to cause the force to vary smoothly from the inner cutoff [\\(r\_{in}\\)]{.math .notranslate .nohighlight} to the outer cutoff [\\(r_c\\)]{.math .notranslate .nohighlight}.

At the inner cutoff the force and its first derivative will match the non-smoothed LJ formula. At the outer cutoff the force and its first derivative will be 0.0. The inner cutoff cannot be 0.0.

Explicit expressions for the coefficients C1, C2, C3, C4, as well as the energy discontinuity at the cutoff can be found here [[(Leoni_1)]{.std .std-ref}](#leoni-1){.reference .internal} and here [[(Leoni_2)]{.std .std-ref}](#leoni-2){.reference .internal}

::: {.admonition .note}
Note

this force smoothing causes the energy to be discontinuous both in its values and first derivative. This can lead to poor energy conservation and may require the use of a thermostat. The energy value discontinuity can be eliminated by shifting the potential energy to be zero at the outer cutoff using the pair_modify shift option. With or without shifting, you can plot the resulting energy and force via the [[pair_write]{.doc}]pair_write.md){.reference .internal} command to see the effect.
:::

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(r\_{in}\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(r_c\\)]{.math .notranslate .nohighlight} (distance units)

The last 2 coefficients are optional inner and outer cutoffs. If not specified, the global values for [\\(r\_{in}\\)]{.math .notranslate .nohighlight} and [\\(r_c\\)]{.math .notranslate .nohighlight} are used.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon, sigma, Rin coefficients and the cutoff distance for this pair style can be mixed. Rin is a cutoff value and is mixed like the cutoff. The other coefficients are mixed according to the pair_modify mix option. The default mix value is *geometric*. See the "pair_modify" command for details.

This pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure, since the energy of the pair interaction is smoothed to 0.0 at the cutoff.

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

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair lj/smooth/linear]{.doc}]pair_lj_smooth_linear.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Leoni_1)** F. Leoni et al., Phys Rev Lett, 134, 128201 (2025).

**(Leoni_2)** F. Leoni et al., Phys Rev Lett, 134, Supplementary Material (2025).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

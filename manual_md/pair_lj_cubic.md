::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#pair-style-lj-cubic-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style lj/cubic command[](#pair-style-lj-cubic-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/cubic/gpu*, *lj/cubic/kk*, *lj/cubic/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/cubic
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/cubic
    pair_coeff * * 1.0 0.8908987
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *lj/cubic* style computes a truncated LJ interaction potential whose energy and force are continuous everywhere. Inside the inflection point the interaction is identical to the standard 12/6 [[Lennard-Jones]{.doc}]pair_lj.md){.reference .internal} potential. The LJ function outside the inflection point is replaced with a cubic function of distance. The energy, force, and second derivative are continuous at the inflection point. The cubic coefficient A3 is chosen so that both energy and force go to zero at the cutoff distance. Outside the cutoff distance the energy and force are zero.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = u\_{LJ}(r) \\qquad r \\leq r_s \\\\ & = u\_{LJ}(r_s) + (r-r_s) u\'\_{LJ}(r_s) - \\frac{1}{6} A_3 (r-r_s)\^3 \\qquad r_s \< r \\leq r_c \\\\ & = 0 \\qquad r \> r_c\\end{split}\\\]
:::

The location of the inflection point [\\(r_s\\)]{.math .notranslate .nohighlight} is defined by the LJ diameter, [\\(r_s/\\sigma = (26/7)\^{1/6}\\)]{.math .notranslate .nohighlight}. The cutoff distance is defined by [\\(r_c/r_s = 67/48\\)]{.math .notranslate .nohighlight} or [\\(r_c/\\sigma = 1.737\...\\)]{.math .notranslate .nohighlight} The analytic expression for the cubic coefficient [\\(A_3 r\_{min}\^3/\\epsilon = 27.93\...\\)]{.math .notranslate .nohighlight} is given in the paper by Holian and Ravelo [[(Holian)]{.std .std-ref}](#holian){.reference .internal}.

This potential is commonly used to study the shock mechanics of FCC solids, as in Ravelo et al. [[(Ravelo)]{.std .std-ref}](#ravelo2){.reference .internal}.

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

Note that [\\(\\sigma\\)]{.math .notranslate .nohighlight} is defined in the LJ formula as the zero-crossing distance for the potential, not as the energy minimum, which is located at [\\(r\_{min} = 2\^{\\frac{1}{6}} \\sigma\\)]{.math .notranslate .nohighlight}. In the above example, [\\(\\sigma = 0.8908987\\)]{.math .notranslate .nohighlight}, so [\\(r\_{min} = 1.0\\)]{.math .notranslate .nohighlight}.

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

The lj/cubic pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option, since pair interaction is already smoothed to 0.0 at the cutoff.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

The lj/cubic pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure, since there are no corrections for a potential that goes to 0.0 at the cutoff.

The lj/cubic pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

The lj/cubic pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
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

[]{#holian}**(Holian)** Holian and Ravelo, Phys Rev B, 51, 11275 (1995).

**(Ravelo)** Ravelo, Holian, Germann and Lomdahl, Phys Rev B, 70, 014103 (2004).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

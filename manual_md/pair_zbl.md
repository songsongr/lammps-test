:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-zbl-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style zbl command[](#pair-style-zbl-command "Link to this heading"){.headerlink}

Accelerator Variants: *zbl/gpu*, *zbl/kk*, *zbl/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style zbl inner outer
:::
::::

- inner = distance where switching function begins

- outer = global cutoff for ZBL interaction
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style zbl 3.0 4.0
    pair_coeff * * 73.0 73.0
    pair_coeff 1 1 14.0 14.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *zbl* computes the Ziegler-Biersack-Littmark (ZBL) screened nuclear repulsion for describing high-energy collisions between atoms. [[(Ziegler)]{.std .std-ref}](#ziegler){.reference .internal}. It includes an additional switching function that ramps the energy, force, and curvature smoothly to zero between an inner and outer cutoff. The potential energy due to a pair of atoms at a distance r_ij is given by:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E\^{ZBL}\_{ij} & = \\frac{1}{4\\pi\\epsilon_0} \\frac{Z_i Z_j \\,e\^2}{r\_{ij}} \\phi(r\_{ij}/a)+ S(r\_{ij})\\\\ a & = \\frac{0.46850}{Z\_{i}\^{0.23} + Z\_{j}\^{0.23}}\\\\ \\phi(x) & = 0.18175e\^{-3.19980x} + 0.50986e\^{-0.94229x} + 0.28022e\^{-0.40290x} + 0.02817e\^{-0.20162x}\\\\\\end{split}\\\]
:::

where *e* is the electron charge, [\\(\\epsilon_0\\)]{.math .notranslate .nohighlight} is the electrical permittivity of vacuum, and [\\(Z_i\\)]{.math .notranslate .nohighlight} and [\\(Z_j\\)]{.math .notranslate .nohighlight} are the nuclear charges of the two atoms. The switching function [\\(S(r)\\)]{.math .notranslate .nohighlight} is identical to that used by [[pair_style lj/gromacs]{.doc}]pair_gromacs.md){.reference .internal}. Here, the inner and outer cutoff are the same for all pairs of atom types.

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the LAMMPS data file.

- [\\(Z_i\\)]{.math .notranslate .nohighlight} (atomic number for first atom type, e.g. 13.0 for aluminum)

- [\\(Z_j\\)]{.math .notranslate .nohighlight} (ditto for second atom type)

The values of [\\(Z_i\\)]{.math .notranslate .nohighlight} and [\\(Z_j\\)]{.math .notranslate .nohighlight} are normally equal to the atomic numbers of the two atom types. Thus, the user may optionally specify only the coefficients for each [\\(i==j\\)]{.math .notranslate .nohighlight} pair, and rely on the obvious mixing rule for cross interactions (see below). Note that when [\\(i==j\\)]{.math .notranslate .nohighlight} it is required that [\\(Z_i == Z_j\\)]{.math .notranslate .nohighlight}. When used with [[hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} and pairs are assigned to more than one sub-style, the mixing rule is not used and each pair of types interacting with the ZBL sub-style must be included in a pair_coeff command.

::: {.admonition .note}
Note

The numerical values of the exponential decay constants in the screening function depend on the unit of distance. In the above equation they are given for units of Angstroms. LAMMPS will automatically convert these values to the distance unit of the specified LAMMPS [[units]{.doc}]units.md){.reference .internal} setting. The values of Z should always be given as multiples of a proton's charge, e.g. 29.0 for copper.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs *i,j* and [\\(i \\neq j\\)]{.math .notranslate .nohighlight}, the [\\(Z_i\\)]{.math .notranslate .nohighlight} and [\\(Z_j\\)]{.math .notranslate .nohighlight} coefficients can be mixed by taking [\\(Z_a\\)]{.math .notranslate .nohighlight} and [\\(Z_b\\)]{.math .notranslate .nohighlight} from the values specified for the two cases where [\\(i == j\\)]{.math .notranslate .nohighlight} and thus [\\(Z_a = Z_i == Z_j\\)]{.math .notranslate .nohighlight} and [\\(Z_b = Z_i == Z_j\\)]{.math .notranslate .nohighlight} for different elements. When used with [[hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} and pairs are assigned to more than one sub-style, the mixing rule is not used and each pair of types interacting with the ZBL sub-style must be included in a pair_coeff command. The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} mix option has no effect on the mixing behavior

The ZBL pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option, since the ZBL interaction is already smoothed to 0.0 at the cutoff.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure, since there are no corrections for a potential that goes to 0.0 at the cutoff.

This pair style does not write information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands must be specified in an input script that reads a restart file.

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

------------------------------------------------------------------------

**(Ziegler)** J.F. Ziegler, J. P. Biersack and U. Littmark, "The Stopping and Range of Ions in Matter", Volume 1, Pergamon, 1985.
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

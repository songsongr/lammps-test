:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#pair-style-meam-spline-command .section}
[]{#index-1}[]{#index-0}

# pair_style meam/spline command[](#pair-style-meam-spline-command "Link to this heading"){.headerlink}

Accelerator Variants: *meam/spline/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style meam/spline
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style meam/spline
    pair_coeff * * Ti.meam.spline Ti
    pair_coeff * * Ti.meam.spline Ti O
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *meam/spline* style computes pairwise interactions for metals using a variant of modified embedded-atom method (MEAM) potentials [[(Lenosky)]{.std .std-ref}](#lenosky1){.reference .internal}. For a single species ("old-style") MEAM, the total energy E is given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & =\\sum\_{i\<j}\\phi(r\_{ij})+\\sum\_{i}U(n\_{i}) \\\\ n\_{i} & =\\sum\_{j}\\rho(r\_{ij})+\\sum\_{\\substack{j\<k,\\\\j,k\\neq i}}f(r\_{ij})f(r\_{ik})g\[\\cos(\\theta\_{jik})\]\\end{split}\\\]
:::

where [\\(\\rho_i\\)]{.math .notranslate .nohighlight} is the density at atom I, [\\(\\theta\_{jik}\\)]{.math .notranslate .nohighlight} is the angle between atoms J, I, and K centered on atom I. The five functions [\\(\\phi, U, \\rho, f,\\)]{.math .notranslate .nohighlight} and *g* are represented by cubic splines.

The *meam/spline* style also supports a new style multicomponent modified embedded-atom method (MEAM) potential [[(Zhang)]{.std .std-ref}](#zhang4){.reference .internal}, where the total energy E is given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E &= \\sum\_{i\<j}\\phi\_{ij}(r\_{ij})+\\sum\_{i}U_i(n\_{i}) \\\\ n\_{i} & = \\sum\_{j\\ne i}\\rho_j(r\_{ij})+\\sum\_{\\substack{j\<k,\\\\j,k\\neq i}}f\_{j}(r\_{ij})f\_{k}(r\_{ik})g\_{jk}\[\\cos(\\theta\_{jik})\]\\end{split}\\\]
:::

where the five functions [\\(\\phi, U, \\rho, f,\\)]{.math .notranslate .nohighlight} and *g* depend on the chemistry of the atoms in the interaction. In particular, if there are N different chemistries, there are N different *U*, [\\(\\rho\\)]{.math .notranslate .nohighlight}, and *f* functions, while there are N(N+1)/2 different [\\(\\phi\\)]{.math .notranslate .nohighlight} and *g* functions. The new style multicomponent MEAM potential files are indicated by the second line in the file starts with "meam/spline" followed by the number of elements and the name of each element.

The cutoffs and the coefficients for these spline functions are listed in a parameter file which is specified by the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command. Parameter files for different elements are included in the "potentials" directory of the LAMMPS distribution and have a ".meam.spline" file suffix. All of these files are parameterized in terms of LAMMPS [[metal units]{.doc}]units.md){.reference .internal}.

Note that unlike for other potentials, cutoffs for spline-based MEAM potentials are not set in the pair_style or pair_coeff command; they are specified in the potential files themselves.

Unlike the EAM pair style, which retrieves the atomic mass from the potential file, the spline-based MEAM potentials do not include mass information; thus you need to use the [[mass]{.doc}]mass.md){.reference .internal} command to specify it.

Only a single pair_coeff command is used with the *meam/spline* style which specifies a potential file with parameters for all needed elements. These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- N element names = mapping of spline-based MEAM elements to atom types

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for the potential file.

As an example, imagine the Ti.meam.spline file has values for Ti (old style). In that case your LAMMPS simulation may only have one atom type which has to be mapped to the Ti element as follows:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * Ti.meam.spline Ti
:::
::::

The first 2 arguments must be \* \* and there may be only one element following or NULL. Systems where there would be multiple atom types assigned to the same element are **not** supported by this pair style due to limitations in its implementation. If a mapping value is specified as NULL, the mapping is not performed. This can be used when a *meam/spline* potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials.

An example with a two component spline (new style) is TiO.meam.spline, where the command

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * TiO.meam.spline Ti O
:::
::::

will map the first atom type to Ti and the second atom type to O. Note in this case that the species names need to match exactly with the names of the elements in the TiO.meam.spline file; otherwise an error will be raised. This behavior is different than the old style MEAM files.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

The *meam/spline* pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in an external potential parameter file. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

The *meam/spline* pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

This pair style does not support mapping multiple atom types to the same element.

This pair style is only enabled if LAMMPS was built with the MANYBODY package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style meam]{.doc}]pair_meam.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Lenosky)** Lenosky, Sadigh, Alonso, Bulatov, de la Rubia, Kim, Voter, Kress, Modelling Simulation Materials Science Engineering, 8, 825 (2000).

**(Zhang)** Zhang and Trinkle, Computational Materials Science, 124, 204-210 (2016).
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

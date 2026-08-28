:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#pair-style-meam-sw-spline-command .section}
[]{#index-0}

# pair_style meam/sw/spline command[](#pair-style-meam-sw-spline-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style meam/sw/spline
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style meam/sw/spline
    pair_coeff * * Ti.meam.sw.spline Ti
    pair_coeff * * Ti.meam.sw.spline Ti Ti Ti
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *meam/sw/spline* style computes pairwise interactions for metals using a variant of modified embedded-atom method (MEAM) potentials [[(Lenosky)]{.std .std-ref}](#lenosky2){.reference .internal} with an additional Stillinger-Weber (SW) term [[(Stillinger)]{.std .std-ref}](#stillinger1){.reference .internal} in the energy. This form of the potential was first proposed by Nicklas, Fellinger, and Park [[(Nicklas)]{.std .std-ref}](#nicklas){.reference .internal}. We refer to it as MEAM+SW. The total energy E is given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = E\_{MEAM} + E\_{SW} \\\\ E\_{MEAM} & = \\sum \_{IJ} \\phi (r\_{IJ}) + \\sum \_{I} U(\\rho \_I) \\\\ E\_{SW} & = \\sum \_{I} \\sum \_{JK} F(r\_{IJ}) \\, F(r\_{IK}) \\, G(\\cos(\\theta \_{JIK})) \\\\ \\rho \_I & = \\sum \_J \\rho(r\_{IJ}) + \\sum \_{JK} f(r\_{IJ}) \\, f(r\_{IK}) \\, g(\\cos(\\theta \_{JIK}))\\end{split}\\\]
:::

where [\\(\\rho_I\\)]{.math .notranslate .nohighlight} is the density at atom I, [\\(\\theta\_{JIK}\\)]{.math .notranslate .nohighlight} is the angle between atoms J, I, and K centered on atom I. The seven functions [\\(\\phi, F, G, U, \\rho, f,\\)]{.math .notranslate .nohighlight} and *g* are represented by cubic splines.

The cutoffs and the coefficients for these spline functions are listed in a parameter file which is specified by the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command. Parameter files for different elements are included in the "potentials" directory of the LAMMPS distribution and have a ".meam.sw.spline" file suffix. All of these files are parameterized in terms of LAMMPS [[metal units]{.doc}]units.md){.reference .internal}.

Note that unlike for other potentials, cutoffs for spline-based MEAM+SW potentials are not set in the pair_style or pair_coeff command; they are specified in the potential files themselves.

Unlike the EAM pair style, which retrieves the atomic mass from the potential file, the spline-based MEAM+SW potentials do not include mass information; thus you need to use the [[mass]{.doc}]mass.md){.reference .internal} command to specify it.

Only a single pair_coeff command is used with the meam/sw/spline style which specifies a potential file with parameters for all needed elements. These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- N element names = mapping of spline-based MEAM+SW elements to atom types

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for the potential file.

As an example, imagine the Ti.meam.sw.spline file has values for Ti. If your LAMMPS simulation has 3 atoms types and they are all to be treated with this potential, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * Ti.meam.sw.spline Ti Ti Ti
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The three Ti arguments map LAMMPS atom types 1,2,3 to the Ti element in the potential file. If a mapping value is specified as NULL, the mapping is not performed. This can be used when a *meam/sw/spline* potential is used as part of the hybrid pair style. The NULL values are placeholders for atom types that will be used with other potentials.

::: {.admonition .note}
Note

The *meam/sw/spline* style currently supports only single-element MEAM+SW potentials. It may be extended for alloy systems in the future.
:::

Example input scripts that use this pair style are provided in the examples/PACKAGES/meam_sw_spline directory.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

The pair style does not support multiple element types or mixing. It has been designed for pure elements only.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

The *meam/sw/spline* pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in an external potential parameter file. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

The *meam/sw/spline* pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

This pair style is only enabled if LAMMPS was built with the MANYBODY package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style meam]{.doc}]pair_meam.md){.reference .internal}, [[pair_style meam/spline]{.doc}]pair_meam_spline.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Lenosky)** Lenosky, Sadigh, Alonso, Bulatov, de la Rubia, Kim, Voter, Kress, Modell. Simul. Mater. Sci. Eng. 8, 825 (2000).

**(Stillinger)** Stillinger, Weber, Phys. Rev. B 31, 5262 (1985).

**(Nicklas)** The spline-based MEAM+SW format was first devised and used to develop potentials for bcc transition metals by Jeremy Nicklas, Michael Fellinger, and Hyoungki Park at The Ohio State University.
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

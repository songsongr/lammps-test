:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#pair-style-colloid-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style colloid command[](#pair-style-colloid-command "Link to this heading"){.headerlink}

Accelerator Variants: *colloid/gpu*, *colloid/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style colloid cutoff
:::
::::

- cutoff = global cutoff for colloidal interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style colloid 10.0
    pair_coeff * *  25 1.0 10.0 10.0
    pair_coeff 1 1 144 1.0 0.0 0.0 3.0
    pair_coeff 1 2  75.398 1.0 0.0 10.0 9.0
    pair_coeff 2 2  39.478 1.0 10.0 10.0 25.0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *colloid* computes pairwise interactions between large colloidal particles and small solvent particles using 3 formulas. A colloidal particle has a size \> sigma; a solvent particle is the usual Lennard-Jones particle of size sigma.

The colloid-colloid interaction energy is given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split} U_A = & - \\frac{A\_{cc}}{6} \\left\[ \\frac{2 a_1 a_2}{r\^2-\\left(a_1+a_2\\right)\^2} + \\frac{2 a_1 a_2}{r\^2 - \\left(a_1 - a_2\\right)\^2} + \\mathrm{ln} \\left( \\frac{r\^2-\\left(a_1+a_2\\right)\^2}{r\^2-\\left(a_1-a_2\\right)\^2} \\right) \\right\] \\\\ & \\\\ U_R = & \\frac{A\_{cc}}{37800} \\frac{\\sigma\^6}{r} \\biggl\[ \\frac{r\^2-7r\\left(a_1+a_2\\right)+6\\left(a_1\^2+7a_1a_2+a_2\^2\\right)} {\\left(r-a_1-a_2\\right)\^7} \\\\ &\\qquad +\\frac{r\^2+7r\\left(a_1+a_2\\right)+6\\left(a_1\^2+7a_1a_2+a_2\^2\\right)} {\\left(r+a_1+a_2\\right)\^7} \\\\ &\\qquad -\\frac{r\^2+7r\\left(a_1-a_2\\right)+6\\left(a_1\^2-7a_1a_2+a_2\^2\\right)} {\\left(r+a_1-a_2\\right)\^7} \\\\ &\\qquad \\left. -\\frac{r\^2-7r\\left(a_1-a_2\\right)+6\\left(a_1\^2-7a_1a_2+a_2\^2\\right)} {\\left(r-a_1+a_2\\right)\^7} \\right\] \\\\ & \\\\ U = & U_A + U_R, \\qquad r \< r_c\\end{split}\\\]
:::

where [\\(A\_{cc}\\)]{.math .notranslate .nohighlight} is the Hamaker constant, [\\(a_1\\)]{.math .notranslate .nohighlight} and [\\(a_2\\)]{.math .notranslate .nohighlight} are the radii of the two colloidal particles, and [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff. This equation results from describing each colloidal particle as an integrated collection of Lennard-Jones particles of size sigma and is derived in [[(Everaers)]{.std .std-ref}](#everaers1){.reference .internal}.

The colloid-solvent interaction energy is given by

::: {.math .notranslate .nohighlight}
\\\[U = \\frac{2 \~ a\^3 \~ \\sigma\^3 \~ A\_{cs}}{9 \\left( a\^2 - r\^2 \\right)\^3} \\left\[ 1 - \\frac{\\left(5 \~ a\^6+45\~a\^4\~r\^2+63\~a\^2\~r\^4+15\~r\^6\\right) \\sigma\^6} {15 \\left(a-r\\right)\^6 \\left( a+r \\right)\^6} \\right\], \\quad r \< r_c\\\]
:::

where [\\(A\_{cs}\\)]{.math .notranslate .nohighlight} is the Hamaker constant, *a* is the radius of the colloidal particle, and [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff. This formula is derived from the colloid-colloid interaction, letting one of the particle sizes go to zero.

The solvent-solvent interaction energy is given by the usual Lennard-Jones formula

::: {.math .notranslate .nohighlight}
\\\[U = \\frac{A\_{ss}}{36} \\left\[ \\left( \\frac{\\sigma}{r} \\right)\^{12} - \\left( \\frac{ \\sigma}{r} \\right)\^6 \\right\], \\quad r \< r_c\\\]
:::

with [\\(A\_{ss}\\)]{.math .notranslate .nohighlight} set appropriately, which results from letting both particle sizes go to zero.

When used in combination with [[pair_style yukawa/colloid]{.doc}]pair_yukawa_colloid.md){.reference .internal}, the two terms become the so-called DLVO potential, which combines electrostatic repulsion and van der Waals attraction.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- A (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- d1 (distance units)

- d2 (distance units)

- cutoff (distance units)

A is the Hamaker energy prefactor and should typically be set as follows:

- [\\(A\_{cc}\\)]{.math .notranslate .nohighlight} = colloid/colloid = [\\(4 \\pi\^2 = 39.5\\)]{.math .notranslate .nohighlight}

- [\\(A\_{cs}\\)]{.math .notranslate .nohighlight} = colloid/solvent = [\\(\\sqrt{A\_{cc} A\_{ss}}\\)]{.math .notranslate .nohighlight}

- [\\(A\_{ss}\\)]{.math .notranslate .nohighlight} = solvent/solvent = 144 (assuming epsilon = 1, so that 144/36 = 4)

[\\(\\sigma\\)]{.math .notranslate .nohighlight} is the size of the solvent particle or the constituent particles integrated over in the colloidal particle and should typically be set as follows:

- [\\(\\sigma\_{cc}\\)]{.math .notranslate .nohighlight} = colloid/colloid = 1.0

- [\\(\\sigma\_{cs}\\)]{.math .notranslate .nohighlight} = colloid/solvent = arithmetic mixing between colloid [\\(\\sigma\\)]{.math .notranslate .nohighlight} and solvent [\\(\\sigma\\)]{.math .notranslate .nohighlight}

- [\\(\\sigma\_{ss}\\)]{.math .notranslate .nohighlight} = solvent/solvent = 1.0 or whatever size the solvent particle is

Thus typically [\\(\\sigma\_{cs} = 1.0\\)]{.math .notranslate .nohighlight}, unless the solvent particle's size != 1.0.

D1 and d2 are particle diameters, so that d1 = 2\*a1 and d2 = 2\*a2 in the formulas above. Both d1 and d2 must be values \>= 0. If d1 \> 0 and d2 \> 0, then the pair interacts via the colloid-colloid formula above. If d1 = 0 and d2 = 0, then the pair interacts via the solvent-solvent formula. I.e. a d value of 0 is a Lennard-Jones particle of size [\\(\\sigma\\)]{.math .notranslate .nohighlight}. If either d1 = 0 or d2 = 0 and the other is larger, then the pair interacts via the colloid-solvent formula.

Note that the diameter of a particular particle type may appear in multiple pair_coeff commands, as it interacts with other particle types. You should ensure the particle diameter is specified consistently each time it appears.

The last coefficient is optional. If not specified, the global cutoff specified in the pair_style command is used. However, you typically want different cutoffs for interactions between different particle sizes. E.g. if colloidal particles of diameter 10 are used with solvent particles of diameter 1, then a solvent-solvent cutoff of 2.5 would correspond to a colloid-colloid cutoff of 25. A good rule-of-thumb is to use a colloid-solvent cutoff that is half the big diameter + 4 times the small diameter. I.e. 9 = 5 + 4 for the colloid-solvent cutoff in this case.

::: {.admonition .note}
Note

When using pair_style colloid for a mixture with 2 (or more) widely different particles sizes (e.g. sigma=10 colloids in a background sigma=1 LJ fluid), you will likely want to use these commands for efficiency: [[neighbor multi]{.doc}]neighbor.md){.reference .internal} and [[comm_modify multi]{.doc}]comm_modify.md){.reference .internal}.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the A, sigma, d1, and d2 coefficients and cutoff distance for this pair style can be mixed. A is an energy value mixed like a LJ epsilon. D1 and d2 are distance values and are mixed like sigma. The default mix value is *geometric*. See the "pair_modify" command for details.

This pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This style is part of the COLLOID package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Normally, this pair style should be used with finite-size particles which have a diameter, e.g. see the [[atom_style sphere]{.doc}]atom_style.md){.reference .internal} command. However, this is not a requirement, since the only definition of particle size is via the pair_coeff parameters for each type. In other words, the physical radius of the particle is ignored. Thus you should ensure that the d1,d2 parameters you specify are consistent with the physical size of the particles of that type.

Per-particle polydispersity is not yet supported by this pair style; only per-type polydispersity is enabled via the pair_coeff parameters.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Everaers)** Everaers, Ejtehadi, Phys Rev E, 67, 041710 (2003).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

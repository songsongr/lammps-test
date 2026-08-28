:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#pair-style-resquared-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style resquared command[](#pair-style-resquared-command "Link to this heading"){.headerlink}

Accelerator Variants: *resquared/gpu*, *resquared/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style resquared cutoff
:::
::::

- cutoff = global cutoff for interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style resquared 10.0
    pair_coeff * * 1.0 1.0 1.7 3.4 3.4 1.0 1.0 1.0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *resquared* computes the RE-squared anisotropic interaction [[(Everaers)]{.std .std-ref}](#everaers3){.reference .internal}, [[(Babadi)]{.std .std-ref}](#babadi){.reference .internal} between pairs of ellipsoidal and/or spherical Lennard-Jones particles. For ellipsoidal interactions, the potential considers the ellipsoid as being comprised of small spheres of size [\\(\\sigma\\)]{.math .notranslate .nohighlight}. LJ particles are a single sphere of size [\\(\\sigma\\)]{.math .notranslate .nohighlight}. The distinction is made to allow the pair style to make efficient calculations of ellipsoid/solvent interactions.

Details for the equations used are given in the references below and in [this supplementary document](PDF/pair_resquared_extra.pdf){.reference .external}.

Use of this pair style requires the NVE, NVT, or NPT fixes with the *asphere* extension (e.g. [[fix nve/asphere]{.doc}]fix_nve_asphere.md){.reference .internal}) in order to integrate particle rotation. Additionally, [[atom_style ellipsoid]{.doc}]atom_style.md){.reference .internal} should be used since it defines the rotational state and the size and shape of each ellipsoidal particle.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- A12 = Energy Prefactor/Hamaker constant (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} = atomic interaction diameter (distance units)

- [\\(\\epsilon\_{i,a}\\)]{.math .notranslate .nohighlight} = relative well depth of type I for side-to-side interactions

- [\\(\\epsilon\_{i,b}\\)]{.math .notranslate .nohighlight} = relative well depth of type I for face-to-face interactions

- [\\(\\epsilon\_{i,c}\\)]{.math .notranslate .nohighlight} = relative well depth of type I for end-to-end interactions

- [\\(\\epsilon\_{j,a}\\)]{.math .notranslate .nohighlight} = relative well depth of type J for side-to-side interactions

- [\\(\\epsilon\_{j,b}\\)]{.math .notranslate .nohighlight} = relative well depth of type J for face-to-face interactions

- [\\(\\epsilon\_{j,c}\\)]{.math .notranslate .nohighlight} = relative well depth of type J for end-to-end interactions

- cutoff (distance units)

The parameters used depend on the type of the interacting particles, i.e. ellipsoids or LJ spheres. The type of a particle is determined by the diameters specified for its 3 shape parameters. If all 3 shape parameters = 0.0, then the particle is treated as an LJ sphere. The [\\(\\epsilon\_{i,\*}\\)]{.math .notranslate .nohighlight} or [\\(\\epsilon\_{j,\*}\\)]{.math .notranslate .nohighlight} parameters are ignored for LJ spheres. If the 3 shape parameters are \> 0.0, then the particle is treated as an ellipsoid (even if the 3 parameters are equal to each other).

A12 specifies the energy prefactor which depends on the types of the two interacting particles.

For ellipsoid/ellipsoid interactions, the interaction is computed by the formulas in the supplementary document referenced above. A12 is the Hamaker constant as described in [[(Everaers)]{.std .std-ref}](#everaers3){.reference .internal}. In LJ units:

::: {.math .notranslate .nohighlight}
\\\[A\_{12} = 4\\pi\^2\\epsilon\_{\\mathrm{LJ}}(\\rho\\sigma\^3)\^2\\\]
:::

where [\\(\\rho\\)]{.math .notranslate .nohighlight} gives the number density of the spherical particles composing the ellipsoids and [\\(\\epsilon\_{\\mathrm{LJ}}\\)]{.math .notranslate .nohighlight} determines the interaction strength of the spherical particles.

For ellipsoid/LJ sphere interactions, the interaction is also computed by the formulas in the supplementary document referenced above. A12 has a modified form (see [here](PDF/pair_resquared_extra.pdf){.reference .external} for details):

::: {.math .notranslate .nohighlight}
\\\[A\_{12} = 4\\pi\^2\\epsilon\_{\\mathrm{LJ}}(\\rho\\sigma\^3)\\\]
:::

For ellipsoid/LJ sphere interactions, a correction to the distance- of-closest approach equation has been implemented to reduce the error from two particles of disparate sizes; see [this supplementary document](PDF/pair_resquared_extra.pdf){.reference .external}.

For LJ sphere/LJ sphere interactions, the interaction is computed using the standard Lennard-Jones formula, which is much cheaper to compute than the ellipsoidal formulas. A12 is used as epsilon in the standard LJ formula:

::: {.math .notranslate .nohighlight}
\\\[A\_{12} = \\epsilon\_{\\mathrm{LJ}}\\\]
:::

and the specified [\\(\\sigma\\)]{.math .notranslate .nohighlight} is used as the [\\(\\sigma\\)]{.math .notranslate .nohighlight} in the standard LJ formula.

When one of both of the interacting particles are ellipsoids, then [\\(\\sigma\\)]{.math .notranslate .nohighlight} specifies the diameter of the continuous distribution of constituent particles within each ellipsoid used to model the RE-squared potential. Note that this is a different meaning for [\\(\\sigma\\)]{.math .notranslate .nohighlight} than the [[pair_style gayberne]{.doc}]pair_gayberne.md){.reference .internal} potential uses.

The [\\(\\epsilon_i\\)]{.math .notranslate .nohighlight} and [\\(\\epsilon_j\\)]{.math .notranslate .nohighlight} coefficients are defined for atom types, not for pairs of atom types. Thus, in a series of pair_coeff commands, they only need to be specified once for each atom type.

Specifically, if any of [\\(\\epsilon\_{i,a}\\)]{.math .notranslate .nohighlight}, [\\(\\epsilon\_{i,b}\\)]{.math .notranslate .nohighlight}, [\\(\\epsilon\_{i,c}\\)]{.math .notranslate .nohighlight} are non-zero, the three values are assigned to atom type I. If all the [\\(\\epsilon_i\\)]{.math .notranslate .nohighlight} values are zero, they are ignored. If any of [\\(\\epsilon\_{j,a}\\)]{.math .notranslate .nohighlight}, [\\(\\epsilon\_{j,b}\\)]{.math .notranslate .nohighlight}, [\\(\\epsilon\_{j,c}\\)]{.math .notranslate .nohighlight} are non-zero, the three values are assigned to atom type J. If all three [\\(\\epsilon_i\\)]{.math .notranslate .nohighlight} values are zero, they are ignored. Thus the typical way to define the [\\(\\epsilon_i\\)]{.math .notranslate .nohighlight} and [\\(\\epsilon_j\\)]{.math .notranslate .nohighlight} coefficients is to list their values in "pair_coeff I J" commands when I = J, but set them to 0.0 when I != J. If you do list them when I != J, you should ensure they are consistent with their values in other pair_coeff commands.

Note that if this potential is being used as a sub-style of [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal}, and there is no "pair_coeff I I" setting made for RE-squared for a particular type I (because I-I interactions are computed by another hybrid pair potential), then you still need to ensure the epsilon a,b,c coefficients are assigned to that type in a "pair_coeff I J" command.

For large uniform molecules it has been shown that the [\\(\\epsilon\_{\*,\*}\\)]{.math .notranslate .nohighlight} energy parameters are approximately representable in terms of local contact curvatures [[(Everaers)]{.std .std-ref}](#everaers3){.reference .internal}:

::: {.math .notranslate .nohighlight}
\\\[\\epsilon_a = \\sigma \\cdot { \\frac{a}{ b \\cdot c } }; \\epsilon_b = \\sigma \\cdot { \\frac{b}{ a \\cdot c } }; \\epsilon_c = \\sigma \\cdot { \\frac{c}{ a \\cdot b } }\\\]
:::

where a, b, and c give the particle diameters.

The last coefficient is optional. If not specified, the global cutoff specified in the pair_style command is used.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon and sigma coefficients and cutoff distance can be mixed, but only for sphere pairs. The default mix value is *geometric*. See the "pair_modify" command for details. Other type pairs cannot be mixed, due to the different meanings of the energy prefactors used to calculate the interactions and the implicit dependence of the ellipsoid-sphere interaction on the equation for the Hamaker constant presented here. Mixing of sigma and epsilon followed by calculation of the energy prefactors using the equations above is recommended.

This pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the Lennard-Jones portion of the pair interaction, but only for sphere-sphere interactions. There is no shifting performed for ellipsoidal interactions due to the anisotropic dependence of the interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords of the [[run_style command]{.doc}]run_style.md){.reference .internal}.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This style is part of the ASPHERE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair style requires that atoms be ellipsoids as defined by the [[atom_style ellipsoid]{.doc}]atom_style.md){.reference .internal} command.

Particles acted on by the potential can be finite-size aspherical or spherical particles, or point particles. Spherical particles have all 3 of their shape parameters equal to each other. Point particles have all 3 of their shape parameters equal to 0.0.

The distance-of-closest-approach approximation used by LAMMPS becomes less accurate when high-aspect ratio ellipsoids are used.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix nve/asphere]{.doc}]fix_nve_asphere.md){.reference .internal}, [[compute temp/asphere]{.doc}]compute_temp_asphere.md){.reference .internal}, [[pair_style gayberne]{.doc}]pair_gayberne.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Everaers)** Everaers and Ejtehadi, Phys Rev E, 67, 041710 (2003).

**(Babadi)** Babadi, Ejtehadi, Everaers, J Comp Phys, 219, 770-779 (2006).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

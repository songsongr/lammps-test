::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#pair-style-gayberne-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style gayberne command[](#pair-style-gayberne-command "Link to this heading"){.headerlink}

Accelerator Variants: *gayberne/gpu*, *gayberne/intel*, *gayberne/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style gayberne gamma upsilon mu cutoff
:::
::::

- gamma = shift for potential minimum (typically 1)

- upsilon = exponent for eta orientation-dependent energy function

- mu = exponent for chi orientation-dependent energy function

- cutoff = global cutoff for interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style gayberne 1.0 1.0 1.0 10.0
    pair_coeff * * 1.0 1.7 1.7 3.4 3.4 1.0 1.0 1.0
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *gayberne* styles compute a Gay-Berne anisotropic LJ interaction [[(Berardi)]{.std .std-ref}](#berardi){.reference .internal} between pairs of ellipsoidal particles or an ellipsoidal and spherical particle via the formulas

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}U ( \\mathbf{A}\_1, \\mathbf{A}\_2, \\mathbf{r}\_{12} ) = & U_r ( \\mathbf{A}\_1, \\mathbf{A}\_2, \\mathbf{r}\_{12}, \\gamma ) \\cdot \\eta\_{12} ( \\mathbf{A}\_1, \\mathbf{A}\_2, \\upsilon ) \\cdot \\chi\_{12} ( \\mathbf{A}\_1, \\mathbf{A}\_2, \\mathbf{r}\_{12}, \\mu ) \\\\ U_r = & 4 \\epsilon ( \\varrho\^{12} - \\varrho\^6) \\\\ \\varrho = & \\frac{\\sigma}{ h\_{12} + \\gamma \\sigma}\\end{split}\\\]
:::

where [\\(\\mathbf{A}\_1\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{A}\_2\\)]{.math .notranslate .nohighlight} are the transformation matrices from the simulation box frame to the body frame and [\\(r\_{12}\\)]{.math .notranslate .nohighlight} is the center to center vector between the particles. [\\(U_r\\)]{.math .notranslate .nohighlight} controls the shifted distance dependent interaction based on the distance of closest approach of the two particles ([\\(h\_{12}\\)]{.math .notranslate .nohighlight}) and the user-specified shift parameter [\\(\\gamma\\)]{.math .notranslate .nohighlight}. When both particles are spherical, the formula reduces to the usual Lennard-Jones interaction (see details below for when Gay-Berne treats a particle as "spherical").

For large uniform molecules it has been shown that the energy parameters are approximately representable in terms of local contact curvatures [[(Everaers)]{.std .std-ref}](#everaers2){.reference .internal}:

::: {.math .notranslate .nohighlight}
\\\[\\epsilon_a = \\sigma \\cdot { \\frac{a}{ b \\cdot c } }; \\epsilon_b = \\sigma \\cdot { \\frac{b}{ a \\cdot c } }; \\epsilon_c = \\sigma \\cdot { \\frac{c}{ a \\cdot b } }\\\]
:::

The variable names utilized as potential parameters are for the most part taken from [[(Everaers)]{.std .std-ref}](#everaers2){.reference .internal} in order to be consistent with the [[RE-squared pair potential]{.doc}]pair_resquared.md){.reference .internal}. Details on the upsilon and mu parameters are given [here](PDF/pair_resquared_extra.pdf){.reference .external}.

More details of the Gay-Berne formulation are given in the references listed below and in [this supplementary document](PDF/pair_gayberne_extra.pdf){.reference .external}.

Use of this pair style requires the NVE, NVT, or NPT fixes with the *asphere* extension (e.g. [[fix nve/asphere]{.doc}]fix_nve_asphere.md){.reference .internal}) in order to integrate particle rotation. Additionally, [[atom_style ellipsoid]{.doc}]atom_style.md){.reference .internal} should be used since it defines the rotational state and the size and shape of each ellipsoidal particle.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} = well depth (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} = minimum effective particle radii (distance units)

- [\\(\\epsilon\_{i,a}\\)]{.math .notranslate .nohighlight} = relative well depth of type I for side-to-side interactions

- [\\(\\epsilon\_{i,b}\\)]{.math .notranslate .nohighlight} = relative well depth of type I for face-to-face interactions

- [\\(\\epsilon\_{i,c}\\)]{.math .notranslate .nohighlight} = relative well depth of type I for end-to-end interactions

- [\\(\\epsilon\_{j,a}\\)]{.math .notranslate .nohighlight} = relative well depth of type J for side-to-side interactions

- [\\(\\epsilon\_{j,b}\\)]{.math .notranslate .nohighlight} = relative well depth of type J for face-to-face interactions

- [\\(\\epsilon\_{j,c}\\)]{.math .notranslate .nohighlight} = relative well depth of type J for end-to-end interactions

- cutoff (distance units)

The last coefficient is optional. If not specified, the global cutoff specified in the pair_style command is used.

It is typical with the Gay-Berne potential to define [\\(\\sigma\\)]{.math .notranslate .nohighlight} as the minimum of the 3 shape diameters of the particles involved in an I,I interaction, though this is not required. Note that this is a different meaning for [\\(\\sigma\\)]{.math .notranslate .nohighlight} than the [[pair_style resquared]{.doc}]pair_resquared.md){.reference .internal} potential uses.

The [\\(\\epsilon_i\\)]{.math .notranslate .nohighlight} and [\\(\\epsilon_j\\)]{.math .notranslate .nohighlight} coefficients are actually defined for atom types, not for pairs of atom types. Thus, in a series of pair_coeff commands, they only need to be specified once for each atom type.

Specifically, if any of [\\(\\epsilon\_{i,a}\\)]{.math .notranslate .nohighlight}, [\\(\\epsilon\_{i,b}\\)]{.math .notranslate .nohighlight}, [\\(\\epsilon\_{i,c}\\)]{.math .notranslate .nohighlight} are non-zero, the three values are assigned to atom type I. If all the [\\(\\epsilon_i\\)]{.math .notranslate .nohighlight} values are zero, they are ignored. If any of [\\(\\epsilon\_{j,a}\\)]{.math .notranslate .nohighlight}, [\\(\\epsilon\_{j,b}\\)]{.math .notranslate .nohighlight}, [\\(\\epsilon\_{j,c}\\)]{.math .notranslate .nohighlight} are non-zero, the three values are assigned to atom type J. If all three epsilon_j values are zero, they are ignored. Thus the typical way to define the [\\(\\epsilon_i\\)]{.math .notranslate .nohighlight} and [\\(\\epsilon_j\\)]{.math .notranslate .nohighlight} coefficients is to list their values in "pair_coeff I J" commands when I = J, but set them to 0.0 when I != J. If you do list them when I != J, you should ensure they are consistent with their values in other pair_coeff commands, since only the last setting will be in effect.

Note that if this potential is being used as a sub-style of [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal}, and there is no "pair_coeff I I" setting made for Gay-Berne for a particular type I (because I-I interactions are computed by another hybrid pair potential), then you still need to ensure the [\\(\\epsilon\\)]{.math .notranslate .nohighlight} a,b,c coefficients are assigned to that type. e.g. in a "pair_coeff I J" command.

::: {.admonition .note}
Note

If the [\\(\\epsilon\_{a}\\)]{.math .notranslate .nohighlight} = [\\(\\epsilon\_{b}\\)]{.math .notranslate .nohighlight} = [\\(\\epsilon\_{c}\\)]{.math .notranslate .nohighlight} for an atom type, and if the shape of the particle itself is spherical, meaning its 3 shape parameters are all the same, then the particle is treated as an LJ sphere by the Gay-Berne potential. This is significant because if two LJ spheres interact, then the simple Lennard-Jones formula is used to compute their interaction energy/force using the specified epsilon and sigma as the standard LJ parameters. This is much cheaper to compute than the full Gay-Berne formula. To treat the particle as a LJ sphere with sigma = D, you should normally set [\\(\\epsilon\_{a}\\)]{.math .notranslate .nohighlight} = [\\(\\epsilon\_{b}\\)]{.math .notranslate .nohighlight} = [\\(\\epsilon\_{c}\\)]{.math .notranslate .nohighlight} = 1.0, set the pair_coeff [\\(\\sigma = D\\)]{.math .notranslate .nohighlight}, and also set the 3 shape parameters for the particle to D. The one exception is that if the 3 shape parameters are set to 0.0, which is a valid way in LAMMPS to specify a point particle, then the Gay-Berne potential will treat that as shape parameters of 1.0 (i.e. a LJ particle with [\\(\\sigma = 1\\)]{.math .notranslate .nohighlight}), since it requires finite-size particles. In this case you should still set the pair_coeff [\\(\\sigma\\)]{.math .notranslate .nohighlight} to 1.0 as well.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon and sigma coefficients and cutoff distance for this pair style can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

This pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the Lennard-Jones portion of the pair interaction, but only for sphere-sphere interactions. There is no shifting performed for ellipsoidal interactions due to the anisotropic dependence of the interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *gayberne* style is part of the ASPHERE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

These pair styles require that atoms store torque and a quaternion to represent their orientation, as defined by the [[atom_style]{.doc}]atom_style.md){.reference .internal}. It also require they store a per-type [[shape]{.doc}]set.md){.reference .internal}. The particles cannot store a per-particle diameter.

This pair style requires that atoms be ellipsoids as defined by the [[atom_style ellipsoid]{.doc}]atom_style.md){.reference .internal} command.

Particles acted on by the potential can be finite-size aspherical or spherical particles, or point particles. Spherical particles have all 3 of their shape parameters equal to each other. Point particles have all 3 of their shape parameters equal to 0.0.

The Gay-Berne potential does not become isotropic as r increases [[(Everaers)]{.std .std-ref}](#everaers2){.reference .internal}. The distance-of-closest-approach approximation used by LAMMPS becomes less accurate when high-aspect ratio ellipsoids are used.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix nve/asphere]{.doc}]fix_nve_asphere.md){.reference .internal}, [[compute temp/asphere]{.doc}]compute_temp_asphere.md){.reference .internal}, [[pair_style resquared]{.doc}]pair_resquared.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Everaers)** Everaers and Ejtehadi, Phys Rev E, 67, 041710 (2003).

**(Berardi)** Berardi, Fava, Zannoni, Chem Phys Lett, 297, 8-14 (1998). Berardi, Muccioli, Zannoni, J Chem Phys, 128, 024905 (2008).

**(Perram)** Perram and Rasmussen, Phys Rev E, 54, 6565-6572 (1996).

**(Allen)** Allen and Germano, Mol Phys 104, 3225-3235 (2006).
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

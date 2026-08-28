:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-yukawa-colloid-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style yukawa/colloid command[](#pair-style-yukawa-colloid-command "Link to this heading"){.headerlink}

Accelerator Variants: *yukawa/colloid/gpu*, *yukawa/colloid/kk*, *yukawa/colloid/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style yukawa/colloid kappa cutoff
:::
::::

- kappa = screening length (inverse distance units)

- cutoff = global cutoff for colloidal Yukawa interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style yukawa/colloid 2.0 2.5
    pair_coeff 1 1 100.0 2.3
    pair_coeff * * 100.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *yukawa/colloid* computes pairwise interactions with the formula

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{A}{\\kappa} e\^{- \\kappa (r - (r_i + r_j))} \\qquad r \< r_c\\\]
:::

where [\\(r_i\\)]{.math .notranslate .nohighlight} and [\\(r_j\\)]{.math .notranslate .nohighlight} are the radii of the two particles and [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff.

In contrast to [[pair_style yukawa]{.doc}]pair_yukawa.md){.reference .internal}, this functional form arises from the Coulombic interaction between two colloid particles, screened due to the presence of an electrolyte, see the book by [[Safran]{.std .std-ref}](#safran){.reference .internal} for a derivation in the context of DLVO theory. [[Pair_style yukawa]{.doc}]pair_yukawa.md){.reference .internal} is a screened Coulombic potential between two point-charges and uses no such approximation.

This potential applies to nearby particle pairs for which the Derjagin approximation holds, meaning [\\(h \<\< r_i + r_j\\)]{.math .notranslate .nohighlight}, where *h* is the surface-to-surface separation of the two particles.

When used in combination with [[pair_style colloid]{.doc}]pair_colloid.md){.reference .internal}, the two terms become the so-called DLVO potential, which combines electrostatic repulsion and van der Waals attraction.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- A (energy/distance units)

- cutoff (distance units)

The prefactor A is determined from the relationship between surface charge and surface potential due to the presence of electrolyte. Note that the A for this potential style has different units than the A used in [[pair_style yukawa]{.doc}]pair_yukawa.md){.reference .internal}. For low surface potentials, i.e. less than about 25 mV, A can be written as:

::: {.math .notranslate .nohighlight}
\\\[A = 2 \\pi R\\varepsilon\\varepsilon_0 \\kappa \\psi\^2\\\]
:::

where

- *R* = colloid radius (distance units)

- [\\(\\varepsilon_0\\)]{.math .notranslate .nohighlight} = permittivity of free space (charge\^2/energy/distance units)

- [\\(\\varepsilon\\)]{.math .notranslate .nohighlight} = relative permittivity of fluid medium (dimensionless)

- [\\(\\kappa\\)]{.math .notranslate .nohighlight} = inverse screening length (1/distance units)

- [\\(\\psi\\)]{.math .notranslate .nohighlight} = surface potential (energy/charge units)

The last coefficient is optional. If not specified, the global yukawa/colloid cutoff is used.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the A coefficient and cutoff distance for this pair style can be mixed. A is an energy value mixed like a LJ epsilon. The default mix value is *geometric*. See the "pair_modify" command for details.

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

This pair style requires that atoms be finite-size spheres with a diameter, as defined by the [[atom_style sphere]{.doc}]atom_style.md){.reference .internal} command.

Per-particle polydispersity is not yet supported by this pair style; per-type polydispersity is allowed. This means all particles of the same type must have the same diameter. Each type can have a different diameter.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Safran)** Safran, Statistical Thermodynamics of Surfaces, Interfaces, And Membranes, Westview Press, ISBN: 978-0813340791 (2003).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-lj-pirani-command .section}
[]{#index-1}[]{#index-0}

# pair_style lj/pirani command[](#pair-style-lj-pirani-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/pirani/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/pirani cutoff
:::
::::

- lj/pirani = name of the pair style

- cutoff = global cutoff (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/pirani 10.0
    pair_coeff 1 1 4.0 7.0 6.0 3.5 0.0045
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 12Jun2025.]{.versionmodified .added}
:::

Pair style *lj/pirani* computes pairwise interactions from an Improved Lennard-Jones (ILJ) potential according to [[(Pirani)]{.std .std-ref}](#pirani){.reference .internal}. The ILJ force field is adequate to model both equilibrium and non-equilibrium properties of matter, in gaseous and condensed phases, and at gas-surface interfaces. In particular, its use improves the description of elementary process dynamics where the traditional Lennard-Jones (LJ) formulation is usually applied.

::: {.math .notranslate .nohighlight}
\\\[ \\begin{align}\\begin{aligned}\\begin{split} x = r/R_m \\\\ n_x = \\alpha\*x\^2 + \\beta \\\\ \\gamma \\equiv m \\\\\\end{split}\\\\V(x) = \\varepsilon \\cdot \\left( \\frac{\\gamma}{ n_x - \\gamma} \\left(\\frac{1}{x} \\right)\^{n_x} - \\frac{n_x}{n_x - \\gamma} \\left(\\frac{1}{x} \\right)\^{\\gamma} \\right) \\qquad r \< r_c\\end{aligned}\\end{align} \\\]
:::

[\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff.

An additional parameter, [\\(\\alpha\\)]{.math .notranslate .nohighlight}, has been introduced in order to be able to recover the traditional Lennard-Jones 12-6 with a specific choice of parameters. With [\\(R_m \\equiv r_0 = \\sigma \\cdot 2\^{1 / 6}\\)]{.math .notranslate .nohighlight}, [\\(\\alpha = 0\\)]{.math .notranslate .nohighlight}, [\\(\\beta = 12\\)]{.math .notranslate .nohighlight} and [\\(\\gamma = 6\\)]{.math .notranslate .nohighlight} it is straightforward to prove that LJ 12-6 is obtained. Also, it can be verified that using [\\(\\alpha= 4\\)]{.math .notranslate .nohighlight}, [\\(\\beta= 8\\)]{.math .notranslate .nohighlight} and [\\(\\gamma = 6\\)]{.math .notranslate .nohighlight}, at the equilibrium distance, the first and second derivatives of ILJ match those of LJ 12-6. The parameter [\\(R_m\\)]{.math .notranslate .nohighlight} corresponds to the equilibrium distance and [\\(\\epsilon\\)]{.math .notranslate .nohighlight} to the well depth.

This potential provides some advantages with respect to the standard LJ potential, as explained in [[(Pirani)]{.std .std-ref}](#pirani){.reference .internal}: it provides a more realistic description of the long range behavior and an attenuation of the hardness of the repulsive wall.

This force field can be used for neutral-neutral ([\\(\\gamma = 6\\)]{.math .notranslate .nohighlight}), ion-neutral ([\\(\\gamma = 4\\)]{.math .notranslate .nohighlight}) or ion-ion systems ([\\(\\gamma = 1\\)]{.math .notranslate .nohighlight}). Notice that this implementation does not include explicit electrostatic interactions. If these are desired, this pair style should be used along with a Coulomb pair style like [[pair styles coul/cut or coul/long]{.doc}]pair_coul.md){.reference .internal} by using [[pair style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} and a suitable [[kspace style]{.doc}]kspace_style.md){.reference .internal}, if needed.

As discussed in [[(Pirani)]{.std .std-ref}](#pirani){.reference .internal}, analysis of a variety of systems showed that [\\(\\alpha= 4\\)]{.math .notranslate .nohighlight} generally works very well. In some special cases (e.g. those involving very small multiple charged ions) this factor may take a slightly different value. The parameter [\\(\\beta\\)]{.math .notranslate .nohighlight} codifies the hardness (polarizability) of the interacting partners, and for neutral-neutral systems it usually ranges from 6 to 11. Moreover, the modulation of [\\(\\beta\\)]{.math .notranslate .nohighlight} can model additional interaction effects, such as charge transfer in the perturbative limit, and can mitigate the effect of some uncertainty in the data used to build up the potential function.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (dimensionless)

- [\\(\\beta\\)]{.math .notranslate .nohighlight} (dimensionless)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (dimensionless)

- [\\(R_m\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- cutoff (distance units)

The last coefficient is optional. If not specified, the global cutoff is used.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

This pair style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table options are not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style supports the use of the *inner*, *middle*, and *outer* keywords of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command, meaning the pairwise forces can be partitioned by distance at different levels of the rRESPA hierarchy. See the [[run_style]{.doc}]run_style.md){.reference .internal} command for details.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is only enabled if LAMMPS was built with the EXTRA-PAIR package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

- [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}

- [[pair_style lj/cut]{.doc}]pair_lj.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Pirani)** F. Pirani, S. Brizi, L. Roncaratti, P. Casavecchia, D. Cappelletti and F. Vecchiocattivi, Phys. Chem. Chem. Phys., 2008, 10, 5489-5503.
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

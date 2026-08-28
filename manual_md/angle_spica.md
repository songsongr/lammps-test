:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-spica-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# angle_style spica command[](#angle-style-spica-command "Link to this heading"){.headerlink}

Accelerator Variants: *spica/omp*, *spica/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style spica

    angle_style spica/omp
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style spica
    angle_coeff 1 300.0 107.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *spica* angle style is a combination of the harmonic angle potential,

::: {.math .notranslate .nohighlight}
\\\[E = K (\\theta - \\theta_0)\^2\\\]
:::

where [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is the equilibrium value of the angle and [\\(K\\)]{.math .notranslate .nohighlight} a prefactor, with the *repulsive* part of the non-bonded *lj/spica* pair style between the atoms 1 and 3. This angle potential is intended for coarse grained MD simulations with the SPICA (formerly called SDK) parameterization using the [[pair_style lj/spica]{.doc}]pair_spica.md){.reference .internal}. Relative to the pair_style *lj/spica*, however, the energy is shifted by [\\(\\epsilon\\)]{.math .notranslate .nohighlight}, to avoid sudden jumps. Note that the usual 1/2 factor is included in [\\(K\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

[\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence [\\(K\\)]{.math .notranslate .nohighlight} is effectively energy per radian\^2.

The required *lj/spica* parameters are extracted automatically from the pair_style.

Style *sdk*, the original implementation of style *spica*, is available for backward compatibility.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This angle style can only be used if LAMMPS was built with the CG-SPICA package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}, [[angle_style harmonic]{.doc}]angle_harmonic.md){.reference .internal}, [[pair_style lj/spica]{.doc}]pair_spica.md){.reference .internal}, [[pair_style lj/spica/coul/long]{.doc}]pair_spica.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

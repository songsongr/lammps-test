:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-cosine-shift-exp-command .section}
[]{#index-1}[]{#index-0}

# angle_style cosine/shift/exp command[](#angle-style-cosine-shift-exp-command "Link to this heading"){.headerlink}

Accelerator Variants: *cosine/shift/exp/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cosine/shift/exp
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cosine/shift/exp
    angle_coeff * 10.0 45.0 2.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *cosine/shift/exp* angle style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = -U\_{\\text{min}} \\frac{e\^{-a U(\\theta,\\theta_0)}-1}{e\^a-1} \\quad \\text{with} \\quad U(\\theta,\\theta_0) = -0.5 \\left(1+\\cos(\\theta-\\theta_0) \\right)\\\]
:::

where [\\(U\_{\\text{min}}\\)]{.math .notranslate .nohighlight}, [\\(\\theta\\)]{.math .notranslate .nohighlight}, and [\\(a\\)]{.math .notranslate .nohighlight} are defined for each angle type.

The potential is bounded between [\\(\[-U\_{\\text{min}}, 0\]\\)]{.math .notranslate .nohighlight} and the minimum is located at the angle [\\(\\theta_0\\)]{.math .notranslate .nohighlight}. The a parameter can be both positive or negative and is used to control the spring constant at the equilibrium.

The spring constant is given by [\\(k = A \\exp(A) U\_{\\text{min}} / \[2 (\\exp(a)-1)\]\\)]{.math .notranslate .nohighlight}. For [\\(a \> 3\\)]{.math .notranslate .nohighlight}, [\\(\\frac{k}{U\_{\\text{min}}} = \\frac{a}{2}\\)]{.math .notranslate .nohighlight} to better than 5% relative error. For negative values of the [\\(a\\)]{.math .notranslate .nohighlight} parameter, the spring constant is essentially zero, and anharmonic terms takes over. The potential is furthermore well behaved in the limit [\\(a \\rightarrow 0\\)]{.math .notranslate .nohighlight}, where it has been implemented to linear order in [\\(a\\)]{.math .notranslate .nohighlight} for [\\(a \< 0.001\\)]{.math .notranslate .nohighlight}. In this limit the potential reduces to the cosineshifted potential.

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(U_min\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta\\)]{.math .notranslate .nohighlight} (angle)

- [\\(A\\)]{.math .notranslate .nohighlight} (real number)

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This angle style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}, [[angle_style cosine/shift]{.doc}]angle_cosine_shift.md){.reference .internal}, [[dihedral_style cosine/shift/exp]{.doc}]dihedral_cosine_shift_exp.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

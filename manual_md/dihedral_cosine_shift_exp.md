:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#dihedral-style-cosine-shift-exp-command .section}
[]{#index-1}[]{#index-0}

# dihedral_style cosine/shift/exp command[](#dihedral-style-cosine-shift-exp-command "Link to this heading"){.headerlink}

Accelerator Variants: *cosine/shift/exp/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style cosine/shift/exp
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style cosine/shift/exp
    dihedral_coeff 1 10.0 45.0 2.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *cosine/shift/exp* dihedral style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = -U\_{min}\\frac{e\^{-a U(\\theta,\\theta_0)}-1}{e\^a-1} \\quad\\mbox{with}\\quad U(\\theta,\\theta_0)=-0.5 \\left(1+\\cos(\\theta-\\theta_0) \\right)\\\]
:::

where [\\(U\_{min}\\)]{.math .notranslate .nohighlight}, [\\(\\theta\\)]{.math .notranslate .nohighlight}, and [\\(a\\)]{.math .notranslate .nohighlight} are defined for each dihedral type.

The potential is bounded between [\\(\\left\[-U\_{min}:0\\right\]\\)]{.math .notranslate .nohighlight} and the minimum is located at the angle [\\(\\theta_0\\)]{.math .notranslate .nohighlight}. The a parameter can be both positive or negative and is used to control the spring constant at the equilibrium.

The spring constant is given by [\\(k=a e\^a \\frac{U\_{min}}{2 \\left(e\^a-1\\right)}\\)]{.math .notranslate .nohighlight}. For [\\(a\>3\\)]{.math .notranslate .nohighlight} and [\\(\\frac{k}{U\_{min}} = \\frac{a}{2}\\)]{.math .notranslate .nohighlight} to better than 5% relative error. For negative values of the a parameter, the spring constant is essentially zero, and anharmonic terms takes over. The potential is furthermore well behaved in the limit [\\(a \\rightarrow 0\\)]{.math .notranslate .nohighlight}, where it has been implemented to linear order in [\\(a\\)]{.math .notranslate .nohighlight} for [\\(a \< 0.001\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each dihedral type via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(U\_{min}\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta\\)]{.math .notranslate .nohighlight} (angle)

- [\\(a\\)]{.math .notranslate .nohighlight} (real number)

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This dihedral style can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}, [[angle_style cosine/shift/exp]{.doc}]angle_cosine_shift_exp.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

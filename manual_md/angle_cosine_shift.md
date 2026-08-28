:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-cosine-shift-command .section}
[]{#index-1}[]{#index-0}

# angle_style cosine/shift command[](#angle-style-cosine-shift-command "Link to this heading"){.headerlink}

Accelerator Variants: *cosine/shift/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cosine/shift
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cosine/shift
    angle_coeff * 10.0 45.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *cosine/shift* angle style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = -\\frac{U\_{\\text{min}}}{2} \\left\[ 1 + \\cos(\\theta-\\theta_0) \\right\]\\\]
:::

where [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is the equilibrium angle. The potential is bounded between [\\(-U\_{\\text{min}}\\)]{.math .notranslate .nohighlight} and zero. In the neighborhood of the minimum [\\(E = - U\_{\\text{min}} + U\_{\\text{min}}/4(\\theta - \\theta_0)\^2\\)]{.math .notranslate .nohighlight} hence the spring constant is [\\(\\frac{U\_{\\text{min}}}{2}\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(U\_{\\text{min}}\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta\\)]{.math .notranslate .nohighlight} (angle)

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

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}, [[angle_style cosine/shift/exp]{.doc}]angle_cosine_shift_exp.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-cosine-periodic-command .section}
[]{#index-1}[]{#index-0}

# angle_style cosine/periodic command[](#angle-style-cosine-periodic-command "Link to this heading"){.headerlink}

Accelerator Variants: *cosine/periodic/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cosine/periodic
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style cosine/periodic
    angle_coeff * 75.0 1 6
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *cosine/periodic* angle style uses the following potential, which may be particularly used for organometallic systems where [\\(n\\)]{.math .notranslate .nohighlight} = 4 might be used for an octahedral complex and [\\(n\\)]{.math .notranslate .nohighlight} = 3 might be used for a trigonal center:

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{2.0}{n\^2} \* C \\left\[ 1 - B(-1)\^n\\cos\\left( n\\theta\\right) \\right\]\\\]
:::

where [\\(C\\)]{.math .notranslate .nohighlight}, [\\(B\\)]{.math .notranslate .nohighlight} and [\\(n\\)]{.math .notranslate .nohighlight} are coefficients defined for each angle type.

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(C\\)]{.math .notranslate .nohighlight} (energy)

- [\\(B\\)]{.math .notranslate .nohighlight} = 1 or -1

- [\\(n\\)]{.math .notranslate .nohighlight} = 1, 2, 3, 4, 5 or 6 for periodicity

Note that the prefactor [\\(C\\)]{.math .notranslate .nohighlight} is specified as coefficient and not the overall force constant [\\(K = \\frac{2 C}{n\^2}\\)]{.math .notranslate .nohighlight}. When [\\(B = 1\\)]{.math .notranslate .nohighlight}, it leads to a minimum for the linear geometry. When [\\(B = -1\\)]{.math .notranslate .nohighlight}, it leads to a maximum for the linear geometry.

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

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

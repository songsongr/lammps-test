::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#improper-style-umbrella-command .section}
[]{#index-1}[]{#index-0}

# improper_style umbrella command[](#improper-style-umbrella-command "Link to this heading"){.headerlink}

Accelerator Variants: *umbrella/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style umbrella
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style umbrella
    improper_coeff 1 100.0 180.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *umbrella* improper style uses the following potential, which is commonly referred to as a classic inversion and used in the [[DREIDING]{.doc}]Howto_bioFF.md){.reference .internal} force field:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{1}{2}K\\left( \\frac{1}{\\sin\\omega_0}\\right) \^2 \\left( \\cos\\omega - \\cos\\omega_0\\right) \^2 \\qquad \\omega_0 \\neq 0\^o \\\\ E = & K\\left( 1-cos\\omega\\right) \\qquad \\omega_0 = 0\^o\\end{split}\\\]
:::

where [\\(K\\)]{.math .notranslate .nohighlight} is the force constant and [\\(\\omega\\)]{.math .notranslate .nohighlight} is the angle between the IL axis and the IJK plane:

![](_images/umbrella.jpg){.align-center}

If [\\(\\omega_0 = 0\\)]{.math .notranslate .nohighlight} the potential term has a minimum for the planar structure. Otherwise it has two minima at [\\(\\omega +/- \\omega_0\\)]{.math .notranslate .nohighlight}, with a barrier in between.

See [[(Mayo)]{.std .std-ref}](#umbrella-mayo){.reference .internal} for a description of the DREIDING force field.

The following coefficients must be defined for each improper type via the [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\omega_0\\)]{.math .notranslate .nohighlight} (degrees)

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#symmetry-convention .section}
## Symmetry convention[](#symmetry-convention "Link to this heading"){.headerlink}

For the *umbrella* improper style, the first and fourth atoms in the quadruplet are atoms of symmetry; only the second and third atoms are considered interchangeable. This convention is relevant for operations that require knowledge of how atoms are ordered, such as automatic assignment of new improper types by [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This improper style can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[improper_coeff]{.doc}]improper_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Mayo)** Mayo, Olfason, Goddard III, J Phys Chem, 94, 8897-8909 (1990),
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

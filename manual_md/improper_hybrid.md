::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#improper-style-hybrid-command .section}
[]{#index-1}[]{#index-0}

# improper_style hybrid command[](#improper-style-hybrid-command "Link to this heading"){.headerlink}

Accelerator Variants: *hybrid/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style hybrid style1 style2 ...
:::
::::

- style1,style2 = list of one or more improper styles
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style hybrid harmonic cvff
    improper_coeff 1 harmonic 120.0 30
    improper_coeff 2 cvff 20.0 -1 2
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *hybrid* style enables the use of multiple improper styles in one simulation. An improper style is assigned to each improper type. For example, impropers in a polymer flow (of improper type 1) could be computed with a *harmonic* potential and impropers in the wall boundary (of improper type 2) could be computed with a *cvff* potential. The assignment of improper type to style is made via the [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command or in the data file.

In the improper_coeff command, the first coefficient sets the improper style and the remaining coefficients are those appropriate to that style. In the example above, the 2 improper_coeff commands would set impropers of improper type 1 to be computed with a *harmonic* potential with coefficients 120.0, 30 for [\\(K\\)]{.math .notranslate .nohighlight}, [\\(\\chi_0\\)]{.math .notranslate .nohighlight}. Improper type 2 would be computed with a *cvff* potential with coefficients 20.0, -1, 2 for K, d, and n, respectively.

If improper coefficients are specified in the data file read via the [[read_data]{.doc}]read_data.md){.reference .internal} command, then the same rule applies. E.g. "harmonic" or "cvff", must be added after the improper type, for each line in the "Improper Coeffs" section, e.g.

:::: {.highlight-none .notranslate}
::: highlight
    Improper Coeffs

    1 harmonic 120.0 30
    2 cvff 20.0 -1 2
    ...
:::
::::

If *class2* is one of the improper hybrid styles, the same rule holds for specifying additional AngleAngle coefficients either via the input script or in the data file. I.e. *class2* must be added to each line after the improper type. For lines in the AngleAngle Coeffs section of the data file for dihedral types that are not *class2*, you must use an improper style of *skip* as a placeholder, e.g.

:::: {.highlight-none .notranslate}
::: highlight
    AngleAngle Coeffs

    1 skip
    2 class2 0.0 0.0 0.0 115.06 130.01 115.06
    ...
:::
::::

Note that it is not necessary to use the improper style *skip* in the input script, since AngleAngle coefficients need not be specified at all for improper types that are not *class2*.

An improper style of *none* can be specified as the second argument to the improper_coeff command, if you desire to turn off certain improper types.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This improper style can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

Unlike other improper styles, the hybrid improper style does not store improper coefficient info for individual sub-styles in [[binary restart files]{.doc}]restart.md){.reference .internal} or [[data files]{.doc}]write_data.md){.reference .internal}. Thus when restarting a simulation, you need to re-specify the improper_coeff commands.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[improper_coeff]{.doc}]improper_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

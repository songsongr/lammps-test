::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#angle-style-hybrid-command .section}
[]{#index-1}[]{#index-0}

# angle_style hybrid command[](#angle-style-hybrid-command "Link to this heading"){.headerlink}

Accelerator Variants: *hybrid/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style hybrid style1 style2 ...
:::
::::

- style1,style2 = list of one or more angle styles
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style hybrid harmonic cosine
    angle_coeff 1 harmonic 80.0 30.0
    angle_coeff 2* cosine 50.0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *hybrid* style enables the use of multiple angle styles in one simulation. An angle style is assigned to each angle type. For example, angles in a polymer flow (of angle type 1) could be computed with a *harmonic* potential and angles in the wall boundary (of angle type 2) could be computed with a *cosine* potential. The assignment of angle type to style is made via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command or in the data file.

In the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} commands, the name of an angle style must be added after the angle type, with the remaining coefficients being those appropriate to that style. In the example above, the 2 angle_coeff commands set angles of angle type 1 to be computed with a *harmonic* potential with coefficients 80.0, 30.0 for [\\(K\\)]{.math .notranslate .nohighlight}, [\\(\\theta_0\\)]{.math .notranslate .nohighlight}. All other angle types [\\((2 - N)\\)]{.math .notranslate .nohighlight} are computed with a *cosine* potential with coefficient 50.0 for [\\(K\\)]{.math .notranslate .nohighlight}.

If angle coefficients are specified in the data file read via the [[read_data]{.doc}]read_data.md){.reference .internal} command, then the same rule applies. E.g. "harmonic" or "cosine", must be added after the angle type, for each line in the "Angle Coeffs" section, e.g.

:::: {.highlight-none .notranslate}
::: highlight
    Angle Coeffs

    1 harmonic 80.0 30.0
    2 cosine 50.0
    ...
:::
::::

If *class2* is one of the angle hybrid styles, the same rule holds for specifying additional BondBond (and BondAngle) coefficients either via the input script or in the data file. I.e. *class2* must be added to each line after the angle type. For lines in the BondBond (or BondAngle) section of the data file for angle types that are not *class2*, you must use an angle style of *skip* as a placeholder, e.g.

:::: {.highlight-none .notranslate}
::: highlight
    BondBond Coeffs

    1 skip
    2 class2 3.6512 1.0119 1.0119
    ...
:::
::::

Note that it is not necessary to use the angle style *skip* in the input script, since BondBond (or BondAngle) coefficients need not be specified at all for angle types that are not *class2*.

An angle style of *none* with no additional coefficients can be used in place of an angle style, either in a input script [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command or in the data file, if you desire to turn off interactions for specific angle types.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This angle style can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

Unlike other angle styles, the hybrid angle style does not store angle coefficient info for individual sub-styles in [[binary restart files]{.doc}]restart.md){.reference .internal} or [[data files]{.doc}]write_data.md){.reference .internal}. Thus when restarting a simulation, you need to re-specify the angle_coeff commands.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

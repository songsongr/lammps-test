::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#bond-style-hybrid-command .section}
[]{#index-1}[]{#index-0}

# bond_style hybrid command[](#bond-style-hybrid-command "Link to this heading"){.headerlink}

Accelerator Variants: *hybrid/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style hybrid style1 style2 ...
:::
::::

- style1,style2 = list of one or more bond styles
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style hybrid harmonic fene
    bond_coeff 1 harmonic 80.0 1.2
    bond_coeff 2* fene 30.0 1.5 1.0 1.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *hybrid* style enables the use of multiple bond styles in one simulation. A bond style is assigned to each bond type. For example, bonds in a polymer flow (of bond type 1) could be computed with a *fene* potential and bonds in the wall boundary (of bond type 2) could be computed with a *harmonic* potential. The assignment of bond type to style is made via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command or in the data file.

In the bond_coeff commands, the name of a bond style must be added after the bond type, with the remaining coefficients being those appropriate to that style. In the example above, the 2 bond_coeff commands set bonds of bond type 1 to be computed with a *harmonic* potential with coefficients 80.0, 1.2 for [\\(K\\)]{.math .notranslate .nohighlight}, [\\(r_0\\)]{.math .notranslate .nohighlight}. All other bond types (2-N) are computed with a *fene* potential with coefficients 30.0, 1.5, 1.0, 1.0 for [\\(K\\)]{.math .notranslate .nohighlight}, [\\(R_0\\)]{.math .notranslate .nohighlight}, [\\(\\epsilon\\)]{.math .notranslate .nohighlight}, [\\(\\sigma\\)]{.math .notranslate .nohighlight}.

If bond coefficients are specified in the data file read via the [[read_data]{.doc}]read_data.md){.reference .internal} command, then the same rule applies. E.g. "harmonic" or "fene" must be added after the bond type, for each line in the "Bond Coeffs" section, e.g.

:::: {.highlight-none .notranslate}
::: highlight
    Bond Coeffs

    1 harmonic 80.0 1.2
    2 fene 30.0 1.5 1.0 1.0
    ...
:::
::::

A bond style of *none* with no additional coefficients can be used in place of a bond style, either in a input script bond_coeff command or in the data file, if you desire to turn off interactions for specific bond types.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Unlike other bond styles, the hybrid bond style does not store bond coefficient info for individual sub-styles in [[binary restart files]{.doc}]restart.md){.reference .internal} or [[data files]{.doc}]write_data.md){.reference .internal}. Thus when restarting a simulation, you need to re-specify the bond_coeff commands.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#bond-style-harmonic-shift-command .section}
[]{#index-1}[]{#index-0}

# bond_style harmonic/shift command[](#bond-style-harmonic-shift-command "Link to this heading"){.headerlink}

Accelerator Variants: *harmonic/shift/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style harmonic/shift
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style harmonic/shift
    bond_coeff 5 10.0 0.5 1.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *harmonic/shift* bond style is a shifted harmonic bond that uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{U\_{\\text{min}}}{(r_0-r_c)\^2} \\left\[ (r-r_0)\^2-(r_c-r_0)\^2 \\right\]\\\]
:::

where [\\(r_0\\)]{.math .notranslate .nohighlight} is the equilibrium bond distance, and [\\(r_c\\)]{.math .notranslate .nohighlight} the critical distance. The potential energy has the value [\\(-U\_{\\text{min}}\\)]{.math .notranslate .nohighlight} at [\\(r_0\\)]{.math .notranslate .nohighlight} and zero at [\\(r_c\\)]{.math .notranslate .nohighlight}. This bond style differs from [[bond_style harmonic]{.doc}]bond_harmonic.md){.reference .internal} by the value of the potential energy.

The equivalent spring constant value *K* for use with [[bond_style harmonic]{.doc}]bond_harmonic.md){.reference .internal} can be computed using [\\(K = U\_{\\text{min}} / \[(r_0-r_c)\^2\]\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(U\_{\\text{min}}\\)]{.math .notranslate .nohighlight} (energy)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_c\\)]{.math .notranslate .nohighlight} (distance)

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}, [[bond style harmonic]{.doc}]bond_harmonic.md){.reference .internal}, [[bond style harmonic/shift/cut]{.doc}]bond_harmonic_shift_cut.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

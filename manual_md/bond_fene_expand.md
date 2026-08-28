:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#bond-style-fene-expand-command .section}
[]{#index-1}[]{#index-0}

# bond_style fene/expand command[](#bond-style-fene-expand-command "Link to this heading"){.headerlink}

Accelerator Variants: *fene/expand/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style fene/expand
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style fene/expand
    bond_coeff 1 30.0 1.5 1.0 1.0 0.5
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *fene/expand* bond style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = -0.5 K R_0\^2 \\ln \\left\[1 -\\left( \\frac{\\left(r - \\Delta\\right)}{R_0}\\right)\^2 \\right\] + 4 \\epsilon \\left\[ \\left(\\frac{\\sigma}{\\left(r - \\Delta\\right)}\\right)\^{12} - \\left(\\frac{\\sigma}{\\left(r - \\Delta\\right)}\\right)\^6 \\right\] + \\epsilon\\\]
:::

to define a finite extensible nonlinear elastic (FENE) potential [[(Kremer)]{.std .std-ref}](#feneexpand-kremer){.reference .internal}, used for bead-spring polymer models. The first term is attractive, the second Lennard-Jones term is repulsive.

The *fene/expand* bond style is similar to *fene* except that an extra shift factor of [\\(\\Delta\\)]{.math .notranslate .nohighlight} (positive or negative) is added to [\\(r\\)]{.math .notranslate .nohighlight} to effectively change the bead size of the bonded atoms. The first term now extends to [\\(R_0 + \\Delta\\)]{.math .notranslate .nohighlight} and the second term is cutoff at [\\(2\^\\frac{1}{6} \\sigma + \\Delta\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(R_0\\)]{.math .notranslate .nohighlight} (distance)

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance)

- [\\(\\Delta\\)]{.math .notranslate .nohighlight} (distance)

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You typically should specify [[special_bonds fene]{.doc}]special_bonds.md){.reference .internal} or [[special_bonds lj/coul 0 1 1]{.doc}]special_bonds.md){.reference .internal} to use this bond style. LAMMPS will issue a warning it that's not the case.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Kremer)** Kremer, Grest, J Chem Phys, 92, 5057 (1990).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#bond-style-class2-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# bond_style class2 command[](#bond-style-class2-command "Link to this heading"){.headerlink}

Accelerator Variants: *class2/omp*, *class2/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style class2
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style class2
    bond_coeff 1 1.0 100.0 80.0 80.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *class2* bond style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = K_2 (r - r_0)\^2 + K_3 (r - r_0)\^3 + K_4 (r - r_0)\^4\\\]
:::

where [\\(r_0\\)]{.math .notranslate .nohighlight} is the equilibrium bond distance.

See [[(Sun)]{.std .std-ref}](#bond-sun){.reference .internal} for a description of the COMPASS class2 force field.

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)

- [\\(K_2\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(K_3\\)]{.math .notranslate .nohighlight} (energy/distance\^3)

- [\\(K_4\\)]{.math .notranslate .nohighlight} (energy/distance\^4)

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the CLASS2 package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Sun)** Sun, J Phys Chem B 102, 7338-7364 (1998).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#bond-style-gromos-command .section}
[]{#index-1}[]{#index-0}

# bond_style gromos command[](#bond-style-gromos-command "Link to this heading"){.headerlink}

Accelerator Variants: *gromos/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style gromos
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style gromos
    bond_coeff 5 80.0 1.2
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *gromos* bond style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = K (r\^2 - r_0\^2)\^2\\\]
:::

where [\\(r_0\\)]{.math .notranslate .nohighlight} is the equilibrium bond distance. Note that the usual 1/4 factor is included in [\\(K\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy/distance\^4)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)

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
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

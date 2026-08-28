:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#dihedral-style-opls-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# dihedral_style opls command[](#dihedral-style-opls-command "Link to this heading"){.headerlink}

Accelerator Variants: *opls/intel*, *opls/kk*, *opls/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style opls
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style opls
    dihedral_coeff 1 1.740 -0.157 0.279 0.00   # CT-CT-CT-CT
    dihedral_coeff 2 0.000 0.000 0.366 0.000   # CT-CT-CT-HC
    dihedral_coeff 3 0.000 0.000 0.318 0.000   # HC-CT-CT-HC
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *opls* dihedral style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{1}{2} K_1 \[1 + \\cos(\\phi)\] + \\frac{1}{2} K_2 \[1 - \\cos(2 \\phi)\] + \\\\ & \\frac{1}{2} K_3 \[1 + \\cos(3 \\phi)\] + \\frac{1}{2} K_4 \[1 - \\cos(4 \\phi)\]\\end{split}\\\]
:::

Note that the usual 1/2 factor is not included in the K values.

This dihedral potential is used in the OPLS force field and is described in [[(Watkins)]{.std .std-ref}](#watkins){.reference .internal}.

The following coefficients must be defined for each dihedral type via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K_1\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_3\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_4\\)]{.math .notranslate .nohighlight} (energy)

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This dihedral style can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Watkins)** Watkins and Jorgensen, J Phys Chem A, 105, 4118-4125 (2001).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#improper-style-ring-command .section}
[]{#index-1}[]{#index-0}

# improper_style ring command[](#improper-style-ring-command "Link to this heading"){.headerlink}

Accelerator Variants: *ring/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style ring
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style ring
    improper_coeff 1 8000 70.5
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *ring* improper style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = &\\frac{1}{6} K \\left(\\Delta\_{ijl} + \\Delta\_{ijk} + \\Delta\_{kjl} \\right)\^6 \\\\ \\Delta\_{ijl} = & \\cos{\\theta\_{ijl} - \\cos{\\theta_0}} \\\\ \\Delta\_{ijk} = & \\cos{\\theta\_{ijk} - \\cos{\\theta_0}} \\\\ \\Delta\_{kjl} = & \\cos{\\theta\_{kjl} - \\cos{\\theta_0}}\\end{split}\\\]
:::

where [\\(K\\)]{.math .notranslate .nohighlight} is a prefactor, [\\(\\theta\\)]{.math .notranslate .nohighlight} is the angle formed by the atoms specified by (i,j,k,l) indices and [\\(\\theta_0\\)]{.math .notranslate .nohighlight} its equilibrium value.

If the 4 atoms in an improper quadruplet (listed in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command) are ordered i,j,k,l then [\\(\\theta\_{ijl}\\)]{.math .notranslate .nohighlight} is the angle between atoms i,j and l, [\\(\\theta\_{ijk}\\)]{.math .notranslate .nohighlight} is the angle between atoms i,j and k, [\\(\\theta\_{kjl}\\)]{.math .notranslate .nohighlight} is the angle between atoms j,k, and l.

The "ring" improper style implements the improper potential introduced by Destree et al., in Equation (9) of [[(Destree)]{.std .std-ref}](#destree){.reference .internal}. This potential does not affect small amplitude vibrations but is used in an ad-hoc way to prevent the onset of accidentally large amplitude fluctuations leading to the occurrence of a planar conformation of the three bonds i-j, j-k and j-l, an intermediate conformation toward the chiral inversion of a methine carbon. In the "Impropers" section of data file four atoms: i, j, k and l are specified with i,j and l lying on the backbone of the chain and k specifying the chirality of j.

The following coefficients must be defined for each improper type via the [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#symmetry-convention .section}
## Symmetry convention[](#symmetry-convention "Link to this heading"){.headerlink}

For the *ring* improper style, the second atom in the quadruplet is the atom of symmetry; all other atoms are considered interchangeable. This convention is relevant for operations that require knowledge of how atoms are ordered, such as automatic assignment of new improper types by [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This improper style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[improper_coeff]{.doc}]improper_coeff.md){.reference .internal}

**(Destree)** M. Destree, F. Laupretre, A. Lyulin, and J.-P. Ryckaert, J Chem Phys, 112, 9632 (2000).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

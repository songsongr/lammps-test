:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-charmm-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# angle_style charmm command[](#angle-style-charmm-command "Link to this heading"){.headerlink}

Accelerator Variants: *charmm/intel*, *charmm/kk*, *charmm/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style charmm
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style charmm
    angle_coeff 1 300.0 107.0 50.0 3.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *charmm* angle style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = K (\\theta - \\theta_0)\^2 + K\_{ub} (r - r\_{ub})\^2\\\]
:::

with an additional Urey_Bradley term based on the distance [\\(r\\)]{.math .notranslate .nohighlight} between the first and third atoms in the angle. [\\(K\\)]{.math .notranslate .nohighlight}, [\\(\\theta_0\\)]{.math .notranslate .nohighlight}, [\\(K\_{ub}\\)]{.math .notranslate .nohighlight}, and [\\(R\_{ub}\\)]{.math .notranslate .nohighlight} are coefficients defined for each angle type.

See [[(MacKerell)]{.std .std-ref}](#angle-mackerell){.reference .internal} for a description of the CHARMM force field.

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(K\_{ub}\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(r\_{ub}\\)]{.math .notranslate .nohighlight} (distance)

[\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence [\\(K\\)]{.math .notranslate .nohighlight} is effectively energy per radian\^2.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This angle style can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}, [[pair_style lj/charmm variants]{.doc}]pair_charmm.md){.reference .internal}, [[dihedral_style charmm]{.doc}]dihedral_charmm.md){.reference .internal}, [[dihedral_style charmmfsw]{.doc}]dihedral_charmm.md){.reference .internal}, [[fix cmap]{.doc}]fix_cmap.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(MacKerell)** MacKerell, Bashford, Bellott, Dunbrack, Evanseck, Field, Fischer, Gao, Guo, Ha, et al, J Phys Chem, 102, 3586 (1998).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

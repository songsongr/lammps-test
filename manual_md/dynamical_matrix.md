::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#dynamical-matrix-command .section}
[]{#index-1}[]{#index-0}

# dynamical_matrix command[](#dynamical-matrix-command "Link to this heading"){.headerlink}

Accelerator Variant: dynamical_matrix/kk

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dynamical_matrix group-ID style gamma args keyword value ...
:::
::::

- group-ID = ID of group of atoms to displace

- style = *regular* or *eskm*

- gamma = finite different displacement length (distance units)

- one or more keyword/arg pairs may be appended

  ``` literal-block
  keyword = file or binary
    file name = name of output file for the dynamical matrix
    binary arg = yes or no or gzip
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dynamical_matrix 1 regular 0.000001
    dynamical_matrix 1 eskm 0.000001
    dynamical_matrix 3 regular 0.00004 file dynmat.dat
    dynamical_matrix 5 eskm 0.00000001 file dynamical.dat binary yes
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Calculate the dynamical matrix by finite difference of the selected group,

::: {.math .notranslate .nohighlight}
\\\[D = \\frac{\\Phi\_{ij}\^{\\alpha\\beta}}{\\sqrt{M_i M_j}}\\\]
:::

where D is the dynamical matrix and [\\(\\Phi\\)]{.math .notranslate .nohighlight} is the force constant matrix defined by

::: {.math .notranslate .nohighlight}
\\\[\\Phi\_{ij}\^{\\alpha\\beta} = \\frac{\\partial\^2 U}{\\partial x\_{i,\\alpha} \\partial x\_{j,\\beta}}\\\]
:::

The output for the dynamical matrix is printed three elements at a time. The three elements are the three [\\(\\beta\\)]{.math .notranslate .nohighlight} elements for a respective i/[\\(\\alpha\\)]{.math .notranslate .nohighlight}/j combination. Each line is printed in order of j increasing first, [\\(\\alpha\\)]{.math .notranslate .nohighlight} second, and i last.

If the style eskm is selected, the dynamical matrix will be in units of inverse squared femtoseconds. These units will then conveniently leave frequencies in THz.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The command collects an array of nine times the number of atoms in a group on every single MPI rank, so the memory requirements can be very significant for large systems.

This command is part of the PHONON package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix phonon]{.doc}]fix_phonon.md){.reference .internal}, [[fix numdiff]{.doc}]fix_numdiff.md){.reference .internal},

[[compute hma]{.doc}]compute_hma.md){.reference .internal} uses an analytic formulation of the Hessian provided by a pair_style's Pair::single_hessian() function, if implemented.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default settings are file = "dynmat.dyn", binary = no
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

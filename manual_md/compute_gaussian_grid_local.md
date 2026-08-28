:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-gaussian-grid-local-command .section}
[]{#index-1}[]{#index-0}

# compute gaussian/grid/local command[](#compute-gaussian-grid-local-command "Link to this heading"){.headerlink}

Accelerator Variants: *gaussian/grid/local/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID gaussian/grid/local grid nx ny nz rcutfac  R_1 R_2 ... sigma_1 sigma_2
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- gaussian/grid/local = style name of this compute command

- *grid* values = nx, ny, nz, number of grid points in x, y, and z directions (positive integer)

- *rcutfac* = scale factor applied to all cutoff radii (positive real)

- *R_1, R_2,...* = list of cutoff radii, one for each type (distance units)

- *sigma_1, sigma_2,...* = Gaussian widths, one for each type (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute mygrid all gaussian/grid/local grid 40 40 40 4.0 0.5 0.5 0.4 0.4
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4Feb2025.]{.versionmodified .added}
:::

Define a computation that calculates a Gaussian representation of the ionic structure. This representation is used for the efficient evaluation of quantities related to the structure factor in a grid-based workflow, such as the ML-DFT workflow MALA [[(Ellis)]{.std .std-ref}](#ellis2021b){.reference .internal}, for which it was originally implemented. Usage of the workflow is described in a separate publication [[(Fiedler)]{.std .std-ref}](#fiedler2023){.reference .internal}.

For each LAMMPS type, a separate sum of Gaussians is calculated, using a separate Gaussian broadening per type. The computation is always performed on the numerical grid, no atom-based version of this compute exists. The Gaussian representation can only be executed in a local fashion, thus the output array only contains rows for grid points that are local to the processor subdomain. The layout of the grid is the same as for the see [[sna/grid/local]{.doc}]compute_sna_atom.md){.reference .internal} command.

Namely, the array contains one row for each of the local grid points, looping over the global index *ix* fastest, then *iy*, and *iz* slowest. Each row of the array contains the global indexes *ix*, *iy*, and *iz* first, followed by the *x*, *y*, and *z* coordinates of the grid point, followed by the values of the Gaussians (one floating point number per type per grid point).

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

Compute *gaussian/grid/local* evaluates a local array. The array contains one row for each of the local grid points, looping over the global index *ix* fastest, then *iy*, and *iz* slowest. The array contains math [\\(ntypes+6\\)]{.math .notranslate .nohighlight} columns, where *ntypes* is the number of LAMMPS types. The first three columns are the global indexes *ix*, *iy*, and *iz*, followed by the *x*, *y*, and *z* coordinates of the grid point, followed by the *ntypes* columns containing the values of the Gaussians for each type.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These computes are part of the ML-SNAP package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute sna/grid/local]{.doc}]compute_sna_atom.md){.reference .internal}

------------------------------------------------------------------------

**(Ellis)** Ellis, Fiedler, Popoola, Modine, Stephens, Thompson, Cangi, Rajamanickam, [Phys. Rev. B, 104, 035120, (2021)](https://doi.org/10.1103/PhysRevB.104.035120){.reference .external}

**(Fiedler)** Fiedler, Modine, Schmerler, Vogel, Popoola, Thompson, Rajamanickam, and Cangi, [npj Comp. Mater., 9, 115 (2023)](https://doi.org/10.1038/s41524-023-01070-z){.reference .external}
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

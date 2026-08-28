::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#parallel-algorithms .section}
# [4.4. ]{.section-number}Parallel algorithms[](#parallel-algorithms "Link to this heading"){.headerlink}

LAMMPS is designed to enable running simulations in parallel using the MPI parallel communication standard with distributed data via domain decomposition. The parallelization aims to be efficient, and resulting in good strong scaling (= good speedup for the same system) and good weak scaling (= the computational cost of enlarging the system is proportional to the system size). Additional parallelization using GPUs or OpenMP can also be applied within the subdomain assigned to an MPI process. For clarity, most of the following illustrations show the 2d simulation case. The underlying algorithms in those cases, however, apply to both 2d and 3d cases equally well.

::: {.admonition .note}
Note

The text and most of the figures in this chapter were adapted for the manual from the section on parallel algorithms in the [[new LAMMPS paper]{.std .std-ref}]Intro_citing.md#lammps-paper){.reference .internal}.
:::

::: {.toctree-wrapper .compound}
- [4.4.1. Partitioning]Developer_par_part.md){.reference .internal}
- [4.4.2. Communication]Developer_par_comm.md){.reference .internal}
- [4.4.3. Neighbor lists]Developer_par_neigh.md){.reference .internal}
- [4.4.4. Long-range interactions]Developer_par_long.md){.reference .internal}
- [4.4.5. OpenMP Parallelism]Developer_par_openmp.md){.reference .internal}
:::
:::::
::::::
:::::::

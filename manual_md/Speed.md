:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#accelerate-performance .section}
# [7. ]{.section-number}Accelerate performance[](#accelerate-performance "Link to this heading"){.headerlink}

This section describes various methods for improving LAMMPS performance for different classes of problems running on different kinds of machines.

There are two thrusts to the discussion that follows. The first is using code options that implement alternate algorithms that can speed-up a simulation. The second is to use one of the several accelerator packages provided with LAMMPS that contain code optimized for certain kinds of hardware, including multicore CPUs, GPUs, and Intel Xeon Phi co-processors.

The [Benchmark page](https://www.lammps.org/bench.html){.reference .external} of the LAMMPS website gives performance results for the various accelerator packages discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page, for several of the standard LAMMPS benchmark problems, as a function of problem size and number of compute nodes, on different hardware platforms.

::: {.toctree-wrapper .compound}
- [7.1. Benchmarks]Speed_bench.md){.reference .internal}
- [7.2. Measuring performance]Speed_measure.md){.reference .internal}
- [7.3. General tips]Speed_tips.md){.reference .internal}
- [7.4. Accelerator packages]Speed_packages.md){.reference .internal}
- [7.5. Comparison of various accelerator packages]Speed_compare.md){.reference .internal}
:::
::::
:::::
::::::

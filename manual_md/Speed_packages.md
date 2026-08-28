::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#accelerator-packages .section}
# [7.4. ]{.section-number}Accelerator packages[](#accelerator-packages "Link to this heading"){.headerlink}

Accelerated versions of various [[pair_style]{.doc}]pair_style.md){.reference .internal}, [[fixes]{.doc}]fix.md){.reference .internal}, [[computes]{.doc}]compute.md){.reference .internal}, and other commands have been added to LAMMPS, which will typically run faster than the standard non-accelerated versions. Some require appropriate hardware to be present on your system, e.g. GPUs or Intel Xeon Phi co-processors.

All of these commands are in packages provided with LAMMPS. An overview of packages is give on the [[Packages]{.doc}]Packages.md){.reference .internal} doc pages.

These are the accelerator packages currently in LAMMPS:

  ------------------------------------------------------------------- -------------------------------------------------------
  [[GPU Package]{.doc}]Speed_gpu.md){.reference .internal}         for GPUs via CUDA, OpenCL, or ROCm HIP
  [[INTEL Package]{.doc}]Speed_intel.md){.reference .internal}     for Intel CPUs and Intel Xeon Phi
  [[KOKKOS Package]{.doc}]Speed_kokkos.md){.reference .internal}   for NVIDIA GPUs, Intel Xeon Phi, and OpenMP threading
  [[OPENMP Package]{.doc}]Speed_omp.md){.reference .internal}      for OpenMP threading and generic CPU optimizations
  [[OPT Package]{.doc}]Speed_opt.md){.reference .internal}         generic CPU optimizations
  ------------------------------------------------------------------- -------------------------------------------------------

::: {.toctree-wrapper .compound}
:::

Inverting this list, LAMMPS currently has acceleration support for three kinds of hardware, via the listed packages:

  ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Many-core CPUs   [[INTEL]{.doc}]Speed_intel.md){.reference .internal}, [[KOKKOS]{.doc}]Speed_kokkos.md){.reference .internal}, [[OPENMP]{.doc}]Speed_omp.md){.reference .internal}, [[OPT]{.doc}]Speed_opt.md){.reference .internal} packages
  GPUs             [[GPU]{.doc}]Speed_gpu.md){.reference .internal}, [[KOKKOS]{.doc}]Speed_kokkos.md){.reference .internal} packages
  Intel Phi/AVX    [[INTEL]{.doc}]Speed_intel.md){.reference .internal}, [[KOKKOS]{.doc}]Speed_kokkos.md){.reference .internal} packages
  ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Which package is fastest for your hardware may depend on the size problem you are running and what commands (accelerated and non-accelerated) are invoked by your input script. While these doc pages include performance guidelines, there is no substitute for trying out the different packages appropriate to your hardware.

Any accelerated style has the same name as the corresponding standard style, except that a suffix is appended. Otherwise, the syntax for the command that uses the style is identical, their functionality is the same, and the numerical results it produces should also be the same, except for precision and round-off effects.

For example, all of these styles are accelerated variants of the Lennard-Jones [[pair_style lj/cut]{.doc}]pair_lj.md){.reference .internal}:

- [[pair_style lj/cut/gpu]{.doc}]pair_lj.md){.reference .internal}

- [[pair_style lj/cut/intel]{.doc}]pair_lj.md){.reference .internal}

- [[pair_style lj/cut/kk]{.doc}]pair_lj.md){.reference .internal}

- [[pair_style lj/cut/omp]{.doc}]pair_lj.md){.reference .internal}

- [[pair_style lj/cut/opt]{.doc}]pair_lj.md){.reference .internal}

To see what accelerate styles are currently available for a particular style, find the style name in the [[Commands]{.doc}]Commands_all.md){.reference .internal} style pages (fix,compute,pair,etc) and see what suffixes are listed (g,i,k,o,t) with it. The doc pages for individual commands (e.g. [[pair lj/cut]{.doc}]pair_lj.md){.reference .internal} or [[fix nve]{.doc}]fix_nve.md){.reference .internal}) also list any accelerated variants available for that style.

To use an accelerator package in LAMMPS, and one or more of the styles it provides, follow these general steps. Details vary from package to package and are explained in the individual accelerator doc pages, listed above.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Configure LAMMPS to include the accelerator package                                                                                                                                                                                            [[Build LAMMPS with CMake]{.doc}]Build_cmake.md){.reference .internal} or [[Build LAMMPS with make]{.doc}]Build_make.md){.reference .internal}
  (Re-)Compile LAMMPS                                                                                                                                                                                                                            [[Build LAMMPS]{.doc}]Build.md){.reference .internal}
  prepare and test a regular LAMMPS simulation                                                                                                                                                                                                   [`lmp`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-in`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`in.script;`{.docutils .literal .notranslate}]{.pre} [`mpirun`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-np`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`32`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`lmp`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-in`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`in.script`{.docutils .literal .notranslate}]{.pre}
  enable specific accelerator support via [`-k`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal}   only needed for KOKKOS package
  set any needed options for the package via [`-pk`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} or [[package]{.doc}]package.md){.reference .internal} command               only if defaults need to be changed
  use accelerated styles in your input via [`-sf`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} or [[suffix]{.doc}]suffix.md){.reference .internal} command                   [`lmp_machine`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-in`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`in.script`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gpu`{.docutils .literal .notranslate}]{.pre}
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is discussed on the [[Packages]{.doc}]Packages.md){.reference .internal} and [[extra Build info]{.doc}]Build_extras.md){.reference .internal} doc pages, and its use is illustrated in the individual accelerator sections. Typically these steps only need to be done once, to create an executable that uses one or more accelerator packages.

::: {.admonition .note}
Note

With a few exceptions, you can build a single LAMMPS executable with all its accelerator packages installed. Note however that the INTEL and KOKKOS packages require you to choose one of their hardware options when building for a specific platform. I.e. CPU or Phi option for the INTEL package. Or the OpenMP, CUDA, HIP, SYCL, or Phi option for the KOKKOS package. Or the OpenCL, HIP, or CUDA option for the GPU package.
:::

As mentioned above, the [Benchmark page](https://www.lammps.org/bench.html){.reference .external} of the LAMMPS website gives performance results for the various accelerator packages for several of the standard LAMMPS benchmark problems, as a function of problem size and number of compute nodes, on different hardware platforms.

Here is a brief summary of what the various packages provide. Details are in the individual accelerator sections.

- Styles with a "gpu" suffix are part of the GPU package and can be run on Intel, NVIDIA, or AMD GPUs. The speed-up on a GPU depends on a variety of factors, discussed in the accelerator sections.

- Styles with an "intel" suffix are part of the INTEL package. These styles support vectorized single and mixed precision calculations, in addition to full double precision. In extreme cases, this can provide speedups over 3.5x on CPUs. The package also supports acceleration in "offload" mode to Intel(R) Xeon Phi(TM) co-processors. This can result in additional speedup over 2x depending on the hardware configuration.

- Styles with a "kk" suffix are part of the KOKKOS package, and can be run using OpenMP on multicore CPUs, on an NVIDIA or AMD GPU, or on an Intel Xeon Phi in "native" mode. The speed-up depends on a variety of factors, as discussed on the KOKKOS accelerator page.

- Styles with an "omp" suffix are part of the OPENMP package and allow a pair-style to be run in multi-threaded mode using OpenMP. This can be useful on nodes with high-core counts when using less MPI processes than cores is advantageous, e.g. when running with PPPM so that FFTs are run on fewer MPI processors or when the many MPI tasks would overload the available bandwidth for communication.

- Styles with an "opt" suffix are part of the OPT package and typically speed-up the pairwise calculations of your simulation by 5-25% on a CPU.

The individual accelerator package doc pages explain:

- what hardware and software the accelerated package requires

- how to build LAMMPS with the accelerated package

- how to run with the accelerated package either via command-line switches or modifying the input script

- speed-ups to expect

- guidelines for best performance

- restrictions
:::::
::::::
:::::::

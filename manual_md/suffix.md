:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#suffix-command .section}
[]{#index-0}

# suffix command[](#suffix-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    suffix style args
:::
::::

- style = *off* or *on* or *gpu* or *intel* or *kk* or *omp* or *opt* or *hybrid*

- args = for hybrid style, default suffix to be used and alternative suffix
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    suffix off
    suffix on
    suffix gpu
    suffix intel
    suffix hybrid intel omp
    suffix kk
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command allows you to use variants of various styles if they exist. In that respect it operates the same as the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal}. It also has options to turn off or back on any suffix setting made via the command-line.

The specified style can be *gpu*, *intel*, *kk*, *omp*, *opt* or *hybrid*. These refer to optional packages that LAMMPS can be built with, as described on the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page. The "gpu" style corresponds to the GPU package, the "intel" style to the INTEL package, the "kk" style to the KOKKOS package, the "omp" style to the OPENMP package, and the "opt" style to the OPT package.

These are the variants these packages provide:

- GPU = a handful of pair styles and the PPPM kspace_style, optimized to run on one or more GPUs or multicore CPU/GPU nodes

- INTEL = a collection of pair styles and neighbor routines optimized to run in single, mixed, or double precision on CPUs and Intel(R) Xeon Phi(TM) co-processors.

- KOKKOS = a collection of atom, pair, and fix styles optimized to run using the Kokkos library on various kinds of hardware, including GPUs via CUDA and many-core chips via OpenMP or threading.

- OPENMP = a collection of pair, bond, angle, dihedral, improper, kspace, compute, and fix styles with support for OpenMP multi-threading

- OPT = a handful of pair styles, cache-optimized for faster CPU performance

- HYBRID = a combination of two packages can be specified (see below)

As an example, all of the packages provide a [[pair_style lj/cut]{.doc}]pair_lj.md){.reference .internal} variant, with style names lj/cut/opt, lj/cut/omp, lj/cut/gpu, lj/cut/intel, or lj/cut/kk. A variant styles can be specified explicitly in your input script, e.g. pair_style lj/cut/gpu. If the suffix command is used with the appropriate style, you do not need to modify your input script. The specified suffix (opt,omp,gpu,intel,kk) is automatically appended whenever your input script command creates a new [[atom]{.doc}]atom_style.md){.reference .internal}, [[pair]{.doc}]pair_style.md){.reference .internal}, [[bond]{.doc}]bond_style.md){.reference .internal}, [[angle]{.doc}]angle_style.md){.reference .internal}, [[dihedral]{.doc}]dihedral_style.md){.reference .internal}, [[improper]{.doc}]improper_style.md){.reference .internal}, [[kspace]{.doc}]kspace_style.md){.reference .internal}, [[fix]{.doc}]fix.md){.reference .internal}, [[compute]{.doc}]compute.md){.reference .internal}, or [[run]{.doc}]run_style.md){.reference .internal} style. If the variant version does not exist, the standard version is created.

For "hybrid", two packages are specified. The first is used whenever available. If a style with the first suffix is not available, the style with the suffix for the second package will be used if available. For example, "hybrid intel omp" will use styles from the INTEL package as a first choice and styles from the OPENMP package as a second choice if no INTEL variant is available.

If the specified style is *off*, then any previously specified suffix is temporarily disabled, whether it was specified by a command-line switch or a previous suffix command. If the specified style is *on*, a disabled suffix is turned back on. The use of these 2 commands lets your input script use a standard LAMMPS style (i.e. a non-accelerated variant), which can be useful for testing or benchmarking purposes. Of course this is also possible by not using any suffix commands, and explicitly appending or not appending the suffix to the relevant commands in your input script.

::: {.admonition .note}
Note

The default [[run_style]{.doc}]run_style.md){.reference .internal} verlet is invoked prior to reading the input script and is therefore not affected by a suffix command in the input script. The KOKKOS package requires "run_style verlet/kk", so when using the KOKKOS package it is necessary to either use the command line "-sf kk" command or add an explicit "run_style verlet" command to the input script.
:::
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

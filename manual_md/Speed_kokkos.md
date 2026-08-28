:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#kokkos-package .section}
# [7.4.3. ]{.section-number}KOKKOS package[](#kokkos-package "Link to this heading"){.headerlink}

Kokkos is a templated C++ library that provides abstractions to allow a single implementation of an application kernel (e.g. a pair style) to run efficiently on different kinds of hardware, such as GPUs, Intel Xeon Phis, or many-core CPUs. Kokkos maps the C++ kernel onto different back end languages such as CUDA, OpenMP, or Pthreads. The Kokkos library also provides data abstractions to adjust (at compile time) the memory layout of data structures like 2d and 3d arrays to optimize performance on different hardware. For more information on Kokkos, see [the Kokkos GitHub page](https://github.com/kokkos/kokkos){.reference .external}.

The LAMMPS KOKKOS package contains versions of pair, fix, and atom styles that use data structures and macros provided by the Kokkos library, which is included with LAMMPS in /lib/kokkos. The KOKKOS package was developed primarily by Christian Trott (Sandia) and Stan Moore (Sandia) with contributions of various styles by others, including Sikandar Mashayak (UIUC), Ray Shan (Sandia), and Dan Ibanez (Sandia). For more information on developing using Kokkos abstractions see the [Kokkos Wiki](https://kokkos.org/kokkos-core-wiki/){.reference .external}.

::: {.admonition .note}
Note

The Kokkos library is under active development and tracking the availability of accelerator hardware, so is the KOKKOS package in LAMMPS. This means that only a certain range of versions of the Kokkos library are compatible with the KOKKOS package of a certain range of LAMMPS versions. For that reason LAMMPS comes with a bundled version of the Kokkos library that has been validated on multiple platforms and may contain selected back-ported bug fixes from upstream Kokkos versions. While it is possible to build LAMMPS with an external version of Kokkos, it is untested and may result in incorrect execution or crashes.
:::

Kokkos currently provides full support for 4 modes of execution (per MPI task). These are Serial (MPI-only for CPUs and Intel Phi), OpenMP (threading for many-core CPUs and Intel Phi), CUDA (for NVIDIA GPUs) and HIP (for AMD GPUs). Additional modes (e.g. OpenMP target, Intel data center GPUs) are under development. You choose the mode at build time to produce an executable compatible with a specific hardware.

The following compatibility notes have been last updated for LAMMPS version 11 February 2026 and its bundled Kokkos library version 5.0.2.

::: {.note .admonition}
C++20 support

Kokkos requires using a compiler that supports the C++20 standard. For some compilers, it may be necessary to add a flag to enable C++20 support. For example, the GNU compiler uses the [`-std=c++20`{.docutils .literal .notranslate}]{.pre} flag. For a list of compilers that have been tested with the Kokkos library, see the [requirements document of the Kokkos Wiki](https://kokkos.org/kokkos-core-wiki/get-started/requirements.html){.reference .external}.
:::

::: {.note .admonition}
NVIDIA CUDA support

To build with Kokkos support for NVIDIA GPUs, the NVIDIA CUDA toolkit software version 12.2 or later must be installed on your system. See the discussion for the [[GPU package]{.doc}]Speed_gpu.md){.reference .internal} for details of how to check and do this.
:::

::: {.note .admonition}
AMD ROCm (HIP) support

To build with Kokkos support for AMD GPUs, the AMD ROCm toolkit software version 6.2.0 or later must be installed on your system.
:::

::: {.note .admonition}
Intel Data Center GPU support

Support for Kokkos with Intel Data Center GPU accelerators (formerly known under the code name "Ponte Vecchio") in LAMMPS is still a work in progress. Minimum required version is the Intel LLVM (not classic) compiler version 2024.1. The LAMMPS developers do not regularly test the status of this, so please contact the LAMMPS developers if you run into problems.
:::

::: {.note .admonition}
CUDA and MPI library compatibility

Kokkos with CUDA currently implicitly assumes that the MPI library is GPU-aware. This is not always the case, especially when using pre-compiled MPI libraries provided by a Linux distribution. This is not a problem when using only a single GPU with a single MPI rank. When running with multiple MPI ranks, you may see segmentation faults without GPU-aware MPI support. These can be avoided by adding the flags [[-pk kokkos gpu/aware off]{.doc}]Run_options.md){.reference .internal} to the LAMMPS command-line or by using the command [[package kokkos gpu/aware off]{.doc}]package.md){.reference .internal} in the input file.
:::

::: {.note .admonition}
Using multiple MPI ranks per GPU

Unlike with the GPU package, there are limited benefits from using multiple MPI processes per GPU with KOKKOS. But when doing this it is **required** to enable CUDA MPS ([Multi-Process Service :: GPU Deployment and Management Documentation](https://docs.nvidia.com/deploy/mps/index.html){.reference .external} ) to get acceptable performance.
:::

::: {#building-lammps-with-the-kokkos-package .section}
## Building LAMMPS with the KOKKOS package[](#building-lammps-with-the-kokkos-package "Link to this heading"){.headerlink}

See the [[Build extras]{.std .std-ref}]Build_extras.md#kokkos){.reference .internal} page for instructions.
:::

:::::::::::::::::::::::::::::::::::::::::::::::: {#running-lammps-with-the-kokkos-package .section}
## Running LAMMPS with the KOKKOS package[](#running-lammps-with-the-kokkos-package "Link to this heading"){.headerlink}

All Kokkos operations occur within the context of an individual MPI task running on a single node of the machine. The total number of MPI tasks used by LAMMPS (one or multiple per compute node) is set in the usual manner via the [`mpirun`{.docutils .literal .notranslate}]{.pre} or [`mpiexec`{.docutils .literal .notranslate}]{.pre} commands, and is independent of Kokkos. E.g. the mpirun command in OpenMPI does this via its [`-np`{.docutils .literal .notranslate}]{.pre} and [`-npernode`{.docutils .literal .notranslate}]{.pre} switches. Ditto for MPICH via [`-np`{.docutils .literal .notranslate}]{.pre} and [`-ppn`{.docutils .literal .notranslate}]{.pre}.

::::::::::: {#running-on-a-multicore-cpu .section}
### Running on a multicore CPU[](#running-on-a-multicore-cpu "Link to this heading"){.headerlink}

Here is a quick overview of how to use the KOKKOS package for CPU acceleration, assuming one or more 16-core nodes.

:::: {.highlight-bash .notranslate}
::: highlight
    # 1 node, 16 MPI tasks/node, no multi-threading
    mpirun -np 16 lmp_kokkos_mpi_only -k on -sf kk -in in.lj

    # 2 nodes, 1 MPI task/node, 16 threads/task
    mpirun -np 2 -ppn 1 lmp_kokkos_omp -k on t 16 -sf kk -in in.lj

    # 1 node,  2 MPI tasks/node, 8 threads/task
    mpirun -np 2 lmp_kokkos_omp -k on t 8 -sf kk -in in.lj

    # 8 nodes, 4 MPI tasks/node, 4 threads/task
    mpirun -np 32 -ppn 4 lmp_kokkos_omp -k on t 4 -sf kk -in in.lj
:::
::::

To run using the KOKKOS package, use the [`-k`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre}, [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kk`{.docutils .literal .notranslate}]{.pre} and [`-pk`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kokkos`{.docutils .literal .notranslate}]{.pre} [[command-line switches]{.doc}]Run_options.md){.reference .internal} in your [`mpirun`{.docutils .literal .notranslate}]{.pre} command. You must use the [`-k`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} to enable the KOKKOS package. It takes additional arguments for hardware settings appropriate to your system. For OpenMP use:

:::: {.highlight-none .notranslate}
::: highlight
    -k on t Nt
:::
::::

The [`t`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Nt`{.docutils .literal .notranslate}]{.pre} option specifies how many OpenMP threads per MPI task to use with a node. The default is [`Nt`{.docutils .literal .notranslate}]{.pre} = 1, which is MPI-only mode. Note that the product of MPI tasks \* OpenMP threads/task should not exceed the physical number of cores (on a node), otherwise performance will suffer. If Hyper-Threading (HT) is enabled, then the product of MPI tasks \* OpenMP threads/task should not exceed the physical number of cores \* hardware threads. The [`-k`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} switch also issues a [`package`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kokkos`{.docutils .literal .notranslate}]{.pre} command (with no additional arguments) which sets various KOKKOS options to default values, as discussed on the [[package]{.doc}]package.md){.reference .internal} command doc page.

The [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kk`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} will automatically append the "/kk" suffix to styles that support it. In this manner no modification to the input script is needed. Alternatively, one can run with the KOKKOS package by editing the input script as described below.

::: {.admonition .note}
Note

When using ONLY a single OpenMP thread, the Kokkos Serial back end (i.e. [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Kokkos_ENABLE_SERIAL=yes`{.docutils .literal .notranslate}]{.pre}) will give better performance than the OpenMP back end (i.e. [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Kokkos_ENABLE_OPENMP=yes`{.docutils .literal .notranslate}]{.pre}) because some of the overhead to make the code thread-safe is removed.
:::

::: {.admonition .note}
Note

Use the [`-pk`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kokkos`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} to change the default [[package kokkos]{.doc}]package.md){.reference .internal} options. See its doc page for details and default settings. Experimenting with its options can provide a speed-up for specific calculations. For example:
:::

:::: {.highlight-bash .notranslate}
::: highlight
    # Newton on, Half neighbor list, non-threaded comm
    mpirun -np 16 lmp_kokkos_mpi_only -k on -sf kk \
           -pk kokkos newton on neigh half comm no -in in.lj
:::
::::

If the [[newton]{.doc}]newton.md){.reference .internal} command is used in the input script, it can also override the Newton flag defaults.

For half neighbor lists and OpenMP, the KOKKOS package uses data duplication (i.e. thread-private arrays) by default to avoid thread-level write conflicts in the force arrays (and other data structures as necessary). Data duplication is typically fastest for small numbers of threads (i.e. 8 or less) but does increase memory footprint and is not scalable to large numbers of threads. An alternative to data duplication is to use thread-level atomic operations which do not require data duplication. The use of atomic operations can be enforced by compiling LAMMPS with the [`-DLMP_KOKKOS_USE_ATOMICS`{.docutils .literal .notranslate}]{.pre} pre-processor flag. Most but not all Kokkos-enabled pair_styles support data duplication. Alternatively, full neighbor lists avoid the need for duplication or atomic operations but require more compute operations per atom. When using the Kokkos Serial back end or the OpenMP back end with a single thread, no duplication or atomic operations are used. For CUDA and half neighbor lists, the KOKKOS package always uses atomic operations.
:::::::::::

::::: {#cpu-cores-sockets-and-thread-affinity .section}
### CPU Cores, Sockets and Thread Affinity[](#cpu-cores-sockets-and-thread-affinity "Link to this heading"){.headerlink}

When using multi-threading, it is important for performance to bind both MPI tasks to physical cores, and threads to physical cores, so they do not migrate during a simulation.

If you are not certain MPI tasks are being bound (check the defaults for your MPI installation), binding can be forced with these flags:

:::: {.highlight-bash .notranslate}
::: highlight
    # OpenMPI 1.8
    mpirun -np 2 --bind-to socket --map-by socket ./lmp_openmpi ...

    # Mvapich2 2.0
    mpiexec -np 2 --bind-to socket --map-by socket ./lmp_mvapich ...
:::
::::

For binding threads with KOKKOS OpenMP, use thread affinity environment variables to force binding. With OpenMP 3.1 (gcc 4.7 or later, intel 12 or later) setting the environment variable [`OMP_PROC_BIND=true`{.docutils .literal .notranslate}]{.pre} should be sufficient. In general, for best performance with OpenMP 4.0 or later set [`OMP_PROC_BIND=spread`{.docutils .literal .notranslate}]{.pre} and [`OMP_PLACES=threads`{.docutils .literal .notranslate}]{.pre}. For binding threads with the KOKKOS pthreads option, compile LAMMPS with the hwloc or libnuma support enabled as described in the [[extra build options page]{.std .std-ref}]Build_extras.md#kokkos){.reference .internal}.
:::::

:::::::::: {#running-on-knight-s-landing-knl-intel-xeon-phi .section}
### Running on Knight's Landing (KNL) Intel Xeon Phi[](#running-on-knight-s-landing-knl-intel-xeon-phi "Link to this heading"){.headerlink}

Here is a quick overview of how to use the KOKKOS package for the Intel Knight's Landing (KNL) Xeon Phi:

KNL Intel Phi chips have 68 physical cores. Typically 1 to 4 cores are reserved for the OS, and only 64 or 66 cores are used. Each core has 4 Hyper-Threads,so there are effectively N = 256 (4\*64) or N = 264 (4\*66) cores to run on. The product of MPI tasks \* OpenMP threads/task should not exceed this limit, otherwise performance will suffer. Note that with the KOKKOS package you do not need to specify how many KNLs there are per node; each KNL is simply treated as running some number of MPI tasks.

Examples of mpirun commands that follow these rules are shown below.

:::: {.highlight-bash .notranslate}
::: highlight
    # Running on an Intel KNL node with 68 cores
    # (272 threads/node via 4x hardware threading):

    # 1 node, 64 MPI tasks/node, 4 threads/task
    mpirun -np 64 lmp_kokkos_phi -k on t 4 -sf kk -in in.lj

    # 1 node, 66 MPI tasks/node, 4 threads/task
    mpirun -np 66 lmp_kokkos_phi -k on t 4 -sf kk -in in.lj

    # 1 node, 32 MPI tasks/node, 8 threads/task
    mpirun -np 32 lmp_kokkos_phi -k on t 8 -sf kk -in in.lj

    # 8 nodes, 64 MPI tasks/node, 4 threads/task
    mpirun -np 512 -ppn 64 lmp_kokkos_phi -k on t 4 -sf kk -in in.lj
:::
::::

The [`-np`{.docutils .literal .notranslate}]{.pre} setting of the mpirun command sets the number of MPI tasks/node. The [`-k`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`t`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Nt`{.docutils .literal .notranslate}]{.pre} command-line switch sets the number of threads/task as [`Nt`{.docutils .literal .notranslate}]{.pre}. The product of these two values should be N, i.e. 256 or 264.

::: {.admonition .note}
Note

The default for the [[package kokkos]{.doc}]package.md){.reference .internal} command when running on KNL is to use "half" neighbor lists and set the Newton flag to "on" for both pairwise and bonded interactions. This will typically be best for many-body potentials. For simpler pairwise potentials, it may be faster to use a "full" neighbor list with Newton flag to "off". Use the [`-pk`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kokkos`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} to change the default [[package kokkos]{.doc}]package.md){.reference .internal} options. See its documentation page for details and default settings. Experimenting with its options can provide a speed-up for specific calculations. For example:
:::

:::: {.highlight-bash .notranslate}
::: highlight
    #  Newton on, half neighbor list, threaded comm
    mpirun -np 64 lmp_kokkos_phi -k on t 4 -sf kk -pk kokkos comm host -in in.reax

    # Newton off, full neighbor list, non-threaded comm
    mpirun -np 64 lmp_kokkos_phi -k on t 4 -sf kk \
           -pk kokkos newton off neigh full comm no -in in.lj
:::
::::

::: {.admonition .note}
Note

MPI tasks and threads should be bound to cores as described above for CPUs.
:::

::: {.admonition .note}
Note

To build with Kokkos support for Intel Xeon Phi co-processors such as Knight's Corner (KNC), your system must be configured to use them in "native" mode, not "offload" mode like the INTEL package supports.
:::
::::::::::

:::::::::::::: {#running-on-gpus .section}
### Running on GPUs[](#running-on-gpus "Link to this heading"){.headerlink}

Use the [`-k`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} to specify the number of GPUs per node. Typically the [`-np`{.docutils .literal .notranslate}]{.pre} setting of the [`mpirun`{.docutils .literal .notranslate}]{.pre} command should set the number of MPI tasks/node to be equal to the number of physical GPUs on the node. You can assign multiple MPI tasks to the same GPU with the KOKKOS package, but this is usually only faster if some portions of the input script have not been ported to use Kokkos. In this case, also packing/unpacking communication buffers on the host may give speedup (see the KOKKOS [[package]{.doc}]package.md){.reference .internal} command). Using CUDA MPS is recommended in this scenario.

Using a GPU-aware MPI library is highly recommended. GPU-aware MPI use can be avoided by using [[-pk kokkos gpu/aware off]{.doc}]package.md){.reference .internal}. As above for multicore CPUs (and no GPU), if N is the number of physical cores/node, then the number of MPI tasks/node should not exceed N.

:::: {.highlight-none .notranslate}
::: highlight
    -k on g Ng
:::
::::

Here are examples of how to use the KOKKOS package for GPUs, assuming one or more nodes, each with two GPUs:

:::: {.highlight-bash .notranslate}
::: highlight
    # 1 node,   2 MPI tasks/node, 2 GPUs/node
    mpirun -np 2 lmp_kokkos_cuda_openmpi -k on g 2 -sf kk -in in.lj

    # 16 nodes, 2 MPI tasks/node, 2 GPUs/node (32 GPUs total)
    mpirun -np 32 -ppn 2 lmp_kokkos_cuda_openmpi -k on g 2 -sf kk -in in.lj
:::
::::

::: {.admonition .note}
Note

The default for the [[package kokkos]{.doc}]package.md){.reference .internal} command when running on GPUs is to use "full" neighbor lists and set the Newton flag to "off" for both pairwise and bonded interactions, along with threaded communication. When running on Maxwell or Kepler GPUs, this will typically be best. For Pascal GPUs and beyond, using "half" neighbor lists and setting the Newton flag to "on" may be faster. For many pair styles, setting the neighbor binsize equal to twice the CPU default value will give speedup, which is the default when running on GPUs. Use the [`-pk`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kokkos`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} to change the default [[package kokkos]{.doc}]package.md){.reference .internal} options. See its documentation page for details and default settings. Experimenting with its options can provide a speed-up for specific calculations. For example:
:::

:::: {.highlight-bash .notranslate}
::: highlight
    # Newton on, half neighbor list, set binsize = neighbor ghost cutoff
    mpirun -np 2 lmp_kokkos_cuda_openmpi -k on g 2 -sf kk \
           -pk kokkos newton on neigh half binsize 2.8 -in in.lj
:::
::::

::: {.admonition .note}
Note

The default binsize for [[atom sorting]{.doc}]atom_modify.md){.reference .internal} on GPUs is equal to the default CPU neighbor binsize (i.e. 2x smaller than the default GPU neighbor binsize). When running simple pair-wise potentials like Lennard Jones on GPUs, using a 2x larger binsize for atom sorting (equal to the default GPU neighbor binsize) and a more frequent sorting than default (e.g. sorting every 100 time steps instead of 1000) may improve performance.
:::

::: {.admonition .note}
Note

When running on GPUs with many MPI ranks (tens of thousands and more), the creation of the atom map (required for molecular systems) on the GPU can slow down significantly or run out of GPU memory and thus slow down the whole calculation or cause a crash. You can use the [`-pk`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kokkos`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`atom/map`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`no`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} of the [[package kokkos atom/map no]{.doc}]package.md){.reference .internal} command to create the atom map on the CPU instead.
:::

::: {.admonition .note}
Note

When using a GPU, you will achieve the best performance if your input script does not use fix or compute styles which are not yet Kokkos-enabled. This allows data to stay on the GPU for multiple timesteps, without being copied back to the host CPU. Invoking a non-Kokkos fix or compute, or performing I/O for [[thermo]{.doc}]thermo_style.md){.reference .internal} or [[dump]{.doc}]dump.md){.reference .internal} output will cause data to be copied back to the CPU incurring a performance penalty.
:::

::: {.admonition .note}
Note

To get an accurate timing breakdown between time spend in pair, kspace, etc., you must set the environment variable [`CUDA_LAUNCH_BLOCKING=1`{.docutils .literal .notranslate}]{.pre}. However, this will reduce performance and is not recommended for production runs.
:::
::::::::::::::

::: {#troubleshooting-segmentation-faults-on-gpus .section}
### Troubleshooting segmentation faults on GPUs[](#troubleshooting-segmentation-faults-on-gpus "Link to this heading"){.headerlink}

As noted above, KOKKOS by default assumes that the MPI library is GPU-aware. This is not always the case and can lead to segmentation faults when using more than one MPI process. Normally, LAMMPS will print a warning like "*Turning off GPU-aware MPI since it is not detected*", or an error message like "*Kokkos with GPU-enabled backend assumes GPU-aware MPI is available*", OR a **segmentation fault**. To confirm that a segmentation fault is caused by this, you can turn off the GPU-aware assumption via the [[package kokkos command]{.doc}]package.md){.reference .internal} or the corresponding command-line flag.

If you still get a segmentation fault, despite running with only one MPI process or using the command-line flag to turn off expecting a GPU-aware MPI library, then using the CMake compile setting [`-DKokkos_ENABLE_DEBUG=on`{.docutils .literal .notranslate}]{.pre} will generate useful output that can be passed to the LAMMPS developers for further debugging.
:::

::::: {#troubleshooting-memory-allocation-on-gpus .section}
### Troubleshooting memory allocation on GPUs[](#troubleshooting-memory-allocation-on-gpus "Link to this heading"){.headerlink}

[Kokkos Tools](https://github.com/kokkos/kokkos-tools/){.reference .external} provides a set of lightweight profiling and debugging utilities, which interface with instrumentation hooks (eg. [space-time-stack](https://github.com/kokkos/kokkos-tools/tree/develop/profiling/space-time-stack){.reference .external}) built directly into the Kokkos runtime. After compiling a dynamic LAMMPS library, you then have to set the environment variable [`KOKKOS_TOOLS_LIBS`{.docutils .literal .notranslate}]{.pre} before executing your LAMMPS Kokkos run. Example:

:::: {.highlight-bash .notranslate}
::: highlight
    export KOKKOS_TOOLS_LIBS=${HOME}/kokkos-tools/src/tools/memory-events/kp_memory_event.so
    mpirun -np 4 lmp_kokkos_cuda_openmpi -in in.lj -k on g 4 -sf kk
:::
::::

Starting with the NVIDIA Pascal GPU architecture, CUDA supports ["Unified Virtual Memory" (UVM)](https://developer.nvidia.com/blog/unified-memory-cuda-beginners/){.reference .external} which enables allocating more memory than a GPU possesses by also using memory on the host CPU and then CUDA will transparently move data between CPU and GPU as needed. The resulting LAMMPS performance depends on [memory access pattern, data residency, and GPU memory oversubscription](https://developer.nvidia.com/blog/improving-gpu-memory-oversubscription-performance/){.reference .external} . The CMake option [`-DKokkos_ENABLE_CUDA_UVM=on`{.docutils .literal .notranslate}]{.pre} enables using [[UVM with Kokkos]{.std .std-ref}]Build_extras.md#kokkos){.reference .internal} when compiling LAMMPS.
:::::

::::::::::: {#run-with-the-kokkos-package-by-editing-an-input-script .section}
### Run with the KOKKOS package by editing an input script[](#run-with-the-kokkos-package-by-editing-an-input-script "Link to this heading"){.headerlink}

Alternatively the effect of the [`-sf`{.docutils .literal .notranslate}]{.pre} or [`-pk`{.docutils .literal .notranslate}]{.pre} switches can be duplicated by adding the [[package kokkos]{.doc}]package.md){.reference .internal} or [[suffix kk]{.doc}]suffix.md){.reference .internal} commands to your input script.

The discussion above for building LAMMPS with the KOKKOS package, the [`mpirun`{.docutils .literal .notranslate}]{.pre} or [`mpiexec`{.docutils .literal .notranslate}]{.pre} command, and setting appropriate thread properties are the same.

You must still use the [`-k`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal} to enable the KOKKOS package, and specify its additional arguments for hardware options appropriate to your system, as documented above.

You can use the [[suffix kk]{.doc}]suffix.md){.reference .internal} command, or you can explicitly add a "kk" suffix to individual styles in your input script, e.g.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/cut/kk 2.5
:::
::::

You only need to use the [[package kokkos]{.doc}]package.md){.reference .internal} command if you wish to change any of its option defaults, as set by the "-k on" [[command-line switch]{.doc}]Run_options.md){.reference .internal}.

**Using OpenMP threading and CUDA together:**

With the KOKKOS package, both OpenMP multi-threading and GPUs can be compiled and used together in a few special cases. You need to enable both features as it is done in the [`kokkos-cuda.cmake`{.docutils .literal .notranslate}]{.pre} CMake preset file.

:::: {.highlight-bash .notranslate}
::: highlight
    cmake -DKokkos_ENABLE_CUDA=yes -DKokkos_ENABLE_OPENMP=yes ../cmake
:::
::::

The suffix "/kk" is equivalent to "/kk/device", and for Kokkos CUDA, using the [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kk`{.docutils .literal .notranslate}]{.pre} in the command-line gives the default CUDA version everywhere. However, if the "/kk/host" suffix is added to a specific style in the input script, the Kokkos OpenMP (CPU) version of that specific style will be used instead. Set the number of OpenMP threads as [`t`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Nt`{.docutils .literal .notranslate}]{.pre} and the number of GPUs as [`g`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Ng`{.docutils .literal .notranslate}]{.pre}

:::: {.highlight-none .notranslate}
::: highlight
    -k on t Nt g Ng
:::
::::

For example, the command to run with 1 GPU and 8 OpenMP threads is then:

:::: {.highlight-bash .notranslate}
::: highlight
    mpiexec -np 1 lmp_kokkos_cuda_openmpi -in in.lj -k on g 1 t 8 -sf kk
:::
::::

Conversely, if the [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kk/host`{.docutils .literal .notranslate}]{.pre} is used in the command-line and then the "/kk" or "/kk/device" suffix is added to a specific style in your input script, then only that specific style will run on the GPU while everything else will run on the CPU in OpenMP mode. Note that the execution of the CPU and GPU styles will NOT overlap, except for a special case:

A kspace style and/or molecular topology (bonds, angles, etc.) running on the host CPU can overlap with a pair style running on the GPU. First compile with [`--default-stream`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`per-thread`{.docutils .literal .notranslate}]{.pre} added to [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_CXX_FLAGS`{.docutils .literal .notranslate}]{.pre} when configuring with CMake. Then explicitly use the "/kk/host" suffix for kspace and bonds, angles, etc. in the input file and the "kk" suffix (equal to "kk/device") on the command-line. Also make sure the environment variable [`CUDA_LAUNCH_BLOCKING`{.docutils .literal .notranslate}]{.pre} is not set to "1" so CPU/GPU overlap can occur.
:::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

::: {#performance-to-expect .section}
## Performance to expect[](#performance-to-expect "Link to this heading"){.headerlink}

The performance of KOKKOS running in different modes is a function of your hardware, which KOKKOS-enable styles are used, and the problem size.

Generally speaking, the following rules of thumb apply:

- When running on CPUs only, with a single thread per MPI task, performance of a KOKKOS style is somewhere between the standard (un-accelerated) styles (MPI-only mode), and those provided by the OPENMP package. However the difference between all 3 is small (less than 20%).

- When running on CPUs only, with multiple threads per MPI task, performance of a KOKKOS style is a bit slower than the OPENMP package.

- When running large number of atoms per GPU, KOKKOS is typically faster than the GPU package when both are compiled for double precision.

- When running on Intel Phi hardware, KOKKOS is not as fast as the INTEL package, which is optimized for x86 hardware (not just from Intel) and compilation with the Intel compilers.

- The KOKKOS package by default assumes that you are using exactly one MPI rank per GPU. When trying to use multiple MPI ranks per GPU it is mandatory to enable [CUDA Multi-Process Service (MPS)](https://docs.nvidia.com/deploy/mps/index.html){.reference .external} to get good performance. In this case it is better to not use all available MPI ranks in order to avoid competing with the MPS daemon for CPU resources.

See the [Benchmark page](https://www.lammps.org/bench.html){.reference .external} of the LAMMPS website for performance of the KOKKOS package on different hardware.
:::

::: {#advanced-kokkos-options .section}
## Advanced Kokkos options[](#advanced-kokkos-options "Link to this heading"){.headerlink}

There are other allowed options when building with the KOKKOS package that can improve performance or assist in debugging or profiling. They are explained on the [[KOKKOS section of the build extras]{.std .std-ref}]Build_extras.md#kokkos){.reference .internal} doc page,
:::

::: {#references .section}
## References[](#references "Link to this heading"){.headerlink}

**(Johansson)** A. Johansson, E. Weinberg, C. Trott, M. McCarthy, and S. Moore. LAMMPS-KOKKOS: Performance portable molecular dynamics across exascale architectures. In Proceedings of the SC '25 Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis, page 1217-1232, 2025.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

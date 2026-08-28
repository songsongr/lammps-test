:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#openmp-package .section}
# [7.4.4. ]{.section-number}OPENMP package[](#openmp-package "Link to this heading"){.headerlink}

The OPENMP package was developed by Axel Kohlmeyer at Temple University. It provides optimized and multi-threaded versions of many pair styles, nearly all bonded styles (bond, angle, dihedral, improper), several Kspace styles, and a few fix styles. It uses the OpenMP interface for multi-threading, but can also be compiled without OpenMP support, providing optimized serial styles in that case.

::: {#required-hardware-software .section}
## Required hardware/software[](#required-hardware-software "Link to this heading"){.headerlink}

To enable multi-threading, your compiler must support the OpenMP interface. You should have one or more multicore CPUs, as multiple threads can only be launched by each MPI task on the local node (using shared memory).
:::

::: {#building-lammps-with-the-openmp-package .section}
## Building LAMMPS with the OPENMP package[](#building-lammps-with-the-openmp-package "Link to this heading"){.headerlink}

See the [[Build extras]{.std .std-ref}]Build_extras.md#openmp){.reference .internal} page for instructions.
:::

::::: {#run-with-the-openmp-package-from-the-command-line .section}
## Run with the OPENMP package from the command-line[](#run-with-the-openmp-package-from-the-command-line "Link to this heading"){.headerlink}

These examples assume one or more 16-core nodes.

:::: {.highlight-bash .notranslate}
::: highlight
    # 1 MPI task, 16 threads according to OMP_NUM_THREADS
    env OMP_NUM_THREADS=16 lmp_omp -sf omp -in in.script

    # 1 MPI task, no threads, optimized kernels
    lmp_mpi -sf omp -in in.script

    # 4 MPI tasks, 4 threads/task
    mpirun -np 4 lmp_omp -sf omp -pk omp 4 -in in.script

    # 8 nodes, 4 MPI tasks/node, 4 threads/task
    mpirun -np 32 -ppn 4 lmp_omp -sf omp -pk omp 4 -in in.script
:::
::::

The [`mpirun`{.docutils .literal .notranslate}]{.pre} or [`mpiexec`{.docutils .literal .notranslate}]{.pre} command sets the total number of MPI tasks used by LAMMPS (one or multiple per compute node) and the number of MPI tasks used per node. E.g. the mpirun command in MPICH does this via its [`-np`{.docutils .literal .notranslate}]{.pre} and [`-ppn`{.docutils .literal .notranslate}]{.pre} switches. Ditto for OpenMPI via [`-np`{.docutils .literal .notranslate}]{.pre} and [`-npernode`{.docutils .literal .notranslate}]{.pre}.

You need to choose how many OpenMP threads per MPI task will be used by the OPENMP package. Note that the product of MPI tasks \* threads/task should not exceed the physical number of cores (on a node), otherwise performance will suffer.

As in the lines above, use the [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`omp`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal}, which will automatically append "omp" to styles that support it. The [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`omp`{.docutils .literal .notranslate}]{.pre} switch also issues a default [[package omp 0]{.doc}]package.md){.reference .internal} command, which will set the number of threads per MPI task via the [`OMP_NUM_THREADS`{.docutils .literal .notranslate}]{.pre} environment variable.

You can also use the [`-pk`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`omp`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Nt`{.docutils .literal .notranslate}]{.pre} [[command-line switch]{.doc}]Run_options.md){.reference .internal}, to explicitly set [`Nt`{.docutils .literal .notranslate}]{.pre} = \# of OpenMP threads per MPI task to use, as well as additional options. Its syntax is the same as the [[package omp]{.doc}]package.md){.reference .internal} command whose page gives details, including the default values used if it is not specified. It also gives more details on how to set the number of threads via the [`OMP_NUM_THREADS`{.docutils .literal .notranslate}]{.pre} environment variable.
:::::

::::: {#or-run-with-the-openmp-package-by-editing-an-input-script .section}
## Or run with the OPENMP package by editing an input script[](#or-run-with-the-openmp-package-by-editing-an-input-script "Link to this heading"){.headerlink}

The discussion above for the [`mpirun`{.docutils .literal .notranslate}]{.pre} or [`mpiexec`{.docutils .literal .notranslate}]{.pre} command, MPI tasks/node, and threads/MPI task is the same.

Use the [[suffix omp]{.doc}]suffix.md){.reference .internal} command, or you can explicitly add an "omp" suffix to individual styles in your input script, e.g.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/cut/omp 2.5
:::
::::

You must also use the [[package omp]{.doc}]package.md){.reference .internal} command to enable the OPENMP package. When you do this you also specify how many threads per MPI task to use. The command page explains other options and how to set the number of threads via the [`OMP_NUM_THREADS`{.docutils .literal .notranslate}]{.pre} environment variable.
:::::

::: {#speed-up-to-expect .section}
## Speed-up to expect[](#speed-up-to-expect "Link to this heading"){.headerlink}

Depending on which styles are accelerated, you should look for a reduction in the "Pair time", "Bond time", "KSpace time", and "Loop time" values printed at the end of a run.

You may see a small performance advantage (5 to 20%) when running a OPENMP style (in serial or parallel) with a single thread per MPI task, versus running standard LAMMPS with its standard un-accelerated styles (in serial or all-MPI parallelization with 1 task/core). This is because many of the OPENMP styles contain similar optimizations to those used in the OPT package, described in [[the OPT package]{.doc}]Speed_opt.md){.reference .internal} doc page.

With multiple threads/task, the optimal choice of number of MPI tasks/node and OpenMP threads/task can vary a lot and should always be tested via benchmark runs for a specific simulation running on a specific machine, paying attention to guidelines discussed in the next subsection.

A description of the multi-threading strategy used in the OPENMP package and some performance examples are [presented here](https://drive.google.com/file/d/1d1gLK6Ru6aPYB50Ld2tO10Li8zgPVNB8/view?usp=sharing){.reference .external}.
:::

::: {#guidelines-for-best-performance .section}
## Guidelines for best performance[](#guidelines-for-best-performance "Link to this heading"){.headerlink}

For many problems on current generation CPUs, running the OPENMP package with a single thread/task is faster than running with multiple threads/task. This is because the MPI parallelization in LAMMPS is often more efficient than multi-threading as implemented in the OPENMP package. The parallel efficiency (in a threaded sense) also varies for different OPENMP styles.

Using multiple threads/task can be more effective under the following circumstances:

- Individual compute nodes have a significant number of CPU cores but the CPU itself has limited memory bandwidth, e.g. for Intel Xeon 53xx (Clovertown) and 54xx (Harpertown) quad-core processors. Running one MPI task per CPU core will result in significant performance degradation, so that running with 4 or even only 2 MPI tasks per node is faster. Running in hybrid MPI+OpenMP mode will reduce the inter-node communication bandwidth contention in the same way, but offers an additional speedup by utilizing the otherwise idle CPU cores.

- The interconnect used for MPI communication does not provide sufficient bandwidth for a large number of MPI tasks per node. For example, this applies to running over gigabit ethernet or on Cray XT4 or XT5 series supercomputers. As in the aforementioned case, this effect worsens when using an increasing number of nodes.

- The system has a spatially inhomogeneous particle density which does not map well to the [[domain decomposition scheme]{.doc}]processors.md){.reference .internal} or [[load-balancing]{.doc}]balance.md){.reference .internal} options that LAMMPS provides. This is because multi-threading achieves parallelism over the number of particles, not via their distribution in space.

- A machine is being used in "capability mode", i.e. near the point where MPI parallelism is maxed out. For example, this can happen when using the [[PPPM solver]{.doc}]kspace_style.md){.reference .internal} for long-range electrostatics on large numbers of nodes. The scaling of the KSpace calculation (see the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command) becomes the performance-limiting factor. Using multi-threading allows less MPI tasks to be invoked and can speed-up the long-range solver, while increasing overall performance by parallelizing the pairwise and bonded calculations via OpenMP. Likewise, additional speedup can sometimes be achieved by increasing the length of the Coulombic cutoff and thus reducing the work done by the long-range solver. Using the [[run_style verlet/split]{.doc}]run_style.md){.reference .internal} command, which is compatible with the OPENMP package, is an alternative way to reduce the number of MPI tasks assigned to the KSpace calculation.

Additional performance tips are as follows:

- The best parallel efficiency from *omp* styles is typically achieved when there is at least one MPI task per physical CPU chip, i.e. socket or die.

- It is usually most efficient to restrict threading to a single socket, i.e. use one or more MPI task per socket.

- NOTE: By default, several current MPI implementations use a processor affinity setting that restricts each MPI task to a single CPU core. Using multi-threading in this mode will force all threads to share the one core and thus is likely to be counterproductive. Instead, binding MPI tasks to a (multicore) socket, should solve this issue.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

None.
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

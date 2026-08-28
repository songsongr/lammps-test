::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#multi-replica-simulations .section}
# [10.1.6. ]{.section-number}Multi-replica simulations[](#multi-replica-simulations "Link to this heading"){.headerlink}

Several commands in LAMMPS run multi-replica simulations, meaning that multiple instances (replicas) of your simulation are run simultaneously, with small amounts of data exchanged between replicas periodically.

These are the relevant commands:

- [[hyper]{.doc}]hyper.md){.reference .internal} for bond boost hyperdynamics (HD)

- [[neb]{.doc}]neb.md){.reference .internal} for nudged elastic band calculations (NEB)

- [[neb_spin]{.doc}]neb_spin.md){.reference .internal} for magnetic nudged elastic band calculations

- [[prd]{.doc}]prd.md){.reference .internal} for parallel replica dynamics (PRD)

- [[tad]{.doc}]tad.md){.reference .internal} for temperature accelerated dynamics (TAD)

- [[temper]{.doc}]temper.md){.reference .internal} for parallel tempering with fixed volume

- [[temper/npt]{.doc}]temper_npt.md){.reference .internal} for parallel tempering extended for NPT

- [[temper/grem]{.doc}]temper_grem.md){.reference .internal} for parallel tempering with generalized replica exchange (gREM)

- [[fix pimd]{.doc}]fix_pimd.md){.reference .internal} for path-integral molecular dynamics (PIMD)

NEB is a method for finding transition states and barrier potential energies. HD, PRD, and TAD are methods for performing accelerated dynamics to find and perform infrequent events. Parallel tempering or replica exchange runs different replicas at a series of temperature to facilitate rare-event sampling. PIMD runs different replicas whose individual particles in different replicas are coupled together by springs to model a system of ring-polymers which can represent the quantum nature of atom cores.

These commands can only be used if LAMMPS was built with the REPLICA package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

In all these cases, you must run with one or more processors per replica. The processors assigned to each replica are determined at run-time by using the [[-partition command-line switch]{.doc}]Run_options.md){.reference .internal} to launch LAMMPS on multiple partitions, which in this context are the same as replicas. E.g. these commands:

:::: {.highlight-bash .notranslate}
::: highlight
    mpirun -np 16 lmp_linux -partition 8x2 -in in.temper
    mpirun -np 8 lmp_linux -partition 8x1 -in in.neb
:::
::::

would each run 8 replicas, on either 16 or 8 processors. Note the use of the [[-in command-line switch]{.doc}]Run_options.md){.reference .internal} to specify the input script which is required when running in multi-replica mode.

Also note that with MPI installed on a machine (e.g. your desktop), you can run on more (virtual) processors than you have physical processors. Thus, the above commands could be run on a single-processor (or few-processor) desktop so that you can run a multi-replica simulation on more replicas than you have physical processors. This is useful for testing and debugging, since with most modern processors and MPI libraries, the efficiency of a calculation can severely diminish when oversubscribing processors.
:::::
::::::
:::::::

:::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::: {#command-line-options .section}
# [4.2. ]{.section-number}Command-line options[](#command-line-options "Link to this heading"){.headerlink}

At run time, LAMMPS recognizes several optional command-line switches which may be used in any order. Either the full word or a one or two letter abbreviation can be used:

- [[-e or -echo]{.std .std-ref}](#echo){.reference .internal}

- [[-h or -help]{.std .std-ref}](#help){.reference .internal}

- [[-i or -in]{.std .std-ref}](#file){.reference .internal}

- [[-k or -kokkos]{.std .std-ref}](#run-kokkos){.reference .internal}

- [[-l or -log]{.std .std-ref}](#log){.reference .internal}

- [[-mdi]{.std .std-ref}](#mdi-flags){.reference .internal}

- [[-m or -mpicolor]{.std .std-ref}](#mpicolor){.reference .internal}

- [[-c or -cite]{.std .std-ref}](#cite){.reference .internal}

- [[-nc or -nocite]{.std .std-ref}](#nocite){.reference .internal}

- [[-nb or -nonbuf]{.std .std-ref}](#nonbuf){.reference .internal}

- [[-pk or -package]{.std .std-ref}](#package){.reference .internal}

- [[-p or -partition]{.std .std-ref}](#partition){.reference .internal}

- [[-pl or -plog]{.std .std-ref}](#plog){.reference .internal}

- [[-ps or -pscreen]{.std .std-ref}](#pscreen){.reference .internal}

- [[-ro or -reorder]{.std .std-ref}](#reorder){.reference .internal}

- [[-r2data or -restart2data]{.std .std-ref}](#restart2data){.reference .internal}

- [[-r2dump or -restart2dump]{.std .std-ref}](#restart2dump){.reference .internal}

- [[-r2info or -restart2info]{.std .std-ref}](#restart2info){.reference .internal}

- [[-sc or -screen]{.std .std-ref}](#screen){.reference .internal}

- [[-sr or skiprun]{.std .std-ref}](#skiprun){.reference .internal}

- [[-sf or -suffix]{.std .std-ref}](#suffix){.reference .internal}

- [[-v or -var]{.std .std-ref}](#var){.reference .internal}

For example, the lmp_mpi executable might be launched as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    mpirun -np 16 lmp_mpi -v f tmp.out -l my.log -sc none -i in.alloy
    mpirun -np 16 lmp_mpi -var f tmp.out -log my.log -screen none -in in.alloy
:::
::::

------------------------------------------------------------------------

**-echo style**

Set the style of command echoing. The style can be *none* or *screen* or *log* or *both*. Depending on the style, each command read from the input script will be echoed to the screen and/or logfile. This can be useful to figure out which line of your script is causing an input error. The default value is *log*. The echo style can also be set by using the [[echo]{.doc}]echo.md){.reference .internal} command in the input script itself.

------------------------------------------------------------------------

**-help**

Print a brief help summary and a list of options compiled into this executable for each LAMMPS style (atom_style, fix, compute, pair_style, bond_style, etc). This can tell you if the command you want to use was included via the appropriate package at compile time. LAMMPS will print the info and immediately exit if this switch is used.

------------------------------------------------------------------------

**-in file**

Specify a file to use as an input script. This is currently an optional but recommended switch when running LAMMPS in the default one-partition mode. If it is not specified, LAMMPS reads its script from standard input, typically from a script via I/O redirection; e.g. [`lmp_linux`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`<`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`in.run`{.docutils .literal .notranslate}]{.pre}. With many MPI implementations (but not all of them), I/O redirection also works in parallel, but using the [`-in`{.docutils .literal .notranslate}]{.pre} flag will *always* work.

This is a **required** switch when running LAMMPS in multi-partition mode (see below), since multiple pools of MPI processes cannot all read from standard input concurrently. The file name may be "none" for starting multi-partition calculations without reading an initial input file when using the library interface.

------------------------------------------------------------------------

**-kokkos on/off keyword/value ...**

Explicitly enable or disable KOKKOS support, as provided by the KOKKOS package. Even if LAMMPS is built with this package, as described in the [[the KOKKOS package page]{.doc}]Speed_kokkos.md){.reference .internal}, this switch must be set to enable running with KOKKOS-enabled styles the package provides. If the switch is not set (the default), LAMMPS will operate as if the KOKKOS package were not installed; i.e. you can run standard LAMMPS or with the GPU or OPENMP packages, for testing or benchmarking purposes.

Additional optional keyword/value pairs can be specified which determine how Kokkos will use the underlying hardware on your platform. These settings apply to each MPI task you launch via the [`mpirun`{.docutils .literal .notranslate}]{.pre} or [`mpiexec`{.docutils .literal .notranslate}]{.pre} command. You may choose to run one or more MPI tasks per physical node. Note that if you are running on a desktop machine, you typically have one physical node. On a cluster or supercomputer there may be dozens or 1000s of physical nodes.

Either the full word or an abbreviation can be used for the keywords. Note that the keywords do not use a leading minus sign. I.e. the keyword is "t", not "-t". Also note that each of the keywords has a default setting. Examples of when to use these options and what settings to use on different platforms is given on the [[KOKKOS package]{.doc}]Speed_kokkos.md){.reference .internal} doc page.

- d or device

- g or gpus

- t or threads

:::: {.highlight-none .notranslate}
::: highlight
    device Nd
:::
::::

This option is only relevant if you built LAMMPS with CUDA=yes, you have more than one GPU per node, and if you are running with only one MPI task per node. The Nd setting is the ID of the GPU on the node to run on. By default Nd = 0. If you have multiple GPUs per node, they have consecutive IDs numbered as 0,1,2,etc. This setting allows you to launch multiple independent jobs on the node, each with a single MPI task per node, and assign each job to run on a different GPU.

:::: {.highlight-none .notranslate}
::: highlight
    gpus Ng Ns
:::
::::

This option is only relevant if you built LAMMPS with CUDA=yes, you have more than one GPU per node, and you are running with multiple MPI tasks per node (up to one per GPU). The Ng setting is how many GPUs you will use. The Ns setting is optional. If set, it is the ID of a GPU to skip when assigning MPI tasks to GPUs. This may be useful if your desktop system reserves one GPU to drive the screen and the rest are intended for computational work like running LAMMPS. By default Ng = 1 and Ns is not set.

Depending on which flavor of MPI you are running, LAMMPS will look for one of these 4 environment variables

:::: {.highlight-none .notranslate}
::: highlight
    SLURM_LOCALID (various MPI variants compiled with SLURM support)
    MPT_LRANK (HPE MPI)
    MV2_COMM_WORLD_LOCAL_RANK (Mvapich)
    OMPI_COMM_WORLD_LOCAL_RANK (OpenMPI)
:::
::::

which are initialized by the [`srun`{.docutils .literal .notranslate}]{.pre}, [`mpirun`{.docutils .literal .notranslate}]{.pre}, or [`mpiexec`{.docutils .literal .notranslate}]{.pre} commands. The environment variable setting for each MPI rank is used to assign a unique GPU ID to the MPI task.

:::: {.highlight-none .notranslate}
::: highlight
    threads Nt
:::
::::

This option assigns Nt number of threads to each MPI task for performing work when Kokkos is executing in OpenMP or pthreads mode. The default is Nt = 1, which essentially runs in MPI-only mode. If there are Np MPI tasks per physical node, you generally want Np\*Nt = the number of physical cores per node, to use your available hardware optimally. This also sets the number of threads used by the host when LAMMPS is compiled with CUDA=yes.

::: deprecated
[Deprecated since version 22Dec2022.]{.versionmodified .deprecated}
:::

Support for the "numa" or "n" option was removed as its functionality was ignored in Kokkos for some time already.

------------------------------------------------------------------------

**-log file**

Specify a log file for LAMMPS to write status information to. In one-partition mode, if the switch is not used, LAMMPS writes to the file log.lammps. If this switch is used, LAMMPS writes to the specified file. In multi-partition mode, if the switch is not used, a log.lammps file is created with high-level status information. Each partition also writes to a log.lammps.N file where N is the partition ID. If the switch is specified in multi-partition mode, the high-level logfile is named "file" and each partition also logs information to a file.N. For both one-partition and multi-partition mode, if the specified file is "none", then no log files are created. Using a [[log]{.doc}]log.md){.reference .internal} command in the input script will override this setting. Option -plog will override the name of the partition log files file.N.

------------------------------------------------------------------------

**-mdi 'multiple flags'**

This flag is only recognized and used when LAMMPS has support for the MolSSI Driver Interface (MDI) included as part of the [[MDI]{.std .std-ref}]Packages_details.md#pkg-mdi){.reference .internal} package. This flag is specific to the MDI library and controls how LAMMPS interacts with MDI. There are usually multiple flags that have to follow it and those have to be placed in quotation marks. For more information about how to launch LAMMPS in MDI client/server mode please refer to the [[MDI Howto]{.doc}]Howto_mdi.md){.reference .internal}.

------------------------------------------------------------------------

**-mpicolor color**

If used, this must be the first command-line argument after the LAMMPS executable name. It is only used when LAMMPS is launched by an mpirun command which also launches another executable(s) at the same time (The other executable could be LAMMPS as well.). The *color* is an integer value which should be different for each executable (another application may set this value in a different way). LAMMPS and the other executable(s) perform an [MPI_Comm_split()](https://docs.open-mpi.org/en/main/man-openmpi/man3/MPI_Comm_split.3.html){.reference .external} with their own colors to replace the [`MPI_COMM_WORLD`{.docutils .literal .notranslate}]{.pre} communicator with a new communicator using the subset of MPI processes they are actually running on.

------------------------------------------------------------------------

**-cite style** or **file name**

Select how and where to output a reminder about citing contributions to the LAMMPS code that were used during the run. Available keywords for styles are "both", "none", "screen", or "log". Any other keyword will be considered a file name to write the detailed citation info to instead of logfile or screen. Default is the "log" style where there is a short summary in the screen output and detailed citations in BibTeX format in the logfile. The option "both" selects the detailed output for both, "none", the short output for both, and "screen" will write the detailed info to the screen and the short version to the log file. If a dedicated citation info file is requested, the screen and log file output will be in the short format (same as with "none").

See the [[citation page]{.doc}]Intro_citing.md){.reference .internal} for more details on how to correctly reference and cite LAMMPS.

------------------------------------------------------------------------

**-nocite**

Disable generating a citation reminder (see above) at all.

------------------------------------------------------------------------

**-nonbuf**

::: versionadded
[Added in version 15Sep2022.]{.versionmodified .added}
:::

Turn off buffering for screen and logfile output. For performance reasons, output to the screen and logfile is usually buffered, i.e. output is only written to a file if its buffer - typically 4096 bytes - has been filled. When LAMMPS crashes for some reason, however, that can mean that there is important output missing. With this flag the buffering can be turned off (only for screen and logfile output) and any output will be committed immediately. Note that when running in parallel with MPI, the screen output may still be buffered by the MPI library and this cannot be changed by LAMMPS. This flag should only be used for debugging and not for production simulations as the performance impact can be significant, especially for large parallel runs.

------------------------------------------------------------------------

**-package style args ....**

Invoke the [[package]{.doc}]package.md){.reference .internal} command with style and args. The syntax is the same as if the command appeared at the top of the input script. For example [`-package`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gpu`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`2`{.docutils .literal .notranslate}]{.pre} or [`-pk`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gpu`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`2`{.docutils .literal .notranslate}]{.pre} is the same as [[package gpu 2]{.doc}]package.md){.reference .internal} in the input script. The possible styles and args are documented on the [[package]{.doc}]package.md){.reference .internal} doc page. This switch can be used multiple times, e.g. to set options for the INTEL and OPENMP packages which can be used together.

Along with the [`-suffix`{.docutils .literal .notranslate}]{.pre} command-line switch, this is a convenient mechanism for invoking accelerator packages and their options without having to edit an input script.

------------------------------------------------------------------------

**-partition 8x2 4 5 ...**

Invoke LAMMPS in multi-partition mode. When LAMMPS is run on *P* MPI processes and this switch is not used, LAMMPS runs in *one partition*, i.e. all *P* MPI processes run a single simulation with the same settings. If this switch *is* used, the *P* MPI processes are split into separate partitions and each partition runs its own simulation. The arguments to the switch specify the number of MPI processes in each partition. Arguments of the form *MxN* mean *M* partitions, each with *N* MPI processes. Arguments of the form *N* mean a single partition with *N* MPI processes. The sum of MPI processes in all partitions must equal *P*. Thus the command [`-partition`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`8x2`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`4`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`5`{.docutils .literal .notranslate}]{.pre} has 10 partitions (eight with 2 MPI processes, one with 4 and one with 5) and runs on a total of 25 MPI processes.

Running with multiple partitions can be useful for running [[multi-replica simulations]{.doc}]Howto_replica.md){.reference .internal}, where each replica runs on one or a few MPI processes.

::: {.admonition .note}
Note

With MPI installed on a standalone machine (e.g. your desktop or laptop), you can run on more (virtual) MPI processes than you have physical processors (for testing purposes), but some MPI implementations (for instance [OpenMPI](https://www.open-mpi.org/){.reference .external}) may require an additional command line flag to enable this so-called oversubscription. You may also have to disable [processor affinity](https://en.wikipedia.org/wiki/Processor_affinity){.reference .external} or else the performance may be exceptionally bad when oversubscribing processors.
:::

To run multiple independent simulations from one input script, using multiple partitions, see the [[Howto multiple]{.doc}]Howto_multiple.md){.reference .internal} page. World- and universe-style [[variables]{.doc}]variable.md){.reference .internal} are useful in this context.

------------------------------------------------------------------------

**-plog file**

Specify the base name for the partition log files, so partition *N* writes log information to [`file.N`{.docutils .literal .notranslate}]{.pre}. If *file* is *none*, then no partition log files are created. This overrides the filename specified in the *-log* command-line option. This option is useful when working with large numbers of partitions, allowing the partition log files to be suppressed ([`-plog`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`none`{.docutils .literal .notranslate}]{.pre}) or placed in a subdirectory ([`-plog`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`replica_files/log.lammps`{.docutils .literal .notranslate}]{.pre}). If this option is not used, the log file for partition *N* is [`log.lammps.N`{.docutils .literal .notranslate}]{.pre} or whatever is specified by the *-log* command-line option.

------------------------------------------------------------------------

**-pscreen file**

Specify the base name for the partition screen file, so partition *N* writes screen information to [`file.N`{.docutils .literal .notranslate}]{.pre}. If *file* is *none*, then no partition screen files are created. This overrides the filename specified in the *-screen* command-line option. This option is useful when working with large numbers of partitions, allowing the partition screen files to be suppressed ([`-pscreen`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`none`{.docutils .literal .notranslate}]{.pre}) or placed in a subdirectory ([`-pscreen`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`replica_files/screen`{.docutils .literal .notranslate}]{.pre}). If this option is not used, the screen file for partition *N* is [`screen.N`{.docutils .literal .notranslate}]{.pre} or whatever is specified by the *-screen* command-line option.

------------------------------------------------------------------------

**-reorder**

This option has 2 forms:

:::: {.highlight-none .notranslate}
::: highlight
    -reorder nth N
    -reorder custom filename
:::
::::

Reorder the ranks in the MPI communicator used to instantiate LAMMPS, in one of several ways. The original MPI communicator ranks all *P* MPI processes from *0* to *P-1*. The mapping of these ranks to physical processors is done by the MPI library before LAMMPS begins. It may be useful in some cases to alter the order of the ranks, for example to ensure that cores within each node are ranked in a desired order. Or when using the [[run_style verlet/split]{.doc}]run_style.md){.reference .internal} command with 2 partitions to ensure that a specific Kspace processor (in the second partition) is matched up with a specific set of processors in the first partition. See the [[General tips]{.doc}]Speed_tips.md){.reference .internal} page for more details.

If the keyword *nth* is used with a setting *N*, then it means every Nth processor will be moved to the end of the ranking. This is useful when using the [[run_style verlet/split]{.doc}]run_style.md){.reference .internal} command with 2 partitions via the *-partition* command-line switch. The first set of processors will be in the first partition, the second set in the second partition. The *-reorder* command-line switch can alter this so that the first *N* MPI processes in the first partition and one MPI process in the second partition will be ordered consecutively, e.g. as the cores on one physical node. This can boost performance. For example, if you use [`-reorder`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`nth`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`4`{.docutils .literal .notranslate}]{.pre} and [`-partition`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`9`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`3`{.docutils .literal .notranslate}]{.pre} and you are running on 12 processors, the MPI process ranks will be reordered from

:::: {.highlight-none .notranslate}
::: highlight
    0 1 2 3 4 5 6 7 8 9 10 11
:::
::::

to

:::: {.highlight-none .notranslate}
::: highlight
    0 1 2 4 5 6 8 9 10 3 7 11
:::
::::

so that the processors in each partition will be

:::: {.highlight-none .notranslate}
::: highlight
    0 1 2 4 5 6 8 9 10
    3 7 11
:::
::::

See the "processors" command for how to ensure processors from each partition could then be grouped optimally for quad-core nodes.

If the keyword is *custom*, then a file that specifies a permutation of the processor ranks is also specified. The format of the reorder file is as follows. Any number of initial blank or comment lines (starting with a "#" character) can be present. These should be followed by *P* lines of the form:

:::: {.highlight-none .notranslate}
::: highlight
    I J
:::
::::

where *P* is the number of processors LAMMPS was launched with. Note that if running in multi-partition mode (see the -partition switch above) *P* is the total number of MPI processes in all partitions. The *I* and *J* values describe a permutation of the *P* MPI process ranks. Every *I* and *J* should be values from *0* to *P-1* inclusive. In the set of *P* *I* values, every MPI rank ID should appear exactly once. Ditto for the set of *P* *J* values. A single *I*, *J* pairing means that the physical processor with MPI rank *I* in the original MPI communicator will have rank *J* in the reordered MPI communicator.

Note that rank ordering can also be specified by many MPI implementations, either by environment variables that specify how to order physical processors, or by config files that specify what physical processors to assign to each MPI rank. The *-reorder* switch simply gives you a portable way to do this without relying on MPI itself. See the [[processors file]{.doc}]processors.md){.reference .internal} command for how to output info on the final assignment of physical processors to the LAMMPS simulation domain.

------------------------------------------------------------------------

**-restart2data restartfile datafile keyword value ...**

Convert the restart file into a data file and immediately exit. This is the same operation as if the following 2-line input script were run:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    read_restart restartfile
    write_data datafile keyword value ...
:::
::::

The specified restartfile and/or datafile name may contain the wild-card character "\*". The restartfile name may also contain the wild-card character "%". The meaning of these characters is explained on the [[read_restart]{.doc}]read_restart.md){.reference .internal} and [[write_data]{.doc}]write_data.md){.reference .internal} doc pages. The use of "%" means that a parallel restart file can be read. Note that a filename such as file.\* may need to be enclosed in quotes or the "\*" character prefixed with a backslash ("\") to avoid shell expansion of the "\*" character.

The syntax following restartfile, namely

:::: {.highlight-none .notranslate}
::: highlight
    datafile keyword value ...
:::
::::

is identical to the arguments of the [[write_data]{.doc}]write_data.md){.reference .internal} command. See its documentation page for details. This includes its optional keyword/value settings.

------------------------------------------------------------------------

**-restart2dump restartfile group-ID dumpstyle dumpfile arg1 arg2 ...**

Convert the restart file into a dump file and immediately exit. This is the same operation as if the following 2-line input script were run:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    read_restart restartfile
    write_dump group-ID dumpstyle dumpfile arg1 arg2 ...
:::
::::

Note that the specified restartfile and dumpfile names may contain wild-card characters ("\*" or "%") as explained on the [[read_restart]{.doc}]read_restart.md){.reference .internal} and [[write_dump]{.doc}]write_dump.md){.reference .internal} doc pages. The use of "%" means that a parallel restart file and/or parallel dump file can be read and/or written. Note that a filename such as file.\* may need to be enclosed in quotes or the "\*" character prefixed with a backslash ("\") to avoid shell expansion of the "\*" character.

The syntax following restartfile, namely

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    group-ID dumpstyle dumpfile arg1 arg2 ...
:::
::::

is identical to the arguments of the [[write_dump]{.doc}]write_dump.md){.reference .internal} command. See its documentation page for details. This includes what per-atom fields are written to the dump file and optional dump_modify settings, including ones that affect how parallel dump files are written, e.g. the *nfile* and *fileper* keywords. See the [[dump_modify]{.doc}]dump_modify.md){.reference .internal} page for details.

------------------------------------------------------------------------

**-restart2info restartfile keyword ...**

::: versionadded
[Added in version 29Aug2024.]{.versionmodified .added}
:::

Write out some info about the restart file and and immediately exit. This is the same operation as if the following 2-line input script were run:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    read_restart restartfile
    info system group computes fixes
:::
::::

The specified restartfile name may contain the wild-card character "\*". The restartfile name may also contain the wild-card character "%". The meaning of these characters is explained on the [[read_restart]{.doc}]read_restart.md){.reference .internal} documentation. The use of "%" means that a parallel restart file can be read. Note that a filename such as file.\* may need to be enclosed in quotes or the "\*" character prefixed with a backslash ("\") to avoid shell expansion of the "\*" character.

Optional keywords may follow the restartfile argument. These must be valid keywords for the [[info command]{.doc}]info.md){.reference .internal}. The most useful ones - *system*, *group*, *computes*, and *fixes* - are already applied. Appending keywords like *coeffs* or *communication* may provide additional useful information stored in the restart file.

------------------------------------------------------------------------

**-screen file**

Specify a file for LAMMPS to write its screen information to. In one-partition mode, if the switch is not used, LAMMPS writes to the screen. If this switch is used, LAMMPS writes to the specified file instead and you will see no screen output. In multi-partition mode, if the switch is not used, high-level status information is written to the screen. Each partition also writes to a screen.N file where N is the partition ID. If the switch is specified in multi-partition mode, the high-level screen dump is named "file" and each partition also writes screen information to a file.N. For both one-partition and multi-partition mode, if the specified file is "none", then no screen output is performed. Option -pscreen will override the name of the partition screen files file.N.

------------------------------------------------------------------------

**-skiprun**

Insert the command [[timer timeout 0 every 1]{.doc}]timer.md){.reference .internal} at the beginning of an input file or after a [[clear]{.doc}]clear.md){.reference .internal} command. This has the effect that the entire LAMMPS input script is processed without executing actual [[run]{.doc}]run.md){.reference .internal} or [[minimize]{.doc}]minimize.md){.reference .internal} and similar commands (their main loops are skipped). This can be helpful and convenient to test input scripts of long running calculations for correctness to avoid having them crash after a long time due to a typo or syntax error in the middle or at the end.

------------------------------------------------------------------------

**-suffix style args**

Use variants of various styles if they exist. The specified style can be *gpu*, *intel*, *kk*, *omp*, *opt*, or *hybrid*. These refer to optional packages that LAMMPS can be built with, as described in [[Accelerate performance]{.doc}]Speed.md){.reference .internal}. The "gpu" style corresponds to the GPU package, the "intel" style to the INTEL package, the "kk" style to the KOKKOS package, the "opt" style to the OPT package, and the "omp" style to the OPENMP package. The hybrid style is the only style that accepts arguments. It allows for two packages to be specified. The first package specified is the default and will be used if it is available. If no style is available for the first package, the style for the second package will be used if available. For example, [`-suffix`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`hybrid`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`intel`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`omp`{.docutils .literal .notranslate}]{.pre} will use styles from the INTEL package if they are installed and available, but styles for the OPENMP package otherwise.

Along with the [`-package`{.docutils .literal .notranslate}]{.pre} command-line switch, this is a convenient mechanism for invoking accelerator packages and their options without having to edit an input script.

As an example, all of the packages provide a [[pair_style lj/cut]{.doc}]pair_lj.md){.reference .internal} variant, with style names lj/cut/gpu, lj/cut/intel, lj/cut/kk, lj/cut/omp, and lj/cut/opt. A variant style can be specified explicitly in your input script, e.g. pair_style lj/cut/gpu. If the -suffix switch is used the specified suffix (gpu,intel,kk,omp,opt) is automatically appended whenever your input script command creates a new [[atom style]{.doc}]atom_style.md){.reference .internal}, [[pair style]{.doc}]pair_style.md){.reference .internal}, [[fix]{.doc}]fix.md){.reference .internal}, [[compute]{.doc}]compute.md){.reference .internal}, or [[run style]{.doc}]run_style.md){.reference .internal}. If the variant version does not exist, the standard version is created.

For the GPU package, using this command-line switch also invokes the default GPU settings, as if the command "package gpu 1" were used at the top of your input script. These settings can be changed by using the [`-package`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gpu`{.docutils .literal .notranslate}]{.pre} command-line switch or the [[package gpu]{.doc}]package.md){.reference .internal} command in your script.

For the INTEL package, using this command-line switch also invokes the default INTEL settings, as if the command "package intel 1" were used at the top of your input script. These settings can be changed by using the [`-package`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`intel`{.docutils .literal .notranslate}]{.pre} command-line switch or the [[package intel]{.doc}]package.md){.reference .internal} command in your script. If the OPENMP package is also installed, the hybrid style with "intel omp" arguments can be used to make the omp suffix a second choice, if a requested style is not available in the INTEL package. It will also invoke the default OPENMP settings, as if the command "package omp 0" were used at the top of your input script. These settings can be changed by using the [`-package`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`omp`{.docutils .literal .notranslate}]{.pre} command-line switch or the [[package omp]{.doc}]package.md){.reference .internal} command in your script.

For the KOKKOS package, using this command-line switch also invokes the default KOKKOS settings, as if the command "package kokkos" were used at the top of your input script. These settings can be changed by using the [`-package`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kokkos`{.docutils .literal .notranslate}]{.pre} command-line switch or the [[package kokkos]{.doc}]package.md){.reference .internal} command in your script.

For the OMP package, using this command-line switch also invokes the default OMP settings, as if the command "package omp 0" were used at the top of your input script. These settings can be changed by using the [`-package`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`omp`{.docutils .literal .notranslate}]{.pre} command-line switch or the [[package omp]{.doc}]package.md){.reference .internal} command in your script.

The [[suffix]{.doc}]suffix.md){.reference .internal} command can also be used within an input script to set a suffix, or to turn off or back on any suffix setting made via the command-line.

------------------------------------------------------------------------

**-var name value1 value2 ...**

Specify a variable that will be defined for substitution purposes when the input script is read. This switch can be used multiple times to define multiple variables. "Name" is the variable name which can be a single character (referenced as \$x in the input script) or a full string (referenced as \${abc}). An [[index-style variable]{.doc}]variable.md){.reference .internal} will be created and populated with the subsequent values, e.g. a set of filenames. Using this command-line option is equivalent to putting the line "variable name index value1 value2 ..." at the beginning of the input script. Defining an index variable as a command-line argument overrides any setting for the same index variable in the input script, since index variables cannot be re-defined.

See the [[variable]{.doc}]variable.md){.reference .internal} command for more info on defining index and other kinds of variables and the [[Parsing rules]{.doc}]Commands_parse.md){.reference .internal} page for more info on using variables in input scripts.

::: {.admonition .note}
Note

Currently, the command-line parser looks for arguments that start with "-" to indicate new switches. Thus you cannot specify multiple variable values if any of them start with a "-", e.g. a negative numeric value. It is OK if the first value1 starts with a "-", since it is automatically skipped.
:::
::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

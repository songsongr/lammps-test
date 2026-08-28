:::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::: {#debugging-crashes .section}
# [5.4. ]{.section-number}Debugging crashes[](#debugging-crashes "Link to this heading"){.headerlink}

If LAMMPS crashes with a "segmentation fault" or a "bus error" or similar message, then you can use the following two methods to further narrow down the origin of the issue. This will help the LAMMPS developers (or yourself) to understand the reason for the crash and apply a fix (either to the input script or the source code). This requires that your LAMMPS executable includes the required [[debug information]{.std .std-ref}]Build_basics.md#debug){.reference .internal}. Otherwise it is not possible to look up the names of functions or variables.

The following patch will introduce a bug into the code for pair style [[lj/cut]{.doc}]pair_lj.md){.reference .internal} when using the [`examples/melt/in.melt`{.docutils .literal .notranslate}]{.pre} input. We use it to show how to identify the origin of a segmentation fault.

:::: {.highlight-diff .notranslate}
::: highlight
    --- a/src/pair_lj_cut.cpp
    +++ b/src/pair_lj_cut.cpp
    @@ -81,6 +81,7 @@ void PairLJCut::compute(int eflag, int vflag)
       int nlocal = atom->nlocal;
       double *special_lj = force->special_lj;
       int newton_pair = force->newton_pair;
    +  double comx = 0.0;

       inum = list->inum;
       ilist = list->ilist;
    @@ -134,8 +135,10 @@ void PairLJCut::compute(int eflag, int vflag)
                                  evdwl,0.0,fpair,delx,dely,delz);
           }
         }
    -  }

    +    comx += atom->rmass[i]*x[i][0]; /* BUG */
    +  }
    +  printf("comx = %g\n",comx);
       if (vflag_fdotr) virial_fdotr_compute();
     }
:::
::::

After recompiling LAMMPS and running the input you should get something like this:

:::: {.highlight-console .notranslate}
::: highlight
    $ ./lmp -in in.melt
    LAMMPS (19 Mar 2020)
      using 1 OpenMP thread(s) per MPI task
    Lattice spacing in x,y,z = 1.6796 1.6796 1.6796
    Created orthogonal box = (0 0 0) to (16.796 16.796 16.796)
      1 by 1 by 1 MPI processor grid
    Created 4000 atoms
      create_atoms CPU = 0.000432253 secs
    Neighbor list info ...
      update every 20 steps, delay 0 steps, check no
      max neighbors/atom: 2000, page size: 100000
      master list distance cutoff = 2.8
      ghost atom cutoff = 2.8
      binsize = 1.4, bins = 12 12 12
      1 neighbor lists, perpetual/occasional/extra = 1 0 0
      (1) pair lj/cut, perpetual
          attributes: half, newton on
          pair build: half/bin/atomonly/newton
          stencil: half/bin/3d/newton
          bin: standard
    Setting up Verlet run ...
      Unit style    : lj
      Current step  : 0
      Time step     : 0.005
    Segmentation fault (core dumped)
:::
::::

::::::::::::: {#using-the-gdb-debugger-to-get-a-stack-trace .section}
## [5.4.1. ]{.section-number}Using the GDB debugger to get a stack trace[](#using-the-gdb-debugger-to-get-a-stack-trace "Link to this heading"){.headerlink}

There are two options to use the GDB debugger for identifying the origin of the segmentation fault or similar crash. The GDB debugger has many more features and options, as can be seen for example its [online documentation](https://www.sourceware.org/gdb/documentation/){.reference .external}.

::::::::: {#run-lammps-from-within-the-debugger .section}
### Run LAMMPS from within the debugger[](#run-lammps-from-within-the-debugger "Link to this heading"){.headerlink}

Running LAMMPS under the control of the debugger as shown below only works for a single MPI rank (for debugging a program running in parallel you usually need a parallel debugger program). A simple way to launch GDB is to prefix the LAMMPS command-line with [`gdb`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--args`{.docutils .literal .notranslate}]{.pre} and then type the command "run" at the GDB prompt. This will launch the debugger, load the LAMMPS executable and its debug info, and then run it. When it reaches the code causing the segmentation fault, it will stop with a message why it stopped, print the current line of code, and drop back to the GDB prompt.

:::: {.highlight-console .notranslate}
::: highlight
    (gdb) run
    [...]
    Setting up Verlet run ...
      Unit style    : lj
      Current step  : 0
      Time step     : 0.005

    Program received signal SIGSEGV, Segmentation fault.
    0x00000000006653ab in LAMMPS_NS::PairLJCut::compute (this=0x829740, eflag=1, vflag=<optimized out>) at /home/akohlmey/compile/lammps/src/pair_lj_cut.cpp:139
    139      comx += atom->rmass[i]*x[i][0]; /* BUG */
    (gdb)
:::
::::

Now typing the command "where" will show the stack of functions starting from the current function back to "main()".

:::: {.highlight-console .notranslate}
::: highlight
    (gdb) where
    #0  0x00000000006653ab in LAMMPS_NS::PairLJCut::compute (this=0x829740, eflag=1, vflag=<optimized out>) at /home/akohlmey/compile/lammps/src/pair_lj_cut.cpp:139
    #1  0x00000000004cf0a2 in LAMMPS_NS::Verlet::setup (this=0x7e6c90, flag=1) at /home/akohlmey/compile/lammps/src/verlet.cpp:131
    #2  0x000000000049db42 in LAMMPS_NS::Run::command (this=this@entry=0x7fffffffcca0, narg=narg@entry=1, arg=arg@entry=0x7e8750)
        at /home/akohlmey/compile/lammps/src/run.cpp:177
    #3  0x000000000041258a in LAMMPS_NS::Input::command_creator<LAMMPS_NS::Run> (lmp=<optimized out>, narg=1, arg=0x7e8750)
        at /home/akohlmey/compile/lammps/src/input.cpp:878
    #4  0x0000000000410ad3 in LAMMPS_NS::Input::execute_command (this=0x7d1410) at /home/akohlmey/compile/lammps/src/input.cpp:864
    #5  0x00000000004111fb in LAMMPS_NS::Input::file (this=0x7d1410) at /home/akohlmey/compile/lammps/src/input.cpp:229
    #6  0x000000000040933a in main (argc=<optimized out>, argv=<optimized out>) at /home/akohlmey/compile/lammps/src/main.cpp:65
    (gdb)
:::
::::

You can also print the value of variables and see if there is anything unexpected. Segmentation faults, for example, commonly happen when a pointer variable is not assigned and still initialized to NULL.

:::: {.highlight-console .notranslate}
::: highlight
    (gdb) print x
    $1 = (double **) 0x7ffff7ca1010
    (gdb) print i
    $2 = 0
    (gdb) print x[0]
    $3 = (double *) 0x7ffff6d80010
    (gdb) print x[0][0]
    $4 = 0
    (gdb) print x[1][0]
    $5 = 0.83979809569125363
    (gdb) print atom->rmass
    $6 = (double *) 0x0
    (gdb)
:::
::::
:::::::::

::::: {#inspect-a-core-dump-file-with-the-debugger .section}
### Inspect a core dump file with the debugger[](#inspect-a-core-dump-file-with-the-debugger "Link to this heading"){.headerlink}

When an executable crashes with a "core dumped" message, it creates a file "core" or "core.\<PID#\>" which contains the information about the current state. This file may be located in the folder where you ran LAMMPS or in some hidden folder managed by the systemd daemon. In the latter case, you need to "extract" the core file with the [`coredumpctl`{.docutils .literal .notranslate}]{.pre} utility to the current folder. Example: [`coredumpctl`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-o`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`core`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`dump`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`lmp`{.docutils .literal .notranslate}]{.pre}. Now you can launch the debugger to load the executable, its debug info and the core dump and drop you to a prompt like before.

:::: {.highlight-console .notranslate}
::: highlight
    $ gdb lmp core
    Reading symbols from lmp...
    [New LWP 1928535]
    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib64/libthread_db.so.1".
    Core was generated by `./lmp -in in.melt'.
    Program terminated with signal SIGSEGV, Segmentation fault.
    #0  0x00000000006653ab in LAMMPS_NS::PairLJCut::compute (this=0x1b10740, eflag=1, vflag=<optimized out>)
        at /home/akohlmey/compile/lammps/src/pair_lj_cut.cpp:139
    139      comx += atom->rmass[i]*x[i][0]; /* BUG */
    (gdb)
:::
::::

From here on, you use the same commands as shown before to get a stack trace and print current values of (pointer) variables.
:::::
:::::::::::::

::::: {#using-valgrind-to-get-a-stack-trace .section}
## [5.4.2. ]{.section-number}Using valgrind to get a stack trace[](#using-valgrind-to-get-a-stack-trace "Link to this heading"){.headerlink}

The [valgrind](https://valgrind.org){.reference .external} suite of tools allows to closely inspect the behavior of a compiled program by essentially emulating a CPU and instrumenting the program while running. This slows down execution quite significantly, but can also report issues that are not resulting in a crash. The default valgrind tool is a memory checker and you can use it by prefixing the normal command-line with [`valgrind`{.docutils .literal .notranslate}]{.pre}. Unlike GDB, this will also work for parallel execution, but it is recommended to redirect the valgrind output to a file (e.g. with [`--log-file=crash-%p.txt`{.docutils .literal .notranslate}]{.pre}, the %p will be substituted with the process ID) so that the messages of the multiple valgrind instances to the console are not mixed.

:::: {.highlight-console .notranslate}
::: highlight
    $ valgrind ./lmp -in in.melt
    ==1933642== Memcheck, a memory error detector
    ==1933642== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
    ==1933642== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
    ==1933642== Command: ./lmp -in in.melt
    ==1933642==
    LAMMPS (19 Mar 2020)
    OMP_NUM_THREADS environment is not set. Defaulting to 1 thread. (src/comm.cpp:94)
      using 1 OpenMP thread(s) per MPI task
    Lattice spacing in x,y,z = 1.6796 1.6796 1.6796
    Created orthogonal box = (0 0 0) to (16.796 16.796 16.796)
      1 by 1 by 1 MPI processor grid
    Created 4000 atoms
      create_atoms CPU = 0.032964 secs
    Neighbor list info ...
      update every 20 steps, delay 0 steps, check no
      max neighbors/atom: 2000, page size: 100000
      master list distance cutoff = 2.8
      ghost atom cutoff = 2.8
      binsize = 1.4, bins = 12 12 12
      1 neighbor lists, perpetual/occasional/extra = 1 0 0
      (1) pair lj/cut, perpetual
          attributes: half, newton on
          pair build: half/bin/atomonly/newton
          stencil: half/bin/3d/newton
          bin: standard
    Setting up Verlet run ...
      Unit style    : lj
      Current step  : 0
      Time step     : 0.005
    ==1933642== Invalid read of size 8
    ==1933642==    at 0x6653AB: LAMMPS_NS::PairLJCut::compute(int, int) (pair_lj_cut.cpp:139)
    ==1933642==    by 0x4CF0A1: LAMMPS_NS::Verlet::setup(int) (verlet.cpp:131)
    ==1933642==    by 0x49DB41: LAMMPS_NS::Run::command(int, char**) (run.cpp:177)
    ==1933642==    by 0x412589: void LAMMPS_NS::Input::command_creator<LAMMPS_NS::Run>(LAMMPS_NS::LAMMPS*, int, char**) (input.cpp:881)
    ==1933642==    by 0x410AD2: LAMMPS_NS::Input::execute_command() (input.cpp:864)
    ==1933642==    by 0x4111FA: LAMMPS_NS::Input::file() (input.cpp:229)
    ==1933642==    by 0x409339: main (main.cpp:65)
    ==1933642==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
    ==1933642==
:::
::::

As you can see, the stack trace information is similar to that obtained from GDB. In addition you get a more specific hint about what cause the segmentation fault, i.e. that it is a NULL pointer dereference. To find out which pointer exactly was NULL, you need to use the debugger, though.
:::::
:::::::::::::::::::::

::: {#debugging-when-lammps-appears-to-be-stuck .section}
# [5.5. ]{.section-number}Debugging when LAMMPS appears to be stuck[](#debugging-when-lammps-appears-to-be-stuck "Link to this heading"){.headerlink}

Sometimes the LAMMPS calculation appears to be stuck, that is the LAMMPS process or processes are active, but there is no visible progress. This can have multiple reasons:

- The selected styles are slow and require a lot of CPU time and the system is large. When extrapolating the expected speed from smaller systems, one has to factor in that not all models scale linearly with system size, e.g. [[kspace styles like ewald or pppm]{.doc}]kspace_style.md){.reference .internal}. There is very little that can be done in this case.

- The output interval is not set or set to a large value with the [[thermo]{.doc}]thermo.md){.reference .internal} command. In the first case, there will be output only at the first and last step.

- The output is block-buffered and instead of line-buffered. The output will only be written to the screen after 4096 or 8192 characters of output have accumulated. This most often happens for files but also with MPI parallel executables for output to the screen, since the output to the screen is handled by the MPI library so that output from all processes can be shown. This can be suppressed by using the [`-nonblock`{.docutils .literal .notranslate}]{.pre} or [`-nb`{.docutils .literal .notranslate}]{.pre} command-line flag, which turns off buffering for screen and logfile output.

- An MPI parallel calculation has a bug where a collective MPI function is called (e.g. [`MPI_Barrier()`{.docutils .literal .notranslate}]{.pre}, [`MPI_Bcast()`{.docutils .literal .notranslate}]{.pre}, [`MPI_Allreduce()`{.docutils .literal .notranslate}]{.pre} and so on) before pending point-to-point communications are completed or when the collective function is only called from a subset of the MPI processes. This also applies to some internal LAMMPS functions like [`Error::all()`{.docutils .literal .notranslate}]{.pre} which uses [`MPI_Barrier()`{.docutils .literal .notranslate}]{.pre} and thus [`Error::one()`{.docutils .literal .notranslate}]{.pre} must be called, if the error condition does not happen on all MPI processes simultaneously.

- Some function in LAMMPS has a bug where a [`for`{.docutils .literal .notranslate}]{.pre} or [`while`{.docutils .literal .notranslate}]{.pre} loop does not trigger the exit condition and thus will loop forever. This can happen when the wrong variable is incremented or when one value in a comparison becomes [`NaN`{.docutils .literal .notranslate}]{.pre} due to an overflow.

In the latter two cases, further information and stack traces (see above) can be obtain by attaching a debugger to a running process. For that the process ID (PID) is needed; this can be found on Linux machines with the [`top`{.docutils .literal .notranslate}]{.pre}, [`htop`{.docutils .literal .notranslate}]{.pre}, [`ps`{.docutils .literal .notranslate}]{.pre}, or [`pstree`{.docutils .literal .notranslate}]{.pre} commands.

Then running the (GNU) debugger [`gdb`{.docutils .literal .notranslate}]{.pre} with the [`-p`{.docutils .literal .notranslate}]{.pre} flag followed by the process id will attach the process to the debugger and stop execution of that specific process. From there on it is possible to issue all debugger commands in the same way as when LAMMPS was started from the debugger (see above). Most importantly it is possible to obtain a stack trace with the [`where`{.docutils .literal .notranslate}]{.pre} command and thus determine where in the execution of a timestep this process is. Also internal data can be printed and execution single stepped or continued. When the debugger is exited, the calculation will resume normally.
:::
:::::::::::::::::::::::
::::::::::::::::::::::::

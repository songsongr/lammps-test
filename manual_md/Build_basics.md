:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#basic-build-options .section}
# [3.5. ]{.section-number}Basic build options[](#basic-build-options "Link to this heading"){.headerlink}

The following topics are covered on this page, for building with both CMake and make:

- [[Serial vs parallel build]{.std .std-ref}](#serial){.reference .internal}

- [[Choice of compiler and compile/link options]{.std .std-ref}](#compile){.reference .internal}

- [[Build the LAMMPS executable and library]{.std .std-ref}](#exe){.reference .internal}

- [[Including and removing debug support]{.std .std-ref}](#debug){.reference .internal}

- [[Install LAMMPS after a build]{.std .std-ref}](#install){.reference .internal}

------------------------------------------------------------------------

:::::::::::::::: {#serial-vs-parallel-build .section}
[]{#serial}

## [3.5.1. ]{.section-number}Serial vs parallel build[](#serial-vs-parallel-build "Link to this heading"){.headerlink}

LAMMPS is written to use the ubiquitous [MPI (Message Passing Interface)](https://en.wikipedia.org/wiki/Message_Passing_Interface){.reference .external} library API for distributed memory parallel computation. You need to have such a library installed for building and running LAMMPS in parallel using a domain decomposition parallelization. It is compatible with the MPI standard version 2.x and later. LAMMPS can also be built into a "serial" executable for use with a single processor using the bundled MPI STUBS library.

Independent of the distributed memory MPI parallelization, parts of LAMMPS are also written with support for shared memory parallelization using the [OpenMP](https://en.wikipedia.org/wiki/OpenMP){.reference .external} threading standard. A more detailed discussion of that is below.

::::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-0-0-0 .sphinx-tabs-panel aria-labelledby="tab-0-0-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D BUILD_MPI=value        # yes or no, default is yes if CMake finds MPI
    -D BUILD_OMP=value        # yes or no, default is yes if a compatible
                              # compiler is detected
    -D LAMMPS_MACHINE=name    # name = mpi, serial, mybox, titan, laptop, etc
                              # no default value
:::
::::

The executable created by CMake (after running make) is named [`lmp`{.docutils .literal .notranslate}]{.pre} unless the [`LAMMPS_MACHINE`{.docutils .literal .notranslate}]{.pre} option is set. When setting [`LAMMPS_MACHINE=name`{.docutils .literal .notranslate}]{.pre}, the executable will be called [`lmp_name`{.docutils .literal .notranslate}]{.pre}. Using [`BUILD_MPI=no`{.docutils .literal .notranslate}]{.pre} will enforce building a serial executable using the MPI STUBS library.
:::::

:::::::: {#panel-0-0-1 .sphinx-tabs-panel aria-labelledby="tab-0-0-1" hidden="true" role="tabpanel" tabindex="0"}
The build with traditional makefiles has to be done inside the source folder [`src`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-bash .notranslate}
::: highlight
    make mpi      # parallel build, produces lmp_mpi using Makefile.mpi
    make serial   # serial build, produces lmp_serial using Makefile/serial
    make mybox    # uses Makefile.mybox to produce lmp_mybox
:::
::::

Any [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`machine`{.docutils .literal .notranslate}]{.pre} command will look up the make settings from a file [`Makefile.machine`{.docutils .literal .notranslate}]{.pre} in the folder [`src/MAKE`{.docutils .literal .notranslate}]{.pre} or one of its subdirectories [`MINE`{.docutils .literal .notranslate}]{.pre}, [`MACHINES`{.docutils .literal .notranslate}]{.pre}, or [`OPTIONS`{.docutils .literal .notranslate}]{.pre}, create a folder [`Obj_machine`{.docutils .literal .notranslate}]{.pre} with all objects and generated files and an executable called [`lmp_machine`{.docutils .literal .notranslate}]{.pre}. The standard parallel build with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`mpi`{.docutils .literal .notranslate}]{.pre} assumes a standard MPI installation with MPI compiler wrappers where all necessary compiler and linker flags to get access and link with the suitable MPI headers and libraries are set by the wrapper programs. For other cases or the serial build, you have to adjust the make file variables [`MPI_INC`{.docutils .literal .notranslate}]{.pre}, [`MPI_PATH`{.docutils .literal .notranslate}]{.pre}, [`MPI_LIB`{.docutils .literal .notranslate}]{.pre} as well as [`CC`{.docutils .literal .notranslate}]{.pre} and [`LINK`{.docutils .literal .notranslate}]{.pre}. To enable OpenMP threading usually a compiler specific flag needs to be added to the compile and link commands. For the GNU compilers, this is [`-fopenmp`{.docutils .literal .notranslate}]{.pre}, which can be added to the [`CC`{.docutils .literal .notranslate}]{.pre} and [`LINK`{.docutils .literal .notranslate}]{.pre} makefile variables.

For the serial build the following make variables are set (see [`src/MAKE/Makefile.serial`{.docutils .literal .notranslate}]{.pre}):

:::: {.highlight-make .notranslate}
::: highlight
    CC =       g++
    LINK =     g++
    MPI_INC =  -I../STUBS
    MPI_PATH = -L../STUBS
    MPI_LIB =  -lmpi_stubs
:::
::::

You also need to build the STUBS library for your platform before making LAMMPS itself. A [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`serial`{.docutils .literal .notranslate}]{.pre} build does this for you automatically, otherwise, type [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`mpi-stubs`{.docutils .literal .notranslate}]{.pre} from the src directory, or [`make`{.docutils .literal .notranslate}]{.pre} from the [`src/STUBS`{.docutils .literal .notranslate}]{.pre} dir. If the build fails, you may need to edit the [`STUBS/Makefile`{.docutils .literal .notranslate}]{.pre} for your platform. The stubs library does not provide MPI/IO functions required by some LAMMPS packages, e.g. [`LATBOLTZ`{.docutils .literal .notranslate}]{.pre}, and thus is not compatible with those packages.

::: {.admonition .note}
Note

The file [`src/STUBS/mpi.cpp`{.docutils .literal .notranslate}]{.pre} provides a CPU timer function called [`MPI_Wtime()`{.docutils .literal .notranslate}]{.pre} that calls [`gettimeofday()`{.docutils .literal .notranslate}]{.pre}. If your operating system does not support [`gettimeofday()`{.docutils .literal .notranslate}]{.pre}, you will need to insert code to call another timer. Note that the ANSI-standard function [`clock()`{.docutils .literal .notranslate}]{.pre} rolls over after an hour or so, and is therefore insufficient for timing long LAMMPS simulations.
:::
::::::::
:::::::::::::

::: {#mpi-and-openmp-support-in-lammps .section}
### MPI and OpenMP support in LAMMPS[](#mpi-and-openmp-support-in-lammps "Link to this heading"){.headerlink}

If you are installing MPI yourself to build a parallel LAMMPS executable, we recommend either MPICH or OpenMPI, which are regularly used and tested with LAMMPS by the LAMMPS developers. MPICH can be downloaded from the [MPICH home page](https://www.mpich.org){.reference .external}, and OpenMPI can be downloaded correspondingly from the [OpenMPI home page](https://www.open-mpi.org){.reference .external}. Other MPI packages should also work. No specific vendor provided and standard compliant MPI library is currently known to be incompatible with LAMMPS. If you are running on a large parallel machine, your system admins or the vendor should have already installed a version of MPI, which is likely to be faster than a self-installed MPICH or OpenMPI, so you should study the provided documentation to find out how to build and link with it.

The majority of OpenMP (threading) support in LAMMPS is provided by the [`OPENMP`{.docutils .literal .notranslate}]{.pre} package; see the [[OPENMP package]{.doc}]Speed_omp.md){.reference .internal} page for details. The [`INTEL`{.docutils .literal .notranslate}]{.pre} package also includes OpenMP threading (it is compatible with [`OPENMP`{.docutils .literal .notranslate}]{.pre} and will usually fall back on styles from that package, if a [`INTEL`{.docutils .literal .notranslate}]{.pre} does not exist) and adds vectorization support when compiled with compatible compilers, in particular the Intel compilers on top of OpenMP. Also, the [`KOKKOS`{.docutils .literal .notranslate}]{.pre} package can be compiled to include OpenMP threading.

In addition, there are a few commands in LAMMPS that have native OpenMP support included as well. These are commands in the [`ML-SNAP`{.docutils .literal .notranslate}]{.pre}, [`DIFFRACTION`{.docutils .literal .notranslate}]{.pre}, and [`DPD-REACT`{.docutils .literal .notranslate}]{.pre} packages. Furthermore, some packages support OpenMP threading indirectly through the libraries they interface to: e.g. [`KSPACE`{.docutils .literal .notranslate}]{.pre}, and [`COLVARS`{.docutils .literal .notranslate}]{.pre}. See the [[Packages details]{.doc}]Packages_details.md){.reference .internal} page for more info on these packages, and the pages for their respective commands for OpenMP threading info.

For CMake, if you use [`BUILD_OMP=yes`{.docutils .literal .notranslate}]{.pre}, you can use these packages and turn on their native OpenMP support at run time by setting the [`OMP_NUM_THREADS`{.docutils .literal .notranslate}]{.pre} environment variable before you launch LAMMPS.

When building LAMMPS with conventional make, the [`CCFLAGS`{.docutils .literal .notranslate}]{.pre} and [`LINKFLAGS`{.docutils .literal .notranslate}]{.pre} variables in Makefile.machine need to include the compiler flag that enables OpenMP. For the GNU compilers or Clang, it is [`-fopenmp`{.docutils .literal .notranslate}]{.pre}. For (recent) Intel compilers, it is [`-qopenmp`{.docutils .literal .notranslate}]{.pre}. If you are using a different compiler, please refer to its documentation.
:::

::: {#openmp-compiler-compatibility .section}
[]{#default-none-issues}

### OpenMP Compiler compatibility[](#openmp-compiler-compatibility "Link to this heading"){.headerlink}

Some compilers do not fully support the [`default(none)`{.docutils .literal .notranslate}]{.pre} directive and others (e.g. GCC version 9 and beyond, Clang version 10 and later) may implement strict OpenMP 4.0 and later semantics, which are incompatible with the OpenMP 3.1 semantics used in LAMMPS for maximal compatibility with compiler versions in use. If compilation with OpenMP enabled fails because of your compiler requiring strict OpenMP 4.0 semantics, you can change the behavior by adding [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`LAMMPS_OMP_COMPAT=4`{.docutils .literal .notranslate}]{.pre} to the [`LMP_INC`{.docutils .literal .notranslate}]{.pre} variable in your makefile, or add it to the command-line flags while configuring with CMake. LAMMPS will auto-detect a suitable setting for most GNU, Clang, and Intel compilers.

------------------------------------------------------------------------
:::
::::::::::::::::

::::::::::::::::::: {#choice-of-compiler-and-compile-link-options .section}
[]{#compile}

## [3.5.2. ]{.section-number}Choice of compiler and compile/link options[](#choice-of-compiler-and-compile-link-options "Link to this heading"){.headerlink}

The choice of compiler and compiler flags can be important for maximum performance. Vendor provided compilers for a specific hardware can produce faster code than open-source compilers like the GNU compilers. On the most common x86 hardware, the most popular C++ compilers are quite similar in their ability to optimize regular C/C++ source code at high optimization levels. When using the [`INTEL`{.docutils .literal .notranslate}]{.pre} package, there is a distinct advantage in using the [Intel C++ compiler](https://software.intel.com/en-us/intel-compilers){.reference .external} due to much improved vectorization through SSE and AVX instructions on compatible hardware. The source code in that package conditionally includes compiler specific directives to enable these high degrees of vectorization. This may change over time as equivalent vectorization directives are included into the OpenMP standard and other compilers adopt them.

On parallel clusters or supercomputers which use "environment modules" for their compile/link environments, you can often access different compilers by simply loading the appropriate module before building LAMMPS.

:::::::::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Makefile.machine settings for traditional make
:::

:::::::: {#panel-1-1-0 .sphinx-tabs-panel aria-labelledby="tab-1-1-0" role="tabpanel" tabindex="0"}
By default CMake will use the compiler it finds according to its internal preferences, and it will add optimization flags appropriate to that compiler and any [[accelerator packages]{.doc}]Speed_packages.md){.reference .internal} you have included in the build. CMake will check if the detected or selected compiler is compatible with the C++ support requirements of LAMMPS and stop with an error, if this is not the case. A C++17 compatible compiler is required.

You can tell CMake to look for a specific compiler with setting CMake variables (listed below) during configuration. For a few common choices, there are also presets in the [`cmake/presets`{.docutils .literal .notranslate}]{.pre} folder. You may also specify the corresponding [`CMAKE_*_FLAGS`{.docutils .literal .notranslate}]{.pre} variables individually, if you want to experiment with alternate optimization flags. You should specify all 3 compilers, so that the (few) LAMMPS source files written in C or Fortran are built with a compiler consistent with the one used for the C++ files:

:::: {.highlight-bash .notranslate}
::: highlight
    -D CMAKE_CXX_COMPILER=name            # name of C++ compiler
    -D CMAKE_C_COMPILER=name              # name of C compiler
    -D CMAKE_Fortran_COMPILER=name        # name of Fortran compiler

    -D CMAKE_CXX_STANDARD=17              # put compiler in C++17 mode
    -D CMAKE_CXX_FLAGS=string             # flags to use with C++ compiler
    -D CMAKE_C_FLAGS=string               # flags to use with C compiler
    -D CMAKE_Fortran_FLAGS=string         # flags to use with Fortran compiler
:::
::::

A few example command lines are:

:::: {.highlight-bash .notranslate}
::: highlight
    # Building with GNU Compilers:
    cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ \
          -DCMAKE_Fortran_COMPILER=gfortran ../cmake
    # Building with Intel Classic Compilers:
    cmake -DCMAKE_C_COMPILER=icc -DCMAKE_CXX_COMPILER=icpc \
          -DCMAKE_Fortran_COMPILER=ifort ../cmake
    # Building with Intel oneAPI Compilers:
    cmake -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx \
          -DCMAKE_Fortran_COMPILER=ifx ../cmake
    # Building with LLVM/Clang Compilers:
    cmake -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ \
          -DCMAKE_Fortran_COMPILER=flang ../cmake
    # Building with PGI/Nvidia Compilers:
    cmake -DCMAKE_C_COMPILER=pgcc -DCMAKE_CXX_COMPILER=pgc++ \
          -DCMAKE_Fortran_COMPILER=pgfortran ../cmake
    # Building with the NVHPC Compilers:
    cmake -DCMAKE_C_COMPILER=nvc -DCMAKE_CXX_COMPILER=nvc++ \
          -DCMAKE_Fortran_COMPILER=nvfortran ../cmake
:::
::::

For compiling with the Clang/LLVM compilers a CMake preset is provided that can be loaded with [`-C`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`../cmake/presets/clang.cmake`{.docutils .literal .notranslate}]{.pre}. Similarly, [`-C`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`../cmake/presets/intel.cmake`{.docutils .literal .notranslate}]{.pre} should switch the compiler toolchain to the legacy Intel compilers, [`-C`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`../cmake/presets/oneapi.cmake`{.docutils .literal .notranslate}]{.pre} will switch to the LLVM based oneAPI Intel compilers, [`-C`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`../cmake/presets/pgi.cmake`{.docutils .literal .notranslate}]{.pre} will switch the compiler to the PGI compilers, and [`-C`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`../cmake/presets/nvhpc.cmake`{.docutils .literal .notranslate}]{.pre} will switch to the NVHPC compilers.

::: {.admonition .note}
Note

When the cmake command completes, it prints a summary to the screen which compilers it is using and what flags and settings will be used for the compilation. Note that if the top-level compiler is [`mpicxx`{.docutils .literal .notranslate}]{.pre}, it is simply a wrapper on a real compiler. The underlying compiler info is what CMake will try to determine and report. You should check to confirm you are using the compiler and optimization flags you want.
:::
::::::::

:::::::::: {#panel-1-1-1 .sphinx-tabs-panel aria-labelledby="tab-1-1-1" hidden="true" role="tabpanel" tabindex="0"}
The "compiler/linker settings" section of a Makefile.machine lists compiler and linker settings for your C++ compiler, including optimization flags. For a parallel build it is recommended to use [`mpicxx`{.docutils .literal .notranslate}]{.pre} or [`mpiCC`{.docutils .literal .notranslate}]{.pre}, since these compiler wrappers will include a variety of settings appropriate for your MPI installation and thus avoiding the guesswork of finding the right flags.

Parallel build (see [`src/MAKE/Makefile.mpi`{.docutils .literal .notranslate}]{.pre}):

:::: {.highlight-make .notranslate}
::: highlight
    CC =        mpicxx
    CCFLAGS =   -g -O3
    LINK =      mpicxx
    LINKFLAGS = -g -O
:::
::::

Serial build with GNU gcc (see [`src/MAKE/Makefile.serial`{.docutils .literal .notranslate}]{.pre}):

:::: {.highlight-make .notranslate}
::: highlight
    CC =        g++
    CCFLAGS =   -g -O3
    LINK =      g++
    LINKFLAGS = -g -O
:::
::::

::::: {.admonition .note}
Note

If compilation stops with a message like the following:

:::: {.highlight-output .notranslate}
::: highlight
    g++ -g -O3  -DLAMMPS_GZIP -DLAMMPS_MEMALIGN=64    -I../STUBS     -c ../main.cpp
    In file included from ../pointers.h:24:0,
               from ../input.h:17,
               from ../main.cpp:16:
    ../lmptype.h:34:2: error: #error LAMMPS requires a C++17 (or later) compliant compiler. Enable C++17 compatibility or upgrade the compiler.
:::
::::

then you have either an unsupported (old) compiler or you have to turn on C++17 mode. For those compilers, you need to add the [`-std=c++17`{.docutils .literal .notranslate}]{.pre} flag. If there is no compiler that supports this flag (or equivalent), you would have to install a newer compiler that supports C++17; either as a binary package or through compiling from source.
:::::

If you build LAMMPS with any [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} included, there may be specific compiler or linker flags that are either required or recommended to enable required features and to achieve optimal performance. You need to include these in the [`CCFLAGS`{.docutils .literal .notranslate}]{.pre} and [`LINKFLAGS`{.docutils .literal .notranslate}]{.pre} settings above. For details, see the documentation for the individual packages listed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. Or examine these files in the [`src/MAKE/OPTIONS`{.docutils .literal .notranslate}]{.pre} directory. They correspond to each of the 5 accelerator packages and their hardware variants:

> ::::: {}
> :::: {.highlight-bash .notranslate}
> ::: highlight
>     Makefile.opt                   # OPT package
>     Makefile.omp                   # OPENMP package
>     Makefile.intel_cpu             # INTEL package for CPUs
>     Makefile.intel_coprocessor     # INTEL package for KNLs
>     Makefile.gpu                   # GPU package
> :::
> ::::
> :::::
::::::::::
::::::::::::::::::

------------------------------------------------------------------------
:::::::::::::::::::

:::::::::::::::: {#build-the-lammps-executable-and-library .section}
[]{#library}[]{#exe}

## [3.5.3. ]{.section-number}Build the LAMMPS executable and library[](#build-the-lammps-executable-and-library "Link to this heading"){.headerlink}

LAMMPS is always built as a library of C++ classes plus an executable. The executable is a simple [`main()`{.docutils .literal .notranslate}]{.pre} function that sets up MPI and then creates a LAMMPS class instance from the LAMMPS library, which will then process commands provided via a file or from the console input. The LAMMPS library can also be called from another application or a scripting language. See the [[Howto couple]{.doc}]Howto_couple.md){.reference .internal} doc page for more info on coupling LAMMPS to other codes. See the [[Python]{.doc}]Python_head.md){.reference .internal} page for more info on wrapping and running LAMMPS from Python via its library interface.

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-2-2-0 .sphinx-tabs-panel aria-labelledby="tab-2-2-0" role="tabpanel" tabindex="0"}
For CMake builds, you can select through setting CMake variables between building a shared or a static LAMMPS library and what kind of suffix is added to them (in case you want to concurrently install multiple variants of binaries with different settings). If none are set, defaults are applied.

:::: {.highlight-bash .notranslate}
::: highlight
    -D BUILD_SHARED_LIBS=value   # yes or no (default)
    -D LAMMPS_MACHINE=name       # name = mpi, serial, mybox, titan, laptop, etc
                                 # no default value
:::
::::

The compilation will always produce a LAMMPS library and an executable linked to it. By default, this will be a static library named [`liblammps.a`{.docutils .literal .notranslate}]{.pre} and an executable named [`lmp`{.docutils .literal .notranslate}]{.pre} Setting [`BUILD_SHARED_LIBS=yes`{.docutils .literal .notranslate}]{.pre} will instead produce a shared library called [`liblammps.so`{.docutils .literal .notranslate}]{.pre} (or [`liblammps.dylib`{.docutils .literal .notranslate}]{.pre} or [`liblammps.dll`{.docutils .literal .notranslate}]{.pre} depending on the platform) If [`LAMMPS_MACHINE=name`{.docutils .literal .notranslate}]{.pre} is set in addition, the name of the generated libraries will be changed to either [`liblammps_name.a`{.docutils .literal .notranslate}]{.pre} or [`liblammps_name.so`{.docutils .literal .notranslate}]{.pre}, respectively and the executable will be called [`lmp_name`{.docutils .literal .notranslate}]{.pre}.
:::::

::::: {#panel-2-2-1 .sphinx-tabs-panel aria-labelledby="tab-2-2-1" hidden="true" role="tabpanel" tabindex="0"}
With the traditional makefile based build process, the choice of the generated executable or library depends on the "mode" setting. Several options are available and [`mode=static`{.docutils .literal .notranslate}]{.pre} is the default.

:::: {.highlight-bash .notranslate}
::: highlight
    make machine               # build LAMMPS executable lmp_machine
    make mode=static machine   # same as "make machine"
    make mode=shared machine   # build LAMMPS shared lib liblammps_machine.so
                               # instead
:::
::::

The "static" build will generate a static library called [`liblammps_machine.a`{.docutils .literal .notranslate}]{.pre} and an executable named [`lmp_machine`{.docutils .literal .notranslate}]{.pre}, while the "shared" build will generate a shared library [`liblammps_machine.so`{.docutils .literal .notranslate}]{.pre} instead and [`lmp_machine`{.docutils .literal .notranslate}]{.pre} will be linked to it. The build step will also create generic soft links, named [`liblammps.a`{.docutils .literal .notranslate}]{.pre} and [`liblammps.so`{.docutils .literal .notranslate}]{.pre}, which point to the specific [`liblammps_machine.a/so`{.docutils .literal .notranslate}]{.pre} files.
:::::
::::::::::

::::::: {#additional-information .section}
### Additional information[](#additional-information "Link to this heading"){.headerlink}

Note that for creating a shared library, all the libraries it depends on must be compiled to be compatible with shared libraries. This should be the case for libraries included with LAMMPS, such as the dummy MPI library in [`src/STUBS`{.docutils .literal .notranslate}]{.pre} or any package libraries in the [`lib`{.docutils .literal .notranslate}]{.pre} directory, since they are always built in a shared library compatible way using the [`-fPIC`{.docutils .literal .notranslate}]{.pre} compiler switch. However, if an auxiliary library (like MPI or FFTW) does not exist as a compatible format, the shared library linking step may generate an error. This means you will need to install a compatible version of the auxiliary library. The build instructions for that library should tell you how to do this.

As an example, here is how to build and install the [MPICH library](https://www.mpich.org){.reference .external}, a popular open-source version of MPI, as a shared library in the default /usr/local/lib location:

:::: {.highlight-bash .notranslate}
::: highlight
    ./configure --enable-shared
    make
    make install
:::
::::

You may need to use [`sudo`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre} in place of the last line if you do not have write privileges for [`/usr/local/lib`{.docutils .literal .notranslate}]{.pre} or use the [`--prefix`{.docutils .literal .notranslate}]{.pre} configuration option to select an installation folder, where you do have write access. The end result should be the file [`/usr/local/lib/libmpich.so`{.docutils .literal .notranslate}]{.pre}. On many Linux installations, the folder [`${HOME}/.local`{.docutils .literal .notranslate}]{.pre} is an alternative to using [`/usr/local`{.docutils .literal .notranslate}]{.pre} and does not require superuser or sudo access. In that case the configuration step becomes:

:::: {.highlight-bash .notranslate}
::: highlight
    ./configure --enable-shared --prefix=${HOME}/.local
:::
::::

Avoiding the use of "sudo" for custom software installation (i.e. from source and not through a package manager tool provided by the OS) is generally recommended to ensure the integrity of the system software installation.

------------------------------------------------------------------------
:::::::
::::::::::::::::

::: {#including-or-removing-debug-support .section}
[]{#debug}

## [3.5.4. ]{.section-number}Including or removing debug support[](#including-or-removing-debug-support "Link to this heading"){.headerlink}

By default the compilation settings will include the [`-g`{.docutils .literal .notranslate}]{.pre} flag which instructs the compiler to include debug information (e.g. which line of source code a particular instruction correspond to). This can be extremely useful in case LAMMPS crashes and can help to provide crucial information in [[tracking down the origin of a crash]{.doc}]Errors_debug.md){.reference .internal} and help the LAMMPS developers fix bugs in the source code. However, this increases the storage requirements for object files, libraries, and the executable 3-5 fold.

If this is a concern, you can change the compilation settings or remove the debug information from the LAMMPS executable:

- **Traditional make**: edit your [`Makefile.<machine>`{.docutils .literal .notranslate}]{.pre} to remove the [`-g`{.docutils .literal .notranslate}]{.pre} flag from the [`CCFLAGS`{.docutils .literal .notranslate}]{.pre} and [`LINKFLAGS`{.docutils .literal .notranslate}]{.pre} definitions

- **CMake**: use [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_BUILD_TYPE=Release`{.docutils .literal .notranslate}]{.pre} or explicitly reset the applicable compiler flags (best done using the text mode or graphical user interface).

- **Remove debug info**: If you are only concerned about the executable being too large, you can use the [`strip`{.docutils .literal .notranslate}]{.pre} tool (e.g. [`strip`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`lmp_serial`{.docutils .literal .notranslate}]{.pre}) to remove the debug information from the executable file. Do not strip libraries or object files, as that will render them unusable.

------------------------------------------------------------------------
:::

:::::::::::: {#build-lammps-tools .section}
[]{#tools}

## [3.5.5. ]{.section-number}Build LAMMPS tools[](#build-lammps-tools "Link to this heading"){.headerlink}

Some tools described in [[Auxiliary tools]{.doc}]Tools.md){.reference .internal} can be built directly using CMake or Make.

::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-3-3-0 .sphinx-tabs-panel aria-labelledby="tab-3-3-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D BUILD_TOOLS=value         # yes or no (default). Build binary2txt,
                                 # chain.x, micelle2d.x, msi2lmp, phana,
                                 # stl_bin2txt
    -D BUILD_LAMMPS_GUI=value    # yes or no (default). Build LAMMPS-GUI
    -D BUILD_WHAM=value          # yes (default). Download and build WHAM;
                                 # only available for BUILD_LAMMPS_GUI=yes
:::
::::

The generated binaries will also become part of the LAMMPS installation (see below).
:::::

:::::: {#panel-3-3-1 .sphinx-tabs-panel aria-labelledby="tab-3-3-1" hidden="true" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    cd lammps/tools
    make all              # build all binaries of tools
    make binary2txt       # build only binary2txt tool
    make chain            # build only chain tool
    make micelle2d        # build only micelle2d tool
:::
::::

::: {.admonition .note}
Note

Building LAMMPS-GUI *requires* building LAMMPS with CMake.
:::
::::::
:::::::::::

------------------------------------------------------------------------
::::::::::::

::::::::: {#install-lammps-after-a-build .section}
[]{#install}

## [3.5.6. ]{.section-number}Install LAMMPS after a build[](#install-lammps-after-a-build "Link to this heading"){.headerlink}

After building LAMMPS, you may wish to copy the LAMMPS executable or library, along with other LAMMPS files (library header, doc files), to a globally visible place on your system, for others to access. Note that you may need super-user privileges (e.g. sudo) if the directory you want to copy files to is protected.

:::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-4-4-0 .sphinx-tabs-panel aria-labelledby="tab-4-4-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    cmake -D CMAKE_INSTALL_PREFIX=path [options ...] ../cmake
    make                        # perform make after CMake command
    make install                # perform the installation into prefix
:::
::::

During the installation process CMake will by default remove any runtime path settings for loading shared libraries. Because of this you may have to set or modify the [`LD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre} (or [`DYLD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre}) environment variable, if you are installing LAMMPS into a non-system location and/or are linking to libraries in a non-system location that depend on such runtime path settings. As an alternative, you may set the CMake variable [`LAMMPS_INSTALL_RPATH`{.docutils .literal .notranslate}]{.pre} to [`on`{.docutils .literal .notranslate}]{.pre} and then the runtime paths for any linked shared libraries and the library installation folder for the LAMMPS library will be embedded and thus the requirement to set environment variables is avoided. The [`off`{.docutils .literal .notranslate}]{.pre} setting is usually preferred for packaged binaries or when setting up environment modules, the [`on`{.docutils .literal .notranslate}]{.pre} setting is more convenient for installing software into a non-system or personal folder.
:::::

::: {#panel-4-4-1 .sphinx-tabs-panel aria-labelledby="tab-4-4-1" hidden="true" role="tabpanel" tabindex="0"}
There is no "install" option in the [`src/Makefile`{.docutils .literal .notranslate}]{.pre} for LAMMPS. If you wish to do this you will need to first build LAMMPS, then manually copy the desired LAMMPS files to the appropriate system directories.
:::
::::::::
:::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

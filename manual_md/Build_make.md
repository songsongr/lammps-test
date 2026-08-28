::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#build-lammps-with-make .section}
# [3.3. ]{.section-number}Build LAMMPS with make[](#build-lammps-with-make "Link to this heading"){.headerlink}

Building LAMMPS with traditional makefiles requires that you have a [`Makefile.<machine>`{.docutils .literal .notranslate}]{.pre} file appropriate for your system in either the [`src/MAKE`{.docutils .literal .notranslate}]{.pre}, [`src/MAKE/MACHINES`{.docutils .literal .notranslate}]{.pre}, [`src/MAKE/OPTIONS`{.docutils .literal .notranslate}]{.pre}, or [`src/MAKE/MINE`{.docutils .literal .notranslate}]{.pre} directory (see below). It can include various options for customizing your LAMMPS build with a number of global compilation options and features.

This build system is slowly being phased out and may not support all optional features and packages in LAMMPS. It is recommended to switch to the [[CMake based build system]{.doc}]Build_cmake.md){.reference .internal}.

::: {#requirements .section}
## [3.3.1. ]{.section-number}Requirements[](#requirements "Link to this heading"){.headerlink}

Those makefiles are written for and tested with GNU make and may not be compatible with other make programs. In most cases, if the "make" program is not GNU make, then there will be a GNU make program available under the name "gmake". If GNU make or a compatible make is not available, you may have to first install it or switch to building with [[CMake]{.doc}]Build_cmake.md){.reference .internal}. The makefiles of the traditional make based build process and the scripts they are calling expect a few additional tools to be available and functioning.

> ::: {}
> - A working C/C++ compiler toolchain supporting the C++17 standard; on Linux, these are often the GNU compilers. Some older compiler versions require adding flags like [`-std=c++17`{.docutils .literal .notranslate}]{.pre} to enable C++17 mode.
>
> - A Bourne shell compatible "Unix" shell program (frequently this is [`bash`{.docutils .literal .notranslate}]{.pre})
>
> - A few shell utilities: [`ls`{.docutils .literal .notranslate}]{.pre}, [`mv`{.docutils .literal .notranslate}]{.pre}, [`ln`{.docutils .literal .notranslate}]{.pre}, [`rm`{.docutils .literal .notranslate}]{.pre}, [`grep`{.docutils .literal .notranslate}]{.pre}, [`sed`{.docutils .literal .notranslate}]{.pre}, [`tr`{.docutils .literal .notranslate}]{.pre}, [`cat`{.docutils .literal .notranslate}]{.pre}, [`touch`{.docutils .literal .notranslate}]{.pre}, [`diff`{.docutils .literal .notranslate}]{.pre}, [`dirname`{.docutils .literal .notranslate}]{.pre}
>
> - Python (optional, required for [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`lib-<pkg>`{.docutils .literal .notranslate}]{.pre} in the [`src`{.docutils .literal .notranslate}]{.pre} folder). Python scripts are currently tested with 3.6 to 3.11. The procedure for [[building the documentation]{.doc}]Build_manual.md){.reference .internal} *requires* Python 3.8 or later.
> :::
:::

:::::: {#getting-started .section}
## [3.3.2. ]{.section-number}Getting started[](#getting-started "Link to this heading"){.headerlink}

To include LAMMPS packages (i.e. optional commands and styles) you must enable (or "install") them first, as discussed on the [[Build package]{.doc}]Build_package.md){.reference .internal} page. If a package requires (provided or external) libraries, you must configure and build those libraries **before** building LAMMPS itself and especially **before** enabling such a package with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`yes-<package>`{.docutils .literal .notranslate}]{.pre}. [[Building LAMMPS with CMake]{.doc}]Build_cmake.md){.reference .internal} can automate much of this for many types of machines, especially workstations, desktops, and laptops, so we suggest you try it first when building LAMMPS in those cases.

The commands below perform a default LAMMPS build, producing the LAMMPS executable [`lmp_serial`{.docutils .literal .notranslate}]{.pre} and [`lmp_mpi`{.docutils .literal .notranslate}]{.pre} in [`lammps/src`{.docutils .literal .notranslate}]{.pre}:

:::: {.highlight-bash .notranslate}
::: highlight
    cd lammps/src   # change to main LAMMPS source folder
    make serial     # build a serial LAMMPS executable using GNU g++
    make mpi        # build a parallel LAMMPS executable with MPI
    make            # see a variety of make options
:::
::::

Compilation can take a long time, since LAMMPS is a large project with many features. If your machine has multiple CPU cores (most do these days), you can speed this up by compiling sources in parallel with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-j`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`N`{.docutils .literal .notranslate}]{.pre} (with N being the maximum number of concurrently executed tasks). Installation of the [ccache](https://ccache.dev/){.reference .external} (= Compiler Cache) software may speed up repeated compilation even more, e.g. during code development, especially when repeatedly switching between branches.

After the initial build, whenever you edit LAMMPS source files, or add or remove new files to the source directory (e.g. by installing or uninstalling packages), you must re-compile and relink the LAMMPS executable with the same [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`<machine>`{.docutils .literal .notranslate}]{.pre} command. The makefile's dependency tracking should ensure that only the necessary subset of files is re-compiled. If you change settings in the makefile, you have to recompile *everything*. To delete all objects, you can use [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`clean-<machine>`{.docutils .literal .notranslate}]{.pre}.

::: {.admonition .note}
Note

Before the actual compilation starts, LAMMPS will perform several steps to collect information from the configuration and setup that is then embedded into the executable. When you build LAMMPS for the first time, it will also compile a tool to quickly determine a list of dependencies. Those are required for the make program to correctly detect, which files need to be recompiled or relinked after changes were made to the sources.
:::
::::::

::::::: {#customized-builds-and-alternate-makefiles .section}
## [3.3.3. ]{.section-number}Customized builds and alternate makefiles[](#customized-builds-and-alternate-makefiles "Link to this heading"){.headerlink}

The [`src/MAKE`{.docutils .literal .notranslate}]{.pre} directory tree contains the [`Makefile.<machine>`{.docutils .literal .notranslate}]{.pre} files included in the LAMMPS distribution. Typing [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`example`{.docutils .literal .notranslate}]{.pre} uses [`Makefile.example`{.docutils .literal .notranslate}]{.pre} from one of those folders, if available. The [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`serial`{.docutils .literal .notranslate}]{.pre} and [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`mpi`{.docutils .literal .notranslate}]{.pre} lines above, for example, use [`src/MAKE/Makefile.serial`{.docutils .literal .notranslate}]{.pre} and [`src/MAKE/Makefile.mpi`{.docutils .literal .notranslate}]{.pre}, respectively. Other makefiles are in these directories:

:::: {.highlight-bash .notranslate}
::: highlight
    OPTIONS      # Makefiles which enable specific options
    MACHINES     # Makefiles for specific machines
    MINE         # customized Makefiles you create (you may need to create this folder)
:::
::::

Simply typing [`make`{.docutils .literal .notranslate}]{.pre} lists all the available [`Makefile.<machine>`{.docutils .literal .notranslate}]{.pre} files with a single line description toward the end of the output. A file with the same name can appear in multiple folders (not a good idea). The order the directories are searched is as follows: [`src/MAKE/MINE`{.docutils .literal .notranslate}]{.pre}, [`src/MAKE`{.docutils .literal .notranslate}]{.pre}, [`src/MAKE/OPTIONS`{.docutils .literal .notranslate}]{.pre}, [`src/MAKE/MACHINES`{.docutils .literal .notranslate}]{.pre}. This gives preference to a customized file you put in [`src/MAKE/MINE`{.docutils .literal .notranslate}]{.pre}. If you create your own custom makefile under a new name, please edit the first line with the description and machine name, so you will not confuse yourself, when looking at the machine summary.

Makefiles you may wish to try out, include those listed below (some require a package first be installed). Many of these include specific compiler flags for optimized performance. Please note, however, that some of these customized machine Makefile are contributed by users, and thus may have modifications specific to the systems of those users. Since compilers, OS configurations, and LAMMPS itself keep changing, their settings may become outdated, too:

:::: {.highlight-bash .notranslate}
::: highlight
    make mac             # build serial LAMMPS on macOS
    make mac_mpi         # build parallel LAMMPS on macOS
    make intel_cpu       # build with the INTEL package optimized for CPUs
    make knl             # build with the INTEL package optimized for KNLs
    make opt             # build with the OPT package optimized for CPUs
    make omp             # build with the OPENMP package optimized for OpenMP
:::
::::
:::::::
:::::::::::::
::::::::::::::
:::::::::::::::

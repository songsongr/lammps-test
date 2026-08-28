::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::::::: {#using-cmake-with-lammps .section}
# [10.6.1. ]{.section-number}Using CMake with LAMMPS[](#using-cmake-with-lammps "Link to this heading"){.headerlink}

The support for building LAMMPS with CMake is a recent addition to LAMMPS thanks to the efforts of Christoph Junghans (LANL) and Richard Berger (LANL). One of the key strengths of CMake is that it is not tied to a specific platform or build system. Instead it generates the files necessary to build and develop for different build systems and on different platforms. Note, that this applies to the build system itself not the LAMMPS code. In other words, without additional porting effort, it is not possible - for example - to compile LAMMPS with Visual C++ on Windows. The build system output can also include support files necessary to program LAMMPS as a project in integrated development environments (IDE) like Eclipse, Visual Studio, QtCreator, Xcode, CodeBlocks, Kate and others.

A second important feature of CMake is that it can detect and validate available libraries, optimal settings, available support tools and so on, so that by default LAMMPS will take advantage of available tools without requiring to provide the details about how to enable/integrate them.

The downside of this approach is, that there is some complexity associated with running CMake itself and how to customize the building of LAMMPS. This tutorial will show how to manage this through some selected examples. Please see the chapter about [[building LAMMPS]{.doc}]Build.md){.reference .internal} for descriptions of specific flags and options for LAMMPS in general and for specific packages.

::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

CMake can be used through either the command-line interface (CLI) program [`cmake`{.docutils .literal .notranslate}]{.pre} (or [`cmake3`{.docutils .literal .notranslate}]{.pre}), a text mode interactive user interface (TUI) program [`ccmake`{.docutils .literal .notranslate}]{.pre} (or [`ccmake3`{.docutils .literal .notranslate}]{.pre}), or a graphical user interface (GUI) program [`cmake-gui`{.docutils .literal .notranslate}]{.pre}. All of them are portable software available on all supported platforms and can be used interchangeably. Since LAMMPS version 10Sep2025, the minimum required CMake version is 3.20.

All details about features and settings for CMake are in the [CMake online documentation](https://cmake.org/documentation/){.reference .external}. We focus below on the most important aspects with respect to compiling LAMMPS.

:::::: {#prerequisites .section}
## Prerequisites[](#prerequisites "Link to this heading"){.headerlink}

This tutorial assumes that you are operating in a command-line environment using a shell like Bash or Zsh.

- Linux: any Terminal window will work or text console

- macOS: launch the Terminal application

- Windows 10 or 11: install and run the [[Windows Subsystem for Linux]{.doc}]Howto_wsl.md){.reference .internal}

- other Unix-like operating systems like FreeBSD

::: {.admonition .note}
Note

It is also possible to use CMake on Windows 10 or 11 through either the Microsoft Visual Studio IDE with the bundled CMake or from the Windows command prompt using a separately installed CMake package, both using the native Microsoft Visual C++ compilers and (optionally) the Microsoft MPI SDK. This tutorial, however, only covers unix-like command-line interfaces.
:::

We also assume that you have downloaded and unpacked a recent LAMMPS source code package or used Git to create a clone of the LAMMPS sources on your compilation machine.

You should change into the top level directory of the LAMMPS source tree all paths mentioned in the tutorial are relative to that. Immediately after downloading it should look like this:

:::: {.highlight-console .notranslate}
::: highlight
    $ ls
    bench  doc       lib      potentials  README  tools
    cmake  examples  LICENSE  python      src
:::
::::
::::::

::: {#build-versus-source-directory .section}
## Build versus source directory[](#build-versus-source-directory "Link to this heading"){.headerlink}

When using CMake the build procedure is separated into multiple distinct phases:

> ::: {}
> 1.  **Configuration:** detect or define which features and settings should be enable and used and how LAMMPS should be compiled
>
> 2.  **Compilation:** generate and compile all necessary source files and build libraries and executables.
>
> 3.  **Installation:** copy selected files from the compilation into your file system, so they can be used without having to keep the source and build tree around.
> :::

The configuration and compilation of LAMMPS has to happen in a dedicated *build directory* which must be different from the source directory. Also the source directory ([`src`{.docutils .literal .notranslate}]{.pre}) must remain pristine, so it is not allowed to "install" packages using the traditional make process and after an compilation attempt all created source files must be removed. This can be achieved with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`no-all`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`purge`{.docutils .literal .notranslate}]{.pre}.

You can pick **any** folder outside the source tree. We recommend to create a folder [`build`{.docutils .literal .notranslate}]{.pre} in the top-level directory, or multiple folders in case you want to have separate builds of LAMMPS with different options ([`build-parallel`{.docutils .literal .notranslate}]{.pre}, [`build-serial`{.docutils .literal .notranslate}]{.pre}) or with different compilers ([`build-gnu`{.docutils .literal .notranslate}]{.pre}, [`build-clang`{.docutils .literal .notranslate}]{.pre}, [`build-intel`{.docutils .literal .notranslate}]{.pre}) and so on. All the auxiliary files created by one build process (executable, object files, log files, etc) are stored in this directory or subdirectories within it that CMake creates.
:::

:::::::: {#running-cmake .section}
## Running CMake[](#running-cmake "Link to this heading"){.headerlink}

::::: {#cli-version .section}
### CLI version[](#cli-version "Link to this heading"){.headerlink}

In the (empty) [`build`{.docutils .literal .notranslate}]{.pre} directory, we now run the command [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`../cmake`{.docutils .literal .notranslate}]{.pre}, which will start the configuration phase and you will see the progress of the configuration printed to the screen followed by a summary of the enabled features, options and compiler settings. A typical summary screen will look like this:

:::: {.highlight-console .notranslate}
::: highlight
    $ cmake ../cmake/
    -- The CXX compiler identification is GNU 8.2.0
    -- Check for working CXX compiler: /opt/tools/gcc-8.2.0/bin/c++
    -- Check for working CXX compiler: /opt/tools/gcc-8.2.0/bin/c++ - works
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Found Git: /usr/bin/git (found version "2.25.2")
    -- Running check for auto-generated files from make-based build system
    -- Found MPI_CXX: /usr/lib64/mpich/lib/libmpicxx.so (found version "3.1")
    -- Found MPI: TRUE (found version "3.1")
    -- Looking for C++ include omp.h
    -- Looking for C++ include omp.h - found
    -- Found OpenMP_CXX: -fopenmp (found version "4.5")
    -- Found OpenMP: TRUE (found version "4.5")
    -- Found JPEG: /usr/lib64/libjpeg.so (found version "62")
    -- Found PNG: /usr/lib64/libpng.so (found version "1.6.37")
    -- Found ZLIB: /usr/lib64/libz.so (found version "1.2.11")
    -- Found GZIP: /usr/bin/gzip
    -- Found FFMPEG: /usr/bin/ffmpeg
    -- Performing Test COMPILER_SUPPORTS-ffast-math
    -- Performing Test COMPILER_SUPPORTS-ffast-math - Success
    -- Performing Test COMPILER_SUPPORTS-march=native
    -- Performing Test COMPILER_SUPPORTS-march=native - Success
    -- Looking for C++ include cmath
    -- Looking for C++ include cmath - found
    -- Generating style_angle.h...
    [...]
    -- Generating lmpinstalledpkgs.h...
    -- The following tools and libraries have been found and configured:
     * Git
     * MPI
     * OpenMP
     * JPEG
     * PNG
     * ZLIB

    -- <<< Build configuration >>>
       Build type:       RelWithDebInfo
       Install path:     /home/akohlmey/.local
       Generator:        Unix Makefiles using /usr/bin/gmake
    -- <<< Compilers and Flags: >>>
    -- C++ Compiler:     /opt/tools/gcc-8.2.0/bin/c++
          Type:          GNU
          Version:       8.2.0
          C++ Flags:     -O2 -g -DNDEBUG
          Defines:       LAMMPS_SMALLBIG;LAMMPS_MEMALIGN=64;LAMMPS_JPEG;LAMMPS_PNG;LAMMPS_GZIP;LAMMPS_FFMPEG
          Options:       -ffast-math;-march=native
    -- <<< Linker flags: >>>
    -- Executable name:  lmp
    -- Static library flags:
    -- <<< MPI flags >>>
    -- MPI includes:     /usr/include/mpich-x86_64
    -- MPI libraries:    /usr/lib64/mpich/lib/libmpicxx.so;/usr/lib64/mpich/lib/libmpi.so;
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/akohlmey/compile/lammps/build
:::
::::

The [`cmake`{.docutils .literal .notranslate}]{.pre} command has one mandatory argument, and that is a folder with either the file [`CMakeLists.txt`{.docutils .literal .notranslate}]{.pre} or [`CMakeCache.txt`{.docutils .literal .notranslate}]{.pre}. The [`CMakeCache.txt`{.docutils .literal .notranslate}]{.pre} file is created during the CMake configuration run and contains all active settings, thus after a first run of CMake all future runs in the build folder can use the folder [`.`{.docutils .literal .notranslate}]{.pre} and CMake will know where to find the CMake scripts and reload the settings from the previous step. This means, that one can modify an existing configuration by re-running CMake, but only needs to provide flags indicating the desired change, everything else will be retained. One can also mix compilation and configuration, i.e. start with a minimal configuration and then, if needed, enable additional features and recompile.

The steps above **will NOT compile the code**. The compilation can be started in a portable fashion with [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--build`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`.`{.docutils .literal .notranslate}]{.pre}, or you use the selected built tool, e.g. [`make`{.docutils .literal .notranslate}]{.pre}.
:::::

::: {#tui-version .section}
### TUI version[](#tui-version "Link to this heading"){.headerlink}

For the text mode UI CMake program the basic principle is the same. You start the command [`ccmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`../cmake`{.docutils .literal .notranslate}]{.pre} in the [`build`{.docutils .literal .notranslate}]{.pre} folder.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <figure id="id1" class="align-center">                                                                                                                                                                                               | <figure id="id2" class="align-center">                                                                                                                                                                                                    | <figure id="id3" class="align-center">                                                                                                                                                                                                  |
| <a href="_images/ccmake-initial.png" class="reference internal image-reference"><img src="_images/ccmake-initial.png" style="width: 378.18px; height: 231.99px;" alt="_images/ccmake-initial.png" /></a>                             | <a href="_images/ccmake-config.png" class="reference internal image-reference"><img src="_images/ccmake-config.png" style="width: 378.18px; height: 231.99px;" alt="_images/ccmake-config.png" /></a>                                     | <a href="_images/ccmake-options.png" class="reference internal image-reference"><img src="_images/ccmake-options.png" style="width: 378.18px; height: 231.99px;" alt="_images/ccmake-options.png" /></a>                                |
| <figcaption><p><span class="caption-text">Initial <span class="pre"><code class="docutils literal notranslate">ccmake</code></span> screen</span><a href="#id1" class="headerlink" title="Link to this image"></a></p></figcaption> | <figcaption><p><span class="caption-text">Configure output of <span class="pre"><code class="docutils literal notranslate">ccmake</code></span></span><a href="#id2" class="headerlink" title="Link to this image"></a></p></figcaption> | <figcaption><p><span class="caption-text">Options screen of <span class="pre"><code class="docutils literal notranslate">ccmake</code></span></span><a href="#id3" class="headerlink" title="Link to this image"></a></p></figcaption> |
| </figure>                                                                                                                                                                                                                            | </figure>                                                                                                                                                                                                                                 | </figure>                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

This will show you the initial screen (left image) with the empty configuration cache. Now you type the 'c' key to run the configuration step. That will do a first configuration run and show the summary (center image). You exit the summary screen with 'e' and see now the main screen with detected options and settings. You can now make changes by moving and down with the arrow keys of the keyboard and modify entries. For on/off settings, the enter key will toggle the state. For others, hitting enter will allow you to modify the value and you commit the change by hitting the enter key again or cancel using the escape key. All "new" settings will be marked with a star '\*' and for as long as one setting is marked like this, you have to re-run the configuration by hitting the 'c' key again, sometimes multiple times unless the TUI shows the word "generate" next to the letter 'g' and by hitting the 'g' key the build files will be written to the folder and the TUI exits. You can quit without generating build files by hitting 'q'.
:::

::: {#gui-version .section}
### GUI version[](#gui-version "Link to this heading"){.headerlink}

For the graphical CMake program the steps are similar to the TUI version. You can type the command [`cmake-gui`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`../cmake`{.docutils .literal .notranslate}]{.pre} in the [`build`{.docutils .literal .notranslate}]{.pre} folder. In this case the path to the CMake script folder is not required, it can also be entered from the GUI.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <figure id="id4" class="align-center">                                                                                                                                                                                                  | <figure id="id5" class="align-center">                                                                                                                                                                                                          | <figure id="id6" class="align-center">                                                                                                                                                                                                     |
| <a href="_images/cmake-gui-initial.png" class="reference internal image-reference"><img src="_images/cmake-gui-initial.png" style="width: 369.20000000000005px; height: 274.8px;" alt="_images/cmake-gui-initial.png" /></a>            | <a href="_images/cmake-gui-popup.png" class="reference internal image-reference"><img src="_images/cmake-gui-popup.png" style="width: 304.8px; height: 232.2px;" alt="_images/cmake-gui-popup.png" /></a>                                       | <a href="_images/cmake-gui-options.png" class="reference internal image-reference"><img src="_images/cmake-gui-options.png" style="width: 369.20000000000005px; height: 274.8px;" alt="_images/cmake-gui-options.png" /></a>               |
| <figcaption><p><span class="caption-text">Initial <span class="pre"><code class="docutils literal notranslate">cmake-gui</code></span> screen</span><a href="#id4" class="headerlink" title="Link to this image"></a></p></figcaption> | <figcaption><p><span class="caption-text">Generator selection in <span class="pre"><code class="docutils literal notranslate">cmake-gui</code></span></span><a href="#id5" class="headerlink" title="Link to this image"></a></p></figcaption> | <figcaption><p><span class="caption-text">Options screen of <span class="pre"><code class="docutils literal notranslate">cmake-gui</code></span></span><a href="#id6" class="headerlink" title="Link to this image"></a></p></figcaption> |
| </figure>                                                                                                                                                                                                                               | </figure>                                                                                                                                                                                                                                       | </figure>                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Again, you start with an empty configuration cache (left image) and need to start the configuration step. For the very first configuration in a folder, you will have a pop-up dialog (center image) asking to select the desired build tool and some configuration settings (stick with the default) and then you get the option screen with all new settings highlighted in red. You can modify them (or not) and click on the "configure" button again until satisfied and click on the "generate" button to write out the build files. You can exit the GUI from the "File" menu or hit "ctrl-q".
:::
::::::::

:::::: {#setting-options .section}
## Setting options[](#setting-options "Link to this heading"){.headerlink}

Options that enable, disable or modify settings are modified by setting the value of CMake variables. This is done on the command-line with the *-D* flag in the format [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`VARIABLE=value`{.docutils .literal .notranslate}]{.pre}, e.g. [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_BUILD_TYPE=Release`{.docutils .literal .notranslate}]{.pre} or [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`BUILD_MPI=on`{.docutils .literal .notranslate}]{.pre}. There is one quirk: when used before the CMake directory, there may be a space between the *-D* flag and the variable, after it must not be. Such CMake variables can have boolean values (on/off, yes/no, or 1/0 are all valid) or are strings representing a choice, or a path, or are free format. If the string would contain whitespace, it must be put in quotes, for example [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`CMAKE_CXX_FLAGS="-O3`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-Wall`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-ftree-vectorize`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-ffast-math"`{.docutils .literal .notranslate}]{.pre}.

CMake variables fall into two categories: 1) common CMake variables that are used by default for any CMake configuration setup and 2) project specific variables, i.e. settings that are specific for LAMMPS. Also CMake variables can be flagged as *advanced*, which means they are not shown in the text mode or graphical CMake program in the overview of all settings by default, but only when explicitly requested (by hitting the 't' key or clicking on the 'Advanced' check-box).

::: {#some-common-cmake-variables .section}
### Some common CMake variables[](#some-common-cmake-variables "Link to this heading"){.headerlink}

  Variable                                                            Description
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`CMAKE_INSTALL_PREFIX`{.docutils .literal .notranslate}]{.pre}     root directory of install location for [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre} (default: [`$HOME/.local`{.docutils .literal .notranslate}]{.pre})
  [`LAMMPS_INSTALL_RPATH`{.docutils .literal .notranslate}]{.pre}     set or remove runtime path setting from binaries for [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre} (default: [`off`{.docutils .literal .notranslate}]{.pre})
  [`CMAKE_BUILD_TYPE`{.docutils .literal .notranslate}]{.pre}         controls compilation options: one of [`RelWithDebInfo`{.docutils .literal .notranslate}]{.pre} (default), [`Release`{.docutils .literal .notranslate}]{.pre}, [`Debug`{.docutils .literal .notranslate}]{.pre}, [`MinSizeRel`{.docutils .literal .notranslate}]{.pre}
  [`BUILD_SHARED_LIBS`{.docutils .literal .notranslate}]{.pre}        if set to [`on`{.docutils .literal .notranslate}]{.pre} build the LAMMPS library as shared library (default: [`off`{.docutils .literal .notranslate}]{.pre})
  [`CMAKE_MAKE_PROGRAM`{.docutils .literal .notranslate}]{.pre}       name/path of the compilation command (default depends on *-G* option, usually [`make`{.docutils .literal .notranslate}]{.pre})
  [`CMAKE_VERBOSE_MAKEFILE`{.docutils .literal .notranslate}]{.pre}   if set to [`on`{.docutils .literal .notranslate}]{.pre} echo commands while executing during build (default: [`off`{.docutils .literal .notranslate}]{.pre})
  [`CMAKE_C_COMPILER`{.docutils .literal .notranslate}]{.pre}         C compiler to be used for compilation (default: system specific, [`gcc`{.docutils .literal .notranslate}]{.pre} on Linux)
  [`CMAKE_CXX_COMPILER`{.docutils .literal .notranslate}]{.pre}       C++ compiler to be used for compilation (default: system specific, [`g++`{.docutils .literal .notranslate}]{.pre} on Linux)
  [`CMAKE_Fortran_COMPILER`{.docutils .literal .notranslate}]{.pre}   Fortran compiler to be used for compilation (default: system specific, [`gfortran`{.docutils .literal .notranslate}]{.pre} on Linux)
  [`CXX_COMPILER_LAUNCHER`{.docutils .literal .notranslate}]{.pre}    tool to launch the C++ compiler, e.g. [`ccache`{.docutils .literal .notranslate}]{.pre} or [`distcc`{.docutils .literal .notranslate}]{.pre} for faster compilation (default: empty)
:::

::: {#some-common-lammps-specific-variables .section}
### Some common LAMMPS specific variables[](#some-common-lammps-specific-variables "Link to this heading"){.headerlink}

  Variable                                                    Description
  ----------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`BUILD_MPI`{.docutils .literal .notranslate}]{.pre}        build LAMMPS with MPI support (default: [`on`{.docutils .literal .notranslate}]{.pre} if a working MPI available, else [`off`{.docutils .literal .notranslate}]{.pre})
  [`BUILD_OMP`{.docutils .literal .notranslate}]{.pre}        build LAMMPS with OpenMP support (default: [`on`{.docutils .literal .notranslate}]{.pre} if compiler supports OpenMP fully, else [`off`{.docutils .literal .notranslate}]{.pre})
  [`BUILD_TOOLS`{.docutils .literal .notranslate}]{.pre}      compile some additional executables from the [`tools`{.docutils .literal .notranslate}]{.pre} folder (default: [`off`{.docutils .literal .notranslate}]{.pre})
  [`BUILD_DOC`{.docutils .literal .notranslate}]{.pre}        include building the HTML format documentation for packaging/installing (default: [`off`{.docutils .literal .notranslate}]{.pre})
  [`LAMMPS_MACHINE`{.docutils .literal .notranslate}]{.pre}   when set to [`name`{.docutils .literal .notranslate}]{.pre} the LAMMPS executable and library will be called [`lmp_name`{.docutils .literal .notranslate}]{.pre} and [`liblammps_name.a`{.docutils .literal .notranslate}]{.pre}
  [`FFT`{.docutils .literal .notranslate}]{.pre}              select which FFT library to use: [`FFTW3`{.docutils .literal .notranslate}]{.pre}, [`MKL`{.docutils .literal .notranslate}]{.pre}, [`KISS`{.docutils .literal .notranslate}]{.pre} (default, unless FFTW3 is found)
  [`FFT_KOKKOS`{.docutils .literal .notranslate}]{.pre}       select which FFT library to use in Kokkos-enabled styles: [`FFTW3`{.docutils .literal .notranslate}]{.pre}, [`MKL`{.docutils .literal .notranslate}]{.pre}, [`HIPFFT`{.docutils .literal .notranslate}]{.pre}, [`CUFFT`{.docutils .literal .notranslate}]{.pre}, [`MKL_GPU`{.docutils .literal .notranslate}]{.pre}, [`KISS`{.docutils .literal .notranslate}]{.pre} (default)
  [`FFT_SINGLE`{.docutils .literal .notranslate}]{.pre}       select whether to use single precision FFTs (default: [`off`{.docutils .literal .notranslate}]{.pre})
  [`WITH_JPEG`{.docutils .literal .notranslate}]{.pre}        whether to support JPEG format in [[dump image]{.doc}]dump_image.md){.reference .internal} (default: [`on`{.docutils .literal .notranslate}]{.pre} if found)
  [`WITH_PNG`{.docutils .literal .notranslate}]{.pre}         whether to support PNG format in [[dump image]{.doc}]dump_image.md){.reference .internal} (default: [`on`{.docutils .literal .notranslate}]{.pre} if found)
  [`WITH_GZIP`{.docutils .literal .notranslate}]{.pre}        whether to support reading and writing compressed files (default: [`on`{.docutils .literal .notranslate}]{.pre} if found)
  [`WITH_FFMPEG`{.docutils .literal .notranslate}]{.pre}      whether to support generating movies with [[dump movie]{.doc}]dump_image.md){.reference .internal} (default: [`on`{.docutils .literal .notranslate}]{.pre} if found)
:::

::: {#enabling-or-disabling-lammps-packages .section}
### Enabling or disabling LAMMPS packages[](#enabling-or-disabling-lammps-packages "Link to this heading"){.headerlink}

The LAMMPS software is organized into a common core that is always included and a large number of [[add-on packages]{.doc}]Packages.md){.reference .internal} that have to be enabled to be included into a LAMMPS executable. Packages are enabled through setting variables of the kind [`PKG_<NAME>`{.docutils .literal .notranslate}]{.pre} to [`on`{.docutils .literal .notranslate}]{.pre} and disabled by setting them to [`off`{.docutils .literal .notranslate}]{.pre} (or using [`yes`{.docutils .literal .notranslate}]{.pre}, [`no`{.docutils .literal .notranslate}]{.pre}, [`1`{.docutils .literal .notranslate}]{.pre}, [`0`{.docutils .literal .notranslate}]{.pre} correspondingly). [`<NAME>`{.docutils .literal .notranslate}]{.pre} has to be replaced by the name of the package, e.g. [`MOLECULE`{.docutils .literal .notranslate}]{.pre} or [`EXTRA-PAIR`{.docutils .literal .notranslate}]{.pre}.
:::
::::::

:::::::: {#using-presets .section}
## Using presets[](#using-presets "Link to this heading"){.headerlink}

Since LAMMPS has a lot of optional features and packages, specifying them all on the command-line can be tedious. Or when selecting a different compiler toolchain, multiple options have to be changed consistently and that is rather error prone. Or when enabling certain packages, they require consistent settings to be operated in a particular mode. For this purpose, we are providing a selection of "preset files" for CMake in the folder [`cmake/presets`{.docutils .literal .notranslate}]{.pre}. They represent a way to pre-load or override the CMake configuration cache by setting or changing CMake variables. Preset files are loaded using the *-C* command-line flag. You can combine loading multiple preset files or change some variables later with additional *-D* flags. A few examples:

:::: {.highlight-bash .notranslate}
::: highlight
    cmake -C ../cmake/presets/basic.cmake -D PKG_MISC=on ../cmake
    cmake -C ../cmake/presets/clang.cmake -C ../cmake/presets/most.cmake ../cmake
    cmake -C ../cmake/presets/basic.cmake -D BUILD_MPI=off ../cmake
:::
::::

The first command will install the packages [`KSPACE`{.docutils .literal .notranslate}]{.pre}, [`MANYBODY`{.docutils .literal .notranslate}]{.pre}, [`MOLECULE`{.docutils .literal .notranslate}]{.pre}, [`RIGID`{.docutils .literal .notranslate}]{.pre}, [`GRAPHICS`{.docutils .literal .notranslate}]{.pre}, and [`MISC`{.docutils .literal .notranslate}]{.pre}; the first five from the preset file and the sixth from the explicit variable definition. The second command will first switch the compiler toolchain to use the Clang compilers and install a large number of packages that are not depending on any special external libraries or tools and are not very unusual. The third command will enable the first four packages like above and then enforce compiling LAMMPS as a serial program (using the MPI STUBS library).

It is also possible to do this incrementally.

:::: {.highlight-bash .notranslate}
::: highlight
    cmake -C ../cmake/presets/basic.cmake ../cmake
    cmake -D PKG_MISC=on .
:::
::::

will achieve the same final configuration as in the first example above. In this scenario it is particularly convenient to do the second configuration step using either the text mode or graphical user interface ([`ccmake`{.docutils .literal .notranslate}]{.pre} or [`cmake-gui`{.docutils .literal .notranslate}]{.pre}).

::: {.admonition .note}
Note

Using a preset to select a compiler package ([`clang.cmake`{.docutils .literal .notranslate}]{.pre}, [`gcc.cmake`{.docutils .literal .notranslate}]{.pre}, [`intel.cmake`{.docutils .literal .notranslate}]{.pre}, [`oneapi.cmake`{.docutils .literal .notranslate}]{.pre}, or [`pgi.cmake`{.docutils .literal .notranslate}]{.pre}) are an exception to the mechanism of updating the configuration incrementally, as they will trigger a reset of cached internal CMake settings and thus reset settings to their default values.
:::
::::::::

::: {#compilation-and-build-targets .section}
## Compilation and build targets[](#compilation-and-build-targets "Link to this heading"){.headerlink}

The actual compilation will be started by running the selected build command (on Linux this is by default [`make`{.docutils .literal .notranslate}]{.pre}, see below how to select alternatives). You can also use the portable command [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--build`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`.`{.docutils .literal .notranslate}]{.pre} which will adapt to whatever the selected build command is. This is particularly convenient, if you have set a custom build command via the [`CMAKE_MAKE_PROGRAM`{.docutils .literal .notranslate}]{.pre} variable.

When calling the build program, you can also select which "target" is to be build through appending the [`--target`{.docutils .literal .notranslate}]{.pre} flag and the name of the target to the build command. When using [`make`{.docutils .literal .notranslate}]{.pre} as build tool, you can just append the target name to the command. Example: [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--build`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`.`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--target`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`all`{.docutils .literal .notranslate}]{.pre} or [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`all`{.docutils .literal .notranslate}]{.pre}. The following abstract targets are available:

  Target                                               Description
  ---------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`all`{.docutils .literal .notranslate}]{.pre}       build "everything" (default)
  [`lammps`{.docutils .literal .notranslate}]{.pre}    build the LAMMPS library and executable
  [`doc`{.docutils .literal .notranslate}]{.pre}       build the HTML documentation (if configured)
  [`install`{.docutils .literal .notranslate}]{.pre}   install all target files into folders in [`CMAKE_INSTALL_PREFIX`{.docutils .literal .notranslate}]{.pre}
  [`test`{.docutils .literal .notranslate}]{.pre}      run some tests (if configured with [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ENABLE_TESTING=on`{.docutils .literal .notranslate}]{.pre})
  [`clean`{.docutils .literal .notranslate}]{.pre}     remove all generated files
:::

::::::: {#choosing-generators .section}
## Choosing generators[](#choosing-generators "Link to this heading"){.headerlink}

While CMake usually defaults to creating makefiles to compile software with the [`make`{.docutils .literal .notranslate}]{.pre} program, it supports multiple alternate build tools (e.g. [`ninja-build`{.docutils .literal .notranslate}]{.pre} which tends to be faster and more efficient in parallelizing builds than [`make`{.docutils .literal .notranslate}]{.pre}) and can generate project files for integrated development environments (IDEs) like VisualStudio, Eclipse or CodeBlocks. This is specific to how the local CMake version was configured and compiled. The list of available options can be seen at the end of the output of [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--help`{.docutils .literal .notranslate}]{.pre}. Example on Fedora 31 this is:

:::: {.highlight-none .notranslate}
::: highlight
    Generators

    The following generators are available on this platform (* marks default):
    * Unix Makefiles               = Generates standard UNIX makefiles.
      Green Hills MULTI            = Generates Green Hills MULTI files
                                     (experimental, work-in-progress).
      Ninja                        = Generates build.ninja files.
      Ninja Multi-Config           = Generates build-<Config>.ninja files.
      Watcom WMake                 = Generates Watcom WMake makefiles.
      CodeBlocks - Ninja           = Generates CodeBlocks project files.
      CodeBlocks - Unix Makefiles  = Generates CodeBlocks project files.
      CodeLite - Ninja             = Generates CodeLite project files.
      CodeLite - Unix Makefiles    = Generates CodeLite project files.
      Sublime Text 2 - Ninja       = Generates Sublime Text 2 project files.
      Sublime Text 2 - Unix Makefiles
                                   = Generates Sublime Text 2 project files.
      Kate - Ninja                 = Generates Kate project files.
      Kate - Unix Makefiles        = Generates Kate project files.
      Eclipse CDT4 - Ninja         = Generates Eclipse CDT 4.0 project files.
      Eclipse CDT4 - Unix Makefiles= Generates Eclipse CDT 4.0 project files.
:::
::::

Below is a screenshot of using the CodeBlocks IDE with the ninja build tool after running CMake as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    cmake -G 'CodeBlocks - Ninja' ../cmake/presets/most.cmake ../cmake/
:::
::::

![](_images/cmake-codeblocks.png){.align-center}
:::::::
:::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::

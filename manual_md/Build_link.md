:::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::: {#link-lammps-as-a-library-to-another-code .section}
# [3.4. ]{.section-number}Link LAMMPS as a library to another code[](#link-lammps-as-a-library-to-another-code "Link to this heading"){.headerlink}

LAMMPS is designed as a library of C++ objects that can be integrated into other applications, including Python scripts. The files [`src/library.cpp`{.docutils .literal .notranslate}]{.pre} and [`src/library.h`{.docutils .literal .notranslate}]{.pre} define a C-style API for using LAMMPS as a library. See the [[Library interface to LAMMPS]{.doc}]Howto_library.md){.reference .internal} page for a description of the interface and how to use it for your needs.

The [[Basic build options]{.doc}]Build_basics.md){.reference .internal} page explains how to build LAMMPS as either a shared or static library. This results in a file in the compilation folder called [`liblammps.a`{.docutils .literal .notranslate}]{.pre} or [`liblammps_<name>.a`{.docutils .literal .notranslate}]{.pre} in case of building a static library. In case of a shared library, the name is the same only that the suffix is going to be either [`.so`{.docutils .literal .notranslate}]{.pre} or [`.dylib`{.docutils .literal .notranslate}]{.pre} or [`.dll`{.docutils .literal .notranslate}]{.pre} instead of [`.a`{.docutils .literal .notranslate}]{.pre} depending on the OS. In some cases, the [`.so`{.docutils .literal .notranslate}]{.pre} file may be a symbolic link to a file with the suffix [`.so.0`{.docutils .literal .notranslate}]{.pre} (or some other number).

::: {.admonition .note}
Note

Care should be taken to use the same MPI library for the calling code and the LAMMPS library, unless LAMMPS is to be compiled without (real) MPI support using the included STUBS MPI library.
:::

:::::::::::::::: {#link-with-lammps-as-a-static-library .section}
## [3.4.1. ]{.section-number}Link with LAMMPS as a static library[](#link-with-lammps-as-a-static-library "Link to this heading"){.headerlink}

The calling application can link to LAMMPS as a static library with compilation and link commands, as in the examples shown below. These are examples for a code written in C in the file [`caller.c`{.docutils .literal .notranslate}]{.pre}. The benefit of linking to a static library is, that the resulting executable is independent of that library since all required executable code from the library is copied into the calling executable.

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-0-0-0 .sphinx-tabs-panel aria-labelledby="tab-0-0-0" role="tabpanel" tabindex="0"}
This assumes that LAMMPS has been configured without setting a [`LAMMPS_MACHINE`{.docutils .literal .notranslate}]{.pre} name, installed with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre}, and the [`PKG_CONFIG_PATH`{.docutils .literal .notranslate}]{.pre} environment variable has been updated to include the [`liblammps.pc`{.docutils .literal .notranslate}]{.pre} file installed into the configured destination folder. The commands to compile and link a coupled executable are then:

:::: {.highlight-bash .notranslate}
::: highlight
    mpicc -c -O $(pkg-config --cflags liblammps) caller.c
    mpicxx -o caller caller.o -$(pkg-config --libs liblammps)
:::
::::
:::::

::::: {#panel-0-0-1 .sphinx-tabs-panel aria-labelledby="tab-0-0-1" hidden="true" role="tabpanel" tabindex="0"}
This assumes that LAMMPS has been compiled in the folder [`${HOME}/lammps/src`{.docutils .literal .notranslate}]{.pre} with "make mpi". The commands to compile and link a coupled executable are then:

:::: {.highlight-bash .notranslate}
::: highlight
    mpicc -c -O -I${HOME}/lammps/src caller.c
    mpicxx -o caller caller.o -L${HOME}/lammps/src -llammps_mpi
:::
::::

The [`-I`{.docutils .literal .notranslate}]{.pre} argument is the path to the location of the [`library.h`{.docutils .literal .notranslate}]{.pre} header file containing the interface to the LAMMPS C-style library interface. The [`-L`{.docutils .literal .notranslate}]{.pre} argument is the path to where the [`liblammps_mpi.a`{.docutils .literal .notranslate}]{.pre} file is located. The [`-llammps_mpi`{.docutils .literal .notranslate}]{.pre} argument is shorthand for telling the compiler to link the file [`liblammps_mpi.a`{.docutils .literal .notranslate}]{.pre}. If LAMMPS has been built as a shared library, then the linker will use [`liblammps_mpi.so`{.docutils .literal .notranslate}]{.pre} instead. If both files are available, the linker will usually prefer the shared library. In case of a shared library, you may need to update the [`LD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre} environment variable or running the [`caller`{.docutils .literal .notranslate}]{.pre} executable will fail since it cannot find the shared library at runtime.
:::::
::::::::::

However, it is only as simple as shown above for the case of a plain LAMMPS library without any optional packages that depend on libraries (bundled or external) or when using a shared library. Otherwise, you need to include all flags, libraries, and paths for the coupled executable, that are also required to link the LAMMPS executable.

::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::: {#panel-1-1-0 .sphinx-tabs-panel aria-labelledby="tab-1-1-0" role="tabpanel" tabindex="0"}
When using CMake, additional libraries with sources in the lib folder are built, but not included in [`liblammps.a`{.docutils .literal .notranslate}]{.pre} and (currently) not installed with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre} and not included in the [`pkgconfig`{.docutils .literal .notranslate}]{.pre} configuration file. They can be found in the top level build folder, but you have to determine the necessary link flags manually. It is therefore recommended to either use the traditional make procedure to build and link with a static library or build and link with a shared library instead.
:::

:::: {#panel-1-1-1 .sphinx-tabs-panel aria-labelledby="tab-1-1-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The traditional make build process no longer supports building packages that require extra build steps in the [`lib`{.docutils .literal .notranslate}]{.pre} folder.
::::
:::::::
::::::::::::::::

:::::::::::::::::::::: {#link-with-lammps-as-a-shared-library .section}
## [3.4.2. ]{.section-number}Link with LAMMPS as a shared library[](#link-with-lammps-as-a-shared-library "Link to this heading"){.headerlink}

When linking to LAMMPS built as a shared library, the situation becomes much simpler, as all dependent libraries and objects are either included in the shared library or registered as a dependent library in the shared library file. Thus, those libraries need not be specified when linking the calling executable. Only the [`-I`{.docutils .literal .notranslate}]{.pre} flags are needed. So the example case from above of the serial version static LAMMPS library with the POEMS package installed becomes:

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-2-2-0 .sphinx-tabs-panel aria-labelledby="tab-2-2-0" role="tabpanel" tabindex="0"}
The commands with a shared LAMMPS library compiled with the CMake build process are the same as for the static library.

:::: {.highlight-bash .notranslate}
::: highlight
    mpicc -c -O $(pkg-config --cflags liblammps) caller.c
    mpicxx -o caller caller.o -$(pkg-config --libs liblammps)
:::
::::
:::::

::::: {#panel-2-2-1 .sphinx-tabs-panel aria-labelledby="tab-2-2-1" hidden="true" role="tabpanel" tabindex="0"}
The commands with a shared LAMMPS library compiled with the traditional make build using [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`mode=shared`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`serial`{.docutils .literal .notranslate}]{.pre} becomes:

:::: {.highlight-bash .notranslate}
::: highlight
    gcc -c -O -I${HOME}/lammps/src caller.c
    g++ -o caller caller.o -L${HOME}/lammps/src -llammps_serial
:::
::::
:::::
::::::::::

::::::::::::: {#locating-liblammps-so-at-runtime .section}
### Locating liblammps.so at runtime[](#locating-liblammps-so-at-runtime "Link to this heading"){.headerlink}

Unlike with a static link, now the [`liblammps.so`{.docutils .literal .notranslate}]{.pre} file is required at runtime and needs to be in a folder, where the shared linker program of the operating system can find it. This would be either a folder like [`/usr/local/lib64`{.docutils .literal .notranslate}]{.pre} or [`${HOME}/.local/lib64`{.docutils .literal .notranslate}]{.pre} or a folder pointed to by the [`LD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre} environment variable. You can type

:::: {.highlight-bash .notranslate}
::: highlight
    printenv LD_LIBRARY_PATH
:::
::::

to see what directories are in that list.

Or you can add the LAMMPS src directory or the directory you performed a CMake style build in to your [`LD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre} environment variable, so that the current version of the shared library is always available to programs that use it.

For the Bourne or Korn shells (/bin/sh, /bin/ksh, /bin/bash etc.), you would add something like this to your [`${HOME}/.profile`{.docutils .literal .notranslate}]{.pre} file:

:::: {.highlight-bash .notranslate}
::: highlight
    LD_LIBRARY_PATH=${LD_LIBRARY_PATH-/usr/lib64}:${HOME}/lammps/src
    export LD_LIBRARY_PATH
:::
::::

For the csh or tcsh shells, you would equivalently add something like this to your [`${HOME}/.cshrc`{.docutils .literal .notranslate}]{.pre} file:

:::: {.highlight-csh .notranslate}
::: highlight
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:${HOME}/lammps/src
:::
::::

You can verify whether all required shared libraries are found with the [`ldd`{.docutils .literal .notranslate}]{.pre} tool. Example:

:::: {.highlight-bash .notranslate}
::: highlight
    LD_LIBRARY_PATH=/home/user/lammps/src ldd caller
         linux-vdso.so.1 (0x00007ffe729e0000)
         liblammps.so => /home/user/lammps/src/liblammps.so (0x00007fc91bb9e000)
         libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007fc91b984000)
         libm.so.6 => /lib64/libm.so.6 (0x00007fc91b83e000)
         libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007fc91b824000)
         libc.so.6 => /lib64/libc.so.6 (0x00007fc91b65b000)
         /lib64/ld-linux-x86-64.so.2 (0x00007fc91c094000)
:::
::::

If a required library is missing, you would get a 'not found' entry:

:::: {.highlight-bash .notranslate}
::: highlight
    ldd caller
         linux-vdso.so.1 (0x00007ffd672fe000)
         liblammps.so => not found
         libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00007fb7c7e86000)
         libm.so.6 => /usr/lib64/libm.so.6 (0x00007fb7c7d40000)
         libgcc_s.so.1 => /usr/lib64/libgcc_s.so.1 (0x00007fb7c7d26000)
         libc.so.6 => /usr/lib64/libc.so.6 (0x00007fb7c7b5d000)
         /lib64/ld-linux-x86-64.so.2 (0x00007fb7c80a2000)
:::
::::
:::::::::::::
::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

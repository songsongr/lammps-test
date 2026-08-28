:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#lammps-library-interfaces .section}
# [1. ]{.section-number}LAMMPS Library Interfaces[](#lammps-library-interfaces "Link to this heading"){.headerlink}

As described on the [[library interface to LAMMPS]{.doc}]Howto_library.md){.reference .internal} page, LAMMPS can be built as a library (static or shared), so that it can be called by another code, used in a [[coupled manner]{.doc}]Howto_couple.md){.reference .internal} with other codes, or driven through a [[Python script]{.doc}]Python_head.md){.reference .internal}. The LAMMPS standalone executable itself is essentially a thin wrapper on top of the LAMMPS library, which creates a LAMMPS instance, passes the input for processing to that instance, and then exits.

Most of the APIs described below are based on C language wrapper functions in the files [`src/library.h`{.docutils .literal .notranslate}]{.pre} and [`src/library.cpp`{.docutils .literal .notranslate}]{.pre}, but it is also possible to use C++ directly. The basic procedure is always the same: you create one or more instances of [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}, pass commands as strings or from files to that LAMMPS instance to execute calculations, and/or call functions that read, manipulate, and update data from the active class instances inside LAMMPS to do analysis or perform operations that are not possible with existing input script commands.

::: {#thread-safety .note .admonition}
Thread-safety

LAMMPS was initially not conceived as a thread-safe program, but over the years changes have been applied to replace operations that collide with creating multiple LAMMPS instances from multiple-threads of the same process with thread-safe alternatives. This primarily applies to the core LAMMPS code and less so on add-on packages, especially when those packages require additional code in the *lib* folder, interface LAMMPS to Fortran libraries, or the code uses static variables (like the COLVARS package).

Another major issue to deal with is to correctly handle MPI. Creating a LAMMPS instance requires passing an MPI communicator, or it assumes the [`MPI_COMM_WORLD`{.docutils .literal .notranslate}]{.pre} communicator, which spans all MPI processor ranks. When creating multiple LAMMPS object instances from different threads, this communicator has to be different for each thread or else collisions can happen. Or it has to be guaranteed, that only one thread at a time is active. MPI communicators, however, are not a problem, if LAMMPS is compiled with the MPI STUBS library, which implies that there is no MPI communication and only 1 MPI rank.
:::

------------------------------------------------------------------------

::::::: {#lammps-c-library-api .section}
[]{#lammps-c-api}

## [1.1. ]{.section-number}LAMMPS C Library API[](#lammps-c-library-api "Link to this heading"){.headerlink}

The C library interface is the most commonly used path to manage LAMMPS instances from a compiled code and it is the basis for the [[Python]{.doc}]Python_module.md){.reference .internal} and [[Fortran]{.doc}]Fortran.md){.reference .internal} modules. Almost all functions of the C language API require an argument containing a "handle" in the form of a [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} type variable, which points to the location of a LAMMPS class instance.

The [`library.h`{.docutils .literal .notranslate}]{.pre} header file by default does not include the [`mpi.h`{.docutils .literal .notranslate}]{.pre} header file and thus hides the [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal} function which requires the declaration of the [`MPI_comm`{.docutils .literal .notranslate}]{.pre} data type. This is only a problem when the communicator that would be passed is different from [`MPI_COMM_WORLD`{.docutils .literal .notranslate}]{.pre}. Otherwise calling [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal} will work just as well. To make [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal} available, you need to compile the code with [`-DLAMMPS_LIB_MPI`{.docutils .literal .notranslate}]{.pre} or add the line [`#define`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`LAMMPS_LIB_MPI`{.docutils .literal .notranslate}]{.pre} before [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"library.h"`{.docutils .literal .notranslate}]{.pre}.

Please note the [`mpi.h`{.docutils .literal .notranslate}]{.pre} file must usually be the same (and thus the MPI library in use) for the LAMMPS code and library and the calling code. The exception is when LAMMPS was compiled in serial mode using the [`STUBS`{.docutils .literal .notranslate}]{.pre} MPI library. In that case the calling code may be compiled with a different MPI library so long as [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal} is called to create a LAMMPS instance. In that case each MPI rank will run LAMMPS in serial mode.

::: {.note .admonition}
Errors versus exceptions

If the LAMMPS executable encounters an error condition, it will abort after printing an error message. It does so by catching the exceptions that LAMMPS could throw. For a C library interface this is usually not desirable since the calling code might lack the ability to catch such exceptions. Thus, the library functions will catch those exceptions and return from the affected functions. The error status [[`can`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`be`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`queried`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv416lammps_has_errorPv "lammps_has_error"){.reference .internal} and an [[`error`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`message`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`retrieved`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv429lammps_get_last_error_messagePvPci "lammps_get_last_error_message"){.reference .internal}. This is, for example used by the [[LAMMPS python module]{.doc}]Python_module.md){.reference .internal} and then a suitable Python exception is thrown.
:::

::: {.note .admonition}
Using the C library interface as a plugin

Rather than including the C library interface directly including the [`library.h`{.docutils .literal .notranslate}]{.pre} header file and linking to the LAMMPS (static or shared) library at compile time, you can dynamically load LAMMPS at runtime, provided you compiled LAMMPS using a shared library or DLL. The [`liblammpsplugin.h`{.docutils .literal .notranslate}]{.pre} header file and the [`liblammpsplugin.c`{.docutils .literal .notranslate}]{.pre} C code in the [`examples/COUPLE/plugin`{.docutils .literal .notranslate}]{.pre} folder for an interface to LAMMPS that is largely identical to the regular library interface, only that it will load a LAMMPS shared library file at runtime. This can be useful for applications where the interface to LAMMPS would be an optional feature or where you would like to load different versions of the LAMMPS library (e.g. an updated one) without replacing the executable. The [[LAMMPS-GUI]{.std .std-ref}]Tools.md#lammps-gui){.reference .internal} is an example for such an application. It has a wrapper class that supports both modes and which is used can be changed at compile time.
:::

::: {.admonition .warning}
Warning

No checks are made on the arguments of the function calls of the C library interface. *All* function arguments must be non-NULL unless *explicitly* allowed, and must point to consistent and valid data. Buffers for storing returned data must be allocated to a suitable size. Passing invalid or unsuitable information will likely cause crashes or corrupt data.
:::

------------------------------------------------------------------------

::: {.toctree-wrapper .compound}
- [1.1.1. Creating or deleting a LAMMPS object]Library_create.md){.reference .internal}
- [1.1.2. Executing commands]Library_execute.md){.reference .internal}
- [1.1.3. System properties]Library_properties.md){.reference .internal}
- [1.1.4. Per-atom properties]Library_atoms.md){.reference .internal}
- [1.1.5. Computes, fixes, variables]Library_objects.md){.reference .internal}
- [1.1.6. Scatter/gather operations]Library_scatter.md){.reference .internal}
- [1.1.7. Neighbor list access]Library_neighbor.md){.reference .internal}
- [1.1.8. Configuration information]Library_config.md){.reference .internal}
- [1.1.9. Utility functions]Library_utility.md){.reference .internal}
- [1.1.10. Extending the C API]Library_add.md){.reference .internal}
:::

------------------------------------------------------------------------
:::::::

::: {#lammps-python-api .section}
[]{#id1}

## [1.2. ]{.section-number}LAMMPS Python API[](#lammps-python-api "Link to this heading"){.headerlink}

The LAMMPS Python module enables calling the LAMMPS C library API from Python by dynamically loading functions in the LAMMPS shared library through the [Python ctypes module](https://docs.python.org/3/library/ctypes.html){.reference .external}. Because of the dynamic loading, it is **required** that LAMMPS is compiled in [["shared" mode]{.std .std-ref}]Build_basics.md#exe){.reference .internal}. The Python interface is object-oriented, but otherwise tries to be very similar to the C library API. More information on this is in the [[Use Python with LAMMPS]{.doc}]Python_head.md){.reference .internal} section of the manual. Use of the LAMMPS Python module is described in [[The lammps Python module]{.doc}]Python_module.md){.reference .internal}.

------------------------------------------------------------------------
:::

:::: {#lammps-fortran-api .section}
[]{#id2}

## [1.3. ]{.section-number}LAMMPS Fortran API[](#lammps-fortran-api "Link to this heading"){.headerlink}

The LAMMPS Fortran module is a wrapper around calling functions from the LAMMPS C library API. This is done using the ISO_C_BINDING feature in Fortran 2003. The interface is object-oriented but otherwise tries to be very similar to the C library API and the basic Python module.

::: {.toctree-wrapper .compound}
- [1.3.1. The [`LIBLAMMPS`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} Fortran Module]Fortran.md){.reference .internal}
- [1.3.2. Creating or deleting a LAMMPS object]Fortran.md#creating-or-deleting-a-lammps-object){.reference .internal}
- [1.3.3. Executing LAMMPS commands]Fortran.md#executing-lammps-commands){.reference .internal}
- [1.3.4. Accessing system properties]Fortran.md#accessing-system-properties){.reference .internal}
- [1.3.5. The [`LIBLAMMPS`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} module API]Fortran.md#the-liblammps-module-api){.reference .internal}
:::

------------------------------------------------------------------------
::::

:::: {#lammps-cplusplus-api .section}
[]{#id3}

## [1.4. ]{.section-number}LAMMPS C++ API[](#lammps-cplusplus-api "Link to this heading"){.headerlink}

It is also possible to invoke the LAMMPS C++ API directly in your code. It lacks some of the convenience of the C library API, but it allows more direct access to simulation data and thus more low-level manipulations. The following links provide some examples and references to the C++ API.

::: {.toctree-wrapper .compound}
- [1.4.1. Using the C++ API directly]Cplusplus.md){.reference .internal}
- [1.4.2. Creating or deleting a LAMMPS object]Cplusplus.md#creating-or-deleting-a-lammps-object){.reference .internal}
- [1.4.3. Executing LAMMPS commands]Cplusplus.md#executing-lammps-commands){.reference .internal}
:::
::::
::::::::::::::
:::::::::::::::
::::::::::::::::

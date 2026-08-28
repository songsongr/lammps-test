::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#creating-or-deleting-a-lammps-object .section}
# [1.1.1. ]{.section-number}Creating or deleting a LAMMPS object[](#creating-or-deleting-a-lammps-object "Link to this heading"){.headerlink}

This section documents the following functions:

- [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal}

- [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal}

- [[`lammps_open_fortran()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_open_fortraniPPci "lammps_open_fortran"){.reference .internal}

- [[`lammps_close()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv412lammps_closePv "lammps_close"){.reference .internal}

- [[`lammps_mpi_init()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv415lammps_mpi_initv "lammps_mpi_init"){.reference .internal}

- [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal}

- [[`lammps_kokkos_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_kokkos_finalizev "lammps_kokkos_finalize"){.reference .internal}

- [[`lammps_python_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_python_finalizev "lammps_python_finalize"){.reference .internal}

- [[`lammps_plugin_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_plugin_finalizev "lammps_plugin_finalize"){.reference .internal}

- [[`lammps_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv412lammps_errorPviPKc "lammps_error"){.reference .internal}

------------------------------------------------------------------------

The [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal} and [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal} functions are used to create and initialize a [`LAMMPS()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre} instance. They return a reference to this instance as a [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} pointer to be used as the "handle" argument in subsequent function calls until that instance is destroyed by calling [[`lammps_close()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv412lammps_closePv "lammps_close"){.reference .internal}. Here is a simple example demonstrating its use:

:::: {.highlight-c .notranslate}
::: highlight
    #include "library.h"
    #include <stdio.h>

    int main(int argc, char **argv)
    {
      void *handle;
      int version;
      const char *lmpargv[] = { "liblammps", "-log", "none"};
      int lmpargc = sizeof(lmpargv)/sizeof(const char *);

      /* create LAMMPS instance */
      handle = lammps_open_no_mpi(lmpargc, (char **)lmpargv, NULL);
      if (handle == NULL) {
        printf("LAMMPS initialization failed");
        lammps_mpi_finalize();
        return 1;
      }

      /* get and print numerical version code */
      version = lammps_version(handle);
      printf("LAMMPS Version: %d\n",version);

      /* delete LAMMPS instance and shut down MPI */
      lammps_close(handle);
      lammps_mpi_finalize();
      return 0;
    }
:::
::::

The LAMMPS library uses the MPI library it was compiled with and will either run on all processors in the [`MPI_COMM_WORLD`{.docutils .literal .notranslate}]{.pre} communicator or on the set of processors in the communicator passed as the [`comm`{.docutils .literal .notranslate}]{.pre} argument of [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal}. This means the calling code can run LAMMPS on all or a subset of processors. For example, a wrapper code might decide to alternate between LAMMPS and another code, allowing them both to run on all the processors. Or it might allocate part of the processors to LAMMPS and the rest to the other code by creating a custom communicator with [`MPI_Comm_split()`{.docutils .literal .notranslate}]{.pre} and running both codes concurrently before syncing them up periodically. Or it might instantiate multiple instances of LAMMPS to perform different calculations and either alternate between them, run them concurrently on split communicators, or run them one after the other. The [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal} function may be called multiple times for this latter purpose.

The [[`lammps_close()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv412lammps_closePv "lammps_close"){.reference .internal} function is used to shut down the [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} class pointed to by the handle passed as an argument and free all its memory. This has to be called for every instance created with one of the [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal} functions. It will, however, **not** call [`MPI_Finalize()`{.docutils .literal .notranslate}]{.pre}, since that may only be called once. See [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal} for an alternative to invoking [`MPI_Finalize()`{.docutils .literal .notranslate}]{.pre} explicitly from the calling program.

------------------------------------------------------------------------

[]{#_CPPv311lammps_openiPPc8MPI_CommPPv}[]{#_CPPv211lammps_openiPPc8MPI_CommPPv}[]{#lammps_open__i.cPP.MPI_Comm.voidPP}[]{#library_8h_1addeff746d1ad7887254c365efd2ea018 .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_open]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[argc]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[argv]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[ptr]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv411lammps_openiPPc8MPI_CommPPv "Link to this definition"){.headerlink}\

:   Create instance of the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class and return pointer to it.

    The [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal} function creates a new [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} class instance while passing in a list of strings as if they were [[command-line arguments]{.doc}]Run_options.md){.reference .internal} for the LAMMPS executable, and an MPI communicator for LAMMPS to run under. Since the list of arguments is **exactly** as when called from the command-line, the first argument would be the name of the executable and thus is otherwise ignored. However [`argc`{.docutils .literal .notranslate}]{.pre} may be set to 0 and then [`argv`{.docutils .literal .notranslate}]{.pre} may be [`NULL`{.docutils .literal .notranslate}]{.pre}. If MPI is not yet initialized, [`MPI_Init()`{.docutils .literal .notranslate}]{.pre} will be called during creation of the LAMMPS class instance.

    If for some reason the creation or initialization of the LAMMPS instance fails a null pointer is returned.

    ::: versionchanged
    [Changed in version 18Sep2020: ]{.versionmodified .changed}This function now has the pointer to the created LAMMPS class instance as return value. For backward compatibility it is still possible to provide the address of a pointer variable as final argument *ptr*.
    :::

    ::: deprecated
    [Deprecated since version 18Sep2020: ]{.versionmodified .deprecated}The *ptr* argument will be removed in a future release of LAMMPS. It should be set to [`NULL`{.docutils .literal .notranslate}]{.pre} instead.
    :::

    *See also*

    :   [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal}, [[`lammps_open_fortran()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_open_fortraniPPci "lammps_open_fortran"){.reference .internal}

    ::: {.admonition .note}
    Note

    This function is **only** declared when the code using the LAMMPS [`library.h`{.docutils .literal .notranslate}]{.pre} include file is compiled with [`-DLAMMPS_LIB_MPI`{.docutils .literal .notranslate}]{.pre}, or contains a [`#define`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`LAMMPS_LIB_MPI`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre} statement before [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"library.h"`{.docutils .literal .notranslate}]{.pre}. Otherwise you can only use the [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal} or [[`lammps_open_fortran()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_open_fortraniPPci "lammps_open_fortran"){.reference .internal} functions.
    :::

    Parameters[:]{.colon}

    :   - **argc** -- number of command-line arguments

        - **argv** -- list of command-line argument strings

        - **comm** -- MPI communicator for this [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **ptr** -- pointer to a void pointer variable which serves as a handle; may be [`NULL`{.docutils .literal .notranslate}]{.pre}

    Returns[:]{.colon}

    :   pointer to new [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

[]{#_CPPv318lammps_open_no_mpiiPPcPPv}[]{#_CPPv218lammps_open_no_mpiiPPcPPv}[]{#lammps_open_no_mpi__i.cPP.voidPP}[]{#library_8h_1a2532f747f8b8f91310a03e81b191c85b .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_open_no_mpi]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[argc]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[argv]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[ptr]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv418lammps_open_no_mpiiPPcPPv "Link to this definition"){.headerlink}\

:   Variant of [`lammps_open()`{.docutils .literal .notranslate}]{.pre} that implicitly uses [`MPI_COMM_WORLD`{.docutils .literal .notranslate}]{.pre}.

    This function is a version of [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal}, that is missing the MPI communicator argument. It will use [`MPI_COMM_WORLD`{.docutils .literal .notranslate}]{.pre} instead. The type and purpose of arguments and return value are otherwise the same.

    Outside of the convenience, this function is useful, when the LAMMPS library was compiled in serial mode, but the calling code runs in parallel and the [`MPI_Comm`{.docutils .literal .notranslate}]{.pre} data type of the STUBS library would not be compatible with that of the calling code.

    If for some reason the creation or initialization of the LAMMPS instance fails a null pointer is returned.

    ::: versionchanged
    [Changed in version 18Sep2020: ]{.versionmodified .changed}This function now has the pointer to the created LAMMPS class instance as return value. For backward compatibility it is still possible to provide the address of a pointer variable as final argument *ptr*.
    :::

    ::: deprecated
    [Deprecated since version 18Sep2020: ]{.versionmodified .deprecated}The *ptr* argument will be removed in a future release of LAMMPS. It should be set to [`NULL`{.docutils .literal .notranslate}]{.pre} instead.
    :::

    *See also*

    :   [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal}, [[`lammps_open_fortran()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_open_fortraniPPci "lammps_open_fortran"){.reference .internal}

    Parameters[:]{.colon}

    :   - **argc** -- number of command-line arguments

        - **argv** -- list of command-line argument strings

        - **ptr** -- pointer to a void pointer variable which serves as a handle; may be [`NULL`{.docutils .literal .notranslate}]{.pre}

    Returns[:]{.colon}

    :   pointer to new [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

[]{#_CPPv319lammps_open_fortraniPPci}[]{#_CPPv219lammps_open_fortraniPPci}[]{#lammps_open_fortran__i.cPP.i}[]{#library_8h_1a00b91f3fe0d663da088490b873ae80d1 .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_open_fortran]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[argc]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[argv]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[f_comm]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419lammps_open_fortraniPPci "Link to this definition"){.headerlink}\

:   Variant of [`lammps_open()`{.docutils .literal .notranslate}]{.pre} using a Fortran MPI communicator.

    ::: versionadded
    [Added in version 18Sep2020.]{.versionmodified .added}
    :::

    This function is a version of [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal}, that uses an integer for the MPI communicator as the MPI Fortran interface does. It is used in the [`lammps()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} constructor of the LAMMPS Fortran module. Internally it converts the *f_comm* argument into a C-style MPI communicator with [`MPI_Comm_f2c()`{.docutils .literal .notranslate}]{.pre} and then calls [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal}.

    If for some reason the creation or initialization of the LAMMPS instance fails a null pointer is returned.

    *See also*

    :   [[`lammps_open_fortran()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_open_fortraniPPci "lammps_open_fortran"){.reference .internal}, [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal}

    Parameters[:]{.colon}

    :   - **argc** -- number of command-line arguments

        - **argv** -- list of command-line argument strings

        - **f_comm** -- Fortran style MPI communicator for this [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

    Returns[:]{.colon}

    :   pointer to new [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

[]{#_CPPv312lammps_closePv}[]{#_CPPv212lammps_closePv}[]{#lammps_close__voidP}[]{#library_8h_1a75570a623be78c153a75eb533a0b65d2 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_close]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv412lammps_closePv "Link to this definition"){.headerlink}\

:   Delete a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance created by lammps_open() or its variants.

    This function deletes the LAMMPS class instance pointed to by [`handle`{.docutils .literal .notranslate}]{.pre} that was created by one of the [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal} variants. It does **not** call [`MPI_Finalize()`{.docutils .literal .notranslate}]{.pre} to allow creating and deleting multiple LAMMPS instances concurrently or sequentially. See [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal} for a function performing this operation.

    Parameters[:]{.colon}

    :   **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

------------------------------------------------------------------------

[]{#_CPPv315lammps_mpi_initv}[]{#_CPPv215lammps_mpi_initv}[]{#lammps_mpi_init}[]{#library_8h_1afee0113d4bcf1cbe55a8f83176b39b59 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_mpi_init]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv415lammps_mpi_initv "Link to this definition"){.headerlink}\

:   Ensure the MPI environment is initialized.

    ::: versionadded
    [Added in version 18Sep2020.]{.versionmodified .added}
    :::

    The MPI standard requires that any MPI application must call [`MPI_Init()`{.docutils .literal .notranslate}]{.pre} exactly once before performing any other MPI function calls. This function checks, whether MPI is already initialized and calls [`MPI_Init()`{.docutils .literal .notranslate}]{.pre} in case it is not.

------------------------------------------------------------------------

[]{#_CPPv319lammps_mpi_finalizev}[]{#_CPPv219lammps_mpi_finalizev}[]{#lammps_mpi_finalize}[]{#library_8h_1a181557f91cb6d49ba67083a51cf110dc .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_mpi_finalize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv419lammps_mpi_finalizev "Link to this definition"){.headerlink}\

:   Shut down the MPI infrastructure.

    ::: versionadded
    [Added in version 18Sep2020.]{.versionmodified .added}
    :::

    The MPI standard requires that any MPI application calls [`MPI_Finalize()`{.docutils .literal .notranslate}]{.pre} before exiting. Even if a calling program does not do any MPI calls, MPI is still initialized internally to avoid errors accessing any MPI functions. This function should then be called right before exiting the program to wait until all (parallel) tasks are completed and then MPI is cleanly shut down. After calling this function no more MPI calls may be made.

    *See also*

    :   [[`lammps_kokkos_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_kokkos_finalizev "lammps_kokkos_finalize"){.reference .internal}, [[`lammps_python_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_python_finalizev "lammps_python_finalize"){.reference .internal}, [[`lammps_plugin_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_plugin_finalizev "lammps_plugin_finalize"){.reference .internal}

------------------------------------------------------------------------

[]{#_CPPv322lammps_kokkos_finalizev}[]{#_CPPv222lammps_kokkos_finalizev}[]{#lammps_kokkos_finalize}[]{#library_8h_1a295c98b87692b72b5bf594e7b291905b .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_kokkos_finalize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv422lammps_kokkos_finalizev "Link to this definition"){.headerlink}\

:   Shut down the Kokkos library environment.

    ::: versionadded
    [Added in version 2Jul2021.]{.versionmodified .added}
    :::

    The Kokkos library may only be initialized once during the execution of a process. This is done automatically the first time Kokkos functionality is used. This requires that the Kokkos environment must be explicitly shut down after any LAMMPS instance using it is closed (to release associated resources). After calling this function no Kokkos functionality may be used.

    *See also*

    :   [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal}, [[`lammps_python_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_python_finalizev "lammps_python_finalize"){.reference .internal}, [[`lammps_plugin_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_plugin_finalizev "lammps_plugin_finalize"){.reference .internal}

------------------------------------------------------------------------

[]{#_CPPv322lammps_python_finalizev}[]{#_CPPv222lammps_python_finalizev}[]{#lammps_python_finalize}[]{#library_8h_1a5d625667e3988ecae35e94490cb5aa8f .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_python_finalize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv422lammps_python_finalizev "Link to this definition"){.headerlink}\

:   Clear the embedded Python environment

    ::: versionadded
    [Added in version 20Sep2021.]{.versionmodified .added}
    :::

    This function resets and clears an embedded Python environment by calling the [Py_Finalize() function](https://docs.python.org/3/c-api/init.html#c.Py_FinalizeEx){.reference .external} of the embedded Python library, if enabled. This call would free up all allocated resources and release loaded shared objects.

    However, this is **not** done when a LAMMPS instance is deleted because a) LAMMPS may have been used through the Python module and thus the Python interpreter is external and not embedded into LAMMPS and therefore may not be reset by LAMMPS b) some Python modules and extensions, most notably NumPy, are not compatible with being initialized multiple times, which would happen if additional LAMMPS instances using Python would be created *after* after calling Py_Finalize().

    This function can be called to explicitly clear the Python environment in case it is safe to do so.

    *See also*

    :   [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal}, [[`lammps_kokkos_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_kokkos_finalizev "lammps_kokkos_finalize"){.reference .internal}, [[`lammps_plugin_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_plugin_finalizev "lammps_plugin_finalize"){.reference .internal}

------------------------------------------------------------------------

[]{#_CPPv322lammps_plugin_finalizev}[]{#_CPPv222lammps_plugin_finalizev}[]{#lammps_plugin_finalize}[]{#library_8h_1af862521905223dac33c7e5bfb331d57b .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_plugin_finalize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv422lammps_plugin_finalizev "Link to this definition"){.headerlink}\

:   Unload all plugins and release the corresponding DSO handles

    ::: versionadded
    [Added in version 12Jun2025.]{.versionmodified .added}
    :::

    This function clears the list of all loaded plugins and closes the corresponding DSO handles and releases the imported executable code.

    However, this is **not** done when a LAMMPS instance is deleted because plugins and their shared objects are global properties.

    This function can be called to explicitly clear out all loaded plugins in case it is safe to do so.

    *See also*

    :   [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal}, [[`lammps_kokkos_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_kokkos_finalizev "lammps_kokkos_finalize"){.reference .internal}, [[`lammps_python_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_python_finalizev "lammps_python_finalize"){.reference .internal}

------------------------------------------------------------------------

[]{#_CPPv312lammps_errorPviPKc}[]{#_CPPv212lammps_errorPviPKc}[]{#lammps_error__voidP.i.cCP}[]{#library_8h_1ad365a1950c1e4e6bf21e414cab86a57a .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_error]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[error_type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[error_text]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv412lammps_errorPviPKc "Link to this definition"){.headerlink}\

:   Call a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} Error class function

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function is a wrapper around functions in the [`Error`{.docutils .literal .notranslate}]{.pre} to print an error message and then stop LAMMPS.

    The *error_type* parameter selects which function to call. It is a sum of constants from [`_LMP_ERROR_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}. If the value does not match any valid combination of constants a warning is printed and the function returns.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **error_type** -- parameter to select function in the Error class

        - **error_text** -- error message
:::::
::::::
:::::::

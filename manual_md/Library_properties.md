::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#system-properties .section}
# [1.1.3. ]{.section-number}System properties[](#system-properties "Link to this heading"){.headerlink}

This section documents the following functions:

- [[`lammps_get_natoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv417lammps_get_natomsPv "lammps_get_natoms"){.reference .internal}

- [[`lammps_get_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv417lammps_get_thermoPvPKc "lammps_get_thermo"){.reference .internal}

- [[`lammps_last_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_last_thermoPvPKci "lammps_last_thermo"){.reference .internal}

- [[`lammps_extract_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_extract_boxPvPdPdPdPdPdPiPi "lammps_extract_box"){.reference .internal}

- [[`lammps_reset_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv416lammps_reset_boxPvPdPdddd "lammps_reset_box"){.reference .internal}

- [[`lammps_memory_usage()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_memory_usagePvPd "lammps_memory_usage"){.reference .internal}

- [[`lammps_get_mpi_comm()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_get_mpi_commPv "lammps_get_mpi_comm"){.reference .internal}

- [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal}

- [[`lammps_extract_global_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv430lammps_extract_global_datatypePvPKc "lammps_extract_global_datatype"){.reference .internal}

- [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal}

- [[`lammps_extract_pair_dimension()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_extract_pair_dimensionPvPKc "lammps_extract_pair_dimension"){.reference .internal}

- [[`lammps_extract_pair()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_extract_pairPvPKc "lammps_extract_pair"){.reference .internal}

- [[`lammps_map_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv415lammps_map_atomPvPKv "lammps_map_atom"){.reference .internal}

------------------------------------------------------------------------

The library interface allows the extraction of different kinds of information about the active simulation instance and also - in some cases - to apply modifications to it. This enables combining of a LAMMPS simulation with other processing and simulation methods computed by the calling code, or by another code that is coupled to LAMMPS via the library interface. In some cases the data returned is direct reference to the original data inside LAMMPS, cast to a void pointer. In that case the data needs to be cast to a suitable pointer for the calling program to access it, and you may need to know the correct dimensions and lengths. This also means you can directly change those value(s) from the calling program (e.g., to modify atom positions). Of course, changing values should be done with care. When accessing per-atom data, please note that these data are the per-processor **local** data and are indexed accordingly. Per-atom data can change sizes and ordering at every neighbor list rebuild or atom sort event as atoms migrate between subdomains and processors.

:::: {.highlight-c .notranslate}
::: highlight
    #include "library.h"
    #include <stdio.h>

    int main(int argc, char **argv)
    {
      void *handle;
      int i;

      handle = lammps_open_no_mpi(0, NULL, NULL);
      lammps_file(handle,"in.sysinit");
      printf("Running a simulation with %g atoms.\n",
             lammps_get_natoms(handle));

      printf(" %d local and %d ghost atoms. %d atom types\n",
             lammps_extract_setting(handle,"nlocal"),
             lammps_extract_setting(handle,"nghost"),
             lammps_extract_setting(handle,"ntypes"));

      double  *dt = (double *)lammps_extract_global(handle,"dt");
      printf("Changing timestep from %g to 0.5\n", *dt);
      *dt = 0.5;

      lammps_command(handle,"run 1000 post no");

      for (i=0; i < 10; ++i) {
        lammps_command(handle,"run 100 pre no post no");
        printf("PE = %g\nKE = %g\n",
               lammps_get_thermo(handle,"pe"),
               lammps_get_thermo(handle,"ke"));
      }
      lammps_close(handle);
      return 0;
    }
:::
::::

------------------------------------------------------------------------

[]{#_CPPv317lammps_get_natomsPv}[]{#_CPPv217lammps_get_natomsPv}[]{#lammps_get_natoms__voidP}[]{#library_8h_1aa7d4ad0dc261c21fa41cffa38ea3ac21 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[lammps_get_natoms]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv417lammps_get_natomsPv "Link to this definition"){.headerlink}\

:   Return the total number of atoms in the system.

    This number may be very large when running large simulations across multiple processes. Depending on compile time choices, LAMMPS may be using either 32-bit or a 64-bit integer to store this number. For portability this function returns thus a double precision floating point number, which can represent up to a 53-bit signed integer exactly ([\\(\\approx 10\^{16}\\)]{.math .notranslate .nohighlight}).

    As an alternative, you can use [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal} and cast the resulting pointer to an integer pointer of the correct size and dereference it. The size of that integer (in bytes) can be queried by calling [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal} to return the size of a [`bigint`{.docutils .literal .notranslate}]{.pre} integer.

    ::: versionchanged
    [Changed in version 18Sep2020: ]{.versionmodified .changed}The type of the return value was changed from [`int`{.docutils .literal .notranslate}]{.pre} to [`double`{.docutils .literal .notranslate}]{.pre} to accommodate reporting atom counts for larger systems that would overflow a 32-bit int without having to depend on a 64-bit bit integer type definition.
    :::

    Parameters[:]{.colon}

    :   **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

    Returns[:]{.colon}

    :   total number of atoms or 0 if value is too large

------------------------------------------------------------------------

[]{#_CPPv317lammps_get_thermoPvPKc}[]{#_CPPv217lammps_get_thermoPvPKc}[]{#lammps_get_thermo__voidP.cCP}[]{#library_8h_1a5f54fbac6f7be9c20605c0faf71ec77a .target}[[double]{.pre}]{.kt}[ ]{.w}[[[lammps_get_thermo]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[keyword]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv417lammps_get_thermoPvPKc "Link to this definition"){.headerlink}\

:   Evaluate a thermo keyword.

    This function returns the current value of a [[thermo keyword]{.doc}]thermo_style.md){.reference .internal}. Unlike [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal} it does not give access to the storage of the desired data but returns its value as a [`double`{.docutils .literal .notranslate}]{.pre}, so it can also return information that is computed on-the-fly. Use [[`lammps_last_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_last_thermoPvPKci "lammps_last_thermo"){.reference .internal} to get access to the cached data from the last thermo output.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **keyword** -- string with the name of the thermo keyword

    Returns[:]{.colon}

    :   value of the requested thermo property or 0.0

------------------------------------------------------------------------

[]{#_CPPv318lammps_last_thermoPvPKci}[]{#_CPPv218lammps_last_thermoPvPKci}[]{#lammps_last_thermo__voidP.cCP.i}[]{#library_8h_1a3d51693ba1f7f0cb5b703b1ddead146a .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_last_thermo]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[what]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[index]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv418lammps_last_thermoPvPKci "Link to this definition"){.headerlink}\

:   Access cached data from last thermo output

    ::: versionadded
    [Added in version 15Jun2023.]{.versionmodified .added}
    :::

    This function provides access to cached data from the last thermo output. This differs from [[`lammps_get_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv417lammps_get_thermoPvPKc "lammps_get_thermo"){.reference .internal} in that it does **not** trigger an evaluation. Instead it provides direct access to a read-only location of the last thermo output data and the corresponding keyword strings. How to handle the return value depends on the value of the *what* argument string. When accessing the data from a concurrent thread while LAMMPS is running, the cache needs to be locked first and then unlocked after the data is obtained, so that the data is not corrupted while reading in case LAMMPS wants to update it at the same time. Outside of a run, the lock/unlock calls have no effect.

    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | Value of *what* | Description of return value                                                                                                | Data type                                | Uses index |
    +=================+============================================================================================================================+==========================================+============+
    | setup           | 1 if setup is not completed and thus thermo data invalid, 0 otherwise                                                      | pointer to int                           | no         |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | line            | line number (0-based) of current line in current file or buffer                                                            | pointer to int                           | no         |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | imagename       | file name of the last [[dump image]{.doc}]dump_image.md){.reference .internal} file written                             | pointer to 0-terminated const char array | no         |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | step            | timestep when the last thermo output was generated or -1                                                                   | pointer to bigint                        | no         |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | num             | number of fields in thermo output                                                                                          | pointer to int                           | no         |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | keyword         | column keyword for thermo output                                                                                           | pointer to 0-terminated const char array | yes        |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | type            | data type of thermo output column; see [`_LMP_DATATYPE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre} | pointer to int                           | yes        |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | data            | actual field data for column                                                                                               | pointer to int, int64_t or double        | yes        |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | lock            | acquires lock to thermo data cache                                                                                         | NULL pointer                             | no         |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+
    | unlock          | releases lock to thermo data cache                                                                                         | NULL pointer                             | no         |
    +-----------------+----------------------------------------------------------------------------------------------------------------------------+------------------------------------------+------------+

    ::: {.admonition .note}
    Note

    The *type* property points to a static location that is reassigned with every call, so the returned pointer should be recast, dereferenced, and assigned immediately. Otherwise, its value may be changed with the next invocation of the function.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **what** -- string with the kind of data requested

        - **index** -- integer with index into data arrays, ignored for scalar data

    Returns[:]{.colon}

    :   pointer to location of requested data cast to void or NULL

------------------------------------------------------------------------

[]{#_CPPv318lammps_extract_boxPvPdPdPdPdPdPiPi}[]{#_CPPv218lammps_extract_boxPvPdPdPdPdPdPiPi}[]{#lammps_extract_box__voidP.doubleP.doubleP.doubleP.doubleP.doubleP.iP.iP}[]{#library_8h_1a5280ea3a305969261faa1a0258b9c7f9 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_extract_box]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[boxlo]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[boxhi]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[xy]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[yz]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[xz]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[pflags]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[boxflag]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv418lammps_extract_boxPvPdPdPdPdPdPiPi "Link to this definition"){.headerlink}\

:   Extract simulation box parameters.

    This function (re-)initializes the simulation box and boundary information and then assign the designated data to the locations in the pointers passed as arguments. Any argument (except the first) may be a NULL pointer and then will not be assigned.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **boxlo** -- pointer to 3 doubles where the lower box boundary is stored

        - **boxhi** -- pointer to 3 doubles where the upper box boundary is stored

        - **xy** -- pointer to a double where the xy tilt factor is stored

        - **yz** -- pointer to a double where the yz tilt factor is stored

        - **xz** -- pointer to a double where the xz tilt factor is stored

        - **pflags** -- pointer to 3 ints, set to 1 for periodic boundaries and 0 for non-periodic

        - **boxflag** -- pointer to an int, which is set to 1 if the box will be changed during a simulation by a fix and 0 if not.

------------------------------------------------------------------------

[]{#_CPPv316lammps_reset_boxPvPdPdddd}[]{#_CPPv216lammps_reset_boxPvPdPdddd}[]{#lammps_reset_box__voidP.doubleP.doubleP.double.double.double}[]{#library_8h_1ada23ca4aacdcc9b5991af9968e0369e8 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_reset_box]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[boxlo]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[boxhi]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[xy]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[yz]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[xz]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv416lammps_reset_boxPvPdPdddd "Link to this definition"){.headerlink}\

:   Reset simulation box parameters.

    This function sets the simulation box dimensions (upper and lower bounds and tilt factors) from the provided data and then re-initializes the box information and all derived settings. It may only be called before atoms are created.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **boxlo** -- pointer to 3 doubles containing the lower box boundary

        - **boxhi** -- pointer to 3 doubles containing the upper box boundary

        - **xy** -- xy tilt factor

        - **yz** -- yz tilt factor

        - **xz** -- xz tilt factor

------------------------------------------------------------------------

[]{#_CPPv319lammps_memory_usagePvPd}[]{#_CPPv219lammps_memory_usagePvPd}[]{#lammps_memory_usage__voidP.doubleP}[]{#library_8h_1ab1a5d06bc29dd1233cde03c857ff0821 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_memory_usage]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[meminfo]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419lammps_memory_usagePvPd "Link to this definition"){.headerlink}\

:   Get memory usage information

    ::: versionadded
    [Added in version 18Sep2020.]{.versionmodified .added}
    :::

    This function will retrieve memory usage information for the current LAMMPS instance or process. The *meminfo* buffer will be filled with 3 different numbers (if supported by the operating system). The first is the tally (in MBytes) of all large memory allocations made by LAMMPS. This is a lower boundary of how much memory is requested and does not account for memory allocated on the stack or allocations via [`new`{.docutils .literal .notranslate}]{.pre}. The second number is the current memory allocation of the current process as returned by a memory allocation reporting in the system library. The third number is the maximum amount of RAM (not swap) used by the process so far. If any of the two latter parameters is not supported by the operating system it will be set to zero.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **meminfo** -- buffer with space for at least 3 double to store data in.

------------------------------------------------------------------------

[]{#_CPPv319lammps_get_mpi_commPv}[]{#_CPPv219lammps_get_mpi_commPv}[]{#lammps_get_mpi_comm__voidP}[]{#library_8h_1a27501b4b00aa53f6621e996e3eeeb149 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_get_mpi_comm]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419lammps_get_mpi_commPv "Link to this definition"){.headerlink}\

:   Return current [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} world communicator as integer

    ::: versionadded
    [Added in version 18Sep2020.]{.versionmodified .added}
    :::

    This will take the LAMMPS "world" communicator and convert it to an integer using [`MPI_Comm_c2f()`{.docutils .literal .notranslate}]{.pre}, so it is equivalent to the corresponding MPI communicator in Fortran. This way it can be safely passed around between different programming languages. To convert it to the C language representation use [`MPI_Comm_f2c()`{.docutils .literal .notranslate}]{.pre}.

    If LAMMPS was compiled with MPI_STUBS, this function returns -1.

    *See also*

    :   [[`lammps_open_fortran()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv419lammps_open_fortraniPPci "lammps_open_fortran"){.reference .internal}

    Parameters[:]{.colon}

    :   **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

    Returns[:]{.colon}

    :   Fortran representation of the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} world communicator

------------------------------------------------------------------------

[]{#_CPPv322lammps_extract_settingPvPKc}[]{#_CPPv222lammps_extract_settingPvPKc}[]{#lammps_extract_setting__voidP.cCP}[]{#library_8h_1aec668a9f577e41295afb673f7edc99da .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_extract_setting]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[keyword]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422lammps_extract_settingPvPKc "Link to this definition"){.headerlink}\

:   Query [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} about global settings.

    This function will retrieve or compute global properties. In contrast to [[`lammps_get_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv417lammps_get_thermoPvPKc "lammps_get_thermo"){.reference .internal} this function returns an [`int`{.docutils .literal .notranslate}]{.pre}. The following tables list the currently supported keyword. If a keyword is not recognized, the function returns -1. The integer sizes functions may be called without a valid LAMMPS object handle (it is ignored).

    - [[Integer sizes]{.std .std-ref}](#extract-integer-sizes){.reference .internal}

    - [[Image masks]{.std .std-ref}](#extract-image-masks){.reference .internal}

    - [[System status]{.std .std-ref}](#extract-system-status){.reference .internal}

    - [[System sizes]{.std .std-ref}](#extract-system-sizes){.reference .internal}

    - [[Neighbor list settings]{.std .std-ref}](#extract-neighbor-settings){.reference .internal}

    - [[Atom style flags]{.std .std-ref}](#extract-atom-flags){.reference .internal}

    - [[Thermo settings]{.std .std-ref}](#extract-thermo-settings){.reference .internal}

    []{#extract-integer-sizes .target}

    **Integer sizes**

    +-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Keyword   | Description / Return value                                                                                                                                                          |
    +===========+=====================================================================================================================================================================================+
    | bigint    | size of the [`bigint`{.docutils .literal .notranslate}]{.pre} integer type, 4 or 8 bytes. Set at [[compile time]{.std .std-ref}]Build_settings.md#size){.reference .internal}.   |
    +-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | tagint    | size of the [`tagint`{.docutils .literal .notranslate}]{.pre} integer type, 4 or 8 bytes. Set at [[compile time]{.std .std-ref}]Build_settings.md#size){.reference .internal}.   |
    +-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | imageint  | size of the [`imageint`{.docutils .literal .notranslate}]{.pre} integer type, 4 or 8 bytes. Set at [[compile time]{.std .std-ref}]Build_settings.md#size){.reference .internal}. |
    +-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | MAX_GROUP | size of the bitmask for groups in bits, should be 32. Currently hard coded.                                                                                                         |
    +-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    []{#extract-image-masks .target}

    **Image masks**

    These settings are related to how LAMMPS stores and interprets periodic images. The values are used internally by the [[Fortran interface]{.doc}]Fortran.md){.reference .internal} and are not likely to be useful to users.

    +-----------+----------------------------------------------------------+
    | Keyword   | Description / Return value                               |
    +===========+==========================================================+
    | IMGMASK   | Bit-mask used to convert image flags to a single integer |
    +-----------+----------------------------------------------------------+
    | IMGMAX    | Maximum allowed image number for a particular atom       |
    +-----------+----------------------------------------------------------+
    | IMGBITS   | Bits used in image counts                                |
    +-----------+----------------------------------------------------------+
    | IMG2BITS  | Second bitmask used in image counts                      |
    +-----------+----------------------------------------------------------+

    []{#extract-system-status .target}

    **System status**

    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Keyword         | Description / Return value                                                                                                                                   |
    +=================+==============================================================================================================================================================+
    | dimension       | Number of dimensions: 2 or 3. See [[dimension command]{.doc}]dimension.md){.reference .internal}.                                                         |
    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | box_exist       | 1 if the simulation box is defined, 0 if not. See [[create_box command]{.doc}]create_box.md){.reference .internal}.                                       |
    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | kokkos_active   | 1 if the KOKKOS package is compiled in **and** activated, 0 if not. See [[KOKKOS package]{.doc}]Speed_kokkos.md){.reference .internal}.                   |
    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | kokkos_nthreads | Number of Kokkos threads per MPI process, 0 if Kokkos is not active. See [[KOKKOS package]{.doc}]Speed_kokkos.md){.reference .internal}.                  |
    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | kokkos_ngpus    | Number of Kokkos gpus per physical node, 0 if Kokkos is not active or no GPU support. See [[KOKKOS package]{.doc}]Speed_kokkos.md){.reference .internal}. |
    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | nthreads        | Number of requested OpenMP threads per MPI process for LAMMPS' execution                                                                                     |
    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | newton_bond     | 1 if Newton's 3rd law is applied to bonded interactions, 0 if not.                                                                                           |
    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | newton_pair     | 1 if Newton's 3rd law is applied to non-bonded interactions, 0 if not.                                                                                       |
    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | triclinic       | 1 if the the simulation box is triclinic, 0 if orthogonal. See [[change_box command]{.doc}]change_box.md){.reference .internal}.                          |
    +-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

    **Communication status**

    +----------------+--------------------------------------------------------------------------------------+
    | Keyword        | Description / Return value                                                           |
    +================+======================================================================================+
    | universe_rank  | MPI rank on LAMMPS' universe communicator (0 \<= universe_rank \< universe_size)     |
    +----------------+--------------------------------------------------------------------------------------+
    | universe_size  | Number of ranks on LAMMPS' universe communicator (world_size \<= universe_size)      |
    +----------------+--------------------------------------------------------------------------------------+
    | world_rank     | MPI rank on LAMMPS' world communicator (0 \<= world_rank \< world_size, = comm-\>me) |
    +----------------+--------------------------------------------------------------------------------------+
    | world_size     | Number of ranks on LAMMPS' world communicator (aka comm-\>nprocs)                    |
    +----------------+--------------------------------------------------------------------------------------+
    | comm_style     | communication style (0 = BRICK, 1 = TILED)                                           |
    +----------------+--------------------------------------------------------------------------------------+
    | comm_layout    | communication layout (0 = LAYOUT_UNIFORM, 1 = LAYOUT_NONUNIFORM, 2 = LAYOUT_TILED)   |
    +----------------+--------------------------------------------------------------------------------------+
    | comm_mode      | communication mode (0 = SINGLE, 1 = MULTI)                                           |
    +----------------+--------------------------------------------------------------------------------------+
    | ghost_velocity | whether velocities are communicated for ghost atoms (0 = no, 1 = yes)                |
    +----------------+--------------------------------------------------------------------------------------+

    []{#extract-system-sizes .target}

    **System sizes**

    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | Keyword           | Description / Return value                                                                                         |
    +===================+====================================================================================================================+
    | nlocal            | number of "owned" atoms of the current MPI rank.                                                                   |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | nghost            | number of "ghost" atoms of the current MPI rank.                                                                   |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | nall              | number of all "owned" and "ghost" atoms of the current MPI rank.                                                   |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | nmax              | maximum of nlocal+nghost across all MPI ranks (for per-atom data array size).                                      |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | ntypes            | number of atom types                                                                                               |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | nbondtypes        | number of bond types                                                                                               |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | nangletypes       | number of angle types                                                                                              |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | ndihedraltypes    | number of dihedral types                                                                                           |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | nimpropertypes    | number of improper types                                                                                           |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | bond_per_atom     | size of per-atom bond data arrays                                                                                  |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | angle_per_atom    | size of per-atom angle data arrays                                                                                 |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | dihedral_per_atom | size of per-atom dihedral data arrays                                                                              |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | improper_per_atom | size of per-atom improper data arrays                                                                              |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | maxspecial        | size of per-atom special data array                                                                                |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | nellipsoids       | number of atoms that have ellipsoid data                                                                           |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | nlines            | number of atoms that have line data (see [[pair style line/lj]{.doc}]pair_line_lj.md){.reference .internal})    |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | ntris             | number of atoms that have triangle data (see [[pair style tri/lj]{.doc}]pair_tri_lj.md){.reference .internal})  |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+
    | nbodies           | number of atoms that have body data (see [[the Body particle HowTo]{.doc}]Howto_body.md){.reference .internal}) |
    +-------------------+--------------------------------------------------------------------------------------------------------------------+

    []{#extract-neighbor-settings .target}

    **Neighbor list settings**

    +------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | neigh_every      | neighbor lists are rebuild every this many steps                                                                                            |
    +==================+=============================================================================================================================================+
    | neigh_delay      | neighbor lists are rebuild delayed this many steps                                                                                          |
    +------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | neigh_dist_check | 0 if always rebuild, 1 rebuild after 1/2 skin                                                                                               |
    +------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | neigh_ago        | neighbor lists were rebuilt this many steps ago                                                                                             |
    +------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | nbondlist        | number of entries in bondlist (get list with [[lammps_extract_global()]{.std .std-ref}](#extract-neighbor-lists){.reference .internal})     |
    +------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | nanglelist       | number of entries in anglelist (get list with [[lammps_extract_global()]{.std .std-ref}](#extract-neighbor-lists){.reference .internal})    |
    +------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | ndihedrallist    | number of entries in dihedrallist (get list with [[lammps_extract_global()]{.std .std-ref}](#extract-neighbor-lists){.reference .internal}) |
    +------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | nimproperlist    | number of entries in improperlist (get list with [[lammps_extract_global()]{.std .std-ref}](#extract-neighbor-lists){.reference .internal}) |
    +------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

    []{#extract-atom-flags .target}

    **Atom style flags**

    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Keyword        | Description / Return value                                                                                                                             |
    +================+========================================================================================================================================================+
    | molecule_flag  | 1 if the atom style includes molecular topology data. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                         |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | q_flag         | 1 if the atom style includes point charges. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                                   |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | mu_flag        | 1 if the atom style includes point dipoles. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                                   |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | rmass_flag     | 1 if the atom style includes per-atom masses, 0 if there are per-type masses. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}. |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | radius_flag    | 1 if the atom style includes a per-atom radius. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                               |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | body_flag      | 1 if the atom style describes body particles. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                                 |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ellipsoid_flag | 1 if the atom style describes extended particles that may be ellipsoidal. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.     |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | line_flag      | 1 if the atom style describes line particles. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                                 |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | tri_flag       | 1 if the atom style describes tri particles. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                                  |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | omega_flag     | 1 if the atom style can store per-atom rotational velocities. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                 |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | torque_flag    | 1 if the atom style can store per-atom torques. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                               |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | angmom_flag    | 1 if the atom style can store per-atom angular momentum. See [[atom_style command]{.doc}]atom_style.md){.reference .internal}.                      |
    +----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

    []{#extract-thermo-settings .target}

    **Thermo settings**

    +--------------+----------------------------------------------------------------------------------------------------------------------+
    | Keyword      | Description / Return value                                                                                           |
    +==============+======================================================================================================================+
    | thermo_every | The current interval of thermo output. See [[thermo command]{.doc}]thermo.md){.reference .internal}.              |
    +--------------+----------------------------------------------------------------------------------------------------------------------+
    | thermo_norm  | 1 if the thermo output is normalized. See [[thermo_modify command]{.doc}]thermo_modify.md){.reference .internal}. |
    +--------------+----------------------------------------------------------------------------------------------------------------------+

    *See also*

    :   [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal}

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **keyword** -- string with the name of the thermo keyword

    Returns[:]{.colon}

    :   value of the queried setting or -1 if unknown

------------------------------------------------------------------------

[]{#_CPPv330lammps_extract_global_datatypePvPKc}[]{#_CPPv230lammps_extract_global_datatypePvPKc}[]{#lammps_extract_global_datatype__voidP.cCP}[]{#library_8h_1a7a5da49a662d7cc3e8eaa79d7cc344e0 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_extract_global_datatype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv430lammps_extract_global_datatypePvPKc "Link to this definition"){.headerlink}\

:   Get data type of internal global [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} variables or arrays.

    ::: versionadded
    [Added in version 18Sep2020.]{.versionmodified .added}
    :::

    This function returns an integer that encodes the data type of the global property with the specified name. See [`_LMP_DATATYPE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre} for valid values. Callers of [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal} can use this information to then decide how to cast the [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} pointer and access the data.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance (unused)

        - **name** -- string with the name of the extracted property

    Returns[:]{.colon}

    :   integer constant encoding the data type of the property or -1 if not found.

------------------------------------------------------------------------

[]{#_CPPv321lammps_extract_globalPvPKc}[]{#_CPPv221lammps_extract_globalPvPKc}[]{#lammps_extract_global__voidP.cCP}[]{#library_8h_1ae1abe908414c1dbb01548581f8fc74a9 .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_extract_global]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421lammps_extract_globalPvPKc "Link to this definition"){.headerlink}\

:   Get pointer to internal global [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} variables or arrays.

    This function returns a pointer to the location of some global property stored in one of the constituent classes of a LAMMPS instance. The returned pointer is cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} and needs to be cast to a pointer of the type that the entity represents. The pointers returned by this function are generally persistent; therefore it is not necessary to call the function again, unless a [[clear command]{.doc}]clear.md){.reference .internal} command is issued which wipes out and recreates the contents of the [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} class.

    Please also see [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal}, [[`lammps_get_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv417lammps_get_thermoPvPKc "lammps_get_thermo"){.reference .internal}, and [[`lammps_extract_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_extract_boxPvPdPdPdPdPdPiPi "lammps_extract_box"){.reference .internal}.

    The following tables list the supported names, their data types, length of the data area, and a short description. The data type can also be queried through calling [[`lammps_extract_global_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv430lammps_extract_global_datatypePvPKc "lammps_extract_global_datatype"){.reference .internal}. The [`bigint`{.docutils .literal .notranslate}]{.pre} type may be defined to be either an [`int`{.docutils .literal .notranslate}]{.pre} or an [`int64_t`{.docutils .literal .notranslate}]{.pre}. This is set at [[compile time]{.std .std-ref}]Build_settings.md#size){.reference .internal} of the LAMMPS library and can be queried through calling [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal}. The function [[`lammps_extract_global_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv430lammps_extract_global_datatypePvPKc "lammps_extract_global_datatype"){.reference .internal} will directly report the "native" data type. The following tables are provided:

    - [[Timestep settings]{.std .std-ref}](#extract-timestep-settings){.reference .internal}

    - [[Simulation box settings]{.std .std-ref}](#extract-box-settings){.reference .internal}

    - [[System property settings]{.std .std-ref}](#extract-system-settings){.reference .internal}

    - [[Neighbor topology data]{.std .std-ref}](#extract-neighbor-lists){.reference .internal}

    - [[Energy and virial tally settings]{.std .std-ref}](#extract-tally-settings){.reference .internal}

    - [[Git revision and version settings]{.std .std-ref}](#extract-git-settings){.reference .internal}

    - [[Unit settings]{.std .std-ref}](#extract-unit-settings){.reference .internal}

    []{#extract-timestep-settings .target}

    **Timestep settings**

    +--------------+--------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Name         | Type   | Length                                              | Description                                                                                                                                            |
    +==============+========+=====================================================+========================================================================================================================================================+
    | dt           | double | 1                                                   | length of the time step. See [[timestep command]{.doc}]timestep.md){.reference .internal}.                                                          |
    +--------------+--------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ntimestep    | bigint | 1                                                   | current time step number. See [[reset_timestep command]{.doc}]reset_timestep.md){.reference .internal}.                                             |
    +--------------+--------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | atime        | double | 1                                                   | accumulated simulation time in time units.                                                                                                             |
    +--------------+--------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | atimestep    | bigint | 1                                                   | the number of the timestep when "atime" was last updated.                                                                                              |
    +--------------+--------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | respa_levels | int    | 1                                                   | [\\(N\_{respa}\\)]{.math .notranslate .nohighlight} = number of r-RESPA levels. See [[run_style command]{.doc}]run_style.md){.reference .internal}. |
    +--------------+--------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
    | respa_dt     | double | [\\(N\_{respa}\\)]{.math .notranslate .nohighlight} | length of the time steps with r-RESPA. See [[run_style command]{.doc}]run_style.md){.reference .internal}.                                          |
    +--------------+--------+-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

    []{#extract-box-settings .target}

    **Simulation box settings**

    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | Name         | Type   | Length | Description                                                                                                                   |
    +==============+========+========+===============================================================================================================================+
    | boxlo        | double | 3      | lower box boundaries in x-, y-, and z-direction; see [[create_box command]{.doc}]create_box.md){.reference .internal}.     |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | boxhi        | double | 3      | lower box boundaries in x-, y-, and z-direction; see [[create_box command]{.doc}]create_box.md){.reference .internal}.     |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | boxxlo       | double | 1      | lower box boundary in x-direction; see [[create_box command]{.doc}]create_box.md){.reference .internal}.                   |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | boxxhi       | double | 1      | upper box boundary in x-direction; see [[create_box command]{.doc}]create_box.md){.reference .internal}.                   |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | boxylo       | double | 1      | lower box boundary in y-direction; see [[create_box command]{.doc}]create_box.md){.reference .internal}.                   |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | boxyhi       | double | 1      | upper box boundary in y-direction; see [[create_box command]{.doc}]create_box.md){.reference .internal}.                   |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | boxzlo       | double | 1      | lower box boundary in z-direction; see [[create_box command]{.doc}]create_box.md){.reference .internal}.                   |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | boxzhi       | double | 1      | upper box boundary in z-direction; see [[create_box command]{.doc}]create_box.md){.reference .internal}.                   |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | sublo        | double | 3      | subbox lower boundaries in x-, y-, and z-direction                                                                            |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | subhi        | double | 3      | subbox upper boundaries in x-, y-, and z-direction                                                                            |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | sublo_lambda | double | 3      | subbox lower boundaries in fractional coordinates (for triclinic cells only)                                                  |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | subhi_lambda | double | 3      | subbox upper boundaries in fractional coordinates (for triclinic cells only)                                                  |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | periodicity  | int    | 3      | 0 if non-periodic, 1 if periodic for x, y, and z; see [[boundary command]{.doc}]boundary.md){.reference .internal}.        |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | triclinic    | int    | 1      | 1 if box is triclinic, 0 if orthogonal; see [[change_box command]{.doc}]change_box.md){.reference .internal}.              |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | xy           | double | 1      | triclinic tilt factor; see [[Triclinic (non-orthogonal) simulation boxes]{.doc}]Howto_triclinic.md){.reference .internal}. |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | yz           | double | 1      | triclinic tilt factor; see [[Triclinic (non-orthogonal) simulation boxes]{.doc}]Howto_triclinic.md){.reference .internal}. |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | xz           | double | 1      | triclinic tilt factor; see [[Triclinic (non-orthogonal) simulation boxes]{.doc}]Howto_triclinic.md){.reference .internal}. |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | xlattice     | double | 1      | lattice spacing in x-direction; see [[lattice command]{.doc}]lattice.md){.reference .internal}.                            |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | ylattice     | double | 1      | lattice spacing in y-direction; see [[lattice command]{.doc}]lattice.md){.reference .internal}.                            |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | zlattice     | double | 1      | lattice spacing in z-direction; see [[lattice command]{.doc}]lattice.md){.reference .internal}.                            |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+
    | procgrid     | int    | 3      | processor count in x-, y-, and z- direction; see [[processors command]{.doc}]processors.md){.reference .internal}.         |
    +--------------+--------+--------+-------------------------------------------------------------------------------------------------------------------------------+

    []{#extract-system-settings .target}

    **System property settings**

    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Name           | Type       | Length   | Description                                                                                                                                                                                                  |
    +================+============+==========+==============================================================================================================================================================================================================+
    | natoms         | bigint     | 1        | total number of atoms in the simulation.                                                                                                                                                                     |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | nbonds         | bigint     | 1        | total number of bonds in the simulation.                                                                                                                                                                     |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | nangles        | bigint     | 1        | total number of angles in the simulation.                                                                                                                                                                    |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ndihedrals     | bigint     | 1        | total number of dihedrals in the simulation.                                                                                                                                                                 |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | nimpropers     | bigint     | 1        | total number of impropers in the simulation.                                                                                                                                                                 |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | nlocal         | int        | 1        | number of "owned" atoms of the current MPI rank.                                                                                                                                                             |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | nghost         | int        | 1        | number of "ghost" atoms of the current MPI rank.                                                                                                                                                             |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | nmax           | int        | 1        | maximum of nlocal+nghost across all MPI ranks (for per-atom data array size).                                                                                                                                |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ntypes         | int        | 1        | number of atom types                                                                                                                                                                                         |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | special_lj     | double     | 4        | special [[pair weighting factors]{.doc}]special_bonds.md){.reference .internal} for LJ interactions (first element is always 1.0)                                                                         |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | special_coul   | double     | 4        | special [[pair weighting factors]{.doc}]special_bonds.md){.reference .internal} for Coulomb interactions (first element is always 1.0)                                                                    |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | map_style      | int        | 1        | [[atom map setting]{.doc}]atom_modify.md){.reference .internal}: 0 = none, 1 = array, 2 = hash, 3 = yes                                                                                                   |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | map_tag_max    | int/bigint | 1        | largest atom ID that can be mapped to a local index (bigint with -DLAMMPS_BIGBIG)                                                                                                                            |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | sametag        | int        | variable | index of next local atom with the same ID in ascending order. -1 signals end.                                                                                                                                |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | sortfreq       | int        | 1        | frequency of atom sorting. 0 means sorting is off.                                                                                                                                                           |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | nextsort       | bigint     | 1        | timestep when atoms are sorted next                                                                                                                                                                          |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | q_flag         | int        | 1        | **deprecated**. Use [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal} instead. |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | atom_style     | char \*    | 1        | string with the current atom style.                                                                                                                                                                          |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | pair_style     | char \*    | 1        | string with the current pair style.                                                                                                                                                                          |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | bond_style     | char \*    | 1        | string with the current bond style.                                                                                                                                                                          |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | angle_style    | char \*    | 1        | string with the current angle style.                                                                                                                                                                         |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | dihedral_style | char \*    | 1        | string with the current dihedral style.                                                                                                                                                                      |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | improper_style | char \*    | 1        | string with the current improper style.                                                                                                                                                                      |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | kspace_style   | char \*    | 1        | string with the current KSpace style.                                                                                                                                                                        |
    +----------------+------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    []{#extract-neighbor-lists .target}

    **Neighbor topology data**

    Get length of lists with [[lammps_extract_setting()]{.std .std-ref}](#extract-neighbor-settings){.reference .internal}.

    +--------------------+--------+---------------+------------------------------------------------------+
    | Name               | Type   | Length        | Description                                          |
    +====================+========+===============+======================================================+
    | neigh_skin         | double | 1             | neighbor list skin                                   |
    +--------------------+--------+---------------+------------------------------------------------------+
    | neigh_cutmin       | double | 1             | minimum neighbor cutoff across all type pairs        |
    +--------------------+--------+---------------+------------------------------------------------------+
    | neigh_cutmax       | double | 1             | maximum neighbor cutoff across all type pairs        |
    +--------------------+--------+---------------+------------------------------------------------------+
    | neigh_bondlist     | 2d int | nbondlist     | list of bonds (atom1, atom2, type)                   |
    +--------------------+--------+---------------+------------------------------------------------------+
    | neigh_anglelist    | 2d int | nanglelist    | list of angles (atom1, atom2, atom3, type)           |
    +--------------------+--------+---------------+------------------------------------------------------+
    | neigh_dihedrallist | 2d int | ndihedrallist | list of dihedrals (atom1, atom2, atom3, atom4, type) |
    +--------------------+--------+---------------+------------------------------------------------------+
    | neigh_improperlist | 2d int | nimproperlist | list of impropers (atom1, atom2, atom3, atom4, type) |
    +--------------------+--------+---------------+------------------------------------------------------+

    []{#extract-tally-settings .target}

    **Energy and virial tally settings**

    +--------------+--------+----------+----------------------------------------+
    | Name         | Type   | Length   | Description                            |
    +==============+========+==========+========================================+
    | eflag_global | bigint | 1        | timestep global energy is tallied on   |
    +--------------+--------+----------+----------------------------------------+
    | eflag_atom   | bigint | 1        | timestep per-atom energy is tallied on |
    +--------------+--------+----------+----------------------------------------+
    | vflag_global | bigint | 1        | timestep global virial is tallied on   |
    +--------------+--------+----------+----------------------------------------+
    | vflag_atom   | bigint | 1        | timestep per-atom virial is tallied on |
    +--------------+--------+----------+----------------------------------------+

    []{#extract-git-settings .target}

    **Git revision and version settings**

    +----------------+---------------+--------+------------------------------------------+
    | Name           | Type          | Length | Description                              |
    +================+===============+========+==========================================+
    | git_commit     | const char \* | 1      | Git commit hash for the LAMMPS version.  |
    +----------------+---------------+--------+------------------------------------------+
    | git_branch     | const char \* | 1      | Git branch for the LAMMPS version.       |
    +----------------+---------------+--------+------------------------------------------+
    | git_descriptor | const char \* | 1      | Combined descriptor for the git revision |
    +----------------+---------------+--------+------------------------------------------+
    | lammps_version | const char \* | 1      | LAMMPS version string.                   |
    +----------------+---------------+--------+------------------------------------------+

    []{#extract-unit-settings .target}

    **Unit settings**

    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Name        | Type    | Length | Description                                                                                                                                                                            |
    +=============+=========+========+========================================================================================================================================================================================+
    | units       | char \* | 1      | string with the current unit style. See [[units command]{.doc}]units.md){.reference .internal}.                                                                                     |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | boltz       | double  | 1      | value of the "boltz" constant. See [[units command]{.doc}]units.md){.reference .internal}.                                                                                          |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | hplanck     | double  | 1      | value of the "hplanck" constant. See [[units command]{.doc}]units.md){.reference .internal}.                                                                                        |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | mvv2e       | double  | 1      | factor to convert [\\(\\frac{1}{2}mv\^2\\)]{.math .notranslate .nohighlight} for a particle to the current energy unit; See [[units command]{.doc}]units.md){.reference .internal}. |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ftm2v       | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | mv2d        | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | nktv2p      | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | qqr2e       | double  | 1      | factor to convert [\\(\\frac{q_i q_j}{r}\\)]{.math .notranslate .nohighlight} to energy units; See [[units command]{.doc}]units.md){.reference .internal}.                          |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | qe2f        | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | vxmu2f      | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | xxt2kmu     | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | dielectric  | double  | 1      | value of the dielectric constant. See [[dielectric command]{.doc}]dielectric.md){.reference .internal}.                                                                             |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | qqrd2e      | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | e_mass      | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | hhmrr2e     | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | mvh2r       | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | angstrom    | double  | 1      | constant to convert current length unit to angstroms; 1.0 for reduced (aka "lj") units. See [[units command]{.doc}]units.md){.reference .internal}.                                 |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | femtosecond | double  | 1      | constant to convert current time unit to femtoseconds; 1.0 for reduced (aka "lj") units                                                                                                |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | qelectron   | double  | 1      | (description missing) See [[units command]{.doc}]units.md){.reference .internal}.                                                                                                   |
    +-------------+---------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    ::: {.admonition .warning}
    Warning

    Modifying the data in the location pointed to by the returned pointer may lead to inconsistent internal data and thus may cause failures or crashes or bogus simulations. In general it is thus usually better to use a LAMMPS input command that sets or changes these parameters. Those will take care of all side effects and necessary updates of settings derived from such settings. Where possible, a reference to such a command or a relevant section of the manual is given below.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- string with the name of the extracted property

    Returns[:]{.colon}

    :   pointer (cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}) to the location of the requested property. NULL if name is not known.

------------------------------------------------------------------------

[]{#_CPPv329lammps_extract_pair_dimensionPvPKc}[]{#_CPPv229lammps_extract_pair_dimensionPvPKc}[]{#lammps_extract_pair_dimension__voidP.cCP}[]{#library_8h_1a8935ce652b4140c850625040c71db8c9 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_extract_pair_dimension]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv429lammps_extract_pair_dimensionPvPKc "Link to this definition"){.headerlink}\

:   Get data dimension of pair style data accessible via Pair::extract().

    ::: versionadded
    [Added in version 29Aug2024.]{.versionmodified .added}
    :::

    This function returns an integer that specified the dimensionality of the data that can be extracted from the current pair style with [`Pair::extract()`{.docutils .literal .notranslate}]{.pre}. Callers of [[`lammps_extract_pair()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_extract_pairPvPKc "lammps_extract_pair"){.reference .internal} can use this information to then decide how to cast the [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} pointer and access the data.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- string with the name of the extracted property

    Returns[:]{.colon}

    :   integer constant encoding the dimensionality of the extractable pair style property or -1 if not found.

------------------------------------------------------------------------

[]{#_CPPv319lammps_extract_pairPvPKc}[]{#_CPPv219lammps_extract_pairPvPKc}[]{#lammps_extract_pair__voidP.cCP}[]{#library_8h_1ab8743566147a6440851e8cc1239146da .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_extract_pair]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419lammps_extract_pairPvPKc "Link to this definition"){.headerlink}\

:   Get extract pair style data accessible via Pair::extract().

    ::: versionadded
    [Added in version 29Aug2024.]{.versionmodified .added}
    :::

    This function returns a pointer to data available from the current pair style with [`Pair::extract()`{.docutils .literal .notranslate}]{.pre}. The dimensionality of the returned pointer can be determined with [[`lammps_extract_pair_dimension()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_extract_pair_dimensionPvPKc "lammps_extract_pair_dimension"){.reference .internal}.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- string with the name of the extracted property

    Returns[:]{.colon}

    :   pointer (cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}) to the location of the requested property. NULL if name is not known.

------------------------------------------------------------------------

[]{#_CPPv315lammps_map_atomPvPKv}[]{#_CPPv215lammps_map_atomPvPKv}[]{#lammps_map_atom__voidP.voidCP}[]{#library_8h_1a40e85a5c09ff9cc7763d119fea9603ec .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_map_atom]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv415lammps_map_atomPvPKv "Link to this definition"){.headerlink}\

:   Map global atom ID to local atom index

    ::: versionadded
    [Added in version 27June2024.]{.versionmodified .added}
    :::

    This function returns an integer that corresponds to the local atom index for an atom with the global atom ID *id*. The atom ID is passed as a void pointer so that it can use the same interface for either a 32-bit or 64-bit tagint. The size of the tagint can be determined using [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal}.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **id** -- void pointer to the atom ID (of data type tagint, i.e. 32-bit or 64-bit integer)

    Returns[:]{.colon}

    :   local atom index or -1 if the atom is not found or no map exists
:::::
::::::
:::::::

::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::: {#the-liblammps-fortran-module .section}
# [1.3.1. ]{.section-number}The [`LIBLAMMPS`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} Fortran Module[](#the-liblammps-fortran-module "Link to this heading"){.headerlink}

The [`LIBLAMMPS`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} module provides an interface to call LAMMPS from Fortran. It is based on the LAMMPS C library interface and requires a fully Fortran 2003-compatible compiler to be compiled. It is designed to be self-contained and not require any support functions written in C, C++, or Fortran other than those in the C library interface and the LAMMPS Fortran module itself.

While C libraries have a defined binary interface (ABI) and can thus be used from multiple compiler versions from different vendors as long as they are compatible with the hosting operating system, the same is not true for Fortran programs. Thus, the LAMMPS Fortran module needs to be compiled alongside the code using it from the source code in [`fortran/lammps.f90`{.docutils .literal .notranslate}]{.pre} *and* with the same compiler used to build the rest of the Fortran code that interfaces to LAMMPS. When linking, you also need to [[link to the LAMMPS library]{.doc}]Build_link.md){.reference .internal}. A typical command for a simple program using the Fortran interface would be:

:::: {.highlight-bash .notranslate}
::: highlight
    mpifort -o testlib.x lammps.f90 testlib.f90 -L. -llammps
:::
::::

Please note that the MPI compiler wrapper is only required when the calling the library *from* an MPI-parallelized program. Otherwise, using the plain Fortran compiler (gfortran, ifort, flang, etc.) will suffice, since there are no direct references to MPI library features, definitions and subroutine calls; MPI communicators are referred to by their integer index representation as required by the Fortran MPI interface. It may be necessary to link to additional libraries, depending on how LAMMPS was configured and whether the LAMMPS library [[was compiled as a static or dynamic library]{.doc}]Build_link.md){.reference .internal}.

If the LAMMPS library itself has been compiled with MPI support, the resulting executable will be able to run LAMMPS in parallel with [`mpirun`{.docutils .literal .notranslate}]{.pre}, [`mpiexec`{.docutils .literal .notranslate}]{.pre}, or equivalent. This may be either on the "world" communicator or a sub-communicator created by the calling Fortran code. If, on the other hand, the LAMMPS library has been compiled **without** MPI support, each LAMMPS instance will run independently using just one processor.

Please also note that the order of the source files matters: the [`lammps.f90`{.docutils .literal .notranslate}]{.pre} file needs to be compiled first, since it provides the [`LIBLAMMPS`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} module that would need to be imported by the calling Fortran code in order to uses the Fortran interface. A working example can be found together with equivalent examples in C and C++ in the [`examples/COUPLE/simple`{.docutils .literal .notranslate}]{.pre} folder of the LAMMPS distribution.

::: {.note .admonition}
Fortran compiler compatibility

A fully Fortran 2003 compatible Fortran compiler is required. This means that currently only GNU Fortran 9 and later are compatible and thus the default compilers of Red Hat or CentOS 7 and Ubuntu 18.04 LTS and not compatible. Either newer compilers need to be installed or the Linux updated.
:::
::::::

------------------------------------------------------------------------

::::::: {#creating-or-deleting-a-lammps-object .section}
# [1.3.2. ]{.section-number}Creating or deleting a LAMMPS object[](#creating-or-deleting-a-lammps-object "Link to this heading"){.headerlink}

With the Fortran interface, the creation of a [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} instance is included in the constructor for creating the [`lammps()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} derived type. To import the definition of that type and its type-bound procedures, you need to add a [`USE`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`LIBLAMMPS`{.docutils .literal .notranslate}]{.pre} statement. Internally, it will call either [[`lammps_open_fortran()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv419lammps_open_fortraniPPci "lammps_open_fortran"){.reference .internal} or [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal} from the C library API to create the class instance. All arguments are optional and [[`lammps_mpi_init()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv415lammps_mpi_initv "lammps_mpi_init"){.reference .internal} will be called automatically if it is needed. Similarly, optional calls to [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal}, [[`lammps_kokkos_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_kokkos_finalizev "lammps_kokkos_finalize"){.reference .internal}, [[`lammps_python_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_python_finalizev "lammps_python_finalize"){.reference .internal}, and [[`lammps_plugin_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_plugin_finalizev "lammps_plugin_finalize"){.reference .internal} are integrated into the [`close()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} function and triggered with the optional logical argument set to [`.TRUE.`{.docutils .literal .notranslate}]{.pre}. Here is a simple example:

:::: {.highlight-fortran .notranslate}
::: highlight
    PROGRAM testlib
      USE LIBLAMMPS                 ! include the LAMMPS library interface
      IMPLICIT NONE
      TYPE(lammps) :: lmp           ! derived type to hold LAMMPS instance
      CHARACTER(LEN=12), PARAMETER :: args(3) = &
          [ CHARACTER(LEN=12) :: 'liblammps', '-log', 'none' ]

      ! create a LAMMPS instance (and initialize MPI)
      lmp = lammps(args)
      ! get and print numerical version code
      PRINT*, 'LAMMPS Version: ', lmp%version()
      ! delete LAMMPS instance (and shutdown MPI)
      CALL lmp%close(.TRUE.)
    END PROGRAM testlib
:::
::::

It is also possible to pass command-line flags from Fortran to C/C++ and thus make the resulting executable behave similarly to the standalone executable (it will ignore the -in/-i flag, though). This allows using the command-line to configure accelerator and suffix settings, configure screen and logfile output, or to set index style variables from the command-line and more. Here is a correspondingly adapted version of the previous example:

:::: {.highlight-fortran .notranslate}
::: highlight
    PROGRAM testlib2
      USE LIBLAMMPS                 ! include the LAMMPS library interface
      IMPLICIT NONE
      TYPE(lammps) :: lmp           ! derived type to hold LAMMPS instance
      CHARACTER(LEN=128), ALLOCATABLE :: command_args(:)
      INTEGER :: i, argc

      ! copy command-line flags to `command_args()`
      argc = COMMAND_ARGUMENT_COUNT()
      ALLOCATE(command_args(0:argc))
      DO i=0, argc
        CALL GET_COMMAND_ARGUMENT(i, command_args(i))
      END DO

      ! create a LAMMPS instance (and initialize MPI)
      lmp = lammps(command_args)
      ! get and print numerical version code
      PRINT*, 'Program name:   ', command_args(0)
      PRINT*, 'LAMMPS Version: ', lmp%version()
      ! delete LAMMPS instance (and shuts down MPI)
      CALL lmp%close(.TRUE.)
      DEALLOCATE(command_args)
    END PROGRAM testlib2
:::
::::
:::::::

------------------------------------------------------------------------

::::: {#executing-lammps-commands .section}
# [1.3.3. ]{.section-number}Executing LAMMPS commands[](#executing-lammps-commands "Link to this heading"){.headerlink}

Once a LAMMPS instance is created, it is possible to "drive" the LAMMPS simulation by telling LAMMPS to read commands from a file or to pass individual or multiple commands from strings or lists of strings. This is done similarly to how it is implemented in the [[C library interface]{.doc}]Library_execute.md){.reference .internal}. Before handing off the calls to the C library interface, the corresponding Fortran versions of the calls ([`file()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}, [`command()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}, [`commands_list()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}, and [`commands_string()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}) have to make copies of the strings passed as arguments so that they can be modified to be compatible with the requirements of strings in C without affecting the original strings. Those copies are automatically deleted after the functions return. Below is a small demonstration of the uses of the different functions.

:::: {.highlight-fortran .notranslate}
::: highlight
    PROGRAM testcmd
      USE LIBLAMMPS
      TYPE(lammps) :: lmp
      CHARACTER(LEN=512) :: cmds
      CHARACTER(LEN=40), ALLOCATABLE :: cmdlist(:)
      CHARACTER(LEN=10) :: trimmed
      INTEGER :: i

      lmp = lammps()
      CALL lmp%file('in.melt')
      CALL lmp%command('variable zpos index 1.0')
      ! define 10 groups of 10 atoms each
      ALLOCATE(cmdlist(10))
      DO i=1, 10
        WRITE(trimmed,'(I10)') 10*i
        WRITE(cmdlist(i),'(A,I1,A,I10,A,A)')       &
            'group g', i-1, ' id ', 10*(i-1)+1, ':', ADJUSTL(trimmed)
      END DO
      CALL lmp%commands_list(cmdlist)
      ! run multiple commands from multi-line string
      cmds = 'clear' // NEW_LINE('A') //                       &
          'region  box block 0 2 0 2 0 2' // NEW_LINE('A') //  &
          'create_box 1 box' // NEW_LINE('A') //               &
          'create_atoms 1 single 1.0 1.0 ${zpos}'
      CALL lmp%commands_string(cmds)
      CALL lmp%close(.TRUE.)
    END PROGRAM testcmd
:::
::::
:::::

------------------------------------------------------------------------

::::: {#accessing-system-properties .section}
# [1.3.4. ]{.section-number}Accessing system properties[](#accessing-system-properties "Link to this heading"){.headerlink}

The C library interface allows the [[extraction of different kinds of information]{.doc}]Library_properties.md){.reference .internal} about the active simulation instance and also---in some cases---to apply modifications to it, and the Fortran interface provides access to the same data using Fortran-style, C-interoperable data types. In some cases, the Fortran library interface makes pointers to internal LAMMPS data structures accessible; when accessing them through the library interfaces, special care is needed to avoid data corruption and crashes. Please see the documentation of the individual type-bound procedures for details.

Below is an example demonstrating some of the possible uses.

:::: {.highlight-fortran .notranslate}
::: highlight
    PROGRAM testprop
      USE LIBLAMMPS
      USE, INTRINSIC :: ISO_C_BINDING, ONLY : c_double, c_int64_t, c_int
      USE, INTRINSIC :: ISO_FORTRAN_ENV, ONLY : OUTPUT_UNIT
      TYPE(lammps) :: lmp
      INTEGER(KIND=c_int64_t), POINTER :: natoms, ntimestep, bval
      REAL(KIND=c_double), POINTER :: dt, dval
      INTEGER(KIND=c_int), POINTER :: nfield, typ, ival
      INTEGER(KIND=c_int) :: i
      CHARACTER(LEN=11) :: key
      REAL(KIND=c_double) :: pe, ke

      lmp = lammps()
      CALL lmp%file('in.sysinit')
      natoms = lmp%extract_global('natoms')
      WRITE(OUTPUT_UNIT,'(A,I0,A)') 'Running a simulation with ', natoms, ' atoms'
      WRITE(OUTPUT_UNIT,'(I0,A,I0,A,I0,A)') lmp%extract_setting('nlocal'), &
          ' local and ', lmp%extract_setting('nghost'), ' ghost atoms. ', &
          lmp%extract_setting('ntypes'), ' atom types'

      CALL lmp%command('run 2 post no')

      ntimestep = lmp%last_thermo('step', 0)
      nfield = lmp%last_thermo('num', 0)
      WRITE(OUTPUT_UNIT,'(A,I0,A,I0)') 'Last thermo output on step: ', ntimestep, &
          ',  number of fields: ', nfield
      DO i=1, nfield
          key = lmp%last_thermo('keyword',i)
          typ = lmp%last_thermo('type',i)
          IF (typ == lmp%dtype%i32) THEN
              ival = lmp%last_thermo('data',i)
              WRITE(OUTPUT_UNIT,*) key, ':', ival
          ELSE IF (typ == lmp%dtype%i64) THEN
              bval = lmp%last_thermo('data',i)
              WRITE(OUTPUT_UNIT,*) key, ':', bval
          ELSE IF (typ == lmp%dtype%r64) THEN
              dval = lmp%last_thermo('data',i)
              WRITE(OUTPUT_UNIT,*) key, ':', dval
          END IF
      END DO

      dt = lmp%extract_global('dt')
      ntimestep = lmp%extract_global('ntimestep')
      WRITE(OUTPUT_UNIT,'(A,I0,A,F4.1,A)') 'At step: ', ntimestep, &
          '  Changing timestep from', dt, ' to 0.5'
      dt = 0.5_c_double
      CALL lmp%command('run 2 post no')

      WRITE(OUTPUT_UNIT,'(A,I0)') 'At step: ', ntimestep
      pe = lmp%get_thermo('pe')
      ke = lmp%get_thermo('ke')
      WRITE(OUTPUT_UNIT,*) 'PE = ', pe
      WRITE(OUTPUT_UNIT,*) 'KE = ', ke

      CALL lmp%close(.TRUE.)
    END PROGRAM testprop
:::
::::
:::::

------------------------------------------------------------------------

:::::::: {#the-liblammps-module-api .section}
# [1.3.5. ]{.section-number}The [`LIBLAMMPS`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} module API[](#the-liblammps-module-api "Link to this heading"){.headerlink}

Below are the detailed descriptions of definitions and interfaces of the contents of the [`LIBLAMMPS`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} Fortran interface to LAMMPS.

*[type]{.pre} * [[lammps]{.pre}]{.sig-name .descname}[](#f/_/lammps "Link to this definition"){.headerlink}

:   Derived type that is the general class of the Fortran interface. It holds a reference to the [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} class instance to which any of the included calls are forwarded.

    Type fields[:]{.colon}

    :   - [% ]{.sig-name .descname}[handle]{.sig-name .descname} *\[c_ptr\]* :: reference to the LAMMPS class

        - [% ]{.sig-name .descname}[style]{.sig-name .descname} *\[type(lammps_style)\]* :: derived type to access lammps style constants

        - [% ]{.sig-name .descname}[type]{.sig-name .descname} *\[type(lammps_type)\]* :: derived type to access lammps type constants

        - [% ]{.sig-name .descname}[dtype]{.sig-name .descname} *\[type(lammps_dtype)\]* :: derived type to access lammps data type constants

        - [% ]{.sig-name .descname}[close]{.sig-name .descname} *\[subroutine\]* :: [`close()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[error]{.sig-name .descname} *\[subroutine\]* :: [`error()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[file]{.sig-name .descname} *\[subroutine\]* :: [`file()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[command]{.sig-name .descname} *\[subroutine\]* :: [`command()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[commands_list]{.sig-name .descname} *\[subroutine\]* :: [`commands_list()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[commands_string]{.sig-name .descname} *\[subroutine\]* :: [`commands_string()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[get_natoms]{.sig-name .descname} *\[function\]* :: [`get_natoms()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[get_thermo]{.sig-name .descname} *\[function\]* :: [`get_thermo()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[last_thermo]{.sig-name .descname} *\[function\]* :: [`last_thermo()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[extract_box]{.sig-name .descname} *\[subroutine\]* :: [`extract_box()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[reset_box]{.sig-name .descname} *\[subroutine\]* :: [`reset_box()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[memory_usage]{.sig-name .descname} *\[subroutine\]* :: [`memory_usage()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[get_mpi_comm]{.sig-name .descname} *\[function\]* :: [`get_mpi_comm()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[extract_setting]{.sig-name .descname} *\[function\]* :: [`extract_setting()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[extract_global]{.sig-name .descname} *\[function\]* :: [`extract_global()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[map_atom]{.sig-name .descname} *\[function\]* :: [`map_atom()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[extract_atom]{.sig-name .descname} *\[function\]* :: [`extract_atom()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[extract_compute]{.sig-name .descname} *\[function\]* :: [`extract_compute()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[extract_fix]{.sig-name .descname} *\[function\]* :: [`extract_fix()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[extract_variable]{.sig-name .descname} *\[function\]* :: [`extract_variable()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[set_variable]{.sig-name .descname} *\[subroutine\]* :: [`set_variable()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[set_string_variable]{.sig-name .descname} *\[subroutine\]* :: [`set_set_string_variable()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[set_internal_variable]{.sig-name .descname} *\[subroutine\]* :: [`set_internal_variable()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[eval]{.sig-name .descname} *\[function\]* :: [`eval()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[clearstep_compute]{.sig-name .descname} *\[subroutine\]* :: [`clearstep_compute()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[addstep_compute]{.sig-name .descname} *\[subroutine\]* :: [`addstep_compute()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[addstep_compute_all]{.sig-name .descname} *\[subroutine\]* :: [`addstep_compute_all()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather_atoms]{.sig-name .descname} *\[subroutine\]* :: [`gather_atoms()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather_atoms_concat]{.sig-name .descname} *\[subroutine\]* :: [`gather_atoms_concat()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather_atoms_subset]{.sig-name .descname} *\[subroutine\]* :: [`gather_atoms_subset()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[scatter_atoms]{.sig-name .descname} *\[subroutine\]* :: [`scatter_atoms()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[scatter_atoms_subset]{.sig-name .descname} *\[subroutine\]* :: [`scatter_atoms_subset()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather_bonds]{.sig-name .descname} *\[subroutine\]* :: [`gather_bonds()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather_angles]{.sig-name .descname} *\[subroutine\]* :: [`gather_angles()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather_dihedrals]{.sig-name .descname} *\[subroutine\]* :: [`gather_dihedrals()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather_impropers]{.sig-name .descname} *\[subroutine\]* :: [`gather_impropers()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather]{.sig-name .descname} *\[subroutine\]* :: [`gather()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather_concat]{.sig-name .descname} *\[subroutine\]* :: [`gather_concat()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[gather_subset]{.sig-name .descname} *\[subroutine\]* :: [`gather_subset()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[scatter]{.sig-name .descname} *\[subroutine\]* :: [`scatter()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[scatter_subset]{.sig-name .descname} *\[subroutine\]* :: [`scatter_subset()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[create_atoms]{.sig-name .descname} *\[subroutine\]* :: [`create_atoms()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[find_pair_neighlist]{.sig-name .descname} *\[function\]* :: [`find_pair_neighlist()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[find_fix_neighlist]{.sig-name .descname} *\[function\]* :: [`find_fix_neighlist()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[find_compute_neighlist]{.sig-name .descname} *\[function\]* :: [`find_compute_neighlist()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[neighlist_num_elements]{.sig-name .descname} *\[function\]* :: [`neighlist_num_elements()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[neighlist_element_neighbors]{.sig-name .descname} *\[subroutine\]* :: [`neighlist_element_neighbors()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[version]{.sig-name .descname} *\[function\]* :: [`version()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[get_os_info]{.sig-name .descname} *\[subroutine\]* :: [`get_os_info()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_has_mpi_support]{.sig-name .descname} *\[function\]* :: [`config_has_mpi_support()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_has_omp_support]{.sig-name .descname} *\[function\]* :: [`config_has_omp_support()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_has_gzip_support]{.sig-name .descname} *\[function\]* :: [`config_has_gzip_support()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_has_png_support]{.sig-name .descname} *\[function\]* :: [`config_has_png_support()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_has_jpeg_support]{.sig-name .descname} *\[function\]* :: [`config_has_jpeg_support()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_has_ffmpeg_support]{.sig-name .descname} *\[function\]* :: [`config_has_ffmpeg_support()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_has_exceptions]{.sig-name .descname} *\[function\]* :: [`config_has_exceptions()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_has_package]{.sig-name .descname} *\[function\]* :: [`config_has_package()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_package_count]{.sig-name .descname} *\[function\]* :: [`config_package_count()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_package_name]{.sig-name .descname} *\[function\]* :: [`config_package_name()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[installed_packages]{.sig-name .descname} *\[subroutine\]* :: [`installed_packages()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[config_accelerator]{.sig-name .descname} *\[function\]* :: [`config_accelerator()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[has_gpu_device]{.sig-name .descname} *\[function\]* :: [`has_gpu_device()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[get_gpu_device_info]{.sig-name .descname} *\[subroutine\]* :: [`get_gpu_device_info()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[has_style]{.sig-name .descname} *\[function\]* :: [`has_style()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[style_count]{.sig-name .descname} *\[function\]* :: [`style_count()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[style_name]{.sig-name .descname} *\[function\]* :: [`style_name()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[has_id]{.sig-name .descname} *\[function\]* :: [`has_id()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[id_count]{.sig-name .descname} *\[function\]* :: [`id_count()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[id_name]{.sig-name .descname} *\[subroutine\]* :: [`id_name()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[plugin_count]{.sig-name .descname} *\[subroutine\]* :: [`plugin_count()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[plugin_name]{.sig-name .descname} :: [`plugin_name()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[encode_image_flags]{.sig-name .descname} *\[function\]* :: [`encode_image_flags()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[decode_image_flags]{.sig-name .descname} *\[subroutine\]* :: [`decode_image_flags()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[set_fix_external_callback]{.sig-name .descname} *\[subroutine\]* :: [`set_fix_external_callback()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[fix_external_get_force]{.sig-name .descname} *\[function\]* :: [`fix_external_get_force()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[fix_external_set_energy_global]{.sig-name .descname} *\[subroutine\]* :: [`fix_external_set_energy_global()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[fix_external_set_virial_global]{.sig-name .descname} *\[subroutine\]* :: [`fix_external_set_virial_global()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[fix_external_set_energy_peratom]{.sig-name .descname} *\[subroutine\]* :: [`fix_external_set_energy_peratom()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[fix_external_set_virial_peratom]{.sig-name .descname} *\[subroutine\]* :: [`fix_external_set_virial_peratom()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[fix_external_set_vector_length]{.sig-name .descname} *\[subroutine\]* :: [`fix_external_set_vector_length()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[fix_external_set_vector]{.sig-name .descname} *\[subroutine\]* :: [`fix_external_set_vector()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[flush_buffers]{.sig-name .descname} *\[subroutine\]* :: [`flush_buffers()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[is_running]{.sig-name .descname} *\[function\]* :: [`is_running()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[force_timeout]{.sig-name .descname} *\[subroutine\]* :: [`force_timeout()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[has_error]{.sig-name .descname} *\[function\]* :: [`has_error()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}

        - [% ]{.sig-name .descname}[get_last_error_message]{.sig-name .descname} *\[subroutine\]* :: [`get_last_error_message()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

*[function]{.pre} * [[lammps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[\[args\]\[,comm\]]{.pre}*[)]{.sig-paren}

:   This is the constructor for the Fortran class and will forward the arguments to a call to either [[`lammps_open_fortran()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv419lammps_open_fortraniPPci "lammps_open_fortran"){.reference .internal} or [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal}. If the LAMMPS library has been compiled with MPI support, it will also initialize MPI, if it has not already been initialized before.

    The *args* argument with the list of command-line parameters is optional and so it the *comm* argument with the MPI communicator. If *comm* is not provided, [`MPI_COMM_WORLD`{.docutils .literal .notranslate}]{.pre} is assumed. For more details please see the documentation of [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal}.

    Options[:]{.colon}

    :   - **args** *\[character(len=\*),dimension(:),optional\]* :: arguments as list of strings

        - **comm** *\[integer,optional\]* :: MPI communicator

    Call to[:]{.colon}

    :   [[`lammps_open_fortran()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv419lammps_open_fortraniPPci "lammps_open_fortran"){.reference .internal} [[`lammps_open_no_mpi()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv418lammps_open_no_mpiiPPcPPv "lammps_open_no_mpi"){.reference .internal}

    Return[:]{.colon}

    :   **lammps** :: an instance of the [`lammps`{.xref .f .f-type .docutils .literal .notranslate}]{.pre} derived type

    ::::: {.admonition .note}
    Note

    The [`MPI_F08`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} module, which defines Fortran 2008 bindings for MPI, is not directly supported by this interface due to the complexities of supporting both the [`MPI_F08`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} and [`MPI`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} modules at the same time. However, you should be able to use the [`MPI_VAL`{.docutils .literal .notranslate}]{.pre} member of the [`MPI_comm`{.docutils .literal .notranslate}]{.pre} derived type to access the integer value of the communicator, such as in

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        PROGRAM testmpi
          USE LIBLAMMPS
          USE MPI_F08
          TYPE(lammps) :: lmp
          lmp = lammps(comm=MPI_COMM_SELF%MPI_VAL)
        END PROGRAM testmpi
    :::
    ::::
    :::::

<!-- -->

*[type]{.pre} * [[lammps_style]{.pre}]{.sig-name .descname}[](#f/_/lammps_style "Link to this definition"){.headerlink}

:   This derived type is there to provide a convenient interface for the style constants used with [`extract_compute()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}, [`extract_fix()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}, and [`extract_variable()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}. Assuming your LAMMPS instance is called [`lmp`{.docutils .literal .notranslate}]{.pre}, these constants will be [`lmp%style%global`{.docutils .literal .notranslate}]{.pre}, [`lmp%style%atom`{.docutils .literal .notranslate}]{.pre}, and [`lmp%style%local`{.docutils .literal .notranslate}]{.pre}. These values are identical to the values described in [[`_LMP_STYLE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv416_LMP_STYLE_CONST "_LMP_STYLE_CONST"){.reference .internal} for the C library interface.

    Type fields[:]{.colon}

    :   - [% ]{.sig-name .descname}[global]{.sig-name .descname} *\[integer(c_int)\]* :: used to request global data

        - [% ]{.sig-name .descname}[atom]{.sig-name .descname} *\[integer(c_int)\]* :: used to request per-atom data

        - [% ]{.sig-name .descname}[local]{.sig-name .descname} *\[integer(c_int)\]* :: used to request local data

<!-- -->

*[type]{.pre} * [[lammps_type]{.pre}]{.sig-name .descname}[](#f/_/lammps_type "Link to this definition"){.headerlink}

:   This derived type is there to provide a convenient interface for the type constants used with [`extract_compute()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}, [`extract_fix()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}, and [`extract_variable()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}. Assuming your LAMMPS instance is called [`lmp`{.docutils .literal .notranslate}]{.pre}, these constants will be [`lmp%type%scalar`{.docutils .literal .notranslate}]{.pre}, [`lmp%type%vector`{.docutils .literal .notranslate}]{.pre}, and [`lmp%type%array`{.docutils .literal .notranslate}]{.pre}. These values are identical to the values described in [[`_LMP_TYPE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv415_LMP_TYPE_CONST "_LMP_TYPE_CONST"){.reference .internal} for the C library interface.

    Type fields[:]{.colon}

    :   - [% ]{.sig-name .descname}[scalar]{.sig-name .descname} *\[integer(c_int)\]* :: used to request scalars

        - [% ]{.sig-name .descname}[vector]{.sig-name .descname} *\[integer(c_int)\]* :: used to request vectors

        - [% ]{.sig-name .descname}[array]{.sig-name .descname} *\[integer(c_int)\]* :: used to request arrays (matrices)

::::::: {#procedures-bound-to-the-lammps-derived-type .section}
## Procedures Bound to the [`lammps`{.xref .f .f-type .docutils .literal .notranslate}]{.pre} Derived Type[](#procedures-bound-to-the-lammps-derived-type "Link to this heading"){.headerlink}

*[subroutine]{.pre} * [[close]{.pre}]{.sig-name .descname}[(]{.sig-paren}[\[]{.optional}*[finalize]{.pre}*[\]]{.optional}[)]{.sig-paren}[](#f/_/close "Link to this definition"){.headerlink}

:   This method will close down the LAMMPS instance through calling [[`lammps_close()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv412lammps_closePv "lammps_close"){.reference .internal}. If the *finalize* argument is present and has a value of [`.TRUE.`{.docutils .literal .notranslate}]{.pre}, then this subroutine also calls [[`lammps_kokkos_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_kokkos_finalizev "lammps_kokkos_finalize"){.reference .internal}, [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal}, [[`lammps_python_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_python_finalizev "lammps_python_finalize"){.reference .internal}, and [[`lammps_plugin_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_plugin_finalizev "lammps_plugin_finalize"){.reference .internal}.

    Options[:]{.colon}

    :   **finalize** *\[logical,optional\]* :: shut down the MPI environment of the LAMMPS library if [`.TRUE.`{.docutils .literal .notranslate}]{.pre}.

    Call to[:]{.colon}

    :   [[`lammps_close()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv412lammps_closePv "lammps_close"){.reference .internal} [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal} [[`lammps_kokkos_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_kokkos_finalizev "lammps_kokkos_finalize"){.reference .internal} [[`lammps_python_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_python_finalizev "lammps_python_finalize"){.reference .internal} [[`lammps_plugin_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_plugin_finalizev "lammps_plugin_finalize"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[error]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[error_type]{.pre}*, *[error_text]{.pre}*[)]{.sig-paren}[](#f/_/error "Link to this definition"){.headerlink}

:   This method is a wrapper around the [[`lammps_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv412lammps_errorPviPKc "lammps_error"){.reference .internal} function and will dispatch an error through the LAMMPS Error class.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   - **error_type** *\[integer(c_int)\]* :: constant to select which Error class function to call

        - **error_text** *\[character(len=\*)\]* :: error message

    Call to[:]{.colon}

    :   [[`lammps_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv412lammps_errorPviPKc "lammps_error"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[file]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[filename]{.pre}*[)]{.sig-paren}[](#f/_/file "Link to this definition"){.headerlink}

:   This method will call [[`lammps_file()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv411lammps_filePvPKc "lammps_file"){.reference .internal} to have LAMMPS read and process commands from a file.

    Parameters[:]{.colon}

    :   **filename** *\[character(len=\*)\]* :: name of file with LAMMPS commands

    Call to[:]{.colon}

    :   [[`lammps_file()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv411lammps_filePvPKc "lammps_file"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[command]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[cmd]{.pre}*[)]{.sig-paren}[](#f/_/command "Link to this definition"){.headerlink}

:   This method will call [[`lammps_command()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv414lammps_commandPvPKc "lammps_command"){.reference .internal} to have LAMMPS execute a single command.

    Parameters[:]{.colon}

    :   **cmd** *\[character(len=\*)\]* :: single LAMMPS command

    Call to[:]{.colon}

    :   [[`lammps_command()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv414lammps_commandPvPKc "lammps_command"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[commands_list]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[cmds]{.pre}*[)]{.sig-paren}[](#f/_/commands_list "Link to this definition"){.headerlink}

:   This method will call [[`lammps_commands_list()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv420lammps_commands_listPviPPKc "lammps_commands_list"){.reference .internal} to have LAMMPS execute a list of input lines.

    Parameters[:]{.colon}

    :   **cmd** *\[character(len=\*),dimension(:)\]* :: list of LAMMPS input lines

    Call to[:]{.colon}

    :   [[`lammps_commands_list()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv420lammps_commands_listPviPPKc "lammps_commands_list"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[commands_string]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[str]{.pre}*[)]{.sig-paren}[](#f/_/commands_string "Link to this definition"){.headerlink}

:   This method will call [[`lammps_commands_string()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv422lammps_commands_stringPvPKc "lammps_commands_string"){.reference .internal} to have LAMMPS execute a block of commands from a string.

    Parameters[:]{.colon}

    :   **str** *\[character(len=\*)\]* :: LAMMPS input in string

    Call to[:]{.colon}

    :   [[`lammps_commands_string()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv422lammps_commands_stringPvPKc "lammps_commands_string"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[get_natoms]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/get_natoms "Link to this definition"){.headerlink}

:   This function will call [[`lammps_get_natoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_natomsPv "lammps_get_natoms"){.reference .internal} and return the number of atoms in the system.

    Call to[:]{.colon}

    :   [[`lammps_get_natoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_natomsPv "lammps_get_natoms"){.reference .internal}

    Return[:]{.colon}

    :   **natoms** *\[real(c_double)\]* :: number of atoms

    ::: {.admonition .note}
    Note

    If you would prefer to get the number of atoms in its native format (i.e., as a 32- or 64-bit integer, depending on how LAMMPS was compiled), this can be extracted with [`extract_global()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}.
    :::

------------------------------------------------------------------------

*[function]{.pre} * [[get_thermo]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*[)]{.sig-paren}[](#f/_/get_thermo "Link to this definition"){.headerlink}

:   This function will call [[`lammps_get_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_thermoPvPKc "lammps_get_thermo"){.reference .internal} and return the value of the corresponding thermodynamic keyword.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   **name** *\[character(len=\*)\]* :: string with the name of the thermo keyword

    Call to[:]{.colon}

    :   [[`lammps_get_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_thermoPvPKc "lammps_get_thermo"){.reference .internal}

    Return[:]{.colon}

    :   **value** *\[real(c_double)\]* :: value of the requested thermo property or 0.0_c_double

------------------------------------------------------------------------

*[function]{.pre} * [[last_thermo]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[what]{.pre}*, *[index]{.pre}*[)]{.sig-paren}[](#f/_/last_thermo "Link to this definition"){.headerlink}

:   This function will call [[`lammps_last_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv418lammps_last_thermoPvPKci "lammps_last_thermo"){.reference .internal} and returns either a string or a pointer to a cached copy of LAMMPS last thermodynamic output, depending on the data requested through *what*. Note that *index* uses 1-based indexing to access thermo output columns.

    ::: versionadded
    [Added in version 15Jun2023.]{.versionmodified .added}
    :::

    Note that this function actually does not return a value, but rather associates the pointer on the left side of the assignment to point to internal LAMMPS data (with the exception of string data, which are copied and returned as ordinary Fortran strings). Pointers must be of the correct data type to point to said data (typically [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre}, [`INTEGER(c_int64_t)`{.docutils .literal .notranslate}]{.pre}, or [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}). The pointer being associated with LAMMPS data is type-checked at run-time via an overloaded assignment operator. The pointers returned by this function point to temporary, read-only data that may be overwritten at any time, so their target values need to be copied to local storage if they are supposed to persist.

    For example,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        PROGRAM thermo
          USE LIBLAMMPS
          USE, INTRINSIC :: ISO_C_BINDING, ONLY : c_double, c_int64_t, c_int
          TYPE(lammps) :: lmp
          INTEGER(KIND=c_int64_t), POINTER :: ntimestep, bval
          REAL(KIND=c_double), POINTER :: dval
          INTEGER(KIND=c_int), POINTER :: nfield, typ, ival
          INTEGER(KIND=c_int) :: i
          CHARACTER(LEN=11) :: key

          lmp = lammps()
          CALL lmp%file('in.sysinit')

          ntimestep = lmp%last_thermo('step', 0)
          nfield = lmp%last_thermo('num', 0)
          PRINT*, 'Last thermo output on step: ', ntimestep, '  Number of fields: ', nfield
          DO i=1, nfield
              key = lmp%last_thermo('keyword',i)
              typ = lmp%last_thermo('type',i)
              IF (typ == lmp%dtype%i32) THEN
                  ival = lmp%last_thermo('data',i)
                  PRINT*, key, ':', ival
              ELSE IF (typ == lmp%dtype%i64) THEN
                  bval = lmp%last_thermo('data',i)
                  PRINT*, key, ':', bval
              ELSE IF (typ == lmp%dtype%r64) THEN
                  dval = lmp%last_thermo('data',i)
                  PRINT*, key, ':', dval
              END IF
          END DO
          CALL lmp%close(.TRUE.)
        END PROGRAM thermo
    :::
    ::::

    would extract the last timestep where thermo output was done and the number of columns it printed. Then it loops over the columns to print out column header keywords and the corresponding data.

    ::: {.admonition .note}
    Note

    If [`last_thermo()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} returns a string, the string must have a length greater than or equal to the length of the string (not including the terminal [`NULL`{.docutils .literal .notranslate}]{.pre} character) that LAMMPS returns. If the variable's length is too short, the string will be truncated. As usual in Fortran, strings are padded with spaces at the end. If you use an allocatable string, the string **must be allocated** prior to calling this function.
    :::

    Parameters[:]{.colon}

    :   - **what** *\[character(len=\*)\]* :: string with the name of the thermo keyword

        - **index** *\[integer(c_int)\]* :: 1-based column index

    Call to[:]{.colon}

    :   [[`lammps_last_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv418lammps_last_thermoPvPKci "lammps_last_thermo"){.reference .internal}

    Return[:]{.colon}

    :   **pointer** *\[polymorphic\]* :: pointer to LAMMPS data. The left-hand side of the assignment should be either a string (if expecting string data) or a C-compatible pointer (e.g., [`INTEGER(c_int),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`::`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`nlocal`{.docutils .literal .notranslate}]{.pre}) to the extracted property.

    ::: {.admonition .warning}
    Warning

    Modifying the data in the location pointed to by the returned pointer may lead to inconsistent internal data and thus may cause failures, crashes, or bogus simulations. In general, it is much better to use a LAMMPS input command that sets or changes these parameters. Using an input command will take care of all side effects and necessary updates of settings derived from such settings.
    :::

------------------------------------------------------------------------

*[subroutine]{.pre} * [[extract_box]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[\[boxlo\]\[,]{.pre} [boxhi\]\[,]{.pre} [xy\]\[,]{.pre} [yz\]\[,]{.pre} [xz\]\[,]{.pre} [pflags\]\[,]{.pre} [boxflag\]]{.pre}*[)]{.sig-paren}[](#f/_/extract_box "Link to this definition"){.headerlink}

:   This subroutine will call [[`lammps_extract_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv418lammps_extract_boxPvPdPdPdPdPdPiPi "lammps_extract_box"){.reference .internal}. All parameters are optional, though obviously at least one should be present. The parameters *pflags* and *boxflag* are stored in LAMMPS as integers, but should be declared as [`LOGICAL`{.docutils .literal .notranslate}]{.pre} variables when calling from Fortran.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Options[:]{.colon}

    :   - **boxlo** *\[real(c_double),dimension(3),optional\]* :: vector in which to store lower-bounds of simulation box

        - **boxhi** *\[real(c_double),dimension(3),optional\]* :: vector in which to store upper-bounds of simulation box

        - **xy** *\[real(c_double),optional\]* :: variable in which to store *xy* tilt factor

        - **yz** *\[real(c_double),optional\]* :: variable in which to store *yz* tilt factor

        - **xz** *\[real(c_double),optional\]* :: variable in which to store *xz* tilt factor

        - **pflags** *\[logical,dimension(3),optional\]* :: vector in which to store periodicity flags ([`.TRUE.`{.docutils .literal .notranslate}]{.pre} means periodic in that dimension)

        - **boxflag** *\[logical,optional\]* :: variable in which to store boolean denoting whether the box will change during a simulation ([`.TRUE.`{.docutils .literal .notranslate}]{.pre} means box will change)

    Call to[:]{.colon}

    :   [[`lammps_extract_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv418lammps_extract_boxPvPdPdPdPdPdPiPi "lammps_extract_box"){.reference .internal}

::::: {.admonition .note}
Note

Note that a frequent use case of this function is to extract only one or more of the options rather than all seven. For example, assuming "lmp" represents a properly-initialized LAMMPS instance, the following code will extract the periodic box settings into the variable "periodic":

:::: {.highlight-fortran .notranslate}
::: highlight
    ! code to start up
    LOGICAL :: periodic(3)
    ! code to initialize LAMMPS / run things / etc.
    CALL lmp%extract_box(pflags = periodic)
:::
::::
:::::

------------------------------------------------------------------------

*[subroutine]{.pre} * [[reset_box]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[boxlo]{.pre}*, *[boxhi]{.pre}*, *[xy]{.pre}*, *[yz]{.pre}*, *[xz]{.pre}*[)]{.sig-paren}[](#f/_/reset_box "Link to this definition"){.headerlink}

:   This subroutine will call [[`lammps_reset_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv416lammps_reset_boxPvPdPdddd "lammps_reset_box"){.reference .internal}. All parameters are required.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   - **boxlo** *\[real(c_double),dimension(3)\]* :: vector of three doubles containing the lower box boundary

        - **boxhi** *\[real(c_double),dimension(3)\]* :: vector of three doubles containing the upper box boundary

        - **xy** *\[real(c_double)\]* :: *x--y* tilt factor

        - **yz** *\[real(c_double)\]* :: *y--z* tilt factor

        - **xz** *\[real(c_double)\]* :: *x--z* tilt factor

    Call to[:]{.colon}

    :   [[`lammps_reset_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv416lammps_reset_boxPvPdPdddd "lammps_reset_box"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[memory_usage]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[meminfo]{.pre}*[)]{.sig-paren}[](#f/_/memory_usage "Link to this definition"){.headerlink}

:   This subroutine will call [[`lammps_memory_usage()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv419lammps_memory_usagePvPd "lammps_memory_usage"){.reference .internal} and store the result in the three-element array *meminfo*.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   **meminfo** *\[real(c_double),dimension(3)\]* :: vector of three doubles in which to store memory usage data

    Call to[:]{.colon}

    :   [[`lammps_memory_usage()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv419lammps_memory_usagePvPd "lammps_memory_usage"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[get_mpi_comm]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/get_mpi_comm "Link to this definition"){.headerlink}

:   This function returns a Fortran representation of the LAMMPS "world" communicator.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Call to[:]{.colon}

    :   [[`lammps_get_mpi_comm()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv419lammps_get_mpi_commPv "lammps_get_mpi_comm"){.reference .internal}

    Return[:]{.colon}

    :   **comm** *\[integer\]* :: Fortran integer equivalent to the MPI communicator LAMMPS is using

    ::: {.admonition .note}
    Note

    The C library interface currently returns type [`int`{.docutils .literal .notranslate}]{.pre} instead of type [`MPI_Fint`{.docutils .literal .notranslate}]{.pre}, which is the C type corresponding to Fortran [`INTEGER`{.docutils .literal .notranslate}]{.pre} types of the default kind. On most compilers, these are the same anyway, but this interface exchanges values this way to avoid warning messages.
    :::

    ::::: {.admonition .note}
    Note

    The [`MPI_F08`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} module, which defines Fortran 2008 bindings for MPI, is not directly supported by this function. However, you should be able to convert between the two using the MPI_VAL member of the communicator. For example,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        USE MPI_F08
        USE LIBLAMMPS
        TYPE(lammps) :: lmp
        TYPE(MPI_Comm) :: comm
        ! ... [commands to set up LAMMPS/etc.]
        comm%MPI_VAL = lmp%get_mpi_comm()
    :::
    ::::

    should assign an [`MPI_F08`{.xref .f .f-mod .docutils .literal .notranslate}]{.pre} communicator properly.
    :::::

------------------------------------------------------------------------

*[function]{.pre} * [[extract_setting]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[keyword]{.pre}*[)]{.sig-paren}[](#f/_/extract_setting "Link to this definition"){.headerlink}

:   Query LAMMPS about global settings. See the documentation for the [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal} function from the C library.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   **keyword** *\[character(len=\*)\]* :: string containing the name of the thermo keyword

    Call to[:]{.colon}

    :   [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal}

    Return[:]{.colon}

    :   **setting** *\[integer(c_int)\]* :: value of the queried setting or [\\(-1\\)]{.math .notranslate .nohighlight} if unknown

------------------------------------------------------------------------

*[function]{.pre} * [[extract_global]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*[)]{.sig-paren}[](#f/_/extract_global "Link to this definition"){.headerlink}

:   This function calls [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal} and returns either a string or a pointer to internal global LAMMPS data, depending on the data requested through *name*.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Note that this function actually does not return a value, but rather associates the pointer on the left side of the assignment to point to internal LAMMPS data (with the exception of string data, which are copied and returned as ordinary Fortran strings). Pointers must be of the correct data type to point to said data (typically [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre}, [`INTEGER(c_int64_t)`{.docutils .literal .notranslate}]{.pre}, or [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}) and have compatible kind and rank. The pointer being associated with LAMMPS data is type-, kind-, and rank-checked at run-time via an overloaded assignment operator. The pointers returned by this function are generally persistent; therefore it is not necessary to call the function again unless a [[clear command]{.doc}]clear.md){.reference .internal} command has been issued, which wipes out and recreates the contents of the [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} class.

    For example,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        PROGRAM demo
          USE, INTRINSIC :: ISO_C_BINDING, ONLY : c_int64_t, c_int, c_double
          USE LIBLAMMPS
          TYPE(lammps) :: lmp
          INTEGER(c_int), POINTER :: nlocal => NULL()
          INTEGER(c_int64_t), POINTER :: ntimestep => NULL()
          REAL(c_double), POINTER :: dt => NULL()
          CHARACTER(LEN=10) :: units
          lmp = lammps()
          ! other commands
          nlocal = lmp%extract_global('nlocal')
          ntimestep = lmp%extract_global('ntimestep')
          dt = lmp%extract_global('dt')
          units = lmp%extract_global('units')
          ! more commands
          lmp.close(.TRUE.)
        END PROGRAM demo
    :::
    ::::

    would extract the number of atoms on this processor, the current time step, the size of the current time step, and the units being used into the variables *nlocal*, *ntimestep*, *dt*, and *units*, respectively.

    ::::: {.admonition .note}
    Note

    If [`extract_global()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} returns a string, the string must have a length greater than or equal to the length of the string (not including the terminal [`NULL`{.docutils .literal .notranslate}]{.pre} character) that LAMMPS returns. If the variable's length is too short, the string will be truncated. As usual in Fortran, strings are padded with spaces at the end. If you use an allocatable string, the string **must be allocated** prior to calling this function, but you can automatically reallocate it to the correct length after the function returns, viz.,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        PROGRAM test
          USE LIBLAMMPS
          TYPE(lammps) :: lmp
          CHARACTER(LEN=:), ALLOCATABLE :: str
          lmp = lammps()
          CALL lmp%command('units metal')
          ALLOCATE(CHARACTER(LEN=80) :: str)
          str = lmp%extract_global('units')
          str = TRIM(str) ! re-allocates to length len_trim(str) here
          PRINT*, LEN(str), LEN_TRIM(str)
        END PROGRAM test
    :::
    ::::

    will print the number 5 (the length of the word "metal") twice.
    :::::

    Parameters[:]{.colon}

    :   **name** *\[character(len=\*)\]* :: string with the name of the property to extract

    Call to[:]{.colon}

    :   [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal}

    Return[:]{.colon}

    :   **pointer** *\[polymorphic\]* :: pointer to LAMMPS data. The left-hand side of the assignment should be either a string (if expecting string data) or a C-compatible pointer (e.g., [`INTEGER(c_int),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`::`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`nlocal`{.docutils .literal .notranslate}]{.pre}) to the extracted property. If expecting vector data, the pointer should have dimension ":".

    ::: {.admonition .warning}
    Warning

    Modifying the data in the location pointed to by the returned pointer may lead to inconsistent internal data and thus may cause failures, crashes, or bogus simulations. In general, it is much better to use a LAMMPS input command that sets or changes these parameters. Using an input command will take care of all side effects and necessary updates of settings derived from such settings.
    :::

------------------------------------------------------------------------

*[function]{.pre} * [[extract_atom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*[)]{.sig-paren}[](#f/_/extract_atom "Link to this definition"){.headerlink}

:   This function calls [[`lammps_extract_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_atoms.md#_CPPv419lammps_extract_atomPvPKc "lammps_extract_atom"){.reference .internal} and returns a pointer to LAMMPS data tied to the [`Atom`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre} class, depending on the data requested through *name*.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Note that this function actually does not return a pointer, but rather associates the pointer on the left side of the assignment to point to internal LAMMPS data. Pointers must be of the correct type, kind, and rank (e.g., [`INTEGER(c_int),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre} for "type", "mask", or "id"; [`INTEGER(c_int64_t),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre} for "id" if LAMMPS was compiled with the [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} flag; [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:,:)`{.docutils .literal .notranslate}]{.pre} for "x", "v", or "f"; and so forth). The pointer being associated with LAMMPS data is type-, kind-, and rank-checked at run-time.

    Parameters[:]{.colon}

    :   **name** *\[character(len=\*)\]* :: string with the name of the property to extract

    Call to[:]{.colon}

    :   [[`lammps_extract_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_atoms.md#_CPPv419lammps_extract_atomPvPKc "lammps_extract_atom"){.reference .internal}

    Return[:]{.colon}

    :   **pointer** *\[polymorphic\]* :: pointer to LAMMPS data. The left-hand side of the assignment should be a C-interoperable pointer of appropriate kind and rank (e.g., [`INTEGER(c_int),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`::`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`mask(:)`{.docutils .literal .notranslate}]{.pre}) to the extracted property. If expecting vector data, the pointer should have dimension ":"; if expecting matrix data, the pointer should have dimension ":,:".

    ::: {.admonition .warning}
    Warning

    Pointers returned by this function are generally not persistent, as per-atom data may be redistributed, reallocated, and reordered at every re-neighboring operation. It is advisable to re-bind pointers using [`extract_atom()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} between runs.
    :::

    ::::::::::: {.tip .admonition}
    Array index order

    Two-dimensional arrays returned from [`extract_atom()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} will be **transposed** from equivalent arrays in C, and they will be indexed from 1 instead of 0. For example, in C,

    :::: {.highlight-c .notranslate}
    ::: highlight
        void *lmp;
        double **x;
        /* more code to setup, etc. */
        x = lammps_extract_atom(lmp, "x");
        printf("%f\n", x[5][1]);
    :::
    ::::

    will print the *y*-coordinate of the sixth atom on this processor. Conversely,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        TYPE(lammps) :: lmp
        REAL(c_double), DIMENSION(:,:), POINTER :: x => NULL()
        ! more code to setup, etc.
        x = lmp%extract_atom("x")
        PRINT '(f0.6)', x(2,6)
    :::
    ::::

    will print the *y*-coordinate of the sixth atom on this processor (note the transposition of the two indices). This is not a choice, but rather a consequence of the different conventions adopted by the Fortran and C standards decades ago: in C, the block of data

    :::: {.highlight-none .notranslate}
    ::: highlight
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    :::
    ::::

    interpreted as a [\\(4\\times4\\)]{.math .notranslate .nohighlight} matrix would be

    ::: {.math .notranslate .nohighlight}
    \\\[\\begin{split}\\begin{bmatrix} 1 & 2 & 3 & 4 \\\\ 5 & 6 & 7 & 8 \\\\ 9 & 10 & 11 & 12 \\\\ 13 & 14 & 15 & 16 \\end{bmatrix},\\end{split}\\\]
    :::

    that is, in row-major order. In Fortran, the same block of data is interpreted in column-major order, namely,

    ::: {.math .notranslate .nohighlight}
    \\\[\\begin{split}\\begin{bmatrix} 1 & 5 & 9 & 13 \\\\ 2 & 6 & 10 & 14 \\\\ 3 & 7 & 11 & 15 \\\\ 4 & 8 & 12 & 16 \\end{bmatrix}.\\end{split}\\\]
    :::

    This difference in interpretation of the same block of data by the two languages means, in effect, that matrices from C or C++ will be transposed when interpreted in Fortran.
    :::::::::::

    ::::: {.admonition .note}
    Note

    If you would like the indices to start at 0 instead of 1 (which follows typical notation in C and C++, but not Fortran), you can create another pointer and associate it thus:

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        REAL(c_double), DIMENSION(:,:), POINTER :: x, x0
        x = lmp%extract_atom("x")
        x0(0:,0:) => x
    :::
    ::::

    The above would cause the dimensions of *x* to be (1:3, 1:nmax) and those of *x0* to be (0:2, 0:nmax[\\(-\\)]{.math .notranslate .nohighlight}1).
    :::::

------------------------------------------------------------------------

*[function]{.pre} * [[extract_compute]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*, *[style]{.pre}*, *[type]{.pre}*[)]{.sig-paren}[](#f/_/extract_compute "Link to this definition"){.headerlink}

:   This function calls [[`lammps_extract_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv422lammps_extract_computePvPKcii "lammps_extract_compute"){.reference .internal} and returns a pointer to LAMMPS data tied to the [`Compute`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre} class, specifically data provided by the compute identified by *id*. Computes may provide global, per-atom, or local data, and those data may be a scalar, a vector, or an array. Since computes may provide multiple kinds of data, the user is required to specify which set of data is to be returned through the *style* and *type* variables.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Note that this function actually does not return a value, but rather associates the pointer on the left side of the assignment to point to internal LAMMPS data. Pointers must be of the correct data type to point to said data (i.e., [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}) and have compatible rank. The pointer being associated with LAMMPS data is type-, kind-, and rank-checked at run-time via an overloaded assignment operator.

    For example,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        TYPE(lammps) :: lmp
        REAL(c_double), DIMENSION(:), POINTER :: COM
        ! code to setup, create atoms, etc.
        CALL lmp%command('compute COM all com')
        COM = lmp%extract_compute('COM', lmp%style%global, lmp%style%type)
    :::
    ::::

    will bind the variable *COM* to the center of mass of the atoms created in your simulation. The vector in this case has length 3; the length (or, in the case of array data, the number of rows and columns) is determined for you based on data from the [`Compute`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre} class.

    ::: {.tip .admonition}
    Array index order

    Two-dimensional arrays returned from [`extract_compute()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} will be **transposed** from equivalent arrays in C, and they will be indexed from 1 instead of 0. See the note at [`extract_atom()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} for further details.
    :::

    The following combinations are possible (assuming [`lmp`{.docutils .literal .notranslate}]{.pre} is the name of your LAMMPS instance):

    +-------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
    | Style                                                       | Type                                                       | Type to assign to                                                                                                                                                                                                                              | Returned data   |
    +=============================================================+============================================================+================================================================================================================================================================================================================================================+=================+
    | [`lmp%style%global`{.docutils .literal .notranslate}]{.pre} | [`lmp%type%scalar`{.docutils .literal .notranslate}]{.pre} | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}                                                                                               | Global scalar   |
    +-------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
    | [`lmp%style%global`{.docutils .literal .notranslate}]{.pre} | [`lmp%type%vector`{.docutils .literal .notranslate}]{.pre} | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}   | Global vector   |
    +-------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
    | [`lmp%style%global`{.docutils .literal .notranslate}]{.pre} | [`lmp%type%array`{.docutils .literal .notranslate}]{.pre}  | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:,:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre} | Global array    |
    +-------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
    | [`lmp%style%atom`{.docutils .literal .notranslate}]{.pre}   | [`lmp%type%vector`{.docutils .literal .notranslate}]{.pre} | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}   | Per-atom vector |
    +-------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
    | [`lmp%style%atom`{.docutils .literal .notranslate}]{.pre}   | [`lmp%type%array`{.docutils .literal .notranslate}]{.pre}  | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:,:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre} | Per-atom array  |
    +-------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
    | [`lmp%style%local`{.docutils .literal .notranslate}]{.pre}  | [`lmp%type%vector`{.docutils .literal .notranslate}]{.pre} | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}   | Local vector    |
    +-------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
    | [`lmp%style%local`{.docutils .literal .notranslate}]{.pre}  | [`lmp%type%array`{.docutils .literal .notranslate}]{.pre}  | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:,:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre} | Local array     |
    +-------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: compute ID from which to extract data

        - **style** *\[integer(c_int)\]* :: value indicating the style of data to extract (global, per-atom, or local)

        - **type** *\[integer(c_int)\]* :: value indicating the type of data to extract (scalar, vector, or array)

    Call to[:]{.colon}

    :   [[`lammps_extract_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv422lammps_extract_computePvPKcii "lammps_extract_compute"){.reference .internal}

    Return[:]{.colon}

    :   **pointer** *\[polymorphic\]* :: pointer to LAMMPS data. The left-hand side of the assignment should be a C-compatible pointer (e.g., [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`::`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`x`{.docutils .literal .notranslate}]{.pre}) to the extracted property. If expecting vector data, the pointer should have dimension ":"; if expecting array (matrix) data, the pointer should have dimension ":,:".

    ::: {.admonition .note}
    Note

    If the compute's data are not already computed for the current step, the compute will be invoked. LAMMPS cannot easily check at that time if it is valid to invoke a compute, so it may fail with an error. The caller has to check to avoid such an error.
    :::

    ::: {.admonition .warning}
    Warning

    The pointers returned by this function are generally not persistent, since the computed data may be re-distributed, re-allocated, and re-ordered at every invocation. It is advisable to re-invoke this function before the data are accessed or make a copy if the data are to be used after other LAMMPS commands have been issued. Do **not** modify the data returned by this function.
    :::

------------------------------------------------------------------------

*[function]{.pre} * [[extract_fix]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id,]{.pre} [style,]{.pre} [type\[,]{.pre} [nrow\]\[,]{.pre} [ncol\]]{.pre}*[)]{.sig-paren}[](#f/_/extract_fix "Link to this definition"){.headerlink}

:   This function calls [[`lammps_extract_fix()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv418lammps_extract_fixPvPKciiii "lammps_extract_fix"){.reference .internal} and returns a pointer to LAMMPS data tied to the [`Fix`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre} class, specifically data provided by the fix identified by *id*. Fixes may provide global, per-atom, or local data, and those data may be a scalar, a vector, or an array. Since many fixes provide multiple kinds of data, the user is required to specify which set of data is to be returned through the *style* and *type* variables.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Global data are calculated at the time they are requested and are only available element-by-element. As such, the user is expected to provide the *nrow* variable to specify which element of a global vector or the *nrow* and *ncol* variables to specify which element of a global array the user wishes LAMMPS to return. The *ncol* variable is optional for global scalar or vector data, and both *nrow* and *ncol* are optional when a global scalar is requested, as well as when per-atom or local data are requested. The following combinations are possible (assuming [`lmp`{.docutils .literal .notranslate}]{.pre} is the name of your LAMMPS instance):

    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
    | Style                                                       | Type                                                       | nrow     | ncol     | Type to assign to                                                                                                                                                                                                                              | Returned data            |
    +=============================================================+============================================================+==========+==========+================================================================================================================================================================================================================================================+==========================+
    | [`lmp%style%global`{.docutils .literal .notranslate}]{.pre} | [`lmp%type%scalar`{.docutils .literal .notranslate}]{.pre} | Ignored  | Ignored  | [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                                      | Global scalar            |
    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
    | [`lmp%style%global`{.docutils .literal .notranslate}]{.pre} | [`lmp%type%vector`{.docutils .literal .notranslate}]{.pre} | Required | Ignored  | [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                                      | Element of global vector |
    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
    | [`lmp%style%global`{.docutils .literal .notranslate}]{.pre} | [`lmp%type%array`{.docutils .literal .notranslate}]{.pre}  | Required | Required | [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                                      | Element of global array  |
    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
    | [`lmp%style%atom`{.docutils .literal .notranslate}]{.pre}   | [`lmp%type%scalar`{.docutils .literal .notranslate}]{.pre} |          |          |                                                                                                                                                                                                                                                | (not allowed)            |
    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
    | [`lmp%style%atom`{.docutils .literal .notranslate}]{.pre}   | [`lmp%type%vector`{.docutils .literal .notranslate}]{.pre} | Ignored  | Ignored  | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}   | Per-atom vector          |
    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
    | [`lmp%style%atom`{.docutils .literal .notranslate}]{.pre}   | [`lmp%type%array`{.docutils .literal .notranslate}]{.pre}  | Ignored  | Ignored  | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:,:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre} | Per-atom array           |
    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
    | [`lmp%style%local`{.docutils .literal .notranslate}]{.pre}  | [`lmp%type%scalar`{.docutils .literal .notranslate}]{.pre} |          |          |                                                                                                                                                                                                                                                | (not allowed)            |
    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
    | [`lmp%style%local`{.docutils .literal .notranslate}]{.pre}  | [`lmp%type%vector`{.docutils .literal .notranslate}]{.pre} | Ignored  | Ignored  | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre}   | Per-atom vector          |
    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+
    | [`lmp%style%local`{.docutils .literal .notranslate}]{.pre}  | [`lmp%type%array`{.docutils .literal .notranslate}]{.pre}  | Ignored  | Ignored  | [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:,:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`POINTER`{.docutils .literal .notranslate}]{.pre} | Per-atom array           |
    +-------------------------------------------------------------+------------------------------------------------------------+----------+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------+

    In the case of global data, this function returns a value of type [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}. For per-atom or local data, this function does not return a value but instead associates the pointer on the left side of the assignment to point to internal LAMMPS data. Pointers must be of the correct type and kind to point to said data (i.e., [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}) and have compatible rank. The pointer being associated with LAMMPS data is type-, kind-, and rank-checked at run-time via an overloaded assignment operator.

    For example,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        TYPE(lammps) :: lmp
        REAL(c_double) :: dr, dx, dy, dz
        ! more code to set up, etc.
        lmp%command('fix george all recenter 2 2 2')
        ! more code
        dr = lmp%extract_fix("george", lmp%style%global, lmp%style%scalar)
        dx = lmp%extract_fix("george", lmp%style%global, lmp%style%vector, 1)
        dy = lmp%extract_fix("george", lmp%style%global, lmp%style%vector, 2)
        dz = lmp%extract_fix("george", lmp%style%global, lmp%style%vector, 3)
    :::
    ::::

    will extract the global scalar calculated by [[fix recenter]{.doc}]fix_recenter.md){.reference .internal} into the variable *dr* and the three elements of the global vector calculated by fix recenter into the variables *dx*, *dy*, and *dz*, respectively.

    If asked for per-atom or local data, [`extract_fix()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} returns a pointer to actual LAMMPS data. The pointer returned will have the appropriate size to match the internal data, and will be type/kind/rank-checked at the time of the assignment. For example,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        TYPE(lammps) :: lmp
        REAL(c_double), DIMENSION(:), POINTER :: r
        ! more code to set up, etc.
        lmp%command('fix state all store/state 0 x y z')
        ! more code
        r = lmp%extract_fix('state', lmp%style%atom, lmp%type%array)
    :::
    ::::

    will bind the pointer *r* to internal LAMMPS data representing the per-atom array computed by [[fix store/state]{.doc}]fix_store_state.md){.reference .internal} when three inputs are specified. Similarly,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        TYPE(lammps) :: lmp
        REAL(c_double), DIMENSION(:), POINTER :: x
        ! more code to set up, etc.
        lmp%command('fix state all store/state 0 x')
        ! more code
        x = lmp%extract_fix('state', lmp%style%atom, lmp%type%vector)
    :::
    ::::

    will associate the pointer *x* with internal LAMMPS data corresponding to the per-atom vector computed by [[fix store/state]{.doc}]fix_store_state.md){.reference .internal} when only one input is specified. Similar examples with [`lmp%style%atom`{.docutils .literal .notranslate}]{.pre} replaced by [`lmp%style%local`{.docutils .literal .notranslate}]{.pre} will extract local data from fixes that define local vectors and/or arrays.

    ::: {.admonition .warning}
    Warning

    The pointers returned by this function for per-atom or local data are generally not persistent, since the computed data may be redistributed, reallocated, and reordered at every invocation of the fix. It is thus advisable to re-invoke this function before the data are accessed or to make a copy if the data are to be used after other LAMMPS commands have been issued.
    :::

    ::: {.admonition .note}
    Note

    LAMMPS cannot easily check if it is valid to access the data, so it may fail with an error. The caller has to avoid such an error.
    :::

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: string with the name of the fix from which to extract data

        - **style** *\[integer(c_int)\]* :: value indicating the style of data to extract (global, per-atom, or local)

        - **type** *\[integer(c_int)\]* :: value indicating the type of data to extract (scalar, vector, or array)

        - **nrow** *\[integer(c_int)\]* :: row index (used only for global vectors and arrays)

        - **ncol** *\[integer(c_int)\]* :: column index (only used for global arrays)

    Call to[:]{.colon}

    :   [[`lammps_extract_fix()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv418lammps_extract_fixPvPKciiii "lammps_extract_fix"){.reference .internal}

    Return[:]{.colon}

    :   **data** *\[polymorphic\]* :: LAMMPS data (for global data) or a pointer to LAMMPS data (for per-atom or local data). The left-hand side of the assignment should be of type [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre} and have appropriate rank (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre} if expecting per-atom or local vector data and [`DIMENSION(:,:)`{.docutils .literal .notranslate}]{.pre} if expecting per-atom or local array data). If expecting local or per-atom data, it should have the [`POINTER`{.docutils .literal .notranslate}]{.pre} attribute, but if expecting global data, it should be an ordinary (non-[`POINTER`{.docutils .literal .notranslate}]{.pre}) variable.

    ::: {.tip .admonition}
    Array index order

    Two-dimensional global, per-atom, or local array data from [`extract_fix()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} will be **transposed** from equivalent arrays in C (or in the ordinary LAMMPS interface accessed through thermodynamic output), and they will be indexed from 1, not 0. This is true even for global data, which are returned as scalars---this is done primarily so the interface is consistent, as there is no choice but to transpose the indices for per-atom or local array data. See the similar note under [`extract_atom()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} for further details.
    :::

------------------------------------------------------------------------

*[function]{.pre} * [[extract_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*[\[]{.optional}, *[group]{.pre}*[\]]{.optional}[)]{.sig-paren}[](#f/_/extract_variable "Link to this definition"){.headerlink}

:   This function calls [[`lammps_extract_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv423lammps_extract_variablePvPKcPKc "lammps_extract_variable"){.reference .internal} and returns a scalar, vector, or string containing the value of the variable identified by *name*. When the variable is an *equal*-style variable (or one compatible with that style such as *internal*), the variable is evaluated and the corresponding value returned. When the variable is an *atom*-style variable, the variable is evaluated and a vector of values is returned. With all other variables, a string is returned. The *group* argument is only used for *atom* style variables and is ignored otherwise. If *group* is absent for *atom*-style variables, the group is assumed to be "all".

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function returns the values of the variables, not pointers to them. Vectors pointing to *atom*-style variables should be of type [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}, be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}), and have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute.

    ::: {.admonition .note}
    Note

    Unlike the C library interface, the Fortran interface does not require you to deallocate memory when you are through; this is done for you, behind the scenes.
    :::

    For example,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        TYPE(lammps) :: lmp
        REAL(c_double) :: area
        ! more code to set up, etc.
        lmp%command('variable A equal lx*ly')
        ! more code
        area = lmp%extract_variable("A")
    :::
    ::::

    will extract the *x*--*y* cross-sectional area of the simulation into the variable *area*.

    Parameters[:]{.colon}

    :   **name** *\[character(len=\*)\]* :: variable name to evaluate

    Options[:]{.colon}

    :   **group** *\[character(len=\*),optional\]* :: group for which to extract per-atom data (if absent, use "all")

    Call to[:]{.colon}

    :   [[`lammps_extract_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv423lammps_extract_variablePvPKcPKc "lammps_extract_variable"){.reference .internal}

    Return[:]{.colon}

    :   **data** *\[polymorphic\]* :: scalar of type [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre} (for *equal*-style variables and others that are *equal*-compatible), vector of type [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(:),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} for *atom*- or *vector*-style variables, or [`CHARACTER(LEN=*)`{.docutils .literal .notranslate}]{.pre} for *string*-style and compatible variables. Strings whose length is too short to hold the result will be truncated. Allocatable strings must be allocated before this function is called; see note at [`extract_global()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} regarding allocatable strings. Allocatable arrays (for *atom*- and *vector*-style data) will be reallocated on assignment.

::: {.admonition .note}
Note

LAMMPS cannot easily check if it is valid to access the data referenced by the variables (e.g., computes, fixes, or thermodynamic info), so it may fail with an error. The caller has to make certain that the data are extracted only when it is safe to evaluate the variable and thus an error and crash are avoided.
:::

------------------------------------------------------------------------

*[subroutine]{.pre} * [[set_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[str]{.pre}*[)]{.sig-paren}[](#f/_/set_variable "Link to this definition"){.headerlink}

:   Set the value of a string-style variable.

    ::: deprecated
    [Deprecated since version 7Feb2024.]{.versionmodified .deprecated}
    :::

    This function assigns a new value from the string *str* to the string-style variable *name*. If *name* does not exist or is not a string-style variable, an error is generated.

    ::: {.admonition .warning}
    Warning

    This subroutine is deprecated and [`set_string_variable()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} should be used instead.
    :::

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: name of the variable

        - **str** *\[character(len=\*)\]* :: new value to assign to the variable

    Call to[:]{.colon}

    :   [[`lammps_set_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv419lammps_set_variablePvPKcPKc "lammps_set_variable"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[set_string_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[str]{.pre}*[)]{.sig-paren}[](#f/_/set_string_variable "Link to this definition"){.headerlink}

:   Set the value of a string-style variable.

    ::: versionadded
    [Added in version 7Feb2024.]{.versionmodified .added}
    :::

    This function assigns a new value from the string *str* to the string-style variable *name*. If *name* does not exist or is not a string-style variable, an error is generated.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: name of the variable

        - **str** *\[character(len=\*)\]* :: new value to assign to the variable

    Call to[:]{.colon}

    :   [[`lammps_set_string_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv426lammps_set_string_variablePvPKcPKc "lammps_set_string_variable"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[set_internal_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[val]{.pre}*[)]{.sig-paren}[](#f/_/set_internal_variable "Link to this definition"){.headerlink}

:   Set the value of a internal-style variable.

    ::: versionadded
    [Added in version 7Feb2024.]{.versionmodified .added}
    :::

    This function assigns a new value from the floating-point number *val* to the internal-style variable *name*. If *name* does not exist or is not an internal-style variable, an error is generated.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: name of the variable

        - **val** *\[real(c_double)\]* :: new value to assign to the variable

    Call to[:]{.colon}

    :   [[`lammps_set_internal_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv428lammps_set_internal_variablePvPKcd "lammps_set_internal_variable"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[eval]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[expr]{.pre}*[)]{.sig-paren}[](#f/_/eval "Link to this definition"){.headerlink}

:   This function is a wrapper around [[`lammps_eval()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv411lammps_evalPvPKc "lammps_eval"){.reference .internal} that takes a LAMMPS equal style variable string, evaluates it and returns the resulting scalar value as a floating-point number.

    ::: versionadded
    [Added in version 4Feb2025.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   **expr** *\[character(len=\*)\]* :: string to be evaluated

    Call to[:]{.colon}

    :   [[`lammps_eval()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv411lammps_evalPvPKc "lammps_eval"){.reference .internal}

    Return[:]{.colon}

    :   **value** *\[real(c_double)\]* :: result of the evaluated string

------------------------------------------------------------------------

*[subroutine]{.pre} * [[clearstep_compute]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/clearstep_compute "Link to this definition"){.headerlink}

:   Clear whether a compute has been invoked

    ::: versionadded
    [Added in version 4Feb2025.]{.versionmodified .added}
    :::

    Call to[:]{.colon}

    :   [[`lammps_clearstep_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv424lammps_clearstep_computePv "lammps_clearstep_compute"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[addstep_compute]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[nextstep]{.pre}*[)]{.sig-paren}[](#f/_/addstep_compute "Link to this definition"){.headerlink}

:   Add timestep to list of future compute invocations if the compute has been invoked on the current timestep

    ::: versionadded
    [Added in version 4Feb2025.]{.versionmodified .added}
    :::

    overloaded for 32-bit and 64-bit integer arguments

    Parameters[:]{.colon}

    :   **nextstep** *\[integer(kind=8 or kind=4)\]* :: next timestep

    Call to[:]{.colon}

    :   [[`lammps_addstep_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv422lammps_addstep_computePvPv "lammps_addstep_compute"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[addstep_compute_all]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[nextstep]{.pre}*[)]{.sig-paren}[](#f/_/addstep_compute_all "Link to this definition"){.headerlink}

:   Add timestep to list of future compute invocations

    ::: versionadded
    [Added in version 4Feb2025.]{.versionmodified .added}
    :::

    overloaded for 32-bit and 64-bit integer arguments

    Parameters[:]{.colon}

    :   **nextstep** *\[integer(kind=8 or kind=4)\]* :: next timestep

    Call to[:]{.colon}

    :   [[`lammps_addstep_compute_all()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv426lammps_addstep_compute_allPvPv "lammps_addstep_compute_all"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather_atoms]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[count]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/gather_atoms "Link to this definition"){.headerlink}

:   This function calls [[`lammps_gather_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv419lammps_gather_atomsPvPKciiPv "lammps_gather_atoms"){.reference .internal} to gather the named atom-based entity for all atoms on all processors and return it in the vector *data*. The vector *data* will be ordered by atom ID, which requires consecutive atom IDs (1 to *natoms*).

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    If you need a similar array but have non-consecutive atom IDs, see [`gather_atoms_concat()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}; for a similar array but for a subset of atoms, see [`gather_atoms_subset()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}.

    The *data* array will be ordered in groups of *count* values, sorted by atom ID (e.g., if *name* is *x* and *count* = 3, then *data* = \[*x*(1,1), *x*(2,1), *x*(3,1), *x*(1,2), *x*(2,2), *x*(3,2), *x*(1,3), [\\(\\dots\\)]{.math .notranslate .nohighlight}\]); *data* must be [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} and will be allocated to length (*count* [\\(\\times\\)]{.math .notranslate .nohighlight} *natoms*), as queried by [`get_natoms()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}.

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: desired quantity (e.g., *x* or *mask*)

        - **count** *\[integer(c_int)\]* :: number of per-atom values you expect per atom (e.g., 1 for *type*, *mask*, or *charge*; 3 for *x*, *v*, or *f*). Use *count* = 3 with *image* if you want a single image flag unpacked into *x*/*y*/*z* components.

        - **data** *\[polymorphic,dimension(:),allocatable\]* :: array into which to store the data. Array *must* have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute and be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}). If this array is already allocated, it will be reallocated to fit the length of the incoming data. It should have type [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} if expecting integer data and [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre} if expecting floating-point data.

    Call to[:]{.colon}

    :   [[`lammps_gather_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv419lammps_gather_atomsPvPKciiPv "lammps_gather_atoms"){.reference .internal}

    ::::: {.admonition .note}
    Note

    If you want data from this function to be accessible as a two-dimensional array, you can declare a rank-2 pointer and reassign it, like so:

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        USE, INTRINSIC :: ISO_C_BINDING
        USE LIBLAMMPS
        TYPE(lammps) :: lmp
        REAL(c_double), DIMENSION(:), ALLOCATABLE, TARGET :: xdata
        REAL(c_double), DIMENSION(:,:), POINTER :: x
        ! other code to set up, etc.
        CALL lmp%gather_atoms('x',3,xdata)
        x(1:3,1:size(xdata)/3) => xdata
    :::
    ::::

    You can then access the *y*-component of atom 3 with [`x(2,3)`{.docutils .literal .notranslate}]{.pre}. See the note about array index order at [`extract_atom()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}.
    :::::

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather_atoms_concat]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[count]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/gather_atoms_concat "Link to this definition"){.headerlink}

:   This function calls [[`lammps_gather_atoms_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv426lammps_gather_atoms_concatPvPKciiPv "lammps_gather_atoms_concat"){.reference .internal} to gather the named atom-based entity for all atoms on all processors and return it in the vector *data*.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    The vector *data* will not be ordered by atom ID, and there is no restriction on the IDs being consecutive. If you need the IDs, you can do another [`gather_atoms_concat()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} with *name* set to [`id`{.docutils .literal .notranslate}]{.pre}.

    If you need a similar array but have consecutive atom IDs, see [`gather_atoms()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}; for a similar array but for a subset of atoms, see [`gather_atoms_subset()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}.

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: desired quantity (e.g., *x* or *mask*)

        - **count** *\[integer(c_int)\]* :: number of per-atom values you expect per atom (e.g., 1 for *type*, *mask*, or *charge*; 3 for *x*, *v*, or *f*). Use *count* = 3 with *image* if you want a single image flag unpacked into *x*/*y*/*z* components.

        - **data** *\[polymorphic,dimension(:),allocatable\]* :: array into which to store the data. Array *must* have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute and be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}). If this array is already allocated, it will be reallocated to fit the length of the incoming data. It should have type [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} if expecting integer data and [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre} if expecting floating-point data.

    Call to[:]{.colon}

    :   [[`lammps_gather_atoms_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv426lammps_gather_atoms_concatPvPKciiPv "lammps_gather_atoms_concat"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather_atoms_subset]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[count]{.pre}*, *[ids]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/gather_atoms_subset "Link to this definition"){.headerlink}

:   This function calls [[`lammps_gather_atoms_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv426lammps_gather_atoms_subsetPvPKciiiPiPv "lammps_gather_atoms_subset"){.reference .internal} to gather the named atom-based entity for the atoms in the array *ids* from all processors and return it in the vector *data*.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This subroutine gathers data for the requested atom IDs and stores them in a one-dimensional allocatable array. The data will be ordered by atom ID, but there is no requirement that the IDs be consecutive. If you wish to return a similar array for *all* the atoms, use [`gather_atoms()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} or [`gather_atoms_concat()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}.

    The *data* array will be in groups of *count* values, sorted by atom ID in the same order as the array *ids* (e.g., if *name* is *x*, *count* = 3, and *ids* is \[100, 57, 210\], then *data* might look like \[*x*(1,100), *x*(2,100), *x*(3,100), *x*(1,57), *x*(2,57), *x*(3,57), *x*(1,210), [\\(\\dots\\)]{.math .notranslate .nohighlight}\]; *ids* must be provided by the user, and *data* must be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}) and have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute.

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: desired quantity (e.g., *x* or *mask*)

        - **count** *\[integer(c_int)\]* :: number of per-atom values you expect per atom (e.g., 1 for *type*, *mask*, or *charge*; 3 for *x*, *v*, or *f*). Use *count* = 3 with *image* if you want a single image flag unpacked into *x*/*y*/*z* components.

        - **ids** *\[integer(c_int),dimension(:)\]* :: atom IDs corresponding to the atoms to be gathered

        - **data** *\[polymorphic,dimension(:),allocatable\]* :: array into which to store the data. Array *must* have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute and be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}). If this array is already allocated, it will be reallocated to fit the length of the incoming data. It should have type [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} if expecting integer data and [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre} if expecting floating-point data.

    Call to[:]{.colon}

    :   [[`lammps_gather_atoms_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv426lammps_gather_atoms_subsetPvPKciiiPiPv "lammps_gather_atoms_subset"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[scatter_atoms]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/scatter_atoms "Link to this definition"){.headerlink}

:   This function calls [[`lammps_scatter_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv420lammps_scatter_atomsPvPKciiPv "lammps_scatter_atoms"){.reference .internal} to scatter the named atom-based entities in *data* to all processors.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This subroutine takes data stored in a one-dimensional array supplied by the user and scatters them to all atoms on all processors. The data must be ordered by atom ID, with the requirement that the IDs be consecutive. Use [`scatter_atoms_subset()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} to scatter data for some (or all) atoms, in any order.

    The *data* array needs to be ordered in groups of *count* values, sorted by atom ID (e.g., if *name* is *x* and *count* = 3, then *data* = \[*x*(1,1), *x*(2,1), *x*(3,1), *x*(1,2), *x*(2,2), *x*(3,2), *x*(1,3), [\\(\\dots\\)]{.math .notranslate .nohighlight}\]); *data* must be of length *natoms* or 3\**natoms*.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: quantity to be scattered (e.g., *x* or *charge*)

        - **data** *\[polymorphic,dimension(:)\]* :: per-atom values packed in a one-dimensional array containing the data to be scattered. This array must have length *natoms* (e.g., for *type* or *charge*) or length *natoms*[\\({}\\times 3\\)]{.math .notranslate .nohighlight} (e.g., for *x* or *f*). The array *data* must be rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}) and be of type [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} (e.g., for *mask* or *type*) or of type [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre} (e.g., for *x* or *charge* or *f*).

    Call to[:]{.colon}

    :   [[`lammps_scatter_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv420lammps_scatter_atomsPvPKciiPv "lammps_scatter_atoms"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[scatter_atoms_subset]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[ids]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/scatter_atoms_subset "Link to this definition"){.headerlink}

:   This function calls [[`lammps_scatter_atoms_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv427lammps_scatter_atoms_subsetPvPKciiiPiPv "lammps_scatter_atoms_subset"){.reference .internal} to scatter the named atom-based entities in *data* to all processors.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This subroutine takes data stored in a one-dimensional array supplied by the user and scatters them to a subset of atoms on all processors. The array *data* contains data associated with atom IDs, but there is no requirement that the IDs be consecutive, as they are provided in a separate array, *ids*. Use [`scatter_atoms()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} to scatter data for all atoms, in order.

    The *data* array needs to be organized in groups of 1 or 3 values, depending on which quantity is being scattered, with the groups in the same order as the array *ids*. For example, if you want *data* to be the array \[*x*(1,1), *x*(2,1), *x*(3,1), *x*(1,100), *x*(2,100), *x*(3,100), *x*(1,57), *x*(2,57), *x*(3,57)\], then *ids* would be \[1, 100, 57\] and *name* would be *x*.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: quantity to be scattered (e.g., *x* or *charge*)

        - **ids** *\[integer(c_int),dimension(:)\]* :: atom IDs corresponding to the atoms being scattered

        - **data** *\[polymorphic,dimension(:)\]* :: per-atom values packed into a one-dimensional array containing the data to be scattered. This array must have either the same length as *ids* (for *mask*, *type*, etc.) or three times its length (for *x*, *f*, etc.); the array must be rank 1 and be of type [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} (e.g., for *mask* or *type*) or of type [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre} (e.g., for *charge*, *x*, or *f*).

    Call to[:]{.colon}

    :   [[`lammps_scatter_atoms_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv427lammps_scatter_atoms_subsetPvPKciiiPiPv "lammps_scatter_atoms_subset"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather_bonds]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[data]{.pre}*[)]{.sig-paren}[](#f/_/gather_bonds "Link to this definition"){.headerlink}

:   Gather type and constituent atom information for all bonds.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function copies the list of all bonds into an allocatable array. The array will be filled with (bond type, bond atom 1, bond atom 2) for each bond. The array is allocated to the right length (i.e., three times the number of bonds). The array *data* must be of the same type as the LAMMPS [`tagint`{.docutils .literal .notranslate}]{.pre} type, which is equivalent to either [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} or [`INTEGER(c_int64_t)`{.docutils .literal .notranslate}]{.pre}, depending on whether [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} was used when LAMMPS was built. If the supplied array does not match, an error will result at run-time.

    An example of how to use this routine is below:

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        PROGRAM bonds
          USE, INTRINSIC :: ISO_C_BINDING, ONLY : c_int
          USE, INTRINSIC :: ISO_FORTRAN_ENV, ONLY : OUTPUT_UNIT
          USE LIBLAMMPS
          IMPLICIT NONE
          INTEGER(c_int), DIMENSION(:), ALLOCATABLE, TARGET :: bonds
          INTEGER(c_int), DIMENSION(:,:), POINTER :: bonds_array
          TYPE(lammps) :: lmp
          INTEGER :: i
          ! other commands to initialize LAMMPS, create bonds, etc.
          CALL lmp%gather_bonds(bonds)
          bonds_array(1:3, 1:SIZE(bonds)/3) => bonds
          DO i = 1, SIZE(bonds)/3
            WRITE(OUTPUT_UNIT,'(A,1X,I4,A,I4,1X,I4)') 'bond', bonds_array(1,i), &
              '; type = ', bonds_array(2,i), bonds_array(3,i)
          END DO
        END PROGRAM bonds
    :::
    ::::

    Parameters[:]{.colon}

    :   **data** *\[integer(kind=\*),allocatable\]* :: array into which to copy the result. \*The [`KIND`{.docutils .literal .notranslate}]{.pre} parameter is either [`c_int`{.docutils .literal .notranslate}]{.pre} or, if LAMMPS was compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, kind [`c_int64_t`{.docutils .literal .notranslate}]{.pre}.

    Call to[:]{.colon}

    :   [[`lammps_gather_bonds()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv419lammps_gather_bondsPvPv "lammps_gather_bonds"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather_angles]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[data]{.pre}*[)]{.sig-paren}[](#f/_/gather_angles "Link to this definition"){.headerlink}

:   Gather type and constituent atom information for all angles.

    ::: versionadded
    [Added in version 8Feb2023.]{.versionmodified .added}
    :::

    This function copies the list of all angles into an allocatable array. The array will be filled with (angle type, angle atom 1, angle atom 2, angle atom 3) for each angle. The array is allocated to the right length (i.e., four times the number of angles). The array *data* must be of the same type as the LAMMPS [`tagint`{.docutils .literal .notranslate}]{.pre} type, which is equivalent to either [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} or [`INTEGER(c_int64_t)`{.docutils .literal .notranslate}]{.pre}, depending on whether [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} was used when LAMMPS was built. If the supplied array does not match, an error will result at run-time.

    An example of how to use this routine is below:

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        PROGRAM angles
          USE, INTRINSIC :: ISO_C_BINDING, ONLY : c_int
          USE, INTRINSIC :: ISO_FORTRAN_ENV, ONLY : OUTPUT_UNIT
          USE LIBLAMMPS
          IMPLICIT NONE
          INTEGER(c_int), DIMENSION(:), ALLOCATABLE, TARGET :: angles
          INTEGER(c_int), DIMENSION(:,:), POINTER :: angles_array
          TYPE(lammps) :: lmp
          INTEGER :: i
          ! other commands to initialize LAMMPS, create angles, etc.
          CALL lmp%gather_angles(angles)
          angles_array(1:4, 1:SIZE(angles)/4) => angles
          DO i = 1, SIZE(angles)/4
            WRITE(OUTPUT_UNIT,'(A,1X,I4,A,I4,1X,I4,1X,I4)') 'angle', angles_array(1,i), &
              '; type = ', angles_array(2,i), angles_array(3,i), angles_array(4,i)
          END DO
        END PROGRAM angles
    :::
    ::::

    Parameters[:]{.colon}

    :   **data** *\[integer(kind=\*),allocatable\]* :: array into which to copy the result. \*The [`KIND`{.docutils .literal .notranslate}]{.pre} parameter is either [`c_int`{.docutils .literal .notranslate}]{.pre} or, if LAMMPS was compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, kind [`c_int64_t`{.docutils .literal .notranslate}]{.pre}.

    Call to[:]{.colon}

    :   [[`lammps_gather_angles()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv420lammps_gather_anglesPvPv "lammps_gather_angles"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[self]{.pre}*, *[name]{.pre}*, *[count]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/gather "Link to this definition"){.headerlink}

:   Gather the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entities from all processes, in order by atom ID.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This subroutine gathers data from all processes and stores them in a one-dimensional allocatable array. The array *data* will be ordered by atom ID, which requires consecutive IDs (1 to *natoms*). If you need a similar array but for non-consecutive atom IDs, see [[`lammps_gather_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv420lammps_gather_concatPvPKciiPv "lammps_gather_concat"){.reference .internal}; for a similar array but for a subset of atoms, see [[`lammps_gather_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv420lammps_gather_subsetPvPKciiiPiPv "lammps_gather_subset"){.reference .internal}.

    The *data* array will be ordered in groups of *count* values, sorted by atom ID (e.g., if *name* is *x*, then *data* is \[x(1,1), x(2,1), x(3,1), x(1,2), x(2,2), x(3,2), x(1,3), [\\(\\dots\\)]{.math .notranslate .nohighlight}\]); *data* must be [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} and will be allocated to length (*count*[\\({}\\times{}\\)]{.math .notranslate .nohighlight}*natoms*), as queried by [`get_natoms()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}.

    This function will return an error if fix or compute data are requested and the fix or compute ID given does not have per-atom data. See the note about re-interpreting the vector as a matrix at [`gather_atoms()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}.

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: desired quantity (e.g., "x" or "mask" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with *count* = 1, "d2_name" or "i2_name" for fix property/atom vectors with *count*[\\({}\> 1\\)]{.math .notranslate .nohighlight})

        - **count** *\[integer(c_int)\]* :: number of per-atom values (e.g., 1 for *type* or *charge*, 3 for *x* or *f*); use *count* = 3 with *image* if you want the image flags unpacked into (*x*,*y*,*z*) components.

        - **data** *\[real(c_double),dimension(:),allocatable\]* :: array into which to store the data. Array *must* have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute and be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}). If this array is already allocated, it will be reallocated to fit the length of the incoming data.

    Call to[:]{.colon}

    :   [[`lammps_gather()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv413lammps_gatherPvPKciiPv "lammps_gather"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather_dihedrals]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[data]{.pre}*[)]{.sig-paren}[](#f/_/gather_dihedrals "Link to this definition"){.headerlink}

:   Gather type and constituent atom information for all dihedrals.

    ::: versionadded
    [Added in version 8Feb2023.]{.versionmodified .added}
    :::

    This function copies the list of all dihedrals into an allocatable array. The array will be filled with (dihedral type, dihedral atom 1, dihedral atom 2, dihedral atom 3, dihedral atom 4) for each dihedral. The array is allocated to the right length (i.e., five times the number of dihedrals). The array *data* must be of the same type as the LAMMPS [`tagint`{.docutils .literal .notranslate}]{.pre} type, which is equivalent to either [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} or [`INTEGER(c_int64_t)`{.docutils .literal .notranslate}]{.pre}, depending on whether [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} was used when LAMMPS was built. If the supplied array does not match, an error will result at run-time.

    An example of how to use this routine is below:

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        PROGRAM dihedrals
          USE, INTRINSIC :: ISO_C_BINDING, ONLY : c_int
          USE, INTRINSIC :: ISO_FORTRAN_ENV, ONLY : OUTPUT_UNIT
          USE LIBLAMMPS
          IMPLICIT NONE
          INTEGER(c_int), DIMENSION(:), ALLOCATABLE, TARGET :: dihedrals
          INTEGER(c_int), DIMENSION(:,:), POINTER :: dihedrals_array
          TYPE(lammps) :: lmp
          INTEGER :: i
          ! other commands to initialize LAMMPS, create dihedrals, etc.
          CALL lmp%gather_dihedrals(dihedrals)
          dihedrals_array(1:5, 1:SIZE(dihedrals)/5) => dihedrals
          DO i = 1, SIZE(dihedrals)/5
            WRITE(OUTPUT_UNIT,'(A,1X,I4,A,I4,1X,I4,1X,I4,1X,I4)') 'dihedral', dihedrals_array(1,i), &
              '; type = ', dihedrals_array(2,i), dihedrals_array(3,i), dihedrals_array(4,i), dihedrals_array(5,i)
          END DO
        END PROGRAM dihedrals
    :::
    ::::

    Parameters[:]{.colon}

    :   **data** *\[integer(kind=\*),allocatable\]* :: array into which to copy the result. \*The [`KIND`{.docutils .literal .notranslate}]{.pre} parameter is either [`c_int`{.docutils .literal .notranslate}]{.pre} or, if LAMMPS was compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, kind [`c_int64_t`{.docutils .literal .notranslate}]{.pre}.

    Call to[:]{.colon}

    :   [[`lammps_gather_dihedrals()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv423lammps_gather_dihedralsPvPv "lammps_gather_dihedrals"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather_impropers]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[data]{.pre}*[)]{.sig-paren}[](#f/_/gather_impropers "Link to this definition"){.headerlink}

:   Gather type and constituent atom information for all impropers.

    ::: versionadded
    [Added in version 8Feb2023.]{.versionmodified .added}
    :::

    This function copies the list of all impropers into an allocatable array. The array will be filled with (improper type, improper atom 1, improper atom 2, improper atom 3, improper atom 4) for each improper. The array is allocated to the right length (i.e., five times the number of impropers). The array *data* must be of the same type as the LAMMPS [`tagint`{.docutils .literal .notranslate}]{.pre} type, which is equivalent to either [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} or [`INTEGER(c_int64_t)`{.docutils .literal .notranslate}]{.pre}, depending on whether [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} was used when LAMMPS was built. If the supplied array does not match, an error will result at run-time.

    An example of how to use this routine is below:

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        PROGRAM impropers
          USE, INTRINSIC :: ISO_C_BINDING, ONLY : c_int
          USE, INTRINSIC :: ISO_FORTRAN_ENV, ONLY : OUTPUT_UNIT
          USE LIBLAMMPS
          IMPLICIT NONE
          INTEGER(c_int), DIMENSION(:), ALLOCATABLE, TARGET :: impropers
          INTEGER(c_int), DIMENSION(:,:), POINTER :: impropers_array
          TYPE(lammps) :: lmp
          INTEGER :: i
          ! other commands to initialize LAMMPS, create impropers, etc.
          CALL lmp%gather_impropers(impropers)
          impropers_array(1:5, 1:SIZE(impropers)/5) => impropers
          DO i = 1, SIZE(impropers)/5
            WRITE(OUTPUT_UNIT,'(A,1X,I4,A,I4,1X,I4,1X,I4,1X,I4)') 'improper', impropers_array(1,i), &
              '; type = ', impropers_array(2,i), impropers_array(3,i), impropers_array(4,i), impropers_array(5,i)
          END DO
        END PROGRAM impropers
    :::
    ::::

    Parameters[:]{.colon}

    :   **data** *\[integer(kind=\*),allocatable\]* :: array into which to copy the result. \*The [`KIND`{.docutils .literal .notranslate}]{.pre} parameter is either [`c_int`{.docutils .literal .notranslate}]{.pre} or, if LAMMPS was compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, kind [`c_int64_t`{.docutils .literal .notranslate}]{.pre}.

    Call to[:]{.colon}

    :   [[`lammps_gather_impropers()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv423lammps_gather_impropersPvPv "lammps_gather_impropers"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather_concat]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[self]{.pre}*, *[name]{.pre}*, *[count]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/gather_concat "Link to this definition"){.headerlink}

:   Gather the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entities from all processes, unordered.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This subroutine gathers data for all atoms and stores them in a one-dimensional allocatable array. The data will be a concatenation of chunks from each processor's owned atoms, in whatever order the atoms are in on each processor. This process has no requirement that the atom IDs be consecutive. If you need the ID of each atom, you can do another call to either [`gather_atoms_concat()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} or [`gather_concat()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} with *name* set to [`id`{.docutils .literal .notranslate}]{.pre}. If you have consecutive IDs and want the data to be in order, use [`gather()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}; for a similar array but for a subset of atoms, use [`gather_subset()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}.

    The *data* array will be in groups of *count* values, with *natoms* groups total, but not in order by atom ID (e.g., if *name* is *x* and *count* is 3, then *data* might be something like \[x(1,11), x(2,11), x(3,11), x(1,3), x(2,3), x(3,3), x(1,5), [\\(\\dots\\)]{.math .notranslate .nohighlight}\]); *data* must be [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} and will be allocated to length (*count* [\\(\\times\\)]{.math .notranslate .nohighlight} *natoms*), as queried by [`get_natoms()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}.

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: desired quantity (e.g., "x" or "mask" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with *count* = 1, "d2_name" or "i2_name" for fix property/atom vectors with *count*[\\({}\> 1\\)]{.math .notranslate .nohighlight})

        - **count** *\[integer(c_int)\]* :: number of per-atom values you expect per atom (e.g., 1 for *type*, *mask*, or *charge*; 3 for *x*, *v*, or *f*). Use *count* = 3 with *image* if you want a single image flag unpacked into *x*/*y*/*z* components.

        - **data** *\[polymorphic,dimension(:),allocatable\]* :: array into which to store the data. Array *must* have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute and be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}). If this array is already allocated, it will be reallocated to fit the length of the incoming data. It should have type [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} if expecting integer data and [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre} if expecting floating-point data.

    Call to[:]{.colon}

    :   [[`lammps_gather_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv420lammps_gather_concatPvPKciiPv "lammps_gather_concat"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[gather_subset]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[count]{.pre}*, *[ids]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/gather_subset "Link to this definition"){.headerlink}

:   Gather the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entities from all processes for a subset of atoms.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This subroutine gathers data for the requested atom IDs and stores them in a one-dimensional allocatable array. The data will be ordered by atom ID, but there is no requirement that the IDs be consecutive. If you wish to return a similar array for *all* the atoms, use [`gather()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} or [`gather_concat()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}.

    The *data* array will be in groups of *count* values, sorted by atom ID in the same order as the array *ids* (e.g., if *name* is *x*, *count* = 3, and *ids* is \[100, 57, 210\], then *data* might look like \[*x*(1,100), *x*(2,100), *x*(3,100), *x*(1,57), *x*(2,57), *x*(3,57), *x*(1,210), [\\(\\dots\\)]{.math .notranslate .nohighlight}\]); *ids* must be provided by the user, and *data* must have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute and be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}). If *data* is already allocated, it will be reallocated to fit the length of the incoming data.

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: quantity to be scattered

        - **ids** *\[integer(c_int),dimension(:)\]* :: atom IDs corresponding to the atoms being scattered (e.g., "x" or "f" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with *count* = 1, "d2_name" or "i2_name" for fix property/atom vectors with *count*[\\({} \> 1\\)]{.math .notranslate .nohighlight})

        - **count** *\[integer(c_int)\]* :: number of per-atom values you expect per atom (e.g., 1 for *type*, *mask*, or *charge*; 3 for *x*, *v*, or *f*). Use *count* = 3 with *image* if you want a single image flag unpacked into *x*/*y*/*z* components.

        - **data** *\[polymorphic,dimension(:),allocatable\]* :: per-atom values packed into a one-dimensional array containing the data to be scattered. This array must have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute and will be allocated either to the same length as *ids* (for *mask*, *type*, etc.) or to three times its length (for *x*, *f*, etc.); the array must be rank 1 and be of type [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} (e.g., for *mask* or *type*) or of type [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre} (e.g., for *charge*, *x*, or *f*).

    Call to[:]{.colon}

    :   [[`lammps_gather_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv420lammps_gather_subsetPvPKciiiPiPv "lammps_gather_subset"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[scatter]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/scatter "Link to this definition"){.headerlink}

:   This function calls [[`lammps_scatter()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv414lammps_scatterPvPKciiPv "lammps_scatter"){.reference .internal} to scatter the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entity in *data* to all processes.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This subroutine takes data stored in a one-dimensional array supplied by the user and scatters them to all atoms on all processes. The data must be ordered by atom ID, with the requirement that the IDs be consecutive. Use [`scatter_subset()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} to scatter data for some (or all) atoms, unordered.

    The *data* array needs to be ordered in groups of *count* values, sorted by atom ID (e.g., if *name* is *x* and *count* = 3, then *data* = \[*x*(1,1), *x*(2,1), *x*(3,1), *x*(1,2), *x*(2,2), *x*(3,2), *x*(1,3), [\\(\\dots\\)]{.math .notranslate .nohighlight}\]); *data* must be of length (*count* [\\(\\times\\)]{.math .notranslate .nohighlight} *natoms*).

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: desired quantity (e.g., "x" or "f" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with *count* = 1, "d2_name" or "i2_name" for fix property/atom vectors with *count*[\\({} \> 1\\)]{.math .notranslate .nohighlight})

        - **data** *\[polymorphic,dimension(:)\]* :: per-atom values packed in a one-dimensional array; *data* should be of type [`INTEGER(c_int)`{.docutils .literal .notranslate}]{.pre} or [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}, depending on the type of data being scattered, and be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}).

    Call to[:]{.colon}

    :   [[`lammps_scatter()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv414lammps_scatterPvPKciiPv "lammps_scatter"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[scatter_subset]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*, *[ids]{.pre}*, *[data]{.pre}*[)]{.sig-paren}[](#f/_/scatter_subset "Link to this definition"){.headerlink}

:   This function calls [[`lammps_scatter_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv421lammps_scatter_subsetPvPKciiiPiPv "lammps_scatter_subset"){.reference .internal} to scatter the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entities in *data* from a subset of atoms to all processes.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This subroutine takes data stored in a one-dimensional array supplied by the user and scatters them to a subset of atoms on all processes. The array *data* contains data associated with atom IDs, but there is no requirement that the IDs be consecutive, as they are provided in a separate array. Use [`scatter()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} to scatter data for all atoms, in order.

    The *data* array needs to be organized in groups of *count* values, with the groups in the same order as the array *ids*. For example, if you want *data* to be the array \[x(1,1), x(2,1), x(3,1), x(1,100), x(2,100), x(3,100), x(1,57), x(2,57), x(3,57)\], then *count* = 3 and *ids* = \[1, 100, 57\].

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **name** *\[character(len=\*)\]* :: desired quantity (e.g., "x" or "mask" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with *count* = 1, "d2_name" or "i2_name" for fix property/atom vectors with *count*[\\({}\> 1\\)]{.math .notranslate .nohighlight})

        - **ids** *\[integer(c_int)\]* :: list of atom IDs to scatter data for

        - **data** *\[polymorphic* *,dimension(:)\]* :: per-atom values packed in a one-dimensional array of length *size(ids)* \* *count*.

    Call to[:]{.colon}

    :   [[`lammps_scatter_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv421lammps_scatter_subsetPvPKciiiPiPv "lammps_scatter_subset"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[create_atoms]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[\[id,\]]{.pre} [type,]{.pre} [x,]{.pre} [\[v,\]]{.pre} [\[image,\]]{.pre} [\[bexpand\]]{.pre}*[)]{.sig-paren}[](#f/_/create_atoms "Link to this definition"){.headerlink}

:   This method calls [[`lammps_create_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv419lammps_create_atomsPviPKiPKiPKdPKdPKii "lammps_create_atoms"){.reference .internal} to create additional atoms from a given list of coordinates and a list of atom types. Additionally, the atom IDs, velocities, and image flags may be provided.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   - **type** *\[integer(c_int),dimension(N)\]* :: vector of [\\(N\\)]{.math .notranslate .nohighlight} atom types (required/see note below)

        - **x** *\[real(c_double),dimension(3N)\]* :: vector of [\\(3N\\ x/y/z\\)]{.math .notranslate .nohighlight} positions of the new atoms, arranged as [\\(\[x_1,y_1,z_1,x_2,y_2,\\dotsc\]\\)]{.math .notranslate .nohighlight} (required/see note below)

    Options[:]{.colon}

    :   - **id** *\[integer(kind=\*),dimension(N),optional\]* :: vector of [\\(N\\)]{.math .notranslate .nohighlight} atom IDs; if absent, LAMMPS will generate them for you. \*The [`KIND`{.docutils .literal .notranslate}]{.pre} parameter should be [`c_int`{.docutils .literal .notranslate}]{.pre} unless LAMMPS was compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, in which case it should be [`c_int64_t`{.docutils .literal .notranslate}]{.pre}.

        - **v** *\[real(c_double),dimension(3N),optional\]* :: vector of [\\(3N\\)]{.math .notranslate .nohighlight} *x*/*y*/*z* velocities of the new atoms, arranged as [\\(\[v\_{1,x},v\_{1,y},v\_{1,z},v\_{2,x}, \\dotsc\]\\)]{.math .notranslate .nohighlight}; if absent, they will be set to zero

        - **image** *\[integer(kind=\*),dimension(N),optional\]* :: vector of [\\(N\\)]{.math .notranslate .nohighlight} image flags; if absent, they are set to zero. \*The [`KIND`{.docutils .literal .notranslate}]{.pre} parameter should be [`c_int`{.docutils .literal .notranslate}]{.pre} unless LAMMPS was compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, in which case it should be [`c_int64_t`{.docutils .literal .notranslate}]{.pre}. See note below.

        - **bexpand** *\[logical,optional\]* :: if [`.TRUE.`{.docutils .literal .notranslate}]{.pre}, atoms outside of shrink-wrap boundaries will be created, not dropped, and the box dimensions will be extended. Default is [`.FALSE.`{.docutils .literal .notranslate}]{.pre}

    Return[:]{.colon}

    :   **atoms** *\[integer(c_int)\]* :: number of created atoms

    Call to[:]{.colon}

    :   [[`lammps_create_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv419lammps_create_atomsPviPKiPKiPKdPKdPKii "lammps_create_atoms"){.reference .internal}

    ::::: {.admonition .note}
    Note

    The *type* and *x* arguments are required, but they are declared [`OPTIONAL`{.docutils .literal .notranslate}]{.pre} in the module because making them mandatory would require *id* to be present as well. To have LAMMPS generate the ids for you, use a call something like

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        lmp%create_atoms(type=new_types, x=new_xs)
    :::
    ::::
    :::::

    ::: {.admonition .note}
    Note

    When LAMMPS has been compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, it is not possible to include the *image* parameter but omit the *id* parameter. Either *id* must be present, or both *id* and *image* must be absent. This is required because having all arguments be optional in both generic functions creates an ambiguous interface. This limitation does not exist if LAMMPS was not compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.
    :::

------------------------------------------------------------------------

*[subroutine]{.pre} * [[create_molecule]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*, *[jsonstr]{.pre}*[)]{.sig-paren}[](#f/_/create_molecule "Link to this definition"){.headerlink}

:   Add molecule template from string with JSON data

    ::: versionadded
    [Added in version 22Jul2025.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: desired molecule-ID

        - **jsonstr** *\[character(len=\*)\]* :: string with JSON data defining the molecule template

    Call to[:]{.colon}

    :   [[`lammps_create_molecule()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv422lammps_create_moleculePvPKcPKc "lammps_create_molecule"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[find_pair_neighlist]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[style\[,]{.pre} [exact\]\[,]{.pre} [nsub\]\[,]{.pre} [reqid\]]{.pre}*[)]{.sig-paren}[](#f/_/find_pair_neighlist "Link to this definition"){.headerlink}

:   Find index of a neighbor list requested by a pair style.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function determines which of the available neighbor lists for pair styles matches the given conditions. It first matches the style name. If *exact* is [`.TRUE.`{.docutils .literal .notranslate}]{.pre}, the name must match exactly; if [`.FALSE.`{.docutils .literal .notranslate}]{.pre}, a regular expression or sub-string match is done. If the pair style is *hybrid* or *hybrid/overlay*, the style is matched against the sub-styles instead. If the same pair style is used multiple times as a sub-style, the *nsub* argument must be [\\(\> 0\\)]{.math .notranslate .nohighlight}; this argument represents the *n*th instance of the sub-style (same as for the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command, for example). In that case, *nsub*[\\({} = 0\\)]{.math .notranslate .nohighlight} will not produce a match, and the function will return [\\(-1\\)]{.math .notranslate .nohighlight}.

    The final condition to be checked is the request ID (*reqid*). This will usually be zero, but some pair styles request multiple neighbor lists and set the request ID to a value greater than zero.

    Parameters[:]{.colon}

    :   **style** *\[character(len=\*)\]* :: String used to search for pair style instance.

    Options[:]{.colon}

    :   - **exact** *\[logical,optional\]* :: Flag to control whether style should match exactly or only a regular expression/sub-string match is applied. Default: [`.TRUE.`{.docutils .literal .notranslate}]{.pre}.

        - **nsub** *\[integer(c_int),optional\]* :: Match *nsub*th hybrid sub-style instance of the same style. Default: 0.

        - **reqid** *\[integer(c_int),optional\]* :: Request ID to identify the neighbor list in case there are multiple requests from the same pair style instance. Default: 0.

    Call to[:]{.colon}

    :   [[`lammps_find_pair_neighlist()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_neighbor.md#_CPPv426lammps_find_pair_neighlistPvPKciii "lammps_find_pair_neighlist"){.reference .internal}

    Return[:]{.colon}

    :   **index** *\[integer(c_int)\]* :: Neighbor list index if found, otherwise [\\(-1\\)]{.math .notranslate .nohighlight}.

------------------------------------------------------------------------

*[function]{.pre} * [[find_fix_neighlist]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*[\[]{.optional}, *[reqid]{.pre}*[\]]{.optional}[)]{.sig-paren}[](#f/_/find_fix_neighlist "Link to this definition"){.headerlink}

:   Find index of a neighbor list requested by a fix.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    The neighbor list request from a fix is identified by the fix ID and the request ID. The request ID is typically zero, but will be [\\(\>0\\)]{.math .notranslate .nohighlight} for fixes with multiple neighbor list requests.

    Parameters[:]{.colon}

    :   **id** *\[character(len=\*)\]* :: Identifier of fix instance

    Options[:]{.colon}

    :   **reqid** *\[integer(c_int),optional\]* :: request ID to identify the neighbor list in cases in which there are multiple requests from the same fix. Default: 0.

    Call to[:]{.colon}

    :   [[`lammps_find_fix_neighlist()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_neighbor.md#_CPPv425lammps_find_fix_neighlistPvPKci "lammps_find_fix_neighlist"){.reference .internal}

    Return[:]{.colon}

    :   **index** *\[integer(c_int)\]* :: neighbor list index if found, otherwise [\\(-1\\)]{.math .notranslate .nohighlight}

------------------------------------------------------------------------

*[function]{.pre} * [[find_compute_neighlist]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*[\[]{.optional}, *[reqid]{.pre}*[\]]{.optional}[)]{.sig-paren}[](#f/_/find_compute_neighlist "Link to this definition"){.headerlink}

:   Find index of a neighbor list requested by a compute.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    The neighbor list request from a compute is identified by the compute ID and the request ID. The request ID is typically zero, but will be [\\(\> 0\\)]{.math .notranslate .nohighlight} in case a compute has multiple neighbor list requests.

    Parameters[:]{.colon}

    :   **id** *\[character(len=\*)\]* :: Identifier of compute instance.

    Options[:]{.colon}

    :   **reqid** *\[integer(c_int),optional\]* :: request ID to identify the neighbor list in cases in which there are multiple requests from the same compute. Default: 0.

    Call to[:]{.colon}

    :   [[`lammps_find_compute_neighlist()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_neighbor.md#_CPPv429lammps_find_compute_neighlistPvPKci "lammps_find_compute_neighlist"){.reference .internal}

    Return[:]{.colon}

    :   **index** *\[integer(c_int)\]* :: neighbor list index if found, otherwise [\\(-1\\)]{.math .notranslate .nohighlight}.

------------------------------------------------------------------------

*[function]{.pre} * [[neighlist_num_elements]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[idx]{.pre}*[)]{.sig-paren}[](#f/_/neighlist_num_elements "Link to this definition"){.headerlink}

:   Return the number of entries in the neighbor list with the given index.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   **idx** *\[integer(c_int)\]* :: neighbor list index

    Call to[:]{.colon}

    :   [[`lammps_neighlist_num_elements()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_neighbor.md#_CPPv429lammps_neighlist_num_elementsPvi "lammps_neighlist_num_elements"){.reference .internal} [[`lammps_neighlist_num_elements()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_neighbor.md#_CPPv429lammps_neighlist_num_elementsPvi "lammps_neighlist_num_elements"){.reference .internal}

    Return[:]{.colon}

    :   **inum** *\[integer(c_int)\]* :: number of entries in neighbor list, or [\\(-1\\)]{.math .notranslate .nohighlight} if *idx* is not a valid index.

------------------------------------------------------------------------

*[subroutine]{.pre} * [[neighlist_element_neighbors]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[idx]{.pre}*, *[element]{.pre}*, *[iatom]{.pre}*, *[neighbors]{.pre}*[)]{.sig-paren}[](#f/_/neighlist_element_neighbors "Link to this definition"){.headerlink}

:   Return atom local index, number of neighbors, and array of neighbor local atom indices of a neighbor list entry.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   - **idx** *\[integer(c_int)\]* :: index of this neighbor list in the list of all neighbor lists

        - **element** *\[integer(c_int)\]* :: index of this neighbor list entry

        - **iatom** *\[integer(c_int)\]* :: local atom index (i.e., in the range \[1,nlocal+nghost\]; -1 if invalid or element value

        - **neighbors** *\[integer(c_int),dimension(:),pointer\]* :: pointer to an array of neighboring atom local indices

    Call to[:]{.colon}

    :   [[`lammps_neighlist_element_neighbors()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_neighbor.md#_CPPv434lammps_neighlist_element_neighborsPviiPiPiPPi "lammps_neighlist_element_neighbors"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[version]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/version "Link to this definition"){.headerlink}

:   This method returns the numeric LAMMPS version like [[`lammps_version()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv414lammps_versionPv "lammps_version"){.reference .internal} does.

    Call to[:]{.colon}

    :   [[`lammps_version()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv414lammps_versionPv "lammps_version"){.reference .internal}

    Return[:]{.colon}

    :   **version** *\[integer\]* :: LAMMPS version

------------------------------------------------------------------------

*[subroutine]{.pre} * [[get_os_info]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[buffer]{.pre}*[)]{.sig-paren}[](#f/_/get_os_info "Link to this definition"){.headerlink}

:   This function can be used to retrieve detailed information about the hosting operating system and compiler/runtime environment.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    A suitable buffer has to be provided. The assembled text will be truncated so as not to overflow this buffer. The string is typically a few hundred bytes long.

    Parameters[:]{.colon}

    :   **buffer** *\[character(len=\*)\]* :: string that will house the information.

    Call to[:]{.colon}

    :   [[`lammps_get_os_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv418lammps_get_os_infoPci "lammps_get_os_info"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[config_has_mpi_support]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/config_has_mpi_support "Link to this definition"){.headerlink}

:   This function is used to query whether LAMMPS was compiled with a real MPI library or in serial.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Call to[:]{.colon}

    :   [[`lammps_config_has_mpi_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv429lammps_config_has_mpi_supportv "lammps_config_has_mpi_support"){.reference .internal}

    Return[:]{.colon}

    :   **has_mpi** *\[logical\]* :: [`.FALSE.`{.docutils .literal .notranslate}]{.pre} when compiled with STUBS, [`.TRUE.`{.docutils .literal .notranslate}]{.pre} if complied with MPI.

------------------------------------------------------------------------

*[function]{.pre} * [[config_has_omp_support]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/config_has_omp_support "Link to this definition"){.headerlink}

:   This function is used to query whether LAMMPS was compiled with OpenMP enabled.

    ::: versionadded
    [Added in version 10Sep2025.]{.versionmodified .added}
    :::

    Call to[:]{.colon}

    :   [[`lammps_config_has_omp_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv429lammps_config_has_omp_supportv "lammps_config_has_omp_support"){.reference .internal}

    Return[:]{.colon}

    :   **has_omp** *\[logical\]* :: [`.TRUE.`{.docutils .literal .notranslate}]{.pre} when compiled with OpenMP enabled, [`.FALSE.`{.docutils .literal .notranslate}]{.pre} if not.

------------------------------------------------------------------------

*[function]{.pre} * [[config_has_gzip_support]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/config_has_gzip_support "Link to this definition"){.headerlink}

:   Check if the LAMMPS library supports reading or writing compressed files via a pipe to gzip or similar compression programs.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Several LAMMPS commands (e.g., [[read_data command]{.doc}]read_data.md){.reference .internal}, [[write_data command]{.doc}]write_data.md){.reference .internal}, [[dump styles atom, custom, and xyz]{.doc}]dump.md){.reference .internal}) support reading and writing compressed files via creating a pipe to the [`gzip`{.docutils .literal .notranslate}]{.pre} program. This function checks whether this feature was [[enabled at compile time]{.std .std-ref}]Build_settings.md#gzip){.reference .internal}. It does **not** check whether [`gzip`{.docutils .literal .notranslate}]{.pre} or any other supported compression programs themselves are installed and usable.

    Call to[:]{.colon}

    :   [[`lammps_config_has_gzip_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv430lammps_config_has_gzip_supportv "lammps_config_has_gzip_support"){.reference .internal}

    Return[:]{.colon}

    :   **has_gzip** *\[logical\]*

------------------------------------------------------------------------

*[function]{.pre} * [[config_has_png_support]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/config_has_png_support "Link to this definition"){.headerlink}

:   Check if the LAMMPS library supports writing PNG format images.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    The LAMMPS [[dump style image]{.doc}]dump_image.md){.reference .internal} supports writing multiple image file formats. Most of them, however, need support from an external library, and using that has to be [[enabled at compile time]{.std .std-ref}]Build_extras.md#graphics){.reference .internal}. This function checks whether support for the [PNG image file format](https://en.wikipedia.org/wiki/Portable_Network_Graphics){.reference .external} is available in the current LAMMPS library.

    Call to[:]{.colon}

    :   [[`lammps_config_has_png_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv429lammps_config_has_png_supportv "lammps_config_has_png_support"){.reference .internal}

    Return[:]{.colon}

    :   **has_png** *\[logical\]*

------------------------------------------------------------------------

*[function]{.pre} * [[config_has_jpeg_support]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/config_has_jpeg_support "Link to this definition"){.headerlink}

:   Check if the LAMMPS library supports writing JPEG format images.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    The LAMMPS [[dump style image]{.doc}]dump_image.md){.reference .internal} supports writing multiple image file formats. Most of them, however, need support from an external library, and using that has to be [[enabled at compile time]{.std .std-ref}]Build_extras.md#graphics){.reference .internal}. This function checks whether support for the [JPEG image file format](https://jpeg.org/jpeg/){.reference .external} is available in the current LAMMPS library.

    Call to[:]{.colon}

    :   [[`lammps_config_has_jpeg_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv430lammps_config_has_jpeg_supportv "lammps_config_has_jpeg_support"){.reference .internal}

    Return[:]{.colon}

    :   **has_jpeg** *\[logical\]*

------------------------------------------------------------------------

*[function]{.pre} * [[config_has_ffmpeg_support]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/config_has_ffmpeg_support "Link to this definition"){.headerlink}

:   Check if the LAMMPS library supports creating movie files via a pipe to ffmpeg.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    The LAMMPS [[dump style movie]{.doc}]dump_image.md){.reference .internal} supports generating movies from images on-the-fly via creating a pipe to the [ffmpeg](https://ffmpeg.org/){.reference .external} program. This function checks whether this feature was [[enabled at compile time]{.std .std-ref}]Build_extras.md#graphics){.reference .internal}. It does **not** check whether the [`ffmpeg`{.docutils .literal .notranslate}]{.pre} itself is installed and usable.

    Call to[:]{.colon}

    :   [[`lammps_config_has_ffmpeg_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv432lammps_config_has_ffmpeg_supportv "lammps_config_has_ffmpeg_support"){.reference .internal}

    Return[:]{.colon}

    :   **has_ffmpeg** *\[logical\]*

------------------------------------------------------------------------

*[function]{.pre} * [[config_has_exceptions]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/config_has_exceptions "Link to this definition"){.headerlink}

:   Check whether LAMMPS errors will throw C++ exceptions.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    When using the library interface, the library interface functions will "catch" exceptions, and then the error status can be checked by calling [`has_error()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}. The most recent error message can be retrieved via [`get_last_error_message()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}. This allows to restart a calculation or delete and recreate the LAMMPS instance when a C++ exception occurs. One application of using exceptions this way is [LAMMPS-GUI](https://lammps-gui.lammps.org){.reference .external}

    Call to[:]{.colon}

    :   [[`lammps_config_has_exceptions()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv428lammps_config_has_exceptionsv "lammps_config_has_exceptions"){.reference .internal}

    Return[:]{.colon}

    :   **has_exceptions** *\[logical\]*

------------------------------------------------------------------------

*[function]{.pre} * [[config_has_package]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[name]{.pre}*[)]{.sig-paren}[](#f/_/config_has_package "Link to this definition"){.headerlink}

:   Check whether a specific package has been included in LAMMPS

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function checks whether the LAMMPS library in use includes the specific [[LAMMPS package]{.doc}]Packages.md){.reference .internal} provided as argument.

    Call to[:]{.colon}

    :   [[`lammps_config_has_package()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv425lammps_config_has_packagePKc "lammps_config_has_package"){.reference .internal}

    Return[:]{.colon}

    :   **has_package** *\[logical\]*

------------------------------------------------------------------------

*[function]{.pre} * [[config_package_count]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/config_package_count "Link to this definition"){.headerlink}

:   Count the number of installed packages in the LAMMPS library.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function counts how many [[LAMMPS packages]{.doc}]Packages.md){.reference .internal} are included in the LAMMPS library in use. It directly calls the C library function [[`lammps_config_package_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv427lammps_config_package_countv "lammps_config_package_count"){.reference .internal}.

    Call to[:]{.colon}

    :   [[`lammps_config_package_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv427lammps_config_package_countv "lammps_config_package_count"){.reference .internal}

    Return[:]{.colon}

    :   **npackages** *\[integer(c_int)\]* :: number of packages installed

------------------------------------------------------------------------

*[subroutine]{.pre} * [[config_package_name]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[idx]{.pre}*, *[buffer]{.pre}*[)]{.sig-paren}[](#f/_/config_package_name "Link to this definition"){.headerlink}

:   Get the name of a package in the list of installed packages in the LAMMPS library.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This subroutine copies the name of the package with the index *idx* into the provided string *buffer*. If the name of the package exceeds the length of the buffer, it will be truncated accordingly. If the index is out of range, *buffer* is set to an empty string.

    Parameters[:]{.colon}

    :   - **idx** *\[integer(c_int)\]* :: index of the package in the list of included packages [\\((0 \\le idx \< \\text{package count})\\)]{.math .notranslate .nohighlight}

        - **buffer** *\[character(len=\*)\]* :: string to hold the name of the package

    Call to[:]{.colon}

    :   [[`lammps_config_package_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv426lammps_config_package_nameiPci "lammps_config_package_name"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[installed_packages]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[package]{.pre}*[\[]{.optional}, *[length]{.pre}*[\]]{.optional}[)]{.sig-paren}[](#f/_/installed_packages "Link to this definition"){.headerlink}

:   Obtain a list of the names of enabled packages in the LAMMPS shared library and store it in *package*.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function is analogous to the [[`installed_packages`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}]Python_module.md#lammps.lammps.installed_packages "lammps.lammps.installed_packages"){.reference .internal} function in the Python API. The optional argument *length* sets the length of each string in the vector *package* (default: 31).

    Parameters[:]{.colon}

    :   **package** *\[character(len=:),dimension(:),allocatable\]* :: list of packages; *must* have the [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre} attribute and be of rank 1 (i.e., [`DIMENSION(:)`{.docutils .literal .notranslate}]{.pre}) with allocatable length.

    Options[:]{.colon}

    :   **length** *\[integer,optional\]* :: length of each string in the list. Default: 31.

    Call to[:]{.colon}

    :   [[`lammps_config_package_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv427lammps_config_package_countv "lammps_config_package_count"){.reference .internal} [[`lammps_config_package_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv426lammps_config_package_nameiPci "lammps_config_package_name"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[config_accelerator]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[package]{.pre}*, *[category]{.pre}*, *[setting]{.pre}*[)]{.sig-paren}[](#f/_/config_accelerator "Link to this definition"){.headerlink}

:   This function calls [[`lammps_config_accelerator()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv425lammps_config_acceleratorPKcPKcPKc "lammps_config_accelerator"){.reference .internal} to check the availability of compile time settings of included [[accelerator packages]{.doc}]Speed_packages.md){.reference .internal} in LAMMPS.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Supported packages names are "GPU", "KOKKOS", "INTEL", and "OPENMP". Supported categories are "api" with possible settings "cuda", "hip", "phi", "pthreads", "opencl", "openmp", and "serial"; and "precision" with possible settings "double", "mixed", and "single".

    Parameters[:]{.colon}

    :   - **package** *\[character(len=\*)\]* :: string with the name of the accelerator package

        - **category** *\[character(len=\*)\]* :: string with the name of the setting

        - **setting** *\[character(len=\*)\]* :: string with the name of the specific setting

    Call to[:]{.colon}

    :   [[`lammps_config_accelerator()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv425lammps_config_acceleratorPKcPKcPKc "lammps_config_accelerator"){.reference .internal}

    Return[:]{.colon}

    :   **available** *\[logical\]* :: [`.TRUE.`{.docutils .literal .notranslate}]{.pre} if the combination of package, category, and setting is available, otherwise [`.FALSE.`{.docutils .literal .notranslate}]{.pre}.

------------------------------------------------------------------------

*[function]{.pre} * [[has_gpu_device]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/has_gpu_device "Link to this definition"){.headerlink}

:   Checks for the presence of a viable GPU package device.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function calls [[`lammps_has_gpu_device()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv421lammps_has_gpu_devicev "lammps_has_gpu_device"){.reference .internal}, which checks at runtime whether an accelerator device is present that can be used with the [[GPU package]{.doc}]Speed_gpu.md){.reference .internal}.

    More detailed information about the available device or devices can be obtained by calling the [`get_gpu_device_info()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} subroutine.

    Call to[:]{.colon}

    :   [[`lammps_has_gpu_device()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv421lammps_has_gpu_devicev "lammps_has_gpu_device"){.reference .internal}

    Return[:]{.colon}

    :   **available** *\[logical\]* :: [`.TRUE.`{.docutils .literal .notranslate}]{.pre} if a viable device is available, [`.FALSE.`{.docutils .literal .notranslate}]{.pre} if not.

------------------------------------------------------------------------

*[subroutine]{.pre} * [[get_gpu_device_info]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[buffer]{.pre}*[)]{.sig-paren}[](#f/_/get_gpu_device_info "Link to this definition"){.headerlink}

:   Get GPU package device information.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Calls [[`lammps_get_gpu_device_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv426lammps_get_gpu_device_infoPci "lammps_get_gpu_device_info"){.reference .internal} to retrieve detailed information about any accelerator devices that are viable for use with the [[GPU package]{.doc}]Speed_gpu.md){.reference .internal}. It will fill *buffer* with a string that is equivalent to the output of the [`nvc_get_device`{.docutils .literal .notranslate}]{.pre} or [`ocl_get_device`{.docutils .literal .notranslate}]{.pre} or [`hip_get_device`{.docutils .literal .notranslate}]{.pre} tools that are compiled alongside LAMMPS if the GPU package is enabled.

    A suitable-length Fortran string has to be provided. The assembled text will be truncated so as not to overflow this buffer. This string can be several kilobytes long if multiple devices are present.

    Parameters[:]{.colon}

    :   **buffer** *\[character(len=\*)\]* :: string into which to copy the information.

    Call to[:]{.colon}

    :   [[`lammps_get_gpu_device_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv426lammps_get_gpu_device_infoPci "lammps_get_gpu_device_info"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[has_style]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[category]{.pre}*, *[name]{.pre}*[)]{.sig-paren}[](#f/_/has_style "Link to this definition"){.headerlink}

:   Check whether a specific style has been included in LAMMPS.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function calls [[`lammps_has_style()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv416lammps_has_stylePvPKcPKc "lammps_has_style"){.reference .internal} to check whether the LAMMPS library in use includes the specific style *name* associated with a specific *category* provided as arguments. Please see [[`lammps_has_style()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv416lammps_has_stylePvPKcPKc "lammps_has_style"){.reference .internal} for a list of valid categories.

    Parameters[:]{.colon}

    :   - **category** *\[character(len=\*)\]* :: category of the style

        - **name** *\[character(len=\*)\]* :: name of the style

    Call to[:]{.colon}

    :   [[`lammps_has_style()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv416lammps_has_stylePvPKcPKc "lammps_has_style"){.reference .internal}

    Return[:]{.colon}

    :   **has_style** *\[logical\]* :: [`.TRUE.`{.docutils .literal .notranslate}]{.pre} if included, [`.FALSE.`{.docutils .literal .notranslate}]{.pre} if not.

------------------------------------------------------------------------

*[function]{.pre} * [[style_count]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[category]{.pre}*[)]{.sig-paren}[](#f/_/style_count "Link to this definition"){.headerlink}

:   Count the number of styles of *category* in the LAMMPS library.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function counts how many styles in the provided *category* are included in the LAMMPS library currently in use. Please see [[`lammps_has_style()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv416lammps_has_stylePvPKcPKc "lammps_has_style"){.reference .internal} for a list of valid categories.

    Parameters[:]{.colon}

    :   **category** *\[character(len=\*)\]* :: category of styles to count

    Call to[:]{.colon}

    :   [[`lammps_style_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv418lammps_style_countPvPKc "lammps_style_count"){.reference .internal}

    Return[:]{.colon}

    :   **count** *\[integer(c_int)\]* :: number of styles in *category*

------------------------------------------------------------------------

*[subroutine]{.pre} * [[style_name]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[category]{.pre}*, *[idx]{.pre}*, *[buffer]{.pre}*[)]{.sig-paren}[](#f/_/style_name "Link to this definition"){.headerlink}

:   Look up the name of a style by index in the list of styles of a given category in the LAMMPS library.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function calls [[`lammps_style_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv417lammps_style_namePvPKciPci "lammps_style_name"){.reference .internal} and copies the name of the *category* style with index *idx* into the provided string *buffer*. The length of *buffer* must be long enough to contain the name of the style; if it is too short, the name will be truncated accordingly. If *idx* is out of range, *buffer* will be the empty string and a warning will be issued.

    Parameters[:]{.colon}

    :   - **category** *\[character(len=\*)\]* :: category of styles

        - **idx** *\[integer(c_int)\]* :: index of the style in the list of *category* styles [\\((1 \\leq idx \\leq \\text{style count})\\)]{.math .notranslate .nohighlight}

        - **buffer** *\[character(len\*)\]* :: string buffer to copy the name of the style into

    Call to[:]{.colon}

    :   [[`lammps_style_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv417lammps_style_namePvPKciPci "lammps_style_name"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[has_id]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[category]{.pre}*, *[name]{.pre}*[)]{.sig-paren}[](#f/_/has_id "Link to this definition"){.headerlink}

:   This function checks if the current LAMMPS instance a *category* ID of the given *name* exists. Valid categories are: *compute*, *dump*, *fix*, *group*, *molecule*, *region*, and *variable*.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   - **category** *\[character(len=\*)\]* :: category of the ID

        - **name** *\[character(len=\*)\]* :: name of the ID

    Call to[:]{.colon}

    :   [[`lammps_has_id()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv413lammps_has_idPvPKcPKc "lammps_has_id"){.reference .internal}

    Return[:]{.colon}

    :   **has_id** *\[logical\]* :: [`.TRUE.`{.docutils .literal .notranslate}]{.pre} if *category* style *name* exists, [`.FALSE.`{.docutils .literal .notranslate}]{.pre} if not.

------------------------------------------------------------------------

*[function]{.pre} * [[id_count]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[category]{.pre}*[)]{.sig-paren}[](#f/_/id_count "Link to this definition"){.headerlink}

:   This function counts how many IDs in the provided *category* are defined in the current LAMMPS instance. Please see [`has_id()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} for a list of valid categories.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   **category** *\[character(len=\*)\]* :: category of the ID

    Call to[:]{.colon}

    :   [[`lammps_id_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv415lammps_id_countPvPKc "lammps_id_count"){.reference .internal}

    Return[:]{.colon}

    :   **count** *\[integer(c_int)\]* :: number of IDs in *category*

------------------------------------------------------------------------

*[subroutine]{.pre} * [[id_name]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[category]{.pre}*, *[idx]{.pre}*, *[buffer]{.pre}*[)]{.sig-paren}[](#f/_/id_name "Link to this definition"){.headerlink}

:   Look up the name of an ID by index in the list of IDs of a given category.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function copies the name of the *category* ID with the index *idx* into the provided string *buffer*. The length of the buffer must be long enough to hold the string; if the name of the style exceeds the length of the buffer, it will be truncated accordingly. If *buffer* is [`ALLOCATABLE`{.docutils .literal .notranslate}]{.pre}, it must be allocated *before* the function is called. If *idx* is out of range, *buffer* is set to an empty string and a warning is issued.

    Parameters[:]{.colon}

    :   - **category** *\[character(len=\*)\]* :: category of IDs

        - **idx** *\[integer(c_int)\]* :: index of the ID in the list of *category* styles ([\\(0 \\leq idx \< count\\)]{.math .notranslate .nohighlight})

        - **buffer** *\[character(len=\*)\]* :: string into which to copy the name of the style

    Call to[:]{.colon}

    :   [[`lammps_id_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv414lammps_id_namePvPKciPci "lammps_id_name"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[plugin_count]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/plugin_count "Link to this definition"){.headerlink}

:   This function counts the number of loaded plugins.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Call to[:]{.colon}

    :   [`lammps_plugin_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}

    Return[:]{.colon}

    :   **n** *\[integer(c_int)\]* :: number of loaded plugins

------------------------------------------------------------------------

*[subroutine]{.pre} * [[plugin_name]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[idx]{.pre}*, *[stylebuf]{.pre}*, *[namebuf]{.pre}*[)]{.sig-paren}[](#f/_/plugin_name "Link to this definition"){.headerlink}

:   Look up the style and name of a plugin by its index in the list of plugins.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function copies the name of the *style* plugin with the index *idx* into the provided C-style string buffer. The length of the buffer must be provided as *buf_size* argument. If the name of the style exceeds the length of the buffer, it will be truncated accordingly. If the index is out of range, both strings are set to the empty string and a warning is printed.

    Parameters[:]{.colon}

    :   - **idx** *\[integer(c_int)\]* :: index of the plugin in the list all or *style* plugins

        - **stylebuf** *\[character(len=\*)\]* :: string into which to copy the style of the plugin

        - **namebuf** *\[character(len=\*)\]* :: string into which to copy the style of the plugin

    Call to[:]{.colon}

    :   [`lammps_plugin_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

*[function]{.pre} * [[encode_image_flags]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[ix]{.pre}*, *[iy]{.pre}*, *[iz]{.pre}*[)]{.sig-paren}[](#f/_/encode_image_flags "Link to this definition"){.headerlink}

:   Encodes three integer image flags into a single imageint.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function performs the bit-shift, addition, and bit-wise OR operations necessary to combine the values of three integers representing the image flags in the [\\(x\\)]{.math .notranslate .nohighlight}-, [\\(y\\)]{.math .notranslate .nohighlight}-, and [\\(z\\)]{.math .notranslate .nohighlight}-directions. Unless LAMMPS is compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, those integers are limited to 10-bit signed integers [\\(\[-512,512)\\)]{.math .notranslate .nohighlight}. If [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} was used when compiling, then the return value is of kind [`c_int64_t`{.docutils .literal .notranslate}]{.pre} instead of kind [`c_int`{.docutils .literal .notranslate}]{.pre}, and the valid range for the individual image flags becomes [\\(\[-1048576,1048575)\\)]{.math .notranslate .nohighlight} (i.e., the range of a 21-bit signed integer). There is no check on whether the arguments conform to these requirements; values out of range will simply be wrapped back into the interval.

    Parameters[:]{.colon}

    :   - **ix** *\[integer(c_int)\]* :: image flag in [\\(x\\)]{.math .notranslate .nohighlight}-direction

        - **iy** *\[integer(c_int)\]* :: image flag in [\\(y\\)]{.math .notranslate .nohighlight}-direction

        - **iz** *\[integer(c_int)\]* :: image flag in [\\(z\\)]{.math .notranslate .nohighlight}-direction

    Return[:]{.colon}

    :   **imageint** *\[integer(kind=\*)\]* :: encoded image flag. \*The [`KIND`{.docutils .literal .notranslate}]{.pre} parameter is [`c_int`{.docutils .literal .notranslate}]{.pre} unless LAMMPS was built with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, in which case it is [`c_int64_t`{.docutils .literal .notranslate}]{.pre}.

    ::::::: {.admonition .note}
    Note

    The fact that the programmer does not know the [`KIND`{.docutils .literal .notranslate}]{.pre} parameter of the return value until compile time means that it is impossible to define an interface that works for both sizes of [`imageint`{.docutils .literal .notranslate}]{.pre}. One side effect of this is that you must assign the return value of this function to a variable; it cannot be used as the argument to another function or as part of an array constructor. For example,

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        my_images = [lmp%encode_image_flags(0,0,0), lmp%encode_image_flags(1,0,0)]
    :::
    ::::

    will *not* work; instead, do something like

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        my_images(1) = lmp%encode_image_flags(0,0,0)
        my_images(2) = lmp%encode_image_flags(1,0,0)
    :::
    ::::
    :::::::

------------------------------------------------------------------------

*[subroutine]{.pre} * [[decode_image_flags]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[image]{.pre}*, *[flags]{.pre}*[)]{.sig-paren}[](#f/_/decode_image_flags "Link to this definition"){.headerlink}

:   This function does the reverse operation of [`encode_image_flags()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}: it takes the image flag and performs the bit-shift and bit-masking operations to decode it and stores the resulting three integers into the array *flags*.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Parameters[:]{.colon}

    :   - **image** *\[integer(kind=\*)\]* :: encoded image flag. \*The [`KIND`{.docutils .literal .notranslate}]{.pre} parameter is either [`c_int`{.docutils .literal .notranslate}]{.pre} or, if LAMMPS was compiled with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, [`c_int64_t`{.docutils .literal .notranslate}]{.pre}. Kind compatibility is checked at run-time.

        - **flags** *\[integer(c_int),dimension(3)\]* :: three-element vector where the decoded image flags will be stored.

------------------------------------------------------------------------

*[subroutine]{.pre} * [[set_fix_external_callback]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*, *[callback]{.pre}*, *[caller]{.pre}*[)]{.sig-paren}[](#f/_/set_fix_external_callback "Link to this definition"){.headerlink}

:   Set the callback function for a [[fix external]{.doc}]fix_external.md){.reference .internal} instance with the given ID.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    Fix [[external]{.doc}]fix_external.md){.reference .internal} allows programs that are running LAMMPS through its library interface to modify certain LAMMPS properties on specific time steps, similar to the way other fixes do.

    This subroutine sets the callback function for use with the "pf/callback" mode. The function should have Fortran language bindings with the following interface, which depends on how LAMMPS was compiled:

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        ABSTRACT INTERFACE
          SUBROUTINE external_callback(caller, timestep, ids, x, fexternal)
            USE, INTRINSIC :: ISO_C_BINDING, ONLY : c_int, c_double, c_int64_t
            CLASS(*), INTENT(INOUT) :: caller
            INTEGER(c_bigint), INTENT(IN) :: timestep
            INTEGER(c_tagint), DIMENSION(:), INTENT(IN) :: ids
            REAL(c_double), DIMENSION(:,:), INTENT(IN) :: x
            REAL(c_double), DIMENSION(:,:), INTENT(OUT) :: fexternal
          END SUBROUTINE external_callback
        END INTERFACE
    :::
    ::::

    where [`c_bigint`{.docutils .literal .notranslate}]{.pre} is [`c_int64_t`{.docutils .literal .notranslate}]{.pre} and [`c_tagint`{.docutils .literal .notranslate}]{.pre} is [`c_int64_t`{.docutils .literal .notranslate}]{.pre} if [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} was used and [`c_int`{.docutils .literal .notranslate}]{.pre} otherwise.

    The argument *caller* to [`set_fix_external_callback()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} is unlimited polymorphic (i.e., it can be any Fortran object you want to pass to the calling function) and will be available as the first argument to the callback function. It can be your LAMMPS instance, which you might need if the callback function needs access to the library interface. The argument must be a scalar; to pass non-scalar data, wrap those data in a derived type and pass an instance of the derived type to *caller*.

    The array *ids* is an array of length *nlocal* (as accessed from the [`Atom`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre} class or through [`extract_global()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}). The arrays *x* and *fexternal* are [\\(3 \\times {}\\)]{.math .notranslate .nohighlight}*nlocal* arrays; these are transposed from what they would look like in C (see note about array index order at [`extract_atom()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}).

    The callback mechanism is one of two ways that forces can be applied to a simulation with the help of [[fix external]{.doc}]fix_external.md){.reference .internal}. The alternative is *array* mode, where one calls [`fix_external_get_force()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre}.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and couple it with external programs.

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: ID of [[fix external]{.doc}]fix_external.md){.reference .internal} instance

        - **callback** *\[external\]* :: subroutine [[fix external]{.doc}]fix_external.md){.reference .internal} should call

        - **caller** *\[class(\*),optional\]* :: object you wish to pass to the callback procedure (must be a scalar; see note)

    Call to[:]{.colon}

    :   [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal}

    ::::: {.admonition .note}
    Note

    The interface for your callback function must match types precisely with the abstract interface block given above. **The compiler probably will not be able to check this for you.** In particular, the first argument ("caller") must be of type [`CLASS(*)`{.docutils .literal .notranslate}]{.pre} or you will probably get a segmentation fault or at least a misinterpretation of whatever is in memory there. You can resolve the object using the [`SELECT`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`TYPE`{.docutils .literal .notranslate}]{.pre} construct. An example callback function (assuming LAMMPS was compiled with [`-DLAMMPS_SMALLBIG`{.docutils .literal .notranslate}]{.pre}) that applies something akin to Hooke's Law (with each atom having a different *k* value) is shown below.

    :::: {.highlight-fortran .notranslate}
    ::: highlight
        MODULE stuff
          USE, INTRINSIC :: ISO_C_BINDING, ONLY : c_int, c_double, c_int64_t
          USE, INTRINSIC :: ISO_FORTRAN_ENV, ONLY : error_unit
          IMPLICIT NONE

          TYPE shield
             REAL(c_double), DIMENSION(:,:), ALLOCATABLE :: k
             ! assume k gets allocated to dimension(3,nlocal) at some point
             ! and assigned values
          END TYPE shield

          SUBROUTINE my_callback(caller, timestep, ids, x, fexternal)
            CLASS(*), INTENT(INOUT) :: caller
            INTEGER(c_int), INTENT(IN) :: timestep
            INTEGER(c_int64_t), INTENT(IN) :: ids
            REAL(c_double), INTENT(IN) :: x(:,:)
            REAL(c_double), INTENT(OUT) :: fexternal(:,:)

            SELECT TYPE (caller)
              TYPE IS (shield)
                 fexternal = - caller%k * x
              CLASS DEFAULT
                 WRITE(error_unit,*) 'UH OH...'
            END SELECT
          END SUBROUTINE my_callback
        END MODULE stuff

        ! then, when assigning the callback function, do this:
        PROGRAM example
          USE LIBLAMMPS
          USE stuff
          TYPE(lammps) :: lmp
          TYPE(shield) :: my_shield
          lmp = lammps()
          CALL lmp%command('fix ext all external pf/callback 1 1')
          CALL lmp%set_fix_external_callback('ext', my_callback, my_shield)
        END PROGRAM example
    :::
    ::::
    :::::

------------------------------------------------------------------------

*[function]{.pre} * [[fix_external_get_force]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*[)]{.sig-paren}[](#f/_/fix_external_get_force "Link to this definition"){.headerlink}

:   Get pointer to the force array storage in a fix external instance with the given ID.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    Fix [[external]{.doc}]fix_external.md){.reference .internal} allows programs that are running LAMMPS through its library interfaces to add or modify certain LAMMPS properties on specific time steps, similar to the way other fixes do.

    This function provides access to the per-atom force storage in a fix external instance with the given fix-ID to be added to the individual atoms when using the "pf/array" mode. The *fexternal* array can be accessed like other "native" per-atom arrays accessible via the [`extract_atom()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} function. Please note that the array stores the forces for *local* atoms for each MPI rank, in the order determined by the neighbor list build. Because the underlying data structures can change as well as the order of atom as they migrate between MPI processes because of the domain decomposition parallelization, this function should be always called immediately before the forces are going to be set to get an up-to-date pointer. You can use, for example, [`extract_setting()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} to obtain the number of local atoms nlocal and then assume the dimensions of the returned force array as [`REAL(c_double)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`::`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`force(3,nlocal)`{.docutils .literal .notranslate}]{.pre}.

    This function is an alternative to the callback mechanism in fix external set up by [`set_fix_external_callback()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}. The main difference is that this mechanism can be used when forces are to be pre-computed and the control alternates between LAMMPS and the external driver, while the callback mechanism can call an external subroutine to compute the force when the fix is triggered and needs them.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external program.

    Parameters[:]{.colon}

    :   **id** *\[character(len=\*)\]* :: ID of [[fix external]{.doc}]fix_external.md){.reference .internal} instance

    Call to[:]{.colon}

    :   [[`lammps_fix_external_get_force()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv429lammps_fix_external_get_forcePvPKc "lammps_fix_external_get_force"){.reference .internal}

    Return[:]{.colon}

    :   **fexternal** *\[real(c_double),dimension(3,nlocal)\]* :: pointer to the per-atom force array allocated by the fix

------------------------------------------------------------------------

*[subroutine]{.pre} * [[fix_external_set_energy_global]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*, *[eng]{.pre}*[)]{.sig-paren}[](#f/_/fix_external_set_energy_global "Link to this definition"){.headerlink}

:   Set the global energy contribution for a [[fix external]{.doc}]fix_external.md){.reference .internal} instance with the given ID.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This is a companion function to [`set_fix_external_callback()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} and [`fix_external_get_force()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} that also sets the contribution to the global energy from the external program. The value of the *eng* argument will be stored in the fix and applied on the current and all following time steps until changed by another call to this function. The energy is in energy units as determined by the current [[units]{.doc}]units.md){.reference .internal} settings and is the **total** energy of the contribution. Thus, when running in parallel, all MPI processes have to call this function with the **same** value, and this will be returned as a scalar property of the fix external instance when accessed in LAMMPS input commands or from variables.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external program.

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: fix ID of fix external instance

        - **eng** *\[real(c_double)\]* :: total energy to be added to the global energy

    Call to[:]{.colon}

    :   [[`lammps_fix_external_set_energy_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv437lammps_fix_external_set_energy_globalPvPKcd "lammps_fix_external_set_energy_global"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[fix_external_set_virial_global]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*, *[virial]{.pre}*[)]{.sig-paren}[](#f/_/fix_external_set_virial_global "Link to this definition"){.headerlink}

:   Set the global virial contribution for a fix external instance with the given ID.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This is a companion function to [`set_fix_external_callback()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} and [`fix_external_get_force()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} to set the contribution to the global virial from an external program.

    The six values of the *virial* array will be stored in the fix and applied on the current and all following time steps until changed by another call to this function. The components of the virial need to be stored in the following order: *xx*, *yy*, *zz*, *xy*, *xz*, *yz*. In LAMMPS, the virial is stored internally as stress\*volume in units of pressure\*volume as determined by the current [[units]{.doc}]units.md){.reference .internal} settings and is the **total** contribution. Thus, when running in parallel, all MPI processes have to call this function with the **same** value, and this will then be added by fix external.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: fix ID of fix external instance

        - **virial** *\[real(c_double),dimension(6)\]* :: the six global stress tensor components to be added to the global virial

    Call to[:]{.colon}

    :   [[`lammps_fix_external_set_virial_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv437lammps_fix_external_set_virial_globalPvPKcPd "lammps_fix_external_set_virial_global"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[fix_external_set_energy_peratom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*, *[eng]{.pre}*[)]{.sig-paren}[](#f/_/fix_external_set_energy_peratom "Link to this definition"){.headerlink}

:   Set the per-atom energy contribution for a fix external instance with the given ID.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This is a companion function to [`set_fix_external_callback()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} to set the per-atom energy contribution due to the fix from the external program as part of the callback function. For this to work, the LAMMPS object must be passed as part of the *caller* argument when registering the callback function, or the callback function must otherwise have access to the LAMMPS object, such as through a module-based pointer.

    ::: {.admonition .note}
    Note

    This function is fully independent from [`fix_external_set_energy_global()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} and will **NOT** add any contributions to the global energy tally and will **NOT** check whether the sum of the contributions added here are consistent with the global added energy.
    :::

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: fix ID of the fix external instance

        - **eng** *\[real(c_double),dimension(:)\]* :: array of length *nlocal* containing the energy to add to the per-atom energy

    Call to[:]{.colon}

    :   [[`lammps_fix_external_set_energy_peratom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv438lammps_fix_external_set_energy_peratomPvPKcPd "lammps_fix_external_set_energy_peratom"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[set_fix_external_set_virial_peratom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*, *[virial]{.pre}*[)]{.sig-paren}[](#f/_/set_fix_external_set_virial_peratom "Link to this definition"){.headerlink}

:   This is a companion function to [`set_fix_external_callback()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} to set the per-atom virial contribution due to the fix from the external program as part of the callback function. For this to work, the LAMMPS object must be passed as the *caller* argument when registering the callback function.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    ::: {.admonition .note}
    Note

    This function is fully independent from [`fix_external_set_virial_global()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} and will **NOT** add any contributions to the global virial tally and **NOT** check whether the sum of the contributions added here are consistent with the global added virial.
    :::

    The order and units of the per-atom stress tensor elements are the same as for the global virial. The type and dimensions of the per-atom virial array must be [`REAL(c_double),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`DIMENSION(6,nlocal)`{.docutils .literal .notranslate}]{.pre}.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external program.

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: fix ID of fix external instance

        - **virial** *\[real(c_double),dimension(:,:)\]* :: an array of [\\(6 \\times{}\\)]{.math .notranslate .nohighlight}*nlocal* components to be added to the per-atom virial

    Call to[:]{.colon}

    :   [`lammps_set_virial_peratom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[fix_external_set_vector_length]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*, *[length]{.pre}*[)]{.sig-paren}[](#f/_/fix_external_set_vector_length "Link to this definition"){.headerlink}

:   Set the vector length for a global vector stored with fix external for analysis.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This is a companion function to [`set_fix_external_callback()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} and [`fix_external_get_force()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} to set the length of a global vector of properties that will be stored with the fix via [`fix_external_set_vector()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}.

    This function needs to be called **before** a call to [`fix_external_set_vector()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} and **before** a run or minimize command. When running in parallel, it must be called from **all** MPI processes with the same length argument.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external program.

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: fix ID of fix external instance

        - **length** *\[integer(c_int)\]* :: length of the global vector to be stored with the fix

    Call to[:]{.colon}

    :   [[`lammps_fix_external_set_vector_length()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv437lammps_fix_external_set_vector_lengthPvPKci "lammps_fix_external_set_vector_length"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[fix_external_set_vector]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[id]{.pre}*, *[idx]{.pre}*, *[val]{.pre}*[)]{.sig-paren}[](#f/_/fix_external_set_vector "Link to this definition"){.headerlink}

:   Store a global vector value for a fix external instance with the given ID.

    ::: versionadded
    [Added in version 22Dec2022.]{.versionmodified .added}
    :::

    This is a companion function to [`set_fix_external_callback()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} and [`fix_external_get_force()`{.xref .f .f-func .docutils .literal .notranslate}]{.pre} to set the values of a global vector of properties that will be stored with the fix and can be accessed from within LAMMPS input commands (e.g., fix ave/time or variables) when used in a vector context.

    This function needs to be called **after** a call to [`fix_external_set_vector_length()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre} and **before** a run or minimize command. When running in parallel, it must be called from **all** MPI processes with the **same** *idx* and *val* parameters. The variable *val* is assumed to be extensive.

    ::: {.admonition .note}
    Note

    The index in the *idx* parameter is 1-based (i.e., the first element is set with *idx*[\\({} = 1\\)]{.math .notranslate .nohighlight}, and the last element of the vector with *idx*[\\({} = N\\)]{.math .notranslate .nohighlight}, where [\\(N\\)]{.math .notranslate .nohighlight} is the value of the *length* parameter of the call to [`fix_external_set_vector_length()`{.xref .f .f-subr .docutils .literal .notranslate}]{.pre}).
    :::

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    Parameters[:]{.colon}

    :   - **id** *\[character(len=\*)\]* :: ID of fix external instance

        - **idx** *\[integer(c_int)\]* :: 1-based index in global vector

        - **val** *\[integer(c_int)\]* :: value to be stored in global vector at index *idx*

    Call to[:]{.colon}

    :   [[`lammps_fix_external_set_vector()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv430lammps_fix_external_set_vectorPvPKcid "lammps_fix_external_set_vector"){.reference .internal}

------------------------------------------------------------------------

*[subroutine]{.pre} * [[flush_buffers]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/flush_buffers "Link to this definition"){.headerlink}

:   This function calls [[`lammps_flush_buffers()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv420lammps_flush_buffersPv "lammps_flush_buffers"){.reference .internal}, which flushes buffered output to be written to screen and logfile. This can simplify capturing output from LAMMPS library calls.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    Call to[:]{.colon}

    :   [[`lammps_flush_buffers()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv420lammps_flush_buffersPv "lammps_flush_buffers"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[is_running]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/is_running "Link to this definition"){.headerlink}

:   Check if LAMMPS is currently inside a run or minimization.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function can be used from signal handlers or multi-threaded applications to determine if the LAMMPS instance is currently active.

    Call to[:]{.colon}

    :   [[`lammps_is_running()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv417lammps_is_runningPv "lammps_is_running"){.reference .internal}

    Return[:]{.colon}

    :   **is_running** *\[logical\]* :: [`.FALSE.`{.docutils .literal .notranslate}]{.pre} if idle or [`.TRUE.`{.docutils .literal .notranslate}]{.pre} if active

------------------------------------------------------------------------

*[subroutine]{.pre} * [[force_timeout]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/force_timeout "Link to this definition"){.headerlink}

:   Force a timeout to stop an ongoing run cleanly.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function can be used from signal handlers or multi-threaded applications to terminate an ongoing run cleanly.

    Call to[:]{.colon}

    :   [[`lammps_force_timeout()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv420lammps_force_timeoutPv "lammps_force_timeout"){.reference .internal}

------------------------------------------------------------------------

*[function]{.pre} * [[has_error]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#f/_/has_error "Link to this definition"){.headerlink}

:   Check if there is a (new) error message available.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function can be used to query if an error inside of LAMMPS has thrown a [[C++ exception]{.std .std-ref}]Build_settings.md#exceptions){.reference .internal}.

    Call to[:]{.colon}

    :   [[`lammps_has_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv416lammps_has_errorPv "lammps_has_error"){.reference .internal}

    Return[:]{.colon}

    :   **has_error** *\[logical\]* :: [`.TRUE.`{.docutils .literal .notranslate}]{.pre} if there is an error.

------------------------------------------------------------------------

*[subroutine]{.pre} * [[get_last_error_message]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[buffer]{.pre}*[\[]{.optional}, *[status]{.pre}*[\]]{.optional}[)]{.sig-paren}[](#f/_/get_last_error_message "Link to this definition"){.headerlink}

:   Copy the last error message into the provided buffer.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function can be used to retrieve the error message that was set in the event of an error inside of LAMMPS that resulted in a [[C++ exception]{.std .std-ref}]Build_settings.md#exceptions){.reference .internal}. A suitable buffer for a string has to be provided. If the internally-stored error message is longer than the string, it will be truncated accordingly. The optional argument *status* indicates the kind of error: a "1" indicates an error that occurred on all MPI ranks and is often recoverable, while a "2" indicates an abort that would happen only in a single MPI rank and thus may not be recoverable, as other MPI ranks may be waiting on the failing MPI rank(s) to send messages.

    Parameters[:]{.colon}

    :   **buffer** *\[character(len=\*)\]* :: string buffer to copy the error message into

    Options[:]{.colon}

    :   **status** *\[integer(c_int),optional\]* :: 1 when all ranks had the error, 2 on a single-rank error.

    Call to[:]{.colon}

    :   [[`lammps_get_last_error_message()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv429lammps_get_last_error_messagePvPci "lammps_get_last_error_message"){.reference .internal}
:::::::
::::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

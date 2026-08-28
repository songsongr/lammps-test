:::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::: {#module-lammps .section}
[]{#the-lammps-python-module}

# [2.4. ]{.section-number}The [`lammps`{.docutils .literal .notranslate}]{.pre} Python module[](#module-lammps "Link to this heading"){.headerlink}

The LAMMPS Python interface is implemented as a module called [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} which is defined in the [`lammps`{.docutils .literal .notranslate}]{.pre} package in the [`python`{.docutils .literal .notranslate}]{.pre} folder of the LAMMPS source code distribution. After compilation of LAMMPS, the module can be installed into a Python system folder or a user folder with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install-python`{.docutils .literal .notranslate}]{.pre}. Components of the module can then loaded into a Python session with the [`import`{.docutils .literal .notranslate}]{.pre} command.

::: {.admonition .warning}
Warning

Alternative interfaces such as [`PyLammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre} and [`IPyLammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre} classes have been deprecated and will be removed in a future version of LAMMPS.
:::

::: {.note .admonition}
Version check

The [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module stores the version number of the LAMMPS version it is installed from. When initializing the [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#lammps.lammps "lammps.lammps"){.reference .internal} class, this version is checked to be the same as the result from [[`lammps.version()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.version "lammps.lammps.version"){.reference .internal}, the version of the LAMMPS shared library that the module interfaces to. If the they are not the same an AttributeError exception is raised since a mismatch of versions (e.g. due to incorrect use of the [`LD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre} or [`PYTHONPATH`{.docutils .literal .notranslate}]{.pre} environment variables can lead to crashes or data corruption and otherwise incorrect behavior.
:::

LAMMPS module global members:

[[lammps.]{.pre}]{.sig-prename .descclassname}[[\_\_version\_\_]{.pre}]{.sig-name .descname}[](#lammps.__version__ "Link to this definition"){.headerlink}

:   Numerical representation of the LAMMPS version this module was taken from. Has the same format as the result of [[`lammps.version()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.version "lammps.lammps.version"){.reference .internal}.

<!-- -->

[[lammps.]{.pre}]{.sig-prename .descclassname}[[get_version_number]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}

:   Extract LAMMPS version string and convert to number

------------------------------------------------------------------------

::: {#the-lammps-class-api .section}
## [2.4.1. ]{.section-number}The [`lammps`{.docutils .literal .notranslate}]{.pre} class API[](#the-lammps-class-api "Link to this heading"){.headerlink}

The [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#lammps.lammps "lammps.lammps"){.reference .internal} class is the core of the LAMMPS Python interface. It is a wrapper around the [[LAMMPS C library API]{.std .std-ref}]Library.md#lammps-c-api){.reference .internal} using the [Python ctypes module](https://docs.python.org/3/library/ctypes.html){.reference .external} and a shared library compiled from the LAMMPS sources code. The individual methods in this class try to closely follow the corresponding C functions. The handle argument that needs to be passed to the C functions is stored internally in the class and automatically added when calling the C library functions. Below is a detailed documentation of the API.

*[[class]{.pre}]{.k}[ ]{.w}*[[lammps.]{.pre}]{.sig-prename .descclassname}[[lammps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}[[=]{.pre}]{.o}[[\'\']{.pre}]{.default_value}*, *[[cmdargs]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[ptr]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[comm]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps "Link to this definition"){.headerlink}

:   Create an instance of the LAMMPS Python class.

    This is a Python wrapper class that exposes the LAMMPS C-library interface to Python. It either requires that LAMMPS has been compiled as shared library which is then dynamically loaded via the ctypes Python module or that this module called from a Python function that is called from a Python interpreter embedded into a LAMMPS executable, for example through the [[python invoke]{.doc}]python.md){.reference .internal} command. When the class is instantiated it calls the [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal} function of the LAMMPS C-library interface, which in turn will create an instance of the [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} C++ class. The handle to this C++ class is stored internally and automatically passed to the calls to the C library interface.

    Parameters[:]{.colon}

    :   - **name** (*string*) -- "machine" name of the shared LAMMPS library ("mpi" loads [`liblammps_mpi.so`{.docutils .literal .notranslate}]{.pre}, "" loads [`liblammps.so`{.docutils .literal .notranslate}]{.pre})

        - **cmdargs** (*list*) -- list of command line arguments to be passed to the [[`lammps_open()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv411lammps_openiPPc8MPI_CommPPv "lammps_open"){.reference .internal} function. The executable name is automatically added.

        - **ptr** (*pointer*) -- pointer to a LAMMPS C++ class instance when called from an embedded Python interpreter. None means load symbols from shared library.

        - **comm** (*MPI_Comm*) -- MPI communicator (as provided by [mpi4py](https://mpi4py.readthedocs.io/){.reference .external}). [`None`{.docutils .literal .notranslate}]{.pre} means use [`MPI_COMM_WORLD`{.docutils .literal .notranslate}]{.pre} implicitly.

    *[[property]{.pre}]{.k}[ ]{.w}*[[numpy]{.pre}]{.sig-name .descname}[](#lammps.lammps.numpy "Link to this definition"){.headerlink}

    :   Return object to access numpy versions of API

        It provides alternative implementations of API functions that return numpy arrays instead of ctypes pointers. If numpy is not installed, accessing this property will lead to an ImportError.

        Returns[:]{.colon}

        :   instance of numpy wrapper object

        Return type[:]{.colon}

        :   [numpy_wrapper](#lammps.numpy_wrapper.numpy_wrapper "lammps.numpy_wrapper.numpy_wrapper"){.reference .internal}

    *[[property]{.pre}]{.k}[ ]{.w}*[[cmd]{.pre}]{.sig-name .descname}[](#lammps.lammps.cmd "Link to this definition"){.headerlink}

    :   Return object that acts as LAMMPS command wrapper

        It provides alternative to [[`lammps.command()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.command "lammps.lammps.command"){.reference .internal} to call LAMMPS commands as if they were regular Python functions and enables auto-complete in interactive Python sessions.

        :::: {.highlight-python .notranslate}
        ::: highlight
            from lammps import lammps

            # melt example
            L = lammps()
            L.cmd.units("lj")
            L.cmd.atom_style("atomic")
            L.cmd.lattice("fcc", 0.8442)
            L.cmd.region("box block", 0, 10, 0, 10, 0, 10)
            L.cmd.create_box(1, "box")
            L.cmd.create_atoms(1, "box")
            L.cmd.mass(1, 1.0)
            L.cmd.velocity("all create", 3.0, 87287, "loop geom")
            L.cmd.pair_style("lj/cut", 2.5)
            L.cmd.pair_coeff(1, 1, 1.0, 1.0, 2.5)
            L.cmd.neighbor(0.3, "bin")
            L.cmd.neigh_modify(every=20, delay=0, check=False)
            L.cmd.fix(1, "all nve")
            L.cmd.thermo(50)
            L.cmd.run(250)
        :::
        ::::

        Returns[:]{.colon}

        :   instance of command_wrapper object

        Return type[:]{.colon}

        :   command_wrapper

    *[[property]{.pre}]{.k}[ ]{.w}*[[ipython]{.pre}]{.sig-name .descname}[](#lammps.lammps.ipython "Link to this definition"){.headerlink}

    :   Return object to access ipython extensions

        Adds commands for visualization in IPython and Jupyter Notebooks.

        Returns[:]{.colon}

        :   instance of ipython wrapper object

        Return type[:]{.colon}

        :   [ipython.wrapper](#lammps.ipython.wrapper "lammps.ipython.wrapper"){.reference .internal}

    [[close]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.close "Link to this definition"){.headerlink}

    :   Explicitly delete a LAMMPS instance through the C-library interface.

        This is a wrapper around the [[`lammps_close()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv412lammps_closePv "lammps_close"){.reference .internal} function of the C-library interface.

    [[finalize]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.finalize "Link to this definition"){.headerlink}

    :   Shut down the MPI communication and Kokkos environment (if active) through the library interface by calling [[`lammps_mpi_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv419lammps_mpi_finalizev "lammps_mpi_finalize"){.reference .internal}, [[`lammps_kokkos_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_kokkos_finalizev "lammps_kokkos_finalize"){.reference .internal}, [[`lammps_python_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_python_finalizev "lammps_python_finalize"){.reference .internal}, and [[`lammps_plugin_finalize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv422lammps_plugin_finalizev "lammps_plugin_finalize"){.reference .internal}

        You cannot create or use any LAMMPS instances after this function is called unless LAMMPS was compiled without MPI and without Kokkos support.

    [[error]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[error_type]{.pre}]{.n}*, *[[error_text]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.error "Link to this definition"){.headerlink}

    :   Forward error to the LAMMPS Error class.

        ::: versionadded
        [Added in version 3Nov2022.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_create.md#_CPPv412lammps_errorPviPKc "lammps_error"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **error_type** (*int*)

            - **error_text** (*string*)

    [[version]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.version "Link to this definition"){.headerlink}

    :   Return a numerical representation of the LAMMPS version in use.

        This is a wrapper around the [[`lammps_version()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv414lammps_versionPv "lammps_version"){.reference .internal} function of the C-library interface.

        Returns[:]{.colon}

        :   version number

        Return type[:]{.colon}

        :   int

    [[get_os_info]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.get_os_info "Link to this definition"){.headerlink}

    :   Return a string with information about the OS and compiler runtime

        This is a wrapper around the [[`lammps_get_os_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv418lammps_get_os_infoPci "lammps_get_os_info"){.reference .internal} function of the C-library interface.

        Returns[:]{.colon}

        :   OS info string

        Return type[:]{.colon}

        :   string

    [[get_mpi_comm]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.get_mpi_comm "Link to this definition"){.headerlink}

    :   Get the MPI communicator in use by the current LAMMPS instance

        This is a wrapper around the [[`lammps_get_mpi_comm()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv419lammps_get_mpi_commPv "lammps_get_mpi_comm"){.reference .internal} function of the C-library interface. It will return [`None`{.docutils .literal .notranslate}]{.pre} if either the LAMMPS library was compiled without MPI support or the mpi4py Python module is not available.

        Returns[:]{.colon}

        :   MPI communicator

        Return type[:]{.colon}

        :   MPI_Comm

    [[expand]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[line]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.expand "Link to this definition"){.headerlink}

    :   Expand a single LAMMPS string like an input line

        This is a wrapper around the [[`lammps_expand()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv413lammps_expandPvPKc "lammps_expand"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   **cmd** (*string*) -- a single lammps line

        Returns[:]{.colon}

        :   expanded string

        Return type[:]{.colon}

        :   string

    [[file]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[path]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.file "Link to this definition"){.headerlink}

    :   Read LAMMPS commands from a file.

        This is a wrapper around the [[`lammps_file()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv411lammps_filePvPKc "lammps_file"){.reference .internal} function of the C-library interface. It will open the file with the name/path file and process the LAMMPS commands line by line until the end. The function will return when the end of the file is reached.

        Parameters[:]{.colon}

        :   **path** (*string*) -- Name of the file/path with LAMMPS commands

    [[command]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[cmd]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.command "Link to this definition"){.headerlink}

    :   Process a single LAMMPS input command from a string.

        This is a wrapper around the [[`lammps_command()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv414lammps_commandPvPKc "lammps_command"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   **cmd** (*string*) -- a single lammps command

    [[commands_list]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[cmdlist]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.commands_list "Link to this definition"){.headerlink}

    :   Process multiple LAMMPS input commands from a list of strings.

        This is a wrapper around the [[`lammps_commands_list()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv420lammps_commands_listPviPPKc "lammps_commands_list"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   **cmdlist** (*list* *of* *strings*) -- a single lammps command

    [[commands_string]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[multicmd]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.commands_string "Link to this definition"){.headerlink}

    :   Process a block of LAMMPS input commands from a string.

        This is a wrapper around the [[`lammps_commands_string()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv422lammps_commands_stringPvPKc "lammps_commands_string"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   **multicmd** (*string*) -- text block of lammps commands

    [[get_natoms]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.get_natoms "Link to this definition"){.headerlink}

    :   Get the total number of atoms in the LAMMPS instance.

        Will be precise up to 53-bit signed integer due to the underlying [[`lammps_get_natoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_natomsPv "lammps_get_natoms"){.reference .internal} function returning a double.

        Returns[:]{.colon}

        :   number of atoms

        Return type[:]{.colon}

        :   int

    [[extract_box]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.extract_box "Link to this definition"){.headerlink}

    :   Extract simulation box parameters

        This is a wrapper around the [[`lammps_extract_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv418lammps_extract_boxPvPdPdPdPdPdPiPi "lammps_extract_box"){.reference .internal} function of the C-library interface. Unlike in the C function, the result is returned as a list.

        Returns[:]{.colon}

        :   list of the extracted data: boxlo, boxhi, xy, yz, xz, periodicity, box_change

        Return type[:]{.colon}

        :   \[ 3\*double, 3\*double, double, double, 3\*int, int\]

    [[reset_box]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[boxlo]{.pre}]{.n}*, *[[boxhi]{.pre}]{.n}*, *[[xy]{.pre}]{.n}*, *[[yz]{.pre}]{.n}*, *[[xz]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.reset_box "Link to this definition"){.headerlink}

    :   Reset simulation box parameters

        This is a wrapper around the [[`lammps_reset_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv416lammps_reset_boxPvPdPdddd "lammps_reset_box"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **boxlo** (*list* *of* *3 floating point numbers*) -- new lower box boundaries

            - **boxhi** (*list* *of* *3 floating point numbers*) -- new upper box boundaries

            - **xy** (*float*) -- xy tilt factor

            - **yz** (*float*) -- yz tilt factor

            - **xz** (*float*) -- xz tilt factor

    [[get_thermo]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.get_thermo "Link to this definition"){.headerlink}

    :   Get current value of a thermo keyword

        This is a wrapper around the [[`lammps_get_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_thermoPvPKc "lammps_get_thermo"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   **name** (*string*) -- name of thermo keyword

        Returns[:]{.colon}

        :   value of thermo keyword

        Return type[:]{.colon}

        :   double or None

    *[[property]{.pre}]{.k}[ ]{.w}*[[last_thermo_step]{.pre}]{.sig-name .descname}[](#lammps.lammps.last_thermo_step "Link to this definition"){.headerlink}

    :   Get the last timestep where thermodynamic data was computed

        Returns[:]{.colon}

        :   the timestep or a negative number if there has not been any thermo output yet

        Return type[:]{.colon}

        :   int

    [[last_thermo]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.last_thermo "Link to this definition"){.headerlink}

    :   Get a dictionary of the last thermodynamic output

        This is a wrapper around the [[`lammps_last_thermo()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv418lammps_last_thermoPvPKci "lammps_last_thermo"){.reference .internal} function of the C-library interface. It collects the cached thermo data from the last timestep into a dictionary. The return value is None, if there has not been any thermo output yet.

        Returns[:]{.colon}

        :   a dictionary containing the last computed thermo output values

        Return type[:]{.colon}

        :   dict or None

    [[extract_setting]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.extract_setting "Link to this definition"){.headerlink}

    :   Query LAMMPS about global settings that can be expressed as an integer.

        This is a wrapper around the [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal} function of the C-library interface. Its documentation includes a list of the supported keywords.

        Parameters[:]{.colon}

        :   **name** (*string*) -- name of the setting

        Returns[:]{.colon}

        :   value of the setting

        Return type[:]{.colon}

        :   int

    [[extract_global_datatype]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.extract_global_datatype "Link to this definition"){.headerlink}

    :   Retrieve global property datatype from LAMMPS

        This is a wrapper around the [[`lammps_extract_global_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv430lammps_extract_global_datatypePvPKc "lammps_extract_global_datatype"){.reference .internal} function of the C-library interface. Its documentation includes a list of the supported keywords. This function returns [`None`{.docutils .literal .notranslate}]{.pre} if the keyword is not recognized. Otherwise it will return a positive integer value that corresponds to one of the [[data type]{.std .std-ref}](#py-datatype-constants){.reference .internal} constants defined in the [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module.

        Parameters[:]{.colon}

        :   **name** (*string*) -- name of the property

        Returns[:]{.colon}

        :   data type of global property, see [[Data Types]{.std .std-ref}](#py-datatype-constants){.reference .internal}

        Return type[:]{.colon}

        :   int

    [[extract_global]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[dtype]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.extract_global "Link to this definition"){.headerlink}

    :   Query LAMMPS about global settings of different types.

        This is a wrapper around the [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal} function of the C-library interface. Since there are no pointers in Python, this method will - unlike the C function - return the value or a list of values. The [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal} documentation includes a list of the supported keywords and their data types. Since Python needs to know the data type to be able to interpret the result, by default, this function will try to auto-detect the data type by asking the library. You can also force a specific data type. For that purpose the [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module contains [[data type]{.std .std-ref}](#py-datatype-constants){.reference .internal} constants. This function returns [`None`{.docutils .literal .notranslate}]{.pre} if either the keyword is not recognized, or an invalid data type constant is used.

        Parameters[:]{.colon}

        :   - **name** (*string*) -- name of the property

            - **dtype** (*int,* *optional*) -- data type of the returned data (see [[Data Types]{.std .std-ref}](#py-datatype-constants){.reference .internal})

        Returns[:]{.colon}

        :   value of the property or list of values or None

        Return type[:]{.colon}

        :   int, float, list, or NoneType

    [[extract_pair_dimension]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.extract_pair_dimension "Link to this definition"){.headerlink}

    :   Retrieve pair style property dimensionality from LAMMPS

        ::: versionadded
        [Added in version 29Aug2024.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_extract_pair_dimension()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv429lammps_extract_pair_dimensionPvPKc "lammps_extract_pair_dimension"){.reference .internal} function of the C-library interface. The list of supported keywords depends on the pair style. This function returns [`None`{.docutils .literal .notranslate}]{.pre} if the keyword is not recognized.

        Parameters[:]{.colon}

        :   **name** (*string*) -- name of the property

        Returns[:]{.colon}

        :   dimensionality of the extractable data (typically 0, 1, or 2)

        Return type[:]{.colon}

        :   int

    [[extract_pair]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.extract_pair "Link to this definition"){.headerlink}

    :   Extract pair style data from LAMMPS.

        ::: versionadded
        [Added in version 29Aug2024.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_extract_pair()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv419lammps_extract_pairPvPKc "lammps_extract_pair"){.reference .internal} function of the C-library interface. Since there are no pointers in Python, this method will - unlike the C function - return the value or a list of values. Since Python needs to know the dimensionality to be able to interpret the result, this function will detect the dimensionality by asking the library. This function returns [`None`{.docutils .literal .notranslate}]{.pre} if the keyword is not recognized.

        Parameters[:]{.colon}

        :   **name** (*string*) -- name of the property

        Returns[:]{.colon}

        :   value of the property or list of values or None

        Return type[:]{.colon}

        :   float, list of float, list of list of floats, or NoneType

    [[map_atom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[atomid]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.map_atom "Link to this definition"){.headerlink}

    :   Map a global atom ID (aka tag) to the local atom index

        This is a wrapper around the [[`lammps_map_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv415lammps_map_atomPvPKv "lammps_map_atom"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   **atomid** (*int*) -- atom ID

        Returns[:]{.colon}

        :   local index

        Return type[:]{.colon}

        :   int

    [[extract_atom_datatype]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.extract_atom_datatype "Link to this definition"){.headerlink}

    :   Retrieve per-atom property datatype from LAMMPS

        This is a wrapper around the [[`lammps_extract_atom_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_atoms.md#_CPPv428lammps_extract_atom_datatypePvPKc "lammps_extract_atom_datatype"){.reference .internal} function of the C-library interface. Its documentation includes a list of the supported keywords. This function returns [`None`{.docutils .literal .notranslate}]{.pre} if the keyword is not recognized. Otherwise it will return an integer value that corresponds to one of the [[data type]{.std .std-ref}](#py-datatype-constants){.reference .internal} constants defined in the [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module.

        Parameters[:]{.colon}

        :   **name** (*string*) -- name of the property

        Returns[:]{.colon}

        :   data type of per-atom property (see [[Data Types]{.std .std-ref}](#py-datatype-constants){.reference .internal})

        Return type[:]{.colon}

        :   int

    [[extract_atom_size]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[dtype]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.extract_atom_size "Link to this definition"){.headerlink}

    :   Retrieve per-atom property dimensions from LAMMPS

        This is a wrapper around the [[`lammps_extract_atom_size()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_atoms.md#_CPPv424lammps_extract_atom_sizePvPKci "lammps_extract_atom_size"){.reference .internal} function of the C-library interface. Its documentation includes a list of the supported keywords. This function returns [`None`{.docutils .literal .notranslate}]{.pre} if the keyword is not recognized. Otherwise it will return an integer value with the size of the per-atom vector or array. If *name* corresponds to a per-atom array, the *dtype* keyword must be either LMP_SIZE_ROWS or LMP_SIZE_COLS from the [[type]{.std .std-ref}](#py-type-constants){.reference .internal} constants defined in the [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module. The return value is the requested size. If *name* corresponds to a per-atom vector the *dtype* keyword is ignored.

        Parameters[:]{.colon}

        :   - **name** (*string*) -- name of the property

            - **type** (*int*) -- either LMP_SIZE_ROWS or LMP_SIZE_COLS for arrays, otherwise ignored

        Returns[:]{.colon}

        :   data type of per-atom property (see [[Data Types]{.std .std-ref}](#py-datatype-constants){.reference .internal})

        Return type[:]{.colon}

        :   int

    [[extract_atom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[dtype]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.extract_atom "Link to this definition"){.headerlink}

    :   Retrieve per-atom properties from LAMMPS

        This is a wrapper around the [[`lammps_extract_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_atoms.md#_CPPv419lammps_extract_atomPvPKc "lammps_extract_atom"){.reference .internal} function of the C-library interface. Its documentation includes a list of the supported keywords and their data types. Since Python needs to know the data type to be able to interpret the result, by default, this function will try to auto-detect the data type by asking the library. You can also force a specific data type by setting [`dtype`{.docutils .literal .notranslate}]{.pre} to one of the [[data type]{.std .std-ref}](#py-datatype-constants){.reference .internal} constants defined in the [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module. This function returns [`None`{.docutils .literal .notranslate}]{.pre} if either the keyword is not recognized, or an invalid data type constant is used.

        ::: {.admonition .note}
        Note

        While the returned vectors or arrays of per-atom data are dimensioned for the range \[0:nmax\] - as is the underlying storage - the data is usually only valid for the range of \[0:nlocal\], unless the property of interest is also updated for ghost atoms. In some cases, this depends on a LAMMPS setting, see for example [[comm_modify vel yes]{.doc}]comm_modify.md){.reference .internal}. The actual size can be determined by calling py:meth:extract_atom_size() \<lammps.lammps.extract_atom_size\>.
        :::

        Parameters[:]{.colon}

        :   - **name** (*string*) -- name of the property

            - **dtype** (*int,* *optional*) -- data type of the returned data (see [[Data Types]{.std .std-ref}](#py-datatype-constants){.reference .internal})

        Returns[:]{.colon}

        :   requested data or [`None`{.docutils .literal .notranslate}]{.pre}

        Return type[:]{.colon}

        :   ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.POINTER(ctypes.c_int64)), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), or NoneType

    [[extract_compute]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[cid]{.pre}]{.n}*, *[[cstyle]{.pre}]{.n}*, *[[ctype]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.extract_compute "Link to this definition"){.headerlink}

    :   Retrieve data from a LAMMPS compute

        This is a wrapper around the [[`lammps_extract_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv422lammps_extract_computePvPKcii "lammps_extract_compute"){.reference .internal} function of the C-library interface. This function returns [`None`{.docutils .literal .notranslate}]{.pre} if either the compute id is not recognized, or an invalid combination of [[cstyle]{.std .std-ref}](#py-style-constants){.reference .internal} and [[ctype]{.std .std-ref}](#py-type-constants){.reference .internal} constants is used. The names and functionality of the constants are the same as for the corresponding C-library function. For requests to return a scalar or a size, the value is returned, otherwise a pointer.

        Parameters[:]{.colon}

        :   - **cid** (*string*) -- compute ID

            - **cstyle** (*int*) -- style of the data retrieve (global, atom, or local), see [[Style Constants]{.std .std-ref}](#py-style-constants){.reference .internal}

            - **ctype** (*int*) -- type or size of the returned data (scalar, vector, or array), see [[Type Constants]{.std .std-ref}](#py-type-constants){.reference .internal}

        Returns[:]{.colon}

        :   requested data as scalar, pointer to 1d or 2d double array, or None

        Return type[:]{.colon}

        :   c_double, ctypes.POINTER(c_double), ctypes.POINTER(ctypes.POINTER(c_double)), or NoneType

    [[extract_fix]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fid]{.pre}]{.n}*, *[[fstyle]{.pre}]{.n}*, *[[ftype]{.pre}]{.n}*, *[[nrow]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*, *[[ncol]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.extract_fix "Link to this definition"){.headerlink}

    :   Retrieve data from a LAMMPS fix

        This is a wrapper around the [[`lammps_extract_fix()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv418lammps_extract_fixPvPKciiii "lammps_extract_fix"){.reference .internal} function of the C-library interface. This function returns [`None`{.docutils .literal .notranslate}]{.pre} if either the fix id is not recognized, or an invalid combination of [[fstyle]{.std .std-ref}](#py-style-constants){.reference .internal} and [[ftype]{.std .std-ref}](#py-type-constants){.reference .internal} constants is used. The names and functionality of the constants are the same as for the corresponding C-library function. For requests to return a scalar or a size, the value is returned, also when accessing global vectors or arrays, otherwise a pointer.

        ::: {.admonition .note}
        Note

        When requesting global data, the fix data can only be accessed one item at a time without access to the whole vector or array. Thus this function will always return a scalar. To access vector or array elements the "nrow" and "ncol" arguments need to be set accordingly (they default to 0).
        :::

        Parameters[:]{.colon}

        :   - **fid** (*string*) -- fix ID

            - **fstyle** (*int*) -- style of the data retrieve (global, atom, or local), see [[Style Constants]{.std .std-ref}](#py-style-constants){.reference .internal}

            - **ftype** (*int*) -- type or size of the returned data (scalar, vector, or array), see [[Type Constants]{.std .std-ref}](#py-type-constants){.reference .internal}

            - **nrow** (*int*) -- index of global vector element or row index of global array element

            - **ncol** (*int*) -- column index of global array element

        Returns[:]{.colon}

        :   requested data or None

        Return type[:]{.colon}

        :   c_double, ctypes.POINTER(c_double), ctypes.POINTER(ctypes.POINTER(c_double)), or NoneType

    [[extract_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[group]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[vartype]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.extract_variable "Link to this definition"){.headerlink}

    :   Evaluate a LAMMPS variable and return its data

        This function is a wrapper around the function [[`lammps_extract_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv423lammps_extract_variablePvPKcPKc "lammps_extract_variable"){.reference .internal} of the C library interface, evaluates variable name and returns a copy of the computed data. The memory temporarily allocated by the C-interface is deleted after the data is copied to a Python variable or list. The variable must be either an equal-style (or equivalent) variable or an atom-style variable. The variable type can be provided as the [`vartype`{.docutils .literal .notranslate}]{.pre} parameter, which may be one of several constants: [`LMP_VAR_EQUAL`{.docutils .literal .notranslate}]{.pre}, [`LMP_VAR_ATOM`{.docutils .literal .notranslate}]{.pre}, [`LMP_VAR_VECTOR`{.docutils .literal .notranslate}]{.pre}, or [`LMP_VAR_STRING`{.docutils .literal .notranslate}]{.pre}. If omitted or [`None`{.docutils .literal .notranslate}]{.pre}, LAMMPS will determine its value for you based on a call to [[`lammps_extract_variable_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv432lammps_extract_variable_datatypePvPKc "lammps_extract_variable_datatype"){.reference .internal} from the C library interface. The group parameter is only used for atom-style variables and defaults to the group "all".

        Parameters[:]{.colon}

        :   - **name** (*string*) -- name of the variable to execute

            - **group** (*string,* *only for atom-style variables*) -- name of group for atom-style variable

            - **vartype** (*int*) -- type of variable, see [[Variable Type Constants]{.std .std-ref}](#py-vartype-constants){.reference .internal}

        Returns[:]{.colon}

        :   the requested data

        Return type[:]{.colon}

        :   c_double, (c_double), or NoneType

    [[clearstep_compute]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.clearstep_compute "Link to this definition"){.headerlink}

    :   Call 'lammps_clearstep_compute()' from Python

    [[addstep_compute]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[nextstep]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.addstep_compute "Link to this definition"){.headerlink}

    :   Call 'lammps_addstep_compute()' from Python

    [[addstep_compute_all]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[nextstep]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.addstep_compute_all "Link to this definition"){.headerlink}

    :   Call 'lammps_addstep_compute_all()' from Python

    [[flush_buffers]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.flush_buffers "Link to this definition"){.headerlink}

    :   Flush output buffers

        This is a wrapper around the [[`lammps_flush_buffers()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv420lammps_flush_buffersPv "lammps_flush_buffers"){.reference .internal} function of the C-library interface.

    [[set_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[value]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.set_variable "Link to this definition"){.headerlink}

    :   Set a new value for a LAMMPS string style variable

        ::: deprecated
        [Deprecated since version 7Feb2024.]{.versionmodified .deprecated}
        :::

        This is a wrapper around the [[`lammps_set_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv419lammps_set_variablePvPKcPKc "lammps_set_variable"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **name** (*string*) -- name of the variable

            - **value** (*any. will be converted to a string*) -- new variable value

        Returns[:]{.colon}

        :   either 0 on success or -1 on failure

        Return type[:]{.colon}

        :   int

    [[set_string_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[value]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.set_string_variable "Link to this definition"){.headerlink}

    :   Set a new value for a LAMMPS string style variable

        ::: versionadded
        [Added in version 7Feb2024.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_set_string_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv426lammps_set_string_variablePvPKcPKc "lammps_set_string_variable"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **name** (*string*) -- name of the variable

            - **value** (*any. will be converted to a string*) -- new variable value

        Returns[:]{.colon}

        :   either 0 on success or -1 on failure

        Return type[:]{.colon}

        :   int

    [[set_internal_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[value]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.set_internal_variable "Link to this definition"){.headerlink}

    :   Set a new value for a LAMMPS internal style variable

        ::: versionadded
        [Added in version 7Feb2024.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_set_internal_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv428lammps_set_internal_variablePvPKcd "lammps_set_internal_variable"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **name** (*string*) -- name of the variable

            - **value** (*float* *or* *compatible. will be converted to float*) -- new variable value

        Returns[:]{.colon}

        :   either 0 on success or -1 on failure

        Return type[:]{.colon}

        :   int

    [[eval]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[expr]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.eval "Link to this definition"){.headerlink}

    :   Evaluate a LAMMPS immediate variable expression

        ::: versionadded
        [Added in version 4Feb2025.]{.versionmodified .added}
        :::

        This function is a wrapper around the function [[`lammps_eval()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv411lammps_evalPvPKc "lammps_eval"){.reference .internal} of the C library interface. It evaluates and expression like in immediate variables and returns the value.

        Parameters[:]{.colon}

        :   **expr** -- immediate variable expression

        Returns[:]{.colon}

        :   the result of the evaluation

        Return type[:]{.colon}

        :   c_double

    [[gather_bonds]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.gather_bonds "Link to this definition"){.headerlink}

    :   Retrieve global list of bonds

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_gather_bonds()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv419lammps_gather_bondsPvPv "lammps_gather_bonds"){.reference .internal} function of the C-library interface.

        This function returns a tuple with the number of bonds and a flat list of ctypes integer values with the bond type, bond atom1, bond atom2 for each bond.

        Returns[:]{.colon}

        :   a tuple with the number of bonds and a list of c_int or c_long

        Return type[:]{.colon}

        :   (int, 3\*nbonds\*c_tagint)

    [[gather_angles]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.gather_angles "Link to this definition"){.headerlink}

    :   Retrieve global list of angles

        ::: versionadded
        [Added in version 8Feb2023.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_gather_angles()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv420lammps_gather_anglesPvPv "lammps_gather_angles"){.reference .internal} function of the C-library interface.

        This function returns a tuple with the number of angles and a flat list of ctypes integer values with the angle type, angle atom1, angle atom2, angle atom3 for each angle.

        Returns[:]{.colon}

        :   a tuple with the number of angles and a list of c_int or c_long

        Return type[:]{.colon}

        :   (int, 4\*nangles\*c_tagint)

    [[gather_dihedrals]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.gather_dihedrals "Link to this definition"){.headerlink}

    :   Retrieve global list of dihedrals

        ::: versionadded
        [Added in version 8Feb2023.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_gather_dihedrals()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv423lammps_gather_dihedralsPvPv "lammps_gather_dihedrals"){.reference .internal} function of the C-library interface.

        This function returns a tuple with the number of dihedrals and a flat list of ctypes integer values with the dihedral type, dihedral atom1, dihedral atom2, dihedral atom3, dihedral atom4 for each dihedral.

        Returns[:]{.colon}

        :   a tuple with the number of dihedrals and a list of c_int or c_long

        Return type[:]{.colon}

        :   (int, 5\*ndihedrals\*c_tagint)

    [[gather_impropers]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.gather_impropers "Link to this definition"){.headerlink}

    :   Retrieve global list of impropers

        ::: versionadded
        [Added in version 8Feb2023.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_gather_impropers()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv423lammps_gather_impropersPvPv "lammps_gather_impropers"){.reference .internal} function of the C-library interface.

        This function returns a tuple with the number of impropers and a flat list of ctypes integer values with the improper type, improper atom1, improper atom2, improper atom3, improper atom4 for each improper.

        Returns[:]{.colon}

        :   a tuple with the number of impropers and a list of c_int or c_long

        Return type[:]{.colon}

        :   (int, 5\*nimpropers\*c_tagint)

    [[encode_image_flags]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[ix]{.pre}]{.n}*, *[[iy]{.pre}]{.n}*, *[[iz]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.encode_image_flags "Link to this definition"){.headerlink}

    :   convert 3 integers with image flags for x-, y-, and z-direction into a single integer like it is used internally in LAMMPS

        This method is a wrapper around the [[`lammps_encode_image_flags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv425lammps_encode_image_flagsiii "lammps_encode_image_flags"){.reference .internal} function of library interface.

        Parameters[:]{.colon}

        :   - **ix** (*int*) -- x-direction image flag

            - **iy** (*int*) -- y-direction image flag

            - **iz** (*int*) -- z-direction image flag

        Returns[:]{.colon}

        :   encoded image flags

        Return type[:]{.colon}

        :   lammps.c_imageint

    [[decode_image_flags]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[image]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.decode_image_flags "Link to this definition"){.headerlink}

    :   Convert encoded image flag integer into list of three regular integers.

        This method is a wrapper around the [[`lammps_decode_image_flags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv425lammps_decode_image_flagsiPi "lammps_decode_image_flags"){.reference .internal} function of library interface.

        Parameters[:]{.colon}

        :   **image** (*lammps.c_imageint*) -- encoded image flags

        Returns[:]{.colon}

        :   list of three image flags in x-, y-, and z- direction

        Return type[:]{.colon}

        :   list of 3 int

    [[create_atoms]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[n]{.pre}]{.n}*, *[[atomid]{.pre}]{.n}*, *[[atype]{.pre}]{.n}*, *[[x]{.pre}]{.n}*, *[[v]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[image]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[shrinkexceed]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.create_atoms "Link to this definition"){.headerlink}

    :   Create N atoms from list of coordinates and properties

        This function is a wrapper around the [[`lammps_create_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv419lammps_create_atomsPviPKiPKiPKdPKdPKii "lammps_create_atoms"){.reference .internal} function of the C-library interface, and the behavior is similar except that the *v*, *image*, and *shrinkexceed* arguments are optional and default to *None*, *None*, and *False*, respectively. With *None* being equivalent to a [`NULL`{.docutils .literal .notranslate}]{.pre} pointer in C.

        The lists of coordinates, types, atom IDs, velocities, image flags can be provided in any format that may be converted into the required internal data types. Also the list may contain more than *N* entries, but not fewer. In the latter case, the function will return without attempting to create atoms. You may use the [[`encode_image_flags`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.encode_image_flags "lammps.lammps.encode_image_flags"){.reference .internal} method to properly combine three integers with image flags into a single integer.

        Parameters[:]{.colon}

        :   - **n** (*int*) -- number of atoms for which data is provided

            - **atomid** (*list* *of* *lammps.tagint*) -- list of atom IDs with at least n elements or None

            - **atype** (*list* *of* *int*) -- list of atom types

            - **x** (*list* *of* *float*) -- list of coordinates for x-, y-, and z (flat list of 3n entries)

            - **v** (*list* *of* *float*) -- list of velocities for x-, y-, and z (flat list of 3n entries) or None (optional)

            - **image** (*list* *of* *lammps.imageint*) -- list of encoded image flags (optional)

            - **shrinkexceed** (*bool*) -- whether to expand shrink-wrap boundaries if atoms are outside the box (optional)

        Returns[:]{.colon}

        :   number of atoms created. 0 if insufficient or invalid data

        Return type[:]{.colon}

        :   int

    [[create_molecule]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[molid]{.pre}]{.n}*, *[[jsonstr]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.create_molecule "Link to this definition"){.headerlink}

    :   Create new molecule template from string with JSON data

        ::: versionadded
        [Added in version 22Jul2025.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_create_molecule()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_scatter.md#_CPPv422lammps_create_moleculePvPKcPKc "lammps_create_molecule"){.reference .internal} function of the library interface.

        Parameters[:]{.colon}

        :   - **molid** -- molecule-id of the new molecule template

            - **jsonstr** (*string*) -- JSON data defining a new molecule template

    *[[property]{.pre}]{.k}[ ]{.w}*[[has_mpi_support]{.pre}]{.sig-name .descname}[](#lammps.lammps.has_mpi_support "Link to this definition"){.headerlink}

    :   Report whether the LAMMPS shared library was compiled with a real MPI library or in serial.

        This is a wrapper around the [[`lammps_config_has_mpi_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv429lammps_config_has_mpi_supportv "lammps_config_has_mpi_support"){.reference .internal} function of the library interface.

        Returns[:]{.colon}

        :   False when compiled with MPI STUBS, otherwise True

        Return type[:]{.colon}

        :   bool

    *[[property]{.pre}]{.k}[ ]{.w}*[[has_omp_support]{.pre}]{.sig-name .descname}[](#lammps.lammps.has_omp_support "Link to this definition"){.headerlink}

    :   Report whether the LAMMPS shared library was compiled with OpenMP enabled.

        This is a wrapper around the [[`lammps_config_has_omp_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv429lammps_config_has_omp_supportv "lammps_config_has_omp_support"){.reference .internal} function of the library interface.

        Returns[:]{.colon}

        :   True when compiled with OpenMP enabled, otherwise False

        Return type[:]{.colon}

        :   bool

    *[[property]{.pre}]{.k}[ ]{.w}*[[is_running]{.pre}]{.sig-name .descname}[](#lammps.lammps.is_running "Link to this definition"){.headerlink}

    :   Report whether being called from a function during a run or a minimization

        ::: versionadded
        [Added in version 9Oct2020.]{.versionmodified .added}
        :::

        Various LAMMPS commands must not be called during an ongoing run or minimization. This property allows to check for that. This is a wrapper around the [[`lammps_is_running()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv417lammps_is_runningPv "lammps_is_running"){.reference .internal} function of the library interface.

        Returns[:]{.colon}

        :   True when called during a run otherwise false

        Return type[:]{.colon}

        :   bool

    [[set_show_error]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[flag]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.set_show_error "Link to this definition"){.headerlink}

    :   Enable or disable direct printing of error messages in C++ code

        ::: versionadded
        [Added in version 2Apr2025.]{.versionmodified .added}
        :::

        This function allows to enable or disable printing of error message directly in the C++ code. Disabling the printing avoids printing error messages twice when detecting and re-throwing them in Python code.

        This is a wrapper around the [[`lammps_set_show_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv421lammps_set_show_errorPvKi "lammps_set_show_error"){.reference .internal} function of the library interface.

        Parameters[:]{.colon}

        :   **flag** (*int*) -- enable (1) or disable (0) printing of error message

        Returns[:]{.colon}

        :   previous setting of the flag

        Return type[:]{.colon}

        :   int

    [[force_timeout]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.force_timeout "Link to this definition"){.headerlink}

    :   Trigger an immediate timeout, i.e. a "soft stop" of a run.

        ::: versionadded
        [Added in version 9Oct2020.]{.versionmodified .added}
        :::

        This function allows to cleanly stop an ongoing run or minimization at the next loop iteration. This is a wrapper around the [[`lammps_force_timeout()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv420lammps_force_timeoutPv "lammps_force_timeout"){.reference .internal} function of the library interface.

    *[[property]{.pre}]{.k}[ ]{.w}*[[has_exceptions]{.pre}]{.sig-name .descname}[](#lammps.lammps.has_exceptions "Link to this definition"){.headerlink}

    :   Report whether the LAMMPS shared library was compiled with C++ exceptions handling enabled

        This is a wrapper around the [[`lammps_config_has_exceptions()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv428lammps_config_has_exceptionsv "lammps_config_has_exceptions"){.reference .internal} function of the library interface.

        Returns[:]{.colon}

        :   state of C++ exception support

        Return type[:]{.colon}

        :   bool

    *[[property]{.pre}]{.k}[ ]{.w}*[[has_gzip_support]{.pre}]{.sig-name .descname}[](#lammps.lammps.has_gzip_support "Link to this definition"){.headerlink}

    :   Report whether the LAMMPS shared library was compiled with support for reading and writing compressed files through [`gzip`{.docutils .literal .notranslate}]{.pre}.

        This is a wrapper around the [[`lammps_config_has_gzip_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv430lammps_config_has_gzip_supportv "lammps_config_has_gzip_support"){.reference .internal} function of the library interface.

        Returns[:]{.colon}

        :   state of gzip support

        Return type[:]{.colon}

        :   bool

    *[[property]{.pre}]{.k}[ ]{.w}*[[has_png_support]{.pre}]{.sig-name .descname}[](#lammps.lammps.has_png_support "Link to this definition"){.headerlink}

    :   Report whether the LAMMPS shared library was compiled with support for writing images in PNG format.

        This is a wrapper around the [[`lammps_config_has_png_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv429lammps_config_has_png_supportv "lammps_config_has_png_support"){.reference .internal} function of the library interface.

        Returns[:]{.colon}

        :   state of PNG support

        Return type[:]{.colon}

        :   bool

    *[[property]{.pre}]{.k}[ ]{.w}*[[has_jpeg_support]{.pre}]{.sig-name .descname}[](#lammps.lammps.has_jpeg_support "Link to this definition"){.headerlink}

    :   Report whether the LAMMPS shared library was compiled with support for writing images in JPEG format.

        This is a wrapper around the [[`lammps_config_has_jpeg_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv430lammps_config_has_jpeg_supportv "lammps_config_has_jpeg_support"){.reference .internal} function of the library interface.

        Returns[:]{.colon}

        :   state of JPEG support

        Return type[:]{.colon}

        :   bool

    *[[property]{.pre}]{.k}[ ]{.w}*[[has_ffmpeg_support]{.pre}]{.sig-name .descname}[](#lammps.lammps.has_ffmpeg_support "Link to this definition"){.headerlink}

    :   State of support for writing movies with [`ffmpeg`{.docutils .literal .notranslate}]{.pre} in the LAMMPS shared library

        This is a wrapper around the [[`lammps_config_has_ffmpeg_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv432lammps_config_has_ffmpeg_supportv "lammps_config_has_ffmpeg_support"){.reference .internal} function of the library interface.

        Returns[:]{.colon}

        :   state of ffmpeg support

        Return type[:]{.colon}

        :   bool

    *[[property]{.pre}]{.k}[ ]{.w}*[[has_curl_support]{.pre}]{.sig-name .descname}[](#lammps.lammps.has_curl_support "Link to this definition"){.headerlink}

    :   Report whether the LAMMPS shared library was compiled with support for downloading files through libcurl.

        This is a wrapper around the [`lammps_config_has_curl_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre} function of the library interface.

        Returns[:]{.colon}

        :   state of CURL support

        Return type[:]{.colon}

        :   bool

    [[has_package]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.has_package "Link to this definition"){.headerlink}

    :   Report if the named package has been enabled in the LAMMPS shared library.

        ::: versionadded
        [Added in version 3Nov2022.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_config_has_package()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv425lammps_config_has_packagePKc "lammps_config_has_package"){.reference .internal} function of the library interface.

        Parameters[:]{.colon}

        :   **name** (*string*) -- name of the package

        Returns[:]{.colon}

        :   state of package availability

        Return type[:]{.colon}

        :   bool

    *[[property]{.pre}]{.k}[ ]{.w}*[[accelerator_config]{.pre}]{.sig-name .descname}[](#lammps.lammps.accelerator_config "Link to this definition"){.headerlink}

    :   Return table with available accelerator configuration settings.

        This is a wrapper around the [[`lammps_config_accelerator()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv425lammps_config_acceleratorPKcPKcPKc "lammps_config_accelerator"){.reference .internal} function of the library interface which loops over all known packages and categories and returns enabled features as a nested dictionary with all enabled settings as list of strings.

        Returns[:]{.colon}

        :   nested dictionary with all known enabled settings as list of strings

        Return type[:]{.colon}

        :   dictionary

    *[[property]{.pre}]{.k}[ ]{.w}*[[has_gpu_device]{.pre}]{.sig-name .descname}[](#lammps.lammps.has_gpu_device "Link to this definition"){.headerlink}

    :   Availability of GPU package compatible device

        This is a wrapper around the [[`lammps_has_gpu_device()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv421lammps_has_gpu_devicev "lammps_has_gpu_device"){.reference .internal} function of the C library interface.

        Returns[:]{.colon}

        :   True if a GPU package compatible device is present, otherwise False

        Return type[:]{.colon}

        :   bool

    [[get_gpu_device_info]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.lammps.get_gpu_device_info "Link to this definition"){.headerlink}

    :   Return a string with detailed information about any devices that are usable by the GPU package.

        This is a wrapper around the [[`lammps_get_gpu_device_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv426lammps_get_gpu_device_infoPci "lammps_get_gpu_device_info"){.reference .internal} function of the C-library interface.

        Returns[:]{.colon}

        :   GPU device info string

        Return type[:]{.colon}

        :   string

    *[[property]{.pre}]{.k}[ ]{.w}*[[installed_packages]{.pre}]{.sig-name .descname}[](#lammps.lammps.installed_packages "Link to this definition"){.headerlink}

    :   List of the names of enabled packages in the LAMMPS shared library

        This is a wrapper around the functions [[`lammps_config_package_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv427lammps_config_package_countv "lammps_config_package_count"){.reference .internal} and [[`lammps_config_package_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv426lammps_config_package_nameiPci "lammps_config_package_name"){.reference .internal} of the library interface.

        :return

    [[has_style]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[category]{.pre}]{.n}*, *[[name]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.has_style "Link to this definition"){.headerlink}

    :   Returns whether a given style name is available in a given category

        This is a wrapper around the function [[`lammps_has_style()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv416lammps_has_stylePvPKcPKc "lammps_has_style"){.reference .internal} of the library interface.

        Parameters[:]{.colon}

        :   - **category** (*string*) -- name of category

            - **name** (*string*) -- name of the style

        Returns[:]{.colon}

        :   true if style is available in given category

        Return type[:]{.colon}

        :   bool

    [[available_styles]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[category]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.available_styles "Link to this definition"){.headerlink}

    :   Returns a list of styles available for a given category

        This is a wrapper around the functions [[`lammps_style_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv418lammps_style_countPvPKc "lammps_style_count"){.reference .internal} and [[`lammps_style_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv417lammps_style_namePvPKciPci "lammps_style_name"){.reference .internal} of the library interface.

        Parameters[:]{.colon}

        :   **category** (*string*) -- name of category

        Returns[:]{.colon}

        :   list of style names in given category

        Return type[:]{.colon}

        :   list

    [[has_id]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[category]{.pre}]{.n}*, *[[name]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.has_id "Link to this definition"){.headerlink}

    :   Returns whether a given ID name is available in a given category

        ::: versionadded
        [Added in version 9Oct2020.]{.versionmodified .added}
        :::

        This is a wrapper around the function [[`lammps_has_id()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv413lammps_has_idPvPKcPKc "lammps_has_id"){.reference .internal} of the library interface.

        Parameters[:]{.colon}

        :   - **category** (*string*) -- name of category

            - **name** (*string*) -- name of the ID

        Returns[:]{.colon}

        :   true if ID is available in given category

        Return type[:]{.colon}

        :   bool

    [[available_ids]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[category]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.available_ids "Link to this definition"){.headerlink}

    :   Returns a list of IDs available for a given category

        ::: versionadded
        [Added in version 9Oct2020.]{.versionmodified .added}
        :::

        This is a wrapper around the functions [[`lammps_id_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv415lammps_id_countPvPKc "lammps_id_count"){.reference .internal} and [[`lammps_id_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_config.md#_CPPv414lammps_id_namePvPKciPci "lammps_id_name"){.reference .internal} of the library interface.

        ::: versionchanged
        [Changed in version 22Jul2025.]{.versionmodified .changed}
        :::

        This function has a different behavior for the "group" category: rather than only listing the available groups, it will return a full list with LMP_MAX_GROUP elements. This is because the list may have "holes" when groups are deleted. The returned list has either the name of the group or "None" for empty entries. This way, the value of 1 \<\< idx is the groupbit that can be compared to the per-atom "mask" property to determine if an atom is member of a group.

        Parameters[:]{.colon}

        :   **category** (*string*) -- name of category

        Returns[:]{.colon}

        :   list of id names in given category

        Return type[:]{.colon}

        :   list

    [[available_plugins]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[category]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.available_plugins "Link to this definition"){.headerlink}

    :   Returns a list of plugins available for a given category

        ::: versionadded
        [Added in version 10Mar2021.]{.versionmodified .added}
        :::

        This is a wrapper around the functions [`lammps_plugin_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre} and [`lammps_plugin_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre} of the library interface.

        Returns[:]{.colon}

        :   list of style/name pairs of loaded plugins

        Return type[:]{.colon}

        :   list

    [[set_fix_external_callback]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*, *[[callback]{.pre}]{.n}*, *[[caller]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.set_fix_external_callback "Link to this definition"){.headerlink}

    :   Set the callback function for a fix external instance with a given fix ID.

        Optionally also set a reference to the calling object.

        This is a wrapper around the [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal} function of the C-library interface. However this is set up to call a Python function with the following arguments.

        - object is the value of the "caller" argument

        - ntimestep is the current timestep

        - nlocal is the number of local atoms on the current MPI process

        - tag is a 1d NumPy array of integers representing the atom IDs of the local atoms

        - x is a 2d NumPy array of doubles of the coordinates of the local atoms

        - f is a 2d NumPy array of doubles of the forces on the local atoms that will be added

        ::: versionchanged
        [Changed in version 28Jul2021.]{.versionmodified .changed}
        :::

        Parameters[:]{.colon}

        :   - **fix_id** -- Fix-ID of a fix external instance

            - **callback** -- Python function that will be called from fix external

            - **caller** -- reference to some object passed to the callback function

        Type[:]{.colon}

        :   string

        Type[:]{.colon}

        :   function

        Type[:]{.colon}

        :   object, optional

    [[fix_external_get_force]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.fix_external_get_force "Link to this definition"){.headerlink}

    :   Get access to the array with per-atom forces of a fix external instance with a given fix ID.

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_fix_external_get_force()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv429lammps_fix_external_get_forcePvPKc "lammps_fix_external_get_force"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   **fix_id** -- Fix-ID of a fix external instance

        Type[:]{.colon}

        :   string

        Returns[:]{.colon}

        :   requested data

        Return type[:]{.colon}

        :   ctypes.POINTER(ctypes.POINTER(ctypes.double))

    [[fix_external_set_energy_global]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*, *[[eng]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.fix_external_set_energy_global "Link to this definition"){.headerlink}

    :   Set the global energy contribution for a fix external instance with the given ID.

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_fix_external_set_energy_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv437lammps_fix_external_set_energy_globalPvPKcd "lammps_fix_external_set_energy_global"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **fix_id** -- Fix-ID of a fix external instance

            - **eng** -- potential energy value to be added by fix external

        Type[:]{.colon}

        :   string

        Type[:]{.colon}

        :   float

    [[fix_external_set_virial_global]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*, *[[virial]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.fix_external_set_virial_global "Link to this definition"){.headerlink}

    :   Set the global virial contribution for a fix external instance with the given ID.

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_fix_external_set_virial_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv437lammps_fix_external_set_virial_globalPvPKcPd "lammps_fix_external_set_virial_global"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **fix_id** -- Fix-ID of a fix external instance

            - **eng** -- list of 6 floating point numbers with the virial to be added by fix external

        Type[:]{.colon}

        :   string

        Type[:]{.colon}

        :   float

    [[fix_external_set_energy_peratom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*, *[[eatom]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.fix_external_set_energy_peratom "Link to this definition"){.headerlink}

    :   Set the per-atom energy contribution for a fix external instance with the given ID.

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_fix_external_set_energy_peratom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv438lammps_fix_external_set_energy_peratomPvPKcPd "lammps_fix_external_set_energy_peratom"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **fix_id** -- Fix-ID of a fix external instance

            - **eatom** -- list of potential energy values for local atoms to be added by fix external

        Type[:]{.colon}

        :   string

        Type[:]{.colon}

        :   float

    [[fix_external_set_virial_peratom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*, *[[vatom]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.fix_external_set_virial_peratom "Link to this definition"){.headerlink}

    :   Set the per-atom virial contribution for a fix external instance with the given ID.

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_fix_external_set_virial_peratom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv438lammps_fix_external_set_virial_peratomPvPKcPPd "lammps_fix_external_set_virial_peratom"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **fix_id** -- Fix-ID of a fix external instance

            - **vatom** -- list of natoms lists with 6 floating point numbers to be added by fix external

        Type[:]{.colon}

        :   string

        Type[:]{.colon}

        :   float

    [[fix_external_set_vector_length]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*, *[[length]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.fix_external_set_vector_length "Link to this definition"){.headerlink}

    :   Set the vector length for a global vector stored with fix external for analysis

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_fix_external_set_vector_length()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv437lammps_fix_external_set_vector_lengthPvPKci "lammps_fix_external_set_vector_length"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **fix_id** -- Fix-ID of a fix external instance

            - **length** -- length of the global vector

        Type[:]{.colon}

        :   string

        Type[:]{.colon}

        :   int

    [[fix_external_set_vector]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*, *[[idx]{.pre}]{.n}*, *[[val]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.fix_external_set_vector "Link to this definition"){.headerlink}

    :   Store a global vector value for a fix external instance with the given ID.

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This is a wrapper around the [[`lammps_fix_external_set_vector()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv430lammps_fix_external_set_vectorPvPKcid "lammps_fix_external_set_vector"){.reference .internal} function of the C-library interface.

        Parameters[:]{.colon}

        :   - **fix_id** -- Fix-ID of a fix external instance

            - **idx** -- 1-based index of the value in the global vector

            - **val** -- value to be stored in the global vector

        Type[:]{.colon}

        :   string

        Type[:]{.colon}

        :   int

        Type[:]{.colon}

        :   float

    [[get_neighlist]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[idx]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.get_neighlist "Link to this definition"){.headerlink}

    :   Returns an instance of [[`NeighList`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#lammps.NeighList "lammps.NeighList"){.reference .internal} which wraps access to the neighbor list with the given index

        See [[`lammps.numpy.get_neighlist()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.numpy_wrapper.numpy_wrapper.get_neighlist "lammps.numpy_wrapper.numpy_wrapper.get_neighlist"){.reference .internal} if you want to use NumPy arrays instead of [`c_int`{.docutils .literal .notranslate}]{.pre} pointers.

        Parameters[:]{.colon}

        :   **idx** (*int*) -- index of neighbor list

        Returns[:]{.colon}

        :   an instance of [[`NeighList`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#lammps.NeighList "lammps.NeighList"){.reference .internal} wrapping access to neighbor list data

        Return type[:]{.colon}

        :   [NeighList](#lammps.NeighList "lammps.NeighList"){.reference .internal}

    [[get_neighlist_size]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[idx]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.get_neighlist_size "Link to this definition"){.headerlink}

    :   Return the number of elements in neighbor list with the given index

        Parameters[:]{.colon}

        :   **idx** (*int*) -- neighbor list index

        Returns[:]{.colon}

        :   number of elements in neighbor list with index idx

        Return type[:]{.colon}

        :   int

    [[get_neighlist_element_neighbors]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[idx]{.pre}]{.n}*, *[[element]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.lammps.get_neighlist_element_neighbors "Link to this definition"){.headerlink}

    :   Return data of neighbor list entry

        Parameters[:]{.colon}

        :   - **element** (*int*) -- neighbor list index

            - **element** -- neighbor list element index

        Returns[:]{.colon}

        :   tuple with atom local index, number of neighbors and array of neighbor local atom indices

        Return type[:]{.colon}

        :   (int, int, POINTER(c_int))

    [[find_pair_neighlist]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[style]{.pre}]{.n}*, *[[exact]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[nsub]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*, *[[reqid]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.find_pair_neighlist "Link to this definition"){.headerlink}

    :   Find neighbor list index of pair style neighbor list

        Search for a neighbor list requested by a pair style instance that matches "style". If exact is True, the pair style name must match exactly. If exact is False, the pair style name is matched against "style" as regular expression or sub-string. If the pair style is a hybrid pair style, the style is instead matched against the hybrid sub-styles. If the same pair style is used as sub-style multiple types, you must set nsub to a value n \> 0 which indicates the nth instance of that sub-style to be used (same as for the pair_coeff command). The default value of 0 will fail to match in that case.

        Once the pair style instance has been identified, it may have requested multiple neighbor lists. Those are uniquely identified by a request ID \> 0 as set by the pair style. Otherwise the request ID is 0.

        Parameters[:]{.colon}

        :   - **style** (*string*) -- name of pair style that should be searched for

            - **exact** (*bool,* *optional*) -- controls whether style should match exactly or only must be contained in pair style name, defaults to True

            - **nsub** (*int,* *optional*) -- match nsub-th hybrid sub-style, defaults to 0

            - **reqid** (*int,* *optional*) -- list request id, \> 0 in case there are more than one, defaults to 0

        Returns[:]{.colon}

        :   neighbor list index if found, otherwise -1

        Return type[:]{.colon}

        :   int

    [[find_fix_neighlist]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fixid]{.pre}]{.n}*, *[[reqid]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.find_fix_neighlist "Link to this definition"){.headerlink}

    :   Find neighbor list index of fix neighbor list

        The fix instance requesting the neighbor list is uniquely identified by the fix ID. In case the fix has requested multiple neighbor lists, those are uniquely identified by a request ID \> 0 as set by the fix. Otherwise the request ID is 0 (the default).

        Parameters[:]{.colon}

        :   - **fixid** (*string*) -- name of fix

            - **reqid** (*int,* *optional*) -- id of neighbor list request, in case there are more than one request, defaults to 0

        Returns[:]{.colon}

        :   neighbor list index if found, otherwise -1

        Return type[:]{.colon}

        :   int

    [[find_compute_neighlist]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[computeid]{.pre}]{.n}*, *[[reqid]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.lammps.find_compute_neighlist "Link to this definition"){.headerlink}

    :   Find neighbor list index of compute neighbor list

        The compute instance requesting the neighbor list is uniquely identified by the compute ID. In case the compute has requested multiple neighbor lists, those are uniquely identified by a request ID \> 0 as set by the compute. Otherwise the request ID is 0 (the default).

        Parameters[:]{.colon}

        :   - **computeid** (*string*) -- name of compute

            - **reqid** (*int,* *optional*) -- index of neighbor list request, in case there are more than one request, defaults to 0

        Returns[:]{.colon}

        :   neighbor list index if found, otherwise -1

        Return type[:]{.colon}

        :   int

<!-- -->

*[[class]{.pre}]{.k}[ ]{.w}*[[lammps.numpy_wrapper.]{.pre}]{.sig-prename .descclassname}[[numpy_wrapper]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[lmp]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper "Link to this definition"){.headerlink}

:   lammps API NumPy Wrapper

    This is a wrapper class that provides additional methods on top of an existing [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} instance. The methods transform raw ctypes pointers into NumPy arrays, which give direct access to the original data while protecting against out-of-bounds accesses.

    There is no need to explicitly instantiate this class. Each instance of [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} has a [`numpy`{.xref .py .py-attr .docutils .literal .notranslate}]{.pre} property that returns an instance.

    Parameters[:]{.colon}

    :   **lmp** ([*lammps*](#lammps.lammps "lammps.lammps"){.reference .internal}) -- instance of the [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} class

    [[extract_atom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[dtype]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[nelem]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[dim]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.extract_atom "Link to this definition"){.headerlink}

    :   Retrieve per-atom properties from LAMMPS as NumPy arrays

        This is a wrapper around the [`lammps.extract_atom()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre} method. It behaves the same as the original method, but returns NumPy arrays instead of [`ctypes`{.docutils .literal .notranslate}]{.pre} pointers.

        ::: {.admonition .note}
        Note

        The returned vectors or arrays of per-atom data are dimensioned according to the return value of [`lammps.extract_atom_size()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}. Except for the "mass" property, the underlying storage will always be dimensioned for the range \[0:nmax\]. The actual usable data may be only in the range \[0:nlocal\] or \[0:nlocal\]\[0:dim\]. Whether there is valid data in the range \[nlocal:nlocal+nghost\] or \[nlocal:local+nghost\]\[0:dim\] depends on whether the property of interest is also updated for ghost atoms. Also the value of *dim* depends on the value of *name*. By using the optional *nelem* and *dim* parameters the dimensions of the returned NumPy array can be overridden. There is no check whether the number of elements chosen is valid.
        :::

        Parameters[:]{.colon}

        :   - **name** (*string*) -- name of the property

            - **dtype** (*int,* *optional*) -- type of the returned data (see [[Data Types]{.std .std-ref}](#py-datatype-constants){.reference .internal})

            - **nelem** (*int,* *optional*) -- number of elements in array

            - **dim** (*int,* *optional*) -- dimension of each element

        Returns[:]{.colon}

        :   requested data as NumPy array with direct access to C data or None

        Return type[:]{.colon}

        :   numpy.array or NoneType

    [[extract_compute]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[cid]{.pre}]{.n}*, *[[cstyle]{.pre}]{.n}*, *[[ctype]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.extract_compute "Link to this definition"){.headerlink}

    :   Retrieve data from a LAMMPS compute

        This is a wrapper around the [[`lammps.extract_compute()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_compute "lammps.lammps.extract_compute"){.reference .internal} method. It behaves the same as the original method, but returns NumPy arrays instead of [`ctypes`{.docutils .literal .notranslate}]{.pre} pointers.

        Parameters[:]{.colon}

        :   - **cid** (*string*) -- compute ID

            - **cstyle** (*int*) -- style of the data retrieve (global, atom, or local), see [[Style Constants]{.std .std-ref}](#py-style-constants){.reference .internal}

            - **ctype** (*int*) -- type of the returned data (scalar, vector, or array), see [[Type Constants]{.std .std-ref}](#py-type-constants){.reference .internal}

        Returns[:]{.colon}

        :   requested data either as float, as NumPy array with direct access to C data, or None

        Return type[:]{.colon}

        :   float, numpy.array, or NoneType

    [[extract_fix]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fid]{.pre}]{.n}*, *[[fstyle]{.pre}]{.n}*, *[[ftype]{.pre}]{.n}*, *[[nrow]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*, *[[ncol]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.extract_fix "Link to this definition"){.headerlink}

    :   Retrieve data from a LAMMPS fix

        This is a wrapper around the [[`lammps.extract_fix()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_fix "lammps.lammps.extract_fix"){.reference .internal} method. It behaves the same as the original method, but returns NumPy arrays instead of [`ctypes`{.docutils .literal .notranslate}]{.pre} pointers.

        ::: {.admonition .note}
        Note

        When requesting global data, the fix data can only be accessed one item at a time without access to the whole vector or array. Thus this function will always return a scalar. To access vector or array elements the "nrow" and "ncol" arguments need to be set accordingly (they default to 0).
        :::

        Parameters[:]{.colon}

        :   - **fid** (*string*) -- fix ID

            - **fstyle** (*int*) -- style of the data retrieve (global, atom, or local), see [[Style Constants]{.std .std-ref}](#py-style-constants){.reference .internal}

            - **ftype** (*int*) -- type or size of the returned data (scalar, vector, or array), see [[Type Constants]{.std .std-ref}](#py-type-constants){.reference .internal}

            - **nrow** (*int*) -- index of global vector element or row index of global array element

            - **ncol** (*int*) -- column index of global array element

        Returns[:]{.colon}

        :   requested data

        Return type[:]{.colon}

        :   integer or double value, pointer to 1d or 2d double array or None

    [[extract_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[group]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[vartype]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.extract_variable "Link to this definition"){.headerlink}

    :   Evaluate a LAMMPS variable and return its data

        This function is a wrapper around the function [[`lammps.extract_variable()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_variable "lammps.lammps.extract_variable"){.reference .internal} method. It behaves the same as the original method, but returns NumPy arrays instead of [`ctypes`{.docutils .literal .notranslate}]{.pre} pointers.

        Parameters[:]{.colon}

        :   - **name** (*string*) -- name of the variable to execute

            - **group** (*string*) -- name of group for atom-style variable (ignored for equal-style variables)

            - **vartype** (*int*) -- type of variable, see [[Variable Type Constants]{.std .std-ref}](#py-vartype-constants){.reference .internal}

        Returns[:]{.colon}

        :   the requested data or None

        Return type[:]{.colon}

        :   c_double, numpy.array, or NoneType

    [[gather_bonds]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.gather_bonds "Link to this definition"){.headerlink}

    :   Retrieve global list of bonds as a NumPy array

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This is a wrapper around [[`lammps.gather_bonds()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.gather_bonds "lammps.lammps.gather_bonds"){.reference .internal}. It behaves the same as the original method, but returns a NumPy array instead of a [`ctypes`{.docutils .literal .notranslate}]{.pre} list.

        Returns[:]{.colon}

        :   the requested data as a 2d-integer numpy array

        Return type[:]{.colon}

        :   numpy.array(nbonds,3)

    [[gather_angles]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.gather_angles "Link to this definition"){.headerlink}

    :   Retrieve global list of angles as a NumPy array

        ::: versionadded
        [Added in version 8Feb2023.]{.versionmodified .added}
        :::

        This is a wrapper around [[`lammps.gather_angles()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.gather_angles "lammps.lammps.gather_angles"){.reference .internal}. It behaves the same as the original method, but returns a NumPy array instead of a [`ctypes`{.docutils .literal .notranslate}]{.pre} list.

        Returns[:]{.colon}

        :   the requested data as a 2d-integer numpy array

        Return type[:]{.colon}

        :   numpy.array(nangles,4)

    [[gather_dihedrals]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.gather_dihedrals "Link to this definition"){.headerlink}

    :   Retrieve global list of dihedrals as a NumPy array

        ::: versionadded
        [Added in version 8Feb2023.]{.versionmodified .added}
        :::

        This is a wrapper around [[`lammps.gather_dihedrals()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.gather_dihedrals "lammps.lammps.gather_dihedrals"){.reference .internal}. It behaves the same as the original method, but returns a NumPy array instead of a [`ctypes`{.docutils .literal .notranslate}]{.pre} list.

        Returns[:]{.colon}

        :   the requested data as a 2d-integer numpy array

        Return type[:]{.colon}

        :   numpy.array(ndihedrals,5)

    [[gather_impropers]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.gather_impropers "Link to this definition"){.headerlink}

    :   Retrieve global list of impropers as a NumPy array

        ::: versionadded
        [Added in version 8Feb2023.]{.versionmodified .added}
        :::

        This is a wrapper around [[`lammps.gather_impropers()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.gather_impropers "lammps.lammps.gather_impropers"){.reference .internal}. It behaves the same as the original method, but returns a NumPy array instead of a [`ctypes`{.docutils .literal .notranslate}]{.pre} list.

        Returns[:]{.colon}

        :   the requested data as a 2d-integer numpy array

        Return type[:]{.colon}

        :   numpy.array(nimpropers,5)

    [[fix_external_get_force]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.fix_external_get_force "Link to this definition"){.headerlink}

    :   Get access to the array with per-atom forces of a fix external instance with a given fix ID.

        ::: versionchanged
        [Changed in version 28Jul2021.]{.versionmodified .changed}
        :::

        This function is a wrapper around the [[`lammps.fix_external_get_force()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.fix_external_get_force "lammps.lammps.fix_external_get_force"){.reference .internal} method. It behaves the same as the original method, but returns a NumPy array instead of a [`ctypes`{.docutils .literal .notranslate}]{.pre} pointer.

        Parameters[:]{.colon}

        :   **fix_id** -- Fix-ID of a fix external instance

        Type[:]{.colon}

        :   string

        Returns[:]{.colon}

        :   requested data

        Return type[:]{.colon}

        :   numpy.array

    [[fix_external_set_energy_peratom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*, *[[eatom]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.fix_external_set_energy_peratom "Link to this definition"){.headerlink}

    :   Set the per-atom energy contribution for a fix external instance with the given ID.

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This function is an alternative to [[`lammps.fix_external_set_energy_peratom()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.fix_external_set_energy_peratom "lammps.lammps.fix_external_set_energy_peratom"){.reference .internal} method. It behaves the same as the original method, but accepts a NumPy array instead of a list as argument.

        Parameters[:]{.colon}

        :   - **fix_id** -- Fix-ID of a fix external instance

            - **eatom** -- per-atom potential energy

        Type[:]{.colon}

        :   string

        Type[:]{.colon}

        :   numpy.array

    [[fix_external_set_virial_peratom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fix_id]{.pre}]{.n}*, *[[vatom]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.fix_external_set_virial_peratom "Link to this definition"){.headerlink}

    :   Set the per-atom virial contribution for a fix external instance with the given ID.

        ::: versionadded
        [Added in version 28Jul2021.]{.versionmodified .added}
        :::

        This function is an alternative to [[`lammps.fix_external_set_virial_peratom()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.fix_external_set_virial_peratom "lammps.lammps.fix_external_set_virial_peratom"){.reference .internal} method. It behaves the same as the original method, but accepts a NumPy array instead of a list as argument.

        Parameters[:]{.colon}

        :   - **fix_id** -- Fix-ID of a fix external instance

            - **eatom** -- per-atom potential energy

        Type[:]{.colon}

        :   string

        Type[:]{.colon}

        :   numpy.array

    [[get_neighlist]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[idx]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.get_neighlist "Link to this definition"){.headerlink}

    :   Returns an instance of [[`NumPyNeighList`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#lammps.numpy_wrapper.NumPyNeighList "lammps.numpy_wrapper.NumPyNeighList"){.reference .internal} which wraps access to the neighbor list with the given index

        Parameters[:]{.colon}

        :   **idx** (*int*) -- index of neighbor list

        Returns[:]{.colon}

        :   an instance of [[`NumPyNeighList`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#lammps.numpy_wrapper.NumPyNeighList "lammps.numpy_wrapper.NumPyNeighList"){.reference .internal} wrapping access to neighbor list data

        Return type[:]{.colon}

        :   [NumPyNeighList](#lammps.numpy_wrapper.NumPyNeighList "lammps.numpy_wrapper.NumPyNeighList"){.reference .internal}

    [[get_neighlist_element_neighbors]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[idx]{.pre}]{.n}*, *[[element]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.get_neighlist_element_neighbors "Link to this definition"){.headerlink}

    :   Return data of neighbor list entry

        This function is a wrapper around the function [[`lammps.get_neighlist_element_neighbors()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}](#lammps.lammps.get_neighlist_element_neighbors "lammps.lammps.get_neighlist_element_neighbors"){.reference .internal} method. It behaves the same as the original method, but returns a NumPy array containing the neighbors instead of a [`ctypes`{.docutils .literal .notranslate}]{.pre} pointer.

        Parameters[:]{.colon}

        :   - **element** (*int*) -- neighbor list index

            - **element** -- neighbor list element index

        Returns[:]{.colon}

        :   tuple with atom local index and numpy array of neighbor local atom indices

        Return type[:]{.colon}

        :   (int, numpy.array)

    [[iarray]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[c_int_type]{.pre}]{.n}*, *[[raw_ptr]{.pre}]{.n}*, *[[nelem]{.pre}]{.n}*, *[[dim]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.iarray "Link to this definition"){.headerlink}

    :   Convert ctypes pointer to an array of integers into a corresponding numpy array

        This will cast the raw pointer into a 1-d or 2-d numpy array and set its shape

        Parameters[:]{.colon}

        :   - **c_int_type** -- type of integer (c_int32 or c_int64)

            - **raw_ptr** -- ctypes pointer to the array data

            - **nelem** -- length of the leading dimension

            - **dim** -- length of the second dimension

        Type[:]{.colon}

        :   ctypes type

        Type[:]{.colon}

        :   POINTER(c_int_type)

        Type[:]{.colon}

        :   integer

        Type[:]{.colon}

        :   integer, optional

        Returns[:]{.colon}

        :   ctypes array converted to numpy style array with proper shape

        Return type[:]{.colon}

        :   numpy.array

    [[darray]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[raw_ptr]{.pre}]{.n}*, *[[nelem]{.pre}]{.n}*, *[[dim]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.numpy_wrapper.numpy_wrapper.darray "Link to this definition"){.headerlink}

    :   Convert ctypes pointer to an array of doubles into a corresponding numpy array

        This will cast the raw pointer into a 1-d or 2-d numpy array and set its shape

        Parameters[:]{.colon}

        :   - **raw_ptr** -- ctypes pointer to the array data

            - **nelem** -- length of the leading dimension

            - **dim** -- length of the second dimension

        Type[:]{.colon}

        :   POINTER(c_double)

        Type[:]{.colon}

        :   integer

        Type[:]{.colon}

        :   integer, optional

        Returns[:]{.colon}

        :   ctypes array converted to numpy style array with proper shape

        Return type[:]{.colon}

        :   numpy.array

<!-- -->

*[[class]{.pre}]{.k}[ ]{.w}*[[lammps.ipython.]{.pre}]{.sig-prename .descclassname}[[wrapper]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[lmp]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.ipython.wrapper "Link to this definition"){.headerlink}

:   lammps API IPython Wrapper

    This is a wrapper class that provides additional methods on top of an existing [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} instance. It provides additional methods that allow create and/or embed visualizations created by native LAMMPS commands.

    There is no need to explicitly instantiate this class. Each instance of [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} has a [`ipython`{.xref .py .py-attr .docutils .literal .notranslate}]{.pre} property that returns an instance.

    Parameters[:]{.colon}

    :   **lmp** ([*lammps*](#lammps.lammps "lammps.lammps"){.reference .internal}) -- instance of the [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} class

    [[image]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}[[=]{.pre}]{.o}[[\'snapshot.png\']{.pre}]{.default_value}*, *[[group]{.pre}]{.n}[[=]{.pre}]{.o}[[\'all\']{.pre}]{.default_value}*, *[[color]{.pre}]{.n}[[=]{.pre}]{.o}[[\'type\']{.pre}]{.default_value}*, *[[diameter]{.pre}]{.n}[[=]{.pre}]{.o}[[\'type\']{.pre}]{.default_value}*, *[[size]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[view]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[center]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[up]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zoom]{.pre}]{.n}[[=]{.pre}]{.o}[[1.0]{.pre}]{.default_value}*, *[[background_color]{.pre}]{.n}[[=]{.pre}]{.o}[[\'white\']{.pre}]{.default_value}*[)]{.sig-paren}[](#lammps.ipython.wrapper.image "Link to this definition"){.headerlink}

    :   Generate image using write_dump command and display it

        See [[dump image]{.doc}]dump_image.md){.reference .internal} for more information.

        Parameters[:]{.colon}

        :   - **filename** (*string*) -- Name of the image file that should be generated. The extension determines whether it is PNG or JPEG

            - **group** (*string*) -- the group of atoms write_image should use

            - **color** (*string*) -- name of property used to determine color

            - **diameter** (*string*) -- name of property used to determine atom diameter

            - **size** (*tuple* *(width,* *height)*) -- dimensions of image

            - **view** (*tuple* *(theta,* *phi)*) -- view parameters

            - **center** (*tuple* *(flag,* *center_x,* *center_y,* *center_z)*) -- center parameters

            - **up** (*tuple* *(up_x,* *up_y,* *up_z)*) -- vector pointing to up direction

            - **zoom** (*float*) -- zoom factor

            - **background_color** (*string*) -- background color of scene

        Returns[:]{.colon}

        :   Image instance used to display image in notebook

        Return type[:]{.colon}

        :   [`IPython.core.display.Image`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}

    [[video]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.ipython.wrapper.video "Link to this definition"){.headerlink}

    :   Load video from file

        Can be used to visualize videos from [[dump movie]{.doc}]dump_image.md){.reference .internal}.

        Parameters[:]{.colon}

        :   **filename** (*string*) -- Path to video file

        Returns[:]{.colon}

        :   HTML Video Tag used by notebook to embed a video

        Return type[:]{.colon}

        :   [`IPython.display.HTML`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}
:::

------------------------------------------------------------------------

:::::::: {#additional-components-of-the-lammps-module .section}
## [2.4.2. ]{.section-number}Additional components of the [`lammps`{.docutils .literal .notranslate}]{.pre} module[](#additional-components-of-the-lammps-module "Link to this heading"){.headerlink}

The [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module additionally contains several constants and the [[`NeighList`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#lammps.NeighList "lammps.NeighList"){.reference .internal} class:

::: {#data-types .section}
[]{#py-datatype-constants}

### Data Types[](#data-types "Link to this heading"){.headerlink}

[[LAMMPS_INT,]{.pre} [LAMMPS_INT_2D,]{.pre} [LAMMPS_DOUBLE,]{.pre} [LAMMPS_DOUBLE_2D,]{.pre} [LAMMPS_INT64,]{.pre} [LAMMPS_INT64_2D,]{.pre} [LAMMPS_STRING]{.pre}]{.sig-name .descname}

:   Constants in the [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module to indicate how to cast data when the C library function returns a void pointer. Used in [[`lammps.extract_global()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_global "lammps.lammps.extract_global"){.reference .internal} and [[`lammps.extract_atom()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_atom "lammps.lammps.extract_atom"){.reference .internal}. See [`_LMP_DATATYPE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre} for the equivalent constants in the C library interface.
:::

::: {#style-constants .section}
[]{#py-style-constants}

### Style Constants[](#style-constants "Link to this heading"){.headerlink}

[[LMP_STYLE_GLOBAL,]{.pre} [LMP_STYLE_ATOM,]{.pre} [LMP_STYLE_LOCAL]{.pre}]{.sig-name .descname}

:   Constants in the [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module to select what style of data to request from computes or fixes. See [[`_LMP_STYLE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv416_LMP_STYLE_CONST "_LMP_STYLE_CONST"){.reference .internal} for the equivalent constants in the C library interface. Used in [[`lammps.extract_compute()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_compute "lammps.lammps.extract_compute"){.reference .internal}, [[`lammps.extract_fix()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_fix "lammps.lammps.extract_fix"){.reference .internal}, and their NumPy variants [[`lammps.numpy.extract_compute()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.numpy_wrapper.numpy_wrapper.extract_compute "lammps.numpy_wrapper.numpy_wrapper.extract_compute"){.reference .internal} and [[`lammps.numpy.extract_fix()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.numpy_wrapper.numpy_wrapper.extract_fix "lammps.numpy_wrapper.numpy_wrapper.extract_fix"){.reference .internal}.
:::

::: {#type-constants .section}
[]{#py-type-constants}

### Type Constants[](#type-constants "Link to this heading"){.headerlink}

[[LMP_TYPE_SCALAR,]{.pre} [LMP_TYPE_VECTOR,]{.pre} [LMP_TYPE_ARRAY,]{.pre} [LMP_SIZE_VECTOR,]{.pre} [LMP_SIZE_ROWS,]{.pre} [LMP_SIZE_COLS]{.pre}]{.sig-name .descname}

:   Constants in the [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module to select what type of data to request from computes or fixes. See [[`_LMP_TYPE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv415_LMP_TYPE_CONST "_LMP_TYPE_CONST"){.reference .internal} for the equivalent constants in the C library interface. Used in [[`lammps.extract_compute()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_compute "lammps.lammps.extract_compute"){.reference .internal}, [[`lammps.extract_fix()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_fix "lammps.lammps.extract_fix"){.reference .internal}, and their NumPy variants [[`lammps.numpy.extract_compute()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.numpy_wrapper.numpy_wrapper.extract_compute "lammps.numpy_wrapper.numpy_wrapper.extract_compute"){.reference .internal} and [[`lammps.numpy.extract_fix()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.numpy_wrapper.numpy_wrapper.extract_fix "lammps.numpy_wrapper.numpy_wrapper.extract_fix"){.reference .internal}.
:::

::: {#variable-type-constants .section}
[]{#py-vartype-constants}

### Variable Type Constants[](#variable-type-constants "Link to this heading"){.headerlink}

[[LMP_VAR_EQUAL,]{.pre} [LMP_VAR_ATOM]{.pre}]{.sig-name .descname}

:   Constants in the [[`lammps`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal} module to select what type of variable to query when calling [[`lammps.extract_variable()`{.xref .py .py-func .docutils .literal .notranslate}]{.pre}](#lammps.lammps.extract_variable "lammps.lammps.extract_variable"){.reference .internal}. See also: [[variable command]{.doc}]variable.md){.reference .internal}.
:::

::: {#classes-representing-internal-objects .section}
### Classes representing internal objects[](#classes-representing-internal-objects "Link to this heading"){.headerlink}

*[[class]{.pre}]{.k}[ ]{.w}*[[lammps.]{.pre}]{.sig-prename .descclassname}[[NeighList]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[lmp]{.pre}]{.n}*, *[[idx]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.NeighList "Link to this definition"){.headerlink}

:   This is a wrapper class that exposes the contents of a neighbor list.

    It can be used like a regular Python list. Each element is a tuple of:

    - the atom local index

    - its number of neighbors

    - and a pointer to an c_int array containing local atom indices of its neighbors

    Internally it uses the lower-level LAMMPS C-library interface.

    Parameters[:]{.colon}

    :   - **lmp** ([*lammps*](#lammps.lammps "lammps.lammps"){.reference .internal}) -- reference to instance of [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal}

        - **idx** (*int*) -- neighbor list index

    *[[property]{.pre}]{.k}[ ]{.w}*[[size]{.pre}]{.sig-name .descname}[](#lammps.NeighList.size "Link to this definition"){.headerlink}

    :   

        Returns[:]{.colon}

        :   number of elements in neighbor list

    [[get]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.NeighList.get "Link to this definition"){.headerlink}

    :   Access a specific neighbor list entry. "element" must be a number from 0 to the size-1 of the list

        Returns[:]{.colon}

        :   tuple with atom local index, number of neighbors and ctypes pointer to neighbor's local atom indices

        Return type[:]{.colon}

        :   (int, int, ctypes.POINTER(c_int))

    [[find]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[iatom]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.NeighList.find "Link to this definition"){.headerlink}

    :   Find the neighbor list for a specific (local) atom iatom. If there is no list for iatom, (-1, None) is returned.

        Returns[:]{.colon}

        :   tuple with number of neighbors and ctypes pointer to neighbor's local atom indices

        Return type[:]{.colon}

        :   (int, ctypes.POINTER(c_int))

<!-- -->

*[[class]{.pre}]{.k}[ ]{.w}*[[lammps.numpy_wrapper.]{.pre}]{.sig-prename .descclassname}[[NumPyNeighList]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[lmp]{.pre}]{.n}*, *[[idx]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.NumPyNeighList "Link to this definition"){.headerlink}

:   This is a wrapper class that exposes the contents of a neighbor list.

    It can be used like a regular Python list. Each element is a tuple of:

    - the atom local index

    - a NumPy array containing the local atom indices of its neighbors

    Internally it uses the lower-level LAMMPS C-library interface.

    Parameters[:]{.colon}

    :   - **lmp** ([*lammps*](#lammps.lammps "lammps.lammps"){.reference .internal}) -- reference to instance of [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](#module-lammps "lammps"){.reference .internal}

        - **idx** (*int*) -- neighbor list index

    [[get]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.NumPyNeighList.get "Link to this definition"){.headerlink}

    :   Access a specific neighbor list entry. "element" must be a number from 0 to the size-1 of the list

        Returns[:]{.colon}

        :   tuple with atom local index, numpy array of neighbor local atom indices

        Return type[:]{.colon}

        :   (int, numpy.array)

    [[find]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[iatom]{.pre}]{.n}*[)]{.sig-paren}[](#lammps.numpy_wrapper.NumPyNeighList.find "Link to this definition"){.headerlink}

    :   Find the neighbor list for a specific (local) atom iatom. If there is no list for iatom, None is returned.

        Returns[:]{.colon}

        :   numpy array of neighbor local atom indices

        Return type[:]{.colon}

        :   numpy.array or None
:::
::::::::
::::::::::::
:::::::::::::
::::::::::::::

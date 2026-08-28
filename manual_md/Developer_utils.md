::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::: {#utility-functions .section}
# [4.15. ]{.section-number}Utility functions[](#utility-functions "Link to this heading"){.headerlink}

The [`utils`{.docutils .literal .notranslate}]{.pre} sub-namespace inside the [`LAMMPS_NS`{.docutils .literal .notranslate}]{.pre} namespace provides a collection of convenience functions and utilities that perform common tasks that are required repeatedly throughout the LAMMPS code like reading or writing to files with error checking or translation of strings into specific types of numbers with checking for validity. This reduces redundant implementations and encourages consistent behavior and thus has some overlap with the [["platform" sub-namespace]{.doc}]Developer_platform.md){.reference .internal}.

- [I/O with status check and similar functions](#i-o-with-status-check-and-similar-functions){#id11 .reference .internal}

- [String to number conversions with validity check](#string-to-number-conversions-with-validity-check){#id12 .reference .internal}

- [String processing](#string-processing){#id13 .reference .internal}

- [Potential file functions](#potential-file-functions){#id14 .reference .internal}

- [Argument processing](#argument-processing){#id15 .reference .internal}

- [Convenience functions](#convenience-functions){#id16 .reference .internal}

- [Customized standard functions](#customized-standard-functions){#id17 .reference .internal}

------------------------------------------------------------------------

::: {#i-o-with-status-check-and-similar-functions .section}
## [[4.15.1. ]{.section-number}I/O with status check and similar functions](#id11){.toc-backref role="doc-backlink"}[](#i-o-with-status-check-and-similar-functions "Link to this heading"){.headerlink}

The the first two functions are wrappers around the corresponding C library calls [`fgets()`{.docutils .literal .notranslate}]{.pre} or [`fread()`{.docutils .literal .notranslate}]{.pre}. They will check if there were errors on reading or an unexpected end-of-file state was reached. In that case, the functions will stop with an error message, indicating the name of the problematic file, if possible unless the *error* argument is a NULL pointer.

The [[`utils::fgets_trunc()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils11fgets_truncEPciP4FILE "LAMMPS_NS::utils::fgets_trunc"){.reference .internal} function will work similar for [`fgets()`{.docutils .literal .notranslate}]{.pre} but it will read in a whole line (i.e. until the end of line or end of file), but store only as many characters as will fit into the buffer including a final newline character and the terminating NULL byte. If the line in the file is longer it will thus be truncated in the buffer. This function is used by [[`utils::read_lines_from_file()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils20read_lines_from_fileEP4FILEiiPci8MPI_Comm "LAMMPS_NS::utils::read_lines_from_file"){.reference .internal} to read individual lines but make certain they follow the size constraints.

The [[`utils::read_lines_from_file()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils20read_lines_from_fileEP4FILEiiPci8MPI_Comm "LAMMPS_NS::utils::read_lines_from_file"){.reference .internal} function will read the requested number of lines of a maximum length into a buffer and will return 0 if successful or 1 if not. It also guarantees that all lines are terminated with a newline character and the entire buffer with a NULL character.

------------------------------------------------------------------------

[]{#_CPPv3N9LAMMPS_NS5utils6sfgetsEPKciPciP4FILEPKcP5Error}[]{#_CPPv2N9LAMMPS_NS5utils6sfgetsEPKciPciP4FILEPKcP5Error}[]{#LAMMPS_NS::utils::sfgets__cCP.i.cP.i.FILEP.cCP.ErrorP}[]{#utils_8h_1a151f0249d5fa35b2f79f9fd411f0c61b .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[sfgets]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[srcname]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[srcline]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[s]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[size]{.pre}]{.n .sig-param}, [[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[filename]{.pre}]{.n .sig-param}, [[Error]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[error]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils6sfgetsEPKciPciP4FILEPKcP5Error "Link to this definition"){.headerlink}\

:   Safe wrapper around fgets() which aborts on errors or EOF and prints a suitable error message to help debugging.

    Use nullptr as the error parameter to avoid the abort on EOF or error.

    Parameters[:]{.colon}

    :   - **srcname** -- name of the calling source file (from FLERR macro)

        - **srcline** -- line in the calling source file (from FLERR macro)

        - **s** -- buffer for storing the result of fgets()

        - **size** -- size of buffer s (max number of bytes read by fgets())

        - **fp** -- file pointer used by fgets()

        - **filename** -- file name associated with fp (may be a null pointer; then [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} will try to detect)

        - **error** -- pointer to Error class instance (for abort) or nullptr

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils6sfreadEPKciPv6size_t6size_tP4FILEPKcP5Error}[]{#_CPPv2N9LAMMPS_NS5utils6sfreadEPKciPv6size_t6size_tP4FILEPKcP5Error}[]{#LAMMPS_NS::utils::sfread__cCP.i.voidP.s.s.FILEP.cCP.ErrorP}[]{#utils_8h_1a5fc62aaa4658e16ec52523996d92af83 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[sfread]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[srcname]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[srcline]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[s]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[size]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[num]{.pre}]{.n .sig-param}, [[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[filename]{.pre}]{.n .sig-param}, [[Error]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[error]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils6sfreadEPKciPv6size_t6size_tP4FILEPKcP5Error "Link to this definition"){.headerlink}\

:   Safe wrapper around fread() which aborts on errors or EOF and prints a suitable error message to help debugging.

    Use nullptr as the error parameter to avoid the abort on EOF or error.

    Parameters[:]{.colon}

    :   - **srcname** -- name of the calling source file (from FLERR macro)

        - **srcline** -- line in the calling source file (from FLERR macro)

        - **s** -- buffer for storing the result of fread()

        - **size** -- size of data elements read by fread()

        - **num** -- number of data elements read by fread()

        - **fp** -- file pointer used by fread()

        - **filename** -- file name associated with fp (may be a null pointer; then [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} will try to detect)

        - **error** -- pointer to Error class instance (for abort) or nullptr

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11fgets_truncEPciP4FILE}[]{#_CPPv2N9LAMMPS_NS5utils11fgets_truncEPciP4FILE}[]{#LAMMPS_NS::utils::fgets_trunc__cP.i.FILEP}[]{#utils_8h_1ae2af7b66ca9a1980b73c1941779e2047 .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[fgets_trunc]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[s]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[size]{.pre}]{.n .sig-param}, [[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11fgets_truncEPciP4FILE "Link to this definition"){.headerlink}\

:   Wrapper around fgets() which reads whole lines but truncates the data to the buffer size and ensures a newline char at the end.

    This function is useful for reading line based text files with possible comments that should be parsed later. This applies to data files, potential files, atomfile variable files and so on. It is used instead of fgets() by utils::read_lines_from_file().

    Parameters[:]{.colon}

    :   - **s** -- buffer for storing the result of fgets()

        - **size** -- size of buffer s (max number of bytes returned)

        - **fp** -- file pointer used by fgets()

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils20read_lines_from_fileEP4FILEiiPci8MPI_Comm}[]{#_CPPv2N9LAMMPS_NS5utils20read_lines_from_fileEP4FILEiiPci8MPI_Comm}[]{#LAMMPS_NS::utils::read_lines_from_file__FILEP.i.i.cP.i.MPI_Comm}[]{#utils_8h_1a7de7c579867fe5cac7f68affc3c9d416 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[read_lines_from_file]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[nlines]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[nmax]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[buffer]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[me]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils20read_lines_from_fileEP4FILEiiPci8MPI_Comm "Link to this definition"){.headerlink}\

:   Read N lines of text from file into buffer and broadcast them

    This function uses repeated calls to fread() to fill a buffer with newline terminated text. If a line does not end in a newline (e.g. at the end of a file), it is added. The caller has to allocate an nlines by nmax sized buffer for storing the text data. Reading is done by MPI rank 0 of the given communicator only, and thus only MPI rank 0 needs to provide a valid file pointer.

    Parameters[:]{.colon}

    :   - **fp** -- file pointer used by fread

        - **nlines** -- number of lines to be read

        - **nmax** -- maximum length of a single line

        - **buffer** -- buffer for storing the data.

        - **me** -- MPI rank of calling process in MPI communicator

        - **comm** -- MPI communicator for broadcast

    Returns[:]{.colon}

    :   1 if the read was short, 0 if read was successful
:::

------------------------------------------------------------------------

::: {#string-to-number-conversions-with-validity-check .section}
## [[4.15.2. ]{.section-number}String to number conversions with validity check](#id12){.toc-backref role="doc-backlink"}[](#string-to-number-conversions-with-validity-check "Link to this heading"){.headerlink}

These functions should be used to convert strings to numbers. They are are strongly preferred over C library calls like [`atoi()`{.docutils .literal .notranslate}]{.pre} or [`atof()`{.docutils .literal .notranslate}]{.pre} since they check if the **entire** string is a valid (floating-point or integer) number, and will error out instead of silently returning the result of a partial conversion or zero in cases where the string is not a valid number. This behavior improves detecting typos or issues when processing input files.

Similarly the [[`utils::logical()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils7logicalEPKciRKNSt6stringEbP6LAMMPS "LAMMPS_NS::utils::logical"){.reference .internal} function will convert a string into a boolean and will only accept certain words.

The *do_abort* flag should be set to [`true`{.docutils .literal .notranslate}]{.pre} in case this function is called only on a single MPI rank, as that will then trigger the a call to [`Error::one()`{.docutils .literal .notranslate}]{.pre} for errors instead of [`Error::all()`{.docutils .literal .notranslate}]{.pre} and avoids a "hanging" calculation when run in parallel.

Please also see [[`utils::is_integer()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils10is_integerERKNSt6stringE "LAMMPS_NS::utils::is_integer"){.reference .internal} and [[`utils::is_double()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils9is_doubleERKNSt6stringE "LAMMPS_NS::utils::is_double"){.reference .internal} for testing strings for compliance without conversion.

------------------------------------------------------------------------

[]{#_CPPv3N9LAMMPS_NS5utils7numericEPKciRKNSt6stringEbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils7numericEPKciRKNSt6stringEbP6LAMMPS}[]{#LAMMPS_NS::utils::numeric__cCP.i.ssCR.b.LAMMPSP}[]{#utils_8h_1a68ccfc10e677337b215ccd51363a03aa .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[numeric]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils7numericEPKciRKNSt6stringEbP6LAMMPS "Link to this definition"){.headerlink}\

:   Convert a string to a floating point number while checking if it is a valid floating point or integer number

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to number

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   double precision floating point number

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils7numericEPKciPKcbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils7numericEPKciPKcbP6LAMMPS}[]{#LAMMPS_NS::utils::numeric__cCP.i.cCP.b.LAMMPSP}[]{#utils_8h_1a503fd271ff7cf07725ad0b03b6d7f762 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[numeric]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils7numericEPKciPKcbP6LAMMPS "Link to this definition"){.headerlink}\

:   This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to number

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   double precision floating point number

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8inumericEPKciRKNSt6stringEbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils8inumericEPKciRKNSt6stringEbP6LAMMPS}[]{#LAMMPS_NS::utils::inumeric__cCP.i.ssCR.b.LAMMPSP}[]{#utils_8h_1a72a1fc411c4fea8f116157d2deb9ecb0 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[inumeric]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8inumericEPKciRKNSt6stringEbP6LAMMPS "Link to this definition"){.headerlink}\

:   Convert a string to an integer number while checking if it is a valid integer number (regular int)

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to number

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   integer number (regular int)

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8inumericEPKciPKcbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils8inumericEPKciPKcbP6LAMMPS}[]{#LAMMPS_NS::utils::inumeric__cCP.i.cCP.b.LAMMPSP}[]{#utils_8h_1a0fa1caaa9b4c196fb960712e6f2dfe5d .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[inumeric]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8inumericEPKciPKcbP6LAMMPS "Link to this definition"){.headerlink}\

:   This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to number

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   double precision floating point number

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8bnumericEPKciRKNSt6stringEbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils8bnumericEPKciRKNSt6stringEbP6LAMMPS}[]{#LAMMPS_NS::utils::bnumeric__cCP.i.ssCR.b.LAMMPSP}[]{#utils_8h_1aa2fc5058efa5708a27f9f755f3b1e405 .target}[[bigint]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[bnumeric]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8bnumericEPKciRKNSt6stringEbP6LAMMPS "Link to this definition"){.headerlink}\

:   Convert a string to an integer number while checking if it is a valid integer number (bigint)

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to number

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   integer number (bigint)

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8bnumericEPKciPKcbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils8bnumericEPKciPKcbP6LAMMPS}[]{#LAMMPS_NS::utils::bnumeric__cCP.i.cCP.b.LAMMPSP}[]{#utils_8h_1af773a99c24a68d2055c9116ae1835f0a .target}[[bigint]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[bnumeric]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8bnumericEPKciPKcbP6LAMMPS "Link to this definition"){.headerlink}\

:   This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to number

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   double precision floating point number

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8tnumericEPKciRKNSt6stringEbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils8tnumericEPKciRKNSt6stringEbP6LAMMPS}[]{#LAMMPS_NS::utils::tnumeric__cCP.i.ssCR.b.LAMMPSP}[]{#utils_8h_1a64a163aaea54730784f7c1797369f106 .target}[[tagint]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[tnumeric]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8tnumericEPKciRKNSt6stringEbP6LAMMPS "Link to this definition"){.headerlink}\

:   Convert a string to an integer number while checking if it is a valid integer number (tagint)

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to number

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   integer number (tagint)

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8tnumericEPKciPKcbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils8tnumericEPKciPKcbP6LAMMPS}[]{#LAMMPS_NS::utils::tnumeric__cCP.i.cCP.b.LAMMPSP}[]{#utils_8h_1a4e8b8a6816b717518c30fd561e6e42fa .target}[[tagint]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[tnumeric]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8tnumericEPKciPKcbP6LAMMPS "Link to this definition"){.headerlink}\

:   This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to number

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   double precision floating point number

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils7logicalEPKciRKNSt6stringEbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils7logicalEPKciRKNSt6stringEbP6LAMMPS}[]{#LAMMPS_NS::utils::logical__cCP.i.ssCR.b.LAMMPSP}[]{#utils_8h_1a57df85d91e1593d0893945852f26eb12 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[logical]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils7logicalEPKciRKNSt6stringEbP6LAMMPS "Link to this definition"){.headerlink}\

:   Convert a string to a boolean while checking whether it is a valid boolean term. Valid terms are 'yes', 'no', 'true', 'false', 'on', 'off', and '1', '0'. Only lower case is accepted.

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to logical

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   1 if string resolves to "true", otherwise 0

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils7logicalEPKciPKcbP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils7logicalEPKciPKcbP6LAMMPS}[]{#LAMMPS_NS::utils::logical__cCP.i.cCP.b.LAMMPSP}[]{#utils_8h_1ae01f31ea9af04975dcdb062b3b340c2e .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[logical]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bool]{.pre}]{.kt}[ ]{.w}[[do_abort]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils7logicalEPKciPKcbP6LAMMPS "Link to this definition"){.headerlink}\

:   This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be converted to logical

        - **do_abort** -- determines whether to call Error::one() or Error::all()

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   1 if string resolves to "true", otherwise 0
:::

------------------------------------------------------------------------

::: {#string-processing .section}
## [[4.15.3. ]{.section-number}String processing](#id13){.toc-backref role="doc-backlink"}[](#string-processing "Link to this heading"){.headerlink}

The following are functions to help with processing strings and parsing files or arguments.

------------------------------------------------------------------------

[]{#_CPPv3N9LAMMPS_NS5utils6strdupERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils6strdupERKNSt6stringE}[]{#LAMMPS_NS::utils::strdup__ssCR}[]{#utils_8h_1a2a9f5a378d6155ae527b04b419fbd3e5 .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[strdup]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils6strdupERKNSt6stringE "Link to this definition"){.headerlink}\

:   Make C-style copy of string in new storage

    This allocates a storage buffer and copies the C-style or C++ style string into it. The buffer is allocated with "new" and thus needs to be deallocated with "delete\[\]".

    Parameters[:]{.colon}

    :   **text** -- string that should be copied

    Returns[:]{.colon}

    :   new buffer with copy of string

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils9lowercaseERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils9lowercaseERKNSt6stringE}[]{#LAMMPS_NS::utils::lowercase__ssCR}[]{#utils_8h_1aa27f09f6c641f8b4c2de6903006d10a2 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[lowercase]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[line]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils9lowercaseERKNSt6stringE "Link to this definition"){.headerlink}\

:   Convert string to lowercase

    Parameters[:]{.colon}

    :   **line** -- string that should be converted

    Returns[:]{.colon}

    :   new string with all lowercase characters

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils9uppercaseERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils9uppercaseERKNSt6stringE}[]{#LAMMPS_NS::utils::uppercase__ssCR}[]{#utils_8h_1a985e66e0bdcd8f73d1ee6a477f9ddc2a .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[uppercase]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[line]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils9uppercaseERKNSt6stringE "Link to this definition"){.headerlink}\

:   Convert string to uppercase

    Parameters[:]{.colon}

    :   **line** -- string that should be converted

    Returns[:]{.colon}

    :   new string with all uppercase characters

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils4trimERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils4trimERKNSt6stringE}[]{#LAMMPS_NS::utils::trim__ssCR}[]{#utils_8h_1a2eaed9f7998793904b0953fe0d9bbf6a .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[trim]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[line]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils4trimERKNSt6stringE "Link to this definition"){.headerlink}\

:   Trim leading and trailing whitespace. Like TRIM() in Fortran.

    Parameters[:]{.colon}

    :   **line** -- string that should be trimmed

    Returns[:]{.colon}

    :   new string without whitespace (string)

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils12trim_commentERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils12trim_commentERKNSt6stringE}[]{#LAMMPS_NS::utils::trim_comment__ssCR}[]{#utils_8h_1ae197fb8181a875095b3dbc0f1e2cdf2d .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[trim_comment]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[line]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils12trim_commentERKNSt6stringE "Link to this definition"){.headerlink}\

:   Return string with anything from the first '#' character onward removed

    Parameters[:]{.colon}

    :   **line** -- string that should be trimmed

    Returns[:]{.colon}

    :   new string without comment (string)

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11strcompressERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils11strcompressERKNSt6stringE}[]{#LAMMPS_NS::utils::strcompress__ssCR}[]{#utils_8h_1a34484ff93c3066920e2a0efa97b91419 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[strcompress]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11strcompressERKNSt6stringE "Link to this definition"){.headerlink}\

:   Compress whitespace in a string

    ::: versionadded
    [Added in version 4Feb2025.]{.versionmodified .added}
    :::

    This function compresses whitespace in a string to just a single blank.

    Parameters[:]{.colon}

    :   **text** -- the text to be compressed

    Returns[:]{.colon}

    :   string with whitespace compressed to single blanks

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils18strip_style_suffixERKNSt6stringEP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils18strip_style_suffixERKNSt6stringEP6LAMMPS}[]{#LAMMPS_NS::utils::strip_style_suffix__ssCR.LAMMPSP}[]{#utils_8h_1ab59c3628bad8784f2df865818395686a .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[strip_style_suffix]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[style]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils18strip_style_suffixERKNSt6stringEP6LAMMPS "Link to this definition"){.headerlink}\

:   Remove style suffix from string if suffix flag is active

    This will try to undo the effect from using the [[suffix command]{.doc}]suffix.md){.reference .internal} or the *-suffix/-sf* command-line flag and return correspondingly modified string.

    Parameters[:]{.colon}

    :   - **style** -- string of style name

        - **lmp** -- pointer to the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class (has suffix_flag and suffix strings)

    Returns[:]{.colon}

    :   processed string

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils10star_substERKNSt6stringE6biginti}[]{#_CPPv2N9LAMMPS_NS5utils10star_substERKNSt6stringE6biginti}[]{#LAMMPS_NS::utils::star_subst__ssCR.bigint.i}[]{#utils_8h_1a36e52b4e7c0e6b89dded52d86413c11d .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[star_subst]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[bigint]{.pre}]{.n}[ ]{.w}[[step]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[pad]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils10star_substERKNSt6stringE6biginti "Link to this definition"){.headerlink}\

:   Replace first '\*' character in a string with a number, optionally zero-padded

    If there is no '*' character in the string, return the original string. If the number requires more characters than the value of the \*pad* argument, do not add zeros; otherwise add as many zeroes as needed to the left to make the the number representation *pad* characters wide.

    Parameters[:]{.colon}

    :   - **name** -- string with file containing a '\*' (or not)

        - **step** -- step number to replace the (first) '\*'

        - **pad** -- zero-padding (may be zero)

    Returns[:]{.colon}

    :   processed string

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8has_utf8ERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils8has_utf8ERKNSt6stringE}[]{#LAMMPS_NS::utils::has_utf8__ssCR}[]{#utils_8h_1aead94e616bd78c82ac237765d713b25a .target}[[inline]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[has_utf8]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[line]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8has_utf8ERKNSt6stringE "Link to this definition"){.headerlink}\

:   Check if a string will likely have UTF-8 encoded characters

    UTF-8 uses the 7-bit standard ASCII table for the first 127 characters and all other characters are encoded as multiple bytes. For the multi-byte characters the first byte has either the highest two, three, or four bits set followed by a zero bit and followed by one, two, or three more bytes, respectively, where the highest bit is set and the second highest bit set to 0. The remaining bits combined are the character code, which is thus limited to 21-bits.

    For the sake of efficiency this test only checks if a character in the string has the highest bit set and thus is very likely an UTF-8 character. It will not be able to tell this this is a valid UTF-8 character or whether it is a 2-byte, 3-byte, or 4-byte character.

    *See also*

    :   [[`utils::utf8_subst()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils10utf8_substERKNSt6stringE "LAMMPS_NS::utils::utf8_subst"){.reference .internal}

    Parameters[:]{.colon}

    :   **line** -- string that should be checked

    Returns[:]{.colon}

    :   true if string contains UTF-8 encoded characters (bool)

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils10utf8_substERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils10utf8_substERKNSt6stringE}[]{#LAMMPS_NS::utils::utf8_subst__ssCR}[]{#utils_8h_1a6ab67644ed865096c60e1fd456a52bd4 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[utf8_subst]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[line]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils10utf8_substERKNSt6stringE "Link to this definition"){.headerlink}\

:   Replace known UTF-8 characters with ASCII equivalents

    *See also*

    :   [[`utils::has_utf8()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils8has_utf8ERKNSt6stringE "LAMMPS_NS::utils::has_utf8"){.reference .internal}

    Parameters[:]{.colon}

    :   **line** -- string that should be converted

    Returns[:]{.colon}

    :   new string with ascii replacements (string)

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11count_wordsEPKc}[]{#_CPPv2N9LAMMPS_NS5utils11count_wordsEPKc}[]{#LAMMPS_NS::utils::count_words__cCP}[]{#utils_8h_1a8cda2fde7eb5a65ed3f071ed17f42054 .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[count_words]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11count_wordsEPKc "Link to this definition"){.headerlink}\

:   Count words in C-string, ignore any whitespace matching " \\t\\r\\n\\f"

    Parameters[:]{.colon}

    :   **text** -- string that should be searched

    Returns[:]{.colon}

    :   number of words found

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11count_wordsERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils11count_wordsERKNSt6stringE}[]{#LAMMPS_NS::utils::count_words__ssCR}[]{#utils_8h_1ab469ccad212a812ee2f67727307509ee .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[count_words]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11count_wordsERKNSt6stringE "Link to this definition"){.headerlink}\

:   Count words in string, ignore any whitespace matching " \\t\\r\\n\\f"

    Parameters[:]{.colon}

    :   **text** -- string that should be searched

    Returns[:]{.colon}

    :   number of words found

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11count_wordsERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils11count_wordsERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::utils::count_words__ssCR.ssCR}[]{#utils_8h_1a31175af2f2305fea6e26a2f780e0a491 .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[count_words]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[separators]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11count_wordsERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

:   Count words in string with custom choice of separating characters

    Parameters[:]{.colon}

    :   - **text** -- string that should be searched

        - **separators** -- string containing characters that will be treated as whitespace

    Returns[:]{.colon}

    :   number of words found

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils20trim_and_count_wordsERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils20trim_and_count_wordsERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::utils::trim_and_count_words__ssCR.ssCR}[]{#utils_8h_1af92e41728a60e9d949fa37e68f132178 .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[trim_and_count_words]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[separators]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"]{.pre} [\\t\\r\\n\\f\"]{.pre}]{.s}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils20trim_and_count_wordsERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

:   Count words in a single line, trim anything from '#' onward

    Parameters[:]{.colon}

    :   - **text** -- string that should be trimmed and searched

        - **separators** -- string containing characters that will be treated as whitespace

    Returns[:]{.colon}

    :   number of words found

<!-- -->

[]{#_CPPv3I0EN9LAMMPS_NS5utils4joinERKNSt6vectorI1TEERKNSt6stringE}[]{#_CPPv2I0EN9LAMMPS_NS5utils4joinERKNSt6vectorI1TEERKNSt6stringE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#utils_8h_1aca962c33d759959412d39b1fe48bd334 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[join]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0EN9LAMMPS_NS5utils4joinENSt6stringERKNSt6vectorI1TEERKNSt6stringE "LAMMPS_NS::utils::join::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[values]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[sep]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4I0EN9LAMMPS_NS5utils4joinENSt6stringERKNSt6vectorI1TEERKNSt6stringE "Link to this definition"){.headerlink}\

:   Take list of values and join them with a given separator text.

    This is the inverse operation of what the Tokenizer classes do. This is a generalization of the join_words() function and similar to fmt::join() but only supports the vector STL container, and to use the begin/end iterator version you have to use: [`utils::join(std::vector(x.begin(),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`x.end()),`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`sep);`{.docutils .literal .notranslate}]{.pre}. This approach can also be used to support other STL containers.

    Parameters[:]{.colon}

    :   - **values** -- STL vector with values

        - **sep** -- separator string (may be empty)

    Returns[:]{.colon}

    :   string with the concatenated values and separators

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils10join_wordsERKNSt6vectorINSt6stringEEERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils10join_wordsERKNSt6vectorINSt6stringEEERKNSt6stringE}[]{#LAMMPS_NS::utils::join_words__std::vector:ss:CR.ssCR}[]{#utils_8h_1a52b303c232166990f27299fb49b19ccb .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[join_words]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[words]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[sep]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils10join_wordsERKNSt6vectorINSt6stringEEERKNSt6stringE "Link to this definition"){.headerlink}\

:   Take list of words and join them with a given separator text.

    This is the inverse operation of what the split_words() function and Tokenizer classes do.

    Parameters[:]{.colon}

    :   - **words** -- STL vector with strings

        - **sep** -- separator string (may be empty)

    Returns[:]{.colon}

    :   string with the concatenated words and separators

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11split_wordsERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils11split_wordsERKNSt6stringE}[]{#LAMMPS_NS::utils::split_words__ssCR}[]{#utils_8h_1ac6b258d9949ba630b8383fa857f9bbb9 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[split_words]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11split_wordsERKNSt6stringE "Link to this definition"){.headerlink}\

:   Take text and split into non-whitespace words.

    This can handle strings with single and double quotes, escaped quotes, and escaped codes within quotes, but due to using an STL container and STL strings is rather slow because of making copies. Designed for parsing command-lines and similar text and not for time critical processing. Use a tokenizer class if performance matters.

    *See also*

    :   [[`Tokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS9TokenizerE "LAMMPS_NS::Tokenizer"){.reference .internal}, [[`ValueTokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS14ValueTokenizerE "LAMMPS_NS::ValueTokenizer"){.reference .internal}

    Parameters[:]{.colon}

    :   **text** -- string that should be split

    Returns[:]{.colon}

    :   STL vector with the words

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11split_linesERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils11split_linesERKNSt6stringE}[]{#LAMMPS_NS::utils::split_lines__ssCR}[]{#utils_8h_1aa1a7c146c8809600ba053e45c914e84e .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[split_lines]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11split_linesERKNSt6stringE "Link to this definition"){.headerlink}\

:   Take multi-line text and split into lines

    Parameters[:]{.colon}

    :   **text** -- string that should be split

    Returns[:]{.colon}

    :   STL vector with the lines

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils7strsameERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils7strsameERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::utils::strsame__ssCR.ssCR}[]{#utils_8h_1a9a77762d9fa650ae84fe26ac84a9b894 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[strsame]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text1]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text2]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils7strsameERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

:   Compare two string while ignoring whitespace

    ::: versionadded
    [Added in version 4Feb2025.]{.versionmodified .added}
    :::

    This function compares two strings while skipping over any kind of whitespace (blank, tab, newline, carriage return, etc.).

    Parameters[:]{.colon}

    :   - **text1** -- the first text to be compared

        - **text2** -- the second text to be compared

    Returns[:]{.colon}

    :   true if the non-whitespace part of the two strings matches, false if not

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8strmatchERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils8strmatchERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::utils::strmatch__ssCR.ssCR}[]{#utils_8h_1a3a2003eb8f17075d799ecf645e4f2c30 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[strmatch]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[pattern]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8strmatchERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

:   Match text against a simplified regex pattern

    More flexible and specific matching of a string against a pattern. This function is supposed to be a more safe, more specific and simple to use API to find pattern matches. The purpose is to replace uses of either strncmp() or strstr() in the code base to find sub-strings safely. With strncmp() finding prefixes, the number of characters to match must be counted, which can lead to errors, while using "\^pattern" will do the same with less problems. Matching for suffixes using strstr() is not as specific as 'pattern\$', and complex matches, e.g. "\^rigid.\*\\/small.\*", to match all small body optimized rigid fixes require only one test.

    The use of std::string arguments allows for simple concatenation even with char \* type variables. Example: utils::strmatch(text, std::string("\^") + charptr)

    Parameters[:]{.colon}

    :   - **text** -- the text to be matched against the pattern

        - **pattern** -- the search pattern, which may contain regexp markers

    Returns[:]{.colon}

    :   true if the pattern matches, false if not

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils7strfindERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils7strfindERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::utils::strfind__ssCR.ssCR}[]{#utils_8h_1a0fc913e925ac5ad63addfae419332e31 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[strfind]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[text]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[pattern]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils7strfindERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

:   Find sub-string that matches a simplified regex pattern

    This function is a companion function to utils::strmatch(). Arguments and logic is the same, but instead of a boolean, it returns the sub-string that matches the regex pattern. There can be only one match. This can be used as a more flexible alternative to strstr().

    Parameters[:]{.colon}

    :   - **text** -- the text to be matched against the pattern

        - **pattern** -- the search pattern, which may contain regexp markers

    Returns[:]{.colon}

    :   the string that matches the pattern or an empty one

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils10is_integerERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils10is_integerERKNSt6stringE}[]{#LAMMPS_NS::utils::is_integer__ssCR}[]{#utils_8h_1a66b3c703e53c70f60ba745a557cace67 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[is_integer]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils10is_integerERKNSt6stringE "Link to this definition"){.headerlink}\

:   Check if string can be converted to valid integer

    Parameters[:]{.colon}

    :   **str** -- string that should be checked

    Returns[:]{.colon}

    :   true, if string contains valid a integer, false otherwise

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils9is_doubleERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils9is_doubleERKNSt6stringE}[]{#LAMMPS_NS::utils::is_double__ssCR}[]{#utils_8h_1a3f130082bbb981e0253f32bc46c1b3b3 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[is_double]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils9is_doubleERKNSt6stringE "Link to this definition"){.headerlink}\

:   Check if string can be converted to valid floating-point number

    Parameters[:]{.colon}

    :   **str** -- string that should be checked

    Returns[:]{.colon}

    :   true, if string contains valid number, false otherwise

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils5is_idERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils5is_idERKNSt6stringE}[]{#LAMMPS_NS::utils::is_id__ssCR}[]{#utils_8h_1a8b19cdd3cde5fe93a7b5f87c3271e117 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[is_id]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils5is_idERKNSt6stringE "Link to this definition"){.headerlink}\

:   Check if string is a valid ID ID strings may contain only letters, numbers, and underscores.

    Parameters[:]{.colon}

    :   **str** -- string that should be checked

    Returns[:]{.colon}

    :   true, if string contains valid id, false otherwise

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils7is_typeERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils7is_typeERKNSt6stringE}[]{#LAMMPS_NS::utils::is_type__ssCR}[]{#utils_8h_1adf45c3878dd1d69dc6a14887244b5f36 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[is_type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils7is_typeERKNSt6stringE "Link to this definition"){.headerlink}\

:   Check if string is a valid type label, or numeric type, or numeric type range. Numeric type or type range may only contain digits or the '*' character. Type label strings may not contain a digit, or a '*', or a '#' character as the first character to distinguish them from comments and numeric types or type ranges. They also may not contain any whitespace. If the string is a valid numeric type or type range the function returns 0, if it is a valid type label the function returns 1, otherwise it returns -1.

    Parameters[:]{.colon}

    :   **str** -- string that should be checked

    Returns[:]{.colon}

    :   0, 1, or -1, depending on whether the string is valid numeric type, valid type label or neither, respectively
:::

------------------------------------------------------------------------

::: {#potential-file-functions .section}
## [[4.15.4. ]{.section-number}Potential file functions](#id14){.toc-backref role="doc-backlink"}[](#potential-file-functions "Link to this heading"){.headerlink}

[]{#_CPPv3N9LAMMPS_NS5utils23get_potential_file_pathERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils23get_potential_file_pathERKNSt6stringE}[]{#LAMMPS_NS::utils::get_potential_file_path__ssCR}[]{#utils_8h_1a54601c14224556c45ed863cb95e8d49c .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[get_potential_file_path]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils23get_potential_file_pathERKNSt6stringE "Link to this definition"){.headerlink}\

:   Determine full path of potential file. If file is not found in current directory, search directories listed in LAMMPS_POTENTIALS environment variable

    Parameters[:]{.colon}

    :   **path** -- file path

    Returns[:]{.colon}

    :   full path to potential file

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils18get_potential_dateERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils18get_potential_dateERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::utils::get_potential_date__ssCR.ssCR}[]{#utils_8h_1a86fd64c9c2c2183daada07c001e91392 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[get_potential_date]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[potential_name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils18get_potential_dateERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

:   Read potential file and return DATE field if it is present

    Parameters[:]{.colon}

    :   - **path** -- file path

        - **potential_name** -- name of potential that is being read

    Returns[:]{.colon}

    :   DATE field if present

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils19get_potential_unitsERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils19get_potential_unitsERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::utils::get_potential_units__ssCR.ssCR}[]{#utils_8h_1ab8b096aefd75e4cef0162f113b800c2e .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[get_potential_units]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[potential_name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils19get_potential_unitsERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

:   Read potential file and return UNITS field if it is present

    Parameters[:]{.colon}

    :   - **path** -- file path

        - **potential_name** -- name of potential that is being read

    Returns[:]{.colon}

    :   UNITS field if present

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils25get_supported_conversionsEKi}[]{#_CPPv2N9LAMMPS_NS5utils25get_supported_conversionsEKi}[]{#LAMMPS_NS::utils::get_supported_conversions__iC}[]{#utils_8h_1a4d70c1d4e44dad6d82bb7fb643adb095 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[get_supported_conversions]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[property]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils25get_supported_conversionsEKi "Link to this definition"){.headerlink}\

:   Return bitmask of available conversion factors for a given property

    Parameters[:]{.colon}

    :   **property** -- property to be converted

    Returns[:]{.colon}

    :   bitmask indicating available conversions

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils21get_conversion_factorEKiKi}[]{#_CPPv2N9LAMMPS_NS5utils21get_conversion_factorEKiKi}[]{#LAMMPS_NS::utils::get_conversion_factor__iC.iC}[]{#utils_8h_1ae069d34c47dc4eeb168de963e592f5ed .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[get_conversion_factor]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[property]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[conversion]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils21get_conversion_factorEKiKi "Link to this definition"){.headerlink}\

:   Return unit conversion factor for given property and selected from/to units

    Parameters[:]{.colon}

    :   - **property** -- property to be converted

        - **conversion** -- constant indicating the conversion

    Returns[:]{.colon}

    :   conversion factor

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils14open_potentialERKNSt6stringEP6LAMMPSPi}[]{#_CPPv2N9LAMMPS_NS5utils14open_potentialERKNSt6stringEP6LAMMPSPi}[]{#LAMMPS_NS::utils::open_potential__ssCR.LAMMPSP.iP}[]{#utils_8h_1a1b92528e9bbdff202464fded75539b84 .target}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[open_potential]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[auto_convert]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils14open_potentialERKNSt6stringEP6LAMMPSPi "Link to this definition"){.headerlink}\

:   Open a potential file as specified by *name*

    If opening the file directly fails, the function will search for it in the list of folder pointed to by the environment variable [`LAMMPS_POTENTIALS`{.docutils .literal .notranslate}]{.pre} (if it is set).

    If the potential file has a [`UNITS`{.docutils .literal .notranslate}]{.pre} tag in the first line, the tag's value is compared to the current unit style setting. The behavior of the function then depends on the value of the *auto_convert* parameter. If it is a null pointer, then the unit values must match or else the open will fail with an error. Otherwise the bitmask that *auto_convert* points to is used check for compatibility with possible automatic conversions by the calling function. If compatible, the bitmask is set to the required conversion or [`utils::NOCONVERT`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **name** -- file- or pathname of the potential file

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

        - **auto_convert** -- pointer to unit conversion bitmask or [`nullptr`{.docutils .literal .notranslate}]{.pre}

    Returns[:]{.colon}

    :   FILE pointer of the opened potential file or [`nullptr`{.docutils .literal .notranslate}]{.pre}
:::

------------------------------------------------------------------------

::: {#argument-processing .section}
## [[4.15.5. ]{.section-number}Argument processing](#id15){.toc-backref role="doc-backlink"}[](#argument-processing "Link to this heading"){.headerlink}

[]{#_CPPv3I0EN9LAMMPS_NS5utils6boundsEPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP5Errori}[]{#_CPPv2I0EN9LAMMPS_NS5utils6boundsEPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP5Errori}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[TYPE]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#utils_8h_1a9f3c61c3ed2de5d6dde5cd07e9b07610 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[bounds]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bigint]{.pre}]{.n}[ ]{.w}[[nmin]{.pre}]{.n .sig-param}, [[bigint]{.pre}]{.n}[ ]{.w}[[nmax]{.pre}]{.n .sig-param}, [[[TYPE]{.pre}]{.n}](#_CPPv4I0EN9LAMMPS_NS5utils6boundsEvPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP5Errori "LAMMPS_NS::utils::bounds::TYPE"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[nlo]{.pre}]{.n .sig-param}, [[[TYPE]{.pre}]{.n}](#_CPPv4I0EN9LAMMPS_NS5utils6boundsEvPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP5Errori "LAMMPS_NS::utils::bounds::TYPE"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[nhi]{.pre}]{.n .sig-param}, [[Error]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[error]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[failed]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[-]{.pre}]{.o}[[2]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN9LAMMPS_NS5utils6boundsEvPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP5Errori "Link to this definition"){.headerlink}\

:   Compute index bounds derived from a string with a possible wildcard

    This functions processes the string in *str* and set the values of *nlo* and *nhi* according to the following five cases:

    - a single number, i: nlo = i; nhi = i;

    - a single asterisk, \*: nlo = nmin; nhi = nmax;

    - a single number followed by an asterisk, i\*: nlo = i; nhi = nmax;

    - a single asterisk followed by a number, \*i: nlo = nmin; nhi = i;

    - two numbers with an asterisk in between. i\*j: nlo = i; nhi = j;

    Template Parameters[:]{.colon}

    :   **TYPE** -- the type of the index that is subject to the wildcard expansion

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be processed

        - **nmin** -- smallest possible lower bound

        - **nmax** -- largest allowed upper bound

        - **nlo** -- **\[out\]** lower bound

        - **nhi** -- **\[out\]** upper bound

        - **error** -- pointer to Error class for out-of-bounds messages

        - **failed** -- argument index with failed expansion (optional)

<!-- -->

[]{#_CPPv3I0EN9LAMMPS_NS5utils16bounds_typelabelEPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP6LAMMPSi}[]{#_CPPv2I0EN9LAMMPS_NS5utils16bounds_typelabelEPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP6LAMMPSi}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[TYPE]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#utils_8h_1a0591b9a07cdbb8d72183972157e7ff02 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[bounds_typelabel]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[bigint]{.pre}]{.n}[ ]{.w}[[nmin]{.pre}]{.n .sig-param}, [[bigint]{.pre}]{.n}[ ]{.w}[[nmax]{.pre}]{.n .sig-param}, [[[TYPE]{.pre}]{.n}](#_CPPv4I0EN9LAMMPS_NS5utils16bounds_typelabelEvPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP6LAMMPSi "LAMMPS_NS::utils::bounds_typelabel::TYPE"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[nlo]{.pre}]{.n .sig-param}, [[[TYPE]{.pre}]{.n}](#_CPPv4I0EN9LAMMPS_NS5utils16bounds_typelabelEvPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP6LAMMPSi "LAMMPS_NS::utils::bounds_typelabel::TYPE"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[nhi]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[mode]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4I0EN9LAMMPS_NS5utils16bounds_typelabelEvPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP6LAMMPSi "Link to this definition"){.headerlink}\

:   Same as utils::bounds(), but string may be a typelabel

    ::: versionadded
    [Added in version 27June2024.]{.versionmodified .added}
    :::

    This functions adds the following case to [[`utils::bounds()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4I0EN9LAMMPS_NS5utils6boundsEvPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP5Errori "LAMMPS_NS::utils::bounds"){.reference .internal}:

    > ::: {}
    > - a single type label, typestr: nlo = nhi = label2type(typestr)
    > :::

    Template Parameters[:]{.colon}

    :   **TYPE** -- the type of the index that is subject to the boundary expansion

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- string to be processed

        - **nmin** -- smallest possible lower bound

        - **nmax** -- largest allowed upper bound

        - **nlo** -- **\[out\]** lower bound

        - **nhi** -- **\[out\]** upper bound

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

        - **mode** -- select labelmap using constants from [[Atom]{.std .std-ref}]Classes_atom.md#classLAMMPS__NS_1_1Atom){.reference .internal} class

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11expand_argsEPKciiPPciRPPcP6LAMMPSPPi}[]{#_CPPv2N9LAMMPS_NS5utils11expand_argsEPKciiPPciRPPcP6LAMMPSPPi}[]{#LAMMPS_NS::utils::expand_args__cCP.i.i.cPP.i.cPPR.LAMMPSP.iPP}[]{#utils_8h_1a09d759410bb0cbe27833003d9f5a96cf .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[expand_args]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[narg]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[arg]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[&]{.pre}]{.p}[[earg]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[argmap]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11expand_argsEPKciiPPciRPPcP6LAMMPSPPi "Link to this definition"){.headerlink}\

:   Expand list of arguments when containing fix/compute wildcards

    This function searches the list of arguments in *arg* for strings of the kind c_ID\[\*\], f_ID\[\*\], v_ID\[\*\], i2_ID\[\*\], d2_ID\[\*\], or c_ID:gname:dname\[\*\] referring to computes, fixes, vector style variables, custom per-atom arrays, or grids, respectively. Any such strings are replaced by one or more strings with the '*' character replaced by the corresponding possible numbers as determined from the fix, compute, variable, property, or grid instance. Unrecognized strings are just copied. If the \*mode* parameter is set to 0, expand global vectors, but not global arrays; if it is set to 1, expand global arrays (by column) but not global vectors.

    If any expansion happens, the earg list and all its strings are new allocations and must be freed explicitly by the caller. Otherwise arg and earg will point to the same address and no explicit de-allocation is needed by the caller.

    The *argmap* pointer to an int pointer may be used to accept an array of integers mapping the arguments after the expansion to their original index. If this pointer is NULL (the default) than this map is not created. Otherwise, it must be deallocated by the calling code.

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **narg** -- number of arguments in current list

        - **arg** -- argument list, possibly containing wildcards

        - **mode** -- select between global vectors(=0) and arrays (=1)

        - **earg** -- new argument list with wildcards expanded

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

        - **argmap** -- pointer to integer pointer for mapping expanded indices to input (optional)

    Returns[:]{.colon}

    :   number of arguments in expanded list

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils13parse_grid_idEPKciRKNSt6stringEP5Error}[]{#_CPPv2N9LAMMPS_NS5utils13parse_grid_idEPKciRKNSt6stringEP5Error}[]{#LAMMPS_NS::utils::parse_grid_id__cCP.i.ssCR.ErrorP}[]{#utils_8h_1a91407dd860f7f2a4fb3fb5c91911f6ca .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[parse_grid_id]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[Error]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[error]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils13parse_grid_idEPKciRKNSt6stringEP5Error "Link to this definition"){.headerlink}\

:   Parse grid reference into 3 sub-strings

    Format of grid ID reference = id:gname:dname. Return vector with the 3 sub-strings.

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **name** -- complete grid ID

        - **error** -- pointer to Error class

    Returns[:]{.colon}

    :   std::vector\<std::string\> containing the 3 sub-strings

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11expand_typeEPKciRKNSt6stringEiP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils11expand_typeEPKciRKNSt6stringEiP6LAMMPS}[]{#LAMMPS_NS::utils::expand_type__cCP.i.ssCR.i.LAMMPSP}[]{#utils_8h_1ac69ac30ade492d1a68c14ce5dd92d5bc .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[expand_type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11expand_typeEPKciRKNSt6stringEiP6LAMMPS "Link to this definition"){.headerlink}\

:   Expand type label string into its equivalent numeric type

    This function checks if a given string may be a type label and then searches the labelmap type indicated by the *mode* argument for the corresponding numeric type. If this is found, a copy of the numeric type string is made and returned. Otherwise a null pointer is returned. If a string is returned, the calling code must free it with delete\[\].

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **str** -- type string to be expanded

        - **mode** -- select labelmap using constants from [[Atom]{.std .std-ref}]Classes_atom.md#classLAMMPS__NS_1_1Atom){.reference .internal} class

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   pointer to expanded string or null pointer
:::

------------------------------------------------------------------------

::: {#convenience-functions .section}
## [[4.15.6. ]{.section-number}Convenience functions](#id16){.toc-backref role="doc-backlink"}[](#convenience-functions "Link to this heading"){.headerlink}

[]{#_CPPv3IDpEN9LAMMPS_NS5utils7logmesgEP6LAMMPSRKNSt6stringEDpRR4Args}[]{#_CPPv2IDpEN9LAMMPS_NS5utils7logmesgEP6LAMMPSRKNSt6stringEDpRR4Args}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[\...]{.pre}]{.p}[[[Args]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#utils_8h_1a9d7d7115e97f2cfac88564c450ee0cfb .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[logmesg]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[format]{.pre}]{.n .sig-param}, [[[Args]{.pre}]{.n}](#_CPPv4IDpEN9LAMMPS_NS5utils7logmesgEvP6LAMMPSRKNSt6stringEDpRR4Args "LAMMPS_NS::utils::logmesg::Args"){.reference .internal}[[&]{.pre}]{.p}[[&]{.pre}]{.p}[[\...]{.pre}]{.p}[ ]{.w}[[args]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4IDpEN9LAMMPS_NS5utils7logmesgEvP6LAMMPSRKNSt6stringEDpRR4Args "Link to this definition"){.headerlink}\

:   Send formatted message to screen and logfile, if available

    This function simplifies the repetitive task of outputting some message to both the screen and/or the log file. The template wrapper with {fmt} formatting and argument processing allows this function to work similar to :cpp:func:[`utils::print()`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`<LAMMPS_NS::utils::print>`{.docutils .literal .notranslate}]{.pre}.

    Parameters[:]{.colon}

    :   - **lmp** -- pointer to [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

        - **format** -- format string of message to be printed

        - **args** -- arguments to format string

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils7logmesgEP6LAMMPSRKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils7logmesgEP6LAMMPSRKNSt6stringE}[]{#LAMMPS_NS::utils::logmesg__LAMMPSP.ssCR}[]{#utils_8h_1a0b5a7272e51011310cc877ba444f9ac7 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[logmesg]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[mesg]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils7logmesgEP6LAMMPSRKNSt6stringE "Link to this definition"){.headerlink}\

:   This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

    Parameters[:]{.colon}

    :   - **lmp** -- pointer to [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

        - **mesg** -- string with message to be printed

<!-- -->

[]{#_CPPv3IDpEN9LAMMPS_NS5utils5printEP4FILERKNSt6stringEDpRR4Args}[]{#_CPPv2IDpEN9LAMMPS_NS5utils5printEP4FILERKNSt6stringEDpRR4Args}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[\...]{.pre}]{.p}[[[Args]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#utils_8h_1abacca1de1e36ee6716022dd58b8a3ab6 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[print]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[format]{.pre}]{.n .sig-param}, [[[Args]{.pre}]{.n}](#_CPPv4IDpEN9LAMMPS_NS5utils5printEvP4FILERKNSt6stringEDpRR4Args "LAMMPS_NS::utils::print::Args"){.reference .internal}[[&]{.pre}]{.p}[[&]{.pre}]{.p}[[\...]{.pre}]{.p}[ ]{.w}[[args]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4IDpEN9LAMMPS_NS5utils5printEvP4FILERKNSt6stringEDpRR4Args "Link to this definition"){.headerlink}\

:   Write formatted message to file

    ::: versionadded
    [Added in version 4Feb2025.]{.versionmodified .added}
    :::

    This function implements a version of (f)printf() that uses {fmt} formatting

    Parameters[:]{.colon}

    :   - **fp** -- stdio FILE pointer

        - **format** -- format string of message to be printed

        - **args** -- arguments to format string

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils5printEP4FILERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils5printEP4FILERKNSt6stringE}[]{#LAMMPS_NS::utils::print__FILEP.ssCR}[]{#utils_8h_1a30621d328f1f944bb9de67bbb5dd6072 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[print]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[mesg]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils5printEP4FILERKNSt6stringE "Link to this definition"){.headerlink}\

:   This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

    Print string message without format

    Parameters[:]{.colon}

    :   - **fp** -- stdio FILE pointer

        - **mesg** -- string with message to be printed

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8errorurlEi}[]{#_CPPv2N9LAMMPS_NS5utils8errorurlEi}[]{#LAMMPS_NS::utils::errorurl__i}[]{#utils_8h_1a0042d23b4761c1937f4cfebee627cada .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[errorurl]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[errorcode]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8errorurlEi "Link to this definition"){.headerlink}\

:   Return text redirecting the user to a specific paragraph in the manual

    The [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} manual contains detailed explanations for errors and warnings where a simple error message may not be sufficient. These can be reached through URLs with a numeric code \> 0. This function creates the corresponding text to be included into the error message that redirects the user to that URL. Using an error code of 0 returns a message pointing to a URL discussing error messages in general.

    Parameters[:]{.colon}

    :   **errorcode** -- non-negative number pointing to a paragraph in the manual

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils16missing_cmd_argsERKNSt6stringEiRKNSt6stringEP5Error}[]{#_CPPv2N9LAMMPS_NS5utils16missing_cmd_argsERKNSt6stringEiRKNSt6stringEP5Error}[]{#LAMMPS_NS::utils::missing_cmd_args__ssCR.i.ssCR.ErrorP}[]{#utils_8h_1a9ebdf3470338d3fddf4d0462b440bb8b .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[missing_cmd_args]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[line]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[cmd]{.pre}]{.n .sig-param}, [[Error]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[error]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils16missing_cmd_argsERKNSt6stringEiRKNSt6stringEP5Error "Link to this definition"){.headerlink}\

:   Print error message about missing arguments for command

    This function simplifies the repetitive reporting missing arguments to a command.

    Parameters[:]{.colon}

    :   - **file** -- name of source file for error message

        - **line** -- line number in source file for error message

        - **cmd** -- name of the failing command

        - **error** -- pointer to Error class instance (for abort) or nullptr

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils14point_to_errorEP5Inputi}[]{#_CPPv2N9LAMMPS_NS5utils14point_to_errorEP5Inputi}[]{#LAMMPS_NS::utils::point_to_error__InputP.i}[]{#utils_8h_1af2c1ac9dd9cde63ac99cf7f5a1a4aef2 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[point_to_error]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Input]{.pre}]{.n}]Classes_input.md#_CPPv4N9LAMMPS_NS5InputE "LAMMPS_NS::Input"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[input]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[failed]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils14point_to_errorEP5Inputi "Link to this definition"){.headerlink}\

:   Create string with last command and optionally pointing to arg with error

    ::: versionadded
    [Added in version 4Feb2025.]{.versionmodified .added}
    :::

    This function is a helper function for error messages. It creates extra output in error messages. It will produce either two or three lines: the original last input line *before* variable substitutions, the corresponding pre-processed command (only when different) and one or more '\^' characters pointing to the faulty argument as indicated by the *failed* argument. Any whitespace in the lines with the command output are compressed to a single blank by calling [[`strcompress()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils11strcompressERKNSt6stringE "LAMMPS_NS::utils::strcompress"){.reference .internal}

    Parameters[:]{.colon}

    :   - **input** -- pointer to the [[Input]{.std .std-ref}]Classes_input.md#classLAMMPS__NS_1_1Input){.reference .internal} class instance (for access to last command args)

        - **failed** -- index of the faulty argument (-1 to point to the command itself)

    Returns[:]{.colon}

    :   string with two or three lines to follow error messages

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils13flush_buffersEP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils13flush_buffersEP6LAMMPS}[]{#LAMMPS_NS::utils::flush_buffers__LAMMPSP}[]{#utils_8h_1a1721a8d265f9cde71f2c20ac1ba581e5 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[flush_buffers]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils13flush_buffersEP6LAMMPS "Link to this definition"){.headerlink}\

:   Flush output buffers

    This function calls fflush() on screen and logfile FILE pointers if available and thus tells the operating system to output all currently buffered data. This is local operation and independent from buffering by a file system or an MPI library.

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils11getsyserrorEv}[]{#_CPPv2N9LAMMPS_NS5utils11getsyserrorEv}[]{#LAMMPS_NS::utils::getsyserror}[]{#utils_8h_1a59872d3df515856d461cc81f8de6777e .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[getsyserror]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils11getsyserrorEv "Link to this definition"){.headerlink}\

:   Return a string representing the current system error status

    This is a wrapper around calling strerror(errno).

    Returns[:]{.colon}

    :   error string

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils24check_packages_for_styleERKNSt6stringERKNSt6stringEP6LAMMPS}[]{#_CPPv2N9LAMMPS_NS5utils24check_packages_for_styleERKNSt6stringERKNSt6stringEP6LAMMPS}[]{#LAMMPS_NS::utils::check_packages_for_style__ssCR.ssCR.LAMMPSP}[]{#utils_8h_1a7958600997ce9aecc9c589d6a340b93b .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[check_packages_for_style]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[style]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils24check_packages_for_styleERKNSt6stringERKNSt6stringEP6LAMMPS "Link to this definition"){.headerlink}\

:   Report if a requested style is in a package or may have a typo

    Parameters[:]{.colon}

    :   - **style** -- type of style that is to be checked for

        - **name** -- name of style that was not found

        - **lmp** -- pointer to top-level [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} class instance

    Returns[:]{.colon}

    :   string usable for error messages

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils16timespec2secondsERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils16timespec2secondsERKNSt6stringE}[]{#LAMMPS_NS::utils::timespec2seconds__ssCR}[]{#utils_8h_1afd22548fe9c6d4570ffcde59947a1764 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[timespec2seconds]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[timespec]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils16timespec2secondsERKNSt6stringE "Link to this definition"){.headerlink}\

:   Convert a time string to seconds

    The strings "off" and "unlimited" result in -1

    Parameters[:]{.colon}

    :   **timespec** -- a string in the following format: (\[\[HH:\]MM:\]SS)

    Returns[:]{.colon}

    :   total in seconds

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils8date2numERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS5utils8date2numERKNSt6stringE}[]{#LAMMPS_NS::utils::date2num__ssCR}[]{#utils_8h_1af07ce9a5537cbc035845686e894f3491 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[date2num]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[date]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils8date2numERKNSt6stringE "Link to this definition"){.headerlink}\

:   Convert a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} version date to a number

    This will generate a number YYYYMMDD from a date string (with or without blanks) that is suitable for numerical comparisons, i.e. later dates will generate a larger number.

    The day may or may not have a leading zero, the month is identified by the first 3 letters (so there may be more) and the year may be 2 or 4 digits (the missing 2 digits will be assumed as 20. That is 04 corresponds to 2004).

    No check is made whether the date is valid.

    Parameters[:]{.colon}

    :   **date** -- string in the format (Day Month Year)

    Returns[:]{.colon}

    :   date code

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils12current_dateEv}[]{#_CPPv2N9LAMMPS_NS5utils12current_dateEv}[]{#LAMMPS_NS::utils::current_date}[]{#utils_8h_1a7a7a3c2717c15c16a93621e9e7d0f288 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[current_date]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils12current_dateEv "Link to this definition"){.headerlink}\

:   Return current date as string

    This will generate a string containing the current date in YYYY-MM-DD format.

    Returns[:]{.colon}

    :   string with current date
:::

------------------------------------------------------------------------

::: {#customized-standard-functions .section}
## [[4.15.7. ]{.section-number}Customized standard functions](#id17){.toc-backref role="doc-backlink"}[](#customized-standard-functions "Link to this heading"){.headerlink}

[]{#_CPPv3N9LAMMPS_NS5utils13binary_searchEKdKiPKd}[]{#_CPPv2N9LAMMPS_NS5utils13binary_searchEKdKiPKd}[]{#LAMMPS_NS::utils::binary_search__doubleC.iC.doubleCP}[]{#utils_8h_1a57ddd765821bb497c07a157b66725a01 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[binary_search]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[needle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[haystack]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils13binary_searchEKdKiPKd "Link to this definition"){.headerlink}\

:   Binary search in a vector of ascending doubles of length N

    If the value is smaller than the smallest value in the vector, 0 is returned. If the value is larger or equal than the largest value in the vector, N-1 is returned. Otherwise the index that satisfies the condition

    haystack\[index\] \<= value \< haystack\[index+1\]

    is returned, i.e. a value from 1 to N-2. Note that if there are tied values in the haystack, always the larger index is returned as only that satisfied the condition.

    Parameters[:]{.colon}

    :   - **needle** -- search value for which are are looking for the closest index

        - **n** -- size of the haystack array

        - **haystack** -- array with data in ascending order.

    Returns[:]{.colon}

    :   index of value in the haystack array smaller or equal to needle

<!-- -->

[]{#_CPPv3N9LAMMPS_NS5utils10merge_sortEPiiPvPFiiiPvE}[]{#_CPPv2N9LAMMPS_NS5utils10merge_sortEPiiPvPFiiiPvE}[]{#utils_8h_1af677fa53e7e5713dfb0fa6d6c3c6f81e .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[utils]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[merge_sort]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[index]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[num]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ptr]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[(]{.pre}]{.p}[[\*]{.pre}]{.p}[[comp]{.pre}]{.n .sig-param}[[)]{.pre}]{.p}[[(]{.pre}]{.p}[[int]{.pre}]{.kt}[[,]{.pre}]{.p}[ ]{.w}[[int]{.pre}]{.kt}[[,]{.pre}]{.p}[ ]{.w}[[void]{.pre}]{.kt}[[\*]{.pre}]{.p}[[)]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS5utils10merge_sortEPiiPvPFiiiPvE "Link to this definition"){.headerlink}\

:   Custom merge sort implementation

    This function provides a custom upward hybrid merge sort implementation with support to pass an opaque pointer to the comparison function, e.g. for access to class members. This avoids having to use global variables. For improved performance, it uses an in-place insertion sort on initial chunks of up to 64 elements and switches to merge sort from then on.

    Parameters[:]{.colon}

    :   - **index** -- Array with indices to be sorted

        - **num** -- Length of the index array

        - **ptr** -- Pointer to opaque object passed to comparison function

        - **comp** -- Pointer to comparison function
:::
::::::::::

------------------------------------------------------------------------

::: {#special-math-functions .section}
# [4.16. ]{.section-number}Special Math functions[](#special-math-functions "Link to this heading"){.headerlink}

The [`MathSpecial`{.docutils .literal .notranslate}]{.pre} namespace implements a selection of custom and optimized mathematical functions for a variety of applications.

[]{#_CPPv3N9LAMMPS_NS11MathSpecial9factorialEKi}[]{#_CPPv2N9LAMMPS_NS11MathSpecial9factorialEKi}[]{#LAMMPS_NS::MathSpecial::factorial__iC}[]{#math__special_8h_1a9a6be409a4fa9407a40b40ab6d226a8f .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[factorial]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial9factorialEKi "Link to this definition"){.headerlink}\

:   Fast tabulated factorial function

    This function looks up pre-computed factorial values for arguments of n = 0 to a maximum of 167, which is the maximal value representable by a double precision floating point number. For other values of n a NaN value is returned.

    Parameters[:]{.colon}

    :   **n** -- argument (valid: 0 \<= n \<= 167)

    Returns[:]{.colon}

    :   value of n! as double precision number or NaN

<!-- -->

[]{#_CPPv3N9LAMMPS_NS11MathSpecial8exp2_x86Ed}[]{#_CPPv2N9LAMMPS_NS11MathSpecial8exp2_x86Ed}[]{#LAMMPS_NS::MathSpecial::exp2_x86__double}[]{#math__special_8h_1a46561242143bc684f0307a2260686505 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[exp2_x86]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[double]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial8exp2_x86Ed "Link to this definition"){.headerlink}\

:   Fast implementation of 2\^x without argument checks for little endian CPUs

    This function implements an optimized version of pow(2.0, x) that does not check for valid arguments and thus may only be used where arguments are well behaved. The implementation makes assumptions about the layout of double precision floating point numbers in memory and thus will only work on little endian CPUs. If little endian cannot be safely detected, the result of calling pow(2.0, x) will be returned. This function also is the basis for the fast exponential fm_exp(x).

    Parameters[:]{.colon}

    :   **x** -- argument

    Returns[:]{.colon}

    :   value of 2\^x as double precision number

<!-- -->

[]{#_CPPv3N9LAMMPS_NS11MathSpecial6fm_expEd}[]{#_CPPv2N9LAMMPS_NS11MathSpecial6fm_expEd}[]{#LAMMPS_NS::MathSpecial::fm_exp__double}[]{#math__special_8h_1a918af8d4a779a4da394bf9cc4a92d628 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[fm_exp]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[double]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial6fm_expEd "Link to this definition"){.headerlink}\

:   Fast implementation of exp(x) for little endian CPUs

    This function implements an optimized version of exp(x) for little endian CPUs. It calls the exp2_x86(x) function with a suitable prefactor to x to return exp(x). The implementation makes assumptions about the layout of double precision floating point numbers in memory and thus will only work on little endian CPUs. If little endian cannot be safely detected, the result of calling the exp(x) implementation in the standard math library will be returned.

    Parameters[:]{.colon}

    :   **x** -- argument

    Returns[:]{.colon}

    :   value of e\^x as double precision number

<!-- -->

[]{#_CPPv3N9LAMMPS_NS11MathSpecial8my_erfcxEKd}[]{#_CPPv2N9LAMMPS_NS11MathSpecial8my_erfcxEKd}[]{#LAMMPS_NS::MathSpecial::my_erfcx__doubleC}[]{#math__special_8h_1aef36df4bf24854a9f82627aae277d702 .target}[[static]{.pre}]{.k}[ ]{.w}[[inline]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[my_erfcx]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial8my_erfcxEKd "Link to this definition"){.headerlink}\

:   Fast scaled error function complement exp(x\*x)\*erfc(x) for coul/long styles

    This is a portable fast implementation of exp(x\*x)\*erfc(x) that can be used in coul/long pair styles as a replacement for the polynomial expansion that is/was widely used. Unlike the polynomial expansion, that is only accurate at the level of single precision floating point it provides full double precision accuracy, but at comparable speed (unlike the erfc() implementation shipped with GNU standard math library).

    Parameters[:]{.colon}

    :   **x** -- argument

    Returns[:]{.colon}

    :   value of e\^(x\*x)\*erfc(x)

<!-- -->

[]{#_CPPv3N9LAMMPS_NS11MathSpecial6expmsqEd}[]{#_CPPv2N9LAMMPS_NS11MathSpecial6expmsqEd}[]{#LAMMPS_NS::MathSpecial::expmsq__double}[]{#math__special_8h_1a7fd2fe6bf8bd6aa18c1bf3f9d8f94db2 .target}[[static]{.pre}]{.k}[ ]{.w}[[inline]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[expmsq]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[double]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial6expmsqEd "Link to this definition"){.headerlink}\

:   Fast implementation of exp(-x\*x) for little endian CPUs for coul/long styles

    This function implements an optimized version of exp(-x\*x) based on exp2_x86() for use with little endian CPUs. If little endian cannot be safely detected, the result of calling the exp(-x\*x) implementation in the standard math library will be returned.

    Parameters[:]{.colon}

    :   **x** -- argument

    Returns[:]{.colon}

    :   value of e\^(-x\*x) as double precision number

<!-- -->

[]{#_CPPv3N9LAMMPS_NS11MathSpecial6squareERKd}[]{#_CPPv2N9LAMMPS_NS11MathSpecial6squareERKd}[]{#LAMMPS_NS::MathSpecial::square__doubleCR}[]{#math__special_8h_1a4e74b26561c4b6337c1bcb5b0feb57c5 .target}[[static]{.pre}]{.k}[ ]{.w}[[inline]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[square]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[x]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial6squareERKd "Link to this definition"){.headerlink}\

:   Fast inline version of pow(x, 2.0)

    Parameters[:]{.colon}

    :   **x** -- argument

    Returns[:]{.colon}

    :   x\*x

<!-- -->

[]{#_CPPv3N9LAMMPS_NS11MathSpecial4cubeERKd}[]{#_CPPv2N9LAMMPS_NS11MathSpecial4cubeERKd}[]{#LAMMPS_NS::MathSpecial::cube__doubleCR}[]{#math__special_8h_1a68ee85149414b5e53c344e3e278fe0f3 .target}[[static]{.pre}]{.k}[ ]{.w}[[inline]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[cube]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[x]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial4cubeERKd "Link to this definition"){.headerlink}\

:   Fast inline version of pow(x, 3.0)

    Parameters[:]{.colon}

    :   **x** -- argument

    Returns[:]{.colon}

    :   x\*x

<!-- -->

[]{#_CPPv3N9LAMMPS_NS11MathSpecial7powsignEKi}[]{#_CPPv2N9LAMMPS_NS11MathSpecial7powsignEKi}[]{#LAMMPS_NS::MathSpecial::powsign__iC}[]{#math__special_8h_1a20919ed7744d1372c199251283472a27 .target}[[static]{.pre}]{.k}[ ]{.w}[[inline]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[powsign]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial7powsignEKi "Link to this definition"){.headerlink}\

:   

<!-- -->

[]{#_CPPv3N9LAMMPS_NS11MathSpecial6powintERKdKi}[]{#_CPPv2N9LAMMPS_NS11MathSpecial6powintERKdKi}[]{#LAMMPS_NS::MathSpecial::powint__doubleCR.iC}[]{#math__special_8h_1aef611f3adb458c7be6ce716bd8d61850 .target}[[static]{.pre}]{.k}[ ]{.w}[[inline]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[powint]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[x]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial6powintERKdKi "Link to this definition"){.headerlink}\

:   

<!-- -->

[]{#_CPPv3N9LAMMPS_NS11MathSpecial8powsinxxERKdi}[]{#_CPPv2N9LAMMPS_NS11MathSpecial8powsinxxERKdi}[]{#LAMMPS_NS::MathSpecial::powsinxx__doubleCR.i}[]{#math__special_8h_1a9601e990a97c44bed7862d2ea539d1c0 .target}[[static]{.pre}]{.k}[ ]{.w}[[inline]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[MathSpecial]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[powsinxx]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MathSpecial8powsinxxERKdi "Link to this definition"){.headerlink}\

:   
:::

------------------------------------------------------------------------

::::::::::::: {#tokenizer-classes .section}
# [4.17. ]{.section-number}Tokenizer classes[](#tokenizer-classes "Link to this heading"){.headerlink}

The purpose of the tokenizer classes is to simplify the recurring task of breaking lines of text down into words and/or numbers. Traditionally, LAMMPS code would be using the [`strtok()`{.docutils .literal .notranslate}]{.pre} function from the C library for that purpose, but that function has two significant disadvantages: 1) it cannot be used concurrently from different LAMMPS instances since it stores its status in a global variable and 2) it modifies the string that it is processing. These classes were implemented to avoid both of these issues and also to reduce the amount of code that needs to be written.

The basic procedure is to create an instance of the tokenizer class with the string to be processed as an argument and then do a loop until all available tokens are read. The constructor has a default set of separator characters, but that can be overridden. The default separators are all "whitespace" characters, i.e. the space character, the tabulator character, the carriage return character, the linefeed character, and the form feed character.

:::::: {#id4 .literal-block-wrapper .docutils .container}
::: code-block-caption
[Tokenizer class example listing entries of the PATH environment variable]{.caption-text}[](#id4 "Link to this code"){.headerlink}
:::

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "tokenizer.h"
    #include <cstdlib>
    #include <string>
    #include <iostream>

    using namespace LAMMPS_NS;

    int main(int, char **)
    {
        const char *path = getenv("PATH");

        if (path != nullptr) {
            Tokenizer p(path,":");
            while (p.has_next())
                std::cout << "Entry: " << p.next() << "\n";
        }
        return 0;
    }
:::
::::
::::::

Most tokenizer operations cannot fail except for [[`LAMMPS_NS::Tokenizer::next()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS9Tokenizer4nextEv "LAMMPS_NS::Tokenizer::next"){.reference .internal} (when used without first checking with [[`LAMMPS_NS::Tokenizer::has_next()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4NK9LAMMPS_NS9Tokenizer8has_nextEv "LAMMPS_NS::Tokenizer::has_next"){.reference .internal}) and [[`LAMMPS_NS::Tokenizer::skip()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS9Tokenizer4skipEi "LAMMPS_NS::Tokenizer::skip"){.reference .internal}. In case of failure, the class will throw an exception, so you may need to wrap the code using the tokenizer into a [`try`{.docutils .literal .notranslate}]{.pre} / [`catch`{.docutils .literal .notranslate}]{.pre} block to handle errors. The [[`LAMMPS_NS::ValueTokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS14ValueTokenizerE "LAMMPS_NS::ValueTokenizer"){.reference .internal} class may also throw an exception when a (type of) number is requested as next token that is not compatible with the string representing the next word.

:::::: {#id5 .literal-block-wrapper .docutils .container}
::: code-block-caption
[ValueTokenizer class example with exception handling]{.caption-text}[](#id5 "Link to this code"){.headerlink}
:::

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "tokenizer.h"
    #include <cstdlib>
    #include <string>
    #include <iostream>

    using namespace LAMMPS_NS;

    int main(int, char **)
    {
        const char *text = "1 2 3 4 5 20.0 21 twentytwo 2.3";
        double num1(0),num2(0),num3(0),num4(0);

        ValueTokenizer t(text);
        // read 4 doubles after skipping over 5 numbers
        try {
            t.skip(5);
            num1 = t.next_double();
            num2 = t.next_double();
            num3 = t.next_double();
            num4 = t.next_double();
        } catch (TokenizerException &e) {
            std::cout << "Reading numbers failed: " << e.what() << "\n";
        }
        std::cout << "Values: " << num1 << " " << num2 << " " << num3 << " " << num4 << "\n";
        return 0;
    }
:::
::::
::::::

This code example should produce the following output:

:::: {.highlight-none .notranslate}
::: highlight
    Reading numbers failed: Not a valid floating-point number: 'twentytwo'
    Values: 20 21 0 0
:::
::::

------------------------------------------------------------------------

[]{#_CPPv3N9LAMMPS_NS9TokenizerE}[]{#_CPPv2N9LAMMPS_NS9TokenizerE}[]{#LAMMPS_NS::Tokenizer}[]{#classLAMMPS__NS_1_1Tokenizer .target}[[class]{.pre}]{.k}[ ]{.w}[[[Tokenizer]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9TokenizerE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS9Tokenizer9TokenizerENSt6stringENSt6stringE}[]{#_CPPv2N9LAMMPS_NS9Tokenizer9TokenizerENSt6stringENSt6stringE}[]{#LAMMPS_NS::Tokenizer::Tokenizer__ss.ss}[]{#classLAMMPS__NS_1_1Tokenizer_1a1a572462a4d7e941633c746e21bb7586 .target}[[[Tokenizer]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[str]{.pre}]{.n .sig-param}, [[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[separators]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[TOKENIZER_DEFAULT_SEPARATORS]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS9Tokenizer9TokenizerENSt6stringENSt6stringE "Link to this definition"){.headerlink}\

    :   Class for splitting text into words

        This tokenizer will break down a string into sub-strings (i.e words) separated by the given separator characters. If the string contains certain known UTF-8 characters they will be replaced by their ASCII equivalents processing the string.

        *See also*

        :   [[`ValueTokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS14ValueTokenizerE "LAMMPS_NS::ValueTokenizer"){.reference .internal}, [[`utils::split_words()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils11split_wordsERKNSt6stringE "LAMMPS_NS::utils::split_words"){.reference .internal}, [[`utils::utf8_subst()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils10utf8_substERKNSt6stringE "LAMMPS_NS::utils::utf8_subst"){.reference .internal}

        Parameters[:]{.colon}

        :   - **str** -- string to be processed

            - **\_separators** -- string with separator characters (default: " \\t\\r\\n\\f")

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS9Tokenizer5resetEv}[]{#_CPPv2N9LAMMPS_NS9Tokenizer5resetEv}[]{#LAMMPS_NS::Tokenizer::reset}[]{#classLAMMPS__NS_1_1Tokenizer_1ad20897c5c8bd47f5d4005989bead0e55 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[reset]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS9Tokenizer5resetEv "Link to this definition"){.headerlink}\

    :   Re-position the tokenizer state to the first word, i.e. the first non-separator character

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS9Tokenizer4skipEi}[]{#_CPPv2N9LAMMPS_NS9Tokenizer4skipEi}[]{#LAMMPS_NS::Tokenizer::skip__i}[]{#classLAMMPS__NS_1_1Tokenizer_1abda0e6255008b1441f06a62f197da9a7 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[skip]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS9Tokenizer4skipEi "Link to this definition"){.headerlink}\

    :   Skip over a given number of tokens

        Parameters[:]{.colon}

        :   **n** -- number of tokens to skip over

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS9Tokenizer8has_nextEv}[]{#_CPPv2NK9LAMMPS_NS9Tokenizer8has_nextEv}[]{#LAMMPS_NS::Tokenizer::has_nextC}[]{#classLAMMPS__NS_1_1Tokenizer_1a5ac70fe9462200eec1fe01b48ea992f3 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[has_next]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS9Tokenizer8has_nextEv "Link to this definition"){.headerlink}\

    :   Indicate whether more tokens are available

        Returns[:]{.colon}

        :   true if there are more tokens, false if not

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS9Tokenizer8containsERKNSt6stringE}[]{#_CPPv2NK9LAMMPS_NS9Tokenizer8containsERKNSt6stringE}[]{#LAMMPS_NS::Tokenizer::contains__ssCRC}[]{#classLAMMPS__NS_1_1Tokenizer_1abf5acdb9f865006dd3d41f084403f74f .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[contains]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS9Tokenizer8containsERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Search the text to be processed for a sub-string.

        This method does a generic sub-string match.

        Parameters[:]{.colon}

        :   **str** -- string to be searched for

        Returns[:]{.colon}

        :   true if string was found, false if not

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS9Tokenizer7matchesERKNSt6stringE}[]{#_CPPv2NK9LAMMPS_NS9Tokenizer7matchesERKNSt6stringE}[]{#LAMMPS_NS::Tokenizer::matches__ssCRC}[]{#classLAMMPS__NS_1_1Tokenizer_1a07a6c962ca23635328ffde2dbac74533 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[matches]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS9Tokenizer7matchesERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Search the text to be processed for regular expression match.

        This method matches the current string against a regular expression using the [[`utils::strmatch()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils8strmatchERKNSt6stringERKNSt6stringE "LAMMPS_NS::utils::strmatch"){.reference .internal} function.

        Parameters[:]{.colon}

        :   **str** -- regular expression to be matched against

        Returns[:]{.colon}

        :   true if string was found, false if not

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS9Tokenizer4nextEv}[]{#_CPPv2N9LAMMPS_NS9Tokenizer4nextEv}[]{#LAMMPS_NS::Tokenizer::next}[]{#classLAMMPS__NS_1_1Tokenizer_1afba811f5984f17a43875432cb2845bc3 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[next]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS9Tokenizer4nextEv "Link to this definition"){.headerlink}\

    :   Retrieve next token.

        Returns[:]{.colon}

        :   string with the next token

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS9Tokenizer5countEv}[]{#_CPPv2N9LAMMPS_NS9Tokenizer5countEv}[]{#LAMMPS_NS::Tokenizer::count}[]{#classLAMMPS__NS_1_1Tokenizer_1ad873dc786f051a2c04e32d1541d3702e .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[count]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS9Tokenizer5countEv "Link to this definition"){.headerlink}\

    :   Count number of tokens in text.

        Returns[:]{.colon}

        :   number of counted tokens

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS9Tokenizer9as_vectorEv}[]{#_CPPv2N9LAMMPS_NS9Tokenizer9as_vectorEv}[]{#LAMMPS_NS::Tokenizer::as_vector}[]{#classLAMMPS__NS_1_1Tokenizer_1abc12e1da3f00c1a120a02b136f0730dd .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[as_vector]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS9Tokenizer9as_vectorEv "Link to this definition"){.headerlink}\

    :   Retrieve the entire text converted to an STL vector of tokens.

        Returns[:]{.colon}

        :   The STL vector
    :::

<!-- -->

[]{#_CPPv3N9LAMMPS_NS18TokenizerExceptionE}[]{#_CPPv2N9LAMMPS_NS18TokenizerExceptionE}[]{#LAMMPS_NS::TokenizerException}[]{#classLAMMPS__NS_1_1TokenizerException .target}[[class]{.pre}]{.k}[ ]{.w}[[[TokenizerException]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[:]{.pre}]{.p}[ ]{.w}[[public]{.pre}]{.k}[ ]{.w}[[exception]{.pre}]{.n}[](#_CPPv4N9LAMMPS_NS18TokenizerExceptionE "Link to this definition"){.headerlink}\

:   General Tokenizer exception class

    Subclassed by [[InvalidFloatException]{.std .std-ref}](#classLAMMPS__NS_1_1InvalidFloatException){.reference .internal}, [[InvalidIntegerException]{.std .std-ref}](#classLAMMPS__NS_1_1InvalidIntegerException){.reference .internal}

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS18TokenizerException18TokenizerExceptionEv}[]{#_CPPv2N9LAMMPS_NS18TokenizerException18TokenizerExceptionEv}[]{#LAMMPS_NS::TokenizerException::TokenizerException}[]{#classLAMMPS__NS_1_1TokenizerException_1a029374723bf07e5d4b7f2716c6546891 .target}[[[TokenizerException]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[delete]{.pre}]{.k}[](#_CPPv4N9LAMMPS_NS18TokenizerException18TokenizerExceptionEv "Link to this definition"){.headerlink}\

    :   The default constructor is disabled

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS18TokenizerException18TokenizerExceptionERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS18TokenizerException18TokenizerExceptionERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::TokenizerException::TokenizerException__ssCR.ssCR}[]{#classLAMMPS__NS_1_1TokenizerException_1afcd938a3385e0b950738c2e24cdbc484 .target}[[explicit]{.pre}]{.k}[ ]{.w}[[[TokenizerException]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[msg]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[token]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS18TokenizerException18TokenizerExceptionERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Thrown during retrieving or skipping tokens

        Parameters[:]{.colon}

        :   - **msg** -- String with error message

            - **token** -- String of the token or word that caused the error

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS18TokenizerException4whatEv}[]{#_CPPv2NK9LAMMPS_NS18TokenizerException4whatEv}[]{#LAMMPS_NS::TokenizerException::whatC}[]{#classLAMMPS__NS_1_1TokenizerException_1abf843cbb29dec939d0731e491bab6f70 .target}[[inline]{.pre}]{.k}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[what]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[ ]{.w}[[override]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS18TokenizerException4whatEv "Link to this definition"){.headerlink}\

    :   Retrieve message describing the thrown exception

        This function provides the message that can be retrieved when the corresponding exception is caught.

        Returns[:]{.colon}

        :   String with error message
    :::

<!-- -->

[]{#_CPPv3N9LAMMPS_NS14ValueTokenizerE}[]{#_CPPv2N9LAMMPS_NS14ValueTokenizerE}[]{#LAMMPS_NS::ValueTokenizer}[]{#classLAMMPS__NS_1_1ValueTokenizer .target}[[class]{.pre}]{.k}[ ]{.w}[[[ValueTokenizer]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS14ValueTokenizerE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS14ValueTokenizer14ValueTokenizerERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS14ValueTokenizer14ValueTokenizerERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::ValueTokenizer::ValueTokenizer__ssCR.ssCR}[]{#classLAMMPS__NS_1_1ValueTokenizer_1a9fbf461f611028a7d95b7df0dc8dbec4 .target}[[[ValueTokenizer]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[separators]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[TOKENIZER_DEFAULT_SEPARATORS]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14ValueTokenizer14ValueTokenizerERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Class for reading text with numbers

        *See also*

        :   [[`Tokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS9TokenizerE "LAMMPS_NS::Tokenizer"){.reference .internal}

        ::: {.admonition .seealso}
        See also

        Tokenizer [[InvalidIntegerException]{.std .std-ref}](#classLAMMPS__NS_1_1InvalidIntegerException){.reference .internal} [[InvalidFloatException]{.std .std-ref}](#classLAMMPS__NS_1_1InvalidFloatException){.reference .internal}
        :::

        Parameters[:]{.colon}

        :   - **str** -- String to be processed

            - **separators** -- String with separator characters (default: " \\t\\r\\n\\f")

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14ValueTokenizer11next_stringEv}[]{#_CPPv2N9LAMMPS_NS14ValueTokenizer11next_stringEv}[]{#LAMMPS_NS::ValueTokenizer::next_string}[]{#classLAMMPS__NS_1_1ValueTokenizer_1ad19df6455b8dfbfd2e5b1d93fc72d257 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[next_string]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14ValueTokenizer11next_stringEv "Link to this definition"){.headerlink}\

    :   Retrieve next token

        Returns[:]{.colon}

        :   string with next token

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14ValueTokenizer11next_tagintEv}[]{#_CPPv2N9LAMMPS_NS14ValueTokenizer11next_tagintEv}[]{#LAMMPS_NS::ValueTokenizer::next_tagint}[]{#classLAMMPS__NS_1_1ValueTokenizer_1a388a19376fd8647693fa10077e29a68f .target}[[tagint]{.pre}]{.n}[ ]{.w}[[[next_tagint]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14ValueTokenizer11next_tagintEv "Link to this definition"){.headerlink}\

    :   Retrieve next token and convert to tagint

        Returns[:]{.colon}

        :   value of next token

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14ValueTokenizer11next_bigintEv}[]{#_CPPv2N9LAMMPS_NS14ValueTokenizer11next_bigintEv}[]{#LAMMPS_NS::ValueTokenizer::next_bigint}[]{#classLAMMPS__NS_1_1ValueTokenizer_1a960e60b9cac96e1abfc9beb6a436e414 .target}[[bigint]{.pre}]{.n}[ ]{.w}[[[next_bigint]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14ValueTokenizer11next_bigintEv "Link to this definition"){.headerlink}\

    :   Retrieve next token and convert to bigint

        Returns[:]{.colon}

        :   value of next token

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14ValueTokenizer8next_intEv}[]{#_CPPv2N9LAMMPS_NS14ValueTokenizer8next_intEv}[]{#LAMMPS_NS::ValueTokenizer::next_int}[]{#classLAMMPS__NS_1_1ValueTokenizer_1a659db78ef3cd8cdbfa35654fbea28929 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[next_int]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14ValueTokenizer8next_intEv "Link to this definition"){.headerlink}\

    :   Retrieve next token and convert to int

        Returns[:]{.colon}

        :   value of next token

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14ValueTokenizer11next_doubleEv}[]{#_CPPv2N9LAMMPS_NS14ValueTokenizer11next_doubleEv}[]{#LAMMPS_NS::ValueTokenizer::next_double}[]{#classLAMMPS__NS_1_1ValueTokenizer_1aa6b2325cb771c1d1aa11cc5bd3c3f2e9 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[next_double]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14ValueTokenizer11next_doubleEv "Link to this definition"){.headerlink}\

    :   Retrieve next token and convert to double

        Returns[:]{.colon}

        :   value of next token

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS14ValueTokenizer8has_nextEv}[]{#_CPPv2NK9LAMMPS_NS14ValueTokenizer8has_nextEv}[]{#LAMMPS_NS::ValueTokenizer::has_nextC}[]{#classLAMMPS__NS_1_1ValueTokenizer_1a5ac70fe9462200eec1fe01b48ea992f3 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[has_next]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS14ValueTokenizer8has_nextEv "Link to this definition"){.headerlink}\

    :   Indicate whether more tokens are available

        Returns[:]{.colon}

        :   true if there are more tokens, false if not

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS14ValueTokenizer8containsERKNSt6stringE}[]{#_CPPv2NK9LAMMPS_NS14ValueTokenizer8containsERKNSt6stringE}[]{#LAMMPS_NS::ValueTokenizer::contains__ssCRC}[]{#classLAMMPS__NS_1_1ValueTokenizer_1a48b6af4c43173e0a07e80d29f125ae62 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[contains]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS14ValueTokenizer8containsERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Search the text to be processed for a sub-string.

        This method does a generic sub-string match.

        Parameters[:]{.colon}

        :   **value** -- string with value to be searched for

        Returns[:]{.colon}

        :   true if string was found, false if not

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS14ValueTokenizer7matchesERKNSt6stringE}[]{#_CPPv2NK9LAMMPS_NS14ValueTokenizer7matchesERKNSt6stringE}[]{#LAMMPS_NS::ValueTokenizer::matches__ssCRC}[]{#classLAMMPS__NS_1_1ValueTokenizer_1a07a6c962ca23635328ffde2dbac74533 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[matches]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS14ValueTokenizer7matchesERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Search the text to be processed for regular expression match.

        This method matches the current string against a regular expression using the [[`utils::strmatch()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils8strmatchERKNSt6stringERKNSt6stringE "LAMMPS_NS::utils::strmatch"){.reference .internal} function.

        Parameters[:]{.colon}

        :   **str** -- regular expression to be matched against

        Returns[:]{.colon}

        :   true if string was found, false if not

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14ValueTokenizer4skipEi}[]{#_CPPv2N9LAMMPS_NS14ValueTokenizer4skipEi}[]{#LAMMPS_NS::ValueTokenizer::skip__i}[]{#classLAMMPS__NS_1_1ValueTokenizer_1a8031283fcb7534c047cd51957d3bfb80 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[skip]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[ntokens]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14ValueTokenizer4skipEi "Link to this definition"){.headerlink}\

    :   Skip over a given number of tokens

        Parameters[:]{.colon}

        :   **n** -- number of tokens to skip over

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14ValueTokenizer5countEv}[]{#_CPPv2N9LAMMPS_NS14ValueTokenizer5countEv}[]{#LAMMPS_NS::ValueTokenizer::count}[]{#classLAMMPS__NS_1_1ValueTokenizer_1ad873dc786f051a2c04e32d1541d3702e .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[count]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14ValueTokenizer5countEv "Link to this definition"){.headerlink}\

    :   Count number of tokens in text.

        Returns[:]{.colon}

        :   number of counted tokens
    :::

<!-- -->

[]{#_CPPv3N9LAMMPS_NS23InvalidIntegerExceptionE}[]{#_CPPv2N9LAMMPS_NS23InvalidIntegerExceptionE}[]{#LAMMPS_NS::InvalidIntegerException}[]{#classLAMMPS__NS_1_1InvalidIntegerException .target}[[class]{.pre}]{.k}[ ]{.w}[[[InvalidIntegerException]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[:]{.pre}]{.p}[ ]{.w}[[public]{.pre}]{.k}[ ]{.w}[[[TokenizerException]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS18TokenizerExceptionE "LAMMPS_NS::TokenizerException"){.reference .internal}[](#_CPPv4N9LAMMPS_NS23InvalidIntegerExceptionE "Link to this definition"){.headerlink}\

:   Exception thrown by ValueTokenizer when trying to convert an invalid integer string

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS23InvalidIntegerException23InvalidIntegerExceptionERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS23InvalidIntegerException23InvalidIntegerExceptionERKNSt6stringE}[]{#LAMMPS_NS::InvalidIntegerException::InvalidIntegerException__ssCR}[]{#classLAMMPS__NS_1_1InvalidIntegerException_1abbff68ef6488f500630d129910eb9136 .target}[[inline]{.pre}]{.k}[ ]{.w}[[explicit]{.pre}]{.k}[ ]{.w}[[[InvalidIntegerException]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[token]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS23InvalidIntegerException23InvalidIntegerExceptionERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Thrown during converting string to integer number

        Parameters[:]{.colon}

        :   **token** -- String of the token/word that caused the error
    :::

<!-- -->

[]{#_CPPv3N9LAMMPS_NS21InvalidFloatExceptionE}[]{#_CPPv2N9LAMMPS_NS21InvalidFloatExceptionE}[]{#LAMMPS_NS::InvalidFloatException}[]{#classLAMMPS__NS_1_1InvalidFloatException .target}[[class]{.pre}]{.k}[ ]{.w}[[[InvalidFloatException]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[:]{.pre}]{.p}[ ]{.w}[[public]{.pre}]{.k}[ ]{.w}[[[TokenizerException]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS18TokenizerExceptionE "LAMMPS_NS::TokenizerException"){.reference .internal}[](#_CPPv4N9LAMMPS_NS21InvalidFloatExceptionE "Link to this definition"){.headerlink}\

:   Exception thrown by ValueTokenizer when trying to convert an floating point string

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS21InvalidFloatException21InvalidFloatExceptionERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS21InvalidFloatException21InvalidFloatExceptionERKNSt6stringE}[]{#LAMMPS_NS::InvalidFloatException::InvalidFloatException__ssCR}[]{#classLAMMPS__NS_1_1InvalidFloatException_1af72f7f4352493364c8f734f17f416ded .target}[[inline]{.pre}]{.k}[ ]{.w}[[explicit]{.pre}]{.k}[ ]{.w}[[[InvalidFloatException]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[token]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS21InvalidFloatException21InvalidFloatExceptionERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Thrown during converting string to floating point number

        Parameters[:]{.colon}

        :   **token** -- String of the token/word that caused the error
    :::
:::::::::::::

------------------------------------------------------------------------

::::::: {#argument-parsing-classes .section}
# [4.18. ]{.section-number}Argument parsing classes[](#argument-parsing-classes "Link to this heading"){.headerlink}

The purpose of argument parsing classes it to simplify and unify how arguments of commands in LAMMPS are parsed and to make abstractions of repetitive tasks.

The [[`LAMMPS_NS::ArgInfo`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS7ArgInfoE "LAMMPS_NS::ArgInfo"){.reference .internal} class provides an abstraction for parsing references to compute or fix styles, variables or custom integer or double properties handled by [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal}. These would start with a "c\_", "f\_", "v\_", "d\_", "d2\_", "i\_", or "i2\_" followed by the ID or name of than instance and may be postfixed with one or two array indices "\[\<number\>\]" with numbers \> 0.

A typical code segment would look like this:

:::::: {#id6 .literal-block-wrapper .docutils .container}
::: code-block-caption
[Usage example for ArgInfo class]{.caption-text}[](#id6 "Link to this code"){.headerlink}
:::

:::: {.highlight-c++ .notranslate}
::: highlight
    int nvalues = 0;
    for (iarg = 0; iarg < nargnew; iarg++) {
      ArgInfo argi(arg[iarg]);

      which[nvalues] = argi.get_type();
      argindex[nvalues] = argi.get_index1();
      ids[nvalues] = argi.copy_name();

      if ((which[nvalues] == ArgInfo::UNKNOWN)
           || (which[nvalues] == ArgInfo::NONE)
           || (argi.get_dim() > 1))
        error->all(FLERR,"Illegal compute XXX command");

      nvalues++;
    }
:::
::::
::::::

------------------------------------------------------------------------

[]{#_CPPv3N9LAMMPS_NS7ArgInfoE}[]{#_CPPv2N9LAMMPS_NS7ArgInfoE}[]{#LAMMPS_NS::ArgInfo}[]{#classLAMMPS__NS_1_1ArgInfo .target}[[class]{.pre}]{.k}[ ]{.w}[[[ArgInfo]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfoE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Types

    []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypesE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypesE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13 .target}[[enum]{.pre}]{.k}[ ]{.w}[[[ArgTypes]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypesE "Link to this definition"){.headerlink}\

    :   constants for argument types

        *Values:*

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes5ERRORE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes5ERRORE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a2fd6f336d08340583bd620a7f5694c90 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[ERROR]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes5ERRORE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes7UNKNOWNE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes7UNKNOWNE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a6ce26a62afab55d7606ad4e92428b30c .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[UNKNOWN]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes7UNKNOWNE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes4NONEE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes4NONEE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13ac157bdf0b85a40d2619cbc8bc1ae5fe2 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[NONE]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes4NONEE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes1XE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes1XE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a58833a3110c570fb05130d40c365d1e4 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[X]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes1XE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes1VE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes1VE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a28f41f1144eee94834387e9a6a088bc1 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[V]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes1VE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes1FE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes1FE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13af382a63cc3d6491bf26b59e66f46826d .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[F]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes1FE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes7COMPUTEE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes7COMPUTEE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a391a0f3463a51c90bdf19aa7f35e0b46 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[COMPUTE]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes7COMPUTEE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes3FIXE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes3FIXE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a4c71825a48c0068b0761fd432c96d451 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[FIX]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes3FIXE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes8VARIABLEE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes8VARIABLEE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a39031ce5df6f91d3778590d6d644b9ea .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[VARIABLE]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes8VARIABLEE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes7KEYWORDE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes7KEYWORDE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a129281444e94f5f509cba213d51a814d .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[KEYWORD]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes7KEYWORDE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes4TYPEE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes4TYPEE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13ab47ea8bb955afd0adc0ef98517dd6084 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[TYPE]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes4TYPEE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes8MOLECULEE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes8MOLECULEE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a52a658fe0a308541e9fd6a5e1248d500 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[MOLECULE]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes8MOLECULEE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes5DNAMEE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes5DNAMEE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13acc5ed32d1085edc116f9e5b127775f6d .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[DNAME]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes5DNAMEE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes5INAMEE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes5INAMEE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a42992693b11698580c1c11967cbca39f .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[INAME]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes5INAMEE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes14DENSITY_NUMBERE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes14DENSITY_NUMBERE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a36aba5a6b73317be76adbe7e40189e16 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[DENSITY_NUMBER]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes14DENSITY_NUMBERE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes12DENSITY_MASSE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes12DENSITY_MASSE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a4763598e36da157b838fe8f74e8063ba .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[DENSITY_MASS]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes12DENSITY_MASSE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes4MASSE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes4MASSE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a1c910486b66cf1ccce2ef81d4318227f .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[MASS]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes4MASSE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes11TEMPERATUREE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes11TEMPERATUREE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13ac4ae6787ff1d8b2d1cf0ae9aa696e56c .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[TEMPERATURE]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes11TEMPERATUREE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes5BIN1DE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes5BIN1DE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13af113047abcb2980258dbb091edc74919 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[BIN1D]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes5BIN1DE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes5BIN2DE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes5BIN2DE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a172ec7ac0684d66a619471d3d6cb1520 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[BIN2D]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes5BIN2DE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes5BIN3DE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes5BIN3DE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a32f02f6ff0b9d0b294a92bd63c5658b6 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[BIN3D]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes5BIN3DE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes9BINSPHEREE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes9BINSPHEREE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13aea2305105c66b4fd68a8acd3b62b548f .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[BINSPHERE]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes9BINSPHEREE "Link to this definition"){.headerlink}\

        :   

        []{#_CPPv3N9LAMMPS_NS7ArgInfo8ArgTypes11BINCYLINDERE}[]{#_CPPv2N9LAMMPS_NS7ArgInfo8ArgTypes11BINCYLINDERE}[]{#classLAMMPS__NS_1_1ArgInfo_1a6df44aeb82f88a507de3bccbb74a6b13a751fb391ace04b5f6bd4bc9b8209bbc0 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[BINCYLINDER]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes11BINCYLINDERE "Link to this definition"){.headerlink}\

        :   
    :::

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS7ArgInfo7ArgInfoERKNSt6stringEi}[]{#_CPPv2N9LAMMPS_NS7ArgInfo7ArgInfoERKNSt6stringEi}[]{#LAMMPS_NS::ArgInfo::ArgInfo__ssCR.i}[]{#classLAMMPS__NS_1_1ArgInfo_1a81a8a9e941f241bc7bd8df5048edd72e .target}[[[ArgInfo]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[arg]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[allowed]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[[COMPUTE]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes7COMPUTEE "LAMMPS_NS::ArgInfo::COMPUTE"){.reference .internal}[ ]{.w}[[\|]{.pre}]{.o}[ ]{.w}[[[FIX]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes3FIXE "LAMMPS_NS::ArgInfo::FIX"){.reference .internal}[ ]{.w}[[\|]{.pre}]{.o}[ ]{.w}[[[VARIABLE]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS7ArgInfo8ArgTypes8VARIABLEE "LAMMPS_NS::ArgInfo::VARIABLE"){.reference .internal}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS7ArgInfo7ArgInfoERKNSt6stringEi "Link to this definition"){.headerlink}\

    :   Class for processing references to fixes, computes and variables

        This class provides an abstraction for the repetitive task of parsing arguments that may contain references to fixes, computes, variables, or custom per-atom properties. It will identify the name and the index value in the first and second dimension, if present.

        Parameters[:]{.colon}

        :   - **arg** -- string with possible reference

            - **allowed** -- integer with bitmap of allowed types of references

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS7ArgInfo8get_typeEv}[]{#_CPPv2NK9LAMMPS_NS7ArgInfo8get_typeEv}[]{#LAMMPS_NS::ArgInfo::get_typeC}[]{#classLAMMPS__NS_1_1ArgInfo_1a328fa3a7797b2464bfb1079d365d0edb .target}[[inline]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[[get_type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS7ArgInfo8get_typeEv "Link to this definition"){.headerlink}\

    :   get type of reference

        Return a type constant for the reference. This may be either COMPUTE, FIX, VARIABLE (if not restricted to a subset of those by the "allowed" argument of the constructor) or NONE, if it if not a recognized or allowed reference, or UNKNOWN, in case some error happened identifying or parsing the values of the indices

        Returns[:]{.colon}

        :   integer with a constant from ArgTypes enumerator

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS7ArgInfo7get_dimEv}[]{#_CPPv2NK9LAMMPS_NS7ArgInfo7get_dimEv}[]{#LAMMPS_NS::ArgInfo::get_dimC}[]{#classLAMMPS__NS_1_1ArgInfo_1a812caf9be8bbe92a2fd8273dd2dda065 .target}[[inline]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[[get_dim]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS7ArgInfo7get_dimEv "Link to this definition"){.headerlink}\

    :   get dimension of reference

        This will return either 0, 1, 2 depending on whether the reference has no, one or two "\[{number}\]" postfixes.

        Returns[:]{.colon}

        :   integer with the dimensionality of the reference

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS7ArgInfo10get_index1Ev}[]{#_CPPv2NK9LAMMPS_NS7ArgInfo10get_index1Ev}[]{#LAMMPS_NS::ArgInfo::get_index1C}[]{#classLAMMPS__NS_1_1ArgInfo_1a1ef3adbaad24c6a95b2cbc7475585ffd .target}[[inline]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[[get_index1]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS7ArgInfo10get_index1Ev "Link to this definition"){.headerlink}\

    :   get index of first dimension

        This will return the number in the first "\[{number}\]" postfix or 0 if there is no postfix.

        Returns[:]{.colon}

        :   integer with index or the postfix or 0

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS7ArgInfo10get_index2Ev}[]{#_CPPv2NK9LAMMPS_NS7ArgInfo10get_index2Ev}[]{#LAMMPS_NS::ArgInfo::get_index2C}[]{#classLAMMPS__NS_1_1ArgInfo_1adcbe39c7eaf369281347891bd0818678 .target}[[inline]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[[get_index2]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS7ArgInfo10get_index2Ev "Link to this definition"){.headerlink}\

    :   get index of second dimension

        This will return the number in the second "\[{number}\]" postfix or -1 if there is no second postfix.

        Returns[:]{.colon}

        :   integer with index of the postfix or -1

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS7ArgInfo8get_nameEv}[]{#_CPPv2NK9LAMMPS_NS7ArgInfo8get_nameEv}[]{#LAMMPS_NS::ArgInfo::get_nameC}[]{#classLAMMPS__NS_1_1ArgInfo_1a635420c59837dceb825845c2301c6db8 .target}[[inline]{.pre}]{.k}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[get_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS7ArgInfo8get_nameEv "Link to this definition"){.headerlink}\

    :   return reference to the ID or name of the reference

        This string is pointing to an internal storage element and is only valid to use while the ArgInfo class instance is in scope. If you need a long-lived string make a copy with copy_name().

        Returns[:]{.colon}

        :   C-style char \* string

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS7ArgInfo9copy_nameEv}[]{#_CPPv2N9LAMMPS_NS7ArgInfo9copy_nameEv}[]{#LAMMPS_NS::ArgInfo::copy_name}[]{#classLAMMPS__NS_1_1ArgInfo_1aec1f62f5dcbdb968f21542406ecafb1c .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[copy_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS7ArgInfo9copy_nameEv "Link to this definition"){.headerlink}\

    :   make copy of the ID of the reference as C-style string

        The ID is copied into a buffer allocated with "new" and thus must be later deleted with "delete \[\]" to avoid a memory leak. Because it is a full copy in a newly allocated buffer, the lifetime of this string extends beyond the the time the ArgInfo class is in scope.

        Returns[:]{.colon}

        :   copy of string as char \*
    :::

------------------------------------------------------------------------
:::::::

::: {#safe-pointer-classes .section}
[]{#id1}

# [4.19. ]{.section-number}Safe pointer classes[](#safe-pointer-classes "Link to this heading"){.headerlink}

These are custom classes to support the [Resource Acquisition Is Initialization (RAII)](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization){.reference .external} programming idiom in LAMMPS for certain types of pointers. Currently there is:

[]{#_CPPv3N9LAMMPS_NS11SafeFilePtrE}[]{#_CPPv2N9LAMMPS_NS11SafeFilePtrE}[]{#LAMMPS_NS::SafeFilePtr}[]{#classLAMMPS__NS_1_1SafeFilePtr .target}[[class]{.pre}]{.k}[ ]{.w}[[[SafeFilePtr]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS11SafeFilePtrE "Link to this definition"){.headerlink}\

:   Class to automatically close a FILE pointer when it goes out of scope

    This is a drop-in replacement for declaring a [`FILE`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} variable and can be passed to functions or used in logical expressions the same way. This is particularly useful when a code block will throw an exception, or has to close and re-open a file and similar. It helps to simplify code and reduces the risk of memory and file descriptor leaks.

    Below are some usage examples:

    :::: {.highlight-c++ .notranslate}
    ::: highlight
        // Replace:
        FILE *fp = nullptr;
        // With:
        SafeFilePtr fp;

        // You can use "fp" as usual:
        fp = fopen("some.file","r");
        // a second assignment will automatically close the opened file
        fp = fopen("other.file", "r");
        // and assigning nullptr will just close it
        fp = nullptr;

        // There also is a custom constructor available as a shortcut
        SafeFilePtr fp(fopen("some.file", "r"));

        // You can indicate that a file was opened with popen() to call pclose() instead of fclose()
        SafeFilePtr fp;
        if (platform::has_compress_extension(filename)) {
          fp.set_pclose();
          fp = platform::compressed_write(filename);
        } else {
          fp = fopen(filename, "w");
        }
        if (!fp) error->one(FLERR, "Failed to open file {}: {}", filename, utils::getsyserror());

        // reading or writing works without needing to change the source code
        fputs("write text to file\n", fp);
        char buffer[100];
        utils::sfgets(FLERR, buffer, 100, fp, filename, error);
    :::
    ::::

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS11SafeFilePtraSEP4FILE}[]{#_CPPv2N9LAMMPS_NS11SafeFilePtraSEP4FILE}[]{#LAMMPS_NS::SafeFilePtr::assign-operator__FILEP}[]{#classLAMMPS__NS_1_1SafeFilePtr_1a4d02cdcf227f753f3ce19c48d5ca6bc4 .target}[[[SafeFilePtr]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS11SafeFilePtrE "LAMMPS_NS::SafeFilePtr"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[[operator]{.pre}]{.k}[[=]{.pre}]{.o}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[\_fp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11SafeFilePtraSEP4FILE "Link to this definition"){.headerlink}\

    :   Assign new file pointer and close old one if still open.

        The value of use_pclose determines whether [`pclose()`{.docutils .literal .notranslate}]{.pre} is called or [`fclose()`{.docutils .literal .notranslate}]{.pre}. Assigning [`nullptr`{.docutils .literal .notranslate}]{.pre} closes the file and resets use_pclose

        Parameters[:]{.colon}

        :   **\_fp** -- new file pointer, may be [`nullptr`{.docutils .literal .notranslate}]{.pre}

        Returns[:]{.colon}

        :   reference to updated class instance

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS11SafeFilePtr10set_pcloseEv}[]{#_CPPv2N9LAMMPS_NS11SafeFilePtr10set_pcloseEv}[]{#LAMMPS_NS::SafeFilePtr::set_pclose}[]{#classLAMMPS__NS_1_1SafeFilePtr_1a94beb8c479950e0551fca2c3cb95d79e .target}[[inline]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[set_pclose]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11SafeFilePtr10set_pcloseEv "Link to this definition"){.headerlink}\

    :   Flag that the file pointer needs to be closed with [`pclose()`{.docutils .literal .notranslate}]{.pre} instead of [`fclose()`{.docutils .literal .notranslate}]{.pre}

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS11SafeFilePtrcvP4FILEEv}[]{#_CPPv2NK9LAMMPS_NS11SafeFilePtrcvP4FILEEv}[]{#LAMMPS_NS::SafeFilePtr::castto-FILEP-operatorC}[]{#classLAMMPS__NS_1_1SafeFilePtr_1a1015f051671d1f606db762e01be07462 .target}[[inline]{.pre}]{.k}[ ]{.w}[[[operator]{.pre}]{.k}[ ]{.w}[[FILE]{.pre}]{.n}[[\*]{.pre}]{.p}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS11SafeFilePtrcvP4FILEEv "Link to this definition"){.headerlink}\

    :   Custom type cast operator so that [[SafeFilePtr]{.std .std-ref}](#classLAMMPS__NS_1_1SafeFilePtr){.reference .internal} can be used where FILE \* was used

        Returns[:]{.colon}

        :   currently stored/monitored file pointer
    :::

------------------------------------------------------------------------
:::

::::::: {#file-reader-classes .section}
[]{#id2}

# [4.20. ]{.section-number}File reader classes[](#file-reader-classes "Link to this heading"){.headerlink}

The purpose of the file reader classes is to simplify the recurring task of reading and parsing files. They can use the [[`ValueTokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS14ValueTokenizerE "LAMMPS_NS::ValueTokenizer"){.reference .internal} class to process the read in text. The [[`TextFileReader`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS14TextFileReaderE "LAMMPS_NS::TextFileReader"){.reference .internal} is a more general version while [[`PotentialFileReader`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS19PotentialFileReaderE "LAMMPS_NS::PotentialFileReader"){.reference .internal} is specialized to implement the behavior expected for looking up and reading/parsing files with potential parameters in LAMMPS. The potential file reader class requires a LAMMPS instance, requires to be run on MPI rank 0 only, will use the [[`utils::get_potential_file_path`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils23get_potential_file_pathERKNSt6stringE "LAMMPS_NS::utils::get_potential_file_path"){.reference .internal} function to look up and open the file, and will call the [`LAMMPS_NS::Error`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre} class in case of failures to read or to convert numbers, so that LAMMPS will be aborted.

:::::: {#id7 .literal-block-wrapper .docutils .container}
::: code-block-caption
[Use of PotentialFileReader class in pair style coul/streitz]{.caption-text}[](#id7 "Link to this code"){.headerlink}
:::

:::: {.highlight-c++ .notranslate}
::: highlight
     PotentialFileReader reader(lmp, file, "coul/streitz");
     char * line;

     while((line = reader.next_line(NPARAMS_PER_LINE))) {
       try {
         ValueTokenizer values(line);
         std::string iname = values.next_string();

         int ielement;
         for (ielement = 0; ielement < nelements; ielement++)
           if (iname == elements[ielement]) break;

         if (nparams == maxparam) {
           maxparam += DELTA;
           params = (Param *) memory->srealloc(params,maxparam*sizeof(Param),
                                               "pair:params");
         }

         params[nparams].ielement = ielement;
         params[nparams].chi = values.next_double();
         params[nparams].eta = values.next_double();
         params[nparams].gamma = values.next_double();
         params[nparams].zeta = values.next_double();
         params[nparams].zcore = values.next_double();

       } catch (TokenizerException & e) {
         error->one(FLERR, e.what());
       }
       nparams++;
     }
:::
::::
::::::

A file that would be parsed by the reader code fragment looks like this:

``` literal-block
# DATE: 2015-02-19 UNITS: metal CONTRIBUTOR: Ray Shan CITATION: Streitz and Mintmire, Phys Rev B, 50, 11996-12003 (1994)
#
# X (eV)                J (eV)          gamma (1/AA)   zeta (1/AA)    Z (e)

Al      0.000000        10.328655       0.000000        0.968438        0.763905
O       5.484763        14.035715       0.000000        2.143957        0.000000
```

------------------------------------------------------------------------

[]{#_CPPv3N9LAMMPS_NS14TextFileReaderE}[]{#_CPPv2N9LAMMPS_NS14TextFileReaderE}[]{#LAMMPS_NS::TextFileReader}[]{#classLAMMPS__NS_1_1TextFileReader .target}[[class]{.pre}]{.k}[ ]{.w}[[[TextFileReader]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS14TextFileReaderE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS14TextFileReader14TextFileReaderERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS14TextFileReader14TextFileReaderERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::TextFileReader::TextFileReader__ssCR.ssCR}[]{#classLAMMPS__NS_1_1TextFileReader_1a2043b5f5a6222c33ed29f356e09fa50a .target}[[[TextFileReader]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[filename]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[filetype]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14TextFileReader14TextFileReaderERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Class for reading and parsing text files

        The value of the class member variable *ignore_comments* controls whether any text following the pound sign (#) should be ignored (true) or not (false). Default: true, i.e. ignore.

        *See also*

        :   [[`TextFileReader`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS14TextFileReaderE "LAMMPS_NS::TextFileReader"){.reference .internal}

        Parameters[:]{.colon}

        :   - **filename** -- Name of file to be read

            - **filetype** -- Description of file type for error messages

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14TextFileReader14TextFileReaderEP4FILENSt6stringE}[]{#_CPPv2N9LAMMPS_NS14TextFileReader14TextFileReaderEP4FILENSt6stringE}[]{#LAMMPS_NS::TextFileReader::TextFileReader__FILEP.ss}[]{#classLAMMPS__NS_1_1TextFileReader_1ae85518b9022db4c1075338ccd8fe5de8 .target}[[[TextFileReader]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}, [[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[filetype]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14TextFileReader14TextFileReaderEP4FILENSt6stringE "Link to this definition"){.headerlink}\

    :   This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

        This function is useful in combination with [[`utils::open_potential()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils14open_potentialERKNSt6stringEP6LAMMPSPi "LAMMPS_NS::utils::open_potential"){.reference .internal}.

        ::: {.admonition .note}
        Note

        The FILE pointer is not closed in the destructor, but will be advanced when reading from it.
        :::

        Parameters[:]{.colon}

        :   - **fp** -- File descriptor of the already opened file

            - **filetype** -- Description of file type for error messages

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14TextFileReaderD0Ev}[]{#_CPPv2N9LAMMPS_NS14TextFileReaderD0Ev}[]{#LAMMPS_NS::TextFileReader::~TextFileReader}[]{#classLAMMPS__NS_1_1TextFileReader_1a60ce1f5ac0e90a8deedc0f0359eacc49 .target}[[virtual]{.pre}]{.k}[ ]{.w}[[[\~TextFileReader]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14TextFileReaderD0Ev "Link to this definition"){.headerlink}\

    :   Closes the file

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14TextFileReader11set_bufsizeEi}[]{#_CPPv2N9LAMMPS_NS14TextFileReader11set_bufsizeEi}[]{#LAMMPS_NS::TextFileReader::set_bufsize__i}[]{#classLAMMPS__NS_1_1TextFileReader_1af2f99f85d2cb5e54a4190e4acdeeb4aa .target}[[void]{.pre}]{.kt}[ ]{.w}[[[set_bufsize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14TextFileReader11set_bufsizeEi "Link to this definition"){.headerlink}\

    :   adjust line buffer size

        Parameters[:]{.colon}

        :   **newsize** -- New size of the internal line buffer

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14TextFileReader6rewindEv}[]{#_CPPv2N9LAMMPS_NS14TextFileReader6rewindEv}[]{#LAMMPS_NS::TextFileReader::rewind}[]{#classLAMMPS__NS_1_1TextFileReader_1ab8734e666421c9fe3b6380a818c6c727 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[rewind]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14TextFileReader6rewindEv "Link to this definition"){.headerlink}\

    :   Reset file to the beginning

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14TextFileReader9skip_lineEv}[]{#_CPPv2N9LAMMPS_NS14TextFileReader9skip_lineEv}[]{#LAMMPS_NS::TextFileReader::skip_line}[]{#classLAMMPS__NS_1_1TextFileReader_1a13171cc94df93641fa41710249bd2828 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[skip_line]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14TextFileReader9skip_lineEv "Link to this definition"){.headerlink}\

    :   Read the next line and ignore it

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14TextFileReader9next_lineEi}[]{#_CPPv2N9LAMMPS_NS14TextFileReader9next_lineEi}[]{#LAMMPS_NS::TextFileReader::next_line__i}[]{#classLAMMPS__NS_1_1TextFileReader_1ac8028df52c806625ec32fe25eb9e87c0 .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[next_line]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[nparams]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14TextFileReader9next_lineEi "Link to this definition"){.headerlink}\

    :   Read the next line(s) until *nparams* words have been read.

        This reads a line and counts the words in it, if the number is less than the requested number, it will read the next line, as well. Output will be a string with all read lines combined. The purpose is to somewhat replicate the reading behavior of formatted files in Fortran.

        If the *ignore_comments* class member has the value *true*, then any text read in is truncated at the first '#' character.

        Parameters[:]{.colon}

        :   **nparams** -- Number of words that must be read. Default: 0

        Returns[:]{.colon}

        :   String with the concatenated text

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14TextFileReader12next_dvectorEPdi}[]{#_CPPv2N9LAMMPS_NS14TextFileReader12next_dvectorEPdi}[]{#LAMMPS_NS::TextFileReader::next_dvector__doubleP.i}[]{#classLAMMPS__NS_1_1TextFileReader_1a4c74ed481f64285779f60633e6301a47 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[next_dvector]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[list]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14TextFileReader12next_dvectorEPdi "Link to this definition"){.headerlink}\

    :   Read lines until *n* doubles have been read and stored in array *list*

        This reads lines from the file using the next_line() function, and splits them into floating-point numbers using the ValueTokenizer class and stores the number in the provided list.

        Parameters[:]{.colon}

        :   - **list** -- Pointer to array with suitable storage for *n* doubles

            - **n** -- Number of doubles to be read

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS14TextFileReader11next_valuesEiRKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS14TextFileReader11next_valuesEiRKNSt6stringE}[]{#LAMMPS_NS::TextFileReader::next_values__i.ssCR}[]{#classLAMMPS__NS_1_1TextFileReader_1a8a0ce533407ad4d77f92c807de0131b0 .target}[[[ValueTokenizer]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS14ValueTokenizerE "LAMMPS_NS::ValueTokenizer"){.reference .internal}[ ]{.w}[[[next_values]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[nparams]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[separators]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[TOKENIZER_DEFAULT_SEPARATORS]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS14TextFileReader11next_valuesEiRKNSt6stringE "Link to this definition"){.headerlink}\

    :   Read text until *nparams* words are read and passed to a tokenizer object for custom parsing.

        This reads lines from the file using the next_line() function, and splits them into floating-point numbers using the ValueTokenizer class and stores the number in the provided list.

        Parameters[:]{.colon}

        :   - **nparams** -- Number of words to be read

            - **separators** -- String with list of separators.

        Returns[:]{.colon}

        :   ValueTokenizer object for read in text
    :::

    ::: {.breathe-sectiondef .docutils .container}
    Public Members

    []{#_CPPv3N9LAMMPS_NS14TextFileReader15ignore_commentsE}[]{#_CPPv2N9LAMMPS_NS14TextFileReader15ignore_commentsE}[]{#LAMMPS_NS::TextFileReader::ignore_comments__b}[]{#classLAMMPS__NS_1_1TextFileReader_1a87625d6c23cbea82833fceab91c31bc4 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[ignore_comments]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS14TextFileReader15ignore_commentsE "Link to this definition"){.headerlink}\

    :   Controls whether comments are ignored.
    :::

<!-- -->

[]{#_CPPv3N9LAMMPS_NS19PotentialFileReaderE}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReaderE}[]{#LAMMPS_NS::PotentialFileReader}[]{#classLAMMPS__NS_1_1PotentialFileReader .target}[[class]{.pre}]{.k}[ ]{.w}[[[PotentialFileReader]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[:]{.pre}]{.p}[ ]{.w}[[protected]{.pre}]{.k}[ ]{.w}[[[Pointers]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS8PointersE "LAMMPS_NS::Pointers"){.reference .internal}[](#_CPPv4N9LAMMPS_NS19PotentialFileReaderE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader19PotentialFileReaderEP6LAMMPSRKNSt6stringERKNSt6stringERKNSt6stringEKi}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader19PotentialFileReaderEP6LAMMPSRKNSt6stringERKNSt6stringERKNSt6stringEKi}[]{#LAMMPS_NS::PotentialFileReader::PotentialFileReader__LAMMPSP.ssCR.ssCR.ssCR.iC}[]{#classLAMMPS__NS_1_1PotentialFileReader_1a149f46f04cd28f4d9d293ff333380d54 .target}[[[PotentialFileReader]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[class]{.pre}]{.k}[ ]{.w}[[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[filename]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[potential_name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name_suffix]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[auto_convert]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader19PotentialFileReaderEP6LAMMPSRKNSt6stringERKNSt6stringERKNSt6stringEKi "Link to this definition"){.headerlink}\

    :   Class for reading and parsing [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} potential files

        The value of the class member variable *ignore_comments* controls whether any text following the pound sign (#) should be ignored (true) or not (false). Default: true, i.e. ignore.

        *See also*

        :   [[`TextFileReader`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS14TextFileReaderE "LAMMPS_NS::TextFileReader"){.reference .internal}

        Parameters[:]{.colon}

        :   - **lmp** -- Pointer to [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

            - **filename** -- Name of file to be read

            - **potential_name** -- Name of potential style for error messages

            - **name_suffix** -- Suffix added to potential name in error messages

            - **auto_convert** -- Bitmask of supported unit conversions

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReaderD0Ev}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReaderD0Ev}[]{#LAMMPS_NS::PotentialFileReader::~PotentialFileReader}[]{#classLAMMPS__NS_1_1PotentialFileReader_1a2fc140e8f6be2389ddffb5f7edce870e .target}[[[\~PotentialFileReader]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[override]{.pre}]{.k}[](#_CPPv4N9LAMMPS_NS19PotentialFileReaderD0Ev "Link to this definition"){.headerlink}\

    :   Closes the file

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader11set_bufsizeEi}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader11set_bufsizeEi}[]{#LAMMPS_NS::PotentialFileReader::set_bufsize__i}[]{#classLAMMPS__NS_1_1PotentialFileReader_1afa75eced2f22d604888f788a3ba34d06 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[set_bufsize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[bufsize]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader11set_bufsizeEi "Link to this definition"){.headerlink}\

    :   Set line buffer size of the internal TextFileReader class instance.

        Parameters[:]{.colon}

        :   **bufsize** -- New size of the line buffer

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader15ignore_commentsEb}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader15ignore_commentsEb}[]{#LAMMPS_NS::PotentialFileReader::ignore_comments__b}[]{#classLAMMPS__NS_1_1PotentialFileReader_1a84753973f8cd425807695e3c889f97f9 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[ignore_comments]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[bool]{.pre}]{.kt}[ ]{.w}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader15ignore_commentsEb "Link to this definition"){.headerlink}\

    :   Set comment (= text after '#') handling preference for the file to be read

        Parameters[:]{.colon}

        :   **value** -- Comment text is ignored if true, or not if false

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader6rewindEv}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader6rewindEv}[]{#LAMMPS_NS::PotentialFileReader::rewind}[]{#classLAMMPS__NS_1_1PotentialFileReader_1ab8734e666421c9fe3b6380a818c6c727 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[rewind]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader6rewindEv "Link to this definition"){.headerlink}\

    :   Reset file to the beginning

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader9skip_lineEv}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader9skip_lineEv}[]{#LAMMPS_NS::PotentialFileReader::skip_line}[]{#classLAMMPS__NS_1_1PotentialFileReader_1a13171cc94df93641fa41710249bd2828 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[skip_line]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader9skip_lineEv "Link to this definition"){.headerlink}\

    :   Read a line but ignore its content

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader9next_lineEi}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader9next_lineEi}[]{#LAMMPS_NS::PotentialFileReader::next_line__i}[]{#classLAMMPS__NS_1_1PotentialFileReader_1ac8028df52c806625ec32fe25eb9e87c0 .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[next_line]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[nparams]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader9next_lineEi "Link to this definition"){.headerlink}\

    :   Read the next line(s) until *nparams* words have been read.

        This reads a line and counts the words in it, if the number is less than the requested number, it will read the next line, as well. Output will be a string with all read lines combined. The purpose is to somewhat replicate the reading behavior of formatted files in Fortran.

        Parameters[:]{.colon}

        :   **nparams** -- Number of words that must be read. Default: 0

        Returns[:]{.colon}

        :   String with the concatenated text

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader12next_dvectorEPdi}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader12next_dvectorEPdi}[]{#LAMMPS_NS::PotentialFileReader::next_dvector__doubleP.i}[]{#classLAMMPS__NS_1_1PotentialFileReader_1a4c74ed481f64285779f60633e6301a47 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[next_dvector]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[list]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader12next_dvectorEPdi "Link to this definition"){.headerlink}\

    :   Read lines until *n* doubles have been read and stored in array *list*

        This reads lines from the file using the next_line() function, and splits them into floating-point numbers using the ValueTokenizer class and stores the number in the provided list.

        Parameters[:]{.colon}

        :   - **list** -- Pointer to array with suitable storage for *n* doubles

            - **n** -- Number of doubles to be read

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader11next_valuesEiRKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader11next_valuesEiRKNSt6stringE}[]{#LAMMPS_NS::PotentialFileReader::next_values__i.ssCR}[]{#classLAMMPS__NS_1_1PotentialFileReader_1a8a0ce533407ad4d77f92c807de0131b0 .target}[[[ValueTokenizer]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS14ValueTokenizerE "LAMMPS_NS::ValueTokenizer"){.reference .internal}[ ]{.w}[[[next_values]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[nparams]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[separators]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[TOKENIZER_DEFAULT_SEPARATORS]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader11next_valuesEiRKNSt6stringE "Link to this definition"){.headerlink}\

    :   Read text until *nparams* words are read and passed to a tokenizer object for custom parsing.

        This reads lines from the file using the next_line() function, and splits them into floating-point numbers using the ValueTokenizer class and stores the number in the provided list.

        Parameters[:]{.colon}

        :   - **nparams** -- Number of words to be read

            - **separators** -- String with list of separators.

        Returns[:]{.colon}

        :   ValueTokenizer object for read in text

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader11next_doubleEv}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader11next_doubleEv}[]{#LAMMPS_NS::PotentialFileReader::next_double}[]{#classLAMMPS__NS_1_1PotentialFileReader_1aa6b2325cb771c1d1aa11cc5bd3c3f2e9 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[next_double]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader11next_doubleEv "Link to this definition"){.headerlink}\

    :   Read next line and convert first word to a double

        Returns[:]{.colon}

        :   Value of first word in line as double

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader8next_intEv}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader8next_intEv}[]{#LAMMPS_NS::PotentialFileReader::next_int}[]{#classLAMMPS__NS_1_1PotentialFileReader_1a659db78ef3cd8cdbfa35654fbea28929 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[next_int]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader8next_intEv "Link to this definition"){.headerlink}\

    :   Read next line and convert first word to an int

        Returns[:]{.colon}

        :   Value of first word in line as int

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader11next_tagintEv}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader11next_tagintEv}[]{#LAMMPS_NS::PotentialFileReader::next_tagint}[]{#classLAMMPS__NS_1_1PotentialFileReader_1a388a19376fd8647693fa10077e29a68f .target}[[tagint]{.pre}]{.n}[ ]{.w}[[[next_tagint]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader11next_tagintEv "Link to this definition"){.headerlink}\

    :   Read next line and convert first word to a tagint

        Returns[:]{.colon}

        :   Value of first word in line as tagint

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader11next_bigintEv}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader11next_bigintEv}[]{#LAMMPS_NS::PotentialFileReader::next_bigint}[]{#classLAMMPS__NS_1_1PotentialFileReader_1a960e60b9cac96e1abfc9beb6a436e414 .target}[[bigint]{.pre}]{.n}[ ]{.w}[[[next_bigint]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader11next_bigintEv "Link to this definition"){.headerlink}\

    :   Read next line and convert first word to a bigint

        Returns[:]{.colon}

        :   Value of first word in line as bigint

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS19PotentialFileReader11next_stringEv}[]{#_CPPv2N9LAMMPS_NS19PotentialFileReader11next_stringEv}[]{#LAMMPS_NS::PotentialFileReader::next_string}[]{#classLAMMPS__NS_1_1PotentialFileReader_1ad19df6455b8dfbfd2e5b1d93fc72d257 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[next_string]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS19PotentialFileReader11next_stringEv "Link to this definition"){.headerlink}\

    :   Read next line and return first word

        Returns[:]{.colon}

        :   First word of read in line
    :::
:::::::

------------------------------------------------------------------------

::::::::::::::: {#type-label-support .section}
# [4.21. ]{.section-number}Type label support[](#type-label-support "Link to this heading"){.headerlink}

::: {#overview .section}
## [4.21.1. ]{.section-number}Overview[](#overview "Link to this heading"){.headerlink}

The [[`LabelMap`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS8LabelMapE "LAMMPS_NS::LabelMap"){.reference .internal} class provides a two way mapping between symbolic type labels in input and output files and numeric types as they are used by LAMMPS internally. Instead of changing the numeric types in files to satisfy the requirements from LAMMPS for a given application, the symbolic types can remain and only the label map needs to be adjusted. When following the convention that the labels for bonded interactions are created by joining the constituent atom types with hyphens, this can significantly improve readability, maintainability, and re-usability of inputs and reduces the chance of errors.

The LabelMap class also provides automatic type inference for bonded interactions based on their constituent atom types. For instance, based on the atom type labels, the corresponding bond, angle, dihedral, or improper types can be inferred provided the corresponding type labels follow the convention that they are composed of the symbolic atom types connected by hyphens.
:::

:::::::::::: {#integration-with-utils-namespace .section}
## [4.21.2. ]{.section-number}Integration with utils namespace[](#integration-with-utils-namespace "Link to this heading"){.headerlink}

Several utility functions in the [`utils`{.docutils .literal .notranslate}]{.pre} namespace work with type labels and interact with the LabelMap class:

- [[`utils::is_type()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils7is_typeERKNSt6stringE "LAMMPS_NS::utils::is_type"){.reference .internal} - Validates whether a string is a valid type label.

- [[`utils::expand_type()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS5utils11expand_typeEPKciRKNSt6stringEiP6LAMMPS "LAMMPS_NS::utils::expand_type"){.reference .internal} - Converts a type label string to its numeric equivalent using the LabelMap.

- [[`utils::bounds_typelabel()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4I0EN9LAMMPS_NS5utils16bounds_typelabelEvPKciRKNSt6stringE6bigint6bigintR4TYPER4TYPEP6LAMMPSi "LAMMPS_NS::utils::bounds_typelabel"){.reference .internal} - Extended version of [`utils::bounds()`{.docutils .literal .notranslate}]{.pre} that accepts type labels in addition to numeric ranges. Uses [`expand_type()`{.docutils .literal .notranslate}]{.pre} internally to convert labels to numeric bounds before processing.

These functions enable seamless integration of type labels throughout LAMMPS, allowing commands that accept type specifications to work with both numeric indices and symbolic labels. Below are some code examples.

::::: {#finding-types-from-labels-and-vice-versa .section}
### Finding types from labels and vice versa[](#finding-types-from-labels-and-vice-versa "Link to this heading"){.headerlink}

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "label_map.h"
    #include "atom.h"

    // assuming this code is used inside a class that is derived from LAMMPS_NS::Pointers
    LabelMap *lmap = atom->lmap;

    // Forward lookup: Get numeric type from label
    int ctype = lmap->find_type("C", Atom::ATOM);    // Returns atom type for "C"
    int htype = lmap->find_type("H", Atom::ATOM);    // Returns atom type for "H"
    int missing = lmap->find_type("X", Atom::ATOM);  // Returns -1 (not found)

    // Reverse lookup: Get label from numeric type
    const std::string &label1 = lmap->find_label(1, Atom::ATOM);  // Returns label for type 1
    const std::string &label2 = lmap->find_label(2, Atom::BOND);  // Returns bond label for type 2

    // Check if all types have labels
    bool complete = lmap->is_complete(Atom::ATOM);  // Returns true if all atom types labeled
:::
::::
:::::

::::: {#inferring-bonded-types-from-atom-types .section}
### Inferring bonded types from atom types[](#inferring-bonded-types-from-atom-types "Link to this heading"){.headerlink}

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "label_map.h"
    #include "atom.h"

    LabelMap *lmap = atom->lmap;

    // Assume we have: labelmap atom 1 C 2 H 3 N
    // And: labelmap bond 1 C-H 2 C-C 3 C-N

    // Infer bond type from numeric atom types
    int bt1 = lmap->infer_bondtype(1, 2);  // Returns 1 (C-H bond)
    int bt2 = lmap->infer_bondtype(1, 1);  // Returns 2 (C-C bond)
    int bt3 = lmap->infer_bondtype(3, 1);  // Returns 3 (C-N bond, symmetric match)

    // Infer bond type from atom type labels (handles symmetry automatically)
    int bt4 = lmap->infer_bondtype({"C", "H"});  // Returns 1 (C-H)
    int bt5 = lmap->infer_bondtype({"H", "C"});  // Returns 1 (symmetric match)
    int bt6 = lmap->infer_bondtype({"C", "N"});  // Returns 3 (C-N)
:::
::::
:::::

::::: {#validating-and-expanding-type-labels .section}
### Validating and expanding type labels[](#validating-and-expanding-type-labels "Link to this heading"){.headerlink}

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "utils.h"
    #include "lammps.h"

    using namespace LAMMPS_NS;

    LAMMPS *lmp = /* ... */;

    // Validate type label strings
    int result1 = utils::is_type("C");     // Returns 1 (valid label)
    int result2 = utils::is_type("123");   // Returns 0 (numeric type)
    int result3 = utils::is_type("*");     // Returns -1 (invalid - starts with *)
    int result4 = utils::is_type("C H");   // Returns -1 (invalid - contains whitespace)

    // Convert type label to numeric string
    char *numstr = utils::expand_type(FLERR, "C", Atom::ATOM, lmp);
    if (numstr) {
        // Use the numeric type string
        delete[] numstr;  // Must delete after use
    }

    // Convert type label to integer
    int type = utils::expand_type_int(FLERR, "C", Atom::ATOM, lmp, true);
    // The 'true' argument enables range verification

    // Use bounds_typelabel for ranges with label support
    int lo, hi;
    utils::bounds_typelabel(FLERR, "C:H", 1, 10, lo, hi, lmp, Atom::ATOM);
    // Expands "C:H" to numeric range, e.g., "1:2" -> lo=1, hi=2
:::
::::
:::::
::::::::::::

------------------------------------------------------------------------

::: {#labelmap-class-reference .section}
## [4.21.3. ]{.section-number}LabelMap class reference[](#labelmap-class-reference "Link to this heading"){.headerlink}

[]{#_CPPv3N9LAMMPS_NS8LabelMapE}[]{#_CPPv2N9LAMMPS_NS8LabelMapE}[]{#LAMMPS_NS::LabelMap}[]{#classLAMMPS__NS_1_1LabelMap .target}[[class]{.pre}]{.k}[ ]{.w}[[[LabelMap]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[:]{.pre}]{.p}[ ]{.w}[[protected]{.pre}]{.k}[ ]{.w}[[[Pointers]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS8PointersE "LAMMPS_NS::Pointers"){.reference .internal}[](#_CPPv4N9LAMMPS_NS8LabelMapE "Link to this definition"){.headerlink}\

:   Manage type labels for atoms, bonds, angles, dihedrals, and impropers.

    The [[LabelMap]{.std .std-ref}](#classLAMMPS__NS_1_1LabelMap){.reference .internal} class provides functionality to map between string labels and numeric type indices for atoms, bonds, angles, dihedrals, and impropers in [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal}. This enables users to reference types by symbolic names (e.g., "C", "H", "C-H") instead of numeric indices, improving readability and maintainability of input scripts.

    Type labels for bonded interactions *may* (but are not required to) use a hyphen-delimited format indicating the types of the constituent atoms. Examples:

    - Bond types: "atom1-atom2" (e.g., "C-H", "N-O")

    - Angle types: "atom1-atom2-atom3" (e.g., "H-C-H", "C-N-C")

    - Dihedral types: "atom1-atom2-atom3-atom4" (e.g., "C-C-N-H")

    - Improper types: "atom1-atom2-atom3-atom4" (e.g., "C-N-C-C")

    The class supports bidirectional lookup (label \<-\> type) and can infer bonded interaction types from constituent atom types when using a hyphen-delimited format convention.

    ::: {.breathe-sectiondef .docutils .container}
    Interaction type inference from hyphen-delimited labels

    These methods infer bonded interaction types (bonds, angles, dihedrals, impropers) from constituent atom types using a hyphen-delimited format. This requires that type labels for bonded interactions were entered following this convention. The inference functions consider the symmetry of the interaction and thus atom types may be swapped accordingly and the bonded type will still be matched.

    []{#_CPPv3N9LAMMPS_NS8LabelMap14infer_bondtypeEii}[]{#_CPPv2N9LAMMPS_NS8LabelMap14infer_bondtypeEii}[]{#LAMMPS_NS::LabelMap::infer_bondtype__i.i}[]{#classLAMMPS__NS_1_1LabelMap_1a1d31a67467cd8c93c332f05d33537054 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[infer_bondtype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[atype1]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[atype2]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap14infer_bondtypeEii "Link to this definition"){.headerlink}\

    :   Infer bond type from two numeric atom types

        Look up or create a bond type from two atom type indices by constructing a hyphen-delimited label (e.g., "C-H") and searching the bond type labels.

        Parameters[:]{.colon}

        :   - **atype1** -- First atom type index

            - **atype2** -- Second atom type index

        Returns[:]{.colon}

        :   Bond type index if types match in the specified order, negative bond type index if types match in reverse order, 0 if there is no match found

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap14infer_bondtypeERKNSt6vectorINSt6stringEEE}[]{#_CPPv2N9LAMMPS_NS8LabelMap14infer_bondtypeERKNSt6vectorINSt6stringEEE}[]{#LAMMPS_NS::LabelMap::infer_bondtype__std::vector:ss:CR}[]{#classLAMMPS__NS_1_1LabelMap_1aa4fb228e995cd03efbe2b57ec25131d1 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[infer_bondtype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[labels]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap14infer_bondtypeERKNSt6vectorINSt6stringEEE "Link to this definition"){.headerlink}\

    :   Infer bond type from atom type labels

        This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

        Look up a bond type from two atom type labels.

        Parameters[:]{.colon}

        :   **labels** -- Vector of two atom type label strings

        Returns[:]{.colon}

        :   Bond type index if types match in the specified order, negative bond type index if types match in reverse order, 0 if there is no match found

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap15infer_angletypeEiii}[]{#_CPPv2N9LAMMPS_NS8LabelMap15infer_angletypeEiii}[]{#LAMMPS_NS::LabelMap::infer_angletype__i.i.i}[]{#classLAMMPS__NS_1_1LabelMap_1a4d4d6f9cb0d9131f82d804866625bc21 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[infer_angletype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[atype1]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[atype2]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[atype3]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap15infer_angletypeEiii "Link to this definition"){.headerlink}\

    :   Infer angle type from three numeric atom types

        Look up or create an angle type from three atom type indices by constructing a hyphen-delimited label (e.g., "H1-C1-H2").

        Parameters[:]{.colon}

        :   - **atype1** -- First atom type index

            - **atype2** -- Second atom type index (center atom)

            - **atype3** -- Third atom type index

        Returns[:]{.colon}

        :   Angle type index if types match in the specified order, negative angle type index if types match in reverse order, 0 if there is no match found

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap15infer_angletypeERKNSt6vectorINSt6stringEEE}[]{#_CPPv2N9LAMMPS_NS8LabelMap15infer_angletypeERKNSt6vectorINSt6stringEEE}[]{#LAMMPS_NS::LabelMap::infer_angletype__std::vector:ss:CR}[]{#classLAMMPS__NS_1_1LabelMap_1a623c7a0d83b8d4611a7505017bab578d .target}[[int]{.pre}]{.kt}[ ]{.w}[[[infer_angletype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[labels]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap15infer_angletypeERKNSt6vectorINSt6stringEEE "Link to this definition"){.headerlink}\

    :   Infer angle type from three atom type labels

        This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

        Look up an angle type from three atom type labels.

        Parameters[:]{.colon}

        :   **labels** -- Vector of three atom type label strings

        Returns[:]{.colon}

        :   Angle type index if types match in the specified order, negative angle type index if types match in reverse order, 0 if there is no match found

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap18infer_dihedraltypeEiiii}[]{#_CPPv2N9LAMMPS_NS8LabelMap18infer_dihedraltypeEiiii}[]{#LAMMPS_NS::LabelMap::infer_dihedraltype__i.i.i.i}[]{#classLAMMPS__NS_1_1LabelMap_1a42cc2e82f160256f1fa2a41ee60e64c5 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[infer_dihedraltype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[atype1]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[atype2]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[atype3]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[atype4]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap18infer_dihedraltypeEiiii "Link to this definition"){.headerlink}\

    :   Infer dihedral type from four numeric atom types

        Look up a dihedral type from four atom type indices by constructing a hyphen-delimited label (e.g., "C-C-N-H").

        Parameters[:]{.colon}

        :   - **atype1** -- First atom type index

            - **atype2** -- Second atom type index

            - **atype3** -- Third atom type index

            - **atype4** -- Fourth atom type index

        Returns[:]{.colon}

        :   Dihedral type index if types match in the specified order, negative dihedral type index if types match in reverse order, 0 if there is no match found

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap18infer_dihedraltypeERKNSt6vectorINSt6stringEEE}[]{#_CPPv2N9LAMMPS_NS8LabelMap18infer_dihedraltypeERKNSt6vectorINSt6stringEEE}[]{#LAMMPS_NS::LabelMap::infer_dihedraltype__std::vector:ss:CR}[]{#classLAMMPS__NS_1_1LabelMap_1ae8776bc2c1e1580977286d129a3fb252 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[infer_dihedraltype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[labels]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap18infer_dihedraltypeERKNSt6vectorINSt6stringEEE "Link to this definition"){.headerlink}\

    :   Infer dihedral type from atom type labels

        This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

        Look up a dihedral type from four atom type labels.

        Parameters[:]{.colon}

        :   **labels** -- Vector of four atom type label strings

        Returns[:]{.colon}

        :   Dihedral type index if types match in the specified order, negative dihedral type index if types match in reverse order, 0 if there is no match found

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap18infer_impropertypeEiiiiPNSt5arrayIiXL4EEEE}[]{#_CPPv2N9LAMMPS_NS8LabelMap18infer_impropertypeEiiiiPNSt5arrayIiX4EEE}[]{#LAMMPS_NS::LabelMap::infer_impropertype__i.i.i.i.std::array:i.4:P}[]{#classLAMMPS__NS_1_1LabelMap_1a41f642fdb354910f584acacfbd8a9b7d .target}[[int]{.pre}]{.kt}[ ]{.w}[[[infer_impropertype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[atype1]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[atype2]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[atype3]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[atype4]{.pre}]{.n .sig-param}, [[std]{.pre}]{.n}[[::]{.pre}]{.p}[[array]{.pre}]{.n}[[\<]{.pre}]{.p}[[int]{.pre}]{.kt}[[,]{.pre}]{.p}[ ]{.w}[[4]{.pre}]{.m}[[\>]{.pre}]{.p}[ ]{.w}[[\*]{.pre}]{.p}[[iorder]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap18infer_impropertypeEiiiiPNSt5arrayIiXL4EEEE "Link to this definition"){.headerlink}\

    :   Infer improper type from four numeric atom types

        Look up an improper type from four atom type indices by constructing a hyphen-delimited label (e.g., "C-N-C-C").

        Parameters[:]{.colon}

        :   - **atype1** -- First atom type index (center atom)

            - **atype2** -- Second atom type index

            - **atype3** -- Third atom type index

            - **atype4** -- Fourth atom type index

            - **iorder** -- Order in which types were matched to improper type label

        Returns[:]{.colon}

        :   Improper type index if types match in the specified order, negative improper type index if types match but different order, 0 if there is no match found

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap18infer_impropertypeERKNSt6vectorINSt6stringEEEPNSt5arrayIiXL4EEEE}[]{#_CPPv2N9LAMMPS_NS8LabelMap18infer_impropertypeERKNSt6vectorINSt6stringEEEPNSt5arrayIiX4EEE}[]{#LAMMPS_NS::LabelMap::infer_impropertype__std::vector:ss:CR.std::array:i.4:P}[]{#classLAMMPS__NS_1_1LabelMap_1a3921f63b6b2e5a1185838709f124f1ed .target}[[int]{.pre}]{.kt}[ ]{.w}[[[infer_impropertype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[labels]{.pre}]{.n .sig-param}, [[std]{.pre}]{.n}[[::]{.pre}]{.p}[[array]{.pre}]{.n}[[\<]{.pre}]{.p}[[int]{.pre}]{.kt}[[,]{.pre}]{.p}[ ]{.w}[[4]{.pre}]{.m}[[\>]{.pre}]{.p}[ ]{.w}[[\*]{.pre}]{.p}[[iorder]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap18infer_impropertypeERKNSt6vectorINSt6stringEEEPNSt5arrayIiXL4EEEE "Link to this definition"){.headerlink}\

    :   Infer improper type from atom type labels

        This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

        Look up an improper type from four atom type labels.

        Parameters[:]{.colon}

        :   - **labels** -- Vector of four atom type label strings

            - **iorder** -- Order in which types were matched to improper type label

        Returns[:]{.colon}

        :   Improper type index if types match in the specified order, negative improper type index if types match but different order, 0 if there is no match found
    :::

    ::: {.breathe-sectiondef .docutils .container}
    I/O methods for label map persistence

    []{#_CPPv3N9LAMMPS_NS8LabelMap10write_dataEP4FILE}[]{#_CPPv2N9LAMMPS_NS8LabelMap10write_dataEP4FILE}[]{#LAMMPS_NS::LabelMap::write_data__FILEP}[]{#classLAMMPS__NS_1_1LabelMap_1a545fee3a22edfdf5984e7a8be7870ae5 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[write_data]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap10write_dataEP4FILE "Link to this definition"){.headerlink}\

    :   Write label map to data file

        Output all type labels as sections to a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} data file.

        Parameters[:]{.colon}

        :   **fp** -- File pointer for writing

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap12read_restartEP4FILE}[]{#_CPPv2N9LAMMPS_NS8LabelMap12read_restartEP4FILE}[]{#LAMMPS_NS::LabelMap::read_restart__FILEP}[]{#classLAMMPS__NS_1_1LabelMap_1a72e9ad229d81013b6687d68ce6ee5ae5 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[read_restart]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap12read_restartEP4FILE "Link to this definition"){.headerlink}\

    :   Read label map from restart file

        Restore label map data from a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} restart file.

        Parameters[:]{.colon}

        :   **fp** -- File pointer for reading

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap13write_restartEP4FILE}[]{#_CPPv2N9LAMMPS_NS8LabelMap13write_restartEP4FILE}[]{#LAMMPS_NS::LabelMap::write_restart__FILEP}[]{#classLAMMPS__NS_1_1LabelMap_1ac58a4d1355dd2ea326da5ac463e9f2eb .target}[[void]{.pre}]{.kt}[ ]{.w}[[[write_restart]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[[\*]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap13write_restartEP4FILE "Link to this definition"){.headerlink}\

    :   Write label map to restart file

        Save label map data to a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} restart file for later restoration.

        Parameters[:]{.colon}

        :   **fp** -- File pointer for writing

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap12check_labelsEv}[]{#_CPPv2N9LAMMPS_NS8LabelMap12check_labelsEv}[]{#LAMMPS_NS::LabelMap::check_labels}[]{#classLAMMPS__NS_1_1LabelMap_1ad6ac365b4cff35672be391325aa2ed02 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[check_labels]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap12check_labelsEv "Link to this definition"){.headerlink}\

    :   Check if type labels are self-consistent.
    :::

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS8LabelMap8LabelMapEP6LAMMPSiiiii}[]{#_CPPv2N9LAMMPS_NS8LabelMap8LabelMapEP6LAMMPSiiiii}[]{#LAMMPS_NS::LabelMap::LabelMap__LAMMPSP.i.i.i.i.i}[]{#classLAMMPS__NS_1_1LabelMap_1a20c994169256ef686e917e04b95311b2 .target}[[[LabelMap]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[LAMMPS]{.pre}]{.n}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmp]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[natomtypes]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[nbondtypes]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[nangletypes]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[ndihedraltypes]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[nimpropertypes]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap8LabelMapEP6LAMMPSiiiii "Link to this definition"){.headerlink}\

    :   Construct a [[LabelMap]{.std .std-ref}](#classLAMMPS__NS_1_1LabelMap){.reference .internal} instance

        Parameters[:]{.colon}

        :   - **lmp** -- Pointer to [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

            - **natomtypes** -- Number of atom types in map

            - **nbondtypes** -- Number of bond types in map

            - **nangletypes** -- Number of angle types in map

            - **ndihedraltypes** -- Number of dihedral types in map

            - **nimpropertypes** -- Number of improper types in map

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap11modify_lmapEiPPc}[]{#_CPPv2N9LAMMPS_NS8LabelMap11modify_lmapEiPPc}[]{#LAMMPS_NS::LabelMap::modify_lmap__i.cPP}[]{#classLAMMPS__NS_1_1LabelMap_1a71dbe208a3426c805b11d01ccfb074c4 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[modify_lmap]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[narg]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[arg]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap11modify_lmapEiPPc "Link to this definition"){.headerlink}\

    :   Process labelmap command from input script

        Add or modify type label mappings from the LAMMPS [[labelmap]{.doc}]labelmap.md){.reference .internal} input command.

        Parameters[:]{.colon}

        :   - **narg** -- Number of arguments

            - **arg** -- Array of argument strings

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap10merge_lmapEP8LabelMapi}[]{#_CPPv2N9LAMMPS_NS8LabelMap10merge_lmapEP8LabelMapi}[]{#LAMMPS_NS::LabelMap::merge_lmap__LabelMapP.i}[]{#classLAMMPS__NS_1_1LabelMap_1a07f14ed7ef2056a57272c02b22755a0a .target}[[void]{.pre}]{.kt}[ ]{.w}[[[merge_lmap]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[LabelMap]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS8LabelMapE "LAMMPS_NS::LabelMap"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmap]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[mode]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap10merge_lmapEP8LabelMapi "Link to this definition"){.headerlink}\

    :   Copy another [[LabelMap]{.std .std-ref}](#classLAMMPS__NS_1_1LabelMap){.reference .internal} into this one

        Merge type labels from another LabelMap instance into the current one. Currently used when combining data from multiple sources with [[read_data add]{.doc}]read_data.md){.reference .internal} or when replicating the system with [[replicate]{.doc}]replicate.md){.reference .internal}.

        Parameters[:]{.colon}

        :   - **lmap** -- Pointer to source [[LabelMap]{.std .std-ref}](#classLAMMPS__NS_1_1LabelMap){.reference .internal}

            - **mode** -- Merge mode flag

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap16create_lmap2lmapEP8LabelMapi}[]{#_CPPv2N9LAMMPS_NS8LabelMap16create_lmap2lmapEP8LabelMapi}[]{#LAMMPS_NS::LabelMap::create_lmap2lmap__LabelMapP.i}[]{#classLAMMPS__NS_1_1LabelMap_1a339071259a22235d777ff21e3cf38196 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[create_lmap2lmap]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[LabelMap]{.pre}]{.n}](#_CPPv4N9LAMMPS_NS8LabelMapE "LAMMPS_NS::LabelMap"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[lmap]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[mode]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap16create_lmap2lmapEP8LabelMapi "Link to this definition"){.headerlink}\

    :   Create index mapping between two LabelMaps

        Build a mapping structure (lmap2lmap) that translates type indices from another [[LabelMap]{.std .std-ref}](#classLAMMPS__NS_1_1LabelMap){.reference .internal} to the current one based on matching labels.

        Parameters[:]{.colon}

        :   - **lmap** -- Pointer to source [[LabelMap]{.std .std-ref}](#classLAMMPS__NS_1_1LabelMap){.reference .internal}

            - **mode** -- Mapping mode flag

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS8LabelMap9find_typeERKNSt6stringEi}[]{#_CPPv2NK9LAMMPS_NS8LabelMap9find_typeERKNSt6stringEi}[]{#LAMMPS_NS::LabelMap::find_type__ssCR.iC}[]{#classLAMMPS__NS_1_1LabelMap_1a7bc199c8fa73144db58679aafe795686 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[find_type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[&]{.pre}]{.p}, [[int]{.pre}]{.kt}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS8LabelMap9find_typeERKNSt6stringEi "Link to this definition"){.headerlink}\

    :   Find numeric type from type label

        Look up the numeric type index corresponding to a type label string.

        Parameters[:]{.colon}

        :   - **mylabel** -- Type label string to search for

            - **mode** -- Type category: Atom::ATOM, Atom::BOND, Atom::ANGLE, Atom::DIHEDRAL, or Atom::IMPROPER

        Returns[:]{.colon}

        :   Numeric type index (1-based), or -1 if not found

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS8LabelMap10find_labelEii}[]{#_CPPv2NK9LAMMPS_NS8LabelMap10find_labelEii}[]{#LAMMPS_NS::LabelMap::find_label__i.iC}[]{#classLAMMPS__NS_1_1LabelMap_1a72fc9131a3738a568dab47e7dcc27508 .target}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[[find_label]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}, [[int]{.pre}]{.kt}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS8LabelMap10find_labelEii "Link to this definition"){.headerlink}\

    :   Find type label from numeric type

        Reverse lookup: retrieve the type label string for a given numeric type.

        Parameters[:]{.colon}

        :   - **i** -- Numeric type index (1-based)

            - **mode** -- Type category: Atom::ATOM, Atom::BOND, Atom::ANGLE, Atom::DIHEDRAL, or Atom::IMPROPER

        Returns[:]{.colon}

        :   Reference to type label string, or empty string if not found

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS8LabelMap11is_completeEi}[]{#_CPPv2NK9LAMMPS_NS8LabelMap11is_completeEi}[]{#LAMMPS_NS::LabelMap::is_complete__iC}[]{#classLAMMPS__NS_1_1LabelMap_1a474bff4af23fa64ef222e403ebdf380a .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[is_complete]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS8LabelMap11is_completeEi "Link to this definition"){.headerlink}\

    :   Check if all types have assigned labels

        Verify that every type in the specified category has a corresponding label.

        Parameters[:]{.colon}

        :   **mode** -- Type category: Atom::ATOM, Atom::BOND, Atom::ANGLE, Atom::DIHEDRAL, or Atom::IMPROPER

        Returns[:]{.colon}

        :   True if all types have labels, false otherwise

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS8LabelMap15parse_typelabelEiRKNSt6stringERNSt6vectorINSt6stringEEE}[]{#_CPPv2N9LAMMPS_NS8LabelMap15parse_typelabelEiRKNSt6stringERNSt6vectorINSt6stringEEE}[]{#LAMMPS_NS::LabelMap::parse_typelabel__i.ssCR.std::vector:ss:R}[]{#classLAMMPS__NS_1_1LabelMap_1a9db42796c457dc32ca98236f48d046f1 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[parse_typelabel]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[ntypes]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[label]{.pre}]{.n .sig-param}, [[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[types]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8LabelMap15parse_typelabelEiRKNSt6stringERNSt6vectorINSt6stringEEE "Link to this definition"){.headerlink}\

    :   Parse hyphen-delimited type label into components

        Split a hyphen-delimited label (e.g., "C-N-H") into individual type strings. Validates that the number of components matches the expected count.

        Parameters[:]{.colon}

        :   - **ntypes** -- Expected number of components

            - **label** -- Hyphen-delimited label string

            - **types** -- **\[out\]** Output vector to store component strings

        Returns[:]{.colon}

        :   0 on success, -1 if component count doesn't match ntypes
    :::

    ::: {.breathe-sectiondef .docutils .container}
    Public Members

    []{#_CPPv3N9LAMMPS_NS8LabelMap9checkflagE}[]{#_CPPv2N9LAMMPS_NS8LabelMap9checkflagE}[]{#LAMMPS_NS::LabelMap::checkflag__i}[]{#classLAMMPS__NS_1_1LabelMap_1af4b8d55bfb3e2c0c78a7f5fa14e78334 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[checkflag]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS8LabelMap9checkflagE "Link to this definition"){.headerlink}\

    :   Flag to check for self-consistent type labels.
    :::
:::
:::::::::::::::

------------------------------------------------------------------------

::::::: {#memory-pool-classes .section}
# [4.22. ]{.section-number}Memory pool classes[](#memory-pool-classes "Link to this heading"){.headerlink}

The memory pool classes are used for cases where otherwise many small memory allocations would be needed and where the data would be either all used or all freed. One example for that is the storage of neighbor lists. The memory management strategy is based on the assumption that allocations will be in chunks of similar sizes. The allocation is then not done per individual call for a reserved chunk of memory, but for a "page" that can hold multiple chunks of data. A parameter for the maximum chunk size must be provided, as that is used to determine whether a new page of memory must be used.

The [[`MyPage`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4I0EN9LAMMPS_NS6MyPageE "LAMMPS_NS::MyPage"){.reference .internal} class offers two ways to reserve a chunk: 1) with [[`MyPage::get()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS6MyPage3getEi "LAMMPS_NS::MyPage::get"){.reference .internal} the chunk size needs to be known in advance, 2) with [[`MyPage::vget()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS6MyPage4vgetEv "LAMMPS_NS::MyPage::vget"){.reference .internal} a pointer to the next chunk is returned, but its size is registered later with [[`MyPage::vgot()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS6MyPage4vgotEi "LAMMPS_NS::MyPage::vgot"){.reference .internal}.

:::::: {#id8 .literal-block-wrapper .docutils .container}
::: code-block-caption
[Example of using [[`MyPage`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}](#_CPPv4I0EN9LAMMPS_NS6MyPageE "LAMMPS_NS::MyPage"){.reference .internal}]{.caption-text}[](#id8 "Link to this code"){.headerlink}
:::

:::: {.highlight-c++ .notranslate}
::: highlight
       #include "my_page.h"
       using namespace LAMMPS_NS;

       MyPage<double> *dpage = new MyPage<double>;
       // max size of chunk: 256, size of page: 10240 doubles (=81920 bytes)
       dpage->init(256,10240);

       double **build_some_lists(int num)
       {
           dpage->reset();
           double **dlist = new double*[num];
           for (int i=0; i < num; ++i) {
               double *dptr = dpage.vget();
               int jnum = 0;
               for (int j=0; j < jmax; ++j) {
                   // compute some dvalue for eligible loop index j
                   dptr[j] = dvalue;
                   ++jnum;
               }
               if (dpage.status() != 0) {
                   // handle out of memory or jnum too large errors
               }
               dpage.vgot(jnum);
               dlist[i] = dptr;
           }
           return dlist;
       }
:::
::::
::::::

------------------------------------------------------------------------

[]{#_CPPv3I0EN9LAMMPS_NS6MyPageE}[]{#_CPPv2I0EN9LAMMPS_NS6MyPageE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#classLAMMPS__NS_1_1MyPage .target}[[class]{.pre}]{.k}[ ]{.w}[[[MyPage]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4I0EN9LAMMPS_NS6MyPageE "Link to this definition"){.headerlink}\

:   Templated class for storing chunks of datums in pages.

    The size of the chunk may vary from call to call, but must be less or equal than the *maxchunk* setting. The chunks are not returnable like with malloc() (i.e. you cannot call free() on them individually). One can only reset and start over. The purpose of this class is to replace many small memory allocations via malloc() with a few large ones. Since the pages are never freed until the class is re-initialized, they can be re-used without having to re-allocate them by calling the [[reset()]{.std .std-ref}](#classLAMMPS__NS_1_1MyPage_1ad20897c5c8bd47f5d4005989bead0e55){.reference .internal} method.

    The settings *maxchunk*, *pagesize*, and *pagedelta* control the memory allocation strategy. The *maxchunk* value represents the largest number of items per chunk allowed; using more will trigger an error. If there is less space than *maxchunk* left on the current page, a new page is allocated for the next chunk. The *pagesize* value represents how many items can fit on a single page. It should have space for multiple chunks of size *maxchunk*. The combination of these two parameters determines how much memory is wasted by either switching to the next page too soon or allocating too large pages that never get fully used. The *pagedelta* parameter determines how many pages are allocated in one go. In combination with the *pagesize* setting, this determines how often blocks of memory get allocated (fewer allocations will result in faster execution).

    ::: {.admonition .note}
    Note

    This is a template class with explicit instantiation. If the class is used with a new data type, a new explicit instantiation may need to be added at the end of the file [`src/my_page.cpp`{.docutils .literal .notranslate}]{.pre} to avoid symbol lookup errors.
    :::

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS6MyPage6MyPageEv}[]{#_CPPv2N9LAMMPS_NS6MyPage6MyPageEv}[]{#LAMMPS_NS::MyPage::MyPage}[]{#classLAMMPS__NS_1_1MyPage_1aaea419ba80ccc8fc23bcfd0870c1e875 .target}[[[MyPage]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS6MyPage6MyPageEv "Link to this definition"){.headerlink}\

    :   Create a class instance

        Need to call [[init()]{.std .std-ref}](#classLAMMPS__NS_1_1MyPage_1a381c748265a923272bd332b3905a9891){.reference .internal} before use to define allocation settings

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS6MyPage4initEiii}[]{#_CPPv2N9LAMMPS_NS6MyPage4initEiii}[]{#LAMMPS_NS::MyPage::init__i.i.i}[]{#classLAMMPS__NS_1_1MyPage_1a381c748265a923272bd332b3905a9891 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[init]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[user_maxchunk]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}, [[int]{.pre}]{.kt}[ ]{.w}[[user_pagesize]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1024]{.pre}]{.m}, [[int]{.pre}]{.kt}[ ]{.w}[[user_pagedelta]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS6MyPage4initEiii "Link to this definition"){.headerlink}\

    :   (Re-)initialize the set of pages and allocation parameters.

        This also frees all previously allocated storage and allocates the first page(s).

        Parameters[:]{.colon}

        :   - **user_maxchunk** -- Maximum allowed number of items for one chunk

            - **user_pagesize** -- Number of items on a single memory page

            - **user_pagedelta** -- Number of pages to allocate with one malloc

        Returns[:]{.colon}

        :   1 if there were invalid parameters, 2 if there was an allocation error or 0 if successful

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS6MyPage3getEi}[]{#_CPPv2N9LAMMPS_NS6MyPage3getEi}[]{#LAMMPS_NS::MyPage::get__i}[]{#classLAMMPS__NS_1_1MyPage_1ac0fe0e7127a43512b203e64202414cab .target}[[[T]{.pre}]{.n}](#_CPPv4I0EN9LAMMPS_NS6MyPageE "LAMMPS_NS::MyPage::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[[get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS6MyPage3getEi "Link to this definition"){.headerlink}\

    :   Pointer to location that can store N items.

        This will allocate more pages as needed. If the parameter *N* is larger than the *maxchunk* setting, an error is flagged.

        Parameters[:]{.colon}

        :   **n** -- number of items for which storage is requested

        Returns[:]{.colon}

        :   memory location or null pointer, if error or allocation failed

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS6MyPage4vgetEv}[]{#_CPPv2N9LAMMPS_NS6MyPage4vgetEv}[]{#LAMMPS_NS::MyPage::vget}[]{#classLAMMPS__NS_1_1MyPage_1adc48a701d14a6bd5d8a1f48a561c4b06 .target}[[inline]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#_CPPv4I0EN9LAMMPS_NS6MyPageE "LAMMPS_NS::MyPage::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[[vget]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS6MyPage4vgetEv "Link to this definition"){.headerlink}\

    :   Get pointer to location that can store *maxchunk* items.

        This will return the same pointer as the previous call to this function unless [[vgot()]{.std .std-ref}](#classLAMMPS__NS_1_1MyPage_1a8b3b7dc16eae4b0445e534a37eb85806){.reference .internal} is called afterwards to record how many items of the chunk were actually used.

        Returns[:]{.colon}

        :   pointer to chunk of memory or null pointer if run out of memory

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS6MyPage4vgotEi}[]{#_CPPv2N9LAMMPS_NS6MyPage4vgotEi}[]{#LAMMPS_NS::MyPage::vgot__i}[]{#classLAMMPS__NS_1_1MyPage_1a8b3b7dc16eae4b0445e534a37eb85806 .target}[[inline]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[vgot]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS6MyPage4vgotEi "Link to this definition"){.headerlink}\

    :   Mark *N* items as used of the chunk reserved with a preceding call to [[vget()]{.std .std-ref}](#classLAMMPS__NS_1_1MyPage_1adc48a701d14a6bd5d8a1f48a561c4b06){.reference .internal}.

        This will advance the internal pointer inside the current memory page. It is not necessary to call this function for *N* = 0, implying the reserved storage was not used. A following call to [[vget()]{.std .std-ref}](#classLAMMPS__NS_1_1MyPage_1adc48a701d14a6bd5d8a1f48a561c4b06){.reference .internal} will then reserve the same location again. It is an error if *N* \> *maxchunk*.

        Parameters[:]{.colon}

        :   **n** -- Number of items used in previously reserved chunk

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS6MyPage5resetEv}[]{#_CPPv2N9LAMMPS_NS6MyPage5resetEv}[]{#LAMMPS_NS::MyPage::reset}[]{#classLAMMPS__NS_1_1MyPage_1ad20897c5c8bd47f5d4005989bead0e55 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[reset]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS6MyPage5resetEv "Link to this definition"){.headerlink}\

    :   Reset state of memory pool without freeing any memory

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS6MyPage4sizeEv}[]{#_CPPv2NK9LAMMPS_NS6MyPage4sizeEv}[]{#LAMMPS_NS::MyPage::sizeC}[]{#classLAMMPS__NS_1_1MyPage_1ac3fe9e82d5f4f1d55a5c104a2a5d37a6 .target}[[inline]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[[size]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS6MyPage4sizeEv "Link to this definition"){.headerlink}\

    :   Return total size of allocated pages

        Returns[:]{.colon}

        :   total storage used in bytes

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS6MyPage6statusEv}[]{#_CPPv2NK9LAMMPS_NS6MyPage6statusEv}[]{#LAMMPS_NS::MyPage::statusC}[]{#classLAMMPS__NS_1_1MyPage_1a92d2adf8350ab6a66718eab4a990dffb .target}[[inline]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[[status]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS6MyPage6statusEv "Link to this definition"){.headerlink}\

    :   Return error status

        Returns[:]{.colon}

        :   0 if no error, 1 requested chunk size \> maxchunk, 2 if malloc failed
    :::

<!-- -->

[]{#_CPPv3I0EN9LAMMPS_NS11MyPoolChunkE}[]{#_CPPv2I0EN9LAMMPS_NS11MyPoolChunkE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#classLAMMPS__NS_1_1MyPoolChunk .target}[[class]{.pre}]{.k}[ ]{.w}[[[MyPoolChunk]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4I0EN9LAMMPS_NS11MyPoolChunkE "Link to this definition"){.headerlink}\

:   Templated class for storing chunks of datums in pages.

    The size of the chunk may vary from call to call between the *minchunk* and *maxchunk* setting. Chunks may be returned to the pool for re-use. Chunks can be reserved in *nbin* different sizes between *minchunk* and *maxchunk*. The *chunksperpage* setting specifies how many chunks are stored on any page and the *pagedelta* setting determines how many pages are allocated in one go. Pages are never freed, so they can be re-used without re-allocation.

    ::: {.admonition .note}
    Note

    This is a template class with explicit instantiation. If the class is used with a new data type, a new explicit instantiation may need to be added at the end of the file [`src/my_pool_chunk.cpp`{.docutils .literal .notranslate}]{.pre} to avoid symbol lookup errors.
    :::

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS11MyPoolChunk11MyPoolChunkEiiiii}[]{#_CPPv2N9LAMMPS_NS11MyPoolChunk11MyPoolChunkEiiiii}[]{#LAMMPS_NS::MyPoolChunk::MyPoolChunk__i.i.i.i.i}[]{#classLAMMPS__NS_1_1MyPoolChunk_1a60daa98fd41e5ff09753fe55f044b453 .target}[[[MyPoolChunk]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[user_minchunk]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}, [[int]{.pre}]{.kt}[ ]{.w}[[user_maxchunk]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}, [[int]{.pre}]{.kt}[ ]{.w}[[user_nbin]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}, [[int]{.pre}]{.kt}[ ]{.w}[[user_chunkperpage]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1024]{.pre}]{.m}, [[int]{.pre}]{.kt}[ ]{.w}[[user_pagedelta]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MyPoolChunk11MyPoolChunkEiiiii "Link to this definition"){.headerlink}\

    :   Create a class instance and set memory pool parameters

        Parameters[:]{.colon}

        :   - **user_minchunk** -- Minimal chunk size

            - **user_maxchunk** -- Maximal chunk size

            - **user_nbin** -- Number of bins of different chunk sizes

            - **user_chunkperpage** -- Number of chunks per page

            - **user_pagedelta** -- Number of pages to allocate in one go

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS11MyPoolChunkD0Ev}[]{#_CPPv2N9LAMMPS_NS11MyPoolChunkD0Ev}[]{#LAMMPS_NS::MyPoolChunk::~MyPoolChunk}[]{#classLAMMPS__NS_1_1MyPoolChunk_1aa185474081f1f923a35914ed67077e11 .target}[[[\~MyPoolChunk]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MyPoolChunkD0Ev "Link to this definition"){.headerlink}\

    :   Destroy class instance and free all allocated memory

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS11MyPoolChunk3getERi}[]{#_CPPv2N9LAMMPS_NS11MyPoolChunk3getERi}[]{#LAMMPS_NS::MyPoolChunk::get__iR}[]{#classLAMMPS__NS_1_1MyPoolChunk_1a591380d4a3a168110139f35e1d56a3c9 .target}[[[T]{.pre}]{.n}](#_CPPv4I0EN9LAMMPS_NS11MyPoolChunkE "LAMMPS_NS::MyPoolChunk::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[[get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[index]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MyPoolChunk3getERi "Link to this definition"){.headerlink}\

    :   Return pointer/index of unused chunk of size maxchunk

        Parameters[:]{.colon}

        :   **index** -- Index of chunk in memory pool

        Returns[:]{.colon}

        :   Pointer to requested chunk of storage

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS11MyPoolChunk3getEiRi}[]{#_CPPv2N9LAMMPS_NS11MyPoolChunk3getEiRi}[]{#LAMMPS_NS::MyPoolChunk::get__i.iR}[]{#classLAMMPS__NS_1_1MyPoolChunk_1a781c43c8f6e18dcb99c613292a38cc4e .target}[[[T]{.pre}]{.n}](#_CPPv4I0EN9LAMMPS_NS11MyPoolChunkE "LAMMPS_NS::MyPoolChunk::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[[get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[index]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MyPoolChunk3getEiRi "Link to this definition"){.headerlink}\

    :   Return pointer/index of unused chunk of size N

        Parameters[:]{.colon}

        :   - **n** -- Size of chunk

            - **index** -- Index of chunk in memory pool

        Returns[:]{.colon}

        :   Pointer to requested chunk of storage

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS11MyPoolChunk3putEi}[]{#_CPPv2N9LAMMPS_NS11MyPoolChunk3putEi}[]{#LAMMPS_NS::MyPoolChunk::put__i}[]{#classLAMMPS__NS_1_1MyPoolChunk_1acf93b81dd253b533195c20ee85621412 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[put]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[index]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS11MyPoolChunk3putEi "Link to this definition"){.headerlink}\

    :   Put indexed chunk back into memory pool via free list

        Parameters[:]{.colon}

        :   **index** -- Memory chunk index returned by call to [[get()]{.std .std-ref}](#classLAMMPS__NS_1_1MyPoolChunk_1a591380d4a3a168110139f35e1d56a3c9){.reference .internal}

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS11MyPoolChunk4sizeEv}[]{#_CPPv2NK9LAMMPS_NS11MyPoolChunk4sizeEv}[]{#LAMMPS_NS::MyPoolChunk::sizeC}[]{#classLAMMPS__NS_1_1MyPoolChunk_1ac3fe9e82d5f4f1d55a5c104a2a5d37a6 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[size]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS11MyPoolChunk4sizeEv "Link to this definition"){.headerlink}\

    :   Return total size of allocated pages

        Returns[:]{.colon}

        :   total storage used in bytes

    <!-- -->

    []{#_CPPv3NK9LAMMPS_NS11MyPoolChunk6statusEv}[]{#_CPPv2NK9LAMMPS_NS11MyPoolChunk6statusEv}[]{#LAMMPS_NS::MyPoolChunk::statusC}[]{#classLAMMPS__NS_1_1MyPoolChunk_1a92d2adf8350ab6a66718eab4a990dffb .target}[[inline]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[[status]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK9LAMMPS_NS11MyPoolChunk6statusEv "Link to this definition"){.headerlink}\

    :   Return error status

        Returns[:]{.colon}

        :   0 if no error, 1 if invalid input, 2 if malloc() failed, 3 if chunk \> maxchunk
    :::
:::::::

------------------------------------------------------------------------

::: {#eigensolver-functions .section}
# [4.23. ]{.section-number}Eigensolver functions[](#eigensolver-functions "Link to this heading"){.headerlink}

The [`MathEigen`{.docutils .literal .notranslate}]{.pre} sub-namespace of the [`LAMMPS_NS`{.docutils .literal .notranslate}]{.pre} namespace contains functions and classes for eigensolvers. Currently only the [[`jacobi3`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`function`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv4N9MathEigen7jacobi3EPPCKdPdPPdi "MathEigen::jacobi3"){.reference .internal} is used in various places in LAMMPS. That function is built on top of a group of more generic eigensolvers that are maintained in the [`math_eigen_impl.h`{.docutils .literal .notranslate}]{.pre} header file. This header contains the implementation of three template classes:

1.  "Jacobi" calculates all of the eigenvalues and eigenvectors of a dense, symmetric, real matrix.

2.  The "PEigenDense" class only calculates the principal eigenvalue (i.e. the largest or smallest eigenvalue), and its corresponding eigenvector. However it is much more efficient than "Jacobi" when applied to large matrices (larger than 13x13). PEigenDense also can understand complex-valued Hermitian matrices.

3.  The "LambdaLanczos" class is a generalization of "PEigenDense" which can be applied to arbitrary sparse matrices.

The "math_eigen_impl.h" code is an amalgamation of [jacobi_pd](https://github.com/jewettaij/jacobi_pd){.reference .external} by Andrew Jewett at Scripps Research (under CC0-1.0 license) and [Lambda Lanczos](https://github.com/mrcdr/lambda-lanczos){.reference .external} by Yuya Kurebayashi at Tohoku University (under MIT license)

------------------------------------------------------------------------

[]{#_CPPv3N9MathEigen7jacobi3EPPCKdPdPPdi}[]{#_CPPv2N9MathEigen7jacobi3EPPCKdPdPPdi}[]{#MathEigen::jacobi3__doubleCPCP.doubleP.doublePP.i}[]{#math__eigen_8h_1a8089fe07bf0c6b60343f2bcfcde5b3b3 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[MathEigen]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[jacobi3]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[double]{.pre}]{.kt}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[\*]{.pre}]{.p}[[const]{.pre}]{.k}[ ]{.w}[[\*]{.pre}]{.p}[[mat]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[eval]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[evec]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[sort]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[-]{.pre}]{.o}[[1]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9MathEigen7jacobi3EPPCKdPdPPdi "Link to this definition"){.headerlink}\

:   A specialized function which finds the eigenvalues and eigenvectors of a 3x3 matrix (in double \*\* format).

    Parameters[:]{.colon}

    :   - **mat** -- the 3x3 matrix you wish to diagonalize

        - **eval** -- store the eigenvalues here

        - **evec** -- store the eigenvectors here...

        - **sort** -- order eigenvalues and -vectors (-1 decreasing (default), 1 increasing, 0 unsorted)

    Returns[:]{.colon}

    :   0 if eigenvalue calculation converged, 1 if it failed

<!-- -->

[]{#_CPPv3N9MathEigen7jacobi3EAL3E_AL3E_KdPdAL3E_AL3E_di}[]{#_CPPv2N9MathEigen7jacobi3EA3_A3_KdPdA3_A3_di}[]{#MathEigen::jacobi3__doubleCAA.doubleP.doubleAA.i}[]{#math__eigen_8h_1a834124ee73c84149d3974cb7e67bc926 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[MathEigen]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[jacobi3]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[double]{.pre}]{.kt}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[mat]{.pre}]{.n .sig-param}[[\[]{.pre}]{.p}[[3]{.pre}]{.m}[[\]]{.pre}]{.p}[[\[]{.pre}]{.p}[[3]{.pre}]{.m}[[\]]{.pre}]{.p}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[eval]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[evec]{.pre}]{.n .sig-param}[[\[]{.pre}]{.p}[[3]{.pre}]{.m}[[\]]{.pre}]{.p}[[\[]{.pre}]{.p}[[3]{.pre}]{.m}[[\]]{.pre}]{.p}, [[int]{.pre}]{.kt}[ ]{.w}[[sort]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[-]{.pre}]{.o}[[1]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N9MathEigen7jacobi3EAL3E_AL3E_KdPdAL3E_AL3E_di "Link to this definition"){.headerlink}\

:   This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

------------------------------------------------------------------------
:::

::: {#communication-buffer-coding-with-ubuf .section}
[]{#id3}

# [4.24. ]{.section-number}Communication buffer coding with *ubuf*[](#communication-buffer-coding-with-ubuf "Link to this heading"){.headerlink}

LAMMPS uses communication buffers where it collects data from various class instances and then exchanges the data with neighboring subdomains. For simplicity those buffers are defined as [`double`{.docutils .literal .notranslate}]{.pre} buffers and used for doubles and integer numbers. This presents a unique problem when 64-bit integers are used. While the storage needed for a [`double`{.docutils .literal .notranslate}]{.pre} is also 64-bit, it cannot be used by a simple assignment. To get around that limitation, LAMMPS uses the [[`ubuf`{.xref .cpp .cpp-union .docutils .literal .notranslate}]{.pre}](#_CPPv4N9LAMMPS_NS4ubufE "LAMMPS_NS::ubuf"){.reference .internal} union. It is used in the various "pack" and "unpack" functions in the LAMMPS classes to store and retrieve integers that may be 64-bit from the communication buffers.

------------------------------------------------------------------------

[]{#_CPPv3N9LAMMPS_NS4ubufE}[]{#_CPPv2N9LAMMPS_NS4ubufE}[]{#unionLAMMPS__NS_1_1ubuf .target}[[union]{.pre}]{.k}[ ]{.w}[[[ubuf]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS4ubufE "Link to this definition"){.headerlink}\

:   ::: {.docutils .container}
    *#include \<lmptype.h\>*
    :::

    Data structure for packing 32-bit and 64-bit integers into double (communication) buffers

    Using this union avoids aliasing issues by having member types (double, int) referencing the same buffer memory location.

    The explicit constructor for 32-bit integers prevents compilers from (incorrectly) calling the double constructor when storing an int into a double buffer.

    **Usage:**

    :::::: {#id9 .literal-block-wrapper .docutils .container}
    ::: code-block-caption
    [To copy an integer into a double buffer:]{.caption-text}[](#id9 "Link to this code"){.headerlink}
    :::

    :::: {.highlight-c++ .notranslate}
    ::: highlight
        double buf[2];
        int    foo =   1;
        tagint bar = 2<<40;
        buf[1] = ubuf(foo).d;
        buf[2] = ubuf(bar).d;
    :::
    ::::
    ::::::

    :::::: {#id10 .literal-block-wrapper .docutils .container}
    ::: code-block-caption
    [To copy from a double buffer back to an int:]{.caption-text}[](#id10 "Link to this code"){.headerlink}
    :::

    :::: {.highlight-c++ .notranslate}
    ::: highlight
        foo = (int)    ubuf(buf[1]).i;
        bar = (tagint) ubuf(buf[2]).i;
    :::
    ::::
    ::::::

    The typecasts prevent compiler warnings about possible truncation issues.

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N9LAMMPS_NS4ubuf4ubufERKd}[]{#_CPPv2N9LAMMPS_NS4ubuf4ubufERKd}[]{#LAMMPS_NS::ubuf::ubuf__doubleCR}[]{#unionLAMMPS__NS_1_1ubuf_1a5cdd4245af25171a133da99e9808170b .target}[[inline]{.pre}]{.k}[ ]{.w}[[[ubuf]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[arg]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS4ubuf4ubufERKd "Link to this definition"){.headerlink}\

    :   

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS4ubuf4ubufERK7int64_t}[]{#_CPPv2N9LAMMPS_NS4ubuf4ubufERK7int64_t}[]{#LAMMPS_NS::ubuf::ubuf__int64_tCR}[]{#unionLAMMPS__NS_1_1ubuf_1a86bb79057870b1bd9b4f9275e5d929fa .target}[[inline]{.pre}]{.k}[ ]{.w}[[[ubuf]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[int64_t]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[arg]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS4ubuf4ubufERK7int64_t "Link to this definition"){.headerlink}\

    :   

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS4ubuf4ubufERKi}[]{#_CPPv2N9LAMMPS_NS4ubuf4ubufERKi}[]{#LAMMPS_NS::ubuf::ubuf__iCR}[]{#unionLAMMPS__NS_1_1ubuf_1a76e1c4df9fb2687d7f2055f90b08360d .target}[[inline]{.pre}]{.k}[ ]{.w}[[[ubuf]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[arg]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS4ubuf4ubufERKi "Link to this definition"){.headerlink}\

    :   
    :::

    ::: {.breathe-sectiondef .docutils .container}
    Public Members

    []{#_CPPv3N9LAMMPS_NS4ubuf1dE}[]{#_CPPv2N9LAMMPS_NS4ubuf1dE}[]{#LAMMPS_NS::ubuf::d__double}[]{#unionLAMMPS__NS_1_1ubuf_1a873684cefeb665f3d5e6b495de57fc0d .target}[[double]{.pre}]{.kt}[ ]{.w}[[[d]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS4ubuf1dE "Link to this definition"){.headerlink}\

    :   

    <!-- -->

    []{#_CPPv3N9LAMMPS_NS4ubuf1iE}[]{#_CPPv2N9LAMMPS_NS4ubuf1iE}[]{#LAMMPS_NS::ubuf::i__int64_t}[]{#unionLAMMPS__NS_1_1ubuf_1a193e7d4afbc8ac1c220aa7130e279451 .target}[[int64_t]{.pre}]{.n}[ ]{.w}[[[i]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS4ubuf1iE "Link to this definition"){.headerlink}\

    :   
    :::
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

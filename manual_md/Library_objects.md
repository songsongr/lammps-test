::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#computes-fixes-variables .section}
# [1.1.5. ]{.section-number}Computes, fixes, variables[](#computes-fixes-variables "Link to this heading"){.headerlink}

This section documents accessing or modifying data stored by computes, fixes, or variables in LAMMPS using the following functions:

- [[`lammps_extract_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_extract_computePvPKcii "lammps_extract_compute"){.reference .internal}

- [[`lammps_extract_fix()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_extract_fixPvPKciiii "lammps_extract_fix"){.reference .internal}

- [[`lammps_extract_variable_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_extract_variable_datatypePvPKc "lammps_extract_variable_datatype"){.reference .internal}

- [[`lammps_extract_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv423lammps_extract_variablePvPKcPKc "lammps_extract_variable"){.reference .internal}

- [[`lammps_set_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_set_variablePvPKcPKc "lammps_set_variable"){.reference .internal}

- [[`lammps_set_string_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_set_string_variablePvPKcPKc "lammps_set_string_variable"){.reference .internal}

- [[`lammps_set_internal_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv428lammps_set_internal_variablePvPKcd "lammps_set_internal_variable"){.reference .internal}

- [[`lammps_variable_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_variable_infoPviPci "lammps_variable_info"){.reference .internal}

- [[`lammps_eval()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_evalPvPKc "lammps_eval"){.reference .internal}

- [[`lammps_clearstep_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv424lammps_clearstep_computePv "lammps_clearstep_compute"){.reference .internal}

- [[`lammps_addstep_compute_all()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_addstep_compute_allPvPv "lammps_addstep_compute_all"){.reference .internal}

- [[`lammps_addstep_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_addstep_computePvPv "lammps_addstep_compute"){.reference .internal}

------------------------------------------------------------------------

[]{#_CPPv322lammps_extract_computePvPKcii}[]{#_CPPv222lammps_extract_computePvPKcii}[]{#lammps_extract_compute__voidP.cCP.i.i}[]{#library_8h_1a2e90e8ad6e8a2566e3fe7970c1965567 .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_extract_compute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[style]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422lammps_extract_computePvPKcii "Link to this definition"){.headerlink}\

:   Get pointer to data from a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} compute.

    This function returns a pointer to the location of data provided by a [[compute command]{.doc}]compute.md){.reference .internal} instance identified by the compute-ID. Computes may provide global, per-atom, or local data, and those may be a scalar, a vector, or an array or they may provide the information about the dimensions of the respective data. Since computes may provide multiple kinds of data, it is required to set style and type flags representing what specific data is desired. This also determines to what kind of pointer the returned pointer needs to be cast to access the data correctly. The function returns [`NULL`{.docutils .literal .notranslate}]{.pre} if the compute ID is not found or the requested data is not available or current. The following table lists the available options.

    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | Style (see [[`_LMP_STYLE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}](#_CPPv416_LMP_STYLE_CONST "_LMP_STYLE_CONST"){.reference .internal}) | Type (see [[`_LMP_TYPE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}](#_CPPv415_LMP_TYPE_CONST "_LMP_TYPE_CONST"){.reference .internal}) | Returned type                                                                                                                      | Returned data                                  |
    +====================================================================================================================================================================+================================================================================================================================================================+====================================================================================================================================+================================================+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_TYPE_SCALAR                                                                                                                                                | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}  | Global scalar                                  |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_TYPE_VECTOR                                                                                                                                                | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}  | Global vector                                  |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_TYPE_ARRAY                                                                                                                                                 | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`**`{.docutils .literal .notranslate}]{.pre} | Global array                                   |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_SIZE_VECTOR                                                                                                                                                | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Length of global vector                        |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_SIZE_ROWS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Rows of global array                           |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_SIZE_COLS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Columns of global array                        |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_ATOM                                                                                                                                                     | LMP_TYPE_VECTOR                                                                                                                                                | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}  | Per-atom value                                 |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_ATOM                                                                                                                                                     | LMP_TYPE_ARRAY                                                                                                                                                 | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`**`{.docutils .literal .notranslate}]{.pre} | Per-atom vector                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_ATOM                                                                                                                                                     | LMP_SIZE_COLS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Columns in per-atom array, 0 if vector         |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_LOCAL                                                                                                                                                    | LMP_TYPE_VECTOR                                                                                                                                                | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}  | Local data vector                              |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_LOCAL                                                                                                                                                    | LMP_TYPE_ARRAY                                                                                                                                                 | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`**`{.docutils .literal .notranslate}]{.pre} | Local data array                               |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_LOCAL                                                                                                                                                    | LMP_SIZE_VECTOR                                                                                                                                                | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Alias for LMP_SIZE_ROWS                        |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_LOCAL                                                                                                                                                    | LMP_SIZE_ROWS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Number of local array rows or length of vector |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+
    | LMP_STYLE_LOCAL                                                                                                                                                    | LMP_SIZE_COLS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Number of local array columns, 0 if vector     |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+

    ::: {.admonition .note}
    Note

    If the compute's data is not computed for the current step, the compute will be invoked. LAMMPS cannot easily check at that time, if it is valid to invoke a compute, so it may fail with an error. The caller has to check to avoid such an error.
    :::

    ::: {.admonition .warning}
    Warning

    The pointers returned by this function are generally not persistent since the computed data may be re-distributed, re-allocated, and re-ordered at every invocation. It is advisable to re-invoke this function before the data is accessed, or make a copy if the data shall be used after other LAMMPS commands have been issued.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **id** -- string with ID of the compute

        - **style** -- constant indicating the style of data requested (global, per-atom, or local)

        - **type** -- constant indicating type of data (scalar, vector, or array) or size of rows or columns

    Returns[:]{.colon}

    :   pointer (cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}) to the location of the requested data or [`NULL`{.docutils .literal .notranslate}]{.pre} if not found.

------------------------------------------------------------------------

[]{#_CPPv318lammps_extract_fixPvPKciiii}[]{#_CPPv218lammps_extract_fixPvPKciiii}[]{#lammps_extract_fix__voidP.cCP.i.i.i.i}[]{#library_8h_1aa7a9a4e488fa0d717a9bfb637f2c6a4e .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_extract_fix]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[style]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[nrow]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[ncol]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv418lammps_extract_fixPvPKciiii "Link to this definition"){.headerlink}\

:   Get pointer to data from a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} fix.

    This function returns a pointer to data provided by a [[fix command]{.doc}]fix.md){.reference .internal} instance identified by its fix-ID. Fixes may provide global, per-atom, or local data, and those may be a scalar, a vector, or an array, or they may provide the information about the dimensions of the respective data. Since individual fixes may provide multiple kinds of data, it is required to set style and type flags representing what specific data is desired. This also determines to what kind of pointer the returned pointer needs to be cast to access the data correctly. The function set the error status and returns [`NULL`{.docutils .literal .notranslate}]{.pre} if the fix ID is not found or the requested data is not available.

    ::::: {.warning .admonition}
    Accessing global data

    When requesting **global** data, the fix data can internally only be accessed one item at a time without access to the underlying pointer itself (it may also be computed on-the-fly). Thus this function allocates temporary storage for the requested data, copy the the data to it, and return a pointer to the location of the copy. Therefore the allocated storage needs to be freed with [[`lammps_free()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv411lammps_freePv "lammps_free"){.reference .internal} after its use to avoid a memory leak. Example:

    :::: {.highlight-c .notranslate}
    ::: highlight
        double *dptr = (double *) lammps_extract_fix(handle, name, LMP_STYLE_GLOBAL, LMP_TYPE_VECTOR, 0, 0);
        double value = *dptr;
        lammps_free((void *)dptr);
    :::
    ::::
    :::::

    ::::: {.hint .admonition}
    Requesting rows, columns, or the entire global array

    In order to avoid the inefficient allocation and deallocation of temporary storage for single values, this functions accepts special values of -1 for the nrow and ncol arguments. For the negative values, the entire row, or column, or full array is copied to a (flat) block of storage and its pointer returned. This still is a copy and needs to be deallocated with [[`lammps_free()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv411lammps_freePv "lammps_free"){.reference .internal} as indicated in the note above. In case of requesting the whole array, the data is returned column by column, i.e. as d(c_0,r_0), d(c_0,r_1), ... d(c_0, c_nrow-1), d(c_1,r_0), d(c_1,r_1), ... d(c_ncol-1, r_nrow-1) for a total of nrow \* ncol elements. Example use:

    :::: {.highlight-c .notranslate}
    ::: highlight
        int nrows = *(int *) lammps_extract_fix(handle, name, LMP_STYLE_GLOBAL, LMP_SIZE_ROWS, 0,0);
        int ncols = *(int *) lammps_extract_fix(handle, name, LMP_STYLE_GLOBAL, LMP_SIZE_COLS, 0,0);
        double *dptr = (double *) lammps_extract_fix(handle, name, LMP_STYLE_GLOBAL, LMP_TYPE_ARRAY, -1, -1);
        printf("values[%d][%d] = {\n", ncols, nrows);
        for (int j = 0; j < ncols; ++j) {
          printf(" { ");
          for (int i = 0; i < nrows; ++i) printf("%g, ", dvalue[j * nrows + i]);
          printf("},\n");
        }
        printf("};\n");
        lammps_free((void *)dptr);
    :::
    ::::
    :::::

    The following table lists the available options.

    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | Style (see [[`_LMP_STYLE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}](#_CPPv416_LMP_STYLE_CONST "_LMP_STYLE_CONST"){.reference .internal}) | Type (see [[`_LMP_TYPE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}](#_CPPv415_LMP_TYPE_CONST "_LMP_TYPE_CONST"){.reference .internal}) | Returned type                                                                                                                      | Returned data                               |
    +====================================================================================================================================================================+================================================================================================================================================================+====================================================================================================================================+=============================================+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_TYPE_SCALAR                                                                                                                                                | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}  | Copy of global scalar                       |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_TYPE_VECTOR                                                                                                                                                | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}  | Copy of global vector element at index nrow |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_TYPE_ARRAY                                                                                                                                                 | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}  | Copy of global array element at nrow, ncol  |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_SIZE_VECTOR                                                                                                                                                | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Length of global vector                     |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_SIZE_ROWS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Rows in global array                        |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_GLOBAL                                                                                                                                                   | LMP_SIZE_COLS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Columns in global array                     |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_ATOM                                                                                                                                                     | LMP_TYPE_VECTOR                                                                                                                                                | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}  | Per-atom value                              |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_ATOM                                                                                                                                                     | LMP_TYPE_ARRAY                                                                                                                                                 | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`**`{.docutils .literal .notranslate}]{.pre} | Per-atom vector                             |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_ATOM                                                                                                                                                     | LMP_SIZE_COLS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Columns of per-atom array, 0 if vector      |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_LOCAL                                                                                                                                                    | LMP_TYPE_VECTOR                                                                                                                                                | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}  | Local data vector                           |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_LOCAL                                                                                                                                                    | LMP_TYPE_ARRAY                                                                                                                                                 | [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`**`{.docutils .literal .notranslate}]{.pre} | Local data array                            |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_LOCAL                                                                                                                                                    | LMP_SIZE_ROWS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Number of local data rows                   |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
    | LMP_STYLE_LOCAL                                                                                                                                                    | LMP_SIZE_COLS                                                                                                                                                  | [`int`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}     | Number of local data columns                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+

    ::: {.admonition .note}
    Note

    LAMMPS cannot easily check if it is valid to access the data, so it may fail with an error and return a NULL pointer. The caller has to avoid such an error.
    :::

    ::: {.admonition .warning}
    Warning

    The pointers returned by this function for per-atom or local data are generally not persistent, since the computed data may be re-distributed, re-allocated, and re-ordered at every invocation of the fix. It is thus advisable to re-invoke this function before the data is accessed, or make a copy, if the data shall be used after other LAMMPS commands have been issued.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **id** -- string with ID of the fix

        - **style** -- constant indicating the style of data requested (global, per-atom, or local)

        - **type** -- constant indicating type of data (scalar, vector, or array) or size of rows or columns

        - **nrow** -- row index (only used for global vectors and arrays), zero-based

        - **ncol** -- column index (only used for global arrays), zero-based

    Returns[:]{.colon}

    :   pointer (cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}) to the location of the requested data or [`NULL`{.docutils .literal .notranslate}]{.pre} if not found.

------------------------------------------------------------------------

[]{#_CPPv332lammps_extract_variable_datatypePvPKc}[]{#_CPPv232lammps_extract_variable_datatypePvPKc}[]{#lammps_extract_variable_datatype__voidP.cCP}[]{#library_8h_1a5725944733b98157d3f6993c2f6499ce .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_extract_variable_datatype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv432lammps_extract_variable_datatypePvPKc "Link to this definition"){.headerlink}\

:   Get data type of a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} variable.

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function returns an integer that encodes the data type of the variable with the specified name. See [[`_LMP_VAR_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}](#_CPPv414_LMP_VAR_CONST "_LMP_VAR_CONST"){.reference .internal} for valid values. Callers of [[`lammps_extract_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv423lammps_extract_variablePvPKcPKc "lammps_extract_variable"){.reference .internal} can use this information to decide how to cast the [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} pointer and access the data.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- string with the name of the extracted variable

    Returns[:]{.colon}

    :   integer constant encoding the data type of the property or -1 if not found.

------------------------------------------------------------------------

[]{#_CPPv323lammps_extract_variablePvPKcPKc}[]{#_CPPv223lammps_extract_variablePvPKcPKc}[]{#lammps_extract_variable__voidP.cCP.cCP}[]{#library_8h_1a95cb08b988b86d74a9fded90c47ad5a1 .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_extract_variable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[group]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423lammps_extract_variablePvPKcPKc "Link to this definition"){.headerlink}\

:   Get pointer to data from a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} variable.

    This function returns a pointer to data from a LAMMPS [[variable command]{.doc}]variable.md){.reference .internal} identified by its name. When the variable is either an *equal*-style compatible variable, a *vector*-style variable, or an *atom*-style variable, the variable is evaluated and the corresponding value(s) returned. Variables of style *internal* are compatible with *equal*-style variables and so are *python*-style variables, if they return a numeric value. For other variable styles, their string value is returned. The function returns [`NULL`{.docutils .literal .notranslate}]{.pre} when a variable of the provided *name* is not found or of an incompatible style. The *group* argument is only used for *atom*-style variables and ignored otherwise, with one exception: for style *vector*, if *group* is "GET_VECTOR_SIZE", the returned pointer will yield the length of the vector to be returned when dereferenced. This pointer must be deallocated after the value is read to avoid a memory leak. If *group* is set to [`NULL`{.docutils .literal .notranslate}]{.pre} when extracting data from an *atom*-style variable, the group is assumed to be "all".

    When requesting data from an *equal*-style or compatible variable this function allocates storage for a single double value, copies the returned value to it, and returns a pointer to the location of the copy. Therefore the allocated storage needs to be freed after its use to avoid a memory leak. Example:

    :::: {.highlight-c .notranslate}
    ::: highlight
        double *dptr = (double *) lammps_extract_variable(handle, name, NULL);
        double value = *dptr;
        lammps_free((void *)dptr);
    :::
    ::::

    For *atom*-style variables, the return value is a pointer to an allocated block of storage of double of the length [`atom->nlocal`{.docutils .literal .notranslate}]{.pre}. Since the data returned are a copy, the location will persist, but its content will not be updated in case the variable is re-evaluated. To avoid a memory leak, this pointer needs to be freed after use in the calling program.

    For *vector*-style variables, the returned pointer points to actual LAMMPS data and thus it should **not** be deallocated. Its length depends on the variable, compute, or fix data used to construct the *vector*-style variable. This length can be fetched by calling this function with *group* set to a non-NULL pointer (NULL returns the vector). In that case it will return the vector length as an allocated int pointer cast to a [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} pointer. That pointer can be recast and dereferenced to an integer yielding the length of the vector. This pointer must be deallocated when finished with it to avoid memory leaks. Example:

    :::: {.highlight-c .notranslate}
    ::: highlight
        double *vectvals = (double *) lammps_extract_variable(handle, name, NULL);
        int *intptr = (int *) lammps_extract_variable(handle, name, 1);
        int vectlen = *intptr;
        lammps_free((void *)intptr);
    :::
    ::::

    For other variable styles the returned pointer needs to be cast to a char pointer and it should **not** be deallocated. Example:

    :::: {.highlight-c .notranslate}
    ::: highlight
        const char *cptr = (const char *) lammps_extract_variable(handle,name,NULL);
        printf("The value of variable %s is %s\n", name, cptr);
    :::
    ::::

    ::: {.admonition .note}
    Note

    LAMMPS cannot easily check if it is valid to access the data referenced by the variables (e.g., computes, fixes, or thermodynamic info), so it may fail with an error. The caller has to make certain that the data is extracted only when it safe to evaluate the variable and thus an error or crash are avoided.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- name of the variable

        - **group** -- group-ID for atom style variable or [`NULL`{.docutils .literal .notranslate}]{.pre} or non-NULL to get vector length

    Returns[:]{.colon}

    :   pointer (cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}) to the location of the requested data or [`NULL`{.docutils .literal .notranslate}]{.pre} if not found.

------------------------------------------------------------------------

[]{#_CPPv319lammps_set_variablePvPKcPKc}[]{#_CPPv219lammps_set_variablePvPKcPKc}[]{#lammps_set_variable__voidP.cCP.cCP}[]{#library_8h_1ab3cc202eaec7472181870b4747b3d577 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_set_variable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419lammps_set_variablePvPKcPKc "Link to this definition"){.headerlink}\

:   Set the value of a string-style variable.

    ::: deprecated
    [Deprecated since version 7Feb2024.]{.versionmodified .deprecated}
    :::

    This function assigns a new value from the string str to the string-style variable *name*. This is a way to directly change the string value of a LAMMPS variable that was previous defined with a [[variable name string]{.doc}]variable.md){.reference .internal} command without using any LAMMPS commands to delete and redefine the variable.

    Returns -1 if a variable of that name does not exist or if it is not a string-style variable, otherwise 0.

    ::: {.admonition .warning}
    Warning

    This function is deprecated and [[`lammps_set_string_variable()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_set_string_variablePvPKcPKc "lammps_set_string_variable"){.reference .internal} should be used instead.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- name of the variable

        - **str** -- new value of the variable

    Returns[:]{.colon}

    :   0 on success or -1 on failure

------------------------------------------------------------------------

[]{#_CPPv326lammps_set_string_variablePvPKcPKc}[]{#_CPPv226lammps_set_string_variablePvPKcPKc}[]{#lammps_set_string_variable__voidP.cCP.cCP}[]{#library_8h_1a540ffa539718883760eb6fafab3627bc .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_set_string_variable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv426lammps_set_string_variablePvPKcPKc "Link to this definition"){.headerlink}\

:   Set the value of a string-style variable.

    ::: versionadded
    [Added in version 7Feb2024.]{.versionmodified .added}
    :::

    This function assigns a new value from the string str to the string-style variable *name*. This is a way to directly change the string value of a LAMMPS variable that was previous defined with a [[variable name string]{.doc}]variable.md){.reference .internal} command without using any LAMMPS commands to delete and redefine the variable.

    Returns -1 if a variable of that name does not exist or if it is not a string-style variable, otherwise 0.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- name of the variable

        - **str** -- new value of the variable

    Returns[:]{.colon}

    :   0 on success or -1 on failure

------------------------------------------------------------------------

[]{#_CPPv328lammps_set_internal_variablePvPKcd}[]{#_CPPv228lammps_set_internal_variablePvPKcd}[]{#lammps_set_internal_variable__voidP.cCP.double}[]{#library_8h_1a250fd1b00f6b69daf98cc4a879c78059 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_set_internal_variable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv428lammps_set_internal_variablePvPKcd "Link to this definition"){.headerlink}\

:   Set the value of an internal-style variable.

    ::: versionadded
    [Added in version 7Feb2024.]{.versionmodified .added}
    :::

    This function assigns a new value from the floating point number *value* to the internal-style variable *name*. This is a way to directly change the numerical value of such a LAMMPS variable that was previous defined with a [[variable name internal]{.doc}]variable.md){.reference .internal} command without using any LAMMPS commands to delete and redefine the variable.

    Returns -1 if a variable of that name does not exist or is not an internal-style variable, otherwise 0.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- name of the variable

        - **value** -- new value of the variable

    Returns[:]{.colon}

    :   0 on success or -1 on failure

------------------------------------------------------------------------

[]{#_CPPv320lammps_variable_infoPviPci}[]{#_CPPv220lammps_variable_infoPviPci}[]{#lammps_variable_info__voidP.i.cP.i}[]{#library_8h_1a7d42a4fb49036f76e6042ca8302aa567 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_variable_info]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[idx]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[buf]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[bufsize]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420lammps_variable_infoPviPci "Link to this definition"){.headerlink}\

:   Retrieve informational string for a variable.

    ::: versionadded
    [Added in version 21Nov2023.]{.versionmodified .added}
    :::

    This function copies a string with human readable information about a defined variable: name, style, current value(s) into the provided C-style string buffer. That is the same info as produced by the [[info variables]{.doc}]info.md){.reference .internal} command. The length of the buffer must be provided as *buf_size* argument. If the info exceeds the length of the buffer, it will be truncated accordingly. If the index is out of range, the function returns 0 and *buffer* is set to an empty string, otherwise 1.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **idx** -- index of the variable (0 \<= idx \< nvar)

        - **buffer** -- string buffer to copy the info to

        - **buf_size** -- size of the provided string buffer

    Returns[:]{.colon}

    :   1 if successful, otherwise 0

------------------------------------------------------------------------

[]{#_CPPv311lammps_evalPvPKc}[]{#_CPPv211lammps_evalPvPKc}[]{#lammps_eval__voidP.cCP}[]{#library_8h_1a506702d4f1ccc8ec61c453eb73a90f16 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[lammps_eval]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[expr]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv411lammps_evalPvPKc "Link to this definition"){.headerlink}\

:   Evaluate an immediate variable expression

    ::: versionadded
    [Added in version 4Feb2025.]{.versionmodified .added}
    :::

    This function takes a string with an expression that can be used for [[equal style variables]{.doc}]variable.md){.reference .internal}, evaluates it and returns the resulting (scalar) value as a floating point number.

    *See also*

    :   [[`lammps_expand()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_execute.md#_CPPv413lammps_expandPvPKc "lammps_expand"){.reference .internal}

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **expr** -- string with expression

    Returns[:]{.colon}

    :   result from expression

------------------------------------------------------------------------

[]{#_CPPv324lammps_clearstep_computePv}[]{#_CPPv224lammps_clearstep_computePv}[]{#lammps_clearstep_compute__voidP}[]{#library_8h_1a155311dfd1742f46d12be15ed95bfbdd .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_clearstep_compute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv424lammps_clearstep_computePv "Link to this definition"){.headerlink}\

:   Clear whether a compute has been invoked.

    ::: versionadded
    [Added in version 4Feb2025: ]{.versionmodified .added}This function clears the invoked flag of all computes. Called everywhere that computes are used, before computes are invoked. The invoked flag is used to avoid re-invoking same compute multiple times and to flag computes that store invocation times as having been invoked
    :::

    *See also*

    :   [[`lammps_addstep_compute_all()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_addstep_compute_allPvPv "lammps_addstep_compute_all"){.reference .internal} [[`lammps_addstep_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_addstep_computePvPv "lammps_addstep_compute"){.reference .internal}

    Parameters[:]{.colon}

    :   **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

------------------------------------------------------------------------

[]{#_CPPv326lammps_addstep_compute_allPvPv}[]{#_CPPv226lammps_addstep_compute_allPvPv}[]{#lammps_addstep_compute_all__voidP.voidP}[]{#library_8h_1a123a452c98e9461aea99e1a4048e2f7a .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_addstep_compute_all]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[nextstep]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv426lammps_addstep_compute_allPvPv "Link to this definition"){.headerlink}\

:   Add next timestep to all computes

    ::: versionadded
    [Added in version 4Feb2025: ]{.versionmodified .added}loop over all computes schedule next invocation for those that store invocation times called when not sure what computes will be needed on newstep do not loop only over n_timeflag, since may not be set yet
    :::

    *See also*

    :   [[`lammps_clearstep_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv424lammps_clearstep_computePv "lammps_clearstep_compute"){.reference .internal} [[`lammps_addstep_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_addstep_computePvPv "lammps_addstep_compute"){.reference .internal}

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **newstep** -- pointer to bigint of next timestep the compute will be invoked

------------------------------------------------------------------------

[]{#_CPPv322lammps_addstep_computePvPv}[]{#_CPPv222lammps_addstep_computePvPv}[]{#lammps_addstep_compute__voidP.voidP}[]{#library_8h_1aabcc86362dc02678435b8759313bcac2 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_addstep_compute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[nextstep]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422lammps_addstep_computePvPv "Link to this definition"){.headerlink}\

:   Add next timestep to compute if it has been invoked in the current timestep

    ::: versionadded
    [Added in version 4Feb2025: ]{.versionmodified .added}loop over computes that store invocation times if its invoked flag set on this timestep, schedule next invocation called everywhere that computes are used, after computes are invoked
    :::

    *See also*

    :   [[`lammps_addstep_compute_all()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_addstep_compute_allPvPv "lammps_addstep_compute_all"){.reference .internal} [[`lammps_clearstep_compute()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv424lammps_clearstep_computePv "lammps_clearstep_compute"){.reference .internal}

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **newstep** -- next timestep the compute will be invoked

------------------------------------------------------------------------

[]{#_CPPv3N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONSTE}[]{#_CPPv2N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONSTE}[]{#structLAMMPS__NS_1_1multitype_1a8f60df5cd520b67959d22185afcdacc5 .target}[[enum]{.pre}]{.k}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[multitype]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[\_LMP_DATATYPE_CONST]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONSTE "Link to this definition"){.headerlink}\

:   Data type constants for extracting data from atoms, computes and fixes

    This enum must be kept in sync with the corresponding enum or constants in [`python/lammps/constants.py`{.docutils .literal .notranslate}]{.pre}, [`fortran/lammps.f90`{.docutils .literal .notranslate}]{.pre}, [`tools/swig/lammps.i`{.docutils .literal .notranslate}]{.pre}, [`src/library.h`{.docutils .literal .notranslate}]{.pre}, and [`examples/COUPLE/plugin/liblammpsplugin.h`{.docutils .literal .notranslate}]{.pre}

    *Values:*

    []{#_CPPv3N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST11LAMMPS_NONEE}[]{#_CPPv2N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST11LAMMPS_NONEE}[]{#structLAMMPS__NS_1_1multitype_1a8f60df5cd520b67959d22185afcdacc5a2092f040c8fd7fd46efa6591c4f03515 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LAMMPS_NONE]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST11LAMMPS_NONEE "Link to this definition"){.headerlink}\

    :   no data type assigned (yet)

    []{#_CPPv3N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST10LAMMPS_INTE}[]{#_CPPv2N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST10LAMMPS_INTE}[]{#structLAMMPS__NS_1_1multitype_1a8f60df5cd520b67959d22185afcdacc5a6f4597ad5c533e63a78fe90151d4d348 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LAMMPS_INT]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST10LAMMPS_INTE "Link to this definition"){.headerlink}\

    :   32-bit integer (array)

    []{#_CPPv3N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST13LAMMPS_INT_2DE}[]{#_CPPv2N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST13LAMMPS_INT_2DE}[]{#structLAMMPS__NS_1_1multitype_1a8f60df5cd520b67959d22185afcdacc5acdc5b9e5771b685c0f5c0377a06380da .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LAMMPS_INT_2D]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST13LAMMPS_INT_2DE "Link to this definition"){.headerlink}\

    :   two-dimensional 32-bit integer array

    []{#_CPPv3N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST13LAMMPS_DOUBLEE}[]{#_CPPv2N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST13LAMMPS_DOUBLEE}[]{#structLAMMPS__NS_1_1multitype_1a8f60df5cd520b67959d22185afcdacc5a5a6c3a30d227047ab64e210c8a2fd468 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LAMMPS_DOUBLE]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST13LAMMPS_DOUBLEE "Link to this definition"){.headerlink}\

    :   64-bit double (array)

    []{#_CPPv3N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST16LAMMPS_DOUBLE_2DE}[]{#_CPPv2N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST16LAMMPS_DOUBLE_2DE}[]{#structLAMMPS__NS_1_1multitype_1a8f60df5cd520b67959d22185afcdacc5a515e6e960fa5de1f4e22596ede33fdeb .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LAMMPS_DOUBLE_2D]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST16LAMMPS_DOUBLE_2DE "Link to this definition"){.headerlink}\

    :   two-dimensional 64-bit double array

    []{#_CPPv3N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST12LAMMPS_INT64E}[]{#_CPPv2N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST12LAMMPS_INT64E}[]{#structLAMMPS__NS_1_1multitype_1a8f60df5cd520b67959d22185afcdacc5a3e0db9f4dfd611ebb971372cc245e80c .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LAMMPS_INT64]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST12LAMMPS_INT64E "Link to this definition"){.headerlink}\

    :   64-bit integer (array)

    []{#_CPPv3N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST15LAMMPS_INT64_2DE}[]{#_CPPv2N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST15LAMMPS_INT64_2DE}[]{#structLAMMPS__NS_1_1multitype_1a8f60df5cd520b67959d22185afcdacc5abfc022018c51b292be00cbc87760ab60 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LAMMPS_INT64_2D]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST15LAMMPS_INT64_2DE "Link to this definition"){.headerlink}\

    :   two-dimensional 64-bit integer array

    []{#_CPPv3N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST13LAMMPS_STRINGE}[]{#_CPPv2N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST13LAMMPS_STRINGE}[]{#structLAMMPS__NS_1_1multitype_1a8f60df5cd520b67959d22185afcdacc5ae8c997bf96560c2d658a3d2a01518d72 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LAMMPS_STRING]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N9LAMMPS_NS9multitype19_LMP_DATATYPE_CONST13LAMMPS_STRINGE "Link to this definition"){.headerlink}\

    :   C-String

<!-- -->

[]{#_CPPv316_LMP_STYLE_CONST}[]{#_CPPv216_LMP_STYLE_CONST}[]{#library_8h_1af78e950523b27d0aa9b74ccf93666d36 .target}[[enum]{.pre}]{.k}[ ]{.w}[[[\_LMP_STYLE_CONST]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv416_LMP_STYLE_CONST "Link to this definition"){.headerlink}\

:   Style constants for extracting data from computes and fixes.

    Must be kept in sync with the equivalent constants in [`python/lammps/constants.py`{.docutils .literal .notranslate}]{.pre}, [`fortran/lammps.f90`{.docutils .literal .notranslate}]{.pre}, [`tools/swig/lammps.i`{.docutils .literal .notranslate}]{.pre}, and [`examples/COUPLE/plugin/liblammpsplugin.h`{.docutils .literal .notranslate}]{.pre}

    *Values:*

    []{#_CPPv3N16_LMP_STYLE_CONST16LMP_STYLE_GLOBALE}[]{#_CPPv2N16_LMP_STYLE_CONST16LMP_STYLE_GLOBALE}[]{#library_8h_1af78e950523b27d0aa9b74ccf93666d36a5d9f763d2a7c13c4aea83405aaf4b3f3 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_STYLE_GLOBAL]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N16_LMP_STYLE_CONST16LMP_STYLE_GLOBALE "Link to this definition"){.headerlink}\

    :   return global data

    []{#_CPPv3N16_LMP_STYLE_CONST14LMP_STYLE_ATOME}[]{#_CPPv2N16_LMP_STYLE_CONST14LMP_STYLE_ATOME}[]{#library_8h_1af78e950523b27d0aa9b74ccf93666d36aa1e72b0a28e28261262774733cdbadfa .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_STYLE_ATOM]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N16_LMP_STYLE_CONST14LMP_STYLE_ATOME "Link to this definition"){.headerlink}\

    :   return per-atom data

    []{#_CPPv3N16_LMP_STYLE_CONST15LMP_STYLE_LOCALE}[]{#_CPPv2N16_LMP_STYLE_CONST15LMP_STYLE_LOCALE}[]{#library_8h_1af78e950523b27d0aa9b74ccf93666d36a9b74ce240cd632e21f8c1a5a1cf07ed0 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_STYLE_LOCAL]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N16_LMP_STYLE_CONST15LMP_STYLE_LOCALE "Link to this definition"){.headerlink}\

    :   return local data

<!-- -->

[]{#_CPPv315_LMP_TYPE_CONST}[]{#_CPPv215_LMP_TYPE_CONST}[]{#library_8h_1a30cd6a0606720be7addec2816760879e .target}[[enum]{.pre}]{.k}[ ]{.w}[[[\_LMP_TYPE_CONST]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv415_LMP_TYPE_CONST "Link to this definition"){.headerlink}\

:   Type and size constants for extracting data from computes and fixes.

    Must be kept in sync with the equivalent constants in [`python/lammps/constants.py`{.docutils .literal .notranslate}]{.pre}, [`fortran/lammps.f90`{.docutils .literal .notranslate}]{.pre}, [`tools/swig/lammps.i`{.docutils .literal .notranslate}]{.pre}, and [`examples/COUPLE/plugin/liblammpsplugin.h`{.docutils .literal .notranslate}]{.pre}

    *Values:*

    []{#_CPPv3N15_LMP_TYPE_CONST15LMP_TYPE_SCALARE}[]{#_CPPv2N15_LMP_TYPE_CONST15LMP_TYPE_SCALARE}[]{#library_8h_1a30cd6a0606720be7addec2816760879ea3a0d5e6c49cc929d953b366ed58c821b .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_TYPE_SCALAR]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N15_LMP_TYPE_CONST15LMP_TYPE_SCALARE "Link to this definition"){.headerlink}\

    :   return scalar

    []{#_CPPv3N15_LMP_TYPE_CONST15LMP_TYPE_VECTORE}[]{#_CPPv2N15_LMP_TYPE_CONST15LMP_TYPE_VECTORE}[]{#library_8h_1a30cd6a0606720be7addec2816760879ead7beec11786a3dc637fcdd2ac62506e8 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_TYPE_VECTOR]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N15_LMP_TYPE_CONST15LMP_TYPE_VECTORE "Link to this definition"){.headerlink}\

    :   return vector

    []{#_CPPv3N15_LMP_TYPE_CONST14LMP_TYPE_ARRAYE}[]{#_CPPv2N15_LMP_TYPE_CONST14LMP_TYPE_ARRAYE}[]{#library_8h_1a30cd6a0606720be7addec2816760879eaaacd44f7a32b76b06051cb01ff40451a .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_TYPE_ARRAY]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N15_LMP_TYPE_CONST14LMP_TYPE_ARRAYE "Link to this definition"){.headerlink}\

    :   return array

    []{#_CPPv3N15_LMP_TYPE_CONST15LMP_SIZE_VECTORE}[]{#_CPPv2N15_LMP_TYPE_CONST15LMP_SIZE_VECTORE}[]{#library_8h_1a30cd6a0606720be7addec2816760879eab7e39a6a361f8bc210064c9d853b4ded .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_SIZE_VECTOR]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N15_LMP_TYPE_CONST15LMP_SIZE_VECTORE "Link to this definition"){.headerlink}\

    :   return length of vector

    []{#_CPPv3N15_LMP_TYPE_CONST13LMP_SIZE_ROWSE}[]{#_CPPv2N15_LMP_TYPE_CONST13LMP_SIZE_ROWSE}[]{#library_8h_1a30cd6a0606720be7addec2816760879eaa65d78d0215fbb5d1f8cf6dfa05ed485 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_SIZE_ROWS]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N15_LMP_TYPE_CONST13LMP_SIZE_ROWSE "Link to this definition"){.headerlink}\

    :   return number of rows

    []{#_CPPv3N15_LMP_TYPE_CONST13LMP_SIZE_COLSE}[]{#_CPPv2N15_LMP_TYPE_CONST13LMP_SIZE_COLSE}[]{#library_8h_1a30cd6a0606720be7addec2816760879ea0213053b1c6d4283bb6d662a00fecc16 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_SIZE_COLS]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N15_LMP_TYPE_CONST13LMP_SIZE_COLSE "Link to this definition"){.headerlink}\

    :   return number of columns

<!-- -->

[]{#_CPPv314_LMP_VAR_CONST}[]{#_CPPv214_LMP_VAR_CONST}[]{#library_8h_1a09d7d9d1e5512d11257c5b6fce67ee37 .target}[[enum]{.pre}]{.k}[ ]{.w}[[[\_LMP_VAR_CONST]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv414_LMP_VAR_CONST "Link to this definition"){.headerlink}\

:   Variable style constants for extracting data from variables.

    Must be kept in sync with the equivalent constants in [`python/lammps/constants.py`{.docutils .literal .notranslate}]{.pre}, [`fortran/lammps.f90`{.docutils .literal .notranslate}]{.pre}, [`tools/swig/lammps.i`{.docutils .literal .notranslate}]{.pre}, and [`examples/COUPLE/plugin/liblammpsplugin.h`{.docutils .literal .notranslate}]{.pre}

    *Values:*

    []{#_CPPv3N14_LMP_VAR_CONST13LMP_VAR_EQUALE}[]{#_CPPv2N14_LMP_VAR_CONST13LMP_VAR_EQUALE}[]{#library_8h_1a09d7d9d1e5512d11257c5b6fce67ee37aeb6a1c0a08cdfb496bcaef2cc37d5047 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_VAR_EQUAL]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N14_LMP_VAR_CONST13LMP_VAR_EQUALE "Link to this definition"){.headerlink}\

    :   compatible with equal-style variables

    []{#_CPPv3N14_LMP_VAR_CONST12LMP_VAR_ATOME}[]{#_CPPv2N14_LMP_VAR_CONST12LMP_VAR_ATOME}[]{#library_8h_1a09d7d9d1e5512d11257c5b6fce67ee37a4a336ec13f20754d421f7d0d218cc1a4 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_VAR_ATOM]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N14_LMP_VAR_CONST12LMP_VAR_ATOME "Link to this definition"){.headerlink}\

    :   compatible with atom-style variables

    []{#_CPPv3N14_LMP_VAR_CONST14LMP_VAR_VECTORE}[]{#_CPPv2N14_LMP_VAR_CONST14LMP_VAR_VECTORE}[]{#library_8h_1a09d7d9d1e5512d11257c5b6fce67ee37a381da764a4e3a5f1bc183cc9905be43c .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_VAR_VECTOR]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N14_LMP_VAR_CONST14LMP_VAR_VECTORE "Link to this definition"){.headerlink}\

    :   compatible with vector-style variables

    []{#_CPPv3N14_LMP_VAR_CONST14LMP_VAR_STRINGE}[]{#_CPPv2N14_LMP_VAR_CONST14LMP_VAR_STRINGE}[]{#library_8h_1a09d7d9d1e5512d11257c5b6fce67ee37a52551a127731cf3f7e193b9d1d83e6e8 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[LMP_VAR_STRING]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N14_LMP_VAR_CONST14LMP_VAR_STRINGE "Link to this definition"){.headerlink}\

    :   return value will be a string (catch-all)
:::
::::
:::::

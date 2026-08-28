::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#per-atom-properties .section}
# [1.1.4. ]{.section-number}Per-atom properties[](#per-atom-properties "Link to this heading"){.headerlink}

This section documents the following functions:

- [[`lammps_extract_atom_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv428lammps_extract_atom_datatypePvPKc "lammps_extract_atom_datatype"){.reference .internal}

- [[`lammps_extract_atom_size()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv424lammps_extract_atom_sizePvPKci "lammps_extract_atom_size"){.reference .internal}

- [[`lammps_extract_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_extract_atomPvPKc "lammps_extract_atom"){.reference .internal}

------------------------------------------------------------------------

[]{#_CPPv328lammps_extract_atom_datatypePvPKc}[]{#_CPPv228lammps_extract_atom_datatypePvPKc}[]{#lammps_extract_atom_datatype__voidP.cCP}[]{#library_8h_1aed36a77c70d91c9497b5eee075d18aab .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_extract_atom_datatype]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv428lammps_extract_atom_datatypePvPKc "Link to this definition"){.headerlink}\

:   Get data type of a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} per-atom property

    ::: versionadded
    [Added in version 18Sep2020.]{.versionmodified .added}
    :::

    This function returns an integer that encodes the data type of the per-atom property with the specified name. See [`_LMP_DATATYPE_CONST`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre} for valid values. Callers of [[`lammps_extract_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_extract_atomPvPKc "lammps_extract_atom"){.reference .internal} can use this information to decide how to cast the [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} pointer and access the data. In addition, [[`lammps_extract_atom_size()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv424lammps_extract_atom_sizePvPKci "lammps_extract_atom_size"){.reference .internal} can be used to get information about the vector or array dimensions.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- string with the name of the extracted property

    Returns[:]{.colon}

    :   integer constant encoding the data type of the property or -1 if not found.

------------------------------------------------------------------------

[]{#_CPPv324lammps_extract_atom_sizePvPKci}[]{#_CPPv224lammps_extract_atom_sizePvPKci}[]{#lammps_extract_atom_size__voidP.cCP.i}[]{#library_8h_1a2e1f204c0e8b8fc3bde330e9fe94cff3 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_extract_atom_size]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv424lammps_extract_atom_sizePvPKci "Link to this definition"){.headerlink}\

:   Get dimension info of a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} per-atom property

    ::: versionadded
    [Added in version 19Nov2024.]{.versionmodified .added}
    :::

    This function returns an integer with the size of the per-atom property with the specified name. This allows to accurately determine the size of the per-atom data vectors or arrays. For per-atom arrays, the *type* argument is required to return either the number of rows or the number of columns. It is ignored for per-atom vectors.

    Callers of [[`lammps_extract_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_extract_atomPvPKc "lammps_extract_atom"){.reference .internal} can use this information in combination with the result from [[`lammps_extract_atom_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv428lammps_extract_atom_datatypePvPKc "lammps_extract_atom_datatype"){.reference .internal} to decide how to cast the [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} pointer and access the data.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- string with the name of the extracted property

        - **type** -- either LMP_SIZE_ROWS or LMP_SIZE_COLS if *name* refers to a per-atom array otherwise ignored

    Returns[:]{.colon}

    :   integer with the size of the vector or array dimension or -1

------------------------------------------------------------------------

[]{#_CPPv319lammps_extract_atomPvPKc}[]{#_CPPv219lammps_extract_atomPvPKc}[]{#lammps_extract_atom__voidP.cCP}[]{#library_8h_1aa195b895bff9cd756ec18ca2e9cab90d .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_extract_atom]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419lammps_extract_atomPvPKc "Link to this definition"){.headerlink}\

:   Get pointer to a [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} per-atom property.

    This function returns a pointer to the location of per-atom properties (and per-atom-type properties in the case of the 'mass' keyword). Per-atom data is distributed across sub-domains and thus MPI ranks. The returned pointer is cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} and needs to be cast to a pointer of data type that the entity represents. You can use the functions [[`lammps_extract_atom_datatype()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv428lammps_extract_atom_datatypePvPKc "lammps_extract_atom_datatype"){.reference .internal} and [[`lammps_extract_atom_size()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv424lammps_extract_atom_sizePvPKci "lammps_extract_atom_size"){.reference .internal} to determine data type, dimensions and sizes of the storage pointed to by the returned pointer.

    A table with supported keywords is included in the documentation of the [[`Atom::extract()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom7extractEPKc "LAMMPS_NS::Atom::extract"){.reference .internal} function.

    ::: {.admonition .warning}
    Warning

    The pointers returned by this function are generally not persistent since per-atom data may be re-distributed, re-allocated, and re-ordered at every re-neighboring operation.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- string with the name of the extracted property

    Returns[:]{.colon}

    :   pointer (cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}) to the location of the requested data or [`NULL`{.docutils .literal .notranslate}]{.pre} if not found.
:::
::::
:::::

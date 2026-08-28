::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#scatter-gather-operations .section}
# [1.1.6. ]{.section-number}Scatter/gather operations[](#scatter-gather-operations "Link to this heading"){.headerlink}

This section has functions which gather per-atom data from one or more processors into a contiguous global list ordered by atom ID. The same list is returned to all calling processors. It also contains functions which scatter per-atom data from a contiguous global list across the processors that own those atom IDs. It also has a create_atoms() function which can create new atoms by scattering them appropriately to owning processors in the LAMMPS spatial decomposition.

It documents the following functions:

- [[`lammps_gather_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_gather_atomsPvPKciiPv "lammps_gather_atoms"){.reference .internal}

- [[`lammps_gather_atoms_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_gather_atoms_concatPvPKciiPv "lammps_gather_atoms_concat"){.reference .internal}

- [[`lammps_gather_atoms_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_gather_atoms_subsetPvPKciiiPiPv "lammps_gather_atoms_subset"){.reference .internal}

- [[`lammps_scatter_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_scatter_atomsPvPKciiPv "lammps_scatter_atoms"){.reference .internal}

- [[`lammps_scatter_atoms_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv427lammps_scatter_atoms_subsetPvPKciiiPiPv "lammps_scatter_atoms_subset"){.reference .internal}

- [[`lammps_gather_bonds()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_gather_bondsPvPv "lammps_gather_bonds"){.reference .internal}

- [[`lammps_gather_angles()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_gather_anglesPvPv "lammps_gather_angles"){.reference .internal}

- [[`lammps_gather_dihedrals()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv423lammps_gather_dihedralsPvPv "lammps_gather_dihedrals"){.reference .internal}

- [[`lammps_gather_impropers()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv423lammps_gather_impropersPvPv "lammps_gather_impropers"){.reference .internal}

- [[`lammps_gather()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv413lammps_gatherPvPKciiPv "lammps_gather"){.reference .internal}

- [[`lammps_gather_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_gather_concatPvPKciiPv "lammps_gather_concat"){.reference .internal}

- [[`lammps_gather_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_gather_subsetPvPKciiiPiPv "lammps_gather_subset"){.reference .internal}

- [[`lammps_scatter()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv414lammps_scatterPvPKciiPv "lammps_scatter"){.reference .internal}

- [[`lammps_scatter_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_scatter_subsetPvPKciiiPiPv "lammps_scatter_subset"){.reference .internal}

- [[`lammps_create_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_create_atomsPviPKiPKiPKdPKdPKii "lammps_create_atoms"){.reference .internal}

- [[`lammps_create_molecule()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_create_moleculePvPKcPKc "lammps_create_molecule"){.reference .internal}

------------------------------------------------------------------------

[]{#_CPPv319lammps_gather_atomsPvPKciiPv}[]{#_CPPv219lammps_gather_atomsPvPKciiPv}[]{#lammps_gather_atoms__voidP.cCP.i.i.voidP}[]{#library_8h_1ad3208ce7d03d54f74573a80565dc335d .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather_atoms]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419lammps_gather_atomsPvPKciiPv "Link to this definition"){.headerlink}\

:   Gather the named atom-based entity for all atoms across all processes, in order.

    This subroutine gathers data for all atoms and stores them in a one-dimensional array allocated by the user. The data will be ordered by atom ID, which requires consecutive atom IDs (1 to *natoms*). If you need a similar array but have non-consecutive atom IDs, see [[`lammps_gather_atoms_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_gather_atoms_concatPvPKciiPv "lammps_gather_atoms_concat"){.reference .internal}; for a similar array but for a subset of atoms, see [[`lammps_gather_atoms_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_gather_atoms_subsetPvPKciiiPiPv "lammps_gather_atoms_subset"){.reference .internal}.

    The *data* array will be ordered in groups of *count* values, sorted by atom ID (e.g., if *name* is *x* and *count* = 3, then *data* = x\[0\]\[0\], x\[0\]\[1\], x\[0\]\[2\], x\[1\]\[0\], x\[1\]\[1\], x\[1\]\[2\], x\[2\]\[0\], [\\(\\dots\\)]{.math .notranslate .nohighlight}); *data* must be pre-allocated by the caller to length (*count* [\\(\\times\\)]{.math .notranslate .nohighlight} *natoms*), as queried by [[`lammps_get_natoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_natomsPv "lammps_get_natoms"){.reference .internal}, [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal}, or [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal}.

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined and consecutive.

    The total number of atoms must not be more than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., *x* or *q*)

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *type* or *q*, 3 for *x* or *f*); use *count* = 3 with *image* if you want a single image flag unpacked into (*x*,*y*,*z*) components.

        - **data** -- per-atom values packed in a 1-dimensional array of length *natoms* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv326lammps_gather_atoms_concatPvPKciiPv}[]{#_CPPv226lammps_gather_atoms_concatPvPKciiPv}[]{#lammps_gather_atoms_concat__voidP.cCP.i.i.voidP}[]{#library_8h_1a5e433d99895ca2aa9d87843bc7ee49d5 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather_atoms_concat]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv426lammps_gather_atoms_concatPvPKciiPv "Link to this definition"){.headerlink}\

:   Gather the named atom-based entity for all atoms across all processes, unordered.

    This subroutine gathers data for all atoms and stores them in a one-dimensional array allocated by the user. The data will be a concatenation of chunks from each processor's owned atoms, in whatever order the atoms are in on each processor. This process has no requirement that the atom IDs be consecutive. If you need the ID of each atom, you can do another [[`lammps_gather_atoms_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_gather_atoms_concatPvPKciiPv "lammps_gather_atoms_concat"){.reference .internal} call with *name* set to [`id`{.docutils .literal .notranslate}]{.pre}. If you have consecutive IDs and want the data to be in order, use [[`lammps_gather_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_gather_atomsPvPKciiPv "lammps_gather_atoms"){.reference .internal}; for a similar array but for a subset of atoms, use [[`lammps_gather_atoms_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_gather_atoms_subsetPvPKciiiPiPv "lammps_gather_atoms_subset"){.reference .internal}.

    The *data* array will be in groups of *count* values, with *natoms* groups total, but not in order by atom ID (e.g., if *name* is *x* and *count* is 3, then *data* might be something like x\[10\]\[0\], x\[10\]\[1\], x\[10\]\[2\], x\[2\]\[0\], x\[2\]\[1\], x\[2\]\[2\], x\[4\]\[0\], [\\(\\dots\\)]{.math .notranslate .nohighlight}); *data* must be pre-allocated by the caller to length (*count* [\\(\\times\\)]{.math .notranslate .nohighlight} *natoms*), as queried by [[`lammps_get_natoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_natomsPv "lammps_get_natoms"){.reference .internal}, [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal}, or [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal}.

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined.

    The total number of atoms must not be more than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., *x* or *q*\\ )

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *type* or *q*, 3 for *x* or *f*); use *count* = 3 with "image" if you want single image flags unpacked into (*x*,*y*,*z*)

        - **data** -- per-atom values packed in a 1-dimensional array of length *natoms* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv326lammps_gather_atoms_subsetPvPKciiiPiPv}[]{#_CPPv226lammps_gather_atoms_subsetPvPKciiiPiPv}[]{#lammps_gather_atoms_subset__voidP.cCP.i.i.i.iP.voidP}[]{#library_8h_1adb2aa14375aa277b1c32ad17a5f4a39f .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather_atoms_subset]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[ndata]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ids]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv426lammps_gather_atoms_subsetPvPKciiiPiPv "Link to this definition"){.headerlink}\

:   Gather the named atom-based entity for a subset of atoms.

    This subroutine gathers data for the requested atom IDs and stores them in a one-dimensional array allocated by the user. The data will be ordered by atom ID, but there is no requirement that the IDs be consecutive. If you wish to return a similar array for *all* the atoms, use [[`lammps_gather_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv419lammps_gather_atomsPvPKciiPv "lammps_gather_atoms"){.reference .internal} or [[`lammps_gather_atoms_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_gather_atoms_concatPvPKciiPv "lammps_gather_atoms_concat"){.reference .internal}.

    The *data* array will be in groups of *count* values, sorted by atom ID in the same order as the array *ids* (e.g., if *name* is *x*, *count* = 3, and *ids* is {100, 57, 210}, then *data* might look like {x\[100\]\[0\], x\[100\]\[1\], x\[100\]\[2\], x\[57\]\[0\], x\[57\]\[1\], x\[57\]\[2\], x\[210\]\[0\], [\\(\\dots\\)]{.math .notranslate .nohighlight}); *ids* must be provided by the user with length *ndata*, and *data* must be pre-allocated by the caller to length (*count* [\\(\\times\\)]{.math .notranslate .nohighlight} *ndata*).

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined and an [[atom map must be enabled]{.doc}]atom_modify.md){.reference .internal}

    The total number of atoms must not be more than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., *x* or *q*)

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *type* or *q*, 3 for *x* or *f*); use *count* = 3 with "image" if you want single image flags unpacked into (*x*,*y*,*z*)

        - **ndata** -- number of atoms for which to return data (can be all of them)

        - **ids** -- list of *ndata* atom IDs for which to return data

        - **data** -- per-atom values packed in a 1-dimensional array of length *ndata* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv320lammps_scatter_atomsPvPKciiPv}[]{#_CPPv220lammps_scatter_atomsPvPKciiPv}[]{#lammps_scatter_atoms__voidP.cCP.i.i.voidP}[]{#library_8h_1a912e450e211db31d9396ad5f421d500d .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_scatter_atoms]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420lammps_scatter_atomsPvPKciiPv "Link to this definition"){.headerlink}\

:   Scatter the named atom-based entities in *data* to all processes.

    This subroutine takes data stored in a one-dimensional array supplied by the user and scatters them to all atoms on all processes. The data must be ordered by atom ID, with the requirement that the IDs be consecutive. Use [[`lammps_scatter_atoms_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv427lammps_scatter_atoms_subsetPvPKciiiPiPv "lammps_scatter_atoms_subset"){.reference .internal} to scatter data for some (or all) atoms, unordered.

    The *data* array needs to be ordered in groups of *count* values, sorted by atom ID (e.g., if *name* is *x* and *count* = 3, then *data* = {x\[0\]\[0\], x\[0\]\[1\], x\[0\]\[2\], x\[1\]\[0\], x\[1\]\[1\], x\[1\]\[2\], x\[2\]\[0\], [\\(\\dots\\)]{.math .notranslate .nohighlight}}); *data* must be of length (*count* [\\(\\times\\)]{.math .notranslate .nohighlight} *natoms*).

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined, must be consecutive, and an [[atom map must be enabled]{.doc}]atom_modify.md){.reference .internal}

    The total number of atoms must not be more than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., *x* or *q*)

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *type* or *q*, 3 for *x* or *f*); use *count* = 3 with *image* if you have a single image flag packed into (*x*,*y*,*z*) components.

        - **data** -- per-atom values packed in a one-dimensional array of length *natoms* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv327lammps_scatter_atoms_subsetPvPKciiiPiPv}[]{#_CPPv227lammps_scatter_atoms_subsetPvPKciiiPiPv}[]{#lammps_scatter_atoms_subset__voidP.cCP.i.i.i.iP.voidP}[]{#library_8h_1a42726943d284b0edad9b8f3cd3129398 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_scatter_atoms_subset]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[ndata]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ids]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv427lammps_scatter_atoms_subsetPvPKciiiPiPv "Link to this definition"){.headerlink}\

:   Scatter the named atom-based entities in *data* from a subset of atoms to all processes.

    This subroutine takes data stored in a one-dimensional array supplied by the user and scatters them to a subset of atoms on all processes. The array *data* contains data associated with atom IDs, but there is no requirement that the IDs be consecutive, as they are provided in a separate array. Use [[`lammps_scatter_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_scatter_atomsPvPKciiPv "lammps_scatter_atoms"){.reference .internal} to scatter data for all atoms, in order.

    The *data* array needs to be organized in groups of *count* values, with the groups in the same order as the array *ids*. For example, if you want *data* to be the array {x\[1\]\[0\], x\[1\]\[1\], x\[1\]\[2\], x\[100\]\[0\], x\[100\]\[1\], x\[100\]\[2\], x\[57\]\[0\], x\[57\]\[1\], x\[57\]\[2\]}, then *count* = 3, *ndata* = 3, and *ids* would be {1, 100, 57}.

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined and an [[atom map must be enabled]{.doc}]atom_modify.md){.reference .internal}

    The total number of atoms must not be more than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., *x* or *q*)

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *dtype* or *q*, 3 for *x* or *f*); use *count* = 3 with "image" if you have all the image flags packed into (*xyz*)

        - **ndata** -- number of atoms listed in *ids* and *data* arrays

        - **ids** -- list of *ndata* atom IDs to scatter data to

        - **data** -- per-atom values packed in a 1-dimensional array of length *ndata* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv319lammps_gather_bondsPvPv}[]{#_CPPv219lammps_gather_bondsPvPv}[]{#lammps_gather_bonds__voidP.voidP}[]{#library_8h_1a360d274b56e28d7a9fd0e195ff2171af .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather_bonds]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419lammps_gather_bondsPvPv "Link to this definition"){.headerlink}\

:   Gather type and constituent atom info for all bonds

    ::: versionadded
    [Added in version 28Jul2021.]{.versionmodified .added}
    :::

    This function copies the list of all bonds into a buffer provided by the calling code. The buffer will be filled with bond type, bond atom 1, bond atom 2 for each bond. Thus the buffer has to be allocated to the dimension of 3 times the **total** number of bonds times the size of the LAMMPS "tagint" type, which is either 4 or 8 bytes depending on whether they are stored in 32-bit or 64-bit integers, respectively. This size depends on the compile time settings used when compiling the LAMMPS library and can be queried by calling [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal} with the keyword "tagint".

    When running in parallel, the data buffer must be allocated on **all** MPI ranks and will be filled with the information for **all** bonds in the system.

    Below is a brief C code demonstrating accessing this collected bond information.

    :::: {.highlight-c .notranslate}
    ::: highlight
        #include "library.h"

        #include <stdint.h>
        #include <stdio.h>
        #include <stdlib.h>

        int main(int argc, char **argv)
        {
            int tagintsize;
            int64_t i, nbonds;
            void *handle, *bonds;

            handle = lammps_open_no_mpi(0, NULL, NULL);
            lammps_file(handle, "in.some_input");

            tagintsize = lammps_extract_setting(handle, "tagint");
            if (tagintsize == 4)
                nbonds = *(int32_t *)lammps_extract_global(handle, "nbonds");
             else
                nbonds = *(int64_t *)lammps_extract_global(handle, "nbonds");
            bonds = malloc(nbonds * 3 * tagintsize);

            lammps_gather_bonds(handle, bonds);

            if (lammps_extract_setting(handle, "world_rank") == 0) {
                if (tagintsize == 4) {
                    int32_t *bonds_real = (int32_t *)bonds;
                    for (i = 0; i < nbonds; ++i) {
                        printf("bond % 4ld: type = %d, atoms: % 4d  % 4d\n",i,
                               bonds_real[3*i], bonds_real[3*i+1], bonds_real[3*i+2]);
                    }
                } else {
                    int64_t *bonds_real = (int64_t *)bonds;
                    for (i = 0; i < nbonds; ++i) {
                        printf("bond % 4ld: type = %ld, atoms: % 4ld  % 4ld\n",i,
                               bonds_real[3*i], bonds_real[3*i+1], bonds_real[3*i+2]);
                    }
                }
            }

            lammps_close(handle);
            lammps_mpi_finalize();
            free(bonds);
            return 0;
        }
    :::
    ::::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **data** -- pointer to data to copy the result to

------------------------------------------------------------------------

[]{#_CPPv320lammps_gather_anglesPvPv}[]{#_CPPv220lammps_gather_anglesPvPv}[]{#lammps_gather_angles__voidP.voidP}[]{#library_8h_1a6f8c39008d113b5c3450c2cffaadcf3c .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather_angles]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420lammps_gather_anglesPvPv "Link to this definition"){.headerlink}\

:   Gather type and constituent atom info for all angles

    ::: versionadded
    [Added in version 8Feb2023.]{.versionmodified .added}
    :::

    This function copies the list of all angles into a buffer provided by the calling code. The buffer will be filled with angle type, angle atom 1, angle atom 2, angle atom 3 for each angle. Thus the buffer has to be allocated to the dimension of 4 times the **total** number of angles times the size of the LAMMPS "tagint" type, which is either 4 or 8 bytes depending on whether they are stored in 32-bit or 64-bit integers, respectively. This size depends on the compile time settings used when compiling the LAMMPS library and can be queried by calling [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal} with the keyword "tagint".

    When running in parallel, the data buffer must be allocated on **all** MPI ranks and will be filled with the information for **all** angles in the system.

    Below is a brief C code demonstrating accessing this collected angle information.

    :::: {.highlight-c .notranslate}
    ::: highlight
        #include "library.h"

        #include <stdint.h>
        #include <stdio.h>
        #include <stdlib.h>

        int main(int argc, char **argv)
        {
            int tagintsize;
            int64_t i, nangles;
            void *handle, *angles;

            handle = lammps_open_no_mpi(0, NULL, NULL);
            lammps_file(handle, "in.some_input");

            tagintsize = lammps_extract_setting(handle, "tagint");
            if (tagintsize == 4)
                nangles = *(int32_t *)lammps_extract_global(handle, "nangles");
             else
                nangles = *(int64_t *)lammps_extract_global(handle, "nangles");
            angles = malloc(nangles * 4 * tagintsize);

            lammps_gather_angles(handle, angles);

            if (lammps_extract_setting(handle, "world_rank") == 0) {
                if (tagintsize == 4) {
                    int32_t *angles_real = (int32_t *)angles;
                    for (i = 0; i < nangles; ++i) {
                        printf("angle % 4ld: type = %d, atoms: % 4d  % 4d  % 4d\n",i,
                               angles_real[4*i], angles_real[4*i+1], angles_real[4*i+2], angles_real[4*i+3]);
                    }
                } else {
                    int64_t *angles_real = (int64_t *)angles;
                    for (i = 0; i < nangles; ++i) {
                        printf("angle % 4ld: type = %ld, atoms: % 4ld  % 4ld  % 4ld\n",i,
                               angles_real[4*i], angles_real[4*i+1], angles_real[4*i+2], angles_real[4*i+3]);
                    }
                }
            }

            lammps_close(handle);
            lammps_mpi_finalize();
            free(angles);
            return 0;
        }
    :::
    ::::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **data** -- pointer to data to copy the result to

------------------------------------------------------------------------

[]{#_CPPv323lammps_gather_dihedralsPvPv}[]{#_CPPv223lammps_gather_dihedralsPvPv}[]{#lammps_gather_dihedrals__voidP.voidP}[]{#library_8h_1a93dac1f42646ebfa89521fc77a38a785 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather_dihedrals]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423lammps_gather_dihedralsPvPv "Link to this definition"){.headerlink}\

:   Gather type and constituent atom info for all dihedrals

    ::: versionadded
    [Added in version 8Feb2023.]{.versionmodified .added}
    :::

    This function copies the list of all dihedrals into a buffer provided by the calling code. The buffer will be filled with dihedral type, dihedral atom 1, dihedral atom 2, dihedral atom 3, dihedral atom 4 for each dihedral. Thus the buffer has to be allocated to the dimension of 5 times the **total** number of dihedrals times the size of the LAMMPS "tagint" type, which is either 4 or 8 bytes depending on whether they are stored in 32-bit or 64-bit integers, respectively. This size depends on the compile time settings used when compiling the LAMMPS library and can be queried by calling [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal} with the keyword "tagint".

    When running in parallel, the data buffer must be allocated on **all** MPI ranks and will be filled with the information for **all** dihedrals in the system.

    Below is a brief C code demonstrating accessing this collected dihedral information.

    :::: {.highlight-c .notranslate}
    ::: highlight
        #include "library.h"

        #include <stdint.h>
        #include <stdio.h>
        #include <stdlib.h>

        int main(int argc, char **argv)
        {
            int tagintsize;
            int64_t i, ndihedrals;
            void *handle, *dihedrals;

            handle = lammps_open_no_mpi(0, NULL, NULL);
            lammps_file(handle, "in.some_input");

            tagintsize = lammps_extract_setting(handle, "tagint");
            if (tagintsize == 4)
                ndihedrals = *(int32_t *)lammps_extract_global(handle, "ndihedrals");
             else
                ndihedrals = *(int64_t *)lammps_extract_global(handle, "ndihedrals");
            dihedrals = malloc(ndihedrals * 5 * tagintsize);

            lammps_gather_dihedrals(handle, dihedrals);

            if (lammps_extract_setting(handle, "world_rank") == 0) {
                if (tagintsize == 4) {
                    int32_t *dihedrals_real = (int32_t *)dihedrals;
                    for (i = 0; i < ndihedrals; ++i) {
                        printf("dihedral % 4ld: type = %d, atoms: % 4d  % 4d  % 4d  % 4d\n",i,
                               dihedrals_real[5*i], dihedrals_real[5*i+1], dihedrals_real[5*i+2], dihedrals_real[5*i+3], dihedrals_real[5*i+4]);
                    }
                } else {
                    int64_t *dihedrals_real = (int64_t *)dihedrals;
                    for (i = 0; i < ndihedrals; ++i) {
                        printf("dihedral % 4ld: type = %ld, atoms: % 4ld  % 4ld  % 4ld  % 4ld\n",i,
                               dihedrals_real[5*i], dihedrals_real[5*i+1], dihedrals_real[5*i+2], dihedrals_real[5*i+3], dihedrals_real[5*i+4]);
                    }
                }
            }

            lammps_close(handle);
            lammps_mpi_finalize();
            free(dihedrals);
            return 0;
        }
    :::
    ::::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **data** -- pointer to data to copy the result to

------------------------------------------------------------------------

[]{#_CPPv323lammps_gather_impropersPvPv}[]{#_CPPv223lammps_gather_impropersPvPv}[]{#lammps_gather_impropers__voidP.voidP}[]{#library_8h_1abf81ea4427e375c6605fb7362e995b92 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather_impropers]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423lammps_gather_impropersPvPv "Link to this definition"){.headerlink}\

:   Gather type and constituent atom info for all impropers

    ::: versionadded
    [Added in version 8Feb2023.]{.versionmodified .added}
    :::

    This function copies the list of all impropers into a buffer provided by the calling code. The buffer will be filled with improper type, improper atom 1, improper atom 2, improper atom 3, improper atom 4 for each improper. Thus the buffer has to be allocated to the dimension of 5 times the **total** number of impropers times the size of the LAMMPS "tagint" type, which is either 4 or 8 bytes depending on whether they are stored in 32-bit or 64-bit integers, respectively. This size depends on the compile time settings used when compiling the LAMMPS library and can be queried by calling [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal} with the keyword "tagint".

    When running in parallel, the data buffer must be allocated on **all** MPI ranks and will be filled with the information for **all** impropers in the system.

    Below is a brief C code demonstrating accessing this collected improper information.

    :::: {.highlight-c .notranslate}
    ::: highlight
        #include "library.h"

        #include <stdint.h>
        #include <stdio.h>
        #include <stdlib.h>

        int main(int argc, char **argv)
        {
            int tagintsize;
            int64_t i, nimpropers;
            void *handle, *impropers;

            handle = lammps_open_no_mpi(0, NULL, NULL);
            lammps_file(handle, "in.some_input");

            tagintsize = lammps_extract_setting(handle, "tagint");
            if (tagintsize == 4)
                nimpropers = *(int32_t *)lammps_extract_global(handle, "nimpropers");
             else
                nimpropers = *(int64_t *)lammps_extract_global(handle, "nimpropers");
            impropers = malloc(nimpropers * 5 * tagintsize);

            lammps_gather_impropers(handle, impropers);

            if (lammps_extract_setting(handle, "world_rank") == 0) {
                if (tagintsize == 4) {
                    int32_t *impropers_real = (int32_t *)impropers;
                    for (i = 0; i < nimpropers; ++i) {
                        printf("improper % 4ld: type = %d, atoms: % 4d  % 4d  % 4d  % 4d\n",i,
                               impropers_real[5*i], impropers_real[5*i+1], impropers_real[5*i+2], impropers_real[5*i+3], impropers_real[5*i+4]);
                    }
                } else {
                    int64_t *impropers_real = (int64_t *)impropers;
                    for (i = 0; i < nimpropers; ++i) {
                        printf("improper % 4ld: type = %ld, atoms: % 4ld  % 4ld  % 4ld  % 4ld\n",i,
                               impropers_real[5*i], impropers_real[5*i+1], impropers_real[5*i+2], impropers_real[5*i+3], impropers_real[5*i+4]);
                    }
                }
            }

            lammps_close(handle);
            lammps_mpi_finalize();
            free(impropers);
            return 0;
        }
    :::
    ::::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **data** -- pointer to data to copy the result to

------------------------------------------------------------------------

[]{#_CPPv313lammps_gatherPvPKciiPv}[]{#_CPPv213lammps_gatherPvPKciiPv}[]{#lammps_gather__voidP.cCP.i.i.voidP}[]{#library_8h_1aeaf5356f9fafd2fd9dbab0958a0a8ac3 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv413lammps_gatherPvPKciiPv "Link to this definition"){.headerlink}\

:   Gather the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entities from all processes, in order by atom ID.

    This subroutine gathers data from all processes and stores them in a one-dimensional array allocated by the user. The array *data* will be ordered by atom ID, which requires consecutive IDs (1 to *natoms*). If you need a similar array but for non-consecutive atom IDs, see [[`lammps_gather_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_gather_concatPvPKciiPv "lammps_gather_concat"){.reference .internal}; for a similar array but for a subset of atoms, see [[`lammps_gather_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_gather_subsetPvPKciiiPiPv "lammps_gather_subset"){.reference .internal}.

    The *data* array will be ordered in groups of *count* values, sorted by atom ID (e.g., if *name* is *x*, then *data* is {x\[0\]\[0\], x\[0\]\[1\], x\[0\]\[2\], x\[1\]\[0\], x\[1\]\[1\], x\[1\]\[2\], x\[2\]\[0\], [\\(\\dots\\)]{.math .notranslate .nohighlight}}); *data* must be pre-allocated by the caller to the correct length (*count*[\\({}\\times{}\\)]{.math .notranslate .nohighlight}*natoms*), as queried by [[`lammps_get_natoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_natomsPv "lammps_get_natoms"){.reference .internal}, [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal}, or [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal}.

    This function will return an error if fix or compute data are requested and the fix or compute ID given does not have per-atom data.

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined and must be consecutive.

    The total number of atoms must not be more than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., "x" or "f" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with *count* = 1, "d2_name" or "i2_name" for fix property/atom vectors with *count* \> 1)

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *type* or *q*, 3 for *x* or *f*); use *count* = 3 with *image* if you want the image flags unpacked into (*x*,*y*,*z*) components.

        - **data** -- per-atom values packed into a one-dimensional array of length *natoms* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv320lammps_gather_concatPvPKciiPv}[]{#_CPPv220lammps_gather_concatPvPKciiPv}[]{#lammps_gather_concat__voidP.cCP.i.i.voidP}[]{#library_8h_1add32cd75d71123448c752d69d96a9009 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather_concat]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420lammps_gather_concatPvPKciiPv "Link to this definition"){.headerlink}\

:   Gather the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entities from all processes, unordered.

    This subroutine gathers data for all atoms and stores them in a one-dimensional array allocated by the user. The data will be a concatenation of chunks from each processor's owned atoms, in whatever order the atoms are in on each processor. This process has no requirement that the atom IDs be consecutive. If you need the ID of each atom, you can do another call to either [[`lammps_gather_atoms_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_gather_atoms_concatPvPKciiPv "lammps_gather_atoms_concat"){.reference .internal} or [[`lammps_gather_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_gather_concatPvPKciiPv "lammps_gather_concat"){.reference .internal} with *name* set to [`id`{.docutils .literal .notranslate}]{.pre}. If you have consecutive IDs and want the data to be in order, use [[`lammps_gather()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv413lammps_gatherPvPKciiPv "lammps_gather"){.reference .internal}; for a similar array but for a subset of atoms, use [[`lammps_gather_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_gather_subsetPvPKciiiPiPv "lammps_gather_subset"){.reference .internal}.

    The *data* array will be in groups of *count* values, with *natoms* groups total, but not in order by atom ID (e.g., if *name* is *x* and *count* is 3, then *data* might be something like {x\[10\]\[0\], x\[10\]\[1\], x\[10\]\[2\], x\[2\]\[0\], x\[2\]\[1\], x\[2\]\[2\], x\[4\]\[0\], [\\(\\dots\\)]{.math .notranslate .nohighlight}}); *data* must be pre-allocated by the caller to length (*count* [\\(\\times\\)]{.math .notranslate .nohighlight} *natoms*), as queried by [[`lammps_get_natoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv417lammps_get_natomsPv "lammps_get_natoms"){.reference .internal}, [[`lammps_extract_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv421lammps_extract_globalPvPKc "lammps_extract_global"){.reference .internal}, or [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal}.

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined.

    The total number of atoms must be less than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., "x" or "f" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with count = 1, "d2_name" or "i2_name" for fix property/atom vectors with count \> 1)

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *type* or *q*, 3 for *x* or *f*); use *count* = 3 with *image* if you want the image flags unpacked into (*x*,*y*,*z*) components.

        - **data** -- per-atom values packed into a one-dimensional array of length *natoms* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv320lammps_gather_subsetPvPKciiiPiPv}[]{#_CPPv220lammps_gather_subsetPvPKciiiPiPv}[]{#lammps_gather_subset__voidP.cCP.i.i.i.iP.voidP}[]{#library_8h_1ab098fa5d18996508a54430ff5e3a0faf .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_gather_subset]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[ndata]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ids]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420lammps_gather_subsetPvPKciiiPiPv "Link to this definition"){.headerlink}\

:   Gather the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entities from all processes for a subset of atoms.

    This subroutine gathers data for the requested atom IDs and stores them in a one-dimensional array allocated by the user. The data will be ordered by atom ID, but there is no requirement that the IDs be consecutive. If you wish to return a similar array for *all* the atoms, use [[`lammps_gather()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv413lammps_gatherPvPKciiPv "lammps_gather"){.reference .internal} or [[`lammps_gather_concat()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_gather_concatPvPKciiPv "lammps_gather_concat"){.reference .internal}.

    The *data* array will be in groups of *count* values, sorted by atom ID in the same order as the array *ids* (e.g., if *name* is *x*, *count* = 3, and *ids* is {100, 57, 210}, then *data* might look like {x\[100\]\[0\], x\[100\]\[1\], x\[100\]\[2\], x\[57\]\[0\], x\[57\]\[1\], x\[57\]\[2\], x\[210\]\[0\], [\\(\\dots\\)]{.math .notranslate .nohighlight}}); *ids* must be provided by the user with length *ndata*, and *data* must be pre-allocated by the caller to length (*count*[\\({}\\times{}\\)]{.math .notranslate .nohighlight}*ndata*).

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined and an [[atom map must be enabled]{.doc}]atom_modify.md){.reference .internal}

    The total number of atoms must not be more than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., "x" or "f" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with *count* = 1, "d2_name" or "i2_name" for fix property/atom vectors with *count* \> 1)

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *type* or *q*, 3 for *x* or *f*); use *count* = 3 with *image* if you want the image flags unpacked into (*x*,*y*,*z*) components.

        - **ndata** -- number of atoms for which to return data (can be all of them)

        - **ids** -- list of *ndata* atom IDs for which to return data

        - **data** -- per-atom values packed into a one-dimensional array of length *ndata* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv314lammps_scatterPvPKciiPv}[]{#_CPPv214lammps_scatterPvPKciiPv}[]{#lammps_scatter__voidP.cCP.i.i.voidP}[]{#library_8h_1a1251a6d15588762a6810ed4021bfce11 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_scatter]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv414lammps_scatterPvPKciiPv "Link to this definition"){.headerlink}\

:   Scatter the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entity in *data* to all processes.

    This subroutine takes data stored in a one-dimensional array supplied by the user and scatters them to all atoms on all processes. The data must be ordered by atom ID, with the requirement that the IDs be consecutive. Use [[`lammps_scatter_subset()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_scatter_subsetPvPKciiiPiPv "lammps_scatter_subset"){.reference .internal} to scatter data for some (or all) atoms, unordered.

    The *data* array needs to be ordered in groups of *count* values, sorted by atom ID (e.g., if *name* is *x* and *count* = 3, then *data* = {x\[0\]\[0\], x\[0\]\[1\], x\[0\]\[2\], x\[1\]\[0\], x\[1\]\[1\], x\[1\]\[2\], x\[2\]\[0\], [\\(\\dots\\)]{.math .notranslate .nohighlight}}); *data* must be of length (*count* [\\(\\times\\)]{.math .notranslate .nohighlight} *natoms*).

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined, must be consecutive, and an [[atom map must be enabled]{.doc}]atom_modify.md){.reference .internal}

    The total number of atoms must not be more than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., "x" or "f" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with *count* = 1, "d2_name" or "i2_name" for fix property/atom vectors with *count* \> 1)

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *type* or *q*, 3 for *x* or *f*); use *count* = 3 with *image* if you have a single image flag packed into (*x*,*y*,*z*) components.

        - **data** -- per-atom values packed in a one-dimensional array of length *natoms* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv321lammps_scatter_subsetPvPKciiiPiPv}[]{#_CPPv221lammps_scatter_subsetPvPKciiiPiPv}[]{#lammps_scatter_subset__voidP.cCP.i.i.i.iP.voidP}[]{#library_8h_1ae379c37f2f8136e130030ddbe832695a .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_scatter_subset]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[count]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[ndata]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ids]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421lammps_scatter_subsetPvPKciiiPiPv "Link to this definition"){.headerlink}\

:   Scatter the named per-atom, per-atom fix, per-atom compute, or fix property/atom-based entities in *data* from a subset of atoms to all processes.

    This subroutine takes data stored in a one-dimensional array supplied by the user and scatters them to a subset of atoms on all processes. The array *data* contains data associated with atom IDs, but there is no requirement that the IDs be consecutive, as they are provided in a separate array. Use [[`lammps_scatter()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv414lammps_scatterPvPKciiPv "lammps_scatter"){.reference .internal} to scatter data for all atoms, in order.

    The *data* array needs to be organized in groups of *count* values, with the groups in the same order as the array *ids*. For example, if you want *data* to be the array {x\[1\]\[0\], x\[1\]\[1\], x\[1\]\[2\], x\[100\]\[0\], x\[100\]\[1\], x\[100\]\[2\], x\[57\]\[0\], x\[57\]\[1\], x\[57\]\[2\]}, then *count* = 3, *ndata* = 3, and *ids* would be {1, 100, 57}.

    ::: {.warning .admonition}
    Restrictions

    This function is not compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}.

    Atom IDs must be defined and an [[atom map must be enabled]{.doc}]atom_modify.md){.reference .internal}

    The total number of atoms must not be more than 2147483647 (max 32-bit signed int).
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **name** -- desired quantity (e.g., "x" or "f" for atom properties, "f_id" for per-atom fix data, "c_id" for per-atom compute data, "d_name" or "i_name" for fix property/atom vectors with *count* = 1, "d2_name" or "i2_name" for fix property/atom vectors with *count* \> 1)

        - **dtype** -- 0 for [`int`{.docutils .literal .notranslate}]{.pre} values, 1 for [`double`{.docutils .literal .notranslate}]{.pre} values

        - **count** -- number of per-atom values (e.g., 1 for *type* or *q*, 3 for *x* or *f*); use *count* = 3 with "image" if you want single image flags unpacked into (*x*,*y*,*z*)

        - **ndata** -- number of atoms listed in *ids* and *data* arrays

        - **ids** -- list of *ndata* atom IDs to scatter data to

        - **data** -- per-atom values packed in a 1-dimensional array of length *ndata* \* *count*.

------------------------------------------------------------------------

[]{#_CPPv319lammps_create_atomsPviPKiPKiPKdPKdPKii}[]{#_CPPv219lammps_create_atomsPviPKiPKiPKdPKdPKii}[]{#lammps_create_atoms__voidP.i.iCP.iCP.doubleCP.doubleCP.iCP.i}[]{#library_8h_1aeebd5ebadb0c014f80e2c25dd369ff44 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_create_atoms]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[n]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[x]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[v]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[image]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[bexpand]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419lammps_create_atomsPviPKiPKiPKdPKdPKii "Link to this definition"){.headerlink}\

:   Create N atoms from list of coordinates

    The prototype for this function when compiling with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} is:

    :::: {.highlight-c .notranslate}
    ::: highlight
        int lammps_create_atoms(void *handle, int n, int64_t *id, int *type, double *x, double *v, int64_t *image, int bexpand);
    :::
    ::::

    This function creates additional atoms from a given list of coordinates and a list of atom types. Additionally the atom-IDs, velocities, and image flags may be provided. If atom-IDs are not provided, they will be automatically created as a sequence following the largest existing atom-ID.

    This function is useful to add atoms to a simulation or - in tandem with [[`lammps_reset_box()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv416lammps_reset_boxPvPdPdddd "lammps_reset_box"){.reference .internal} - to restore a previously extracted and saved state of a simulation. Additional properties for the new atoms can then be assigned via the [[`lammps_scatter_atoms()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_scatter_atomsPvPKciiPv "lammps_scatter_atoms"){.reference .internal} [[`lammps_extract_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_atoms.md#_CPPv419lammps_extract_atomPvPKc "lammps_extract_atom"){.reference .internal} functions.

    For non-periodic boundaries, atoms will **not** be created that have coordinates outside the box unless it is a shrink-wrap boundary and the shrinkexceed flag has been set to a non-zero value. For periodic boundaries atoms will be wrapped back into the simulation cell and its image flags adjusted accordingly, unless explicit image flags are provided.

    The function returns the number of atoms created or -1 on failure (e.g., when called before as box has been created).

    Coordinates and velocities have to be given in a 1d-array in the order X(1), Y(1), Z(1), X(2), Y(2), Z(2), ..., X(N), Y(N), Z(N).

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **n** -- number of atoms, N, to be added to the system

        - **id** -- pointer to N atom IDs; [`NULL`{.docutils .literal .notranslate}]{.pre} will generate IDs

        - **type** -- pointer to N atom types (required)

        - **x** -- pointer to 3N doubles with x-,y-,z- positions of the new atoms (required)

        - **v** -- pointer to 3N doubles with x-,y-,z- velocities of the new atoms (set to 0.0 if [`NULL`{.docutils .literal .notranslate}]{.pre})

        - **image** -- pointer to N imageint sets of image flags, or [`NULL`{.docutils .literal .notranslate}]{.pre}

        - **bexpand** -- if 1, atoms outside of shrink-wrap boundaries will still be created and not dropped and the box extended

    Returns[:]{.colon}

    :   number of atoms created on success; -1 on failure (no box, no atom IDs, etc.)

------------------------------------------------------------------------

[]{#_CPPv322lammps_create_moleculePvPKcPKc}[]{#_CPPv222lammps_create_moleculePvPKcPKc}[]{#lammps_create_molecule__voidP.cCP.cCP}[]{#library_8h_1a7b7caa908362faf8ae99168df2e7420a .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_create_molecule]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[json]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422lammps_create_moleculePvPKcPKc "Link to this definition"){.headerlink}\

:   Create new molecule template from JSON data provided as C-style string

    ::: versionadded
    [Added in version 22Jul2025.]{.versionmodified .added}
    :::

    This function creates a new molecule template similar to the [[molecule command]{.doc}]molecule.md){.reference .internal}, but uses JSON data passed as a C-style string instead of reading it from a file.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **id** -- molecule-ID

        - **jsonstr** -- molecule data in JSON format as C-style string
:::
::::
:::::

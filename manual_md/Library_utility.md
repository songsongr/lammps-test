::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#utility-functions .section}
# [1.1.9. ]{.section-number}Utility functions[](#utility-functions "Link to this heading"){.headerlink}

To simplify some tasks, the library interface contains these utility functions. They do not directly call the LAMMPS library.

- [[`lammps_encode_image_flags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv425lammps_encode_image_flagsiii "lammps_encode_image_flags"){.reference .internal}

- [[`lammps_decode_image_flags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv425lammps_decode_image_flagsiPi "lammps_decode_image_flags"){.reference .internal}

- [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal}

- [[`lammps_fix_external_get_force()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_fix_external_get_forcePvPKc "lammps_fix_external_get_force"){.reference .internal}

- [[`lammps_fix_external_set_energy_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv437lammps_fix_external_set_energy_globalPvPKcd "lammps_fix_external_set_energy_global"){.reference .internal}

- [[`lammps_fix_external_set_energy_peratom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv438lammps_fix_external_set_energy_peratomPvPKcPd "lammps_fix_external_set_energy_peratom"){.reference .internal}

- [[`lammps_fix_external_set_virial_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv437lammps_fix_external_set_virial_globalPvPKcPd "lammps_fix_external_set_virial_global"){.reference .internal}

- [[`lammps_fix_external_set_virial_peratom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv438lammps_fix_external_set_virial_peratomPvPKcPPd "lammps_fix_external_set_virial_peratom"){.reference .internal}

- [[`lammps_fix_external_set_vector_length()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv437lammps_fix_external_set_vector_lengthPvPKci "lammps_fix_external_set_vector_length"){.reference .internal}

- [[`lammps_fix_external_set_vector()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv430lammps_fix_external_set_vectorPvPKcid "lammps_fix_external_set_vector"){.reference .internal}

- [[`lammps_flush_buffers()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_flush_buffersPv "lammps_flush_buffers"){.reference .internal}

- [[`lammps_free()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_freePv "lammps_free"){.reference .internal}

- [[`lammps_is_running()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv417lammps_is_runningPv "lammps_is_running"){.reference .internal}

- [[`lammps_force_timeout()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_force_timeoutPv "lammps_force_timeout"){.reference .internal}

- [[`lammps_has_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv416lammps_has_errorPv "lammps_has_error"){.reference .internal}

- [[`lammps_get_last_error_message()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_get_last_error_messagePvPci "lammps_get_last_error_message"){.reference .internal}

- [[`lammps_set_show_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_set_show_errorPvKi "lammps_set_show_error"){.reference .internal}

- [[`lammps_python_api_version()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv425lammps_python_api_versionv "lammps_python_api_version"){.reference .internal}

The [[`lammps_free()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_freePv "lammps_free"){.reference .internal} function is a clean-up function to free memory that the library had allocated previously via other function calls. Look for notes in the descriptions of the individual commands where such memory buffers were allocated that require the use of [[`lammps_free()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_freePv "lammps_free"){.reference .internal}.

------------------------------------------------------------------------

[]{#_CPPv325lammps_encode_image_flagsiii}[]{#_CPPv225lammps_encode_image_flagsiii}[]{#lammps_encode_image_flags__i.i.i}[]{#library_8h_1ad12aad3df456f3c85418ff8af6e55e10 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_encode_image_flags]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[ix]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[iy]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[iz]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv425lammps_encode_image_flagsiii "Link to this definition"){.headerlink}\

:   Encode three integer image flags into a single imageint.

    The prototype for this function when compiling with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} is:

    :::: {.highlight-c .notranslate}
    ::: highlight
        int64_t lammps_encode_image_flags(int ix, int iy, int iz);
    :::
    ::::

    This function performs the bit-shift, addition, and bit-wise OR operations necessary to combine the values of three integers representing the image flags in x-, y-, and z-direction. Unless LAMMPS is compiled with -DLAMMPS_BIGBIG, those integers are limited 10-bit signed integers \[-512, 511\]. Otherwise the return type changes from [`int`{.docutils .literal .notranslate}]{.pre} to [`int64_t`{.docutils .literal .notranslate}]{.pre} and the valid range for the individual image flags becomes \[-1048576,1048575\], i.e. that of a 21-bit signed integer. There is no check on whether the arguments conform to these requirements.

    Parameters[:]{.colon}

    :   - **ix** -- image flag value in x

        - **iy** -- image flag value in y

        - **iz** -- image flag value in z

    Returns[:]{.colon}

    :   encoded image flag integer

------------------------------------------------------------------------

[]{#_CPPv325lammps_decode_image_flagsiPi}[]{#_CPPv225lammps_decode_image_flagsiPi}[]{#lammps_decode_image_flags__i.iP}[]{#library_8h_1ae774bc2a40ffa11e7a7aecfac7a9c3c6 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_decode_image_flags]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[image]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[flags]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv425lammps_decode_image_flagsiPi "Link to this definition"){.headerlink}\

:   Decode a single image flag integer into three regular integers

    The prototype for this function when compiling with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre} is:

    :::: {.highlight-c .notranslate}
    ::: highlight
        void lammps_decode_image_flags(int64_t image, int *flags);
    :::
    ::::

    This function does the reverse operation of [[`lammps_encode_image_flags()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv425lammps_encode_image_flagsiii "lammps_encode_image_flags"){.reference .internal} and takes an image flag integer does the bit-shift and bit-masking operations to decode it and stores the resulting three regular integers into the buffer pointed to by *flags*.

    Parameters[:]{.colon}

    :   - **image** -- encoded image flag integer

        - **flags** -- pointer to storage where the decoded image flags are stored.

------------------------------------------------------------------------

[]{#_CPPv332lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv}[]{#_CPPv232lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv}[]{#lammps_set_fix_external_callback__voidP.cCP.FixExternalFnPtr.voidP}[]{#library_8h_1a2b2994fdf05652cb2f3fe2afc4d00d1a .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_set_fix_external_callback]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[FixExternalFnPtr]{.pre}]{.n}[ ]{.w}[[funcptr]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ptr]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "Link to this definition"){.headerlink}\

:   Set up the callback function for a fix external instance with the given ID.

    Fix [[external]{.doc}]fix_external.md){.reference .internal} allows programs that are running LAMMPS through its library interface to modify certain LAMMPS properties on specific timesteps, similar to the way other fixes do.

    This function sets the callback function for use with the "pf/callback" mode. The function has to have C language bindings with the prototype:

    :::: {.highlight-c .notranslate}
    ::: highlight
        void func(void *ptr, bigint timestep, int nlocal, tagint *ids, double **x, double **fexternal);
    :::
    ::::

    The argument *ptr* to this function will be stored in fix external and the passed as the first argument calling the callback function func(). This would usually be a pointer to the active LAMMPS instance, i.e. the same pointer as the *handle* argument. This would be needed to call functions that set the global or per-atom energy or virial contributions from within the callback function.

    The callback mechanism is one of the two modes of how forces and can be applied to a simulation with the help of fix external. The alternative is the array mode where you call [[`lammps_fix_external_get_force()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_fix_external_get_forcePvPKc "lammps_fix_external_get_force"){.reference .internal}.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    ::: versionchanged
    [Changed in version 28Jul2021.]{.versionmodified .changed}
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **id** -- fix ID of fix external instance

        - **funcptr** -- pointer to callback function

        - **ptr** -- pointer to object in calling code, passed to callback function as first argument

------------------------------------------------------------------------

[]{#_CPPv329lammps_fix_external_get_forcePvPKc}[]{#_CPPv229lammps_fix_external_get_forcePvPKc}[]{#lammps_fix_external_get_force__voidP.cCP}[]{#library_8h_1a3e5a4c1f126c6b6cdd756f99764e69d7 .target}[[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[[lammps_fix_external_get_force]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv429lammps_fix_external_get_forcePvPKc "Link to this definition"){.headerlink}\

:   Get pointer to the force array storage in a fix external instance with the given ID.

    ::: versionadded
    [Added in version 28Jul2021.]{.versionmodified .added}
    :::

    Fix [[external]{.doc}]fix_external.md){.reference .internal} allows programs that are running LAMMPS through its library interface to add or modify certain LAMMPS properties on specific timesteps, similar to the way other fixes do.

    This function provides access to the per-atom force storage in a fix external instance with the given fix-ID to be added to the individual atoms when using the "pf/array" mode. The *fexternal* array can be accessed like other "native" per-atom arrays accessible via the [[`lammps_extract_atom()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_atoms.md#_CPPv419lammps_extract_atomPvPKc "lammps_extract_atom"){.reference .internal} function. Please note that the array stores holds the forces for *local* atoms for each MPI ranks, in the order determined by the neighbor list build. Because the underlying data structures can change as well as the order of atom as they migrate between MPI processes because of the domain decomposition parallelization, this function should be always called immediately before the forces are going to be set to get an up-to-date pointer. You can use, for example, [[`lammps_extract_setting()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_properties.md#_CPPv422lammps_extract_settingPvPKc "lammps_extract_setting"){.reference .internal} to obtain the number of local atoms nlocal and then assume the dimensions of the returned force array as [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`force[nlocal][3]`{.docutils .literal .notranslate}]{.pre}.

    This is an alternative to the callback mechanism in fix external set up by [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal}. The main difference is that this mechanism can be used when forces are be pre-computed and the control alternates between LAMMPS and the external code, while the callback mechanism can call the external code to compute the force when the fix is triggered and needs them.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **id** -- fix ID of fix external instance

    Returns[:]{.colon}

    :   a pointer to the per-atom force array allocated by the fix

------------------------------------------------------------------------

[]{#_CPPv337lammps_fix_external_set_energy_globalPvPKcd}[]{#_CPPv237lammps_fix_external_set_energy_globalPvPKcd}[]{#lammps_fix_external_set_energy_global__voidP.cCP.double}[]{#library_8h_1a6ac4888e2c82846dcb9b1d013ef90f96 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_fix_external_set_energy_global]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[eng]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv437lammps_fix_external_set_energy_globalPvPKcd "Link to this definition"){.headerlink}\

:   Set the global energy contribution for a fix external instance with the given ID.

    ::: versionadded
    [Added in version 28Jul2021.]{.versionmodified .added}
    :::

    This is a companion function to [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal} and [[`lammps_fix_external_get_force()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_fix_external_get_forcePvPKc "lammps_fix_external_get_force"){.reference .internal} to also set the contribution to the global energy from the external code. The value of the *eng* argument will be stored in the fix and applied on the current and all following timesteps until changed by another call to this function. The energy is in energy units as determined by the current [[units]{.doc}]units.md){.reference .internal} settings and is the **total** energy of the contribution. Thus when running in parallel all MPI processes have to call this function with the **same** value and this will be returned as scalar property of the fix external instance when accessed in LAMMPS input commands or from variables.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **id** -- fix ID of fix external instance

        - **eng** -- total energy to be added to the global energy

------------------------------------------------------------------------

[]{#_CPPv338lammps_fix_external_set_energy_peratomPvPKcPd}[]{#_CPPv238lammps_fix_external_set_energy_peratomPvPKcPd}[]{#lammps_fix_external_set_energy_peratom__voidP.cCP.doubleP}[]{#library_8h_1aac2c2027c2779613dfe2ffa47205bbdf .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_fix_external_set_energy_peratom]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[eng]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv438lammps_fix_external_set_energy_peratomPvPKcPd "Link to this definition"){.headerlink}\

:   Set the per-atom energy contribution for a fix external instance with the given ID.

    ::: versionadded
    [Added in version 28Jul2021.]{.versionmodified .added}
    :::

    This is a companion function to [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal} to set the per-atom energy contribution due to the fix from the external code as part of the callback function. For this to work, the handle to the LAMMPS object must be passed as the *ptr* argument when registering the callback function.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    ::: {.admonition .note}
    Note

    This function is fully independent from [[`lammps_fix_external_set_energy_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv437lammps_fix_external_set_energy_globalPvPKcd "lammps_fix_external_set_energy_global"){.reference .internal} and will **NOT** add any contributions to the global energy tally and **NOT** check whether the sum of the contributions added here are consistent with the global added energy.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **id** -- fix ID of fix external instance

        - **eng** -- pointer to array of length nlocal with the energy to be added to the per-atom energy

------------------------------------------------------------------------

[]{#_CPPv337lammps_fix_external_set_virial_globalPvPKcPd}[]{#_CPPv237lammps_fix_external_set_virial_globalPvPKcPd}[]{#lammps_fix_external_set_virial_global__voidP.cCP.doubleP}[]{#library_8h_1af707a45ddf44addec9b8345546deb83e .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_fix_external_set_virial_global]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[virial]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv437lammps_fix_external_set_virial_globalPvPKcPd "Link to this definition"){.headerlink}\

:   Set the global virial contribution for a fix external instance with the given ID.

    ::: versionadded
    [Added in version 28Jul2021.]{.versionmodified .added}
    :::

    This is a companion function to [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal} and [[`lammps_fix_external_get_force()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_fix_external_get_forcePvPKc "lammps_fix_external_get_force"){.reference .internal} to set the contribution to the global virial from the external code.

    The 6 values of the *virial* array will be stored in the fix and applied on the current and all following timesteps until changed by another call to this function. The components of the virial need to be stored in the order: *xx*, *yy*, *zz*, *xy*, *xz*, *yz*. In LAMMPS the virial is stored internally as stress\*volume in units of pressure\*volume as determined by the current [[units]{.doc}]units.md){.reference .internal} settings and is the **total** contribution. Thus when running in parallel all MPI processes have to call this function with the **same** value and this will then be added by fix external.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **id** -- fix ID of fix external instance

        - **virial** -- the 6 global stress tensor components to be added to the global virial

------------------------------------------------------------------------

[]{#_CPPv338lammps_fix_external_set_virial_peratomPvPKcPPd}[]{#_CPPv238lammps_fix_external_set_virial_peratomPvPKcPPd}[]{#lammps_fix_external_set_virial_peratom__voidP.cCP.doublePP}[]{#library_8h_1ae85311d7c556c3c7aace6e329ab352a2 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_fix_external_set_virial_peratom]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[virial]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv438lammps_fix_external_set_virial_peratomPvPKcPPd "Link to this definition"){.headerlink}\

:   Set the per-atom virial contribution for a fix external instance with the given ID.

    ::: versionadded
    [Added in version 28Jul2021.]{.versionmodified .added}
    :::

    This is a companion function to [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal} to set the per-atom virial contribution due to the fix from the external code as part of the callback function. For this to work, the handle to the LAMMPS object must be passed as the *ptr* argument when registering the callback function.

    The order and units of the per-atom stress tensor elements are the same as for the global virial. The code in fix external assumes the dimensions of the per-atom virial array is [`double`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`virial[nlocal][6]`{.docutils .literal .notranslate}]{.pre}.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    ::: {.admonition .note}
    Note

    This function is fully independent from [[`lammps_fix_external_set_virial_global()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv437lammps_fix_external_set_virial_globalPvPKcPd "lammps_fix_external_set_virial_global"){.reference .internal} and will **NOT** add any contributions to the global virial tally and **NOT** check whether the sum of the contributions added here are consistent with the global added virial.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **id** -- fix ID of fix external instance

        - **virial** -- a list of nlocal entries with the 6 per-atom stress tensor components to be added to the per-atom virial

------------------------------------------------------------------------

[]{#_CPPv337lammps_fix_external_set_vector_lengthPvPKci}[]{#_CPPv237lammps_fix_external_set_vector_lengthPvPKci}[]{#lammps_fix_external_set_vector_length__voidP.cCP.i}[]{#library_8h_1a65eccbce0a2c1154051c56296acc7598 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_fix_external_set_vector_length]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[len]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv437lammps_fix_external_set_vector_lengthPvPKci "Link to this definition"){.headerlink}\

:   Set the vector length for a global vector stored with fix external for analysis

    ::: versionadded
    [Added in version 28Jul2021.]{.versionmodified .added}
    :::

    This is a companion function to [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal} and [[`lammps_fix_external_get_force()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_fix_external_get_forcePvPKc "lammps_fix_external_get_force"){.reference .internal} to set the length of a global vector of properties that will be stored with the fix via [[`lammps_fix_external_set_vector()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv430lammps_fix_external_set_vectorPvPKcid "lammps_fix_external_set_vector"){.reference .internal}.

    This function needs to be called **before** a call to [[`lammps_fix_external_set_vector()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv430lammps_fix_external_set_vectorPvPKcid "lammps_fix_external_set_vector"){.reference .internal} and **before** a run or minimize command. When running in parallel it must be called from **all** MPI processes and with the same length parameter.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **id** -- fix ID of fix external instance

        - **len** -- length of the global vector to be stored with the fix

------------------------------------------------------------------------

[]{#_CPPv330lammps_fix_external_set_vectorPvPKcid}[]{#_CPPv230lammps_fix_external_set_vectorPvPKcid}[]{#lammps_fix_external_set_vector__voidP.cCP.i.double}[]{#library_8h_1a627a37da0a0f1cd076cfac35ea488c18 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_fix_external_set_vector]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[id]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[idx]{.pre}]{.n .sig-param}, [[double]{.pre}]{.kt}[ ]{.w}[[val]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv430lammps_fix_external_set_vectorPvPKcid "Link to this definition"){.headerlink}\

:   Store a global vector value for a fix external instance with the given ID.

    ::: versionadded
    [Added in version 28Jul2021.]{.versionmodified .added}
    :::

    This is a companion function to [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal} and [[`lammps_fix_external_get_force()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_fix_external_get_forcePvPKc "lammps_fix_external_get_force"){.reference .internal} to set the values of a global vector of properties that will be stored with the fix. And can be accessed from within LAMMPS input commands (e.g., fix ave/time or variables) when used in a vector context.

    This function needs to be called **after** a call to [[`lammps_fix_external_set_vector_length()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv437lammps_fix_external_set_vector_lengthPvPKci "lammps_fix_external_set_vector_length"){.reference .internal} and the and **before** a run or minimize command. When running in parallel it must be called from **all** MPI processes and with the **same** index and value parameters. The value is assumed to be extensive.

    Please see the documentation for [[fix external]{.doc}]fix_external.md){.reference .internal} for more information about how to use the fix and how to couple it with an external code.

    ::: {.admonition .note}
    Note

    The index in the *idx* parameter is 1-based, i.e. the first element is set with idx = 1 and the last element of the vector with idx = N, where N is the value of the *len* parameter of the call to [[`lammps_fix_external_set_vector_length()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv437lammps_fix_external_set_vector_lengthPvPKci "lammps_fix_external_set_vector_length"){.reference .internal}.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **id** -- fix ID of fix external instance

        - **idx** -- 1-based index of in global vector

        - **val** -- value to be stored in global vector

------------------------------------------------------------------------

[]{#_CPPv320lammps_flush_buffersPv}[]{#_CPPv220lammps_flush_buffersPv}[]{#lammps_flush_buffers__voidP}[]{#library_8h_1af54eb973fef3aa2bfe7708a0cf1139ff .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_flush_buffers]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ptr]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420lammps_flush_buffersPv "Link to this definition"){.headerlink}\

:   Flush output buffers

    This function can be used to flush buffered output to be written to screen and logfile pointers to simplify capturing output from LAMMPS library calls.

    Parameters[:]{.colon}

    :   **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

------------------------------------------------------------------------

[]{#_CPPv311lammps_freePv}[]{#_CPPv211lammps_freePv}[]{#lammps_free__voidP}[]{#library_8h_1aa521d27718fc92e9a58a255ae9f9cf87 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_free]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[ptr]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv411lammps_freePv "Link to this definition"){.headerlink}\

:   Free memory buffer allocated by [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal}.

    Some of the LAMMPS C library interface functions return data as pointer to a buffer that has been allocated by LAMMPS or the library interface. This function can be used to delete those in order to avoid memory leaks.

    Parameters[:]{.colon}

    :   **ptr** -- pointer to data allocated by [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal}

------------------------------------------------------------------------

[]{#_CPPv317lammps_is_runningPv}[]{#_CPPv217lammps_is_runningPv}[]{#lammps_is_running__voidP}[]{#library_8h_1a96130bd0ac1fcfbb01f56fe92f8cf7da .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_is_running]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv417lammps_is_runningPv "Link to this definition"){.headerlink}\

:   Check if [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} is currently inside a run or minimization

    This function can be used from signal handlers or multi-threaded applications to determine if the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance is currently active.

    Parameters[:]{.colon}

    :   **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

    Returns[:]{.colon}

    :   0 if idle or \>0 if active

------------------------------------------------------------------------

[]{#_CPPv320lammps_force_timeoutPv}[]{#_CPPv220lammps_force_timeoutPv}[]{#lammps_force_timeout__voidP}[]{#library_8h_1a298dbff8f43185d82bcbf0a8d76b9aa9 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_force_timeout]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420lammps_force_timeoutPv "Link to this definition"){.headerlink}\

:   Force a timeout to stop an ongoing run cleanly.

    This function can be used from signal handlers or multi-threaded applications to cleanly terminate an ongoing run.

    Parameters[:]{.colon}

    :   **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

[]{#_CPPv316lammps_has_errorPv}[]{#_CPPv216lammps_has_errorPv}[]{#lammps_has_error__voidP}[]{#library_8h_1a6f2f23eeafb8d56983ef90ad55e0c37d .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_has_error]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv416lammps_has_errorPv "Link to this definition"){.headerlink}\

:   Check if there is a (new) error message available

    This function can be used to query if an error inside of LAMMPS has thrown a [[C++ exception]{.std .std-ref}]Build_settings.md#exceptions){.reference .internal}.

    :::: {.admonition .note}
    Note

    ::: versionchanged
    [Changed in version 2Aug2023.]{.versionmodified .changed}
    :::

    The *handle* pointer may be [`NULL`{.docutils .literal .notranslate}]{.pre} for this function, as would be the case when a call to create a LAMMPS instance has failed. Then this function will not check the error status inside the LAMMPS instance, but instead would check the global error buffer of the library interface.
    ::::

    Parameters[:]{.colon}

    :   **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} or NULL

    Returns[:]{.colon}

    :   0 on no error, 1 on error.

------------------------------------------------------------------------

[]{#_CPPv329lammps_get_last_error_messagePvPci}[]{#_CPPv229lammps_get_last_error_messagePvPci}[]{#lammps_get_last_error_message__voidP.cP.i}[]{#library_8h_1a1900bdb6311f7f9649b5c82e20257cff .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_get_last_error_message]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[buffer]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[buf_size]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv429lammps_get_last_error_messagePvPci "Link to this definition"){.headerlink}\

:   Copy the last error message into the provided buffer

    This function can be used to retrieve the error message that was set in the event of an error inside of LAMMPS which resulted in a [[C++ exception]{.std .std-ref}]Build_settings.md#exceptions){.reference .internal}. A suitable buffer for a C-style string has to be provided and its length. If the internally stored error message is longer, it will be truncated accordingly. If the buffer is a NULL pointer, then nothing will be copied. The return value of the function corresponds to the kind of error: a "1" indicates an error that occurred on all MPI ranks and is often recoverable, while a "2" indicates an abort that would happen only in a single MPI rank and thus may not be recoverable, as other MPI ranks may be waiting on the failing MPI ranks to send messages.

    ::::: {.admonition .note}
    Note

    ::: versionchanged
    [Changed in version 2Aug2023.]{.versionmodified .changed}
    :::

    The *handle* pointer may be [`NULL`{.docutils .literal .notranslate}]{.pre} for this function, as would be the case when a call to create a LAMMPS instance has failed. Then this function will not check the error buffer inside the LAMMPS instance, but instead would check the global error buffer of the library interface.

    ::: versionchanged
    [Changed in version 21Nov2023.]{.versionmodified .changed}
    :::

    The *buffer* pointer may be [`NULL`{.docutils .literal .notranslate}]{.pre}. This will clear any error status without copying the error message.
    :::::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} or NULL.

        - **buffer** -- string buffer to copy the error message to, may be NULL

        - **buf_size** -- size of the provided string buffer

    Returns[:]{.colon}

    :   1 when all ranks had the error, 2 on a single rank error.

------------------------------------------------------------------------

[]{#_CPPv321lammps_set_show_errorPvKi}[]{#_CPPv221lammps_set_show_errorPvKi}[]{#lammps_set_show_error__voidP.iC}[]{#library_8h_1a169a51e4853a187e9d5f2ebf05f01ca5 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_set_show_error]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[flag]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421lammps_set_show_errorPvKi "Link to this definition"){.headerlink}\

:   Enable or disable direct printing of error messages

    ::: versionadded
    [Added in version 2Apr2025.]{.versionmodified .added}
    :::

    This function can be used to stop LAMMPS from printing error messages *before* LAMMPS throws a [[C++ exception]{.std .std-ref}]Build_settings.md#exceptions){.reference .internal}. This is so it may be left to the code calling the library interface whether to check for them, and retrieve and print error messages using the library interface functions [[`lammps_has_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv416lammps_has_errorPv "lammps_has_error"){.reference .internal} and [[`lammps_get_last_error_message()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_get_last_error_messagePvPci "lammps_get_last_error_message"){.reference .internal}. The function returns the previous setting so that one can easily override the setting temporarily and restore it afterwards.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre} or NULL

        - **flag** -- enable (not 0) or disable (0) printing error messages before throwing exception

    Returns[:]{.colon}

    :   previous setting of the flag

------------------------------------------------------------------------

[]{#_CPPv325lammps_python_api_versionv}[]{#_CPPv225lammps_python_api_versionv}[]{#lammps_python_api_version}[]{#library_8h_1ac696ed37ed39b295adbf05577111da90 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_python_api_version]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv425lammps_python_api_versionv "Link to this definition"){.headerlink}\

:   Return API version of embedded Python interpreter

    ::: versionadded
    [Added in version 3Nov2022.]{.versionmodified .added}
    :::

    This function is used by the ML-IAP python code (mliappy) to verify the API version of the embedded python interpreter of the PYTHON package. It returns -1 if the PYTHON package is not enabled.

    Returns[:]{.colon}

    :   PYTHON_API_VERSION constant of the python interpreter or -1
:::
::::
:::::

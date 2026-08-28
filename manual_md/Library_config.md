::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::: {#configuration-information .section}
# [1.1.8. ]{.section-number}Configuration information[](#configuration-information "Link to this heading"){.headerlink}

This section documents the following functions:

- [[`lammps_version()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv414lammps_versionPv "lammps_version"){.reference .internal}

- [[`lammps_get_os_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_get_os_infoPci "lammps_get_os_info"){.reference .internal}

- [[`lammps_config_has_mpi_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_config_has_mpi_supportv "lammps_config_has_mpi_support"){.reference .internal}

- [[`lammps_config_has_omp_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_config_has_omp_supportv "lammps_config_has_omp_support"){.reference .internal}

- [[`lammps_config_has_gzip_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv430lammps_config_has_gzip_supportv "lammps_config_has_gzip_support"){.reference .internal}

- [[`lammps_config_has_png_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_config_has_png_supportv "lammps_config_has_png_support"){.reference .internal}

- [[`lammps_config_has_jpeg_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv430lammps_config_has_jpeg_supportv "lammps_config_has_jpeg_support"){.reference .internal}

- [[`lammps_config_has_ffmpeg_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv432lammps_config_has_ffmpeg_supportv "lammps_config_has_ffmpeg_support"){.reference .internal}

- [[`lammps_config_has_exceptions()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv428lammps_config_has_exceptionsv "lammps_config_has_exceptions"){.reference .internal}

- [[`lammps_config_has_package()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv425lammps_config_has_packagePKc "lammps_config_has_package"){.reference .internal}

- [[`lammps_config_package_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv427lammps_config_package_countv "lammps_config_package_count"){.reference .internal}

- [[`lammps_config_package_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_config_package_nameiPci "lammps_config_package_name"){.reference .internal}

- [[`lammps_config_accelerator()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv425lammps_config_acceleratorPKcPKcPKc "lammps_config_accelerator"){.reference .internal}

- [[`lammps_has_gpu_device()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_has_gpu_devicev "lammps_has_gpu_device"){.reference .internal}

- [`lammps_gpu_device_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}

- [[`lammps_has_style()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv416lammps_has_stylePvPKcPKc "lammps_has_style"){.reference .internal}

- [[`lammps_style_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_style_countPvPKc "lammps_style_count"){.reference .internal}

- [[`lammps_style_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv417lammps_style_namePvPKciPci "lammps_style_name"){.reference .internal}

- [[`lammps_has_id()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv413lammps_has_idPvPKcPKc "lammps_has_id"){.reference .internal}

- [[`lammps_id_count()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv415lammps_id_countPvPKc "lammps_id_count"){.reference .internal}

- [[`lammps_id_name()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv414lammps_id_namePvPKciPci "lammps_id_name"){.reference .internal}

------------------------------------------------------------------------

These library functions can be used to query the LAMMPS library for compile time settings and included packages and styles. This enables programs that use the library interface to determine whether the linked LAMMPS library is compatible with the requirements of the application without crashing during the LAMMPS functions (e.g. due to missing pair styles from packages) or to choose between different options (e.g. whether to use [`lj/cut`{.docutils .literal .notranslate}]{.pre}, [`lj/cut/opt`{.docutils .literal .notranslate}]{.pre}, [`lj/cut/omp`{.docutils .literal .notranslate}]{.pre} or [`lj/cut/intel`{.docutils .literal .notranslate}]{.pre}). Most of the functions can be called directly without first creating a LAMMPS instance. While crashes within LAMMPS may be recovered from by enabling [[exceptions]{.std .std-ref}]Build_settings.md#exceptions){.reference .internal}, avoiding them proactively is a safer approach.

:::::: {#id1 .literal-block-wrapper .docutils .container}
::: code-block-caption
[Example for using configuration settings functions]{.caption-text}[](#id1 "Link to this code"){.headerlink}
:::

:::: {.highlight-c .notranslate}
::: highlight
    #include "library.h"
    #include <stdio.h>

    int main(int argc, char **argv)
    {
      void *handle;

      handle = lammps_open_no_mpi(0, NULL, NULL);
      lammps_file(handle, "in.missing");
      if (lammps_has_error(handle)) {
        char errmsg[256];
        int errtype;
        errtype = lammps_get_last_error_message(handle, errmsg, 256);
        fprintf(stderr, "LAMMPS failed with error: %s\n", errmsg);
        return 1;
      }
      /* write compressed dump file depending on available of options */
      if (lammps_has_style(handle, "dump", "atom/zstd")) {
        lammps_command(handle, "dump d1 all atom/zstd 100 dump.zst");
      } else if (lammps_has_style(handle, "dump", "atom/gz")) {
        lammps_command(handle, "dump d1 all atom/gz 100 dump.gz");
      } else if (lammps_config_has_gzip_support()) {
        lammps_command(handle, "dump d1 all atom 100 dump.gz");
      } else {
        lammps_command(handle, "dump d1 all atom 100 dump");
      }
      lammps_close(handle);
      return 0;
    }
:::
::::
::::::

------------------------------------------------------------------------

[]{#_CPPv314lammps_versionPv}[]{#_CPPv214lammps_versionPv}[]{#lammps_version__voidP}[]{#library_8h_1a41f44a4eef975f8a189d3186259a8ef9 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_version]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv414lammps_versionPv "Link to this definition"){.headerlink}\

:   Get numerical representation of the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} version date.

    The [[`lammps_version()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv414lammps_versionPv "lammps_version"){.reference .internal} function returns an integer representing the version of the LAMMPS code in the format YYYYMMDD. This can be used to implement backward compatibility in software using the LAMMPS library interface. The specific format guarantees, that this version number is growing with every new LAMMPS release.

    Parameters[:]{.colon}

    :   **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

    Returns[:]{.colon}

    :   an integer representing the version data in the format YYYYMMDD

------------------------------------------------------------------------

[]{#_CPPv318lammps_get_os_infoPci}[]{#_CPPv218lammps_get_os_infoPci}[]{#lammps_get_os_info__cP.i}[]{#library_8h_1ae4b6178f693ff83002ee8a1559edd6ed .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_get_os_info]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[buffer]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[buf_size]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv418lammps_get_os_infoPci "Link to this definition"){.headerlink}\

:   Get operating system and architecture information

    ::: versionadded
    [Added in version 9Oct2020.]{.versionmodified .added}
    :::

    The [[`lammps_get_os_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv418lammps_get_os_infoPci "lammps_get_os_info"){.reference .internal} function can be used to retrieve detailed information about the hosting operating system and compiler/runtime.

    A suitable buffer for a C-style string has to be provided and its length. The assembled text will be truncated to not overflow this buffer. The string is typically a few hundred bytes long.

    Parameters[:]{.colon}

    :   - **buffer** -- string buffer to copy the information to

        - **buf_size** -- size of the provided string buffer

------------------------------------------------------------------------

[]{#_CPPv329lammps_config_has_mpi_supportv}[]{#_CPPv229lammps_config_has_mpi_supportv}[]{#lammps_config_has_mpi_support}[]{#library_8h_1ada45e7d079fddf8400e31cc98710b5f8 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_has_mpi_support]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv429lammps_config_has_mpi_supportv "Link to this definition"){.headerlink}\

:   This function is used to query whether [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} was compiled with a real MPI library or in serial. For the real MPI library it reports the size of the MPI communicator in bytes (4 or 8), which allows to check for compatibility with a hosting code.

    Returns[:]{.colon}

    :   0 when compiled with MPI STUBS, otherwise the MPI_Comm size in bytes

------------------------------------------------------------------------

[]{#_CPPv329lammps_config_has_omp_supportv}[]{#_CPPv229lammps_config_has_omp_supportv}[]{#lammps_config_has_omp_support}[]{#library_8h_1a0660c97f79fa11df21ecc4b13ef451f2 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_has_omp_support]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv429lammps_config_has_omp_supportv "Link to this definition"){.headerlink}\

:   This function is used to query whether [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} was compiled with OpenMP enabled.

    ::: versionadded
    [Added in version 10Sep2025.]{.versionmodified .added}
    :::

    *See also*

    :   [[`lammps_config_has_mpi_support()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv429lammps_config_has_mpi_supportv "lammps_config_has_mpi_support"){.reference .internal}

    Returns[:]{.colon}

    :   1 when compiled with OpenMP enabled, otherwise 0

------------------------------------------------------------------------

[]{#_CPPv330lammps_config_has_gzip_supportv}[]{#_CPPv230lammps_config_has_gzip_supportv}[]{#lammps_config_has_gzip_support}[]{#library_8h_1a0bd41d39a5dd5992d614e150b6d88a5f .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_has_gzip_support]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv430lammps_config_has_gzip_supportv "Link to this definition"){.headerlink}\

:   Check if the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} library supports reading or writing compressed files via a pipe to gzip or similar compression programs

    Several LAMMPS commands (e.g., [[read_data command]{.doc}]read_data.md){.reference .internal}, [[write_data command]{.doc}]write_data.md){.reference .internal}, [[dump styles atom, custom, and xyz]{.doc}]dump.md){.reference .internal}) support reading and writing compressed files via creating a pipe to the [`gzip`{.docutils .literal .notranslate}]{.pre} program. This function checks whether this feature was [[enabled at compile time]{.std .std-ref}]Build_settings.md#gzip){.reference .internal}. It does **not** check whether\`\`gzip\`\` or any other supported compression programs themselves are installed and usable.

    Returns[:]{.colon}

    :   1 if yes, otherwise 0

------------------------------------------------------------------------

[]{#_CPPv329lammps_config_has_png_supportv}[]{#_CPPv229lammps_config_has_png_supportv}[]{#lammps_config_has_png_support}[]{#library_8h_1a9de61d7686a3db2344fb94a4a22c67e4 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_has_png_support]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv429lammps_config_has_png_supportv "Link to this definition"){.headerlink}\

:   Check if the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} library supports writing PNG format images

    The LAMMPS [[dump style image]{.doc}]dump_image.md){.reference .internal} supports writing multiple image file formats. Most of them, however, need support from an external library, and using that has to be [[enabled at compile time]{.std .std-ref}]Build_extras.md#graphics){.reference .internal}. This function checks whether support for the [PNG image file format](https://en.wikipedia.org/wiki/Portable_Network_Graphics){.reference .external} is available in the current LAMMPS library.

    Returns[:]{.colon}

    :   1 if yes, otherwise 0

------------------------------------------------------------------------

[]{#_CPPv330lammps_config_has_jpeg_supportv}[]{#_CPPv230lammps_config_has_jpeg_supportv}[]{#lammps_config_has_jpeg_support}[]{#library_8h_1ac3835bbc1c6797e56f8aa47443d11af6 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_has_jpeg_support]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv430lammps_config_has_jpeg_supportv "Link to this definition"){.headerlink}\

:   Check if the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} library supports writing JPEG format images

    The LAMMPS [[dump style image]{.doc}]dump_image.md){.reference .internal} supports writing multiple image file formats. Most of them, however, need support from an external library, and using that has to be [[enabled at compile time]{.std .std-ref}]Build_extras.md#graphics){.reference .internal}. This function checks whether support for the [JPEG image file format](https://jpeg.org/jpeg/){.reference .external} is available in the current LAMMPS library.

    Returns[:]{.colon}

    :   1 if yes, otherwise 0

------------------------------------------------------------------------

[]{#_CPPv332lammps_config_has_ffmpeg_supportv}[]{#_CPPv232lammps_config_has_ffmpeg_supportv}[]{#lammps_config_has_ffmpeg_support}[]{#library_8h_1acbbc33bf81d78002a4ed94e2b7ff8f06 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_has_ffmpeg_support]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv432lammps_config_has_ffmpeg_supportv "Link to this definition"){.headerlink}\

:   Check if the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} library supports creating movie files via a pipe to ffmpeg

    The LAMMPS [[dump style movie]{.doc}]dump_image.md){.reference .internal} supports generating movies from images on-the-fly via creating a pipe to the [ffmpeg](https://ffmpeg.org/){.reference .external} program. This function checks whether this feature was [[enabled at compile time]{.std .std-ref}]Build_extras.md#graphics){.reference .internal}. It does **not** check whether the [`ffmpeg`{.docutils .literal .notranslate}]{.pre} itself is installed and usable.

    Returns[:]{.colon}

    :   1 if yes, otherwise 0

------------------------------------------------------------------------

[]{#_CPPv328lammps_config_has_exceptionsv}[]{#_CPPv228lammps_config_has_exceptionsv}[]{#lammps_config_has_exceptions}[]{#library_8h_1ade5f1cc597079d8cb32a9765cbfff44c .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_has_exceptions]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv428lammps_config_has_exceptionsv "Link to this definition"){.headerlink}\

:   Check whether [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} errors will throw C++ exceptions.

    ::: deprecated
    [Deprecated since version 21Nov2023: ]{.versionmodified .deprecated}LAMMPS has now exceptions always enabled, so this function will now always return 1 and can be removed from applications using the library interface.
    :::

    In case of an error, LAMMPS will either abort or throw a C++ exception. The latter has to be [[enabled at compile time]{.std .std-ref}]Build_settings.md#exceptions){.reference .internal}. This function checks if exceptions were enabled.

    When using the library interface with C++ exceptions enabled, the library interface functions will "catch" them and the error status can then be checked by calling [[`lammps_has_error()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv416lammps_has_errorPv "lammps_has_error"){.reference .internal} and the most recent error message can be retrieved via [[`lammps_get_last_error_message()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv429lammps_get_last_error_messagePvPci "lammps_get_last_error_message"){.reference .internal}. This can allow to restart a calculation or delete and recreate the LAMMPS instance when C++ exceptions are enabled. One application of using exceptions this way is the [[LAMMPS-GUI]{.std .std-ref}]Tools.md#lammps-gui){.reference .internal}. If C++ exceptions are disabled and an error happens during a call to LAMMPS, the application will terminate.

    Returns[:]{.colon}

    :   1 if yes, otherwise 0

------------------------------------------------------------------------

[]{#_CPPv325lammps_config_has_packagePKc}[]{#_CPPv225lammps_config_has_packagePKc}[]{#lammps_config_has_package__cCP}[]{#library_8h_1adca5959e5b824ab7413c74ee05eb9f0d .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_has_package]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv425lammps_config_has_packagePKc "Link to this definition"){.headerlink}\

:   Check whether a specific package has been included in [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal}

    This function checks whether the LAMMPS library in use includes the specific [[LAMMPS package]{.doc}]Packages.md){.reference .internal} provided as argument.

    Parameters[:]{.colon}

    :   **name** -- string with the name of the package

    Returns[:]{.colon}

    :   1 if included, 0 if not.

------------------------------------------------------------------------

[]{#_CPPv327lammps_config_package_countv}[]{#_CPPv227lammps_config_package_countv}[]{#lammps_config_package_count}[]{#library_8h_1a233aefab279fd9290f14fae1e4c16be4 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_package_count]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv427lammps_config_package_countv "Link to this definition"){.headerlink}\

:   Count the number of installed packages in the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} library.

    This function counts how many [[LAMMPS packages]{.doc}]Packages.md){.reference .internal} are included in the LAMMPS library in use.

    Returns[:]{.colon}

    :   number of packages included

------------------------------------------------------------------------

[]{#_CPPv326lammps_config_package_nameiPci}[]{#_CPPv226lammps_config_package_nameiPci}[]{#lammps_config_package_name__i.cP.i}[]{#library_8h_1aca1da31b8eb4342ee1eff02d721fa48d .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_package_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}, [[char]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[int]{.pre}]{.kt}[)]{.sig-paren}[](#_CPPv426lammps_config_package_nameiPci "Link to this definition"){.headerlink}\

:   Get the name of a package in the list of installed packages in the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} library.

    This function copies the name of the package with the index *idx* into the provided C-style string buffer. The length of the buffer must be provided as *buf_size* argument. If the name of the package exceeds the length of the buffer, it will be truncated accordingly. If the index is out of range, the function returns 0 and *buffer* is set to an empty string, otherwise 1;

    Parameters[:]{.colon}

    :   - **idx** -- index of the package in the list of included packages (0 \<= idx \< package count)

        - **buffer** -- string buffer to copy the name of the package to

        - **buf_size** -- size of the provided string buffer

    Returns[:]{.colon}

    :   1 if successful, otherwise 0

------------------------------------------------------------------------

[]{#_CPPv325lammps_config_acceleratorPKcPKcPKc}[]{#_CPPv225lammps_config_acceleratorPKcPKcPKc}[]{#lammps_config_accelerator__cCP.cCP.cCP}[]{#library_8h_1a503c6feaadbab30ac00b978fcf199399 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_config_accelerator]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv425lammps_config_acceleratorPKcPKcPKc "Link to this definition"){.headerlink}\

:   Check for compile time settings in accelerator packages included in [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal}.

    This function checks availability of compile time settings of included [[accelerator packages]{.doc}]Speed_packages.md){.reference .internal} in LAMMPS. Supported packages names are "GPU", "KOKKOS", "INTEL", and "OPENMP". Supported categories are "api" with possible settings "cuda", "hip", "phi", "pthreads", "opencl", "openmp", and "serial", and "precision" with possible settings "double", "mixed", and "single". If the combination of package, category, and setting is available, the function returns 1, otherwise 0.

    Parameters[:]{.colon}

    :   - **package** -- string with the name of the accelerator package

        - **category** -- string with the category name of the setting

        - **setting** -- string with the name of the specific setting

    Returns[:]{.colon}

    :   1 if available, 0 if not.

------------------------------------------------------------------------

[]{#_CPPv321lammps_has_gpu_devicev}[]{#_CPPv221lammps_has_gpu_devicev}[]{#lammps_has_gpu_device}[]{#library_8h_1acd3fd9fa79e08b7fb530b51b9ca79c8e .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_has_gpu_device]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv421lammps_has_gpu_devicev "Link to this definition"){.headerlink}\

:   Check for presence of a viable GPU package device

    ::: versionadded
    [Added in version 14May2021.]{.versionmodified .added}
    :::

    The [[`lammps_has_gpu_device()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv421lammps_has_gpu_devicev "lammps_has_gpu_device"){.reference .internal} function checks at runtime if an accelerator device is present that can be used with the [[GPU package]{.doc}]Speed_gpu.md){.reference .internal}. If at least one suitable device is present the function will return 1, otherwise 0.

    More detailed information about the available device or devices can be obtained by calling the [[`lammps_get_gpu_device_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_get_gpu_device_infoPci "lammps_get_gpu_device_info"){.reference .internal} function.

    Returns[:]{.colon}

    :   1 if viable device is available, 0 if not.

------------------------------------------------------------------------

[]{#_CPPv326lammps_get_gpu_device_infoPci}[]{#_CPPv226lammps_get_gpu_device_infoPci}[]{#lammps_get_gpu_device_info__cP.i}[]{#library_8h_1a8439a498ff1b8117a45e705e2a636c18 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_get_gpu_device_info]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[buffer]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[buf_size]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv426lammps_get_gpu_device_infoPci "Link to this definition"){.headerlink}\

:   Get GPU package device information

    ::: versionadded
    [Added in version 14May2021.]{.versionmodified .added}
    :::

    The [[`lammps_get_gpu_device_info()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv426lammps_get_gpu_device_infoPci "lammps_get_gpu_device_info"){.reference .internal} function can be used to retrieve detailed information about any accelerator devices that are viable for use with the [[GPU package]{.doc}]Speed_gpu.md){.reference .internal}. It will produce a string that is equivalent to the output of the [`nvc_get_device`{.docutils .literal .notranslate}]{.pre} or [`ocl_get_device`{.docutils .literal .notranslate}]{.pre} or [`hip_get_device`{.docutils .literal .notranslate}]{.pre} tools that are compiled alongside LAMMPS if the GPU package is enabled.

    A suitable buffer for a C-style string has to be provided and its length. The assembled text will be truncated to not overflow this buffer. This string can be several kilobytes long, if multiple devices are present.

    Parameters[:]{.colon}

    :   - **buffer** -- string buffer to copy the information to

        - **buf_size** -- size of the provided string buffer

------------------------------------------------------------------------

[]{#_CPPv316lammps_has_stylePvPKcPKc}[]{#_CPPv216lammps_has_stylePvPKcPKc}[]{#lammps_has_style__voidP.cCP.cCP}[]{#library_8h_1a74aa598ce1e183ed70ce5eabf7202bec .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_has_style]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv416lammps_has_stylePvPKcPKc "Link to this definition"){.headerlink}\

:   Check if a specific style has been included in [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal}

    This function checks if the LAMMPS library in use includes the specific *style* of a specific *category* provided as an argument. Valid categories are: *atom*, *integrate*, *minimize*, *pair*, *bond*, *angle*, *dihedral*, *improper*, *kspace*, *compute*, *fix*, *region*, *dump*, and *command*.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **category** -- category of the style

        - **name** -- name of the style

    Returns[:]{.colon}

    :   1 if included, 0 if not.

------------------------------------------------------------------------

[]{#_CPPv318lammps_style_countPvPKc}[]{#_CPPv218lammps_style_countPvPKc}[]{#lammps_style_count__voidP.cCP}[]{#library_8h_1aef8b5d9f8c06dc22c55deb9088dbafd6 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_style_count]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv418lammps_style_countPvPKc "Link to this definition"){.headerlink}\

:   Count the number of styles of category in the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} library.

    This function counts how many styles in the provided *category* are included in the LAMMPS library in use. Please see [[`lammps_has_style()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv416lammps_has_stylePvPKcPKc "lammps_has_style"){.reference .internal} for a list of valid categories.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **category** -- category of styles

    Returns[:]{.colon}

    :   number of styles in category

------------------------------------------------------------------------

[]{#_CPPv317lammps_style_namePvPKciPci}[]{#_CPPv217lammps_style_namePvPKciPci}[]{#lammps_style_name__voidP.cCP.i.cP.i}[]{#library_8h_1ab91b5c7e97982f7a804d8d7cfa0f190a .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_style_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[int]{.pre}]{.kt}, [[char]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[int]{.pre}]{.kt}[)]{.sig-paren}[](#_CPPv417lammps_style_namePvPKciPci "Link to this definition"){.headerlink}\

:   Look up the name of a style by index in the list of style of a given category in the [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} library.

    This function copies the name of the *category* style with the index *idx* into the provided C-style string buffer. The length of the buffer must be provided as *buf_size* argument. If the name of the style exceeds the length of the buffer, it will be truncated accordingly. If the index is out of range, the function returns 0 and *buffer* is set to an empty string, otherwise 1.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **category** -- category of styles

        - **idx** -- index of the style in the list of *category* styles (0 \<= idx \< style count)

        - **buffer** -- string buffer to copy the name of the style to

        - **buf_size** -- size of the provided string buffer

    Returns[:]{.colon}

    :   1 if successful, otherwise 0

------------------------------------------------------------------------

[]{#_CPPv313lammps_has_idPvPKcPKc}[]{#_CPPv213lammps_has_idPvPKcPKc}[]{#lammps_has_id__voidP.cCP.cCP}[]{#library_8h_1ad1ee62546d5d560747379cba84bea178 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_has_id]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv413lammps_has_idPvPKcPKc "Link to this definition"){.headerlink}\

:   Check if a specific ID exists in the current [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

    ::: versionadded
    [Added in version 9Oct2020.]{.versionmodified .added}
    :::

    This function checks if the current LAMMPS instance a *category* ID of the given *name* exists. Valid categories are: *compute*, *dump*, *fix*, *group*, *molecule*, *region*, and *variable*.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **category** -- category of the id

        - **name** -- name of the id

    Returns[:]{.colon}

    :   1 if included, 0 if not.

------------------------------------------------------------------------

[]{#_CPPv315lammps_id_countPvPKc}[]{#_CPPv215lammps_id_countPvPKc}[]{#lammps_id_count__voidP.cCP}[]{#library_8h_1aaa1311b9ce55c53bfae199c2ee9cb955 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_id_count]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv415lammps_id_countPvPKc "Link to this definition"){.headerlink}\

:   Count the number of IDs of a category.

    ::: versionadded
    [Added in version 9Oct2020.]{.versionmodified .added}
    :::

    This function counts how many IDs in the provided *category* are defined in the current LAMMPS instance. Please see [[`lammps_has_id()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv413lammps_has_idPvPKcPKc "lammps_has_id"){.reference .internal} for a list of valid categories.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **category** -- category of IDs

    Returns[:]{.colon}

    :   number of IDs in category

------------------------------------------------------------------------

[]{#_CPPv314lammps_id_namePvPKciPci}[]{#_CPPv214lammps_id_namePvPKciPci}[]{#lammps_id_name__voidP.cCP.i.cP.i}[]{#library_8h_1a42ba710155bca355ba451fd45dcda0f9 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[lammps_id_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[int]{.pre}]{.kt}, [[char]{.pre}]{.kt}[[\*]{.pre}]{.p}, [[int]{.pre}]{.kt}[)]{.sig-paren}[](#_CPPv414lammps_id_namePvPKciPci "Link to this definition"){.headerlink}\

:   Look up the name of an ID by index in the list of IDs of a given category.

    ::: versionadded
    [Added in version 9Oct2020.]{.versionmodified .added}
    :::

    This function copies the name of the *category* ID with the index *idx* into the provided C-style string buffer. The length of the buffer must be provided as *buf_size* argument. If the name of the style exceeds the length of the buffer, it will be truncated accordingly. If the index is out of range, the function returns 0 and *buffer* is set to an empty string, otherwise 1.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance cast to [`void`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`*`{.docutils .literal .notranslate}]{.pre}.

        - **category** -- category of IDs

        - **idx** -- index of the ID in the list of *category* styles (0 \<= idx \< count)

        - **buffer** -- string buffer to copy the name of the style to

        - **buf_size** -- size of the provided string buffer

    Returns[:]{.colon}

    :   1 if successful, otherwise 0
:::::::
::::::::
:::::::::

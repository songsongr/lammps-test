:::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::: {#platform-abstraction-functions .section}
# [4.14. ]{.section-number}Platform abstraction functions[](#platform-abstraction-functions "Link to this heading"){.headerlink}

The [`platform`{.docutils .literal .notranslate}]{.pre} sub-namespace inside the [`LAMMPS_NS`{.docutils .literal .notranslate}]{.pre} namespace provides a collection of wrapper and convenience functions and utilities that perform common tasks for which platform specific code would be required or for which a more high-level abstraction would be convenient and reduce duplicated code. This reduces redundant implementations and encourages consistent behavior and thus has some overlap with the [["utils" sub-namespace]{.doc}]Developer_utils.md){.reference .internal}.

::: {#time-functions .section}
## [4.14.1. ]{.section-number}Time functions[](#time-functions "Link to this heading"){.headerlink}

[]{#_CPPv3N9LAMMPS_NS8platform7cputimeEv}[]{#_CPPv2N9LAMMPS_NS8platform7cputimeEv}[]{#LAMMPS_NS::platform::cputime}[]{#platform_8h_1a5f4b3548be5eb5c6ecb125ef68070fba .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[cputime]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform7cputimeEv "Link to this definition"){.headerlink}\

:   Return the consumed CPU time for the current process in seconds

    This is a wrapper around the POSIX function getrusage() and its Windows equivalent. It is to be used in a similar fashion as MPI_Wtime(). Its resolution may be rather low so it can only be trusted when observing processes consuming CPU time of at least a few seconds.

    Returns[:]{.colon}

    :   used CPU time in seconds

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform8walltimeEv}[]{#_CPPv2N9LAMMPS_NS8platform8walltimeEv}[]{#LAMMPS_NS::platform::walltime}[]{#platform_8h_1aca5f89d1d77efd166713bf8dd6d7fcd4 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[walltime]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform8walltimeEv "Link to this definition"){.headerlink}\

:   Return the wall clock state for the current process in seconds

    This clock is counting continuous time and is initialized during load of the executable/library. Its absolute value must be considered arbitrary and thus elapsed wall times are measured in taking differences. It is therefore to be used in a similar fashion as MPI_Wtime() but has a different offset, usually leading to better resolution.

    Returns[:]{.colon}

    :   wall clock time in seconds

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform6usleepEi}[]{#_CPPv2N9LAMMPS_NS8platform6usleepEi}[]{#LAMMPS_NS::platform::usleep__i}[]{#platform_8h_1afb043f14811cda3d34904e2eec5f07b9 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[usleep]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[usec]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform6usleepEi "Link to this definition"){.headerlink}\

:   Suspend execution for a microsecond interval

    This emulates the usleep(3) BSD function call also mentioned in POSIX.1-2001. This is not a precise delay; it may be longer, but not shorter.

    Parameters[:]{.colon}

    :   **usec** -- length of delay in microseconds
:::

::: {#platform-information-functions .section}
## [4.14.2. ]{.section-number}Platform information functions[](#platform-information-functions "Link to this heading"){.headerlink}

[]{#_CPPv3N9LAMMPS_NS8platform7os_infoEv}[]{#_CPPv2N9LAMMPS_NS8platform7os_infoEv}[]{#LAMMPS_NS::platform::os_info}[]{#platform_8h_1aaf549959ee090489b6146d8918e07d0c .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[os_info]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform7os_infoEv "Link to this definition"){.headerlink}\

:   Return string with the operating system version and architecture info

    Returns[:]{.colon}

    :   string with info about the OS and the platform is is running on

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform13compiler_infoEv}[]{#_CPPv2N9LAMMPS_NS8platform13compiler_infoEv}[]{#LAMMPS_NS::platform::compiler_info}[]{#platform_8h_1aff1bead546363da736aa6e7d5a356c8f .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[compiler_info]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform13compiler_infoEv "Link to this definition"){.headerlink}\

:   Return string with compiler version info

    This function uses predefined compiler macros to identify Compilers and their version and configuration info.

    Returns[:]{.colon}

    :   string with the compiler information text

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform12cxx_standardEv}[]{#_CPPv2N9LAMMPS_NS8platform12cxx_standardEv}[]{#LAMMPS_NS::platform::cxx_standard}[]{#platform_8h_1a6b0cd92425b2ba864c0827aa84634092 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[cxx_standard]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform12cxx_standardEv "Link to this definition"){.headerlink}\

:   Return string with C++ standard version used to compile [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal}.

    This function uses predefined compiler macros to identify the C++ standard version used to compile [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} with.

    Returns[:]{.colon}

    :   string with the C++ standard version or "unknown"

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform15openmp_standardEv}[]{#_CPPv2N9LAMMPS_NS8platform15openmp_standardEv}[]{#LAMMPS_NS::platform::openmp_standard}[]{#platform_8h_1a9a1ea03475feccb71ba24c81ed47bcbe .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[openmp_standard]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform15openmp_standardEv "Link to this definition"){.headerlink}\

:   Return string with OpenMP standard version info

    This function uses predefined compiler macros to identify OpenMP support and the supported version of the standard.

    Returns[:]{.colon}

    :   string with the openmp information text

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform10mpi_vendorEv}[]{#_CPPv2N9LAMMPS_NS8platform10mpi_vendorEv}[]{#LAMMPS_NS::platform::mpi_vendor}[]{#platform_8h_1a91f4f7bc79930f0ced868e82f5a0c85f .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[mpi_vendor]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform10mpi_vendorEv "Link to this definition"){.headerlink}\

:   Return string with MPI vendor info

    This function uses predefined macros to identify the vendor of the MPI library used.

    Returns[:]{.colon}

    :   string with the MPI vendor information text

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform8mpi_infoERiRi}[]{#_CPPv2N9LAMMPS_NS8platform8mpi_infoERiRi}[]{#LAMMPS_NS::platform::mpi_info__iR.iR}[]{#platform_8h_1a138dd5b5a0f070a142ae99957f7ba161 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[mpi_info]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[major]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[&]{.pre}]{.p}[[minor]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform8mpi_infoERiRi "Link to this definition"){.headerlink}\

:   Return string with MPI version info

    This function uses predefined macros and MPI function calls to identify the version of the MPI library used.

    Parameters[:]{.colon}

    :   - **major** -- major version of the MPI standard (set on exit)

        - **minor** -- minor version of the MPI standard (set on exit)

    Returns[:]{.colon}

    :   string with the MPI version information text

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform13compress_infoEv}[]{#_CPPv2N9LAMMPS_NS8platform13compress_infoEv}[]{#LAMMPS_NS::platform::compress_info}[]{#platform_8h_1aec1a0eb6ddfe528d22869aa0aa1b1004 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[compress_info]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform13compress_infoEv "Link to this definition"){.headerlink}\

:   Return string with list of available compression types and executables

    This function tests which of the supported compression executables are available for reading or writing compressed files where supported.

    Returns[:]{.colon}

    :   string with list of available compression tools
:::

::: {#file-and-path-functions-and-global-constants .section}
## [4.14.3. ]{.section-number}File and path functions and global constants[](#file-and-path-functions-and-global-constants "Link to this heading"){.headerlink}

Since we are requiring C++17 to compile LAMMPS, you can also make use of the functionality of the [C++ filesystem library](https://cppreference.com/w/cpp/filesystem.html){.reference .external}. The following functions are in part convenience functions or emulate the behavior of similar Python functions or Unix shell commands. Please note that the you need to use the [`string()`{.docutils .literal .notranslate}]{.pre} member function of the [std::filesystem::path class](https://cppreference.com/w/cpp/filesystem/path.html){.reference .external} to get access to the path as a C++ string class instance.

[]{#_CPPv3N9LAMMPS_NS8platform11filepathsepE}[]{#_CPPv2N9LAMMPS_NS8platform11filepathsepE}[]{#LAMMPS_NS::platform::filepathsep__cA}[]{#platform_8h_1a3174b82f12dfbffab20b2b96fbc442f3 .target}[[char]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[filepathsep]{.pre}]{.n}]{.sig-name .descname}[[\[]{.pre}]{.p}[[\]]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"/\"]{.pre}]{.s}[](#_CPPv4N9LAMMPS_NS8platform11filepathsepE "Link to this definition"){.headerlink}\

:   Platform specific file path component separator

    This is a string with the character that separates directories and filename in paths on a platform. If multiple are characters are provided, the first is the preferred one.

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform10pathvarsepE}[]{#_CPPv2N9LAMMPS_NS8platform10pathvarsepE}[]{#LAMMPS_NS::platform::pathvarsep__c}[]{#platform_8h_1a0427d2d3074fc8188d6731545bc33855 .target}[[char]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[pathvarsep]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\':\']{.pre}]{.sc}[](#_CPPv4N9LAMMPS_NS8platform10pathvarsepE "Link to this definition"){.headerlink}\

:   Platform specific path environment variable component separator

    This is the character that separates entries in "PATH"-style environment variables.

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform9guesspathEP4FILEPci}[]{#_CPPv2N9LAMMPS_NS8platform9guesspathEP4FILEPci}[]{#LAMMPS_NS::platform::guesspath__FILEP.cP.i}[]{#platform_8h_1aa344b662f8d3c394089253824eca591d .target}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[guesspath]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[buf]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[len]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform9guesspathEP4FILEPci "Link to this definition"){.headerlink}\

:   Try to detect pathname from FILE pointer

    Currently only supported on Linux, MacOS, and Windows. Otherwise will report "(unknown)".

    On Linux the folder /proc/self/fd holds symbolic links to the actual pathnames associated with each open file descriptor of the current process. On MacOS the same kind of information can be obtained using [`fcntl(fd,F_GETPATH,buf)`{.docutils .literal .notranslate}]{.pre}. On Windows we use [`GetFinalPathNameByHandleA()`{.docutils .literal .notranslate}]{.pre} which is available with Windows Vista and later. If the buffer is too small (\< 16 bytes) a null pointer is returned.

    This function is used to provide a filename with error messages in functions where the filename is not passed as an argument, but the FILE \* pointer.

    Parameters[:]{.colon}

    :   - **fp** -- FILE pointer struct from STDIO library for which we want to detect the name

        - **buf** -- storage buffer for pathname. output will be truncated if not large enough

        - **len** -- size of storage buffer. output will be truncated to this length - 1

    Returns[:]{.colon}

    :   pointer to the storage buffer with path or a NULL pointer if buf is invalid or the buffer size is too small

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform13path_basenameERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform13path_basenameERKNSt6stringE}[]{#LAMMPS_NS::platform::path_basename__ssCR}[]{#platform_8h_1af571f031125be18774c73496bf428f1e .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[path_basename]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform13path_basenameERKNSt6stringE "Link to this definition"){.headerlink}\

:   Strip off leading part of path, return just the filename

    Parameters[:]{.colon}

    :   **path** -- file path

    Returns[:]{.colon}

    :   file name

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform12path_dirnameERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform12path_dirnameERKNSt6stringE}[]{#LAMMPS_NS::platform::path_dirname__ssCR}[]{#platform_8h_1ab100315d6ea8390c0a3f9678010131ff .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[path_dirname]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform12path_dirnameERKNSt6stringE "Link to this definition"){.headerlink}\

:   Return the directory part of a path. Return "." if empty

    Parameters[:]{.colon}

    :   **path** -- file path

    Returns[:]{.colon}

    :   directory name

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform9path_joinERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform9path_joinERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::platform::path_join__ssCR.ssCR}[]{#platform_8h_1afdc0fd0cefb9e5241e4ba20852877f4e .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[path_join]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[a]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[b]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform9path_joinERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

:   Join two pathname segments

    This uses the forward slash '/' character unless [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} is compiled for Windows where it uses the backward slash '\'

    Parameters[:]{.colon}

    :   - **a** -- first path

        - **b** -- second path

    Returns[:]{.colon}

    :   combined path

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform16file_is_readableERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform16file_is_readableERKNSt6stringE}[]{#LAMMPS_NS::platform::file_is_readable__ssCR}[]{#platform_8h_1a9b6a15dfd00fe9eebeb84f092402b6b1 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[file_is_readable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform16file_is_readableERKNSt6stringE "Link to this definition"){.headerlink}\

:   Check if file exists and is readable

    Parameters[:]{.colon}

    :   **path** -- file path

    Returns[:]{.colon}

    :   true if file exists and is readable

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform16file_is_writableERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform16file_is_writableERKNSt6stringE}[]{#LAMMPS_NS::platform::file_is_writable__ssCR}[]{#platform_8h_1a523f82f0cdb2ec5d7162171a067eeb30 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[file_is_writable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform16file_is_writableERKNSt6stringE "Link to this definition"){.headerlink}\

:   Check if file can be opened for writing

    Parameters[:]{.colon}

    :   **path** -- file path

    Returns[:]{.colon}

    :   true if file can be opened for writing

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform13file_redirectERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform13file_redirectERKNSt6stringE}[]{#LAMMPS_NS::platform::file_redirect__ssCR}[]{#platform_8h_1a8afb68742818f797f471b722475bb3bc .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[file_redirect]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform13file_redirectERKNSt6stringE "Link to this definition"){.headerlink}\

:   Return target path if the file is a 'redirect file'

    Git uses 'redirect files' instead of symbolic links on Windows since the Windows file system has no symbolic links. The redirect file is a text file with just one line: the symbolic link target path. This function opens the path parameter and reads a line. If that line is a readable file, it returns that path, otherwise the original path. The check is only performed when compiled for Windows. Otherwise the original path is always returned.

    Parameters[:]{.colon}

    :   **path** -- file path to check

    Returns[:]{.colon}

    :   the redirected path or the original path

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform10is_consoleEP4FILE}[]{#_CPPv2N9LAMMPS_NS8platform10is_consoleEP4FILE}[]{#LAMMPS_NS::platform::is_console__FILEP}[]{#platform_8h_1ad3dce4729b475039e1f3cd7ad5dc4cf5 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[is_console]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform10is_consoleEP4FILE "Link to this definition"){.headerlink}\

:   Check if a file pointer may be connected to a console

    Parameters[:]{.colon}

    :   **fp** -- file pointer

    Returns[:]{.colon}

    :   true if the file pointer is flagged as a TTY

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform9disk_freeERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform9disk_freeERKNSt6stringE}[]{#LAMMPS_NS::platform::disk_free__ssCR}[]{#platform_8h_1a6ed051736e3bf0c472eacaa8d7ac86e6 .target}[[double]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[disk_free]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform9disk_freeERKNSt6stringE "Link to this definition"){.headerlink}\

:   Return free disk space in bytes of file system pointed to by path

    Returns -1.0 if the path is invalid or free space reporting not supported.

    Parameters[:]{.colon}

    :   **path** -- file or folder path in file system

    Returns[:]{.colon}

    :   

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform14list_directoryERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform14list_directoryERKNSt6stringE}[]{#LAMMPS_NS::platform::list_directory__ssCR}[]{#platform_8h_1ad9f70de7fed649daa7ef1957c9997e38 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[list_directory]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[dir]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform14list_directoryERKNSt6stringE "Link to this definition"){.headerlink}\

:   Get list of entries in a directory

    This provides a list of strings of the entries in the directory without the leading path name while also skipping over ".." and ".".

    Parameters[:]{.colon}

    :   **dir** -- path to directory

    Returns[:]{.colon}

    :   vector with strings of all directory entries

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform5chdirERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform5chdirERKNSt6stringE}[]{#LAMMPS_NS::platform::chdir__ssCR}[]{#platform_8h_1a8dc97878b620dd294214f33d426b25dd .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[chdir]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform5chdirERKNSt6stringE "Link to this definition"){.headerlink}\

:   Change current directory

    Parameters[:]{.colon}

    :   **path** -- new current working directory path

    Returns[:]{.colon}

    :   -1 if unsuccessful, otherwise \>= 0

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform5mkdirERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform5mkdirERKNSt6stringE}[]{#LAMMPS_NS::platform::mkdir__ssCR}[]{#platform_8h_1aeacc2f1b5e3104760c86fb4644cb684a .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[mkdir]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform5mkdirERKNSt6stringE "Link to this definition"){.headerlink}\

:   Create a directory or directory path

    Unlike the the [`mkdir()`{.docutils .literal .notranslate}]{.pre} or [`_mkdir()`{.docutils .literal .notranslate}]{.pre} functions of the C library, this function will also try to create non-existing sub-directories in case they don't exist, and thus it behaves like the [`mkdir`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-p`{.docutils .literal .notranslate}]{.pre} command rather than plain [`mkdir`{.docutils .literal .notranslate}]{.pre} or [`md`{.docutils .literal .notranslate}]{.pre} in a Unix or Windows shell, respectively.

    Parameters[:]{.colon}

    :   **path** -- directory path

    Returns[:]{.colon}

    :   -1 if unsuccessful, otherwise \>= 0

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform5rmdirERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform5rmdirERKNSt6stringE}[]{#LAMMPS_NS::platform::rmdir__ssCR}[]{#platform_8h_1a3302c183fe617ad6bf01e5f1bfff8dd9 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[rmdir]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform5rmdirERKNSt6stringE "Link to this definition"){.headerlink}\

:   Delete a directory

    Unlike the the [`rmdir()`{.docutils .literal .notranslate}]{.pre} or [`_rmdir()`{.docutils .literal .notranslate}]{.pre} functions of the C library, this function will check for the contents of the folder and recurse into any sub-folders, if necessary, and delete all contained folders and their contents before deleting the folder *path*.

    Parameters[:]{.colon}

    :   **path** -- directory path

    Returns[:]{.colon}

    :   -1 if unsuccessful, otherwise \>= 0

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform6unlinkERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform6unlinkERKNSt6stringE}[]{#LAMMPS_NS::platform::unlink__ssCR}[]{#platform_8h_1a6555cc4e8063ed94d56cd815278a9421 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[unlink]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform6unlinkERKNSt6stringE "Link to this definition"){.headerlink}\

:   Delete a file

    Parameters[:]{.colon}

    :   **path** -- path to file to be deleted

    Returns[:]{.colon}

    :   0 on success, -1 on error
:::

::: {#standard-i-o-function-wrappers .section}
## [4.14.4. ]{.section-number}Standard I/O function wrappers[](#standard-i-o-function-wrappers "Link to this heading"){.headerlink}

[]{#_CPPv3N9LAMMPS_NS8platform11END_OF_FILEE}[]{#_CPPv2N9LAMMPS_NS8platform11END_OF_FILEE}[]{#LAMMPS_NS::platform::END_OF_FILE__bigint}[]{#platform_8h_1aff22a2f6cfc75229f3c6691a64679ab0 .target}[[bigint]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[END_OF_FILE]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[-]{.pre}]{.o}[[1]{.pre}]{.m}[](#_CPPv4N9LAMMPS_NS8platform11END_OF_FILEE "Link to this definition"){.headerlink}\

:   constant to seek to the end of the file

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform5ftellEP4FILE}[]{#_CPPv2N9LAMMPS_NS8platform5ftellEP4FILE}[]{#LAMMPS_NS::platform::ftell__FILEP}[]{#platform_8h_1afd4bf7f50771420b35850e961c8fa487 .target}[[bigint]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[ftell]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform5ftellEP4FILE "Link to this definition"){.headerlink}\

:   Get current file position

    Parameters[:]{.colon}

    :   **fp** -- FILE pointer of the given file

    Returns[:]{.colon}

    :   current FILE pointer position cast to a bigint

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform5fseekEP4FILE6bigint}[]{#_CPPv2N9LAMMPS_NS8platform5fseekEP4FILE6bigint}[]{#LAMMPS_NS::platform::fseek__FILEP.bigint}[]{#platform_8h_1af983f9763b57efcf3888b2a19f9babcd .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[fseek]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}, [[bigint]{.pre}]{.n}[ ]{.w}[[pos]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform5fseekEP4FILE6bigint "Link to this definition"){.headerlink}\

:   Set absolute file position

    If the absolute position is END_OF_FILE, then position at the end of the file.

    Parameters[:]{.colon}

    :   - **fp** -- FILE pointer of the given file

        - **pos** -- new position of the FILE pointer

    Returns[:]{.colon}

    :   0 if successful, otherwise -1

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform9ftruncateEP4FILE6bigint}[]{#_CPPv2N9LAMMPS_NS8platform9ftruncateEP4FILE6bigint}[]{#LAMMPS_NS::platform::ftruncate__FILEP.bigint}[]{#platform_8h_1ad9bfc18919956b05289d2eff3643aff1 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[ftruncate]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}, [[bigint]{.pre}]{.n}[ ]{.w}[[length]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform9ftruncateEP4FILE6bigint "Link to this definition"){.headerlink}\

:   Truncate file to a given length and re-position file pointer

    Parameters[:]{.colon}

    :   - **fp** -- FILE pointer of the given file

        - **length** -- length to which the file is being truncated to

    Returns[:]{.colon}

    :   0 if successful, otherwise -1

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform5popenERKNSt6stringERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform5popenERKNSt6stringERKNSt6stringE}[]{#LAMMPS_NS::platform::popen__ssCR.ssCR}[]{#platform_8h_1ac811c6a9953c81b80fd6b761701b7bfe .target}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[popen]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[cmd]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[mode]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform5popenERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

:   Open a pipe to a command for reading or writing

    Parameters[:]{.colon}

    :   - **cmd** -- command for the pipe

        - **mode** -- "r" for reading from *cmd* or "w" for writing to *cmd*

    Returns[:]{.colon}

    :   file pointer to the pipe if successful or null

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform6pcloseEP4FILE}[]{#_CPPv2N9LAMMPS_NS8platform6pcloseEP4FILE}[]{#LAMMPS_NS::platform::pclose__FILEP}[]{#platform_8h_1abca9eaf3eb5f2010062ee8f6a4017733 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[pclose]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[fp]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform6pcloseEP4FILE "Link to this definition"){.headerlink}\

:   Close a previously opened pipe

    Parameters[:]{.colon}

    :   **fp** -- FILE pointer for the pipe

    Returns[:]{.colon}

    :   exit status of the pipe command or -1 in case of errors
:::

::: {#environment-variable-functions .section}
## [4.14.5. ]{.section-number}Environment variable functions[](#environment-variable-functions "Link to this heading"){.headerlink}

[]{#_CPPv3N9LAMMPS_NS8platform6putenvERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform6putenvERKNSt6stringE}[]{#LAMMPS_NS::platform::putenv__ssCR}[]{#platform_8h_1aae6f2f54e54291876e6bbd8f952c9c5f .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[putenv]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[vardef]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform6putenvERKNSt6stringE "Link to this definition"){.headerlink}\

:   Add variable to the environment

    Parameters[:]{.colon}

    :   **vardef** -- variable name or variable definition (NAME=value)

    Returns[:]{.colon}

    :   -1 if failure otherwise 0

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform8unsetenvERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform8unsetenvERKNSt6stringE}[]{#LAMMPS_NS::platform::unsetenv__ssCR}[]{#platform_8h_1add0ec024cf89b7fe7a83b4c54fdf8f94 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[unsetenv]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform8unsetenvERKNSt6stringE "Link to this definition"){.headerlink}\

:   Delete variable from the environment

    Parameters[:]{.colon}

    :   **variable** -- variable name

    Returns[:]{.colon}

    :   -1 if failure otherwise 0

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform12list_pathenvERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform12list_pathenvERKNSt6stringE}[]{#LAMMPS_NS::platform::list_pathenv__ssCR}[]{#platform_8h_1ac52391dc7686d4a9e21b5d6ded324869 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[list_pathenv]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[var]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform12list_pathenvERKNSt6stringE "Link to this definition"){.headerlink}\

:   Get list of entries in a path environment variable

    This provides a list of strings of the entries in an environment variable that is containing a "path" like "PATH" or "LD_LIBRARY_PATH".

    Parameters[:]{.colon}

    :   **var** -- name of the environment variable

    Returns[:]{.colon}

    :   vector with strings of all entries in that path variable

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform13find_exe_pathERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform13find_exe_pathERKNSt6stringE}[]{#LAMMPS_NS::platform::find_exe_path__ssCR}[]{#platform_8h_1ac7d2f135d11783248a70f4a66fddf671 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[find_exe_path]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[cmd]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform13find_exe_pathERKNSt6stringE "Link to this definition"){.headerlink}\

:   Find pathname of an executable in the standard search path

    This function will traverse the list of directories in the PATH environment variable and look for the executable *cmd*. If the file exists and is executable the full path is returned as string, otherwise an empty string is returned.

    On Windows the *cmd* string must not include an extension as this function will automatically append the extensions ".exe", ".com" and ".bat" and look for those paths. On Windows also the current directory is checked (and first), but otherwise is not checked unless "." exists in the PATH environment variable.

    Because of the nature of the check, this will not detect shell functions built-in command or aliases.

    Parameters[:]{.colon}

    :   **cmd** -- name of command

    Returns[:]{.colon}

    :   vector with strings of all directory entries
:::

::: {#dynamically-loaded-object-or-library-functions .section}
## [4.14.6. ]{.section-number}Dynamically loaded object or library functions[](#dynamically-loaded-object-or-library-functions "Link to this heading"){.headerlink}

[]{#_CPPv3N9LAMMPS_NS8platform6dlopenERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform6dlopenERKNSt6stringE}[]{#LAMMPS_NS::platform::dlopen__ssCR}[]{#platform_8h_1acd2e0d5c0aa701ba30307f5dfee05b8c .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[dlopen]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[fname]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform6dlopenERKNSt6stringE "Link to this definition"){.headerlink}\

:   Open a shared object file or library

    Parameters[:]{.colon}

    :   **fname** -- name or path of the shared object

    Returns[:]{.colon}

    :   handle to the shared object or null

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform7dlcloseEPv}[]{#_CPPv2N9LAMMPS_NS8platform7dlcloseEPv}[]{#LAMMPS_NS::platform::dlclose__voidP}[]{#platform_8h_1af483b6c4400965aa885f9f1a144138a5 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[dlclose]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform7dlcloseEPv "Link to this definition"){.headerlink}\

:   Close a shared object

    This releases the object corresponding to the provided handle. Resolved symbols associated with this handle may not be used after this call

    Parameters[:]{.colon}

    :   **handle** -- handle to an opened shared object

    Returns[:]{.colon}

    :   0 if successful, non-zero of not

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform5dlsymEPvRKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform5dlsymEPvRKNSt6stringE}[]{#LAMMPS_NS::platform::dlsym__voidP.ssCR}[]{#platform_8h_1ab1b3f356af1d5cbe80f8188b1d63770b .target}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[dlsym]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[symbol]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform5dlsymEPvRKNSt6stringE "Link to this definition"){.headerlink}\

:   Resolve a symbol in shared object

    Parameters[:]{.colon}

    :   - **handle** -- handle to an opened shared object

        - **symbol** -- name of the symbol to extract

    Returns[:]{.colon}

    :   pointer to the resolved symbol or null

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform7dlerrorEv}[]{#_CPPv2N9LAMMPS_NS8platform7dlerrorEv}[]{#LAMMPS_NS::platform::dlerror}[]{#platform_8h_1a5cfc90f8002e180ad96c73a101c6aa23 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[dlerror]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform7dlerrorEv "Link to this definition"){.headerlink}\

:   Obtain error diagnostic info after dynamic linking function calls

    Return a human-readable string describing the most recent error that occurred when using one of the functions for dynamic loading objects the last call to this function. If there was no error, the string is empty.

    Returns[:]{.colon}

    :   string with error message or empty
:::

::: {#compressed-file-i-o-functions .section}
## [4.14.7. ]{.section-number}Compressed file I/O functions[](#compressed-file-i-o-functions "Link to this heading"){.headerlink}

[]{#_CPPv3N9LAMMPS_NS8platform22has_compress_extensionERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform22has_compress_extensionERKNSt6stringE}[]{#LAMMPS_NS::platform::has_compress_extension__ssCR}[]{#platform_8h_1acb172eb1662e351bab844ccfafbd9427 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[has_compress_extension]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform22has_compress_extensionERKNSt6stringE "Link to this definition"){.headerlink}\

:   Check if a file name ends in a known extension for a compressed file format

    Currently supported file extensions are: .gz, .bz2, .zst, .xz, .lzma, .lz4, .br, and .7z

    Parameters[:]{.colon}

    :   **file** -- name of the file to check

    Returns[:]{.colon}

    :   true if the file has a known extension, otherwise false

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform15compressed_readERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform15compressed_readERKNSt6stringE}[]{#LAMMPS_NS::platform::compressed_read__ssCR}[]{#platform_8h_1a07977ea469d1405938f4225010fd0a3e .target}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[compressed_read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform15compressed_readERKNSt6stringE "Link to this definition"){.headerlink}\

:   Open pipe to compressed text file for reading

    Parameters[:]{.colon}

    :   **file** -- name of the file to open

    Returns[:]{.colon}

    :   FILE pointer to pipe using for reading the compressed file.

<!-- -->

[]{#_CPPv3N9LAMMPS_NS8platform16compressed_writeERKNSt6stringE}[]{#_CPPv2N9LAMMPS_NS8platform16compressed_writeERKNSt6stringE}[]{#LAMMPS_NS::platform::compressed_write__ssCR}[]{#platform_8h_1a6789ec6955f5cbc9555c83bd0b3ef1c1 .target}[[FILE]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[LAMMPS_NS]{.pre}]{.n}[[::]{.pre}]{.p}[[platform]{.pre}]{.n}[[::]{.pre}]{.p}]{.sig-prename .descclassname}[[[compressed_write]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N9LAMMPS_NS8platform16compressed_writeERKNSt6stringE "Link to this definition"){.headerlink}\

:   Open pipe to compressed text file for writing

    Parameters[:]{.colon}

    :   **file** -- name of the file to open

    Returns[:]{.colon}

    :   FILE pointer to pipe using for reading the compressed file.
:::
::::::::::
:::::::::::
::::::::::::

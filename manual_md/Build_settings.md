:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#optional-build-settings .section}
# [3.6. ]{.section-number}Optional build settings[](#optional-build-settings "Link to this heading"){.headerlink}

LAMMPS can be built with several optional settings. Each subsection explains how to do this for building both with CMake and make.

- [C++17 standard compliance](#c-17-standard-compliance){.reference .internal} when building all of LAMMPS

- [FFT library](#fft-library){.reference .internal} for use with the [[kspace_style pppm]{.doc}]kspace_style.md){.reference .internal} command

- [Size of LAMMPS integer types and size limits](#size-of-lammps-integer-types-and-size-limits){.reference .internal}

- [Read or write compressed files](#read-or-write-compressed-files){.reference .internal}

- [Support for downloading files from the input](#support-for-downloading-files-from-the-input){.reference .internal}

- [Prevent download of large potential files](#prevent-download-of-large-potential-files){.reference .internal}

- [Memory allocation alignment](#memory-allocation-alignment){.reference .internal}

- [Workaround for long long integers](#workaround-for-long-long-integers){.reference .internal}

- [Exception handling when using LAMMPS as a library](#exception-handling-when-using-lammps-as-a-library){.reference .internal} to capture errors

------------------------------------------------------------------------

:::::: {#c-17-standard-compliance .section}
[]{#cxx17}

## [3.6.1. ]{.section-number}C++17 standard compliance[](#c-17-standard-compliance "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

A C++17 standard compatible compiler is currently the minimum requirement for compiling LAMMPS. LAMMPS version 22 July 2025 is the last version compatible with the C++11 standard for the core code and most packages. Most currently used C++ compilers are compatible with C++17, but some older ones may need extra flags to enable C++17 compliance.

:::: {.highlight-make .notranslate}
::: highlight
    CCFLAGS = -g -O3 -std=c++17
:::
::::

Individual packages may require compliance with a later C++ standard like C++20. These requirements will be documented with the [[individual packages]{.doc}]Packages_details.md){.reference .internal}.

------------------------------------------------------------------------
::::::

:::::::::::::::::::::: {#fft-library .section}
[]{#fft}

## [3.6.2. ]{.section-number}FFT library[](#fft-library "Link to this heading"){.headerlink}

When the KSPACE package is included in a LAMMPS build, the [[kspace_style pppm]{.doc}]kspace_style.md){.reference .internal} command performs 3d FFTs which require use of an FFT library to compute 1d FFTs. The KISS FFT library is included with LAMMPS, but other libraries can be faster. LAMMPS can use them if they are available on your system.

::: versionadded
[Added in version 7Feb2024.]{.versionmodified .added}
:::

Alternatively, LAMMPS can use the [heFFTe](https://icl-utk-edu.github.io/heffte/){.reference .external} library for the MPI communication algorithms, which comes with many optimizations for special cases, e.g. leveraging available 2D and 3D FFTs in the back end libraries and better pipelining for packing and communication.

:::::::::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::::::: {#panel-0-0-0 .sphinx-tabs-panel aria-labelledby="tab-0-0-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D FFT=value              # FFTW3 or MKL or NVPL or KISS,
                              # default is FFTW3 if found, else KISS
    -D FFT_KOKKOS=value       # FFTW3 or MKL or NVPL or KISS or CUFFT
                              # or HIPFFT or MKL_GPU, default is KISS
    -D FFT_SINGLE=value       # yes or no (default), no = double precision
    -D FFT_PACK=value         # array (default) or pointer or memcpy
    -D FFT_USE_HEFFTE=value   # yes or no (default), yes links to heFFTe
:::
::::

::: {.admonition .note}
Note

When the Kokkos variant of a package is compiled and selected at run time, the FFT library selected by the [`FFT_KOKKOS`{.docutils .literal .notranslate}]{.pre} variable applies. Otherwise, the FFT library selected by the FFT variable applies. The same FFT settings apply to both. [`FFT_KOKKOS`{.docutils .literal .notranslate}]{.pre} must be compatible with the Kokkos back end - for example, when using the CUDA back end of Kokkos, you must use either [`CUFFT`{.docutils .literal .notranslate}]{.pre} or [`KISS`{.docutils .literal .notranslate}]{.pre}.
:::

Usually these settings are all that is needed. If FFTW3 is selected, then CMake will try to detect, if threaded FFTW libraries are available and enable them by default. This setting is independent of whether OpenMP threads are enabled and a package like KOKKOS or OPENMP is used. If CMake cannot detect the FFT library, you can set these variables to assist:

:::: {.highlight-bash .notranslate}
::: highlight
    -D FFTW3_INCLUDE_DIR=path   # path to FFTW3 include files
    -D FFTW3_LIBRARY=path       # path to FFTW3 libraries
    -D FFTW3_OMP_LIBRARY=path   # path to FFTW3 OpenMP wrapper libraries
    -D FFT_FFTW_THREADS=on      # enable using OpenMP threaded FFTW3 libraries
    -D MKL_INCLUDE_DIR=path     # ditto for Intel MKL library
    -D FFT_MKL_THREADS=on       # enable using threaded FFTs with MKL libraries
    -D MKL_LIBRARY=path         # path to MKL libraries
    -D FFT_HEFFTE_BACKEND=value # FFTW or MKL or empty/undefined for the stock
                                # heFFTe back end
    -D Heffte_ROOT=path         # path to an existing heFFTe installation
    -D nvpl_fft_INCLUDE_DIR=path # path to NVPL FFT include files
    -D nvpl_fft_LIBRARY_DIR=path # path to NVPL FFT libraries
:::
::::

::: {.admonition .note}
Note

heFFTe comes with a builtin (= stock) back end for FFTs, i.e. a default internal FFT implementation; however, this stock back end is intended for testing purposes only and is not optimized for production runs.
:::
:::::::::

::::::::: {#panel-0-0-1 .sphinx-tabs-panel aria-labelledby="tab-0-0-1" hidden="true" role="tabpanel" tabindex="0"}
To change the FFT library to be used and its options, you have to edit your machine Makefile. Below are examples how the makefile variables could be changed.

:::: {.highlight-make .notranslate}
::: highlight
    FFT_INC = -DFFT_<NAME>        # where <NAME> is KISS (default), FFTW3,
                                  # FFTW (same as FFTW3), NVPL, or MKL
    FFT_INC = -DFFT_KOKKOS_<NAME> # where <NAME> is KISS (default), FFTW3,
                                  # FFTW (same as FFTW3), NVPL, MKL, CUFFT,
                                  # HIPFFT, or MKL_GPU
    FFT_INC = -DFFT_SINGLE       # do not specify for double precision
    FFT_INC = -DFFT_FFTW_THREADS # enable using threaded FFTW3 libraries
    FFT_INC = -DFFT_MKL_THREADS  # enable using threaded FFTs with MKL libraries
    FFT_INC = -DFFT_PACK_ARRAY   # or -DFFT_PACK_POINTER or -DFFT_PACK_MEMCPY
                                 # default is FFT_PACK_ARRAY if not specified
:::
::::

:::: {.highlight-make .notranslate}
::: highlight
    FFT_INC =  -I/usr/local/include
    FFT_PATH = -L/usr/local/lib

    # hipFFT either precision
    FFT_LIB =  -lhipfft

    # cuFFT either precision
    FFT_LIB =  -lcufft

    # MKL_GPU either precision
    FFT_LIB = -lmkl_sycl_dft -lmkl_intel_ilp64 -lmkl_tbb_thread -lmkl_core -ltbb

    # FFTW3 double precision
    FFT_LIB =  -lfftw3

    # FFTW3 double precision with threads (needs -DFFT_FFTW_THREADS)
    FFT_LIB =  -lfftw3 -lfftw3_omp

    # FFTW3 single precision
    FFT_LIB =  -lfftw3 -lfftw3f

    # serial MKL with Intel compiler
    FFT_LIB =  -lmkl_intel_lp64 -lmkl_sequential -lmkl_core

    # serial MKL with GNU compiler
    FFT_LIB =  -lmkl_gf_lp64 -lmkl_sequential -lmkl_core

    # threaded MKL with Intel compiler
    FFT_LIB =  -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core

    # threaded MKL with GNU compiler
    FFT_LIB =  -lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core

    # MKL with automatic runtime selection of interface libs
    FFT_LIB =  -lmkl_rt

    # threaded NVPL FFT
    FFT_LIB =  -lnvpl_fftw
:::
::::

As with CMake, you do not need to set paths in [`FFT_INC`{.docutils .literal .notranslate}]{.pre} or [`FFT_PATH`{.docutils .literal .notranslate}]{.pre}, if the compiler can find the FFT header and library files in its default search path. You must specify [`FFT_LIB`{.docutils .literal .notranslate}]{.pre} with the appropriate FFT libraries to include in the link.

Traditional make can also link to heFFTe using an existing installation

:::: {.highlight-make .notranslate}
::: highlight
    include <path-to-heffte-installation>/share/heffte/HeffteMakefile.in
    FFT_INC = -DFFT_HEFFTE -DFFT_HEFFTE_FFTW $(heffte_include)
    FFT_PATH =
    FFT_LIB = $(heffte_link) $(heffte_libs)
:::
::::

The heFFTe install path will contain [`HeffteMakefile.in`{.docutils .literal .notranslate}]{.pre}. which will define the [`heffte_`{.docutils .literal .notranslate}]{.pre} include variables needed to link to heFFTe from an external project using traditional make. The [`-DFFT_HEFFTE`{.docutils .literal .notranslate}]{.pre} is required to switch to using heFFTe, while the optional [`-DFFT_HEFFTE_FFTW`{.docutils .literal .notranslate}]{.pre} selects the desired heFFTe back end, e.g., [`-DFFT_HEFFTE_FFTW`{.docutils .literal .notranslate}]{.pre} or [`-DFFT_HEFFTE_MKL`{.docutils .literal .notranslate}]{.pre}, omitting the variable will default to the stock back end. The heFFTe stock back end is intended to be used for testing and debugging, but is not performance optimized for large scale production runs.
:::::::::
::::::::::::::::::

The [KISS FFT library](https://github.com/mborgerding/kissfft){.reference .external} is included in the LAMMPS distribution. It is portable across all platforms. Depending on the size of the FFTs and the number of processors used, the other libraries listed here can be faster.

However, note that long-range Coulombics are only a portion of the per-timestep CPU cost, FFTs are only a portion of long-range Coulombics, and 1d FFTs are only a portion of the FFT cost (parallel communication can be costly). A breakdown of these timings is printed to the screen at the end of a run when using the [[kspace_style pppm]{.doc}]kspace_style.md){.reference .internal} command. The [[Screen and logfile output]{.doc}]Run_output.md){.reference .internal} page gives more details. A more detailed (and time consuming) report of the FFT performance is generated with the [[kspace_modify fftbench yes]{.doc}]kspace_modify.md){.reference .internal} command.

FFTW is a fast, portable FFT library that should also work on any platform and can be faster than the KISS FFT library. You can download it from [www.fftw.org](https://www.fftw.org){.reference .external}. LAMMPS requires version 3.X; the legacy version 2.1.X is no longer supported.

Building FFTW for your box should be as simple as [`./configure;`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`make;`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre}. The install command typically requires root privileges (e.g. invoke it via sudo), unless you specify a local directory with the [`--prefix`{.docutils .literal .notranslate}]{.pre} option of configure. Type [`./configure`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--help`{.docutils .literal .notranslate}]{.pre} to see various options.

The Intel MKL math library is part of the Intel compiler suite. It can be used with the Intel or GNU compiler (see the [`FFT_LIB`{.docutils .literal .notranslate}]{.pre} setting above).

The NVIDIA Performance Libraries (NVPL) FFT library is optimized for NVIDIA Grace Armv9.0 architecture. You can download it from [https://docs.nvidia.com/nvpl/](https://docs.nvidia.com/nvpl/){.reference .external}

The cuFFT and hipFFT FFT libraries are packaged with NVIDIA's CUDA and AMD's HIP installations, respectively. These FFT libraries require the Kokkos acceleration package to be enabled and the Kokkos back end to be GPU-resident (i.e., HIP or CUDA). Similarly, GPU offload of FFTs on Intel GPUs with oneMKL currently requires the Kokkos acceleration package to be enabled with the SYCL back end.

Performing 3d FFTs in parallel can be time-consuming due to data access and required communication. This cost can be reduced by performing single-precision FFTs instead of double precision. Single precision means the real and imaginary parts of a complex datum are 4-byte floats. Double precision means they are 8-byte doubles. Note that Fourier transform and related PPPM operations are somewhat less sensitive to floating point truncation errors, and thus the resulting error is generally less than the difference in precision. Using the [`-DFFT_SINGLE`{.docutils .literal .notranslate}]{.pre} setting trades off a little accuracy for reduced memory use and parallel communication costs for transposing 3d FFT data.

When using [`-DFFT_SINGLE`{.docutils .literal .notranslate}]{.pre} with FFTW3, you may need to ensure that the FFTW3 installation includes support for single-precision.

When compiling FFTW3 from source, you can do the following, which should produce the additional libraries [`libfftw3f.a`{.docutils .literal .notranslate}]{.pre} and [`libfftw3f.so`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-bash .notranslate}
::: highlight
    make clean
    ./configure --enable-single; make; make install
:::
::::

Performing 3d FFTs requires communication to transpose the 3d FFT grid. The data packing/unpacking for this can be done in one of 3 modes (ARRAY, POINTER, MEMCPY) as set by the [`FFT_PACK`{.docutils .literal .notranslate}]{.pre} syntax above. Depending on the machine, the size of the FFT grid, the number of processors used, one option may be slightly faster. The default is ARRAY mode.

When using [`-DFFT_HEFFTE`{.docutils .literal .notranslate}]{.pre} CMake will first look for an existing install with hints provided by [`-DHeffte_ROOT`{.docutils .literal .notranslate}]{.pre}, as recommended by the CMake standard and note that the name is case sensitive. If CMake cannot find a heFFTe installation with the correct back end (e.g., FFTW or MKL), it will attempt to download and build the library automatically. In this case, LAMMPS CMake will also accept all heFFTe specific variables listed in the [heFFTe documentation](https://icl-utk-edu.github.io/heffte/md_doxygen_installation.html){.reference .external} and those variables will be passed into the heFFTe build.

------------------------------------------------------------------------
::::::::::::::::::::::

:::::::::::: {#size-of-lammps-integer-types-and-size-limits .section}
[]{#size}

## [3.6.3. ]{.section-number}Size of LAMMPS integer types and size limits[](#size-of-lammps-integer-types-and-size-limits "Link to this heading"){.headerlink}

LAMMPS uses a few custom integer data types, which can be defined as either 4-byte (= 32-bit) or 8-byte (= 64-bit) integers at compile time. This has an impact on the size of a system that can be simulated, or how large counters can become before "rolling over". The default setting of "smallbig" is almost always adequate.

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional build
:::

::::: {#panel-1-1-0 .sphinx-tabs-panel aria-labelledby="tab-1-1-0" role="tabpanel" tabindex="0"}
With CMake the choice of integer types is made via setting a variable during configuration.

:::: {.highlight-bash .notranslate}
::: highlight
    -D LAMMPS_SIZES=value   # smallbig (default) or bigbig
:::
::::

If the variable is not set explicitly, "smallbig" is used.
:::::

::::: {#panel-1-1-1 .sphinx-tabs-panel aria-labelledby="tab-1-1-1" hidden="true" role="tabpanel" tabindex="0"}
If you want a setting different from the default, you need to edit the [`LMP_INC`{.docutils .literal .notranslate}]{.pre} variable setting your machine Makefile.

:::: {.highlight-make .notranslate}
::: highlight
    LMP_INC = -DLAMMPS_SMALLBIG    # or -DLAMMPS_BIGBIG
:::
::::

The default setting is [`-DLAMMPS_SMALLBIG`{.docutils .literal .notranslate}]{.pre} if nothing is specified
:::::
::::::::::

::: {#lammps-system-size-restrictions .section}
### LAMMPS system size restrictions[](#lammps-system-size-restrictions "Link to this heading"){.headerlink}

+-------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
|                   | smallbig                                                                                                                  | bigbig                                                                                                                    |
+===================+===========================================================================================================================+===========================================================================================================================+
| Total atom count  | [\\(2\^{63}\\)]{.math .notranslate .nohighlight} atoms (= [\\(9.223 \\cdot 10\^{18}\\)]{.math .notranslate .nohighlight}) | [\\(2\^{63}\\)]{.math .notranslate .nohighlight} atoms (= [\\(9.223 \\cdot 10\^{18}\\)]{.math .notranslate .nohighlight}) |
+-------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Total timesteps   | [\\(2\^{63}\\)]{.math .notranslate .nohighlight} steps (= [\\(9.223 \\cdot 10\^{18}\\)]{.math .notranslate .nohighlight}) | [\\(2\^{63}\\)]{.math .notranslate .nohighlight} steps (= [\\(9.223 \\cdot 10\^{18}\\)]{.math .notranslate .nohighlight}) |
+-------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Atom ID values    | [\\(1 \\le i \\le 2\^{31} (= 2.147 \\cdot 10\^9)\\)]{.math .notranslate .nohighlight}                                     | [\\(1 \\le i \\le 2\^{63} (= 9.223 \\cdot 10\^{18})\\)]{.math .notranslate .nohighlight}                                  |
+-------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Image flag values | [\\(-512 \\le i \\le 511\\)]{.math .notranslate .nohighlight}                                                             | [\\(- 1\\,048\\,576 \\le i \\le 1\\,048\\,575\\)]{.math .notranslate .nohighlight}                                        |
+-------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

The "bigbig" setting increases the size of image flags and atom IDs over the default "smallbig" setting.

These are limits for the core of the LAMMPS code, specific features or some styles may impose additional limits. Also, there are limitations when using the library interface where some functions with known issues have been replaced by dummy calls printing a corresponding error message rather than crashing randomly or corrupting data.

Atom IDs are not required for atomic systems which do not store bond topology information, though IDs are enabled by default. The [[atom_modify id no]{.doc}]atom_modify.md){.reference .internal} command will turn them off. Atom IDs are required for molecular systems with bond topology (bonds, angles, dihedrals, etc). Similarly, some force or compute or fix styles require atom IDs. Thus, if you model a molecular system or use one of those styles with more than 2 billion atoms, you need the "bigbig" setting.

Regardless of the total system size limits, the maximum number of atoms per MPI rank (local + ghost atoms) is limited to 2 billion for atomic systems and 500 million for systems with bonds (the additional restriction is due to using the 2 upper bits of the local atom index in neighbor lists for storing special bonds info).

Image flags store 3 values per atom in a single integer, which count the number of times an atom has moved through the periodic box in each dimension. See the [[dump]{.doc}]dump.md){.reference .internal} manual page for a discussion. If an atom moves through the periodic box more than this limit, the value will "roll over", e.g. from 511 to -512, which can cause diagnostics like the mean-squared displacement, as calculated by the [[compute msd]{.doc}]compute_msd.md){.reference .internal} command, to be faulty.

Also note that the GPU package requires its lib/gpu library to be compiled with the same size setting, or the link will fail. A CMake build does this automatically. When building with make, the setting in whichever [`lib/gpu/Makefile`{.docutils .literal .notranslate}]{.pre} is used must be the same as above.

------------------------------------------------------------------------
:::
::::::::::::

::::::::::::: {#read-or-write-compressed-files .section}
[]{#gzip}

## [3.6.4. ]{.section-number}Read or write compressed files[](#read-or-write-compressed-files "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 11Feb2026: ]{.versionmodified .changed}Added support for [`brotli`{.docutils .literal .notranslate}]{.pre} and [`7-zip`{.docutils .literal .notranslate}]{.pre}
:::

If this option is enabled, large files can be read or written with compression by [`gzip`{.docutils .literal .notranslate}]{.pre} or similar tools by several LAMMPS commands, including [[read_data]{.doc}]read_data.md){.reference .internal}, [[write_data]{.doc}]write_data.md){.reference .internal}, [[rerun]{.doc}]rerun.md){.reference .internal}, [[dump]{.doc}]dump.md){.reference .internal}, and [[write_dump]{.doc}]write_dump.md){.reference .internal}. Supported compression tools and algorithms are currently [`gzip`{.docutils .literal .notranslate}]{.pre}, [`bzip2`{.docutils .literal .notranslate}]{.pre}, [`zstd`{.docutils .literal .notranslate}]{.pre}, [`xz`{.docutils .literal .notranslate}]{.pre}, [`lz4`{.docutils .literal .notranslate}]{.pre}, [`lzma`{.docutils .literal .notranslate}]{.pre} (via xz), [`brotli`{.docutils .literal .notranslate}]{.pre}, and [`7-zip`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(via`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`7z)`{.docutils .literal .notranslate}]{.pre}. LAMMPS checks at runtime, which compression commands are available and adjusts the check for supported suffixes accordingly. The list of available compression formats and suffixes is shown when running LAMMPS with the [[-help or -h command_line flag]{.doc}]Run_options.md){.reference .internal}.

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-2-2-0 .sphinx-tabs-panel aria-labelledby="tab-2-2-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D WITH_GZIP=value  # yes or no
                        # default is yes if CMake can find the gzip program
:::
::::
:::::

::::: {#panel-2-2-1 .sphinx-tabs-panel aria-labelledby="tab-2-2-1" hidden="true" role="tabpanel" tabindex="0"}
:::: {.highlight-make .notranslate}
::: highlight
    LMP_INC = -DLAMMPS_GZIP   <other LMP_INC settings>
:::
::::
:::::
::::::::::

This option requires that your operating system fully supports the "popen()" function in the standard runtime library and that a [`gzip`{.docutils .literal .notranslate}]{.pre} or other executable can be found by LAMMPS in the standard search path during a run.

::: {.admonition .note}
Note

On clusters with high-speed networks, using the "fork()" library call (required by "popen()") can interfere with the fast communication library and lead to simulations using compressed output or input to hang or crash. For selected operations, compressed file I/O is also available using a compression library instead, which is what the [[COMPRESS package]{.std .std-ref}]Packages_details.md#pkg-compress){.reference .internal} provides.
:::

------------------------------------------------------------------------
:::::::::::::

:::::::::::::: {#support-for-downloading-files-from-the-input .section}
[]{#libcurl}

## [3.6.5. ]{.section-number}Support for downloading files from the input[](#support-for-downloading-files-from-the-input "Link to this heading"){.headerlink}

::: versionadded
[Added in version 29Aug2024.]{.versionmodified .added}
:::

The [[geturl command]{.doc}]geturl.md){.reference .internal} command uses the [the libcurl library](https://curl.se/libcurl/){.reference .external} to download files. This requires that LAMMPS is compiled accordingly which needs the following settings:

:::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::::: {#panel-3-3-0 .sphinx-tabs-panel aria-labelledby="tab-3-3-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D WITH_CURL=value      # yes or no
                            # default = yes if CMake finds CURL development files, else no
:::
::::

Usually these settings are all that is needed. If CMake cannot find the graphics header, library, executable files, you can set these variables:

:::: {.highlight-bash .notranslate}
::: highlight
    -D CURL_INCLUDE_DIR=path    # path to folder which contains curl.h header file
    -D CURL_LIBRARY=path        # path to libcurls.a (.so) file
:::
::::
:::::::

::::: {#panel-3-3-1 .sphinx-tabs-panel aria-labelledby="tab-3-3-1" hidden="true" role="tabpanel" tabindex="0"}
:::: {.highlight-make .notranslate}
::: highlight
    LMP_INC = -DLAMMPS_CURL  <other LMP_INC settings>

    CURL_INC = -I/usr/local/include   # path to curl folder with curl.h
    CURL_PATH = -L/usr/lib            # paths to libcurl.a(.so) if make cannot find it
    CURL_LIB = -lcurl                 # library names
:::
::::

As with CMake, you do not need to set [`CURL_INC`{.docutils .literal .notranslate}]{.pre} or [`CURL_PATH`{.docutils .literal .notranslate}]{.pre}, if make can find the libcurl header and library files in their default system locations. You must specify [`CURL_LIB`{.docutils .literal .notranslate}]{.pre} with a paths or linker flags to link to libcurl.
:::::
::::::::::::

------------------------------------------------------------------------
::::::::::::::

:::: {#prevent-download-of-large-potential-files .section}
[]{#download-pot}

## [3.6.6. ]{.section-number}Prevent download of large potential files[](#prevent-download-of-large-potential-files "Link to this heading"){.headerlink}

::: versionadded
[Added in version 8Feb2023.]{.versionmodified .added}
:::

LAMMPS bundles a selection of potential files in the [`potentials`{.docutils .literal .notranslate}]{.pre} folder as examples of how those kinds of potential files look like and for use with the provided input examples in the [`examples`{.docutils .literal .notranslate}]{.pre} tree. To keep the size of the distributed LAMMPS source package small, very large potential files (\> 5 MBytes) are not bundled, but only downloaded on demand when the [[corresponding package]{.doc}]Packages.md){.reference .internal} is installed. This automatic download can be prevented when [[building LAMMPS with CMake]{.doc}]Build_cmake.md){.reference .internal} by adding the setting -D DOWNLOAD_POTENTIALS=off when configuring.

------------------------------------------------------------------------
::::

::::::::::: {#memory-allocation-alignment .section}
[]{#align}

## [3.6.7. ]{.section-number}Memory allocation alignment[](#memory-allocation-alignment "Link to this heading"){.headerlink}

This setting enables the use of the [`posix_memalign()`{.docutils .literal .notranslate}]{.pre} call instead of [`malloc()`{.docutils .literal .notranslate}]{.pre} when LAMMPS allocates large chunks of memory. Vector instructions on CPUs may become more efficient, if dynamically allocated memory is aligned on larger-than-default byte boundaries. On most current operating systems, the [`malloc()`{.docutils .literal .notranslate}]{.pre} implementation returns pointers that are aligned to 16-byte boundaries. Using SSE vector instructions efficiently, however, requires memory blocks being aligned on 64-byte boundaries.

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-4-4-0 .sphinx-tabs-panel aria-labelledby="tab-4-4-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D LAMMPS_MEMALIGN=value            # 0, 8, 16, 32, 64 (default)
:::
::::

Use a [`LAMMPS_MEMALIGN`{.docutils .literal .notranslate}]{.pre} value of 0 to disable using [`posix_memalign()`{.docutils .literal .notranslate}]{.pre} and revert to using the [`malloc()`{.docutils .literal .notranslate}]{.pre} C-library function instead. When compiling LAMMPS for Windows systems, [`malloc()`{.docutils .literal .notranslate}]{.pre} will always be used and this setting is ignored.
:::::

::::: {#panel-4-4-1 .sphinx-tabs-panel aria-labelledby="tab-4-4-1" hidden="true" role="tabpanel" tabindex="0"}
:::: {.highlight-make .notranslate}
::: highlight
    LMP_INC = -DLAMMPS_MEMALIGN=value   # 8, 16, 32, 64
:::
::::

Do not set [`-DLAMMPS_MEMALIGN`{.docutils .literal .notranslate}]{.pre}, if you want to have memory allocated with the [`malloc()`{.docutils .literal .notranslate}]{.pre} function call instead. [`-DLAMMPS_MEMALIGN`{.docutils .literal .notranslate}]{.pre} **cannot** be used on Windows, as Windows different function calls with different semantics for allocating aligned memory, that are not compatible with how LAMMPS manages its dynamical memory.
:::::
::::::::::

------------------------------------------------------------------------
:::::::::::

::::::::::: {#workaround-for-long-long-integers .section}
[]{#longlong}

## [3.6.8. ]{.section-number}Workaround for long long integers[](#workaround-for-long-long-integers "Link to this heading"){.headerlink}

If your system or MPI version does not recognize "long long" data types, the following setting will be needed. It converts "long long" to a "long" data type, which should be the desired 8-byte integer on those systems:

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-5-5-0 .sphinx-tabs-panel aria-labelledby="tab-5-5-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D LAMMPS_LONGLONG_TO_LONG=value     # yes or no (default)
:::
::::
:::::

::::: {#panel-5-5-1 .sphinx-tabs-panel aria-labelledby="tab-5-5-1" hidden="true" role="tabpanel" tabindex="0"}
:::: {.highlight-make .notranslate}
::: highlight
    LMP_INC = -DLAMMPS_LONGLONG_TO_LONG  <other LMP_INC settings>
:::
::::
:::::
::::::::::

------------------------------------------------------------------------
:::::::::::

:::: {#exception-handling-when-using-lammps-as-a-library .section}
[]{#exceptions}

## [3.6.9. ]{.section-number}Exception handling when using LAMMPS as a library[](#exception-handling-when-using-lammps-as-a-library "Link to this heading"){.headerlink}

LAMMPS errors do not kill the calling code, but throw an exception. In the C-library interface, the call stack is unwound and control returns to the caller, e.g. to Python or a code that is coupled to LAMMPS. The error status can then be queried. When using C++ directly, the calling code has to be set up to *catch* exceptions thrown from within LAMMPS.

::: {.admonition .note}
Note

When LAMMPS is running in parallel, it is not always possible to cleanly recover from an exception since not all parallel ranks may throw an exception and thus other MPI ranks may get stuck waiting for messages from the ones with errors.
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

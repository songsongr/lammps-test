:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#packages-with-extra-build-options .section}
# [3.8. ]{.section-number}Packages with extra build options[](#packages-with-extra-build-options "Link to this heading"){.headerlink}

When building with some packages, additional steps may be required, in addition to

+-------------------------------------+-------------------------------------+
| CMake build                         | Traditional make                    |
+=====================================+=====================================+
| :::: {.highlight-bash .notranslate} | :::: {.highlight-bash .notranslate} |
| ::: highlight                       | ::: highlight                       |
|     cmake -D PKG_NAME=yes           |     make yes-name                   |
| :::                                 | :::                                 |
| ::::                                | ::::                                |
+-------------------------------------+-------------------------------------+

as described on the [[Build_package]{.doc}]Build_package.md){.reference .internal} page.

For a CMake build there may be additional optional or required variables to set.

::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The traditional build system with GNU make no longer supports packages that require extra steps in the [`lammps/lib`{.docutils .literal .notranslate}]{.pre} directory.

This is the list of packages that may require additional steps.

  ------------------------------------------------------------ ---------------------------------------------------------- ------------------------------------------------------------ -------------------------------------------------------------- ---------------------------------------------------------------- --------------------------------------------------------------
  [[ADIOS]{.std .std-ref}](#adios){.reference .internal}       [[APIP]{.std .std-ref}](#apip){.reference .internal}       [[COLVARS]{.std .std-ref}](#colvar){.reference .internal}    [[COMPRESS]{.std .std-ref}](#compress){.reference .internal}   [[ELECTRODE]{.std .std-ref}](#electrode){.reference .internal}   [[GRAPHICS]{.std .std-ref}](#graphics){.reference .internal}
  [[GPU]{.std .std-ref}](#gpu){.reference .internal}           [[H5MD]{.std .std-ref}](#h5md){.reference .internal}       [[INTEL]{.std .std-ref}](#intel){.reference .internal}       [[KIM]{.std .std-ref}](#kim){.reference .internal}             [[KOKKOS]{.std .std-ref}](#kokkos){.reference .internal}         [[LEPTON]{.std .std-ref}](#lepton){.reference .internal}
  [[MACHDYN]{.std .std-ref}](#machdyn){.reference .internal}   [[MBX]{.std .std-ref}](#mbx){.reference .internal}         [[MDI]{.std .std-ref}](#mdi){.reference .internal}           [[MISC]{.std .std-ref}](#misc){.reference .internal}           [[ML-HDNNP]{.std .std-ref}](#ml-hdnnp){.reference .internal}     [[ML-IAP]{.std .std-ref}](#mliap){.reference .internal}
  [[ML-PACE]{.std .std-ref}](#ml-pace){.reference .internal}   [[ML-POD]{.std .std-ref}](#ml-pod){.reference .internal}   [[ML-QUIP]{.std .std-ref}](#ml-quip){.reference .internal}   [[MOLFILE]{.std .std-ref}](#molfile){.reference .internal}     [[NETCDF]{.std .std-ref}](#netcdf){.reference .internal}         [[OPENMP]{.std .std-ref}](#openmp){.reference .internal}
  [[OPT]{.std .std-ref}](#opt){.reference .internal}           [[PLUMED]{.std .std-ref}](#plumed){.reference .internal}   [[PYTHON]{.std .std-ref}](#python){.reference .internal}     [[QMMM]{.std .std-ref}](#qmmm){.reference .internal}           [[RHEO]{.std .std-ref}](#rheo){.reference .internal}             [[SCAFACOS]{.std .std-ref}](#scafacos){.reference .internal}
  [[VORONOI]{.std .std-ref}](#voronoi){.reference .internal}   [[VTK]{.std .std-ref}](#vtk){.reference .internal}                                                                                                                                                                                                      
  ------------------------------------------------------------ ---------------------------------------------------------- ------------------------------------------------------------ -------------------------------------------------------------- ---------------------------------------------------------------- --------------------------------------------------------------

------------------------------------------------------------------------

:::::::::: {#compress-package .section}
[]{#compress}

## [3.8.1. ]{.section-number}COMPRESS package[](#compress-package "Link to this heading"){.headerlink}

To build with this package you must have the [zlib compression library](https://zlib.net){.reference .external} available on your system to build dump styles with a [`/gz`{.docutils .literal .notranslate}]{.pre} suffix. There are also styles using the [Zstandard](https://facebook.github.io/zstd/){.reference .external} library which have a '/zstd' suffix. The zstd library version must be at least 1.4. Older versions use an incompatible API and thus LAMMPS will fail to compile.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-0-0-0 .sphinx-tabs-panel aria-labelledby="tab-0-0-0" role="tabpanel" tabindex="0"}
If CMake cannot find the zlib library or include files, you can set these variables:

:::: {.highlight-bash .notranslate}
::: highlight
    -D ZLIB_INCLUDE_DIR=path    # path to zlib.h header file
    -D ZLIB_LIBRARY=path        # path to libz.a (.so) file
:::
::::

Support for Zstandard compression is auto-detected and for that CMake depends on the [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/){.reference .external} tool to identify the necessary flags to compile with this library, so the corresponding [`libzstandard.pc`{.docutils .literal .notranslate}]{.pre} file must be in a folder where [`pkg-config`{.docutils .literal .notranslate}]{.pre} can find it, which may require adding it to the [`PKG_CONFIG_PATH`{.docutils .literal .notranslate}]{.pre} environment variable.
:::::

:::: {#panel-0-0-1 .sphinx-tabs-panel aria-labelledby="tab-0-0-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The COMPRESS package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

::::::::::::::: {#graphics-package .section}
[]{#graphics}

## [3.8.2. ]{.section-number}GRAPHICS package[](#graphics-package "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026: ]{.versionmodified .added}*dump image*, *dump_movie* and supporting classes were moved to form the new GRAPHICS package together with several *fix graphics/...* styles.
:::

The [[dump image]{.doc}]dump_image.md){.reference .internal} command has options to output JPEG or PNG image files in addition to the default PPM format, and the [[fix graphics/labels]{.doc}]fix_graphics_labels.md){.reference .internal} can read images in JPEG or PNG format in addition to PPM format files. Likewise, the [[dump movie]{.doc}]dump_image.md){.reference .internal} command outputs movie files in a variety of movie formats. Using these additional options requires the following settings:

:::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::::: {#panel-1-1-0 .sphinx-tabs-panel aria-labelledby="tab-1-1-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D WITH_JPEG=value    # yes or no
                          # default = yes if CMake finds JPEG development files, else no
    -D WITH_PNG=value     # yes or no
                          # default = yes if CMake finds PNG and ZLIB development files,
                          # else no
    -D WITH_FFMPEG=value  # yes or no
                          # default = yes if CMake can find ffmpeg, else no
:::
::::

Usually these settings are all that is needed. If CMake cannot find the graphics header, library, executable files, you can set these variables:

:::: {.highlight-bash .notranslate}
::: highlight
    -D JPEG_INCLUDE_DIR=path    # path to jpeglib.h header file
    -D JPEG_LIBRARY=path        # path to libjpeg.a (.so) file
    -D PNG_INCLUDE_DIR=path     # path to png.h header file
    -D PNG_LIBRARY=path         # path to libpng.a (.so) file
    -D ZLIB_INCLUDE_DIR=path    # path to zlib.h header file
    -D ZLIB_LIBRARY=path        # path to libz.a (.so) file
    -D FFMPEG_EXECUTABLE=path   # path to ffmpeg executable
:::
::::
:::::::

::::: {#panel-1-1-1 .sphinx-tabs-panel aria-labelledby="tab-1-1-1" hidden="true" role="tabpanel" tabindex="0"}
:::: {.highlight-make .notranslate}
::: highlight
    LMP_INC = -DLAMMPS_JPEG -DLAMMPS_PNG -DLAMMPS_FFMPEG  <other LMP_INC settings>

    JPG_INC = -I/usr/local/include   # path to jpeglib.h, png.h, zlib.h headers
                                     # if make cannot find them
    JPG_PATH = -L/usr/lib            # paths to libjpeg.a, libpng.a, libz.a (.so)
                                     # files if make cannot find them
    JPG_LIB = -ljpeg -lpng -lz       # library names
:::
::::

As with CMake, you do not need to set [`JPG_INC`{.docutils .literal .notranslate}]{.pre} or [`JPG_PATH`{.docutils .literal .notranslate}]{.pre}, if make can find the graphics header and library files in their default system locations. You must specify [`JPG_LIB`{.docutils .literal .notranslate}]{.pre} with a list of graphics libraries to include in the link. You must make certain that the ffmpeg executable (or ffmpeg.exe on Windows) is in a directory where LAMMPS can find it at runtime; that is usually a directory list in your [`PATH`{.docutils .literal .notranslate}]{.pre} environment variable.
:::::
::::::::::::

Using [`ffmpeg`{.docutils .literal .notranslate}]{.pre} to output movie files requires that your machine supports the "popen" function in the standard runtime library.

::: {.admonition .note}
Note

On some clusters with high-speed networks, using the fork() library call (required by popen()) can interfere with the fast communication library and lead to simulations using ffmpeg to hang or crash.
:::

------------------------------------------------------------------------
:::::::::::::::

::::::::::::::: {#gpu-package .section}
[]{#gpu}

## [3.8.3. ]{.section-number}GPU package[](#gpu-package "Link to this heading"){.headerlink}

To build with this package, you must choose options for precision and which GPU hardware to build for. The GPU package currently supports three different types of back ends: OpenCL, CUDA and HIP.

:::::::::::::: {#cmake-build .section}
### CMake build[](#cmake-build "Link to this heading"){.headerlink}

:::: {.highlight-bash .notranslate}
::: highlight
    -D GPU_API=value             # value = opencl (default) or cuda or hip
    -D GPU_PREC=value            # precision setting
                                 # value = double or mixed (default) or single
    -D GPU_ARCH=value            # primary GPU hardware choice for GPU_API=cuda
                                 # value = sm_XX (see below, default is sm_75)
    -D GPU_DEBUG=value           # enable debug code in the GPU package library,
                                 # mostly useful for developers
                                 # value = yes or no (default)
    -D HIP_PATH=value            # value = path to HIP installation. Must be set if
                                 # GPU_API=HIP
    -D HIP_ARCH=value            # primary GPU hardware choice for GPU_API=hip
                                 # value depends on selected HIP_PLATFORM
                                 # default is 'gfx906' for HIP_PLATFORM=amd and 'sm_75' for
                                 # HIP_PLATFORM=nvcc
    -D HIP_USE_DEVICE_SORT=value # enables GPU sorting
                                 # value = yes (default) or no
    -D CUDPP_OPT=value           # use GPU binning with CUDA (should be off for modern GPUs)
                                 # enables CUDA Performance Primitives, must be "no" for
                                 # CUDA_MPS_SUPPORT=yes
                                 # value = yes or no (default)
    -D CUDA_MPS_SUPPORT=value    # enables some tweaks required to run with active
                                 # nvidia-cuda-mps daemon
                                 # value = yes or no (default)
    -D CUDA_BUILD_MULTIARCH=value  # enables building CUDA kernels for all supported GPU
                                   # architectures
                                   # value = yes (default) or no
    -D USE_STATIC_OPENCL_LOADER=value  # downloads/includes OpenCL ICD loader library,
                                       # no local OpenCL headers/libs needed
                                       # value = yes (default) or no
:::
::::

The GPU package supports 3 precision modes: single, double, and mixed, with the latter being the default. In the double precision mode, atom positions, forces and energies are stored, computed and accumulated in double precision. In the mixed precision mode, forces and energies are accumulated in double precision while atom coordinates are stored and arithmetic operations are performed in single precision. In the single precision mode, all are stored, executed and accumulated in single precision.

To specify the precision mode (output to the screen before LAMMPS runs for verification), set [`GPU_PREC`{.docutils .literal .notranslate}]{.pre} to one of [`single`{.docutils .literal .notranslate}]{.pre}, [`double`{.docutils .literal .notranslate}]{.pre}, or [`mixed`{.docutils .literal .notranslate}]{.pre}.

Some accelerators or OpenCL implementations only support single precision. This mode should be used with care and appropriate validation as the errors can scale with system size in this implementation. This can be useful for accelerating test runs when setting up a simulation for production runs on another machine. In the case where only single precision is supported, either LAMMPS must be compiled with [`-DFFT_SINGLE`{.docutils .literal .notranslate}]{.pre} to use PPPM with GPU acceleration or GPU acceleration should be disabled for PPPM (e.g. suffix off or [`pair/only`{.docutils .literal .notranslate}]{.pre} as described in the LAMMPS documentation).

[`GPU_ARCH`{.docutils .literal .notranslate}]{.pre} settings for different GPU hardware is as follows:

- [`sm_30`{.docutils .literal .notranslate}]{.pre} for Kepler (supported since CUDA 5 and until CUDA 10.x)

- [`sm_35`{.docutils .literal .notranslate}]{.pre} or [`sm_37`{.docutils .literal .notranslate}]{.pre} for Kepler (supported since CUDA 5 and until CUDA 11.x)

- [`sm_50`{.docutils .literal .notranslate}]{.pre} or [`sm_52`{.docutils .literal .notranslate}]{.pre} for Maxwell (supported since CUDA 6)

- [`sm_60`{.docutils .literal .notranslate}]{.pre} or [`sm_61`{.docutils .literal .notranslate}]{.pre} for Pascal (supported since CUDA 8)

- [`sm_70`{.docutils .literal .notranslate}]{.pre} for Volta (supported since CUDA 9)

- [`sm_75`{.docutils .literal .notranslate}]{.pre} for Turing (supported since CUDA 10)

- [`sm_80`{.docutils .literal .notranslate}]{.pre} or [`sm_86`{.docutils .literal .notranslate}]{.pre} for Ampere (supported since CUDA 11, [`sm_86`{.docutils .literal .notranslate}]{.pre} since CUDA 11.1)

- [`sm_89`{.docutils .literal .notranslate}]{.pre} for Lovelace (supported since CUDA 11.8)

- [`sm_90`{.docutils .literal .notranslate}]{.pre} or [`sm_90a`{.docutils .literal .notranslate}]{.pre} for Hopper (supported since CUDA 12.0)

- [`sm_100`{.docutils .literal .notranslate}]{.pre} or [`sm_103`{.docutils .literal .notranslate}]{.pre} for Blackwell B100/B200/B300 (supported since CUDA 12.8)

- [`sm_120`{.docutils .literal .notranslate}]{.pre} for Blackwell B20x/B40 (supported since CUDA 12.8)

- [`sm_121`{.docutils .literal .notranslate}]{.pre} for Blackwell (supported since CUDA 12.9)

A more detailed list can be found, for example, at [Wikipedia's CUDA article](https://en.wikipedia.org/wiki/CUDA#GPUs_supported){.reference .external}

CMake can detect which version of the CUDA toolkit is used and thus will try to include support for **all** major GPU architectures supported by this toolkit. Thus the [`GPU_ARCH`{.docutils .literal .notranslate}]{.pre} setting is merely an optimization, to have code for the preferred GPU architecture directly included rather than having to wait for the JIT compiler of the CUDA driver to translate it. This behavior can be turned off (e.g. to speed up compilation) by setting [`CUDA_ENABLE_MULTIARCH`{.docutils .literal .notranslate}]{.pre} to [`no`{.docutils .literal .notranslate}]{.pre}.

When compiling for CUDA or HIP with CUDA, version 8.0 or later of the CUDA toolkit is required and a GPU architecture of Kepler or later, which must *also* be supported by the CUDA toolkit in use **and** the CUDA driver in use. When compiling for OpenCL, OpenCL version 1.2 or later is required and the GPU must be supported by the GPU driver and OpenCL runtime bundled with the driver.

Please note that the GPU library accesses the CUDA driver library directly, so it needs to be linked with the CUDA driver library ([`libcuda.so`{.docutils .literal .notranslate}]{.pre}) that ships with the Nvidia driver. If you are compiling LAMMPS on the head node of a GPU cluster, this library may not be installed, so you may need to copy it over from one of the compute nodes (best into this directory). Recent versions of the CUDA toolkit starting from CUDA 9 provide a dummy [`libcuda.so`{.docutils .literal .notranslate}]{.pre} library (typically under [`$(CUDA_HOME)/lib64/stubs`{.docutils .literal .notranslate}]{.pre}), that can be used for linking. If you are compiling LAMMPS with the [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`BUILD_SHARED_LIBS=ON`{.docutils .literal .notranslate}]{.pre} setting, you may get to see [`ld:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`warning:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`libcuda.so.1,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`needed`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`by`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`liblammps.so.0,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`not`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`found`{.docutils .literal .notranslate}]{.pre}. This may be worked around by also setting: [`-DCMAKE_EXE_LINKER_FLAGS=-Wl,--unresolved-symbols=ignore-in-shared-libs`{.docutils .literal .notranslate}]{.pre}.

To support the CUDA multi-process server (MPS) you can set the define [`-DCUDA_MPS_SUPPORT`{.docutils .literal .notranslate}]{.pre}. Please note that in this case you must **not** use the CUDA performance primitives and thus set the variable [`CUDPP_OPT`{.docutils .literal .notranslate}]{.pre} to empty.

If you are compiling for OpenCL, the default setting is to download, build, and link with a static OpenCL ICD loader library and standard OpenCL headers. This way no local OpenCL development headers or library needs to be present and only OpenCL compatible drivers need to be installed to use OpenCL. If this is not desired, you can set [`USE_STATIC_OPENCL_LOADER`{.docutils .literal .notranslate}]{.pre} to [`no`{.docutils .literal .notranslate}]{.pre}.

If [`GERYON_NUMA_FISSION`{.docutils .literal .notranslate}]{.pre} is defined at build time ([`-DGPU_DEBUG=no`{.docutils .literal .notranslate}]{.pre}), LAMMPS will consider separate NUMA nodes on GPUs or accelerators as separate devices. For example, a 2-socket CPU would appear as two separate devices for OpenCL (and LAMMPS would require two MPI processes to use both sockets with the GPU library - each with its own device ID as output by ocl_get_devices). OpenCL version 1.2 or later is required.

If you are compiling with HIP, note that before running CMake you will have to set appropriate environment variables. Some variables such as [`HCC_AMDGPU_TARGET`{.docutils .literal .notranslate}]{.pre} (for ROCm \<= 4.0) or [`CUDA_PATH`{.docutils .literal .notranslate}]{.pre} are necessary for [`hipcc`{.docutils .literal .notranslate}]{.pre} and the linker to work correctly.

When compiling for HIP ROCm, GPU sorting with [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`HIP_USE_DEVICE_SORT=on`{.docutils .literal .notranslate}]{.pre} requires installing the [`hipcub`{.docutils .literal .notranslate}]{.pre} library ([https://github.com/ROCmSoftwarePlatform/hipCUB](https://github.com/ROCmSoftwarePlatform/hipCUB){.reference .external}). The HIP CUDA-backend additionally requires CUB ([https://nvidia.github.io/cccl/cub/](https://nvidia.github.io/cccl/cub/){.reference .external}). Setting [`-DDOWNLOAD_CUB=yes`{.docutils .literal .notranslate}]{.pre} will download and compile CUB.

The GPU library has some multi-thread support using OpenMP. If LAMMPS is built with [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`BUILD_OMP=on`{.docutils .literal .notranslate}]{.pre} this will also be enabled.

For a debug build, set [`GPU_DEBUG`{.docutils .literal .notranslate}]{.pre} to be [`yes`{.docutils .literal .notranslate}]{.pre}.

::: versionadded
[Added in version 3Aug2022.]{.versionmodified .added}
:::

Using the CHIP-SPV implementation of HIP is supported. It allows one to run HIP code on Intel GPUs via the OpenCL or Level Zero back ends. To use CHIP-SPV, you must set [`-DHIP_USE_DEVICE_SORT=OFF`{.docutils .literal .notranslate}]{.pre} in your CMake command-line as CHIP-SPV does not yet support hipCUB. As of Summer 2022, the use of HIP for Intel GPUs is experimental. You should only use this option in preparations to run on Aurora system at Argonne.

:::: {.highlight-bash .notranslate}
::: highlight
    # AMDGPU target (ROCm <= 4.0)
    export HIP_PLATFORM=hcc
    export HIP_PATH=/path/to/HIP/install
    export HCC_AMDGPU_TARGET=gfx906
    cmake -D PKG_GPU=on -D GPU_API=HIP -D HIP_ARCH=gfx906 -D CMAKE_CXX_COMPILER=hipcc ..
    make -j 4
:::
::::

:::: {.highlight-bash .notranslate}
::: highlight
    # AMDGPU target (ROCm >= 4.1)
    export HIP_PLATFORM=amd
    export HIP_PATH=/path/to/HIP/install
    cmake -D PKG_GPU=on -D GPU_API=HIP -D HIP_ARCH=gfx906 -D CMAKE_CXX_COMPILER=hipcc ..
    make -j 4
:::
::::

:::: {.highlight-bash .notranslate}
::: highlight
    # CUDA target (not recommended, use GPU_API=cuda)
    # !!! DO NOT set CMAKE_CXX_COMPILER !!!
    export HIP_PLATFORM=nvcc
    export HIP_PATH=/path/to/HIP/install
    export CUDA_PATH=/usr/local/cuda
    cmake -D PKG_GPU=on -D GPU_API=HIP -D HIP_ARCH=sm_70 ..
    make -j 4
:::
::::

:::: {.highlight-bash .notranslate}
::: highlight
    # SPIR-V target (Intel GPUs)
    export HIP_PLATFORM=spirv
    export HIP_PATH=/path/to/HIP/install
    export CMAKE_CXX_COMPILER=<hipcc/clang++>
    cmake -D PKG_GPU=on -D GPU_API=HIP ..
    make -j 4
:::
::::

------------------------------------------------------------------------
::::::::::::::
:::::::::::::::

:::::::::::: {#kim-package .section}
[]{#kim}

## [3.8.4. ]{.section-number}KIM package[](#kim-package "Link to this heading"){.headerlink}

To build with this package, the KIM API v2.0+ must be downloaded and built on your system. See [Obtaining KIM Models](https://openkim.org/doc/usage/obtaining-models){.reference .external} to learn how to install the KIM API, as well as how to install any models you wish to use afterward. See the list of all KIM models here: [https://openkim.org/browse/models](https://openkim.org/browse/models){.reference .external}

If you would like to use the [[kim query]{.doc}]kim_commands.md){.reference .internal} command, you also need to have libcurl installed with the matching development headers and the curl-config tool.

If you would like to use the [[kim property]{.doc}]kim_commands.md){.reference .internal} command, you need to build LAMMPS with the PYTHON package installed and linked to Python 3.6 or later. See the [[PYTHON package build info]{.std .std-ref}](#python){.reference .internal} for more details on this. After successfully building LAMMPS with Python, you also need to install the [`kim-property`{.docutils .literal .notranslate}]{.pre} Python package, which can be easily done using *pip* as [`pip`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kim-property`{.docutils .literal .notranslate}]{.pre}, or from the *conda-forge* channel as [`conda`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kim-property`{.docutils .literal .notranslate}]{.pre} if LAMMPS is built in Conda. More detailed information is available at: [kim-property installation](https://github.com/openkim/kim-property#installing-kim-property){.reference .external}.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-2-2-0 .sphinx-tabs-panel aria-labelledby="tab-2-2-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D DOWNLOAD_KIM=value           # download OpenKIM API v2 for build
                                    # value = no (default) or yes
    -D LMP_DEBUG_CURL=value         # set libcurl verbose mode on/off
                                    # value = off (default) or on
    -D LMP_NO_SSL_CHECK=value       # tell libcurl to not verify the peer
                                    # value = no (default) or yes
    -D KIM_EXTRA_UNITTESTS=value    # enables extra unit tests
                                    # value = no (default) or yes
:::
::::

If [`DOWNLOAD_KIM`{.docutils .literal .notranslate}]{.pre} is set to [`yes`{.docutils .literal .notranslate}]{.pre} (or [`on`{.docutils .literal .notranslate}]{.pre}), the KIM API library will be downloaded and built inside the CMake build directory. Note that in most cases it is recommended that you do not use this option, and instead provide a KIM API installation yourself before building LAMMPS. If the KIM library is already installed on your system (in a location where CMake cannot find it), you may need to set the [`PKG_CONFIG_PATH`{.docutils .literal .notranslate}]{.pre} environment variable so that libkim-api can be found, or run the command [`source`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kim-api-activate`{.docutils .literal .notranslate}]{.pre}. If CMake cannot find the KIM API when configuring for the first time (or after clearing the CMake cache), the default value of the [`DOWNLOAD_KIM`{.docutils .literal .notranslate}]{.pre} option will be [`yes`{.docutils .literal .notranslate}]{.pre}.

Extra unit tests can only be available if they are explicitly requested ([`KIM_EXTRA_UNITTESTS`{.docutils .literal .notranslate}]{.pre} is set to [`yes`{.docutils .literal .notranslate}]{.pre} (or [`on`{.docutils .literal .notranslate}]{.pre})) and the prerequisites are met. See [[KIM Extra unit tests]{.std .std-ref}](#kim-extra-unittests){.reference .internal} for more details on this.
:::::

:::: {#panel-2-2-1 .sphinx-tabs-panel aria-labelledby="tab-2-2-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The KIM package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

::: {#debugging-openkim-web-queries-in-lammps .section}
### Debugging OpenKIM web queries in LAMMPS[](#debugging-openkim-web-queries-in-lammps "Link to this heading"){.headerlink}

If [`LMP_DEBUG_CURL`{.docutils .literal .notranslate}]{.pre} is set, the libcurl verbose mode will be turned on, and any libcurl calls within the KIM web query display a lot of information about libcurl operations. You hardly ever want this set in production use, you will almost always want this when you debug or report problems.

The libcurl library performs peer SSL certificate verification by default. This verification is done using a CA certificate store that the SSL library can use to make sure the peer's server certificate is valid. If SSL reports an error ("certificate verify failed") during the handshake and thus refuses further communicate with that server, you can set [`LMP_NO_SSL_CHECK`{.docutils .literal .notranslate}]{.pre} to override that behavior. When LAMMPS is compiled with [`LMP_NO_SSL_CHECK`{.docutils .literal .notranslate}]{.pre} set, libcurl does not verify the peer and connection attempts will succeed regardless of the names in the certificate. This option is insecure. As an alternative, you can specify your own CA cert path by setting the environment variable [`CURL_CA_BUNDLE`{.docutils .literal .notranslate}]{.pre} to the path of your choice. A call to the KIM web query would get this value from the environment variable.
:::

::: {#kim-extra-unit-tests-cmake-only .section}
[]{#kim-extra-unittests}

### KIM Extra unit tests (CMake only)[](#kim-extra-unit-tests-cmake-only "Link to this heading"){.headerlink}

During development, testing, or debugging, if [[unit testing]{.doc}]Build_development.md){.reference .internal} is enabled in LAMMPS, one can also enable extra tests on [[KIM commands]{.doc}]kim_commands.md){.reference .internal} by setting the [`KIM_EXTRA_UNITTESTS`{.docutils .literal .notranslate}]{.pre} to [`yes`{.docutils .literal .notranslate}]{.pre} (or [`on`{.docutils .literal .notranslate}]{.pre}).

Enabling the extra unit tests have some requirements,

- It requires to have internet access.

- It requires to have libcurl installed with the matching development headers and the curl-config tool.

- It requires to build LAMMPS with the PYTHON package installed and linked to Python 3.6 or later. See the [[PYTHON package build info]{.std .std-ref}](#python){.reference .internal} for more details on this.

- It requires to have [`kim-property`{.docutils .literal .notranslate}]{.pre} Python package installed, which can be easily done using *pip* as [`pip`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kim-property`{.docutils .literal .notranslate}]{.pre}, or from the *conda-forge* channel as [`conda`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kim-property`{.docutils .literal .notranslate}]{.pre} if LAMMPS is built in Conda. More detailed information is available at: [kim-property installation](https://github.com/openkim/kim-property#installing-kim-property){.reference .external}.

- It is also necessary to install the following KIM models:

  - [`EAM_Dynamo_MendelevAckland_2007v3_Zr__MO_004835508849_001`{.docutils .literal .notranslate}]{.pre}

  - [`EAM_Dynamo_ErcolessiAdams_1994_Al__MO_123629422045_006`{.docutils .literal .notranslate}]{.pre}

  - [`LennardJones612_UniversalShifted__MO_959249795837_003`{.docutils .literal .notranslate}]{.pre} (this model is an example model automatically built with the API unless explicitly disabled)

  See [Obtaining KIM Models](https://openkim.org/doc/usage/obtaining-models){.reference .external} to learn how to install a pre-built binary of the OpenKIM Repository of Models or see [Installing KIM Models](https://openkim.org/doc/usage/obtaining-models/#installing_models){.reference .external} to learn how to install the specific KIM models.

------------------------------------------------------------------------
:::
::::::::::::

::::::::::::::::::::::: {#kokkos-package .section}
[]{#kokkos}

## [3.8.5. ]{.section-number}KOKKOS package[](#kokkos-package "Link to this heading"){.headerlink}

Using the KOKKOS package requires choosing several settings. You have to select whether you want to compile with parallelization on the host and whether you want to include offloading of calculations to a device (e.g. a GPU). The default setting is to have no host parallelization and no device offloading. In addition, you can select the hardware architecture to select the instruction set. Since most hardware is backward compatible, you may choose settings for an older architecture to have an executable that will run on this and newer architectures.

::: {.admonition .note}
Note

If you run Kokkos on a different GPU architecture than what LAMMPS was compiled with, there will be a delay during device initialization while the just-in-time compiler is recompiling all GPU kernels for the new hardware. This is, however, only supported for GPUs of the **same** major hardware version and different minor hardware versions, e.g. 5.0 and 5.2 but not 5.2 and 6.0. LAMMPS will abort with an error message indicating a mismatch, if the major version differs.
:::

The settings discussed below have been tested with LAMMPS and are confirmed to work. Kokkos is an active project with ongoing improvements and projects working on including support for additional architectures. More information on Kokkos can be found on the [Kokkos GitHub project](https://github.com/kokkos){.reference .external}.

:::::::::::::::::::: {#available-architecture-settings .section}
### Available Architecture settings[](#available-architecture-settings "Link to this heading"){.headerlink}

These are the possible choices for the Kokkos architecture ID. They must be specified in uppercase.

  ----------------- ----------------- ---------------------------------------------------------
  **Arch-ID**       **HOST or GPU**   **Description**
  NATIVE            HOST              Local machine
  AMDAVX            HOST              AMD chip
  ARMV80            HOST              ARMv8.0 Compatible CPU
  ARMV81            HOST              ARMv8.1 Compatible CPU
  ARMV84            HOST              ARMv8.4 Compatible CPU
  ARMV84_SVE        HOST              Generic ARMv8.4 with SVE support (-march=armv8.4-a+sve)
  ARMV8_THUNDERX    HOST              ARMv8 Cavium ThunderX CPU
  ARMV8_THUNDERX2   HOST              ARMv8 Cavium ThunderX2 CPU
  A64FX             HOST              ARMv8.2 with SVE Support
  ARMV9_GRACE       HOST              ARMv9 NVIDIA Grace CPU
  SNB               HOST              Intel Sandy/Ivy Bridge CPUs
  HSW               HOST              Intel Haswell CPUs
  BDW               HOST              Intel Broadwell Xeon E-class CPUs
  ICL               HOST              Intel Ice Lake Client CPUs (AVX512)
  ICX               HOST              Intel Ice Lake Xeon Server CPUs (AVX512)
  SKL               HOST              Intel Skylake Client CPUs
  SKX               HOST              Intel Skylake Xeon Server CPUs (AVX512)
  KNC               HOST              Intel Knights Corner Xeon Phi
  KNL               HOST              Intel Knights Landing Xeon Phi
  SPR               HOST              Intel Sapphire Rapids Xeon Server CPUs (AVX512)
  POWER8            HOST              IBM POWER8 CPUs
  POWER9            HOST              IBM POWER9 CPUs
  ZEN               HOST              AMD Zen architecture
  ZEN2              HOST              AMD Zen2 architecture
  ZEN3              HOST              AMD Zen3 architecture
  ZEN4              HOST              AMD Zen4 architecture
  ZEN5              HOST              AMD Zen5 architecture
  RISCV_SG2042      HOST              SG2042 (RISC-V) CPUs
  RISCV_RVA22V      HOST              RVA22V (RISC-V) CPUs
  RISCV_U74MC       HOST              U74MC (RISC-V) CPUs
  KEPLER30          GPU               NVIDIA Kepler generation CC 3.0
  KEPLER32          GPU               NVIDIA Kepler generation CC 3.2
  KEPLER35          GPU               NVIDIA Kepler generation CC 3.5
  KEPLER37          GPU               NVIDIA Kepler generation CC 3.7
  MAXWELL50         GPU               NVIDIA Maxwell generation CC 5.0
  MAXWELL52         GPU               NVIDIA Maxwell generation CC 5.2
  MAXWELL53         GPU               NVIDIA Maxwell generation CC 5.3
  PASCAL60          GPU               NVIDIA Pascal generation CC 6.0
  PASCAL61          GPU               NVIDIA Pascal generation CC 6.1
  VOLTA70           GPU               NVIDIA Volta generation CC 7.0
  VOLTA72           GPU               NVIDIA Volta generation CC 7.2
  TURING75          GPU               NVIDIA Turing generation CC 7.5
  AMPERE80          GPU               NVIDIA Ampere generation CC 8.0
  AMPERE86          GPU               NVIDIA Ampere generation CC 8.6
  AMPERE87          GPU               NVIDIA Ampere generation CC 8.7
  ADA89             GPU               NVIDIA Ada generation CC 8.9
  HOPPER90          GPU               NVIDIA Hopper generation CC 9.0
  BLACKWELL100      GPU               NVIDIA Blackwell generation CC 10.0
  BLACKWELL120      GPU               NVIDIA Blackwell generation CC 12.0
  AMD_GFX906        GPU               AMD GPU MI50/60
  AMD_GFX908        GPU               AMD GPU MI100
  AMD_GFX90A        GPU               AMD GPU MI200
  AMD_GFX940        GPU               AMD GPU MI300
  AMD_GFX942        GPU               AMD GPU MI300
  AMD_GFX942_APU    GPU               AMD APU MI300A
  AMD_GFX1030       GPU               AMD GPU V620/W6800
  AMD_GFX1100       GPU               AMD GPU RX7900XTX
  AMD_GFX1103       GPU               AMD APU Phoenix
  INTEL_GEN         GPU               SPIR64-based devices, e.g. Intel GPUs, using JIT
  INTEL_DG1         GPU               Intel Iris XeMAX GPU
  INTEL_GEN9        GPU               Intel GPU Gen9
  INTEL_GEN11       GPU               Intel GPU Gen11
  INTEL_GEN12LP     GPU               Intel GPU Gen12LP
  INTEL_XEHP        GPU               Intel GPU Xe-HP
  INTEL_PVC         GPU               Intel GPU Ponte Vecchio
  INTEL_DG2         GPU               Intel GPU DG2
  ----------------- ----------------- ---------------------------------------------------------

This list was last updated for version 4.7.1 of the Kokkos library.

::::::::::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
Basic CMake build settings:

Basic traditional make settings:
:::

::::::::::::::: {#panel-3-3-0 .sphinx-tabs-panel aria-labelledby="tab-3-3-0" role="tabpanel" tabindex="0"}
For multicore CPUs using OpenMP, set these 2 variables.

:::: {.highlight-bash .notranslate}
::: highlight
    -D Kokkos_ARCH_HOSTARCH=yes  # HOSTARCH = HOST from list above
    -D Kokkos_ENABLE_OPENMP=yes
    -D BUILD_OMP=yes
:::
::::

Please note that enabling OpenMP for KOKKOS requires that OpenMP is also [[enabled for the rest of LAMMPS]{.std .std-ref}]Build_basics.md#serial){.reference .internal}.

For Intel KNLs using OpenMP, set these variables:

:::: {.highlight-bash .notranslate}
::: highlight
    -D Kokkos_ARCH_KNL=yes
    -D Kokkos_ENABLE_OPENMP=yes
:::
::::

For NVIDIA GPUs using CUDA, set these variables:

:::: {.highlight-bash .notranslate}
::: highlight
    -D Kokkos_ARCH_HOSTARCH=yes   # HOSTARCH = HOST from list above
    -D Kokkos_ARCH_GPUARCH=yes    # GPUARCH = GPU from list above
    -D Kokkos_ENABLE_CUDA=yes
    -D Kokkos_ENABLE_OPENMP=yes
:::
::::

This will also enable executing FFTs on the GPU, either via the internal KISSFFT library, or - by preference - with the cuFFT library bundled with the CUDA toolkit, depending on whether CMake can identify its location.

For AMD or NVIDIA GPUs using HIP, set these variables:

:::: {.highlight-bash .notranslate}
::: highlight
    -D Kokkos_ARCH_HOSTARCH=yes   # HOSTARCH = HOST from list above
    -D Kokkos_ARCH_GPUARCH=yes    # GPUARCH = GPU from list above
    -D Kokkos_ENABLE_HIP=yes
    -D Kokkos_ENABLE_OPENMP=yes
:::
::::

This will enable FFTs on the GPU, either by the internal KISSFFT library or with the hipFFT wrapper library, which will call out to the platform-appropriate vendor library: rocFFT on AMD GPUs or cuFFT on NVIDIA GPUs.

For Intel GPUs using SYCL, set these variables:

:::: {.highlight-bash .notranslate}
::: highlight
    -D Kokkos_ARCH_HOSTARCH=yes   # HOSTARCH = HOST from list above
    -D Kokkos_ARCH_GPUARCH=yes    # GPUARCH = GPU from list above
    -D Kokkos_ENABLE_SYCL=yes
    -D Kokkos_ENABLE_OPENMP=yes
    -D FFT_KOKKOS=MKL_GPU
:::
::::

This will enable FFTs on the GPU using the oneMKL library.

To simplify compilation, seven preset files are included in the [`cmake/presets`{.docutils .literal .notranslate}]{.pre} folder, [`kokkos-serial.cmake`{.docutils .literal .notranslate}]{.pre}, [`kokkos-openmp.cmake`{.docutils .literal .notranslate}]{.pre}, [`kokkos-cuda.cmake`{.docutils .literal .notranslate}]{.pre}, [`kokkos-cuda-nowrapper.cmake`{.docutils .literal .notranslate}]{.pre}, [`kokkos-hip.cmake`{.docutils .literal .notranslate}]{.pre}, [`kokkos-sycl-nvidia.cmake`{.docutils .literal .notranslate}]{.pre}, and [`kokkos-sycl-intel.cmake`{.docutils .literal .notranslate}]{.pre}. They will enable the KOKKOS package and enable some hardware choices. For GPU support those preset files may need to be customized to match the hardware used. For some platforms, e.g. CUDA, the Kokkos library will try to auto-detect a suitable configuration. So to compile with CUDA device parallelization with some common packages enabled, you can do the following:

:::: {.highlight-bash .notranslate}
::: highlight
    mkdir build-kokkos-cuda
    cd build-kokkos-cuda
    cmake -C ../cmake/presets/basic.cmake \
          -C ../cmake/presets/kokkos-cuda-nowrapper.cmake ../cmake
    cmake --build .
:::
::::

The [`kokkos-openmp.cmake`{.docutils .literal .notranslate}]{.pre} preset can be combined with any of the others, but it is not possible to combine multiple GPU acceleration settings (CUDA, HIP, SYCL) into a single executable.
:::::::::::::::

:::: {#panel-3-3-1 .sphinx-tabs-panel aria-labelledby="tab-3-3-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 11Feb2026.]{.versionmodified .changed}
:::

The KOKKOS package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::::::::::::
::::::::::::::::::::

::: {#advanced-kokkos-compilation-settings .section}
### Advanced KOKKOS compilation settings[](#advanced-kokkos-compilation-settings "Link to this heading"){.headerlink}

There are other allowed options when building with the KOKKOS package that can improve performance or assist in debugging or profiling. Below are some examples that may be useful in combination with LAMMPS. For the full list (which keeps changing as the Kokkos package itself evolves), please consult the Kokkos library documentation.

As alternative to using multi-threading via OpenMP ([`-DKokkos_ENABLE_OPENMP=on`{.docutils .literal .notranslate}]{.pre}) it is also possible to use Posix threads directly ([`-DKokkos_ENABLE_PTHREAD=on`{.docutils .literal .notranslate}]{.pre}). While binding of threads to individual or groups of CPU cores is managed in OpenMP with environment variables, you need assistance from either the "hwloc" or "libnuma" library for the Pthread thread parallelization option. To enable use with CMake: [`-DKokkos_ENABLE_HWLOC=on`{.docutils .literal .notranslate}]{.pre} or [`-DKokkos_ENABLE_LIBNUMA=on`{.docutils .literal .notranslate}]{.pre}.

The CMake option [`-DKokkos_ENABLE_LIBRT=on`{.docutils .literal .notranslate}]{.pre} enables the use of a more accurate timer mechanism on many Unix-like platforms for internal profiling.

The CMake option [`-DKokkos_ENABLE_DEBUG=on`{.docutils .literal .notranslate}]{.pre} enables printing of run-time debugging information that can be useful. It also enables runtime bounds checking on Kokkos data structures. As to be expected, enabling this option will negatively impact the performance and thus is only recommended when developing a Kokkos-enabled style in LAMMPS.

The CMake option [`-DKokkos_ENABLE_CUDA_UVM=on`{.docutils .literal .notranslate}]{.pre} enables the use of CUDA "Unified Virtual Memory" (UVM) in Kokkos. UVM allows to transparently use RAM on the host to supplement the memory used on the GPU (with some performance penalty) and thus enables running larger problems that would otherwise not fit into the RAM on the GPU.

The CMake option [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`KOKKOS_PREC=value`{.docutils .literal .notranslate}]{.pre} sets the floating point precision of the calculations, where [`value`{.docutils .literal .notranslate}]{.pre} can be one of: [`double`{.docutils .literal .notranslate}]{.pre} (FP64, default) or [`mixed`{.docutils .literal .notranslate}]{.pre} (FP64 for accumulation of forces, energy, and virial, FP32 otherwise) or [`single`{.docutils .literal .notranslate}]{.pre} (FP32). When using reduced precision (single or mixed), the simulation should be carefully checked to ensure it is stable and that energy is acceptably conserved.

The CMake option [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`KOKKOS_LAYOUT=value`{.docutils .literal .notranslate}]{.pre} sets the array layout of Kokkos views (e.g. forces, velocities, etc.) on GPUs, where [`value`{.docutils .literal .notranslate}]{.pre} can be one of: [`legacy`{.docutils .literal .notranslate}]{.pre} (mostly LayoutRight, default) or [`default`{.docutils .literal .notranslate}]{.pre} (mostly LayoutLeft). Using the default layout (LayoutLeft) can give speedup on GPUs for some models, but a slowdown for others. LayoutRight is always used for positions on GPUs since it has been found to be faster, and when compiling exclusively for CPUs.

------------------------------------------------------------------------
:::
:::::::::::::::::::::::

:::::::: {#lepton-package .section}
[]{#lepton}

## [3.8.6. ]{.section-number}LEPTON package[](#lepton-package "Link to this heading"){.headerlink}

To build with this package, you must build the Lepton library which is included in the LAMMPS source distribution in the [`lib/lepton`{.docutils .literal .notranslate}]{.pre} folder.

::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::: {#panel-4-4-0 .sphinx-tabs-panel aria-labelledby="tab-4-4-0" role="tabpanel" tabindex="0"}
This is the recommended build procedure for using Lepton in LAMMPS. No additional settings are normally needed besides [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_LEPTON=yes`{.docutils .literal .notranslate}]{.pre}.

On x86 hardware the Lepton library will also include a just-in-time compiler for faster execution. This is auto detected but can be explicitly disabled by setting [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`LEPTON_ENABLE_JIT=no`{.docutils .literal .notranslate}]{.pre} (or enabled by setting it to yes).
:::

:::: {#panel-4-4-1 .sphinx-tabs-panel aria-labelledby="tab-4-4-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The LEPTON package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::

------------------------------------------------------------------------
::::::::

:::::::::: {#machdyn-package .section}
[]{#machdyn}

## [3.8.7. ]{.section-number}MACHDYN package[](#machdyn-package "Link to this heading"){.headerlink}

To build with this package, you must download the Eigen3 library. Eigen3 is a template library, so you do not need to build it.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-5-5-0 .sphinx-tabs-panel aria-labelledby="tab-5-5-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D DOWNLOAD_EIGEN3            # download Eigen3, value = no (default) or yes
    -D EIGEN3_INCLUDE_DIR=path    # path to Eigen library (only needed if a
                                  # custom location)
:::
::::

If [`DOWNLOAD_EIGEN3`{.docutils .literal .notranslate}]{.pre} is set, the Eigen3 library will be downloaded and inside the CMake build directory. If the Eigen3 library is already on your system (in a location where CMake cannot find it), set [`EIGEN3_INCLUDE_DIR`{.docutils .literal .notranslate}]{.pre} to the directory the [`Eigen3`{.docutils .literal .notranslate}]{.pre} include file is in.
:::::

:::: {#panel-5-5-1 .sphinx-tabs-panel aria-labelledby="tab-5-5-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The MACHDYN package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

::::::::: {#ml-iap-package .section}
[]{#mliap}

## [3.8.8. ]{.section-number}ML-IAP package[](#ml-iap-package "Link to this heading"){.headerlink}

Building the ML-IAP package requires including the [[ML-SNAP]{.std .std-ref}]Packages_details.md#pkg-ml-snap){.reference .internal} package. There will be an error message if this requirement is not satisfied. Using the *mliappy* model also requires enabling Python support, which in turn requires to include the [[PYTHON]{.std .std-ref}]Packages_details.md#pkg-python){.reference .internal} package **and** requires to have the [cython](https://cython.org){.reference .external} software installed and with it a working [`cythonize`{.docutils .literal .notranslate}]{.pre} command. This feature requires compiling LAMMPS with Python version 3.6 or later.

:::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-6-6-0 .sphinx-tabs-panel aria-labelledby="tab-6-6-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D MLIAP_ENABLE_PYTHON=value   # enable mliappy model (default is autodetect)
:::
::::

Without this setting, CMake will check whether it can find a suitable Python version and the [`cythonize`{.docutils .literal .notranslate}]{.pre} command and choose the default accordingly. During the build procedure the provided .pyx file(s) will be automatically translated to C++ code and compiled. Please do **not** run [`cythonize`{.docutils .literal .notranslate}]{.pre} manually in the [`src/ML-IAP`{.docutils .literal .notranslate}]{.pre} folder, as that can lead to compilation errors if Python support is not enabled. If you did it by accident, please remove the generated .cpp and .h files.
:::::

::: {#panel-6-6-1 .sphinx-tabs-panel aria-labelledby="tab-6-6-1" hidden="true" role="tabpanel" tabindex="0"}
The build uses the [`lib/python/Makefile.mliap_python`{.docutils .literal .notranslate}]{.pre} file in the compile/link process to add a rule to update the files generated by the [`cythonize`{.docutils .literal .notranslate}]{.pre} command in case the corresponding .pyx file(s) were modified. You may need to modify [`lib/python/Makefile.lammps`{.docutils .literal .notranslate}]{.pre} if the LAMMPS build fails.

To enable building the ML-IAP package with Python support enabled, you need to add [`-DMLIAP_PYTHON`{.docutils .literal .notranslate}]{.pre} to the [`LMP_INC`{.docutils .literal .notranslate}]{.pre} variable in your machine makefile. You may have to manually run the [`cythonize`{.docutils .literal .notranslate}]{.pre} command on .pyx file(s) in the [`src`{.docutils .literal .notranslate}]{.pre} folder, if this is not automatically done during installing the ML-IAP package. Please do **not** run [`cythonize`{.docutils .literal .notranslate}]{.pre} in the [`src/ML-IAP`{.docutils .literal .notranslate}]{.pre} folder, as that can lead to compilation errors if Python support is not enabled. If you did this by accident, please remove the generated .cpp and .h files.
:::
::::::::

------------------------------------------------------------------------
:::::::::

::::::: {#opt-package .section}
[]{#opt}

## [3.8.9. ]{.section-number}OPT package[](#opt-package "Link to this heading"){.headerlink}

:::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::: {#panel-7-7-0 .sphinx-tabs-panel aria-labelledby="tab-7-7-0" role="tabpanel" tabindex="0"}
No additional settings are needed besides [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_OPT=yes`{.docutils .literal .notranslate}]{.pre}
:::

::: {#panel-7-7-1 .sphinx-tabs-panel aria-labelledby="tab-7-7-1" hidden="true" role="tabpanel" tabindex="0"}
The compiler flag [`-restrict`{.docutils .literal .notranslate}]{.pre} must be used to build LAMMPS with the OPT package when using Intel compilers. It should be added to the [`CCFLAGS`{.docutils .literal .notranslate}]{.pre} line of your [`Makefile.machine`{.docutils .literal .notranslate}]{.pre}. See [`src/MAKE/OPTIONS/Makefile.opt`{.docutils .literal .notranslate}]{.pre} for an example.
:::
::::::

------------------------------------------------------------------------
:::::::

:::::::::: {#python-package .section}
[]{#python}

## [3.8.10. ]{.section-number}PYTHON package[](#python-package "Link to this heading"){.headerlink}

Building with the PYTHON package requires you have a the Python development headers and library available on your system, which needs to be Python version 3.6 or later. See [`lib/python/README`{.docutils .literal .notranslate}]{.pre} for additional details.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-8-8-0 .sphinx-tabs-panel aria-labelledby="tab-8-8-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D Python_EXECUTABLE=path   # path to Python executable to use
:::
::::

Without this setting, CMake will guess the default Python version on your system. To use a different Python version, you can either create a virtualenv, activate it and then run cmake. Or you can set the Python_EXECUTABLE variable to specify which Python interpreter should be used. Note note that you will also need to have the development headers installed for this version, e.g. python3-devel.
:::::

:::: {#panel-8-8-1 .sphinx-tabs-panel aria-labelledby="tab-8-8-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The PYTHON package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

:::::::::: {#voronoi-package .section}
[]{#voronoi}

## [3.8.11. ]{.section-number}VORONOI package[](#voronoi-package "Link to this heading"){.headerlink}

To build with this package, you must download and build the [Voro++ library](https://math.lbl.gov/voro++/){.reference .external} or install a binary package provided by your operating system.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-9-9-0 .sphinx-tabs-panel aria-labelledby="tab-9-9-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D DOWNLOAD_VORO=value    # download Voro++ for build
                              # value = no (default) or yes
    -D VORO_LIBRARY=path      # Voro++ library file
                              # (only needed if at custom location)
    -D VORO_INCLUDE_DIR=path  # Voro++ include directory
                              # (only needed if at custom location)
:::
::::

If [`DOWNLOAD_VORO`{.docutils .literal .notranslate}]{.pre} is set, the Voro++ library will be downloaded and built inside the CMake build directory. If the Voro++ library is already on your system (in a location CMake cannot find it), [`VORO_LIBRARY`{.docutils .literal .notranslate}]{.pre} is the filename (plus path) of the Voro++ library file, not the directory the library file is in. [`VORO_INCLUDE_DIR`{.docutils .literal .notranslate}]{.pre} is the directory the Voro++ include file is in.
:::::

:::: {#panel-9-9-1 .sphinx-tabs-panel aria-labelledby="tab-9-9-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The VORONOI package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

::::::::::::: {#adios-package .section}
[]{#adios}

## [3.8.12. ]{.section-number}ADIOS package[](#adios-package "Link to this heading"){.headerlink}

The ADIOS package requires the [ADIOS I/O library](https://github.com/ornladios/ADIOS2){.reference .external}, version 2.3.1 or newer. Make sure that you have ADIOS built either with or without MPI to match if you build LAMMPS with or without MPI. ADIOS compilation settings for LAMMPS are automatically detected, if the PATH and LD_LIBRARY_PATH environment variables have been updated for the local ADIOS installation and the instructions below are followed for the respective build systems.

:::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-10-10-0 .sphinx-tabs-panel aria-labelledby="tab-10-10-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D ADIOS2_DIR=path        # path is where ADIOS 2.x is installed
    -D PKG_ADIOS=yes
:::
::::
:::::

::::::: {#panel-10-10-1 .sphinx-tabs-panel aria-labelledby="tab-10-10-1" hidden="true" role="tabpanel" tabindex="0"}
Turn on the ADIOS package before building LAMMPS. If the ADIOS 2.x software is installed in PATH, there is nothing else to do:

:::: {.highlight-bash .notranslate}
::: highlight
    make yes-adios
:::
::::

otherwise, set ADIOS2_DIR environment variable when turning on the package:

:::: {.highlight-bash .notranslate}
::: highlight
    ADIOS2_DIR=path make yes-adios   # path is where ADIOS 2.x is installed
:::
::::
:::::::
::::::::::::

------------------------------------------------------------------------
:::::::::::::

:::::::: {#apip-package .section}
[]{#apip}

## [3.8.13. ]{.section-number}APIP package[](#apip-package "Link to this heading"){.headerlink}

The APIP package depends on the library of the [[ML-PACE]{.std .std-ref}](#ml-pace){.reference .internal} package. The code for the library can be found at: [https://github.com/ICAMS/lammps-user-pace/](https://github.com/ICAMS/lammps-user-pace/){.reference .external}

::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::: {#panel-11-11-0 .sphinx-tabs-panel aria-labelledby="tab-11-11-0" role="tabpanel" tabindex="0"}
No additional settings are needed besides [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_APIP=yes`{.docutils .literal .notranslate}]{.pre} and [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_ML-PACE=yes`{.docutils .literal .notranslate}]{.pre}. One can use a local version of the ML-PACE library instead of automatically downloading the library as described [[here]{.std .std-ref}](#ml-pace){.reference .internal}.
:::

:::: {#panel-11-11-1 .sphinx-tabs-panel aria-labelledby="tab-11-11-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The APIP package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::

------------------------------------------------------------------------
::::::::

:::::::::: {#colvars-package .section}
[]{#colvar}

## [3.8.14. ]{.section-number}COLVARS package[](#colvars-package "Link to this heading"){.headerlink}

This package enables the use of the [Colvars](https://colvars.github.io/){.reference .external} module included in the LAMMPS source distribution.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-12-12-0 .sphinx-tabs-panel aria-labelledby="tab-12-12-0" role="tabpanel" tabindex="0"}
This is the recommended build procedure for using Colvars in LAMMPS. No additional settings are normally needed besides [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_COLVARS=yes`{.docutils .literal .notranslate}]{.pre}. The following CMake variables are available.

:::: {.highlight-bash .notranslate}
::: highlight
    -D PKG_COLVARS=yes          # enable the package itself
    -D COLVARS_LEPTON=yes       # use the Lepton library for custom expression (on by defaul)
    -D COLVARS_DEBUG=no         # eneable debugging message (verbose, off by default)
:::
::::
:::::

:::: {#panel-12-12-1 .sphinx-tabs-panel aria-labelledby="tab-12-12-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The COLVARS package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

::::::::: {#electrode-package .section}
[]{#electrode}

## [3.8.15. ]{.section-number}ELECTRODE package[](#electrode-package "Link to this heading"){.headerlink}

This package depends on the KSPACE package.

:::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-13-13-0 .sphinx-tabs-panel aria-labelledby="tab-13-13-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D PKG_ELECTRODE=yes          # enable the package itself
    -D PKG_KSPACE=yes             # the ELECTRODE package requires KSPACE
    -D USE_INTERNAL_LINALG=value  #
:::
::::

Features in the ELECTRODE package are dependent on code in the KSPACE package so the latter one *must* be enabled.

The ELECTRODE package also requires LAPACK (and BLAS) and CMake can identify their locations and pass that info to the ELECTRODE build script. But on some systems this may cause problems when linking or the dependency is not desired. Try enabling [`USE_INTERNAL_LINALG`{.docutils .literal .notranslate}]{.pre} in those cases to use the bundled linear algebra library and work around the limitation.
:::::

::: {#panel-13-13-1 .sphinx-tabs-panel aria-labelledby="tab-13-13-1" hidden="true" role="tabpanel" tabindex="0"}
The ELECTRODE package no longer supports the traditional make build. You need to build LAMMPS with CMake.
:::
::::::::

------------------------------------------------------------------------
:::::::::

::::::::: {#mbx-package .section}
[]{#mbx}

## [3.8.16. ]{.section-number}MBX package[](#mbx-package "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

This package requires the MBX library that can be downloaded and built either before LAMMPS is built or as part of the LAMMPS compilation. The code for the library can be found at: [https://github.com/paesanilab/MBX/](https://github.com/paesanilab/MBX/){.reference .external}

Instead of including the MBX package directly into LAMMPS, it is also possible to skip this step and build the MBX package as a plugin using the CMake script files in the [`examples/PACKAGE/mbx/plugin`{.docutils .literal .notranslate}]{.pre} folder and then load this plugin at runtime with the [[plugin command]{.doc}]plugin.md){.reference .internal}.

::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

:::: {#panel-14-14-0 .sphinx-tabs-panel aria-labelledby="tab-14-14-0" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 30Mar2026: ]{.versionmodified .changed}Replaced MD5 checksums with SHA-256
:::

By default the MBX library will be downloaded from the git repository and built automatically when the MBX package is enabled with [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_MBX=yes`{.docutils .literal .notranslate}]{.pre}. The location for the sources may be customized by setting the variable [`MBXLIB_URL`{.docutils .literal .notranslate}]{.pre} when configuring with CMake (e.g. to use a local archive on machines without internet access). Since CMake checks the validity of the archive using a SHA-256 checksum you may also need to set the [`MBXLIB_SHA256`{.docutils .literal .notranslate}]{.pre} variable to the corresponding checksum (e.g. computed with [`sha256sum`{.docutils .literal .notranslate}]{.pre}) if you provide a different library version than what is downloaded automatically.
::::

::: {#panel-14-14-1 .sphinx-tabs-panel aria-labelledby="tab-14-14-1" hidden="true" role="tabpanel" tabindex="0"}
The MBX package does not support the traditional make build. You need to build LAMMPS with CMake to use it.
:::
:::::::

------------------------------------------------------------------------
:::::::::

::::::::: {#ml-pace-package .section}
[]{#ml-pace}

## [3.8.17. ]{.section-number}ML-PACE package[](#ml-pace-package "Link to this heading"){.headerlink}

This package requires a library that can be downloaded and built in lib/pace or somewhere else, which must be done before building LAMMPS with this package. The code for the library can be found at: [https://github.com/ICAMS/lammps-user-pace/](https://github.com/ICAMS/lammps-user-pace/){.reference .external}

Instead of including the ML-PACE package directly into LAMMPS, it is also possible to skip this step and build the ML-PACE package as a plugin using the CMake script files in the [`examples/PACKAGE/pace/plugin`{.docutils .literal .notranslate}]{.pre} folder and then load this plugin at runtime with the [[plugin command]{.doc}]plugin.md){.reference .internal}.

:::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

:::: {#panel-15-15-0 .sphinx-tabs-panel aria-labelledby="tab-15-15-0" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 30Mar2026: ]{.versionmodified .changed}Replaced MD5 checksums with SHA-256
:::

By default the library will be downloaded from the git repository and built automatically when the ML-PACE package is enabled with [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_ML-PACE=yes`{.docutils .literal .notranslate}]{.pre}. The location for the sources may be customized by setting the variable [`PACELIB_URL`{.docutils .literal .notranslate}]{.pre} when configuring with CMake (e.g. to use a local archive on machines without internet access). Since CMake checks the validity of the archive using a SHA-256 checksum you may also need to set the [`PACELIB_SHA256`{.docutils .literal .notranslate}]{.pre} variable to the corresponding checksum (e.g. computed with [`sha256sum`{.docutils .literal .notranslate}]{.pre}) if you provide a different library version than what is downloaded automatically.
::::

:::: {#panel-15-15-1 .sphinx-tabs-panel aria-labelledby="tab-15-15-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The ML-PACE package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
::::::::

------------------------------------------------------------------------
:::::::::

:::::::: {#ml-pod-package .section}
[]{#ml-pod}

## [3.8.18. ]{.section-number}ML-POD package[](#ml-pod-package "Link to this heading"){.headerlink}

::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::: {#panel-16-16-0 .sphinx-tabs-panel aria-labelledby="tab-16-16-0" role="tabpanel" tabindex="0"}
No additional settings are needed besides [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_ML-POD=yes`{.docutils .literal .notranslate}]{.pre}.
:::

:::: {#panel-16-16-1 .sphinx-tabs-panel aria-labelledby="tab-16-16-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The ML-POD package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::

------------------------------------------------------------------------
::::::::

:::::::::: {#ml-quip-package .section}
[]{#ml-quip}

## [3.8.19. ]{.section-number}ML-QUIP package[](#ml-quip-package "Link to this heading"){.headerlink}

To build with this package, you must download and build the QUIP library. It can be obtained from GitHub. For support of GAP potentials, additional files with specific licensing conditions need to be downloaded and configured. The automatic download will from within CMake will download the non-commercial use version.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-17-17-0 .sphinx-tabs-panel aria-labelledby="tab-17-17-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D DOWNLOAD_QUIP=value       # download QUIP library for build
                                 # value = no (default) or yes
    -D QUIP_LIBRARY=path         # path to libquip.a
                                 # (only needed if a custom location)
    -D USE_INTERNAL_LINALG=value # Use the internal linear algebra library
                                 # instead of LAPACK
                                 # value = no (default) or yes
:::
::::

CMake will try to download and build the QUIP library from GitHub, if it is not found on the local machine. This requires to have git installed. It will use the same compilers and flags as used for compiling LAMMPS. Currently this is only supported for the GNU and the Intel compilers. Set the [`QUIP_LIBRARY`{.docutils .literal .notranslate}]{.pre} variable if you want to use a previously compiled and installed QUIP library and CMake cannot find it.

The QUIP library requires LAPACK (and BLAS) and CMake can identify their locations and pass that info to the QUIP build script. But on some systems this triggers a (current) limitation of CMake and the configuration will fail. Try enabling [`USE_INTERNAL_LINALG`{.docutils .literal .notranslate}]{.pre} in those cases to use the bundled linear algebra library and work around the limitation.
:::::

:::: {#panel-17-17-1 .sphinx-tabs-panel aria-labelledby="tab-17-17-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The ML-QUIP package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

:::::::::: {#plumed-package .section}
[]{#plumed}

## [3.8.20. ]{.section-number}PLUMED package[](#plumed-package "Link to this heading"){.headerlink}

Before building LAMMPS with this package, you must first build PLUMED. PLUMED can be built as part of the LAMMPS build or installed separately from LAMMPS using the generic [PLUMED installation instructions](https://www.plumed.org/doc-v2.9/user-doc/html/_installation.html){.reference .external}. The PLUMED package has been tested to work with Plumed versions 2.4.x, to 2.9.x and will error out, when trying to run calculations with a different version of the Plumed kernel.

PLUMED can be linked into MD codes in three different modes: static, shared, and runtime. With the "static" mode, all the code that PLUMED requires is linked statically into LAMMPS. LAMMPS is then fully independent from the PLUMED installation, but you have to rebuild/relink it in order to update the PLUMED code inside it. With the "shared" linkage mode, LAMMPS is linked to a shared library that contains the PLUMED code. This library should preferably be installed in a globally accessible location. When PLUMED is linked in this way the same library can be used by multiple MD packages. Furthermore, the PLUMED library LAMMPS uses can be updated without the need for a recompile of LAMMPS for as long as the shared PLUMED library is ABI-compatible.

The third linkage mode is "runtime" which allows the user to specify which PLUMED kernel should be used at runtime by using the PLUMED_KERNEL environment variable. This variable should point to the location of the libplumedKernel.so dynamical shared object, which is then loaded at runtime. This mode of linking is particularly convenient for doing PLUMED development and comparing multiple PLUMED versions as these sorts of comparisons can be done without recompiling the hosting MD code. All three linkage modes are supported by LAMMPS on selected operating systems (e.g. Linux) and using either CMake or traditional make build. The "static" mode should be the most portable, while the "runtime" mode support in LAMMPS makes the most assumptions about operating system and compiler environment. If one mode does not work, try a different one, switch to a different build system, consider a global PLUMED installation or consider downloading PLUMED during the LAMMPS build.

Instead of including the PLUMED package directly into LAMMPS, it is also possible to skip this step and build the PLUMED package as a plugin using the CMake script files in the [`examples/PACKAGE/plumed/plugin`{.docutils .literal .notranslate}]{.pre} folder and then load this plugin at runtime with the [[plugin command]{.doc}]plugin.md){.reference .internal}.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-18-18-0 .sphinx-tabs-panel aria-labelledby="tab-18-18-0" role="tabpanel" tabindex="0"}
When the [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_PLUMED=yes`{.docutils .literal .notranslate}]{.pre} flag is included in the cmake command you must ensure that the GNU Scientific Library (GSL) \<https://www.gnu.org/software/gsl/\> is installed in locations that are accessible in your environment. There are then two additional variables that control the manner in which PLUMED is obtained and linked into LAMMPS.

:::: {.highlight-bash .notranslate}
::: highlight
    -D DOWNLOAD_PLUMED=value   # download PLUMED for build
                               # value = no (default) or yes
    -D PLUMED_MODE=value       # Linkage mode for PLUMED
                               # value = static (default), shared,
                               #         or runtime
:::
::::

If [`DOWNLOAD_PLUMED`{.docutils .literal .notranslate}]{.pre} is set to [`yes`{.docutils .literal .notranslate}]{.pre}, the PLUMED library will be downloaded (the version of PLUMED that will be downloaded is hard-coded to a vetted version of PLUMED, usually a recent stable release version) and built inside the CMake build directory. If [`DOWNLOAD_PLUMED`{.docutils .literal .notranslate}]{.pre} is set to "no" (the default), CMake will try to detect and link to an installed version of PLUMED. For this to work, the PLUMED library has to be installed into a location where the [`pkg-config`{.docutils .literal .notranslate}]{.pre} tool can find it or the [`PKG_CONFIG_PATH`{.docutils .literal .notranslate}]{.pre} environment variable has to be set up accordingly. PLUMED should be installed in such a location if you compile it using the default make; make install commands.

The [`PLUMED_MODE`{.docutils .literal .notranslate}]{.pre} setting determines the linkage mode for the PLUMED library. The allowed values for this flag are "static" (default), "shared", or "runtime". If you want to switch the linkage mode, just re-run CMake with a different setting. For a discussion of PLUMED linkage modes, please see above. When [`DOWNLOAD_PLUMED`{.docutils .literal .notranslate}]{.pre} is enabled the static linkage mode is recommended.
:::::

:::: {#panel-18-18-1 .sphinx-tabs-panel aria-labelledby="tab-18-18-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The PLUMED package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

:::::::: {#h5md-package .section}
[]{#h5md}

## [3.8.21. ]{.section-number}H5MD package[](#h5md-package "Link to this heading"){.headerlink}

To build with this package you must have the HDF5 software package installed on your system, which should include the h5cc compiler and the HDF5 library.

::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::: {#panel-19-19-0 .sphinx-tabs-panel aria-labelledby="tab-19-19-0" role="tabpanel" tabindex="0"}
No additional settings are needed besides [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_H5MD=yes`{.docutils .literal .notranslate}]{.pre}.

This should auto-detect the H5MD library on your system. Several advanced CMake H5MD options exist if you need to specify where it is installed. Use the ccmake (terminal window) or cmake-gui (graphical) tools to see these options and set them interactively from their user interfaces.
:::

:::: {#panel-19-19-1 .sphinx-tabs-panel aria-labelledby="tab-19-19-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The H5MD package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::

------------------------------------------------------------------------
::::::::

::::::::::: {#ml-hdnnp-package .section}
[]{#ml-hdnnp}

## [3.8.22. ]{.section-number}ML-HDNNP package[](#ml-hdnnp-package "Link to this heading"){.headerlink}

To build with the ML-HDNNP package it is required to download and build the external [n2p2](https://github.com/CompPhysVienna/n2p2){.reference .external} library [`v2.1.4`{.docutils .literal .notranslate}]{.pre} (or higher). The LAMMPS build process offers an automatic download and compilation of *n2p2* or allows you to choose the installation directory of *n2p2* manually. Please see the boxes below for the CMake and traditional build system for detailed information.

In case of a manual installation of *n2p2* you only need to build the *n2p2* core library [`libnnp`{.docutils .literal .notranslate}]{.pre} and interface library [`libnnpif`{.docutils .literal .notranslate}]{.pre}. When using GCC it should suffice to execute [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`libnnpif`{.docutils .literal .notranslate}]{.pre} in the *n2p2* [`src`{.docutils .literal .notranslate}]{.pre} directory. For more details please see [`lib/hdnnp/README`{.docutils .literal .notranslate}]{.pre} and the [n2p2 build documentation](https://compphysvienna.github.io/n2p2/topics/build.html){.reference .external}.

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

:::::: {#panel-20-20-0 .sphinx-tabs-panel aria-labelledby="tab-20-20-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D DOWNLOAD_N2P2=value    # download n2p2 for build
                              # value = no (default) or yes
    -D N2P2_DIR=path          # n2p2 base directory
                              # (only needed if a custom location)
:::
::::

If [`DOWNLOAD_N2P2`{.docutils .literal .notranslate}]{.pre} is set, the *n2p2* library will be downloaded and built inside the CMake build directory. If the *n2p2* library is already on your system (in a location CMake cannot find it), set the [`N2P2_DIR`{.docutils .literal .notranslate}]{.pre} to path where *n2p2* is located. If *n2p2* is located directly in [`lib/hdnnp/n2p2`{.docutils .literal .notranslate}]{.pre} it will be automatically found by CMake.

::: {.note .admonition}
Failure to build n2p2 due to git branch names

Some script code inside the *n2p2* library build processes the current branch name used by git and that will fail for LAMMPS repository branch names containing the forward slash '/' character, for example: [`user/update-n2p2`{.docutils .literal .notranslate}]{.pre}. The workaround is to change the (local) branch name, e.g. for the given example with: [`git`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`branch`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-m`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`user/update-n2p2`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`user_update-n2p2`{.docutils .literal .notranslate}]{.pre}
:::
::::::

:::: {#panel-20-20-1 .sphinx-tabs-panel aria-labelledby="tab-20-20-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The ML-HDNNP package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
::::::::::

------------------------------------------------------------------------
:::::::::::

::::::::::::: {#intel-package .section}
[]{#intel}

## [3.8.23. ]{.section-number}INTEL package[](#intel-package "Link to this heading"){.headerlink}

To build with this package, you must choose which hardware you want to build for, either x86 CPUs or Intel KNLs in offload mode. You should also typically [[install the OPENMP package]{.std .std-ref}](#openmp){.reference .internal}, as it can be used in tandem with the INTEL package to good effect, as explained on the [[INTEL package]{.doc}]Speed_intel.md){.reference .internal} page.

When using Intel compilers version 16.0 or later is required. You can also use the GNU or Clang compilers and they will provide performance improvements over regular styles and OPENMP styles, but less so than with the Intel compilers. Please also note, that some compilers have been found to apply memory alignment constraints incompletely or incorrectly and thus can cause segmentation faults in otherwise correct code when using features from the INTEL package.

:::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-21-21-0 .sphinx-tabs-panel aria-labelledby="tab-21-21-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D INTEL_ARCH=value     # value = cpu (default) or knl
    -D INTEL_LRT_MODE=value # value = threads, none, or c++17
:::
::::
:::::

::::::: {#panel-21-21-1 .sphinx-tabs-panel aria-labelledby="tab-21-21-1" hidden="true" role="tabpanel" tabindex="0"}
Choose which hardware to compile for in Makefile.machine via the following settings. See [`src/MAKE/OPTIONS/Makefile.intel_cpu*`{.docutils .literal .notranslate}]{.pre} and [`Makefile.knl`{.docutils .literal .notranslate}]{.pre} files for examples. and [`src/INTEL/README`{.docutils .literal .notranslate}]{.pre} for additional information.

For CPUs:

:::: {.highlight-make .notranslate}
::: highlight
    OPTFLAGS =  -xHost -O2 -fp-model fast=2 -no-prec-div -qoverride-limits -qopt-zmm-usage=high
    CCFLAGS =   -g -qopenmp -DLAMMPS_MEMALIGN=64 -no-offload -fno-alias -ansi-alias -restrict $(OPTFLAGS)
    LINKFLAGS = -g -qopenmp $(OPTFLAGS)
    LIB =       -ltbbmalloc
:::
::::

For KNLs:

:::: {.highlight-make .notranslate}
::: highlight
    OPTFLAGS =  -xMIC-AVX512 -O2 -fp-model fast=2 -no-prec-div -qoverride-limits
    CCFLAGS =   -g -qopenmp -DLAMMPS_MEMALIGN=64 -no-offload -fno-alias -ansi-alias -restrict $(OPTFLAGS)
    LINKFLAGS = -g -qopenmp $(OPTFLAGS)
    LIB =       -ltbbmalloc
:::
::::
:::::::
::::::::::::

In Long-range thread mode (LRT) a modified verlet style is used, that operates the Kspace calculation in a separate thread concurrently to other calculations. This has to be enabled in the [[package intel]{.doc}]package.md){.reference .internal} command at runtime. With the setting "threads" it used the pthreads library, while "c++17" will use the built-in thread support of C++17 compilers. The option "none" skips compilation of this feature. The default is to use "threads" if pthreads is available and otherwise "none".

Best performance is achieved with Intel hardware, Intel compilers, as well as the Intel TBB and MKL libraries. However, the code also compiles, links, and runs with other compilers / hardware and without TBB and MKL.

------------------------------------------------------------------------
:::::::::::::

:::::::::: {#mdi-package .section}
[]{#mdi}

## [3.8.24. ]{.section-number}MDI package[](#mdi-package "Link to this heading"){.headerlink}

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-22-22-0 .sphinx-tabs-panel aria-labelledby="tab-22-22-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D DOWNLOAD_MDI=value    # download MDI Library for build
                             # value = no (default) or yes
:::
::::
:::::

:::: {#panel-22-22-1 .sphinx-tabs-panel aria-labelledby="tab-22-22-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The MDI package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

::::::::::: {#misc-package .section}
[]{#misc}

## [3.8.25. ]{.section-number}MISC package[](#misc-package "Link to this heading"){.headerlink}

The [[fix imd]{.doc}]fix_imd.md){.reference .internal} style in this package can be run either synchronously (communication with IMD clients is done in the main process) or asynchronously (the fix spawns a separate thread that can communicate with IMD clients concurrently to the LAMMPS execution).

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-23-23-0 .sphinx-tabs-panel aria-labelledby="tab-23-23-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D LAMMPS_ASYNC_IMD=value  # Run IMD server asynchronously
                               # value = no (default) or yes
:::
::::
:::::

::::: {#panel-23-23-1 .sphinx-tabs-panel aria-labelledby="tab-23-23-1" hidden="true" role="tabpanel" tabindex="0"}
To enable asynchronous mode the [`-DLAMMPS_ASYNC_IMD`{.docutils .literal .notranslate}]{.pre} define needs to be added to the [`LMP_INC`{.docutils .literal .notranslate}]{.pre} variable in the [`Makefile.machine`{.docutils .literal .notranslate}]{.pre} you are using. For example:

:::: {.highlight-make .notranslate}
::: highlight
    LMP_INC = -DLAMMPS_ASYNC_IMD -DLAMMPS_MEMALIGN=64
:::
::::
:::::
::::::::::

------------------------------------------------------------------------
:::::::::::

:::::::::: {#molfile-package .section}
[]{#molfile}

## [3.8.26. ]{.section-number}MOLFILE package[](#molfile-package "Link to this heading"){.headerlink}

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-24-24-0 .sphinx-tabs-panel aria-labelledby="tab-24-24-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D MOLFILE_INCLUDE_DIR=path   # (optional) path where VMD molfile
                                  # plugin headers are installed
    -D PKG_MOLFILE=yes
:::
::::

Using [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_MOLFILE=yes`{.docutils .literal .notranslate}]{.pre} enables the package, and setting [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`MOLFILE_INCLUDE_DIR`{.docutils .literal .notranslate}]{.pre} allows to provide a custom location for the molfile plugin header files. These should match the ABI of the plugin files used, and thus one typically sets them to include folder of the local VMD installation in use. LAMMPS ships with a couple of default header files that correspond to a popular VMD version, usually the latest release.
:::::

:::: {#panel-24-24-1 .sphinx-tabs-panel aria-labelledby="tab-24-24-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The MOLFILE package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

:::::::: {#netcdf-package .section}
[]{#netcdf}

## [3.8.27. ]{.section-number}NETCDF package[](#netcdf-package "Link to this heading"){.headerlink}

To build with this package you must have the NetCDF library installed on your system.

::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::: {#panel-25-25-0 .sphinx-tabs-panel aria-labelledby="tab-25-25-0" role="tabpanel" tabindex="0"}
No additional settings are needed besides [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_NETCDF=yes`{.docutils .literal .notranslate}]{.pre}.

This should auto-detect the NETCDF library if it is installed on your system at standard locations. Several advanced CMake NETCDF options exist if you need to specify where it was installed. Use the [`ccmake`{.docutils .literal .notranslate}]{.pre} (terminal window) or [`cmake-gui`{.docutils .literal .notranslate}]{.pre} (graphical) tools to see these options and set them interactively from their user interfaces.
:::

:::: {#panel-25-25-1 .sphinx-tabs-panel aria-labelledby="tab-25-25-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The NETCDF package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::

------------------------------------------------------------------------
::::::::

:::::::::: {#openmp-package .section}
[]{#openmp}

## [3.8.28. ]{.section-number}OPENMP package[](#openmp-package "Link to this heading"){.headerlink}

:::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::: {#panel-26-26-0 .sphinx-tabs-panel aria-labelledby="tab-26-26-0" role="tabpanel" tabindex="0"}
No additional settings are required besides [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_OPENMP=yes`{.docutils .literal .notranslate}]{.pre}. If CMake detects OpenMP compiler support, the OPENMP code will be compiled with multi-threading support enabled, otherwise as optimized serial code.
:::

::::: {#panel-26-26-1 .sphinx-tabs-panel aria-labelledby="tab-26-26-1" hidden="true" role="tabpanel" tabindex="0"}
To enable multi-threading support in the OPENMP package (and other styles supporting OpenMP) the following compile and link flags must be added to your Makefile.machine file. See [`src/MAKE/OPTIONS/Makefile.omp`{.docutils .literal .notranslate}]{.pre} for an example.

:::: {.highlight-none .notranslate}
::: highlight
    CCFLAGS: -fopenmp               # for GNU and Clang Compilers
    CCFLAGS: -qopenmp -restrict     # for Intel compilers on Linux
    LINKFLAGS: -fopenmp             # for GNU and Clang Compilers
    LINKFLAGS: -qopenmp             # for Intel compilers on Linux
:::
::::

For other platforms and compilers, please consult the documentation about OpenMP support for your compiler.
:::::
::::::::

::: {.note .admonition}
Adding OpenMP support on macOS

Apple offers the [Xcode package and IDE](https://developer.apple.com/xcode/){.reference .external} for compiling software on macOS, so you have likely installed it to compile LAMMPS. Their compiler is based on [Clang](https://clang.llvm.org/){.reference .external}, but while it is capable of processing OpenMP directives, the necessary header files and OpenMP runtime library are missing. The [R developers](https://www.r-project.org/){.reference .external} have figured out a way to build those in a compatible fashion. One can download them from [https://mac.r-project.org/openmp/](https://mac.r-project.org/openmp/){.reference .external}. Simply adding those files as instructed enables the Xcode C++ compiler to compile LAMMPS with [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`BUILD_OMP=yes`{.docutils .literal .notranslate}]{.pre}.
:::

------------------------------------------------------------------------
::::::::::

:::::::::: {#qmmm-package .section}
[]{#qmmm}

## [3.8.29. ]{.section-number}QMMM package[](#qmmm-package "Link to this heading"){.headerlink}

For using LAMMPS to do QM/MM simulations via the QMMM package you need to build LAMMPS as a library. A LAMMPS executable with [[fix qmmm]{.doc}]fix_qmmm.md){.reference .internal} included can be built, but will not be able to do a QM/MM simulation on as such. You must also build a QM code - currently only Quantum ESPRESSO (QE) is supported - and create a new executable which links LAMMPS and the QM code together. Details are given in the [`lib/qmmm/README`{.docutils .literal .notranslate}]{.pre} file. It is also recommended to read the instructions for [[linking with LAMMPS as a library]{.doc}]Build_link.md){.reference .internal} for background information. This requires compatible Quantum Espresso and LAMMPS versions. The current interface and makefiles have last been verified to work in February 2020 with Quantum Espresso versions 6.3 to 6.5.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-27-27-0 .sphinx-tabs-panel aria-labelledby="tab-27-27-0" role="tabpanel" tabindex="0"}
When using CMake, building a LAMMPS library is required and it is recommended to build a shared library, since any libraries built from the sources in the *lib* folder (including the essential libqmmm.a) are not included in the static LAMMPS library and are (currently) not installed, while their code is included in the shared LAMMPS library. Thus a typical command to configure building LAMMPS for QMMM would be:

:::: {.highlight-bash .notranslate}
::: highlight
    cmake -C ../cmake/presets/basic.cmake -D PKG_QMMM=yes \
        -D BUILD_LIB=yes -DBUILD_SHARED_LIBS=yes ../cmake
:::
::::

After completing the LAMMPS build and also configuring and compiling Quantum ESPRESSO with external library support (via "make couple"), go back to the [`lib/qmmm`{.docutils .literal .notranslate}]{.pre} folder and follow the instructions on the README file to build the combined LAMMPS/QE QM/MM executable (pwqmmm.x) in the [`lib/qmmm`{.docutils .literal .notranslate}]{.pre} folder.
:::::

:::: {#panel-27-27-1 .sphinx-tabs-panel aria-labelledby="tab-27-27-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The QMMM package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

:::::::::: {#rheo-package .section}
[]{#rheo}

## [3.8.30. ]{.section-number}RHEO package[](#rheo-package "Link to this heading"){.headerlink}

This package depends on the BPM package.

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-28-28-0 .sphinx-tabs-panel aria-labelledby="tab-28-28-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D PKG_RHEO=yes               # enable the package itself
    -D PKG_BPM=yes                # the RHEO package requires BPM
    -D USE_INTERNAL_LINALG=value  # prefer internal LAPACK if true
:::
::::

Some features in the RHEO package are dependent on code in the BPM package so the latter one *must* be enabled as well.

The RHEO package also requires LAPACK (and BLAS) and CMake can identify their locations and pass that info to the RHEO build script. But on some systems this may cause problems when linking or the dependency is not desired. By using the setting [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`USE_INTERNAL_LINALG=yes`{.docutils .literal .notranslate}]{.pre} when running the CMake configuration, you will select compiling and linking the bundled linear algebra library and work around the limitations.
:::::

:::: {#panel-28-28-1 .sphinx-tabs-panel aria-labelledby="tab-28-28-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The RHEO package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

:::::::::: {#scafacos-package .section}
[]{#scafacos}

## [3.8.31. ]{.section-number}SCAFACOS package[](#scafacos-package "Link to this heading"){.headerlink}

To build with this package, you must download and build the [ScaFaCoS Coulomb solver library](http://www.scafacos.de/){.reference .external}

::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-29-29-0 .sphinx-tabs-panel aria-labelledby="tab-29-29-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    -D DOWNLOAD_SCAFACOS=value    # download ScaFaCoS for build, value = no (default) or yes
    -D SCAFACOS_LIBRARY=path      # ScaFaCos library file (only needed if at custom location)
    -D SCAFACOS_INCLUDE_DIR=path  # ScaFaCoS include directory (only needed if at custom location)
:::
::::

If [`DOWNLOAD_SCAFACOS`{.docutils .literal .notranslate}]{.pre} is set, the ScaFaCoS library will be downloaded and built inside the CMake build directory. If the ScaFaCoS library is already on your system (in a location CMake cannot find it), [`SCAFACOS_LIBRARY`{.docutils .literal .notranslate}]{.pre} is the filename (plus path) of the ScaFaCoS library file, not the directory the library file is in. [`SCAFACOS_INCLUDE_DIR`{.docutils .literal .notranslate}]{.pre} is the directory the ScaFaCoS include file is in.
:::::

:::: {#panel-29-29-1 .sphinx-tabs-panel aria-labelledby="tab-29-29-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The SCAFACOS package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::::

------------------------------------------------------------------------
::::::::::

:::::::: {#vtk-package .section}
[]{#vtk}

## [3.8.32. ]{.section-number}VTK package[](#vtk-package "Link to this heading"){.headerlink}

To build with this package you must have the VTK library installed on your system.

::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::: {#panel-30-30-0 .sphinx-tabs-panel aria-labelledby="tab-30-30-0" role="tabpanel" tabindex="0"}
No additional settings are needed besides [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_VTK=yes`{.docutils .literal .notranslate}]{.pre}.

This should auto-detect the VTK library if it is installed on your system at standard locations. Several advanced VTK options exist if you need to specify where it was installed. Use the [`ccmake`{.docutils .literal .notranslate}]{.pre} (terminal window) or [`cmake-gui`{.docutils .literal .notranslate}]{.pre} (graphical) tools to see these options and set them interactively from their user interfaces.
:::

:::: {#panel-30-30-1 .sphinx-tabs-panel aria-labelledby="tab-30-30-1" hidden="true" role="tabpanel" tabindex="0"}
::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The VTK package no longer supports the traditional make build. You need to build LAMMPS with CMake.
::::
:::::::
::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

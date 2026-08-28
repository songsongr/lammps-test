:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#lammps-portability-and-compatibility .section}
# [1.5. ]{.section-number}LAMMPS portability and compatibility[](#lammps-portability-and-compatibility "Link to this heading"){.headerlink}

The primary form of distributing LAMMPS is through highly portable source code. But also several ways of obtaining LAMMPS as [[precompiled packages or through automated build mechanisms]{.doc}]Install.md){.reference .internal} exist. Most of LAMMPS is written in C++, some support tools are written in Fortran or Python or MATLAB.

::::: {#programming-language-standards .section}
## [1.5.1. ]{.section-number}Programming language standards[](#programming-language-standards "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The C++ code in LAMMPS currently requires a compiler that is compatible with the C++17 standard. The Kokkos library used for the KOKKOS package currently also requires at least C++17. If your compilers are not compatible *and* you cannot upgrade to a compatible version, please use LAMMPS version 22 July 2025, which requires only C++11 as the minimum C++ standard.

Most of the Python code in LAMMPS is written to be compatible with Python 3.6 and later.

::: deprecated
[Deprecated since version 2Apr2025.]{.versionmodified .deprecated}
:::

Python 2.x is no longer supported and trying to use it, e.g. for the LAMMPS Python module should result in an error. If you come across some part of the LAMMPS distribution that is not (yet) compatible with Python 3, please notify [[the LAMMPS developers]{.doc}]Intro_authors.md){.reference .internal}.
:::::

:::: {#build-systems .section}
## [1.5.2. ]{.section-number}Build systems[](#build-systems "Link to this heading"){.headerlink}

LAMMPS can be compiled from source code using the cross-platform CMake system. CMake must be at least version 3.20. Alternatively, using a (traditional) build system based on shell scripts, a few shell utilities (grep, sed, cat, tr) and the GNU make program. This requires running within a Bourne shell ([`/bin/sh`{.docutils .literal .notranslate}]{.pre} or [`/bin/bash`{.docutils .literal .notranslate}]{.pre}).

::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The traditional GNU make based build system no longer supports all packages. Details can be found in the [[package specific build instructions]{.doc}]Build_extras.md){.reference .internal}.
::::

::: {#operating-systems .section}
## [1.5.3. ]{.section-number}Operating systems[](#operating-systems "Link to this heading"){.headerlink}

The primary development platform for LAMMPS is Linux. Thus, the chances for LAMMPS to compile without problems are the best on Linux machines. Also, compilation and correct execution on macOS and Windows (using Microsoft Visual C++) is checked automatically for the largest part of the source code. Some (optional) features are not compatible with all operating systems, either through limitations of the corresponding LAMMPS source code or through incompatibilities or build system limitations of required external libraries or packages.

Executables for Windows may be created either natively using Cygwin, MinGW, Intel, Clang, or Microsoft Visual C++ compilers, or with a Linux to Windows MinGW cross-compiler. Native compilation is supported using Microsoft Visual Studio or a terminal window (using the CMake build system).

Executables for macOS may be created either using Xcode or GNU compilers installed with Homebrew. In the latter case, building of LAMMPS through Homebrew instead of a manual compile is also possible.

Additionally, FreeBSD and Solaris have been tested successfully to run LAMMPS and produce results consistent with those on Linux.
:::

:::: {#compilers .section}
## [1.5.4. ]{.section-number}Compilers[](#compilers "Link to this heading"){.headerlink}

The most commonly used compilers are the GNU compilers, but also Clang and the Intel compilers have been successfully used on Linux, macOS, and Windows. Also, the Nvidia HPC SDK (formerly PGI compilers) will compile LAMMPS (tested on Linux).

::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

The GNU compilers *before* version 9.3 have known problems with supporting C++17 and thus are **not** recommended to build LAMMPS.
::::

::: {#cpu-architectures .section}
## [1.5.5. ]{.section-number}CPU architectures[](#cpu-architectures "Link to this heading"){.headerlink}

The primary CPU architecture for running LAMMPS is 64-bit x86, but also 64-bit ARM is currently regularly tested. Further architectures are tested by Linux distributions that bundle LAMMPS.
:::

::: {#portability-compliance .section}
## [1.5.6. ]{.section-number}Portability compliance[](#portability-compliance "Link to this heading"){.headerlink}

Only a subset of the LAMMPS source code is *fully* compliant to *all* of the above mentioned standards. There is also the case that the source code bundled with LAMMPS *is* compliant and portable, but an external library it depends on is not.

This is rather typical for projects like LAMMPS that largely depend on contributions from the user community. Not all contributors are trained as programmers and not all of them have access to multiple platforms for testing or are familiar with requirement of different C++ standards. As part of the continuous integration process, however, all contributions are automatically tested to compile, link, and pass *some* runtime tests on a selection of Linux flavors, macOS, and Windows, and on Linux with different compilers. Thus portability issues are often found *before* a pull request is merged or a release is made. Other platforms may be checked occasionally or when portability bugs are reported.
:::

::: {#code-review-and-static-code-analysis .section}
## [1.5.7. ]{.section-number}Code review and static code analysis[](#code-review-and-static-code-analysis "Link to this heading"){.headerlink}

In addition to using automated tests, code contributed to LAMMPS is subject to a code review by core LAMMPS developers (that includes contributions by the core LAMMPS developers themselves).

We make use of a number of static code analysis tools for maintaining and improving the quality of the LAMMPS source code. Tools used include:

- [Coverity SCAN](https://scan.coverity.com/){.reference .external}

- [CodeQL](https://codeql.github.com/){.reference .external}

- [Clang Static Analyzer](https://clang-analyzer.llvm.org/){.reference .external}

- [Clang-Tidy](https://clang.llvm.org/extra/clang-tidy/){.reference .external}

- Enabling and looking at compiler warnings

CodeQL alerts for the [`develop`{.docutils .literal .notranslate}]{.pre} branch of LAMMPS can be seen at [https://github.com/lammps/lammps/security/code-scanning](https://github.com/lammps/lammps/security/code-scanning){.reference .external}. Static code analysis reports for the [`develop`{.docutils .literal .notranslate}]{.pre} branch from the clang tools are available at [https://download.lammps.org/analysis/](https://download.lammps.org/analysis/){.reference .external}

We currently also request code reviews from [GitHub Copilot](https://github.com/features/copilot){.reference .external} to lower the code review workload for the LAMMPS developers. The LAMMPS git repository includes specific instructions for Copilot to particularly look for compliance of submitted pull requests with LAMMPS coding and documentation conventions.

A discussion of software engineering methods applied to LAMMPS over time can be found in the paper LAMMPS: A Case Study For Applying Modern Software Engineering to an Established Research Software Package, \<https://doi.org/10.5281/zenodo.17117558\> in USRSE'25 conference proceedings.
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

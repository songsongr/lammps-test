::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#install-lammps .section}
# [2. ]{.section-number}Install LAMMPS[](#install-lammps "Link to this heading"){.headerlink}

You can download LAMMPS as an executable or as source code.

When downloading the LAMMPS source code, you also have to [[build LAMMPS]{.doc}]Build.md){.reference .internal}. But you have more flexibility as to what features to include or exclude in the build. When you download and install pre-compiled LAMMPS executables, you are limited to install which version of LAMMPS is available and which features are included of these builds. If you plan to [[modify or extend LAMMPS]{.doc}]Modify.md){.reference .internal}, then you **must** build LAMMPS from the source code.

::: {.admonition .note}
Note

If you have questions about the pre-compiled LAMMPS executables, you need to contact the people preparing those executables. The LAMMPS developers have no control over their choices of how they configure and build their packages and when they update them.
:::

------------------------------------------------------------------------

::: {.toctree-wrapper .compound}
- [2.1. Download an executable for Linux]Install_linux.md){.reference .internal}
- [2.2. Download an executable for macOS]Install_mac.md){.reference .internal}
- [2.3. Download an executable for Windows]Install_windows.md){.reference .internal}
- [2.4. Download an executable for Linux or macOS via Conda]Install_conda.md){.reference .internal}
- [2.5. Download source and documentation as a tarball]Install_tarball.md){.reference .internal}
- [2.6. Download the LAMMPS source with git]Install_git.md){.reference .internal}
:::

------------------------------------------------------------------------

These are the files and subdirectories in the LAMMPS distribution:

  -------------------------------------------------------- ---------------------------------------------
  [`README`{.docutils .literal .notranslate}]{.pre}        Short description of the LAMMPS package
  [`LICENSE`{.docutils .literal .notranslate}]{.pre}       GNU General Public License (GPL)
  [`SECURITY.md`{.docutils .literal .notranslate}]{.pre}   Security policy for the LAMMPS package
  [`bench`{.docutils .literal .notranslate}]{.pre}         benchmark inputs
  [`cmake`{.docutils .literal .notranslate}]{.pre}         CMake build files
  [`doc`{.docutils .literal .notranslate}]{.pre}           documentation and tools to build the manual
  [`examples`{.docutils .literal .notranslate}]{.pre}      example input files
  [`fortran`{.docutils .literal .notranslate}]{.pre}       Fortran module for LAMMPS library interface
  [`lib`{.docutils .literal .notranslate}]{.pre}           additional provided or external libraries
  [`potentials`{.docutils .literal .notranslate}]{.pre}    selected interatomic potential files
  [`python`{.docutils .literal .notranslate}]{.pre}        Python module for LAMMPS library interface
  [`src`{.docutils .literal .notranslate}]{.pre}           LAMMPS source files
  [`tools`{.docutils .literal .notranslate}]{.pre}         pre- and post-processing tools
  [`unittest`{.docutils .literal .notranslate}]{.pre}      source code and inputs for testing LAMMPS
  -------------------------------------------------------- ---------------------------------------------

You will have all of these if you downloaded the LAMMPS source code. You will have only some of them if you downloaded executables, as explained on the pages listed above.
:::::
::::::
:::::::

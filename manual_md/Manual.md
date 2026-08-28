::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#lammps-documentation-version-version .section}
# LAMMPS Documentation (30 Mar 2026 version)[](#lammps-documentation-version-version "Link to this heading"){.headerlink}

::: {.toctree-wrapper .compound}
:::

::: {#about-lammps-and-this-manual .section}
## About LAMMPS and this manual[](#about-lammps-and-this-manual "Link to this heading"){.headerlink}

LAMMPS stands for **L**arge-scale **A**tomic/**M**olecular **M**assively **P**arallel **S**imulator.

LAMMPS is a classical molecular dynamics simulation code focusing on materials modeling. It was designed to run efficiently on parallel computers and to be easy to extend and modify. Originally developed at Sandia National Laboratories, a US Department of Energy facility, LAMMPS now includes contributions from many research groups and individuals from many institutions. Most of the funding for LAMMPS has come from the US Department of Energy (DOE). LAMMPS is open-source software distributed under the terms of the GNU Public License Version 2 (GPLv2).

The [LAMMPS website](https://www.lammps.org){.reference .external} has a variety of information about the code. It includes links to an online version of this manual, an [online forum](https://www.lammps.org/forum.html){.reference .external} where users can post questions and discuss LAMMPS, and a [GitHub site](https://github.com/lammps/lammps){.reference .external} where all LAMMPS development is coordinated.

------------------------------------------------------------------------

The content for this manual is part of the LAMMPS distribution in its doc directory.

- The version of the manual on the LAMMPS website corresponds to the latest LAMMPS feature release. It is available at: [https://docs.lammps.org/](https://docs.lammps.org/){.reference .external}.

- A version of the manual corresponding to the latest LAMMPS stable release (state of the *stable* branch on GitHub) is available online at: [https://docs.lammps.org/stable/](https://docs.lammps.org/stable/){.reference .external}

- A version of the manual with the features most recently added to LAMMPS (state of the *develop* branch on GitHub) is available at: [https://docs.lammps.org/latest/](https://docs.lammps.org/latest/){.reference .external}

If needed, you can build a copy on your local machine of the manual (HTML pages or PDF file) for the version of LAMMPS you have downloaded. Follow the steps on the [[Build the LAMMPS documentation]{.doc}]Build_manual.md){.reference .internal} page.

If you have difficulties viewing the HTML pages, please [[see this note]{.std .std-ref}](#webbrowser){.reference .internal} about compatibility with web browsers.

------------------------------------------------------------------------

The manual is organized into three parts:

1.  The [[User Guide]{.std .std-ref}](#user-documentation){.reference .internal} with information about how to obtain, configure, compile, install, and use LAMMPS,

2.  the [[Programmer Guide]{.std .std-ref}](#programmer-documentation){.reference .internal} with information about how to use the LAMMPS library interface from different programming languages, how to modify and extend LAMMPS, the program design, internal programming interfaces, and code design conventions,

3.  the [[Command Reference]{.std .std-ref}](#id1){.reference .internal} with detailed descriptions of all input script commands available in LAMMPS.

------------------------------------------------------------------------

After becoming familiar with LAMMPS, consider bookmarking [[this page]{.doc}]Commands_all.md){.reference .internal}, since it gives quick access to tables with links to the documentation for all LAMMPS commands.

------------------------------------------------------------------------
:::

:::: {#user-guide .section}
[]{#user-documentation}

## User Guide[](#user-guide "Link to this heading"){.headerlink}

::: {#userdoc .toctree-wrapper .compound}
[User Guide]{.caption-text}

- [1. Introduction]Intro.md){.reference .internal}
  - [1.1. Overview of LAMMPS]Intro_overview.md){.reference .internal}
  - [1.2. What does a LAMMPS version mean]Manual_version.md){.reference .internal}
  - [1.3. LAMMPS features]Intro_features.md){.reference .internal}
  - [1.4. LAMMPS non-features]Intro_nonfeatures.md){.reference .internal}
  - [1.5. LAMMPS portability and compatibility]Intro_portability.md){.reference .internal}
  - [1.6. LAMMPS open-source license]Intro_opensource.md){.reference .internal}
  - [1.7. Authors of LAMMPS]Intro_authors.md){.reference .internal}
  - [1.8. Citing LAMMPS]Intro_citing.md){.reference .internal}
  - [1.9. Additional website links]Intro_website.md){.reference .internal}
- [2. Install LAMMPS]Install.md){.reference .internal}
  - [2.1. Download an executable for Linux]Install_linux.md){.reference .internal}
  - [2.2. Download an executable for macOS]Install_mac.md){.reference .internal}
  - [2.3. Download an executable for Windows]Install_windows.md){.reference .internal}
  - [2.4. Download an executable for Linux or macOS via Conda]Install_conda.md){.reference .internal}
  - [2.5. Download source and documentation as a tarball]Install_tarball.md){.reference .internal}
  - [2.6. Download the LAMMPS source with git]Install_git.md){.reference .internal}
- [3. Build LAMMPS]Build.md){.reference .internal}
  - [3.1. Prerequisites]Build_prerequisites.md){.reference .internal}
  - [3.2. Build LAMMPS with CMake]Build_cmake.md){.reference .internal}
  - [3.3. Build LAMMPS with make]Build_make.md){.reference .internal}
  - [3.4. Link LAMMPS as a library to another code]Build_link.md){.reference .internal}
  - [3.5. Basic build options]Build_basics.md){.reference .internal}
  - [3.6. Optional build settings]Build_settings.md){.reference .internal}
  - [3.7. Include packages in build]Build_package.md){.reference .internal}
  - [3.8. Packages with extra build options]Build_extras.md){.reference .internal}
  - [3.9. Build the LAMMPS documentation]Build_manual.md){.reference .internal}
  - [3.10. Notes for building LAMMPS on Windows]Build_windows.md){.reference .internal}
  - [3.11. Notes for saving disk space when building LAMMPS from source]Build_diskspace.md){.reference .internal}
  - [3.12. Development build options]Build_development.md){.reference .internal}
- [4. Run LAMMPS]Run_head.md){.reference .internal}
  - [4.1. Basics of running LAMMPS]Run_basics.md){.reference .internal}
  - [4.2. Command-line options]Run_options.md){.reference .internal}
  - [4.3. Screen and logfile output]Run_output.md){.reference .internal}
  - [4.4. Error message output]Run_output.md#error-message-output){.reference .internal}
  - [4.5. File formats used by LAMMPS]Run_formats.md){.reference .internal}
  - [4.6. Running LAMMPS on Windows]Run_windows.md){.reference .internal}
- [5. Errors]Errors.md){.reference .internal}
  - [5.1. Common issues that are often regarded as bugs]Errors_common.md){.reference .internal}
  - [5.2. Errors and warnings details]Errors_details.md){.reference .internal}
  - [5.3. Reporting bugs]Errors_bugs.md){.reference .internal}
  - [5.4. Debugging crashes]Errors_debug.md){.reference .internal}
  - [5.5. Debugging when LAMMPS appears to be stuck]Errors_debug.md#debugging-when-lammps-appears-to-be-stuck){.reference .internal}
  - [5.6. Error messages]Errors_messages.md){.reference .internal}
  - [5.7. Warning messages]Errors_warnings.md){.reference .internal}
- [6. Commands]Commands.md){.reference .internal}
  - [6.1. LAMMPS input scripts]Commands_input.md){.reference .internal}
  - [6.2. Parsing rules for input scripts]Commands_parse.md){.reference .internal}
  - [6.3. Input script structure]Commands_structure.md){.reference .internal}
  - [6.4. Commands by category]Commands_category.md){.reference .internal}
  - [6.5. General commands]Commands_all.md){.reference .internal}
  - [6.6. Fix styles]Commands_fix.md){.reference .internal}
  - [6.7. Compute styles]Commands_compute.md){.reference .internal}
  - [6.8. Pair styles]Commands_pair.md){.reference .internal}
  - [6.9. Bond styles]Commands_bond.md){.reference .internal}
  - [6.10. Angle styles]Commands_bond.md#angle-styles){.reference .internal}
  - [6.11. Dihedral styles]Commands_bond.md#dihedral-styles){.reference .internal}
  - [6.12. Improper styles]Commands_bond.md#improper-styles){.reference .internal}
  - [6.13. KSpace styles]Commands_kspace.md){.reference .internal}
  - [6.14. Dump styles]Commands_dump.md){.reference .internal}
  - [6.15. Removed commands and packages]Commands_removed.md){.reference .internal}
- [7. Accelerate performance]Speed.md){.reference .internal}
  - [7.1. Benchmarks]Speed_bench.md){.reference .internal}
  - [7.2. Measuring performance]Speed_measure.md){.reference .internal}
  - [7.3. General tips]Speed_tips.md){.reference .internal}
  - [7.4. Accelerator packages]Speed_packages.md){.reference .internal}
  - [7.5. Comparison of various accelerator packages]Speed_compare.md){.reference .internal}
- [8. Optional packages]Packages.md){.reference .internal}
  - [8.1. Package details]Packages_details.md){.reference .internal}
- [9. Auxiliary tools]Tools.md){.reference .internal}
  - [9.1. Pre-processing tools]Tools.md#pre-processing-tools){.reference .internal}
  - [9.2. Post-processing tools]Tools.md#post-processing-tools){.reference .internal}
  - [9.3. Miscellaneous tools]Tools.md#miscellaneous-tools){.reference .internal}
  - [9.4. Tool descriptions]Tools.md#tool-descriptions){.reference .internal}
- [10. Howto discussions]Howto.md){.reference .internal}
  - [10.1. General howto]Howto.md#general-howto){.reference .internal}
  - [10.2. Settings howto]Howto.md#settings-howto){.reference .internal}
  - [10.3. Analysis howto]Howto.md#analysis-howto){.reference .internal}
  - [10.4. Force fields howto]Howto.md#force-fields-howto){.reference .internal}
  - [10.5. Packages howto]Howto.md#packages-howto){.reference .internal}
  - [10.6. Tutorials howto]Howto.md#tutorials-howto){.reference .internal}
- [11. Example scripts]Examples.md){.reference .internal}
  - [11.1. Lowercase directories]Examples.md#lowercase-directories){.reference .internal}
  - [11.2. Uppercase directories]Examples.md#uppercase-directories){.reference .internal}
:::
::::

:::: {#programmer-guide .section}
[]{#programmer-documentation}

## Programmer Guide[](#programmer-guide "Link to this heading"){.headerlink}

::: {#progdoc .toctree-wrapper .compound}
[Programmer Guide]{.caption-text}

- [1. LAMMPS Library Interfaces]Library.md){.reference .internal}
  - [1.1. LAMMPS C Library API]Library.md#lammps-c-library-api){.reference .internal}
  - [1.2. LAMMPS Python API]Library.md#lammps-python-api){.reference .internal}
  - [1.3. LAMMPS Fortran API]Library.md#lammps-fortran-api){.reference .internal}
  - [1.4. LAMMPS C++ API]Library.md#lammps-cplusplus-api){.reference .internal}
- [2. Use Python with LAMMPS]Python_head.md){.reference .internal}
  - [2.1. Overview]Python_overview.md){.reference .internal}
  - [2.2. Installation]Python_install.md){.reference .internal}
  - [2.3. Run LAMMPS from Python]Python_run.md){.reference .internal}
  - [2.4. The [`lammps`{.docutils .literal .notranslate}]{.pre} Python module]Python_module.md){.reference .internal}
  - [2.5. Extending the Python interface]Python_ext.md){.reference .internal}
  - [2.6. Calling Python from LAMMPS]Python_call.md){.reference .internal}
  - [2.7. Output Readers]Python_formats.md){.reference .internal}
  - [2.8. Example Python scripts]Python_examples.md){.reference .internal}
  - [2.9. Using LAMMPS in IPython notebooks and Jupyter]Python_jupyter.md){.reference .internal}
  - [2.10. Handling LAMMPS errors]Python_error.md){.reference .internal}
  - [2.11. Troubleshooting]Python_trouble.md){.reference .internal}
- [3. Modifying & extending LAMMPS]Modify.md){.reference .internal}
  - [3.1. Overview]Modify_overview.md){.reference .internal}
  - [3.2. Submitting new features for inclusion in LAMMPS]Modify_contribute.md){.reference .internal}
  - [3.3. Requirements for contributions to LAMMPS]Modify_requirements.md){.reference .internal}
  - [3.4. LAMMPS programming style]Modify_style.md){.reference .internal}
  - [3.5. Atom styles]Modify_atom.md){.reference .internal}
  - [3.6. Pair styles]Modify_pair.md){.reference .internal}
  - [3.7. Bond, angle, dihedral, improper styles]Modify_bond.md){.reference .internal}
  - [3.8. Compute styles]Modify_compute.md){.reference .internal}
  - [3.9. Fix styles]Modify_fix.md){.reference .internal}
  - [3.10. Input script command style]Modify_command.md){.reference .internal}
  - [3.11. Dump styles]Modify_dump.md){.reference .internal}
  - [3.12. Kspace styles]Modify_kspace.md){.reference .internal}
  - [3.13. Minimization styles]Modify_min.md){.reference .internal}
  - [3.14. Region styles]Modify_region.md){.reference .internal}
  - [3.15. Body styles]Modify_body.md){.reference .internal}
  - [3.16. Granular Sub-Model styles]Modify_gran_sub_mod.md){.reference .internal}
  - [3.17. Thermodynamic output options]Modify_thermo.md){.reference .internal}
  - [3.18. Variable options]Modify_variable.md){.reference .internal}
- [4. Information for Developers]Developer.md){.reference .internal}
  - [4.1. Source files]Developer_org.md){.reference .internal}
  - [4.2. Class topology]Developer_org.md#class-topology){.reference .internal}
  - [4.3. Code design]Developer_code_design.md){.reference .internal}
  - [4.4. Parallel algorithms]Developer_parallel.md){.reference .internal}
  - [4.5. Accessing per-atom data]Developer_atom.md){.reference .internal}
  - [4.6. Communication patterns]Developer_comm_ops.md){.reference .internal}
  - [4.7. How a timestep works]Developer_flow.md){.reference .internal}
  - [4.8. Writing new styles]Developer_write.md){.reference .internal}
  - [4.9. Notes for developers and code maintainers]Developer_notes.md){.reference .internal}
  - [4.10. Notes for updating code written for older LAMMPS versions]Developer_updating.md){.reference .internal}
  - [4.11. Writing plugins]Developer_plugins.md){.reference .internal}
  - [4.12. Adding tests for unit testing]Developer_unittest.md){.reference .internal}
  - [4.13. C++ base classes]Classes.md){.reference .internal}
  - [4.14. Platform abstraction functions]Developer_platform.md){.reference .internal}
  - [4.15. Utility functions]Developer_utils.md){.reference .internal}
  - [4.16. Special Math functions]Developer_utils.md#special-math-functions){.reference .internal}
  - [4.17. Tokenizer classes]Developer_utils.md#tokenizer-classes){.reference .internal}
  - [4.18. Argument parsing classes]Developer_utils.md#argument-parsing-classes){.reference .internal}
  - [4.19. Safe pointer classes]Developer_utils.md#safe-pointer-classes){.reference .internal}
  - [4.20. File reader classes]Developer_utils.md#file-reader-classes){.reference .internal}
  - [4.21. Type label support]Developer_utils.md#type-label-support){.reference .internal}
  - [4.22. Memory pool classes]Developer_utils.md#memory-pool-classes){.reference .internal}
  - [4.23. Eigensolver functions]Developer_utils.md#eigensolver-functions){.reference .internal}
  - [4.24. Communication buffer coding with *ubuf*]Developer_utils.md#communication-buffer-coding-with-ubuf){.reference .internal}
  - [4.25. Internal Styles]Developer_internal.md){.reference .internal}
  - [4.26. Use of distributed grids within style classes]Developer_grid.md){.reference .internal}
:::
::::

:::: {#command-reference .section}
## Command Reference[](#command-reference "Link to this heading"){.headerlink}

::: {#reference .toctree-wrapper .compound}
[]{#id1}

[Command Reference]{.caption-text}

- [Commands]commands_list.md){.reference .internal}
- [Fix Styles]fixes.md){.reference .internal}
- [Compute Styles]computes.md){.reference .internal}
- [Pair Styles]pairs.md){.reference .internal}
- [Bond Styles]bonds.md){.reference .internal}
- [Angle Styles]angles.md){.reference .internal}
- [Dihedral Styles]dihedrals.md){.reference .internal}
- [Improper Styles]impropers.md){.reference .internal}
- [Dump Styles]dumps.md){.reference .internal}
- [Bibliography]Bibliography.md){.reference .internal}
:::
::::

:::: {#indices-and-tables .section}
## Indices and tables[](#indices-and-tables "Link to this heading"){.headerlink}

- [[Index]{.std .std-ref}]genindex.md){.reference .internal}

- [[Search Page]{.std .std-ref}]search.md){.reference .internal}

::: {#webbrowser .note .admonition}
Web Browser Compatibility

The HTML version of the manual makes use of advanced features present in "modern" web browsers. This leads to incompatibilities with older web browsers and specific vendor browsers (e.g. Internet Explorer on Windows) where parts of the pages are not rendered as expected (e.g. the layout is broken or mathematical expressions not typeset). In that case we recommend to install/use a different/newer web browser or use the [PDF version of the manual](https://docs.lammps.org/Manual.pdf){.reference .external}.

The following web browser versions have been verified to work as expected on Linux, macOS, and Windows where available:

- Safari version 11.1 and later

- Firefox version 54 and later

- Chrome version 54 and later

- Opera version 41 and later

- Edge version 80 and later

Also Android version 7.1 and later and iOS version 11 and later have been verified to render this website as expected.
:::
::::
:::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#auxiliary-tools .section}
# [9. ]{.section-number}Auxiliary tools[](#auxiliary-tools "Link to this heading"){.headerlink}

LAMMPS is designed to be a computational kernel for performing molecular dynamics computations. Additional pre- and post-processing steps are often necessary to setup and analyze a simulation. A list of such tools can be found on the [LAMMPS webpage](https://www.lammps.org){.reference .external} at these links:

- [Pre/Post processing](https://www.lammps.org/prepost.html){.reference .external}

- [External LAMMPS packages & tools](https://www.lammps.org/external.html){.reference .external}

- [Pizza.py toolkit](https://lammps.github.io/pizza/){.reference .external}

The last link for [Pizza.py](https://lammps.github.io/pizza/){.reference .external} is a Python-based tool developed at Sandia which provides tools for doing setup, analysis, plotting, and visualization for LAMMPS simulations.

Additional tools included in the LAMMPS distribution are described on this page.

Note that many users write their own setup or analysis tools or use other existing codes and convert their output to a LAMMPS input format or vice versa. The tools listed here are included in the LAMMPS distribution as examples of auxiliary tools. Some of them are not actively supported by the LAMMPS developers, as they were contributed by LAMMPS users. If you have problems using them, we can direct you to the authors.

The source code for each of these codes is in the tools subdirectory of the LAMMPS distribution. There is a Makefile (which you may need to edit for your platform) which will build several of the tools which reside in that directory. Most of them are larger packages in their own subdirectories with their own Makefiles and/or README files.

------------------------------------------------------------------------

::: {#pre-processing-tools .section}
## [9.1. ]{.section-number}Pre-processing tools[](#pre-processing-tools "Link to this heading"){.headerlink}

  ------------------------------------------------------------------- -------------------------------------------------------------- -------------------------------------------------------------------- ----------------------------------------------------------------------- --------------------------------------------------------------- ---------------------------------------------------------------
  [[ch2lmp]{.std .std-ref}](#charmm){.reference .internal}            [[chain]{.std .std-ref}](#chain){.reference .internal}         [[createatoms]{.std .std-ref}](#createatoms){.reference .internal}   [[drude]{.std .std-ref}](#drude){.reference .internal}                  [[eam database]{.std .std-ref}](#eamdb){.reference .internal}   [[eam generate]{.std .std-ref}](#eamgn){.reference .internal}
  [[eff]{.std .std-ref}](#eff){.reference .internal}                  [[ipp]{.std .std-ref}](#ipp){.reference .internal}             [[micelle2d]{.std .std-ref}](#micelle){.reference .internal}         [[moltemplate]{.std .std-ref}](#moltemplate){.reference .internal}      [[msi2lmp]{.std .std-ref}](#msi){.reference .internal}          [[polybond]{.std .std-ref}](#polybond){.reference .internal}
  [[stl_bin2txt]{.std .std-ref}](#stlconvert){.reference .internal}   [[tabulate]{.std .std-ref}](#tabulate){.reference .internal}   [[tinker]{.std .std-ref}](#tinker){.reference .internal}             [[AMBER2LAMMPS]{.doc}]Howto_amber2lammps.md){.reference .internal}                                                                   
  ------------------------------------------------------------------- -------------------------------------------------------------- -------------------------------------------------------------------- ----------------------------------------------------------------------- --------------------------------------------------------------- ---------------------------------------------------------------
:::

::: {#post-processing-tools .section}
## [9.2. ]{.section-number}Post-processing tools[](#post-processing-tools "Link to this heading"){.headerlink}

  -------------------------------------------------------------- ---------------------------------------------------------- ------------------------------------------------------------------ ---------------------------------------------------------------- --------------------------------------------------------------- ------------------------------------------------------------
  [[binary2txt]{.std .std-ref}](#binary){.reference .internal}   [[ch2lmp]{.std .std-ref}](#charmm){.reference .internal}   [[colvars]{.std .std-ref}](#colvars-tools){.reference .internal}   [[eff]{.std .std-ref}](#eff){.reference .internal}               [[fep]{.std .std-ref}](#fep){.reference .internal}              [[lmp2arc]{.std .std-ref}](#arc){.reference .internal}
  [[lmp2cfg]{.std .std-ref}](#cfg){.reference .internal}         [[matlab]{.std .std-ref}](#matlab){.reference .internal}   [[phonon]{.std .std-ref}](#phonon){.reference .internal}           [[pymol_asphere]{.std .std-ref}](#pymol){.reference .internal}   [[python]{.std .std-ref}](#pythontools){.reference .internal}   [[replica]{.std .std-ref}](#replica){.reference .internal}
  [[smd]{.std .std-ref}](#smd){.reference .internal}             [[spin]{.std .std-ref}](#spin){.reference .internal}       [[xmgrace]{.std .std-ref}](#xmgrace){.reference .internal}                                                                                                                                          
  -------------------------------------------------------------- ---------------------------------------------------------- ------------------------------------------------------------------ ---------------------------------------------------------------- --------------------------------------------------------------- ------------------------------------------------------------
:::

::: {#miscellaneous-tools .section}
## [9.3. ]{.section-number}Miscellaneous tools[](#miscellaneous-tools "Link to this heading"){.headerlink}

  ------------------------------------------------------------------------------------ ----------------------------------------------------------------------- ------------------------------------------------------------------------- ----------------------------------------------------------------------------------- ---------------------------------------------------------------- ------------------------------------------------------------------
  [[LAMMPS coding standards]{.std .std-ref}](#coding-standard){.reference .internal}   [[emacs]{.std .std-ref}](#emacs){.reference .internal}                  [[i-PI]{.std .std-ref}](#ipi){.reference .internal}                       [[JSON support]{.std .std-ref}](#json){.reference .internal}                        [[kate]{.std .std-ref}](#kate){.reference .internal}             [[LAMMPS-GUI]{.std .std-ref}](#lammps-gui){.reference .internal}
  [[LAMMPS magic patterns for file(1)]{.std .std-ref}](#magic){.reference .internal}   [[Offline build tool]{.std .std-ref}](#offline){.reference .internal}   [[Regression tester]{.std .std-ref}](#regression){.reference .internal}   [[singularity/apptainer]{.std .std-ref}](#singularity-tool){.reference .internal}   [[SWIG interface]{.std .std-ref}](#swig){.reference .internal}   [[valgrind]{.std .std-ref}](#valgrind){.reference .internal}
  [[vim]{.std .std-ref}](#vim){.reference .internal}                                                                                                                                                                                                                                                                                                                                          
  ------------------------------------------------------------------------------------ ----------------------------------------------------------------------- ------------------------------------------------------------------------- ----------------------------------------------------------------------------------- ---------------------------------------------------------------- ------------------------------------------------------------------
:::

------------------------------------------------------------------------

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#tool-descriptions .section}
## [9.4. ]{.section-number}Tool descriptions[](#tool-descriptions "Link to this heading"){.headerlink}

::::: {#binary2txt-tool .section}
[]{#binary}

### [9.4.1. ]{.section-number}binary2txt tool[](#binary2txt-tool "Link to this heading"){.headerlink}

The file binary2txt.cpp converts one or more binary LAMMPS dump file into ASCII text files. The syntax for running the tool is

:::: {.highlight-bash .notranslate}
::: highlight
    binary2txt file1 file2 ...
:::
::::

which creates file1.txt, file2.txt, etc. This tool must be compiled on a platform that can read the binary file created by a LAMMPS run, since binary files are not compatible across all platforms.

------------------------------------------------------------------------
:::::

::: {#ch2lmp-tool .section}
[]{#charmm}

### [9.4.2. ]{.section-number}ch2lmp tool[](#ch2lmp-tool "Link to this heading"){.headerlink}

The ch2lmp subdirectory contains tools for converting files back-and-forth between the CHARMM MD code and LAMMPS.

They are intended to make it easy to use CHARMM as a builder and as a post-processor for LAMMPS. Using charmm2lammps.pl, you can convert a PDB file with associated CHARMM info, including CHARMM force field data, into its LAMMPS equivalent. Support for the CMAP correction of CHARMM22 and later is available as an option. This tool can also add solvent water molecules and Na+ or Cl- ions to the system. Using lammps2pdb.pl you can convert LAMMPS atom dumps into PDB files.

See the README file in the ch2lmp subdirectory for more information.

These tools were created by Pieter in't Veld (pjintve at sandia.gov) and Paul Crozier (pscrozi at sandia.gov) at Sandia.

CMAP support added and tested by Xiaohu Hu (hux2 at ornl.gov) and Robert A. Latour (latourr at clemson.edu), David Hyde-Volpe, and Tigran Abramyan, (Clemson University) and Chris Lorenz (chris.lorenz at kcl.ac.uk), King's College London.

------------------------------------------------------------------------
:::

::::: {#chain-tool .section}
[]{#chain}

### [9.4.3. ]{.section-number}chain tool[](#chain-tool "Link to this heading"){.headerlink}

The file chain.f90 creates a LAMMPS data file containing bead-spring polymer chains and/or monomer solvent atoms. It uses a text file containing chain definition parameters as an input. The created chains and solvent atoms can strongly overlap, so LAMMPS needs to run the system initially with a "soft" pair potential to un-overlap it. The syntax for running the tool is

:::: {.highlight-bash .notranslate}
::: highlight
    chain < def.chain > data.file
:::
::::

See the def.chain or def.chain.ab files in the tools directory for examples of definition files. This tool was used to create the system for the [[chain benchmark]{.doc}]Speed_bench.md){.reference .internal}.

------------------------------------------------------------------------
:::::

::::: {#lammps-coding-standard .section}
[]{#coding-standard}

### [9.4.4. ]{.section-number}LAMMPS coding standard[](#lammps-coding-standard "Link to this heading"){.headerlink}

The [`coding_standard`{.docutils .literal .notranslate}]{.pre} folder contains multiple python scripts to check for and apply some LAMMPS coding conventions. The following scripts are available:

:::: {.highlight-none .notranslate}
::: highlight
    permissions.py   # detects if sources have executable permissions and scripts have not
    whitespace.py    # detects TAB characters and trailing whitespace
    homepage.py      # detects outdated LAMMPS homepage URLs (pointing to sandia.gov instead of lammps.org)
    errordocs.py     # detects deprecated error docs in header files
    versiontags.py   # detects .. versionadded:: or .. versionchanged:: with pending version date
:::
::::

The tools need to be given the main folder of the LAMMPS distribution or individual file names as argument and will by default check them and report any non-compliance. With the optional [`-f`{.docutils .literal .notranslate}]{.pre} argument the corresponding script will try to change the non-compliant file(s) to match the conventions.

For convenience this scripts can also be invoked by the make file in the [`src`{.docutils .literal .notranslate}]{.pre} folder with, make check-whitespace or make fix-whitespace to either detect or edit the files. Correspondingly for the other python scripts. make check will run all checks.

------------------------------------------------------------------------
:::::

::: {#colvars-tools .section}
[]{#id1}

### [9.4.5. ]{.section-number}colvars tools[](#colvars-tools "Link to this heading"){.headerlink}

The colvars directory contains a collection of tools for post-processing data produced by the colvars collective variable library. To compile the tools, edit the makefile for your system and run "make".

Please report problems and issues the colvars library and its tools at: [https://github.com/colvars/colvars/issues](https://github.com/colvars/colvars/issues){.reference .external}

abf_integrate:

MC-based integration of multidimensional free energy gradient Version 20110511

``` literal-block
./abf_integrate < filename > [-n < nsteps >] [-t < temp >] [-m [0|1] (metadynamics)] [-h < hill_height >] [-f < variable_hill_factor >]
```

The LAMMPS interface to the colvars collective variable library, as well as these tools, were created by Axel Kohlmeyer (akohlmey at gmail.com) while at ICTP, Italy.

------------------------------------------------------------------------
:::

::: {#createatoms-tool .section}
[]{#createatoms}

### [9.4.6. ]{.section-number}createatoms tool[](#createatoms-tool "Link to this heading"){.headerlink}

The tools/createatoms directory contains a Fortran program called createAtoms.f which can generate a variety of interesting crystal structures and geometries and output the resulting list of atom coordinates in LAMMPS or other formats.

See the included Manual.pdf for details.

The tool is authored by Xiaowang Zhou (Sandia), xzhou at sandia.gov.

------------------------------------------------------------------------
:::

::: {#drude-tool .section}
[]{#drude}

### [9.4.7. ]{.section-number}drude tool[](#drude-tool "Link to this heading"){.headerlink}

The tools/drude directory contains a Python script called polarizer.py which can add Drude oscillators to a LAMMPS data file in the required format.

See the header of the polarizer.py file for details.

The tool is authored by Agilio Padua and Alain Dequidt: agilio.padua at ens-lyon.fr, alain.dequidt at uca.fr

------------------------------------------------------------------------
:::

:::: {#eam-database-tool .section}
[]{#eamdb}

### [9.4.8. ]{.section-number}eam database tool[](#eam-database-tool "Link to this heading"){.headerlink}

The tools/eam_database directory contains a Fortran and a Python program that will generate EAM alloy setfl potential files for any combination of the 17 elements: Cu, Ag, Au, Ni, Pd, Pt, Al, Pb, Fe, Mo, Ta, W, Mg, Co, Ti, Zr, Cr. The files can then be used with the [[pair_style eam/alloy]{.doc}]pair_eam.md){.reference .internal} command.

The Fortran version of the tool was authored by Xiaowang Zhou (Sandia), xzhou at sandia.gov, with updates from Lucas Hale (NIST) lucas.hale at nist.gov and is based on his paper:

X. W. Zhou, R. A. Johnson, and H. N. G. Wadley, Phys. Rev. B, 69, 144113 (2004).

The parameters for Cr were taken from:

Lin Z B, Johnson R A and Zhigilei L V, Phys. Rev. B 77 214108 (2008).

The Python version of the tool was authored by Germain Clavier (Unicaen) germain.clavier at unicaen.fr

::: {.admonition .note}
Note

The parameters in the database are only optimized for individual elements. The mixed parameters for interactions between different elements generated by this tool are derived from simple mixing rules and are thus inferior to parameterizations that are specifically optimized for specific mixtures and combinations of elements.
:::

------------------------------------------------------------------------
::::

::: {#eam-generate-tool .section}
[]{#eamgn}

### [9.4.9. ]{.section-number}eam generate tool[](#eam-generate-tool "Link to this heading"){.headerlink}

The tools/eam_generate directory contains several one-file C programs that convert an analytic formula into a tabulated [[embedded atom method (EAM)]{.doc}]pair_eam.md){.reference .internal} setfl potential file. The potentials they produce are in the potentials directory, and can be used with the [[pair_style eam/alloy]{.doc}]pair_eam.md){.reference .internal} command.

The source files and potentials were provided by Gerolf Ziegenhain (gerolf at ziegenhain.com).

------------------------------------------------------------------------
:::

::: {#eff-tool .section}
[]{#eff}

### [9.4.10. ]{.section-number}eff tool[](#eff-tool "Link to this heading"){.headerlink}

The tools/eff directory contains various scripts for generating structures and post-processing output for simulations using the electron force field (eFF).

These tools were provided by Andres Jaramillo-Botero at CalTech (ajaramil at wag.caltech.edu).

------------------------------------------------------------------------
:::

::: {#emacs-tool .section}
[]{#emacs}

### [9.4.11. ]{.section-number}emacs tool[](#emacs-tool "Link to this heading"){.headerlink}

The tools/emacs directory contains an Emacs Lisp add-on file for GNU Emacs that enables a lammps-mode for editing input scripts when using GNU Emacs, with various highlighting options set up.

These tools were provided by Aidan Thompson at Sandia (athomps at sandia.gov).

------------------------------------------------------------------------
:::

::: {#fep-tool .section}
[]{#fep}

### [9.4.12. ]{.section-number}fep tool[](#fep-tool "Link to this heading"){.headerlink}

The tools/fep directory contains Python scripts useful for post-processing results from performing free-energy perturbation simulations using the FEP package.

The scripts were contributed by Agilio Padua (ENS de Lyon), agilio.padua at ens-lyon.fr.

See README file in the tools/fep directory.

------------------------------------------------------------------------
:::

:::::::: {#i-pi-tool .section}
[]{#ipi}

### [9.4.13. ]{.section-number}i-PI tool[](#i-pi-tool "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 27June2024.]{.versionmodified .changed}
:::

The tools/i-pi directory used to contain a bundled version of the i-PI software package for use with LAMMPS. This version, however, was removed in 06/2024.

The i-PI package was created and is maintained by Michele Ceriotti, michele.ceriotti at gmail.com, to interface to a variety of molecular dynamics codes.

i-PI is now available via PyPI using the pip package manager at: [https://pypi.org/project/ipi/](https://pypi.org/project/ipi/){.reference .external}

Here are the commands to set up a virtual environment and install i-PI into it with all its dependencies.

:::: {.highlight-sh .notranslate}
::: highlight
    python -m venv ipienv
    source ipienv/bin/activate
    pip install --upgrade pip
    pip install ipi
:::
::::

To install the development version from GitHub, please use:

:::: {.highlight-sh .notranslate}
::: highlight
    pip install git+https://github.com/i-pi/i-pi.git
:::
::::

For further information, please consult the \[i-PI home page\]([https://ipi-code.org](https://ipi-code.org){.reference .external}).

------------------------------------------------------------------------
::::::::

::: {#ipp-tool .section}
[]{#ipp}

### [9.4.14. ]{.section-number}ipp tool[](#ipp-tool "Link to this heading"){.headerlink}

The tools/ipp directory contains a Perl script ipp which can be used to facilitate the creation of a complicated file (say, a LAMMPS input script or tools/createatoms input file) using a template file.

ipp was created and is maintained by Reese Jones (Sandia), rjones at sandia.gov.

See two examples in the tools/ipp directory. One of them is for the tools/createatoms tool's input file.

------------------------------------------------------------------------
:::

:::::::::::::::: {#json-support-files .section}
[]{#json}

### [9.4.15. ]{.section-number}JSON support files[](#json-support-files "Link to this heading"){.headerlink}

::: versionadded
[Added in version 12June2025.]{.versionmodified .added}
:::

The [`tools/json`{.docutils .literal .notranslate}]{.pre} directory contains files and tools to support using [JSON format](https://www.json.org/){.reference .external} files in LAMMPS. Currently only the [[molecule command]{.doc}]molecule.md){.reference .internal} supports files in JSON format directly, but this is planned to be expanded in the future.

::::::::: {#json-file-validation .section}
#### JSON file validation[](#json-file-validation "Link to this heading"){.headerlink}

The JSON syntax is independent of its content, and thus the data in the file must follow suitable conventions to be correctly parsed during input. This can be done in a portable fashion using a [JSON schema file](https://json-schema.org/){.reference .external} (which is in JSON format as well) to define those conventions. A suitable JSON validator software can then validate JSON files against the requirements. Validating a particular JSON file against a schema ensures that both, the syntax *and* the conventions are followed. This is useful when writing or editing JSON files in a text editor or when writing a pre-processing script or tool to create JSON files for a specific purpose in LAMMPS. It **cannot** check whether the file contents are physically meaningful, though.

One such validator tool is [check-jsonschema](https://check-jsonschema.readthedocs.io/){.reference .external} which is written in Python and can be installed using the [pip Python package manager](https://pypi.org/){.reference .external}, best in a virtual environment as shown below (for a Bourne Shell command line):

:::: {.highlight-sh .notranslate}
::: highlight
    python -m venv validate-json
    source validate-json/bin/activate
    pip install --upgrade pip
    pip install check-jsonschema
:::
::::

To validate a specific JSON file against a provided schema (here for a [[molecule command file]{.doc}]molecule.md){.reference .internal} you would then run for example:

:::: {.highlight-sh .notranslate}
::: highlight
    check-jsonschema --schemafile molecule-schema.json tip3p.json
:::
::::

The latest schema files are also maintained and available for download at [https://download.lammps.org/json/](https://download.lammps.org/json/){.reference .external} . This enables validation of JSON files even if the LAMMPS sources are not locally available. Example:

:::: {.highlight-sh .notranslate}
::: highlight
    check-jsonschema --schemafile https://download.lammps.org/json/molecule-schema.json tip3p.json
:::
::::
:::::::::

::::::: {#json-file-format-normalization .section}
#### JSON file format normalization[](#json-file-format-normalization "Link to this heading"){.headerlink}

There are extensions to the strict JSON format that allow for comments or ignore additional (dangling) commas. The [`reformat-json.cpp`{.docutils .literal .notranslate}]{.pre} tool will read JSON files in relaxed format, but write it out in strict format. It is also possible to change the level of indentation from -1 (all data one long line) to any positive integer value. The original file will be backed up (.bak added to file name) and then overwritten.

Manual compilation (it will be automatically included in the CMake build if building tools is requested during CMake configuration):

:::: {.highlight-sh .notranslate}
::: highlight
    g++ -I <path/to/lammps/src> -o reformat-json reformat-json.cpp
:::
::::

Usage:

:::: {.highlight-none .notranslate}
::: highlight
    reformat-json <indent-width> <json-file-1> [<json-file-2> ...]
:::
::::

------------------------------------------------------------------------
:::::::
::::::::::::::::

::: {#kate-tool .section}
[]{#kate}

### [9.4.16. ]{.section-number}kate tool[](#kate-tool "Link to this heading"){.headerlink}

The file in the tools/kate directory is an add-on to the Kate editor in the KDE suite that allow syntax highlighting of LAMMPS input scripts. See the README.txt file for details.

The file was provided by Alessandro Luigi Sellerio (alessandro.sellerio at ieni.cnr.it).

------------------------------------------------------------------------
:::

:::: {#lammps-gui .section}
[]{#id2}

### [9.4.17. ]{.section-number}LAMMPS-GUI[](#lammps-gui "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 10Sep2025.]{.versionmodified .changed}
:::

LAMMPS-GUI is a graphical text editor customized for editing LAMMPS input files that is linked to the [[LAMMPS C-library]{.std .std-ref}]Library.md#lammps-c-api){.reference .internal}. It used to be included with LAMMPS in the [`tools/lammps-gui`{.docutils .literal .notranslate}]{.pre} folder, but it is now hosted in its own git repository at [https://github.com/akohlmey/lammps-gui/](https://github.com/akohlmey/lammps-gui/){.reference .external} and the online documentation is at [https://lammps-gui.lammps.org/](https://lammps-gui.lammps.org/){.reference .external}

It is still possible to compile [[LAMMPS-GUI together with LAMMPS]{.std .std-ref}]Build_basics.md#tools){.reference .internal}.

------------------------------------------------------------------------
::::

::: {#lmp2arc-tool .section}
[]{#arc}

### [9.4.18. ]{.section-number}lmp2arc tool[](#lmp2arc-tool "Link to this heading"){.headerlink}

The lmp2arc subdirectory contains a tool for converting LAMMPS output files to the format for Accelrys' Insight MD code (formerly MSI/Biosym and its Discover MD code). See the README file for more information.

This tool was written by John Carpenter (Cray), Michael Peachey (Cray), and Steve Lustig (Dupont). John is now at the Mayo Clinic (jec at mayo.edu), but still fields questions about the tool.

This tool was updated for the current LAMMPS C++ version by Jeff Greathouse at Sandia (jagreat at sandia.gov).

------------------------------------------------------------------------
:::

::: {#lmp2cfg-tool .section}
[]{#cfg}

### [9.4.19. ]{.section-number}lmp2cfg tool[](#lmp2cfg-tool "Link to this heading"){.headerlink}

The lmp2cfg subdirectory contains a tool for converting LAMMPS output files into a series of \*.cfg files which can be read into the [AtomEye](http://li.mit.edu/Archive/Graphics/A/){.reference .external} visualizer. See the README file for more information.

This tool was written by Ara Kooser at Sandia (askoose at sandia.gov).

------------------------------------------------------------------------
:::

:::::: {#magic-patterns-for-the-file-command .section}
[]{#magic}

### [9.4.20. ]{.section-number}Magic patterns for the "file" command[](#magic-patterns-for-the-file-command "Link to this heading"){.headerlink}

::: versionadded
[Added in version 10Mar2021.]{.versionmodified .added}
:::

The file [`magic`{.docutils .literal .notranslate}]{.pre} contains patterns that are used by the [file program](https://en.wikipedia.org/wiki/File_(command)){.reference .external} available on most Unix-like operating systems which enables it to detect various LAMMPS files and print some useful information about them. To enable these patterns, append or copy the contents of the file to either the file [`.magic`{.docutils .literal .notranslate}]{.pre} in your home directory or (as administrator) to [`/etc/magic`{.docutils .literal .notranslate}]{.pre} (for a system-wide installation). Afterwards the [`file`{.docutils .literal .notranslate}]{.pre} command should be able to detect most LAMMPS restarts, dump, data and log files. Examples:

:::: {.highlight-console .notranslate}
::: highlight
    $ file *.*
    dihedral-quadratic.restart:   LAMMPS binary restart file (rev 2), Version 10 Mar 2021, Little Endian
    mol-pair-wf_cut.restart:      LAMMPS binary restart file (rev 2), Version 24 Dec 2020, Little Endian
    atom.bin:                     LAMMPS atom style binary dump (rev 2), Little Endian, First time step: 445570
    custom.bin:                   LAMMPS custom style binary dump (rev 2), Little Endian, First time step: 100
    bn1.lammpstrj:                LAMMPS text mode dump, First time step: 5000
    data.fourmol:                 LAMMPS data file written by LAMMPS
    pnc.data:                     LAMMPS data file written by msi2lmp
    data.spce:                    LAMMPS data file written by TopoTools
    B.data:                       LAMMPS data file written by OVITO
    log.lammps:                   LAMMPS log file written by version 10 Feb 2021
:::
::::

------------------------------------------------------------------------
::::::

::: {#matlab-tool .section}
[]{#matlab}

### [9.4.21. ]{.section-number}matlab tool[](#matlab-tool "Link to this heading"){.headerlink}

The matlab subdirectory contains several [MATLAB](https://www.mathworks.com){.reference .external} scripts for post-processing LAMMPS output. The scripts include readers for log and dump files, a reader for EAM potential files, and a converter that reads LAMMPS dump files and produces CFG files that can be visualized with the [AtomEye](http://li.mit.edu/Archive/Graphics/A/){.reference .external} visualizer.

See the README.pdf file for more information.

These scripts were written by Arun Subramaniyan at Purdue Univ (asubrama at purdue.edu).

------------------------------------------------------------------------
:::

::::: {#micelle2d-tool .section}
[]{#micelle}

### [9.4.22. ]{.section-number}micelle2d tool[](#micelle2d-tool "Link to this heading"){.headerlink}

The file micelle2d.f creates a LAMMPS data file containing short lipid chains in a monomer solution. It uses a text file containing lipid definition parameters as an input. The created molecules and solvent atoms can strongly overlap, so LAMMPS needs to run the system initially with a "soft" pair potential to un-overlap it. The syntax for running the tool is

:::: {.highlight-bash .notranslate}
::: highlight
    micelle2d < def.micelle2d > data.file
:::
::::

See the def.micelle2d file in the tools directory for an example of a definition file. This tool was used to create the system for the [[micelle example]{.doc}]Examples.md){.reference .internal}.

------------------------------------------------------------------------
:::::

::: {#moltemplate-tool .section}
[]{#moltemplate}

### [9.4.23. ]{.section-number}moltemplate tool[](#moltemplate-tool "Link to this heading"){.headerlink}

The moltemplate subdirectory contains instructions for installing moltemplate, a Python-based tool for building molecular systems based on a text-file description, and creating LAMMPS data files that encode their molecular topology as lists of bonds, angles, dihedrals, etc. See the README.txt file for more information.

This tool was written by Andrew Jewett (jewett.aij at gmail.com), who supports it. It has its own WWW page at [https://moltemplate.org](https://moltemplate.org){.reference .external}. The latest sources can be found [on its GitHub page](https://github.com/jewettaij/moltemplate/releases){.reference .external}

------------------------------------------------------------------------
:::

::: {#msi2lmp-tool .section}
[]{#msi}

### [9.4.24. ]{.section-number}msi2lmp tool[](#msi2lmp-tool "Link to this heading"){.headerlink}

The msi2lmp subdirectory contains a tool for creating LAMMPS template input and data files from BIOVIA's Materias Studio files (formerly Accelrys' Insight MD code, formerly MSI/Biosym and its Discover MD code).

This tool was written by John Carpenter (Cray), Michael Peachey (Cray), and Steve Lustig (Dupont). Several people contributed changes to remove bugs and adapt its output to changes in LAMMPS.

This tool has several known limitations and is no longer under active development, so there are no changes except for the occasional bug fix.

See the README file in the tools/msi2lmp folder for more information.

------------------------------------------------------------------------
:::

:::::::::::: {#scripts-for-building-lammps-when-offline .section}
[]{#offline}

### [9.4.25. ]{.section-number}Scripts for building LAMMPS when offline[](#scripts-for-building-lammps-when-offline "Link to this heading"){.headerlink}

In some situations it might be necessary to build LAMMPS on a system without direct internet access. The scripts in [`tools/offline`{.docutils .literal .notranslate}]{.pre} folder allow you to pre-load external dependencies for both the documentation build and for building LAMMPS with CMake.

It does so by

> ::: {}
> 1.  downloading necessary [`pip`{.docutils .literal .notranslate}]{.pre} packages,
>
> 2.  cloning [`git`{.docutils .literal .notranslate}]{.pre} repositories
>
> 3.  downloading tarballs
> :::

to a designated cache folder.

As of April 2021, all of these downloads make up around 600MB. By default, the offline scripts will download everything into the [`$HOME/.cache/lammps`{.docutils .literal .notranslate}]{.pre} folder, but this can be changed by setting the [`LAMMPS_CACHING_DIR`{.docutils .literal .notranslate}]{.pre} environment variable.

Once the caches have been initialized, they can be used for building the LAMMPS documentation or compiling LAMMPS using CMake on an offline system.

The [`use_caches.sh`{.docutils .literal .notranslate}]{.pre} script must be sourced into the current shell to initialize the offline build environment. Note that it must use the same [`LAMMPS_CACHING_DIR`{.docutils .literal .notranslate}]{.pre}. This script does the following:

> ::: {}
> 1.  Set up environment variables that modify the behavior of both, [`pip`{.docutils .literal .notranslate}]{.pre} and [`git`{.docutils .literal .notranslate}]{.pre}
>
> 2.  Start a simple local HTTP server using Python to host files for CMake
> :::

Afterwards, it will print out instructions on how to modify the CMake commands to make sure it uses the local HTTP server.

To undo the environment changes and shutdown the local HTTP server, run the [`deactivate_caches`{.docutils .literal .notranslate}]{.pre} command.

::::: {#examples .section}
#### Examples[](#examples "Link to this heading"){.headerlink}

For all of the examples below, you first need to create the cache, which requires an internet connection.

:::: {.highlight-bash .notranslate}
::: highlight
    ./tools/offline/init_caches.sh
:::
::::

Afterwards, you can disconnect or copy the contents of the [`LAMMPS_CACHING_DIR`{.docutils .literal .notranslate}]{.pre} folder to an offline system.
:::::

::::: {#documentation-build .section}
#### Documentation Build[](#documentation-build "Link to this heading"){.headerlink}

The documentation build will create a new virtual environment that typically first installs dependencies from [`pip`{.docutils .literal .notranslate}]{.pre}. With the offline environment loaded, these installations will instead grab the necessary packages from your local cache.

:::: {.highlight-bash .notranslate}
::: highlight
    # if LAMMPS_CACHING_DIR is different from default, make sure to set it first
    # export LAMMPS_CACHING_DIR=path/to/folder
    source tools/offline/use_caches.sh
    cd doc/
    make html

    deactivate_caches
:::
::::
:::::

::::: {#cmake-build .section}
#### CMake Build[](#cmake-build "Link to this heading"){.headerlink}

When compiling certain packages with external dependencies, the CMake build system will download necessary files or sources from the web. For more flexibility the CMake configuration allows users to specify the URL of each of these dependencies. What the [`init_caches.sh`{.docutils .literal .notranslate}]{.pre} script does is create a CMake "preset" file, which sets the URLs for all of the known dependencies and redirects the download to the local cache.

:::: {.highlight-bash .notranslate}
::: highlight
    # if LAMMPS_CACHING_DIR is different from default, make sure to set it first
    # export LAMMPS_CACHING_DIR=path/to/folder
    source tools/offline/use_caches.sh

    mkdir build
    cd build
    cmake -D LAMMPS_DOWNLOADS_URL=${HTTP_CACHE_URL} -C "${LAMMPS_HTTP_CACHE_CONFIG}" -C ../cmake/presets/most.cmake -D DOWNLOAD_POTENTIALS=off ../cmake
    make -j 8

    deactivate_caches
:::
::::

------------------------------------------------------------------------
:::::
::::::::::::

::: {#phonon-tool .section}
[]{#phonon}

### [9.4.26. ]{.section-number}phonon tool[](#phonon-tool "Link to this heading"){.headerlink}

The phonon subdirectory contains a post-processing tool, *phana*, useful for analyzing the output of the [[fix phonon]{.doc}]fix_phonon.md){.reference .internal} command in the PHONON package.

See the README file for instructions on building the tool and what library it needs. And see the examples/PACKAGES/phonon directory for example problems that can be post-processed with this tool.

This tool was written by Ling-Ti Kong at Shanghai Jiao Tong University.

------------------------------------------------------------------------
:::

::: {#polybond-tool .section}
[]{#polybond}

### [9.4.27. ]{.section-number}polybond tool[](#polybond-tool "Link to this heading"){.headerlink}

The polybond subdirectory contains a Python-based tool useful for performing "programmable polymer bonding". The Python file lmpsdata.py provides a "Lmpsdata" class with various methods which can be invoked by a user-written Python script to create data files with complex bonding topologies.

See the Manual.pdf for details and example scripts.

This tool was written by Zachary Kraus at Georgia Tech.

------------------------------------------------------------------------
:::

::: {#pymol-asphere-tool .section}
[]{#pymol}

### [9.4.28. ]{.section-number}pymol_asphere tool[](#pymol-asphere-tool "Link to this heading"){.headerlink}

The pymol_asphere subdirectory contains a tool for converting a LAMMPS dump file that contains orientation info for ellipsoidal particles into an input file for the [PyMol visualization package](https://www.pymol.org){.reference .external} or its [open source variant](https://github.com/schrodinger/pymol-open-source){.reference .external}.

Specifically, the tool triangulates the ellipsoids so they can be viewed as true ellipsoidal particles within PyMol. See the README and examples directory within pymol_asphere for more information.

This tool was written by Mike Brown at Sandia.

------------------------------------------------------------------------
:::

::: {#python-tool .section}
[]{#pythontools}

### [9.4.29. ]{.section-number}python tool[](#python-tool "Link to this heading"){.headerlink}

The python subdirectory contains several Python scripts that perform common LAMMPS post-processing tasks, such as:

- extract thermodynamic info from a log file as columns of numbers

- plot two columns of thermodynamic info from a log file using GnuPlot

- sort the snapshots in a dump file by atom ID

- convert multiple [[NEB]{.doc}]neb.md){.reference .internal} dump files into one dump file for viz

- convert dump files into XYZ, CFG, or PDB format for viz by other packages

These are simple scripts built on [Pizza.py](https://lammps.github.io/pizza/){.reference .external} modules. See the README for more info on Pizza.py and how to use these scripts.

------------------------------------------------------------------------
:::

::: {#regression-tester-tool .section}
[]{#regression}

### [9.4.30. ]{.section-number}Regression tester tool[](#regression-tester-tool "Link to this heading"){.headerlink}

The regression-tests subdirectory contains a tool for performing regression tests with a given LAMMPS binary. The tool launches the LAMMPS binary with any given input script under one of the examples subdirectories, and compares the thermo output in the generated log file with those in the provided log file with the same number of processors in the same subdirectory. If the differences between the actual and reference values are within specified tolerances, the test is considered passed. For each test batch, that is, a set of example input scripts, the [`mpirun`{.docutils .literal .notranslate}]{.pre} command, the LAMMPS command-line arguments, and the tolerances for individual thermo quantities can be specified in a configuration file in YAML format.

The tool also reports if and how the run fails, and if a reference log file is missing. See the README file for more information.

This tool was written by Trung Nguyen at U of Chicago (ndactrung at gmail.com).

------------------------------------------------------------------------
:::

::: {#replica-tool .section}
[]{#replica}

### [9.4.31. ]{.section-number}replica tool[](#replica-tool "Link to this heading"){.headerlink}

The tools/replica directory contains the reorder_remd_traj python script which can be used to reorder the replica trajectories (resulting from the use of the temper command) according to temperature. This will produce discontinuous trajectories with all frames at the same temperature in each trajectory. Additional options can be used to calculate the canonical configurational log-weight for each frame at each temperature using the pymbar package. See the README.md file for further details. Try out the peptide example provided.

This tool was written by (and is maintained by) Tanmoy Sanyal, while at the Shell lab at UC Santa Barbara. (tanmoy dot 7989 at gmail.com)

------------------------------------------------------------------------
:::

::: {#smd-tool .section}
[]{#smd}

### [9.4.32. ]{.section-number}smd tool[](#smd-tool "Link to this heading"){.headerlink}

The smd subdirectory contains a C++ file dump2vtk_tris.cpp and Makefile which can be compiled and used to convert triangle output files created by the Smooth-Mach Dynamics (MACHDYN) package into a VTK-compatible unstructured grid file. It could then be read in and visualized by VTK.

See the header of dump2vtk.cpp for more details.

This tool was written by the MACHDYN package author, Georg Ganzenmuller at the Fraunhofer-Institute for High-Speed Dynamics, Ernst Mach Institute in Germany (georg.ganzenmueller at emi.fhg.de).

------------------------------------------------------------------------
:::

::: {#spin-tool .section}
[]{#spin}

### [9.4.33. ]{.section-number}spin tool[](#spin-tool "Link to this heading"){.headerlink}

The spin subdirectory contains a C file interpolate.c which can be compiled and used to perform a cubic polynomial interpolation of the MEP following a GNEB calculation.

See the README file in tools/spin/interpolate_gneb for more details.

This tool was written by the SPIN package author, Julien Tranchida at Sandia National Labs (jtranch at sandia.gov, and by Aleksei Ivanov, at University of Iceland (ali5 at hi.is).

------------------------------------------------------------------------
:::

::: {#singularity-apptainer-tool .section}
[]{#singularity-tool}

### [9.4.34. ]{.section-number}singularity/apptainer tool[](#singularity-apptainer-tool "Link to this heading"){.headerlink}

The singularity subdirectory contains container definitions files that can be used to build container images for building and testing LAMMPS on specific OS variants using the [Apptainer](https://apptainer.org){.reference .external} or [Singularity](https://sylabs.io){.reference .external} container software. Contributions for additional variants are welcome. For more details please see the README.md file in that folder.

------------------------------------------------------------------------
:::

::::: {#stl-bin2txt-tool .section}
[]{#stlconvert}

### [9.4.35. ]{.section-number}stl_bin2txt tool[](#stl-bin2txt-tool "Link to this heading"){.headerlink}

The file stl_bin2txt.cpp converts binary STL files - like they are frequently offered for download on the web - into ASCII format STL files that LAMMPS can read with the [[create_atoms mesh]{.doc}]create_atoms.md){.reference .internal} or the [[fix smd/wall_surface]{.doc}]fix_smd_wall_surface.md){.reference .internal} commands. The syntax for running the tool is

:::: {.highlight-bash .notranslate}
::: highlight
    stl_bin2txt infile.stl outfile.stl
:::
::::

which creates outfile.stl from infile.stl. This tool must be compiled on a platform compatible with the byte-ordering that was used to create the binary file. This usually is a so-called little endian hardware (like x86).

------------------------------------------------------------------------
:::::

::::::::::::::: {#swig-interface .section}
[]{#swig}

### [9.4.36. ]{.section-number}SWIG interface[](#swig-interface "Link to this heading"){.headerlink}

The [SWIG tool](https://swig.org){.reference .external} offers a mostly automated way to incorporate compiled code modules into scripting languages. It processes the function prototypes in C and generates wrappers for a wide variety of scripting languages from it. Thus it can also be applied to the [[C language library interface]{.doc}]Library.md){.reference .internal} of LAMMPS so that build a wrapper that allows to call LAMMPS from programming languages like: C#/Mono, Lua, Java, JavaScript, Perl, Python, R, Ruby, Tcl, and more.

::: {#what-is-included .section}
#### What is included[](#what-is-included "Link to this heading"){.headerlink}

We provide here an "interface file", [`lammps.i`{.docutils .literal .notranslate}]{.pre}, that has the content of the [`library.h`{.docutils .literal .notranslate}]{.pre} file adapted so SWIG can process it. That will create wrappers for all the functions that are present in the LAMMPS C library interface. Please note that not all kinds of C functions can be automatically translated, so you would have to add custom functions to be able to utilize those where the automatic translation does not work. A few functions for converting pointers and accessing arrays are predefined. We provide the file here on an "as is" basis to help people getting started, but not as a fully tested and supported feature of the LAMMPS distribution. Any contributions to complete this are, of course, welcome. Please also note, that for the case of creating a Python wrapper, a fully supported [[Ctypes based lammps module]{.doc}]Python_module.md){.reference .internal} already exists. That module is designed to be object-oriented while SWIG will generate a 1:1 translation of the functions in the interface file.
:::

::::::::: {#building-the-wrapper .section}
#### Building the wrapper[](#building-the-wrapper "Link to this heading"){.headerlink}

When using CMake, the build steps for building a wrapper module are integrated for the languages: Java, Lua, Perl5, Python, Ruby, and Tcl. These require that the LAMMPS library is build as a shared library and all necessary development headers and libraries are present.

:::: {.highlight-bash .notranslate}
::: highlight
    -D WITH_SWIG=on          # to enable building any SWIG wrapper
    -D BUILD_SWIG_JAVA=on    # to enable building the Java wrapper
    -D BUILD_SWIG_LUA=on     # to enable building the Lua wrapper
    -D BUILD_SWIG_PERL5=on   # to enable building the Perl 5.x wrapper
    -D BUILD_SWIG_PYTHON=on  # to enable building the Python wrapper
    -D BUILD_SWIG_RUBY=on    # to enable building the Ruby wrapper
    -D BUILD_SWIG_TCL=on     # to enable building the Tcl wrapper
:::
::::

Manual building allows a little more flexibility. E.g. one can choose the name of the module and build and use a dynamically loaded object for Tcl with:

:::: {.highlight-bash .notranslate}
::: highlight
    swig -tcl -module tcllammps lammps.i
    gcc -fPIC -shared $(pkg-config tcl --cflags) -o tcllammps.so \
                lammps_wrap.c -L ../src/ -llammps
    tclsh
:::
::::

Or one can build an extended Tcl shell command with the wrapped functions included with:

:::: {.highlight-bash .notranslate}
::: highlight
    swig -tcl -module tcllmps lammps_shell.i
    gcc -o tcllmpsh lammps_wrap.c -Xlinker -export-dynamic \
             -DHAVE_CONFIG_H $(pkg-config tcl --cflags) \
             $(pkg-config tcl --libs) -L ../src -llammps
:::
::::

In both cases it is assumed that the LAMMPS library was compiled as a shared library in the [`src`{.docutils .literal .notranslate}]{.pre} folder. Otherwise the last part of the commands needs to be adjusted.
:::::::::

::: {#utility-functions .section}
#### Utility functions[](#utility-functions "Link to this heading"){.headerlink}

Definitions for several utility functions required to manage and access data passed or returned as pointers are included in the [`lammps.i`{.docutils .literal .notranslate}]{.pre} file. So most of the functionality of the library interface should be accessible. What works and what does not depends a bit on the individual language for which the wrappers are built and how well SWIG supports those. The [SWIG documentation](https://swig.org/doc.html){.reference .external} has very detailed instructions and recommendations.
:::

::::: {#usage-examples .section}
#### Usage examples[](#usage-examples "Link to this heading"){.headerlink}

The [`tools/swig`{.docutils .literal .notranslate}]{.pre} folder has multiple shell scripts, [`run_<name>_example.sh`{.docutils .literal .notranslate}]{.pre} that will create a small example script and demonstrate how to load the wrapper and run LAMMPS through it in the corresponding programming language.

For illustration purposes below is a part of the Tcl example script.

:::: {.highlight-tcl .notranslate}
::: highlight
    load ./tcllammps.so
    set lmp [lammps_open_no_mpi 0 NULL NULL]
    lammps_command $lmp "units real"
    lammps_command $lmp "lattice fcc 2.5"
    lammps_command $lmp "region box block -5 5 -5 5 -5 5"
    lammps_command $lmp "create_box 1 box"
    lammps_command $lmp "create_atoms 1 box"

    set dt [doublep_value [voidp_to_doublep [lammps_extract_global $lmp dt]]]
    puts "LAMMPS version $ver"
    puts [format "Number of created atoms: %g" [lammps_get_natoms $lmp]]
    puts "Current size of timestep: $dt"
    puts "LAMMPS version: [lammps_version $lmp]"
    lammps_close $lmp
:::
::::

------------------------------------------------------------------------
:::::
:::::::::::::::

:::: {#tabulate-tool .section}
[]{#tabulate}

### [9.4.37. ]{.section-number}tabulate tool[](#tabulate-tool "Link to this heading"){.headerlink}

::: versionadded
[Added in version 22Dec2022.]{.versionmodified .added}
:::

The [`tabulate`{.docutils .literal .notranslate}]{.pre} folder contains Python scripts to generate and visualize tabulated potential files for LAMMPS. The bulk of the code is in the [`tabulate`{.docutils .literal .notranslate}]{.pre} module in the [`tabulate.py`{.docutils .literal .notranslate}]{.pre} file. Some example files demonstrating its use are included. See the README file for more information.

------------------------------------------------------------------------
::::

::: {#tinker-tool .section}
[]{#tinker}

### [9.4.38. ]{.section-number}tinker tool[](#tinker-tool "Link to this heading"){.headerlink}

The [`tinker`{.docutils .literal .notranslate}]{.pre} folder contains Python scripts to convert Tinker input files to LAMMPS.

See the README file for more information.

Those scripts were written by Steve Plimpton sjplimp at gmail.com

------------------------------------------------------------------------
:::

::: {#valgrind-tool .section}
[]{#valgrind}

### [9.4.39. ]{.section-number}valgrind tool[](#valgrind-tool "Link to this heading"){.headerlink}

The [`valgrind`{.docutils .literal .notranslate}]{.pre} folder contains additional suppressions for LAMMPS when using [valgrind's](https://valgrind.org/){.reference .external} \` [memcheck tool](https://valgrind.org/info/tools.html#memcheck){.reference .external} to search for memory access violation and memory leaks. These suppressions are automatically invoked when running tests through CMake "ctest -T memcheck". See the instructions in the [`README`{.docutils .literal .notranslate}]{.pre} file to add these suppressions when using valgrind with LAMMPS or other programs.

------------------------------------------------------------------------
:::

::: {#vim-tool .section}
[]{#vim}

### [9.4.40. ]{.section-number}vim tool[](#vim-tool "Link to this heading"){.headerlink}

The files in the [`tools/vim`{.docutils .literal .notranslate}]{.pre} directory are add-ons to the VIM editor that allow easier editing of LAMMPS input scripts. See the [`README.txt`{.docutils .literal .notranslate}]{.pre} file for details.

These files were provided by Gerolf Ziegenhain (gerolf at ziegenhain.com)

------------------------------------------------------------------------
:::

::: {#xmgrace-tool .section}
[]{#xmgrace}

### [9.4.41. ]{.section-number}xmgrace tool[](#xmgrace-tool "Link to this heading"){.headerlink}

The files in the tools/xmgrace directory can be used to plot the thermodynamic data in LAMMPS log files via the xmgrace plotting package. There are several tools in the directory that can be used in post-processing mode. The lammpsplot.cpp file can be compiled and used to create plots from the current state of a running LAMMPS simulation.

See the README file for details.

These files were provided by Vikas Varshney (vv0210 at gmail.com)
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::: {#build-the-lammps-documentation .section}
# [3.9. ]{.section-number}Build the LAMMPS documentation[](#build-the-lammps-documentation "Link to this heading"){.headerlink}

Depending on how you obtained LAMMPS and whether you have built the manual yourself, this directory has a number of subdirectories and files. Here is a list with descriptions:

:::: {.highlight-bash .notranslate}
::: highlight
    README           # brief info about the documentation
    src              # content files for LAMMPS documentation
    html             # HTML version of the LAMMPS manual (see html/Manual.html)
    utils            # tools and settings for building the documentation
    lammps.1         # man page for the lammps command
    msi2lmp.1        # man page for the msi2lmp command
    Manual.pdf       # large PDF version of entire manual
    LAMMPS.epub      # Manual in ePUB e-book format
    LAMMPS.mobi      # Manual in MOBI e-book format
    docenv           # virtualenv folder for processing the manual sources
    doctrees         # temporary data from processing the manual
    doxygen          # doxygen configuration and output
    .gitignore       # list of files and folders to be ignored by git
    doxygen-warn.log # logfile with warnings from running doxygen
    github-development-workflow.md   # notes on the LAMMPS development workflow
:::
::::

If you downloaded LAMMPS as a tarball from [the LAMMPS website](https://www.lammps.org){.reference .external}, the html folder and the PDF files should be included.

If you downloaded LAMMPS from the public git repository, then the HTML and PDF files are not included. You can build the HTML or PDF files yourself, by typing [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`html`{.docutils .literal .notranslate}]{.pre} or [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`pdf`{.docutils .literal .notranslate}]{.pre} in the [`doc`{.docutils .literal .notranslate}]{.pre} folder. This requires various tools and files. Some of them have to be installed (see below). For the rest the build process will attempt to download and install them into a python virtual environment and local folders.

A current version of the manual (latest feature release, that is the state of the *release* branch) is available online at: [https://docs.lammps.org/](https://docs.lammps.org/){.reference .external}. A version of the manual corresponding to the ongoing development (that is the state of the *develop* branch) is available online at: [https://docs.lammps.org/latest/](https://docs.lammps.org/latest/){.reference .external} A version of the manual corresponding to the latest stable LAMMPS release (that is the state of the *stable* branch) is available online at: [https://docs.lammps.org/stable/](https://docs.lammps.org/stable/){.reference .external}

::::: {#build-using-gnu-make .section}
## [3.9.1. ]{.section-number}Build using GNU make[](#build-using-gnu-make "Link to this heading"){.headerlink}

The LAMMPS manual is written in [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html){.reference .external} format which can be translated to different output format using the [Sphinx](https://www.sphinx-doc.org/){.reference .external} document generator tool. It also incorporates programmer documentation extracted from the LAMMPS C++ sources through the [Doxygen](https://doxygen.nl/){.reference .external} program. Currently the translation to HTML, PDF (via LaTeX), ePUB (for many e-book readers) and MOBI (for Amazon Kindle readers) are supported. For that to work a Python interpreter version 3.8 or later, the [`doxygen`{.docutils .literal .notranslate}]{.pre} tools and internet access to download additional files and tools are required. This download is usually only required once or after the documentation folder is returned to a pristine state with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`clean-all`{.docutils .literal .notranslate}]{.pre}. You can also upgrade those packages to their latest available versions with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`upgrade`{.docutils .literal .notranslate}]{.pre}.

For the documentation build a python virtual environment is set up in the folder [`doc/docenv`{.docutils .literal .notranslate}]{.pre} and various python packages are installed into that virtual environment via the [`pip`{.docutils .literal .notranslate}]{.pre} tool. For rendering embedded LaTeX code also the [MathJax](https://www.mathjax.org/){.reference .external} JavaScript engine needs to be downloaded. If you need to pass additional options to the pip commands to work (e.g. to use a web proxy or to point to additional SSL certificates) you can set them via the [`PIP_OPTIONS`{.docutils .literal .notranslate}]{.pre} environment variable or uncomment and edit the [`PIP_OPTIONS`{.docutils .literal .notranslate}]{.pre} setting at beginning of the makefile.

The actual translation is then done via [`make`{.docutils .literal .notranslate}]{.pre} commands in the doc folder. The following [`make`{.docutils .literal .notranslate}]{.pre} commands are available:

:::: {.highlight-bash .notranslate}
::: highlight
    make html          # generate HTML in html dir using Sphinx
    make pdf           # generate PDF  as Manual.pdf using Sphinx and PDFLaTeX
    make epub          # generate LAMMPS.epub in ePUB format using Sphinx
    make mobi          # generate LAMMPS.mobi in MOBI format using ebook-convert

    make fasthtml      # generate approximate HTML in fasthtml dir using pandoc

    make upgrade       # upgrade sphinx, extensions, and dependencies to latest supported versions
    make clean         # remove intermediate RST files created by HTML build
    make clean-all     # remove entire build folder and any cached data
    make upgrade       # upgrade the python packages in the virtual environment

    make check         # run all checks listed in this block
    make anchor_check  # check for duplicate anchor labels
    make style_check   # check for complete and consistent style lists
    make package_check # check for complete and consistent package lists
    make char_check    # check for non-ASCII characters
    make role_check    # check for misformatted role keywords

    make link_check    # check for broken external URLs
    make spelling      # spell-check the manual
:::
::::
:::::

------------------------------------------------------------------------

::::: {#build-using-cmake .section}
## [3.9.2. ]{.section-number}Build using CMake[](#build-using-cmake "Link to this heading"){.headerlink}

It is also possible to create the HTML version (and **only** the HTML version) of the manual within the [[CMake build directory]{.doc}]Build_cmake.md){.reference .internal}. The reason for this option is to include the installation of the HTML manual pages into the "install" step when installing LAMMPS after the CMake build via [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--build`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`.`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--target`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre}. The documentation build is included in the default build target, but can also be requested independently with [`cmake`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--build`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`.`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--target`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`doc`{.docutils .literal .notranslate}]{.pre}. If you need to pass additional options to the pip commands to work (e.g. to use a web proxy or to point to additional SSL certificates) you can set them via the [`PIP_OPTIONS`{.docutils .literal .notranslate}]{.pre} environment variable.

:::: {.highlight-bash .notranslate}
::: highlight
    -D BUILD_DOC=value       # yes or no (default)
:::
::::
:::::

------------------------------------------------------------------------

:::::::::::: {#prerequisites-for-html .section}
## [3.9.3. ]{.section-number}Prerequisites for HTML[](#prerequisites-for-html "Link to this heading"){.headerlink}

To run the HTML documentation build toolchain, Python 3.8 or later, git, doxygen, and virtualenv have to be installed locally. Here are instructions for common setups:

::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
Ubuntu

Fedora or RHEL/AlmaLinux/RockyLinux (8.x or later)

macOS
:::

::::: {#panel-0-0-0 .sphinx-tabs-panel aria-labelledby="tab-0-0-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt-get install git doxygen
:::
::::
:::::

::::: {#panel-0-0-1 .sphinx-tabs-panel aria-labelledby="tab-0-0-1" hidden="true" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    sudo dnf install git doxygen
:::
::::
:::::

::: {#panel-0-0-2 .sphinx-tabs-panel aria-labelledby="tab-0-0-2" hidden="true" role="tabpanel" tabindex="0"}
*Python 3*

If Python 3 is not available on your macOS system, you can download the latest Python 3 macOS package from [https://www.python.org](https://www.python.org){.reference .external} and install it. This will install both Python 3 and pip3.
:::
:::::::::::
::::::::::::

::: {#prerequisites-for-pdf .section}
## [3.9.4. ]{.section-number}Prerequisites for PDF[](#prerequisites-for-pdf "Link to this heading"){.headerlink}

In addition to the tools needed for building the HTML format manual, a working LaTeX installation with support for PDFLaTeX and a selection of LaTeX styles/packages are required. Apart from LaTeX packages that are usually installed by default, the following packages are required:

  --------- ---------- -------- ----------- -------- -------- ---------- ---------- ------------- --------- ----------
  amsmath   anysize    babel    capt-of     cmap     dvipng   ellipse    fncychap   fontawesome   framed    geometry
  gyre      hyperref   hypcap   needspace   pict2e   times    tabulary   titlesec   upquote       wrapfig   xindy
  --------- ---------- -------- ----------- -------- -------- ---------- ---------- ------------- --------- ----------

To run the PDFLaTeX translation the [`latexmk`{.docutils .literal .notranslate}]{.pre} script needs to be installed as well.
:::

::: {#prerequisites-for-epub-and-mobi .section}
## [3.9.5. ]{.section-number}Prerequisites for ePUB and MOBI[](#prerequisites-for-epub-and-mobi "Link to this heading"){.headerlink}

In addition to the tools needed for building the HTML format manual, a working LaTeX installation with a few add-on LaTeX packages as well as the [`dvipng`{.docutils .literal .notranslate}]{.pre} tool are required to convert embedded math expressions transparently into embedded images.

For converting the generated ePUB file to a MOBI format file (for e-book readers, like Kindle, that cannot read ePUB), you also need to have the [`ebook-convert`{.docutils .literal .notranslate}]{.pre} tool from the "calibre" software installed. [https://calibre-ebook.com/](https://calibre-ebook.com/){.reference .external} Typing [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`mobi`{.docutils .literal .notranslate}]{.pre} will first create the ePUB file and then convert it. On the Kindle readers in particular, you also have support for PDF files, so you could download and view the PDF version as an alternative.
:::

:::::: {#instructions-for-developers .section}
## [3.9.6. ]{.section-number}Instructions for Developers[](#instructions-for-developers "Link to this heading"){.headerlink}

When adding new styles or options to the LAMMPS code, corresponding documentation is required and either existing files in the [`src`{.docutils .literal .notranslate}]{.pre} folder need to be updated or new files added. These files are written in [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html){.reference .external} markup for translation with the Sphinx tool.

::: {#testing-your-contribution .section}
### Testing your contribution[](#testing-your-contribution "Link to this heading"){.headerlink}

Before contributing any documentation, please check that both the HTML and the PDF format documentation can translate without errors and that there are no spelling issues. This is done with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`html`{.docutils .literal .notranslate}]{.pre}, [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`pdf`{.docutils .literal .notranslate}]{.pre}, and [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`spelling`{.docutils .literal .notranslate}]{.pre}, respectively.
:::

::: {#fast-and-approximate-translation-to-html .section}
### Fast and approximate translation to HTML[](#fast-and-approximate-translation-to-html "Link to this heading"){.headerlink}

Translating the full manual to HTML or PDF can take a long time. Thus there is a fast and approximate way to translate the reStructuredText to HTML as a quick-n-dirty way of checking your manual page.

This translation uses [Pandoc](https://pandoc.org){.reference .external} instead of Sphinx and thus all special Sphinx features (cross-references, advanced tables, embedding of Python docstrings or doxygen documentation, and so on) will not render correctly. Most embedded math should render correctly. This is a **very fast** way to check the syntax and layout of a documentation file translated to HTML while writing or updating it.

To translate **all** manual pages, you can type [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`fasthtml`{.docutils .literal .notranslate}]{.pre} at the command line. The translated HTML files are then in the [`fasthtml`{.docutils .literal .notranslate}]{.pre} folder. All subsequent [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`fasthtml`{.docutils .literal .notranslate}]{.pre} commands will only translate [`.rst`{.docutils .literal .notranslate}]{.pre} files that have been changed. The [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`fasthtml`{.docutils .literal .notranslate}]{.pre} command can be parallelized with make using the -j flag. You can also directly translate only individual pages: e.g. to translate only the [`doc/src/pair_lj.rst`{.docutils .literal .notranslate}]{.pre} page type [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`fasthtml/pair_lj.html`{.docutils .literal .notranslate}]{.pre}

After writing the documentation is completed, you will still need to verify with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`html`{.docutils .literal .notranslate}]{.pre} and [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`pdf`{.docutils .literal .notranslate}]{.pre} that it translates correctly in both formats.
:::

::: {#tests-for-consistency-completeness-and-other-known-issues .section}
### Tests for consistency, completeness, and other known issues[](#tests-for-consistency-completeness-and-other-known-issues "Link to this heading"){.headerlink}

Please also check the output to the console for any warnings or problems. There will be multiple tests run automatically:

- A test for correctness of all anchor labels and their references

- A test that all LAMMPS packages (= folders with sources in [`lammps/src`{.docutils .literal .notranslate}]{.pre}) are documented and listed. A typical warning shows the name of the folder with the suspected new package code and the documentation files where they need to be listed:

  :::: {.highlight-none .notranslate}
  ::: highlight
      Found 88 packages
      Package NEWPACKAGE missing in Packages_list.rst
      Package NEWPACKAGE missing in Packages_details.rst
  :::
  ::::

- A test that only standard, printable ASCII text characters are used. This runs the command [`env`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`LC_ALL=C`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`grep`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-n`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'[^`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-~]'`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`src/*.rst`{.docutils .literal .notranslate}]{.pre} and thus prints all offending lines with filename and line number prepended to the screen. Special characters like Greek letters ([\\(\\alpha\~\~\\sigma\~\~\\epsilon\\)]{.math .notranslate .nohighlight}), super- or subscripts ([\\(x\^2\~\~\\mathrm{U}\_{LJ}\\)]{.math .notranslate .nohighlight}), mathematical expressions ([\\(\\frac{1}{2}\\mathrm{N}\~\~x\\to\\infty\\)]{.math .notranslate .nohighlight}), or the Angstrom symbol ([\\(\\AA\\)]{.math .notranslate .nohighlight}) should be typeset with embedded LaTeX (like this [`` :math:`\alpha ``{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`\sigma`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`` \epsilon` ``{.docutils .literal .notranslate}]{.pre}, [`` :math:`x^2 ``{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`` \mathrm{E}_{LJ}` ``{.docutils .literal .notranslate}]{.pre}, [`` :math:`\frac{1}{2}\mathrm{N} ``{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`` x\to\infty` ``{.docutils .literal .notranslate}]{.pre}, or [`` :math:`\AA` ``{.docutils .literal .notranslate}]{.pre}).

- Embedded LaTeX is rendered in HTML output with [MathJax](https://www.mathjax.org/){.reference .external} and in PDF output by passing the embedded text to LaTeX. Some care has to be taken, though, since there are limitations which macros and features can be used in either mode, so it is recommended to always check whether any new or changed documentation does translate and render correctly with either output.

- A test whether all styles are documented and listed in their respective overview pages. A typical output with warnings looks like this:

  :::: {.highlight-none .notranslate}
  ::: highlight
      Parsed style names w/o suffixes from C++ tree in ../src:
         Angle styles:      21    Atom styles:       24
         Body styles:        3    Bond styles:       17
         Command styles:    41    Compute styles:   143
         Dihedral styles:   16    Dump styles:       26
         Fix styles:       223    Improper styles:   13
         Integrate styles:   4    Kspace styles:     15
         Minimize styles:    9    Pair styles:      234
         Reader styles:      4    Region styles:      8
      Compute style entry newcomp is missing or incomplete in Commands_compute.rst
      Compute style entry newcomp is missing or incomplete in compute.rst
      Fix style entry newfix is missing or incomplete in Commands_fix.rst
      Fix style entry newfix is missing or incomplete in fix.rst
      Pair style entry new is missing or incomplete in Commands_pair.rst
      Pair style entry new is missing or incomplete in pair_style.rst
      Found 6 issue(s) with style lists
  :::
  ::::

In addition, there is the option to run a spellcheck on the entire manual with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`spelling`{.docutils .literal .notranslate}]{.pre}. This requires [a library called enchant](https://github.com/rrthomas/enchant){.reference .external}. To avoid printing out *false positives* (e.g. keywords, names, abbreviations) those can be added to the file [`lammps/doc/utils/sphinx-config/false_positives.txt`{.docutils .literal .notranslate}]{.pre}.
:::
::::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::

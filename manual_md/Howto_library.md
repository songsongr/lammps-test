::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#library-interface-to-lammps .section}
# [10.1.7. ]{.section-number}Library interface to LAMMPS[](#library-interface-to-lammps "Link to this heading"){.headerlink}

As described on the [[Build basics]{.doc}]Build_basics.md){.reference .internal} doc page, LAMMPS can be built as a static or shared library, so that it can be called by another code, used in a [[coupled manner]{.doc}]Howto_couple.md){.reference .internal} with other codes, or driven through a [[Python interface]{.doc}]Python_head.md){.reference .internal}.

At the core of LAMMPS is the [`LAMMPS`{.docutils .literal .notranslate}]{.pre} class, which encapsulates the state of the simulation program through the state of the various class instances that it is composed of. So a calculation using LAMMPS requires creating an instance of the [`LAMMPS`{.docutils .literal .notranslate}]{.pre} class and then send it (text) commands, either individually or from a file, or perform other operations that modify the state stored inside that instance or drive simulations. This is essentially what the [`src/main.cpp`{.docutils .literal .notranslate}]{.pre} file does as well for the standalone LAMMPS executable, reading commands either from an input file or the standard input.

Creating a LAMMPS instance can be done by using C++ code directly or through a C-style interface library to LAMMPS that is provided in the files [`src/library.cpp`{.docutils .literal .notranslate}]{.pre} and [`src/library.h`{.docutils .literal .notranslate}]{.pre}. This [[C language API]{.std .std-ref}]Library.md#lammps-c-api){.reference .internal}, can be used from C and C++, and is also the basis for the [[Python]{.doc}]Python_module.md){.reference .internal} and [[Fortran]{.doc}]Fortran.md){.reference .internal} interfaces or the [[SWIG based wrappers]{.std .std-ref}]Tools.md#swig){.reference .internal} included in the LAMMPS source code.

The [`examples/COUPLE`{.docutils .literal .notranslate}]{.pre} and [`python/examples`{.docutils .literal .notranslate}]{.pre} directories contain some example programs written in C++, C, Fortran, and Python, which show how a driver code can link to LAMMPS as a library, run LAMMPS on a subset of processors (so the others are available to run some other code concurrently), grab data from LAMMPS, change it, and send it back into LAMMPS.

A detailed documentation of the available APIs and examples of how to use them can be found in the [[Programmer Guide]{.std .std-ref}]Manual.md#programmer-documentation){.reference .internal} section of this manual.
:::
::::
:::::

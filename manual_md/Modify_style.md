:::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::: {#lammps-programming-style .section}
# [3.4. ]{.section-number}LAMMPS programming style[](#lammps-programming-style "Link to this heading"){.headerlink}

The aim of the LAMMPS developers is to use a consistent programming style and naming conventions across the entire code base, as this helps with maintenance, debugging, and understanding the code, both for developers and users. This page provides a list of standard style choices used in LAMMPS. Some of these standards are required, while others are just preferred. Following these conventions will make it much easier to integrate your contribution. If you are uncertain, please ask.

The files pair_lj_cut.h, pair_lj_cut.cpp, utils.h, and utils.cpp may serve as representative examples.

::: {#include-files-varied .section}
## [3.4.1. ]{.section-number}Include files (varied)[](#include-files-varied "Link to this heading"){.headerlink}

- Header files that define a new LAMMPS style (i.e. that have a [`SomeStyle(some/name,SomeName);`{.docutils .literal .notranslate}]{.pre} macro in them) should only use the include file for the base class and otherwise use forward declarations and pointers; when interfacing to a library use the PIMPL (pointer to implementation) approach where you have a pointer to a struct that contains all library specific data (and thus requires the library header) but use a forward declaration and define the struct only in the implementation file. This is a **strict** requirement since this is where type clashes between packages and hard-to-find bugs have regularly manifested in the past.

- Header files, especially those defining a "style", should only use the absolute minimum number of include files and **must not** contain any [`using`{.docutils .literal .notranslate}]{.pre} statements. Typically, that would only be the header for the base class. Instead, any include statements should be put in the corresponding implementation files and forward declarations be used. For implementation files, the "include what you use" principle should be employed. However, there is the notable exception that when the [`pointers.h`{.docutils .literal .notranslate}]{.pre} header is included (or the header of one of the classes derived from it), certain headers will *always* be included and thus do not need to be explicitly specified. These are: mpi.h, cstddef, cstdio, cstdlib, string, utils.h, vector, fmt/format.h (or format when using C++20 and later), climits, cinttypes. This also means any such file can assume that FILE, NULL, and INT_MAX are defined.

- Class members variables should not be initialized in the header file, but instead should be initialized either in the initializer list of the constructor or explicitly assigned in the body of the constructor. If the member variable is relevant to the functionality of a class (for example when it stores a value from a command-line argument), the member variable declaration is followed by a brief comment explaining its purpose and what its values can be. Class members that are pointers should always be initialized to [`nullptr`{.docutils .literal .notranslate}]{.pre} in the initializer list of the constructor. This reduces clutter in the header and avoids accessing uninitialized pointers, which leads to hard to debug issues, class members are often implicitly initialized to [`NULL`{.docutils .literal .notranslate}]{.pre} on the first use (but *not* after a [[clear command]{.doc}]clear.md){.reference .internal}). Please see the files [`reset_atoms_mol.h`{.docutils .literal .notranslate}]{.pre} and [`reset_atoms_mol.cpp`{.docutils .literal .notranslate}]{.pre} as an example.

- System headers or headers from installed libraries are included with angular brackets (example: [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`<vector>`{.docutils .literal .notranslate}]{.pre}), while local include files use double quotes (example: [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"atom.h"`{.docutils .literal .notranslate}]{.pre})

- When including system header files from the C library use the C++-style names ([`<cstdlib>`{.docutils .literal .notranslate}]{.pre} or [`<cstring>`{.docutils .literal .notranslate}]{.pre}) instead of the C-style names ([`<stdlib.h>`{.docutils .literal .notranslate}]{.pre} or [`<string.h>`{.docutils .literal .notranslate}]{.pre})

- The order of [`#include`{.docutils .literal .notranslate}]{.pre} statements in a file [`some_name.cpp`{.docutils .literal .notranslate}]{.pre} that implements a class [`SomeName`{.docutils .literal .notranslate}]{.pre} defined in a header file [`some_name.h`{.docutils .literal .notranslate}]{.pre} should be as follows:

  - [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"some_name.h"`{.docutils .literal .notranslate}]{.pre} followed by an empty line

  - LAMMPS include files e.g. [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"comm.h"`{.docutils .literal .notranslate}]{.pre} or [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"modify.h"`{.docutils .literal .notranslate}]{.pre} in alphabetical order followed by an empty line

  - System header files from the C++ or C standard library followed by an empty line

  - [`using`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`namespace`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`LAMMPS_NS`{.docutils .literal .notranslate}]{.pre} or other namespace imports.
:::

::: {#whitespace-preferred .section}
## [3.4.2. ]{.section-number}Whitespace (preferred)[](#whitespace-preferred "Link to this heading"){.headerlink}

Source files should not contain TAB characters unless required by the syntax (e.g. in makefiles) and no trailing whitespace. Text files should have Unix-style line endings (LF-only). Git will automatically convert those in both directions when running on Windows; use dos2unix on Linux machines to convert files to Unix-style line endings. The last line of text files include a line ending.

You can check for these issues with the python scripts in the [["tools/coding_standard"]{.std .std-ref}]Tools.md#coding-standard){.reference .internal} folder. When run normally with a source file or a source folder as argument, they will list all non-conforming lines. By adding the -f flag to the command line, they will modify the flagged files to try to remove the detected issues.
:::

::: {#constants-strongly-preferred .section}
## [3.4.3. ]{.section-number}Constants (strongly preferred)[](#constants-strongly-preferred "Link to this heading"){.headerlink}

Global or per-file constants should be declared as static constexpr variables rather than via the pre-processor with #define. The name of constants should be all uppercase. This has multiple advantages:

- constants are easily identified as such by their all upper case name

- rather than a pure text substitution during pre-processing, constexpr variables have a type associated with them and are processed later in the parsing process where the syntax checks and type specific processing (e.g. via overloads) can be applied to them.

- compilers can emit a warning if the constant is not used and thus can be removed (we regularly check for and remove dead code like this)

- there are no unexpected substitutions and thus confusing syntax errors when compiling leading to, for instance, conflicts so that LAMMPS cannot be compiled with certain combinations of packages (this *has* happened multiple times in the past).

Pre-processor defines should be limited to macros (but consider C++ templates) and conditional compilation. If a per-processor define must be used, it should be defined at the top of the .cpp file after the include statements and at all cost it should be avoided to put them into header files.

Some sets of commonly used constants are provided in the [`MathConst`{.docutils .literal .notranslate}]{.pre} and [`EwaldConst`{.docutils .literal .notranslate}]{.pre} namespaces and implemented in the files [`math_const.h`{.docutils .literal .notranslate}]{.pre} and [`ewald_const.h`{.docutils .literal .notranslate}]{.pre}, respectively.

There are always exceptions, special cases, and legacy code in LAMMPS, so please contact the LAMMPS developers if you are not sure.
:::

::: {#placement-of-braces-strongly-preferred .section}
## [3.4.4. ]{.section-number}Placement of braces (strongly preferred)[](#placement-of-braces-strongly-preferred "Link to this heading"){.headerlink}

For new files added to the "src" tree, a [clang-format](https://clang.llvm.org/docs/ClangFormat.html){.reference .external} configuration file is provided under the name .clang-format. This file is compatible with clang-format version 8 and later. With that file present, files can be reformatted according to the configuration with a command like: clang-format -i new-file.cpp. Ideally, this is done while writing the code or before a pull request is submitted. Blocks of code where the reformatting from clang-format yields hard-to-read or otherwise undesirable output may be protected with placing a pair // clang-format off and // clang-format on comments around that block.
:::

::: {#miscellaneous-standards-varied .section}
## [3.4.5. ]{.section-number}Miscellaneous standards (varied)[](#miscellaneous-standards-varied "Link to this heading"){.headerlink}

- I/O is done via the C-style stdio library and **not** iostreams.

- Do not use so-called "alternative tokens" like [`and`{.docutils .literal .notranslate}]{.pre}, [`or`{.docutils .literal .notranslate}]{.pre}, [`not`{.docutils .literal .notranslate}]{.pre} and similar, but rather use the corresponding operators [`&&`{.docutils .literal .notranslate}]{.pre}, [`||`{.docutils .literal .notranslate}]{.pre}, and [`!`{.docutils .literal .notranslate}]{.pre}. The alternative tokens are not available by default on all compilers.

- Output to the screen and the logfile should use the corresponding FILE pointers and only be done on MPI rank 0. Use the [[`utils::logmesg()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4IDpEN9LAMMPS_NS5utils7logmesgEvP6LAMMPSRKNSt6stringEDpRR4Args "LAMMPS_NS::utils::logmesg"){.reference .internal} convenience function where possible.

- Usage of C++ virtual, override, final keywords: Please follow the [C++ Core Guideline C.128](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rh-override){.reference .external}. That means, you should only use virtual to declare a new virtual function, override to indicate you are overriding an existing virtual function, and final to prevent any further overriding.

- Trivial destructors: Do not write destructors when they are empty and default.

  :::: {.highlight-c++ .notranslate}
  ::: highlight
      // don't write destructors for A or B like this

      class A : protected Pointers {
       public:
         A();
         ~A() override {}
      };

      class B : protected Pointers {
       public:
         B();
         ~B() override = default;
      };

      // instead, let the compiler create the implicit default destructor by not writing it

      class A : protected Pointers {
       public:
         A();
      };

      class B : protected Pointers {
       public:
         B();
      };
  :::
  ::::

- Please use clang-format only to reformat files that you have contributed. For header files containing a [`SomeStyle(keyword,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ClassName)`{.docutils .literal .notranslate}]{.pre} macros it is required to have this macro embedded with a pair of [`//`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`clang-format`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`off`{.docutils .literal .notranslate}]{.pre}, [`//`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`clang-format`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on`{.docutils .literal .notranslate}]{.pre} comments and the line must be terminated with a semicolon (;). Example:

  :::: {.highlight-c++ .notranslate}
  ::: highlight
      #ifdef COMMAND_CLASS
      // clang-format off
      CommandStyle(run,Run);
      // clang-format on
      #else

      #ifndef LMP_RUN_H
      [...]
  :::
  ::::

  You may also use [`//`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`clang-format`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`on/off`{.docutils .literal .notranslate}]{.pre} throughout your files to protect individual sections from being reformatted.

- All files should have 0644 permissions, i.e. writable by the user only and readable by all and no executable permissions. Executable permissions (0755) should only be for shell scripts or python or similar scripts for interpreted script languages.
:::
::::::::
:::::::::
::::::::::

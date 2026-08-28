::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::: {#code-design .section}
# [4.3. ]{.section-number}Code design[](#code-design "Link to this heading"){.headerlink}

This section explains some code design choices in LAMMPS with the goal of helping developers write new code similar to the existing code. Please see the section on [[Requirements for contributed code]{.doc}]Modify_style.md){.reference .internal} for more specific recommendations and guidelines. While that section is organized more in the form of a checklist for code contributors, the focus here is on overall code design strategy, choices made between possible alternatives, and discussing some relevant C++ programming language constructs.

Historically, the basic design philosophy of the LAMMPS C++ code was a "C with classes" style. The motivation was to make it easy to modify LAMMPS for people without significant training in C++ programming. Data structures and code constructs were used that resemble the previous implementation(s) in Fortran. A contributing factor to this choice was that at the time, C++ compilers were often not mature and some advanced features contained bugs or did not function as the standard required. There were also disagreements between compiler vendors as to how to interpret the C++ standard documents.

However, C++ compilers and the C++ programming language have advanced significantly. In 2020, the LAMMPS developers decided to require the C++11 standard as the minimum C++ language standard for LAMMPS. Since then, we have begun to replace C-style constructs with equivalent C++ functionality. This was taken either from the C++ standard library or implemented as custom classes or functions. The goal is to improve readability of the code and to increase code reuse through abstraction of commonly used functionality. In summer 2025, after the 22 July 2025 stable release, the minimum required C++ language standard was raised to C++17.

::: {.admonition .note}
Note

Please note that as of summer 2025 there is still a sizable chunk of legacy code in LAMMPS that has not yet been refactored to reflect these style conventions in full. LAMMPS has a large code base and many contributors. There is also a hierarchy of precedence in which the code is adapted. Highest priority has been the code in the [`src`{.docutils .literal .notranslate}]{.pre} folder, followed by code in packages in order of their popularity and complexity (simpler code gets adapted sooner), followed by code in the [`lib`{.docutils .literal .notranslate}]{.pre} folder. Source code that is downloaded from external packages or libraries during compilation is not subject to the conventions discussed here.
:::

::::::::::::::: {#object-oriented-code .section}
## [4.3.1. ]{.section-number}Object-oriented code[](#object-oriented-code "Link to this heading"){.headerlink}

LAMMPS is designed to be an object-oriented code. Each simulation is represented by an instance of the LAMMPS class. When running in parallel, each MPI process creates such an instance. This can be seen in the [`main.cpp`{.docutils .literal .notranslate}]{.pre} file where the core steps of running a LAMMPS simulation are the following 3 lines of code:

:::: {.highlight-c++ .notranslate}
::: highlight
    LAMMPS *lammps = new LAMMPS(argc, argv, lammps_comm);
    lammps->input->file();
    delete lammps;
:::
::::

The first line creates a LAMMPS class instance and passes the command line arguments and the global communicator to its constructor. The second line triggers the LAMMPS instance to process the input (either from standard input or a provided input file) until the simulation ends. The third line deletes the LAMMPS instance. The remainder of the main.cpp file has code for error handling, MPI configuration, and other special features.

The basic LAMMPS class hierarchy which is created by the LAMMPS class constructor is shown in [[LAMMPS class topology]{.std .std-ref}]Developer_org.md#id1){.reference .internal}. When input commands are processed, additional class instances are created, or deleted, or replaced. Likewise, specific member functions of specific classes are called to trigger actions such as creating atoms, computing forces, computing properties, time-propagating the system, or writing output.

::: {#compositing-and-inheritance .section}
### Compositing and Inheritance[](#compositing-and-inheritance "Link to this heading"){.headerlink}

LAMMPS makes extensive use of the object-oriented programming (OOP) principles of *compositing* and *inheritance*. Classes like the [`LAMMPS`{.docutils .literal .notranslate}]{.pre} class are a **composite** containing pointers to instances of other classes like [`Atom`{.docutils .literal .notranslate}]{.pre}, [`Comm`{.docutils .literal .notranslate}]{.pre}, [`Force`{.docutils .literal .notranslate}]{.pre}, [`Neighbor`{.docutils .literal .notranslate}]{.pre}, [`Modify`{.docutils .literal .notranslate}]{.pre}, and so on. Each of these classes implements certain functionality by storing and manipulating data related to the simulation and providing member functions that trigger certain actions. Some of those classes like [`Force`{.docutils .literal .notranslate}]{.pre} are themselves composites, containing instances of classes describing different force interactions. Similarly, the [`Modify`{.docutils .literal .notranslate}]{.pre} class contains a list of [`Fix`{.docutils .literal .notranslate}]{.pre} and [`Compute`{.docutils .literal .notranslate}]{.pre} classes. If the input commands that correspond to these classes include the word *style*, then LAMMPS stores only a single instance of that class. E.g. *atom_style*, *comm_style*, *pair_style*, *bond_style*. If the input command does **not** include the word *style*, then there may be many instances of that class defined, for example *region*, *fix*, *compute*, *dump*.

**Inheritance** enables creation of *derived* classes that can share common functionality in their base class while providing a consistent interface. The derived classes replace (dummy or pure) functions in the base class. The higher level classes can then call those methods of the instantiated classes without having to know which specific derived class variant was instantiated. In LAMMPS these derived classes are often referred to as "styles", e.g. pair styles, fix styles, atom styles and so on.

This is the origin of the flexibility of LAMMPS. For example, pair styles implement a variety of different non-bonded interatomic potentials functions. All details for the implementation of a potential are stored and executed in a single class.

As mentioned above, there can be multiple instances of classes derived from the [`Fix`{.docutils .literal .notranslate}]{.pre} or [`Compute`{.docutils .literal .notranslate}]{.pre} base classes. They represent a different facet of LAMMPS' flexibility, as they provide methods which can be called at different points within a timestep, as explained in the [[How a timestep works]{.doc}]Developer_flow.md){.reference .internal} doc page. This allows the input script to tailor how a specific simulation is run, what diagnostic computations are performed, and how the output of those computations is further processed or output.

Additional code sharing is possible by creating derived classes from the derived classes (e.g., to implement an accelerated version of a pair style) where only a subset of the derived class methods are replaced with accelerated versions.
:::

:::::::: {#polymorphism .section}
### Polymorphism[](#polymorphism "Link to this heading"){.headerlink}

Polymorphism and dynamic dispatch are another OOP feature that play an important role in how LAMMPS selects what code to execute. In a nutshell, this is a mechanism where the decision of which member function to call from a class is determined at runtime and not when the code is compiled. To enable it, the function has to be declared as [`virtual`{.docutils .literal .notranslate}]{.pre} and all corresponding functions in derived classes should use the [`override`{.docutils .literal .notranslate}]{.pre} property. Below is a brief example.

:::: {.highlight-c++ .notranslate}
::: highlight
    class Base {
    public:
     virtual ~Base() = default;
     void call();
     void normal();
     virtual void poly();
    };

    void Base::call() {
     normal();
     poly();
    }

    class Derived : public Base {
    public:
     ~Derived() override = default;
     void normal();
     void poly() override;
    };

    // [....]

    Base *base1 = new Base();
    Base *base2 = new Derived();

    base1->call();
    base2->call();
:::
::::

The difference in behavior of the [`normal()`{.docutils .literal .notranslate}]{.pre} and the [`poly()`{.docutils .literal .notranslate}]{.pre} member functions is which of the two member functions is called when executing base1-\>call() versus base2-\>call(). Without polymorphism, a function within the base class can only call member functions within the same scope: that is, [`Base::call()`{.docutils .literal .notranslate}]{.pre} will always call [`Base::normal()`{.docutils .literal .notranslate}]{.pre}. But for the base2-\>call() case, the call of the virtual member function will be dispatched to [`Derived::poly()`{.docutils .literal .notranslate}]{.pre} instead. This mechanism results in calling functions that are within the scope of the class that was used to *create* the instance, even if they are assigned to a pointer for their base class. This is the desired behavior, and this way LAMMPS can even use styles that are loaded at runtime from a shared object file with the [[plugin command]{.doc}]plugin.md){.reference .internal}.

A special case of virtual functions are so-called pure functions. These are virtual functions that are initialized to 0 in the class declaration (see example below).

:::: {.highlight-c++ .notranslate}
::: highlight
    class Base {
    public:
     virtual void pure() = 0;
    };
:::
::::

This has the effect that an instance of the base class cannot be created and that derived classes **must** implement these functions. Many of the functions listed with the various class styles in the section [[Modifying & extending LAMMPS]{.doc}]Modify.md){.reference .internal} are pure functions. The motivation for this is to define the interface or API of the functions, but defer their implementation to the derived classes.

However, there are downsides to this. For example, calls to virtual functions from within a constructor, will *not* be in the scope of the derived class, and thus it is good practice to either avoid calling them or to provide an explicit scope such as [`Base::poly()`{.docutils .literal .notranslate}]{.pre} or [`Derived::poly()`{.docutils .literal .notranslate}]{.pre}. Furthermore, any destructors in classes containing virtual functions should be declared virtual too, so they will be processed in the expected order before types are removed from dynamic dispatch.

::: {.note .admonition}
Important Notes

In order to be able to detect incompatibilities at compile time and to avoid unexpected behavior, it is crucial that all member functions that are intended to replace a virtual or pure function use the [`override`{.docutils .literal .notranslate}]{.pre} property keyword. For the same reason, the use of overloads or default arguments for virtual functions should be avoided, as they lead to confusion over which function is supposed to override which, and which arguments need to be declared.
:::
::::::::

::::: {#style-factories .section}
### Style Factories[](#style-factories "Link to this heading"){.headerlink}

In order to create class instances for different styles, LAMMPS often uses a programming pattern called Factory. Those are functions that create an instance of a specific derived class, say [`PairLJCut`{.docutils .literal .notranslate}]{.pre} and return a pointer to the type of the common base class of that style, [`Pair`{.docutils .literal .notranslate}]{.pre} in this case. To associate the factory function with the style keyword, a [`std::map`{.docutils .literal .notranslate}]{.pre} class is used with function pointers indexed by their keyword (for example "lj/cut" for [`PairLJCut`{.docutils .literal .notranslate}]{.pre} and "morse" for [`PairMorse`{.docutils .literal .notranslate}]{.pre}). A couple of typedefs help keep the code readable, and a template function is used to implement the actual factory functions for the individual classes. Below is an example of such a factory function from the [`Force`{.docutils .literal .notranslate}]{.pre} class as declared in [`force.h`{.docutils .literal .notranslate}]{.pre} and implemented in [`force.cpp`{.docutils .literal .notranslate}]{.pre}. The file [`style_pair.h`{.docutils .literal .notranslate}]{.pre} is generated during compilation and includes all main header files (i.e. those starting with [`pair_`{.docutils .literal .notranslate}]{.pre}) of pair styles and then the macro [`PairStyle()`{.docutils .literal .notranslate}]{.pre} will associate the style name "lj/cut" with a factory function creating an instance of the [`PairLJCut`{.docutils .literal .notranslate}]{.pre} class.

:::: {.highlight-c++ .notranslate}
::: highlight
    // from force.h
    typedef Pair *(*PairCreator)(LAMMPS *);
    typedef std::map<std::string, PairCreator> PairCreatorMap;
    PairCreatorMap *pair_map;

    // from force.cpp
    template <typename S, typename T> static S *style_creator(LAMMPS *lmp)
    {
      return new T(lmp);
    }

    // [...]

    pair_map = new PairCreatorMap();

    #define PAIR_CLASS
    #define PairStyle(key, Class) (*pair_map)[#key] = &style_creator<Pair, Class>;
    #include "style_pair.h"
    #undef PairStyle
    #undef PAIR_CLASS

    // from pair_lj_cut.h

    #ifdef PAIR_CLASS
    PairStyle(lj/cut,PairLJCut);
    #else
    // [...]
:::
::::

Similar code constructs are present in other files like [`modify.cpp`{.docutils .literal .notranslate}]{.pre} and [`modify.h`{.docutils .literal .notranslate}]{.pre} or [`neighbor.cpp`{.docutils .literal .notranslate}]{.pre} and [`neighbor.h`{.docutils .literal .notranslate}]{.pre}. Those contain similar macros and include [`style_*.h`{.docutils .literal .notranslate}]{.pre} files for creating class instances of styles they manage.
:::::
:::::::::::::::

:::::::::: {#i-o-and-output-formatting .section}
## [4.3.2. ]{.section-number}I/O and output formatting[](#i-o-and-output-formatting "Link to this heading"){.headerlink}

::: {#c-style-stdio-versus-c-style-iostreams .section}
### C-style stdio versus C++ style iostreams[](#c-style-stdio-versus-c-style-iostreams "Link to this heading"){.headerlink}

LAMMPS uses the stdio \<https://cppreference.com/w/cpp/io/c.html\> library of the standard C library for reading from and writing to files and console instead of C++ [iostreams](https://cppreference.com/w/cpp/io.html){.reference .external}. This is mainly motivated by better performance, better control over formatting, and less effort to achieve specific formatting.

Since mixing "stdio" and "iostreams" can lead to unexpected behavior, use of the latter is strongly discouraged. Output to the screen should *not* use the predefined [`stdout`{.docutils .literal .notranslate}]{.pre} FILE pointer, but rather the [`screen`{.docutils .literal .notranslate}]{.pre} and [`logfile`{.docutils .literal .notranslate}]{.pre} FILE pointers managed by the LAMMPS class. Furthermore, output should generally only be done by MPI rank 0 ([`comm->me`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`==`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0`{.docutils .literal .notranslate}]{.pre}). Output that is sent to both [`screen`{.docutils .literal .notranslate}]{.pre} and [`logfile`{.docutils .literal .notranslate}]{.pre} should use the [[`utils::logmesg()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`convenience`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`function`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4IDpEN9LAMMPS_NS5utils7logmesgEvP6LAMMPSRKNSt6stringEDpRR4Args "LAMMPS_NS::utils::logmesg"){.reference .internal}.

We strongly discourage the use of [stringstreams](https://cppreference.com/w/cpp/io/basic_stringstream.html){.reference .external} because the bundled [{fmt} library](https://fmt.dev){.reference .external} or the [C++ format library](https://cppreference.com/w/cpp/utility/format.html){.reference .external} (for C++20 and later) and the customized tokenizer classes provide the same functionality in a cleaner way with better performance. This also helps maintain a consistent programming syntax with code from many different contributors.
:::

::: {#formatting-with-the-fmt-library-and-std-format .section}
### Formatting with the {fmt} library and std::format[](#formatting-with-the-fmt-library-and-std-format "Link to this heading"){.headerlink}

The LAMMPS source code currently includes a slightly modified copy of the [{fmt} library](https://fmt.dev){.reference .external}, which is preferred over formatting with the "printf()" family of functions. When compiling for C++20 and later we switch to using the [C++ format library](https://cppreference.com/w/cpp/utility/format.html){.reference .external}. The namespace prefix currently remains [`fmt::`{.docutils .literal .notranslate}]{.pre} through a small wrapper. In the future, this will be switched to [`std::`{.docutils .literal .notranslate}]{.pre} when LAMMPS requires the C++20 standard as the minimum C++ standard. Thus only functionality compatible with the C++ format library for C++20 is accepted. Using [`std::format`{.docutils .literal .notranslate}]{.pre} requires a fully C++20 compatible compiler (e.g. GCC 13 and later, Clang 14 and later, or MSVC 16.10 and later) and we [use the \_\_cpp_lib_format feature test macro](https://cppreference.com/w/cpp/utility/feature_test.html){.reference .external} to confirm the availability of [`std::format`{.docutils .literal .notranslate}]{.pre}.

The primary reason for this choice is that it allows a typesafe default format for any type of supported data. This is particularly useful for formatting integers of a given size (32-bit or 64-bit) which may require different format strings depending on compile time settings or compilers/operating systems. Furthermore, {fmt} gives better performance, has more functionality, a familiar formatting syntax that has similarities to [`format()`{.docutils .literal .notranslate}]{.pre} in Python, and provides a facility that can be used to integrate format strings and a variable number of arguments into custom functions in a much simpler way than the varargs mechanism of the C library.

Formatted strings are frequently created by calling the [`fmt::format()`{.docutils .literal .notranslate}]{.pre} function, which will return a string as a [`std::string`{.docutils .literal .notranslate}]{.pre} class instance. In contrast to the [`%`{.docutils .literal .notranslate}]{.pre} placeholder in [`printf()`{.docutils .literal .notranslate}]{.pre}, the {fmt} library uses [`{}`{.docutils .literal .notranslate}]{.pre} to embed format descriptors. In the simplest case, no additional characters are needed, as {fmt} will choose the default format based on the data type of the argument. Otherwise, the [[`utils::print()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4IDpEN9LAMMPS_NS5utils5printEvP4FILERKNSt6stringEDpRR4Args "LAMMPS_NS::utils::print"){.reference .internal} function may be used instead of [`printf()`{.docutils .literal .notranslate}]{.pre} or [`fprintf()`{.docutils .literal .notranslate}]{.pre}. The equivalent [std::print() function](https://cppreference.com/w/cpp/io/print.html){.reference .external} will become available in C++ 23. In addition, several LAMMPS output functions, that originally accepted a single string as argument have been overloaded to accept a format string with optional arguments as well (e.g., [`Error::all()`{.docutils .literal .notranslate}]{.pre}, [`Error::one()`{.docutils .literal .notranslate}]{.pre}, [[`utils::logmesg()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4IDpEN9LAMMPS_NS5utils7logmesgEvP6LAMMPSRKNSt6stringEDpRR4Args "LAMMPS_NS::utils::logmesg"){.reference .internal}).
:::

::::::: {#summary-of-the-fmt-format-and-std-format-syntax .section}
### Summary of the {fmt} format and std::format syntax[](#summary-of-the-fmt-format-and-std-format-syntax "Link to this heading"){.headerlink}

The syntax of the format string is "{\[\<argument id\>\]\[:\<format spec\>\]}", where either the argument id or the format spec (separated by a colon ':') is optional. The argument id is usually a number starting from 0 that is the index to the arguments following the format string. By default, these are assigned in order (i.e. 0, 1, 2, 3, 4 etc.). The most common case for using argument id would be to use the same argument in multiple places in the format string without having to provide it as an argument multiple times. The argument id is rarely used in the LAMMPS source code.

More common is the use of a format specifier, which starts with a colon. This may optionally be followed by a fill character (default is ' '). If provided, the fill character **must** be followed by an alignment character ('\<', '\^', '\>' for left, centered, or right alignment (default)). The alignment character may be used without a fill character. The next important format parameter would be the minimum width, which may be followed by a dot '.' and a precision for floating point numbers. The final character in the format string would be an indicator for the "presentation", i.e. 'd' for decimal presentation of integers, 'x' for hexadecimal, 'o' for octal, 'c' for character etc. This mostly follows the "printf()" scheme, but without requiring an additional length parameter to distinguish between different integer widths. The {fmt} library will detect those and adapt the formatting accordingly. For floating point numbers there are correspondingly, 'g' for generic presentation, 'e' for exponential presentation, and 'f' for fixed point presentation.

The format string "{:8}" would thus represent *any* type argument and be replaced by at least 8 characters; "{:\<8}" would do this as left aligned, "{:\^8}" as centered, "{:\>8}" as right aligned. If a specific presentation is selected, the argument type must be compatible or else the {fmt} formatting code will throw an exception. Some format string examples are given below:

:::: {.highlight-c++ .notranslate}
::: highlight
    auto mesg = fmt::format("  CPU time: {:4d}:{:02d}:{:02d}\n", cpuh, cpum, cpus);
    mesg = fmt::format("{:<8s}| {:<10.5g} | {:<10.5g} | {:<10.5g} |{:6.1f} |{:6.2f}\n",
                       label, time_min, time, time_max, time_sq, tmp);
    utils::logmesg(lmp,"{:>6} = max # of 1-2 neighbors\n",maxall);
    utils::logmesg(lmp,"Lattice spacing in x,y,z = {:.8} {:.8} {:.8}\n",
                   xlattice,ylattice,zlattice);
:::
::::

which will create the following output lines:

:::: {.highlight-none .notranslate}
::: highlight
    CPU time:    0:02:16
    Pair    | 2.0133     | 2.0133     | 2.0133     |   0.0 | 84.21
         4 = max # of 1-2 neighbors
    Lattice spacing in x,y,z = 1.6795962 1.6795962 1.6795962
:::
::::

Finally, a special feature of the {fmt} library is that format parameters like the width or the precision may be also provided as arguments. In that case a nested format is used where a pair of curly braces (with an optional argument id) "{}" are used instead of the value, for example "{:{}d}" will consume two integer arguments, the first will be the value shown and the second the minimum width.

For more details and examples, please consult the [{fmt} syntax documentation](https://fmt.dev/latest/syntax/){.reference .external} website or the [corresponding C++ syntax reference](https://cppreference.com/w/cpp/utility/format/spec.html){.reference .external}. Since we plan to eventually transition from {fmt} to using [`std::format()`{.docutils .literal .notranslate}]{.pre} of the C++ standard library, it is advisable to avoid using any extensions beyond what the [C++20 standard offers](https://cppreference.com/w/cpp/utility/format/format.html){.reference .external}.
:::::::
::::::::::

::: {#json-format-input-and-output .section}
## [4.3.3. ]{.section-number}JSON format input and output[](#json-format-input-and-output "Link to this heading"){.headerlink}

Since LAMMPS version 12 June 2025, the LAMMPS source code includes a copy of the header-only JSON C++ library from [https://json.nlohmann.me/](https://json.nlohmann.me/){.reference .external}. Same as with the {fmt} library described above some modification to the namespace has been made to avoid collisions with other uses of the same library, which may use a different, incompatible version. To have a uniform interface with other parts of LAMMPS, you should be using [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"json.h"`{.docutils .literal .notranslate}]{.pre} or [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"json_fwd.h"`{.docutils .literal .notranslate}]{.pre} (in header files). See the implementation of the [[molecule command]{.doc}]molecule.md){.reference .internal} for an example of using this library.
:::

::: {#memory-management .section}
## [4.3.4. ]{.section-number}Memory management[](#memory-management "Link to this heading"){.headerlink}

Dynamical allocation of small data and objects can be done with the C++ commands "new" and "delete/delete\[\]". Large data should use the member functions of the [`Memory`{.docutils .literal .notranslate}]{.pre} class, most commonly, [`Memory::create()`{.docutils .literal .notranslate}]{.pre}, [`Memory::grow()`{.docutils .literal .notranslate}]{.pre}, and [`Memory::destroy()`{.docutils .literal .notranslate}]{.pre}, which provide variants for vectors, 2d arrays, 3d arrays, etc. These can also be used for small data.

The use of [`malloc()`{.docutils .literal .notranslate}]{.pre}, [`calloc()`{.docutils .literal .notranslate}]{.pre}, [`realloc()`{.docutils .literal .notranslate}]{.pre} and [`free()`{.docutils .literal .notranslate}]{.pre} directly is strongly discouraged. To simplify adapting legacy code into the LAMMPS code base the member functions [`Memory::smalloc()`{.docutils .literal .notranslate}]{.pre}, [`Memory::srealloc()`{.docutils .literal .notranslate}]{.pre}, and [`Memory::sfree()`{.docutils .literal .notranslate}]{.pre} are available, which perform additional error checks for safety.

Use of these custom memory allocation functions is motivated by the following considerations:

- Memory allocation failures on *any* MPI rank during a parallel run will trigger an immediate abort of the entire parallel calculation.

- A failing "new" will trigger an exception, which is also captured by LAMMPS and triggers a global abort.

- Allocation of multidimensional arrays will be done in a C compatible fashion, but such that the storage of the actual data is stored in one large contiguous block. Thus, when MPI communication is needed, the data can be communicated directly (similar to Fortran arrays).

- The "destroy()" and "sfree()" functions may safely be called on NULL pointers.

- The "destroy()" functions will nullify the pointer variables, thus making "use after free" errors easy to detect.

- It is possible to use a larger than default memory alignment (not on all operating systems, since the allocated storage pointers must be compatible with [`free()`{.docutils .literal .notranslate}]{.pre} for technical reasons).

In the practical implementation of code this means, that any pointer variables, that are class members should be initialized to a [`nullptr`{.docutils .literal .notranslate}]{.pre} value in their respective constructors. That way, it is safe to call [`Memory::destroy()`{.docutils .literal .notranslate}]{.pre} or [`delete[]`{.docutils .literal .notranslate}]{.pre} on them before *any* allocation outside the constructor. This helps prevent memory leaks.
:::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::

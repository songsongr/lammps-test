::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#extending-the-c-api .section}
# [1.1.10. ]{.section-number}Extending the C API[](#extending-the-c-api "Link to this heading"){.headerlink}

The functionality of the LAMMPS library interface has historically been motivated by the needs of its users. Functions have been added or expanded as they were needed and used. Contributions to the interface are always welcome. However with a refactoring of the library interface and its documentation that started in Spring 2020, there are now a few requirements for including new changes or extensions.

> ::: {}
> - New functions should be orthogonal to existing ones and not implement functionality that can already be achieved with the existing APIs.
>
> - All changes and additions should be documented with [Doxygen](https://doxygen.nl){.reference .external} style comments and references to those functions added to the corresponding files in the [`doc/src`{.docutils .literal .notranslate}]{.pre} folder.
>
> - If possible, new unit tests to test those new features should be added.
>
> - New features should also be implemented and documented not just for the C interface, but also the Python and Fortran interfaces.
>
> - All additions should work and be compatible with [`-DLAMMPS_BIGBIG`{.docutils .literal .notranslate}]{.pre}, [`-DLAMMPS_SMALLBIG`{.docutils .literal .notranslate}]{.pre} as well as when compiling with and without MPI support.
>
> - The [`library.h`{.docutils .literal .notranslate}]{.pre} file should be kept compatible to C code at a level similar to C89. Its interfaces may not reference any custom data types (e.g. [`bigint`{.docutils .literal .notranslate}]{.pre}, [`tagint`{.docutils .literal .notranslate}]{.pre}, and so on) that are only known inside of LAMMPS; instead [`int`{.docutils .literal .notranslate}]{.pre} and [`int64_t`{.docutils .literal .notranslate}]{.pre} should be used.
>
> - only use C style comments, not C++ style
> :::

Please note that these are not **strict** requirements, but the LAMMPS developers very much appreciate, if they are followed and can assist with implementing what is missing. It helps maintaining the code base and keeping it consistent.
:::
::::
:::::

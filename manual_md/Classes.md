:::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::: {#c-base-classes .section}
# [4.13. ]{.section-number}C++ base classes[](#c-base-classes "Link to this heading"){.headerlink}

LAMMPS is designed to be used as a C++ class library where one can set up and drive a simulation through creating a class instance and then calling some abstract operations or commands on that class or its member class instances. These are interfaced to the [[C library API]{.doc}]Library.md){.reference .internal}, which providing an additional level of abstraction simplification for common operations. The C API is also the basis for calling LAMMPS from Python or Fortran.

When used from a C++ program, most of the symbols and functions in LAMMPS are wrapped into the [`LAMMPS_NS`{.docutils .literal .notranslate}]{.pre} namespace so they will not collide with your own classes or other libraries. This, however, does not extend to the additional libraries bundled with LAMMPS in the lib folder and some of the low-level code of some packages.

Behind the scenes this is implemented through inheritance and polymorphism where base classes define the abstract interface and derived classes provide the specialized implementation for specific models or optimizations or ports to accelerator platforms. This document will provide an outline of the fundamental class hierarchy and some selected examples for derived classes of specific models.

::: {.admonition .note}
Note

Please see the [[note about thread-safety]{.std .std-ref}]Library.md#thread-safety){.reference .internal} in the library Howto doc page.
:::

------------------------------------------------------------------------

::: {#lammpsbase .toctree-wrapper .compound}
[Individual Base Classes]{.caption-text}

- [4.13.1. LAMMPS Class]Classes_lammps.md){.reference .internal}
  - [[`LAMMPS_NS::LAMMPS`{.docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE){.reference .internal}
    - [[`non_pair_suffix()`{.docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4NK9LAMMPS_NS6LAMMPS15non_pair_suffixEv){.reference .internal}
    - [[`match_style()`{.docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPS11match_styleEPKcPKc){.reference .internal}
    - [[`LAMMPS()`{.docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPS6LAMMPSER4argv8MPI_Comm){.reference .internal}
    - [[`LAMMPS()`{.docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPS6LAMMPSEiPPc8MPI_Comm){.reference .internal}
    - [[`~LAMMPS()`{.docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSD0Ev){.reference .internal}
    - [[`argv_pointers()`{.docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPS13argv_pointersER4argv){.reference .internal}
  - [[`LAMMPS_NS::Pointers`{.docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS8PointersE){.reference .internal}
- [4.13.2. LAMMPS Atom and AtomVec Base Classes]Classes_atom.md){.reference .internal}
  - [[`LAMMPS_NS::Atom`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4AtomE){.reference .internal}
    - [[`Atom()`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom4AtomEP6LAMMPS){.reference .internal}
    - [[`find_custom()`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom11find_customEPKcRiRi){.reference .internal}
    - [[`find_custom_ghost()`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom17find_custom_ghostEPKcRiRiRi){.reference .internal}
    - [[`add_custom()`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom10add_customEPKciii){.reference .internal}
    - [[`remove_custom()`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom13remove_customEiii){.reference .internal}
    - [[`extract()`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom7extractEPKc){.reference .internal}
    - [[`extract_datatype()`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom16extract_datatypeEPKc){.reference .internal}
    - [[`extract_size()`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom12extract_sizeEPKci){.reference .internal}
    - [[`LAMMPS_NS::Atom::PerAtom`{.docutils .literal .notranslate}]{.pre}]Classes_atom.md#_CPPv4N9LAMMPS_NS4Atom7PerAtomE){.reference .internal}
- [4.13.3. LAMMPS Input Base Class]Classes_input.md){.reference .internal}
  - [[`LAMMPS_NS::Input`{.docutils .literal .notranslate}]{.pre}]Classes_input.md#_CPPv4N9LAMMPS_NS5InputE){.reference .internal}
    - [[`Input()`{.docutils .literal .notranslate}]{.pre}]Classes_input.md#_CPPv4N9LAMMPS_NS5Input5InputEP6LAMMPSiPPc){.reference .internal}
    - [[`file()`{.docutils .literal .notranslate}]{.pre}]Classes_input.md#_CPPv4N9LAMMPS_NS5Input4fileEv){.reference .internal}
    - [[`file()`{.docutils .literal .notranslate}]{.pre}]Classes_input.md#_CPPv4N9LAMMPS_NS5Input4fileEPKc){.reference .internal}
    - [[`one()`{.docutils .literal .notranslate}]{.pre}]Classes_input.md#_CPPv4N9LAMMPS_NS5Input3oneERKNSt6stringE){.reference .internal}
:::

------------------------------------------------------------------------

::: {#lammpsutils .toctree-wrapper .compound}
[Individual Utility Classes]{.caption-text}

- [4.13.4. Citation management for contributed features]Classes_cite.md){.reference .internal}
  - [Overview]Classes_cite.md#overview){.reference .internal}
  - [Adding a citation reminder to contributed code]Classes_cite.md#adding-a-citation-reminder-to-contributed-code){.reference .internal}
  - [Implementation details]Classes_cite.md#implementation-details){.reference .internal}
    - [[`LAMMPS_NS::CiteMe`{.docutils .literal .notranslate}]{.pre}]Classes_cite.md#_CPPv4N9LAMMPS_NS6CiteMeE){.reference .internal}
      - [[`CiteMe()`{.docutils .literal .notranslate}]{.pre}]Classes_cite.md#_CPPv4N9LAMMPS_NS6CiteMe6CiteMeEP6LAMMPSiiPKc){.reference .internal}
      - [[`~CiteMe()`{.docutils .literal .notranslate}]{.pre}]Classes_cite.md#_CPPv4N9LAMMPS_NS6CiteMeD0Ev){.reference .internal}
      - [[`add()`{.docutils .literal .notranslate}]{.pre}]Classes_cite.md#_CPPv4N9LAMMPS_NS6CiteMe3addERKNSt6stringE){.reference .internal}
      - [[`flush()`{.docutils .literal .notranslate}]{.pre}]Classes_cite.md#_CPPv4N9LAMMPS_NS6CiteMe5flushEv){.reference .internal}
:::
::::::
:::::::
::::::::

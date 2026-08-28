::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#notes-for-updating-code-written-for-older-lammps-versions .section}
# [4.10. ]{.section-number}Notes for updating code written for older LAMMPS versions[](#notes-for-updating-code-written-for-older-lammps-versions "Link to this heading"){.headerlink}

This section documents how C++ source files that are available *outside of the LAMMPS source distribution* (e.g. in external USER packages or as source files provided as a supplement to a publication) that are written for an older version of LAMMPS and thus need to be updated to be compatible with the current version of LAMMPS. Due to the active development of LAMMPS it is likely to always be incomplete. Please contact [developers@lammps.org](mailto:developers%40lammps.org){.reference .external} in case you run across an issue that is not (yet) listed here. Please also review the latest information about the LAMMPS [[programming style conventions]{.doc}]Modify_style.md){.reference .internal}, especially if you are considering to submit the updated version for inclusion into the LAMMPS distribution.

Available topics in mostly chronological order are:

- [Setting flags in the constructor](#setting-flags-in-the-constructor){.reference .internal}

- [Rename of pack/unpack_comm() to pack/unpack_forward_comm()](#rename-of-pack-unpack-comm-to-pack-unpack-forward-comm){.reference .internal}

- [Use ev_init() to initialize variables derived from eflag and vflag](#use-ev-init-to-initialize-variables-derived-from-eflag-and-vflag){.reference .internal}

- [Use utils::count_words() functions instead of atom-\>count_words()](#use-utils-count-words-functions-instead-of-atom-count-words){.reference .internal}

- [Use utils::numeric() functions instead of force-\>numeric()](#use-utils-numeric-functions-instead-of-force-numeric){.reference .internal}

- [Use utils::open_potential() function to open potential files](#use-utils-open-potential-function-to-open-potential-files){.reference .internal}

- [Use symbolic Atom and AtomVec constants instead of numerical values](#use-symbolic-atom-and-atomvec-constants-instead-of-numerical-values){.reference .internal}

- [Simplify customized error messages](#simplify-customized-error-messages){.reference .internal}

- [Use of "override" instead of "virtual"](#use-of-override-instead-of-virtual){.reference .internal}

- [Simplified and more compact neighbor list requests](#simplified-and-more-compact-neighbor-list-requests){.reference .internal}

- [Split of fix STORE into fix STORE/GLOBAL and fix STORE/PERATOM](#split-of-fix-store-into-fix-store-global-and-fix-store-peratom){.reference .internal}

- [Rename of fix STORE/PERATOM to fix STORE/ATOM and change of arguments](#rename-of-fix-store-peratom-to-fix-store-atom-and-change-of-arguments){.reference .internal}

- [Use Output::get_dump_by_id() instead of Output::find_dump()](#use-output-get-dump-by-id-instead-of-output-find-dump){.reference .internal}

- [Refactored grid communication using Grid3d/Grid2d classes instead of GridComm](#refactored-grid-communication-using-grid3d-grid2d-classes-instead-of-gridcomm){.reference .internal}

- [FLERR as first argument to minimum image functions in Domain class](#flerr-as-first-argument-to-minimum-image-functions-in-domain-class){.reference .internal}

- [Use utils::logmesg() instead of error-\>warning()](#use-utils-logmesg-instead-of-error-warning){.reference .internal}

------------------------------------------------------------------------

::: {#setting-flags-in-the-constructor .section}
## [4.10.1. ]{.section-number}Setting flags in the constructor[](#setting-flags-in-the-constructor "Link to this heading"){.headerlink}

As LAMMPS gains additional functionality, new flags may need to be set in the constructor or a class to signal compatibility with such features. Most of the time the defaults are chosen conservatively, but sometimes the conservative choice is the uncommon choice, and then those settings need to be made when updating code.

Pair styles:

> ::: {}
> - [`manybody_flag`{.docutils .literal .notranslate}]{.pre}: set to 1 if your pair style is not pair-wise additive
>
> - [`restartinfo`{.docutils .literal .notranslate}]{.pre}: set to 0 if your pair style does not store data in restart files
> :::
:::

::::::::: {#rename-of-pack-unpack-comm-to-pack-unpack-forward-comm .section}
## [4.10.2. ]{.section-number}Rename of pack/unpack_comm() to pack/unpack_forward_comm()[](#rename-of-pack-unpack-comm-to-pack-unpack-forward-comm "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 8Aug2014.]{.versionmodified .changed}
:::

In this change set, the functions to pack/unpack data into communication buffers for [[forward communications]{.doc}]Developer_comm_ops.md){.reference .internal} were renamed from [`pack_comm()`{.docutils .literal .notranslate}]{.pre} and [`unpack_comm()`{.docutils .literal .notranslate}]{.pre} to [`pack_forward_comm()`{.docutils .literal .notranslate}]{.pre} and [`unpack_forward_comm()`{.docutils .literal .notranslate}]{.pre}, respectively. Also the meaning of the return value of these functions was changed: rather than returning the number of items per atom stored in the buffer, now the total number of items added (or unpacked) needs to be returned. Here is an example from the PairEAM class. Of course the member function declaration in corresponding header file needs to be updated accordingly.

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    int PairEAM::pack_comm(int n, int *list, double *buf, int pbc_flag, int *pbc)
    {
      int m = 0;
      for (int i = 0; i < n; i++) {
        int j = list[i];
        buf[m++] = fp[j];
      }
      return 1;
    }
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    int PairEAM::pack_forward_comm(int n, int *list, double *buf, int pbc_flag, int *pbc)
    {
      int m = 0;
      for (int i = 0; i < n; i++) {
        int j = list[i];
        buf[m++] = fp[j];
      }
      return m;
    }
:::
::::

::: {.admonition .note}
Note

Because the various "pack" and "unpack" functions are defined in the respective base classes as dummy functions doing nothing, and because of the the name mismatch the custom versions in the derived class will no longer be called, there will be no compilation error when this change is not applied. Only calculations will suddenly produce incorrect results because the required forward communication calls will cease to function correctly.
:::
:::::::::

:::::::: {#use-ev-init-to-initialize-variables-derived-from-eflag-and-vflag .section}
## [4.10.3. ]{.section-number}Use ev_init() to initialize variables derived from eflag and vflag[](#use-ev-init-to-initialize-variables-derived-from-eflag-and-vflag "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 29Mar2019.]{.versionmodified .changed}
:::

There are several variables that need to be initialized based on the values of the "eflag" and "vflag" variables and since sometimes there are new bits added and new variables need to be set to 1 or 0. To make this consistent across all styles, there is now an inline function [`ev_init(eflag,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`vflag)`{.docutils .literal .notranslate}]{.pre} that makes those settings consistently and calls either [`ev_setup()`{.docutils .literal .notranslate}]{.pre} or [`ev_unset()`{.docutils .literal .notranslate}]{.pre}. Example from a pair style:

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    if (eflag || vflag) ev_setup(eflag, vflag);
    else evflag = vflag_fdotr = eflag_global = eflag_atom = 0;
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    ev_init(eflag, vflag);
:::
::::

Not applying this change will not cause a compilation error, but can lead to inconsistent behavior and incorrect tallying of energy or virial.
::::::::

::::::::: {#use-utils-count-words-functions-instead-of-atom-count-words .section}
## [4.10.4. ]{.section-number}Use utils::count_words() functions instead of atom-\>count_words()[](#use-utils-count-words-functions-instead-of-atom-count-words "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 2Jun2020.]{.versionmodified .changed}
:::

The "count_words()" functions for parsing text have been moved from the Atom class to the [[utils namespace]{.doc}]Developer_utils.md){.reference .internal}. The "count_words()" function in "utils" uses the Tokenizer class internally to split a line into words and count them, thus it will not modify the argument string as the function in the Atoms class did and thus had a variant using a copy buffer. Unlike the old version, the new version does not remove comments. For that you can use the [[`utils::trim_comment()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`function`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils12trim_commentERKNSt6stringE "LAMMPS_NS::utils::trim_comment"){.reference .internal} as shown in the example below.

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    nwords = atom->count_words(line);
    int nwords = atom->count_words(buf);
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    nwords = utils::count_words(line);
    int nwords = utils::count_words(utils::trim_comment(buf));
:::
::::

::: {.admonition .seealso}
See also

[[`utils::count_words()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils11count_wordsEPKc "LAMMPS_NS::utils::count_words"){.reference .internal}, [[`utils::trim_comment()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils12trim_commentERKNSt6stringE "LAMMPS_NS::utils::trim_comment"){.reference .internal}
:::
:::::::::

::::::::: {#use-utils-numeric-functions-instead-of-force-numeric .section}
## [4.10.5. ]{.section-number}Use utils::numeric() functions instead of force-\>numeric()[](#use-utils-numeric-functions-instead-of-force-numeric "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 18Sep2020.]{.versionmodified .changed}
:::

The "numeric()" conversion functions (including "inumeric()", "bnumeric()", and "tnumeric()") have been moved from the Force class to the [[utils namespace]{.doc}]Developer_utils.md){.reference .internal}. Also they take an additional argument that selects whether the [`Error::all()`{.docutils .literal .notranslate}]{.pre} or [`Error::one()`{.docutils .literal .notranslate}]{.pre} function should be called in case of an error. The former should be used when *all* MPI processes call the conversion function and the latter *must* be used when they are called from only one or a subset of the MPI processes.

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    val = force->numeric(FLERR, arg[1]);
    num = force->inumeric(FLERR, arg[2]);
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    val = utils::numeric(FLERR, true, arg[1], lmp);
    num = utils::inumeric(FLERR, false, arg[2], lmp);
:::
::::

::: {.admonition .seealso}
See also

[[`utils::numeric()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils7numericEPKciRKNSt6stringEbP6LAMMPS "LAMMPS_NS::utils::numeric"){.reference .internal}, [[`utils::inumeric()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils8inumericEPKciRKNSt6stringEbP6LAMMPS "LAMMPS_NS::utils::inumeric"){.reference .internal}, [[`utils::bnumeric()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils8bnumericEPKciRKNSt6stringEbP6LAMMPS "LAMMPS_NS::utils::bnumeric"){.reference .internal}, [[`utils::tnumeric()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils8tnumericEPKciRKNSt6stringEbP6LAMMPS "LAMMPS_NS::utils::tnumeric"){.reference .internal}
:::
:::::::::

:::::::: {#use-utils-open-potential-function-to-open-potential-files .section}
## [4.10.6. ]{.section-number}Use utils::open_potential() function to open potential files[](#use-utils-open-potential-function-to-open-potential-files "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 18Sep2020.]{.versionmodified .changed}
:::

The [[`utils::open_potential()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils14open_potentialERKNSt6stringEP6LAMMPSPi "LAMMPS_NS::utils::open_potential"){.reference .internal} function must be used to replace calls to [`force->open_potential()`{.docutils .literal .notranslate}]{.pre} and should be used to replace [`fopen()`{.docutils .literal .notranslate}]{.pre} for opening potential files for reading. The custom function does three additional steps compared to [`fopen()`{.docutils .literal .notranslate}]{.pre}: 1) it will try to parse the [`UNITS:`{.docutils .literal .notranslate}]{.pre} and [`DATE:`{.docutils .literal .notranslate}]{.pre} metadata and will stop with an error on a units mismatch and will print the date info, if present, in the log file; 2) for pair styles that support it, it will set up possible automatic unit conversions based on the embedded unit information and LAMMPS' current units setting; 3) it will not only try to open a potential file at the given path, but will also search in the folders listed in the [`LAMMPS_POTENTIALS`{.docutils .literal .notranslate}]{.pre} environment variable. This allows potential files to reside in a common location instead of having to copy them around for simulations.

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    fp = force->open_potential(filename);
    fp = fopen(filename, "r");
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    fp = utils::open_potential(filename, lmp);
:::
::::
::::::::

:::::::: {#use-symbolic-atom-and-atomvec-constants-instead-of-numerical-values .section}
## [4.10.7. ]{.section-number}Use symbolic Atom and AtomVec constants instead of numerical values[](#use-symbolic-atom-and-atomvec-constants-instead-of-numerical-values "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 18Sep2020.]{.versionmodified .changed}
:::

Properties in LAMMPS that were represented by integer values (0, 1, 2, 3) to indicate settings in the [`Atom`{.docutils .literal .notranslate}]{.pre} and [`AtomVec`{.docutils .literal .notranslate}]{.pre} classes (or classes derived from it) (and its derived classes) have been converted to use scoped enumerators instead.

+-------------------+-------+-------------------+-------+-------------------+-------+
| Symbolic Constant | Value | Symbolic Constant | Value | Symbolic Constant | Value |
+===================+=======+===================+=======+===================+=======+
| Atom::GROW        | 0     | Atom::ATOMIC      | 0     | Atom::MAP_NONE    | 0     |
+-------------------+-------+-------------------+-------+-------------------+-------+
| Atom::RESTART     | 1     | Atom::MOLECULAR   | 1     | Atom::MAP_ARRAY   | 1     |
+-------------------+-------+-------------------+-------+-------------------+-------+
| Atom::BORDER      | 2     | Atom::TEMPLATE    | 2     | Atom::MAP_HASH    | 2     |
+-------------------+-------+-------------------+-------+-------------------+-------+
| AtomVec::PER_ATOM | 0     | AtomVec::PER_TYPE | 1     | Atom::MAP_YES     | 3     |
+-------------------+-------+-------------------+-------+-------------------+-------+

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    molecular = 0;
    mass_type = 1;
    if (atom->molecular == 2)
    if (atom->map_style == 2)
    atom->add_callback(0);
    atom->delete_callback(id,1);
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    molecular = Atom::ATOMIC;
    mass_type = AtomVec::PER_TYPE;
    if (atom->molecular == Atom::TEMPLATE)
    if (atom->map_style == Atom::MAP_HASH)
    atom->add_callback(Atom::GROW);
    atom->delete_callback(id,Atom::RESTART);
:::
::::
::::::::

:::::::: {#simplify-customized-error-messages .section}
## [4.10.8. ]{.section-number}Simplify customized error messages[](#simplify-customized-error-messages "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 14May2021.]{.versionmodified .changed}
:::

Aided by features of the bundled {fmt} library, error messages now can have a variable number of arguments and the string will be interpreted as a {fmt} style format string so that error messages can be easily customized without having to use temporary buffers and [`sprintf()`{.docutils .literal .notranslate}]{.pre}. Example:

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    if (fptr == NULL) {
      char str[128];
      sprintf(str,"Cannot open AEAM potential file %s",filename);
      error->one(FLERR,str);
    }
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    if (fptr == nullptr)
      error->one(FLERR, "Cannot open AEAM potential file {}: {}", filename, utils::getsyserror());
:::
::::
::::::::

:::::::: {#use-of-override-instead-of-virtual .section}
## [4.10.9. ]{.section-number}Use of "override" instead of "virtual"[](#use-of-override-instead-of-virtual "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 17Feb2022.]{.versionmodified .changed}
:::

Since LAMMPS requires C++17, we switched to use the "override" keyword instead of "virtual" to indicate polymorphism in derived classes. This allows the C++ compiler to better detect inconsistencies when an override is intended or not. Please note that "override" has to be added to **all** polymorph functions in derived classes and "virtual" *only* to the function in the base class (or the destructor). Here is an example from the [`FixWallReflect`{.docutils .literal .notranslate}]{.pre} class:

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    FixWallReflect(class LAMMPS *, int, char **);
    virtual ~FixWallReflect();
    int setmask();
    void init();
    void post_integrate();
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    FixWallReflect(class LAMMPS *, int, char **);
    ~FixWallReflect() override;
    int setmask() override;
    void init() override;
    void post_integrate() override;
:::
::::

This change set will neither cause a compilation failure, nor will it change functionality, but if you plan to submit the updated code for inclusion into the LAMMPS distribution, it will be requested for achieve a consistent [[programming style]{.doc}]Modify_style.md){.reference .internal}.
::::::::

:::::::: {#simplified-function-names-for-forward-and-reverse-communication .section}
## [4.10.10. ]{.section-number}Simplified function names for forward and reverse communication[](#simplified-function-names-for-forward-and-reverse-communication "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 24Mar2022.]{.versionmodified .changed}
:::

Rather than using the function name to distinguish between the different forward and reverse communication functions for styles, LAMMPS now uses the type of the "this" pointer argument.

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    comm->forward_comm_pair(this);
    comm->forward_comm_fix(this);
    comm->forward_comm_compute(this);
    comm->forward_comm_dump(this);
    comm->reverse_comm_pair(this);
    comm->reverse_comm_fix(this);
    comm->reverse_comm_compute(this);
    comm->reverse_comm_dump(this);
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    comm->forward_comm(this);
    comm->reverse_comm(this);
:::
::::

This change is **required** or else the code will not compile.
::::::::

:::::::: {#simplified-and-more-compact-neighbor-list-requests .section}
## [4.10.11. ]{.section-number}Simplified and more compact neighbor list requests[](#simplified-and-more-compact-neighbor-list-requests "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 24Mar2022.]{.versionmodified .changed}
:::

This change set reduces the amount of code required to request a neighbor list. It enforces consistency and no longer requires to change internal data of the request. More information on neighbor list requests can be [[found here]{.doc}]Developer_notes.md){.reference .internal}. Example from the [`ComputeRDF`{.docutils .literal .notranslate}]{.pre} class:

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    int irequest = neighbor->request(this,instance_me);
    neighbor->requests[irequest]->pair = 0;
    neighbor->requests[irequest]->compute = 1;
    neighbor->requests[irequest]->occasional = 1;
    if (cutflag) {
      neighbor->requests[irequest]->cut = 1;
      neighbor->requests[irequest]->cutoff = mycutneigh;
    }
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    auto req = neighbor->add_request(this, NeighConst::REQ_OCCASIONAL);
    if (cutflag) req->set_cutoff(mycutneigh);
:::
::::

Public access to the [`NeighRequest`{.docutils .literal .notranslate}]{.pre} class data members has been removed so this update is **required** to avoid compilation failure.
::::::::

:::::::::::: {#split-of-fix-store-into-fix-store-global-and-fix-store-peratom .section}
## [4.10.12. ]{.section-number}Split of fix STORE into fix STORE/GLOBAL and fix STORE/PERATOM[](#split-of-fix-store-into-fix-store-global-and-fix-store-peratom "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 15Sep2022.]{.versionmodified .changed}
:::

This change splits the GLOBAL and PERATOM modes of fix STORE into two separate fixes STORE/GLOBAL and STORE/PERATOM. There was very little shared code between the two fix STORE modes and the two different code paths had to be prefixed with if statements. Furthermore, some flags were used differently in the two modes leading to confusion. Splitting the code into two fix styles, makes it more easily maintainable. Since these are internal fixes, there is no user visible change.

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "fix_store.h"

    FixStore *fix = dynamic_cast<FixStore *>(
       modify->add_fix(fmt::format("{} {} STORE peratom 1 13",id_pole,group->names[0]));

    FixStore *fix = dynamic_cast<FixStore *>(modify->get_fix_by_id(id_pole));
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "fix_store_peratom.h"

    FixStorePeratom *fix = dynamic_cast<FixStorePeratom *>(
       modify->add_fix(fmt::format("{} {} STORE/PERATOM 1 13",id_pole,group->names[0]));

    FixStorePeratom *fix = dynamic_cast<FixStorePeratom *>(modify->get_fix_by_id(id_pole));
:::
::::

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "fix_store.h"

    FixStore *fix = dynamic_cast<FixStore *>(
       modify->add_fix(fmt::format("{} {} STORE global 1 1",id_fix,group->names[igroup]));

    FixStore *fix = dynamic_cast<FixStore *>(modify->get_fix_by_id(id_fix));
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "fix_store_global.h"

    FixStoreGlobal *fix = dynamic_cast<FixStoreGlobal *>(
       modify->add_fix(fmt::format("{} {} STORE/GLOBAL 1 1",id_fix,group->names[igroup]));

    FixStoreGlobal *fix = dynamic_cast<FixStoreGlobal *>(modify->get_fix_by_id(id_fix));
:::
::::

This change is **required** or else the code will not compile.
::::::::::::

:::: {#rename-of-fix-store-peratom-to-fix-store-atom-and-change-of-arguments .section}
## [4.10.13. ]{.section-number}Rename of fix STORE/PERATOM to fix STORE/ATOM and change of arguments[](#rename-of-fix-store-peratom-to-fix-store-atom-and-change-of-arguments "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 28Mar2023.]{.versionmodified .changed}
:::

The available functionality of the internal fix to store per-atom properties was expanded to enable storing data with ghost atoms and to support binary restart files. With those changes, the fix was renamed to fix STORE/ATOM and the number and order of (required) arguments has changed.

Old syntax: [`ID`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`group-ID`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`STORE/PERATOM`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`rflag`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`n1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`n2`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[n3]`{.docutils .literal .notranslate}]{.pre}

- *rflag* = 0/1, *no*/*yes* store per-atom values in restart file

- [\\(n1 = 1, n2 = 1, \\mathrm{no}\\;n3 \\to\\)]{.math .notranslate .nohighlight} per-atom vector, single value per atom

- [\\(n1 = 1, n2 \> 1, \\mathrm{no}\\;n3 \\to\\)]{.math .notranslate .nohighlight} per-atom array, *n2* values per atom

- [\\(n1 = 1, n2 \> 0, n3 \> 0 \\to\\)]{.math .notranslate .nohighlight} per-atom tensor, *n2* x *n3* values per atom

New syntax: [`ID`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`group-ID`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`STORE/ATOM`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`n1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`n2`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gflag`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`rflag`{.docutils .literal .notranslate}]{.pre}

- [\\(n1 = 1, n2 = 0 \\to\\)]{.math .notranslate .nohighlight} per-atom vector, single value per atom

- [\\(n1 \> 1, n2 = 0 \\to\\)]{.math .notranslate .nohighlight} per-atom array, *n1* values per atom

- [\\(n1 \> 0, n2 \> 0 \\to\\)]{.math .notranslate .nohighlight} per-atom tensor, *n1* x *n2* values per atom

- *gflag* = 0/1, *no*/*yes* communicate per-atom values with ghost atoms

- *rflag* = 0/1, *no*/*yes* store per-atom values in restart file

Since this is an internal fix, there is no user visible change.
::::

:::::::: {#use-output-get-dump-by-id-instead-of-output-find-dump .section}
## [4.10.14. ]{.section-number}Use Output::get_dump_by_id() instead of Output::find_dump()[](#use-output-get-dump-by-id-instead-of-output-find-dump "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 15Sep2022.]{.versionmodified .changed}
:::

The accessor function to individual dump style instances has been changed from [`Output::find_dump()`{.docutils .literal .notranslate}]{.pre} returning the index of the dump instance in the list of dumps to [`Output::get_dump_by_id()`{.docutils .literal .notranslate}]{.pre} returning a pointer to the dump directly. Example:

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    int idump = output->find_dump(arg[iarg+1]);
    if (idump < 0)
      error->all(FLERR,"Dump ID in hyper command does not exist");
    memory->grow(dumplist,ndump+1,"hyper:dumplist");
    dumplist[ndump++] = idump;

    [...]

    if (dumpflag)
      for (int idump = 0; idump < ndump; idump++)
        output->dump[dumplist[idump]]->write();
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    auto idump = output->get_dump_by_id(arg[iarg+1]);
    if (!idump) error->all(FLERR,"Dump ID {} in hyper command does not exist", arg[iarg+1]);
    dumplist.emplace_back(idump);

    [...]

    if (dumpflag) for (auto idump : dumplist) idump->write();
:::
::::

This change is **required** or else the code will not compile.
::::::::

:::: {#refactored-grid-communication-using-grid3d-grid2d-classes-instead-of-gridcomm .section}
## [4.10.15. ]{.section-number}Refactored grid communication using Grid3d/Grid2d classes instead of GridComm[](#refactored-grid-communication-using-grid3d-grid2d-classes-instead-of-gridcomm "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 22Dec2022.]{.versionmodified .changed}
:::

The [`GridComm`{.docutils .literal .notranslate}]{.pre} class was for creating and communicating distributed grids was replaced by the [`Grid3d`{.docutils .literal .notranslate}]{.pre} class with added functionality. A [`Grid2d`{.docutils .literal .notranslate}]{.pre} class was also added for additional flexibility.

The new functionality and commands using the two grid classes are discussed on the following documentation pages:

- [[Using distributed grids]{.doc}]Howto_grid.md){.reference .internal}

- [[Use of distributed grids within style classes]{.doc}]Developer_grid.md){.reference .internal}

If you have custom LAMMPS code, which uses the GridComm class, here are some notes on how to adapt it for using the Grid3d class.

1.  The constructor has changed to allow the [`Grid3d`{.docutils .literal .notranslate}]{.pre} / [`Grid2d`{.docutils .literal .notranslate}]{.pre} classes to partition the global grid across processors, both for owned and ghost grid cells. Previously any class which called [`GridComm`{.docutils .literal .notranslate}]{.pre} performed the partitioning itself and that information was passed in the [`GridComm::GridComm()`{.docutils .literal .notranslate}]{.pre} constructor. There are several "set" functions which can be called to alter how [`Grid3d`{.docutils .literal .notranslate}]{.pre} / [`Grid2d`{.docutils .literal .notranslate}]{.pre} perform the partitioning. They should be sufficient for most use cases of the grid classes.

2.  The partitioning is triggered by the [`setup_grid()`{.docutils .literal .notranslate}]{.pre} method.

3.  The [`setup()`{.docutils .literal .notranslate}]{.pre} method of the [`GridComm`{.docutils .literal .notranslate}]{.pre} class has been replaced by the [`setup_comm()`{.docutils .literal .notranslate}]{.pre} method in the new grid classes. The syntax for the [`forward_comm()`{.docutils .literal .notranslate}]{.pre} and [`reverse_comm()`{.docutils .literal .notranslate}]{.pre} methods is slightly altered as is the syntax of the associated pack/unpack callback methods. But the functionality of these operations is the same as before.

4.  The new [`Grid3d`{.docutils .literal .notranslate}]{.pre} / [`Grid2d`{.docutils .literal .notranslate}]{.pre} classes have additional functionality for dynamic load-balancing of grids and their associated data across processors. This did not exist in the [`GridComm`{.docutils .literal .notranslate}]{.pre} class.

This and more is explained in detail on the [[Use of distributed grids within style classes]{.doc}]Developer_grid.md){.reference .internal} page. The following LAMMPS source files can be used as illustrative examples for how the new grid classes are used by computes, fixes, and various KSpace solvers which use distributed FFT grids:

- [`src/fix_ave_grid.cpp`{.docutils .literal .notranslate}]{.pre}

- [`src/compute_property_grid.cpp`{.docutils .literal .notranslate}]{.pre}

- [`src/EXTRA-FIX/fix_ttm_grid.cpp`{.docutils .literal .notranslate}]{.pre}

- [`src/KSPACE/pppm.cpp`{.docutils .literal .notranslate}]{.pre}

This change is **required** or else the code will not compile.
::::

:::::::: {#flerr-as-first-argument-to-minimum-image-functions-in-domain-class .section}
## [4.10.16. ]{.section-number}FLERR as first argument to minimum image functions in Domain class[](#flerr-as-first-argument-to-minimum-image-functions-in-domain-class "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 12Jun2025.]{.versionmodified .changed}
:::

The [`Domain::minimum_image()`{.docutils .literal .notranslate}]{.pre} and [`Domain::minimum_image_big()`{.docutils .literal .notranslate}]{.pre} functions were changed to take the [`FLERR`{.docutils .literal .notranslate}]{.pre} macros as first argument. This way the error message indicates *where* the function was called instead of pointing to the implementation of the function. Example:

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
    double delx1 = x[i1][0] - x[i2][0];
    double dely1 = x[i1][1] - x[i2][1];
    double delz1 = x[i1][2] - x[i2][2];
    domain->minimum_image(delx1, dely1, delz1);
    double r1 = sqrt(delx1 * delx1 + dely1 * dely1 + delz1 * delz1);

    double delx2 = x[i3][0] - x[i2][0];
    double dely2 = x[i3][1] - x[i2][1];
    double delz2 = x[i3][2] - x[i2][2];
    domain->minimum_image_big(delx2, dely2, delz2);
    double r2 = sqrt(delx2 * delx2 + dely2 * dely2 + delz2 * delz2);
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    double delx1 = x[i1][0] - x[i2][0];
    double dely1 = x[i1][1] - x[i2][1];
    double delz1 = x[i1][2] - x[i2][2];
    domain->minimum_image(FLERR, delx1, dely1, delz1);
    double r1 = sqrt(delx1 * delx1 + dely1 * dely1 + delz1 * delz1);

    double delx2 = x[i3][0] - x[i2][0];
    double dely2 = x[i3][1] - x[i2][1];
    double delz2 = x[i3][2] - x[i2][2];
    domain->minimum_image_big(FLERR, delx2, dely2, delz2);
    double r2 = sqrt(delx2 * delx2 + dely2 * dely2 + delz2 * delz2);
:::
::::

This change is **required** or else the code will not compile.
::::::::

:::::::: {#use-utils-logmesg-instead-of-error-warning .section}
## [4.10.17. ]{.section-number}Use utils::logmesg() instead of error-\>warning()[](#use-utils-logmesg-instead-of-error-warning "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 22Jul2025.]{.versionmodified .changed}
:::

The [`Error::message()`{.docutils .literal .notranslate}]{.pre} method has been removed since its functionality has been superseded by the [[`utils::logmesg()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4IDpEN9LAMMPS_NS5utils7logmesgEvP6LAMMPSRKNSt6stringEDpRR4Args "LAMMPS_NS::utils::logmesg"){.reference .internal} function.

Old:

:::: {.highlight-c++ .notranslate}
::: highlight
     if (comm->me == 0) {
       error->message(FLERR, "INFO: About to read data file: {}", filename);
    }
:::
::::

New:

:::: {.highlight-c++ .notranslate}
::: highlight
    if (comm->me == 0) utils::logmesg(lmp, "INFO: About to read data file: {}\n", filename);
:::
::::

This change is **required** or else the code will not compile.
::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

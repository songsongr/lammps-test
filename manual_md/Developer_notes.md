:::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::: {#notes-for-developers-and-code-maintainers .section}
# [4.9. ]{.section-number}Notes for developers and code maintainers[](#notes-for-developers-and-code-maintainers "Link to this heading"){.headerlink}

This section documents how some of the code functionality within LAMMPS works at a conceptual level. Comments on code in source files typically document what a variable stores, what a small section of code does, or what a function does and its input/outputs. The topics on this page are intended to document code functionality at a higher level.

Available notes

- [Reading and parsing of text and text files](#reading-and-parsing-of-text-and-text-files){#id3 .reference .internal}

- [Requesting and accessing neighbor lists](#requesting-and-accessing-neighbor-lists){#id4 .reference .internal}

- [Errors, warnings, and informational messages](#errors-warnings-and-informational-messages){#id5 .reference .internal}

- [Choosing between a custom atom style, fix property/atom, and fix STORE/ATOM](#choosing-between-a-custom-atom-style-fix-property-atom-and-fix-store-atom){#id6 .reference .internal}

- [Fix contributions to instantaneous energy, virial, and cumulative energy](#fix-contributions-to-instantaneous-energy-virial-and-cumulative-energy){#id7 .reference .internal}

- [KSpace PPPM FFT grids](#kspace-pppm-fft-grids){#id8 .reference .internal}

------------------------------------------------------------------------

::: {#reading-and-parsing-of-text-and-text-files .section}
## [[4.9.1. ]{.section-number}Reading and parsing of text and text files](#id3){.toc-backref role="doc-backlink"}[](#reading-and-parsing-of-text-and-text-files "Link to this heading"){.headerlink}

Classes in LAMMPS frequently need to read in additional data from a file, e.g. potential parameters from a potential file for manybody potentials. LAMMPS provides several custom classes and convenience functions to simplify the process. They offer the following benefits:

- better code reuse and fewer lines of code needed to implement reading and parsing data from a file

- better detection of format errors, incompatible data, and better error messages

- exit with an error message instead of silently converting only part of the text to a number or returning a 0 on unrecognized text and thus reading incorrect values

- re-entrant code through avoiding global static variables (as used by [`strtok()`{.docutils .literal .notranslate}]{.pre})

- transparent support for translating unsupported UTF-8 characters to their ASCII equivalents (the text-to-value conversion functions **only** accept ASCII characters)

In most cases (e.g. potential files) the same data is needed on all MPI ranks. Then it is best to do the reading and parsing only on MPI rank 0, and communicate the data later with one or more [`MPI_Bcast()`{.docutils .literal .notranslate}]{.pre} calls. For reading generic text and potential parameter files the custom classes [[`TextFileReader`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS14TextFileReaderE "LAMMPS_NS::TextFileReader"){.reference .internal} and [[`PotentialFileReader`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS19PotentialFileReaderE "LAMMPS_NS::PotentialFileReader"){.reference .internal} are available. They allow reading the file as individual lines for which they can return a tokenizer class (see below) for parsing the line. Or they can return blocks of numbers as a vector directly. The documentation on [[File reader classes]{.std .std-ref}]Developer_utils.md#file-reader-classes){.reference .internal} contains an example for a typical case.

When reading per-atom data, the data on each line of the file usually needs to include an atom ID so it can be associated with a particular atom. In that case the data can be read in multi-line chunks and broadcast to all MPI ranks with [[`utils::read_lines_from_file()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils20read_lines_from_fileEP4FILEiiPci8MPI_Comm "LAMMPS_NS::utils::read_lines_from_file"){.reference .internal}. Those chunks are then split into lines, parsed, and applied only to atoms the MPI rank "owns".

For splitting a string (incrementally) into words and optionally converting those to numbers, the [[`Tokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS9TokenizerE "LAMMPS_NS::Tokenizer"){.reference .internal} and [[`ValueTokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS14ValueTokenizerE "LAMMPS_NS::ValueTokenizer"){.reference .internal} can be used. Those provide a superset of the functionality of [`strtok()`{.docutils .literal .notranslate}]{.pre} from the C-library and the latter also includes conversion to different types. Any errors while processing the string in those classes will result in an exception, which can be caught and the error processed as needed. Unlike the C-library functions [`atoi()`{.docutils .literal .notranslate}]{.pre}, [`atof()`{.docutils .literal .notranslate}]{.pre}, [`strtol()`{.docutils .literal .notranslate}]{.pre}, or [`strtod()`{.docutils .literal .notranslate}]{.pre} the conversion will check if the converted text is a valid integer or floating point number and will not silently return an unexpected or incorrect value. For example, [`atoi()`{.docutils .literal .notranslate}]{.pre} will return 12 when converting "12.5", while the ValueTokenizer class will throw an [[`InvalidIntegerException`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS23InvalidIntegerExceptionE "LAMMPS_NS::InvalidIntegerException"){.reference .internal} if [[`ValueTokenizer::next_int()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS14ValueTokenizer8next_intEv "LAMMPS_NS::ValueTokenizer::next_int"){.reference .internal} is called on the same string.
:::

::::::::::::::::::: {#requesting-and-accessing-neighbor-lists .section}
[]{#request-neighbor-list}

## [[4.9.2. ]{.section-number}Requesting and accessing neighbor lists](#id4){.toc-backref role="doc-backlink"}[](#requesting-and-accessing-neighbor-lists "Link to this heading"){.headerlink}

LAMMPS uses Verlet-style neighbor lists to avoid having to loop over *all* pairs of *all* atoms when computing pairwise properties with a cutoff (e.g. pairwise forces or radial distribution functions). There are three main algorithms that can be selected by the [[neighbor command]{.doc}]neighbor.md){.reference .internal}: bin (the default, uses binning to achieve linear scaling with system size), nsq (without binning, quadratic scaling), multi (with binning, optimized for varying cutoffs or polydisperse granular particles). In addition to how the neighbor lists are constructed a number of different variants of neighbor lists need to be created (e.g. "full" or "half") for different purposes and styles and those may be required in every time step ("perpetual") or on some steps ("occasional").

The neighbor list creation is managed by the [`Neighbor`{.docutils .literal .notranslate}]{.pre} class. Individual classes can obtain a neighbor list by creating an instance of a [`NeighRequest`{.docutils .literal .notranslate}]{.pre} class which is stored in a list inside the [`Neighbor`{.docutils .literal .notranslate}]{.pre} class. The [`Neighbor`{.docutils .literal .notranslate}]{.pre} class will then analyze the various requests and apply optimizations where neighbor lists that have the same settings will be created only once and then copied, or a list may be constructed by processing a neighbor list from a different request that is a superset of the requested list. The neighbor list build is then [[processed in parallel]{.doc}]Developer_par_neigh.md){.reference .internal}.

The most commonly required neighbor list is a so-called "half" neighbor list, where each pair of atoms is listed only once (except when the [[newton command setting]{.doc}]newton.md){.reference .internal} for pair is off; in that case pairs straddling subdomains or periodic boundaries will be listed twice). Thus these are the default settings when a neighbor list request is created in:

:::: {.highlight-c++ .notranslate}
::: highlight
    void Pair::init_style()
    {
      neighbor->add_request(this);
    }

    void Pair::init_list(int /*id*/, NeighList *ptr)
    {
      list = ptr;
    }
:::
::::

The [`this`{.docutils .literal .notranslate}]{.pre} pointer argument is required so the neighbor list code can access the requesting class instance to store the assembled neighbor list with that instance by calling its [`init_list()`{.docutils .literal .notranslate}]{.pre} member function. The optional second argument (omitted here) contains a bitmask of flags that determines the kind of neighbor list requested. The default value used here asks for a perpetual "half" neighbor list.

Non-default values of the second argument need to be used to adjust a neighbor list request to the specific needs of a style. The [[tersoff]{.doc}]pair_tersoff.md){.reference .internal} pair style, for example, needs a "full" neighbor list:

:::: {.highlight-c++ .notranslate}
::: highlight
    void PairTersoff::init_style()
    {
      // [...]
      neighbor->add_request(this, NeighConst::REQ_FULL);
    }
:::
::::

When a pair style supports r-RESPA time integration with different cutoff regions, the request flag may depend on the corresponding r-RESPA settings. Here is an example from pair style lj/cut:

:::: {.highlight-c++ .notranslate}
::: highlight
    void PairLJCut::init_style()
    {
      int list_style = NeighConst::REQ_DEFAULT;

      if (update->whichflag == 1 && utils::strmatch(update->integrate_style, "^respa")) {
        auto respa = (Respa *) update->integrate;
        if (respa->level_inner >= 0) list_style = NeighConst::REQ_RESPA_INOUT;
        if (respa->level_middle >= 0) list_style = NeighConst::REQ_RESPA_ALL;
      }
      neighbor->add_request(this, list_style);
      // [...]
    }
:::
::::

Granular pair styles need neighbor lists based on particle sizes and not cutoff and also may need to store data across timesteps ("history"). For example with:

:::: {.highlight-c++ .notranslate}
::: highlight
    if (use_history) neighbor->add_request(this, NeighConst::REQ_SIZE | NeighConst::REQ_HISTORY);
    else neighbor->add_request(this, NeighConst::REQ_SIZE);
:::
::::

In case a class would need to make multiple neighbor list requests with different settings, each request can set an id which is then used in the corresponding [`init_list()`{.docutils .literal .notranslate}]{.pre} function to assign it to the suitable pointer variable. This is done for example by the [[pair style meam]{.doc}]pair_meam.md){.reference .internal}:

:::: {.highlight-c++ .notranslate}
::: highlight
    void PairMEAM::init_style()
    {
    // [...]
      neighbor->add_request(this, NeighConst::REQ_FULL)->set_id(1);
      neighbor->add_request(this)->set_id(2);
    }
    void PairMEAM::init_list(int id, NeighList *ptr)
    {
      if (id == 1) listfull = ptr;
      else if (id == 2) listhalf = ptr;
    }
:::
::::

Fixes may require a neighbor list that is only build occasionally (or just once) and this can also be indicated by a flag. As an example here is the request from the [`FixPeriNeigh`{.docutils .literal .notranslate}]{.pre} class which is created internally by [[Peridynamics pair styles]{.doc}]pair_peri.md){.reference .internal}:

:::: {.highlight-c++ .notranslate}
::: highlight
    neighbor->add_request(this, NeighConst::REQ_FULL | NeighConst::REQ_OCCASIONAL);
:::
::::

It is also possible to request a neighbor list that uses a different cutoff than what is usually inferred from the pair style settings (largest cutoff of all pair styles plus neighbor list skin). The following is used in the [[compute rdf]{.doc}]compute_rdf.md){.reference .internal} command implementation:

:::: {.highlight-c++ .notranslate}
::: highlight
    if (cutflag)
      neighbor->add_request(this, NeighConst::REQ_OCCASIONAL)->set_cutoff(mycutneigh);
    else
      neighbor->add_request(this, NeighConst::REQ_OCCASIONAL);
:::
::::

The neighbor list request function has a slightly different set of arguments when created by a command style. In this case the neighbor list is *always* an occasional neighbor list, so that flag is not needed. However for printing the neighbor list summary the name of the requesting command should be set. Below is the request from the [[delete atoms]{.doc}]delete_atoms.md){.reference .internal} command:

:::: {.highlight-c++ .notranslate}
::: highlight
    neighbor->add_request(this, "delete_atoms", NeighConst::REQ_FULL);
:::
::::
:::::::::::::::::::

::::::::: {#errors-warnings-and-informational-messages .section}
[]{#error-messages}

## [[4.9.3. ]{.section-number}Errors, warnings, and informational messages](#id5){.toc-backref role="doc-backlink"}[](#errors-warnings-and-informational-messages "Link to this heading"){.headerlink}

LAMMPS has specialized functionality to handle errors (which should terminate LAMMPS), warning messages (which should indicate possible problems *without* terminating LAMMPS), and informational text for messages about the progress and chosen settings. We *strongly* encourage using these facilities and to *stay away* from using [`printf()`{.docutils .literal .notranslate}]{.pre} or [`fprintf()`{.docutils .literal .notranslate}]{.pre} or [`std::cout`{.docutils .literal .notranslate}]{.pre} or [`std::cerr`{.docutils .literal .notranslate}]{.pre} and calling [`MPI_Abort()`{.docutils .literal .notranslate}]{.pre} or [`exit()`{.docutils .literal .notranslate}]{.pre} directly. Warnings and informational messages should be printed only on MPI rank 0 to avoid flooding the output when running in parallel with many MPI processes.

**Errors**

When LAMMPS encounters an error, for example a syntax error in the input, then a suitable error message should be printed giving a brief, one line remark about the reason and then call either [`Error::all()`{.docutils .literal .notranslate}]{.pre} or [`Error::one()`{.docutils .literal .notranslate}]{.pre}. [`Error::all()`{.docutils .literal .notranslate}]{.pre} must be called when the failing code path is executed by *all* MPI processes and the error condition will appear for *all* MPI processes the same. If desired, each MPI process may set a flag to either 0 or 1 and then MPI_Allreduce() searching for the maximum can be used to determine if there was an error on *any* of the MPI processes and make this information available to *all*. [`Error::one()`{.docutils .literal .notranslate}]{.pre} in contrast needs to be called when only one or a few MPI processes execute the code path or can have the error condition. [`Error::all()`{.docutils .literal .notranslate}]{.pre} is generally the preferred option.

Calling these functions does not abort LAMMPS directly, but rather throws either a [`LAMMPSException`{.docutils .literal .notranslate}]{.pre} (from [`Error::all()`{.docutils .literal .notranslate}]{.pre}) or a [`LAMMPSAbortException`{.docutils .literal .notranslate}]{.pre} (from [`Error::one()`{.docutils .literal .notranslate}]{.pre}). These exceptions are caught by the LAMMPS [`main()`{.docutils .literal .notranslate}]{.pre} program and then handled accordingly. The reason for this approach is to support applications, especially graphical applications like [[LAMMPS-GUI]{.std .std-ref}]Tools.md#lammps-gui){.reference .internal}, that are linked to the LAMMPS library and have a mechanism to avoid that an error in LAMMPS terminates the application. By catching the exceptions, the application can delete the failing LAMMPS class instance and create a new one to try again. In a similar fashion, the [[LAMMPS Python module]{.doc}]Python_module.md){.reference .internal} checks for this and then re-throws a corresponding Python exception, which in turn can be caught by the calling Python code.

There are multiple "signatures" that can be called:

- [`Error::all(FLERR,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"Error`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`message")`{.docutils .literal .notranslate}]{.pre}: this will abort LAMMPS with the error message "Error message", followed by the last line of input that was read and processed before the error condition happened.

- [`Error::all(FLERR,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Error::NOLASTLINE,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"Error`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`message")`{.docutils .literal .notranslate}]{.pre}: this is the same as before but without the last line of input. This is preferred for errors that would happen *during* a [[run]{.doc}]run.md){.reference .internal} or [[minimization]{.doc}]minimize.md){.reference .internal}, since the last line would be showing the "run" or "minimize" command yet those are unrelated to the command *causing* the error.

- [`Error::all(FLERR,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`idx,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"Error`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`message")`{.docutils .literal .notranslate}]{.pre}: this is for argument parsing where "idx" is the index (starting at 0) of the argument for a LAMMPS command that is causing the failure (use [`Error::COMMAND`{.docutils .literal .notranslate}]{.pre} for the command itself). For index 0, i.e. the first command argument, you need to use the constant [`Error::ARGZERO`{.docutils .literal .notranslate}]{.pre} to work around the inability of some compilers to disambiguate between a NULL pointer and an integer constant 0, even with an added type cast. The output may also include the last input line *before* and *after* substituting variables, if they differ. A textual indicator is pointing to the specific word that failed. Using the constant [`Error::NOPOINTER`{.docutils .literal .notranslate}]{.pre} in place of the *idx* argument will suppress the marker and then the behavior is like the *idx* argument is not provided.

FLERR is a macro containing the filename and line where the Error class is called and that information is appended to the error message. This allows to quickly find the relevant source code causing the error. For all three signatures, the single string "Error message" may be replaced with a format string using '{}' placeholders and followed by a variable number of arguments, one for each placeholder. This format string and the arguments are then handed for formatting to the [{fmt} library](https://fmt.dev){.reference .external} (which is bundled with LAMMPS) or the [C++ format library](https://cppreference.com/w/cpp/utility/format.html){.reference .external} (for C++20 and later) and thus allow processing similar to the "format()" functionality in Python.

::: {.admonition .note}
Note

Commands that accept wildcard arguments, for example [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}, use [[`utils::expand_args()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils11expand_argsEPKciiPPciRPPcP6LAMMPSPPi "LAMMPS_NS::utils::expand_args"){.reference .internal} to convert the wildcards into a list of explicit arguments. This function accepts a pointer address as an optional argument, which will be set to a map to the original arguments from the expanded argument indices. Please see the corresponding source code for details on how to apply this map in error messages.
:::

For complex errors, that can have multiple causes and which cannot be explained in a single line, you can append to the error message, the string created by [[`utils::errorurl()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS5utils8errorurlEi "LAMMPS_NS::utils::errorurl"){.reference .internal}, which then provides a URL pointing to a paragraph of the [[Errors and warnings details]{.doc}]Errors_details.md){.reference .internal} that corresponds to the number provided. Example:

:::: {.highlight-c++ .notranslate}
::: highlight
    error->all(FLERR, "Unknown identifier in data file: {}{}", keyword, utils::errorurl(1));
:::
::::

This will output something like this:

:::: {.highlight-none .notranslate}
::: highlight
    ERROR: Unknown identifier in data file: Massess
    For more information see https://docs.lammps.org/err0001 (src/read_data.cpp:1482)
    Last input line: read_data       data.peptide
:::
::::

Where the URL points to the first paragraph with explanations on the [[Errors and warnings details]{.doc}]Errors_details.md){.reference .internal} page in the manual.

**Warnings**

To print warnings, the [`Errors::warning()`{.docutils .literal .notranslate}]{.pre} function should be used. It also requires the FLERR macros as first argument to easily identify the location of the warning in the source code. Same as with the error functions above, the function has two variants: one just taking a single string as final argument and a second that uses the [{fmt} library](https://fmt.dev){.reference .external} to make it similar to, say, [`fprintf()`{.docutils .literal .notranslate}]{.pre}. One motivation to use this function is that it will output warnings with always the same capitalization of the leading "WARNING" string. A second is that it has a built in rate limiter. After a given number (by default 100), that can be set via the [[thermo_modify command]{.doc}]thermo_modify.md){.reference .internal} no more warnings are printed. Also, warnings are written consistently to both screen and logfile or not, depending on the settings for [[screen]{.std .std-ref}]Run_options.md#screen){.reference .internal} or [[logfile]{.doc}]log.md){.reference .internal} output.

::: {.admonition .note}
Note

Unlike [`Error::all()`{.docutils .literal .notranslate}]{.pre}, the warning function will produce output on *every* MPI process, so it typically would be prefixed with an if statement testing for [`comm->me`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`==`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0`{.docutils .literal .notranslate}]{.pre}, i.e. limiting output to MPI rank 0.
:::

**Informational messages**

Finally, for informational message LAMMPS has the [[`utils::logmesg()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`convenience`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`function`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4IDpEN9LAMMPS_NS5utils7logmesgEvP6LAMMPSRKNSt6stringEDpRR4Args "LAMMPS_NS::utils::logmesg"){.reference .internal}. It also uses the [{fmt} library](https://fmt.dev){.reference .external} to support using a format string followed by a matching number of arguments. It will output the resulting formatted text to both, the screen and the logfile and will honor the corresponding settings about whether this output is active and to which file it should be send. Same as for [`Error::warning()`{.docutils .literal .notranslate}]{.pre}, it would produce output for every MPI process and thus should usually be called only on MPI rank 0 to avoid flooding the output when running with many parallel processes.
:::::::::

::: {#choosing-between-a-custom-atom-style-fix-property-atom-and-fix-store-atom .section}
## [[4.9.4. ]{.section-number}Choosing between a custom atom style, fix property/atom, and fix STORE/ATOM](#id6){.toc-backref role="doc-backlink"}[](#choosing-between-a-custom-atom-style-fix-property-atom-and-fix-store-atom "Link to this heading"){.headerlink}

There are multiple ways to manage per-atom data within LAMMPS. Often the per-atom storage is only used locally and managed by the class that uses it. If the data has to persist between multiple time steps and migrate with atoms when they move from sub-domain to sub-domain or across periodic boundaries, then using a custom atom style, or [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal}, or the internal fix STORE/ATOM are possible options.

- Using the atom style is usually the most programming effort and mostly needed when the per-atom data is an integral part of the model like a per-atom charge or diameter and thus should be part of the Atoms section of a [[data file]{.doc}]read_data.md){.reference .internal}.

- Fix property/atom is useful if the data is optional or should be entered by the user, or accessed as a (named) custom property. In this case the fix should be entered as part of the input (and not internally) which allows to enter and store its content with data files.

- Fix STORE/ATOM should be used when the data should be accessed internally only and thus the fix can be created internally.
:::

:::: {#fix-contributions-to-instantaneous-energy-virial-and-cumulative-energy .section}
## [[4.9.5. ]{.section-number}Fix contributions to instantaneous energy, virial, and cumulative energy](#id7){.toc-backref role="doc-backlink"}[](#fix-contributions-to-instantaneous-energy-virial-and-cumulative-energy "Link to this heading"){.headerlink}

Fixes can calculate contributions to the instantaneous energy and/or virial of the system, both in a global and peratom sense. Fixes that perform thermostatting or barostatting can calculate the cumulative energy they add to or subtract from the system, which is accessed by the *ecouple* and *econserve* thermodynamic keywords. This subsection explains how both work and what flags to set in a new fix to enable this functionality.

Let's start with thermostatting and barostatting fixes. Examples are the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} and [[fix npt]{.doc}]fix_nh.md){.reference .internal} commands. Here is what the fix needs to do:

- Set the variable *ecouple_flag* = 1 in the constructor. Also set *scalar_flag* = 1, *extscalar* = 1, and *global_freq* to a timestep increment which matches how often the fix is invoked.

- Implement a compute_scalar() method that returns the cumulative energy added or subtracted by the fix, e.g. by rescaling the velocity of atoms. The sign convention is that subtracted energy is positive, added energy is negative. This must be the total energy added to the entire system, i.e. an "extensive" quantity, not a per-atom energy. Cumulative means the summed energy since the fix was instantiated, even across multiple runs. This is because the energy is used by the *econserve* thermodynamic keyword to check that the fix is conserving the total energy of the system, i.e. potential energy + kinetic energy + coupling energy = a constant.

And here is how the code operates:

- The Modify class makes a list of all fixes that set *ecouple_flag* = 1.

- The [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command defines *ecouple* and *econserve* keywords.

- These keywords sum the energy contributions from all the *ecouple_flag* = 1 fixes by invoking the *energy_couple()* method in the Modify class, which calls the *compute_scalar()* method of each fix in the list.

------------------------------------------------------------------------

Next, here is how a fix contributes to the instantaneous energy and virial of the system. First, it sets any or all of these flags to a value of 1 in their constructor:

- *energy_global_flag* to contribute to global energy, example: [[fix indent]{.doc}]fix_indent.md){.reference .internal}

- *energy_peratom_flag* to contribute to peratom energy, [[fix cmap]{.doc}]fix_cmap.md){.reference .internal}

- *virial_global_flag* to contribute to global virial, example: [[fix wall]{.doc}]fix_wall.md){.reference .internal}

- *virial_peratom_flag* to contribute to peratom virial, example: [[fix wall]{.doc}]fix_wall.md){.reference .internal}

The fix must also do the following:

- For global energy, implement a compute_scalar() method that returns the energy added or subtracted on this timestep. Here the sign convention is that added energy is positive, subtracted energy is negative.

- For peratom energy, invoke the ev_init(eflag,vflag) function each time the fix is invoked, which initializes per-atom energy storage. The value of eflag may need to be stored from an earlier call to the fix during the same timestep. See how the [[fix cmap]{.doc}]fix_cmap.md){.reference .internal} command does this in src/MOLECULE/fix_cmap.cpp. When an energy for one or more atoms is calculated, invoke the ev_tally() function to tally the contribution to each atom. Both the ev_init() and ev_tally() methods are in the parent Fix class.

- For global and/or peratom virial, invoke the v_init(vflag) function each time the fix is invoked, which initializes virial storage. When forces on one or more atoms are calculated, invoke the v_tally() function to tally the contribution. Both the v_init() and v_tally() methods are in the parent Fix class. Note that there are several variants of v_tally(); choose the one appropriate to your fix.

::: {.admonition .note}
Note

The ev_init() and ev_tally() methods also account for global and peratom virial contributions. Thus you do not need to invoke the v_init() and v_tally() methods if the fix also calculates peratom energies.
:::

The fix must also specify whether (by default) to include or exclude these contributions to the global/peratom energy/virial of the system. For the fix to include the contributions, set either or both of these variables in the constructor:

- *thermo_energy* = 1, for global and peratom energy

- *thermo_virial* = 1, for global and peratom virial

Note that these variables are zeroed in fix.cpp. Thus if you don't set the variables, the contributions will be excluded (by default).

However, the user has ultimate control over whether to include or exclude the contributions of the fix via the [[fix modify]{.doc}]fix_modify.md){.reference .internal} command:

- fix modify *energy yes* to include global and peratom energy contributions

- fix modify *virial yes* to include global and peratom virial contributions

If the fix contributes to any of the global/peratom energy/virial values for the system, it should be explained on the fix doc page, along with the default values for the *energy yes/no* and *virial yes/no* settings of the [[fix modify]{.doc}]fix_modify.md){.reference .internal} command.

Finally, these 4 contributions are included in the output of 4 computes:

- global energy in [[compute pe]{.doc}]compute_pe.md){.reference .internal}

- peratom energy in [[compute pe/atom]{.doc}]compute_pe_atom.md){.reference .internal}

- global virial in [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}

- peratom virial in [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal}

These computes invoke a method of the Modify class to include contributions from fixes that have the corresponding flags set, e.g. *energy_peratom_flag* and *thermo_energy* for [[compute pe/atom]{.doc}]compute_pe_atom.md){.reference .internal}.

Note that each compute has an optional keyword to either include or exclude all contributions from fixes. Also note that [[compute pe]{.doc}]compute_pe.md){.reference .internal} and [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} are what is used (by default) by [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} to calculate values for its *pe* and *press* keywords.
::::

::::::::::::: {#kspace-pppm-fft-grids .section}
## [[4.9.6. ]{.section-number}KSpace PPPM FFT grids](#id8){.toc-backref role="doc-backlink"}[](#kspace-pppm-fft-grids "Link to this heading"){.headerlink}

The various [[KSpace PPPM]{.doc}]kspace_style.md){.reference .internal} styles in LAMMPS use FFTs to solve Poisson's equation. This subsection describes:

- how FFT grids are defined

- how they are decomposed across processors

- how they are indexed by each processor

- how particle charge and electric field values are mapped to/from the grid

An FFT grid cell is a 3d volume; grid points are corners of a grid cell and the code stores values assigned to grid points in vectors or 3d arrays. A global 3d FFT grid has points indexed 0 to N-1 inclusive in each dimension.

Each processor owns two subsets of the grid, each subset is brick-shaped. Depending on how it is used, these subsets are allocated as a 1d vector or 3d array. Either way, the ordering of values within contiguous memory x fastest, then y, z slowest.

For the [`3d`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`decomposition`{.docutils .literal .notranslate}]{.pre} of the grid, the global grid is partitioned into bricks that correspond to the subdomains of the simulation box that each processor owns. Often, this is a regular 3d array (Px by Py by Pz) of bricks, where P = number of processors = Px \* Py \* Pz. More generally it can be a tiled decomposition, where each processor owns a brick and the union of all the bricks is the global grid. Tiled decompositions are produced by load balancing with the RCB algorithm; see the [[balance rcb]{.doc}]balance.md){.reference .internal} command.

For the [`FFT`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`decompostion`{.docutils .literal .notranslate}]{.pre} of the grid, each processor owns a brick that spans the entire x dimension of the grid while the y and z dimensions are partitioned as a regular 2d array (P1 by P2), where P = P1 \* P2.

The following indices store the inclusive bounds of the brick a processor owns, within the global grid:

:::: {.highlight-none .notranslate}
::: highlight
    nFOO_in = 3d decomposition brick
    nFOO_fft = FFT decomposition brick
    nFOO_out = 3d decomposition brick + ghost cells
:::
::::

where [`FOO`{.docutils .literal .notranslate}]{.pre} corresponds to [`xlo,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`xhi,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`ylo,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`yhi,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`zlo,`{.docutils .literal .notranslate}]{.pre} or [`zhi`{.docutils .literal .notranslate}]{.pre}.

The [`in`{.docutils .literal .notranslate}]{.pre} and [`fft`{.docutils .literal .notranslate}]{.pre} indices are from 0 to N-1 inclusive in each dimension, where N is the grid size.

The [`out`{.docutils .literal .notranslate}]{.pre} indices index an array which stores the [`in`{.docutils .literal .notranslate}]{.pre} subset of the grid plus ghost cells that surround it. These indices can thus be \< 0 or \>= N.

The number of ghost cells a processor owns in each of the 6 directions is a function of:

:::: {.highlight-none .notranslate}
::: highlight
    neighbor skin distance (since atoms can move outside a proc subdomain)
    qdist = offset or charge from atom due to TIP4P fictitious charge
    order = mapping stencil size
    shift = factor used when order is an even number (see below)
:::
::::

Here is an explanation of how the PPPM variables [`order`{.docutils .literal .notranslate}]{.pre}, [`nlower`{.docutils .literal .notranslate}]{.pre} / [`nupper`{.docutils .literal .notranslate}]{.pre}, [`shift`{.docutils .literal .notranslate}]{.pre}, and [`OFFSET`{.docutils .literal .notranslate}]{.pre} work. They are the relevant variables that determine how atom charge is mapped to grid points and how field values are mapped from grid points to atoms:

:::: {.highlight-none .notranslate}
::: highlight
    order = # of nearby grid points in each dim that atom charge/field are mapped to/from
    nlower,nupper = extent of stencil around the grid point an atom is assigned to
    OFFSET = large integer added/subtracted when mapping to avoid int(-0.75) = 0 when -1 is the desired result
:::
::::

The particle_map() method assigns each atom to a grid point.

If order is even, say 4:

:::: {.highlight-none .notranslate}
::: highlight
    atom is assigned to grid point to its left (in each dim)
    shift = OFFSET
    nlower = -1, nupper = 2, which are offsets from assigned grid point
    window of mapping grid pts is thus 2 grid points to left of atom, 2 to right
:::
::::

If order is odd, say 5:

:::: {.highlight-none .notranslate}
::: highlight
    atom is assigned to left/right grid pt it is closest to (in each dim)
    shift = OFFSET + 0.5
    nlower = 2, nupper = 2
    if point is in left half of cell, then window of affected grid pts is 3 grid points to left of atom, 2 to right
    if point is in right half of cell, then window of affected grid pts is 2 grid points to left of atom, 3 to right
:::
::::

These settings apply to each dimension, so that if order = 5, an atom's charge is mapped to 125 grid points that surround the atom.
:::::::::::::
::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::

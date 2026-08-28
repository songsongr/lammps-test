::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#errors-and-warnings-details .section}
# [5.2. ]{.section-number}Errors and warnings details[](#errors-and-warnings-details "Link to this heading"){.headerlink}

Many errors and warnings that LAMMPS outputs are self-explanatory and thus straightforward to resolve. However, there are also cases where there is no single cause or simple explanation that can be provided in a short message printed by LAMMPS. Therefore, more detailed discussions of such scenarios are provided here; first on a more general level and then for specific errors. In the latter cases, LAMMPS will output a short message and then provide a URL that links to a specific section on this page.

------------------------------------------------------------------------

Individual paragraphs

- [General troubleshooting advice](#general-troubleshooting-advice){#id1 .reference .internal}

  - [Create a small test system](#create-a-small-test-system){#id2 .reference .internal}

  - [Visualize your trajectory](#visualize-your-trajectory){#id3 .reference .internal}

  - [Parallel versus serial](#parallel-versus-serial){#id4 .reference .internal}

  - [Segmentation Fault](#segmentation-fault){#id5 .reference .internal}

  - [Fast moving atoms](#fast-moving-atoms){#id6 .reference .internal}

  - [Ignoring lost atoms](#ignoring-lost-atoms){#id7 .reference .internal}

  - [Pressure, forces, positions becoming NaN or Inf](#pressure-forces-positions-becoming-nan-or-inf){#id8 .reference .internal}

  - [Communication cutoff](#communication-cutoff){#id9 .reference .internal}

  - [Neighbor list settings](#neighbor-list-settings){#id10 .reference .internal}

  - [Units](#units){#id11 .reference .internal}

  - [No error message printed](#no-error-message-printed){#id12 .reference .internal}

  - [Errors before or after the simulation box is created](#errors-before-or-after-the-simulation-box-is-created){#id13 .reference .internal}

  - [Illegal ... command](#illegal-command){#id14 .reference .internal}

- [Unknown identifier in data file](#unknown-identifier-in-data-file){#id15 .reference .internal}

- [Incorrect format in ... section of data file](#incorrect-format-in-section-of-data-file){#id16 .reference .internal}

- [Illegal variable command: expected X arguments but found Y](#illegal-variable-command-expected-x-arguments-but-found-y){#id17 .reference .internal}

- [Out of range atoms - cannot compute ...](#out-of-range-atoms-cannot-compute){#id18 .reference .internal}

- [Bond (or angle, dihedral, improper, cmap, or shake) atoms missing](#bond-or-angle-dihedral-improper-cmap-or-shake-atoms-missing){#id19 .reference .internal}

- [Non-numeric atom coords or pressure or box dimensions - simulation unstable](#non-numeric-atom-coords-or-pressure-or-box-dimensions-simulation-unstable){#id20 .reference .internal}

- [Fix used in ... not computed at compatible time](#fix-used-in-not-computed-at-compatible-time){#id21 .reference .internal}

- [Lost atoms ...](#lost-atoms){#id22 .reference .internal}

- [Too many neighbor bins](#too-many-neighbor-bins){#id23 .reference .internal}

- [Unrecognized ... style ...](#unrecognized-style){#id24 .reference .internal}

- [Energy or stress was not tallied by pair style](#energy-or-stress-was-not-tallied-by-pair-style){#id25 .reference .internal}

- [fmt::format_error](#fmt-format-error){#id26 .reference .internal}

- [Substitution for illegal variable](#substitution-for-illegal-variable){#id27 .reference .internal}

- [Bond atom missing in image check or box size check](#bond-atom-missing-in-image-check-or-box-size-check){#id28 .reference .internal}

- [Cannot use neighbor bins - box size \<\< cutoff](#cannot-use-neighbor-bins-box-size-cutoff){#id29 .reference .internal}

- [Did not assign all atoms correctly](#did-not-assign-all-atoms-correctly){#id30 .reference .internal}

- [Domain too large for neighbor bins](#domain-too-large-for-neighbor-bins){#id31 .reference .internal}

- [Step X: (h)bondchk failed](#step-x-h-bondchk-failed){#id32 .reference .internal}

- [Numeric index X is out of bounds](#numeric-index-x-is-out-of-bounds){#id33 .reference .internal}

- [Compute, fix, or variable vector or array is accessed out-of-range](#compute-fix-or-variable-vector-or-array-is-accessed-out-of-range){#id34 .reference .internal}

- [Incorrect args for pair coefficients (also bond/angle/dihedral/improper coefficients)](#incorrect-args-for-pair-coefficients-also-bond-angle-dihedral-improper-coefficients){#id35 .reference .internal}

- [Energy was not tallied on needed timestep (also virial, per-atom energy, per-atom virial)](#energy-was-not-tallied-on-needed-timestep-also-virial-per-atom-energy-per-atom-virial){#id36 .reference .internal}

- [Molecule auto special bond generation overflow](#molecule-auto-special-bond-generation-overflow){#id37 .reference .internal}

- [Molecule topology/atom exceeds system topology/atom](#molecule-topology-atom-exceeds-system-topology-atom){#id38 .reference .internal}

- [Molecule topology type exceeds system topology type](#molecule-topology-type-exceeds-system-topology-type){#id39 .reference .internal}

- [Molecule attributes do not match system attributes](#molecule-attributes-do-not-match-system-attributes){#id40 .reference .internal}

- [Inconsistent image flags](#inconsistent-image-flags){#id41 .reference .internal}

- [No fixes with time integration, atoms won't move](#no-fixes-with-time-integration-atoms-won-t-move){#id42 .reference .internal}

- [System is not charge neutral, net charge = ...](#system-is-not-charge-neutral-net-charge){#id43 .reference .internal}

- [Variable evaluation before simulation box is defined](#variable-evaluation-before-simulation-box-is-defined){#id44 .reference .internal}

- [Invalid thermo keyword 'X' in variable formula](#invalid-thermo-keyword-x-in-variable-formula){#id45 .reference .internal}

- [One or more atoms are time integrated more than once](#one-or-more-atoms-are-time-integrated-more-than-once){#id46 .reference .internal}

- [XXX command before simulation box is defined](#xxx-command-before-simulation-box-is-defined){#id47 .reference .internal}

- [XXX command after simulation box is defined](#xxx-command-after-simulation-box-is-defined){#id48 .reference .internal}

- [Error messages ending in 'Please contact the LAMMPS developers'](#error-messages-ending-in-please-contact-the-lammps-developers){#id49 .reference .internal}

- [Neighbor list overflow, boost neigh_modify one](#neighbor-list-overflow-boost-neigh-modify-one){#id50 .reference .internal}

- [Variable ...: Compute/Fix ... does not compute requested property](#variable-compute-fix-does-not-compute-requested-property){#id51 .reference .internal}

- [The ... style ... is no longer available](#the-style-is-no-longer-available){#id52 .reference .internal}

------------------------------------------------------------------------

:::::::::::::::: {#general-troubleshooting-advice .section}
## [[5.2.1. ]{.section-number}General troubleshooting advice](#id1){.toc-backref role="doc-backlink"}[](#general-troubleshooting-advice "Link to this heading"){.headerlink}

Below are suggestions that can help to understand the causes of problems with simulations leading to errors or unexpected results.

::: {#create-a-small-test-system .section}
[]{#hint01}

### [Create a small test system](#id2){.toc-backref role="doc-backlink"}[](#create-a-small-test-system "Link to this heading"){.headerlink}

Debugging problems often requires running a simulation many times with small modifications, thus it can be a huge time saver to first assemble a small test system input that has the same issue, but will take much less time until it triggers the error condition. Also, it will be easier to see what happens when visualizing the system or looking at output files.
:::

::: {#visualize-your-trajectory .section}
[]{#hint02}

### [Visualize your trajectory](#id3){.toc-backref role="doc-backlink"}[](#visualize-your-trajectory "Link to this heading"){.headerlink}

To better understand what is causing problems, it is often very useful to visualize the system close to the point of failure. It may be necessary to have LAMMPS output trajectory frames rather frequently. To avoid gigantic files, you can use [[dump_modify delay]{.doc}]dump_modify.md){.reference .internal} to delay output until the critical section is reached, and you can use a smaller test system (see above).
:::

::: {#parallel-versus-serial .section}
[]{#hint03}

### [Parallel versus serial](#id4){.toc-backref role="doc-backlink"}[](#parallel-versus-serial "Link to this heading"){.headerlink}

Issues where something is "lost" or "missing" often exhibit that issue *only* when running in parallel. That doesn't mean there is no problem when running in serial, only the symptoms are not triggering an error. This may be because there is no domain decomposition with just one processor and thus all atoms are accessible, or it may be because the problem will manifest faster with smaller subdomains. Correspondingly, errors may be triggered faster with more processors and thus smaller sub-domains.
:::

::: {#segmentation-fault .section}
[]{#hint04}

### [Segmentation Fault](#id5){.toc-backref role="doc-backlink"}[](#segmentation-fault "Link to this heading"){.headerlink}

A segmentation fault is an error reported by the **operating system** and not LAMMPS itself. It happens when a process tries to access a memory address that is not available. This can have **many** reasons: memory has not been allocated, a memory buffer is not large enough, a memory address is computed from an incorrect index, a memory buffer is used after it has been freed, some general memory corruption. When investigating a segmentation fault (aka segfault), it is important to determine which process is causing it; it may not always be LAMMPS. For example, some MPI library implementations report a segmentation fault from their "mpirun" or "mpiexec" command when the application has been terminated unexpectedly.

While a segmentation fault is likely an indication of a bug in LAMMPS, it need not always be; it can also be the consequence of too aggressive simulation settings. For time critical code paths, LAMMPS will assume the user has chosen the settings carefully and will not make any checks to avoid performance penalties.

A crucial step in resolving a segmentation fault is to identify the exact location in the code where it happens. Please see [[Debugging crashes]{.doc}]Errors_debug.md){.reference .internal} for a couple of examples showing how to do this on a Linux machine. With this information -- a simple way to reproduce the segmentation fault and the exact [[LAMMPS version]{.doc}]Manual_version.md){.reference .internal} and platform you are running on -- you can contact the LAMMPS developers or post in the LAMMPS forum to get assistance.
:::

::: {#fast-moving-atoms .section}
[]{#hint05}

### [Fast moving atoms](#id6){.toc-backref role="doc-backlink"}[](#fast-moving-atoms "Link to this heading"){.headerlink}

Fast moving atoms may be "lost" or "missing" when their velocity becomes so large that they can cross a sub-domain within one timestep. This often happens when atoms are too close, but atoms may also "move" too fast from sub-domain to sub-domain if the box changes rapidly. E.g. when setting a large initial box with [[shrink-wrap boundary conditions]{.doc}]boundary.md){.reference .internal} that collapses on the first step (in this case the solution is often using 'm' instead of 's' as a boundary condition).

To reduce the impact of "close contacts", one can remove those atoms or molecules with something like [[delete_atoms overlap 0.1 all all]{.doc}]delete_atoms.md){.reference .internal}. With periodic boundaries, a close contact pair of atoms may be on opposite sides of the simulation box. Another option would be to first run a minimization (aka quench) before starting the MD. Reducing the time step can also help. Many times, one just needs to "ease" the system into a balanced state and can then switch to more aggressive settings.

The speed of atoms during an MD run depends on the steepness of the potential function and their mass. Since the positions and velocities of atoms are computed with finite timesteps, the timestep needs to be small enough for stable numeric integration of the trajectory. If the timestep is too large during initialization (or other instances of extreme dynamics), using [[fix nve/limit]{.doc}]fix_nve_limit.md){.reference .internal} or [[fix dt/reset]{.doc}]fix_dt_reset.md){.reference .internal} temporarily can help to avoid too large updates or adapt the timestep according to the displacements.
:::

::: {#ignoring-lost-atoms .section}
[]{#hint06}

### [Ignoring lost atoms](#id7){.toc-backref role="doc-backlink"}[](#ignoring-lost-atoms "Link to this heading"){.headerlink}

It is tempting to use the [[thermo_modify lost ignore]{.doc}]thermo_modify.md){.reference .internal} to avoid LAMMPS aborting with an error on lost atoms. This setting should, however, *only* be used when atoms *should* leave the system. In general, ignoring a problem does not solve it.
:::

::: {#pressure-forces-positions-becoming-nan-or-inf .section}
[]{#hint07}

### [Pressure, forces, positions becoming NaN or Inf](#id8){.toc-backref role="doc-backlink"}[](#pressure-forces-positions-becoming-nan-or-inf "Link to this heading"){.headerlink}

Some potentials can overflow or have a division by zero with close contacts or bad geometries (for the given force styles in use) leading to forces that can no longer be represented as numbers. Those will show as "NaN" or "Inf". On most machines, the program will continue, but there is no way to recover from it and those NaN or Inf values will propagate.

If the "NaN" or "Inf" appears in the first simulation step, the most common cause is overlapping atoms. Note that when atoms are *very* close, this cannot be seen when visualizing the geometry, since the atoms are effectively sitting on top of each other. A good test is to insert a command like [[delete_atoms 0.1 all all]{.doc}]delete_atoms.md){.reference .internal} and then monitor the output to see how many atoms are deleted, if any. A non-zero number would be an indication of overlapping atoms. Note that atoms can also overlap through periodic boundaries when the box dimensions are too small (e.g. determined by min/max position of atoms without padding).

So-called [["soft-core" potentials]{.doc}]pair_fep_soft.md){.reference .internal} or the [["soft" repulsive-only pair style]{.doc}]pair_soft.md){.reference .internal} are less prone for this behavior (depending on the settings in use) and can be used at the beginning of a simulation. Also, single precision numbers can overflow much faster, so for the GPU, KOKKOS, or INTEL package it may be beneficial to run with double precision initially before switching to mixed or single precision for faster execution when the system has relaxed.
:::

::: {#communication-cutoff .section}
[]{#hint08}

### [Communication cutoff](#id9){.toc-backref role="doc-backlink"}[](#communication-cutoff "Link to this heading"){.headerlink}

The communication cutoff determines the "overlap" between sub-domains and atoms in these regions are referred to in LAMMPS as "ghost atoms". This region has to be large enough to contain all atoms of a bond, angle, dihedral, or improper with just one atom in the actual sub-domain. Typically, this cutoff is set to the largest cutoff from the [[pair style(s)]{.doc}]pair_style.md){.reference .internal} plus the [[neighbor list skin distance]{.doc}]neighbor.md){.reference .internal} and will typically be sufficient for all bonded interactions. But if the pair style cutoff is small (e.g. with a repulsive-only Lennard-Jones potential) this may not be enough. It is even worse if there is no pair style defined (or the pair style is set to "none"), since then there will be no ghost atoms created at all.

The communication cutoff can be set or adjusted with [[comm_modify cutoff \<value\>]{.doc}]comm_modify.md){.reference .internal}, but setting this too large will waste CPU time and memory. LAMMPS will print warnings in these cases. For bonds it uses some heuristic based on the equilibrium bond length, but that still may not be sufficient for cases where the force constants are small and thus bonds may be stretched very far.
:::

::: {#neighbor-list-settings .section}
[]{#hint09}

### [Neighbor list settings](#id10){.toc-backref role="doc-backlink"}[](#neighbor-list-settings "Link to this heading"){.headerlink}

Every time LAMMPS rebuilds the neighbor lists, LAMMPS will also check for "lost" or "missing" atoms. Thus it can help to use very conservative [[neighbor list settings]{.doc}]neigh_modify.md){.reference .internal} and then examine the neighbor list statistics if the neighbor list rebuild can be safely delayed. Rebuilding the neighbor list less frequently (i.e. through increasing the *delay* or *every*) setting has diminishing returns and increasing risks.
:::

::: {#units .section}
[]{#hint10}

### [Units](#id11){.toc-backref role="doc-backlink"}[](#units "Link to this heading"){.headerlink}

A frequent cause for a variety of problems is due to using the wrong [[units]{.doc}]units.md){.reference .internal} settings for a particular potentials, especially when reading them from a potential file. Most of the (example) potentials bundled with LAMMPS have a "UNITS:" tag that allows LAMMPS to check of the units are consistent with what is intended, but potential files from publications or potential parameter databases may lack this metadata information and thus will not error out or warn when using the wrong setting. Most potential files usually use "metal" units, but some are parameterized for other settings, most notably [[ReaxFF potentials]{.doc}]pair_reaxff.md){.reference .internal} that use "real" units.

Also, individual parameters for [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} commands taken from publications or other MD software may need to be converted and sometimes in unexpected ways. Thus some careful checking is recommended.
:::

::: {#no-error-message-printed .section}
[]{#hint11}

### [No error message printed](#id12){.toc-backref role="doc-backlink"}[](#no-error-message-printed "Link to this heading"){.headerlink}

In some cases -- especially when running in parallel with MPI -- LAMMPS may stop without displaying an error. But the fact that nothing was displayed does not mean there was not an error message. Instead it is highly likely that the message was written to a buffer and LAMMPS was aborted before the buffer was output. Usually, output buffers are output for every line of output, but sometimes this is delayed until 4096 or 8192 bytes of output have been accumulated. This buffering for screen and logfile output can be disabled by using the [[-nb or -nonbuf]{.std .std-ref}]Run_options.md#nonbuf){.reference .internal} command-line flag. This is most often needed when debugging crashing multi-replica calculations.
:::

::: {#errors-before-or-after-the-simulation-box-is-created .section}
[]{#hint12}

### [Errors before or after the simulation box is created](#id13){.toc-backref role="doc-backlink"}[](#errors-before-or-after-the-simulation-box-is-created "Link to this heading"){.headerlink}

As critical step in a LAMMPS input is when the simulation box is defined, either with a [[create_box command]{.doc}]create_box.md){.reference .internal}, a [[read_data command]{.doc}]read_data.md){.reference .internal}, or a [[read_restart command]{.doc}]read_restart.md){.reference .internal}. After this step, certain settings are locked in (e.g. units, or number of atom, bond, angle, dihedral, improper types) and cannot be changed after that. Consequently, commands that change such settings (e.g. [[units]{.doc}]units.md){.reference .internal}) are only allowed before the box is defined. Very few commands can be used before and after, like [[pair_style]{.doc}]pair_style.md){.reference .internal} (but not [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}). Most LAMMPS commands must be used after the simulation box is created.

Consequently, LAMMPS will stop with an error, if a command is used in the wrong place. This is not always obvious. So index or string style [[variables]{.doc}]variable.md){.reference .internal} can be expanded anywhere in the input, but equal style (or similar) variables can only be expanded before the box is defined if they do not reference anything that cannot be defined before the box (e.g. a compute or fix reference or a thermo keyword).
:::

::: {#illegal-command .section}
[]{#hint13}

### [Illegal ... command](#id14){.toc-backref role="doc-backlink"}[](#illegal-command "Link to this heading"){.headerlink}

These are catchall error messages that used to be used a *lot* in LAMMPS (also programmers are sometimes lazy). They usually include the name of the source file and the line where the error happened. This can be used to track down what caused the error (most often some form of syntax error) by looking at the source code. However, this has two disadvantages: 1. one has to check the source file from the exact same LAMMPS version, or else the line number would be different or the core may have been rewritten and that specific error does not exist anymore.

The LAMMPS developers are committed to replace these too generic error messages with more descriptive errors, e.g. listing *which* keyword was causing the error, so that it will be much simpler to look up the correct syntax in the manual (and without referring to the source code).

------------------------------------------------------------------------
:::
::::::::::::::::

::: {#unknown-identifier-in-data-file .section}
[]{#err0001}

## [[5.2.2. ]{.section-number}Unknown identifier in data file](#id15){.toc-backref role="doc-backlink"}[](#unknown-identifier-in-data-file "Link to this heading"){.headerlink}

This error happens when LAMMPS encounters a line of text with an unexpected keyword while [[reading a data file]{.doc}]read_data.md){.reference .internal}. This would be either header keywords or section header keywords. This is most commonly due to a mistyped keyword or due to a keyword that is inconsistent with the [[atom style]{.doc}]atom_style.md){.reference .internal} used.

The header section informs LAMMPS how many entries or lines are expected in the various sections (like Atoms, Masses, Pair Coeffs, *etc.*) of the data file. If there is a mismatch, LAMMPS will either keep reading beyond the end of a section or stop reading before the section has ended. In that case the next line will not contain a recognized keyword.

Such a mismatch can also happen when the first line of the data is *not* a comment as required by the format, but a line with a valid header keyword. That would result in LAMMPS expecting, for instance, 0 atoms because the "atoms" header line is the first line and thus treated as a comment.

Another possibility to trigger this error is to have a keyword in the data file that corresponds to a fix (e.g. [[fix cmap]{.doc}]fix_cmap.md){.reference .internal}) but the [[read_data]{.doc}]read_data.md){.reference .internal} command is missing the (optional) arguments that identify the fix and its header and section keywords. Alternatively, those arguments are inconsistent with the keywords in the data file.
:::

::: {#incorrect-format-in-section-of-data-file .section}
[]{#err0002}

## [[5.2.3. ]{.section-number}Incorrect format in ... section of data file](#id16){.toc-backref role="doc-backlink"}[](#incorrect-format-in-section-of-data-file "Link to this heading"){.headerlink}

This error happens when LAMMPS reads the contents of a section of a [[data file]{.doc}]read_data.md){.reference .internal} and the number of parameters in the line differs from what is expected. This most commonly happens when the atom style is different from what is expected for a specific data file since changing the atom style usually changes the format of the line.

This error can also occur when the number of entries indicated in the header of a data file (e.g. the number of atoms) is larger than the number of lines provided (e.g. in the corresponding Atoms section) causing LAMMPS to continue reading into the next section which has a completely different format.
:::

::: {#illegal-variable-command-expected-x-arguments-but-found-y .section}
[]{#err0003}

## [[5.2.4. ]{.section-number}Illegal variable command: expected X arguments but found Y](#id17){.toc-backref role="doc-backlink"}[](#illegal-variable-command-expected-x-arguments-but-found-y "Link to this heading"){.headerlink}

This error indicates that a variable command has either incorrectly formatted arguments or the wrong number of arguments. A common reason for this is that a variable expression contains whitespace, but is not enclosed in single or double quotes.

To explain, the LAMMPS input parser reads and processes lines. The resulting line is broken down into "words". Those are usually individual commands, labels, names, and values separated by whitespace (a space or tab character). For "words" that may contain whitespace, they have to be enclosed in single (') or double (") quotes. The parser will then remove the outermost pair of quotes and pass that string as single argument to the variable command.

Thus missing quotes or accidental extra whitespace will trigger this error because the unquoted whitespace will result in the text being broken into more "words" than expected, i.e. the variable expression being split.
:::

::: {#out-of-range-atoms-cannot-compute .section}
[]{#err0004}

## [[5.2.5. ]{.section-number}Out of range atoms - cannot compute ...](#id18){.toc-backref role="doc-backlink"}[](#out-of-range-atoms-cannot-compute "Link to this heading"){.headerlink}

The PPPM (and also PPPMDisp and MSM) methods need to assemble a grid of electron density data derived from the (partial) charges assigned to the atoms. These charges are smeared out across multiple grid points (see [[kspace_modify order]{.doc}]kspace_modify.md){.reference .internal}). When running in parallel with MPI, LAMMPS uses a [[domain decomposition scheme]{.doc}]Developer_par_part.md){.reference .internal} where each processor manages a subset of atoms and thus also a grid representing the density. The processor's grid covers the actual volume of the sub-domain and some extra space corresponding to the [[neighbor list skin]{.doc}]neighbor.md){.reference .internal}. These are then [[combined and redistributed]{.doc}]Developer_par_long.md){.reference .internal} for parallel processing of the long-range component of the Coulomb interaction.

The [`Out`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`of`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`range`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`atoms`{.docutils .literal .notranslate}]{.pre} error can happen when atoms move too fast, the neighbor list skin is too small, or the neighbor lists are not updated frequently enough. The smeared charges cannot then be fully assigned to the density grid for all atoms. LAMMPS checks for this condition and stops with an error. Most of the time, this is an indication of a system with very high forces, often at the beginning of a simulation or when boundary conditions are changed. The error becomes more likely with more MPI processes.

There are multiple options to explore for avoiding the error. The best choice depends strongly on the individual system, and often a combination of changes is required. For example, more conservative MD parameter settings can be used (larger neighbor skin, shorter time step, more frequent neighbor list updates). Sometimes, it helps to revisit the system generation and avoid close contacts when building it. Otherwise one can use the [[delete_atoms overlap]{.doc}]delete_atoms.md){.reference .internal} command to delete those close contact atoms or run a minimization before the MD. It can also help to temporarily use a cutoff-Coulomb pair style and no kspace style until the system has somewhat equilibrated and then switch to the long-range solver.
:::

::: {#bond-or-angle-dihedral-improper-cmap-or-shake-atoms-missing .section}
[]{#err0005}

## [[5.2.6. ]{.section-number}Bond (or angle, dihedral, improper, cmap, or shake) atoms missing](#id19){.toc-backref role="doc-backlink"}[](#bond-or-angle-dihedral-improper-cmap-or-shake-atoms-missing "Link to this heading"){.headerlink}

The second atom needed to compute a particular bond (or the third or fourth atom for angle, dihedral, or improper) is missing on the indicated timestep and processor. Typically, this is because the two bonded atoms have become too far apart relative to the communication cutoff distance for ghost atoms. By default, the communication cutoff is set by the pair cutoff. However, to accommodate larger distances between topologically connected atoms, it can be manually adjusted using [[comm_modify]{.doc}]comm_modify.md){.reference .internal} at the cost of increased communication and more ghost atoms. However, missing bond atoms may also indicate that there are unstable dynamics which caused the atoms to blow apart. In this scenario, increasing the communication distance will not solve the underlying issue. Rather, see [[Fast moving atoms]{.std .std-ref}](#hint05){.reference .internal} and [[Neighbor list settings]{.std .std-ref}](#hint09){.reference .internal} in the general troubleshooting section above for ideas to fix unstable dynamics.

If atoms are intended to be lost during a simulation (e.g. due to open boundary conditions or [[fix evaporate]{.doc}]fix_evaporate.md){.reference .internal}) such that two bonded atoms may be lost at different times from each other, this error can be converted to a warning or turned off using the *lost/bond* keyword in the [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} command.
:::

::: {#non-numeric-atom-coords-or-pressure-or-box-dimensions-simulation-unstable .section}
[]{#err0006}

## [[5.2.7. ]{.section-number}Non-numeric atom coords or pressure or box dimensions - simulation unstable](#id20){.toc-backref role="doc-backlink"}[](#non-numeric-atom-coords-or-pressure-or-box-dimensions-simulation-unstable "Link to this heading"){.headerlink}

This error usually occurs due to overly aggressive simulation settings or issues with the system geometry or the potential. See [[Pressure, forces, positions becoming NaN or Inf]{.std .std-ref}](#hint07){.reference .internal} above in the general troubleshooting section. This error is more likely to happen during equilibration, so it can help to do a minimization before or even add a second or third minimization after running a few equilibration MD steps. It also is more likely when directly using a Nose-Hoover (or other) barostat, and thus it may be advisable to run with only a thermostat for a bit until the potential energy has stabilized.
:::

::: {#fix-used-in-not-computed-at-compatible-time .section}
[]{#err0007}

## [[5.2.8. ]{.section-number}Fix used in ... not computed at compatible time](#id21){.toc-backref role="doc-backlink"}[](#fix-used-in-not-computed-at-compatible-time "Link to this heading"){.headerlink}

Many fix styles are invoked only every *nevery* timesteps, which means their data is only valid on those steps. When data from a fix is used as input for a compute, a dump, another fix, or thermo output, it must read that data at timesteps when the fix in question was invoked, i.e. on timesteps that are multiples of its *nevery* setting. If this is not the case, LAMMPS will stop with an error. To remedy this, it may be required to change the output frequency or the *nevery* setting of the fix.
:::

::: {#lost-atoms .section}
[]{#err0008}

## [[5.2.9. ]{.section-number}Lost atoms ...](#id22){.toc-backref role="doc-backlink"}[](#lost-atoms "Link to this heading"){.headerlink}

A simulation stopping with an error due to lost atoms can have multiple causes. By default, LAMMPS checks for whether the total number of atoms is consistent with the sum of atoms "owned" by MPI processors every time that thermodynamic output is written. In the majority of cases, lost atoms are unexpected and a result of extremely high velocities causing instabilities in the system. Such velocities can result from a variety of issues. For ideas on how to track down issues with unexpected lost atoms, see [[Fast moving atoms]{.std .std-ref}](#hint05){.reference .internal} and [[Neighbor list settings]{.std .std-ref}](#hint09){.reference .internal} in the general troubleshooting section above. In specific situations however, losing atoms is expected material behavior (e.g. with sputtering and surface evaporation simulations), and an unwanted crash can be avoided by changing the [[thermo_modify lost]{.doc}]thermo_modify.md){.reference .internal} keyword from the default 'error' to 'warn' or 'ignore' (though heed the advice in [[Ignoring lost atoms]{.std .std-ref}](#hint06){.reference .internal} above!).
:::

::: {#too-many-neighbor-bins .section}
[]{#err0009}

## [[5.2.10. ]{.section-number}Too many neighbor bins](#id23){.toc-backref role="doc-backlink"}[](#too-many-neighbor-bins "Link to this heading"){.headerlink}

The simulation box is or has become too large relative to the size of a neighbor bin (which in turn depends on the largest pair-wise cutoff by default) such that LAMMPS is unable to store the needed number of bins. This typically implies the simulation box has expanded too far. That can occur when some atoms move rapidly apart with shrink-wrap boundaries or when a fix (like fix deform or a barostat) excessively grows the simulation box. This can also happen if the largest pair-wise cutoff is small. In this case, the error can be avoided by using the [[neigh_modify command]{.doc}]neigh_modify.md){.reference .internal} to set the bin width to a suitably large value.
:::

::: {#unrecognized-style .section}
[]{#err0010}

## [[5.2.11. ]{.section-number}Unrecognized ... style ...](#id24){.toc-backref role="doc-backlink"}[](#unrecognized-style "Link to this heading"){.headerlink}

There are multiple variants of this error message. The most common case is that there is a typo or syntax error in the input file and the style name of a command was not found in the LAMMPS executable.

Another case is that the input is using the correct style command, but the LAMMPS executable in use was not compiled with the package containing that specific style. LAMMPS executables include tables of all available packages and styles in the distribution, and thus will print in this case a message indicating which package is missing. This indicates that the executable needs to be re-built after enabling the correct package. See the [[LAMMPS build instructions]{.doc}]Build.md){.reference .internal} for more details on including packages. One can check if the expected package and style is present in the executable by running it with the [`-help`{.docutils .literal .notranslate}]{.pre} (or [`-h`{.docutils .literal .notranslate}]{.pre}) flag on the command line. One common oversight, especially for LAMMPS users with limited experience in compiling software from source, is enabling the package but forgetting to rebuild or install the executable. One can also check the documentation for the style in question for a "Restrictions" section, which should indicate which requirements apply to a given command.

Finally, there is the case that the necessary package is included, but the missing style depends also on *another* style from a *different* package and *this* package is missing. In that case, LAMMPS does not know which package is missing, and it is necessary to check the documentation for the missing style in the manual.

If this error occurs with an executable that the user does not control (e.g., through a module on HPC clusters), the user will need to get in contact with the relevant person or people who can update the executable. In rare cases, there may be licensing or portability issues that prevent including a package in publicly accessible binaries or in a specific environment.
:::

::: {#energy-or-stress-was-not-tallied-by-pair-style .section}
[]{#err0011}

## [[5.2.12. ]{.section-number}Energy or stress was not tallied by pair style](#id25){.toc-backref role="doc-backlink"}[](#energy-or-stress-was-not-tallied-by-pair-style "Link to this heading"){.headerlink}

This warning can be printed by computes from the [[TALLY package]{.std .std-ref}]Packages_details.md#pkg-tally){.reference .internal}. Those use a callback mechanism that only work for regular pair-wise additive pair styles like [[Lennard-Jones]{.doc}]pair_lj.md){.reference .internal}, [[Morse]{.doc}]pair_morse.md){.reference .internal}, [[Born-Meyer-Huggins]{.doc}]pair_born.md){.reference .internal}, and similar. Such required callbacks have not been implemented for many-body potentials so one would have to implement them to add compatibility with these computes (which may be difficult to do in a generic fashion). Whether this warning indicates that contributions to the computed properties are missing depends on the groups used. At any rate, careful testing of the results is advised when this warning appears.
:::

::: {#fmt-format-error .section}
[]{#err0012}

## [[5.2.13. ]{.section-number}fmt::format_error](#id26){.toc-backref role="doc-backlink"}[](#fmt-format-error "Link to this heading"){.headerlink}

LAMMPS uses the [{fmt} library](https://fmt.dev){.reference .external} for advanced string formatting tasks. This is similar to the [`printf()`{.docutils .literal .notranslate}]{.pre} family of functions from the standard C library, but more flexible. If there is a bug in the LAMMPS code and the format string does not match the list of arguments or has some other error, this error message will be shown. You should contact the LAMMPS developers and report the bug as a [GitHub Bug Report Issue](https://github.com/lammps/lammps/issues){.reference .external} along with sufficient information to easily reproduce it.
:::

::::: {#substitution-for-illegal-variable .section}
[]{#err0013}

## [[5.2.14. ]{.section-number}Substitution for illegal variable](#id27){.toc-backref role="doc-backlink"}[](#substitution-for-illegal-variable "Link to this heading"){.headerlink}

A variable in an input script or a variable expression was not found in the list of valid variables. The most common reason for this is a typo somewhere in the input file such that the expression uses an invalid variable name. The second most common reason is omitting the curly braces for a direct variable with a name that is not a single letter. For example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable cutoff index 10.0
    pair_style lj/cut ${cutoff}  # this is correct
    pair_style lj/cut $cutoff    # this is incorrect, LAMMPS looks for 'c' instead of 'cutoff'
    variable c      index 5.0    # if $c is defined, LAMMPS substitutes only '$c' and reads: 5utoff
:::
::::

Another potential source of this error may be invalid command line variables (-var or -v argument) used when launching LAMMPS from an interactive shell or shell scripts. An uncommon source for this error is using the [[next command]{.doc}]next.md){.reference .internal} to advance through a list of values provided by an index style variable. If there is no remaining element in the list, LAMMPS will delete the variable and any following expansion or reference attempt will trigger the error.

Users with harder-to-track variable errors might also find reading the [[Parsing rules for input scripts]{.doc}]Commands_parse.md){.reference .internal} helpful.
:::::

::: {#bond-atom-missing-in-image-check-or-box-size-check .section}
[]{#err0014}

## [[5.2.15. ]{.section-number}Bond atom missing in image check or box size check](#id28){.toc-backref role="doc-backlink"}[](#bond-atom-missing-in-image-check-or-box-size-check "Link to this heading"){.headerlink}

This can be either an error or a warning depending on your [[thermo_modify settings]{.doc}]thermo_modify.md){.reference .internal}. It is flagged in a part of the LAMMPS code where it updates the domain decomposition and before it builds the neighbor lists. It checks that both atoms of a bond are within the communication cutoff of a subdomain. It is usually caused by atoms moving too fast (see the [[paragraph on fast moving atoms]{.std .std-ref}](#hint05){.reference .internal}), or by the [[communication cutoff being too small]{.doc}]comm_modify.md){.reference .internal}, or by waiting too long between [[sub-domain and neighbor list updates]{.doc}]neigh_modify.md){.reference .internal}.
:::

::: {#cannot-use-neighbor-bins-box-size-cutoff .section}
[]{#err0015}

## [[5.2.16. ]{.section-number}Cannot use neighbor bins - box size \<\< cutoff](#id29){.toc-backref role="doc-backlink"}[](#cannot-use-neighbor-bins-box-size-cutoff "Link to this heading"){.headerlink}

LAMMPS is unable to build neighbor bins since the size of the box is much smaller than an interaction cutoff in at least one of its dimensions. Typically, this error is triggered when the simulation box has one very thin dimension. If a cubic neighbor bin had to fit exactly within the thin dimension, then an inordinate amount of bins would be created to fill space. This error can be avoided using the generally slower [[nsq neighbor style]{.doc}]neighbor.md){.reference .internal} or by increasing the size of the smallest box lengths.
:::

::: {#did-not-assign-all-atoms-correctly .section}
[]{#err0016}

## [[5.2.17. ]{.section-number}Did not assign all atoms correctly](#id30){.toc-backref role="doc-backlink"}[](#did-not-assign-all-atoms-correctly "Link to this heading"){.headerlink}

This error happens most commonly when [[reading a data file]{.doc}]read_data.md){.reference .internal} under [[non-periodic boundary conditions]{.doc}]boundary.md){.reference .internal}. Only atoms with positions **inside** the simulation box will be read and thus any atoms outside the box will be skipped and the total atom count will not match, which triggers the error. This does not happen with periodic boundary conditions where atoms outside the principal box will be "wrapped" into the principal box and their image flags set accordingly.

Similar errors can happen with the [[replicate command]{.doc}]replicate.md){.reference .internal} or the [[read_restart command]{.doc}]read_restart.md){.reference .internal}. In these cases the cause may be a problematic geometry, an insufficient communication cutoff, or a bug in the LAMMPS source code. In these cases it is advisable to set up [[small test case]{.std .std-ref}](#hint01){.reference .internal} for testing and debugging. This will be required in case you need to get help from a LAMMPS developer.
:::

::: {#domain-too-large-for-neighbor-bins .section}
[]{#err0017}

## [[5.2.18. ]{.section-number}Domain too large for neighbor bins](#id31){.toc-backref role="doc-backlink"}[](#domain-too-large-for-neighbor-bins "Link to this heading"){.headerlink}

The domain has become extremely large so that neighbor bins cannot be used. Too many neighbor bins would need to be created to fill space. Most likely, one or more atoms have been blown a great distance out of the simulation box or a fix (like fix deform or a barostat) has excessively grown the simulation box.
:::

::: {#step-x-h-bondchk-failed .section}
[]{#err0018}

## [[5.2.19. ]{.section-number}Step X: (h)bondchk failed](#id32){.toc-backref role="doc-backlink"}[](#step-x-h-bondchk-failed "Link to this heading"){.headerlink}

This error is a consequence of the heuristic memory allocations for buffers of the regular ReaxFF version. In ReaxFF simulations, the lists of bonds and hydrogen bonds can change due to chemical reactions. The default approach, however, assumes that these changes are not very large, so it allocates buffers for the current system setup plus a safety margin. This can be adjusted with the [[safezone, mincap, and minhbonds settings of the pair style]{.doc}]pair_reaxff.md){.reference .internal}, but only to some extent. When equilibrating a new system, or simulating a sparse system in parallel, this can be difficult to control and become wasteful. A simple workaround is often to break a simulation down in multiple chunks. A better approach, however, is to compile and use the KOKKOS package version of ReaxFF (you do not need a GPU for that, but can also compile it in serial or OpenMP mode), which uses a more robust memory allocation approach.
:::

::: {#numeric-index-x-is-out-of-bounds .section}
[]{#err0019}

## [[5.2.20. ]{.section-number}Numeric index X is out of bounds](#id33){.toc-backref role="doc-backlink"}[](#numeric-index-x-is-out-of-bounds "Link to this heading"){.headerlink}

This error most commonly happens when setting force field coefficients with either the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}, the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}, or the [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command. These commands accept type labels, explicit numbers, and wildcards for ranges of numbers. If the numeric value of any of these is outside the valid range (defined by the number of corresponding types), LAMMPS will stop with this error. A few other commands and styles also allow ranges of numbers and check using the same method and thus print the same kind of error.

The cause is almost always a typo in the input or a logic error when defining the values or ranges. So one needs to carefully review the input. Along with the error, LAMMPS will print the valid range as a hint.
:::

::: {#compute-fix-or-variable-vector-or-array-is-accessed-out-of-range .section}
[]{#err0020}

## [[5.2.21. ]{.section-number}Compute, fix, or variable vector or array is accessed out-of-range](#id34){.toc-backref role="doc-backlink"}[](#compute-fix-or-variable-vector-or-array-is-accessed-out-of-range "Link to this heading"){.headerlink}

When accessing an individual element of a global vector or array or a per-atom vector or array provided by a compute or fix or atom-style or vector-style variable or data from a specific atom, an index in square brackets ("\[ \]") (or two indices) must be provided to determine which element to access and it must be in a valid range or else LAMMPS would access invalid data or crash with a segmentation fault. In the two most common cases, where this data is accessed, [[variable expressions]{.doc}]variable.md){.reference .internal} and [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}, LAMMPS will check for valid indices and stop with an error otherwise.

While LAMMPS is written in C++ (which uses 0 based indexing) these indices start at 1 (i.e. similar to Fortran). Any index smaller than 1 or larger than the maximum allowed value should trigger this error. Since this kind of error frequently happens with rather complex expressions, it is recommended to test these with small test systems, where the values can be tracked with output files for all relevant properties at every step.
:::

::: {#incorrect-args-for-pair-coefficients-also-bond-angle-dihedral-improper-coefficients .section}
[]{#err0021}

## [[5.2.22. ]{.section-number}Incorrect args for pair coefficients (also bond/angle/dihedral/improper coefficients)](#id35){.toc-backref role="doc-backlink"}[](#incorrect-args-for-pair-coefficients-also-bond-angle-dihedral-improper-coefficients "Link to this heading"){.headerlink}

The parameters in the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command for a specified [[pair_style]{.doc}]pair_style.md){.reference .internal} have a missing or erroneous argument. The same applies when seeing this error for [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}, [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}, or [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} and their respective style commands when using the MOLECULE or EXTRA-MOLECULE packages. The cases below describe some ways to approach pair coefficient errors, but the same strategies apply to bonded systems as well.

Outside of normal typos, this error can have several sources. In all cases, the first step is to compare the command arguments to the expected format found in the corresponding [[pair_style]{.doc}]pair_style.md){.reference .internal} page. This can reveal cases where, for example, a pair style was changed, but the pair coefficients were not updated. This can happen especially with pair style variants such as [[pair_style eam]{.doc}]pair_eam.md){.reference .internal} vs. [[pair_style eam/alloy]{.doc}]pair_style.md){.reference .internal} that look very similar but accept different parameters (the latter 'eam/alloy' variant takes element type names while 'eam' does not).

Another common source of coefficient errors is when using multiple pair styles with commands such as [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal}. Using hybrid pair styles requires adding an extra "label" argument in the coefficient commands that designates which pair style the command line refers to. Moreover, if the same pair style is used multiple times, this label must be followed by an additional numeric argument. Also, different pair styles may require different arguments.

This error message might also require a close look at other LAMMPS input files that are read in by the input script, such as data files or restart files.
:::

::::: {#energy-was-not-tallied-on-needed-timestep-also-virial-per-atom-energy-per-atom-virial .section}
[]{#err0022}

## [[5.2.23. ]{.section-number}Energy was not tallied on needed timestep (also virial, per-atom energy, per-atom virial)](#id36){.toc-backref role="doc-backlink"}[](#energy-was-not-tallied-on-needed-timestep-also-virial-per-atom-energy-per-atom-virial "Link to this heading"){.headerlink}

This error is generated when LAMMPS attempts to access an out-of-date or non-existent energy, pressure, or virial. For efficiency reasons, LAMMPS does *not* calculate these quantities when the forces are calculated on every timestep or iteration. Global quantities are only calculated when they are needed for [[thermo]{.doc}]thermo_style.md){.reference .internal} output (at the beginning, end, and at regular intervals specified by the [[thermo]{.doc}]thermo.md){.reference .internal} command). Similarly, per-atom quantities are only calculated if they are needed to write per-atom energy or virial to a dump file. This system works fine for simple input scripts. However, the many user-specified variable, fix, and compute commands that LAMMPS provides make it difficult to anticipate when a quantity will be requested. In some use cases, LAMMPS will figure out that a quantity is needed and arrange for it to be calculated on that timestep e.g. if it is requested by [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} or similar commands. If that fails, it can be detected by a mismatch between the current timestep and when a quantity was last calculated, in which case an error message of this type is generated.

The most common cause of this type of error is requesting a quantity before the start of the simulation.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # run 0 post no               # this will fix the error
    variable e equal pe           # requesting energy compute
    print "Potential energy = $e" # this will generate the error
    run 1000                      # start of simulation
:::
::::

This situation can be avoided by adding in a "run 0" command, as explained in more detail in the "Variable Accuracy" section of the [[variable]{.doc}]variable.md){.reference .internal} doc page.

Another cause is requesting a quantity on a timestep that is not a thermo or dump output timestep. This can often be remedied by increasing the frequency of thermo or dump output.
:::::

::: {#molecule-auto-special-bond-generation-overflow .section}
[]{#err0023}

## [[5.2.24. ]{.section-number}Molecule auto special bond generation overflow](#id37){.toc-backref role="doc-backlink"}[](#molecule-auto-special-bond-generation-overflow "Link to this heading"){.headerlink}

In order to correctly apply the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} settings (also known as "exclusions"), LAMMPS needs to maintain for each atom a list of atoms that are connected to this atom, either directly with a bond or indirectly through bonding with an intermediate atom(s). The purpose is to either remove or tag those pairs of atoms in the neighbor list. This information is stored with individual atoms and thus the maximum number of such "special" neighbors is set when the simulation box is created. When reading (relative) geometry and topology of a 'molecule' from a [[molecule file]{.doc}]molecule.md){.reference .internal}, LAMMPS will build the list of such "special" neighbors for the molecule atom (if not given in the molecule file explicitly). The error is triggered when the resulting list is too long for the space reserved when creating the simulation box. The solution is to increase the corresponding setting. Overestimating this value will only consume more memory, and is thus a safe choice.
:::

::: {#molecule-topology-atom-exceeds-system-topology-atom .section}
[]{#err0024}

## [[5.2.25. ]{.section-number}Molecule topology/atom exceeds system topology/atom](#id38){.toc-backref role="doc-backlink"}[](#molecule-topology-atom-exceeds-system-topology-atom "Link to this heading"){.headerlink}

LAMMPS uses [[domain decomposition]{.doc}]Developer_par_part.md){.reference .internal} to distribute data (i.e. atoms) across the MPI processes in parallel runs. This includes topology data about bonds, angles, dihedrals, impropers and [["special" neighbors]{.doc}]special_bonds.md){.reference .internal}. This information is stored with either one or all atoms involved in such a topology entry (which of the two option applies depends on the [[newton]{.doc}]newton.md){.reference .internal} setting for bonds). When reading a data file, LAMMPS analyzes the requirements for this file and then the values are "locked in" and cannot be extended.

So loading a molecule file that requires more of the topology per atom storage or adding a data file with such needs will lead to an error. To avoid the error, one or more of the extra/XXX/per/atom keywords are required to extend the corresponding storage. It is no problem to choose those numbers generously and have more storage reserved than actually needed, but having these numbers set too small will lead to an error.
:::

::: {#molecule-topology-type-exceeds-system-topology-type .section}
[]{#err0025}

## [[5.2.26. ]{.section-number}Molecule topology type exceeds system topology type](#id39){.toc-backref role="doc-backlink"}[](#molecule-topology-type-exceeds-system-topology-type "Link to this heading"){.headerlink}

The total number of atom, bond, angle, dihedral, and improper types is "locked in" when LAMMPS creates the simulation box. This can happen through either the [[create_box]{.doc}]create_box.md){.reference .internal}, the [[read_data]{.doc}]read_data.md){.reference .internal}, or the [[read_restart]{.doc}]read_restart.md){.reference .internal} command. After this it is not possible to refer to an additional type. So loading a molecule file that uses additional types or adding a data file that would require additional types will lead to an error. To avoid the error, one or more of the extra/XXX/types keywords are required to extend the maximum number of the individual types.
:::

::: {#molecule-attributes-do-not-match-system-attributes .section}
[]{#err0026}

## [[5.2.27. ]{.section-number}Molecule attributes do not match system attributes](#id40){.toc-backref role="doc-backlink"}[](#molecule-attributes-do-not-match-system-attributes "Link to this heading"){.headerlink}

Choosing an [[atom_style]{.doc}]atom_style.md){.reference .internal} in LAMMPS determines which per-atom properties are available. In a [[molecule file]{.doc}]molecule.md){.reference .internal}, however, it is possible to add sections (for example Masses or Charges) that are not supported by the atom style. Masses for example, are usually not a per-atom property, but defined through the atom type. Thus it would not be required to have a Masses section and the included data would be ignored. LAMMPS prints this warning to inform about this case.
:::

::: {#inconsistent-image-flags .section}
[]{#err0027}

## [[5.2.28. ]{.section-number}Inconsistent image flags](#id41){.toc-backref role="doc-backlink"}[](#inconsistent-image-flags "Link to this heading"){.headerlink}

This warning happens when the distance between the *unwrapped* x-, y-, or z-components of the coordinates of a bond is larger than half the box with periodic boundaries or larger than the box with non-periodic boundaries. It means that the positions and image flags have become inconsistent. LAMMPS will still compute bonded interactions based on the closest periodic images of the atoms and thus in most cases the results will be correct. However they can cause problems when such atoms are used with the fix rigid or replicate commands. Thus, it is good practice to update the system so that the message does not appear. It will help with future manipulations of the system.

There is one case where this warning *must* appear: when you have a chain of connected bonds that pass through the entire box and connect back to the first atom in the chain through periodic boundaries, i.e. some kind of "infinite polymer". In that case, the bond image flags *must* be inconsistent for the one bond that reaches back to the beginning of the chain.
:::

::: {#no-fixes-with-time-integration-atoms-won-t-move .section}
[]{#err0028}

## [[5.2.29. ]{.section-number}No fixes with time integration, atoms won't move](#id42){.toc-backref role="doc-backlink"}[](#no-fixes-with-time-integration-atoms-won-t-move "Link to this heading"){.headerlink}

This warning will be issued if LAMMPS encounters a [[run]{.doc}]run.md){.reference .internal} command that does not have a preceding [[fix]{.doc}]fix.md){.reference .internal} command that updates atom/object positions and velocities per step. In other words, there are no fixes detected that perform velocity-Verlet time integration, such as [[fix nve]{.doc}]fix_nve.md){.reference .internal}. Note that this alert does not mean that there are no active fixes. LAMMPS has a very wide variety of fixes, many of which do not move objects but also operate through steps, such as printing outputs (e.g. [[fix print]{.doc}]fix_print.md){.reference .internal}), performing calculations (e.g. [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}), or changing other system parameters (e.g. [[fix dt/reset]{.doc}]fix_dt_reset.md){.reference .internal}). It is up to the user to determine whether the lack of a time-integrating fix is intentional or not.
:::

::: {#system-is-not-charge-neutral-net-charge .section}
[]{#err0029}

## [[5.2.30. ]{.section-number}System is not charge neutral, net charge = ...](#id43){.toc-backref role="doc-backlink"}[](#system-is-not-charge-neutral-net-charge "Link to this heading"){.headerlink}

The sum of charges in the system is not zero. When a system is not charge-neutral, methods that evolve/manipulate per-atom charges, evaluate Coulomb interactions, evaluate Coulomb forces, or evaluate/manipulate other properties relying on per-atom charges may raise this warning. A non-zero net charge most commonly arises after setting per-atom charges [[set]{.doc}]set.md){.reference .internal} such that the sum is non-zero or by reading in a system through [[read_data]{.doc}]read_data.md){.reference .internal} where the per-atom charges do not sum to zero. However, a loss of charge neutrality may occur in other less common ways, like when charge equilibration methods (e.g., [[fix qeq]{.doc}]fix_qeq.md){.reference .internal}) fail.

A similar warning/error may be raised when using certain charge equilibration methods: [[fix qeq]{.doc}]fix_qeq.md){.reference .internal}, [[fix qeq/comb]{.doc}]fix_qeq_comb.md){.reference .internal}, [[fix qeq/reaxff]{.doc}]fix_qeq_reaxff.md){.reference .internal}, and [[fix qtpie/reaxff]{.doc}]fix_qtpie_reaxff.md){.reference .internal}. In such cases, this warning/error will be raised for the fix [[group]{.doc}]group.md){.reference .internal} when the group has a non-zero net charge.

When the system is expected to be charge-neutral, this warning often arises due to an error in the lammps input (e.g., an incorrect [[set]{.doc}]set.md){.reference .internal} command, error in the data file read by [[read_data]{.doc}]read_data.md){.reference .internal}, incorrectly grouping atoms with charge, etc.). If the system is NOT expected to be charge-neutral, the user should make sure that the method(s) used are appropriate for systems with a non-zero net charge. Some commonly used fixes for charge equilibration [[fix qeq]{.doc}]fix_qeq.md){.reference .internal}, pair styles that include charge interactions [[pair_style coul/XXX]{.doc}]pair_coul.md){.reference .internal}, and kspace methods [[kspace_style]{.doc}]kspace_style.md){.reference .internal} can, in theory, support systems with non-zero net charge. However, non-zero net charge can lead to spurious artifacts. The severity of these artifacts depends on the magnitude of total charge, system size, and methods used. Before running simulations or calculations for systems with non-zero net charge, users should test for artifacts and convergence of properties.
:::

::: {#variable-evaluation-before-simulation-box-is-defined .section}
[]{#err0030}

## [[5.2.31. ]{.section-number}Variable evaluation before simulation box is defined](#id44){.toc-backref role="doc-backlink"}[](#variable-evaluation-before-simulation-box-is-defined "Link to this heading"){.headerlink}

This error happens, when trying to expand or use an equal- or atom-style variable (or an equivalent style), where the expression contains a reference to something (e.g. a compute reference, a property of an atom, or a thermo keyword) that is not allowed to be used before the simulation box is defined. See the paragraph on [[errors before or after the simulation box is created]{.std .std-ref}](#hint12){.reference .internal} for additional information.
:::

::: {#invalid-thermo-keyword-x-in-variable-formula .section}
[]{#err0031}

## [[5.2.32. ]{.section-number}Invalid thermo keyword 'X' in variable formula](#id45){.toc-backref role="doc-backlink"}[](#invalid-thermo-keyword-x-in-variable-formula "Link to this heading"){.headerlink}

This error message is often misleading. It is caused when evaluating a [[variable command]{.doc}]variable.md){.reference .internal} expression and LAMMPS comes across a string that it does not recognize. LAMMPS first checks if a string is a reference to a compute, fix, custom property, or another variable by looking at the first 2-3 characters (and if it is, it checks whether the referenced item exists). Next LAMMPS checks if the string matches one of the available functions or constants. If that fails, LAMMPS will assume that this string is a [[thermo keyword]{.doc}]thermo_style.md){.reference .internal} and let the code for printing thermodynamic output return the corresponding value. However, if this fails too, since the string is not a thermo keyword, LAMMPS stops with the 'Invalid thermo keyword' error. But it is also possible, that there is just a typo in the name of a valid variable function. Thus it is recommended to check the failing variable expression very carefully.
:::

::: {#one-or-more-atoms-are-time-integrated-more-than-once .section}
[]{#err0032}

## [[5.2.33. ]{.section-number}One or more atoms are time integrated more than once](#id46){.toc-backref role="doc-backlink"}[](#one-or-more-atoms-are-time-integrated-more-than-once "Link to this heading"){.headerlink}

This is probably an error since you typically do not want to advance the positions or velocities of an atom more than once per timestep. This typically happens when there are multiple fix commands that advance atom positions with overlapping groups. Also, for some fix styles it is not immediately obvious that they include time integration. Please check the documentation carefully.
:::

::: {#xxx-command-before-simulation-box-is-defined .section}
[]{#err0033}

## [[5.2.34. ]{.section-number}XXX command before simulation box is defined](#id47){.toc-backref role="doc-backlink"}[](#xxx-command-before-simulation-box-is-defined "Link to this heading"){.headerlink}

This error occurs when trying to execute a LAMMPS command that requires information about the system dimensions, or the number atom, bond, angle, dihedral, or improper types, or the number of atoms or similar data that is only available *after* the simulation box has been created. See the paragraph on [[errors before or after the simulation box is created]{.std .std-ref}](#hint12){.reference .internal} for additional information.
:::

::: {#xxx-command-after-simulation-box-is-defined .section}
[]{#err0034}

## [[5.2.35. ]{.section-number}XXX command after simulation box is defined](#id48){.toc-backref role="doc-backlink"}[](#xxx-command-after-simulation-box-is-defined "Link to this heading"){.headerlink}

This error occurs when trying to execute a LAMMPS command that changes a global setting *after* it is locked in when the simulation box is created (for instance defining the [[atom style]{.doc}]atom_style.md){.reference .internal}, [[dimension]{.doc}]dimension.md){.reference .internal}, [[newton]{.doc}]newton.md){.reference .internal}, or [[units]{.doc}]units.md){.reference .internal} setting). These settings may only be changed *before* the simulation box has been created. See the paragraph on [[errors before or after the simulation box is created]{.std .std-ref}](#hint12){.reference .internal} for additional information.
:::

::: {#error-messages-ending-in-please-contact-the-lammps-developers .section}
[]{#err0035}

## [[5.2.36. ]{.section-number}Error messages ending in 'Please contact the LAMMPS developers'](#id49){.toc-backref role="doc-backlink"}[](#error-messages-ending-in-please-contact-the-lammps-developers "Link to this heading"){.headerlink}

Such error messages indicate that something unexpected has happened and that it will require a good understanding of the details of the design of LAMMPS to resolve this. This can be due to some bug in contributed code, an oversight when updating functionality, a feature that is scheduled to be removed or reaching a combination of flags and settings that should not be possible or similar.

Even if you find a way to work around this error or warning, you should contact the LAMMPS developers and prepare a minimal set of inputs that can be used to reproduce this error or warning. By providing the input, the LAMMPS developers can then assess whether additional action is needed and who else to contact about this, if needed.

There are multiple ways to get into contact and report your issue. In order of preference there are:

- Submit a bug report [issue in the LAMMPS GitHub](https://github.com/lammps/lammps/issues){.reference .external} repository

- Post a message in the "LAMMPS Development" forum in the [MatSci Community Discourse](https://matsci.org/c/lammps/lammps-development/42){.reference .external}

- Send an email to [`developers@lammps.org`{.docutils .literal .notranslate}]{.pre}

- Send an email to an [[individual LAMMPS developer]{.doc}]Intro_authors.md){.reference .internal} that you know and trust
:::

::: {#neighbor-list-overflow-boost-neigh-modify-one .section}
[]{#err0036}

## [[5.2.37. ]{.section-number}Neighbor list overflow, boost neigh_modify one](#id50){.toc-backref role="doc-backlink"}[](#neighbor-list-overflow-boost-neigh-modify-one "Link to this heading"){.headerlink}

The neighbor list code in LAMMPS uses a special memory allocation strategy to speed up building and accessing neighbor lists.

Instead of making a memory allocation for each list of neighbors of the atoms LAMMPS allocates "pages" that have room for several neighbor lists. This has two main advantages:

1.  It is not needed to first count how many neighbors there are for an atom to determine the storage required. Since the pages are much larger than individual lists, LAMMPS just "fills up" the page until there is not enough space left and then allocates a new page.

2.  There are fewer calls to the memory allocator functions (which can be time consuming for long-running jobs and fragmented memory space) and the resulting neighbor lists are close to each other physically which improves cache efficiency.

This is controlled by the two parameters "one" and "page", respectively, that can be set via the [[neigh_modify command]{.doc}]neigh_modify.md){.reference .internal}. The parameter "one" is the maximum number of entries in a list of neighbors for a single atom. If an atom has more neighbors as the "one" parameter allows, the "overflow" error message is triggered. The parameter "page" sets the size of the page. The neighbor list code checks, if there are "one" entries left in the current page. If not, a new page is allocated.

The default settings are suitable for most systems. They need to be changed, for instance, when simulating a system with a very high density or when setting a very long cutoff (e.g. [\\(\\gtrapprox 15 \\AA\\)]{.math .notranslate .nohighlight} with [[units real]{.doc}]units.md){.reference .internal}). The value of "page" **must** be at least 10x the value of "one", but 50x to 100x are recommended to avoid wasting memory. The neighbor list storage is typically the largest amount of RAM required by a LAMMPS calculation.

Even though the LAMMPS error message recommends to increase the "one" parameter, this may not always be the correct solution. The neighbor list overflow can also be a symptom for some other error that cannot be easily detected. For example, a frequent reason for an (unexpected) high density are incorrect box dimensions (since LAMMPS wraps atoms back into the principal box with periodic boundaries) or coordinates provided as fractional coordinates (LAMMPS does not support this for data files). In both cases, LAMMPS cannot easily know whether the input geometry has such a high density (and thus requiring more neighbor list storage per atom) on purpose or by accident. Rather than blindly increasing the "one" parameter, it is thus worth checking if this is justified by the combination of density and cutoff. This is particularly recommended when using some tool(s) to convert input or data files.

When boosting (= increasing) the "one" parameter, it is recommended to also increase the value for the "page" parameter to maintain the ratio between "one" and "page" to reduce waste of memory. For some more details, please check out the documentation for the [[neigh_modify command]{.doc}]neigh_modify.md){.reference .internal}.
:::

::: {#variable-compute-fix-does-not-compute-requested-property .section}
[]{#err0037}

## [[5.2.38. ]{.section-number}Variable ...: Compute/Fix ... does not compute requested property](#id51){.toc-backref role="doc-backlink"}[](#variable-compute-fix-does-not-compute-requested-property "Link to this heading"){.headerlink}

Compute and fix styles can compute different kinds of properties: for example, global scalars, vectors, or arrays, or per-atom vectors or arrays. In equal-style or similar variable, only scalar properties can be used, so to access a particular element in a vector one has to use square brackets with a suitable index to select it. However, not all fixes and computes provide all types of properties. So this error message will be shown if there is a mismatch, of if there are not enough or too many square brackets. To differentiate between accessing an element of a global array or a per-atom array element of a specific atom, one has to use a reference with a lower case 'c' (e.g. 'c_name') for the former and upper case 'C' (e.g. 'C_name') for the latter. The same applies to fix styles. The full details are in the documentation for the [[variable command]{.doc}]variable.md){.reference .internal}.
:::

::: {#the-style-is-no-longer-available .section}
[]{#err0038}

## [[5.2.39. ]{.section-number}The ... style ... is no longer available](#id52){.toc-backref role="doc-backlink"}[](#the-style-is-no-longer-available "Link to this heading"){.headerlink}

While the LAMMPS developers try to keep the software backward compatible as far as input files and file formats are concerned, this is not always desired and changes are made and commands renamed or removed. In that case an error message is printed describing why the command cannot be executed. More details can be found on the manual page [[Removed commands and packages]{.doc}]Commands_removed.md){.reference .internal}.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#output-from-lammps-thermo-dumps-computes-fixes-variables .section}
# [10.3.1. ]{.section-number}Output from LAMMPS (thermo, dumps, computes, fixes, variables)[](#output-from-lammps-thermo-dumps-computes-fixes-variables "Link to this heading"){.headerlink}

There are four basic forms of LAMMPS output:

- [[Thermodynamic output]{.doc}]thermo_style.md){.reference .internal}, which is a list of quantities printed every few timesteps to the screen and logfile.

- [[Dump files]{.doc}]dump.md){.reference .internal}, which contain snapshots of atoms and various per-atom values and are written at a specified frequency.

- Certain fixes can output user-specified quantities to files: [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} for time averaging, [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} for spatial or other averaging, and [[fix print]{.doc}]fix_print.md){.reference .internal} for single-line output of [[variables]{.doc}]variable.md){.reference .internal}. Fix print can also output to the screen.

- [[Restart files]{.doc}]restart.md){.reference .internal}.

A simulation prints one set of thermodynamic output and (optionally) restart files. It can generate any number of dump files and fix output files, depending on what [[dump]{.doc}]dump.md){.reference .internal} and [[fix]{.doc}]fix.md){.reference .internal} commands you specify.

As discussed below, LAMMPS gives you a variety of ways to determine what quantities are calculated and printed when the thermodynamics, dump, or fix commands listed above perform output. Throughout this discussion, note that users can also [[add their own computes and fixes to LAMMPS]{.doc}]Modify.md){.reference .internal} which can generate values that can then be output with these commands.

The following subsections discuss different LAMMPS commands related to output and the kind of data they operate on and produce:

- [[Global/per-atom/local/per-grid data]{.std .std-ref}](#global){.reference .internal}

- [[Scalar/vector/array data]{.std .std-ref}](#scalar){.reference .internal}

- [[Disambiguation]{.std .std-ref}](#disambiguation){.reference .internal}

- [[Thermodynamic output]{.std .std-ref}](#thermo){.reference .internal}

- [[Dump file output]{.std .std-ref}](#dump){.reference .internal}

- [[Fixes that write output files]{.std .std-ref}](#fixoutput){.reference .internal}

- [[Computes that process output quantities]{.std .std-ref}](#computeoutput){.reference .internal}

- [[Fixes that process output quantities]{.std .std-ref}](#fixprocoutput){.reference .internal}

- [[Computes that generate values to output]{.std .std-ref}](#compute){.reference .internal}

- [[Fixes that generate values to output]{.std .std-ref}](#fix){.reference .internal}

- [[Variables that generate values to output]{.std .std-ref}](#variable){.reference .internal}

- [[Summary table of output options and data flow between commands]{.std .std-ref}](#table){.reference .internal}

::: {#global-per-atom-local-per-grid-data .section}
[]{#global}

## Global/per-atom/local/per-grid data[](#global-per-atom-local-per-grid-data "Link to this heading"){.headerlink}

Various output-related commands work with four different "styles" of data: global, per-atom, local, and per-grid. A global datum is one or more system-wide values, e.g. the temperature of the system. A per-atom datum is one or more values per atom, e.g. the kinetic energy of each atom. Local datums are calculated by each processor based on the atoms it owns, and there may be zero or more per atom, e.g. a list of bond distances.

A per-grid datum is one or more values per grid cell, for a grid which overlays the simulation domain. Similar to atoms and per-atom data, the grid cells and the data they store are distributed across processors; each processor owns the grid cells whose center points fall within its subdomain.
:::

::: {#scalar-vector-array-data .section}
[]{#scalar}

## Scalar/vector/array data[](#scalar-vector-array-data "Link to this heading"){.headerlink}

Global, per-atom, local, and per-grid datums can come in three "kinds": a single scalar value, a vector of values, or a 2d array of values. More specifically these are the valid kinds for each style:

- global scalar

- global vector

- global array

- per-atom vector

- per-atom array

- local vector

- local array

- per-grid vector

- per-grid array

A per-atom vector means a single value per atom; the "vector" is the length of the number of atoms. A per-atom array means multiple values per atom. Similarly a local vector or array means one or multiple values per entity (e.g. per bond in the system). And a per-grid vector or array means one or multiple values per grid cell.

The doc page for a compute or fix or variable that generates data will specify both the styles and kinds of data it produces, e.g. a per-atom vector. Note that a compute or fix may generate multiple styles and kinds of output. However, for per-atom data only a vector or array is output, never both. Likewise for per-local and per-grid data. An example of a fix which generates multiple styles and kinds of data is the [[fix mdi/qm]{.doc}]fix_mdi_qm.md){.reference .internal} command. It outputs a global scalar, global vector, and per-atom array for the quantum mechanical energy and virial of the system and forces on each atom.

By contrast, different variable styles generate only a single kind of data: a global scalar for an equal-style variable, global vector for a vector-style variable, and a per-atom vector for an atom-style variable.

When data is accessed by another command, as in many of the output commands discussed below, it can be referenced via the following bracket notation, where ID in this case is the ID of a compute. The leading "c\_" would be replaced by "f\_" for a fix, or "v\_" for a variable (and ID would be the name of the variable):

  ---------------- --------------------------------------------
  c_ID             entire scalar, vector, or array
  c_ID\[I\]        one element of vector, one column of array
  c_ID\[I\]\[J\]   one element of array
  ---------------- --------------------------------------------

Note that using one bracket reduces the dimension of the data once (vector -\> scalar, array -\> vector). Using two brackets reduces the dimension twice (array -\> scalar). Thus a command that uses scalar values as input can also conceptually operate on an element of a vector or array.

Per-grid vectors or arrays are accessed similarly, except that the ID for the compute or fix includes a grid name and a data name. This is because a fix or compute can create multiple grids (of different sizes) and multiple sets of data (for each grid). The fix or compute defines names for each grid and for each data set, so that all of them can be accessed by other commands. See the [[Howto grid]{.doc}]Howto_grid.md){.reference .internal} doc page for more details.
:::

::: {#disambiguation .section}
[]{#id1}

## Disambiguation[](#disambiguation "Link to this heading"){.headerlink}

When a compute or fix produces data in multiple styles, e.g. global and per-atom, a reference to the data can sometimes be ambiguous. Usually the context in which the input script references the data determines which style is meant.

For example, if a compute outputs a global vector and a per-atom array, an element of the global vector will be accessed by using [`c_ID[I]`{.docutils .literal .notranslate}]{.pre} in [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}, while a column of the per-atom array will be accessed by using [`c_ID[I]`{.docutils .literal .notranslate}]{.pre} in a [[dump custom]{.doc}]dump.md){.reference .internal} command.

However, if a [[atom-style variable]{.doc}]variable.md){.reference .internal} references [`c_ID[I]`{.docutils .literal .notranslate}]{.pre}, then it could be intended to refer to a single element of the global vector or a column of the per-atom array. The doc page for any command that has a potential ambiguity (variables are the most common) will explain how to resolve the ambiguity.

In this case, an atom-style variables references per-atom data if it exists. If access to an element of a global vector is needed (as in this example), an equal-style variable which references the value can be defined and used in the atom-style variable formula instead.

Similarly, [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} can only reference global data from a compute or fix. But you can indirectly access per-atom data as follows. The reference [`c_ID[245][2]`{.docutils .literal .notranslate}]{.pre} for the ID of a [[compute displace/atom]{.doc}]compute_displace_atom.md){.reference .internal} command, refers to the y-component of displacement for the atom with ID 245. While you cannot use that reference directly in the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command, you can use it an equal-style variable formula, and then reference the variable in thermodynamic output.
:::

::: {#thermodynamic-output .section}
[]{#thermo}

## Thermodynamic output[](#thermodynamic-output "Link to this heading"){.headerlink}

The frequency and format of thermodynamic output is set by the [[thermo]{.doc}]thermo.md){.reference .internal}, [[thermo_style]{.doc}]thermo_style.md){.reference .internal}, and [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} commands. The [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command also specifies what values are calculated and written out. Pre-defined keywords can be specified (e.g. press, etotal, etc). Three additional kinds of keywords can also be specified (c_ID, f_ID, v_name), where a [[compute]{.doc}]compute.md){.reference .internal} or [[fix]{.doc}]fix.md){.reference .internal} or [[variable]{.doc}]variable.md){.reference .internal} provides the value to be output. In each case, the compute, fix, or variable must generate global values for input to the [[thermo_style custom]{.doc}]dump.md){.reference .internal} command.

Note that thermodynamic output values can be "extensive" or "intensive". The former scale with the number of atoms in the system (e.g. total energy), the latter do not (e.g. temperature). The setting for [[thermo_modify norm]{.doc}]thermo_modify.md){.reference .internal} determines whether extensive quantities are normalized or not. Computes and fixes produce either extensive or intensive values; see their individual doc pages for details. [[Equal-style variables]{.doc}]variable.md){.reference .internal} produce only intensive values; you can include a division by "natoms" in the formula if desired, to make an extensive calculation produce an intensive result.
:::

::: {#dump-file-output .section}
[]{#dump}

## Dump file output[](#dump-file-output "Link to this heading"){.headerlink}

Dump file output is specified by the [[dump]{.doc}]dump.md){.reference .internal} and [[dump_modify]{.doc}]dump_modify.md){.reference .internal} commands. There are several pre-defined formats (dump atom, dump xtc, etc).

There is also a [[dump custom]{.doc}]dump.md){.reference .internal} format where the user specifies what values are output with each atom. Pre-defined atom attributes can be specified (id, x, fx, etc). Three additional kinds of keywords can also be specified (c_ID, f_ID, v_name), where a [[compute]{.doc}]compute.md){.reference .internal} or [[fix]{.doc}]fix.md){.reference .internal} or [[variable]{.doc}]variable.md){.reference .internal} provides the values to be output. In each case, the compute, fix, or variable must generate per-atom values for input to the [[dump custom]{.doc}]dump.md){.reference .internal} command.

There is also a [[dump local]{.doc}]dump.md){.reference .internal} format where the user specifies what local values to output. A pre-defined index keyword can be specified to enumerate the local values. Two additional kinds of keywords can also be specified (c_ID, f_ID), where a [[compute]{.doc}]compute.md){.reference .internal} or [[fix]{.doc}]fix.md){.reference .internal} or [[variable]{.doc}]variable.md){.reference .internal} provides the values to be output. In each case, the compute or fix must generate local values for input to the [[dump local]{.doc}]dump.md){.reference .internal} command.

There is also a [[dump grid]{.doc}]dump.md){.reference .internal} format where the user specifies what per-grid values to output from computes or fixes that generate per-grid data.
:::

::: {#fixes-that-write-output-files .section}
[]{#fixoutput}

## Fixes that write output files[](#fixes-that-write-output-files "Link to this heading"){.headerlink}

Several fixes take various quantities as input and can write output files: [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}, [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal}, [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal}, [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal}, and [[fix print]{.doc}]fix_print.md){.reference .internal}.

The [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} command enables direct output to a file and/or time-averaging of global scalars or vectors. The user specifies one or more quantities as input. These can be global [[compute]{.doc}]compute.md){.reference .internal} values, global [[fix]{.doc}]fix.md){.reference .internal} values, or [[variables]{.doc}]variable.md){.reference .internal} of any style except the atom style which produces per-atom values. Since a variable can refer to keywords used by the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command (like temp or press) and individual per-atom values, a wide variety of quantities can be time averaged and/or output in this way. If the inputs are one or more scalar values, then the fix generate a global scalar or vector of output. If the inputs are one or more vector values, then the fix generates a global vector or array of output. The time-averaged output of this fix can also be used as input to other output commands.

The [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} command enables direct output to a file of chunk-averaged per-atom quantities like those output in dump files. Chunks can represent spatial bins or other collections of atoms, e.g. individual molecules. The per-atom quantities can be atom density (mass or number) or atom attributes such as position, velocity, force. They can also be per-atom quantities calculated by a [[compute]{.doc}]compute.md){.reference .internal}, by a [[fix]{.doc}]fix.md){.reference .internal}, or by an atom-style [[variable]{.doc}]variable.md){.reference .internal}. The chunk-averaged output of this fix is global and can also be used as input to other output commands.

Note that the [[fix ave/grid]{.doc}]fix_ave_grid.md){.reference .internal} command can also average the same per-atom quantities within spatial bins, but it does this for a distributed grid whose grid cells are owned by different processors. It outputs per-grid data, not global data, so it is more efficient for large numbers of averaging bins.

The [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal} command enables direct output to a file of histogrammed quantities, which can be global or per-atom or local quantities. The histogram output of this fix can also be used as input to other output commands.

The [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} command enables direct output to a file of time-correlated quantities, which can be global values. The correlation matrix output of this fix can also be used as input to other output commands.

The [[fix print]{.doc}]fix_print.md){.reference .internal} command can generate a line of output written to the screen and log file or to a separate file, periodically during a running simulation. The line can contain one or more [[variable]{.doc}]variable.md){.reference .internal} values for any style variable except the vector or atom styles). As explained above, variables themselves can contain references to global values generated by [[thermodynamic keywords]{.doc}]thermo_style.md){.reference .internal}, [[computes]{.doc}]compute.md){.reference .internal}, [[fixes]{.doc}]fix.md){.reference .internal}, or other [[variables]{.doc}]variable.md){.reference .internal}, or to per-atom values for a specific atom. Thus the [[fix print]{.doc}]fix_print.md){.reference .internal} command is a means to output a wide variety of quantities separate from normal thermodynamic or dump file output.
:::

::: {#computes-that-process-output-quantities .section}
[]{#computeoutput}

## Computes that process output quantities[](#computes-that-process-output-quantities "Link to this heading"){.headerlink}

The [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} and [[compute reduce/region]{.doc}]compute_reduce.md){.reference .internal} commands take one or more per-atom or local vector quantities as inputs and "reduce" them (sum, min, max, ave) to scalar quantities. These are produced as output values which can be used as input to other output commands.

The [[compute slice]{.doc}]compute_slice.md){.reference .internal} command take one or more global vector or array quantities as inputs and extracts a subset of their values to create a new vector or array. These are produced as output values which can be used as input to other output commands.

The [[compute property/atom]{.doc}]compute_property_atom.md){.reference .internal} command takes a list of one or more pre-defined atom attributes (id, x, fx, etc) and stores the values in a per-atom vector or array. These are produced as output values which can be used as input to other output commands. The list of atom attributes is the same as for the [[dump custom]{.doc}]dump.md){.reference .internal} command.

The [[compute property/local]{.doc}]compute_property_local.md){.reference .internal} command takes a list of one or more pre-defined local attributes (bond info, angle info, etc) and stores the values in a local vector or array. These are produced as output values which can be used as input to other output commands.

The [[compute property/grid]{.doc}]compute_property_grid.md){.reference .internal} command takes a list of one or more pre-defined per-grid attributes (id, grid cell coords, etc) and stores the values in a per-grid vector or array. These are produced as output values which can be used as input to the [[dump grid]{.doc}]dump.md){.reference .internal} command.

The [[compute property/chunk]{.doc}]compute_property_chunk.md){.reference .internal} command takes a list of one or more pre-defined chunk attributes (id, count, coords for spatial bins) and stores the values in a global vector or array. These are produced as output values which can be used as input to other output commands.
:::

::: {#fixes-that-process-output-quantities .section}
[]{#fixprocoutput}

## Fixes that process output quantities[](#fixes-that-process-output-quantities "Link to this heading"){.headerlink}

The [[fix vector]{.doc}]fix_vector.md){.reference .internal} command can create global vectors as output from global scalars as input, accumulating them one element at a time.

The [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal} command performs time-averaging of per-atom vectors. The per-atom quantities can be atom attributes such as position, velocity, force. They can also be per-atom quantities calculated by a [[compute]{.doc}]compute.md){.reference .internal}, by a [[fix]{.doc}]fix.md){.reference .internal}, or by an atom-style [[variable]{.doc}]variable.md){.reference .internal}. The time-averaged per-atom output of this fix can be used as input to other output commands.

The [[fix store/state]{.doc}]fix_store_state.md){.reference .internal} command can archive one or more per-atom attributes at a particular time, so that the old values can be used in a future calculation or output. The list of atom attributes is the same as for the [[dump custom]{.doc}]dump.md){.reference .internal} command, including per-atom quantities calculated by a [[compute]{.doc}]compute.md){.reference .internal}, by a [[fix]{.doc}]fix.md){.reference .internal}, or by an atom-style [[variable]{.doc}]variable.md){.reference .internal}. The output of this fix can be used as input to other output commands.

The [[fix ave/grid]{.doc}]fix_ave_grid.md){.reference .internal} command performs time-averaging of either per-atom or per-grid data.

For per-atom data it performs averaging for the atoms within each grid cell, similar to the [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} command when its chunks are defined as regular 2d or 3d bins. The per-atom quantities can be atom density (mass or number) or atom attributes such as position, velocity, force. They can also be per-atom quantities calculated by a [[compute]{.doc}]compute.md){.reference .internal}, by a [[fix]{.doc}]fix.md){.reference .internal}, or by an atom-style [[variable]{.doc}]variable.md){.reference .internal}.

The chief difference between the [[fix ave/grid]{.doc}]fix_ave_grid.md){.reference .internal} and [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} commands when used in this context is that the former uses a distributed grid, while the latter uses a global grid. Distributed means that each processor owns the subset of grid cells within its subdomain. Global means that each processor owns a copy of the entire grid. The [[fix ave/grid]{.doc}]fix_ave_grid.md){.reference .internal} command is thus more efficient for large grids.

For per-grid data, the [[fix ave/grid]{.doc}]fix_ave_grid.md){.reference .internal} command takes inputs for grid data produced by other computes or fixes and averages the values for each grid point over time.
:::

::: {#computes-that-generate-values-to-output .section}
[]{#compute}

## Computes that generate values to output[](#computes-that-generate-values-to-output "Link to this heading"){.headerlink}

Every [[compute]{.doc}]compute.md){.reference .internal} in LAMMPS produces either global or per-atom or local or per-grid values. The values can be scalars or vectors or arrays of data. These values can be output using the other commands described in this section. The page for each compute command describes what it produces. Computes that produce per-atom or local or per-grid values have the word "atom" or "local" or "grid" as the last word in their style name. Computes without the word "atom" or "local" or "grid" produce global values.
:::

::: {#fixes-that-generate-values-to-output .section}
[]{#fix}

## Fixes that generate values to output[](#fixes-that-generate-values-to-output "Link to this heading"){.headerlink}

Some [[fixes]{.doc}]fix.md){.reference .internal} in LAMMPS produces either global or per-atom or local or per-grid values which can be accessed by other commands. The values can be scalars or vectors or arrays of data. These values can be output using the other commands described in this section. The page for each fix command tells whether it produces any output quantities and describes them.
:::

::: {#variables-that-generate-values-to-output .section}
[]{#variable}

## Variables that generate values to output[](#variables-that-generate-values-to-output "Link to this heading"){.headerlink}

[[Variables]{.doc}]variable.md){.reference .internal} defined in an input script can store one or more strings. But equal-style, vector-style, and atom-style or atomfile-style variables generate a global scalar value, global vector or values, or a per-atom vector, respectively, when accessed. The formulas used to define these variables can contain references to the thermodynamic keywords and to global and per-atom data generated by computes, fixes, and other variables. The values generated by variables can be used as input to and thus output by the other commands described in this section.

Per-grid variables have not (yet) been implemented.
:::

::: {#summary-table-of-output-options-and-data-flow-between-commands .section}
[]{#table}

## Summary table of output options and data flow between commands[](#summary-table-of-output-options-and-data-flow-between-commands "Link to this heading"){.headerlink}

This table summarizes the various commands that can be used for generating output from LAMMPS. Each command produces output data of some kind and/or writes data to a file. Most of the commands can take data from other commands as input. Thus you can link many of these commands together in pipeline form, where data produced by one command is used as input to another command and eventually written to the screen or to a file. Note that to hook two commands together the output and input data types must match, e.g. global/per-atom/local data and scalar/vector/array data.

Also note that, as described above, when a command takes a scalar as input, that could also be an element of a vector or array. Likewise a vector input could be a column of an array.

  ------------------------------------------------------------------------------------- ---------------------------------------------- ----------------------------------------------------
  Command                                                                               Input                                          Output
  [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal}                global scalars                                 screen, log file
  [[dump custom]{.doc}]dump.md){.reference .internal}                                per-atom vectors                               dump file
  [[dump local]{.doc}]dump.md){.reference .internal}                                 local vectors                                  dump file
  [[dump grid]{.doc}]dump.md){.reference .internal}                                  per-grid vectors                               dump file
  [[fix print]{.doc}]fix_print.md){.reference .internal}                             global scalar from variable                    screen, file
  [[print]{.doc}]print.md){.reference .internal}                                     global scalar from variable                    screen
  [[computes]{.doc}]compute.md){.reference .internal}                                N/A                                            global/per-atom/local/per-grid scalar/vector/array
  [[fixes]{.doc}]fix.md){.reference .internal}                                       N/A                                            global/per-atom/local/per-grid scalar/vector/array
  [[variables]{.doc}]variable.md){.reference .internal}                              global scalars and vectors, per-atom vectors   global scalar and vector, per-atom vector
  [[compute reduce]{.doc}]compute_reduce.md){.reference .internal}                   per-atom/local vectors                         global scalar/vector
  [[compute slice]{.doc}]compute_slice.md){.reference .internal}                     global vectors/arrays                          global vector/array
  [[compute property/atom]{.doc}]compute_property_atom.md){.reference .internal}     N/A                                            per-atom vector/array
  [[compute property/local]{.doc}]compute_property_local.md){.reference .internal}   N/A                                            local vector/array
  [[compute property/grid]{.doc}]compute_property_grid.md){.reference .internal}     N/A                                            per-grid vector/array
  [[compute property/chunk]{.doc}]compute_property_chunk.md){.reference .internal}   N/A                                            global vector/array
  [[fix vector]{.doc}]fix_vector.md){.reference .internal}                           global scalars                                 global vector
  [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal}                       per-atom vectors                               per-atom vector/array
  [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}                       global scalars/vectors                         global scalar/vector/array, file
  [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal}                     per-atom vectors                               global array, file
  [[fix ave/grid]{.doc}]fix_ave_grid.md){.reference .internal}                       per-atom vectors or per-grid vectors           per-grid vector/array
  [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal}                     global/per-atom/local scalars and vectors      global array, file
  [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal}             global scalars                                 global array, file
  [[fix store/state]{.doc}]fix_store_state.md){.reference .internal}                 per-atom vectors                               per-atom vector/array
  ------------------------------------------------------------------------------------- ---------------------------------------------- ----------------------------------------------------
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#use-chunks-to-calculate-system-properties .section}
# [10.3.2. ]{.section-number}Use chunks to calculate system properties[](#use-chunks-to-calculate-system-properties "Link to this heading"){.headerlink}

In LAMMPS, "chunks" are collections of atoms, as defined by the [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command, which assigns each atom to a chunk ID (or to no chunk at all). The number of chunks and the assignment of chunk IDs to atoms can be static or change over time. Examples of "chunks" are molecules or spatial bins or atoms with similar values (e.g. coordination number or potential energy).

The per-atom chunk IDs can be used as input to two other kinds of commands, to calculate various properties of a system:

- [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal}

- any of the [[compute \*/chunk]{.doc}]compute.md){.reference .internal} commands

Here a brief overview for each of the 4 kinds of chunk-related commands is provided. Then some examples are given of how to compute different properties with chunk commands.

::: {#compute-chunk-atom-command .section}
## Compute chunk/atom command:[](#compute-chunk-atom-command "Link to this heading"){.headerlink}

This compute can assign atoms to chunks of various styles. Only atoms in the specified group and optional specified region are assigned to a chunk. Here are some possible chunk definitions:

  --------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  atoms in same molecule                                    chunk ID = molecule ID
  atoms of same atom type                                   chunk ID = atom type
  all atoms with same atom property (charge, radius, etc)   chunk ID = output of compute property/atom
  atoms in same cluster                                     chunk ID = output of [[compute cluster/atom]{.doc}]compute_cluster_atom.md){.reference .internal} command
  atoms in same spatial bin                                 chunk ID = bin ID
  atoms in same rigid body                                  chunk ID = molecule ID used to define rigid bodies
  atoms with similar potential energy                       chunk ID = output of [[compute pe/atom]{.doc}]compute_pe_atom.md){.reference .internal}
  atoms with same local defect structure                    chunk ID = output of [[compute centro/atom]{.doc}]compute_centro_atom.md){.reference .internal} or [[compute coord/atom]{.doc}]compute_coord_atom.md){.reference .internal} command
  --------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note that chunk IDs are integer values, so for atom properties or computes that produce a floating point value, they will be truncated to an integer. You could also use the compute in a variable that scales the floating point value to spread it across multiple integers.

Spatial bins can be of various kinds, e.g. 1d bins = slabs, 2d bins = pencils, 3d bins = boxes, spherical bins, cylindrical bins.

This compute also calculates the number of chunks *Nchunk*, which is used by other commands to tally per-chunk data. *Nchunk* can be a static value or change over time (e.g. the number of clusters). The chunk ID for an individual atom can also be static (e.g. a molecule ID), or dynamic (e.g. what spatial bin an atom is in as it moves).

Note that this compute allows the per-atom output of other [[computes]{.doc}]compute.md){.reference .internal}, [[fixes]{.doc}]fix.md){.reference .internal}, and [[variables]{.doc}]variable.md){.reference .internal} to be used to define chunk IDs for each atom. This means you can write your own compute or fix to output a per-atom quantity to use as chunk ID. See the [[Modify]{.doc}]Modify.md){.reference .internal} doc pages for info on how to do this. You can also define a [[per-atom variable]{.doc}]variable.md){.reference .internal} in the input script that uses a formula to generate a chunk ID for each atom.
:::

::: {#fix-ave-chunk-command .section}
## Fix ave/chunk command:[](#fix-ave-chunk-command "Link to this heading"){.headerlink}

This fix takes the ID of a [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command as input. For each chunk, it then sums one or more specified per-atom values over the atoms in each chunk. The per-atom values can be any atom property, such as velocity, force, charge, potential energy, kinetic energy, stress, etc. Additional keywords are defined for per-chunk properties like density and temperature. More generally any per-atom value generated by other [[computes]{.doc}]compute.md){.reference .internal}, [[fixes]{.doc}]fix.md){.reference .internal}, and [[per-atom variables]{.doc}]variable.md){.reference .internal}, can be summed over atoms in each chunk.

Similar to other averaging fixes, this fix allows the summed per-chunk values to be time-averaged in various ways, and output to a file. The fix produces a global array as output with one row of values per chunk.
:::

::: {#compute-chunk-commands .section}
## Compute \*/chunk commands:[](#compute-chunk-commands "Link to this heading"){.headerlink}

The following computes operate on chunks of atoms to produce per-chunk values. Any compute whose style name ends in "/chunk" is in this category:

- [[compute com/chunk]{.doc}]compute_com_chunk.md){.reference .internal}

- [[compute gyration/chunk]{.doc}]compute_gyration_chunk.md){.reference .internal}

- [[compute inertia/chunk]{.doc}]compute_inertia_chunk.md){.reference .internal}

- [[compute msd/chunk]{.doc}]compute_msd_chunk.md){.reference .internal}

- [[compute property/chunk]{.doc}]compute_property_chunk.md){.reference .internal}

- [[compute temp/chunk]{.doc}]compute_temp_chunk.md){.reference .internal}

- [[compute torque/chunk]{.doc}]compute_torque_chunk.md){.reference .internal}

- [[compute vcm/chunk]{.doc}]compute_vcm_chunk.md){.reference .internal}

They each take the ID of a [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command as input. As their names indicate, they calculate the center-of-mass, radius of gyration, moments of inertia, mean-squared displacement, temperature, torque, and velocity of center-of-mass for each chunk of atoms. The [[compute property/chunk]{.doc}]compute_property_chunk.md){.reference .internal} command can tally the count of atoms in each chunk and extract other per-chunk properties.

The reason these various calculations are not part of the [[fix ave/chunk command]{.doc}]fix_ave_chunk.md){.reference .internal}, is that each requires a more complicated operation than simply summing and averaging over per-atom values in each chunk. For example, many of them require calculation of a center of mass, which requires summing mass\*position over the atoms and then dividing by summed mass.

All of these computes produce a global vector or global array as output, with one or more values per chunk. The output can be used in various ways:

- As input to the [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} command, which can write the values to a file and optionally time average them.

- As input to the [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal} command to histogram values across chunks. E.g. a histogram of cluster sizes or molecule diffusion rates.

- As input to special functions of [[equal-style variables]{.doc}]variable.md){.reference .internal}, like sum() and max() and ave(). E.g. to find the largest cluster or fastest diffusing molecule or average radius-of-gyration of a set of molecules (chunks).
:::

::: {#other-chunk-commands .section}
## Other chunk commands:[](#other-chunk-commands "Link to this heading"){.headerlink}

- [[compute chunk/spread/atom]{.doc}]compute_chunk_spread_atom.md){.reference .internal}

- [[compute reduce/chunk]{.doc}]compute_reduce_chunk.md){.reference .internal}

The [[compute chunk/spread/atom]{.doc}]compute_chunk_spread_atom.md){.reference .internal} command spreads per-chunk values to each atom in the chunk, producing per-atom values as its output. This can be useful for outputting per-chunk values to a per-atom [[dump file]{.doc}]dump.md){.reference .internal}. Or for using an atom's associated chunk value in an [[atom-style variable]{.doc}]variable.md){.reference .internal}. Or as input to the [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} command to spatially average per-chunk values calculated by a per-chunk compute.

The [[compute reduce/chunk]{.doc}]compute_reduce_chunk.md){.reference .internal} command reduces a peratom value across the atoms in each chunk to produce a value per chunk. When used with the [[compute chunk/spread/atom]{.doc}]compute_chunk_spread_atom.md){.reference .internal} command it can create peratom values that induce a new set of chunks with a second [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command.
:::

::::::::::::: {#example-calculations-with-chunks .section}
## Example calculations with chunks[](#example-calculations-with-chunks "Link to this heading"){.headerlink}

Here are examples using chunk commands to calculate various properties:

1.  Average velocity in each of 1000 2d spatial bins:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cc1 all chunk/atom bin/2d x 0.0 0.1 y lower 0.01 units reduced
    fix 1 all ave/chunk 100 10 1000 cc1 vx vy file tmp.out
:::
::::

2\. Temperature in each spatial bin, after subtracting a flow velocity:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cc1 all chunk/atom bin/2d x 0.0 0.1 y lower 0.1 units reduced
    compute vbias all temp/profile 1 0 0 y 10
    fix 1 all ave/chunk 100 10 1000 cc1 temp bias vbias file tmp.out
:::
::::

3.  Center of mass of each molecule:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cc1 all chunk/atom molecule
    compute myChunk all com/chunk cc1
    fix 1 all ave/time 100 1 100 c_myChunk[*] file tmp.out mode vector
:::
::::

4.  Total force on each molecule and ave/max across all molecules:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cc1 all chunk/atom molecule
    fix 1 all ave/chunk 1000 1 1000 cc1 fx fy fz file tmp.out
    variable xave equal ave(f_1[2])
    variable xmax equal max(f_1[2])
    thermo 1000
    thermo_style custom step temp v_xave v_xmax
:::
::::

5.  Histogram of cluster sizes:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cluster all cluster/atom 1.0
    compute cc1 all chunk/atom c_cluster compress yes
    compute size all property/chunk cc1 count
    fix 1 all ave/histo 100 1 100 0 20 20 c_size mode vector ave running beyond ignore file tmp.histo
:::
::::

6\. An example for using a per-chunk value to apply per-atom forces to compress individual polymer chains (molecules) in a mixture, is explained on the [[compute chunk/spread/atom]{.doc}]compute_chunk_spread_atom.md){.reference .internal} command doc page.

7\. An example for using one set of per-chunk values for molecule chunks, to create a second set of micelle-scale chunks (clustered molecules, due to hydrophobicity), is explained on the [[compute reduce/chunk]{.doc}]compute_reduce_chunk.md){.reference .internal} command doc page.

8\. An example for using one set of per-chunk values (dipole moment vectors) for molecule chunks, spreading the values to each atom in each chunk, then defining a second set of chunks as spatial bins, and using the [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} command to calculate an average dipole moment vector for each bin. This example is explained on the [[compute chunk/spread/atom]{.doc}]compute_chunk_spread_atom.md){.reference .internal} command doc page.
:::::::::::::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

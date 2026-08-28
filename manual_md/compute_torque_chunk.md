::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#compute-torque-chunk-command .section}
[]{#index-0}

# compute torque/chunk command[](#compute-torque-chunk-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID torque/chunk chunkID
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- torque/chunk = style name of this compute command

- chunkID = ID of [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 fluid torque/chunk molchunk
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the torque on multiple chunks of atoms.

In LAMMPS, chunks are collections of atoms defined by a [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command, which assigns each atom to a single chunk (or no chunk). The ID for this command is specified as chunkID. For example, a single chunk could be the atoms in a molecule or atoms in a spatial bin. See the [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} and [[Howto chunk]{.doc}]Howto_chunk.md){.reference .internal} doc pages for details of how chunks can be defined and examples of how they can be used to measure properties of a system.

This compute calculates the three components of the torque vector for eqch chunk, due to the forces on the individual atoms in the chunk around the center-of-mass of the chunk. The calculation includes all effects due to atoms passing through periodic boundaries.

Note that only atoms in the specified group contribute to the calculation. The [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command defines its own group; atoms will have a chunk ID = 0 if they are not in that group, signifying they are not assigned to a chunk, and will thus also not contribute to this calculation. You can specify the "all" group for this command if you simply want to include atoms with non-zero chunk IDs.

::: {.admonition .note}
Note

The coordinates of an atom contribute to the chunk's torque in "unwrapped" form, by using the image flags associated with each atom. See the [[dump custom]{.doc}]dump.md){.reference .internal} command for a discussion of "unwrapped" coordinates. See the Atoms section of the [[read_data]{.doc}]read_data.md){.reference .internal} command for a discussion of image flags and how they are set for each atom. You can reset the image flags (e.g., to 0) before invoking this compute by using the [[set image]{.doc}]set.md){.reference .internal} command.
:::

The simplest way to output the results of the compute torque/chunk calculation to a file is to use the [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} command, for example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cc1 all chunk/atom molecule
    compute myChunk all torque/chunk cc1
    fix 1 all ave/time 100 1 100 c_myChunk[*] file tmp.out mode vector
:::
::::
::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global array where the number of rows is equal to the number of chunks *Nchunk* as calculated by the specified [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command. The number of columns is three for the [\\(x\\)]{.math .notranslate .nohighlight}, [\\(y\\)]{.math .notranslate .nohighlight}, and [\\(z\\)]{.math .notranslate .nohighlight} components of the torque for each chunk. These values can be accessed by any command that uses global array values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The array values are "intensive". The array values will be in force-distance [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[variable torque() function]{.doc}]variable.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

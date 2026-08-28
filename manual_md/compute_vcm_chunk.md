:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#compute-vcm-chunk-command .section}
[]{#index-0}

# compute vcm/chunk command[](#compute-vcm-chunk-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID vcm/chunk chunkID
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- vcm/chunk = style name of this compute command

- chunkID = ID of [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 fluid vcm/chunk molchunk
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the center-of-mass velocity for multiple chunks of atoms.

In LAMMPS, chunks are collections of atoms defined by a [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command, which assigns each atom to a single chunk (or no chunk). The ID for this command is specified as chunkID. For example, a single chunk could be the atoms in a molecule or atoms in a spatial bin. See the [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} and [[Howto chunk]{.doc}]Howto_chunk.md){.reference .internal} doc pages for details of how chunks can be defined and examples of how they can be used to measure properties of a system.

This compute calculates the [\\((x,y,z)\\)]{.math .notranslate .nohighlight} components of the center-of-mass velocity for each chunk. This is done by summing mass\*velocity for each atom in the chunk and dividing the sum by the total mass of the chunk.

Note that only atoms in the specified group contribute to the calculation. The [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command defines its own group; atoms will have a chunk ID = 0 if they are not in that group, signifying they are not assigned to a chunk, and will thus also not contribute to this calculation. You can specify the "all" group for this command if you simply want to include atoms with non-zero chunk IDs.

The simplest way to output the results of the compute vcm/chunk calculation to a file is to use the [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} command, for example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cc1 all chunk/atom molecule
    compute myChunk all vcm/chunk cc1
    fix 1 all ave/time 100 1 100 c_myChunk[*] file tmp.out mode vector
:::
::::
:::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global array where the number of rows is the number of chunks *Nchunk* as calculated by the specified [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command. The number of columns is 3 for the [\\((x,y,z)\\)]{.math .notranslate .nohighlight} center-of-mass velocity coordinates of each chunk. These values can be accessed by any command that uses global array values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The array values are "intensive". The array values will be in velocity [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

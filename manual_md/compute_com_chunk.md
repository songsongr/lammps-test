:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#compute-com-chunk-command .section}
[]{#index-0}

# compute com/chunk command[](#compute-com-chunk-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID com/chunk chunkID keyword args ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- com/chunk = style name of this compute command

- chunkID = ID of [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command

- zero or more keyword/value pairs may be appended

- keyword = *wrap*

  ``` literal-block
  wrap logical = wrap center of mass back to cell if argument is yes, true, on or 1, otherwise do not (default)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 fluid com/chunk molchunk
    compute 1 all com/chunk molchunk wrap on
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the center-of-mass for multiple chunks of atoms.

In LAMMPS, chunks are collections of atoms defined by a [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command, which assigns each atom to a single chunk (or no chunk). The ID for this command is specified as chunkID. For example, a single chunk could be the atoms in a molecule or atoms in a spatial bin. See the [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} and [[Howto chunk]{.doc}]Howto_chunk.md){.reference .internal} doc pages for details of how chunks can be defined and examples of how they can be used to measure properties of a system.

This compute calculates the [\\((x,y,z)\\)]{.math .notranslate .nohighlight} coordinates of the center of mass for each chunk, which includes all effects due to atoms passing through periodic boundaries.

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

If the *wrap* flag is used with an argument of *yes*, *true*, *on* or *1* the computed center of mass is wrapped back into the simulation cell. With an argument of *no*, *false*, *off* or 0 it is not (the default).

Note that only atoms in the specified group contribute to the calculation. The [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command defines its own group; atoms will have a chunk ID = 0 if they are not in that group, signifying they are not assigned to a chunk, and will thus also not contribute to this calculation. You can specify the "all" group for this command if you simply want to include atoms with non-zero chunk IDs.

::: {.admonition .note}
Note

The coordinates of an atom contribute to the chunk's center-of-mass in "unwrapped" form, by using the image flags associated with each atom. See the [[dump custom]{.doc}]dump.md){.reference .internal} command for a discussion of "unwrapped" coordinates. See the Atoms section of the [[read_data]{.doc}]read_data.md){.reference .internal} command for a discussion of image flags and how they are set for each atom. You can reset the image flags (e.g., to 0) before invoking this compute by using the [[reset_atoms image]{.doc}]reset_atoms.md){.reference .internal} or [[set image]{.doc}]set.md){.reference .internal} commands.
:::

The simplest way to output the results of the compute com/chunk calculation to a file is to use the [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} command, for example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cc1 all chunk/atom molecule
    compute myChunk all com/chunk cc1
    fix 1 all ave/time 100 1 100 c_myChunk[*] file tmp.out mode vector
:::
::::
:::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global array where the number of rows = the number of chunks *Nchunk* as calculated by the specified [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command. The number of columns is 3 for the [\\((x,y,z)\\)]{.math .notranslate .nohighlight} center-of-mass coordinates of each chunk. These values can be accessed by any command that uses global array values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The array values are "intensive". The array values will be in distance [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute com]{.doc}]compute_com.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

wrap = off
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

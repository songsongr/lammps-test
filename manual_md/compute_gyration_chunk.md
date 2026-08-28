:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#compute-gyration-chunk-command .section}
[]{#index-0}

# compute gyration/chunk command[](#compute-gyration-chunk-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID gyration/chunk chunkID keyword value ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- gyration/chunk = style name of this compute command

- chunkID = ID of [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command

- zero or more keyword/value pairs may be appended

- keyword = *tensor*

  ``` literal-block
  tensor value = none
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 molecule gyration/chunk molchunk
    compute 2 molecule gyration/chunk molchunk tensor
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the radius of gyration [\\(R_g\\)]{.math .notranslate .nohighlight} for multiple chunks of atoms.

In LAMMPS, chunks are collections of atoms defined by a [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command, which assigns each atom to a single chunk (or no chunk). The ID for this command is specified as chunkID. For example, a single chunk could be the atoms in a molecule or atoms in a spatial bin. See the [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} and [[Howto chunk]{.doc}]Howto_chunk.md){.reference .internal} doc pages for details of how chunks can be defined and examples of how they can be used to measure properties of a system.

This compute calculates the radius of gyration [\\(R_g\\)]{.math .notranslate .nohighlight} for each chunk, which includes all effects due to atoms passing through periodic boundaries.

[\\(R_g\\)]{.math .notranslate .nohighlight} is a measure of the size of a chunk, and is computed by the formula

::: {.math .notranslate .nohighlight}
\\\[R_g\^2 = \\frac{1}{M} \\sum_i m_i (r_i - r\_{\\text{cm}})\^2\\\]
:::

where [\\(M\\)]{.math .notranslate .nohighlight} is the total mass of the chunk, [\\(r\_{\\text{cm}}\\)]{.math .notranslate .nohighlight} is the center-of-mass position of the chunk, and the sum is over all atoms in the chunk.

Note that only atoms in the specified group contribute to the calculation. The [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command defines its own group; atoms will have a chunk ID = 0 if they are not in that group, signifying they are not assigned to a chunk, and will thus also not contribute to this calculation. You can specify the "all" group for this command if you simply want to include atoms with non-zero chunk IDs.

If the *tensor* keyword is specified, then the scalar [\\(R_g\\)]{.math .notranslate .nohighlight} value is not calculated, but an [\\(R_g\\)]{.math .notranslate .nohighlight} tensor is instead calculated for each chunk. The formula for the components of the tensor is the same as the above formula, except that [\\((r_i - r\_{\\text{cm}})\^2\\)]{.math .notranslate .nohighlight} is replaced by [\\((r\_{i,x} - r\_{\\text{cm},x}) \\cdot (r\_{i,y} - r\_{\\text{cm},y})\\)]{.math .notranslate .nohighlight} for the [\\(xy\\)]{.math .notranslate .nohighlight} component, and so on. The six components of the tensor are ordered [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}.

::: {.admonition .note}
Note

The coordinates of an atom contribute to [\\(R_g\\)]{.math .notranslate .nohighlight} in "unwrapped" form, by using the image flags associated with each atom. See the [[dump custom]{.doc}]dump.md){.reference .internal} command for a discussion of "unwrapped" coordinates. See the Atoms section of the [[read_data]{.doc}]read_data.md){.reference .internal} command for a discussion of image flags and how they are set for each atom. You can reset the image flags (e.g., to 0) before invoking this compute by using the [[set image]{.doc}]set.md){.reference .internal} command.
:::

The simplest way to output the results of the compute gyration/chunk calculation to a file is to use the [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} command, for example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cc1 all chunk/atom molecule
    compute myChunk all gyration/chunk cc1
    fix 1 all ave/time 100 1 100 c_myChunk file tmp.out mode vector
:::
::::
:::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector if the *tensor* keyword is not specified and a global array if it is. The length of the vector or number of rows in the array = the number of chunks *Nchunk* as calculated by the specified [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command. If the *tensor* keyword is specified, the global array has six columns. The vector or array can be accessed by any command that uses global values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

All the vector or array values calculated by this compute are "intensive". The vector or array values will be in distance [[units]{.doc}]units.md){.reference .internal}, since they are the square root of values represented by the formula above.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none

[[compute gyration]{.doc}]compute_gyration.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#compute-gyration-command .section}
[]{#index-0}

# compute gyration command[](#compute-gyration-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID gyration
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- gyration = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 molecule gyration
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the radius of gyration [\\(R_g\\)]{.math .notranslate .nohighlight} of the group of atoms, including all effects due to atoms passing through periodic boundaries.

[\\(R_g\\)]{.math .notranslate .nohighlight} is a measure of the size of the group of atoms, and is computed as the square root of the [\\(R_g\^2\\)]{.math .notranslate .nohighlight} value in this formula

::: {.math .notranslate .nohighlight}
\\\[R_g\^2 = \\frac{1}{M} \\sum_i m_i (r_i - r\_{\\text{cm}})\^2\\\]
:::

where [\\(M\\)]{.math .notranslate .nohighlight} is the total mass of the group, [\\(r\_{\\text{cm}}\\)]{.math .notranslate .nohighlight} is the center-of-mass position of the group, and the sum is over all atoms in the group.

A [\\(R_g\^2\\)]{.math .notranslate .nohighlight} tensor, stored as a 6-element vector, is also calculated by this compute. The formula for the components of the tensor is the same as the above formula, except that [\\((r_i - r\_{\\text{cm}})\^2\\)]{.math .notranslate .nohighlight} is replaced by [\\((r\_{i,x} - r\_{\\text{cm},x}) \\cdot (r\_{i,y} - r\_{\\text{cm},y})\\)]{.math .notranslate .nohighlight} for the [\\(xy\\)]{.math .notranslate .nohighlight} component, and so on. The six components of the vector are ordered [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}. Note that unlike the scalar [\\(R_g\\)]{.math .notranslate .nohighlight}, each of the six values of the tensor is effectively a "squared" value, since the cross-terms may be negative and taking a square root would be invalid.

::: {.admonition .note}
Note

The coordinates of an atom contribute to [\\(R_g\\)]{.math .notranslate .nohighlight} in "unwrapped" form, by using the image flags associated with each atom. See the [[dump custom]{.doc}]dump.md){.reference .internal} command for a discussion of "unwrapped" coordinates. See the Atoms section of the [[read_data]{.doc}]read_data.md){.reference .internal} command for a discussion of image flags and how they are set for each atom. You can reset the image flags (e.g., to 0) before invoking this compute by using the [[set image]{.doc}]set.md){.reference .internal} command.
:::
:::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar ([\\(R_g\\)]{.math .notranslate .nohighlight}) and a global vector of length 6 ([\\(R_g\^2\\)]{.math .notranslate .nohighlight} tensor), which can be accessed by indices 1--6. These values can be used by any command that uses a global scalar value or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar and vector values calculated by this compute are "intensive". The scalar and vector values will be in distance and distance[\\(\^2\\)]{.math .notranslate .nohighlight} [[units]{.doc}]units.md){.reference .internal}, respectively.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute gyration/chunk]{.doc}]compute_gyration_chunk.md){.reference .internal}, [[compute gyration/shape]{.doc}]compute_gyration_shape.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

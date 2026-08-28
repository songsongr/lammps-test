::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#compute-dipole-command .section}
[]{#index-1}[]{#index-0}

# compute dipole command[](#compute-dipole-command "Link to this heading"){.headerlink}
:::

:::::::::::::::: {#compute-dipole-tip4p-command .section}
# compute dipole/tip4p command[](#compute-dipole-tip4p-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID style arg
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- style = *dipole* or *dipole/tip4p*

- arg = *mass* or *geometry* = use COM or geometric center for charged chunk correction (optional)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 fluid dipole
    compute dw water dipole geometry
    compute dw water dipole/tip4p
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the dipole vector and total dipole for a group of atoms.

These computes calculate the x,y,z coordinates of the dipole vector and the total dipole moment for the atoms in the compute group. This includes all effects due to atoms passing through periodic boundaries. For a group with a net charge the resulting dipole is made position independent by subtracting the position vector of the center of mass or geometric center times the net charge from the computed dipole vector. Both per-atom charges and per-atom dipole moments, if present, contribute to the computed dipole.

::: versionadded
[Added in version 28Mar2023.]{.versionmodified .added}
:::

Compute *dipole/tip4p* includes adjustments for the charge carrying point M in molecules with TIP4P water geometry. The corresponding parameters are extracted from the pair style.

::: {.admonition .note}
Note

The coordinates of an atom contribute to the dipole in "unwrapped" form, by using the image flags associated with each atom. See the [[dump custom]{.doc}]dump.md){.reference .internal} command for a discussion of "unwrapped" coordinates. See the Atoms section of the [[read_data]{.doc}]read_data.md){.reference .internal} command for a discussion of image flags and how they are set for each atom. You can reset the image flags (e.g., to 0) before invoking this compute by using the [[set image]{.doc}]set.md){.reference .internal} command.
:::
:::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

These computes calculate a global scalar containing the magnitude of the computed dipole moment and a global vector of length 3 with the dipole vector. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The computed values are "intensive". The array values will be in dipole units (i.e., charge [[units]{.doc}]units.md){.reference .internal} times distance [[units]{.doc}]units.md){.reference .internal}).
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Compute style *dipole/tip4p* is part of the EXTRA-COMPUTE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Compute style *dipole/tip4p* can only be used with tip4p pair styles.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute dipole/chunk]{.doc}]compute_dipole_chunk.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

Using the center of mass is the default setting for the net charge correction.
:::
::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

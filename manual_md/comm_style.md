::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#comm-style-command .section}
[]{#index-0}

# comm_style command[](#comm-style-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    comm_style style
:::
::::

- style = *brick* or *tiled*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    comm_style brick
    comm_style tiled
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command sets the style of inter-processor communication of atom information that occurs each timestep as coordinates and other properties are exchanged between neighboring processors and stored as properties of ghost atoms.

For the default *brick* style, the domain decomposition used by LAMMPS to partition the simulation box must be a regular 3d grid of bricks, one per processor. Each processor communicates with its 6 Cartesian neighbors in the grid to acquire information for nearby atoms.

For the *tiled* style, a more general domain decomposition can be used, as triggered by the [[balance]{.doc}]balance.md){.reference .internal} or [[fix balance]{.doc}]fix_balance.md){.reference .internal} commands. The simulation box can be partitioned into non-overlapping rectangular-shaped "tiles" or varying sizes and shapes. Again there is one tile per processor. To acquire information for nearby atoms, communication must now be done with a more complex pattern of neighboring processors.

Note that this command does not actually define a partitioning of the simulation box (a domain decomposition), rather it determines what kinds of decompositions are allowed and the pattern of communication used to enable the decomposition. A decomposition is created when the simulation box is first created, via the [[create_box]{.doc}]create_box.md){.reference .internal} or [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands. For both the *brick* and *tiled* styles, the initial decomposition will be the same, as described by [[create_box]{.doc}]create_box.md){.reference .internal} and [[processors]{.doc}]processors.md){.reference .internal} commands. The decomposition can be changed via the [[balance]{.doc}]balance.md){.reference .internal} or [[fix balance]{.doc}]fix_balance.md){.reference .internal} commands.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[comm_modify]{.doc}]comm_modify.md){.reference .internal}, [[processors]{.doc}]processors.md){.reference .internal}, [[balance]{.doc}]balance.md){.reference .internal}, [[fix balance]{.doc}]fix_balance.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default style is brick.
:::
:::::::::::::
::::::::::::::
:::::::::::::::

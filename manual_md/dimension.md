:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#dimension-command .section}
[]{#index-0}

# dimension command[](#dimension-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dimension N
:::
::::

- N = 2 or 3
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dimension 2
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set the dimensionality of the simulation. By default LAMMPS runs 3d simulations. To run a 2d simulation, this command should be used prior to setting up a simulation box via the [[create_box]{.doc}]create_box.md){.reference .internal} or [[read_data]{.doc}]read_data.md){.reference .internal} commands. Restart files also store this setting.

See the discussion on the [[Howto 2d]{.doc}]Howto_2d.md){.reference .internal} page for additional instructions on how to run 2d simulations.

::: {.admonition .note}
Note

Some models in LAMMPS treat particles as finite-size spheres or ellipsoids, as opposed to point particles. In 2d, the particles will still be spheres or ellipsoids, not circular disks or ellipses, meaning their moment of inertia will be the same as in 3d.
:::
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command must be used before the simulation box is defined by a [[read_data]{.doc}]read_data.md){.reference .internal} or [[create_box]{.doc}]create_box.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix enforce2d]{.doc}]fix_enforce2d.md){.reference .internal}
:::

::::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dimension 3
:::
::::
:::::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

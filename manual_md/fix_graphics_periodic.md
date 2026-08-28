::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#fix-graphics-periodic-command .section}
[]{#index-0}

# fix graphics/periodic command[](#fix-graphics-periodic-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID graphics/periodic Nevery keyword args ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- graphics/periodic = style name of this fix command

- Nevery = update graphics information every this many time steps

- zero or more keywords or keyword/value pairs may be appended

- keyword = *xlo* or *xhi* or *ylo* or *yhi* or *zlo* or *zhi* or *radius* or *atoms* or *bonds*

  ``` literal-block
  xlo, xhi, ylo, yhi, zlo, zhi = enable periodic images of atoms and bonds to either side of the simulation box in the given direction
  radius value = sets the atom radius
     value = either "auto" or a number (distance units)
  atoms yes/no = enables or disables displaying periodic images of atoms
  bonds yes/no = enables or disables displaying periodic images of bonds
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix vec all graphics/periodic 10 ylo zhi zlo yhi xlo
    fix vec all graphics/periodic 1000 ylo zhi zlo yhi bonds no radius 0.5
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

This fix allows to add graphics of periodic images of atoms and bonds to [[dump image]{.doc}]dump_image.md){.reference .internal} images using the *fix* keyword. This can be useful to visualize periodic systems.

The *group-ID* sets the group ID of the atoms selected to be displayed as periodic images. For bonds to be displayed, *both* atoms of the bond have to be inside the group.

The *Nevery* keyword determines how often the periodic graphics data is updated. This should be the same value as the corresponding *N* parameter of the [[dump]{.doc}]dump.md){.reference .internal} image command. LAMMPS will stop with an error message if the settings for this fix and the dump command are not compatible.

The *xlo*, *xhi*, *ylo*, *yhi*, *zlo*, *zhi* keywords, if set, enable display of a periodic image of the system to the corresponding side in the corresponding direction of the principal simulations cell. If all keywords are used, there will be 26 additional copies of the system rendered.

The *radius* keyword determines the radius of the atoms. If a value of "auto" is used, the radius is inherited from the atom type.
::::

------------------------------------------------------------------------

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

Fix graphics/periodic is designed to be used with the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix adds graphics objects of periodic images of atoms and bonds in the fix group to *dump image* so that they are included in the rendered image.

The color of the atoms and bonds is by default the same as that of the atoms and bonds in the principal simulation cell when using color styles "type" or "element" with the fix command. With fix color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

The *fflag1* setting of dump of *dump image fix* determines if the bonds are capped with spheres: a value of 0 means no caps, a value of 1 a cap at the lower end, a value of 2 a cap at the upper end, and a value of 3 caps at both ends. When also replicating atoms, a value other than 0 would be redundant, otherwise a value of 3 is probably the desired choice.

The *fflag2* settings of *dump image fix* allows to modify the bond diameter relative to the automatically chosen one. In most use cases a value of 0.0 is probably the desired choice.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options apply to this fix.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the GRAPHICS package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Currently only periodic images of atoms and bonds in each direction can be displayed.

Body particles or ellipsoids and similar are not fully supported; they are shown as spheres with this fix.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix graphics/arrows]{.doc}]fix_graphics_arrows.md){.reference .internal}, [[fix graphics/labels]{.doc}]fix_graphics_labels.md){.reference .internal}, [[fix graphics/lines]{.doc}]fix_graphics_lines.md){.reference .internal}, [[fix graphics/isosurface]{.doc}]fix_graphics_isosurface.md){.reference .internal}, [[fix graphics/objects]{.doc}]fix_graphics_objects.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

radius = auto, atoms = yes, bonds = yes, if supported by atom style otherwise no, no periodic graphics
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

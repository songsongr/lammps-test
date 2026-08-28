:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-graphics-lines-command .section}
[]{#index-0}

# fix graphics/lines command[](#fix-graphics-lines-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID graphics/lines Nevery Nrepeat Nfreq Nlength
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- graphics/lines = style name of this fix command

- Nevery = retrieve unwrapped position information every this many timesteps

- Nrepeat = number of times to use the position information for calculating averages

- Nfreq = store position averages every this many timesteps

- Nlength = length of averaged position history
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix  lines  ogroup  graphics/lines 10 50 500 15
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

This fix allows to add a trace of averaged atom positions in the fix group to images rendered with [[dump image]{.doc}]dump_image.md){.reference .internal} using the *fix* keyword. This kind of position trace is sometimes referred to as "trajectory lines".

The trace is represented by a chain of connected cylinders where the endpoints are taken from the current atom positions and an internal history of averaged positions of the atoms. The averaging is performed by using [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal} internally on unwrapped atom positions taken from [[compute property/atom]{.doc}]compute_property_atom.md){.reference .internal}. The *Nevery*, *Nrepeat*, and *Nfreq* values are passed on to the internal fix *ave/atom* instance for averaging. The averaged unwrapped positions are wrapped back into the simulation box and stored internally using up to *Nlength* sets. For any additional sets of positions, the then oldest set in the history storage will be overwritten and thus limiting the length of the trace.

The *group-ID* sets the group ID of the atoms selected to have the selected property represented. This may *not* be a dynamic group.

The *Nfreq* value determines how often the graphics data is updated. This should be the same value as the corresponding *N* parameter of the [[dump]{.doc}]dump.md){.reference .internal} image command. LAMMPS will stop with an error message if the settings for this fix and the dump command are not compatible.
::::

------------------------------------------------------------------------

::::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

Fix graphics/lines is designed to be used with the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix will add a connected chain of cylinders based on the averaged position history of the atoms in the fix group to the rendered image.

The color of the cylinders is by default that of the atoms when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

The *fflag1* setting of *dump image fix* determines whether the cylinder objects are capped with spheres: 0 means no caps, 1 means the lower end is capped, 2 means the upper end is capped, and 3 means both ends are capped.

The *fflag2* setting determines the diameter of the cylinders.

The following input can be added to the [`examples/obstacle/in.obstacle`{.docutils .literal .notranslate}]{.pre} example input after adjusting its [[create_box]{.doc}]create_box.md){.reference .internal} and [[mass]{.doc}]mass.md){.reference .internal} commands to support 4 atom types instead of 3.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # select atoms to trace and assign atom type 4 so they have a different color (yellow)
    region   trace block 2 3 1.25 8.75 INF INF
    group    trace region trace
    set      group trace type 4

    # create trajectory lines by averaging positions over 10 MD steps each 10 steps apart
    fix      lines trace graphics/lines 10 10 100 25
    # visualize the trace in silver with a diameter of 0.6 which is half of that of the atoms
    dump     viz   all image 100 obstacle-*.png type type size 800 600 zoom 2.5 center s 0.50 0.7 0 &
                                            shiny 0.5 fsaa yes box no 0.025 fix lines const 1 0.6
    dump_modify  viz  pad 6 backcolor darkgray adiam * 1.2 fcolor lines silver
:::
::::

[![lines1](_images/lines-start.png){style="width: 33%;"}](_images/lines-start.png){.reference .internal} [![lines2](_images/lines-mid.png){style="width: 33%;"}](_images/lines-mid.png){.reference .internal} [![lines3](_images/lines-end.png){style="width: 33%;"}](_images/lines-end.png){.reference .internal}

(Trajectory lines visualization example. Click to see the full-size images)

\
:::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes its current status to [[binary restart files]{.doc}]restart.md){.reference .internal}. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the fix continues in an uninterrupted fashion. Upon restarting, the fix checks that the *Nevery*, *Nrepeat*, *Nfreq*, and *Nlength* settings are the same as when the restart file was written. Otherwise it stops with an error.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options apply to this fix.

This fix computes a global scalar representing the current length of the position history vector.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the GRAPHICS package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix graphics/arrows]{.doc}]fix_graphics_arrows.md){.reference .internal}, [[fix graphics/isosurface]{.doc}]fix_graphics_isosurface.md){.reference .internal}, [[fix graphics/labels]{.doc}]fix_graphics_labels.md){.reference .internal}, [[fix graphics/objects]{.doc}]fix_graphics_objects.md){.reference .internal}, [[fix graphics/periodic]{.doc}]fix_graphics_periodic.md){.reference .internal}, [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal}
:::

::: {#defaults .section}
## Defaults[](#defaults "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

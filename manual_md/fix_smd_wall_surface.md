:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-smd-wall-surface-command .section}
[]{#index-0}

# fix smd/wall_surface command[](#fix-smd-wall-surface-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID smd/wall_surface arg type mol-ID
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- smd/wall_surface = style name of this fix command

- arg = *file*

  ``` literal-block
  file = file name of a triangular mesh in stl format
  ```

- type = particle type to be given to the new particles created by this fix

- mol-ID = molecule-ID to be given to the new particles created by this fix (must be \>= 65535)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix stl_surf all smd/wall_surface tool.stl 2 65535
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix creates reads a triangulated surface from a file in .STL format. For each triangle, a new particle is created which stores the barycenter of the triangle and the vertex positions. The radius of the new particle is that of the minimum circle which encompasses the triangle vertices.

The triangulated surface can be used as a complex rigid wall via the [[smd/tri_surface]{.doc}]pair_smd_triangulated_surface.md){.reference .internal} pair style. It is possible to move the triangulated surface via the [[smd/move_tri_surf]{.doc}]fix_smd_move_triangulated_surface.md){.reference .internal} fix style.

Immediately after a .STL file has been read, the simulation needs to be run for 0 timesteps in order to properly register the new particles in the system. See the "funnel_flow" example in the MACHDYN examples directory.

See [this PDF guide](PDF/MACHDYN_LAMMPS_userguide.pdf){.reference .external} to use Smooth Mach Dynamics in LAMMPS.
:::

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

Fix *smd/wall_surface* supports the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix will pass geometry information about the wall particles to *dump image* so that they be included in the rendered image.

The color of the wall mesh object is by default that of the first atom type when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

The *fflag1* setting of *dump image fix* determines whether the wall will be rendered as a set of connected triangles (1) or as a mesh of cylinders (2).

When rendering triangles, the *fflag2* setting is ignored. When using a mesh of cylinders, the *fflag2* setting determines the diameter of the cylinders.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

Currently, no part of MACHDYN supports restarting nor minimization. This fix has no outputs.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MACHDYN package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The molecule ID given to the particles created by this fix have to be equal to or larger than 65535.

Within each .STL file, only a single triangulated object must be present, even though the STL format allows for the possibility of multiple objects in one file.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[smd/triangle_mesh_vertices]{.doc}]compute_smd_triangle_vertices.md){.reference .internal}, [[smd/move_tri_surf]{.doc}]fix_smd_move_triangulated_surface.md){.reference .internal}, [[smd/tri_surface]{.doc}]pair_smd_triangulated_surface.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-smd-move-tri-surf-command .section}
[]{#index-0}

# fix smd/move_tri_surf command[](#fix-smd-move-tri-surf-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID smd/move_tri_surf keyword
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- smd/move_tri_surf keyword = style name of this fix command

- keyword = *\*LINEAR* or *\*WIGGLE* or *\*ROTATE*

  ``` literal-block
  *LINEAR args = Vx Vy Vz
     Vx,Vy,Vz = components of velocity vector (velocity units), any component can be specified as NULL
  *WIGGLE args = Vx Vy Vz max_travel
     vx,vy,vz = components of velocity vector (velocity units), any component can be specified as NULL
     max_travel = wiggle amplitude
  *ROTATE args = Px Py Pz Rx Ry Rz period
     Px,Py,Pz = origin point of axis of rotation (distance units)
     Rx,Ry,Rz = axis of rotation vector
     period = period of rotation (time units)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 tool smd/move_tri_surf *LINEAR 20 20 10
    fix 2 tool smd/move_tri_surf *WIGGLE 20 20 10
    fix 2 tool smd/move_tri_surf *ROTATE 0 0 0 5 2 1
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix applies only to rigid surfaces read from .STL files via fix [[smd/wall_surface]{.doc}]fix_smd_wall_surface.md){.reference .internal} . It updates position and velocity for the particles in the group each timestep without regard to forces on the particles. The rigid surfaces can thus be moved along simple trajectories during the simulation.

The *\*LINEAR* style moves particles with the specified constant velocity vector V = (Vx,Vy,Vz). This style also sets the velocity of each particle to V = (Vx,Vy,Vz).

The *\*WIGGLE* style moves particles in an oscillatory fashion. Particles are moved along (vx, vy, vz) with constant velocity until a displacement of max_travel is reached. Then, the velocity vector is reversed. This process is repeated.

The *\*ROTATE* style rotates particles around a rotation axis R = (Rx,Ry,Rz) that goes through a point P = (Px,Py,Pz). The period of the rotation is also specified. This style also sets the velocity of each particle to (omega cross Rperp) where omega is its angular velocity around the rotation axis and Rperp is a perpendicular vector from the rotation axis to the particle.

See [this PDF guide](PDF/MACHDYN_LAMMPS_userguide.pdf){.reference .external} to using Smooth Mach Dynamics in LAMMPS.
:::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

Currently, no part of MACHDYN supports restarting nor minimization. This fix has no outputs.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MACHDYN package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[smd/triangle_mesh_vertices]{.doc}]compute_smd_triangle_vertices.md){.reference .internal}, [[smd/wall_surface]{.doc}]fix_smd_wall_surface.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#fix-graphics-arrows-command .section}
[]{#index-0}

# fix graphics/arrows command[](#fix-graphics-arrows-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID graphics/arrows Nevery mode keyword args ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- graphics/arrows = style name of this fix command

- Nevery = update graphics information every this many time steps

- mode = one of the following modes *dipole* or *force* or *velocity* or *variable* or *chunk*

  ``` literal-block
  dipole args = scale radius
    scale = scale factor for the dipole moment to determine the arrow length
    radius = radius for arrows (length units)
  force args = scale radius
    scale = scale factor for the force vector to determine the arrow length
    radius = radius for arrows (length units)
  velocity args = scale radius
    scale = scale factor for the velocity vector to determine the arrow length
    radius = radius for arrows (length units)
  variable args = xval yval zval radius
    xval = x value for arrow vector (may be a variable)
    yval = y value for arrow vector (may be a variable)
    zval = z value for arrow vector (may be a variable)
    radius = radius for arrows (length units)
  chunk args = chunk-ID pos-ID vec-ID scale radius
    chunk-ID = ID of compute chunk/atom command
    pos-ID = ID of a per-chunk compute that computes the positions for the arrows
    vec-ID = ID of a per-chunk compute that computes the arrow vectors
    scale = scale factor for the per-chunk vector to determine the arrow length
    radius = radius for arrows (length units)
  ```

- zero or more keyword/value pairs may be appended

- keyword = *autoscale*

  ``` literal-block
  autoscale value = automatically scale arrows so they have an average length of "value"
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix vec all graphics/arrows 10 velocity 20.0 0.066 autoscale 0.5
    fix vec all graphics/arrows 100 variable v_xnorm v_znorm 0.0 0.066
    fix vec all graphics/arrows 100 chunk molchunk com dip 1.0 0.05
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

This fix allows to add arrows to images rendered with [[dump image]{.doc}]dump_image.md){.reference .internal} using the *fix* keyword to represent vector properties with arrows for either all atoms in the fix group or for [[chunks]{.doc}]Howto_chunk.md){.reference .internal}.

The *group-ID* sets the group ID of the atoms selected to have the selected property represented. This may be a dynamic group.

The *Nevery* keyword determines how often the arrows graphics data is updated. This should be the same value as the corresponding *N* parameter of the [[dump]{.doc}]dump.md){.reference .internal} image command. LAMMPS will stop with an error message if the settings for this fix and the dump command are not compatible.

There are five keywords available that determine what is shown: *dipole* will show the per-atom dipole vector, *force* the per-atom force, *velocity* the per-atom velocity, *variable* a custom vector constructed from three constants or atom- or equal-style variables. With the *chunk* keyword the arrows shown will represent per-chunk vector data.

The *xval*, *yval*, and *zval*, arguments to the *variable* mode define a custom vector that can be composed of numbers or [[atom- or equal-style variables]{.doc}]variable.md){.reference .internal}. If any of these values is a variable, it should be specified as *v_name*, where "name" is the variable name. In this case, the variable will be evaluated each timestep, and its value used to define the arrow for each atom. Since variables can reference [[computes]{.doc}]compute.md){.reference .internal}, [[fixes]{.doc}]fix.md){.reference .internal}, [[custom per-atom properties]{.doc}]fix_property_atom.md){.reference .internal}, and other variables, this can be used to construct arrows for almost any per-atom property available in LAMMPS.

The *chunk-ID* is the ID of a [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command. In LAMMPS, chunks are collections of atoms and there are per-chunk computes that compute properties for them. See the [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} and [[Howto chunk]{.doc}]Howto_chunk.md){.reference .internal} pages for details of how chunks can be defined and examples of how they can be used to measure properties of a system.

The *pos-ID* is the ID of a per-chunk [[compute command]{.doc}]compute.md){.reference .internal}. Most commonly this will be either [[compute com/chunk]{.doc}]compute_com_chunk.md){.reference .internal} for "mobile" chunks or compute [[compute property/chunk]{.doc}]compute_property_chunk.md){.reference .internal} for binning based chunks. The *vec-ID* is the ID of a per-chunk [[compute command]{.doc}]compute.md){.reference .internal}. Either per-chunk compute must return a global array with at least 3 columns and *only* the first three columns are used for the arrows. For computes that compute a tensor only the trace of the tensor is used. Currently the following computes are compatible:

> ::: {}
> - [[angmom/chunk]{.doc}]compute_angmom_chunk.md){.reference .internal}
>
> - [[com/chunk]{.doc}]compute_com_chunk.md){.reference .internal}
>
> - [[dipole/chunk]{.doc}]compute_dipole_chunk.md){.reference .internal}
>
> - [[dipole/tip4p/chunk]{.doc}]compute_dipole_chunk.md){.reference .internal}
>
> - [[gyration/chunk]{.doc}]compute_gyration_chunk.md){.reference .internal} (with optional *tensor* keyword)
>
> - [[gyration/shape/chunk]{.doc}]compute_gyration_shape_chunk.md){.reference .internal}
>
> - [[inertia/chunk]{.doc}]compute_inertia_chunk.md){.reference .internal}
>
> - [[msd/chunk]{.doc}]compute_msd_chunk.md){.reference .internal}
>
> - [[omega/chunk]{.doc}]compute_omega_chunk.md){.reference .internal}
>
> - [[property/chunk]{.doc}]compute_property_chunk.md){.reference .internal} (with arguments *coord1* *coord2* *coord3*)
>
> - [[reduce/chunk]{.doc}]compute_reduce_chunk.md){.reference .internal} (with three or more properties)
>
> - [[torque/chunk]{.doc}]compute_torque_chunk.md){.reference .internal}
>
> - [[vacf/chunk]{.doc}]compute_vacf_chunk.md){.reference .internal}
>
> - [[vcm/chunk]{.doc}]compute_vcm_chunk.md){.reference .internal}
> :::

The *scale* quantity determines the length of the arrows. It should be chosen so that when multiplied with the per-atom vector quantity the result is of the same order of magnitude as atom positions, so that the vectors can be seen well.

The *radius* quantity determines the width of the arrows.

The optional *autoscale* keyword allows to dynamically determine the *scale* quantity so that the average length of the arrows is set to the value of the keyword's argument. The computed scale factor can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal} as a global scalar (see below).
::::

------------------------------------------------------------------------

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

Fix graphics/arrows is designed to be used with the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix will add arrows based on the atoms in the fix group or based on chunks to *dump image* so that they are included in the rendered image.

The color of the arrows is by default that of the atoms when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

The *fflag1* setting of *dump image fix* allows to adjust the length of the arrows. Since that value is already set or computed by the fix, *fflag1* should be set to 0.0.

The *fflag2* setting allows you to adjust the radius of the rendered arrows. Since the radius of the arrows is an input parameter for this fix, it is recommended to set this flag to 0.0.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options apply to this fix.

This fix computes a global scalar representing the current scale factor for displaying the arrows, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. This is the *autoscale* keyword argument value divided by the average length of the selected vector property. If the *autoscale* keyword is not used, it is the scale value set by the *fix graphics/arrows* command or 1.0. The scalar value calculated by this fix is "intensive".
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the GRAPHICS package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The *dipole* mode requires the use of [[atom style dipole]{.doc}]atom_style.md){.reference .internal} or a hybrid atom style that includes it.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix graphics/labels]{.doc}]fix_graphics_labels.md){.reference .internal}, [[fix graphics/isosurface]{.doc}]fix_graphics_isosurface.md){.reference .internal}, [[fix graphics/lines]{.doc}]fix_graphics_lines.md){.reference .internal}, [[fix graphics/objects]{.doc}]fix_graphics_objects.md){.reference .internal}, [[fix graphics/periodic]{.doc}]fix_graphics_periodic.md){.reference .internal}, [[compute hbond/local]{.doc}]compute_hbond_local.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

autoscale is off by default
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

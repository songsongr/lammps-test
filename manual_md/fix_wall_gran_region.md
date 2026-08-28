::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#fix-wall-gran-region-command .section}
[]{#index-0}

# fix wall/gran/region command[](#fix-wall-gran-region-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID wall/gran/region fstyle fstyle_params wallstyle regionID keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- wall/region = style name of this fix command

- fstyle = style of force interactions between particles and wall

  :::: {.highlight-none .notranslate}
  ::: highlight
      possible choices: hooke, hooke/history, hertz/history, granular
  :::
  ::::

- fstyle_params = parameters associated with force interaction style

  ``` literal-block
  For hooke, hooke/history, and hertz/history, fstyle_params are:
        Kn = elastic constant for normal particle repulsion (force/distance units or pressure units - see discussion below)
        Kt = elastic constant for tangential contact (force/distance units or pressure units - see discussion below)
        gamma_n = damping coefficient for collisions in normal direction (1/time units or 1/time-distance units - see discussion below)
        gamma_t = damping coefficient for collisions in tangential direction (1/time units or 1/time-distance units - see discussion below)
        xmu = static yield criterion (unitless value between 0.0 and 1.0e4)
        dampflag = 0 or 1 if tangential damping force is excluded or included
  ```

  ``` literal-block
  For granular, fstyle_params are set using the same syntax as for the pair_coeff command of pair_style granular
  ```

- wallstyle = region (see [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal} for options for other kinds of walls)

- region-ID = region whose boundary will act as wall

- keyword = *contacts* or *temperature*

  ``` literal-block
  contacts value = none
     generate contact information for each particle
  temperature value = temperature
     specify temperature of wall
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix wall all wall/gran/region hooke/history 1000.0 200.0 200.0 100.0 0.5 1 region myCone
    fix 3 all wall/gran/region granular hooke 1000.0 50.0 tangential linear_nohistory 1.0 0.4 damping velocity region myBox
    fix 4 all wall/gran/region granular jkr 1e5 1500.0 0.3 10.0 tangential mindlin NULL 1.0 0.5 rolling sds 500.0 200.0 0.5 twisting marshall region myCone
    fix 5 all wall/gran/region granular dmt 1e5 0.2 0.3 10.0 tangential mindlin NULL 1.0 0.5 rolling sds 500.0 200.0 0.5 twisting marshall damping tsuji region myCone
    fix wall all wall/gran/region hooke/history 1000.0 200.0 200.0 100.0 0.5 1 region myCone contacts
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Treat the surface of the geometric region defined by the *region-ID* as a bounding frictional wall which interacts with nearby finite-size granular particles when they are close enough to touch the wall. See the [[fix wall/region]{.doc}]fix_wall_region.md){.reference .internal} and [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal} commands for related kinds of walls for non-granular particles and simpler wall geometries, respectively.

Here are snapshots of example models using this command. Corresponding input scripts can be found in examples/granregion. Movies of these simulations are [here on the Movies page](https://www.lammps.org/movies.html#granregion){.reference .external} of the LAMMPS website.

[![wallgran1](_images/gran_funnel.png){style="width: 48%;"}](_images/gran_funnel.png){.reference .internal} [![wallgran2](_images/gran_mixer.png){style="width: 48%;"}](_images/gran_mixer.png){.reference .internal}

Click on the images to see a bigger picture.

------------------------------------------------------------------------

The distance between a particle and the region boundary is the distance to the nearest point on the region surface. The force the wall exerts on the particle is along the direction between that point and the particle center, which is the direction normal to the surface at that point. Note that if the region surface is comprised of multiple "faces", then each face can exert a force on the particle if it is close enough. E.g. for [[region_style block]{.doc}]region.md){.reference .internal}, a particle in the interior, near a corner of the block, could feel wall forces from 1, 2, or 3 faces of the block.

Regions are defined using the [[region]{.doc}]region.md){.reference .internal} command. Note that the region volume can be interior or exterior to the bounding surface, which will determine in which direction the surface interacts with particles, i.e. the direction of the surface normal. The exception to this is if one or more *open* options are specified for the region command, in which case particles interact with both the interior and exterior surfaces of regions.

Regions can either be primitive shapes (block, sphere, cylinder, etc) or combinations of primitive shapes specified via the *union* or *intersect* region styles. These latter styles can be used to construct particle containers with complex shapes.

Regions can also move dynamically via the [[region]{.doc}]region.md){.reference .internal} command keywords (move) and *rotate*, or change their shape by use of variables as inputs to the [[region]{.doc}]region.md){.reference .internal} command. If such a region is used with this fix, then the region surface will move in time in the corresponding manner.

::: {.admonition .note}
Note

As discussed on the [[region]{.doc}]region.md){.reference .internal} command doc page, regions in LAMMPS do not get wrapped across periodic boundaries. It is up to you to ensure that the region location with respect to periodic or non-periodic boundaries is specified appropriately via the [[region]{.doc}]region.md){.reference .internal} and [[boundary]{.doc}]boundary.md){.reference .internal} commands when using a region as a wall that bounds particle motion.
:::

::: {.admonition .note}
Note

For primitive regions with sharp corners and/or edges (e.g. a block or cylinder), wall/particle forces are computed accurately for both interior and exterior regions. For *union* and *intersect* regions, additional sharp corners and edges may be present due to the intersection of the surfaces of 2 or more primitive volumes. These corners and edges can be of two types: concave or convex. Concave points/edges are like the corners of a cube as seen by particles in the interior of a cube. Wall/particle forces around these features are computed correctly. Convex points/edges are like the corners of a cube as seen by particles exterior to the cube, i.e. the points jut into the volume where particles are present. LAMMPS does NOT compute the location of these convex points directly, and hence wall/particle forces in the cutoff volume around these points suffer from inaccuracies. The basic problem is that the outward normal of the surface is not continuous at these points. This can cause particles to feel no force (they don't "see" the wall) when in one location, then move a distance epsilon, and suddenly feel a large force because they now "see" the wall. In a worst-case scenario, this can blow particles out of the simulation box. Thus, as a general rule you should not use the fix wall/gran/region command with *union* or *interesect* regions that have convex points or edges resulting from the union/intersection (convex points/edges in the union/intersection due to a single sub-region are still OK).
:::

::: {.admonition .note}
Note

Similarly, you should not define *union* or *intersert* regions for use with this command that share an overlapping common face that is part of the overall outer boundary (interior boundary is OK), even if the face is smooth. E.g. two regions of style block in a *union* region, where the two blocks overlap on one or more of their faces. This is because LAMMPS discards points that are part of multiple sub-regions when calculating wall/particle interactions, to avoid double-counting the interaction. Having two coincident faces could cause the face to become invisible to the particles. The solution is to make the two faces differ by epsilon in their position.
:::

The nature of the wall/particle interactions are determined by the *fstyle* setting. It can be any of the styles defined by the [[pair_style gran/\*]{.doc}]pair_gran.md){.reference .internal} or the more general [[pair_style granular]{.doc}]pair_granular.md){.reference .internal} commands. Currently the options are *hooke*, *hooke/history*, or *hertz/history* for the former, and *granular* with all the possible options of the associated *pair_coeff* command for the latter. The equation for the force between the wall and particles touching it is the same as the corresponding equation on the [[pair_style gran/\*]{.doc}]pair_gran.md){.reference .internal} and [[pair_style granular]{.doc}]pair_granular.md){.reference .internal} doc pages, but the effective radius is calculated using the radius of the particle and the radius of curvature of the wall at the contact point.

Specifically, delta = radius - r = overlap of particle with wall, m_eff = mass of particle, and RiRj/Ri+Rj is the effective radius, with Rj replaced by the radius of curvature of the wall at the contact point. The radius of curvature can be negative for a concave wall section, e.g. the interior of cylinder. For a flat wall, delta = radius - r = overlap of particle with wall, m_eff = mass of particle, and the effective radius of contact is just the radius of the particle.

The parameters *Kn*, *Kt*, *gamma_n*, *gamma_t*, *xmu*, *dampflag*, and the optional keyword *limit_damping* have the same meaning and units as those specified with the [[pair_style gran/\*]{.doc}]pair_gran.md){.reference .internal} commands. This means a NULL can be used for either *Kt* or *gamma_t* as described on that page. If a NULL is used for *Kt*, then a default value is used where *Kt* = 2/7 *Kn*. If a NULL is used for *gamma_t*, then a default value is used where *gamma_t* = 1/2 *gamma_n*.

All the model choices for cohesion, tangential friction, rolling friction and twisting friction supported by the [[pair_style granular]{.doc}]pair_granular.md){.reference .internal} through its *pair_coeff* command are also supported for walls. These are discussed in greater detail on the doc page for [[pair_style granular]{.doc}]pair_granular.md){.reference .internal}.

Note that you can choose a different force styles and/or different values for the 6 wall/particle coefficients than for particle/particle interactions. E.g. if you wish to model the wall as a different material.

The *temperature* keyword is used to assign a temperature to the wall. The following value can either be a numeric value or an equal-style [[variable]{.doc}]variable.md){.reference .internal}. If the value is a variable, it should be specified as v_name, where name is the variable name. In this case, the variable will be evaluated each timestep, and its value used to determine the temperature. This option must be used in conjunction with a heat conduction model defined in [[pair_style granular]{.doc}]pair_granular.md){.reference .internal}, [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal} to store temperature and a heat flow, and [[fix heat/flow]{.doc}]fix_heat_flow.md){.reference .internal} to integrate heat flow.
::::::

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

Similar to [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal} command, this fix writes the shear friction state of atoms interacting with the wall to [[binary restart files]{.doc}]restart.md){.reference .internal}, so that a simulation can continue correctly if granular potentials with shear "history" effects are being used. This fix also includes info about a moving region in the restart file. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

::: {.admonition .note}
Note

Information about region definitions is NOT included in restart files, as discussed on the [[read_restart]{.doc}]read_restart.md){.reference .internal} doc page. So you must re-define your region and if it is a moving region, define its motion attributes in a way that is consistent with the simulation that wrote the restart file. In particular, if you want to change the region motion attributes (e.g. its velocity), then you should ensure the position/orientation of the region at the initial restart timestep is the same as it was on the timestep the restart file was written. If this is not possible, you may need to ignore info in the restart file by defining a new fix wall/gran/region command in your restart script, e.g. with a different fix ID. Or if you want to keep the shear history info but discard the region motion information, you can use the same fix ID for fix wall/gran/region, but assign it a region with a different region ID.
:::

If the [`contacts`{.code .docutils .literal .notranslate}]{.pre} option is used, this fix generates a per-atom array with at least 8 columns as output, containing the contact information for owned particles (nlocal on each processor). All columns in this per-atom array will be zero if no contact has occurred. The first 8 values of these columns are listed in the following table.

  Index   Value                                                                            Units
  ------- -------------------------------------------------------------------------------- ----------------
  1       1.0 if particle is in contact with wall, 0.0 otherwise                           
  2       Force [\\(f_x\\)]{.math .notranslate .nohighlight} exerted by the wall           force units
  3       Force [\\(f_y\\)]{.math .notranslate .nohighlight} exerted by the wall           force units
  4       Force [\\(f_z\\)]{.math .notranslate .nohighlight} exerted by the wall           force units
  5       [\\(x\\)]{.math .notranslate .nohighlight}-coordinate of contact point on wall   distance units
  6       [\\(y\\)]{.math .notranslate .nohighlight}-coordinate of contact point on wall   distance units
  7       [\\(z\\)]{.math .notranslate .nohighlight}-coordinate of contact point on wall   distance units
  8       Radius [\\(r\\)]{.math .notranslate .nohighlight} of atom                        distance units

If a granular sub-model calculates additional contact information (e.g. the heat sub-models calculate the amount of heat exchanged), these quantities are appended to the end of this array. First, any extra values from the normal sub-model are appended followed by the damping, tangential, rolling, twisting, then heat models. See the descriptions of granular sub-models in the [[pair granular]{.doc}]pair_granular.md){.reference .internal} page for information on any extra quantities.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
::::

::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

This fix does **not** support the *fix* keyword of the [[dump image]{.doc}]dump_image.md){.reference .internal} command. Instead the region used by the fix can be visualized using the *region* keyword of *dump image*.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the GRANULAR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix_move]{.doc}]fix_move.md){.reference .internal}, [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal}, [[fix wall/region]{.doc}]fix_wall_region.md){.reference .internal}, [[pair_style granular]{.doc}]pair_gran.md){.reference .internal}, [[region]{.doc}]region.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

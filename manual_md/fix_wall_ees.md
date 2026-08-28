::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#fix-wall-ees-command .section}
[]{#index-1}[]{#index-0}

# fix wall/ees command[](#fix-wall-ees-command "Link to this heading"){.headerlink}
:::

:::::::::::::::::::: {#fix-wall-region-ees-command .section}
# fix wall/region/ees command[](#fix-wall-region-ees-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID style args
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- style = *wall/ees* or *wall/region/ees*

  ``` literal-block
  args for style wall/ees: one or more face parameters groups may be appended
  face = xlo or xhi or ylo or yhi or zlo or zhi
  parameters = coord epsilon sigma cutoff
    coord = position of wall = EDGE or constant or variable
      EDGE = current lo or hi edge of simulation box
      constant = number like 0.0 or -30.0 (distance units)
      variable = equal-style variable like v_x or v_wiggle
    epsilon = strength factor for wall-particle interaction (energy or energy/distance^2 units)
      epsilon can be a variable (see below)
    sigma = size factor for wall-particle interaction (distance units)
      sigma can be a variable (see below)
    cutoff = distance from wall at which wall-particle interaction is cut off (distance units)
  ```

  ``` literal-block
  args for style wall/region/ees: region-ID epsilon sigma cutoff
    region-ID = region whose boundary will act as wall
    epsilon = strength factor for wall-particle interaction (energy or energy/distance^2 units)
    sigma = size factor for wall-particle interaction (distance units)
    cutoff = distance from wall at which wall-particle interaction is cut off (distance units)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix wallhi all wall/ees xlo -1.0 1.0 1.0 2.5 units box
    fix wallhi all wall/ees xhi EDGE 1.0 1.0 2.5
    fix wallhi all wall/ees v_wiggle 23.2 1.0 1.0 2.5
    fix zwalls all wall/ees zlo 0.0 1.0 1.0 0.858 zhi 40.0 1.0 1.0 0.858

    fix ees_cube all wall/region/ees myCube 1.0 1.0 2.5
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Fix *wall/ees* bounds the simulation domain on one or more of its faces with a flat wall that interacts with the ellipsoidal atoms in the group by generating a force on the atom in a direction perpendicular to the wall and a torque parallel with the wall. The energy of wall-particle interactions E is given by:

::: {.math .notranslate .nohighlight}
\\\[E = \\epsilon \\left\[ \\frac{2 \\sigma\_{LJ}\^{12} \\left(7 r\^5+14 r\^3 \\sigma\_{n}\^2+3 r \\sigma\_{n}\^4\\right) }{945 \\left(r\^2-\\sigma\_{n}\^2\\right)\^7} -\\frac{ \\sigma\_{LJ}\^6 \\left(2 r \\sigma\_{n}\^3+\\sigma\_{n}\^2 \\left(r\^2-\\sigma\_{n}\^2\\right)\\log{ \\left\[\\frac{r-\\sigma\_{n}}{r+\\sigma\_{n}}\\right\]}\\right) }{12 \\sigma\_{n}\^5 \\left(r\^2-\\sigma\_{n}\^2\\right)} \\right\]\\qquad \\sigma_n \< r \< r_c\\\]
:::

Introduced by Babadi and Ejtehadi in [[(Babadi2)]{.std .std-ref}](#babadiejtehadi){.reference .internal}. Here, *r* is the distance from the particle to the wall at position *coord*, and Rc is the *cutoff* distance at which the particle and wall no longer interact. Also, [\\(\\sigma_n\\)]{.math .notranslate .nohighlight} is the distance between center of ellipsoid and the nearest point of its surface to the wall as shown below.

![](_images/fix_wall_ees_image.jpg){.align-center}

Details of using this command and specifications are the same as fix/wall command. You can also find an example in USER/ees/ under examples/ directory.

The prefactor [\\(\\epsilon\\)]{.math .notranslate .nohighlight} can be thought of as an effective Hamaker constant with energy units for the strength of the ellipsoid-wall interaction. More specifically, the [\\(\\epsilon\\)]{.math .notranslate .nohighlight} prefactor is

::: {.math .notranslate .nohighlight}
\\\[8 \\pi\^2 \\quad \\rho\_{wall} \\quad \\rho\_{ellipsoid} \\quad \\epsilon \\quad \\sigma_a \\quad \\sigma_b \\quad \\sigma_c\\\]
:::

where [\\(\\epsilon\\)]{.math .notranslate .nohighlight} is the LJ energy parameter for the constituent LJ particles and [\\(\\sigma_a\\)]{.math .notranslate .nohighlight}, [\\(\\sigma_b\\)]{.math .notranslate .nohighlight}, and [\\(\\sigma_c\\)]{.math .notranslate .nohighlight} are the radii of the ellipsoidal particles. [\\(\\rho\_{wall}\\)]{.math .notranslate .nohighlight} and [\\(\\rho\_{ellipsoid}\\)]{.math .notranslate .nohighlight} are the number density of the constituent particles, in the wall and ellipsoid respectively, in units of 1/volume.

::: {.admonition .note}
Note

You must ensure that r is always bigger than [\\(\\sigma_n\\)]{.math .notranslate .nohighlight} for all particles in the group, or LAMMPS will generate an error. This means you cannot start your simulation with particles touching the wall position *coord* ([\\(r = \\sigma_n\\)]{.math .notranslate .nohighlight}) or with particles penetrating the wall ([\\(0 =\< r \< \\sigma_n\\)]{.math .notranslate .nohighlight}) or with particles on the wrong side of the wall ([\\(r \< 0\\)]{.math .notranslate .nohighlight}).
:::

Fix *wall/region/ees* treats the surface of the geometric region defined by the *region-ID* as a bounding wall which interacts with nearby ellipsoidal particles according to the EES potential introduced above.

Other details of this command are the same as for the [[fix wall/region]{.doc}]fix_wall_region.md){.reference .internal} command. One may also find an example of using this fix in the examples/PACKAGES/ees/ directory.
::::::

------------------------------------------------------------------------

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about these fixes are written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by these fixes to add the energy of interaction between atoms and all the specified walls or region wall to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default settings for these fixes are [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by these fixes. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is adding its forces. Default is the outermost level.

These fixes computes a global scalar and a global vector of forces, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. See the [[fix wall]{.doc}]fix_wall.md){.reference .internal} command for a description of the scalar and vector.

No parameter of these fixes can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The forces due to these fixes are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command.

::: {.admonition .note}
Note

If you want the atom/wall interaction energy to be included in the total potential energy of the system (the quantity being minimized), you MUST enable the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for this fix.
:::
::::

------------------------------------------------------------------------

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

Fix *wall/ees* fix supports the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix will pass geometry information about the walls to *dump image* so that the walls will be included in the rendered image. Please note, that for [[2d systems]{.doc}]dimension.md){.reference .internal}, a wall rendered as a plane would be invisible and it is thus rendered as a cylinder. Fix *wall/ees/region* does **not** support graphics info, but the region can be visualized with the *region* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}.

The color of the wall is by default that of the first atom type when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

For 2d systems, the *fflag1* setting determines whether the cylinder representing the wall is capped with a sphere at the ends: 0 means no caps, 1 means the lower end is capped, 2 means the upper end is capped, and 3 means both ends are capped. The *fflag2* setting allows to adjust the radius of the rendered cylinder. It should be set to a value \> 0 or the cylinder will not be visible since the diameter is set internally to zero due to lack of a suitable heuristic for deriving a meaningful diameter for all types of walls and unit settings.

For 3d systems, both *fflag1* and *fflag2* are ignored.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These fixes are part of the EXTRA-FIX package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

These fixes requires that atoms be ellipsoids as defined by the [[atom_style ellipsoid]{.doc}]atom_style.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix wall]{.doc}]fix_wall.md){.reference .internal}, [[pair resquared]{.doc}]pair_resquared.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Babadi2)** Babadi and Ejtehadi, EPL, 77 (2007) 23002.
:::
::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

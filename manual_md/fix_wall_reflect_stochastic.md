::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-wall-reflect-stochastic-command .section}
[]{#index-0}

# fix wall/reflect/stochastic command[](#fix-wall-reflect-stochastic-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID wall/reflect/stochastic rstyle seed face args ... keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- wall/reflect/stochastic = style name of this fix command

- rstyle = diffusive or maxwell or ccl

- seed = random seed for stochasticity (positive integer)

- one or more face/args pairs may be appended

- face = *xlo* or *xhi* or *ylo* or *yhi* or *zlo* or *zhi*

  :::: {.highlight-none .notranslate}
  ::: highlight
      args = pos temp velx vely velz accomx accomy accomz
        pos = EDGE or constant
          EDGE = current lo or hi edge of simulation box
          constant = number like 0.0 or 30.0 (distance units)
        temp = wall temperature (temperature units)
        velx,vely,velz = wall velocity in x,y,z directions (velocity units)
        accomx,accomy,accomz = accommodation coeffs in x,y,z directions (unitless)
          not specified for rstyle = diffusive
          single accom coeff specified for rstyle maxwell
          all 3 coeffs specified for rstyle cll
  :::
  ::::

- zero or more keyword/value pairs may be appended

- keyword = *units*

  ``` literal-block
  units value = lattice or box
    lattice = the wall position is defined in lattice units
    box = the wall position is defined in simulation box units
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix zwalls all wall/reflect/stochastic diffusive 23424 zlo EDGE 300 0.1 0.1 0 zhi EDGE 200 0.1 0.1 0
    fix ywalls all wall/reflect/stochastic maxwell 345533 ylo 5.0 300 0.1 0.0 0.0 0.8 yhi 10.0 300 0.1 0.0 0.0 0.8
    fix xwalls all wall/reflect/stochastic cercignanilampis 2308 xlo 0.0 300 0.0 0.1 0.9 0.8 0.7 xhi EDGE 300 0.0 0.1 0 0.9 0.8 0.7 units box
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Bound the simulation with one or more walls which reflect particles in the specified group when they attempt to move through them.

Reflection means that if an atom moves outside the wall on a timestep (e.g. due to the [[fix nve]{.doc}]fix_nve.md){.reference .internal} command), then it is put back inside the wall with a changed velocity.

This fix models treats the wall as a moving solid boundary with a finite temperature, which can exchange energy with particles that collide with it. This is different than the simpler [[fix wall/reflect]{.doc}]fix_wall_reflect.md){.reference .internal} command which models mirror reflection. For this fix, the post collision velocity of each particle is treated stochastically. The randomness can come from many sources: thermal motion of the wall atoms, surface roughness, etc. Three stochastic reflection models are currently implemented.

For rstyle *diffusive*, particles are reflected diffusively. Their velocity distribution corresponds to an equilibrium distribution of particles at the wall temperature. No accommodation coefficients are specified.

For rstyle *maxwell*, particle reflection is Maxwellian which means partially diffusive and partially specular ([[Maxwell]{.std .std-ref}](#maxwell){.reference .internal}). A single accommodation coeff is specified which must be between 0.0 and 1.0 inclusive. It determines the fraction of the collision which is diffusive versus specular. An accommodation coefficient of 1.0 is fully diffusive; a coefficient of 0.0 is fully specular.

For rstyle *cll*, particle collisions are computed by the Cercignani/Lampis model. See [[CL]{.std .std-ref}](#cl){.reference .internal} and [[To]{.std .std-ref}](#to){.reference .internal} for details. Three accommodations coefficient are specified. Each must be between 0.0 and 1.0 inclusive. Two are velocity accommodation coefficients; one is a normal kinetic energy accommodation. The normal coeff is the one corresponding to the normal of the wall itself. For example if the wall is *ylo* or *yhi*, *accomx* and *accomz* are the tangential velocity accommodation coefficients, and *accomy* is the normal kinetic energy accommodation coefficient.

The optional *units* keyword determines the distance units used to define a wall position. A *box* value selects standard distance units as defined by the [[units]{.doc}]units.md){.reference .internal} command, e.g. Angstroms for units = real or metal. A *lattice* value means the distance units are in lattice spacings. The [[lattice]{.doc}]lattice.md){.reference .internal} command must have been previously used to define the lattice spacings.
:::

------------------------------------------------------------------------

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

This wall fix supports the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix will pass geometry information about the walls to *dump image* so that the walls will be included in the rendered image. Please note, that for [[2d systems]{.doc}]dimension.md){.reference .internal}, a wall rendered as a plane would be invisible and it is thus rendered as a cylinder.

The color of the wall is by default that of the first atom type when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

The *fflag1* setting and the *fflag2* setting of *dump image fix* are only relevant for 2d systems. The *fflag1* setting determines whether the cylinder is capped with a sphere at the ends: 0 means no caps, 1 means the lower end is capped, 2 means the upper end is capped, and 3 means both ends are capped. The *fflag2* setting allows to adjust the radius of the rendered cylinder. It should be set to a value \> 0 or the cylinder will not be visible since the diameter is set internally to zero due to lack of a suitable heuristic for deriving a meaningful diameter for all types of walls and unit settings.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix has the same limitations as the [[fix wall/reflect]{.doc}]fix_wall_reflect.md){.reference .internal} command. Any dimension (xyz) that has a wall must be non-periodic. It should not be used with rigid bodies such as those defined by the [[fix rigid]{.doc}]fix_rigid.md){.reference .internal} command. The wall velocity must lie on the same plane as the wall itself.

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix wall/reflect]{.doc}]fix_wall_reflect.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default for the units keyword is lattice.

------------------------------------------------------------------------

**(Maxwell)** J.C. Maxwell, Philos. Tans. Royal Soc. London, 157: 49-88 (1867).

**(Cercignani)** C. Cercignani and M. Lampis. Trans. Theory Stat. Phys. 1, 2, 101 (1971).

**(To)** Q.D. To, V.H. Vu, G. Lauriat, and C. Leonard. J. Math. Phys. 56, 103101 (2015).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-wall-reflect-command .section}
[]{#index-1}[]{#index-0}

# fix wall/reflect command[](#fix-wall-reflect-command "Link to this heading"){.headerlink}

Accelerator Variants: *wall/reflect/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID wall/reflect face arg ... keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- wall/reflect = style name of this fix command

- one or more face/arg pairs may be appended

- face = *xlo* or *xhi* or *ylo* or *yhi* or *zlo* or *zhi*

  ``` literal-block
  arg = EDGE or constant or variable
    EDGE = current lo edge of simulation box
    constant = number like 0.0 or 30.0 (distance units)
    variable = equal-style variable like v_x or v_wiggle
  ```

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
    fix xwalls all wall/reflect xlo EDGE xhi EDGE
    fix walls all wall/reflect xlo 0.0 ylo 10.0 units box
    fix top all wall/reflect zhi v_pressdown
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Bound the simulation with one or more walls which reflect particles in the specified group when they attempt to move through them.

Reflection means that if an atom moves outside the wall on a timestep by a distance delta (e.g. due to [[fix nve]{.doc}]fix_nve.md){.reference .internal}), then it is put back inside the face by the same delta, and the sign of the corresponding component of its velocity is flipped.

When used in conjunction with [[fix nve]{.doc}]fix_nve.md){.reference .internal} and [[run_style verlet]{.doc}]run_style.md){.reference .internal}, the resultant time-integration algorithm is equivalent to the primitive splitting algorithm (PSA) described by [[Bond]{.std .std-ref}](#bond1){.reference .internal}. Because each reflection event divides the corresponding timestep asymmetrically, energy conservation is only satisfied to O(dt), rather than to O(dt\^2) as it would be for velocity-Verlet integration without reflective walls.

Up to 6 walls or faces can be specified in a single command: *xlo*, *xhi*, *ylo*, *yhi*, *zlo*, *zhi*. A *lo* face reflects particles that move to a coordinate less than the wall position, back in the *hi* direction. A *hi* face reflects particles that move to a coordinate higher than the wall position, back in the *lo* direction.

The position of each wall can be specified in one of 3 ways: as the EDGE of the simulation box, as a constant value, or as a variable. If EDGE is used, then the corresponding boundary of the current simulation box is used. If a numeric constant is specified then the wall is placed at that position in the appropriate dimension (x, y, or z). In both the EDGE and constant cases, the wall will never move. If the wall position is a variable, it should be specified as v_name, where name is an [[equal-style variable]{.doc}]variable.md){.reference .internal} name. In this case the variable is evaluated each timestep and the result becomes the current position of the reflecting wall. Equal-style variables can specify formulas with various mathematical functions, and include [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command keywords for the simulation box parameters and timestep and elapsed time. Thus it is easy to specify a time-dependent wall position.

The *units* keyword determines the meaning of the distance units used to define a wall position, but only when a numeric constant or variable is used. It is not relevant when EDGE is used to specify a face position. In the variable case, the variable is assumed to produce a value compatible with the *units* setting you specify.

A *box* value selects standard distance units as defined by the [[units]{.doc}]units.md){.reference .internal} command, e.g. Angstroms for units = real or metal. A *lattice* value means the distance units are in lattice spacings. The [[lattice]{.doc}]lattice.md){.reference .internal} command must have been previously used to define the lattice spacings.

------------------------------------------------------------------------

Here are examples of variable definitions that move the wall position in a time-dependent fashion using equal-style [[variables]{.doc}]variable.md){.reference .internal}.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable ramp equal ramp(0,10)
    fix 1 all wall/reflect xlo v_ramp

    variable linear equal vdisplace(0,20)
    fix 1 all wall/reflect xlo v_linear

    variable wiggle equal swiggle(0.0,5.0,3.0)
    fix 1 all wall/reflect xlo v_wiggle

    variable wiggle equal cwiggle(0.0,5.0,3.0)
    fix 1 all wall/reflect xlo v_wiggle
:::
::::

The *ramp(lo,hi)* function adjusts the wall position linearly from *lo* to *hi* over the course of a run. The *vdisplace(c0,velocity)* function does something similar using the equation *position = c0 + velocity\*delta*, where *delta* is the elapsed time.

The *swiggle(c0,A,period)* function causes the wall position to oscillate sinusoidally according to this equation, where *omega = 2 PI / period*:

``` literal-block
position = c0 + A sin(omega*delta)
```

The *cwiggle(c0,A,period)* function causes the wall position to oscillate sinusoidally according to this equation, which will have an initial wall velocity of 0.0, and thus may impose a gentler perturbation on the particles:

``` literal-block
position = c0 + A (1 - cos(omega*delta))
```
:::::

------------------------------------------------------------------------

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

These wall fixes support the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fixes will pass geometry information about the walls to *dump image* so that the walls will be included in the rendered image. Please note, that for [[2d systems]{.doc}]dimension.md){.reference .internal}, a wall rendered as a plane would be invisible and it is thus rendered as a cylinder.

The color of the wall is by default that of the first atom type when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed globally with *dump_modify ftrans*.

For 2d systems, the *fflag1* setting determines whether the cylinder representing the wall is capped with a sphere at the ends: 0 means no caps, 1 means the lower end is capped, 2 means the upper end is capped, and 3 means both ends are capped. The *fflag2* setting allows to adjust the radius of the rendered cylinder. It should be set to a value \> 0 or the cylinder will not be visible since the diameter is set internally to zero due to lack of a suitable heuristic for deriving a meaningful diameter for all types of walls and unit settings.

For 3d systems, both *fflag1* and *fflag2* are ignored.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Any dimension (xyz) that has a reflecting wall must be non-periodic.

A reflecting wall should not be used with rigid bodies such as those defined by a "fix rigid" command. This is because the wall/reflect displaces atoms directly rather than exerts a force on them. For rigid bodies, use a soft wall instead, such as [[fix wall/lj93]{.doc}]fix_wall.md){.reference .internal}. LAMMPS will flag the use of a rigid fix with fix wall/reflect with a warning, but will not generate an error.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix wall/lj93]{.doc}]fix_wall.md){.reference .internal}, [[fix oneway]{.doc}]fix_oneway.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default for the units keyword is lattice.

------------------------------------------------------------------------

**(Bond)** Bond and Leimkuhler, SIAM J Sci Comput, 30, p 134 (2007).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

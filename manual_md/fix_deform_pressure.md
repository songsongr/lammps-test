:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#fix-deform-pressure-command .section}
[]{#index-0}

# fix deform/pressure command[](#fix-deform-pressure-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-none .notranslate}
::: highlight
    fix ID group-ID deform/pressure N parameter style args ... keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- deform/pressure = style name of this fix command

- N = perform box deformation every this many timesteps

- one or more parameter/args sequences may be appended

  ``` literal-block
  parameter = x or y or z or xy or xz or yz or box
    x, y, z args = style value(s)
      style = final or delta or scale or vel or erate or trate or volume or wiggle or variable or pressure or pressure/mean
        final values = lo hi
          lo hi = box boundaries at end of run (distance units)
        delta values = dlo dhi
          dlo dhi = change in box boundaries at end of run (distance units)
        scale values = factor
          factor = multiplicative factor for change in box length at end of run
        vel value = V
          V = change box length at this velocity (distance/time units),
              effectively an engineering strain rate
        erate value = R
          R = engineering strain rate (1/time units)
        trate value = R
          R = true strain rate (1/time units)
        volume value = none = adjust this dim to preserve volume of system
        wiggle values = A Tp
          A = amplitude of oscillation (distance units)
          Tp = period of oscillation (time units)
        variable values = v_name1 v_name2
          v_name1 = variable with name1 for box length change as function of time
          v_name2 = variable with name2 for change rate as function of time
        pressure values = target gain
          target = target pressure (pressure units)
          gain = proportional gain constant (1/(time * pressure) or 1/time units)
        pressure/mean values = target gain
          target = target pressure (pressure units)
          gain = proportional gain constant (1/(time * pressure) or 1/time units)

    xy, xz, yz args = style value
      style = final or delta or vel or erate or erate/rescale or trate or wiggle or variable or pressure
        final value = tilt
          tilt = tilt factor at end of run (distance units)
        delta value = dtilt
          dtilt = change in tilt factor at end of run (distance units)
        vel value = V
          V = change tilt factor at this velocity (distance/time units),
              effectively an engineering shear strain rate
        erate value = R
          R = engineering shear strain rate (1/time units)
        erate/rescale value = R
          R = engineering shear strain rate (1/time units)
        trate value = R
          R = true shear strain rate (1/time units)
        wiggle values = A Tp
          A = amplitude of oscillation (distance units)
          Tp = period of oscillation (time units)
        variable values = v_name1 v_name2
          v_name1 = variable with name1 for tilt change as function of time
          v_name2 = variable with name2 for change rate as function of time
        pressure values = target gain
          target = target pressure (pressure units)
          gain = proportional gain constant (1/(time * pressure) or 1/time units)

    box = style value
      style = volume or pressure
        volume value = none = isotropically adjust system to preserve volume of system
        pressure values = target gain
          target = target mean pressure (pressure units)
          gain = proportional gain constant (1/(time * pressure) or 1/time units)
  ```

- zero or more keyword/value pairs may be appended

- keyword = *remap* or *flip* or *units* or *couple* or *vol/balance/p* or *max/rate* or *normalize/pressure*

  ``` literal-block
  remap value = x or v or none
    x = remap coords of atoms in group into deforming box
    v = remap velocities of atoms in group when they cross periodic boundaries
    none = no remapping of x or v
  flip value = yes or no
    allow or disallow box flips when it becomes highly skewed
  units value = lattice or box
    lattice = distances are defined in lattice units
    box = distances are defined in simulation box units
  couple value = none or xyz or xy or yz or xz
    couple pressure values of various dimensions
  vol/balance/p value = yes or no
    Modifies the behavior of the volume option to try and balance pressures
  max/rate value = rate
    rate = maximum strain rate for pressure control
  normalize/pressure value = yes or no
    Modifies pressure controls such that the deviation in pressure is normalized by the target pressure
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all deform/pressure 1 x pressure 2.0 0.1 normalize/pressure yes max/rate 0.001
    fix 1 all deform/pressure 1 x trate 0.1 y volume z volume vol/balance/p yes
    fix 1 all deform/pressure 1 x trate 0.1 y pressure/mean 0.0 1.0 z pressure/mean 0.0 1.0
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 17Apr2024.]{.versionmodified .added}
:::

This fix is an extension of the [[fix deform]{.doc}]fix_deform.md){.reference .internal} command, which allows all of its options to be used as well as new pressure-based controls implemented by this command.

All arguments described on the [[fix deform]{.doc}]fix_deform.md){.reference .internal} doc page also apply to this fix unless otherwise noted below. The rest of this page explains the arguments specific to this fix only. Note that a simulation can define only a single deformation command: fix deform or fix deform/pressure.

::: {.warning .admonition}
Inconsistent trajectories due to image flags

When running long simulations while shearing the box or using a high shearing rate, it is possible that the image flags used for storing unwrapped atom positions will "wrap around". When LAMMPS is compiled with the default settings, case image flags are limited to a range of [\\(-512 \\le i \\le 511\\)]{.math .notranslate .nohighlight}, which will overflow when atoms starting at zero image flag value have passed through a periodic box dimension more than 512 times.

Changing the [[size of LAMMPS integer types]{.std .std-ref}]Build_settings.md#size){.reference .internal} to the "bigbig" setting can make this overflow much less likely, since it increases the image flag value range to [\\(- 1,048,576 \\le i \\le 1\\,048\\,575\\)]{.math .notranslate .nohighlight}
:::

------------------------------------------------------------------------

For the *x*, *y*, and *z* parameters, this is the meaning of the styles and values provided by this fix.

The *pressure* style adjusts a dimension's box length to control the corresponding component of the pressure tensor. This option attempts to maintain a specified target pressure using a linear controller where the box length [\\(L\\)]{.math .notranslate .nohighlight} evolves according to the equation

::: {.math .notranslate .nohighlight}
\\\[\\frac{d L(t)}{dt} = L(t) k (P_t - P)\\\]
:::

where [\\(k\\)]{.math .notranslate .nohighlight} is a proportional gain constant, [\\(P_t\\)]{.math .notranslate .nohighlight} is the target pressure, and [\\(P\\)]{.math .notranslate .nohighlight} is the current pressure along that dimension. This approach is similar to the method used to control the pressure by [[fix press/berendsen]{.doc}]fix_press_berendsen.md){.reference .internal}. The target pressure accepts either a constant numeric value or a LAMMPS [[variable]{.std .std-ref}]Howto_output.md#variable){.reference .internal}. Notably, this variable can be a function of time or other components of the pressure tensor. By default, [\\(k\\)]{.math .notranslate .nohighlight} has units of 1/(time \* pressure) although this will change if the *normalize/pressure* option is set as [[discussed below]{.std .std-ref}](#deform-normalize){.reference .internal}. There is no proven method to choosing an appropriate value of [\\(k\\)]{.math .notranslate .nohighlight} as it will depend on the specific details of a simulation. Testing different values is recommended.

By default, there is no limit on the resulting strain rate in any dimension. A maximum limit can be applied using the [[max/rate]{.std .std-ref}](#deform-max-rate){.reference .internal} option. Akin to [[fix npt and nph]{.doc}]fix_nh.md){.reference .internal}, pressures in different dimensions can be coupled using the [[couple]{.std .std-ref}](#deform-couple){.reference .internal} option. This means the instantaneous pressure along coupled dimensions are averaged and the box strains identically along the coupled dimensions.

The *pressure/mean* style changes a dimension's box length to maintain a constant mean pressure defined as the trace of the pressure tensor. This option has identical arguments to the *pressure* style and a similar functional equation, except the current and target pressures refer to the mean trace of the pressure tensor. All options for the *pressure* style also apply to the *pressure/mean* style except for the [[couple]{.std .std-ref}](#deform-couple){.reference .internal} option.

Note that while this style can be identical to coupled *pressure* styles, it is generally not the same. For instance in 2D, a coupled *pressure* style in the *x* and *y* dimensions would be equivalent to using the *pressure/mean* style with identical settings in each dimension. However, it would not be the same if settings (e.g. gain constants) were used in the *x* and *y* dimensions or if the *pressure/mean* command was only applied along one dimension.

------------------------------------------------------------------------

For the *xy*, *xz*, and *yz* parameters, this is the meaning of the styles and values provided by this fix. Note that changing the tilt factors of a triclinic box does not change its volume.

The *pressure* style adjusts a tilt factor to control the corresponding off-diagonal component of the pressure tensor. This option attempts to maintain a specified target value using a linear controller where the tilt factor T evolves according to the equation

::: {.math .notranslate .nohighlight}
\\\[\\frac{d T(t)}{dt} = L(t) k (P - P_t)\\\]
:::

where [\\(k\\)]{.math .notranslate .nohighlight} is a proportional gain constant, [\\(P_t\\)]{.math .notranslate .nohighlight} is the target pressure, [\\(P\\)]{.math .notranslate .nohighlight} is the current pressure, and [\\(L\\)]{.math .notranslate .nohighlight} is the perpendicular box length. The target pressure accepts either a constant numeric value or a LAMMPS [[variable]{.std .std-ref}]Howto_output.md#variable){.reference .internal}. Notably, this variable can be a function of time or other components of the pressure tensor. By default, [\\(k\\)]{.math .notranslate .nohighlight} has units of 1/(time \* pressure) although this will change if the *normalize/pessure* option is set as [[discussed below]{.std .std-ref}](#deform-normalize){.reference .internal}. There is no proven method to choosing an appropriate value of [\\(k\\)]{.math .notranslate .nohighlight} as it will depend on the specific details of a simulation and testing different values is recommended. One can also apply a maximum limit to the magnitude of the applied strain using the [[max/rate]{.std .std-ref}](#deform-max-rate){.reference .internal} option.

------------------------------------------------------------------------

The *box* parameter provides an additional control over the *x*, *y*, and *z* box lengths by isotropically dilating or contracting the box to either maintain a fixed mean pressure or volume. This isotropic scaling is applied after the box is deformed by the above *x*, *y*, *z*, *xy*, *xz*, and *yz* styles, acting as a second deformation step. This parameter will change the overall strain rate in the *x*, *y*, or *z* dimensions. This parameter can only be used in combination with the *x*, *y*, or *z* commands: *vel*, *erate*, *trate*, *pressure*, or *wiggle*. This is the meaning of its styles and values.

The *volume* style isotropically scales box lengths to maintain a constant box volume in response to deformation from other parameters. This style may be useful in scenarios where one wants to apply a constant deviatoric pressure using *pressure* styles in the *x*, *y*, and *z* dimensions ( deforming the shape of the box), while maintaining a constant volume.

The *pressure* style isotropically scales box lengths in an attempt to maintain a target mean pressure (the trace of the pressure tensor) of the system. This is accomplished by isotropically scaling all box lengths [\\(L\\)]{.math .notranslate .nohighlight} by an additional factor of [\\(k (P_t - P_m)\\)]{.math .notranslate .nohighlight} where [\\(k\\)]{.math .notranslate .nohighlight} is the proportional gain constant, [\\(P_t\\)]{.math .notranslate .nohighlight} is the target pressure, and [\\(P_m\\)]{.math .notranslate .nohighlight} is the current mean pressure. This style may be useful in scenarios where one wants to apply a constant deviatoric strain rate using various strain-based styles (e.g. *trate*) along the *x*, *y*, and *z* dimensions (deforming the shape of the box), while maintaining a mean pressure.

------------------------------------------------------------------------

The optional keywords provided by this fix are described below.

The *normalize/pressure* keyword changes how box dimensions evolve when using the *pressure* or *pressure/mean* deformation styles. If the *deform/normalize* value is set to *yes*, then the deviation from the target pressure is normalized by the absolute value of the target pressure such that the proportional gain constant scales a percentage error and has units of 1/time. If the target pressure is ever zero, this will produce an error unless the *max/rate* keyword is defined, described below, which will cap the divergence.

The *max/rate* keyword sets an upper threshold, *rate*, that limits the maximum magnitude of the instantaneous strain rate applied in any dimension. This keyword only applies to the *pressure* and *pressure/mean* options. If a pressure-controlled rate is used for both *box* and either *x*, *y*, or *z*, then this threshold will apply separately to each individual controller such that the cumulative strain rate on a box dimension may be up to twice the value of *rate*.

The *couple* keyword allows two or three of the diagonal components of the pressure tensor to be "coupled" together for the *pressure* option. The value specified with the keyword determines which are coupled. For example, *xz* means the *Pxx* and *Pzz* components of the stress tensor are coupled. *Xyz* means all 3 diagonal components are coupled. Coupling means two things: the instantaneous stress will be computed as an average of the corresponding diagonal components, and the coupled box dimensions will be changed together in lockstep, meaning coupled dimensions will be dilated or contracted by the same percentage every timestep. If a *pressure* style is defined for more than one coupled dimension, the target pressures and gain constants must be identical. Alternatively, if a *pressure* style is only defined for one of the coupled dimensions, its settings are copied to other dimensions with undefined styles. *Couple xyz* can be used for a 2d simulation; the *z* dimension is simply ignored.

The *vol/balance/p* keyword modifies the behavior of the *volume* style when applied to two of the *x*, *y*, and *z* dimensions. Instead of straining the two dimensions in lockstep, the two dimensions are allowed to separately dilate or contract in a manner to maintain a constant volume while simultaneously trying to keep the pressure along each dimension equal using a method described in [[(Huang2014)]{.std .std-ref}](#huang2014){.reference .internal}.

------------------------------------------------------------------------

If any pressure controls are used, this fix computes a temperature and pressure each timestep. To do this, the fix creates its own computes of style "temp" and "pressure", as if these commands had been issued:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute fix-ID_temp group-ID temp
    compute fix-ID_press group-ID pressure fix-ID_temp
:::
::::

See the [[compute temp]{.doc}]compute_temp.md){.reference .internal} and [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} commands for details. Note that the IDs of the new computes are the fix-ID + underscore + "temp" or fix_ID + underscore + "press", and the group for the new computes is the same as the fix group.

Note that these are NOT the computes used by thermodynamic output (see the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command) with ID = *thermo_temp* and *thermo_press*. This means you can change the attributes of this fix's temperature or pressure via the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command or print this temperature or pressure during thermodynamic output via the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command using the appropriate compute-ID. It also means that changing attributes of *thermo_temp* or *thermo_press* will have no effect on this fix.
:::::::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix will restore the initial box settings from [[binary restart files]{.doc}]restart.md){.reference .internal}, which allows the fix to be properly continue deformation, when using the start/stop options of the [[run]{.doc}]run.md){.reference .internal} command. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}.

If any pressure controls are used, the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* and *press* options are supported by this fix, unlike in [[fix deform]{.doc}]fix_deform.md){.reference .internal}. You can use them to assign a [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its temperature and pressure calculations. If you do this, note that the kinetic energy derived from the compute temperature should be consistent with the virial term computed using all atoms for the pressure. LAMMPS will warn you if you choose to compute temperature on a subset of atoms.

This fix can perform deformation over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You cannot apply x, y, or z deformations to a dimension that is shrink-wrapped via the [[boundary]{.doc}]boundary.md){.reference .internal} command.

You cannot apply xy, yz, or xz deformations to a second dimension (y in xy) that is shrink-wrapped via the [[boundary]{.doc}]boundary.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix deform]{.doc}]fix_deform.md){.reference .internal}, [[change_box]{.doc}]change_box.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are normalize/pressure = no.

------------------------------------------------------------------------

**(Huang2014)** X. Huang, "Exploring critical-state behavior using DEM", Doctoral dissertation, Imperial College. (2014). [https://doi.org/10.25560/25316](https://doi.org/10.25560/25316){.reference .external}
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

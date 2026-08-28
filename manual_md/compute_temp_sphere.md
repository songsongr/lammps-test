:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#compute-temp-sphere-command .section}
[]{#index-0}

# compute temp/sphere command[](#compute-temp-sphere-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID temp/sphere keyword value ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- temp/sphere = style name of this compute command

- zero or more keyword/value pairs may be appended

- keyword = *bias* or *dof*

  ``` literal-block
  bias value = bias-ID
    bias-ID = ID of a temperature compute that removes a velocity bias
  dof value = all or rotate
    all = compute temperature of translational and rotational degrees of freedom
    rotate = compute temperature of just rotational degrees of freedom
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all temp/sphere
    compute myTemp mobile temp/sphere bias tempCOM
    compute myTemp mobile temp/sphere dof rotate
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the temperature of a group of spherical particles, including a contribution from both their translational and rotational kinetic energy. This differs from the usual [[compute temp]{.doc}]compute_temp.md){.reference .internal} command, which assumes point particles with only translational kinetic energy.

Both point and finite-size particles can be included in the group. Point particles do not rotate, so they have only three translational degrees of freedom. For 3d spherical particles, each has six degrees of freedom (three translational, three rotational). For 2d spherical particles, each has three degrees of freedom (two translational, one rotational).

::: {.admonition .note}
Note

This choice for degrees of freedom (DOF) assumes that all finite-size spherical particles in your model will freely rotate, sampling all their rotational DOF. It is possible to use a combination of interaction potentials and fixes that induce no torque or otherwise constrain some of all of your particles so that this is not the case. Then there are less DOF and you should use the [[compute_modify extra/dof]{.doc}]compute_modify.md){.reference .internal} command to adjust the DOF accordingly.
:::

The translational kinetic energy is computed the same as is described by the [[compute temp]{.doc}]compute_temp.md){.reference .internal} command. The rotational kinetic energy is computed as [\\(\\frac12 I \\omega\^2\\)]{.math .notranslate .nohighlight}, where [\\(I\\)]{.math .notranslate .nohighlight} is the moment of inertia for a sphere and [\\(\\omega\\)]{.math .notranslate .nohighlight} is the particle's angular velocity.

::: {.admonition .note}
Note

For [[2d models]{.doc}]dimension.md){.reference .internal}, particles are treated as spheres, not disks, meaning their moment of inertia will be the same as in 3d.
:::

A kinetic energy tensor, stored as a six-element vector, is also calculated by this compute. The formula for the components of the tensor is the same as the above formulas, except that [\\(v\^2\\)]{.math .notranslate .nohighlight} and [\\(\\omega\^2\\)]{.math .notranslate .nohighlight} are replaced by [\\(v_x v_y\\)]{.math .notranslate .nohighlight} and [\\(\\omega_x \\omega_y\\)]{.math .notranslate .nohighlight} for the [\\(xy\\)]{.math .notranslate .nohighlight} component. The six components of the vector are ordered [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}.

A symmetric tensor, stored as a six-element vector, is also calculated by this compute for use in the computation of a pressure tensor by the [[compute pressue]{.doc}]compute_pressure.md){.reference .internal} command. The formula for the components of the tensor is the same as the above expression for [\\(E\_\\mathrm{kin}\\)]{.math .notranslate .nohighlight}, except that the 1/2 factor is NOT included and the [\\(v_i\^2\\)]{.math .notranslate .nohighlight} and [\\(\\omega\^2\\)]{.math .notranslate .nohighlight} are replaced by [\\(v_x v_y\\)]{.math .notranslate .nohighlight} and [\\(\\omega_x \\omega_y\\)]{.math .notranslate .nohighlight} for the [\\(xy\\)]{.math .notranslate .nohighlight} component, and so on. Note that because it lacks the 1/2 factor, these tensor components are twice those of the traditional kinetic energy tensor. The six components of the vector are ordered [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}.

The number of atoms contributing to the temperature is assumed to be constant for the duration of the run; use the *dynamic* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command if this is not the case.

This compute subtracts out translational degrees-of-freedom due to fixes that constrain molecular motion, such as [[fix shake]{.doc}]fix_shake.md){.reference .internal} and [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}. This means the temperature of groups of atoms that include these constraints will be computed correctly. If needed, the subtracted degrees of freedom can be altered using the *extra/dof* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command.

See the [[Howto thermostat]{.doc}]Howto_thermostat.md){.reference .internal} page for a discussion of different ways to compute temperature and perform thermostatting.

------------------------------------------------------------------------

The keyword/value option pairs are used in the following ways.

For the *bias* keyword, *bias-ID* refers to the ID of a temperature compute that removes a "bias" velocity from each atom. This allows compute temp/sphere to compute its thermal temperature after the translational kinetic energy components have been altered in a prescribed way (e.g., to remove a flow velocity profile). Thermostats that use this compute will work with this bias term. See the doc pages for individual computes that calculate a temperature and the doc pages for fixes that perform thermostatting for more details.

For the *dof* keyword, a setting of *all* calculates a temperature that includes both translational and rotational degrees of freedom. A setting of *rotate* calculates a temperature that includes only rotational degrees of freedom.
:::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the temperature) and a global vector of length 6 (symmetric tensor), which can be accessed by indices 1--6. These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "intensive". The vector values are "extensive".

The scalar value is in temperature [[units]{.doc}]units.md){.reference .internal}. The vector values are in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix requires that atoms store torque and angular velocity (omega) and a radius as defined by the [[atom_style sphere]{.doc}]atom_style.md){.reference .internal} command.

All particles in the group must be finite-size spheres, or point particles with radius = 0.0.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute temp]{.doc}]compute_temp.md){.reference .internal}, [[compute temp/asphere]{.doc}]compute_temp.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are no bias and dof = all.
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

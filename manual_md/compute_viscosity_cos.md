::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#compute-viscosity-cos-command .section}
[]{#index-0}

# compute viscosity/cos command[](#compute-viscosity-cos-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID viscosity/cos
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- viscosity/cos = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    units    real
    compute  cos all viscosity/cos
    variable V equal c_cos[7]
    variable A equal 0.02E-5  # A/fs^2
    variable density equal density
    variable lz equal lz
    variable reciprocalViscosity equal v_V/${A}/v_density*39.4784/v_lz/v_lz*100  # 1/(Pa*s)
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the velocity amplitude of a group of atoms with an cosine-shaped velocity profile and the temperature of them after subtracting out the velocity profile before computing the kinetic energy. A compute of this style can be used by any command that computes a temperature (e.g., [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal}, [[fix npt]{.doc}]fix_nh.md){.reference .internal}).

This command together with [[fix_accelerate/cos]{.doc}]fix_accelerate_cos.md){.reference .internal} enables viscosity calculation with periodic perturbation method, as described by [[Hess]{.std .std-ref}](#hess1){.reference .internal}. An acceleration along the [\\(x\\)]{.math .notranslate .nohighlight}-direction is applied to the simulation system by using [[fix_accelerate/cos]{.doc}]fix_accelerate_cos.md){.reference .internal} command. The acceleration is a periodic function along the [\\(z\\)]{.math .notranslate .nohighlight}-direction:

::: {.math .notranslate .nohighlight}
\\\[a\_{x}(z) = A \\cos \\left(\\frac{2 \\pi z}{l\_{z}}\\right)\\\]
:::

where [\\(A\\)]{.math .notranslate .nohighlight} is the acceleration amplitude, [\\(l_z\\)]{.math .notranslate .nohighlight} is the [\\(z\\)]{.math .notranslate .nohighlight}-length of the simulation box. At steady state, the acceleration generates a velocity profile:

::: {.math .notranslate .nohighlight}
\\\[v\_{x}(z) = V \\cos \\left(\\frac{2 \\pi z}{l\_{z}}\\right)\\\]
:::

The generated velocity amplitude [\\(V\\)]{.math .notranslate .nohighlight} is related to the shear viscosity [\\(\\eta\\)]{.math .notranslate .nohighlight} by

::: {.math .notranslate .nohighlight}
\\\[V = \\frac{A \\rho}{\\eta}\\left(\\frac{l\_{z}}{2 \\pi}\\right)\^{2},\\\]
:::

and it can be obtained from ensemble average of the velocity profile via

::: {.math .notranslate .nohighlight}
\\\[V = \\frac{\\sum\\limits_i 2 m\_{i} v\_{i, x} \\cos \\left(\\frac{2 \\pi z_i}{l\_{z}}\\right)}{\\sum\\limits_i m\_{i}}\\\]
:::

where [\\(m_i\\)]{.math .notranslate .nohighlight}, [\\(v\_{i,x}\\)]{.math .notranslate .nohighlight} and [\\(z_i\\)]{.math .notranslate .nohighlight} are the mass, [\\(x\\)]{.math .notranslate .nohighlight}-component velocity, and [\\(z\\)]{.math .notranslate .nohighlight}-coordinate of a particle, respectively.

After the cosine-shaped collective velocity in the [\\(x\\)]{.math .notranslate .nohighlight}-direction has been subtracted for each atom, the temperature is calculated by the formula

::: {.math .notranslate .nohighlight}
\\\[\\text{KE} = \\frac{\\text{dim}}{2} N k_B T,\\\]
:::

where KE is the total kinetic energy of the group of atoms (sum of [\\(\\frac12 m v\^2\\)]{.math .notranslate .nohighlight}), dim = 2 or 3 is the dimensionality of the simulation, [\\(N\\)]{.math .notranslate .nohighlight} is the number of atoms in the group, [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant, and [\\(T\\)]{.math .notranslate .nohighlight} is the absolute temperature.

A symmetric tensor, stored as a six-element vector, is also calculated by this compute for use in the computation of a pressure tensor by the [[compute pressue]{.doc}]compute_pressure.md){.reference .internal} command. The formula for the components of the tensor is the same as the above expression for [\\(E\_\\mathrm{kin}\\)]{.math .notranslate .nohighlight}, except that the 1/2 factor is NOT included and the [\\(v_i\^2\\)]{.math .notranslate .nohighlight} is replaced by [\\(v\_{i,x} v\_{i,y}\\)]{.math .notranslate .nohighlight} for the [\\(xy\\)]{.math .notranslate .nohighlight} component, and so on. Note that because it lacks the 1/2 factor, these tensor components are twice those of the traditional kinetic energy tensor. The six components of the vector are ordered [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}.

The number of atoms contributing to the temperature is assumed to be constant for the duration of the run; use the *dynamic* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command if this is not the case. However, in order to get meaningful results, the group ID of this compute should be all.

The removal of the cosine-shaped velocity component by this command is essentially computing the temperature after a "bias" has been removed from the velocity of the atoms. If this compute is used with a fix command that performs thermostatting then this bias will be subtracted from each atom, thermostatting of the remaining thermal velocity will be performed, and the bias will be added back in. Thermostatting fixes that work in this way include [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, [[fix temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal}, and [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}.

This compute subtracts out degrees of freedom due to fixes that constrain molecular motion, such as [[fix shake]{.doc}]fix_shake.md){.reference .internal} and [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}. This means that the temperature of groups of atoms that include these constraints will be computed correctly. If needed, the subtracted degrees of freedom can be altered using the *extra* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command.

See the [[Howto thermostat]{.doc}]Howto_thermostat.md){.reference .internal} page for a discussion of different ways to compute temperature and perform thermostatting.
::::::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the temperature) and a global vector of length 7, which can be accessed by indices 1--7. The first six elements of the vector are those of the symmetric tensor discussed above. The seventh is the cosine-shaped velocity amplitude [\\(V\\)]{.math .notranslate .nohighlight}, which can be used to calculate the reciprocal viscosity, as shown in the example. These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "intensive". The first six elements of vector values are "extensive", and the seventh element of vector values is "intensive".

The scalar value is in temperature [[units]{.doc}]units.md){.reference .internal}. The first six elements of vector values are in energy [[units]{.doc}]units.md){.reference .internal}. The seventh element of vector value us in velocity [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the MISC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Since this compute depends on [[fix accelerate/cos]{.doc}]fix_accelerate_cos.md){.reference .internal} which can only work for 3d systems, it cannot be used for 2d systems.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix accelerate/cos]{.doc}]fix_accelerate_cos.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Hess)** Hess, B. The Journal of Chemical Physics 2002, 116 (1), 209-217.
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

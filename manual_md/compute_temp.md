::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#compute-temp-command .section}
[]{#index-1}[]{#index-0}

# compute temp command[](#compute-temp-command "Link to this heading"){.headerlink}

Accelerator Variants: *temp/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID temp
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- temp = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all temp
    compute myTemp mobile temp
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the temperature of a group of atoms. A compute of this style can be used by any command that computes a temperature, e.g. [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal}, [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, [[fix npt]{.doc}]fix_nh.md){.reference .internal}, etc.

The temperature is calculated by the formula

::: {.math .notranslate .nohighlight}
\\\[T = \\frac{2 E\_\\mathrm{kin}}{N\_\\mathrm{DOF} k_B} \\quad \\mathrm{with} \\quad E\_\\mathrm{kin} = \\sum\^{N\_\\mathrm{atoms}}\_{i=1} \\frac{1}{2} m_i v\^2_i \\quad \\mathrm{and} \\quad N\_\\mathrm{DOF} = n\_\\mathrm{dim} N\_\\mathrm{atoms} - n\_\\mathrm{dim} - N\_\\mathrm{fix DOFs}\\\]
:::

where [\\(E\_\\mathrm{kin}\\)]{.math .notranslate .nohighlight} is the total kinetic energy of the group of atoms, [\\(n\_\\mathrm{dim}\\)]{.math .notranslate .nohighlight} is the dimensionality of the simulation (i.e. either 2 or 3), [\\(N\_\\mathrm{atoms}\\)]{.math .notranslate .nohighlight} is the number of atoms in the group, [\\(N\_\\mathrm{fix DOFs}\\)]{.math .notranslate .nohighlight} is the number of degrees of freedom removed by fix commands (see below), [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant, and [\\(T\\)]{.math .notranslate .nohighlight} is the resulting computed temperature.

A symmetric tensor, stored as a six-element vector, is also calculated by this compute for use in the computation of a pressure tensor by the [[compute pressue]{.doc}]compute_pressure.md){.reference .internal} command. The formula for the components of the tensor is the same as the above expression for [\\(E\_\\mathrm{kin}\\)]{.math .notranslate .nohighlight}, except that the 1/2 factor is NOT included and the [\\(v_i\^2\\)]{.math .notranslate .nohighlight} is replaced by [\\(v\_{i,x} v\_{i,y}\\)]{.math .notranslate .nohighlight} for the [\\(xy\\)]{.math .notranslate .nohighlight} component, and so on. Note that because it lacks the 1/2 factor, these tensor components are twice those of the traditional kinetic energy tensor. The six components of the vector are ordered [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}.

The number of atoms contributing to the temperature is assumed to be constant for the duration of the run; use the *dynamic* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command if this is not the case.

This compute subtracts out degrees-of-freedom due to fixes that constrain molecular motion, such as [[fix shake]{.doc}]fix_shake.md){.reference .internal} and [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}. This means the temperature of groups of atoms that include these constraints will be computed correctly. If needed, the subtracted degrees-of-freedom can be altered using the *extra* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command. By default this *extra* component is initialized to [\\(n\_\\mathrm{dim}\\)]{.math .notranslate .nohighlight} (as shown in the formula above) to represent the degrees of freedom removed from a system due to its translation invariance due to periodic boundary conditions.

A compute of this style with the ID of "thermo_temp" is created when LAMMPS starts up, as if this command were in the input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute thermo_temp all temp
:::
::::

See the "thermo_style" command for more details.

See the [[Howto thermostat]{.doc}]Howto_thermostat.md){.reference .internal} page for a discussion of different ways to compute temperature and perform thermostatting.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the temperature) and a global vector of length six (symmetric tensor), which can be accessed by indices 1--6. These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "intensive". The vector values are "extensive".

The scalar value is in temperature [[units]{.doc}]units.md){.reference .internal}. The vector values are in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute temp/partial]{.doc}]compute_temp_partial.md){.reference .internal}, [[compute temp/region]{.doc}]compute_temp_region.md){.reference .internal}, [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

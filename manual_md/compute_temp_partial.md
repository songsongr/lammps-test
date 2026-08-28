::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-temp-partial-command .section}
[]{#index-0}

# compute temp/partial command[](#compute-temp-partial-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID temp/partial xflag yflag zflag
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- temp/partial = style name of this compute command

- xflag,yflag,zflag = 0/1 for whether to exclude/include this dimension
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute newT flow temp/partial 1 1 0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the temperature of a group of atoms, after excluding one or more velocity components. A compute of this style can be used by any command that computes a temperature (e.g. [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal}, [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, [[fix npt]{.doc}]fix_nh.md){.reference .internal}).

The temperature is calculated by the formula

::: {.math .notranslate .nohighlight}
\\\[\\text{KE} = \\frac{\\text{dim}}{2} N k_B T,\\\]
:::

where KE is the total kinetic energy of the group of atoms (sum of [\\(\\frac12 m v\^2\\)]{.math .notranslate .nohighlight}), dim = 2 or 3 is the dimensionality of the simulation, [\\(N\\)]{.math .notranslate .nohighlight} is the number of atoms in the group, [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant, and [\\(T\\)]{.math .notranslate .nohighlight} = temperature. The calculation of KE excludes the [\\(x\\)]{.math .notranslate .nohighlight}, [\\(y\\)]{.math .notranslate .nohighlight}, or [\\(z\\)]{.math .notranslate .nohighlight} dimensions if *xflag*, *yflag*, or *zflag* is 0. The dim parameter is adjusted to give the correct number of degrees of freedom.

A symmetric tensor, stored as a six-element vector, is also calculated by this compute for use in the computation of a pressure tensor by the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} command. The formula for the components of the tensor is the same as the above expression for [\\(E\_\\mathrm{kin}\\)]{.math .notranslate .nohighlight}, except that the 1/2 factor is NOT included and the [\\(v_i\^2\\)]{.math .notranslate .nohighlight} is replaced by [\\(v\_{i,x} v\_{i,y}\\)]{.math .notranslate .nohighlight} for the [\\(xy\\)]{.math .notranslate .nohighlight} component, and so on. Note that because it lacks the 1/2 factor, these tensor components are twice those of the traditional kinetic energy tensor. The six components of the vector are ordered [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}.

The number of atoms contributing to the temperature is assumed to be constant for the duration of the run; use the *dynamic* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command if this is not the case.

The removal of velocity components by this fix is essentially computing the temperature after a "bias" has been removed from the velocity of the atoms. If this compute is used with a fix command that performs thermostatting then this bias will be subtracted from each atom, thermostatting of the remaining thermal velocity will be performed, and the bias will be added back in. Thermostatting fixes that work in this way include [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, [[fix temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal}, and [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}.

This compute subtracts out degrees-of-freedom due to fixes that constrain molecular motion, such as [[fix shake]{.doc}]fix_shake.md){.reference .internal} and [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}. This means the temperature of groups of atoms that include these constraints will be computed correctly. If needed, the subtracted degrees-of-freedom can be altered using the *extra* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command.

See the [[Howto thermostat]{.doc}]Howto_thermostat.md){.reference .internal} page for a discussion of different ways to compute temperature and perform thermostatting.
::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the temperature) and a global vector of length 6 (symmetric tensor), which can be accessed by indices 1--6. These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "intensive". The vector values are "extensive".

The scalar value is in temperature [[units]{.doc}]units.md){.reference .internal}. The vector values are in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute temp]{.doc}]compute_temp.md){.reference .internal}, [[compute temp/region]{.doc}]compute_temp_region.md){.reference .internal}, [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

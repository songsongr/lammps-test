:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#compute-temp-eff-command .section}
[]{#index-0}

# compute temp/eff command[](#compute-temp-eff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID temp/eff
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- temp/eff = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all temp/eff
    compute myTemp mobile temp/eff
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the temperature of a group of nuclei and electrons in the [[electron force field]{.doc}]pair_eff.md){.reference .internal} model. A compute of this style can be used by commands that compute a temperature (e.g., [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal}, [[fix npt/eff]{.doc}]fix_nh_eff.md){.reference .internal}).

The temperature is calculated by the formula

::: {.math .notranslate .nohighlight}
\\\[\\text{KE} = \\frac{\\text{dim}}{2} N k_B T,\\\]
:::

where KE is the total kinetic energy of the group of atoms (sum of [\\(\\frac12 m v\^2\\)]{.math .notranslate .nohighlight} for nuclei and sum of [\\(\\frac12 (m v\^2 + \\frac34 m s\^2\\)]{.math .notranslate .nohighlight}) for electrons, where [\\(s\\)]{.math .notranslate .nohighlight} includes the radial electron velocity contributions), dim = 2 or 3 is the dimensionality of the simulation, [\\(N\\)]{.math .notranslate .nohighlight} is the number of atoms (only total number of nuclei in the eFF (see the [[pair_eff]{.doc}]pair_style.md){.reference .internal} command) in the group, [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant, and [\\(T\\)]{.math .notranslate .nohighlight} is the absolute temperature. This expression is summed over all nuclear and electronic degrees of freedom, essentially by setting the kinetic contribution to the heat capacity to [\\(\\frac32 k\\)]{.math .notranslate .nohighlight} (where only nuclei contribute). This subtlety is valid for temperatures well below the Fermi temperature, which for densities two to five times the density of liquid hydrogen ranges from 86,000 to 170,000 K.

::: {.admonition .note}
Note

For eFF models, in order to override the default temperature reported by LAMMPS in the thermodynamic quantities reported via the [[thermo]{.doc}]thermo.md){.reference .internal} command, the user should apply a [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} command, as shown in the following example:
:::

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute         effTemp all temp/eff
    thermo_style    custom step etotal pe ke temp press
    thermo_modify   temp effTemp
:::
::::

A six-component kinetic energy tensor is also calculated by this compute for use in the computation of a pressure tensor. The formula for the components of the tensor is the same as the above formula, except that [\\(v\^2\\)]{.math .notranslate .nohighlight} is replaced by [\\(v_x v_y\\)]{.math .notranslate .nohighlight} for the [\\(xy\\)]{.math .notranslate .nohighlight} component, etc. For the eFF, again, the radial electronic velocities are also considered.

The number of atoms contributing to the temperature is assumed to be constant for the duration of the run; use the *dynamic* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command if this is not the case.

This compute subtracts out degrees-of-freedom due to fixes that constrain molecular motion, such as [[fix shake]{.doc}]fix_shake.md){.reference .internal} and [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}. This means the temperature of groups of atoms that include these constraints will be computed correctly. If needed, the subtracted degrees-of-freedom can be altered using the *extra* option of the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command.

See the [[Howto thermostat]{.doc}]Howto_thermostat.md){.reference .internal} page for a discussion of different ways to compute temperature and perform thermostatting.
:::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

The scalar value calculated by this compute is "intensive", meaning it is independent of the number of atoms in the simulation. The vector values are "extensive", meaning they scale with the number of atoms in the simulation.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute temp/partial]{.doc}]compute_temp_partial.md){.reference .internal}, [[compute temp/region]{.doc}]compute_temp_region.md){.reference .internal}, [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

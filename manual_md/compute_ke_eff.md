::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#compute-ke-eff-command .section}
[]{#index-0}

# compute ke/eff command[](#compute-ke-eff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID ke/eff
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- ke/eff = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all ke/eff
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the kinetic energy of motion of a group of eFF particles (nuclei and electrons), as modeled with the [[electronic force field]{.doc}]pair_eff.md){.reference .internal}.

The kinetic energy for each nucleus is computed as [\\(\\frac{1}{2} m v\^2\\)]{.math .notranslate .nohighlight} and the kinetic energy for each electron is computed as [\\(\\frac{1}{2}(m_e v\^2 + \\frac{3}{4} m_e s\^2)\\)]{.math .notranslate .nohighlight}, where [\\(m\\)]{.math .notranslate .nohighlight} corresponds to the nuclear mass, [\\(m_e\\)]{.math .notranslate .nohighlight} to the electron mass, [\\(v\\)]{.math .notranslate .nohighlight} to the translational velocity of each particle, and [\\(s\\)]{.math .notranslate .nohighlight} to the radial velocity of the electron, respectively.

There is a subtle difference between the quantity calculated by this compute and the kinetic energy calculated by the *ke* or *etotal* keyword used in thermodynamic output, as specified by the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command. For this compute, kinetic energy is "translational" and "radial" (only for electrons) kinetic energy, calculated by the simple formula above. For thermodynamic output, the *ke* keyword infers kinetic energy from the temperature of the system with [\\(\\frac{1}{2} k_B T\\)]{.math .notranslate .nohighlight} of energy for each degree of freedom. For the eFF temperature computation via the [[compute temp_eff]{.doc}]compute_temp_eff.md){.reference .internal} command, these are the same. But different computes that calculate temperature can subtract out different non-thermal components of velocity and/or include other degrees of freedom.

::: {.admonition .warning}
Warning

The temperature in eFF models should be monitored via the [[compute temp/eff]{.doc}]compute_temp_eff.md){.reference .internal} command, which can be printed with thermodynamic output by using the [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} command, as shown in the following example:
:::

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute         effTemp all temp/eff
    thermo_style    custom step etotal pe ke temp press
    thermo_modify   temp effTemp
:::
::::

See [[compute temp/eff]{.doc}]compute_temp_eff.md){.reference .internal}.
::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the KE). This value can be used by any command that uses a global scalar value from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "extensive". The scalar value will be in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

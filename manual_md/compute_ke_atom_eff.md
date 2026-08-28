::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#compute-ke-atom-eff-command .section}
[]{#index-0}

# compute ke/atom/eff command[](#compute-ke-atom-eff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID ke/atom/eff
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- ke/atom/eff = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all ke/atom/eff
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the per-atom translational (nuclei and electrons) and radial kinetic energy (electron only) in a group. The particles are assumed to be nuclei and electrons modeled with the [[electronic force field]{.doc}]pair_eff.md){.reference .internal}.

The kinetic energy for each nucleus is computed as [\\(\\frac{1}{2} m v\^2\\)]{.math .notranslate .nohighlight}, where *m* corresponds to the corresponding nuclear mass, and the kinetic energy for each electron is computed as [\\(\\frac{1}{2} (m_e v\^2 + \\frac{3}{4} m_e s\^2)\\)]{.math .notranslate .nohighlight}, where [\\(m_e\\)]{.math .notranslate .nohighlight} and *v* correspond to the mass and translational velocity of each electron, and *s* to its radial velocity, respectively.

There is a subtle difference between the quantity calculated by this compute and the kinetic energy calculated by the *ke* or *etotal* keyword used in thermodynamic output, as specified by the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command. For this compute, kinetic energy is "translational" plus electronic "radial" kinetic energy, calculated by the simple formula above. For thermodynamic output, the *ke* keyword infers kinetic energy from the temperature of the system with [\\(\\frac{1}{2} k_B T\\)]{.math .notranslate .nohighlight} of energy for each (nuclear-only) degree of freedom in eFF.

::: {.admonition .note}
Note

The temperature in eFF should be monitored via the [[compute temp/eff]{.doc}]compute_temp_eff.md){.reference .internal} command, which can be printed with thermodynamic output by using the [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} command, as shown in the following example:
:::

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute         effTemp all temp/eff
    thermo_style    custom step etotal pe ke temp press
    thermo_modify   temp effTemp
:::
::::

The value of the kinetic energy will be 0.0 for atoms (nuclei or electrons) not in the specified compute group.
::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a scalar quantity for each atom, which can be accessed by any command that uses per-atom computes as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The per-atom vector values will be in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dump custom]{.doc}]dump.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

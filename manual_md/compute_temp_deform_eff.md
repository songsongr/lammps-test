::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-temp-deform-eff-command .section}
[]{#index-0}

# compute temp/deform/eff command[](#compute-temp-deform-eff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID temp/deform/eff keyword value ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- temp/deform/eff = style name of this compute command

- zero or more keyword/value pairs may be appended

- keyword = *temp*

  ``` literal-block
  temp value = compute ID that calculates a temperature
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute myTemp all temp/deform/eff
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the temperature of a group of nuclei and electrons in the [[electron force field]{.doc}]pair_eff.md){.reference .internal} model, after subtracting out a streaming velocity induced by the simulation box changing size and/or shape, for example in a non-equilibrium MD (NEMD) simulation. The size/shape change is induced by use of the [[fix deform]{.doc}]fix_deform.md){.reference .internal} command. A compute of this style is created by the [[fix nvt/sllod/eff]{.doc}]fix_nvt_sllod_eff.md){.reference .internal} command to compute the thermal temperature of atoms for thermostatting purposes. A compute of this style can also be used by any command that computes a temperature (e.g., [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal}, [[fix npt/eff]{.doc}]fix_nh_eff.md){.reference .internal}).

The calculation performed by this compute is exactly like that described by the [[compute temp/deform]{.doc}]compute_temp_deform.md){.reference .internal} command, except that the formulas for the temperature (scalar) and diagonal components of the symmetric tensor (vector) include the radial electron velocity contributions, as discussed by the [[compute temp/eff]{.doc}]compute_temp_eff.md){.reference .internal} command. Note that only the translational degrees of freedom for each nuclei or electron are affected by the streaming velocity adjustment. The radial velocity component of the electrons is not affected.

::: versionchanged
[Changed in version 11Feb2026.]{.versionmodified .changed}
:::

By default, the internal temperature compute has the style [[compute temp/eff]{.doc}]compute_temp_eff.md){.reference .internal}. If an internal temperature compute is used which does not have the /eff suffix, the contribution to the scalar and vector values due to the radial electron velocity will be added in by this compute.
::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the temperature) and a global vector of length 6 (symmetric tensor), which can be accessed by indices 1--6. These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "intensive". The vector values are "extensive".

The scalar value is in temperature [[units]{.doc}]units.md){.reference .internal}. The vector values are in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute temp/ramp]{.doc}]compute_temp_ramp.md){.reference .internal}, [[fix deform]{.doc}]fix_deform.md){.reference .internal}, [[fix nvt/sllod/eff]{.doc}]fix_nvt_sllod_eff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

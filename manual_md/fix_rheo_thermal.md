::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-rheo-thermal-command .section}
[]{#index-0}

# fix rheo/thermal command[](#fix-rheo-thermal-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-none .notranslate}
::: highlight
    fix ID group-ID rheo/thermal attribute values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- rheo/thermal = style name of this fix command

- one or more attributes may be appended

- attribute = *conductivity* or *specific/heat* or *latent/heat* or *Tfreeze* or *react*

  ``` literal-block
  conductivity args = types style args
    types = lists of types (see below)
    style = constant
      constant arg = conductivity (power/(length*temperature))
  specific/heat args = types style args
    types = lists of types (see below)
    style = constant
      constant arg = specific heat (energy/(mass*temperature))
  latent/heat args = types style args
    types = lists of types (see below)
    style = constant
      constant arg = latent heat (energy/mass)
  Tfreeze args = types style args
    types = lists of types (see below)
    style = constant
      constant arg = freezing temperature (temperature)
  react args = cut type
    cut = maximum bond distance
    type = bond type
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all rheo/thermal conductivity * constant 1.0 specific/heat * constant 1.0 Tfreeze * constant 1.0
    fix 1 all rheo/pressure conductivity 1*2 constant 1.0 conductivity 3*4 constant 2.0 specific/heat * constant 1.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 29Aug2024.]{.versionmodified .added}
:::

This fix performs time integration of temperature for atom style rheo/thermal. In addition, it defines multiple thermal properties of particles and handles melting/solidification, if applicable. For more details on phase transitions in RHEO, see [[the RHEO howto]{.doc}]Howto_rheo.md){.reference .internal}.

Note that the temperature of a particle is always derived from the energy. This implies the *temperature* attribute of [[the set command]{.doc}]set.md){.reference .internal} does not affect particles. Instead, one should use the *sph/e* attribute.

For each atom type, one can define expressions for the *conductivity*, *specific/heat*, *latent/heat*, and critical temperature (*Tfreeze*). The conductivity and specific heat must be defined for all atom types. The latent heat and critical temperature are optional. However, a critical temperature must be defined to specify a latent heat.

Note, if shifting is turned on in [[fix rheo]{.doc}]fix_rheo.md){.reference .internal}, the gradient of the energy is used to shift energies. This may be inappropriate in systems with multiple atom types with different specific heats.

For each property, one must first define a list of atom types. A wild-card asterisk can be used in place of or in conjunction with the *types* argument to set values for multiple atom types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of atom types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive).

The *types* definition for each property is followed by the style. Currently, the only option is *constant*. Style *constant* simply applies a constant value of respective property to each particle of the assigned type.

The *react* keyword controls whether bonds are created/deleted when particles transition between a fluid and solid state. This option only applies to atom types that have a defined value of *Tfreeze*. When a fluid particle's temperature drops below *Tfreeze*, bonds of type *btype* are created between nearby solid particles within a distance of *cut*. The particle's status also swaps to a solid state. When a solid particle's temperature rises above *Tfreeze*, all bonds of type *btype* are broken and the particle's status swaps to a fluid state.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix must be used with an atom style that includes temperature, heatflow, and conductivity such as atom_style rheo/thermal This fix must be used in conjunction with [[fix rheo]{.doc}]fix_rheo.md){.reference .internal} with the *thermal* setting. The fix group must be set to all. Only one instance of fix rheo/pressure can be defined.

This fix is part of the RHEO package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix rheo]{.doc}]fix_rheo.md){.reference .internal}, [[pair rheo]{.doc}]pair_rheo.md){.reference .internal}, [[compute rheo/property/atom]{.doc}]compute_rheo_property_atom.md){.reference .internal}, [[fix add/heat]{.doc}]fix_add_heat.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

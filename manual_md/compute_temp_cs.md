::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-temp-cs-command .section}
[]{#index-0}

# compute temp/cs command[](#compute-temp-cs-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID temp/cs group1 group2
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- temp/cs = style name of this compute command

- group1 = group-ID of either cores or shells

- group2 = group-ID of either shells or cores
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute oxygen_c-s all temp/cs O_core O_shell
    compute core_shells all temp/cs cores shells
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the temperature of a system based on the center-of-mass velocity of atom pairs that are bonded to each other. This compute is designed to be used with the adiabatic core/shell model of [[(Mitchell and Fincham)]{.std .std-ref}](#mitchellfincham1){.reference .internal}. See the [[Howto coreshell]{.doc}]Howto_coreshell.md){.reference .internal} page for an overview of the model as implemented in LAMMPS. Specifically, this compute enables correct temperature calculation and thermostatting of core/shell pairs where it is desirable for the internal degrees of freedom of the core/shell pairs to not be influenced by a thermostat. A compute of this style can be used by any command that computes a temperature via [[fix_modify]{.doc}]fix_modify.md){.reference .internal} (e.g., [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, [[fix npt]{.doc}]fix_nh.md){.reference .internal}).

Note that this compute does not require all ions to be polarized, hence defined as core/shell pairs. One can mix core/shell pairs and ions without a satellite particle if desired. The compute will consider the non-polarized ions according to the physical system.

For this compute, core and shell particles are specified by two respective group IDs, which can be defined using the [[group]{.doc}]group.md){.reference .internal} command. The number of atoms in the two groups must be the same and there should be one bond defined between a pair of atoms in the two groups. Non-polarized ions which might also be included in the treated system should not be included into either of these groups, they are taken into account by the *group-ID* (second argument) of the compute.

The temperature is calculated by the formula

::: {.math .notranslate .nohighlight}
\\\[\\text{KE} = \\frac{\\text{dim}}{2} N k_B T,\\\]
:::

where KE is the total kinetic energy of the group of atoms (sum of [\\(\\frac12 m v\^2\\)]{.math .notranslate .nohighlight}), dim = 2 or 3 is the dimensionality of the simulation, [\\(N\\)]{.math .notranslate .nohighlight} is the number of atoms in the group, [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant, and [\\(T\\)]{.math .notranslate .nohighlight} is the absolute temperature. Note that the velocity of each core or shell atom used in the KE calculation is the velocity of the center-of-mass (COM) of the core/shell pair the atom is part of.

A symmetric tensor, stored as a six-element vector, is also calculated by this compute for use in the computation of a pressure tensor by the [[compute pressue]{.doc}]compute_pressure.md){.reference .internal} command. The formula for the components of the tensor is the same as the above expression for [\\(E\_\\mathrm{kin}\\)]{.math .notranslate .nohighlight}, except that the 1/2 factor is NOT included and the [\\(v_i\^2\\)]{.math .notranslate .nohighlight} is replaced by [\\(v\_{i,x} v\_{i,y}\\)]{.math .notranslate .nohighlight} for the [\\(xy\\)]{.math .notranslate .nohighlight} component, and so on. Note that because it lacks the 1/2 factor, these tensor components are twice those of the traditional kinetic energy tensor. The six components of the vector are ordered [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}.

The change this fix makes to core/shell atom velocities is essentially computing the temperature after a "bias" has been removed from the velocity of the atoms. This "bias" is the velocity of the atom relative to the center-of-mass velocity of the core/shell pair. If this compute is used with a fix command that performs thermostatting then this bias will be subtracted from each atom, thermostatting of the remaining center-of-mass velocity will be performed, and the bias will be added back in. This means the thermostatting will effectively be performed on the core/shell pairs, instead of on the individual core and shell atoms. Thermostatting fixes that work in this way include [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}, [[fix temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal}, and [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}.

The internal energy of core/shell pairs can be calculated by the [[compute temp/chunk]{.doc}]compute_temp_chunk.md){.reference .internal} command, if chunks are defined as core/shell pairs. See the [[Howto coreshell]{.doc}]Howto_coreshell.md){.reference .internal} doc page for more discussion on how to do this.
::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the temperature) and a global vector of length 6 (symmetric tensor), which can be accessed by indices 1--6. These values can be used by any command that uses global scalar or vector values from a compute as input.

The scalar value calculated by this compute is "intensive". The vector values are "extensive".

The scalar value is in temperature [[units]{.doc}]units.md){.reference .internal}. The vector values are in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The number of core/shell pairs contributing to the temperature is assumed to be constant for the duration of the run. No fixes should be used which generate new molecules or atoms during a simulation.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute temp]{.doc}]compute_temp.md){.reference .internal}, [[compute temp/chunk]{.doc}]compute_temp_chunk.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Mitchell and Fincham)** Mitchell, Fincham, J Phys Condensed Matter, 5, 1031-1038 (1993).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

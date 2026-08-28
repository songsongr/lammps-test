:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-temp-drude-command .section}
[]{#index-0}

# compute temp/drude command[](#compute-temp-drude-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID temp/drude
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- temp/drude = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute TDRUDE all temp/drude
:::
::::

Example input scripts available: [`examples/PACKAGES/drude`{.file .docutils .literal .notranslate}]{.pre}.
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the temperatures of core--Drude pairs. This compute is designed to be used with the [[thermalized Drude oscillator model]{.doc}]Howto_drude.md){.reference .internal}. Polarizable models in LAMMPS are described on the [[Howto polarizable]{.doc}]Howto_polarizable.md){.reference .internal} doc page.

Drude oscillators consist of a core particle and a Drude particle connected by a harmonic bond, and the relative motion of these Drude oscillators is usually maintained cold by a specific thermostat that acts on the relative motion of the core--Drude particle pairs. Therefore, because LAMMPS considers Drude particles as normal atoms in its default temperature compute ([[compute temp]{.doc}]compute_temp.md){.reference .internal} command), the reduced temperature of the core--Drude particle pairs is not calculated correctly.

By contrast, this compute calculates the temperature of the cores using center-of-mass velocities of the core--Drude pairs, and the reduced temperature of the Drude particles using the relative velocities of the Drude particles with respect to their cores. Non-polarizable atoms are considered as cores. Their velocities contribute to the temperature of the cores.
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the temperature) and a global vector of length 6, which can be accessed by indices 1--6, whose components are

1.  temperature of the centers of mass (temperature units)

2.  temperature of the dipoles (temperature units)

3.  number of degrees of freedom of the centers of mass

4.  number of degrees of freedom of the dipoles

5.  kinetic energy of the centers of mass (energy units)

6.  kinetic energy of the dipoles (energy units)

These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

Both the scalar value and the first two values of the vector calculated by this compute are "intensive". The other four vector values are "extensive".
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The number of degrees of freedom contributing to the temperature is assumed to be constant for the duration of the run unless the [[fix_modify command]{.doc}]fix_modify.md){.reference .internal} sets the option *dynamic/dof yes*.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix drude]{.doc}]fix_drude.md){.reference .internal}, [[fix langevin/drude]{.doc}]fix_langevin_drude.md){.reference .internal}, [[fix drude/transform]{.doc}]fix_drude_transform.md){.reference .internal}, [[pair_style thole]{.doc}]pair_thole.md){.reference .internal}, [[compute temp]{.doc}]compute_temp.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

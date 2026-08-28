:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-smd-internal-energy-command .section}
[]{#index-0}

# compute smd/internal/energy command[](#compute-smd-internal-energy-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID smd/internal/energy
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- smd/smd/internal/energy = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all smd/internal/energy
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation which outputs the per-particle enthalpy, i.e., the sum of potential energy and heat.

See [this PDF guide](PDF/MACHDYN_LAMMPS_userguide.pdf){.reference .external} to use Smooth Mach Dynamics in LAMMPS.
:::

::: {#output-info .section}
## Output Info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-particle vector, which can be accessed by any command that uses per-particle values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The per-particle vector values will be given in [[units]{.doc}]units.md){.reference .internal} of energy.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the MACHDYN package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. This compute can only be used for particles which interact via the updated Lagrangian or total Lagrangian SPH pair styles.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

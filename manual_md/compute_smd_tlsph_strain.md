:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-smd-tlsph-strain-command .section}
[]{#index-0}

# compute smd/tlsph/strain command[](#compute-smd-tlsph-strain-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID smd/tlsph/strain
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- smd/tlsph/strain = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all smd/tlsph/strain
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the Green-Lagrange strain tensor for particles interacting via the Total-Lagrangian SPH pair style.

See [this PDF guide](PDF/MACHDYN_LAMMPS_userguide.pdf){.reference .external} to using Smooth Mach Dynamics in LAMMPS.
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-particle vector of vectors (tensors), which can be accessed by any command that uses per-particle values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The per-particle tensor values will be given dimensionless. See [[units]{.doc}]units.md){.reference .internal}.

The per-particle vector has 6 entries, corresponding to the xx, yy, zz, xy, xz, yz components of the symmetric strain tensor.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the MACHDYN package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This quantity will be computed only for particles which interact with the Total-Lagrangian SPH pair style.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[smd/tlsph/strain/rate]{.doc}]compute_smd_tlsph_strain_rate.md){.reference .internal}, [[smd/tlsph/stress]{.doc}]compute_smd_tlsph_stress.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

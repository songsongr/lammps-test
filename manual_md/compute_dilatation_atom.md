:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-dilatation-atom-command .section}
[]{#index-0}

# compute dilatation/atom command[](#compute-dilatation-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID dilatation/atom
:::
::::

- ID, group-ID are documented in compute command

- dilatation/atom = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all dilatation/atom
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the per-atom dilatation for each atom in a group. This is a quantity relevant for [[Peridynamics models]{.doc}]pair_peri.md){.reference .internal}. See [this document](PDF/PDLammps_overview.pdf){.reference .external} for an overview of LAMMPS commands for Peridynamics modeling.

For small deformation, dilatation of is the measure of the volumetric strain.

The dilatation [\\(\\theta\\)]{.math .notranslate .nohighlight} for each peridynamic particle [\\(i\\)]{.math .notranslate .nohighlight} is calculated as a sum over its neighbors with unbroken bonds, where the contribution of the [\\(ij\\)]{.math .notranslate .nohighlight} pair is a function of the change in bond length (versus the initial length in the reference state), the volume fraction of the particles and an influence function. See the [[Peridynamics Howto]{.doc}]Howto_peri.md){.reference .internal} for a formal definition of dilatation.

This command can only be used with a subset of the Peridynamic [[pair styles]{.doc}]pair_peri.md){.reference .internal}: *peri/lps*, *peri/ves*, and *peri/eps*.

The dilatation value will be 0.0 for atoms not in the specified compute group.
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom vector, which can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The per-atom vector values are unitless numbers [\\((\\theta \\ge 0.0)\\)]{.math .notranslate .nohighlight}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the PERI package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute damage/atom]{.doc}]compute_damage_atom.md){.reference .internal}, [[compute plasticity/atom]{.doc}]compute_plasticity_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

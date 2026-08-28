:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-plasticity-atom-command .section}
[]{#index-0}

# compute plasticity/atom command[](#compute-plasticity-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID plasticity/atom
:::
::::

- ID, group-ID are documented in compute command

- plasticity/atom = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all plasticity/atom
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the per-atom plasticity for each atom in a group. This is a quantity relevant for [[Peridynamics models]{.doc}]pair_peri.md){.reference .internal}. See [this document](PDF/PDLammps_overview.pdf){.reference .external} for an overview of LAMMPS commands for Peridynamics modeling.

The plasticity for a Peridynamic particle is the so-called consistency parameter ([\\(\\lambda\\)]{.math .notranslate .nohighlight}). For elastic deformation, [\\(\\lambda = 0\\)]{.math .notranslate .nohighlight}, otherwise [\\(\\lambda \> 0\\)]{.math .notranslate .nohighlight} for plastic deformation. For details, see [[(Mitchell)]{.std .std-ref}](#mitchell){.reference .internal} and the PDF doc included in the LAMMPS distribution in [doc/PDF/PDLammps_EPS.pdf](PDF/PDLammps_EPS.pdf){.reference .external}.

This command can be invoked for one of the Peridynamic [[pair styles]{.doc}]pair_peri.md){.reference .internal}: peri/eps.

The plasticity value will be 0.0 for atoms not in the specified compute group.
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom vector, which can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The per-atom vector values are unitless numbers [\\(\\lambda \\ge 0.0\\)]{.math .notranslate .nohighlight}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the PERI package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute damage/atom]{.doc}]compute_damage_atom.md){.reference .internal}, [[compute dilatation/atom]{.doc}]compute_dilatation_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Mitchell)** Mitchell, "A non-local, ordinary-state-based viscoelasticity model for peridynamics", Sandia National Lab Report, 8064:1-28 (2011).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

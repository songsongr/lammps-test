::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#compute-pressure-uef-command .section}
[]{#index-0}

# compute pressure/uef command[](#compute-pressure-uef-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID pressure/uef temp-ID keyword ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- pressure/uef = style name of this compute command

- temp-ID = ID of compute that calculates temperature, can be NULL if not needed

- zero or more keywords may be appended

- keyword = *ke* or *pair* or *bond* or *angle* or *dihedral* or *improper* or *kspace* or *fix* or *virial*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all pressure/uef my_temp_uef
    compute 2 all pressure/uef my_temp_uef virial
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command is used to compute the pressure tensor in the reference frame of the applied flow field when [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal} or [[fix npt/uef]{.doc}]fix_nh_uef.md){.reference .internal} is used. It is not necessary to use this command to compute the scalar value of the pressure. A [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} may be used for that purpose.

The keywords and output information are documented in [[compute_pressure]{.doc}]compute_pressure.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the UEF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This command can only be used when [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal} or [[fix npt/uef]{.doc}]fix_nh_uef.md){.reference .internal} is active.

The kinetic contribution to the pressure tensor will be accurate only when the compute specified by *temp-ID* is a [[compute temp/uef]{.doc}]compute_temp_uef.md){.reference .internal}.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute pressure]{.doc}]compute_pressure.md){.reference .internal}, [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal}, [[compute temp/uef]{.doc}]compute_temp_uef.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

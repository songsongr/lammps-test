::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#compute-temp-uef-command .section}
[]{#index-0}

# compute temp/uef command[](#compute-temp-uef-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID temp/uef
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- temp/uef = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all temp/uef
    compute 2 sel temp/uef
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command is used to compute the kinetic energy tensor in the reference frame of the applied flow field when [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal} or [[fix npt/uef]{.doc}]fix_nh_uef.md){.reference .internal} is used. It is not necessary to use this command to compute the scalar value of the temperature. A [[compute temp]{.doc}]compute_temp.md){.reference .internal} may be used for that purpose.

Output information for this command can be found in the documentation for [[compute temp]{.doc}]compute_temp.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the UEF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This command can only be used when [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal} or [[fix npt/uef]{.doc}]fix_nh_uef.md){.reference .internal} is active.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute temp]{.doc}]compute_temp.md){.reference .internal}, [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal}, [[compute pressure/uef]{.doc}]compute_pressure_uef.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

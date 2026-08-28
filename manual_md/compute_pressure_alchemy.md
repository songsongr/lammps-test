::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-pressure-alchemy-command .section}
[]{#index-0}

# compute pressure/alchemy command[](#compute-pressure-alchemy-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID pressure/alchemy fix-ID
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- pressure/alchemy = style name of this compute command

- fix-ID = ID of [[fix alchemy]{.doc}]fix_alchemy.md){.reference .internal} command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix trans all alchemy
    compute mixed all pressure/alchemy trans
    thermo_modify press mixed
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 28Mar2023.]{.versionmodified .added}
:::

Define a compute style that makes the "mixed" system pressure available for a system that uses the [[fix alchemy]{.doc}]fix_alchemy.md){.reference .internal} command to transform one topology to another. This can be used in combination with either [[thermo_modify press]{.doc}]thermo_modify.md){.reference .internal} or [[fix_modify press]{.doc}]fix_modify.md){.reference .internal} to output and access a pressure consistent with the simulated combined two topology system.

The actual pressure is determined with [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} commands that are internally used by [[fix alchemy]{.doc}]fix_alchemy.md){.reference .internal} for each topology individually and then combined. This command just extracts the information from the fix.

The [`examples/PACKAGES/alchemy`{.docutils .literal .notranslate}]{.pre} folder contains an example input for this command.
::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the pressure) and a global vector of length 6 (the pressure tensor), which can be accessed by indices 1--6. These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The ordering of values in the symmetric pressure tensor is as follows: [\\(p\_{xx},\\)]{.math .notranslate .nohighlight} [\\(p\_{yy},\\)]{.math .notranslate .nohighlight} [\\(p\_{zz},\\)]{.math .notranslate .nohighlight} [\\(p\_{xy},\\)]{.math .notranslate .nohighlight} [\\(p\_{xz},\\)]{.math .notranslate .nohighlight} [\\(p\_{yz}.\\)]{.math .notranslate .nohighlight}

The scalar and vector values calculated by this compute are "intensive". The scalar and vector values will be in pressure [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the REPLICA package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix alchemy]{.doc}]fix_alchemy.md){.reference .internal}, [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}, [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal}, [[fix_modify]{.doc}]fix_modify.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

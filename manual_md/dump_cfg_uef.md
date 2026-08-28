::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#dump-cfg-uef-command .section}
[]{#index-0}

# dump cfg/uef command[](#dump-cfg-uef-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dump ID group-ID cfg/uef N file mass type xs ys zs args
:::
::::

- ID = user-assigned name for the dump

- group-ID = ID of the group of atoms to be dumped

- N = dump every this many timesteps

- file = name of file to write dump info to

  ``` literal-block
  args = same as args for dump custom
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dump 1 all cfg/uef 10 dump.*.cfg mass type xs ys zs
    dump 2 all cfg/uef 100 dump.*.cfg mass type xs ys zs id c_stress
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command is used to dump atomic coordinates in the reference frame of the applied flow field when [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal} or [[fix npt/uef]{.doc}]fix_nh_uef.md){.reference .internal} is used. Only the atomic coordinates and frame-invariant scalar quantities will be in the flow frame. If velocities are selected as output, for example, they will not be in the same reference frame as the atomic positions.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the UEF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This command can only be used when [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal} or [[fix npt/uef]{.doc}]fix_nh_uef.md){.reference .internal} is active.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dump]{.doc}]dump.md){.reference .internal}, [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-smd-contact-radius-command .section}
[]{#index-0}

# compute smd/contact/radius command[](#compute-smd-contact-radius-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID smd/contact/radius
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- smd/contact/radius = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all smd/contact/radius
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation which outputs the contact radius, i.e., the radius used to prevent particles from penetrating each other. The contact radius is used only to prevent particles belonging to different physical bodies from penetrating each other. It is used by the contact pair styles, e.g., smd/hertz and smd/tri_surface.

See [this PDF guide](PDF/MACHDYN_LAMMPS_userguide.pdf){.reference .external} to using Smooth Mach Dynamics in LAMMPS.

The value of the contact radius will be 0.0 for particles not in the specified compute group.
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-particle vector, which can be accessed by any command that uses per-particle values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The per-particle vector values will be in distance [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the MACHDYN package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dump custom]{.doc}]dump.md){.reference .internal} smd/hertz smd/tri_surface
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

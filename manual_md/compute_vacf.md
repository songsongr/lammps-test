::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#compute-vacf-command .section}
[]{#index-0}

# compute vacf command[](#compute-vacf-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID vacf
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- vacf = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all vacf
    compute 1 upper vacf
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the velocity auto-correlation function (VACF), averaged over a group of atoms. Each atom's contribution to the VACF is its current velocity vector dotted into its initial velocity vector at the time the compute was specified.

A vector of four quantities is calculated by this compute. The first three elements of the vector are [\\(v_x v\_{x,0}\\)]{.math .notranslate .nohighlight} (and similar for the [\\(y\\)]{.math .notranslate .nohighlight} and [\\(z\\)]{.math .notranslate .nohighlight} components), summed and averaged over atoms in the group, where [\\(v_x\\)]{.math .notranslate .nohighlight} is the current [\\(x\\)]{.math .notranslate .nohighlight}-component of the velocity of the atom and [\\(v\_{x,0}\\)]{.math .notranslate .nohighlight} is the initial [\\(x\\)]{.math .notranslate .nohighlight}-component of the velocity of the atom. The fourth element of the vector is the total VACF (i.e., [\\((v_x v\_{x,0} + v_y v\_{y,0} + v_z v\_{z,0})\\)]{.math .notranslate .nohighlight}), summed and averaged over atoms in the group.

The integral of the VACF versus time is proportional to the diffusion coefficient of the diffusing atoms. This can be computed in the following manner, using the [[variable trap()]{.doc}]variable.md){.reference .internal} function:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute         2 all vacf
    fix             5 all vector 1 c_2[4]
    variable        diff equal dt*trap(f_5)
    thermo_style    custom step v_diff
:::
::::

::: {.admonition .note}
Note

If you want the quantities calculated by this compute to be continuous when running from a [[restart file]{.doc}]read_restart.md){.reference .internal}, then you should use the same ID for this compute, as in the original run. This is so that the fix this compute creates to store per-atom quantities will also have the same ID, and thus be initialized correctly with time=0 atom velocities from the restart file.
:::
::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector of length 4, which can be accessed by indices 1--4 by any command that uses global vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The vector values are "intensive". The vector values will be in velocity[\\(\^2\\)]{.math .notranslate .nohighlight} [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute msd]{.doc}]compute_msd.md){.reference .internal}, [[compute vacf/chunk]{.doc}]compute_vacf_chunk.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

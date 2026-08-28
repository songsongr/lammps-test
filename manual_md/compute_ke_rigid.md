:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-ke-rigid-command .section}
[]{#index-0}

# compute ke/rigid command[](#compute-ke-rigid-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID ke/rigid fix-ID
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- ke = style name of this compute command

- fix-ID = ID of rigid body fix
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all ke/rigid myRigid
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the translational kinetic energy of a collection of rigid bodies, as defined by one of the [[fix rigid]{.doc}]fix_rigid.md){.reference .internal} command variants.

The kinetic energy of each rigid body is computed as [\\(\\frac12 M V\_\\text{cm}\^2\\)]{.math .notranslate .nohighlight}, where [\\(M\\)]{.math .notranslate .nohighlight} is the total mass of the rigid body, and [\\(V\_\\text{cm}\\)]{.math .notranslate .nohighlight} is its center-of-mass velocity.

The *fix-ID* should be the ID of one of the [[fix rigid]{.doc}]fix_rigid.md){.reference .internal} commands which defines the rigid bodies. The group specified in the compute command is ignored. The kinetic energy of all the rigid bodies defined by the fix rigid command in included in the calculation.
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the summed KE of all the rigid bodies). This value can be used by any command that uses a global scalar value from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "extensive". The scalar value will be in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the RIGID package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute erotate/rigid]{.doc}]compute_erotate_rigid.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

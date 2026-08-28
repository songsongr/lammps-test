:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#compute-pair-command .section}
[]{#index-0}

# compute pair command[](#compute-pair-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID pair pstyle [nstyle] [evalue]
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- pair = style name of this compute command

- pstyle = style name of a pair style that calculates additional values

- nsub = *n*-instance of a sub-style, if a pair style is used multiple times in a hybrid style

- *evalue* = *epair* or *evdwl* or *ecoul* or blank (optional)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all pair gauss
    compute 1 all pair lj/cut/coul/cut ecoul
    compute 1 all pair tersoff 2 epair
    compute 1 all pair reaxff
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that extracts additional values calculated by a pair style, and makes them accessible for output or further processing by other commands.

::: {.admonition .note}
Note

The group specified for this command is **ignored**.
:::

The specified *pstyle* must be a pair style used in your simulation either by itself or as a sub-style in a [[pair_style hybrid or hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} command. If the sub-style is used more than once, an additional number *nsub* has to be specified in order to choose which instance of the sub-style will be used by the compute. Not specifying the number in this case will cause the compute to fail.

The *evalue* setting is optional. All pair styles tally a potential energy *epair* which may be broken into two parts: *evdwl* and *ecoul* such that *epair* = *evdwl* + *ecoul*. If the pair style calculates Coulombic interactions, their energy will be tallied in *ecoul*. Everything else (whether it is a Lennard-Jones style van der Waals interaction or not) is tallied in *evdwl*. If *evalue* is blank or specified as *epair*, then *epair* is stored as a global scalar by this compute. This is useful when using [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal} if you want to know the portion of the total energy contributed by one sub-style. If *evalue* is specified as *evdwl* or *ecoul*, then just that portion of the energy is stored as a global scalar.

::: {.admonition .note}
Note

The energy returned by the *evdwl* keyword does not include tail corrections, even if they are enabled via the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} command.
:::

Some pair styles tally additional quantities, e.g. a breakdown of potential energy into 14 components is tallied by the [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} command. These values (1 or more) are stored as a global vector by this compute. See the page for [[individual pair styles]{.doc}]pair_style.md){.reference .internal} for info on these values.
:::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar which is *epair* or *evdwl* or *ecoul*. If the pair style supports it, it also calculates a global vector of length [\\(\\ge\\)]{.math .notranslate .nohighlight} 1, as determined by the pair style. These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The scalar and vector values calculated by this compute are "extensive".

The scalar value will be in energy [[units]{.doc}]units.md){.reference .internal}. The vector values will typically also be in energy [[units]{.doc}]units.md){.reference .internal}, but see the page for the pair style for details.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute pe]{.doc}]compute_pe.md){.reference .internal}, [[compute bond]{.doc}]compute_bond.md){.reference .internal}, [[fix pair]{.doc}]fix_pair.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The keyword defaults are *evalue* = *epair*, nsub = 0.
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

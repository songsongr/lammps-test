::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#fix-pair-command .section}
[]{#index-0}

# fix pair command[](#fix-pair-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID pair N pstyle name flag ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- pair = style name of this fix command

- N = invoke this fix once every N timesteps

- pstyle = name of pair style to extract info from (e.g. eam)

- one or more name/flag pairs can be listed

- name = name of quantity the pair style allows extraction of

- flag = 1 if pair style needs to be triggered to produce data for name, 0 if not
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix request all pair 100 eam rho 0
    fix request all pair 100 amoeba uind 0 uinp 0
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 15Sep2022.]{.versionmodified .added}
:::

Extract per-atom quantities from a pair style and store them in this fix so they can be accessed by other LAMMPS commands, e.g. by a [[dump]{.doc}]dump.md){.reference .internal} command or by another [[fix]{.doc}]fix.md){.reference .internal}, [[compute]{.doc}]compute.md){.reference .internal}, or [[variable]{.doc}]variable.md){.reference .internal} command.

These are example use cases:

- extract per-atom density from [[pair_style eam]{.doc}]pair_eam.md){.reference .internal} to a dump file

- extract induced dipoles from [[pair_style amoeba]{.doc}]pair_amoeba.md){.reference .internal} to a dump file

- extract accuracy metrics from a machine-learned potential to trigger output when a condition is met (see the [[dump_modify skip]{.doc}]dump_modify.md){.reference .internal} command)

The *N* argument determines how often the fix is invoked.

The *pstyle* argument is the name of the pair style. It can be a sub-style used in a [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal} command. If there are multiple sub-styles using the same pair style, then *pstyle* should be specified as "style:N", where *N* is the number of the instance of the pair style you wish monitor (e.g., the first or second). For example, *pstyle* could be specified as "pace/extrapolation" or "amoeba" or "eam:1" or "eam:2".

One or more *name/flag* pairs of arguments follow. Each *name* is a per-atom quantity which the pair style must recognize as an extraction request. See the doc pages for individual [[pair_styles]{.doc}]pair_style.md){.reference .internal} to see what fix pair requests (if any) they support.

The *flag* setting determines whether this fix will also trigger the pair style to compute the named quantity so it can be extracted. If the quantity is always computed by the pair style, no trigger is needed; specify *flag* = 0. If the quantity is not always computed (e.g. because it is expensive to calculate), then specify *flag* = 1. This will trigger the quantity to be calculated only on timesteps it is needed. Again, see the doc pages for individual [[pair_styles]{.doc}]pair_style.md){.reference .internal} to determine which fix pair requests (if any) need to be triggered with a *flag* = 1 setting.

The per-atom data extracted from the pair style is stored by this fix as either a per-atom vector or array. If there is only one *name* argument specified and the pair style computes a single value for each atom, then this fix stores it as a per-atom vector. Otherwise a per-atom array is created, with its data in the order of the *name* arguments.

For example, [[pair_style amoeba]{.doc}]pair_amoeba.md){.reference .internal} allows extraction of two named quantities: "uind" and "uinp", both of which are 3-vectors for each atom, i.e. dipole moments. In the example below a 6-column per-atom array will be created. Columns 1-3 will store the "uind" values; columns 4-6 will store the "uinp" values.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style amoeba
    fix ex all pair 10 amoeba uind 0 uinp 0
:::
::::
::::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

As explained above, this fix produces a per-atom vector or array which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. If an array is produced, the number of columns is the sum of the number of per-atom quantities produced by each *name* argument requested from the pair style.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute pair]{.doc}]compute_pair.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

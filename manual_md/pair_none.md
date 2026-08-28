::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#pair-style-none-command .section}
[]{#index-0}

# pair_style none command[](#pair-style-none-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style none
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style none
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Using a pair style of *none* means that any previous pair style setting will be deleted and pairwise forces and energies are not computed.

As a consequence there will be a pairwise force cutoff of 0.0, which has implications for the default setting of the neighbor list and the communication cutoff. Those are the sum of the largest pairwise cutoff and the neighbor skin distance (see the documentation of the [[neighbor]{.doc}]neighbor.md){.reference .internal} command and the [[comm_modify]{.doc}]comm_modify.md){.reference .internal} command). When you have bonds, angles, dihedrals, or impropers defined at the same time, you must set the communication cutoff so that communication cutoff distance is large enough to acquire and communicate sufficient ghost atoms from neighboring subdomains as needed for computing bonds, angles, etc.

A pair style of *none* will also not request a pairwise neighbor list. However if the [[neighbor]{.doc}]neighbor.md){.reference .internal} style is *bin*, data structures for binning are still allocated. If the neighbor list cutoff is small, then these data structures can consume a large amount of memory. So you should either set the neighbor style to *nsq* or set the skin distance to a larger value.

See the [[pair_style zero]{.doc}]pair_zero.md){.reference .internal} for a way to set a pairwise cutoff and thus trigger the building of a neighbor lists and setting a corresponding communication cutoff, but compute no pairwise interactions.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

You must not use a [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command with this pair style. Since there is no interaction computed, you cannot set any coefficients for it.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style zero]{.doc}]pair_zero.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

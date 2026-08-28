::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#bond-style-zero-command .section}
[]{#index-0}

# bond_style zero command[](#bond-style-zero-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style zero keyword
:::
::::

- zero or more keywords may be appended

- keyword = *nocoeff*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style zero
    bond_style zero nocoeff
    bond_coeff *
    bond_coeff * 2.14
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Using an bond style of zero means bond forces and energies are not computed, but the geometry of bond pairs is still accessible to other commands.

As an example, the [[compute bond/local]{.doc}]compute_bond_local.md){.reference .internal} command can be used to compute distances for the list of pairs of bond atoms listed in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command. If no bond style is defined, this command cannot be used.

The optional *nocoeff* flag allows to read data files with a BondCoeff section for any bond style. Similarly, any bond_coeff commands will only be checked for the bond type number and the rest ignored.

Note that the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command must be used for all bond types. If specified, there can be only one value, which is going to be used to assign an equilibrium distance, e.g. for use with [[fix shake]{.doc}]fix_shake.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_style none]{.doc}]bond_none.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

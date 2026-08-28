::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#dihedral-style-zero-command .section}
[]{#index-0}

# dihedral_style zero command[](#dihedral-style-zero-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style zero keyword
:::
::::

- zero or more keywords may be appended

- keyword = *nocoeff*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style zero
    dihedral_style zero nocoeff
    dihedral_coeff *
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Using a dihedral style of zero means dihedral forces and energies are not computed, but the geometry of dihedral quadruplets is still accessible to other commands.

As an example, the [[compute dihedral/local]{.doc}]compute_dihedral_local.md){.reference .internal} command can be used to compute the theta values for the list of quadruplets of dihedral atoms listed in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command. If no dihedral style is defined, this command cannot be used.

The optional *nocoeff* flag allows to read data files with a DihedralCoeff section for any dihedral style. Similarly, any dihedral_coeff commands will only be checked for the dihedral type number and the rest ignored.

Note that the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command must be used for all dihedral types, though no additional values are specified.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none

[[dihedral_style none]{.doc}]dihedral_none.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

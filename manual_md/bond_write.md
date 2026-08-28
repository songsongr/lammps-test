::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#bond-write-command .section}
[]{#index-0}

# bond_write command[](#bond-write-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_write btype N inner outer file keyword itype jtype
:::
::::

- btype = bond type

- N = \# of values

- inner,outer = inner and outer bond length (distance units)

- file = name of file to write values to

- keyword = section name in file for this set of tabulated values

- itype,jtype = two atom types (optional)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_write 1 500 0.5 3.5 table.txt Harmonic_1
    bond_write 3 1000 0.1 6.0 table.txt Morse
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Write energy and force values to a file as a function of distance for the currently defined [[bond style]{.doc}]bond_style.md){.reference .internal} for a selected bond type. This is useful for plotting the potential function or otherwise debugging its values. The resulting file can also be used as input for use with [[bond style table]{.doc}]bond_table.md){.reference .internal}.

If the file already exists, the table of values is appended to the end of the file to allow multiple tables of energy and force to be included in one file. The individual sections may be identified by the *keyword*.

The energy and force values are computed at distances from *inner* to *outer* for two interacting atoms forming a bond of type *btype*, using the appropriate [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} coefficients. N evenly spaced distances are used.

For example, for N = 7, inner = 1.0, and outer = 4.0, values are computed at r = 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0.

The file is written in the format used as input for the [[bond_style table]{.doc}]bond_table.md){.reference .internal} option with *keyword* as the section name. Each line written to the file lists an index number (1-N), a distance (in distance units), an energy (in energy units), and a force (in force units). In case a new file is created, the first line will be a comment with a "DATE:" and "UNITS:" tag with the current date and [[units]{.doc}]units.md){.reference .internal} settings. For subsequent invocations of the *bond_write* command for the same file, data will be appended and the current units settings will be compared to the data from the header, if present. The *bond_write* command will refuse to add a table to an existing file if the units are not the same.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

All force field coefficients for bond and other kinds of interactions must be set before this command can be invoked.

Due to how the bond force is computed, an inner value \> 0.0 must be specified even if the potential has a finite value at r = 0.0.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_style table]{.doc}]bond_table.md){.reference .internal}, [[angle_write]{.doc}]angle_write.md){.reference .internal}, [[bond_style]{.doc}]bond_style.md){.reference .internal}, [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

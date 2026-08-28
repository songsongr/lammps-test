::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#bond-coeff-command .section}
[]{#index-0}

# bond_coeff command[](#bond-coeff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_coeff N args
:::
::::

- N = numeric bond type (see asterisk form below), or type label

- args = coefficients for one or more bond types
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_coeff 5 80.0 1.2
    bond_coeff * 30.0 1.5 1.0 1.0
    bond_coeff 1*4 30.0 1.5 1.0 1.0
    bond_coeff 1 harmonic 200.0 1.0 # (for bond_style hybrid)

    labelmap bond 5 carbonyl
    bond_coeff carbonyl 80.0 1.2
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Specify the bond force field coefficients for one or more bond types. The number and meaning of the coefficients depends on the bond style. Bond coefficients can also be set in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command or in a restart file.

[\\(N\\)]{.math .notranslate .nohighlight} can be specified in one of several ways. An explicit numeric value can be used, as in the first example above. Or [\\(N\\)]{.math .notranslate .nohighlight} can be a type label, which is an alphanumeric string defined by the [[labelmap]{.doc}]labelmap.md){.reference .internal} command or in a section of a data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command.

For numeric values only, a wild-card asterisk can be used to set the coefficients for multiple bond types. This takes the form "\*" or "\*n" or "n\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of bond types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from n to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive).

Note that using a bond_coeff command can override a previous setting for the same bond type. For example, these commands set the coeffs for all bond types, then overwrite the coeffs for just bond type 2:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_coeff * 100.0 1.2
    bond_coeff 2 200.0 1.2
:::
::::

A line in a data file that specifies bond coefficients uses the exact same format as the arguments of the bond_coeff command in an input script, except that wild-card asterisks should not be used since coefficients for all [\\(N\\)]{.math .notranslate .nohighlight} types must be listed in the file. For example, under the "Bond Coeffs" section of a data file, the line that corresponds to the first example above would be listed as

:::: {.highlight-none .notranslate}
::: highlight
    5 80.0 1.2
:::
::::

------------------------------------------------------------------------

The list of all bond styles defined in LAMMPS is given on the [[bond_style]{.doc}]bond_style.md){.reference .internal} doc page. They are also listed in more compact form on the [[Commands bond]{.doc}]Commands_bond.md){.reference .internal} doc page.

On either of those pages, click on the style to display the formula it computes and its coefficients as specified by the associated bond_coeff command.
:::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command must come after the simulation box is defined by a [[read_data]{.doc}]read_data.md){.reference .internal}, [[read_restart]{.doc}]read_restart.md){.reference .internal}, or [[create_box]{.doc}]create_box.md){.reference .internal} command.

A bond style must be defined before any bond coefficients are set, either in the input script or in a data file.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_style]{.doc}]bond_style.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

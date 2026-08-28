:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#dihedral-coeff-command .section}
[]{#index-0}

# dihedral_coeff command[](#dihedral-coeff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_coeff N args
:::
::::

- N = numeric dihedral type (see asterisk form below) or alphanumeric type label

- args = coefficients for one or more dihedral types
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_coeff 1 80.0 1 3
    dihedral_coeff * 80.0 1 3 0.5
    dihedral_coeff 2* 80.0 1 3 0.5

    labelmap dihedral 1 backbone
    dihedral_coeff backbone 80.0 1 3
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Specify the dihedral force field coefficients for one or more dihedral types. The number and meaning of the coefficients depends on the dihedral style. Dihedral coefficients can also be set in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command or in a restart file.

[\\(N\\)]{.math .notranslate .nohighlight} can be specified in one of two ways. An explicit numeric value can be used, as in the first example above. Or [\\(N\\)]{.math .notranslate .nohighlight} can be an alphanumeric type label, which is a string defined by the [[labelmap]{.doc}]labelmap.md){.reference .internal} command or in a corresponding section of a data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command.

For numeric values only, a wild-card asterisk can be used to set the coefficients for multiple dihedral types. This takes the form "\*" or "\*n" or "n\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of dihedral types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from n to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive).

Note that using a dihedral_coeff command can override a previous setting for the same dihedral type. For example, these commands set the coeffs for all dihedral types, then overwrite the coeffs for just dihedral type 2:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_coeff * 80.0 1 3
    dihedral_coeff 2 200.0 1 3
:::
::::

A line in a data file that specifies dihedral coefficients uses the exact same format as the arguments of the dihedral_coeff command in an input script, except that wild-card asterisks should not be used since coefficients for all [\\(N\\)]{.math .notranslate .nohighlight} types must be listed in the file. For example, under the "Dihedral Coeffs" section of a data file, the line that corresponds to the first example above would be listed as

:::: {.highlight-none .notranslate}
::: highlight
    1 80.0 1 3
:::
::::

The [[dihedral_style class2]{.doc}]dihedral_class2.md){.reference .internal} is an exception to this rule, in that an additional argument is used in the input script to allow specification of the cross-term coefficients. See its doc page for details.

::: {.admonition .note}
Note

When comparing the formulas and coefficients for various LAMMPS dihedral styles with dihedral equations defined by other force fields, note that some force field implementations divide/multiply the energy prefactor *K* by the multiple number of torsions that contain the *J*--*K* bond in an *I*-*J*-*K*-*L* torsion. LAMMPS does not do this (i.e., the listed dihedral equation applies to each individual dihedral). Thus, you need to define *K* appropriately to account for this difference, if necessary.
:::

------------------------------------------------------------------------

The list of all dihedral styles defined in LAMMPS is given on the [[dihedral_style]{.doc}]dihedral_style.md){.reference .internal} doc page. They are also listed in more compact form on the [[Commands dihedral]{.std .std-ref}]Commands_bond.md#dihedral){.reference .internal} doc page.

On either of those pages, click on the style to display the formula it computes and its coefficients as specified by the associated dihedral_coeff command.
::::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command must come after the simulation box is defined by a [[read_data]{.doc}]read_data.md){.reference .internal}, [[read_restart]{.doc}]read_restart.md){.reference .internal}, or [[create_box]{.doc}]create_box.md){.reference .internal} command.

A dihedral style must be defined before any dihedral coefficients are set, either in the input script or in a data file.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dihedral_style]{.doc}]dihedral_style.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

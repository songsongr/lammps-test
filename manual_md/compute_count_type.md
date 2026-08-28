::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#compute-count-type-command .section}
[]{#index-0}

# compute count/type command[](#compute-count-type-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID count/type mode
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- count/type = style name of this compute command

- mode = *atom* or *bond* or *angle* or *dihedral* or *improper*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all count/type atom
    compute 1 flowmols count/type bond
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 15Jun2023.]{.versionmodified .added}
:::

Define a computation that counts the current number of atoms for each atom type. Or the number of bonds (angles, dihedrals, impropers) for each bond (angle, dihedral, improper) type.

The former can be useful if atoms are added to or deleted from the system in random ways, e.g. via the [[fix deposit]{.doc}]fix_deposit.md){.reference .internal}, [[fix pour]{.doc}]fix_pour.md){.reference .internal}, or [[fix evaporate]{.doc}]fix_evaporate.md){.reference .internal} commands. The latter can be useful in reactive simulations where molecular bonds are broken or created, as well as angles, dihedrals, impropers.

Note that for this command, bonds (angles, etc) are the topological kind enumerated in a data file, initially read by the [[read_data]{.doc}]read_data.md){.reference .internal} command or defined by the [[molecule]{.doc}]molecule.md){.reference .internal} command. They do not refer to implicit bonds defined on-the-fly by bond-order or reactive pair styles based on the current conformation of small clusters of atoms.

These commands can turn off topological bonds (angles, etc) by setting their bond (angle, etc) types to negative values. This command includes the turned-off bonds (angles, etc) in the count for each type:

- [[fix shake]{.doc}]fix_shake.md){.reference .internal}

- [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}

These commands can create and/or break topological bonds (angles, etc). In the case of breaking, they remove the bond (angle, etc) from the system, so that they no longer exist ([[bond_style quartic]{.doc}]bond_quartic.md){.reference .internal} and [[BPM bond styles]{.doc}]Howto_bpm.md){.reference .internal} are exceptions, see the discussion below). Thus they are not included in the counts for each type:

- [[delete_bonds remove]{.doc}]delete_bonds.md){.reference .internal}

- [[bond_style quartic]{.doc}]bond_quartic.md){.reference .internal}

- [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}

- [[fix bond/create]{.doc}]fix_bond_create.md){.reference .internal}

- [[fix bond/break]{.doc}]fix_bond_break.md){.reference .internal}

- [[BPM package]{.doc}]Howto_bpm.md){.reference .internal} bond styles

------------------------------------------------------------------------

If the *mode* setting is *atom* then the count of atoms for each atom type is tallied. Only atoms in the specified group are counted.

The atom count for each type can be normalized by the total number of atoms like so:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute typevec all count/type atom # number of atoms of each type
    variable normtypes vector c_typevec/atoms # divide by total number of atoms
    variable ntypes equal extract_setting(ntypes) # number of atom types
    thermo_style custom step v_normtypes[*${ntypes}] # vector variable needs upper limit
:::
::::

Similarly, bond counts can be normalized by the total number of bonds. The same goes for angles, dihedrals, and impropers (see below).

If the *mode* setting is *bond* then the count of bonds for each bond type is tallied. Only bonds with both atoms in the specified group are counted.

For *mode* = *bond*, broken bonds with a bond type of zero are also counted. The [[bond_style quartic]{.doc}]bond_quartic.md){.reference .internal} and [[BPM bond styles]{.doc}]Howto_bpm.md){.reference .internal} break bonds by doing this. See the [[Howto broken bonds]{.doc}]Howto_broken_bonds.md){.reference .internal} doc page for more details. Note that the group setting is ignored for broken bonds; all broken bonds in the system are counted.

If the *mode* setting is *angle* then the count of angles for each angle type is tallied. Only angles with all 3 atoms in the specified group are counted.

If the *mode* setting is *dihedral* then the count of dihedrals for each dihedral type is tallied. Only dihedrals with all 4 atoms in the specified group are counted.

If the *mode* setting is *improper* then the count of impropers for each improper type is tallied. Only impropers with all 4 atoms in the specified group are counted.
::::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector of counts. If the mode is *atom* or *bond* or *angle* or *dihedral* or *improper*, then the vector length is the number of atom types or bond types or angle types or dihedral types or improper types, respectively.

If the mode is *bond* this compute also calculates a global scalar which is the number of broken bonds with type = 0, as explained above.

These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar and vector values calculated by this compute are both "intensive".
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

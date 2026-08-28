::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#broken-bonds .section}
# [10.1.10. ]{.section-number}Broken Bonds[](#broken-bonds "Link to this heading"){.headerlink}

Typically, molecular bond interactions persist for the duration of a simulation in LAMMPS. However, some commands break bonds dynamically, including the following:

- [[bond_style quartic]{.doc}]bond_quartic.md){.reference .internal}

- [[fix bond/break]{.doc}]fix_bond_break.md){.reference .internal}

- [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}

- [[BPM package]{.doc}]Howto_bpm.md){.reference .internal} bond styles

A bond can break if it is stretched beyond a user-defined threshold or more generally if other criteria are met.

For the quartic bond style, when a bond is broken its bond type is set to 0 to effectively break it and pairwise forces between the two atoms in the broken bond are "turned on". Angles, dihedrals, etc cannot be defined for a system when [[bond_style quartic]{.doc}]bond_quartic.md){.reference .internal} is used.

Similarly, bond styles in the BPM package are also incompatible with angles, dihedrals, etc. and when a bond breaks its type is set to zero. However, in the BPM package one can either turn off all pair interactions between bonded particles or leave them on, overlaying pair forces on top of bond forces. To remove pair forces, the special bond list is dynamically updated. More details can be found on the [[Howto BPM]{.doc}]Howto_bpm.md){.reference .internal} page.

The [[fix bond/break]{.doc}]fix_bond_break.md){.reference .internal} and [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal} commands allow breaking of bonds within a molecular topology with may also define angles, dihedrals, etc. These commands update internal topology data structures to remove broken bonds, as well as the appropriate angle, dihedral, etc interactions which include the bond. They also trigger a rebuild of the neighbor list when this occurs, to turn on the appropriate pairwise forces.

Note that when bonds are dumped to a file via the [[dump local]{.doc}]dump.md){.reference .internal} command, bonds with type 0 are not included.

The [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal} command can be used to query the status of broken bonds with type = 0 or permanently delete them, e.g.:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    delete_bonds all stats
    delete_bonds all bond 0 remove
:::
::::

The compute [[count/type]{.doc}]compute_count_type.md){.reference .internal} command tallies the current number of bonds (or angles, etc) for each bond (angle, etc) type. It also tallies broken bonds with type = 0.

The compute [[nbond/atom]{.doc}]compute_nbond_atom.md){.reference .internal} command tallies the current number of bonds each atom is part of, excluding broken bonds with type = 0.
:::::
::::::
:::::::

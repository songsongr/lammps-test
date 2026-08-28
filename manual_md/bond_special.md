:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#bond-style-special-command .section}
[]{#index-0}

# bond_style special command[](#bond-style-special-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style special
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style special
    bond_coeff 0.5 0.5
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *special* bond style can be used to create conceptual bonds which effectively impose weightings on the pairwise Lennard Jones and/or Coulombic interactions between selected pairs of particles in the system. The form of the pairwise interaction will be whatever is computed by the [[pair_style]{.doc}]pair_style.md){.reference .internal} command defined for the system; this command defines the weightings for its two terms.

This command can thus be useful to apply weightings that cannot be handled by the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command, such as on 1-5 or 1-6 interactions. Or it can be used to add pairwise forces between one or more pairs of atoms that otherwise would not be include in the [[pair_style]{.doc}]pair_style.md){.reference .internal} computation.

The potential for this bond style has the form

::: {.math .notranslate .nohighlight}
\\\[E = w\_{LJ} E\_{LJ} + w\_{Coul} E\_{Coul}\\\]
:::

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(w\_{LJ}\\)]{.math .notranslate .nohighlight} weight (0.0 to 1.0) on pairwise Lennard-Jones interactions

- [\\(w\_{Coul}\\)]{.math .notranslate .nohighlight} weight (0.0 to 1.0) on pairwise Coulombic interactions

------------------------------------------------------------------------

Normally this bond style should be used in conjunction with one (or more) other bond styles which compute forces between atoms directly bonded to each other in a molecule. This means the [[bond_style hybrid]{.doc}]bond_hybrid.md){.reference .internal} command should be used with bond_style special as one of its sub-styles.

Note that the same as for any other bond style, pairs of bonded atoms must be enumerated in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command. Thus if this command is used to weight all 1-5 interactions in the system, all the 1-5 pairs of atoms must be listed in the "Bonds" section of the data file.

This bond style imposes strict requirements on settings made with the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command. These requirements ensure that the new bonds created by this style do not create spurious 1-2, 1-3, or 1-4 interactions within the molecular topology.

Specifically 1-2 interactions must have weights of zero, 1-3 interactions must either have weights of unity or [[special_bonds angle yes]{.doc}]special_bonds.md){.reference .internal} must be used, and 1-4 interactions must have weights of unity or [[special_bonds dihedral yes]{.doc}]special_bonds.md){.reference .internal} must be used.

If this command is used to create bonded interactions between particles that are further apart than usual (e.g. 1-5 or 1-6 interactions), this style may require an increase in the communication cutoff via the [[comm_modify cutoff]{.doc}]comm_modify.md){.reference .internal} command. If LAMMPS cannot find a partner atom in a bond, an error will be issued.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the MISC package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

This bond style requires the use of a [[pair_style]{.doc}]pair_style.md){.reference .internal} which computes a pairwise additive interaction and provides the ability to compute interactions for individual pairs of atoms. Manybody potentials are not compatible in general, but also some other pair styles are missing the required functionality and thus will cause an error.

This command is not compatible with long-range Coulombic interactions. If a kspace_style \<kspace_style\> is declared, an error will be issued.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[special_bonds]{.doc}]special_bonds.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

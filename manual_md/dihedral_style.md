::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#dihedral-style-command .section}
[]{#index-0}

# dihedral_style command[](#dihedral-style-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style style
:::
::::

- style = *none* or *zero* or *hybrid* or *charmm* or *charmmfsw* or *class2* or *class2xe* or *cosine/shift/exp* or *cosine/squared/restricted* or *fourier* or *harmonic* or *helix* or *lepton* or *multi/harmonic* or *nharmonic* or *opls* or *spherical* or *table* or *table/cut*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style harmonic
    dihedral_style multi/harmonic
    dihedral_style hybrid harmonic charmm
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set the formula(s) LAMMPS uses to compute dihedral interactions between quadruplets of atoms, which remain in force for the duration of the simulation. The list of dihedral quadruplets is read in by a [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} command from a data or restart file.

Hybrid models where dihedrals are computed using different dihedral potentials can be setup using the *hybrid* dihedral style.

The coefficients associated with a dihedral style can be specified in a data or restart file or via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command.

All dihedral potentials store their coefficient data in binary restart files which means dihedral_style and [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} commands do not need to be re-specified in an input script that restarts a simulation. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for details on how to do this. The one exception is that dihedral_style *hybrid* only stores the list of sub-styles in the restart file; dihedral coefficients need to be re-specified.

::: {.admonition .note}
Note

When both a dihedral and pair style is defined, the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command often needs to be used to turn off (or weight) the pairwise interaction that would otherwise exist between four bonded atoms.
:::

In the formulas listed for each dihedral style, *phi* is the torsional angle defined by the quadruplet of atoms. This angle has a sign convention as shown in this diagram:

![](_images/dihedral_sign.jpg){.align-center}

where the [\\(I,J,K,L\\)]{.math .notranslate .nohighlight} ordering of the four atoms that define the dihedral is from left to right.

This sign convention effects several of the dihedral styles listed below (e.g., charmm, helix) in the sense that the energy formula depends on the sign of phi, which may be reflected in the value of the coefficients you specify.

::: {.admonition .note}
Note

When comparing the formulas and coefficients for various LAMMPS dihedral styles with dihedral equations defined by other force fields, note that some force field implementations divide/multiply the energy prefactor *K* by the multiple number of torsions that contain the *J*--*K* bond in an *I*--*J*--*K*--*L* torsion. LAMMPS does not do this (i.e., the listed dihedral equation applies to each individual dihedral). Thus, you need to define *K* appropriately via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command to account for this difference if necessary.
:::

------------------------------------------------------------------------

Here is an alphabetic list of dihedral styles defined in LAMMPS. Click on the style to display the formula it computes and coefficients specified by the associated [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command.

Click on the style to display the formula it computes, any additional arguments specified in the dihedral_style command, and coefficients specified by the associated [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command.

There are also additional accelerated pair styles included in the LAMMPS distribution for faster performance on CPUs, GPUs, and KNLs. The individual style names on the [[Commands dihedral]{.std .std-ref}]Commands_bond.md#dihedral){.reference .internal} page are followed by one or more of (g,i,k,o,t) to indicate which accelerated styles exist.

- [[none]{.doc}]dihedral_none.md){.reference .internal} - turn off dihedral interactions

- [[zero]{.doc}]dihedral_zero.md){.reference .internal} - topology but no interactions

- [[hybrid]{.doc}]dihedral_hybrid.md){.reference .internal} - define multiple styles of dihedral interactions

- [[charmm]{.doc}]dihedral_charmm.md){.reference .internal} - CHARMM dihedral

- [[charmmfsw]{.doc}]dihedral_charmm.md){.reference .internal} - CHARMM dihedral with force switching

- [[class2]{.doc}]dihedral_class2.md){.reference .internal} - COMPASS (class 2) dihedral

- [[class2xe]{.doc}]dihedral_class2.md){.reference .internal} - ClassII-xe (class 2) dihedral

- [[cosine/shift/exp]{.doc}]dihedral_cosine_shift_exp.md){.reference .internal} - dihedral with exponential in spring constant

- [[cosine/squared/restricted]{.doc}]dihedral_cosine_squared_restricted.md){.reference .internal} - squared cosine dihedral with restricted term

- [[fourier]{.doc}]dihedral_fourier.md){.reference .internal} - dihedral with multiple cosine terms

- [[harmonic]{.doc}]dihedral_harmonic.md){.reference .internal} - harmonic dihedral

- [[helix]{.doc}]dihedral_helix.md){.reference .internal} - helix dihedral

- [[lepton]{.doc}]dihedral_lepton.md){.reference .internal} - dihedral potential from evaluating a string

- [[multi/harmonic]{.doc}]dihedral_multi_harmonic.md){.reference .internal} - dihedral with 5 harmonic terms

- [[nharmonic]{.doc}]dihedral_nharmonic.md){.reference .internal} - same as multi-harmonic with N terms

- [[opls]{.doc}]dihedral_opls.md){.reference .internal} - OPLS dihedral

- [[quadratic]{.doc}]dihedral_quadratic.md){.reference .internal} - dihedral with quadratic term in angle

- [[spherical]{.doc}]dihedral_spherical.md){.reference .internal} - dihedral which includes angle terms to avoid singularities

- [[table]{.doc}]dihedral_table.md){.reference .internal} - tabulated dihedral

- [[table/cut]{.doc}]dihedral_table.md){.reference .internal} - tabulated dihedral with analytic cutoff
:::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Dihedral styles can only be set for atom styles that allow dihedrals to be defined.

Most dihedral styles are part of the MOLECULE package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. The doc pages for individual dihedral potentials tell if it is part of a package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

dihedral_style none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

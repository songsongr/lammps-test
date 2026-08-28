:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#bond-style-command .section}
[]{#index-0}

# bond_style command[](#bond-style-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style style args
:::
::::

- style = *none* or *zero* or *hybrid* or *bpm/rotational* or *bpm/spring* or *bpm/spring/plastic* or *class2* or *fene* or *fene/expand* or *fene/nm* or *gaussian* or *gromos* or *harmonic* or *harmonic/restrain* *harmonic/shift* or *harmonic/shift/cut* or *lepton* or *morse* or *nonlinear* or *oxdna/fene* or *oxdena2/fene* or *oxrna2/fene* or *quartic* or *special* or *table*

- args = none for any style except *hybrid*

  - *hybrid* args = list of one or more styles
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style harmonic
    bond_style fene
    bond_style hybrid harmonic fene
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set the formula(s) LAMMPS uses to compute bond interactions between pairs of atoms. In LAMMPS, a bond differs from a pairwise interaction, which are set via the [[pair_style]{.doc}]pair_style.md){.reference .internal} command. Bonds are defined between specified pairs of atoms and remain in force for the duration of the simulation (unless new bonds are created or existing bonds break, which is possible in some fixes and bond potentials). The list of bonded atoms is read in by a [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} command from a data or restart file. By contrast, pair potentials are typically defined between all pairs of atoms within a cutoff distance and the set of active interactions changes over time.

Hybrid models where bonds are computed using different bond potentials can be setup using the *hybrid* bond style.

The coefficients associated with a bond style can be specified in a data or restart file or via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command.

All bond potentials store their coefficient data in binary restart files which means bond_style and [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} commands do not need to be re-specified in an input script that restarts a simulation. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for details on how to do this. The one exception is that bond_style *hybrid* only stores the list of sub-styles in the restart file; bond coefficients need to be re-specified.

::: {.admonition .note}
Note

When both a bond and pair style is defined, the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command often needs to be used to turn off (or weight) the pairwise interaction that would otherwise exist between two bonded atoms.
:::

In the formulas listed for each bond style, *r* is the distance between the two atoms in the bond.

------------------------------------------------------------------------

Here is an alphabetic list of bond styles defined in LAMMPS. Click on the style to display the formula it computes and coefficients specified by the associated [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command.

Click on the style to display the formula it computes, any additional arguments specified in the bond_style command, and coefficients specified by the associated [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command.

There are also additional accelerated pair styles included in the LAMMPS distribution for faster performance on CPUs, GPUs, and KNLs. The individual style names on the [[Commands bond]{.doc}]Commands_bond.md){.reference .internal} doc page are followed by one or more of (g,i,k,o,t) to indicate which accelerated styles exist.

- [[none]{.doc}]bond_none.md){.reference .internal} - turn off bonded interactions

- [[zero]{.doc}]bond_zero.md){.reference .internal} - topology but no interactions

- [[hybrid]{.doc}]bond_hybrid.md){.reference .internal} - define multiple styles of bond interactions

- [[bpm/rotational]{.doc}]bond_bpm_rotational.md){.reference .internal} - breakable bond with forces and torques based on deviation from reference state

- [[bpm/spring]{.doc}]bond_bpm_spring.md){.reference .internal} - breakable bond with forces based on deviation from reference length

- [[bpm/spring/plastic]{.doc}]bond_bpm_spring_plastic.md){.reference .internal} - a similar breakable bond with plastic yield

- [[class2]{.doc}]bond_class2.md){.reference .internal} - COMPASS (class 2) bond

- [[fene]{.doc}]bond_fene.md){.reference .internal} - FENE (finite-extensible non-linear elastic) bond

- [[fene/expand]{.doc}]bond_fene_expand.md){.reference .internal} - FENE bonds with variable size particles

- [[fene/nm]{.doc}]bond_fene.md){.reference .internal} - FENE bonds with a generalized Lennard-Jones potential

- [[gaussian]{.doc}]bond_gaussian.md){.reference .internal} - multicentered Gaussian-based bond potential

- [[gromos]{.doc}]bond_gromos.md){.reference .internal} - GROMOS force field bond

- [[harmonic]{.doc}]bond_harmonic.md){.reference .internal} - harmonic bond

- [[harmonic/restrain]{.doc}]bond_harmonic_restrain.md){.reference .internal} - harmonic bond to restrain to original bond distance

- [[harmonic/shift]{.doc}]bond_harmonic_shift.md){.reference .internal} - shifted harmonic bond

- [[harmonic/shift/cut]{.doc}]bond_harmonic_shift_cut.md){.reference .internal} - shifted harmonic bond with a cutoff

- [[lepton]{.doc}]bond_lepton.md){.reference .internal} - bond potential from evaluating a string

- [[mesocnt]{.doc}]bond_mesocnt.md){.reference .internal} - Harmonic bond wrapper with parameterization presets for nanotubes

- [[mm3]{.doc}]bond_mm3.md){.reference .internal} - MM3 anharmonic bond

- [[morse]{.doc}]bond_morse.md){.reference .internal} - Morse bond

- [[nonlinear]{.doc}]bond_nonlinear.md){.reference .internal} - nonlinear bond

- [[oxdna/fene]{.doc}]bond_oxdna.md){.reference .internal} - modified FENE bond suitable for DNA modeling

- [[oxdna2/fene]{.doc}]bond_oxdna.md){.reference .internal} - same as oxdna but used with different pair styles

- [[oxrna2/fene]{.doc}]bond_oxdna.md){.reference .internal} - modified FENE bond suitable for RNA modeling

- [[quartic]{.doc}]bond_quartic.md){.reference .internal} - breakable quartic bond

- [[rheo/shell]{.doc}]bond_rheo_shell.md){.reference .internal} - shell bond for oxidation modeling in RHEO

- [[special]{.doc}]bond_special.md){.reference .internal} - enable special bond exclusions for 1-5 pairs and beyond

- [[table]{.doc}]bond_table.md){.reference .internal} - tabulated by bond length
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Bond styles can only be set for atom styles that allow bonds to be defined.

Most bond styles are part of the MOLECULE package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. The doc pages for individual bond potentials tell if it is part of a package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}
:::

::::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style none
:::
::::
:::::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

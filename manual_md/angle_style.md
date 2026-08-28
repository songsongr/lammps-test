:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#angle-style-command .section}
[]{#index-0}

# angle_style command[](#angle-style-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style style
:::
::::

- style = *none* or *zero* or *hybrid* or *amoeba* or *charmm* or *class2* or *class2xe* or *class2/p6* or *cosine* or *cosine/buck6d* or *cosine/delta* or *cosine/periodic* or *cosine/shift* or *cosine/shift/exp* or *cosine/squared* or *cosine/squared/restricted* or *cross* or *dipole* or *fourier* or *fourier/simple* or *gaussian* or *harmonic* or *lepton* or *mm3* or *quartic* or *spica* or *table*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style harmonic
    angle_style charmm
    angle_style hybrid harmonic cosine
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set the formula(s) LAMMPS uses to compute angle interactions between triplets of atoms, which remain in force for the duration of the simulation. The list of angle triplets is read in by a [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} command from a data or restart file.

Hybrid models where angles are computed using different angle potentials can be setup using the *hybrid* angle style.

The coefficients associated with a angle style can be specified in a data or restart file or via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command.

All angle potentials store their coefficient data in binary restart files which means angle_style and [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} commands do not need to be re-specified in an input script that restarts a simulation. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for details on how to do this. The one exception is that angle_style *hybrid* only stores the list of sub-styles in the restart file; angle coefficients need to be re-specified.

::: {.admonition .note}
Note

When both an angle and pair style is defined, the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command often needs to be used to turn off (or weight) the pairwise interaction that would otherwise exist between 3 bonded atoms.
:::

In the formulas listed for each angle style, *theta* is the angle between the three atoms in the angle.

------------------------------------------------------------------------

Here is an alphabetic list of angle styles defined in LAMMPS. Click on the style to display the formula it computes and coefficients specified by the associated [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command.

Click on the style to display the formula it computes, any additional arguments specified in the angle_style command, and coefficients specified by the associated [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command.

There are also additional accelerated pair styles included in the LAMMPS distribution for faster performance on CPUs, GPUs, and KNLs. The individual style names on the [[Commands angle]{.std .std-ref}]Commands_bond.md#angle){.reference .internal} page are followed by one or more of (g,i,k,o,t) to indicate which accelerated styles exist.

- [[none]{.doc}]angle_none.md){.reference .internal} - turn off angle interactions

- [[zero]{.doc}]angle_zero.md){.reference .internal} - topology but no interactions

- [[hybrid]{.doc}]angle_hybrid.md){.reference .internal} - define multiple styles of angle interactions

- [[amoeba]{.doc}]angle_amoeba.md){.reference .internal} - AMOEBA angle

- [[charmm]{.doc}]angle_charmm.md){.reference .internal} - CHARMM angle

- [[class2]{.doc}]angle_class2.md){.reference .internal} - COMPASS (class 2) angle

- [[class2xe]{.doc}]angle_class2.md){.reference .internal} - ClassII-xe (class 2) angle

- [[class2/p6]{.doc}]angle_class2.md){.reference .internal} - COMPASS (class 2) angle expanded to 6th order

- [[cosine]{.doc}]angle_cosine.md){.reference .internal} - angle with cosine term

- [[cosine/buck6d]{.doc}]angle_cosine_buck6d.md){.reference .internal} - same as cosine with Buckingham term between 1-3 atoms

- [[cosine/delta]{.doc}]angle_cosine_delta.md){.reference .internal} - angle with difference of cosines

- [[cosine/periodic]{.doc}]angle_cosine_periodic.md){.reference .internal} - DREIDING angle

- [[cosine/shift]{.doc}]angle_cosine_shift.md){.reference .internal} - angle cosine with a shift

- [[cosine/shift/exp]{.doc}]angle_cosine_shift_exp.md){.reference .internal} - cosine with shift and exponential term in spring constant

- [[cosine/squared]{.doc}]angle_cosine_squared.md){.reference .internal} - angle with cosine squared term

- [[cosine/squared/restricted]{.doc}]angle_cosine_squared_restricted.md){.reference .internal} - angle with restricted cosine squared term

- [[cross]{.doc}]angle_cross.md){.reference .internal} - cross term coupling angle and bond lengths

- [[dipole]{.doc}]angle_dipole.md){.reference .internal} - angle that controls orientation of a point dipole

- [[fourier]{.doc}]angle_fourier.md){.reference .internal} - angle with multiple cosine terms

- [[fourier/simple]{.doc}]angle_fourier_simple.md){.reference .internal} - angle with a single cosine term

- [[gaussian]{.doc}]angle_gaussian.md){.reference .internal} - multi-centered Gaussian-based angle potential

- [[harmonic]{.doc}]angle_harmonic.md){.reference .internal} - harmonic angle

- [[lepton]{.doc}]angle_lepton.md){.reference .internal} - angle potential from evaluating a string

- [[mesocnt]{.doc}]angle_mesocnt.md){.reference .internal} - piecewise harmonic and linear angle for bending-buckling of nanotubes

- [[mm3]{.doc}]angle_mm3.md){.reference .internal} - anharmonic angle

- [[mwlc]{.doc}]angle_mwlc.md){.reference .internal} - meltable wormlike chain

- [[quartic]{.doc}]angle_quartic.md){.reference .internal} - angle with cubic and quartic terms

- [[spica]{.doc}]angle_spica.md){.reference .internal} - harmonic angle with repulsive SPICA pair style between 1-3 atoms

- [[table]{.doc}]angle_table.md){.reference .internal} - tabulated by angle
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Angle styles can only be set for atom_styles that allow angles to be defined.

Most angle styles are part of the MOLECULE package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. The doc pages for individual bond potentials tell if it is part of a package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}
:::

::::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style none
:::
::::
:::::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#improper-style-command .section}
[]{#index-0}

# improper_style command[](#improper-style-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style style
:::
::::

- style = *none* or *hybrid* or *class2* or *cvff* or *harmonic*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style harmonic
    improper_style cvff
    improper_style hybrid cvff harmonic
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set the formula(s) LAMMPS uses to compute improper interactions between quadruplets of atoms, which remain in force for the duration of the simulation. The list of improper quadruplets is read in by a [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} command from a data or restart file. Note that the ordering of the 4 atoms in an improper quadruplet determines the definition of the improper angle used in the formula for each style. See the doc pages of individual styles for details.

Hybrid models where impropers are computed using different improper potentials can be setup using the *hybrid* improper style.

The coefficients associated with an improper style can be specified in a data or restart file or via the [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command.

All improper potentials store their coefficient data in binary restart files which means improper_style and [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} commands do not need to be re-specified in an input script that restarts a simulation. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for details on how to do this. The one exception is that improper_style *hybrid* only stores the list of sub-styles in the restart file; improper coefficients need to be re-specified.

::: {.admonition .note}
Note

When both an improper and pair style is defined, the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command often needs to be used to turn off (or weight) the pairwise interaction that would otherwise exist between a group of 4 bonded atoms.
:::

------------------------------------------------------------------------

Here is an alphabetic list of improper styles defined in LAMMPS. Click on the style to display the formula it computes and coefficients specified by the associated [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command.

Click on the style to display the formula it computes, any additional arguments specified in the improper_style command, and coefficients specified by the associated [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command.

There are also additional accelerated pair styles included in the LAMMPS distribution for faster performance on CPUs, GPUs, and KNLs. The individual style names on the [[Commands improper]{.std .std-ref}]Commands_bond.md#improper){.reference .internal} page are followed by one or more of (g,i,k,o,t) to indicate which accelerated styles exist.

- [[none]{.doc}]improper_none.md){.reference .internal} - turn off improper interactions

- [[zero]{.doc}]improper_zero.md){.reference .internal} - topology but no interactions

- [[hybrid]{.doc}]improper_hybrid.md){.reference .internal} - define multiple styles of improper interactions

- [[amoeba]{.doc}]improper_amoeba.md){.reference .internal} - AMOEBA out-of-plane improper

- [[class2]{.doc}]improper_class2.md){.reference .internal} - COMPASS (class 2) improper

- [[cossq]{.doc}]improper_cossq.md){.reference .internal} - improper with a cosine squared term

- [[cvff]{.doc}]improper_cvff.md){.reference .internal} - CVFF improper

- [[distance]{.doc}]improper_distance.md){.reference .internal} - improper based on distance between atom planes

- [[distharm]{.doc}]improper_distharm.md){.reference .internal} - improper that is harmonic in the out-of-plane distance

- [[fourier]{.doc}]improper_fourier.md){.reference .internal} - improper with multiple cosine terms

- [[harmonic]{.doc}]improper_harmonic.md){.reference .internal} - harmonic improper

- [[inversion/harmonic]{.doc}]improper_inversion_harmonic.md){.reference .internal} - harmonic improper with Wilson-Decius out-of-plane definition

- [[ring]{.doc}]improper_ring.md){.reference .internal} - improper which prevents planar conformations

- [[umbrella]{.doc}]improper_umbrella.md){.reference .internal} - DREIDING improper

- [[sqdistharm]{.doc}]improper_sqdistharm.md){.reference .internal} - improper that is harmonic in the square of the out-of-plane distance
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Improper styles can only be set for atom_style choices that allow impropers to be defined.

Most improper styles are part of the MOLECULE package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. The doc pages for individual improper potentials tell if it is part of a package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[improper_coeff]{.doc}]improper_coeff.md){.reference .internal}
:::

::::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style none
:::
::::
:::::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

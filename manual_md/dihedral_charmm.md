:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#dihedral-style-charmm-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# dihedral_style charmm command[](#dihedral-style-charmm-command "Link to this heading"){.headerlink}

Accelerator Variants: *charmm/intel*, *charmm/kk*, *charmm/omp*
:::

::::::::::::::: {#dihedral-style-charmmfsw-command .section}
# dihedral_style charmmfsw command[](#dihedral-style-charmmfsw-command "Link to this heading"){.headerlink}

Accelerator Variants: *charmmfsw/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style style
:::
::::

- style = *charmm* or *charmmfsw*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style charmm
    dihedral_style charmmfsw
    dihedral_coeff  1 0.2 1 180 1.0
    dihedral_coeff  2 1.8 1   0 1.0
    dihedral_coeff  1 3.1 2 180 0.5
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *charmm* and *charmmfsw* dihedral styles use the potential

::: {.math .notranslate .nohighlight}
\\\[E = K \[ 1 + \\cos (n \\phi - d) \]\\\]
:::

See [[(MacKerell)]{.std .std-ref}](#dihedral-mackerell){.reference .internal} for a description of the CHARMM force field. This dihedral style can also be used for the AMBER force field (see comment on weighting factors below). See [[(Cornell)]{.std .std-ref}](#dihedral-cornell){.reference .internal} for a description of the AMBER force field.

::: {.admonition .note}
Note

The newer *charmmfsw* style was released in March 2017. We recommend it be used instead of the older *charmm* style when running a simulation with the CHARMM force field, either with long-range Coulombics or a Coulombic cutoff, via the [[pair_style lj/charmmfsw/coul/long]{.doc}]pair_charmm.md){.reference .internal} and [[pair_style lj/charmmfsw/coul/charmmfsh]{.doc}]pair_charmm.md){.reference .internal} commands respectively. Otherwise the older *charmm* style is fine to use. See the discussion below and more details on the [[pair_style charmm]{.doc}]pair_charmm.md){.reference .internal} doc page.
:::

The following coefficients must be defined for each dihedral type via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(n\\)]{.math .notranslate .nohighlight} (integer \>= 0)

- [\\(d\\)]{.math .notranslate .nohighlight} (integer value of degrees)

- weighting factor (1.0, 0.5, or 0.0)

The weighting factor is required to correct for double counting pairwise non-bonded Lennard-Jones interactions in cyclic systems or when using the CHARMM dihedral style with non-CHARMM force fields. With the CHARMM dihedral style, interactions between the first and fourth atoms in a dihedral are skipped during the normal non-bonded force computation and instead evaluated as part of the dihedral using special epsilon and sigma values specified with the [[pair_coeff]{.doc}]pair_charmm.md){.reference .internal} command of pair styles that contain "lj/charmm" (e.g. [[pair_style lj/charmm/coul/long]{.doc}]pair_charmm.md){.reference .internal}) In 6-membered rings, the same 1-4 interaction would be computed twice (once for the clockwise 1-4 pair in dihedral 1-2-3-4 and once in the counterclockwise dihedral 1-6-5-4) and thus the weighting factor has to be 0.5 in this case. In 4-membered or 5-membered rings, the 1-4 dihedral also is counted as a 1-2 or 1-3 interaction when going around the ring in the opposite direction and thus the weighting factor is 0.0, as the 1-2 and 1-3 exclusions take precedence.

Note that this dihedral weighting factor is unrelated to the scaling factor specified by the [[special bonds]{.doc}]special_bonds.md){.reference .internal} command which applies to all 1-4 interactions in the system. For CHARMM force fields, the special_bonds 1-4 interaction scaling factor should be set to 0.0. Since the corresponding 1-4 non-bonded interactions are computed with the dihedral. This means that if any of the weighting factors defined as dihedral coefficients (fourth coeff above) are non-zero, then you must use a pair style with "lj/charmm" and set the special_bonds 1-4 scaling factor to 0.0 (which is the default). Otherwise 1-4 non-bonded interactions in dihedrals will be computed twice.

For simulations using the CHARMM force field with a Coulombic cutoff, the difference between the *charmm* and *charmmfsw* styles is in the computation of the 1-4 non-bond interactions, though only if the distance between the two atoms is within the switching region of the pairwise potential defined by the corresponding CHARMM pair style, i.e. within the outer cutoff specified for the pair style. The *charmmfsw* style should only be used when using the corresponding [[pair_style lj/charmmfsw/coul/charmmfsw]{.doc}]pair_charmm.md){.reference .internal} or [[pair_style lj/charmmfsw/coul/long]{.doc}]pair_charmm.md){.reference .internal} commands. Use the *charmm* style with the older [[pair_style]{.doc}]pair_charmm.md){.reference .internal} commands that have just "charmm" in their style name. See the discussion on the [[CHARMM pair_style]{.doc}]pair_charmm.md){.reference .internal} page for details.

Note that for AMBER force fields, which use pair styles with "lj/cut", the special_bonds 1-4 scaling factor should be set to the AMBER defaults (1/2 and 5/6) and all the dihedral weighting factors (fourth coeff above) must be set to 0.0. In this case, you can use any pair style you wish, since the dihedral does not need any Lennard-Jones parameter information and will not compute any 1-4 non-bonded interactions. Likewise the *charmm* or *charmmfsw* styles are identical in this case since no 1-4 non-bonded interactions are computed.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

When using run_style [[respa]{.doc}]run_style.md){.reference .internal}, these dihedral styles must be assigned to the same r-RESPA level as *pair* or *outer*.

When used in combination with CHARMM pair styles, the 1-4 [[special_bonds]{.doc}]special_bonds.md){.reference .internal} scaling factors must be set to 0.0. Otherwise non-bonded contributions for these 1-4 pairs will be computed multiple times.

These dihedral styles can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}, [[pair_style lj/charmm variants]{.doc}]pair_charmm.md){.reference .internal}, [[angle_style charmm]{.doc}]angle_charmm.md){.reference .internal}, [[fix cmap]{.doc}]fix_cmap.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Cornell)** Cornell, Cieplak, Bayly, Gould, Merz, Ferguson, Spellmeyer, Fox, Caldwell, Kollman, JACS 117, 5179-5197 (1995).

**(MacKerell)** MacKerell, Bashford, Bellott, Dunbrack, Evanseck, Field, Fischer, Gao, Guo, Ha, et al, J Phys Chem B, 102, 3586 (1998).
:::
:::::::::::::::
:::::::::::::::::
::::::::::::::::::

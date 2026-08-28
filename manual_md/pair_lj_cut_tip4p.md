::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-lj-cut-tip4p-cut-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style lj/cut/tip4p/cut command[](#pair-style-lj-cut-tip4p-cut-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/cut/tip4p/cut/omp*
:::

:::::::::::::::::::: {#pair-style-lj-cut-tip4p-long-command .section}
# pair_style lj/cut/tip4p/long command[](#pair-style-lj-cut-tip4p-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/cut/tip4p/long/gpu*, *lj/cut/tip4p/long/omp*, *lj/cut/tip4p/long/opt*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *lj/cut/tip4p/cut* or *lj/cut/tip4p/long*

- args = list of arguments for a particular style

``` literal-block
lj/cut/tip4p/cut args = otype htype btype atype qdist cutoff (cutoff2)
  otype,htype = atom types (numeric or type label) for TIP4P O and H
  btype,atype = bond and angle types (numeric or type label) for TIP4P waters
  qdist = distance from O atom to massless charge (distance units)
  cutoff = global cutoff for LJ (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
lj/cut/tip4p/long args = otype htype btype atype qdist cutoff (cutoff2)
  otype,htype = atom types (numeric or type label) for TIP4P O and H
  btype,atype = bond and angle types (numeric or type label) for TIP4P waters
  qdist = distance from O atom to massless charge (distance units)
  cutoff = global cutoff for LJ (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/cut/tip4p/cut 1 2 7 8 0.15 12.0
    pair_style lj/cut/tip4p/cut 1 2 7 8 0.15 12.0 10.0
    pair_coeff * * 100.0 3.0
    pair_coeff 1 1 100.0 3.5 9.0

    pair_style lj/cut/tip4p/long 1 2 7 8 0.15 12.0
    pair_style lj/cut/tip4p/long 1 2 7 8 0.15 12.0 10.0
    pair_coeff * * 100.0 3.0
    pair_coeff 1 1 100.0 3.5 9.0

    pair_style lj/cut/tip4p/long OW HW HW-OW HW-OW-HW 0.15 12.0
    labelmap atom 1 OW 2 HW
    labelmap bond 1 HW-OW
    labelmap angle 1 HW-OW-HW
    pair_coeff * * 100.0 3.0
    pair_coeff OW OW 100.0 3.5 9.0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *lj/cut/tip4p* styles implement the TIP4P water model of [[(Jorgensen)]{.std .std-ref}](#jorgensen2){.reference .internal} and similar models, which introduce a massless site M located a short distance away from the oxygen atom along the bisector of the HOH angle. The atomic types of the oxygen and hydrogen atoms, the bond and angle types for OH and HOH interactions, and the distance to the massless charge site are specified as pair_style arguments and are used to identify the TIP4P-like molecules and determine the position of the M site from the positions of the hydrogen and oxygen atoms of the water molecules. The M site location is used for all Coulomb interactions instead of the oxygen atom location, also with all other atom types, while the location of the oxygen atom is used for the Lennard-Jones interactions. Style *lj/cut/tip4p/cut* uses a cutoff for Coulomb interactions; style *lj/cut/tip4p/long* is for use with a long-range Coulombic solver (Ewald or PPPM).

::: {.admonition .note}
Note

For each TIP4P water molecule in your system, the atom IDs for the O and 2 H atoms must be consecutive, with the O atom first. This is to enable LAMMPS to "find" the 2 H atoms associated with each O atom. For example, if the atom ID of an O atom in a TIP4P water molecule is 500, then its 2 H atoms must have IDs 501 and 502.
:::

::: {.admonition .note}
Note

If using type labels, the type labels must be defined before calling the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command.
:::

See the [[Howto tip4p]{.doc}]Howto_tip4p.md){.reference .internal} page for more information on how to use the TIP4P pair styles and lists of parameters to set. Note that the neighbor list cutoff for Coulomb interactions is effectively extended by a distance 2\*qdist when using the TIP4P pair style, to account for the offset distance of the fictitious charges on O atoms in water molecules. Thus it is typically best in an efficiency sense to use a LJ cutoff \>= Coulombic cutoff + 2\*qdist, to shrink the size of the neighbor list. This leads to slightly larger cost for the long-range calculation, so you can test the trade-off for your model.

The *lj/cut/tip4p* styles compute the standard 12/6 Lennard-Jones potential, given by

::: {.math .notranslate .nohighlight}
\\\[E = 4 \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - \\left(\\frac{\\sigma}{r}\\right)\^6 \\right\] \\qquad r \< r_c\\\]
:::

[\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff.

They add Coulombic pairwise interactions given by

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{C q_i q_j}{\\epsilon r} \\qquad r \< r_c\\\]
:::

where [\\(C\\)]{.math .notranslate .nohighlight} is an energy-conversion constant, [\\(q_i\\)]{.math .notranslate .nohighlight} and [\\(q_j\\)]{.math .notranslate .nohighlight} are the charges on the two atoms, and [\\(\\epsilon\\)]{.math .notranslate .nohighlight} is the dielectric constant which can be set by the [[dielectric]{.doc}]dielectric.md){.reference .internal} command. If one cutoff is specified in the pair_style command, it is used for both the LJ and Coulombic terms. If two cutoffs are specified, they are used as cutoffs for the LJ and Coulombic terms respectively.

Style *lj/cut/tip4p/long* compute the same Coulombic interactions as style *lj/cut/tip4p/cut* except that an additional damping factor is applied to the Coulombic term so it can be used in conjunction with the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command and its *ewald* or *pppm* option. The Coulombic cutoff specified for this style means that pairwise interactions within this distance are computed directly; interactions outside that distance are computed in reciprocal space.
:::::::

:::: {#coefficients .section}
## Coefficients[](#coefficients "Link to this heading"){.headerlink}

For all of the *lj/cut* pair styles, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- LJ cutoff (distance units)

Note that [\\(\\sigma\\)]{.math .notranslate .nohighlight} is defined in the LJ formula as the zero-crossing distance for the potential, not as the energy minimum at [\\(2\^{\\frac{1}{6}} \\sigma\\)]{.math .notranslate .nohighlight}.

The last coefficient is optional. If not specified, the global LJ cutoff specified in the pair_style command is used.

For *lj/cut/tip4p/cut* and *lj/cut/tip4p/long* only the LJ cutoff can be specified since a Coulombic cutoff cannot be specified for an individual I,J type pair. All type pairs use the same global Coulombic cutoff specified in the pair_style command.

::: {.admonition .warning}
Warning

Because of how these pair styles implement the coulomb interactions by implicitly defining a fourth site for the negative charge of the TIP4P and similar water models, special care must be taken when using these pair styles with other computations that also use charges. Unless they are specially set up to also handle the implicit definition of the 4th site, results are likely incorrect. Example: [[compute dipole/chunk]{.doc}]compute_dipole_chunk.md){.reference .internal}. For the same reason, when using one of these pair styles with [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal}, **all** coulomb interactions should be handled by a single sub-style with TIP4P support. All other instances and styles will "see" the M point charges at the position of the Oxygen atom and thus compute incorrect forces and energies. LAMMPS will print a warning when it detects one of these issues.
:::

------------------------------------------------------------------------

A version of these styles with a soft core, *lj/cut/tip4p/long/soft*, suitable for use in free energy calculations, is part of the FEP package and is documented with the [[pair_style \*/soft]{.doc}]pair_fep_soft.md){.reference .internal} styles.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon and sigma coefficients and cutoff distance for all of the lj/cut pair styles can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

All of the *lj/cut* pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the Lennard-Jones portion of the pair interaction.

The *lj/cut/coul/long* and *lj/cut/tip4p/long* pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option since they can tabulate the short-range portion of the long-range Coulombic interaction.

All of the *lj/cut* pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding a long-range tail correction to the energy and pressure for the Lennard-Jones portion of the pair interaction.

All of the *lj/cut* pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

The *lj/cut* and *lj/cut/coul/long* pair styles support the use of the *inner*, *middle*, and *outer* keywords of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command, meaning the pairwise forces can be partitioned by distance at different levels of the rRESPA hierarchy. The other styles only support the *pair* keyword of run_style respa. See the [[run_style]{.doc}]run_style.md){.reference .internal} command for details.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *lj/cut/tip4p/long* styles are part of the KSPACE package. The *lj/cut/tip4p/cut* style is part of the MOLECULE package. These styles are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Jorgensen)** Jorgensen, Chandrasekhar, Madura, Impey, Klein, J Chem Phys, 79, 926 (1983).
:::
::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

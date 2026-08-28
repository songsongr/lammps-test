::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#pair-style-drip-command .section}
[]{#index-0}

# pair_style drip command[](#pair-style-drip-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay drip [styles ...]
:::
::::

- styles = other styles to be overlayed with drip (optional)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay drip
    pair_coeff * * none
    pair_coeff * * drip  C.drip  C

    pair_style hybrid/overlay drip rebo
    pair_coeff * * drip  C.drip     C
    pair_coeff * * rebo  CH.airebo  C

    pair_style hybrid/overlay drip rebo
    pair_coeff * * drip  C.drip     C NULL
    pair_coeff * * rebo  CH.airebo  C H
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *drip* computes the interlayer interactions of layered materials using the dihedral-angle-corrected registry-dependent (DRIP) potential as described in [[(Wen)]{.std .std-ref}](#wen2018){.reference .internal}, which is based on the [[(Kolmogorov)]{.std .std-ref}](#kolmogorov2005){.reference .internal} potential and provides an improved prediction for forces. The total potential energy of a system is

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{1}{2} \\sum\_{i} \\sum\_{j\\notin\\text{layer}\\,i} \\phi\_{ij} \\\\ \\phi\_{ij} = &f\_\\text{c}(x_r) \\left\[ e\^{-\\lambda(r\_{ij} - z_0 )} \\left\[C+f(\\rho\_{ij})+ g(\\rho\_{ij}, \\{\\alpha\_{ij}\^{(m)}\\}) \\right\]- A\\left (\\frac{z_0}{r\_{ij}} \\right)\^6 \\right\]\\end{split}\\\]
:::

where the [\\(r\^{-6}\\)]{.math .notranslate .nohighlight} term models the attractive London dispersion, the exponential term is designed to capture the registry effect due to overlapping *pi* bonds, and *fc* is a cutoff function.

This potential (DRIP) only provides the interlayer interactions between graphene layers. So, to perform a realistic simulation, it should be used in combination with an intralayer potential such as [[REBO]{.doc}]pair_airebo.md){.reference .internal} and [[Tersoff]{.doc}]pair_tersoff.md){.reference .internal}. To keep the intralayer interactions unaffected, we should avoid applying DRIP to contribute energy to intralayer interactions. This can be achieved by assigning different molecular IDs to atoms in different layers, and DRIP is implemented such that only atoms with different molecular ID can interact with each other. For this purpose, [[atom style]{.doc}]atom_style.md){.reference .internal} "molecular" or "full" has to be used.

On the other way around, [[REBO]{.doc}]pair_airebo.md){.reference .internal} ([[Tersoff]{.doc}]pair_tersoff.md){.reference .internal} or any other potential used to provide the intralayer interactions) should not interfere with the interlayer interactions described by DRIP. This is typically automatically achieved using the commands provided in the *Examples* section above, since the cutoff distance for carbon-carbon interaction in the intralayer potentials (e.g. 2 Angstrom for [[REBO]{.doc}]pair_airebo.md){.reference .internal}) is much smaller than the equilibrium layer distance of graphene layers (about 3.4 Angstrom). If you want, you can enforce this by assigning different atom types to atoms in different layers, and apply an intralayer potential to one atom type. See [[pair_hybrid]{.doc}]pair_hybrid.md){.reference .internal} for details.

------------------------------------------------------------------------

The [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command for DRIP takes *4+N* arguments, where *N* is the number of LAMMPS atom types. The fist three arguments must be fixed to be *\* \* drip*, the fourth argument is the path to the DRIP parameter file, and the remaining N arguments specifying the mapping between element in the parameter file and atom types. For example, if your LAMMPS simulation has 3 atom types and you want all of them to be C, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * drip  C.drip  C C C
:::
::::

If a mapping value is specified as NULL, the mapping is not performed. This could be useful when DRIP is used to model part of the system where other element exists. Suppose you have a hydrocarbon system, with C of atom type 1 and H of atom type 2, you can use the following command to inform DRIP not to model H atoms:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay drip rebo
    pair_coeff * * drip  C.drip     C NULL
    pair_coeff * * rebo  CH.airebo  C H
:::
::::

::: {.admonition .note}
Note

The potential parameters developed in [[(Wen)]{.std .std-ref}](#wen2018){.reference .internal} are provided with LAMMPS (see the "potentials" directory). Besides those in [[Wen]{.std .std-ref}](#wen2018){.reference .internal}, an additional parameter "normal_cutoff", specific to the LAMMPS implementation, is used to find the three nearest neighbors of an atom to construct the normal.
:::
:::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support the pair_modify mix, shift, table, and tail options.

This pair style does not write their information to binary restart files, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the INTERLAYER package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair style requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

The *C.drip* parameter file provided with LAMMPS (see the "potentials" directory) is parameterized for metal [[units]{.doc}]units.md){.reference .internal}. You can use the DRIP potential with any LAMMPS units, but you would need to create your own custom parameter file with coefficients listed in the appropriate units, if your simulation does not use "metal" units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style lebedeva_z]{.doc}]pair_lebedeva_z.md){.reference .internal}, [[pair_style kolmogorov/crespi/z]{.doc}]pair_kolmogorov_crespi_z.md){.reference .internal}, [[pair_style kolmogorov/crespi/full]{.doc}]pair_kolmogorov_crespi_full.md){.reference .internal}, [[pair_style ilp/graphene/hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}.

------------------------------------------------------------------------

**(Wen)** M. Wen, S. Carr, S. Fang, E. Kaxiras, and E. B. Tadmor, Phys. Rev. B, 98, 235404 (2018)

**(Kolmogorov)** A. N. Kolmogorov, V. H. Crespi, Phys. Rev. B 71, 235415 (2005)
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#pair-style-kolmogorov-crespi-full-command .section}
[]{#index-0}

# pair_style kolmogorov/crespi/full command[](#pair-style-kolmogorov-crespi-full-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay kolmogorov/crespi/full cutoff tap_flag
:::
::::

- cutoff = global cutoff (distance units)

- tap_flag = 0/1 to turn off/on the taper function
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay kolmogorov/crespi/full 20.0 0
    pair_coeff * * none
    pair_coeff * * kolmogorov/crespi/full  CH.KC   C C

    pair_style hybrid/overlay rebo kolmogorov/crespi/full 16.0 1
    pair_coeff * * rebo                    CH.rebo      C H
    pair_coeff * * kolmogorov/crespi/full  CH_taper.KC  C H
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *kolmogorov/crespi/full* style computes the Kolmogorov-Crespi (KC) interaction potential as described in [[(Kolmogorov)]{.std .std-ref}](#kolmogorov1){.reference .internal}. No simplification is made,

::: {.math .notranslate .nohighlight}
\\\[\\begin{split} E = & \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} V\_{ij} \\\\ V\_{ij} = & e\^{-\\lambda (r\_{ij} -z_0)} \\left \[ C + f(\\rho\_{ij}) + f(\\rho\_{ji}) \\right \] - A \\left ( \\frac{r\_{ij}}{z_0}\\right )\^{-6} \\\\ \\rho\_{ij}\^2 = & r\_{ij}\^2 - (\\mathbf{r}\_{ij}\\cdot \\mathbf{n}\_{i})\^2 \\\\ \\rho\_{ji}\^2 = & r\_{ij}\^2 - (\\mathbf{r}\_{ij}\\cdot \\mathbf{n}\_{j})\^2 \\\\ f(\\rho) & = e\^{-(\\rho/\\delta)\^2} \\sum\_{n=0}\^2 C\_{2n} { (\\rho/\\delta) }\^{2n}\\end{split}\\\]
:::

It is important to have a sufficiently large cutoff to ensure smooth forces and to include all the pairs to build the neighbor list for calculating the normals. Energies are shifted so that they go continuously to zero at the cutoff assuming that the exponential part of [\\(V\_{ij}\\)]{.math .notranslate .nohighlight} (first term) decays sufficiently fast. This shift is achieved by the last term in the equation for [\\(V\_{ij}\\)]{.math .notranslate .nohighlight} above. This is essential only when the tapper function is turned off. The formula of taper function can be found in pair style [[ilp/graphene/hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}.

::: {.admonition .note}
Note

This potential (ILP) is intended for interlayer interactions between two different layers of graphene. To perform a realistic simulation, this potential must be used in combination with intralayer potential, such as [[AIREBO]{.doc}]pair_airebo.md){.reference .internal} or [[Tersoff]{.doc}]pair_tersoff.md){.reference .internal} potential. To keep the intralayer properties unaffected, the interlayer interaction within the same layers should be avoided. Hence, each atom has to have a layer identifier such that atoms residing on the same layer interact via the appropriate intralayer potential and atoms residing on different layers interact via the ILP. Here, the molecule id is chosen as the layer identifier, thus a data file with the "full" atom style is required to use this potential.
:::

The parameter file (e.g. CH.KC), is intended for use with *metal* [[units]{.doc}]units.md){.reference .internal}, with energies in meV. Two additional parameters, *S*, and *rcut* are included in the parameter file. *S* is designed to facilitate scaling of energies. *rcut* is designed to build the neighbor list for calculating the normals for each atom pair.

::: {.admonition .note}
Note

Two new sets of parameters of KC potential for hydrocarbons, CH.KC (without the taper function) and CH_taper.KC (with the taper function) are presented in [[(Ouyang1)]{.std .std-ref}](#ouyang3){.reference .internal}. The energy for the KC potential with the taper function goes continuously to zero at the cutoff. The parameters in both CH.KC and CH_taper.KC provide a good description in both short- and long-range interaction regimes. While the original parameters (CC.KC) published in [[(Kolmogorov)]{.std .std-ref}](#kolmogorov1){.reference .internal} are only suitable for long-range interaction regime. This feature is essential for simulations in high pressure regime (i.e., the interlayer distance is smaller than the equilibrium distance). The benchmark tests and comparison of these parameters can be found in [[(Ouyang1)]{.std .std-ref}](#ouyang3){.reference .internal} and [[(Ouyang2)]{.std .std-ref}](#ouyang4){.reference .internal}.
:::

This potential must be used in combination with hybrid/overlay. Other interactions can be set to zero using pair_style *none*.

This pair style tallies a breakdown of the total interlayer potential energy into sub-categories, which can be accessed via the [[compute pair]{.doc}]compute_pair.md){.reference .internal} command as a vector of values of length 2. The 2 values correspond to the following sub-categories:

1.  *E_vdW* = vdW (attractive) energy

2.  *E_Rep* = Repulsive energy

To print these quantities to the log file (with descriptive column headings) the following commands could be included in an input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 0 all pair kolmogorov/crespi/full
    variable Evdw  equal c_0[1]
    variable Erep  equal c_0[2]
    thermo_style custom step temp epair v_Erep v_Evdw
:::
::::
::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support the pair_modify mix, shift, table, and tail options.

This pair style does not write their information to binary restart files, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the INTERLAYER package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair style requires the newton setting to be *on* for pair interactions.

The CH.KC potential file provided with LAMMPS (see the potentials folder) is parameterized for metal units. You can use this pair style with any LAMMPS units, but you would need to create your own custom CH.KC potential file with all coefficients converted to the appropriate units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_none]{.doc}]pair_none.md){.reference .internal}, [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[pair_style drip]{.doc}]pair_drip.md){.reference .internal}, [[pair_style pair_lebedeva_z]{.doc}]pair_lebedeva_z.md){.reference .internal}, [[pair_style kolmogorov/crespi/z]{.doc}]pair_kolmogorov_crespi_z.md){.reference .internal}, [[pair_style ilp/graphene/hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

tap_flag = 0

------------------------------------------------------------------------

**(Kolmogorov)** A. N. Kolmogorov, V. H. Crespi, Phys. Rev. B 71, 235415 (2005)

**(Ouyang1)** W. Ouyang, D. Mandelli, M. Urbakh and O. Hod, Nano Lett. 18, 6009-6016 (2018).

**(Ouyang2)** W. Ouyang et al., J. Chem. Theory Comput. 16(1), 666-676 (2020).
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

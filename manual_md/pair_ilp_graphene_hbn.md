:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#pair-style-ilp-graphene-hbn-command .section}
[]{#index-1}[]{#index-0}

# pair_style ilp/graphene/hbn command[](#pair-style-ilp-graphene-hbn-command "Link to this heading"){.headerlink}

Accelerator Variant: *ilp/graphene/hbn/opt*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style [hybrid/overlay ...] ilp/graphene/hbn cutoff tap_flag
:::
::::

- cutoff = global cutoff (distance units)

- tap_flag = 0/1 to turn off/on the taper function
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style  hybrid/overlay ilp/graphene/hbn 16.0 1
    pair_coeff  * * ilp/graphene/hbn  BNCH.ILP B N C

    pair_style  hybrid/overlay rebo tersoff ilp/graphene/hbn 16.0 coul/shield 16.0
    pair_coeff  * * rebo              CH.rebo     NULL NULL C
    pair_coeff  * * tersoff           BNC.tersoff B    N    NULL
    pair_coeff  * * ilp/graphene/hbn  BNCH.ILP    B    N    C
    pair_coeff  1 1 coul/shield 0.70
    pair_coeff  1 2 coul/shield 0.695
    pair_coeff  2 2 coul/shield 0.69
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *ilp/graphene/hbn* style computes the registry-dependent interlayer potential (ILP) potential as described in [[(Leven1)]{.std .std-ref}](#leven1){.reference .internal}, [[(Leven2)]{.std .std-ref}](#leven2){.reference .internal} and [[(Maaravi)]{.std .std-ref}](#maaravi2){.reference .internal}. The normals are calculated in the way as described in [[(Kolmogorov)]{.std .std-ref}](#kolmogorov2){.reference .internal}.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} V\_{ij} \\\\ V\_{ij} = & \\mathrm{Tap}(r\_{ij})\\left \\{ e\^{-\\alpha (r\_{ij}/\\beta -1)} \\left \[ \\epsilon + f(\\rho\_{ij}) + f(\\rho\_{ji})\\right \] - \\frac{1}{1+e\^{-d\\left \[ \\left ( r\_{ij}/\\left (s_R \\cdot r\^{eff} \\right ) \\right )-1 \\right \]}} \\cdot \\frac{C_6}{r\^6\_{ij}} \\right \\}\\\\ \\rho\_{ij}\^2 = & r\_{ij}\^2 - (\\mathbf{r}\_{ij} \\cdot \\mathbf{n}\_i)\^2 \\\\ \\rho\_{ji}\^2 = & r\_{ij}\^2 - (\\mathbf{r}\_{ij} \\cdot \\mathbf{n}\_j)\^2 \\\\ f(\\rho) = & C e\^{ -( \\rho / \\delta )\^2 } \\\\ \\mathrm{Tap}(r\_{ij}) = & 20\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^7 - 70\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^6 + 84\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^5 - 35\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^4 + 1\\end{split}\\\]
:::

Where [\\(\\mathrm{Tap}(r\_{ij})\\)]{.math .notranslate .nohighlight} is the taper function which provides a continuous cutoff (up to third derivative) for interatomic separations larger than [\\(r_c\\)]{.math .notranslate .nohighlight} [[(Maaravi)]{.std .std-ref}](#maaravi2){.reference .internal}. The definitions of each parameter in the above equation can be found in [[(Leven1)]{.std .std-ref}](#leven1){.reference .internal} and [[(Maaravi)]{.std .std-ref}](#maaravi2){.reference .internal}.

It is important to include all the pairs to build the neighbor list for calculating the normals.

::: {.admonition .note}
Note

This potential (ILP) is intended for interlayer interactions between two different layers of graphene, hexagonal boron nitride (h-BN) and their hetero-junction. To perform a realistic simulation, this potential must be used in combination with intralayer potential, such as [[AIREBO]{.doc}]pair_airebo.md){.reference .internal} or [[Tersoff]{.doc}]pair_tersoff.md){.reference .internal} potential. To keep the intralayer properties unaffected, the interlayer interaction within the same layers should be avoided. Hence, each atom has to have a layer identifier such that atoms residing on the same layer interact via the appropriate intralayer potential and atoms residing on different layers interact via the ILP. Here, the molecule id is chosen as the layer identifier, thus a data file with the "full" atom style is required to use this potential.
:::

The parameter file (e.g. BNCH.ILP), is intended for use with *metal* [[units]{.doc}]units.md){.reference .internal}, with energies in meV. Two additional parameters, *S*, and *rcut* are included in the parameter file. *S* is designed to facilitate scaling of energies. *rcut* is designed to build the neighbor list for calculating the normals for each atom pair.

::: {.admonition .note}
Note

The parameters presented in the parameter file (e.g. BNCH.ILP), are fitted with taper function by setting the cutoff equal to 16.0 Angstrom. Using different cutoff or taper function should be careful. The parameters for atoms pairs between Boron and Nitrogen are fitted with a screened Coulomb interaction [[coul/shield]{.doc}]pair_coul_shield.md){.reference .internal}. Therefore, to simulated the properties of h-BN correctly, this potential must be used in combination with the pair style [[coul/shield]{.doc}]pair_coul_shield.md){.reference .internal}.
:::

::: {.admonition .note}
Note

Four new sets of parameters of ILP for 2D layered Materials with bilayer and bulk configurations are presented in [[(Ouyang1)]{.std .std-ref}](#ouyang1){.reference .internal} and [[(Ouyang2)]{.std .std-ref}](#ouyang2){.reference .internal}, respectively. These parameters provide a good description in both short- and long-range interaction regimes. While the old ILP parameters published in [[(Leven2)]{.std .std-ref}](#leven2){.reference .internal} and [[(Maaravi)]{.std .std-ref}](#maaravi2){.reference .internal} are only suitable for long-range interaction regime. This feature is essential for simulations in high pressure regime (i.e., the interlayer distance is smaller than the equilibrium distance). The benchmark tests and comparison of these parameters can be found in [[(Ouyang1)]{.std .std-ref}](#ouyang1){.reference .internal} and [[(Ouyang2)]{.std .std-ref}](#ouyang2){.reference .internal}.
:::

This potential must be used in combination with hybrid/overlay. Other interactions can be set to zero using pair_style *none*.

This pair style tallies a breakdown of the total interlayer potential energy into sub-categories, which can be accessed via the [[compute pair]{.doc}]compute_pair.md){.reference .internal} command as a vector of values of length 2. The 2 values correspond to the following sub-categories:

1.  *E_vdW* = vdW (attractive) energy

2.  *E_Rep* = Repulsive energy

To print these quantities to the log file (with descriptive column headings) the following commands could be included in an input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 0 all pair ilp/graphene/hbn
    variable Evdw  equal c_0[1]
    variable Erep  equal c_0[2]
    thermo_style custom step temp epair v_Erep v_Evdw
:::
::::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
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

This pair style requires the newton setting to be *on* for pair interactions.

The BNCH.ILP potential file provided with LAMMPS (see the potentials directory) are parameterized for *metal* units. You can use this potential with any LAMMPS units, but you would need to create your own custom BNCH.ILP potential file with coefficients listed in the appropriate units, if your simulation does not use *metal* units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_none]{.doc}]pair_none.md){.reference .internal}, [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[pair_style drip]{.doc}]pair_drip.md){.reference .internal}, [[pair_style ilp_tmd]{.doc}]pair_ilp_tmd.md){.reference .internal}, [[pair_style saip_metal]{.doc}]pair_saip_metal.md){.reference .internal}, [[pair_style pair_kolmogorov_crespi_z]{.doc}]pair_kolmogorov_crespi_z.md){.reference .internal}, [[pair_style pair_kolmogorov_crespi_full]{.doc}]pair_kolmogorov_crespi_full.md){.reference .internal}, [[pair_style pair_lebedeva_z]{.doc}]pair_lebedeva_z.md){.reference .internal}, [[pair_style pair_coul_shield]{.doc}]pair_coul_shield.md){.reference .internal}.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

tap_flag = 1

------------------------------------------------------------------------

**(Ouyang1)** W. Ouyang, D. Mandelli, M. Urbakh and O. Hod, Nano Lett. 18, 6009-6016 (2018).

**(Ouyang2)** W. Ouyang et al., J. Chem. Theory Comput. 16(1), 666-676 (2020).

**(Leven1)** I. Leven, I. Azuri, L. Kronik and O. Hod, J. Chem. Phys. 140, 104106 (2014).

**(Leven2)** I. Leven et al, J. Chem.Theory Comput. 12, 2896-905 (2016).

**(Maaravi)** T. Maaravi et al, J. Phys. Chem. C 121, 22826-22835 (2017).

**(Kolmogorov)** A. N. Kolmogorov, V. H. Crespi, Phys. Rev. B 71, 235415 (2005).
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

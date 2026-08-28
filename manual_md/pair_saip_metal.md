:::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-saip-metal-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style saip/metal command[](#pair-style-saip-metal-command "Link to this heading"){.headerlink}

Accelerator Variant: *saip/metal/opt*
:::

::::::::::::::::::::: {#pair-style-saip-metal-tmd-command .section}
# pair_style saip/metal/tmd command[](#pair-style-saip-metal-tmd-command "Link to this heading"){.headerlink}

Accelerator Variant: *saip/metal/tmd/opt*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style [hybrid/overlay ...] style cutoff tap_flag
:::
::::

- style = *saip/metal* or *saip/metal/tmd*

- cutoff = global cutoff (distance units)

- tap_flag = 0/1 to turn off/on the taper function
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style  hybrid/overlay saip/metal 16.0 1
    pair_coeff  * * saip/metal CHAu.ILP Au C H

    pair_style  hybrid/overlay eam rebo saip/metal 16.0
    pair_coeff  1 1 eam  Au_u3.eam  Au NULL NULL
    pair_coeff  * * rebo CH.rebo    NULL  C H
    pair_coeff  * * saip/metal      CHAu.ILP  Au C H

    pair_style  hybrid/overlay eam sw/mod saip/metal/tmd 16.0
    pair_coeff  1 1 eam  Au_u3.eam    Au NULL NULL
    pair_coeff  * * sw/mod tmd.sw.mod NULL  S Mo S
    pair_coeff  * * saip/metal/tmd    TMDAu.SAIP  Au S Mo S
:::
::::
:::::

:::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 17Feb2022.]{.versionmodified .added}
:::

The *saip/metal* style computes the semi-anisotropic interfacial potential (SAIP) potential for hetero-junctions formed with hexagonal 2D materials and metal surfaces, as described in [[(Ouyang6)]{.std .std-ref}](#ouyang6){.reference .internal} and [[(Yao1)]{.std .std-ref}](#yao1){.reference .internal}.

::: versionadded
[Added in version 10Dec2025.]{.versionmodified .added}
:::

The *saip/metal/tmd* style computes the semi-anisotropic interfacial potential (SAIP) potential for hetero-junctions formed with transition metal dichalcogenides (TMDCs) and metal surfaces, as described in [[(Yao2)]{.std .std-ref}](#yao2){.reference .internal}.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} V\_{ij} \\\\ V\_{ij} = & \\mathrm{Tap}(r\_{ij})\\left \\{ e\^{-\\alpha (r\_{ij}/\\beta -1)} \\left \[ \\epsilon + f(\\rho\_{ij}) + f(\\rho\_{ji})\\right \] - \\frac{1}{1+e\^{-d\\left \[ \\left ( r\_{ij}/\\left (s_R \\cdot r\^{eff} \\right ) \\right )-1 \\right \]}} \\cdot \\frac{C_6}{r\^6\_{ij}} \\right \\}\\\\ \\rho\_{ij}\^2 = & r\_{ij}\^2 - (\\mathbf{r}\_{ij} \\cdot \\mathbf{n}\_i)\^2 \\\\ \\rho\_{ji}\^2 = & r\_{ij}\^2 - (\\mathbf{r}\_{ij} \\cdot \\mathbf{n}\_j)\^2 \\\\ f(\\rho) = & C e\^{ -( \\rho / \\delta )\^2 } \\\\ \\mathrm{Tap}(r\_{ij}) = & 20\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^7 - 70\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^6 + 84\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^5 - 35\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^4 + 1\\end{split}\\\]
:::

Where [\\(\\mathrm{Tap}(r\_{ij})\\)]{.math .notranslate .nohighlight} is the taper function which provides a continuous cutoff (up to third derivative) for interatomic separations larger than [\\(r_c\\)]{.math .notranslate .nohighlight} [[pair_style ilp_graphene_hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}.

It is important to include all the pairs to build the neighbor list for calculating the normals.

::: {.admonition .note}
Note

To account for the isotropic nature of the isolated gold atom electron cloud, their corresponding normal vectors (mathbf{n}\_i) are assumed to lie along the interatomic vector mathbf{r}\_ij. Notably, this assumption is suitable for many bulk material surfaces, for example, for systems possessing s-type valence orbitals or metallic surfaces, whose valence electrons are mostly delocalized, such that their Pauli repulsion with the electrons of adjacent surfaces are isotropic. Caution should be used in the case of very small gold contacts, for example, nano-clusters, where edge effects may become relevant.
:::

The parameter file (e.g. CHAu.ILP), is intended for use with *metal* [[units]{.doc}]units.md){.reference .internal}, with energies in meV. Two additional parameters, *S*, and *rcut* are included in the parameter file. *S* is designed to facilitate scaling of energies. *rcut* is designed to build the neighbor list for calculating the normals for each atom pair.

::: {.admonition .note}
Note

The parameters presented in the parameter file (e.g. TMDAu.SAIP), are fitted with taper function by setting the cutoff equal to 16.0 Angstrom. Using different cutoff or taper function should be careful.
:::

This potential must be used in combination with hybrid/overlay. Other interactions can be set to zero using pair_style *none*.

This pair style tallies a breakdown of the total interlayer potential energy into sub-categories, which can be accessed via the [[compute pair]{.doc}]compute_pair.md){.reference .internal} command as a vector of values of length 2. The 2 values correspond to the following sub-categories:

1.  *E_vdW* = vdW (attractive) energy

2.  *E_Rep* = Repulsive energy

To print these quantities to the log file (with descriptive column headings) the following commands could be included in an input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 0 all pair saip/metal
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
::::::::::

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

The CHAu.ILP and TMDAu.SAIP potential file provided with LAMMPS (see the potentials directory) are parameterized for *metal* units. You can use this potential with any LAMMPS units, but you would need to create your own custom CHAu.ILP potential file with coefficients listed in the appropriate units, if your simulation does not use *metal* units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_none]{.doc}]pair_none.md){.reference .internal}, [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[pair_style drip]{.doc}]pair_drip.md){.reference .internal}, [[pair_style ilp_tmd]{.doc}]pair_ilp_tmd.md){.reference .internal}, [[pair_style ilp_graphene_hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}, [[pair_style pair_kolmogorov_crespi_z]{.doc}]pair_kolmogorov_crespi_z.md){.reference .internal}, [[pair_style pair_kolmogorov_crespi_full]{.doc}]pair_kolmogorov_crespi_full.md){.reference .internal}, [[pair_style pair_lebedeva_z]{.doc}]pair_lebedeva_z.md){.reference .internal}, [[pair_style pair_coul_shield]{.doc}]pair_coul_shield.md){.reference .internal}.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

tap_flag = 1

------------------------------------------------------------------------

**(Ouyang6)** W. Ouyang, O. Hod, and R. Guerra, J. Chem. Theory Comput. 17, 7215 (2021).

**(Yao1)** Y. Yao, ..., W. Ouyang, J. Phys. Chem. C, 128, 6836 (2024).

**(Yao2)** Y. Yao, ..., W. Ouyang, Adv. Sci. 12, 2415884 (2025).
:::
:::::::::::::::::::::
:::::::::::::::::::::::
::::::::::::::::::::::::

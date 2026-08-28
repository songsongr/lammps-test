:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#pair-style-aip-water-2dm-command .section}
[]{#index-1}[]{#index-0}

# pair_style aip/water/2dm command[](#pair-style-aip-water-2dm-command "Link to this heading"){.headerlink}

Accelerator Variant: *aip/water/2dm/opt*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style [hybrid/overlay ...] aip/water/2dm cutoff tap_flag
:::
::::

- cutoff = global cutoff (distance units)

- tap_flag = 0/1 to turn off/on the taper function
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style  hybrid/overlay aip/water/2dm 16.0 1
    pair_coeff  * * aip/water/2dm  CBNOH.aip.water.2dm C Ow Hw

    pair_style  hybrid/overlay aip/water/2dm 16.0 lj/cut/tip4p/long 2 3 1 1 0.1546 10 8.5
    pair_coeff  2 2   lj/cut/tip4p/long    8.0313e-3  3.1589      # O-O
    pair_coeff  2 3   lj/cut/tip4p/long    0.0        0.0         # O-H
    pair_coeff  3 3   lj/cut/tip4p/long    0.0        0.0         # H-H
    pair_coeff  * *   aip/water/2dm        CBNOH.aip.water.2dm    C Ow Hw

    pair_style  hybrid/overlay aip/water/2dm 16.0 lj/cut/tip4p/long 3 4 1 1 0.1546 10 8.5 coul/shield 16.0 1
    pair_coeff  1*2 1*2   none
    pair_coeff  3 3   lj/cut/tip4p/long    8.0313e-3  3.1589      # O-O
    pair_coeff  3 4   lj/cut/tip4p/long    0.0        0.0         # O-H
    pair_coeff  4 4   lj/cut/tip4p/long    0.0        0.0         # H-H
    pair_coeff  * *   aip/water/2dm        CBNOH.aip.water.2dm  B N Ow Hw
    pair_coeff  1 3   coul/shield          1.333
    pair_coeff  1 4   coul/shield          1.333
    pair_coeff  2 3   coul/shield          1.333
    pair_coeff  2 4   coul/shield          1.333
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 15Jun2023.]{.versionmodified .added}
:::

The *aip/water/2dm* style computes the anisotropic interfacial potential (AIP) potential for interfaces of water with two-dimensional (2D) materials as described in [[(Feng1)]{.std .std-ref}](#feng1){.reference .internal} and [[(Feng2)]{.std .std-ref}](#feng2){.reference .internal}.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} V\_{ij} \\\\ V\_{ij} = & \\mathrm{Tap}(r\_{ij})\\left \\{ e\^{-\\alpha (r\_{ij}/\\beta -1)} \\left \[ \\epsilon + f(\\rho\_{ij}) + f(\\rho\_{ji})\\right \] - \\frac{1}{1+e\^{-d\\left \[ \\left ( r\_{ij}/\\left (s_R \\cdot r\^{eff} \\right ) \\right )-1 \\right \]}} \\cdot \\frac{C_6}{r\^6\_{ij}} \\right \\}\\\\ \\rho\_{ij}\^2 = & r\_{ij}\^2 - (\\mathbf{r}\_{ij} \\cdot \\mathbf{n}\_i)\^2 \\\\ \\rho\_{ji}\^2 = & r\_{ij}\^2 - (\\mathbf{r}\_{ij} \\cdot \\mathbf{n}\_j)\^2 \\\\ f(\\rho) = & C e\^{ -( \\rho / \\delta )\^2 } \\\\ \\mathrm{Tap}(r\_{ij}) = & 20\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^7 - 70\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^6 + 84\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^5 - 35\\left ( \\frac{r\_{ij}}{R\_{cut}} \\right )\^4 + 1\\end{split}\\\]
:::

Where [\\(\\mathrm{Tap}(r\_{ij})\\)]{.math .notranslate .nohighlight} is the taper function which provides a continuous cutoff (up to third derivative) for interatomic separations larger than [\\(r_c\\)]{.math .notranslate .nohighlight} [[pair_style ilp_graphene_hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}.

::: {.admonition .note}
Note

This pair style uses the atomic normal vector definition from [[(Feng1)]{.std .std-ref}](#feng1){.reference .internal}), where the atomic normal vectors of the hydrogen atoms are assumed to lie along the corresponding oxygen-hydrogen bonds and the normal vector of the central oxygen atom is defined as their average.
:::

The provided parameter file, [`CBNOH.aip.water.2dm`{.docutils .literal .notranslate}]{.pre}, is intended for use with *metal* [[units]{.doc}]units.md){.reference .internal}, with energies in meV. Two additional parameters, *S*, and *rcut* are included in the parameter file. *S* is designed to facilitate scaling of energies; *rcut* is the cutoff for an internal, short distance neighbor list that is generated for speeding up the calculation of the normals for all atom pairs.

::: {.admonition .note}
Note

The parameters presented in the provided parameter file, [`CBNOH.aip.water.2dm`{.docutils .literal .notranslate}]{.pre}, are fitted with the taper function enabled by setting the cutoff equal to 16.0 Angstrom. Using a different cutoff or taper function setting should be carefully checked as they can lead to significant errors. These parameters provide a good description in both short- and long-range interaction regimes. This is essential for simulations in high pressure regime (i.e., the interlayer distance is smaller than the equilibrium distance).
:::

This potential must be used in combination with hybrid/overlay. Other interactions can be set to zero using [[pair_coeff settings]{.doc}]pair_coeff.md){.reference .internal} with the pair style set to *none*.

This pair style tallies a breakdown of the total interlayer potential energy into sub-categories, which can be accessed via the [[compute pair]{.doc}]compute_pair.md){.reference .internal} command as a vector of values of length 2. The 2 values correspond to the following sub-categories:

1.  *E_vdW* = vdW (attractive) energy

2.  *E_Rep* = Repulsive energy

To print these quantities to the log file (with descriptive column headings) the following commands could be included in an input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 0 all pair aip/water/2dm
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

The [`CBNOH.aip.water.2dm`{.docutils .literal .notranslate}]{.pre} potential file provided with LAMMPS is parameterized for *metal* units. You can use this pair style with any LAMMPS units, but you would need to create your own potential file with parameters in the appropriate units, if your simulation does not use *metal* units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_none]{.doc}]pair_none.md){.reference .internal}, [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[pair_style drip]{.doc}]pair_drip.md){.reference .internal}, [[pair_style ilp_tmd]{.doc}]pair_ilp_tmd.md){.reference .internal}, [[pair_style saip_metal]{.doc}]pair_saip_metal.md){.reference .internal}, [[pair_style ilp_graphene_hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}, [[pair_style pair_kolmogorov_crespi_z]{.doc}]pair_kolmogorov_crespi_z.md){.reference .internal}, [[pair_style pair_kolmogorov_crespi_full]{.doc}]pair_kolmogorov_crespi_full.md){.reference .internal}, [[pair_style pair_lebedeva_z]{.doc}]pair_lebedeva_z.md){.reference .internal}, [[pair_style pair_coul_shield]{.doc}]pair_coul_shield.md){.reference .internal}.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

tap_flag = 1

------------------------------------------------------------------------

**(Feng1)** Z. Feng, ..., and W. Ouyang, J. Phys. Chem. C. 127(18), 8704-8713 (2023).

**(Feng2)** Z. Feng, ..., and W. Ouyang, Langmuir 39(50), 18198-18207 (2023).
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

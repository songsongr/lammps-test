:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#pair-style-lebedeva-z-command .section}
[]{#index-0}

# pair_style lebedeva/z command[](#pair-style-lebedeva-z-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style [hybrid/overlay ...] lebedeva/z cutoff
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay lebedeva/z 20.0
    pair_coeff * * none
    pair_coeff 1 2 lebedeva/z  CC.Lebedeva   C C

    pair_style hybrid/overlay rebo lebedeva/z 14.0
    pair_coeff * * rebo        CH.rebo       C C
    pair_coeff 1 2 lebedeva/z  CC.Lebedeva   C C
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *lebedeva/z* pair style computes the Lebedeva interaction potential as described in [[(Lebedeva1)]{.std .std-ref}](#leb01){.reference .internal} and [[(Lebedeva2)]{.std .std-ref}](#leb02){.reference .internal}. An important simplification is made, which is to take all normals along the z-axis.

The Lebedeva potential is intended for the description of the interlayer interaction between graphene layers. To perform a realistic simulation, this potential must be used in combination with an intralayer potential such as [[AIREBO]{.doc}]pair_airebo.md){.reference .internal} or [[Tersoff]{.doc}]pair_tersoff.md){.reference .internal} facilitated by using pair style [[hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}. To keep the intralayer properties unaffected, the interlayer interaction within the same layers should be avoided. This can be achieved by assigning different atom types to atoms of different layers (e.g. 1 and 2 in the examples above).

Other interactions can be set to zero using pair_style *none*.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} V\_{ij}\\\\ V\_{ij} = & B e\^{-\\alpha(r\_{ij} - z_0)} \\\\ & + C(1 + D_1\\rho\^2\_{ij} + D_2\\rho\^4\_{ij}) e\^{-\\lambda_1\\rho\^2\_{ij}} e\^{-\\lambda_2 (z\^2\_{ij} - z\^2_0)} \\\\ & - A \\left(\\frac{z_0}{r_ij}\\right)\^6 + A \\left( \\frac{z_0}{r_c} \\right)\^6 \\\\ \\rho\^2\_{ij} = & x\^2\_{ij} + y\^2\_{ij} \\qquad (\\mathbf{n_i} \\equiv \\mathbf{\\hat{z}})\\end{split}\\\]
:::

It is important to have a sufficiently large cutoff to ensure smooth forces. Energies are shifted so that they go continuously to zero at the cutoff assuming that the exponential part of [\\(V\_{ij}\\)]{.math .notranslate .nohighlight} (first term) decays sufficiently fast. This shift is achieved by the last term in the equation for [\\(V\_{ij}\\)]{.math .notranslate .nohighlight} above.

The provided parameter file (CC.Lebedeva) contains two sets of parameters.

- The first set (element name "C") is suitable for normal conditions and is taken from [[(Popov1)]{.std .std-ref}](#popov){.reference .internal}

- The second set (element name "C1") is suitable for high-pressure conditions and is taken from [[(Koziol1)]{.std .std-ref}](#koziol){.reference .internal}

Both sets contain an additional parameter, *S*, that can be used to facilitate scaling of energies and is set to 1.0 by default.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the INTERLAYER package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style none]{.doc}]pair_none.md){.reference .internal}, [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[pair_style drip]{.doc}]pair_drip.md){.reference .internal}, [[pair_style ilp/graphene/hbd]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}, [[pair_style kolmogorov/crespi/z]{.doc}]pair_kolmogorov_crespi_z.md){.reference .internal}, [[pair_style kolmogorov/crespi/full]{.doc}]pair_kolmogorov_crespi_full.md){.reference .internal}.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Lebedeva1)** I. V. Lebedeva, A. A. Knizhnik, A. M. Popov, Y. E. Lozovik, B. V. Potapkin, Phys. Rev. B, 84, 245437 (2011)

**(Lebedeva2)** I. V. Lebedeva, A. A. Knizhnik, A. M. Popov, Y. E. Lozovik, B. V. Potapkin, Physica E: 44, 949-954 (2012)

**(Popov1)** A.M. Popov, I. V. Lebedeva, A. A. Knizhnik, Y. E. Lozovik and B. V. Potapkin, Chem. Phys. Lett. 536, 82-86 (2012).

**(Koziol1)** Z. Koziol, G. Gawlik and J. Jagielski, Chinese Phys. B 28, 096101 (2019).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

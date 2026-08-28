:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#pair-style-kolmogorov-crespi-z-command .section}
[]{#index-0}

# pair_style kolmogorov/crespi/z command[](#pair-style-kolmogorov-crespi-z-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style [hybrid/overlay ...] kolmogorov/crespi/z cutoff
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay kolmogorov/crespi/z 20.0
    pair_coeff * * none
    pair_coeff 1 2 kolmogorov/crespi/z  CC.KC   C C

    pair_style hybrid/overlay rebo kolmogorov/crespi/z 14.0
    pair_coeff * * rebo                 CH.rebo    C C
    pair_coeff 1 2 kolmogorov/crespi/z  CC.KC      C C
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *kolmogorov/crespi/z* style computes the Kolmogorov-Crespi interaction potential as described in [[(Kolmogorov)]{.std .std-ref}](#kc05){.reference .internal}. An important simplification is made, which is to take all normals along the z-axis.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} V\_{ij} \\\\ V\_{ij} = & e\^{-\\lambda(r\_{ij} -z_0)} \\left\[ C + f(\\rho\_{ij}) + f(\\rho\_{ji}) \\right\] - A \\left( \\frac{r\_{ij}}{z_0}\\right)\^{-6} + A \\left( \\frac{\\textrm{cutoff}}{z_0}\\right)\^{-6} \\\\ \\rho\_{ij}\^2 = & \\rho\_{ji}\^2 = x\_{ij}\^2 + y\_{ij}\^2 \\qquad \\qquad (\\mathbf{n}\_i \\equiv \\mathbf{\\hat{z}}) \\\\ f(\\rho) = & e\^{-(\\rho/\\delta)\^2} \\sum\_{n=0}\^2 C\_{2n} \\left( \\rho/\\delta \\right)\^{2n}\\end{split}\\\]
:::

It is important to have a sufficiently large cutoff to ensure smooth forces. Energies are shifted so that they go continuously to zero at the cutoff assuming that the exponential part of [\\(V\_{ij}\\)]{.math .notranslate .nohighlight} (first term) decays sufficiently fast. This shift is achieved by the last term in the equation for [\\(V\_{ij}\\)]{.math .notranslate .nohighlight} above.

This potential is intended for interactions between two layers of graphene. Therefore, to avoid interaction between layers in multi-layered materials, each layer should have a separate atom type and interactions should only be computed between atom types of neighboring layers.

The parameter file (e.g. CC.KC), is intended for use with metal [[units]{.doc}]units.md){.reference .internal}, with energies in meV. An additional parameter, *S*, is available to facilitate scaling of energies in accordance with [[(vanWijk)]{.std .std-ref}](#vanwijk){.reference .internal}.

This potential must be used in combination with hybrid/overlay. Other interactions can be set to zero using pair_style *none*.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the INTERLAYER package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_none]{.doc}]pair_none.md){.reference .internal}, [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[pair_style drip]{.doc}]pair_drip.md){.reference .internal}, [[pair_style ilp/graphene/hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal}. [[pair_style kolmogorov/crespi/full]{.doc}]pair_kolmogorov_crespi_full.md){.reference .internal}, [[pair_style lebedeva/z]{.doc}]pair_lebedeva_z.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Kolmogorov)** A. N. Kolmogorov, V. H. Crespi, Phys. Rev. B 71, 235415 (2005)

**(vanWijk)** M. M. van Wijk, A. Schuring, M. I. Katsnelson, and A. Fasolino, Physical Review Letters, 113, 135504 (2014)
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#pair-style-spin-magelec-command .section}
[]{#index-0}

# pair_style spin/magelec command[](#pair-style-spin-magelec-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/magelec cutoff
:::
::::

- cutoff = global cutoff pair (distance in metal units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/magelec 4.5
    pair_coeff * * magelec 4.5 0.00109 1.0 1.0 1.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *spin/me* computes a magneto-electric interaction between pairs of magnetic spins. According to the derivation reported in [[(Katsura)]{.std .std-ref}](#katsura1){.reference .internal}, this interaction is defined as:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\vec{\\omega}\_i & = -\\frac{1}{\\hbar} \\sum\_{j}\^{Neighb} \\vec{s}\_{j}\\times\\vec{D}(r\_{ij}) \\\\ \\vec{F}\_i & = -\\sum\_{j}\^{Neighb} \\frac{\\partial D(r\_{ij})}{\\partial r\_{ij}} \\left(\\vec{s}\_{i}\\times \\vec{s}\_{j} \\right) \\cdot \\vec{r}\_{ij}\\end{split}\\\]
:::

where [\\(\\vec{s}\_i\\)]{.math .notranslate .nohighlight} and [\\(\\vec{s}\_j\\)]{.math .notranslate .nohighlight} are neighboring magnetic spins of two particles.

From this magneto-electric interaction, each spin i will be submitted to a magnetic torque omega, and its associated atom can be submitted to a force F for spin-lattice calculations (see [[fix nve/spin]{.doc}]fix_nve_spin.md){.reference .internal}), such as:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\vec{F}\^{i} & = -\\sum\_{j}\^{Neighbor} \\left( \\vec{s}\_{i}\\times \\vec{s}\_{j} \\right) \\times \\vec{E} \\\\ \\vec{\\omega}\^{i} = -\\frac{1}{\\hbar} \\sum\_{j}\^{Neighbor} \\vec{s}\_j \\times \\left(\\vec{E}\\times r\_{ij} \\right)\\end{split}\\\]
:::

with h the Planck constant (in metal units) and [\\(\\vec{E}\\)]{.math .notranslate .nohighlight} an electric polarization vector. The norm and direction of E are giving the intensity and the direction of a screened dielectric atomic polarization (in eV).

More details about the derivation of these torques/forces are reported in [[(Tranchida)]{.std .std-ref}](#tranchida4){.reference .internal}.
:::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

All the *pair/spin* styles are part of the SPIN package. These styles are only enabled if LAMMPS was built with this package, and if the atom_style "spin" was declared. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[atom_style spin]{.doc}]atom_style.md){.reference .internal}, [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style spin/exchange]{.doc}]pair_spin_exchange.md){.reference .internal}, [[pair_eam]{.doc}]pair_eam.md){.reference .internal},
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Katsura)** H. Katsura, N. Nagaosa, A.V. Balatsky. Phys. Rev. Lett., 95(5), 057205. (2005)

**(Tranchida)** Tranchida, Plimpton, Thibaudeau, and Thompson, Journal of Computational Physics, 372, 406-425, (2018).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

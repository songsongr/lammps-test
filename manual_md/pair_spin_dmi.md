::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#pair-style-spin-dmi-command .section}
[]{#index-0}

# pair_style spin/dmi command[](#pair-style-spin-dmi-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/dmi cutoff
:::
::::

- cutoff = global cutoff pair (distance in metal units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/dmi 4.0
    pair_coeff * * dmi 2.6 0.001 1.0 0.0 0.0
    pair_coeff 1 2 dmi 4.0 0.00109 0.0 0.0 1.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *spin/dmi* computes the Dzyaloshinskii-Moriya (DM) interaction between pairs of magnetic spins. According to the expression reported in [[(Rohart)]{.std .std-ref}](#rohart){.reference .internal}, one has the following DM energy:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{H}\_{dm} = \\sum\_{{ i,j}=1,i\\neq j}\^{N} \\left( \\vec{e}\_{ij} \\times \\vec{D} \\right) \\cdot\\left(\\vec{s}\_{i}\\times \\vec{s}\_{j}\\right),\\\]
:::

where [\\(\\vec{s}\_i\\)]{.math .notranslate .nohighlight} and [\\(\\vec{s}\_j\\)]{.math .notranslate .nohighlight} are two neighboring magnetic spins of two particles, [\\(\\vec{e}\_ij = \\frac{r_i - r_j}{\\left\| r_i - r_j \\right\|}\\)]{.math .notranslate .nohighlight} is the unit vector between sites *i* and *j*, and [\\(\\vec{D}\\)]{.math .notranslate .nohighlight} is the DM vector defining the intensity (in eV) and the direction of the interaction.

In [[(Rohart)]{.std .std-ref}](#rohart){.reference .internal}, [\\(\\vec{D}\\)]{.math .notranslate .nohighlight} is defined as the direction normal to the film oriented from the high spin-orbit layer to the magnetic ultra-thin film.

The application of a spin-lattice Poisson bracket to this energy (as described in [[(Tranchida)]{.std .std-ref}](#tranchida5){.reference .internal}) allows to derive a magnetic torque omega, and a mechanical force F (for spin-lattice calculations only) for each magnetic particle i:

::: {.math .notranslate .nohighlight}
\\\[\\vec{\\omega}\_i = -\\frac{1}{\\hbar} \\sum\_{j}\^{Neighb} \\vec{s}\_{j}\\times \\left(\\vec{e}\_{ij}\\times \\vec{D} \\right) \~\~\\mathrm{and}\~\~ \\vec{F}\_i = -\\sum\_{j}\^{Neighb} \\frac{1}{r\_{ij}} \\vec{D} \\times \\left( \\vec{s}\_{i}\\times \\vec{s}\_{j} \\right)\\\]
:::

More details about the derivation of these torques/forces are reported in [[(Tranchida)]{.std .std-ref}](#tranchida5){.reference .internal}.

For the *spin/dmi* pair style, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, and set in the following order:

- rc (distance units)

- \|D\| (energy units)

- Dx, Dy, Dz (direction of D)

Note that rc is the radius cutoff of the considered DM interaction, \|D\| is the norm of the DM vector (in eV), and Dx, Dy and Dz define its direction.

None of those coefficients is optional. If not specified, the *spin/dmi* pair style cannot be used.
:::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

All the *pair/spin* styles are part of the SPIN package. These styles are only enabled if LAMMPS was built with this package, and if the atom_style "spin" was declared. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[atom_style spin]{.doc}]atom_style.md){.reference .internal}, [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_eam]{.doc}]pair_eam.md){.reference .internal},
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

[]{#rohart}**(Rohart)** Rohart and Thiaville, Physical Review B, 88(18), 184422. (2013).

**(Tranchida)** Tranchida, Plimpton, Thibaudeau and Thompson, Journal of Computational Physics, 372, 406-425, (2018).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

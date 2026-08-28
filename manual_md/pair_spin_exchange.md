::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-spin-exchange-command .section}
[]{#index-1}[]{#index-0}

# pair_style spin/exchange command[](#pair-style-spin-exchange-command "Link to this heading"){.headerlink}
:::

:::::::::::::::::::: {#pair-style-spin-exchange-biquadratic-command .section}
# pair_style spin/exchange/biquadratic command[](#pair-style-spin-exchange-biquadratic-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/exchange cutoff
    pair_style spin/exchange/biquadratic cutoff
:::
::::

- cutoff = global cutoff pair (distance in metal units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/exchange 4.0
    pair_coeff * * exchange 4.0 0.0446928 0.003496 1.4885
    pair_coeff 1 2 exchange 6.0 -0.01575 0.0 1.965 offset yes

    pair_style spin/exchange/biquadratic 4.0
    pair_coeff * * biquadratic 4.0 0.05 0.03 1.48 0.05 0.03 1.48 offset no
    pair_coeff 1 2 biquadratic 6.0 -0.01 0.0 1.9 0.0 0.1 19
:::
::::
:::::

:::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *spin/exchange* computes the exchange interaction between pairs of magnetic spins:

::: {.math .notranslate .nohighlight}
\\\[H\_{ex} = -\\sum\_{i,j}\^N J\_{ij} (r\_{ij}) \\,\\vec{s}\_i \\cdot \\vec{s}\_j\\\]
:::

where [\\(\\vec{s}\_i\\)]{.math .notranslate .nohighlight} and [\\(\\vec{s}\_j\\)]{.math .notranslate .nohighlight} are two unit vectors representing the magnetic spins of two particles (usually atoms), and [\\(r\_{ij} = \\vert \\vec{r}\_i - \\vec{r}\_j \\vert\\)]{.math .notranslate .nohighlight} is the inter-atomic distance between those two particles. The summation is over pairs of nearest neighbors. [\\(J(r\_{ij})\\)]{.math .notranslate .nohighlight} is a function defining the intensity and the sign of the exchange interaction for different neighboring shells.

Style *spin/exchange/biquadratic* computes a biquadratic exchange interaction between pairs of magnetic spins:

::: {.math .notranslate .nohighlight}
\\\[H\_{bi} = -\\sum\_{i, j}\^{N} {J}\_{ij} \\left(r\_{ij} \\right)\\, \\vec{s}\_{i}\\cdot \\vec{s}\_{j} -\\sum\_{i, j}\^{N} {K}\_{ij} \\left(r\_{ij} \\right)\\, \\left(\\vec{s}\_{i}\\cdot \\vec{s}\_{j}\\right)\^2\\\]
:::

where [\\(\\vec{s}\_i\\)]{.math .notranslate .nohighlight}, [\\(\\vec{s}\_j\\)]{.math .notranslate .nohighlight}, [\\(r\_{ij}\\)]{.math .notranslate .nohighlight} and [\\(J(r\_{ij})\\)]{.math .notranslate .nohighlight} have the same definitions as above, and [\\(K(r\_{ij})\\)]{.math .notranslate .nohighlight} is a second function, defining the intensity and the sign of the biquadratic term.

The interatomic dependence of [\\(J(r\_{ij})\\)]{.math .notranslate .nohighlight} and [\\(K(r\_{ij})\\)]{.math .notranslate .nohighlight} in both interactions above is defined by the following function:

::: {.math .notranslate .nohighlight}
\\\[{f}\\left( r\_{ij} \\right) = 4 a \\left( \\frac{r\_{ij}}{d} \\right)\^2 \\left( 1 - b \\left( \\frac{r\_{ij}}{d} \\right)\^2 \\right) e\^{-\\left( \\frac{r\_{ij}}{d} \\right)\^2 }\\Theta (R_c - r\_{ij})\\\]
:::

where [\\(a\\)]{.math .notranslate .nohighlight}, [\\(b\\)]{.math .notranslate .nohighlight} and [\\(d\\)]{.math .notranslate .nohighlight} are the three constant coefficients defined in the associated "pair_coeff" command, and [\\(R_c\\)]{.math .notranslate .nohighlight} is the radius cutoff associated to the pair interaction (see below for more explanations).

The coefficients [\\(a\\)]{.math .notranslate .nohighlight}, [\\(b\\)]{.math .notranslate .nohighlight}, and [\\(d\\)]{.math .notranslate .nohighlight} need to be fitted so that the function above matches with the value of the exchange interaction for the [\\(N\\)]{.math .notranslate .nohighlight} neighbor shells taken into account. Examples and more explanations about this function and its parameterization are reported in [[(Tranchida)]{.std .std-ref}](#tranchida3){.reference .internal}.

When a *spin/exchange/biquadratic* pair style is defined, six coefficients (three for [\\(J(r\_{ij})\\)]{.math .notranslate .nohighlight}, and three for [\\(K(r\_{ij})\\)]{.math .notranslate .nohighlight}) have to be fitted.

From this exchange interaction, each spin [\\(i\\)]{.math .notranslate .nohighlight} will be submitted to a magnetic torque [\\(\\vec{\\omega}\_{i}\\)]{.math .notranslate .nohighlight}, and its associated atom can be submitted to a force [\\(\\vec{F}\_{i}\\)]{.math .notranslate .nohighlight} for spin-lattice calculations (see [[fix nve/spin]{.doc}]fix_nve_spin.md){.reference .internal}), such as:

::: {.math .notranslate .nohighlight}
\\\[\\vec{\\omega}\_{i} = \\frac{1}{\\hbar} \\sum\_{j}\^{Neighb} {J} \\left(r\_{ij} \\right)\\,\\vec{s}\_{j} \~\~\\mathrm{and}\~\~ \\vec{F}\_{i} = \\sum\_{j}\^{Neighb} \\frac{\\partial {J} \\left(r\_{ij} \\right)}{ \\partial r\_{ij}} \\left( \\vec{s}\_{i}\\cdot \\vec{s}\_{j} \\right) \\vec{e}\_{ij}\\\]
:::

with [\\(\\hbar\\)]{.math .notranslate .nohighlight} the Planck constant (in metal units), and [\\(\\vec{e}\_{ij} = \\frac{\\vec{r}\_i - \\vec{r}\_j}{\\vert \\vec{r}\_i-\\vec{r}\_j \\vert}\\)]{.math .notranslate .nohighlight} the unit vector between sites [\\(i\\)]{.math .notranslate .nohighlight} and [\\(j\\)]{.math .notranslate .nohighlight}. Equivalent forces and magnetic torques are generated for the biquadratic term when a *spin/exchange/biquadratic* pair style is defined.

More details about the derivation of these torques/forces are reported in [[(Tranchida)]{.std .std-ref}](#tranchida3){.reference .internal}.

For the *spin/exchange* and *spin/exchange/biquadratic* pair styles, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, and set in the following order:

- [\\(R_c\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(a\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(b\\)]{.math .notranslate .nohighlight} (adim parameter)

- [\\(d\\)]{.math .notranslate .nohighlight} (distance units)

for the *spin/exchange* pair style, and:

- [\\(R_c\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(a_j\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(b_j\\)]{.math .notranslate .nohighlight} (adim parameter)

- [\\(d_j\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(a_k\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(b_k\\)]{.math .notranslate .nohighlight} (adim parameter)

- [\\(d_k\\)]{.math .notranslate .nohighlight} (distance units)

for the *spin/exchange/biquadratic* pair style.

Note that [\\(R_c\\)]{.math .notranslate .nohighlight} is the radius cutoff of the considered exchange interaction, and [\\(a\\)]{.math .notranslate .nohighlight}, [\\(b\\)]{.math .notranslate .nohighlight} and [\\(d\\)]{.math .notranslate .nohighlight} are the three coefficients performing the parameterization of the function [\\(J(r\_{ij})\\)]{.math .notranslate .nohighlight} defined above (in the *biquadratic* style, [\\(a_j\\)]{.math .notranslate .nohighlight}, [\\(b_j\\)]{.math .notranslate .nohighlight}, [\\(d_j\\)]{.math .notranslate .nohighlight} and [\\(a_k\\)]{.math .notranslate .nohighlight}, [\\(b_k\\)]{.math .notranslate .nohighlight}, [\\(d_k\\)]{.math .notranslate .nohighlight} are the coefficients of [\\(J(r\_{ij})\\)]{.math .notranslate .nohighlight} and [\\(K(r\_{ij})\\)]{.math .notranslate .nohighlight} respectively).

None of those coefficients is optional. If not specified, the *spin/exchange* pair style cannot be used.

------------------------------------------------------------------------

**Offsetting magnetic forces and energies**:

For spin-lattice simulation, it can be useful to offset the mechanical forces and energies generated by the exchange interaction. The *offset* keyword allows to apply this offset. By setting *offset* to *yes*, the energy definitions above are replaced by:

::: {.math .notranslate .nohighlight}
\\\[H\_{ex} = -\\sum\_{i,j}\^N J\_{ij} (r\_{ij}) \\,\[ \\vec{s}\_i \\cdot \\vec{s}\_j-1 \]\\\]
:::

for the *spin/exchange* pair style, and:

::: {.math .notranslate .nohighlight}
\\\[H\_{bi} = -\\sum\_{i, j}\^{N} {J}\_{ij} \\left(r\_{ij} \\right)\\, \[ \\vec{s}\_{i}\\cdot \\vec{s}\_{j} -1 \] -\\sum\_{i, j}\^{N} {K}\_{ij} \\left(r\_{ij} \\right)\\, \[ \\left(\\vec{s}\_{i}\\cdot \\vec{s}\_{j}\\right)\^2 -1\]\\\]
:::

for the *spin/exchange/biquadratic* pair style.

Note that this offset only affects the calculation of the energy and mechanical forces. It does not modify the calculation of the precession vectors (and thus does no impact the purely magnetic properties). This ensures that when all spins are aligned, the magnetic energy and the associated mechanical forces (and thus the pressure generated by the magnetic potential) are null.

::: {.admonition .note}
Note

This offset term can be very important when calculations such as equations of state (energy vs volume, or energy vs pressure) are being performed. Indeed, setting the *offset* term ensures that at the ground state of the crystal and at the equilibrium magnetic configuration (typically ferromagnetic), the pressure is null, as expected. Otherwise, magnetic forces could generate a residual pressure.
:::

When the *offset* option is set to *no*, no offset is applied (also corresponding to the default option).
::::::::::

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

The default *offset* keyword value is *no*.

------------------------------------------------------------------------

**(Tranchida)** Tranchida, Plimpton, Thibaudeau and Thompson, Journal of Computational Physics, 372, 406-425, (2018).
:::
::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

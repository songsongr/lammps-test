::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#pair-style-sdpd-taitwater-isothermal-command .section}
[]{#index-0}

# pair_style sdpd/taitwater/isothermal command[](#pair-style-sdpd-taitwater-isothermal-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style sdpd/taitwater/isothermal temperature viscosity seed
:::
::::

- temperature = temperature of the fluid (temperature units)

- viscosity = dynamic viscosity of the fluid (mass\*distance/time units)

- seed = random number generator seed (positive integer, optional)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style sdpd/taitwater/isothermal 300. 1. 28681
    pair_coeff * * 1000.0 1430.0 2.4
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The sdpd/taitwater/isothermal style computes forces between mesoscopic particles according to the Smoothed Dissipative Particle Dynamics model described in this paper by [[(Espanol and Revenga)]{.std .std-ref}](#espanol-revenga){.reference .internal} under the following assumptions:

1.  The temperature is constant and uniform.

2.  The shear viscosity is constant and uniform.

3.  The volume viscosity is negligible before the shear viscosity.

4.  The Boltzmann constant is negligible before the heat capacity of a single mesoscopic particle of fluid.

The third assumption is true for water in nearly incompressible flows. The fourth holds true for water for any reasonable size one can imagine for a mesoscopic particle.

The pressure forces between particles will be computed according to Tait's equation of state:

::: {.math .notranslate .nohighlight}
\\\[p = B \\left\[(\\frac{\\rho}{\\rho_0})\^{\\gamma} - 1\\right\]\\\]
:::

where [\\(\\gamma = 7\\)]{.math .notranslate .nohighlight} and [\\(B = c_0\^2 \\rho_0 / \\gamma\\)]{.math .notranslate .nohighlight}, with [\\(\\rho_0\\)]{.math .notranslate .nohighlight} being the reference density and [\\(c_0\\)]{.math .notranslate .nohighlight} the reference speed of sound.

The laminar viscosity and the random forces will be computed according to formulas described in [[(Espanol and Revenga)]{.std .std-ref}](#espanol-revenga){.reference .internal}.

::: {.admonition .warning}
Warning

Similar to [[brownian]{.doc}]pair_brownian.md){.reference .internal} and [[dpd]{.doc}]pair_dpd.md){.reference .internal} styles, the [[newton]{.doc}]newton.md){.reference .internal} setting for pairwise interactions needs to be on when running LAMMPS in parallel if you want to ensure linear momentum conservation. Otherwise random forces generated for pairs straddling processor boundary will not be equal and opposite.
:::

::: {.admonition .note}
Note

The actual random seed used will be a mix of what you specify and other parameters like the MPI ranks. This is to ensure that different MPI tasks have distinct seeds.
:::

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above.

- [\\(\\rho_0\\)]{.math .notranslate .nohighlight} reference density (mass/volume units)

- [\\(c_0\\)]{.math .notranslate .nohighlight} reference soundspeed (distance/time units)

- h kernel function cutoff (distance units)
::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This style does not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

This style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This style does not write information to [[binary restart files]{.doc}]restart.md){.reference .internal}. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the DPD-SMOOTH package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair sph/rhosum]{.doc}]pair_sph_rhosum.md){.reference .internal}, [[pair sph/taitwater]{.doc}]pair_sph_taitwater.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default seed is 0 (before mixing).

------------------------------------------------------------------------

**(Espanol and Revenga)** Espanol, Revenga, Physical Review E, 67, 026705 (2003).
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

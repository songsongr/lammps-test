:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-sph-taitwater-morris-command .section}
[]{#index-0}

# pair_style sph/taitwater/morris command[](#pair-style-sph-taitwater-morris-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style sph/taitwater/morris
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style sph/taitwater/morris
    pair_coeff * * 1000.0 1430.0 1.0 2.4
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The sph/taitwater/morris style computes pressure forces between SPH particles according to Tait's equation of state:

::: {.math .notranslate .nohighlight}
\\\[p = B \\biggl\[\\left(\\frac{\\rho}{\\rho_0}\\right)\^{\\gamma} - 1\\biggr\]\\\]
:::

where [\\(\\gamma = 7\\)]{.math .notranslate .nohighlight} and [\\(B = c_0\^2 \\rho_0 / \\gamma\\)]{.math .notranslate .nohighlight}, with [\\(\\rho_0\\)]{.math .notranslate .nohighlight} being the reference density and [\\(c_0\\)]{.math .notranslate .nohighlight} the reference speed of sound.

This pair style also computes laminar viscosity [[(Morris)]{.std .std-ref}](#morris){.reference .internal}.

See [this PDF guide](PDF/SPH_LAMMPS_userguide.pdf){.reference .external} to using SPH in LAMMPS.

::: {.admonition .note}
Note

Please note that the SPH PDF guide file has not been updated for many years and thus does not reflect the current *syntax* of the SPH package commands. For that please refer to the LAMMPS manual.
:::

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above.

- [\\(\\rho_0\\)]{.math .notranslate .nohighlight} reference density (mass/volume units)

- [\\(c_0\\)]{.math .notranslate .nohighlight} reference soundspeed (distance/time units)

- [\\(\\nu\\)]{.math .notranslate .nohighlight} dynamic viscosity (mass\*distance/time units)

- h kernel function cutoff (distance units)
:::::

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

This pair style is part of the SPH package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, pair_sph/rhosum
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Morris)** Morris, Fox, Zhu, J Comp Physics, 136, 214-226 (1997).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

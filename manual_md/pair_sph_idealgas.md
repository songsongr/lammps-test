:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-sph-idealgas-command .section}
[]{#index-0}

# pair_style sph/idealgas command[](#pair-style-sph-idealgas-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style sph/idealgas
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style sph/idealgas
    pair_coeff * * 1.0 2.4
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The sph/idealgas style computes pressure forces between particles according to the ideal gas equation of state:

::: {.math .notranslate .nohighlight}
\\\[p = (\\gamma - 1) \\rho e\\\]
:::

where [\\(\\gamma = 1.4\\)]{.math .notranslate .nohighlight} is the heat capacity ratio, [\\(\\rho\\)]{.math .notranslate .nohighlight} is the local density, and e is the internal energy per unit mass. This pair style also computes Monaghan's artificial viscosity to prevent particles from interpenetrating [[(Monaghan)]{.std .std-ref}](#ideal-monoghan){.reference .internal}.

See [this PDF guide](PDF/SPH_LAMMPS_userguide.pdf){.reference .external} to using SPH in LAMMPS.

::: {.admonition .note}
Note

Please note that the SPH PDF guide file has not been updated for many years and thus does not reflect the current *syntax* of the SPH package commands. For that please refer to the LAMMPS manual.
:::

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above.

- [\\(\\nu\\)]{.math .notranslate .nohighlight} artificial viscosity (no units)

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

**(Monaghan)** Monaghan and Gingold, Journal of Computational Physics, 52, 374-389 (1983).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

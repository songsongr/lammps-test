::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#pair-style-rheo-command .section}
[]{#index-0}

# pair_style rheo command[](#pair-style-rheo-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style rheo cutoff keyword values
:::
::::

- cutoff = global cutoff for kernel (distance units)

- zero or more keyword/value pairs may be appended to args

- keyword = *rho/damp* or *artificial/visc* or *harmonic/means*

``` literal-block
rho/damp args = density damping prefactor \(\xi\)
artificial/visc args = artificial viscosity prefactor \(\zeta\)
harmonic/means args = none
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style rheo 3.0 rho/damp 1.0 artificial/visc 2.0
    pair_coeff * *
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 29Aug2024.]{.versionmodified .added}
:::

Pair style *rheo* computes pressure and viscous forces between particles in the [[rheo package]{.doc}]Howto_rheo.md){.reference .internal}. If thermal evolution is turned on in [[fix rheo]{.doc}]fix_rheo.md){.reference .internal}, then the pair style also calculates heat exchanged between particles.

The *artificial/viscosity* keyword is used to specify the magnitude [\\(\\zeta\\)]{.math .notranslate .nohighlight} of an optional artificial viscosity contribution to forces. This factor can help stabilize simulations by smoothing out small length scale variations in velocity fields. Artificial viscous forces typically are only exchanged by fluid particles. However, if interfaces are not reconstructed in fix rheo, fluid particles will also exchange artificial viscous forces with solid particles to improve stability.

The *rho/damp* keyword is used to specify the magnitude [\\(\\xi\\)]{.math .notranslate .nohighlight} of an optional pairwise damping term between the density of particles. This factor can help stabilize simulations by smoothing out small length scale variations in density fields. However, in systems that develop a density gradient in equilibrium (e.g. in a hydrostatic column underlying gravity), this option may be inappropriate.

If particles have different viscosities or conductivities, the *harmonic/means* keyword changes how they are averaged before calculating pairwise forces or heat exchanges. By default, an arithmetic averaged is used, however, a harmonic mean may improve stability in systems with multiple fluid phases with large disparities in viscosities.

No coefficients are defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This style does not write information to [[binary restart files]{.doc}]restart.md){.reference .internal}. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the RHEO package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix rheo]{.doc}]fix_rheo.md){.reference .internal}, [[fix rheo/pressure]{.doc}]fix_rheo_pressure.md){.reference .internal}, [[fix rheo/thermal]{.doc}]fix_rheo_thermal.md){.reference .internal}, [[fix rheo/viscosity]{.doc}]fix_rheo_viscosity.md){.reference .internal}, [[compute rheo/property/atom]{.doc}]compute_rheo_property_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

Density damping and artificial viscous forces are not calculated. Arithmetic means are used for mixing particle properties.
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

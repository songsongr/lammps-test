::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#pair-style-bpm-spring-command .section}
[]{#index-0}

# pair_style bpm/spring command[](#pair-style-bpm-spring-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style bpm/spring keyword value  ...
:::
::::

- optional keyword = *anharmonic*

  ``` literal-block
  anharmonic value = yes or no
     whether forces include the anharmonic term
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style bpm/spring
    pair_coeff * * 1.0 1.0 1.0
    pair_style bpm/spring anharmonic yes
    pair_coeff 1 1 1.0 1.0 1.0 50.0
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

Style *bpm/spring* computes pairwise forces with the formula

::: {.math .notranslate .nohighlight}
\\\[F = k (r - r_c) + k_a (r - r_c)\^3\\\]
:::

where [\\(k\\)]{.math .notranslate .nohighlight} is a stiffness, [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff length, and [\\(k_a\\)]{.math .notranslate .nohighlight} is an optional anharmonic cubic prefactor that can be enabled using the *anharmonic* keyword. The anharmonic term may be useful in scenarios that need to prevent large particle overlap.

An additional damping force is also applied to interacting particles. The force is proportional to the difference in the normal velocity of particles

::: {.math .notranslate .nohighlight}
\\\[F_D = - \\gamma w (\\hat{r} \\bullet \\vec{v})\\\]
:::

where [\\(\\gamma\\)]{.math .notranslate .nohighlight} is the damping strength, [\\(\\hat{r}\\)]{.math .notranslate .nohighlight} is the radial normal vector, [\\(\\vec{v}\\)]{.math .notranslate .nohighlight} is the velocity difference between the two particles, and [\\(w\\)]{.math .notranslate .nohighlight} is a smoothing factor. This smoothing factor is constructed such that damping forces go to zero as particles come out of contact to avoid discontinuities. It is given by

::: {.math .notranslate .nohighlight}
\\\[w = 1.0 - \\left( \\frac{r}{r_c} \\right)\^8 .\\\]
:::

This pair style is designed for use in a spring-based bonded particle model. It mirrors the construction of the [[bpm/spring]{.doc}]bond_bpm_spring.md){.reference .internal} bond style.

This pair interaction is always applied to pairs of non-bonded particles that are within the interaction distance. For pairs of bonded particles that are within the interaction distance, there is the option to either include this pair interaction and overlay the pair force over the bond force or to exclude this pair interaction such that the two particles only interact via the bond force. See discussion of the *overlay/pair* option for BPM bond styles and the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command in the [[how to]{.doc}]Howto_bpm.md){.reference .internal} page on BPMs for more details.

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(k\\)]{.math .notranslate .nohighlight} (force/distance units)

- [\\(r_c\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

::: versionadded
[Added in version 4Feb2025.]{.versionmodified .added}
:::

Additionally, if *anharmonic* is set to *yes*, a fourth coefficient must be provided:

- [\\(k_a\\)]{.math .notranslate .nohighlight} (force/distance\^3 units)
::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the A coefficient and cutoff distance for this pair style can be mixed. A is always mixed via a *geometric* rule. The cutoff is mixed according to the pair_modify mix value. The default mix value is *geometric*. See the "pair_modify" command for details.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option, since the pair interaction goes to 0.0 at the cutoff.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table and tail options are not relevant for this pair style.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.

The potential energy and the single() function of this pair style returns [\\(k (r - r_c)\^2 / 2 + k_a (r - r_c)\^4 / 4\\)]{.math .notranslate .nohighlight} for a proxy of the energy of a pair interaction, ignoring any smoothing or dissipative forces.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the BPM package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[bond bpm/spring]{.doc}]bond_bpm_spring.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *anharmonic* = *no*
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

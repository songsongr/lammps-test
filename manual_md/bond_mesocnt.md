::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#bond-style-mesocnt-command .section}
[]{#index-0}

# bond_style mesocnt command[](#bond-style-mesocnt-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style mesocnt
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style mesocnt
    bond_coeff 1 C 10 10 20.0
    bond_coeff 4 custom 800.0 10.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 15Sep2022.]{.versionmodified .added}
:::

The *mesocnt* bond style is a wrapper for the [[harmonic]{.doc}]bond_harmonic.md){.reference .internal} style, and uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = K (r - r_0)\^2\\\]
:::

where [\\(r_0\\)]{.math .notranslate .nohighlight} is the equilibrium bond distance. Note that the usual 1/2 factor is included in [\\(K\\)]{.math .notranslate .nohighlight}. The style implements parameterization presets of [\\(K\\)]{.math .notranslate .nohighlight} for mesoscopic simulations of carbon nanotubes based on the atomistic simulations of [[(Srivastava)]{.std .std-ref}](#srivastava-1){.reference .internal}.

Other presets can be readily implemented in the future.

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- preset = *C* or *custom*

- additional parameters depending on preset

Preset *C* is for carbon nanotubes, and the additional parameters are:

- chiral index [\\(n\\)]{.math .notranslate .nohighlight} (unitless)

- chiral index [\\(m\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)

Preset *custom* is simply a direct wrapper for the [[harmonic]{.doc}]bond_harmonic.md){.reference .internal} style, and the additional parameters are:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)
:::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the MOLECULE and MESONT packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Srivastava)** Zhigilei, Wei and Srivastava, Phys. Rev. B 71, 165417 (2005).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

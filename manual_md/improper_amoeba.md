::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#improper-style-amoeba-command .section}
[]{#index-0}

# improper_style amoeba command[](#improper-style-amoeba-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style amoeba
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style amoeba
    improper_coeff 1 49.6
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *amoeba* improper style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = K (\\chi)\^2\\\]
:::

where [\\(\\chi\\)]{.math .notranslate .nohighlight} is the improper angle and [\\(K\\)]{.math .notranslate .nohighlight} is a prefactor. Note that the usual 1/2 factor is included in [\\(K\\)]{.math .notranslate .nohighlight}.

This formula seems like a simplified version of the formula for the [[improper_style harmonic]{.doc}]improper_harmonic.md){.reference .internal} command with [\\(\\chi_0\\)]{.math .notranslate .nohighlight} = 0.0. However the computation of the angle [\\(\\chi\\)]{.math .notranslate .nohighlight} is done differently to match how the Tinker MD code computes its out-of-plane improper for the AMOEBA and HIPPO force fields. See the [[Howto amoeba]{.doc}]Howto_amoeba.md){.reference .internal} doc page for more information about the implementation of AMOEBA and HIPPO in LAMMPS.

If the 4 atoms in an improper quadruplet (listed in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command are ordered I,J,K,L then atoms I,K,L are considered to lie in a plane and atom J is out-of-plane. The angle [\\(\\chi_0\\)]{.math .notranslate .nohighlight} is computed as the Allinger angle which is defined as the angle between the plane of I,K,L, and the vector from atom I to atom J.

The following coefficient must be defined for each improper type via the [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

Note that the angle [\\(\\chi\\)]{.math .notranslate .nohighlight} is computed in radians; hence [\\(K\\)]{.math .notranslate .nohighlight} is effectively energy per radian\^2.
::::

------------------------------------------------------------------------

::: {#symmetry-convention .section}
## Symmetry convention[](#symmetry-convention "Link to this heading"){.headerlink}

For the *amoeba* improper style, the second atom in the quadruplet is the atom of symmetry; all other atoms are considered interchangeable. This convention is relevant for operations that require knowledge of how atoms are ordered, such as automatic assignment of new improper types by [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This improper style can only be used if LAMMPS was built with the AMOEBA package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[improper_coeff]{.doc}]improper_coeff.md){.reference .internal}, [[improper_harmonic]{.doc}]improper_harmonic.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

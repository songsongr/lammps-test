::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#angle-style-mwlc-command .section}
[]{#index-0}

# angle_style mwlc command[](#angle-style-mwlc-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style mwlc
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style mwlc
    angle_coeff * 25 1 10 1
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4Feb2025.]{.versionmodified .added}
:::

The *mwlc* angle style models a meltable wormlike chain and can be used to model non-linear bending elasticity of polymers, e.g. DNA. *mwlc* uses a potential that is a canonical-ensemble superposition of a non-melted and a melted state [[(Farrell)]{.std .std-ref}](#farrell){.reference .internal}. The potential is

::: {.math .notranslate .nohighlight}
\\\[E = -k\_{B}T\\,\\log \[q + q\^{m}\] + E\_{0},\\\]
:::

where the non-melted and melted partition functions are

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}q = \\exp \[-k\_{1}(1+\\cos{\\theta})/k\_{B}T\]; \\\\ q\^{m} = \\exp \[-(\\mu+k\_{2}(1+\\cos{\\theta}))/k\_{B}T\].\\end{split}\\\]
:::

[\\(k_1\\)]{.math .notranslate .nohighlight} is the bending elastic constant of the non-melted state, [\\(k_2\\)]{.math .notranslate .nohighlight} is the bending elastic constant of the melted state, [\\(\\mu\\)]{.math .notranslate .nohighlight} is the melting energy, and [\\(T\\)]{.math .notranslate .nohighlight} is the reference temperature. The reference energy,

::: {.math .notranslate .nohighlight}
\\\[E\_{0} = -k\_{B}T\\,\\log \[1 + \\exp\[-\\mu/k\_{B}T\]\],\\\]
:::

ensures that E is zero for a fully extended chain.

This potential is a continuous version of the two-state potential introduced by [[(Yan)]{.std .std-ref}](#yan){.reference .internal}.

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(k_1\\)]{.math .notranslate .nohighlight} (energy)

- [\\(k_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\mu\\)]{.math .notranslate .nohighlight} (energy)

- [\\(T\\)]{.math .notranslate .nohighlight} (temperature)
:::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This angle style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Farrell)** [Farrell, Dobnikar, Podgornik, Curk, Phys Rev Lett, 133, 148101 (2024).](https://doi.org/10.1103/PhysRevLett.133.148101){.reference .external}

**(Yan)** [Yan, Marko, Phys Rev Lett, 93, 108108 (2004).](https://doi.org/10.1103/PhysRevLett.93.108108){.reference .external}
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

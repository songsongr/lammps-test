::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#improper-style-inversion-harmonic-command .section}
[]{#index-0}

# improper_style inversion/harmonic command[](#improper-style-inversion-harmonic-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style inversion/harmonic
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style inversion/harmonic
    improper_coeff 1 18.776340 0.000000
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *inversion/harmonic* improper style follows the Wilson-Decius out-of-plane angle definition and uses an harmonic potential:

::: {.math .notranslate .nohighlight}
\\\[E = K \\left(\\omega - \\omega_0\\right)\^2\\\]
:::

where [\\(K\\)]{.math .notranslate .nohighlight} is the force constant and [\\(\\omega\\)]{.math .notranslate .nohighlight} is the angle evaluated for all three axis-plane combinations centered around the atom I. For the IL axis and the IJK plane [\\(\\omega\\)]{.math .notranslate .nohighlight} looks as follows:

![](_images/umbrella.jpg){.align-center}

Note that the *inversion/harmonic* angle term evaluation differs to the [[improper_umbrella]{.doc}]improper_umbrella.md){.reference .internal} due to the cyclic evaluation of all possible angles [\\(\\omega\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each improper type via the [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\omega_0\\)]{.math .notranslate .nohighlight} (degrees)

If [\\(\\omega_0 = 0\\)]{.math .notranslate .nohighlight} the potential term has a single minimum for the planar structure. Otherwise it has two minima at +/- [\\(\\omega_0\\)]{.math .notranslate .nohighlight}, with a barrier in between.
::::

------------------------------------------------------------------------

::: {#symmetry-convention .section}
## Symmetry convention[](#symmetry-convention "Link to this heading"){.headerlink}

For the *inversion/harmonic* improper style, the first atom in the quadruplet is the atom of symmetry; all other atoms are considered interchangeable. This convention is relevant for operations that require knowledge of how atoms are ordered, such as automatic assignment of new improper types by [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This improper style can only be used if LAMMPS was built with the MOFFF package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[improper_coeff]{.doc}]improper_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

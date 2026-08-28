::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#improper-style-distance-command .section}
[]{#index-0}

# improper_style distance command[](#improper-style-distance-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style distance
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style distance
    improper_coeff 1 80.0 100.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *distance* improper style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = K_2 d\^2 + K_4 d\^4\\\]
:::

where [\\(d\\)]{.math .notranslate .nohighlight} is the distance between the central atom and the plane formed by the other three atoms. If the 4 atoms in an improper quadruplet (listed in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command) are ordered I,J,K,L then the I-atom is assumed to be the central atom.

![](_images/improper_distance.jpg){.align-center}

Note that defining 4 atoms to interact in this way, does not mean that bonds necessarily exist between I-J, J-K, or K-L, as they would in a linear dihedral. Normally, the bonds I-J, I-K, I-L would exist for an improper to be defined between the 4 atoms.

The following coefficients must be defined for each improper type via the improper_coeff command as in the example above, or in the data file or restart files read by the read_data or read_restart commands:

- [\\(K_2\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(K_4\\)]{.math .notranslate .nohighlight} (energy/distance\^4)
::::

------------------------------------------------------------------------

::: {#symmetry-convention .section}
## Symmetry convention[](#symmetry-convention "Link to this heading"){.headerlink}

For the *distance* improper style, the first atom in the quadruplet is the atom of symmetry; all other atoms are considered interchangeable. This convention is relevant for operations that require knowledge of how atoms are ordered, such as automatic assignment of new improper types by [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This improper style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
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

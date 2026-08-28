::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#dihedral-style-cosine-squared-restricted-command .section}
[]{#index-0}

# dihedral_style cosine/squared/restricted command[](#dihedral-style-cosine-squared-restricted-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style cosine/squared/restricted
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style cosine/squared/restricted
    dihedral_coeff 1 10.0 120
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 17Apr2024.]{.versionmodified .added}
:::

The *cosine/squared/restricted* dihedral style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = K \[\\cos(\\phi) - \\cos(\\phi_0)\]\^2 / \\sin\^2(\\phi)\\\]
:::

, which is commonly used in the MARTINI force field.

See [[(Bulacu)]{.std .std-ref}](#restricted-bul){.reference .internal} for a description of the restricted dihedral for the MARTINI force field.

The following coefficients must be defined for each dihedral type via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\phi_0\\)]{.math .notranslate .nohighlight} (degrees)

[\\(\\phi_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally.
:::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This dihedral style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Bulacu)** Bulacu, Goga, Zhao, Rossi, Monticelli, Periole, Tieleman, Marrink, J Chem Theory Comput, 9, 3282-3292 (2013).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

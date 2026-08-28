:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#pair-style-list-command .section}
[]{#index-0}

# pair_style list command[](#pair-style-list-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style list listfile cutoff keyword
:::
::::

- listfile = name of file with list of pairwise interactions

- cutoff = global cutoff (distance units)

- keyword = optional flag *nocheck* or *check* (default is *check*)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style list restraints.txt 200.0
    pair_coeff * *

    pair_style hybrid/overlay lj/cut 1.1225 list pair_list.txt 300.0
    pair_coeff * * lj/cut 1.0 1.0
    pair_coeff 3* 3* list
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *list* computes interactions between explicitly listed pairs of atoms with the option to select functional form and parameters for each individual pair. Because the parameters are set in the list file, the pair_coeff command has no parameters (but still needs to be provided). The *check* and *nocheck* keywords enable/disable tests that checks whether all listed pairs of atom IDs were present and the interactions computed. If *nocheck* is set and either atom ID is not present, the interaction is skipped.

This pair style can be thought of as a hybrid between bonded, non-bonded, and restraint interactions. It will typically be used as an additional interaction within the *hybrid/overlay* pair style. It currently supports three interaction styles: a 12-6 Lennard-Jones, a Morse and a harmonic potential.

The format of the list file is as follows:

- one line per pair of atoms

- empty lines will be ignored

- comment text starts with a '#' character

- line syntax: *ID1 ID2 style coeffs cutoff*

  :::: {.highlight-none .notranslate}
  ::: highlight
      ID1 = atom ID of first atom
      ID2 = atom ID of second atom
      style = style of interaction
      coeffs = list of coeffs
      cutoff = cutoff for interaction (optional)
  :::
  ::::

The cutoff parameter is optional for all but the *quartic* interactions. If it is not specified, the global cutoff is used.

Here is an example file:

:::: {.highlight-none .notranslate}
::: highlight
    # this is a comment

    15 259 lj126     1.0 1.0      50.0
    15 603 morse    10.0 1.2 2.0  10.0 # and another comment
    18 470 harmonic 50.0 1.2       5.0
    19 332 quartic  10.0 5.0 -1.2 1.2
:::
::::

The style *lj126* computes pairwise interactions with the formula

::: {.math .notranslate .nohighlight}
\\\[E = 4 \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - \\left(\\frac{\\sigma}{r}\\right)\^6 \\right\] \\qquad r \< r_c\\\]
:::

and the coefficients:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

The style *morse* computes pairwise interactions with the formula

::: {.math .notranslate .nohighlight}
\\\[E = D_0 \\left\[ 1 - e\^{-\\alpha (r - r_0)} \\right\]\^2 \\qquad r \< r_c\\\]
:::

and the coefficients:

- [\\(D_0\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (1/distance units)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance units)

The style *harmonic* computes pairwise interactions with the formula

::: {.math .notranslate .nohighlight}
\\\[E = K (r - r_0)\^2 \\qquad r \< r_c\\\]
:::

and the coefficients:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance units)

Note that the usual 1/2 factor is included in [\\(K\\)]{.math .notranslate .nohighlight}.

The style *quartic* computes pairwise interactions with the formula

::: {.math .notranslate .nohighlight}
\\\[E = K (r - r_0)\^2 (r - r_0 -b_1) (r - r_0 - b_2) \\qquad r \< r_c\\\]
:::

and the coefficients:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(b_1\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(b_2\\)]{.math .notranslate .nohighlight} (distance units)
:::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support mixing since all parameters are explicit for each pair.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option is supported by this pair style.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table and tail options are not relevant for this pair style.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style does not use a neighbor list and instead identifies atoms by their IDs. This has two consequences: 1) The cutoff has to be chosen sufficiently large, so that the second atom of a pair has to be a ghost atom on the same node on which the first atom is local; otherwise the interaction will be skipped. You can use the *check* option to detect, if interactions are missing. 2) Unlike other pair styles in LAMMPS, an atom I will not interact with multiple images of atom J (assuming the images are within the cutoff distance), but only with the closest image.

This style is part of the MISC package. It is only enabled if LAMMPS is build with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page on for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, [[pair_style lj/cut]{.doc}]pair_lj.md){.reference .internal}, [[bond_style morse]{.doc}]bond_morse.md){.reference .internal}, [[bond_style harmonic]{.doc}]bond_harmonic.md){.reference .internal} [[bond_style quartic]{.doc}]bond_quartic.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

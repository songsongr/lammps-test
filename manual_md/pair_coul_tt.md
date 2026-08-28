::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#pair-style-coul-tt-command .section}
[]{#index-0}

# pair_style coul/tt command[](#pair-style-coul-tt-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *coul/tt*

- args = list of arguments for a particular style

``` literal-block
coul/tt args = n cutoff
  n = degree of polynomial
  cutoff = global cutoff (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay ... coul/tt 4 12.0
    pair_coeff 1 2  coul/tt 4.5 1.0
    pair_coeff 1 2  coul/tt 4.0 1.0 4 12.0
    pair_coeff 1 3* coul/tt 4.5 1.0 4
:::
::::

Example input scripts available: examples/PACKAGES/drude
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *coul/tt* pair style is meant to be used with force fields that include explicit polarization through Drude dipoles.

The *coul/tt* pair style should be used as a sub-style within in the [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} command, in conjunction with a main pair style including Coulomb interactions and *thole* pair style, or with *lj/cut/thole/long* pair style that is equivalent to the combination of preceding two.

The *coul/tt* pair styles compute the charge-dipole Coulomb interaction damped at short distances by a function

::: {.math .notranslate .nohighlight}
\\\[f\_{n,ij}(r) = 1 - c\_{ij} \\cdot e\^{-b\_{ij} r} \\sum\_{k=0}\^n \\frac{(b\_{ij} r)\^k}{k!}\\\]
:::

This function results from an adaptation to the Coulomb interaction [[(Salanne)]{.std .std-ref}](#salanne1){.reference .internal} of the damping function originally proposed by [[Tang Toennies]{.std .std-ref}](#tangtoennies1){.reference .internal} for van der Waals interactions.

The polynomial takes the degree 4 for damping the Coulomb interaction. The parameters [\\(b\_{ij}\\)]{.math .notranslate .nohighlight} and [\\(c\_{ij}\\)]{.math .notranslate .nohighlight} could be determined from first-principle calculations for small, mainly mono-atomic, ions [[(Salanne)]{.std .std-ref}](#salanne1){.reference .internal}, or else treated as empirical for large molecules.

In pair styles with Drude induced dipoles, this damping function is typically applied to the interactions between a Drude charge (either [\\(q\_{D,i}\\)]{.math .notranslate .nohighlight} on a Drude particle or [\\(-q\_{D,i}\\)]{.math .notranslate .nohighlight} on the respective Drude core)) and a charge on a non-polarizable atom, [\\(q\_{j}\\)]{.math .notranslate .nohighlight}.

The Tang-Toennies function could also be used to damp electrostatic interactions between the (non-polarizable part of the) charge of a core, [\\(q\_{i}-q\_{D,i}\\)]{.math .notranslate .nohighlight}, and the Drude charge of another, [\\(-q\_{D,j}\\)]{.math .notranslate .nohighlight}. The [\\(b\_{ij}\\)]{.math .notranslate .nohighlight} and [\\(c\_{ij}\\)]{.math .notranslate .nohighlight} are equal to [\\(b\_{ji}\\)]{.math .notranslate .nohighlight} and [\\(c\_{ji}\\)]{.math .notranslate .nohighlight} in the case of core-core interactions.

For pair_style *coul/tt*, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the example above.

- [\\(b\_{ij}\\)]{.math .notranslate .nohighlight}

- [\\(c\_{ij}\\)]{.math .notranslate .nohighlight}

- degree of polynomial (positive integer)

- cutoff (distance units)

The last two coefficients are optional. If not specified the global degree of the polynomial or the global cutoff specified in the pair_style command are used. In order to specify a cutoff (forth argument), the degree of the polynomial (third argument) must also be specified.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

The *coul/tt* pair style does not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the DRUDE package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair_style should currently not be used with the [[charmm dihedral style]{.doc}]dihedral_charmm.md){.reference .internal} if the latter has non-zero 1-4 weighting factors. This is because the *coul/tt* pair style does not know which pairs are 1-4 partners of which dihedrals.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix drude]{.doc}]fix_drude.md){.reference .internal}, [[fix langevin/drude]{.doc}]fix_langevin_drude.md){.reference .internal}, [[fix drude/transform]{.doc}]fix_drude_transform.md){.reference .internal}, [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal}, [[pair_style thole]{.doc}]pair_thole.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Thole)** Chem Phys, 59, 341 (1981).

**(Salanne)** Salanne, Rotenberg, Jahn, Vuilleumier, Simon, Christian and Madden, Theor Chem Acc, 131, 1143 (2012).

**(Tang and Toennies)** J Chem Phys, 80, 3726 (1984).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

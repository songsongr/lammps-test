:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#pair-style-spin-neel-command .section}
[]{#index-0}

# pair_style spin/neel command[](#pair-style-spin-neel-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/neel cutoff
:::
::::

- cutoff = global cutoff pair (distance in metal units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/neel 4.0
    pair_coeff * * neel 4.0 0.0048 0.234 1.168 2.6905 0.705 0.652
    pair_coeff 1 2 neel 4.0 0.0048 0.234 1.168 0.0 0.0 1.0
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *spin/neel* computes the Neel pair anisotropy model between pairs of magnetic spins:

::: {.math .notranslate .nohighlight}
\\\[\\mathcal{H}\_{N\\acute{e}el}=-\\sum\_{{ i,j=1,i\\neq j}}\^N g_1(r\_{ij})\\left(({\\mathbf{e}}\_{ij}\\cdot {\\mathbf{s}}\_{i})({\\mathbf{e}}\_{ij} \\cdot {\\mathbf{s}}\_{j})-\\frac{{\\mathbf{s}}\_{i}\\cdot{\\mathbf{s}}\_{j}}{3} \\right) +q_1(r\_{ij})\\left( ({\\mathbf{e}}\_{ij}\\cdot {\\mathbf{s}}\_{i})\^2 -\\frac{{\\mathbf{s}}\_{i}\\cdot{\\mathbf{s}}\_{j}}{3}\\right) \\left( ({\\mathbf{e}}\_{ij}\\cdot {\\mathbf{s}}\_{i})\^2 -\\frac{{\\mathbf{s}}\_{i}\\cdot{\\mathbf{s}}\_{j}}{3} \\right) + q_2(r\_{ij}) \\Big( ({\\mathbf{e}}\_{ij}\\cdot {\\mathbf{s}}\_{i}) ({\\mathbf{e}}\_{ij}\\cdot {\\mathbf{s}}\_{j})\^3 + ({\\mathbf{e}}\_{ij}\\cdot {\\mathbf{s}}\_{j}) ({\\mathbf{e}}\_{ij}\\cdot {\\mathbf{s}}\_{i})\^3\\Big)\\\]
:::

where [\\(\\mathbf{s}\_i\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{s}\_j\\)]{.math .notranslate .nohighlight} are two neighboring magnetic spins of two particles, [\\(r\_{ij} = \\vert \\mathbf{r}\_i - \\mathbf{r}\_j \\vert\\)]{.math .notranslate .nohighlight} is the inter-atomic distance between the two particles, [\\(\\mathbf{e}\_{ij} = \\frac{\\mathbf{r}\_i - \\mathbf{r}\_j}{\\vert \\mathbf{r}\_i - \\mathbf{r}\_j\\vert}\\)]{.math .notranslate .nohighlight} is their normalized separation vector and [\\(g_1\\)]{.math .notranslate .nohighlight}, [\\(q_1\\)]{.math .notranslate .nohighlight} and [\\(q_2\\)]{.math .notranslate .nohighlight} are three functions defining the intensity of the dipolar and quadrupolar contributions, with:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}g_1(r\_{ij}) &= g(r\_{ij}) + \\frac{12}{35} q(r\_{ij}) \\\\ q_1(r\_{ij}) &= \\frac{9}{5} q(r\_{ij}) \\\\ q_2(r\_{ij}) &= - \\frac{2}{5} q(r\_{ij})\\end{split}\\\]
:::

With the functions [\\(g(r\_{ij})\\)]{.math .notranslate .nohighlight} and [\\(q(r\_{ij})\\)]{.math .notranslate .nohighlight} defined and fitted according to the same Bethe-Slater function used to fit the exchange interaction:

::: {.math .notranslate .nohighlight}
\\\[{J}\\left( r\_{ij} \\right) = 4 a \\left( \\frac{r\_{ij}}{d} \\right)\^2 \\left( 1 - b \\left( \\frac{r\_{ij}}{d} \\right)\^2 \\right) e\^{-\\left( \\frac{r\_{ij}}{d} \\right)\^2 }\\Theta (R_c - r\_{ij})\\\]
:::

where [\\(a\\)]{.math .notranslate .nohighlight}, [\\(b\\)]{.math .notranslate .nohighlight} and [\\(d\\)]{.math .notranslate .nohighlight} are the three constant coefficients defined in the associated "pair_coeff" command.

The coefficients [\\(a\\)]{.math .notranslate .nohighlight}, [\\(b\\)]{.math .notranslate .nohighlight}, and [\\(d\\)]{.math .notranslate .nohighlight} need to be fitted so that the function above matches with the values of the magneto-elastic constant of the materials at stake.

Examples and more explanations about this function and its parameterization are reported in [[(Tranchida)]{.std .std-ref}](#tranchida6){.reference .internal}. More examples of parameterization will be provided in future work.

From this DM interaction, each spin [\\(i\\)]{.math .notranslate .nohighlight} will be submitted to a magnetic torque [\\(\\mathbf{\\omega}\\)]{.math .notranslate .nohighlight} and its associated atom to a force [\\(\\mathbf{F}\\)]{.math .notranslate .nohighlight} (for spin-lattice calculations only).

More details about the derivation of these torques/forces are reported in [[(Tranchida)]{.std .std-ref}](#tranchida6){.reference .internal}.
::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

All the *pair/spin* styles are part of the SPIN package. These styles are only enabled if LAMMPS was built with this package, and if the atom_style "spin" was declared. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[atom_style spin]{.doc}]atom_style.md){.reference .internal}, [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_eam]{.doc}]pair_eam.md){.reference .internal},
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Tranchida)** Tranchida, Plimpton, Thibaudeau and Thompson, Journal of Computational Physics, 372, 406-425, (2018).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

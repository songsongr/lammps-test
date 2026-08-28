::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-spin-dipole-cut-command .section}
[]{#index-1}[]{#index-0}

# pair_style spin/dipole/cut command[](#pair-style-spin-dipole-cut-command "Link to this heading"){.headerlink}
:::

:::::::::::::: {#pair-style-spin-dipole-long-command .section}
# pair_style spin/dipole/long command[](#pair-style-spin-dipole-long-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/dipole/cut cutoff
    pair_style spin/dipole/long cutoff
:::
::::

- cutoff = global cutoff for magnetic dipole energy and forces (optional) (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style spin/dipole/cut 10.0
    pair_coeff * * 10.0
    pair_coeff 2 3 8.0

    pair_style spin/dipole/long 9.0
    pair_coeff * * 10.0
    pair_coeff 2 3 6.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *spin/dipole/cut* computes a short-range dipole-dipole interaction between pairs of magnetic particles that each have a magnetic spin. The magnetic dipole-dipole interactions are computed by the following formulas for the magnetic energy, magnetic precession vector omega and mechanical force between particles I and J.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathcal{H}\_\\mathrm{long} & = -\\frac{\\mu\_{0} \\left( \\mu_B\\right)\^2}{4\\pi} \\sum\_{i,j,i\\neq j}\^{N} \\frac{g_i g_j}{r\_{ij}\^3} \\biggl(3 \\left(\\vec{e}\_{ij}\\cdot \\vec{s}\_{i}\\right) \\left(\\vec{e}\_{ij}\\cdot \\vec{s}\_{j}\\right) -\\vec{s}\_i\\cdot\\vec{s}\_j \\biggr) \\\\ \\mathbf{\\omega}\_i & = \\frac{\\mu_0 (\\mu_B)\^2}{4\\pi\\hbar}\\sum\_{j} \\frac{g_i g_j}{r\_{ij}\^3} \\, \\biggl( 3\\,(\\vec{e}\_{ij}\\cdot\\vec{s}\_{j})\\vec{e}\_{ij} -\\vec{s}\_{j} \\biggr) \\\\ \\mathbf{F}\_i & = \\frac{3\\, \\mu_0 (\\mu_B)\^2}{4\\pi} \\sum_j \\frac{g_i g_j}{r\_{ij}\^4} \\biggl\[\\bigl( (\\vec{s}\_i\\cdot\\vec{s}\_j) -5(\\vec{e}\_{ij}\\cdot\\vec{s}\_i) (\\vec{e}\_{ij}\\cdot\\vec{s}\_j)\\bigr) \\vec{e}\_{ij}+ \\bigl( (\\vec{e}\_{ij}\\cdot\\vec{s}\_i)\\vec{s}\_j+ (\\vec{e}\_{ij}\\cdot\\vec{s}\_j)\\vec{s}\_i \\bigr) \\biggr\]\\end{split}\\\]
:::

where [\\(\\vec{s}\_i\\)]{.math .notranslate .nohighlight} and [\\(\\vec{s}\_j\\)]{.math .notranslate .nohighlight} are the spin on two magnetic particles, r is their separation distance, and the vector [\\(\\vec{e}\_{ij} = \\frac{r_i - r_j}{\\left\| r_i - r_j \\right\|}\\)]{.math .notranslate .nohighlight} is the direction vector between the two particles.

Style *spin/dipole/long* computes long-range magnetic dipole-dipole interaction. A [[kspace_style]{.doc}]kspace_style.md){.reference .internal} must be defined to use this pair style. Currently, [[kspace_style ewald/dipole/spin]{.doc}]kspace_style.md){.reference .internal} and [[kspace_style pppm/dipole/spin]{.doc}]kspace_style.md){.reference .internal} support long-range magnetic dipole-dipole interactions.

------------------------------------------------------------------------

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *spin/dipole/cut* and *spin/dipole/long* styles are part of the SPIN package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Using dipole/spin pair styles with *electron* [[units]{.doc}]units.md){.reference .internal} is not currently supported.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[kspace_style]{.doc}]kspace_style.md){.reference .internal} [[fix nve/spin]{.doc}]fix_nve_spin.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
::::::::::::::::
:::::::::::::::::

::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#pair-style-wf-cut-command .section}
[]{#index-0}

# pair_style wf/cut command[](#pair-style-wf-cut-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style wf/cut cutoff
:::
::::

- cutoff = cutoff for wf interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style        wf/cut 2.0
    pair_coeff        1 1 1.0 1.0 1 1  2.0
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *wf/cut* (Wang-Frenkel) style computes LJ-like potentials as described in [[Wang2020]{.std .std-ref}](#wang2020){.reference .internal}. This potential is by construction finite ranged and it vanishes quadratically at the cutoff distance, avoiding truncation, shifting, interpolation and other typical procedures with the LJ potential. The *wf/cut* can be used when a typical short-ranged potential with attraction is required. The potential is given by which is given by:

::: {.math .notranslate .nohighlight}
\\\[\\phi(r)= \\epsilon \\alpha \\left(\\left\[{\\sigma\\over r}\\right\]\^{2\\mu} -1 \\right)\\left(\\left\[{r_c\\over r}\\right\]\^{2\\mu}-1\\right)\^{2\\nu}\\\]
:::

with

::: {.math .notranslate .nohighlight}
\\\[\\alpha=2\\nu\\left(\\frac{r_c}{\\sigma}\\right)\^{2\\mu}\\left\[\\frac{1+2\\nu}{2\\nu\\left\[(r_c/\\sigma)\^{2\\mu}-1\\right\]}\\right\]\^{2\\nu+1}\\\]
:::

and

::: {.math .notranslate .nohighlight}
\\\[r\_{min}=r_c\\left\[\\frac{1+2\\nu}{1+2\\nu(r_c/\\sigma)\^{2\\nu}}\\right\]\^{1/{2\\mu}}\\\]
:::

[\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff.

Comparison of the non-truncated Lennard-Jones 12-6 potential (red curve), and the WF potentials with [\\(\\mu=1\\)]{.math .notranslate .nohighlight} and [\\(\\nu=1\\)]{.math .notranslate .nohighlight} are shown in the figure below. The blue curve has [\\(r_c =2.0\\)]{.math .notranslate .nohighlight} and the green curve has [\\(r_c =1.2\\)]{.math .notranslate .nohighlight} and can be used to describe colloidal interactions.

[![](_images/WF_LJ.jpg){.align-center style="width: 326.04px; height: 246.51000000000002px;"}](_images/WF_LJ.jpg){.reference .internal .image-reference}

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(\\nu\\)]{.math .notranslate .nohighlight}

- [\\(\\mu\\)]{.math .notranslate .nohighlight}

- [\\(r_c\\)]{.math .notranslate .nohighlight} (distance units)

The last coefficient is optional. If not specified, the global cutoff given in the pair_style command is used. The exponents [\\(\\nu\\)]{.math .notranslate .nohighlight} and [\\(\\mu\\)]{.math .notranslate .nohighlight} are positive integers, usually set to 1. There is usually little to be gained by choosing other values of [\\(\\nu\\)]{.math .notranslate .nohighlight} and [\\(\\mu\\)]{.math .notranslate .nohighlight} (See discussion in [[Wang2020]{.std .std-ref}](#wang2020){.reference .internal})

------------------------------------------------------------------------

**Mixing, shift, table, tail correction, restart, rRESPA info**:

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} mixing and table options.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail and shift options are not relevant for this pair style as it goes to zero at the cut-off radius.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style does not support the use of the *inner*, *middle*, and *outer* keywords of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command.
::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style can only be used if LAMMPS was built with the EXTRA-PAIR package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}

**Default:** none

------------------------------------------------------------------------

**(Wang2020)** X. Wang, S. Ramirez-Hinestrosa, J. Dobnikar, and D. Frenkel, Phys. Chem. Chem. Phys. 22, 10624 (2020).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

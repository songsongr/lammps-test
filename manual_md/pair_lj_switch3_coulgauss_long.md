::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-lj-switch3-coulgauss-long-command .section}
[]{#index-1}[]{#index-0}

# pair_style lj/switch3/coulgauss/long command[](#pair-style-lj-switch3-coulgauss-long-command "Link to this heading"){.headerlink}
:::

:::::::::::::::::: {#pair-style-mm3-switch3-coulgauss-long-command .section}
# pair_style mm3/switch3/coulgauss/long command[](#pair-style-mm3-switch3-coulgauss-long-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *lj/switch3/coulgauss/long* or *mm3/switch3/coulgauss/long*

- args = list of arguments for a particular style

``` literal-block
lj/switch3/coulgauss/long args = cutoff (cutoff2) width
  cutoff  = global cutoff for LJ (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
  width  = width parameter of the smoothing function (distance units)

mm3/switch3/coulgauss/long args = cutoff (cutoff2) width
  cutoff  = global cutoff for MM3 (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
  width  = width parameter of the smoothing function (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/switch3/coulgauss/long    12.0 3.0
    pair_coeff 1  0.2 2.5 1.2

    pair_style lj/switch3/coulgauss/long   12.0 10.0 3.0
    pair_coeff 1  0.2 2.5 1.2

    pair_style mm3/switch3/coulgauss/long    12.0 3.0
    pair_coeff 1  0.2 2.5 1.2

    pair_style mm3/switch3/coulgauss/long   12.0 10.0 3.0
    pair_coeff 1  0.2 2.5 1.2
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *lj/switch3/coulgauss* style evaluates the LJ vdW potential

::: {.math .notranslate .nohighlight}
\\\[E = 4\\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12}-\\left(\\frac{\\sigma}{r}\\right)\^{6} \\right\]\\\]
:::

The *mm3/switch3/coulgauss/long* style evaluates the MM3 vdW potential [[(Allinger)]{.std .std-ref}]bond_mm3.md#mm3-allinger1989){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = \\epsilon\_{ij} \\left\[ -2.25 \\left(\\frac{r\_{v,ij}}{r\_{ij}}\\right)\^6 + 1.84(10)\^5 \\exp\\left\[-12.0 r\_{ij}/r\_{v,ij}\\right\] \\right\] S_3(r\_{ij}) \\\\ r\_{v,ij} & = r\_{v,i} + r\_{v,j} \\\\ \\epsilon\_{ij} & = \\sqrt{\\epsilon_i \\epsilon_j}\\end{split}\\\]
:::

Both potentials go smoothly to zero at the cutoff r_c as defined by the switching function

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}S_3(r) = \\left\\lbrace \\begin{array}{ll} 1 & \\quad\\mathrm{if}\\quad r \< r\_\\mathrm{c} - w \\\\ 3x\^2 - 2x\^3 & \\quad\\mathrm{if}\\quad r \< r\_\\mathrm{c} \\quad\\mathrm{with\\quad} x=\\frac{r\_\\mathrm{c} - r}{w} \\\\ 0 & \\quad\\mathrm{if}\\quad r \>= r\_\\mathrm{c} \\end{array} \\right.\\end{split}\\\]
:::

where w is the width defined in the arguments. This potential is combined with Coulomb interaction between Gaussian charge densities:

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{q_i q_j \\mathrm{erf}\\left( r/\\sqrt{\\gamma_1\^2+\\gamma_2\^2} \\right) }{\\epsilon r\_{ij}}\\\]
:::

where [\\(q_i\\)]{.math .notranslate .nohighlight} and [\\(q_j\\)]{.math .notranslate .nohighlight} are the charges on the two atoms, [\\(\\epsilon\\)]{.math .notranslate .nohighlight} is the dielectric constant which can be set by the [[dielectric]{.doc}]dielectric.md){.reference .internal} command, [\\(\\gamma_i\\)]{.math .notranslate .nohighlight} and [\\(\\gamma_j\\)]{.math .notranslate .nohighlight} are the widths of the Gaussian charge distribution and erf() is the error-function. This style has to be used in conjunction with the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command

If one cutoff is specified it is used for both the vdW and Coulomb terms. If two cutoffs are specified, the first is used as the cutoff for the vdW terms, and the second is the cutoff for the Coulombic term.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (distance)
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon and sigma coefficients and cutoff distance for all of the lj/long pair styles can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

Shifting the potential energy is not necessary because the switching function ensures that the potential is zero at the cut-off.

These pair styles support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table and options since they can tabulate the short-range portion of the long-range Coulombic interactions.

Thes pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding a long-range tail correction to the Lennard-Jones portion of the energy and pressure.

These pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These styles are part of the YAFF package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

:::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-lj-mdf-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style lj/mdf command[](#pair-style-lj-mdf-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-buck-mdf-command .section}
# pair_style buck/mdf command[](#pair-style-buck-mdf-command "Link to this heading"){.headerlink}
:::

:::::::::::::::::::: {#pair-style-lennard-mdf-command .section}
# pair_style lennard/mdf command[](#pair-style-lennard-mdf-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *lj/mdf* or *buck/mdf* or *lennard/mdf*

- args = list of arguments for a particular style

  ``` literal-block
  lj/mdf args = cutoff1 cutoff2
    cutoff1 = inner cutoff for the start of the tapering function
    cutoff1 = out cutoff for the end of the tapering function
  buck/mdf args = cutoff1 cutoff2
    cutoff1 = inner cutoff for the start of the tapering function
    cutoff1 = out cutoff for the end of the tapering function
  lennard/mdf args = cutoff1 cutoff2
    cutoff1 = inner cutoff for the start of the tapering function
    cutoff1 = out cutoff for the end of the tapering function
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/mdf 2.5 3.0
    pair_coeff * * 1.0 1.0
    pair_coeff 1 1 1.1 2.8 3.0 3.2

    pair_style buck/mdf 2.5 3.0
    pair_coeff * * 100.0 1.5 200.0
    pair_coeff * * 100.0 1.5 200.0 3.0 3.5

    pair_style lennard/mdf 2.5 3.0
    pair_coeff * * 1.0 1.0
    pair_coeff 1 1 1021760.3664 2120.317338 3.0 3.2
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *lj/mdf*, *buck/mdf* and *lennard/mdf* compute the standard 12-6 Lennard-Jones and Buckingham potential with the addition of a taper function that ramps the energy and force smoothly to zero between an inner and outer cutoff.

::: {.math .notranslate .nohighlight}
\\\[E\_{smooth}(r) = E(r)\*f(r)\\\]
:::

The tapering, *f(r)*, is done by using the Mei, Davenport, Fernando function [[(Mei)]{.std .std-ref}](#mei){.reference .internal}.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}f(r) & = 1.0 \\qquad \\qquad \\mathrm{for} \\qquad r \< r_m \\\\ f(r) & = (1 - x)\^3\*(1+3x+6x\^2) \\quad \\mathrm{for} \\qquad r_m \< r \< r\_{cut} \\\\ f(r) & = 0.0 \\qquad \\qquad \\mathrm{for} \\qquad r \>= r\_{cut} \\\\\\end{split}\\\]
:::

where

::: {.math .notranslate .nohighlight}
\\\[x = \\frac{(r-r_m)}{(r\_{cut}-r_m)}\\\]
:::

Here [\\(r_m\\)]{.math .notranslate .nohighlight} is the inner cutoff radius and [\\(r\_{cut}\\)]{.math .notranslate .nohighlight} is the outer cutoff radius.

------------------------------------------------------------------------

For the *lj/mdf* pair_style, the potential energy, *E(r)*, is the standard 12-6 Lennard-Jones written in the epsilon/sigma form:

::: {.math .notranslate .nohighlight}
\\\[E(r) = 4 \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - \\left(\\frac{\\sigma}{r}\\right)\^6 \\right\]\\\]
:::

Either the first two or all of the following coefficients must be defined for each pair of atoms types via the pair_coeff command as in the examples above, or in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal}. The two cutoffs default to the global values and [\\(\\epsilon\\)]{.math .notranslate .nohighlight} and [\\(\\sigma\\)]{.math .notranslate .nohighlight} can also be determined by mixing as described below:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(r_m\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(r\_{cut}\\)]{.math .notranslate .nohighlight} (distance units)

------------------------------------------------------------------------

For the *buck/mdf* pair_style, the potential energy, *E(r)*, is the standard Buckingham potential with three required coefficients. The two cutoffs can be omitted and default to the corresponding global values:

::: {.math .notranslate .nohighlight}
\\\[E(r) = A e\^{(-r/\\rho)} -\\frac{C}{r\^6}\\\]
:::

- *A* (energy units)

- [\\(\\rho\\)]{.math .notranslate .nohighlight} (distance units)

- *C* (energy-distance\^6 units)

- [\\(r_m\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(r\_{cut}\\)]{.math .notranslate .nohighlight} (distance units)

------------------------------------------------------------------------

For the *lennard/mdf* pair_style, the potential energy, *E(r)*, is the standard 12-6 Lennard-Jones written in the A/B form:

::: {.math .notranslate .nohighlight}
\\\[E(r) = \\frac{A}{r\^{12}} - \\frac{B}{r\^{6}}\\\]
:::

The following coefficients must be defined for each pair of atoms types via the pair_coeff command as in the examples above, or in the data file read by the read_data commands, or by mixing as described below. The two cutoffs default to their global values and must be either both given or both left out:

- *A* (energy-distance\^12 units)

- *B* (energy-distance\^6 units)

- [\\(r_m\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(r\_{cut}\\)]{.math .notranslate .nohighlight} (distance units)
:::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the [\\(\\epsilon\\)]{.math .notranslate .nohighlight} and [\\(\\sigma\\)]{.math .notranslate .nohighlight} coefficients and cutoff distances for the lj/mdf pair style can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details. The other two pair styles buck/mdf and lennard/mdf do not support mixing, so all I,J pairs of coefficients must be specified explicitly.

None of the lj/mdf, buck/mdf, or lennard/mdf pair styles supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option or long-range tail corrections to pressure and energy.

These styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles can only be used if LAMMPS was built with the EXTRA-PAIR package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Mei)** Mei, Davenport, Fernando, Phys Rev B, 43 4653 (1991)
:::
::::::::::::::::::::
:::::::::::::::::::::::
::::::::::::::::::::::::

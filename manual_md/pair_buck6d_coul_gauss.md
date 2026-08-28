::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-buck6d-coul-gauss-dsf-command .section}
[]{#index-1}[]{#index-0}

# pair_style buck6d/coul/gauss/dsf command[](#pair-style-buck6d-coul-gauss-dsf-command "Link to this heading"){.headerlink}
:::

:::::::::::::::: {#pair-style-buck6d-coul-gauss-long-command .section}
# pair_style buck6d/coul/gauss/long command[](#pair-style-buck6d-coul-gauss-long-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *buck6d/coul/gauss/dsf* or *buck6d/coul/gauss/long*

- args = list of arguments for a particular style

``` literal-block
buck6d/coul/gauss/dsf args = smooth cutoff (cutoff2)
  smooth  = smoothing onset within Buckingham cutoff (ratio)
  cutoff  = global cutoff for Buckingham (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
buck6d/coul/gauss/long args = smooth smooth2 cutoff (cutoff2)
  smooth   = smoothing onset within Buckingham cutoff (ratio)
  smooth2  = smoothing onset within Coulombic cutoff (ratio)
  cutoff   = global cutoff for Buckingham (and Coulombic if only 1 arg) (distance units)
  cutoff2  = global cutoff for Coulombic (optional) (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style buck6d/coul/gauss/dsf    0.9000    12.0000
    pair_coeff 1  1  1030.  3.061  457.179  4.521  0.608

    pair_style buck6d/coul/gauss/long   0.9000  1.0000  12.0000
    pair_coeff 1  1  1030.  3.061  457.179  4.521  0.608
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *buck6d/coul/gauss* styles evaluate vdW and Coulomb interactions following the MOF-FF force field after [[(Schmid)]{.std .std-ref}](#schmid){.reference .internal}. The vdW term of the *buck6d* styles computes a dispersion damped Buckingham potential:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = A e\^{-\\kappa r} - \\frac{C}{r\^6} \\cdot \\frac{1}{1 + D r\^{14}} \\qquad r \< r_c \\\\\\end{split}\\\]
:::

where A and C are a force constant, [\\(\\kappa\\)]{.math .notranslate .nohighlight} is an ionic-pair dependent reciprocal length parameter, D is a dispersion correction parameter, and the cutoff [\\(r_c\\)]{.math .notranslate .nohighlight} truncates the interaction distance. The first term in the potential corresponds to the Buckingham repulsion term and the second term to the dispersion attraction with a damping correction analog to the Grimme correction used in DFT. The latter corrects for artifacts occurring at short distances which become an issue for soft vdW potentials.

The *buck6d* styles include a smoothing function which is invoked according to the global smoothing parameter within the specified cutoff. Hereby a parameter of i.e. 0.9 invokes the smoothing within 90% of the cutoff. No smoothing is applied at a value of 1.0. For the *gauss/dsf* style this smoothing is only applicable for the dispersion damped Buckingham potential. For the *gauss/long* styles the smoothing function can also be invoked for the real space coulomb interactions which enforce continuous energies and forces at the cutoff.

Both styles *buck6d/coul/gauss/dsf* and *buck6d/coul/gauss/long* evaluate a Coulomb potential using spherical Gaussian type charge distributions which effectively dampen electrostatic interactions for high charges at close distances. The electrostatic potential is thus evaluated as:

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{C\_{q_i q_j}}{\\epsilon r\_{ij}}\\,\\, \\textrm{erf}\\left(\\alpha\_{ij} r\_{ij}\\right)\\quad\\quad\\quad r \< r_c\\\]
:::

where C is an energy-conversion constant, [\\(q_i\\)]{.math .notranslate .nohighlight} and [\\(q_j\\)]{.math .notranslate .nohighlight} are the charges on the two atoms, epsilon is the dielectric constant which can be set by the [[dielectric]{.doc}]dielectric.md){.reference .internal} command, [\\(\\alpha\\)]{.math .notranslate .nohighlight} is the ion pair dependent damping parameter and erf() is the error-function. The cutoff [\\(r_c\\)]{.math .notranslate .nohighlight} truncates the interaction distance.

The style *buck6d/coul/gauss/dsf* computes the Coulomb interaction via the damped shifted force model described in [[(Fennell)]{.std .std-ref}](#fennell){.reference .internal} approximating an Ewald sum similar to the [[pair coul/dsf]{.doc}]pair_coul.md){.reference .internal} styles. In *buck6d/coul/gauss/long* an additional damping factor is applied to the Coulombic term so it can be used in conjunction with the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command and its *ewald* or *pppm* options. The Coulombic cutoff in this case separates the real and reciprocal space evaluation of the Ewald sum.

If one cutoff is specified it is used for both the vdW and Coulomb terms. If two cutoffs are specified, the first is used as the cutoff for the vdW terms, and the second is the cutoff for the Coulombic term.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- A (energy units)

- [\\(\\rho\\)]{.math .notranslate .nohighlight} (distance\^-1 units)

- C (energy-distance\^6 units)

- D (distance\^14 units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (distance\^-1 units)

- cutoff (distance units)

The second coefficient, [\\(\\rho\\)]{.math .notranslate .nohighlight}, must be greater than zero. The latter coefficient is optional. If not specified, the global vdW cutoff is used.
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

These pair styles do not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

These styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy. Instead the smoothing function should be applied by setting the global smoothing parameter to a value \< 1.0.

These styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These styles are part of the MOFFF package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

[]{#schmid}**(Schmid)** S. Bureekaew, S. Amirjalayer, M. Tafipolsky, C. Spickermann, T.K. Roy and R. Schmid, Phys. Status Solidi B, 6, 1128 (2013).

**(Fennell)** C. J. Fennell, J. D. Gezelter, J Chem Phys, 124, 234104 (2006).
:::
::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

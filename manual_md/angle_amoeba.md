:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#angle-style-amoeba-command .section}
[]{#index-0}

# angle_style amoeba command[](#angle-style-amoeba-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style amoeba
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style amoeba
    angle_coeff * 75.0 -25.0 1.0 0.3 0.02 0.003
    angle_coeff * ba 3.6551 24.895 1.0119 1.5228
    angle_coeff * ub -7.6 1.5537
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *amoeba* angle style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = E_a + E\_{ba} + E\_{ub} \\\\ E_a & = K_2\\left(\\theta - \\theta_0\\right)\^2 + K_3\\left(\\theta - \\theta_0\\right)\^3 + K_4\\left(\\theta - \\theta_0\\right)\^4 + K_5\\left(\\theta - \\theta_0\\right)\^5 + K_6\\left(\\theta - \\theta_0\\right)\^6 \\\\ E\_{ba} & = N_1 (r\_{ij} - r_1) (\\theta - \\theta_0) + N_2(r\_{jk} - r_2)(\\theta - \\theta_0) \\\\ E\_{UB} & = K\_{ub} (r\_{ik} - r\_{ub})\^2\\end{split}\\\]
:::

where [\\(E_a\\)]{.math .notranslate .nohighlight} is the angle term, [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} is a bond-angle term, [\\(E\_{UB}\\)]{.math .notranslate .nohighlight} is a Urey-Bradley bond term, [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is the equilibrium angle, [\\(r_1\\)]{.math .notranslate .nohighlight} and [\\(r_2\\)]{.math .notranslate .nohighlight} are the equilibrium bond lengths, and [\\(r\_{ub}\\)]{.math .notranslate .nohighlight} is the equilibrium Urey-Bradley bond length.

These formulas match how the Tinker MD code performs its angle calculations for the AMOEBA and HIPPO force fields. See the [[Howto amoeba]{.doc}]Howto_amoeba.md){.reference .internal} page for more information about the implementation of AMOEBA and HIPPO in LAMMPS.

Note that the [\\(E_a\\)]{.math .notranslate .nohighlight} and [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} formulas are identical to those used for the [[angle_style class2/p6]{.doc}]angle_class2.md){.reference .internal} command, however there is no bond-bond cross term formula for [\\(E\_{bb}\\)]{.math .notranslate .nohighlight}. Additionally, there is a [\\(E\_{UB}\\)]{.math .notranslate .nohighlight} term for a Urey-Bradley bond. It is effectively a harmonic bond between the I and K atoms of angle IJK, even though that bond is not enumerated in the "Bonds" section of the data file.

There are also two ways that Tinker computes the angle [\\(\\theta\\)]{.math .notranslate .nohighlight} in the [\\(E_a\\)]{.math .notranslate .nohighlight} formula. The first is the standard way of treating IJK as an "in-plane" angle. The second is an "out-of-plane" method which Tinker may use if the center atom J in the angle is bonded to one additional atom in addition to I and K. In this case, all 4 atoms are used to compute the [\\(E_a\\)]{.math .notranslate .nohighlight} formula, resulting in forces on all 4 atoms. In the Tinker PRM file, these 2 options are denoted by *angle* versus *anglep* entries in the "Angle Bending Parameters" section of the PRM force field file. The *pflag* coefficient described below selects between the 2 options.

------------------------------------------------------------------------

Coefficients for the [\\(E_a\\)]{.math .notranslate .nohighlight}, [\\(E\_{bb}\\)]{.math .notranslate .nohighlight}, and [\\(E\_{ub}\\)]{.math .notranslate .nohighlight} formulas must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

These are the 8 coefficients for the [\\(E_a\\)]{.math .notranslate .nohighlight} formula:

- pflag = 0 or 1

- ubflag = 0 or 1

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(K_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_3\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_4\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_5\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_6\\)]{.math .notranslate .nohighlight} (energy)

A pflag value of 0 vs 1 selects between the "in-plane" and "out-of-plane" options described above. Ubflag is 1 if there is a Urey-Bradley term associated with this angle type, else it is 0. [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence the various [\\(K\\)]{.math .notranslate .nohighlight} values are effectively energy per radian\^2 or radian\^3 or radian\^4 or radian\^5 or radian\^6.

For the [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} formula, each line in a [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command in the input script lists 5 coefficients, the first of which is "ba" to indicate they are BondAngle coefficients. In a data file, these coefficients should be listed under a "BondAngle Coeffs" heading and you must leave out the "ba", i.e. only list 4 coefficients after the angle type.

- ba

- [\\(N_1\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(N_2\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_2\\)]{.math .notranslate .nohighlight} (distance)

The [\\(\\theta_0\\)]{.math .notranslate .nohighlight} value in the [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} formula is not specified, since it is the same value from the [\\(E_a\\)]{.math .notranslate .nohighlight} formula.

For the [\\(E\_{ub}\\)]{.math .notranslate .nohighlight} formula, each line in a [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command in the input script lists 3 coefficients, the first of which is "ub" to indicate they are UreyBradley coefficients. In a data file, these coefficients should be listed under a "UreyBradley Coeffs" heading and you must leave out the "ub", i.e. only list 2 coefficients after the angle type.

- ub

- [\\(K\_{ub}\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(r\_{ub}\\)]{.math .notranslate .nohighlight} (distance)
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This angle style can only be used if LAMMPS was built with the AMOEBA package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

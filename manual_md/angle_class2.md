::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#angle-style-class2-command .section}
[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# angle_style class2 command[](#angle-style-class2-command "Link to this heading"){.headerlink}

Accelerator Variants: *class2/kk*, *class2/omp*
:::

::: {#angle-style-class2xe-command .section}
# angle_style class2xe command[](#angle-style-class2xe-command "Link to this heading"){.headerlink}
:::

::::::::::::::::::: {#angle-style-class2-p6-command .section}
# angle_style class2/p6 command[](#angle-style-class2-p6-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style class2
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style class2
    angle_coeff * 75.0 25.0 0.3 0.002
    angle_coeff 1 bb 10.5872 1.0119 1.5228
    angle_coeff * ba 3.6551 24.895 1.0119 1.5228
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *class2* angle style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = E_a + E\_{bb} + E\_{ba} \\\\ E_a & = K_2 (\\theta - \\theta_0)\^2 + K_3 (\\theta - \\theta_0)\^3 + K_4(\\theta - \\theta_0)\^4 \\\\ E\_{bb} & = M (r\_{ij} - r_1) (r\_{jk} - r_2) \\\\ E\_{ba} & = N_1 (r\_{ij} - r_1) (\\theta - \\theta_0) + N_2(r\_{jk} - r_2)(\\theta - \\theta_0)\\end{split}\\\]
:::

where [\\(E_a\\)]{.math .notranslate .nohighlight} is the angle term, [\\(E\_{bb}\\)]{.math .notranslate .nohighlight} is a bond-bond term, and [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} is a bond-angle term. [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is the equilibrium angle and [\\(r_1\\)]{.math .notranslate .nohighlight} and [\\(r_2\\)]{.math .notranslate .nohighlight} are the equilibrium bond lengths.

See [[(Sun)]{.std .std-ref}](#angle-sun){.reference .internal} for a description of the COMPASS class2 force field.

Coefficients for the [\\(E_a\\)]{.math .notranslate .nohighlight}, [\\(E\_{bb}\\)]{.math .notranslate .nohighlight}, and [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} formulas must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

These are the 4 coefficients for the [\\(E_a\\)]{.math .notranslate .nohighlight} formula:

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(K_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_3\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_4\\)]{.math .notranslate .nohighlight} (energy)

[\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence the various [\\(K\\)]{.math .notranslate .nohighlight} are effectively energy per radian\^2 or radian\^3 or radian\^4.

For the [\\(E\_{bb}\\)]{.math .notranslate .nohighlight} formula, each line in a [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command in the input script lists 4 coefficients, the first of which is "bb" to indicate they are BondBond coefficients. In a data file, these coefficients should be listed under a "BondBond Coeffs" heading and you must leave out the "bb", i.e. only list 3 coefficients after the angle type.

- bb

- [\\(M\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_2\\)]{.math .notranslate .nohighlight} (distance)

For the [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} formula, each line in a [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command in the input script lists 5 coefficients, the first of which is "ba" to indicate they are BondAngle coefficients. In a data file, these coefficients should be listed under a "BondAngle Coeffs" heading and you must leave out the "ba", i.e. only list 4 coefficients after the angle type.

- ba

- [\\(N_1\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(N_2\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_2\\)]{.math .notranslate .nohighlight} (distance)

The [\\(\\theta_0\\)]{.math .notranslate .nohighlight} value in the [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} formula is not specified, since it is the same value from the [\\(E_a\\)]{.math .notranslate .nohighlight} formula.

::: {.admonition .note}
Note

It is important that the order of the I,J,K atoms in each angle listed in the Angles section of the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command be consistent with the order of the [\\(r_1\\)]{.math .notranslate .nohighlight} and [\\(r_2\\)]{.math .notranslate .nohighlight} BondBond and BondAngle coefficients. This is because the terms in the formulas for [\\(E\_{bb}\\)]{.math .notranslate .nohighlight} and [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} will use the I,J atoms to compute [\\(r\_{ij}\\)]{.math .notranslate .nohighlight} and the J,K atoms to compute [\\(r\_{jk}\\)]{.math .notranslate .nohighlight}.
:::

------------------------------------------------------------------------

::: versionadded
[Added in version 30Mar2026.]{.versionmodified .added}
:::

The *class2xe* angle style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\begin{aligned} E_a = & K_2 (\\theta - \\theta_0)\^2 + K_3 (\\theta - \\theta_0)\^3 + K_4(\\theta - \\theta_0)\^4 \\\\ E\_{bb} = & D \\left\[ 1 - e\^{-\\alpha (r\_{ij} - r_1)} \\right\] \\left\[ 1 - e\^{-\\alpha (r\_{jk} - r_2)} \\right\] \\\\ E\_{ba} = & D_1 \\left\[ 1 - e\^{-\\alpha_1 (r\_{ij} - r_1)} \\right\] \\left\[\\theta - \\theta_0\\right\] + D_2 \\left\[ 1 - e\^{-\\alpha_2 (r\_{jk} - r_2)} \\right\] \\left\[\\theta - \\theta_0\\right\] \\end{aligned}\\end{split}\\\]
:::

where [\\(E_a\\)]{.math .notranslate .nohighlight} is the angle term, [\\(E\_{bb}\\)]{.math .notranslate .nohighlight} is a bond-bond term ([\\(D\\)]{.math .notranslate .nohighlight} is the dissociation energy), and [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} is a bond-angle term ([\\(D_1\\)]{.math .notranslate .nohighlight} and [\\(D_2\\)]{.math .notranslate .nohighlight} are the dissociation energies). [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is the equilibrium angle and [\\(r_1\\)]{.math .notranslate .nohighlight} and [\\(r_2\\)]{.math .notranslate .nohighlight} are the equilibrium bond lengths.

See [[(Kemppainen)]{.std .std-ref}](#angle-kemppainen){.reference .internal} for a description of the ClassII-xe force field and see [[Howto bioFF]{.doc}]Howto_bioFF.md){.reference .internal} page for a motivation for the ClassII-xe force field.

::: {.admonition .note}
Note

The *class2xe* angle style only describes the dissociation of a bond stretch. However once a bond is dissociated and stretched beyond the processor communication cutoff distance in parallel, the simulation will crash with atoms missing errors. This is often after the material fractures and thus for post-fracture phenomena the bonded interactions need to be removed for proper parallel communication.

To disconnect the dissociated bond and remove higher order interactions (angles, dihedrals, and impropers) the following LAMMPS commands can be used with the *class2xe* angle style [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal} or [[fix bond/break]{.doc}]fix_bond_break.md){.reference .internal}. See the [[Howto bioFF]{.doc}]Howto_bioFF.md){.reference .internal} page for more details.
:::

Coefficients for the [\\(E_a\\)]{.math .notranslate .nohighlight}, [\\(E\_{bb}\\)]{.math .notranslate .nohighlight}, and [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} formulas must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

These are the 4 coefficients for the [\\(E_a\\)]{.math .notranslate .nohighlight} formula:

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(K_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_3\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_4\\)]{.math .notranslate .nohighlight} (energy)

[\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence the various [\\(K\\)]{.math .notranslate .nohighlight} are effectively energy per radian\^2 or radian\^3 or radian\^4.

For the [\\(E\_{bb}\\)]{.math .notranslate .nohighlight} formula, each line in a [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command in the input script lists 5 coefficients, the first of which is "bb" to indicate they are BondBond coefficients. In a data file, these coefficients should be listed under a "BondBond Coeffs" heading and you must leave out the "bb", i.e. only list 4 coefficients after the angle type.

- bb

- [\\(D\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (inverse distance)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_2\\)]{.math .notranslate .nohighlight} (distance)

For the [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} formula, each line in a [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command in the input script lists 7 coefficients, the first of which is "ba" to indicate they are BondAngle coefficients. In a data file, these coefficients should be listed under a "BondAngle Coeffs" heading and you must leave out the "ba", i.e. only list 6 coefficients after the angle type.

- ba

- [\\(D_1\\)]{.math .notranslate .nohighlight} (energy)

- [\\(D_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\alpha_1\\)]{.math .notranslate .nohighlight} (inverse distance)

- [\\(\\alpha_2\\)]{.math .notranslate .nohighlight} (inverse distance)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_2\\)]{.math .notranslate .nohighlight} (distance)

The [\\(\\theta_0\\)]{.math .notranslate .nohighlight} value in the [\\(E\_{ba}\\)]{.math .notranslate .nohighlight} formula is not specified, since it is the same value from the [\\(E_a\\)]{.math .notranslate .nohighlight} formula.

------------------------------------------------------------------------

The *class2/p6* angle style uses the *class2* potential expanded to sixth order:

::: {.math .notranslate .nohighlight}
\\\[E\_{a} = K_2\\left(\\theta - \\theta_0\\right)\^2 + K_3\\left(\\theta - \\theta_0\\right)\^3 + K_4\\left(\\theta - \\theta_0\\right)\^4 + K_5\\left(\\theta - \\theta_0\\right)\^5 + K_6\\left(\\theta - \\theta_0\\right)\^6\\\]
:::

In this expanded term 6 coefficients for the [\\(E_a\\)]{.math .notranslate .nohighlight} formula need to be set:

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(K_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_3\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_4\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_5\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_6\\)]{.math .notranslate .nohighlight} (energy)

[\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence the various [\\(K\\)]{.math .notranslate .nohighlight} are effectively energy per radian\^2 or radian\^3 or radian\^4 or radian\^5 or radian\^6.

The bond-bond and bond-angle terms remain unchanged.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *class2* and *class2xe* angle styles can only be used if LAMMPS was built with the CLASS2 package. For the *class2/p6* angle style LAMMPS needs to be built with the MOFFF package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Sun)** Sun, J Phys Chem B 102, 7338-7364 (1998).

**(Kemppainen)** Kemppainen, npj Computational Materials 11, 341 (2025).
:::
:::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

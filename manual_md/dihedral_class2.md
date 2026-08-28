:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#dihedral-style-class2-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# dihedral_style class2 command[](#dihedral-style-class2-command "Link to this heading"){.headerlink}

Accelerator Variants: *class2/omp*, *class2/kk*
:::

::::::::::::::::: {#dihedral-style-class2xe-command .section}
# dihedral_style class2xe command[](#dihedral-style-class2xe-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style class2
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style class2
    dihedral_coeff 1 100 75 100 70 80 60
    dihedral_coeff * mbt 3.5945 0.1704 -0.5490 1.5228
    dihedral_coeff * ebt 0.3417 0.3264 -0.9036 0.1368 0.0 -0.8080 1.0119 1.1010
    dihedral_coeff 2 at 0.0 -0.1850 -0.7963 -2.0220 0.0 -0.3991 110.2453 105.1270
    dihedral_coeff * aat -13.5271 110.2453 105.1270
    dihedral_coeff * bb13 0.0 1.0119 1.1010
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *class2* dihedral style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & E_d + E\_{mbt} + E\_{ebt} + E\_{at} + E\_{aat} + E\_{bb13} \\\\ E_d = & \\sum\_{n=1}\^{3} K_n \[ 1 - \\cos (n \\phi - \\phi_n) \] \\\\ E\_{mbt} = & (r\_{jk} - r_2) \[ A_1 \\cos (\\phi) + A_2 \\cos (2\\phi) + A_3 \\cos (3\\phi) \] \\\\ E\_{ebt} = & (r\_{ij} - r_1) \[ B_1 \\cos (\\phi) + B_2 \\cos (2\\phi) + B_3 \\cos (3\\phi) \] + \\\\ & (r\_{kl} - r_3) \[ C_1 \\cos (\\phi) + C_2 \\cos (2\\phi) + C_3 \\cos (3\\phi) \] \\\\ E\_{at} = & (\\theta\_{ijk} - \\theta_1) \[ D_1 \\cos (\\phi) + D_2 \\cos (2\\phi) + D_3 \\cos (3\\phi) \] + \\\\ & (\\theta\_{jkl} - \\theta_2) \[ E_1 \\cos (\\phi) + E_2 \\cos (2\\phi) + E_3 \\cos (3\\phi) \] \\\\ E\_{aat} = & M (\\theta\_{ijk} - \\theta_1) (\\theta\_{jkl} - \\theta_2) \\cos (\\phi) \\\\ E\_{bb13} = & N (r\_{ij} - r_1) (r\_{kl} - r_3)\\end{split}\\\]
:::

where [\\(E_d\\)]{.math .notranslate .nohighlight} is the dihedral term, [\\(E\_{mbt}\\)]{.math .notranslate .nohighlight} is a middle-bond-torsion term, [\\(E\_{ebt}\\)]{.math .notranslate .nohighlight} is an end-bond-torsion term, [\\(E\_{at}\\)]{.math .notranslate .nohighlight} is an angle-torsion term, [\\(E\_{aat}\\)]{.math .notranslate .nohighlight} is an angle-angle-torsion term, and [\\(E\_{bb13}\\)]{.math .notranslate .nohighlight} is a bond-bond-13 term.

[\\(\\theta_1\\)]{.math .notranslate .nohighlight} and [\\(\\theta_2\\)]{.math .notranslate .nohighlight} are equilibrium angles and :math:[\\(r_1\\)]{.math .notranslate .nohighlight}, [\\(r_2\\)]{.math .notranslate .nohighlight}, and r_3 are equilibrium bond lengths.

See [[(Sun)]{.std .std-ref}](#dihedral-sun){.reference .internal} for a description of the COMPASS class2 force field.

Coefficients for the [\\(E_d\\)]{.math .notranslate .nohighlight}, [\\(E\_{mbt}\\)]{.math .notranslate .nohighlight}, [\\(E\_{ebt}\\)]{.math .notranslate .nohighlight}, [\\(E\_{at}\\)]{.math .notranslate .nohighlight}, [\\(E\_{aat}\\)]{.math .notranslate .nohighlight}, and [\\(E\_{bb13}\\)]{.math .notranslate .nohighlight} formulas must be defined for each dihedral type via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

These are the 6 coefficients for the [\\(E_d\\)]{.math .notranslate .nohighlight} formula:

- [\\(K_1\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\phi_1\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(K_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\phi_2\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(K_3\\)]{.math .notranslate .nohighlight} (energy)

- [\\(phi_3\\)]{.math .notranslate .nohighlight} (degrees)

For the [\\(E\_{mbt}\\)]{.math .notranslate .nohighlight} formula, each line in a [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command in the input script lists 5 coefficients, the first of which is *mbt* to indicate they are MiddleBondTorsion coefficients. In a data file, these coefficients should be listed under a *MiddleBondTorsion Coeffs* heading and you must leave out the *mbt*, i.e. only list 4 coefficients after the dihedral type.

- *mbt*

- [\\(A_1\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(A_2\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(A_3\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(r_2\\)]{.math .notranslate .nohighlight} (distance)

For the [\\(E\_{ebt}\\)]{.math .notranslate .nohighlight} formula, each line in a [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command in the input script lists 9 coefficients, the first of which is *ebt* to indicate they are EndBondTorsion coefficients. In a data file, these coefficients should be listed under a *EndBondTorsion Coeffs* heading and you must leave out the *ebt*, i.e. only list 8 coefficients after the dihedral type.

- *ebt*

- [\\(B_1\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(B_2\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(B_3\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(C_1\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(C_2\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(C_3\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_3\\)]{.math .notranslate .nohighlight} (distance)

For the [\\(E\_{at}\\)]{.math .notranslate .nohighlight} formula, each line in a [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command in the input script lists 9 coefficients, the first of which is *at* to indicate they are AngleTorsion coefficients. In a data file, these coefficients should be listed under a *AngleTorsion Coeffs* heading and you must leave out the *at*, i.e. only list 8 coefficients after the dihedral type.

- *at*

- [\\(D_1\\)]{.math .notranslate .nohighlight} (energy)

- [\\(D_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(D_3\\)]{.math .notranslate .nohighlight} (energy)

- [\\(E_1\\)]{.math .notranslate .nohighlight} (energy)

- [\\(E_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(E_3\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta_1\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(\\theta_2\\)]{.math .notranslate .nohighlight} (degrees)

[\\(\\theta_1\\)]{.math .notranslate .nohighlight} and [\\(\\theta_2\\)]{.math .notranslate .nohighlight} are specified in degrees, but LAMMPS converts them to radians internally; hence the various [\\(D\\)]{.math .notranslate .nohighlight} and [\\(E\\)]{.math .notranslate .nohighlight} are effectively energy per radian.

For the [\\(E\_{aat}\\)]{.math .notranslate .nohighlight} formula, each line in a [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command in the input script lists 4 coefficients, the first of which is *aat* to indicate they are AngleAngleTorsion coefficients. In a data file, these coefficients should be listed under a *AngleAngleTorsion Coeffs* heading and you must leave out the *aat*, i.e. only list 3 coefficients after the dihedral type.

- *aat*

- [\\(M\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta_1\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(\\theta_2\\)]{.math .notranslate .nohighlight} (degrees)

[\\(\\theta_1\\)]{.math .notranslate .nohighlight} and [\\(\\theta_2\\)]{.math .notranslate .nohighlight} are specified in degrees, but LAMMPS converts them to radians internally; hence [\\(M\\)]{.math .notranslate .nohighlight} is effectively energy per radian\^2.

For the [\\(E\_{bb13}\\)]{.math .notranslate .nohighlight} formula, each line in a [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command in the input script lists 4 coefficients, the first of which is *bb13* to indicate they are BondBond13 coefficients. In a data file, these coefficients should be listed under a *BondBond13 Coeffs* heading and you must leave out the *bb13*, i.e. only list 3 coefficients after the dihedral type.

- *bb13*

- [\\(N\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_3\\)]{.math .notranslate .nohighlight} (distance)

------------------------------------------------------------------------

::: versionadded
[Added in version 30Mar2026.]{.versionmodified .added}
:::

The *class2xe* dihedral style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\begin{aligned} E\_{mbt} = & \\left\[ 1 - e\^{-\\alpha_2 (r\_{jk} - r_2)} \\right\] \[ A_1 \\cos (\\phi) + A_2 \\cos (2\\phi) + A_3 \\cos (3\\phi) \] \\\\ E\_{ebt} = & \\left\[ 1 - e\^{-\\alpha_1 (r\_{ij} - r_1)} \\right\] \[ B_1 \\cos (\\phi) + B_2 \\cos (2\\phi) + B_3 \\cos (3\\phi) \] + \\\\ & \\left\[ 1 - e\^{-\\alpha_3 (r\_{kl} - r_3)} \\right\] \[ C_1 \\cos (\\phi) + C_2 \\cos (2\\phi) + C_3 \\cos (3\\phi) \] \\\\ E\_{bb13} = & D \\left\[ 1 - e\^{-\\alpha (r\_{ij} - r_1)} \\right\] \\left\[ 1 - e\^{-\\alpha (r\_{kl} - r_3)} \\right\] \\end{aligned}\\end{split}\\\]
:::

where [\\(E\_{mbt}\\)]{.math .notranslate .nohighlight} is a middle-bond-torsion term, [\\(E\_{ebt}\\)]{.math .notranslate .nohighlight} is an end-bond-torsion term, and [\\(E\_{bb13}\\)]{.math .notranslate .nohighlight} is a bond-bond-13 term ([\\(D\\)]{.math .notranslate .nohighlight} is the dissociation energy).

[\\(\\theta_1\\)]{.math .notranslate .nohighlight} and [\\(\\theta_2\\)]{.math .notranslate .nohighlight} are equilibrium angles and :math:[\\(r_1\\)]{.math .notranslate .nohighlight}, [\\(r_2\\)]{.math .notranslate .nohighlight}, and r_3 are equilibrium bond lengths.

See [[(Kemppainen)]{.std .std-ref}](#dihedral-kemppainen){.reference .internal} for a description of the ClassII-xe force field and see [[Howto bioFF]{.doc}]Howto_bioFF.md){.reference .internal} page for a motivation for the ClassII-xe force field.

::: {.admonition .note}
Note

The *class2xe* dihedral style only describes the dissociation of a bond stretch. However once a bond is dissociated and stretched beyond the processor communication cutoff distance in parallel, the simulation will crash with atoms missing errors. This is often after the material fractures and thus for post-fracture phenomena the bonded interactions need to be removed for proper parallel communication.

To disconnect the dissociated bond and remove higher order interactions (angles, dihedrals, and impropers) the following LAMMPS commands can be used with the *class2xe* dihedral style [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal} or [[fix bond/break]{.doc}]fix_bond_break.md){.reference .internal}. See the [[Howto bioFF]{.doc}]Howto_bioFF.md){.reference .internal} page for more details.
:::

Coefficients for the [\\(E\_{mbt}\\)]{.math .notranslate .nohighlight}, [\\(E\_{ebt}\\)]{.math .notranslate .nohighlight}, and [\\(E\_{bb13}\\)]{.math .notranslate .nohighlight} formulas must be defined for each dihedral type via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

For the [\\(E\_{mbt}\\)]{.math .notranslate .nohighlight} formula, each line in a [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command in the input script lists 6 coefficients, the first of which is *mbt* to indicate they are MiddleBondTorsion coefficients. In a data file, these coefficients should be listed under a *MiddleBondTorsion Coeffs* heading and you must leave out the *mbt*, i.e. only list 5 coefficients after the dihedral type.

- *mbt*

- [\\(\\alpha_2\\)]{.math .notranslate .nohighlight} (inverse distance)

- [\\(A_1\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(A_2\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(A_3\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(r_2\\)]{.math .notranslate .nohighlight} (distance)

For the [\\(E\_{ebt}\\)]{.math .notranslate .nohighlight} formula, each line in a [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command in the input script lists 11 coefficients, the first of which is *ebt* to indicate they are EndBondTorsion coefficients. In a data file, these coefficients should be listed under a *EndBondTorsion Coeffs* heading and you must leave out the *ebt*, i.e. only list 10 coefficients after the dihedral type.

- *ebt*

- [\\(\\alpha_1\\)]{.math .notranslate .nohighlight} (inverse distance)

- [\\(\\alpha_3\\)]{.math .notranslate .nohighlight} (inverse distance)

- [\\(B_1\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(B_2\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(B_3\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(C_1\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(C_2\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(C_3\\)]{.math .notranslate .nohighlight} (energy/distance)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_3\\)]{.math .notranslate .nohighlight} (distance)

For the [\\(E\_{bb13}\\)]{.math .notranslate .nohighlight} formula, each line in a [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command in the input script lists 5 coefficients, the first of which is *bb13* to indicate they are BondBond13 coefficients. In a data file, these coefficients should be listed under a *BondBond13 Coeffs* heading and you must leave out the *bb13*, i.e. only list 4 coefficients after the dihedral type.

- *bb13*

- [\\(D\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (inverse distance)

- [\\(r_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_3\\)]{.math .notranslate .nohighlight} (distance)

The dihedral, AngleTorsion and AngleAngleTorsion terms remain unchanged.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This dihedral style can only be used if LAMMPS was built with the CLASS2 package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Sun)** Sun, J Phys Chem B 102, 7338-7364 (1998).

**(Kemppainen)** Kemppainen, npj Computational Materials 11, 341 (2025).
:::
:::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

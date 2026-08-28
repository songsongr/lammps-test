::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#improper-style-class2-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# improper_style class2 command[](#improper-style-class2-command "Link to this heading"){.headerlink}

Accelerator Variants: *class2/omp*, *class2/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style class2
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    improper_style class2
    improper_coeff 1 100.0 0
    improper_coeff * aa 0.0 0.0 0.0 115.06 130.01 115.06
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *class2* improper style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & E_i + E\_{aa} \\\\ E_i = & K \[ \\frac{\\chi\_{ijkl} + \\chi\_{kjli} + \\chi\_{ljik}}{3} - \\chi_0 \]\^2 \\\\ E\_{aa} = & M_1 (\\theta\_{ijk} - \\theta_1) (\\theta\_{kjl} - \\theta_3) + \\\\ & M_2 (\\theta\_{ijk} - \\theta_1) (\\theta\_{ijl} - \\theta_2) + \\\\ & M_3 (\\theta\_{ijl} - \\theta_2) (\\theta\_{kjl} - \\theta_3)\\end{split}\\\]
:::

where [\\(E_i\\)]{.math .notranslate .nohighlight} is the improper term and [\\(E\_{aa}\\)]{.math .notranslate .nohighlight} is an angle-angle term. The 3 [\\(\\chi\\)]{.math .notranslate .nohighlight} terms in [\\(E_i\\)]{.math .notranslate .nohighlight} are an average over 3 out-of-plane angles.

The 4 atoms in an improper quadruplet (listed in the data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command) are ordered I,J,K,L. [\\(\\chi\_{ijkl}\\)]{.math .notranslate .nohighlight} refers to the angle between the plane of I,J,K and the plane of J,K,L, and the bond JK lies in both planes. Similarly for [\\(\\chi\_{kjli}\\)]{.math .notranslate .nohighlight} and [\\(\\chi\_{ljik}\\)]{.math .notranslate .nohighlight}. Note that atom J appears in the common bonds (JI, JK, JL) of all 3 X terms. Thus J (the second atom in the quadruplet) is the atom of symmetry in the 3 [\\(\\chi\\)]{.math .notranslate .nohighlight} angles.

The subscripts on the various [\\(\\theta\\)]{.math .notranslate .nohighlight}s refer to different combinations of three atoms (I,J,K,L) used to form a particular angle. E.g. [\\(\\theta\_{ijl}\\)]{.math .notranslate .nohighlight} is the angle formed by atoms I,J,L with J in the middle. [\\(\\theta_1\\)]{.math .notranslate .nohighlight}, [\\(\\theta_2\\)]{.math .notranslate .nohighlight}, [\\(\\theta_3\\)]{.math .notranslate .nohighlight} are the equilibrium positions of those angles. Again, atom J (the second atom in the quadruplet) is the atom of symmetry in the theta angles, since it is always the center atom.

Since atom J is the atom of symmetry, normally the bonds J-I, J-K, J-L would exist for an improper to be defined between the 4 atoms, but this is not required.

See [[(Sun)]{.std .std-ref}](#improper-sun){.reference .internal} for a description of the COMPASS class2 force field.

Coefficients for the [\\(E_i\\)]{.math .notranslate .nohighlight} and [\\(E\_{aa}\\)]{.math .notranslate .nohighlight} formulas must be defined for each improper type via the [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

These are the 2 coefficients for the [\\(E_i\\)]{.math .notranslate .nohighlight} formula:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\chi_0\\)]{.math .notranslate .nohighlight} (degrees)

[\\(\\chi_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence [\\(K\\)]{.math .notranslate .nohighlight} is effectively energy per radian\^2.

For the [\\(E\_{aa}\\)]{.math .notranslate .nohighlight} formula, each line in a [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal} command in the input script lists 7 coefficients, the first of which is *aa* to indicate they are AngleAngle coefficients. In a data file, these coefficients should be listed under a *AngleAngle Coeffs* heading and you must leave out the *aa*, i.e. only list 6 coefficients after the improper type.

- *aa*

- [\\(M_1\\)]{.math .notranslate .nohighlight} (energy)

- [\\(M_2\\)]{.math .notranslate .nohighlight} (energy)

- [\\(M_3\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta_1\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(\\theta_2\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(\\theta_3\\)]{.math .notranslate .nohighlight} (degrees)

The [\\(\\theta\\)]{.math .notranslate .nohighlight} values are specified in degrees, but LAMMPS converts them to radians internally; hence the hence the various [\\(M\\)]{.math .notranslate .nohighlight} are effectively energy per radian\^2.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#symmetry-convention .section}
## Symmetry convention[](#symmetry-convention "Link to this heading"){.headerlink}

For the *class2* improper style, the second atom in the quadruplet is the atom of symmetry; all other atoms are considered interchangeable. This convention is relevant for operations that require knowledge of how atoms are ordered, such as automatic assignment of new improper types by [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This improper style can only be used if LAMMPS was built with the CLASS2 package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[improper_coeff]{.doc}]improper_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Sun)** Sun, J Phys Chem B 102, 7338-7364 (1998).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

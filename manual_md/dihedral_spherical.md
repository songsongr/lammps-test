:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#dihedral-style-spherical-command .section}
[]{#index-0}

# dihedral_style spherical command[](#dihedral-style-spherical-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style spherical
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_coeff 1 1  286.1  1 124  1    1 90.0 0    1 90.0 0
    dihedral_coeff 1 3  69.3   1 93.9 1    1 90   0    1 90   0  &
                        49.1   0 0.00 0    1 74.4 1    0 0.00 0  &
                        25.2   0 0.00 0    0 0.00 0    1 48.1 1
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *spherical* dihedral style uses the potential:

![](_images/dihedral_spherical_angles.jpg){.align-center}

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E(\\phi,\\theta_1,\\theta_2) & = \\sum\_{i=1}\^N C_i\\ \\Phi_i(\\phi)\\ \\Theta\_{1i}(\\theta_1)\\ \\Theta\_{2i}(\\theta_2) \\\\ \\Phi\_{i}(\\phi) & = u_i - \\mathrm{cos}((\\phi - a_i)K_i) \\\\ \\Theta\_{1i}(\\theta_1) & = v_i - \\mathrm{cos}((\\theta_1-b_i)L_i) \\\\ \\Theta\_{2i}(\\theta_2) & = w_i - \\mathrm{cos}((\\theta_2-c_i)M_i)\\end{split}\\\]
:::

For this dihedral style, the energy can be any function that combines the 4-body dihedral-angle ([\\(\\phi\\)]{.math .notranslate .nohighlight}) and the two 3-body bond-angles ([\\(\\theta_1\\)]{.math .notranslate .nohighlight}, [\\(\\theta_2\\)]{.math .notranslate .nohighlight}). For this reason, there is usually no need to define 3-body "angle" forces separately for the atoms participating in these interactions. It is probably more efficient to incorporate 3-body angle forces into the dihedral interaction even if it requires adding additional terms to the expansion (as was done in the second example). A careful choice of parameters can prevent singularities that occur with traditional force-fields whenever theta1 or theta2 approach 0 or 180 degrees.

The last example above corresponds to an interaction with a single energy minima located near [\\(\\phi=93.9\\)]{.math .notranslate .nohighlight}, [\\(\\theta_1=74.4\\)]{.math .notranslate .nohighlight}, [\\(\\theta_2=48.1\\)]{.math .notranslate .nohighlight} degrees, and it remains numerically stable at all angles ([\\(\\phi\\)]{.math .notranslate .nohighlight}, [\\(\\theta_1\\)]{.math .notranslate .nohighlight}, [\\(\\theta_2\\)]{.math .notranslate .nohighlight}). In this example, the coefficients 49.1, and 25.2 can be physically interpreted as the harmonic spring constants for theta1 and theta2 around their minima. The coefficient 69.3 is the harmonic spring constant for phi after division by sin(74.4)\*sin(48.1) (the minima positions for theta1 and theta2).

The following coefficients must be defined for each dihedral type via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command as in the example above, or in the Dihedral Coeffs section of a data file read by the [[read_data]{.doc}]read_data.md){.reference .internal} command:

- [\\(n\\)]{.math .notranslate .nohighlight} (integer \>= 1)

- [\\(C_1\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_1\\)]{.math .notranslate .nohighlight} (typically an integer)

- [\\(a_1\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(u_1\\)]{.math .notranslate .nohighlight} (typically 0.0 or 1.0)

- [\\(L_1\\)]{.math .notranslate .nohighlight} (typically an integer)

- [\\(b_1\\)]{.math .notranslate .nohighlight} (degrees, typically 0.0 or 90.0)

- [\\(v_1\\)]{.math .notranslate .nohighlight} (typically 0.0 or 1.0)

- [\\(M_1\\)]{.math .notranslate .nohighlight} (typically an integer)

- [\\(c_1\\)]{.math .notranslate .nohighlight} (degrees, typically 0.0 or 90.0)

- [\\(w_1\\)]{.math .notranslate .nohighlight} (typically 0.0 or 1.0)

- \[...\]

- [\\(C_n\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K_n\\)]{.math .notranslate .nohighlight} (typically an integer)

- [\\(a_n\\)]{.math .notranslate .nohighlight} (degrees)

- [\\(u_n\\)]{.math .notranslate .nohighlight} (typically 0.0 or 1.0)

- [\\(L_n\\)]{.math .notranslate .nohighlight} (typically an integer)

- [\\(b_n\\)]{.math .notranslate .nohighlight} (degrees, typically 0.0 or 90.0)

- [\\(v_n\\)]{.math .notranslate .nohighlight} (typically 0.0 or 1.0)

- [\\(M_n\\)]{.math .notranslate .nohighlight} (typically an integer)

- [\\(c_n\\)]{.math .notranslate .nohighlight} (degrees, typically 0.0 or 90.0)

- [\\(w_n\\)]{.math .notranslate .nohighlight} (typically 0.0 or 1.0)
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This dihedral style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

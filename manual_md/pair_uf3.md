::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::: {#pair-style-uf3-command .section}
[]{#index-1}[]{#index-0}

# pair_style uf3 command[](#pair-style-uf3-command "Link to this heading"){.headerlink}

Accelerator Variants: *uf3/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style BodyFlag
:::
::::

- style = *uf3* or *uf3/kk*

  :::: {.highlight-none .notranslate}
  ::: highlight
      BodyFlag = Indicates whether to calculate only 2-body or 2 and 3-body interactions. Possible values: 2 or 3
  :::
  ::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style uf3 3
    pair_coeff * * Nb.uf3 Nb

    pair_style uf3 2
    pair_coeff * * NbSn.uf3 Nb Sn

    pair_style uf3 3
    pair_coeff * * NbSn.uf3 Nb Sn
:::
::::
:::::

:::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 27June2024.]{.versionmodified .added}
:::

The *uf3* style computes the [[Ultra-Fast Force Fields (UF3)]{.std .std-ref}](#xie23){.reference .internal} potential, a machine-learning interatomic potential. In UF3, the total energy of the system is defined via two- and three-body interactions:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = \\sum\_{i,j} V_2(r\_{ij}) + \\sum\_{i,j,k} V_3 (r\_{ij},r\_{ik},r\_{jk}) \\\\ V_2(r\_{ij}) & = \\sum\_{n=0}\^N c_n B_n(r\_{ij}) \\\\ V_3 (r\_{ij},r\_{ik},r\_{jk}) & = \\sum\_{l=0}\^{N_l} \\sum\_{m=0}\^{N_m} \\sum\_{n=0}\^{N_n} c\_{l,m,n} B_l(r\_{ij}) B_m(r\_{ik}) B_n(r\_{jk})\\end{split}\\\]
:::

where [\\(V_2(r\_{ij})\\)]{.math .notranslate .nohighlight} and [\\(V_3 (r\_{ij},r\_{ik},r\_{jk})\\)]{.math .notranslate .nohighlight} are the two- and three-body interactions, respectively. For the two-body the summation is over all neighbors J and for the three-body the summation is over all neighbors J and K of atom I within a cutoff distance determined from the potential files. [\\(B_n(r\_{ij})\\)]{.math .notranslate .nohighlight} are the cubic b-spline basis, [\\(c_n\\)]{.math .notranslate .nohighlight} and [\\(c\_{l,m,n}\\)]{.math .notranslate .nohighlight} are the machine-learned interaction parameters and [\\(N\\)]{.math .notranslate .nohighlight}, [\\(N_l\\)]{.math .notranslate .nohighlight}, [\\(N_m\\)]{.math .notranslate .nohighlight}, and [\\(N_n\\)]{.math .notranslate .nohighlight} denote the number of basis functions per spline or tensor spline dimension.

With *uf3* style only a single pair_coeff command is used to indicate the UF3 LAMMPS potential file containing all the two- and three-body interactions followed by N additional arguments specifying the mapping of UF3 elements to LAMMPS atom types, where N is the number of LAMMPS atom types:

- UF3 LAMMPS potential file

- N elements names = mapping of UF3 elements to atom types

As an example, if a LAMMPS simulation contains 2 atom types (elements 'A' and 'B'), the pair_coeff command will be:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style uf3 3
    pair_coeff * * AB.uf3 A B
:::
::::

The AB.uf3 file should contain all two-body (A-A, A-B, B-B) and three-body (A-A-A, A-A-B, A-B-B, B-A-A, B-A-B, B-B-B).

If a value of "2" is specified in the [`pair_style`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`uf3`{.code .docutils .literal .notranslate}]{.pre} command, only the two-body potentials are needed. For 3-body interaction the first atom type is the central atom. We recommend using the [`generate_uf3_lammps_pots.py`{.code .docutils .literal .notranslate}]{.pre} script (found [here](https://github.com/uf3/uf3/tree/develop/lammps_plugin/scripts){.reference .external}) for generating the UF3 LAMMPS potential file from the UF3 JSON potentials.

------------------------------------------------------------------------

UF3 LAMMPS potential file in the *potentials* directory of the LAMMPS distribution have a ".uf3" suffix. The interaction block in UF3 LAMMPS potential file should start with [`#UF3`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`POT`{.code .docutils .literal .notranslate}]{.pre} and end with [`#`{.code .docutils .literal .notranslate}]{.pre} characters. Following shows the format of a generic 2-body and 3-body potential block in UF3 LAMMPS potential file-

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    #UF3 POT UNITS: units DATE: POT_GEN_DATE AUTHOR: AUTHOR_NAME CITATION: CITE
    2B ELEMENT1 ELEMENT2 LEADING_TRIM TRAILING_TRIM
    Rij_CUTOFF NUM_OF_KNOTS
    BSPLINE_KNOTS
    NUM_OF_COEFF
    COEFF
    #
    #UF3 POT UNITS: units DATE: POT_GEN_DATE AUTHOR: AUTHOR_NAME CITATION: CITE
    3B ELEMENT1 ELEMENT2 ELEMENT3 LEADING_TRIM TRAILING_TRIM
    Rjk_CUTOFF Rik_CUTOFF Rij_CUTOFF NUM_OF_KNOTS_JK NUM_OF_KNOTS_IK NUM_OF_KNOTS_IJ
    BSPLINE_KNOTS_FOR_JK
    BSPLINE_KNOTS_FOR_IK
    BSPLINE_KNOTS_FOR_IJ
    SHAPE_OF_COEFF_MATRIX[I][J][K]
    COEFF_MATRIX[0][0][K]
    COEFF_MATRIX[0][1][K]
    COEFF_MATRIX[0][2][K]
    .
    .
    .
    COEFF_MATRIX[1][0][K]
    COEFF_MATRIX[1][1][K]
    COEFF_MATRIX[1][2][K]
    .
    .
    .
    #
:::
::::

The second line indicates whether the block contains data for 2-body ([`2B`{.code .docutils .literal .notranslate}]{.pre}) or 3-body ([`3B`{.code .docutils .literal .notranslate}]{.pre}) interaction. This is followed by element combination interaction, [`LEADING_TRIM`{.code .docutils .literal .notranslate}]{.pre} and [`TRAILING_TRIM`{.code .docutils .literal .notranslate}]{.pre} number on the same line. The current implementation is only tested for [`LEADING_TRIM=0`{.code .docutils .literal .notranslate}]{.pre} and [`TRAILING_TRIM=3`{.code .docutils .literal .notranslate}]{.pre}. If other values are used LAMMPS is terminated after issuing an error message. The [`Rij_CUTOFF`{.code .docutils .literal .notranslate}]{.pre} sets the 2-body cutoff for the interaction described by the potential block. [`NUM_OF_KNOTS`{.code .docutils .literal .notranslate}]{.pre} is the number of knots (or the length of the knot vector) present on the very next line. The [`BSPLINE_KNOTS`{.code .docutils .literal .notranslate}]{.pre} line should contain all the knots in ascending order. [`NUM_OF_COEFF`{.code .docutils .literal .notranslate}]{.pre} is the number of coefficients in the [`COEFF`{.code .docutils .literal .notranslate}]{.pre} line. All the numbers in the BSPLINE_KNOTS and COEFF line should be space-separated. Similar to the 2-body potential block, the third line sets the cutoffs and length of the knots. The cutoff distance between atom-type I and J is [`Rij_CUTOFF`{.code .docutils .literal .notranslate}]{.pre}, atom-type I and K is [`Rik_CUTOFF`{.code .docutils .literal .notranslate}]{.pre} and between J and K is [`Rjk_CUTOFF`{.code .docutils .literal .notranslate}]{.pre}.

::: {.admonition .note}
Note

The current implementation only works for UF3 potentials with cutoff distances for 3-body interactions that follows [`2Rij_CUTOFF=2Rik_CUTOFF=Rjk_CUTOFF`{.code .docutils .literal .notranslate}]{.pre} relation.
:::

The [`BSPLINE_KNOTS_FOR_JK`{.code .docutils .literal .notranslate}]{.pre}, [`BSPLINE_KNOTS_FOR_IK`{.code .docutils .literal .notranslate}]{.pre}, and [`BSPLINE_KNOTS_FOR_IJ`{.code .docutils .literal .notranslate}]{.pre} lines (note the order) contain the knots in increasing order for atoms J and K, I and K, and atoms I and J respectively. The number of knots is defined by the [`NUM_OF_KNOTS_*`{.code .docutils .literal .notranslate}]{.pre} characters in the previous line. The shape of the coefficient matrix is defined on the [`SHAPE_OF_COEFF_MATRIX[I][J][K]`{.code .docutils .literal .notranslate}]{.pre} line followed by the columns of the coefficient matrix, one per line, as shown above. For example, if the coefficient matrix has the shape of 8x8x13, then [`SHAPE_OF_COEFF_MATRIX[I][J][K]`{.code .docutils .literal .notranslate}]{.pre} will be [`8`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`8`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`13`{.code .docutils .literal .notranslate}]{.pre} followed by 64 (8x8) lines each containing 13 coefficients separated by space.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, where types I and J correspond to two different element types, mixing is performed by LAMMPS as described above from values in the potential file.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The 'uf3' pair style is part of the ML-UF3 package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair style requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on".

The UF3 LAMMPS potential file provided with LAMMPS (see the potentials directory) are parameterized for metal [[units]{.doc}]units.md){.reference .internal}.

The single() function of 'uf3' pair style only return the 2-body interaction energy.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Xie23)** Xie, S.R., Rupp, M. & Hennig, R.G. Ultra-fast interpretable machine-learning potentials. npj Comput Mater 9, 162 (2023). [https://doi.org/10.1038/s41524-023-01092-7](https://doi.org/10.1038/s41524-023-01092-7){.reference .external}
:::
:::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

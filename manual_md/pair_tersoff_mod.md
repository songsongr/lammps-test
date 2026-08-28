::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-tersoff-mod-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style tersoff/mod command[](#pair-style-tersoff-mod-command "Link to this heading"){.headerlink}

Accelerator Variants: *tersoff/mod/gpu*, *tersoff/mod/kk*, *tersoff/mod/omp*
:::

:::::::::::::::::: {#pair-style-tersoff-mod-c-command .section}
# pair_style tersoff/mod/c command[](#pair-style-tersoff-mod-c-command "Link to this heading"){.headerlink}

Accelerator Variants: *tersoff/mod/c/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style keywords values
:::
::::

- style = *tersoff/mod* or *tersoff/mod/c*

- keyword = *shift*

  ``` literal-block
  shift value = delta
    delta = negative shift in equilibrium bond length
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style tersoff/mod
    pair_coeff * * Si.tersoff.mod Si Si

    pair_style tersoff/mod/c
    pair_coeff * * Si.tersoff.modc Si Si
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *tersoff/mod* and *tersoff/mod/c* styles computes a bond-order type interatomic potential [[(Kumagai)]{.std .std-ref}](#kumagai){.reference .internal} based on a 3-body Tersoff potential [[(Tersoff_1)]{.std .std-ref}](#tersoff-12){.reference .internal}, [[(Tersoff_2)]{.std .std-ref}](#tersoff-22){.reference .internal} with modified cutoff function and angular-dependent term, giving the energy E of a system of atoms as

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} V\_{ij} \\\\ V\_{ij} & = f_C(r\_{ij} + \\delta) \\left\[ f_R(r\_{ij} + \\delta) + b\_{ij} f_A(r\_{ij} + \\delta) \\right\] \\\\ f_C(r) & = \\left\\{ \\begin{array} {r@{\\quad:\\quad}l} 1 & r \< R - D \\\\ \\frac{1}{2} - \\frac{9}{16} \\sin \\left( \\frac{\\pi}{2} \\frac{r-R}{D} \\right) - \\frac{1}{16} \\sin \\left( \\frac{3\\pi}{2} \\frac{r-R}{D} \\right) & R-D \< r \< R + D \\\\ 0 & r \> R + D \\end{array} \\right. \\\\ f_R(r) & = A \\exp (-\\lambda_1 r) \\\\ f_A(r) & = -B \\exp (-\\lambda_2 r) \\\\ b\_{ij} & = \\left( 1 + {\\zeta\_{ij}}\^\\eta \\right)\^{-\\frac{1}{2n}} \\\\ \\zeta\_{ij} & = \\sum\_{k \\neq i,j} f_C(r\_{ik} + \\delta) g(\\theta\_{ijk}) \\exp \\left\[ \\alpha (r\_{ij} - r\_{ik})\^\\beta \\right\] \\\\ g(\\theta) & = c_1 + g_o(\\theta) g_a(\\theta) \\\\ g_o(\\theta) & = \\frac{c_2 (h - \\cos \\theta)\^2}{c_3 + (h - \\cos \\theta)\^2} \\\\ g_a(\\theta) & = 1 + c_4 \\exp \\left\[ -c_5 (h - \\cos \\theta)\^2 \\right\] \\\\\\end{split}\\\]
:::

where [\\(f_R\\)]{.math .notranslate .nohighlight} is a two-body term and [\\(f_A\\)]{.math .notranslate .nohighlight} includes three-body interactions. [\\(\\delta\\)]{.math .notranslate .nohighlight} is an optional negative shift of the equilibrium bond length, as described below.

The summations in the formula are over all neighbors J and K of atom I within a cutoff distance = R + D. The *tersoff/mod/c* style differs from *tersoff/mod* only in the formulation of the V_ij term, where it contains an additional c0 term.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}V\_{ij} = f_C(r\_{ij} + \\delta) \\left\[ f_R(r\_{ij} + \\delta) + b\_{ij} f_A(r\_{ij} + \\delta) + c_0 \\right\] \\\\\\end{split}\\\]
:::

The modified cutoff function [\\(f_C\\)]{.math .notranslate .nohighlight} proposed by [[(Murty)]{.std .std-ref}](#murty){.reference .internal} and having a continuous second-order differential is employed. The angular-dependent term [\\(g(\\theta)\\)]{.math .notranslate .nohighlight} was modified to increase the flexibility of the potential.

The *tersoff/mod* potential is fitted to both the elastic constants and melting point by employing the modified Tersoff potential function form in which the angular-dependent term is improved. The model performs extremely well in describing the crystalline, liquid, and amorphous phases [[(Schelling)]{.std .std-ref}](#schelling){.reference .internal}.

Only a single pair_coeff command is used with the *tersoff/mod* style which specifies a Tersoff/MOD potential file with parameters for all needed elements. These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- N element names = mapping of Tersoff/MOD elements to atom types

As an example, imagine the Si.tersoff_mod file has Tersoff values for Si. If your LAMMPS simulation has 3 Si atoms types, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * Si.tersoff_mod Si Si Si
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The three Si arguments map LAMMPS atom types 1,2,3 to the Si element in the Tersoff/MOD file. If a mapping value is specified as NULL, the mapping is not performed. This can be used when a *tersoff/mod* potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials.

Tersoff/MOD file in the *potentials* directory of the LAMMPS distribution have a ".tersoff.mod" suffix. Potential files for the *tersoff/mod/c* style have the suffix ".tersoff.modc". Lines that are not blank or comments (starting with #) define parameters for a triplet of elements. The parameters in a single entry correspond to coefficients in the formulae above:

- element 1 (the center atom in a 3-body interaction)

- element 2 (the atom bonded to the center atom)

- element 3 (the atom influencing the 1-2 bond in a bond-order sense)

- [\\(\\beta\\)]{.math .notranslate .nohighlight}

- [\\(\\alpha\\)]{.math .notranslate .nohighlight}

- h

- [\\(\\eta\\)]{.math .notranslate .nohighlight}

- [\\(\\beta\_{ters}\\)]{.math .notranslate .nohighlight} = 1 (dummy parameter)

- [\\(\\lambda_2\\)]{.math .notranslate .nohighlight} (1/distance units)

- B (energy units)

- R (distance units)

- D (distance units)

- [\\(\\lambda_1\\)]{.math .notranslate .nohighlight} (1/distance units)

- A (energy units)

- n

- c1

- c2

- c3

- c4

- c5

- c0 (energy units, tersoff/mod/c only)

The n, [\\(\\eta\\)]{.math .notranslate .nohighlight}, [\\(\\lambda_2\\)]{.math .notranslate .nohighlight}, B, [\\(\\lambda_1\\)]{.math .notranslate .nohighlight}, and A parameters are only used for two-body interactions. The [\\(\\beta\\)]{.math .notranslate .nohighlight}, [\\(\\alpha\\)]{.math .notranslate .nohighlight}, c1, c2, c3, c4, c5, h parameters are only used for three-body interactions. The R and D parameters are used for both two-body and three-body interactions. The c0 term applies to *tersoff/mod/c* only. The non-annotated parameters are unitless.

The Tersoff/MOD potential file must contain entries for all the elements listed in the pair_coeff command. It can also contain entries for additional elements not being used in a particular simulation; LAMMPS ignores those entries.

For a single-element simulation, only a single entry is required (e.g. SiSiSi). As annotated above, the first element in the entry is the center atom in a three-body interaction and it is bonded to the second atom and the bond is influenced by the third atom. Thus an entry for SiSiSi means Si bonded to a Si with another Si atom influencing the bond.

The *shift* keyword computes the energy E of a system of atoms, whose formula is the same as the Tersoff potential. The only modification is that the original equilibrium bond length ( [\\(r_0\\)]{.math .notranslate .nohighlight}) of the system is shifted to [\\(r_0-\\delta\\)]{.math .notranslate .nohighlight}. The minus sign arises because each radial distance [\\(r\\)]{.math .notranslate .nohighlight} is replaced by [\\(r+\\delta\\)]{.math .notranslate .nohighlight}. More information on this option is given on the main [[pair_tersoff]{.doc}]pair_tersoff.md){.reference .internal} page.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the MANYBODY package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair style requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

The *shift* keyword is not supported by the *tersoff/gpu*, *tersoff/intel*, *tersoff/kk*, *tersoff/table* or *tersoff/table/omp* variants.

The *tersoff/mod* potential files provided with LAMMPS (see the potentials directory) are parameterized for metal [[units]{.doc}]units.md){.reference .internal}. You can use the *tersoff/mod* pair style with any LAMMPS units, but you would need to create your own Tersoff/MOD potential file with coefficients listed in the appropriate units if your simulation does not use "metal" units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Kumagai)** T. Kumagai, S. Izumi, S. Hara, S. Sakai, Comp. Mat. Science, 39, 457 (2007).

**(Tersoff_1)** J. Tersoff, Phys Rev B, 37, 6991 (1988).

**(Tersoff_2)** J. Tersoff, Phys Rev B, 38, 9902 (1988).

**(Murty)** M.V.R. Murty, H.A. Atwater, Phys Rev B, 51, 4889 (1995).

**(Schelling)** Patrick K. Schelling, Comp. Mat. Science, 44, 274 (2008).
:::
::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

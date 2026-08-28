:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#pair-style-tersoff-zbl-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style tersoff/zbl command[](#pair-style-tersoff-zbl-command "Link to this heading"){.headerlink}

Accelerator Variants: *tersoff/zbl/gpu*, *tersoff/zbl/kk*, *tersoff/zbl/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style tersoff/zbl keywords values
:::
::::

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
    pair_style tersoff/zbl
    pair_coeff * * SiC.tersoff.zbl Si C Si
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *tersoff/zbl* style computes a 3-body Tersoff potential [[(Tersoff_1)]{.std .std-ref}](#zbl-tersoff-1){.reference .internal} with a close-separation pairwise modification based on a Coulomb potential and the Ziegler-Biersack-Littmark universal screening function [[(ZBL)]{.std .std-ref}](#zbl-zbl){.reference .internal}, giving the energy E of a system of atoms as

::: {.math .notranslate .nohighlight}
\\\[\\begin{split} E & = \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} V\_{ij} \\\\ V\_{ij} & = (1 - f_F(r\_{ij} + \\delta)) V\^{ZBL}(r\_{ij} + \\delta) + f_F(r\_{ij} + \\delta) V\^{Tersoff}(r\_{ij} + \\delta) \\\\ f_F(r) & = \\frac{1}{1 + e\^{-A_F(r - r_C)}}\\\\ \\\\ \\\\ V\^{ZBL}(r) & = \\frac{1}{4\\pi\\epsilon_0} \\frac{Z_1 Z_2 \\,e\^2}{r} \\phi(r/a) \\\\ a & = \\frac{0.8854\\,a_0}{Z\_{1}\^{0.23} + Z\_{2}\^{0.23}}\\\\ \\phi(x) & = 0.1818e\^{-3.2x} + 0.5099e\^{-0.9423x} + 0.2802e\^{-0.4029x} + 0.02817e\^{-0.2016x}\\\\ \\\\ \\\\ V\^{Tersoff}(r) & = f_C(r) \\left\[ f_R(r) + b\_{ij} f_A(r) \\right\] \\\\ f_C(r) & = \\left\\{ \\begin{array} {r@{\\quad:\\quad}l} 1 & r \< R - D \\\\ \\frac{1}{2} - \\frac{1}{2} \\sin \\left( \\frac{\\pi}{2} \\frac{r-R}{D} \\right) & R-D \< r \< R + D \\\\ 0 & r \> R + D \\end{array} \\right. \\\\ f_R(r) & = A \\exp (-\\lambda_1 r) \\\\ f_A(r) & = -B \\exp (-\\lambda_2 r) \\\\ b\_{ij} & = \\left( 1 + \\beta\^n {\\zeta\_{ij}}\^n \\right)\^{-\\frac{1}{2n}} \\\\ \\zeta\_{ij} & = \\sum\_{k \\neq i,j} f_C(r\_{ik} + \\delta) g(\\theta\_{ijk}) \\exp \\left\[ {\\lambda_3}\^m (r\_{ij} - r\_{ik})\^m \\right\] \\\\ g(\\theta) & = \\gamma\_{ijk} \\left( 1 + \\frac{c\^2}{d\^2} - \\frac{c\^2}{\\left\[ d\^2 + (\\cos \\theta - \\cos \\theta_0)\^2\\right\]} \\right)\\end{split}\\\]
:::

The [\\(f_F\\)]{.math .notranslate .nohighlight} term is a fermi-like function used to smoothly connect the ZBL repulsive potential with the Tersoff potential. There are 2 parameters used to adjust it: [\\(A_F\\)]{.math .notranslate .nohighlight} and [\\(r_C\\)]{.math .notranslate .nohighlight}. [\\(A_F\\)]{.math .notranslate .nohighlight} controls how "sharp" the transition is between the two, and [\\(r_C\\)]{.math .notranslate .nohighlight} is essentially the cutoff for the ZBL potential.

For the ZBL portion, there are two terms. The first is the Coulomb repulsive term, with Z1, Z2 as the number of protons in each nucleus, e as the electron charge (1 for metal and real units) and [\\(\\epsilon_0\\)]{.math .notranslate .nohighlight} as the permittivity of vacuum. The second part is the ZBL universal screening function, with a0 being the Bohr radius (typically 0.529 Angstroms), and the remainder of the coefficients provided by the original paper. This screening function should be applicable to most systems. However, it is only accurate for small separations (i.e. less than 1 Angstrom).

For the Tersoff portion, [\\(f_R\\)]{.math .notranslate .nohighlight} is a two-body term and [\\(f_A\\)]{.math .notranslate .nohighlight} includes three-body interactions. The summations in the formula are over all neighbors J and K of atom I within a cutoff distance = R + D.

[\\(\\delta\\)]{.math .notranslate .nohighlight} is an optional negative shift of the equilibrium bond length, as described below.

Only a single pair_coeff command is used with the *tersoff/zbl* style which specifies a Tersoff/ZBL potential file with parameters for all needed elements. These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- N element names = mapping of Tersoff/ZBL elements to atom types

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for the potential file.

As an example, imagine the SiC.tersoff.zbl file has Tersoff/ZBL values for Si and C. If your LAMMPS simulation has 4 atoms types and you want the first 3 to be Si, and the fourth to be C, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * SiC.tersoff Si Si Si C
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The first three Si arguments map LAMMPS atom types 1,2,3 to the Si element in the Tersoff/ZBL file. The final C argument maps LAMMPS atom type 4 to the C element in the Tersoff/ZBL file. If a mapping value is specified as NULL, the mapping is not performed. This can be used when a *tersoff/zbl* potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials.

Tersoff/ZBL files in the *potentials* directory of the LAMMPS distribution have a ".tersoff.zbl" suffix. Lines that are not blank or comments (starting with #) define parameters for a triplet of elements. The parameters in a single entry correspond to coefficients in the formula above:

- element 1 (the center atom in a 3-body interaction)

- element 2 (the atom bonded to the center atom)

- element 3 (the atom influencing the 1-2 bond in a bond-order sense)

- m

- [\\(\\gamma\\)]{.math .notranslate .nohighlight}

- [\\(\\lambda_3\\)]{.math .notranslate .nohighlight} (1/distance units)

- c

- d

- [\\(\\cos\\theta_0\\)]{.math .notranslate .nohighlight} (can be a value \< -1 or \> 1)

- n

- [\\(\\beta\\)]{.math .notranslate .nohighlight}

- [\\(\\lambda_2\\)]{.math .notranslate .nohighlight} (1/distance units)

- B (energy units)

- R (distance units)

- D (distance units)

- [\\(\\lambda_1\\)]{.math .notranslate .nohighlight} (1/distance units)

- A (energy units)

- [\\(Z_i\\)]{.math .notranslate .nohighlight}

- [\\(Z_j\\)]{.math .notranslate .nohighlight}

- ZBLcut (distance units)

- ZBLexpscale (1/distance units)

The n, [\\(\\beta\\)]{.math .notranslate .nohighlight}, [\\(\\lambda_2\\)]{.math .notranslate .nohighlight}, B, [\\(\\lambda_1\\)]{.math .notranslate .nohighlight}, and A parameters are only used for two-body interactions. The m, [\\(\\gamma\\)]{.math .notranslate .nohighlight}, [\\(\\lambda_3\\)]{.math .notranslate .nohighlight}, c, d, and [\\(\\cos\\theta_0\\)]{.math .notranslate .nohighlight} parameters are only used for three-body interactions. The R and D parameters are used for both two-body and three-body interactions. The [\\(Z_i\\)]{.math .notranslate .nohighlight}, [\\(Z_j\\)]{.math .notranslate .nohighlight}, ZBLcut, ZBLexpscale parameters are used in the ZBL repulsive portion of the potential and in the Fermi-like function. The non-annotated parameters are unitless. The value of m must be 3 or 1.

The Tersoff/ZBL potential file must contain entries for all the elements listed in the pair_coeff command. It can also contain entries for additional elements not being used in a particular simulation; LAMMPS ignores those entries.

For a single-element simulation, only a single entry is required (e.g. SiSiSi). For a two-element simulation, the file must contain 8 entries (for SiSiSi, SiSiC, SiCSi, SiCC, CSiSi, CSiC, CCSi, CCC), that specify Tersoff parameters for all permutations of the two elements interacting in three-body configurations. Thus for 3 elements, 27 entries would be required, etc.

As annotated above, the first element in the entry is the center atom in a three-body interaction and it is bonded to the second atom and the bond is influenced by the third atom. Thus an entry for SiCC means Si bonded to a C with another C atom influencing the bond. Thus three-body parameters for SiCSi and SiSiC entries will not, in general, be the same. The parameters used for the two-body interaction come from the entry where the second element is repeated. Thus the two-body parameters for Si interacting with C, comes from the SiCC entry.

The parameters used for a particular three-body interaction come from the entry with the corresponding three elements. The parameters used only for two-body interactions (n, [\\(\\beta\\)]{.math .notranslate .nohighlight}, [\\(\\lambda_2\\)]{.math .notranslate .nohighlight}, B, [\\(\\lambda_1\\)]{.math .notranslate .nohighlight}, and A) in entries whose second and third element are different (e.g. SiCSi) are not used for anything and can be set to 0.0 if desired.

Note that the twobody parameters in entries such as SiCC and CSiSi are often the same, due to the common use of symmetric mixing rules, but this is not always the case. For example, the beta and n parameters in Tersoff_2 [[(Tersoff_2)]{.std .std-ref}](#zbl-tersoff-2){.reference .internal} are not symmetric.

We chose the above form so as to enable users to define all commonly used variants of the Tersoff portion of the potential. In particular, our form reduces to the original Tersoff form when m = 3 and gamma = 1, while it reduces to the form of [[Albe et al.]{.std .std-ref}](#zbl-albe){.reference .internal} when beta = 1 and m = 1. Note that in the current Tersoff implementation in LAMMPS, m must be specified as either 3 or 1. Tersoff used a slightly different but equivalent form for alloys, which we will refer to as Tersoff_2 potential [[(Tersoff_2)]{.std .std-ref}](#zbl-tersoff-2){.reference .internal}.

LAMMPS parameter values for Tersoff_2 can be obtained as follows: [\\(\\gamma = \\omega\_{ijk}\\)]{.math .notranslate .nohighlight}, [\\(\\lambda_3 = 0\\)]{.math .notranslate .nohighlight} and the value of m has no effect. The parameters for species i and j can be calculated using the Tersoff_2 mixing rules:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\lambda_1\^{i,j} & = \\frac{1}{2}(\\lambda_1\^i + \\lambda_1\^j)\\\\ \\lambda_2\^{i,j} & = \\frac{1}{2}(\\lambda_2\^i + \\lambda_2\^j)\\\\ A\_{i,j} & = (A\_{i}A\_{j})\^{1/2}\\\\ B\_{i,j} & = \\chi\_{ij}(B\_{i}B\_{j})\^{1/2}\\\\ R\_{i,j} & = (R\_{i}R\_{j})\^{1/2}\\\\ S\_{i,j} & = (S\_{i}S\_{j})\^{1/2}\\\\\\end{split}\\\]
:::

Tersoff_2 parameters R and S must be converted to the LAMMPS parameters R and D (R is different in both forms), using the following relations: R=(R'+S')/2 and D=(S'-R')/2, where the primes indicate the Tersoff_2 parameters.

In the potentials directory, the file SiCGe.tersoff provides the LAMMPS parameters for Tersoff's various versions of Si, as well as his alloy parameters for Si, C, and Ge. This file can be used for pure Si, (three different versions), pure C, pure Ge, binary SiC, and binary SiGe. LAMMPS will generate an error if this file is used with any combination involving C and Ge, since there are no entries for the GeC interactions (Tersoff did not publish parameters for this cross-interaction.) Tersoff files are also provided for the SiC alloy (SiC.tersoff) and the GaN (GaN.tersoff) alloys.

Many thanks to Rutuparna Narulkar, David Farrell, and Xiaowang Zhou for helping clarify how Tersoff parameters for alloys have been defined in various papers. Also thanks to Ram Devanathan for providing the base ZBL implementation.

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

For atom type pairs I,J and I != J, where types I and J correspond to two different element types, mixing is performed by LAMMPS as described above from values in the potential file.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the MANYBODY package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair style requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

The *shift* keyword is currently not supported for the *tersoff/gpu* and *tersoff/kk* variants of this pair style.

The tersoff/zbl potential files provided with LAMMPS (see the potentials directory) are parameterized for [["metal" units]{.doc}]units.md){.reference .internal}. Also the pair style supports converting potential file parameters on-the-fly between "metal" and "real" units. You can use the tersoff/zbl pair style with any LAMMPS units, but you would need to create your own tersoff/zbl potential file with coefficients listed in the appropriate units if your simulation does not use "metal" or "real" units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Tersoff_1)** J. Tersoff, Phys Rev B, 37, 6991 (1988).

**(ZBL)** J.F. Ziegler, J.P. Biersack, U. Littmark, 'Stopping and Ranges of Ions in Matter' Vol 1, 1985, Pergamon Press.

**(Albe)** J. Nord, K. Albe, P. Erhart and K. Nordlund, J. Phys.: Condens. Matter, 15, 5649(2003).

**(Tersoff_2)** J. Tersoff, Phys Rev B, 39, 5566 (1989); errata (PRB 41, 3248)
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

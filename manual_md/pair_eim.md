::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#pair-style-eim-command .section}
[]{#index-1}[]{#index-0}

# pair_style eim command[](#pair-style-eim-command "Link to this heading"){.headerlink}

Accelerator Variants: *eim/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style
:::
::::

- style = *eim*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style eim
    pair_coeff * * Na Cl ../potentials/ffield.eim Na Cl
    pair_coeff * * Na Cl ffield.eim  Na Na Na Cl
    pair_coeff * * Na Cl ../potentials/ffield.eim Cl NULL Na
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *eim* computes pairwise interactions for ionic compounds using embedded-ion method (EIM) potentials [[(Zhou)]{.std .std-ref}](#zhou2){.reference .internal}. The energy of the system E is given by

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{1}{2} \\sum\_{i=1}\^{N} \\sum\_{j=i_1}\^{i_N} \\phi\_{ij} \\left(r\_{ij}\\right) + \\sum\_{i=1}\^{N}E_i\\left(q_i,\\sigma_i\\right)\\\]
:::

The first term is a double pairwise sum over the J neighbors of all I atoms, where [\\(\\phi\_{ij}\\)]{.math .notranslate .nohighlight} is a pair potential. The second term sums over the embedding energy [\\(E_i\\)]{.math .notranslate .nohighlight} of atom I, which is a function of its charge [\\(q_i\\)]{.math .notranslate .nohighlight} and the electrical potential [\\(\\sigma_i\\)]{.math .notranslate .nohighlight} at its location. [\\(E_i\\)]{.math .notranslate .nohighlight}, [\\(q_i\\)]{.math .notranslate .nohighlight}, and [\\(\\sigma_i\\)]{.math .notranslate .nohighlight} are calculated as

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}q_i = & \\sum\_{j=i_1}\^{i_N} \\eta\_{ji}\\left(r\_{ij}\\right) \\\\ \\sigma_i = & \\sum\_{j=i_1}\^{i_N} q_j \\cdot \\psi\_{ij} \\left(r\_{ij}\\right) \\\\ E_i\\left(q_i,\\sigma_i\\right) = & \\frac{1}{2} \\cdot q_i \\cdot \\sigma_i\\end{split}\\\]
:::

where [\\(\\eta\_{ji}\\)]{.math .notranslate .nohighlight} is a pairwise function describing electron flow from atom I to atom J, and [\\(\\psi\_{ij}\\)]{.math .notranslate .nohighlight} is another pairwise function. The multi-body nature of the EIM potential is a result of the embedding energy term. A complete list of all the pair functions used in EIM is summarized below

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\phi\_{ij}\\left(r\\right) = & \\left\\{ \\begin{array}{lr} \\left\[\\frac{E\_{b,ij}\\beta\_{ij}}{\\beta\_{ij}-\\alpha\_{ij}}\\exp\\left(-\\alpha\_{ij} \\frac{r-r\_{e,ij}}{r\_{e,ij}}\\right)-\\frac{E\_{b,ij}\\alpha\_{ij}}{\\beta\_{ij}-\\alpha\_{ij}}\\exp\\left(-\\beta\_{ij} \\frac{r-r\_{e,ij}}{r\_{e,ij}}\\right)\\right\]f_c\\left(r,r\_{e,ij},r\_{c,\\phi,ij}\\right),& p\_{ij}=1 \\\\ \\left\[\\frac{E\_{b,ij}\\beta\_{ij}}{\\beta\_{ij}-\\alpha\_{ij}} \\left(\\frac{r\_{e,ij}}{r}\\right)\^{\\alpha\_{ij}} -\\frac{E\_{b,ij}\\alpha\_{ij}}{\\beta\_{ij}-\\alpha\_{ij}} \\left(\\frac{r\_{e,ij}}{r}\\right)\^{\\beta\_{ij}}\\right\]f_c\\left(r,r\_{e,ij},r\_{c,\\phi,ij}\\right),& p\_{ij}=2 \\end{array} \\right.\\\\ \\eta\_{ji} = & A\_{\\eta,ij}\\left(\\chi_j-\\chi_i\\right)f_c\\left(r,r\_{s,\\eta,ij},r\_{c,\\eta,ij}\\right) \\\\ \\psi\_{ij}\\left(r\\right) = & A\_{\\psi,ij}\\exp\\left(-\\zeta\_{ij}r\\right)f_c\\left(r,r\_{s,\\psi,ij},r\_{c,\\psi,ij}\\right) \\\\ f\_{c}\\left(r,r_p,r_c\\right) = & 0.510204 \\cdot \\mathrm{erfc}\\left\[\\frac{1.64498\\left(2r-r_p-r_c\\right)}{r_c-r_p}\\right\] - 0.010204\\end{split}\\\]
:::

Here [\\(E_b, r_e, r\_(c,\\phi), \\alpha, \\beta, A\_(\\psi), \\zeta, r\_(s,\\psi), r\_(c,\\psi), A\_(\\eta), r\_(s,\\eta), r\_(c,\\eta), \\chi,\\)]{.math .notranslate .nohighlight} and pair function type *p* are parameters, with subscripts *ij* indicating the two species of atoms in the atomic pair.

::: {.admonition .note}
Note

Even though the EIM potential is treating atoms as charged ions, you should not use a LAMMPS [[atom_style]{.doc}]atom_style.md){.reference .internal} that stores a charge on each atom and thus requires you to assign a charge to each atom, e.g. the *charge* or *full* atom styles. This is because the EIM potential infers the charge on an atom from the equation above for [\\(q_i\\)]{.math .notranslate .nohighlight}; you do not assign charges explicitly.
:::

------------------------------------------------------------------------

All the EIM parameters are listed in a potential file which is specified by the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command. This is an ASCII text file in a format described below. The "ffield.eim" file included in the "potentials" directory of the LAMMPS distribution currently includes nine elements Li, Na, K, Rb, Cs, F, Cl, Br, and I. A system with any combination of these elements can be modeled. This file is parameterized in terms of LAMMPS [[metal units]{.doc}]units.md){.reference .internal}.

Note that unlike other potentials, cutoffs for EIM potentials are not set in the pair_style or pair_coeff command; they are specified in the EIM potential file itself. Likewise, the EIM potential file lists atomic masses; thus you do not need to use the [[mass]{.doc}]mass.md){.reference .internal} command to specify them.

Only a single pair_coeff command is used with the *eim* style which specifies an EIM potential file and the element(s) to extract information for. The EIM elements are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- Elem1, Elem2, ...

- EIM potential file

- N element names = mapping of EIM elements to atom types

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for the potential file.

As an example like one of those above, suppose you want to model a system with Na and Cl atoms. If your LAMMPS simulation has 4 atoms types and you want the first 3 to be Na, and the fourth to be Cl, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * Na Cl ffield.eim Na Na Na Cl
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The filename is the EIM potential file. The Na and Cl arguments (before the file name) are the two elements for which info will be extracted from the potential file. The first three trailing Na arguments map LAMMPS atom types 1,2,3 to the EIM Na element. The final Cl argument maps LAMMPS atom type 4 to the EIM Cl element.

If a mapping value is specified as NULL, the mapping is not performed. This can be used when an *eim* potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials.

The ffield.eim file in the *potentials* directory of the LAMMPS distribution is formatted as follows:

Lines starting with \# are comments and are ignored by LAMMPS. Lines starting with "global:" include three global values. The first value divides the cations from anions, i.e., any elements with electronegativity above this value are viewed as anions, and any elements with electronegativity below this value are viewed as cations. The second and third values are related to the cutoff function - i.e. the 0.510204, 1.64498, and 0.010204 shown in the above equation can be derived from these values.

Lines starting with "element:" are formatted as follows: name of element, atomic number, atomic mass, electronic negativity, atomic radius (LAMMPS ignores it), ionic radius (LAMMPS ignores it), cohesive energy (LAMMPS ignores it), and q0 (must be 0).

Lines starting with "pair:" are entered as: element 1, element 2, r\_(c,phi), r\_(c,phi) (redundant for historical reasons), E_b, r_e, alpha, beta, r\_(c,eta), A\_(eta), r\_(s,eta), r\_(c,psi), A\_(psi), zeta, r\_(s,psi), and p.

The lines in the file can be in any order; LAMMPS extracts the info it needs.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This style is part of the MANYBODY package. It is only enabled if LAMMPS was built with that package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Zhou)** Zhou, submitted for publication (2010). Please contact Xiaowang Zhou (Sandia) for details via email at xzhou at sandia.gov.
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

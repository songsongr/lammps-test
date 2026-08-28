:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#pair-style-adp-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style adp command[](#pair-style-adp-command "Link to this heading"){.headerlink}

Accelerator Variants: *adp/kk*, *adp/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style adp
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style adp
    pair_coeff * * Ta.adp Ta
    pair_coeff * * ../potentials/AlCu.adp Al Al Cu
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *adp* computes pairwise interactions for metals and metal alloys using the angular dependent potential (ADP) of [[(Mishin)]{.std .std-ref}](#mishin){.reference .internal}, which is a generalization of the [[embedded atom method (EAM) potential]{.doc}]pair_eam.md){.reference .internal}. The LAMMPS implementation is discussed in [[(Singh)]{.std .std-ref}](#singh){.reference .internal}. The total energy Ei of an atom I is given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E_i & = F\_\\alpha \\left( \\sum\_{j\\neq i} \\rho\_\\beta (r\_{ij}) \\right) + \\frac{1}{2} \\sum\_{j\\neq i}\\phi\_{\\alpha\\beta}(r\_{ij})+ \\frac{1}{2} \\sum_s (\\mu_i\^s)\^2 + \\frac{1}{2} \\sum\_{s,t} (\\lambda_i\^{st})\^2 - \\frac{1}{6} \\nu_i\^2 \\\\ \\mu_i\^s & = \\sum\_{j\\neq i}u\_{\\alpha\\beta}(r\_{ij})r\_{ij}\^s\\\\ \\lambda_i\^{st} & = \\sum\_{j\\neq i}w\_{\\alpha\\beta}(r\_{ij})r\_{ij}\^sr\_{ij}\^t\\\\ \\nu_i & = \\sum_s\\lambda_i\^{ss}\\end{split}\\\]
:::

where [\\(F\\)]{.math .notranslate .nohighlight} is the embedding energy which is a function of the atomic electron density [\\(\\rho\\)]{.math .notranslate .nohighlight}, [\\(\\phi\\)]{.math .notranslate .nohighlight} is a pair potential interaction, [\\(\\alpha\\)]{.math .notranslate .nohighlight} and [\\(\\beta\\)]{.math .notranslate .nohighlight} are the element types of atoms [\\(I\\)]{.math .notranslate .nohighlight} and [\\(J\\)]{.math .notranslate .nohighlight}, and [\\(s\\)]{.math .notranslate .nohighlight} and [\\(t = 1,2,3\\)]{.math .notranslate .nohighlight} and refer to the cartesian coordinates. The [\\(\\mu\\)]{.math .notranslate .nohighlight} and [\\(\\lambda\\)]{.math .notranslate .nohighlight} terms represent the dipole and quadruple distortions of the local atomic environment which extend the original EAM framework by introducing angular forces.

Note that unlike for other potentials, cutoffs for ADP potentials are not set in the pair_style or pair_coeff command; they are specified in the ADP potential files themselves. Likewise, the ADP potential files list atomic masses; thus you do not need to use the [[mass]{.doc}]mass.md){.reference .internal} command to specify them.

**ADP potentials are available from:**

- The NIST WWW site at [https://www.ctcms.nist.gov/potentials/](https://www.ctcms.nist.gov/potentials/){.reference .external}. Note that ADP potentials obtained from NIST must be converted into the extended DYNAMO *setfl* format discussed below.

- The OpenKIM Project at [https://openkim.org/browse/models/by-type](https://openkim.org/browse/models/by-type){.reference .external} provides ADP potentials that can be used directly in LAMMPS with the [[kim command]{.doc}]kim_commands.md){.reference .internal} interface.

------------------------------------------------------------------------

Only a single pair_coeff command is used with the *adp* style which specifies an extended DYNAMO *setfl* file, which contains information for [\\(M\\)]{.math .notranslate .nohighlight} elements. These are mapped to LAMMPS atom types by specifying [\\(N\\)]{.math .notranslate .nohighlight} additional arguments after the filename in the pair_coeff command, where [\\(N\\)]{.math .notranslate .nohighlight} is the number of LAMMPS atom types:

- filename

- [\\(N\\)]{.math .notranslate .nohighlight} element names = mapping of extended *setfl* elements to atom types

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for the potential file.

As an example, the potentials/AlCu.adp file, included in the potentials directory of the LAMMPS distribution, is an extended *setfl* file which has tabulated ADP values for w elements and their alloy interactions: Cu and Al. If your LAMMPS simulation has 4 atoms types and you want the first 3 to be Al, and the fourth to be Cu, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * AlCu.adp Al Al Al Cu
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The first three Al arguments map LAMMPS atom types 1,2,3 to the Al element in the extended *setfl* file. The final Cu argument maps LAMMPS atom type 4 to the Al element in the extended *setfl* file. Note that there is no requirement that your simulation use all the elements specified by the extended *setfl* file.

If a mapping value is specified as NULL, the mapping is not performed. This can be used when an *adp* potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials.

*Adp* files in the *potentials* directory of the LAMMPS distribution have an ".adp" suffix. A DYNAMO *setfl* file extended for ADP is formatted as follows. Basically it is the standard *setfl* format with additional tabulated functions u and w added to the file after the tabulated pair potentials. See the [[pair_eam]{.doc}]pair_eam.md){.reference .internal} command for further details on the *setfl* format.

- lines 1,2,3 = comments (ignored)

- line 4: [\\(N\_{\\text{elements}}\\)]{.math .notranslate .nohighlight} Element1 Element2 ... ElementN

- line 5: [\\(N\_{\\rho}\\)]{.math .notranslate .nohighlight}, [\\(d\_{\\rho}\\)]{.math .notranslate .nohighlight}, [\\(N_r\\)]{.math .notranslate .nohighlight}, [\\(d_r\\)]{.math .notranslate .nohighlight}, cutoff

Following the 5 header lines are [\\(N\_{\\text{elements}}\\)]{.math .notranslate .nohighlight} sections, one for each element, each with the following format:

- line 1 = atomic number, mass, lattice constant, lattice type (e.g. FCC)

- embedding function [\\(F(\\rho)\\)]{.math .notranslate .nohighlight} ([\\(N\_{\\rho}\\)]{.math .notranslate .nohighlight} values)

- density function [\\(\\rho(r)\\)]{.math .notranslate .nohighlight} ([\\(N_r\\)]{.math .notranslate .nohighlight} values)

Following the [\\(N\_{\\text{elements}}\\)]{.math .notranslate .nohighlight} sections, [\\(N_r\\)]{.math .notranslate .nohighlight} values for each pair potential [\\(\\phi(r)\\)]{.math .notranslate .nohighlight} array are listed for all [\\(i,j\\)]{.math .notranslate .nohighlight} element pairs in the same format as other arrays. Since these interactions are symmetric ([\\(i,j = j,i\\)]{.math .notranslate .nohighlight}) only [\\(\\phi\\)]{.math .notranslate .nohighlight} arrays with [\\(i \\geq j\\)]{.math .notranslate .nohighlight} are listed, in the following order:

::: {.math .notranslate .nohighlight}
\\\[i,j = (1,1), (2,1), (2,2), (3,1), (3,2), (3,3), (4,1), \..., (N\_{\\text{elements}},N\_{\\text{elements}}).\\\]
:::

The tabulated values for each [\\(\\phi\\)]{.math .notranslate .nohighlight} function are listed as [\\(r\*\\phi\\)]{.math .notranslate .nohighlight} (in units of eV-Angstroms), since they are for atom pairs, the same as for [[other EAM files]{.doc}]pair_eam.md){.reference .internal}.

After the [\\(\\phi(r)\\)]{.math .notranslate .nohighlight} arrays, each of the [\\(u(r)\\)]{.math .notranslate .nohighlight} arrays are listed in the same order with the same assumptions of symmetry. Directly following the [\\(u(r)\\)]{.math .notranslate .nohighlight}, the [\\(w(r)\\)]{.math .notranslate .nohighlight} arrays are listed. Note that [\\(\\phi(r)\\)]{.math .notranslate .nohighlight} is the only array tabulated with a scaling by [\\(r\\)]{.math .notranslate .nohighlight}.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, where types I and J correspond to two different element types, no special mixing rules are needed, since the ADP potential files specify alloy interactions explicitly.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in tabulated potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the MANYBODY package. It is only enabled if LAMMPS was built with that package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_eam]{.doc}]pair_eam.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Mishin)** Mishin, Mehl, and Papaconstantopoulos, Acta Mater, 53, 4029 (2005).

**(Singh)** Singh and Warner, Acta Mater, 58, 5797-5805 (2010),
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

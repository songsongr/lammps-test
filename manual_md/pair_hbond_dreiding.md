::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-hbond-dreiding-lj-command .section}
[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style hbond/dreiding/lj command[](#pair-style-hbond-dreiding-lj-command "Link to this heading"){.headerlink}

Accelerator Variants: *hbond/dreiding/lj/omp*
:::

::: {#pair-style-hbond-dreiding-lj-angleoffset-command .section}
# pair_style hbond/dreiding/lj/angleoffset command[](#pair-style-hbond-dreiding-lj-angleoffset-command "Link to this heading"){.headerlink}

Accelerator Variants: *hbond/dreiding/lj/angleoffset/omp*
:::

::: {#pair-style-hbond-dreiding-morse-command .section}
# pair_style hbond/dreiding/morse command[](#pair-style-hbond-dreiding-morse-command "Link to this heading"){.headerlink}

Accelerator Variants: *hbond/dreiding/morse/omp*
:::

:::::::::::::::::::::::: {#pair-style-hbond-dreiding-morse-angleoffset-command .section}
# pair_style hbond/dreiding/morse/angleoffset command[](#pair-style-hbond-dreiding-morse-angleoffset-command "Link to this heading"){.headerlink}

Accelerator Variants: *hbond/dreiding/morse/angleoffset/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style N inner_distance_cutoff outer_distance_cutoff angle_cutoff equilibrium_angle
:::
::::

- style = *hbond/dreiding/lj* or *hbond/dreiding/morse* or *hbond/dreiding/lj/angleoffset* or *hbond/dreiding/morse/angleoffset*

- N = power of cosine of angle theta (integer)

- inner_distance_cutoff = global inner cutoff for Donor-Acceptor interactions (distance units)

- outer_distance_cutoff = global cutoff for Donor-Acceptor interactions (distance units)

- angle_cutoff = global angle cutoff for Acceptor-Hydrogen-Donor interactions (degrees)

- (with style angleoffset) equilibrium_angle = global equilibrium angle for Acceptor-Hydrogen-Donor interactions (degrees)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay lj/cut 10.0 hbond/dreiding/lj 4 9.0 11.0 90.0
    pair_coeff 1 2 hbond/dreiding/lj 3 i 9.5 2.75 4 9.0 11.0 90.0

    pair_style hybrid/overlay lj/cut 10.0 hbond/dreiding/morse 2 9.0 11.0 90.0
    pair_coeff 1 2 hbond/dreiding/morse 3 i 3.88 1.7241379 2.9 2 9.0 11.0 90.0

    labelmap atom 1 C 2 O 3 H
    pair_coeff C O hbond/dreiding/morse H i 3.88 1.7241379 2.9 2 9.0 11.0 90.0

    pair_style hybrid/overlay lj/cut 10.0 hbond/dreiding/lj 4 9.0 11.0 90 170.0
    pair_coeff 1 2 hbond/dreiding/lj 3 i 9.5 2.75 4 9.0 11.0 90.0
:::
::::
:::::

::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *hbond/dreiding* styles compute the Acceptor-Hydrogen-Donor (AHD) 3-body hydrogen bond interaction for the [[DREIDING]{.doc}]Howto_bioFF.md){.reference .internal} force field, given by:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\left\[LJ(r) \| Morse(r) \\right\] \\qquad \\qquad \\qquad r \< r\_\\mathrm{in} \\\\ = & S(r) \* \\left\[LJ(r) \| Morse(r) \\right\] \\qquad \\qquad r\_\\mathrm{in} \< r \< r\_\\mathrm{out} \\\\ = & 0 \\qquad \\qquad \\qquad \\qquad \\qquad \\qquad \\qquad r \> r\_\\mathrm{out} \\\\ LJ(r) = & AR\^{-12}-BR\^{-10}cos\^n\\theta= \\epsilon\\left\\lbrace 5\\left\[ \\frac{\\sigma}{r}\\right\]\^{12}- 6\\left\[ \\frac{\\sigma}{r}\\right\]\^{10} \\right\\rbrace cos\^n\\theta\\\\ Morse(r) = & D_0\\left\\lbrace \\chi\^2 - 2\\chi\\right\\rbrace cos\^n\\theta= D\_{0}\\left\\lbrace e\^{- 2 \\alpha (r - r_0)} - 2 e\^{- \\alpha (r - r_0)} \\right\\rbrace cos\^n\\theta \\\\ S(r) = & \\frac{ \\left\[r\_\\mathrm{out}\^2 - r\^2\\right\]\^2 \\left\[r\_\\mathrm{out}\^2 + 2r\^2 - 3{r\_\\mathrm{in}\^2}\\right\]} { \\left\[r\_\\mathrm{out}\^2 - {r\_\\mathrm{in}}\^2\\right\]\^3 }\\end{split}\\\]
:::

where [\\(r\_\\mathrm{in}\\)]{.math .notranslate .nohighlight} is the inner spline distance cutoff, [\\(r\_\\mathrm{out}\\)]{.math .notranslate .nohighlight} is the outer distance cutoff, [\\(\\theta_c\\)]{.math .notranslate .nohighlight} is the angle cutoff, and [\\(n\\)]{.math .notranslate .nohighlight} is the power of the cosine of the angle [\\(\\theta\\)]{.math .notranslate .nohighlight}.

Here, *r* is the radial distance between the donor (D) and acceptor (A) atoms and [\\(\\theta\\)]{.math .notranslate .nohighlight} is the bond angle between the acceptor, the hydrogen (H) and the donor atoms:

![](_images/dreiding_hbond.jpg){.align-center}

These 3-body interactions can be defined for pairs of acceptor and donor atoms, based on atom types. For each donor/acceptor atom pair, the third atom in the interaction is a hydrogen permanently bonded to the donor atom, e.g. in a bond list read in from a data file via the [[read_data]{.doc}]read_data.md){.reference .internal} command. The atom types of possible hydrogen atoms for each donor/acceptor type pair are specified by the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command (see below).

Style *hbond/dreiding/lj* is the original DREIDING potential of [[(Mayo)]{.std .std-ref}](#pair-mayo){.reference .internal}. It uses a LJ 12/10 functional for the Donor-Acceptor interactions. To match the results in the original paper, use n = 4.

Style *hbond/dreiding/morse* is an improved version using a Morse potential for the Donor-Acceptor interactions. [[(Liu)]{.std .std-ref}](#liu){.reference .internal} showed that the Morse form gives improved results for Dendrimer simulations, when n = 2.

::: versionadded
[Added in version 4Feb2025.]{.versionmodified .added}
:::

The style variants *hbond/dreiding/lj/angleoffset* and *hbond/dreiding/lj/angleoffset* take the equilibrium angle of the AHD as input, allowing it to reach 180 degrees. This variant option was added to account for cases (especially in some coarse-grained models) in which the equilibrium state of the bonds may equal the minimum energy state.

See the [[Howto bioFF]{.doc}]Howto_bioFF.md){.reference .internal} page for more information on the DREIDING force field.

::: {.admonition .note}
Note

Because the Dreiding hydrogen bond potential is only one portion of an overall force field which typically includes other pairwise interactions, it is common to use it as a sub-style in a [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} command, where another pair style provides the repulsive core interaction between pairs of atoms, e.g. a 1/r\^12 Lennard-Jones repulsion.
:::

::: {.admonition .note}
Note

When using the hbond/dreiding pair styles with [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}, you should explicitly define pair interactions between the donor atom and acceptor atoms, (as well as between these atoms and ALL other atoms in your system). Whenever [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} is used, ordinary mixing rules are not applied to atoms like the donor and acceptor atoms because they are typically referenced in multiple pair styles. Neglecting to do this can cause difficult-to-detect physics problems.
:::

::: {.admonition .note}
Note

In the original Dreiding force field paper 1-4 non-bonded interactions ARE allowed. If this is desired for your model, use the special_bonds command (e.g. "special_bonds lj 0.0 0.0 1.0") to turn these interactions on.
:::

::: {.admonition .note}
Note

For the *angleoffset* variants, the referenced angle offset is the supplementary angle of the equilibrium angle parameter. It means if the equilibrium angle is 166.6 degrees, the calculated angle offset is 13.4 degrees.
:::

------------------------------------------------------------------------

The following coefficients must be defined for pairs of eligible donor/acceptor types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above.

::: {.admonition .note}
Note

Unlike other pair styles and their associated [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} commands, you do not need to specify pair_coeff settings for all possible I,J type pairs. Only I,J type pairs for atoms which act as joint donors/acceptors need to be specified; all other type pairs are assumed to be inactive.
:::

::: {.admonition .note}
Note

A [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command can be specified multiple times for the same donor/acceptor type pair. This enables multiple hydrogen types to be assigned to the same donor/acceptor type pair. For other pair_styles, if the pair_coeff command is re-used for the same I.J type pair, the settings for that type pair are overwritten. For the hydrogen bond potentials this is not the case; the settings are cumulative. This means the only way to turn off a previous setting, is to re-use the pair_style command and start over.
:::

For the *hbond/dreiding/lj* style the list of coefficients is as follows:

- K = hydrogen atom type = 1 to Ntypes, or type label

- donor flag = *i* or *j*

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- *n* = exponent in formula above

- distance cutoff [\\(r\_\\mathrm{in}\\)]{.math .notranslate .nohighlight} (distance units)

- distance cutoff [\\(r\_\\mathrm{out}\\)]{.math .notranslate .nohighlight} (distance units)

- angle cutoff (degrees)

For the *hbond/dreiding/morse* style the list of coefficients is as follows:

- K = hydrogen atom type = 1 to Ntypes, or type label

- donor flag = *i* or *j*

- [\\(D_0\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (1/distance units)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance units)

- *n* = exponent in formula above

- distance cutoff [\\(r\_\\mathrm{in}\\)]{.math .notranslate .nohighlight} (distance units)

- distance cutoff [\\(r\_{out}\\)]{.math .notranslate .nohighlight} (distance units)

- angle cutoff (degrees)

For both the *hbond/dreiding/lj/angleoffset* and *hbond/dreiding/morse/angleoffset* styles an additional parameter is added: \* equilibrium angle (degrees)

For all styles, a single hydrogen atom type K can be specified, or a wild-card asterisk can be used in place of or in conjunction with the K arguments to select multiple types as hydrogen atoms. This takes the form "\*" or "\*n" or "n\*" or "m\*n". See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command page for details.

If the donor flag is *i*, then the atom of type I in the pair_coeff command is treated as the donor, and J is the acceptor. If the donor flag is *j*, then the atom of type J in the pair_coeff command is treated as the donor and I is the donor. This option is required because the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command requires that I \<= J.

[\\(\\epsilon\\)]{.math .notranslate .nohighlight} and [\\(\\sigma\\)]{.math .notranslate .nohighlight} are settings for the hydrogen bond potential based on a Lennard-Jones functional form. Note that sigma is defined as the zero-crossing distance for the potential, not as the energy minimum at [\\(2\^{1/6} \\sigma\\)]{.math .notranslate .nohighlight}.

[\\(D_0\\)]{.math .notranslate .nohighlight} and [\\(\\alpha\\)]{.math .notranslate .nohighlight} and [\\(r_0\\)]{.math .notranslate .nohighlight} are settings for the hydrogen bond potential based on a Morse functional form.

The last 3 coefficients for both styles are optional. If not specified, the global n, distance cutoff, and angle cutoff specified in the pair_style command are used. If you wish to only override the second or third optional parameter, you must also specify the preceding optional parameters.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::::::

------------------------------------------------------------------------

::::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

These pair styles do not support mixing. You must explicitly identify each donor/acceptor type pair.

These styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the interactions.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for these pair styles.

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

These pair styles do not write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands need to be re-specified in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.

These pair styles tally a count of how many hydrogen bonding interactions they calculate each timestep and the hbond energy. These quantities can be accessed via the [[compute pair]{.doc}]compute_pair.md){.reference .internal} command as a vector of values of length 2.

To print these quantities to the log file (with a descriptive column heading) the following commands could be included in an input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute hb all pair hbond/dreiding/lj
    variable n_hbond equal c_hb[1] #number hbonds
    variable E_hbond equal c_hb[2] #hbond energy
    thermo_style custom step temp epair v_E_hbond
:::
::::
:::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The base pair styles can only be used if LAMMPS was built with the MOLECULE package. The *angleoffset* variant also requires the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Mayo)** Mayo, Olfason, Goddard III, J Phys Chem, 94, 8897-8909 (1990).

**(Liu)** Liu, Bryantsev, Diallo, Goddard III, J. Am. Chem. Soc 131 (8) 2798 (2009)
:::
::::::::::::::::::::::::
::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::

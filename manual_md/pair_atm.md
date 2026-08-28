::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::: {#pair-style-atm-command .section}
[]{#index-0}

# pair_style atm command[](#pair-style-atm-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style atm cutoff cutoff_triple
:::
::::

- cutoff = cutoff for each pair in 3-body interaction (distance units)

- cutoff_triple = additional cutoff applied to product of 3 pairwise distances (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style atm 4.5 2.5
    pair_coeff * * * 0.072

    pair_style hybrid/overlay lj/cut 6.5 atm 4.5 2.5
    pair_coeff * * lj/cut 1.0 1.0
    pair_coeff 1 1 atm 1 0.064
    pair_coeff 1 1 atm 2 0.080
    pair_coeff 1 2 atm 2 0.100
    pair_coeff 2 2 atm 2 0.125
:::
::::
:::::

:::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *atm* style computes a 3-body [[Axilrod-Teller-Muto]{.std .std-ref}](#axilrod){.reference .internal} potential for the energy E of a system of atoms as

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = \\nu\\frac{1+3\\cos\\gamma_1\\cos\\gamma_2\\cos\\gamma_3}{r\_{12}\^3r\_{23}\^3r\_{31}\^3} \\\\\\end{split}\\\]
:::

where [\\(\\nu\\)]{.math .notranslate .nohighlight} is the three-body interaction strength. The distances between pairs of atoms [\\(r\_{12}\\)]{.math .notranslate .nohighlight}, [\\(r\_{23}\\)]{.math .notranslate .nohighlight}, [\\(r\_{31}\\)]{.math .notranslate .nohighlight} and the angles [\\(\\gamma_1\\)]{.math .notranslate .nohighlight}, [\\(\\gamma_2\\)]{.math .notranslate .nohighlight}, [\\(\\gamma_3\\)]{.math .notranslate .nohighlight} are as shown in this diagram:

![](_images/pair_atm_dia.jpg){.align-center}

Note that for the interaction between a triplet of atoms [\\(I,J,K\\)]{.math .notranslate .nohighlight}, there is no "central" atom. The interaction is symmetric with respect to permutation of the three atoms. Thus the [\\(\\nu\\)]{.math .notranslate .nohighlight} value is the same for all those permutations of the atom types of [\\(I,J,K\\)]{.math .notranslate .nohighlight} and needs to be specified only once, as discussed below.

The *atm* potential is typically used in combination with a two-body potential using the [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} command as in the example above.

The potential for a triplet of atom is calculated only if all 3 distances [\\(r\_{12}\\)]{.math .notranslate .nohighlight}, [\\(r\_{23}\\)]{.math .notranslate .nohighlight}, [\\(r\_{31}\\)]{.math .notranslate .nohighlight} between the three atoms satisfy [\\(r\_{IJ} \< \\text{cutoff}\\)]{.math .notranslate .nohighlight}. In addition, the product of the 3 distances [\\(r\_{12} r\_{23} r\_{31}\\)]{.math .notranslate .nohighlight} \< cutoff_triple [\\(\^3\\)]{.math .notranslate .nohighlight} is required, which excludes from calculation the triplets with small contribution to the interaction.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the restart files read by the [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} = atom type of the third atom (1 to [\\(N\_{\\text{types}}\\)]{.math .notranslate .nohighlight})

- [\\(\\nu\\)]{.math .notranslate .nohighlight} = prefactor (energy/distance\^9 units)

[\\(K\\)]{.math .notranslate .nohighlight} can be specified in one of two ways. An explicit numeric value or type label can be used, as in the second example above. LAMMPS sets the coefficients for the other 5 symmetric interactions to the same values. E.g. if [\\(I = 1\\)]{.math .notranslate .nohighlight}, [\\(J = 2\\)]{.math .notranslate .nohighlight}, [\\(K = 3\\)]{.math .notranslate .nohighlight}, then these 6 values are set to the specified [\\(\\nu\\)]{.math .notranslate .nohighlight}: [\\(\\nu\_{123}\\)]{.math .notranslate .nohighlight}, [\\(\\nu\_{132}\\)]{.math .notranslate .nohighlight}, [\\(\\nu\_{213}\\)]{.math .notranslate .nohighlight}, [\\(\\nu\_{231}\\)]{.math .notranslate .nohighlight}, [\\(\\nu\_{312}\\)]{.math .notranslate .nohighlight}, [\\(\\nu\_{321}\\)]{.math .notranslate .nohighlight}. This enforces the symmetry discussed above.

A wildcard asterisk can be used for K to set the coefficients for multiple triplets of atom types. This takes the form "\*" or "\*n" or "n\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} equals the number of atom types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to [\\(n\\)]{.math .notranslate .nohighlight} (inclusive). A trailing asterisk means all types from [\\(n\\)]{.math .notranslate .nohighlight} to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from [\\(m\\)]{.math .notranslate .nohighlight} to [\\(n\\)]{.math .notranslate .nohighlight} (inclusive). Note that only type triplets with [\\(J \\leq K\\)]{.math .notranslate .nohighlight} are considered; if asterisks imply type triplets where [\\(K \< J\\)]{.math .notranslate .nohighlight}, they are ignored.

Note that a pair_coeff command can override a previous setting for the same [\\(I,J,K\\)]{.math .notranslate .nohighlight} triplet. For example, these commands set [\\(\\nu\\)]{.math .notranslate .nohighlight} for all [\\(I,J.K\\)]{.math .notranslate .nohighlight} triplets, then overwrite nu for just the [\\(I,J,K = 2,3,4\\)]{.math .notranslate .nohighlight} triplet:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * * 0.25
    pair_coeff 2 3 4 0.1
:::
::::

Note that for a simulation with a single atom type, only a single entry is required, e.g.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff 1 1 1 0.25
:::
::::

For a simulation with two atom types, four pair_coeff commands will specify all possible nu values:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff 1 1 1 nu1
    pair_coeff 1 1 2 nu2
    pair_coeff 1 2 2 nu3
    pair_coeff 2 2 2 nu4
:::
::::

For a simulation with three atom types, ten pair_coeff commands will specify all possible nu values:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff 1 1 1 nu1
    pair_coeff 1 1 2 nu2
    pair_coeff 1 1 3 nu3
    pair_coeff 1 2 2 nu4
    pair_coeff 1 2 3 nu5
    pair_coeff 1 3 3 nu6
    pair_coeff 2 2 2 nu7
    pair_coeff 2 2 3 nu8
    pair_coeff 2 3 3 nu9
    pair_coeff 3 3 3 nu10
:::
::::

By default the [\\(\\nu\\)]{.math .notranslate .nohighlight} value for all triplets is set to 0.0. Thus it is not required to provide pair_coeff commands that enumerate triplet interactions for all [\\(K\\)]{.math .notranslate .nohighlight} types. If some [\\(I,J,K\\)]{.math .notranslate .nohighlight} combination is not specified, then there will be no 3-body ATM interactions for that combination and all its permutations. However, as with all pair styles, it is required to specify a pair_coeff command for all [\\(I,J\\)]{.math .notranslate .nohighlight} combinations, else an error will result.
::::::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} mix, shift, table, and tail options.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file. However, if the *atm* potential is used in combination with other potentials using the [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} command then pair_coeff commands need to be re-specified in the restart input script.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, and *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the MANYBODY package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Axilrod)** Axilrod and Teller, J Chem Phys, 11, 299 (1943); Muto, Nippon Sugaku-Buturigakkwaishi 17, 629 (1943).
:::
:::::::::::::::::::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#pair-style-ufm-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style ufm command[](#pair-style-ufm-command "Link to this heading"){.headerlink}

Accelerator Variants: *ufm/gpu*, *ufm/omp*, *ufm/opt*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style ufm cutoff
:::
::::

- cutoff = global cutoff for *ufm* interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style ufm 4.0
    pair_coeff 1 1 100.0 1.0 2.5
    pair_coeff * * 100.0 1.0

    pair_style ufm 4.0
    pair_coeff * * 10.0 1.0
    variable prefactor equal ramp(10,100)
    fix 1 all adapt 1 pair ufm epsilon * * v_prefactor
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *ufm* computes pairwise interactions using the Uhlenbeck-Ford model (UFM) potential [[(Paula Leite2016)]{.std .std-ref}](#pl2){.reference .internal} which is given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = -\\varepsilon\\, \\ln{\\left\[1-\\exp{\\left(-r\^{2}/\\sigma\^{2}\\right)}\\right\]} \\qquad r \< r_c \\\\ \\varepsilon & = p\\,k_B\\,T\\end{split}\\\]
:::

where [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff, [\\(\\sigma\\)]{.math .notranslate .nohighlight} is a distance-scale and [\\(\\epsilon\\)]{.math .notranslate .nohighlight} is an energy-scale, i.e., a product of Boltzmann constant [\\(k_B\\)]{.math .notranslate .nohighlight}, temperature [\\(T\\)]{.math .notranslate .nohighlight} and the Uhlenbeck-Ford p-parameter which is responsible to control the softness of the interactions [[(Paula Leite2017)]{.std .std-ref}](#pl1){.reference .internal}. This model is useful as a reference system for fluid-phase free-energy calculations [[(Paula Leite2016)]{.std .std-ref}](#pl2){.reference .internal}.

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- cutoff (distance units)

The last coefficient is optional. If not specified, the global *ufm* cutoff is used.

The [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command can be used to vary epsilon and sigma for this pair style over the course of a simulation, in which case pair_coeff settings for epsilon and sigma must still be specified, but will be overridden. For example these commands will vary the prefactor epsilon for all pairwise interactions from 10.0 at the beginning to 100.0 at the end of a run:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable prefactor equal ramp(10,100)
    fix 1 all adapt 1 pair ufm epsilon * * v_prefactor
:::
::::

::: {.admonition .note}
Note

The thermodynamic integration procedure can be performed with this potential using [[fix adapt]{.doc}]fix_adapt.md){.reference .internal}. This command will rescale the force on each atom by varying a scale variable, which always starts with value 1.0. The syntax is the same described above, however, changing epsilon to scale. A detailed explanation of how to use this command and perform nonequilibrium thermodynamic integration in LAMMPS is given in the paper by [[(Freitas)]{.std .std-ref}](#freitas2){.reference .internal}.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the epsilon and sigma coefficients and cutoff distance for this pair style can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

This pair style support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table and tail are not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the EXTRA-PAIR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix adapt]{.doc}]fix_adapt.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

**(Paula Leite2017)** Paula Leite, Santos-Florez, and de Koning, Phys Rev E, 96, 32115 (2017).

**(Paula Leite2016)** Paula Leite , Freitas, Azevedo, and de Koning, J Chem Phys, 126, 044509 (2016).

**(Freitas)** Freitas, Asta, and de Koning, Computational Materials Science, 112, 333 (2016).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

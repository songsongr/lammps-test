:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#pair-style-soft-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style soft command[](#pair-style-soft-command "Link to this heading"){.headerlink}

Accelerator Variants: *soft/gpu*, *soft/kk*, *soft/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style soft cutoff
:::
::::

- cutoff = global cutoff for soft interactions (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style soft 1.0
    pair_coeff * * 10.0
    pair_coeff 1 1 10.0 3.0

    pair_style soft 1.0
    pair_coeff * * 0.0
    variable prefactor equal ramp(0,30)
    fix 1 all adapt 1 pair soft a * * v_prefactor
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *soft* computes pairwise interactions with the formula

::: {.math .notranslate .nohighlight}
\\\[E = A \\left\[ 1 + \\cos\\left(\\frac{\\pi r}{r_c}\\right) \\right\] \\qquad r \< r_c\\\]
:::

It is useful for pushing apart overlapping atoms, since it does not blow up as r goes to 0. A is a prefactor that can be made to vary in time from the start to the end of the run (see discussion below), e.g. to start with a very soft potential and slowly harden the interactions over time. [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff. See the [[fix nve/limit]{.doc}]fix_nve_limit.md){.reference .internal} command for another way to push apart overlapping atoms.

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- A (energy units)

- cutoff (distance units)

The last coefficient is optional. If not specified, the global soft cutoff is used.

::: {.admonition .note}
Note

The syntax for [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} with a single A coeff is different in the current version of LAMMPS than in older versions which took two values, Astart and Astop, to ramp between them. This functionality is now available in a more general form through the [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command, as explained below. Note that if you use an old input script and specify Astart and Astop without a cutoff, then LAMMPS will interpret that as A and a cutoff, which is probably not what you want.
:::

The [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command can be used to vary A for one or more pair types over the course of a simulation, in which case pair_coeff settings for A must still be specified, but will be overridden. For example these commands will vary the prefactor A for all pairwise interactions from 0.0 at the beginning to 30.0 at the end of a run:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable prefactor equal ramp(0,30)
    fix 1 all adapt 1 pair soft a * * v_prefactor
:::
::::

Note that a formula defined by an [[equal-style variable]{.doc}]variable.md){.reference .internal} can use the current timestep, elapsed time in the current run, elapsed time since the beginning of a series of runs, as well as access other variables.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the A coefficient and cutoff distance for this pair style can be mixed. A is always mixed via a *geometric* rule. The cutoff is mixed according to the pair_modify mix value. The default mix value is *geometric*. See the "pair_modify" command for details.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option, since the pair interaction goes to 0.0 at the cutoff.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table and tail options are not relevant for this pair style.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix nve/limit]{.doc}]fix_nve_limit.md){.reference .internal}, [[fix adapt]{.doc}]fix_adapt.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

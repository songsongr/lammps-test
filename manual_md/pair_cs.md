:::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-born-coul-dsf-cs-command .section}
[]{#index-10}[]{#index-9}[]{#index-8}[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style born/coul/dsf/cs command[](#pair-style-born-coul-dsf-cs-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-born-coul-long-cs-command .section}
# pair_style born/coul/long/cs command[](#pair-style-born-coul-long-cs-command "Link to this heading"){.headerlink}

Accelerator Variants: *born/coul/long/cs/gpu*
:::

::: {#pair-style-born-coul-wolf-cs-command .section}
# pair_style born/coul/wolf/cs command[](#pair-style-born-coul-wolf-cs-command "Link to this heading"){.headerlink}

Accelerator Variants: *born/coul/wolf/cs/gpu*
:::

::: {#pair-style-buck-coul-long-cs-command .section}
# pair_style buck/coul/long/cs command[](#pair-style-buck-coul-long-cs-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-coul-long-cs-command .section}
# pair_style coul/long/cs command[](#pair-style-coul-long-cs-command "Link to this heading"){.headerlink}

Accelerator Variants: *coul/long/cs/gpu*
:::

::: {#pair-style-coul-wolf-cs-command .section}
# pair_style coul/wolf/cs command[](#pair-style-coul-wolf-cs-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-lj-cut-coul-long-cs-command .section}
# pair_style lj/cut/coul/long/cs command[](#pair-style-lj-cut-coul-long-cs-command "Link to this heading"){.headerlink}
:::

::::::::::::::: {#pair-style-lj-class2-coul-long-cs-command .section}
# pair_style lj/class2/coul/long/cs command[](#pair-style-lj-class2-coul-long-cs-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *born/coul/dsf/cs* or *born/coul/long/cs* or *born/coul/wolf/cs* or *buck/coul/long/cs* or *coul/long/cs* or *coul/wolf/cs* or *lj/cut/coul/long/cs* or *lj/class2/coul/long/cs*

- args = list of arguments for a particular style

``` literal-block
born/coul/dsf/cs args = alpha cutoff (cutoff2)
  alpha = damping parameter (inverse distance units)
  cutoff = global cutoff for non-Coulombic (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (distance units)
born/coul/long/cs args = cutoff (cutoff2)
  cutoff = global cutoff for non-Coulombic (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
born/coul/wolf/cs args = alpha cutoff (cutoff2)
  alpha = damping parameter (inverse distance units)
  cutoff = global cutoff for Buckingham (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
buck/coul/long/cs args = cutoff (cutoff2)
  cutoff = global cutoff for Buckingham (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
coul/long args = cutoff
  cutoff = global cutoff for Coulombic (distance units)
coul/wolf args = alpha cutoff
  alpha = damping parameter (inverse distance units)
  cutoff = global cutoff for Coulombic (distance units)
lj/cut/coul/long/cs args = cutoff (cutoff2)
  cutoff = global cutoff for LJ (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
lj/class2/coul/long/cs args = cutoff (cutoff2)
  cutoff = global cutoff for LJ (and Coulombic if only 1 arg) (distance units)
  cutoff2 = global cutoff for Coulombic (optional) (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style born/coul/dsf/cs 0.1 10.0 12.0
    pair_coeff * *   0.0 1.00 0.00 0.00 0.00
    pair_coeff 1 1 480.0 0.25 0.00 1.05 0.50

    pair_style born/coul/long/cs 10.0 8.0
    pair_coeff 1 1 6.08 0.317 2.340 24.18 11.51

    pair_style born/coul/wolf/cs 0.25 10.0 12.0
    pair_coeff * *   0.0 1.00 0.00 0.00 0.00
    pair_coeff 1 1 480.0 0.25 0.00 1.05 0.50

    pair_style buck/coul/long/cs 10.0
    pair_style buck/coul/long/cs 10.0 8.0
    pair_coeff * * 100.0 1.5 200.0
    pair_coeff 1 1 100.0 1.5 200.0 9.0

    pair_style coul/long/cs 10.0
    pair_coeff * *

    pair_style coul/wolf/cs 0.2 9.0
    pair_coeff * *

    pair_style lj/cut/coul/long/cs 10.0
    pair_style lj/cut/coul/long/cs 10.0 8.0
    pair_coeff * * 100.0 3.0
    pair_coeff 1 1 100.0 3.5 9.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

These pair styles are designed to be used with the adiabatic core/shell model of [[(Mitchell and Fincham)]{.std .std-ref}](#mitchellfincham3){.reference .internal}. See the [[Howto coreshell]{.doc}]Howto_coreshell.md){.reference .internal} page for an overview of the model as implemented in LAMMPS.

All the styles are identical to the corresponding pair style without the "/cs" in the name:

- [[pair_style born/coul/dsf]{.doc}]pair_born.md){.reference .internal}

- [[pair_style born/coul/long]{.doc}]pair_born.md){.reference .internal}

- [[pair_style born/coul/wolf]{.doc}]pair_born.md){.reference .internal}

- [[pair_style buck/coul/long]{.doc}]pair_buck.md){.reference .internal}

- [[pair_style coul/long]{.doc}]pair_coul.md){.reference .internal}

- [[pair_style coul/wolf]{.doc}]pair_coul.md){.reference .internal}

- [[pair_style lj/cut/coul/long]{.doc}]pair_lj_cut_coul.md){.reference .internal}

- [[pair_style lj/class2/coul/long]{.doc}]pair_class2.md){.reference .internal}

except that they correctly treat the special case where the distance between two charged core and shell atoms in the same core/shell pair approach r = 0.0.

Styles with a "/long" in the name are used with a long-range solver for Coulombic interactions via the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command. They require special treatment of the short-range Coulombic interactions within the cor/shell model.

Specifically, the short-range Coulomb interaction between a core and its shell should be turned off using the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command by setting the 1-2 weight to 0.0, which works because the core and shell atoms are bonded to each other. This induces a long-range correction approximation which fails at small distances (\~\< 10e-8). Therefore, the Coulomb term which is used to calculate the correction factor is extended by a minimal distance (r_min = 1.0-6) when the interaction between a core/shell pair is treated, as follows

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{C q_i q_j}{\\epsilon (r + r\_{min})} \\qquad r \\rightarrow 0\\\]
:::

where C is an energy-conversion constant, [\\(q_i\\)]{.math .notranslate .nohighlight} and [\\(q_j\\)]{.math .notranslate .nohighlight} are the charges on the core and shell, epsilon is the dielectric constant and [\\(r\_{min}\\)]{.math .notranslate .nohighlight} is the minimal distance.

For styles that are not used with a long-range solver, i.e. those with "/dsf" or "/wolf" in the name, the only correction is the addition of a minimal distance to avoid the possible r = 0.0 case for a core/shell pair.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

See the corresponding doc pages for pair styles without the "cs" suffix to see how mixing, shifting, tabulation, tail correction, restarting, and rRESPA are handled by theses pair styles.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the CORESHELL package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style born]{.doc}]pair_born.md){.reference .internal}, [[pair_style buck]{.doc}]pair_buck.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Mitchell and Fincham)** Mitchell, Fincham, J Phys Condensed Matter, 5, 1031-1038 (1993).
:::
:::::::::::::::
:::::::::::::::::::::::
::::::::::::::::::::::::

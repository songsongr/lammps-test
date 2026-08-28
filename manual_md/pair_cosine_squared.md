:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#pair-style-cosine-squared-command .section}
[]{#index-0}

# pair_style cosine/squared command[](#pair-style-cosine-squared-command "Link to this heading"){.headerlink}

::::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style cosine/squared cutoff
:::
::::

- cutoff = global cutoff for cosine-squared interactions (distance units)

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff I J eps sigma
    pair_coeff I J eps sigma cutoff
    pair_coeff I J eps sigma wca
    pair_coeff I J eps sigma cutoff wca
:::
::::

- I, J = a particle type

- eps = interaction strength, i.e. the depth of the potential minimum (energy units)

- sigma = distance of the potential minimum from 0

- cutoff = the cutoff distance for this pair type, if different from global (distance units)

- wca = if specified a Weeks-Chandler-Andersen potential (with eps strength and minimum at sigma) is added, otherwise not
:::::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style cosine/squared 3.0
    pair_coeff * * 1.0 1.3
    pair_coeff 1 3 1.0 1.3 2.0
    pair_coeff 1 3 1.0 1.3 wca
    pair_coeff 1 3 1.0 1.3 2.0 wca
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *cosine/squared* computes a potential of the form

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = \\begin{cases} -\\epsilon& \\quad r \< \\sigma \\\\ -\\epsilon\\cos\\left(\\frac{\\pi\\left(r - \\sigma\\right)}{2\\left(r_c - \\sigma\\right)}\\right)\^2&\\quad \\sigma \\leq r \< r_c \\\\ 0& \\quad r \\geq r_c \\end{cases}\\end{split}\\\]
:::

between two point particles, where ([\\(\\sigma, -\\epsilon\\)]{.math .notranslate .nohighlight}) is the location of the (rightmost) minimum of the potential, as explained in the syntax section above.

This potential was first used in [[(Cooke)]{.std .std-ref}](#ckd){.reference .internal} for a coarse-grained lipid membrane model. It is generally very useful as a non-specific interaction potential because it is fully adjustable in depth and width while joining the minimum at (sigma, -epsilon) and zero at (cutoff, 0) smoothly, requiring no shifting and causing no related artifacts, tail energy calculations etc. This evidently requires *cutoff* to be larger than *sigma*.

If the *wca* option is used then a Weeks-Chandler-Andersen potential [[(Weeks)]{.std .std-ref}](#wca){.reference .internal} is added to the above specified cosine-squared potential, specifically the following:

::: {.math .notranslate .nohighlight}
\\\[E = \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - 2\\left(\\frac{\\sigma}{r}\\right)\^6 + 1\\right\] , \\quad r \< \\sigma\\\]
:::

In this case, and this case only, the [\\(\\sigma\\)]{.math .notranslate .nohighlight} parameter can be equal to *cutoff* ([\\(\\sigma =\\)]{.math .notranslate .nohighlight} cutoff) which will result in ONLY the WCA potential being used (and print a warning), so the minimum will be attained at (sigma, 0). This is a convenience feature that enables a purely repulsive potential to be used without a need to define an additional pair style and use the hybrid styles.

The energy and force of this pair style for parameters epsilon = 1.0, sigma = 1.0, cutoff = 2.5, with and without the WCA potential, are shown in the graphs below:

![](_images/pair_cosine_squared_graphs.jpg){.align-center}
:::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

Mixing is not supported for this style.

The *shift*, *table* and *tail* options are not relevant for this style.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *cosine/squared* style is part of the EXTRA-PAIR package. It is only enabled if LAMMPS is build with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style lj/cut]{.doc}]pair_lj.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

**(Cooke)** "Cooke, Kremer and Deserno, Phys. Rev. E, 72, 011506 (2005)"

**(Weeks)** "Weeks, Chandler and Andersen, J. Chem. Phys., 54, 5237 (1971)"
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

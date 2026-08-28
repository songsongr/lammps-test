:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-eos-cv-command .section}
[]{#index-0}

# fix eos/cv command[](#fix-eos-cv-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID eos/cv cv
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- eos/cv = style name of this fix command

- cv = constant-volume heat capacity (energy/temperature units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all eos/cv 0.01
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Fix *eos/cv* applies a mesoparticle equation of state to relate the particle internal energy ([\\(u_i\\)]{.math .notranslate .nohighlight}) to the particle internal temperature ([\\(\\theta_i\\)]{.math .notranslate .nohighlight}). The *eos/cv* mesoparticle equation of state requires the constant-volume heat capacity, and is defined as follows:

::: {.math .notranslate .nohighlight}
\\\[u\_{i} = u\^{mech}\_{i} + u\^{cond}\_{i} = C\_{V} \\theta\_{i}\\\]
:::

where [\\(C_V\\)]{.math .notranslate .nohighlight} is the constant-volume heat capacity, [\\(u\^{cond}\\)]{.math .notranslate .nohighlight} is the internal conductive energy, and [\\(u\^{mech}\\)]{.math .notranslate .nohighlight} is the internal mechanical energy. Note that alternative definitions of the mesoparticle equation of state are possible.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command is part of the DPD-REACT package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This command also requires use of the [[atom_style dpd]{.doc}]atom_style.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix shardlow]{.doc}]fix_shardlow.md){.reference .internal}, [[pair dpd/fdt]{.doc}]pair_dpd_fdt.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Larentzos)** J.P. Larentzos, J.K. Brennan, J.D. Moore, and W.D. Mattson, "LAMMPS Implementation of Constant Energy Dissipative Particle Dynamics (DPD-E)", ARL-TR-6863, U.S. Army Research Laboratory, Aberdeen Proving Ground, MD (2014).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

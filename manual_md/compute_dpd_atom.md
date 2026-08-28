:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-dpd-atom-command .section}
[]{#index-0}

# compute dpd/atom command[](#compute-dpd-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID dpd/atom
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- dpd/atom = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all dpd/atom
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that accesses the per-particle internal conductive energy ([\\(u\^\\text{cond}\\)]{.math .notranslate .nohighlight}), internal mechanical energy ([\\(u\^\\text{mech}\\)]{.math .notranslate .nohighlight}), internal chemical energy ([\\(u\^\\text{chem}\\)]{.math .notranslate .nohighlight}) and internal temperatures ([\\(\\theta\\)]{.math .notranslate .nohighlight}) for each particle in a group. See the [[compute dpd]{.doc}]compute_dpd.md){.reference .internal} command if you want the total internal conductive energy, the total internal mechanical energy, the total chemical energy and average internal temperature of the entire system or group of dpd particles.
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-particle array with four columns ([\\(u\^\\text{cond}\\)]{.math .notranslate .nohighlight}, [\\(u\^\\text{mech}\\)]{.math .notranslate .nohighlight}, [\\(u\^\\text{chem}\\)]{.math .notranslate .nohighlight}, [\\(\\theta\\)]{.math .notranslate .nohighlight}), which can be accessed by indices 1--4 by any command that uses per-particle values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The per-particle array values will be in energy ([\\(u\^\\text{cond}\\)]{.math .notranslate .nohighlight}, [\\(u\^\\text{mech}\\)]{.math .notranslate .nohighlight}, [\\(u\^\\text{chem}\\)]{.math .notranslate .nohighlight}) and temperature ([\\(\\theta\\)]{.math .notranslate .nohighlight}) [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command is part of the DPD-REACT package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This command also requires use of the [[atom_style dpd]{.doc}]atom_style.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dump custom]{.doc}]dump.md){.reference .internal}, [[compute dpd]{.doc}]compute_dpd.md){.reference .internal}
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

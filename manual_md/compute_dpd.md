::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-dpd-command .section}
[]{#index-0}

# compute dpd command[](#compute-dpd-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID dpd
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- dpd = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all dpd
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that accumulates the total internal conductive energy ([\\(U\^{\\text{cond}}\\)]{.math .notranslate .nohighlight}), the total internal mechanical energy ([\\(U\^{\\text{mech}}\\)]{.math .notranslate .nohighlight}), the total chemical energy ([\\(U\^\\text{chem}\\)]{.math .notranslate .nohighlight}) and the *harmonic* average of the internal temperature ([\\(\\theta\_\\text{avg}\\)]{.math .notranslate .nohighlight}) for the entire system of particles. See the [[compute dpd/atom]{.doc}]compute_dpd_atom.md){.reference .internal} command if you want per-particle internal energies and internal temperatures.

The system internal properties are computed according to the following relations:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}U\^\\text{cond} = & \\sum\_{i=1}\^{N} u\_{i}\^\\text{cond} \\\\ U\^\\text{mech} = & \\sum\_{i=1}\^{N} u\_{i}\^\\text{mech} \\\\ U\^\\text{chem} = & \\sum\_{i=1}\^{N} u\_{i}\^\\text{chem} \\\\ U = & \\sum\_{i=1}\^{N} (u\_{i}\^\\text{cond} + u\_{i}\^\\text{mech} + u\_{i}\^\\text{chem}) \\\\ \\theta\_{avg} = & \\biggl(\\frac{1}{N}\\sum\_{i=1}\^{N} \\frac{1}{\\theta\_{i}}\\biggr)\^{-1} \\\\\\end{split}\\\]
:::

where [\\(N\\)]{.math .notranslate .nohighlight} is the number of particles in the system.
::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector of length 5 ([\\(U\^\\text{cond}\\)]{.math .notranslate .nohighlight}, [\\(U\^\\text{mech}\\)]{.math .notranslate .nohighlight}, [\\(U\^\\text{chem}\\)]{.math .notranslate .nohighlight}, [\\(\\theta\_\\text{avg}\\)]{.math .notranslate .nohighlight}, [\\(N\\)]{.math .notranslate .nohighlight}), which can be accessed by indices 1 through 5. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The vector values will be in energy and temperature [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command is part of the DPD-REACT package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This command also requires use of the [[atom_style dpd]{.doc}]atom_style.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute dpd/atom]{.doc}]compute_dpd_atom.md){.reference .internal}, [[thermo_style]{.doc}]thermo_style.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Larentzos)** J.P. Larentzos, J.K. Brennan, J.D. Moore, and W.D. Mattson, "LAMMPS Implementation of Constant Energy Dissipative Particle Dynamics (DPD-E)", ARL-TR-6863, U.S. Army Research Laboratory, Aberdeen Proving Ground, MD (2014).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

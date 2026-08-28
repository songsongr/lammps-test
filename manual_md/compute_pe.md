::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#compute-pe-command .section}
[]{#index-0}

# compute pe command[](#compute-pe-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID pe keyword ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- pe = style name of this compute command

- zero or more keywords may be appended

- keyword = *pair* or *bond* or *angle* or *dihedral* or *improper* or *kspace* or *fix*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all pe
    compute molPE all pe bond angle dihedral improper
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the potential energy of the entire system of atoms. The specified group must be "all". See the [[compute pe/atom]{.doc}]compute_pe_atom.md){.reference .internal} command if you want per-atom energies. These per-atom values could be summed for a group of atoms via the [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} command.

The energy is calculated by the various pair, bond, etc. potentials defined for the simulation. If no extra keywords are listed, then the potential energy is the sum of pair, bond, angle, dihedral, improper, [\\(k\\)]{.math .notranslate .nohighlight}-space (long-range), and fix energy (i.e., it is as though all the keywords were listed). If any extra keywords are listed, then only those components are summed to compute the potential energy.

The [\\(k\\)]{.math .notranslate .nohighlight}-space contribution requires 1 extra FFT each timestep the energy is calculated, if using the PPPM solver via the [[kspace_style pppm]{.doc}]kspace_style.md){.reference .internal} command. Thus it can increase the cost of the PPPM calculation if it is needed on a large fraction of the simulation timesteps.

Various fixes can contribute to the total potential energy of the system if the *fix* contribution is included. See the doc pages for [[individual fixes]{.doc}]fix.md){.reference .internal} for details of which ones compute a potential energy.

::: {.admonition .note}
Note

The [[fix_modify energy yes]{.doc}]fix_modify.md){.reference .internal} command must also be specified if a fix is to contribute potential energy to this command.
:::

A compute of this style with the ID of "thermo_pe" is created when LAMMPS starts up, as if this command were in the input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute thermo_pe all pe
:::
::::

See the "thermo_style" command for more details.
::::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the potential energy). This value can be used by any command that uses a global scalar value from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "extensive". The scalar value will be in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute pe/atom]{.doc}]compute_pe_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

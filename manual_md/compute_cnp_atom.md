::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#compute-cnp-atom-command .section}
[]{#index-0}

# compute cnp/atom command[](#compute-cnp-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID cnp/atom cutoff
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- cnp/atom = style name of this compute command

- cutoff = cutoff distance for nearest neighbors (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all cnp/atom 3.08
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the Common Neighborhood Parameter (CNP) for each atom in the group. In solid-state systems the CNP is a useful measure of the local crystal structure around an atom and can be used to characterize whether the atom is part of a perfect lattice, a local defect (e.g., a dislocation or stacking fault), or at a surface.

The value of the CNP parameter will be 0.0 for atoms not in the specified compute group. Note that normally a CNP calculation should only be performed on single component systems.

This parameter is computed using the following formula from [[(Tsuzuki)]{.std .std-ref}](#tsuzuki2){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[Q\_{i} = \\frac{1}{n_i}\\sum\_{j = 1}\^{n_i} \\left\\lVert \\sum\_{k = 1}\^{n\_{ij}} \\vec{R}\_{ik} + \\vec{R}\_{jk} \\right\\rVert\^{2}\\\]
:::

where the index *j* goes over the [\\(n_i\\)]{.math .notranslate .nohighlight} nearest neighbors of atom *i*, and the index *k* goes over the [\\(n\_{ij}\\)]{.math .notranslate .nohighlight} common nearest neighbors between atom *i* and atom *j*. [\\(\\vec{R}\_{ik}\\)]{.math .notranslate .nohighlight} and [\\(\\vec{R}\_{jk}\\)]{.math .notranslate .nohighlight} are the vectors connecting atom *k* to atoms *i* and *j*. The quantity in the double sum is computed for each atom.

The CNP calculation is sensitive to the specified cutoff value. You should ensure that the appropriate nearest neighbors of an atom are found within the cutoff distance for the presumed crystal structure. E.g. 12 nearest neighbor for perfect FCC and HCP crystals, 14 nearest neighbors for perfect BCC crystals. These formulas can be used to obtain a good cutoff distance:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}r\_{c}\^{\\mathrm{fcc}} = & \\frac{1}{2} \\left(\\frac{\\sqrt{2}}{2} + 1\\right) a \\approx 0.8536 a \\\\ r\_{c}\^{\\mathrm{bcc}} = & \\frac{1}{2}(\\sqrt{2} + 1) a \\approx 1.207 a \\\\ r\_{c}\^{\\mathrm{hcp}} = & \\frac{1}{2}\\left(1+\\sqrt{\\frac{4+2x\^{2}}{3}}\\right) a\\end{split}\\\]
:::

where [\\(a\\)]{.math .notranslate .nohighlight} is the lattice constant for the crystal structure concerned and in the HCP case, [\\(x = (c/a) / 1.633\\)]{.math .notranslate .nohighlight}, where 1.633 is the ideal [\\(c/a\\)]{.math .notranslate .nohighlight} for HCP crystals.

Also note that since the CNP calculation in LAMMPS uses the neighbors of an owned atom to find the nearest neighbors of a ghost atom, the following relation should also be satisfied:

::: {.math .notranslate .nohighlight}
\\\[r_c + r_s \> 2\*\\mathrm{cutoff}\\\]
:::

where [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff distance of the potential, [\\(r_s\\)]{.math .notranslate .nohighlight} is the skin distance as specified by the [[neighbor]{.doc}]neighbor.md){.reference .internal} command, and cutoff is the argument used with the compute cnp/atom command. LAMMPS will issue a warning if this is not the case.

The neighbor list needed to compute this quantity is constructed each time the calculation is performed (e.g., each time a snapshot of atoms is dumped). Thus it can be inefficient to compute/dump this quantity too frequently or to have multiple compute/dump commands, each with a *cnp/atom* style.
::::::

::::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom vector, which can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The per-atom vector values will be real positive numbers. Some typical CNP values:

:::: {.highlight-none .notranslate}
::: highlight
    FCC lattice = 0.0
    BCC lattice = 0.0
    HCP lattice = 4.4

    FCC (111) surface = 13.0
    FCC (100) surface = 26.5
    FCC dislocation core = 11
:::
::::
:::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EXTRA-COMPUTE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute cna/atom]{.doc}]compute_cna_atom.md){.reference .internal} [[compute centro/atom]{.doc}]compute_centro_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Tsuzuki)** Tsuzuki, Branicio, Rino, Comput Phys Comm, 177, 518 (2007).
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

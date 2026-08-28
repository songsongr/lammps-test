:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#compute-cna-atom-command .section}
[]{#index-0}

# compute cna/atom command[](#compute-cna-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID cna/atom cutoff
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- cna/atom = style name of this compute command

- cutoff = cutoff distance for nearest neighbors (distance units)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all cna/atom 3.08
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the CNA (Common Neighbor Analysis) pattern for each atom in the group. In solid-state systems the CNA pattern is a useful measure of the local crystal structure around an atom. The CNA methodology is described in [[(Faken)]{.std .std-ref}](#faken){.reference .internal} and [[(Tsuzuki)]{.std .std-ref}](#tsuzuki1){.reference .internal}.

Currently, there are five kinds of CNA patterns LAMMPS recognizes:

- fcc = 1

- hcp = 2

- bcc = 3

- icosahedral = 4

- unknown = 5

The value of the CNA pattern will be 0 for atoms not in the specified compute group. Note that normally a CNA calculation should only be performed on mono-component systems.

The CNA calculation can be sensitive to the specified cutoff value. You should ensure the appropriate nearest neighbors of an atom are found within the cutoff distance for the presumed crystal structure (e.g., 12 nearest neighbor for perfect FCC and HCP crystals, 14 nearest neighbors for perfect BCC crystals). These formulas can be used to obtain a good cutoff distance:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}r\_{c}\^{\\mathrm{fcc}} = & \\frac{1}{2} \\left(\\frac{\\sqrt{2}}{2} + 1\\right) a \\approx 0.8536 a \\\\ r\_{c}\^{\\mathrm{bcc}} = & \\frac{1}{2}(\\sqrt{2} + 1) a \\approx 1.207 a \\\\ r\_{c}\^{\\mathrm{hcp}} = & \\frac{1}{2}\\left(1+\\sqrt{\\frac{4+2x\^{2}}{3}}\\right) a\\end{split}\\\]
:::

where [\\(a\\)]{.math .notranslate .nohighlight} is the lattice constant for the crystal structure concerned and in the HCP case, [\\(x = (c/a) / 1.633\\)]{.math .notranslate .nohighlight}, where 1.633 is the ideal [\\(c/a\\)]{.math .notranslate .nohighlight} for HCP crystals.

Also note that since the CNA calculation in LAMMPS uses the neighbors of an owned atom to find the nearest neighbors of a ghost atom, the following relation should also be satisfied:

::: {.math .notranslate .nohighlight}
\\\[r_c + r_s \> 2\*\\mathrm{cutoff}\\\]
:::

where [\\(r_c\\)]{.math .notranslate .nohighlight} is the cutoff distance of the potential, [\\(r_s\\)]{.math .notranslate .nohighlight} is the skin distance as specified by the [[neighbor]{.doc}]neighbor.md){.reference .internal} command, and cutoff is the argument used with the compute cna/atom command. LAMMPS will issue a warning if this is not the case.

The neighbor list needed to compute this quantity is constructed each time the calculation is performed (e.g. each time a snapshot of atoms is dumped). Thus it can be inefficient to compute/dump this quantity too frequently or to have multiple compute/dump commands, each with a *cna/atom* style.
:::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom vector, which can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The per-atom vector values will be a number from 0 to 5, as explained above.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute centro/atom]{.doc}]compute_centro_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Faken)** Faken, Jonsson, Comput Mater Sci, 2, 279 (1994).

**(Tsuzuki)** Tsuzuki, Branicio, Rino, Comput Phys Comm, 177, 518 (2007).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

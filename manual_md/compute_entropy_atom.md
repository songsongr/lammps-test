::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::: {#compute-entropy-atom-command .section}
[]{#index-0}

# compute entropy/atom command[](#compute-entropy-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID entropy/atom sigma cutoff keyword value ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- entropy/atom = style name of this compute command

- sigma = width of Gaussians used in the [\\(g(r)\\)]{.math .notranslate .nohighlight} smoothing

- cutoff = cutoff for the [\\(g(r)\\)]{.math .notranslate .nohighlight} calculation

- one or more keyword/value pairs may be appended

``` literal-block
keyword = avg or local
  avg args = neigh cutoff2
    neigh value = yes or no = whether to average the pair entropy over neighbors
    cutoff2 = cutoff for the averaging over neighbors
  local arg = yes or no = use the local density around each atom to normalize the g(r)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all entropy/atom 0.25 5.
    compute 1 all entropy/atom 0.25 5. avg yes 5.
    compute 1 all entropy/atom 0.125 7.3 avg yes 5.1 local yes
:::
::::
:::::

:::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the pair entropy fingerprint for each atom in the group. The fingerprint is useful to distinguish between ordered and disordered environments, for instance liquid and solid-like environments, or glassy and crystalline-like environments. Some applications could be the identification of grain boundaries, a melt-solid interface, or a solid cluster emerging from the melt. The advantage of this parameter over others is that no a priori information about the solid structure is required.

This parameter for atom i is computed using the following formula from [[(Piaggi)]{.std .std-ref}](#piaggi){.reference .internal} and [[(Nettleton)]{.std .std-ref}](#nettleton){.reference .internal} ,

::: {.math .notranslate .nohighlight}
\\\[s_S\^i=-2\\pi\\rho k_B \\int\\limits_0\^{r_m} \\left \[ g(r) \\ln g(r) - g(r) + 1 \\right \] r\^2 dr\\\]
:::

where [\\(r\\)]{.math .notranslate .nohighlight} is a distance, [\\(g(r)\\)]{.math .notranslate .nohighlight} is the radial distribution function of atom [\\(i\\)]{.math .notranslate .nohighlight}, and [\\(\\rho\\)]{.math .notranslate .nohighlight} is the density of the system. The [\\(g(r)\\)]{.math .notranslate .nohighlight} computed for each atom [\\(i\\)]{.math .notranslate .nohighlight} can be noisy and therefore it is smoothed using

::: {.math .notranslate .nohighlight}
\\\[g_m\^i(r) = \\frac{1}{4 \\pi \\rho r\^2} \\sum\\limits\_{j} \\frac{1}{\\sqrt{2 \\pi \\sigma\^2}} e\^{-(r-r\_{ij})\^2/(2\\sigma\^2)}\\\]
:::

where the sum over [\\(j\\)]{.math .notranslate .nohighlight} goes through the neighbors of atom [\\(i\\)]{.math .notranslate .nohighlight} and [\\(\\sigma\\)]{.math .notranslate .nohighlight} is a parameter to control the smoothing.

The input parameters are *sigma* the smoothing parameter [\\(\\sigma\\)]{.math .notranslate .nohighlight}, and the *cutoff* for the calculation of [\\(g(r)\\)]{.math .notranslate .nohighlight}.

If the keyword *avg* has the setting *yes*, then this compute also averages the parameter over the neighbors of atom [\\(i\\)]{.math .notranslate .nohighlight} according to

::: {.math .notranslate .nohighlight}
\\\[\\left\< s_S\^i \\right\> = \\frac{\\sum_j s_S\^j + s_S\^i}{N + 1},\\\]
:::

where the sum over [\\(j\\)]{.math .notranslate .nohighlight} goes over the neighbors of atom [\\(i\\)]{.math .notranslate .nohighlight} and [\\(N\\)]{.math .notranslate .nohighlight} is the number of neighbors. This procedure provides a sharper distinction between order and disorder environments. In this case the input parameter *cutoff2* is the cutoff for the averaging over the neighbors and must also be specified.

If the *avg yes* option is used, the effective cutoff of the neighbor list should be *cutoff*+*cutoff2* and therefore it might be necessary to increase the skin of the neighbor list with:

:::: {.highlight-none .notranslate}
::: highlight
    neighbor <skin distance> bin
:::
::::

See [[neighbor]{.doc}]neighbor.md){.reference .internal} for details.

If the *local yes* option is used, the [\\(g(r)\\)]{.math .notranslate .nohighlight} is normalized by the local density around each atom, that is to say the density around each atom is the number of neighbors within the neighbor list cutoff divided by the corresponding volume. This option can be useful when dealing with inhomogeneous systems such as those that have surfaces.

Here are typical input parameters for fcc aluminum (lattice constant [\\(4.05\~\\AA\\)]{.math .notranslate .nohighlight}),

:::: {.highlight-none .notranslate}
::: highlight
    compute 1 all entropy/atom 0.25 5.7 avg yes 3.7
:::
::::

and for bcc sodium (lattice constant [\\(4.23\~\\AA\\)]{.math .notranslate .nohighlight}),

:::: {.highlight-none .notranslate}
::: highlight
    compute 1 all entropy/atom 0.25 7.3 avg yes 5.1
:::
::::
::::::::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

By default, this compute calculates the pair entropy value for each atom as a per-atom vector, which can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The pair entropy values have units of the Boltzmann constant. They are always negative, and lower values (lower entropy) correspond to more ordered environments.
:::

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

The default values for the optional keywords are avg = no and local = no.

------------------------------------------------------------------------

**(Piaggi)** Piaggi and Parrinello, J Chem Phys, 147, 114112 (2017).

**(Nettleton)** Nettleton and Green, J Chem Phys, 29, 6 (1958).
:::
:::::::::::::::::::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

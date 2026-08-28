:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-ackland-atom-command .section}
[]{#index-0}

# compute ackland/atom command[](#compute-ackland-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID ackland/atom keyword/value
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- ackland/atom = style name of this compute command

- zero or more keyword/value pairs may be appended

- keyword = *legacy*

  ``` literal-block
  legacy args = yes or no = use (yes) or do not use (no) legacy Ackland algorithm implementation
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all ackland/atom
    compute 1 all ackland/atom legacy yes
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Defines a computation that calculates the local lattice structure according to the formulation given in [[(Ackland)]{.std .std-ref}](#ackland){.reference .internal}. Historically, LAMMPS had two, slightly different implementations of the algorithm from the paper. With the *legacy* keyword, it is possible to switch between the pre-2015 (*legacy yes*) and post-2015 implementation (*legacy no*). The post-2015 variant is the default.

In contrast to the [[centro-symmetry parameter]{.doc}]compute_centro_atom.md){.reference .internal} this method is stable against temperature boost, because it is based not on the distance between particles but the angles. Therefore statistical fluctuations are averaged out a little more. A comparison with the Common Neighbor Analysis metric is made in the paper.

The result is a number which is mapped to the following different lattice structures:

- 0 = UNKNOWN

- 1 = BCC

- 2 = FCC

- 3 = HCP

- 4 = ICO

The neighbor list needed to compute this quantity is constructed each time the calculation is performed (i.e. each time a snapshot of atoms is dumped). Thus it can be inefficient to compute/dump this quantity too frequently or to have multiple compute/dump commands, each of which computes this quantity.-
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom vector, which can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EXTRA-COMPUTE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The per-atom vector values will be unitless since they are the integers defined above.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute centro/atom]{.doc}]compute_centro_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The keyword *legacy* defaults to *no*.

------------------------------------------------------------------------

**(Ackland)** Ackland, Jones, Phys Rev B, 73, 054104 (2006).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

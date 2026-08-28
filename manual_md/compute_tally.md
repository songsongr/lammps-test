::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#compute-force-tally-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# compute force/tally command[](#compute-force-tally-command "Link to this heading"){.headerlink}
:::

::: {#compute-heat-flux-tally-command .section}
# compute heat/flux/tally command[](#compute-heat-flux-tally-command "Link to this heading"){.headerlink}
:::

::: {#compute-heat-flux-virial-tally-command .section}
# compute heat/flux/virial/tally command[](#compute-heat-flux-virial-tally-command "Link to this heading"){.headerlink}
:::

::: {#compute-pe-tally-command .section}
# compute pe/tally command[](#compute-pe-tally-command "Link to this heading"){.headerlink}
:::

::: {#compute-pe-mol-tally-command .section}
# compute pe/mol/tally command[](#compute-pe-mol-tally-command "Link to this heading"){.headerlink}
:::

:::::::::::::::::: {#compute-stress-tally-command .section}
# compute stress/tally command[](#compute-stress-tally-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID style group2-ID
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- style = *force/tally* or *heat/flux/tally* or *heat/flux/virial/tally* or *pe/tally* or *pe/mol/tally* or *stress/tally*

- group2-ID = group ID of second (or same) group
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 lower force/tally upper
    compute 1 left pe/tally right
    compute 1 lower stress/tally lower
    compute 1 subregion heat/flux/tally all
    compute 1 liquid heat/flux/virial/tally solid
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates properties between two groups of atoms by accumulating them from pairwise non-bonded computations. Except for *heat/flux/virial/tally*, the two groups can be the same. This is similar to [[compute group/group]{.doc}]compute_group_group.md){.reference .internal} only that the data is accumulated directly during the non-bonded force computation. The computes *force/tally*, *pe/tally*, *stress/tally*, and *heat/flux/tally* are primarily provided as example how to program additional, more sophisticated computes using the tally callback mechanism. Compute *pe/mol/tally* is one such style, that can---through using this mechanism---separately tally intermolecular and intramolecular energies. Something that would otherwise be impossible without integrating this as a core functionality into the base classes of LAMMPS.

------------------------------------------------------------------------

Compute *heat/flux/tally* obtains the heat flux (strictly speaking, heat flow) inside the first group, which is the sum of the convective contribution due to atoms in the first group and the virial contribution due to interaction between the first and second groups:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathbf{Q}= \\sum\_{i \\in \\text{group 1}} e_i \\mathbf{v}\_i + \\frac{1}{2} \\sum\_{i \\in \\text{group 1}} \\sum\_{\\substack{j \\in \\text{group 2} \\\\ j \\neq i } } \\left( \\mathbf{F}\_{ij} \\cdot \\mathbf{v}\_j \\right) \\mathbf{r}\_{ij}\\end{split}\\\]
:::

When the second group in *heat/flux/tally* is set to "all", the resulting values will be identical to that obtained by [[compute heat/flux]{.doc}]compute_heat_flux.md){.reference .internal}, provided only pairwise interactions exist.

Compute *heat/flux/virial/tally* obtains the total virial heat flux (strictly speaking, heat flow) into the first group due to interaction with the second group, and is defined as:

::: {.math .notranslate .nohighlight}
\\\[Q = \\frac{1}{2} \\sum\_{i \\in \\text{group 1}} \\sum\_{j \\in \\text{group 2}} \\mathbf{F}\_{ij} \\cdot \\left(\\mathbf{v}\_i + \\mathbf{v}\_j \\right)\\\]
:::

Although, the *heat/flux/virial/tally* compute does not include the convective term, it can be used to obtain the total heat flux over control surfaces, when there are no particles crossing over, such as is often in solid--solid and solid--liquid interfaces. This would be identical to the method of planes method. Note that the *heat/flux/virial/tally* compute is distinctly different from the *heat/flux* and *heat/flux/tally* computes, that are essentially volume averaging methods. The following example demonstrates the difference:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # System with only pairwise interactions.
    # Non-periodic boundaries in the x direction.
    # Has LeftLiquid and RightWall groups along x direction.

    # Heat flux over the solid-liquid interface
    compute hflow_hfvt RightWall heat/flux/virial/tally LeftLiquid
    variable hflux_hfvt equal c_hflow_hfvt/(ly*lz)

    # x component of approximate heat flux vector inside the liquid region,
    # two approaches.
    #
    compute myKE all ke/atom
    compute myPE all pe/atom
    compute myStress all stress/atom NULL virial
    compute hflow_hf LeftLiquid heat/flux myKE myPE myStress
    variable hflux_hf equal c_hflow_hf[1]/${volLiq}
    #
    compute hflow_hft LeftLiquid heat/flux/tally all
    variable hflux_hft equal c_hflow_hft[1]/${volLiq}

    # Pressure over the solid-liquid interface, three approaches.
    #
    compute force_gg RightWall group/group LeftLiquid
    variable press_gg equal c_force_gg[1]/(ly*lz)
    #
    compute force_ft RightWall force/tally LeftLiquid
    compute rforce_ft RightWall reduce sum c_force_ft[1]
    variable press_ft equal c_rforce_ft/(ly*lz)
    #
    compute rforce_hfvt all reduce sum c_hflow_hfvt[1]
    variable press_hfvt equal c_rforce_hfvt/(ly*lz)
:::
::::

------------------------------------------------------------------------

The pairwise contributions are computing via a callback that the compute registers with the non-bonded pairwise force computation. This limits the use to systems that have no bonds, no Kspace, and no many-body interactions. On the other hand, the computation does not have to compute forces or energies a second time and thus can be much more efficient. The callback mechanism allows to write more complex pairwise property computations.
:::::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

- Compute *pe/tally* calculates a global scalar (the energy) and a per atom scalar (the contributions of the single atom to the global scalar).

- Compute *pe/mol/tally* calculates a global four-element vector containing (in this order): *evdwl* and *ecoul* for intramolecular pairs and *evdwl* and *ecoul* for intermolecular pairs. Since molecules are identified by their molecule IDs, the partitioning does not have to be related to molecules, but the energies are tallied into the respective slots depending on whether the molecule IDs of a pair are the same or different.

- Compute *force/tally* calculates a global scalar (the force magnitude) and a per atom 3-element vector (force contribution from each atom).

- Compute *stress/tally* calculates a global scalar (average of the diagonal elements of the stress tensor) and a per atom vector (the six elements of stress tensor contributions from the individual atom).

- As in [[compute heat/flux]{.doc}]compute_heat_flux.md){.reference .internal}, compute *heat/flux/tally* calculates a global vector of length 6, where the first three components are the [\\(x\\)]{.math .notranslate .nohighlight}, [\\(y\\)]{.math .notranslate .nohighlight}, [\\(z\\)]{.math .notranslate .nohighlight} components of the full heat flow vector, and the next three components are the corresponding components of just the convective portion of the flow (i.e., the first term in the equation for [\\(\\mathbf{Q}\\)]{.math .notranslate .nohighlight}).

- Compute *heat/flux/virial/tally* calculates a global scalar (heat flow) and a per atom three-element vector (contribution to the force acting over atoms in the first group from individual atoms in both groups).

Both the scalar and vector values calculated by this compute are "extensive".
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the TALLY package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Not all pair styles can be evaluated in a pairwise mode as required by this compute. For example, 3-body and other many-body potentials, such as [[Tersoff]{.doc}]pair_tersoff.md){.reference .internal} and [[Stillinger-Weber]{.doc}]pair_sw.md){.reference .internal} cannot be used. [[EAM]{.doc}]pair_eam.md){.reference .internal} potentials only include the pair potential portion of the EAM interaction when used by this compute, not the embedding term. Also bonded or Kspace interactions do not contribute to this compute.

These computes are not compatible with accelerated pair styles from the GPU, INTEL, KOKKOS, or OPENMP packages. They will either create an error or print a warning when required data was not tallied in the required way and thus the data acquisition functions from these computes not called.

When used with dynamic groups, a [[run 0]{.doc}]run.md){.reference .internal} command needs to be inserted in order to initialize the dynamic groups before accessing the computes.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

- [[compute group/group]{.doc}]compute_group_group.md){.reference .internal}

- [[compute heat/flux]{.doc}]compute_heat_flux.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#compute-fep-ta-command .section}
[]{#index-0}

# compute fep/ta command[](#compute-fep-ta-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID fep/ta temp plane scale_factor keyword value ...
:::
::::

- ID, group-ID are documented in the [[compute]{.doc}]compute.md){.reference .internal} command

- fep/ta = name of this compute command

- temp = external temperature (as specified for constant-temperature run)

- plane = *xy* or *xz* or *yz*

- scale_factor = multiplicative factor for change in plane area

- zero or more keyword/value pairs may be appended

- keyword = *tail*

  ``` literal-block
  tail value = no or yes
    no = ignore tail correction to pair energies (usually small in fep)
    yes = include tail correction to pair energies
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all fep/ta 298 xy 1.0005
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

Define a computation that calculates the change in the free energy due to a test-area (TA) perturbation [[(Gloor)]{.std .std-ref}](#gloor){.reference .internal}. The test-area approach can be used to determine the interfacial tension of the system in a single simulation:

::: {.math .notranslate .nohighlight}
\\\[\\gamma = \\lim\_{\\Delta \\mathcal{A} \\to 0} \\left( \\frac{\\Delta A\_{0 \\to 1 }}{\\Delta \\mathcal{A}}\\right)\_{N,V,T} = - \\frac{k_B T}{\\Delta \\mathcal{A}} \\ln \\left\\langle \\exp\\left(\\frac{-(U_1 - U_0)}{k_B T}\\right) \\right\\rangle_0\\\]
:::

During the perturbation, both axes of *plane* are scaled by multiplying [\\(\\sqrt{\\mathrm{scale\\\_factor}}\\)]{.math .notranslate .nohighlight}, while the other axis divided by [\\(\\mathrm{scale\\\_factor}\\)]{.math .notranslate .nohighlight} such that the overall volume of the system is maintained.

The *tail* keyword controls the calculation of the tail correction to "van der Waals" pair energies beyond the cutoff, if this has been activated via the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} command. If the perturbation is small, the tail contribution to the energy difference between the reference and perturbed systems should be negligible.
:::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector of length 3 which contains the energy difference [\\((U_1-U_0)\\)]{.math .notranslate .nohighlight} as c_ID\[1\], the Boltzmann factor [\\(\\exp\\bigl(-(U_1-U_0)/k_B T\\bigr)\\)]{.math .notranslate .nohighlight}, as c_ID\[2\] and the change in the *plane* area [\\(\\Delta \\mathcal{A}\\)]{.math .notranslate .nohighlight} as c_ID\[3\]. [\\(U_1\\)]{.math .notranslate .nohighlight} is the potential energy of the perturbed state and [\\(U_0\\)]{.math .notranslate .nohighlight} is the potential energy of the reference state. The energies include kspace terms if these are used in the simulation.

These output results can be used by any command that uses a global scalar or vector from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options. For example, the computed values can be averaged using [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Constraints, like fix shake, may lead to incorrect values for energy difference.

This compute is distributed as the FEP package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute fep]{.doc}]compute_fep.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *tail* = *no*.

------------------------------------------------------------------------

**(Gloor)** Gloor, J Chem Phys, 123, 134703 (2005)
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

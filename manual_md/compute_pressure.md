:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#compute-pressure-command .section}
[]{#index-0}

# compute pressure command[](#compute-pressure-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID pressure temp-ID keyword ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- pressure = style name of this compute command

- temp-ID = ID of compute that calculates temperature, can be NULL if not needed

- zero or more keywords may be appended

- keyword = *ke* or *pair* or *bond* or *angle* or *dihedral* or *improper* or *kspace* or *fix* or *virial* or *pair/hybrid*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all pressure thermo_temp
    compute 1 all pressure NULL pair bond
    compute 1 all pressure NULL pair/hybrid lj/cut
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the pressure of the entire system of atoms. The specified group must be "all". See the [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} command if you want per-atom pressure (stress). These per-atom values could be summed for a group of atoms via the [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} command.

The pressure is computed by the formula

::: {.math .notranslate .nohighlight}
\\\[P = \\frac{N k_B T}{V} + \\frac{1}{V d}\\sum\_{i=1}\^{N\'} \\vec r_i \\cdot \\vec f_i\\\]
:::

where *N* is the number of atoms in the system (see discussion of DOF below), [\\(k_B\\)]{.math .notranslate .nohighlight} is the Boltzmann constant, [\\(T\\)]{.math .notranslate .nohighlight} is the temperature, *d* is the dimensionality of the system (2 for 2d, 3 for 3d), and *V* is the system volume (or area in 2d). The second term is the virial, equal to [\\(-dU/dV\\)]{.math .notranslate .nohighlight}, computed for all pairwise as well as 2-body, 3-body, 4-body, many-body, and long-range interactions, where [\\(\\vec r_i\\)]{.math .notranslate .nohighlight} and [\\(\\vec f_i\\)]{.math .notranslate .nohighlight} are the position and force vector of atom *i*, and the dot indicates the dot product (scalar product). This is computed in parallel for each subdomain and then summed over all parallel processes. Thus [\\(N\'\\)]{.math .notranslate .nohighlight} necessarily includes atoms from neighboring subdomains (so-called ghost atoms) and the position and force vectors of ghost atoms are thus included in the summation. Only when running in serial and without periodic boundary conditions is [\\(N\' = N\\)]{.math .notranslate .nohighlight} the number of atoms in the system. [[Fixes]{.doc}]fix.md){.reference .internal} that impose constraints (e.g., the [[fix shake]{.doc}]fix_shake.md){.reference .internal} command) may also contribute to the virial term.

A symmetric pressure tensor, stored as a 6-element vector, is also calculated by this compute. The six components of the vector are ordered [\\(xx,\\)]{.math .notranslate .nohighlight} [\\(yy,\\)]{.math .notranslate .nohighlight} [\\(zz,\\)]{.math .notranslate .nohighlight} [\\(xy,\\)]{.math .notranslate .nohighlight} [\\(xz,\\)]{.math .notranslate .nohighlight} [\\(yz.\\)]{.math .notranslate .nohighlight} The equation for the [\\((I,J)\\)]{.math .notranslate .nohighlight} components (where [\\(I\\)]{.math .notranslate .nohighlight} and [\\(J\\)]{.math .notranslate .nohighlight} are [\\(x\\)]{.math .notranslate .nohighlight}, [\\(y\\)]{.math .notranslate .nohighlight}, or [\\(z\\)]{.math .notranslate .nohighlight}) is similar to the above formula, except that the first term uses components related to the kinetic energy tensor and the second term uses components of the virial tensor:

::: {.math .notranslate .nohighlight}
\\\[P\_{IJ} = \\frac{1}{V}\\sum\_{k=1}\^{N} m_k v\_{k_I} v\_{k_J} + \\frac{1}{V}\\sum\_{k=1}\^{N\'} r\_{k_I} f\_{k_J}.\\\]
:::

If no extra keywords are listed, the entire equations above are calculated. This includes a kinetic energy (temperature) term and the virial as the sum of pair, bond, angle, dihedral, improper, kspace (long-range), and fix contributions to the force on each atom. If any extra keywords are listed, then only those components are summed to compute temperature or ke and/or the virial. The *virial* keyword means include all terms except the kinetic energy *ke*.

The *pair/hybrid* keyword means to only include contribution from a sub-style in a *hybrid* or *hybrid/overlay* pair style.

Details of how LAMMPS computes the virial efficiently for the entire system, including for many-body potentials and accounting for the effects of periodic boundary conditions are discussed in [[(Thompson)]{.std .std-ref}](#thompson1){.reference .internal}.

The temperature and kinetic energy tensor are not calculated by this compute, but rather by the temperature compute specified with the command. See the doc pages for individual compute temp variants for an explanation of how they calculate temperature and a symmetric tensor (6-element vector) whose components are twice that of the traditional KE tensor. That tensor is what appears in the pressure tensor formula above.

If the kinetic energy is not included in the pressure, than the temperature compute is not used and can be specified as NULL. Normally the temperature compute used by compute pressure should calculate the temperature of all atoms for consistency with the virial term, but any compute style that calculates temperature can be used (e.g., one that excludes frozen atoms or other degrees of freedom).

Note that if desired the specified temperature compute can be one that subtracts off a bias to calculate a temperature using only the thermal velocity of the atoms (e.g., by subtracting a background streaming velocity). See the doc pages for individual [[compute commands]{.doc}]compute.md){.reference .internal} to determine which ones include a bias.

Also note that the [\\(N\\)]{.math .notranslate .nohighlight} in the first formula above is really degrees-of-freedom divided by [\\(d\\)]{.math .notranslate .nohighlight} = dimensionality, where the DOF value is calculated by the temperature compute. See the various [[compute temperature]{.doc}]compute.md){.reference .internal} styles for details.

A compute of this style with the ID of thermo_press is created when LAMMPS starts up, as if this command were in the input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute thermo_press all pressure thermo_temp
:::
::::

where thermo_temp is the ID of a similarly defined compute of style "temp". See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command for more details.
:::::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the pressure) and a global vector of length 6 (pressure tensor), which can be accessed by indices 1--6. These values can be used by any command that uses global scalar or vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The ordering of values in the symmetric pressure tensor is as follows: [\\(p\_{xx},\\)]{.math .notranslate .nohighlight} [\\(p\_{yy},\\)]{.math .notranslate .nohighlight} [\\(p\_{zz},\\)]{.math .notranslate .nohighlight} [\\(p\_{xy},\\)]{.math .notranslate .nohighlight} [\\(p\_{xz},\\)]{.math .notranslate .nohighlight} [\\(p\_{yz}.\\)]{.math .notranslate .nohighlight}

The scalar and vector values calculated by this compute are "intensive". The scalar and vector values will be in pressure [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute temp]{.doc}]compute_temp.md){.reference .internal}, [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal}, [[thermo_style]{.doc}]thermo_style.md){.reference .internal}, [[fix numdiff/virial]{.doc}]fix_numdiff_virial.md){.reference .internal},
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

By default the compute includes contributions from the keywords: [`ke`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`pair`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`bond`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`angle`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`dihedral`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`improper`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kspace`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`fix`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

**(Thompson)** Thompson, Plimpton, Mattson, J Chem Phys, 131, 154107 (2009).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

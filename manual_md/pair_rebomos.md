:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#pair-style-rebomos-command .section}
[]{#index-1}[]{#index-0}

# pair_style rebomos command[](#pair-style-rebomos-command "Link to this heading"){.headerlink}

Accelerator Variants: *rebomos/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style rebomos
:::
::::

- rebomos = name of this pair style
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style rebomos
    pair_coeff * * ../potentials/MoS.rebomos Mo S
:::
::::

Example input scripts available: examples/threebody/
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 17Apr2024.]{.versionmodified .added}
:::

The *rebomos* pair style computes the interactions between molybdenum and sulfur atoms [[(Stewart)]{.std .std-ref}](#stewart){.reference .internal} utilizing an adaptive interatomic reactive empirical bond order potential that is similar in form to the AIREBO potential [[(Stuart)]{.std .std-ref}](#stuart2){.reference .internal}. The potential is based on an earlier parameterizations for [\\(\\text{MoS}\_2\\)]{.math .notranslate .nohighlight} developed by [[(Liang)]{.std .std-ref}](#liang){.reference .internal}.

The REBOMoS potential consists of two terms:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} \\left\[ E\^{\\text{REBO}}\_{ij} + E\^{\\text{LJ}}\_{ij} \\right\] \\\\\\end{split}\\\]
:::

The [\\(E\^{\\text{REBO}}\\)]{.math .notranslate .nohighlight} term describes the covalently bonded interactions between Mo and S atoms while the [\\(E\^{\\text{LJ}}\\)]{.math .notranslate .nohighlight} term describes longer range dispersion forces between layers. A cubic spline function is applied to smoothly switch between covalent bonding at short distances to dispersion interactions at longer distances. This allows the model to capture bond formation and breaking events which may occur between adjacent MoS2 layers, edges, defects, and more.

------------------------------------------------------------------------

Only a single pair_coeff command is used with the *rebomos* pair style which specifies an REBOMoS potential file with parameters for Mo and S. These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- [\\(N\\)]{.math .notranslate .nohighlight} element names = mapping of REBOMoS elements to atom types

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for the potential file.

As an example, if your LAMMPS simulation has three atom types and you want the first two to be Mo, and the third to be S, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * MoS.rebomos Mo Mo S
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The first two Mo arguments map LAMMPS atom types 1 and 2 to the Mo element in the REBOMoS file. The final S argument maps LAMMPS atom type 3 to the S element in the REBOMoS file. If a mapping value is specified as NULL, the mapping is not performed. This can be used when a *rebomos* potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} mix, shift, table, and tail options.

This pair style does not write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the MANYBODY package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

These pair potentials require the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

The MoS.rebomos potential file provided with LAMMPS (see the potentials directory) is parameterized for metal [[units]{.doc}]units.md){.reference .internal}. You can use the *rebomos* pair style with any LAMMPS units setting, but you would need to create your own REBOMoS potential file with coefficients listed in the appropriate units.

The pair style provided here **only** supports potential files parameterized for the elements molybdenum and sulfur (designated with "Mo" and "S" in the *pair_coeff* command. Using potential files for other elements will trigger an error.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair style rebo]{.doc}]pair_airebo.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Steward)** Stewart, Spearot, Modelling Simul. Mater. Sci. Eng. 21, 045003, (2013).

**(Stuart)** Stuart, Tutein, Harrison, J Chem Phys, 112, 6472-6486, (2000).

**(Liang)** Liang, Phillpot, Sinnott Phys. Rev. B79 245110, (2009), Erratum: Phys. Rev. B85 199903(E), (2012)
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

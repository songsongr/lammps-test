::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-brownian-command .section}
[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style brownian command[](#pair-style-brownian-command "Link to this heading"){.headerlink}

Accelerator Variants: *brownian/omp*, *brownian/kk*
:::

:::::::::::::: {#pair-style-brownian-poly-command .section}
# pair_style brownian/poly command[](#pair-style-brownian-poly-command "Link to this heading"){.headerlink}

Accelerator Variants: *brownian/poly/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style mu flaglog flagfld cutinner cutoff t_target seed flagHI flagVF
:::
::::

- style = *brownian* or *brownian/poly*

- mu = dynamic viscosity (dynamic viscosity units)

- flaglog = 0/1 log terms in the lubrication approximation on/off

- flagfld = 0/1 to include/exclude Fast Lubrication Dynamics effects

- cutinner = inner cutoff distance (distance units)

- cutoff = outer cutoff for interactions (distance units)

- t_target = target temp of the system (temperature units)

- seed = seed for the random number generator (positive integer)

- flagHI (optional) = 0/1 to include/exclude 1/r hydrodynamic interactions

- flagVF (optional) = 0/1 to include/exclude volume fraction corrections in the long-range isotropic terms
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style brownian 1.5 1 1 2.01 2.5 2.0 5878567 # (assuming radius = 1)
    pair_coeff 1 1 2.05 2.8
    pair_coeff * *
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Styles *brownian* and *brownian/poly* compute Brownian forces and torques on finite-size spherical particles. The former requires monodisperse spherical particles; the latter allows for polydisperse spherical particles.

These pair styles are designed to be used with either the [[pair_style lubricate]{.doc}]pair_lubricate.md){.reference .internal} or [[pair_style lubricateU]{.doc}]pair_lubricateU.md){.reference .internal} commands to provide thermostatting when dissipative lubrication forces are acting. Thus the parameters *mu*, *flaglog*, *flagfld*, *cutinner*, and *cutoff* should be specified consistent with the settings in the lubrication pair styles. For details, refer to either of the lubrication pair styles.

The *t_target* setting is used to specify the target temperature of the system. The random number *seed* is used to generate random numbers for the thermostatting procedure.

The *flagHI* and *flagVF* settings are optional. Neither should be used, or both must be defined.

------------------------------------------------------------------------

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- cutinner (distance units)

- cutoff (distance units)

The two coefficients are optional. If neither is specified, the two cutoffs specified in the pair_style command are used. Otherwise both must be specified.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the two cutoff distances for these pair styles can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for these pair styles.

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

These pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These styles are part of the COLLOID package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Only spherical monodisperse particles are allowed for pair_style brownian.

Only spherical particles are allowed for pair_style brownian/poly.

These pair styles are only compatible with the following wall fixes: doc:fix wall/lj93, fix wall/lj126, fix wall/lj1043, fix wall/colloid, fix wall/harmonic, fix wall/lepton, fix wall/morse, fix wall/table \<fix_wall\>.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_style lubricate]{.doc}]pair_lubricate.md){.reference .internal}, [[pair_style lubricateU]{.doc}]pair_lubricateU.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default settings for the optional args are flagHI = 1 and flagVF = 1.
:::
::::::::::::::
::::::::::::::::
:::::::::::::::::

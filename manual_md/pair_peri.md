::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-peri-pmb-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style peri/pmb command[](#pair-style-peri-pmb-command "Link to this heading"){.headerlink}

Accelerator Variants: *peri/pmb/omp*
:::

::: {#pair-style-peri-lps-command .section}
# pair_style peri/lps command[](#pair-style-peri-lps-command "Link to this heading"){.headerlink}

Accelerator Variants: *peri/lps/omp*
:::

::: {#pair-style-peri-ves-command .section}
# pair_style peri/ves command[](#pair-style-peri-ves-command "Link to this heading"){.headerlink}
:::

:::::::::::::: {#pair-style-peri-eps-command .section}
# pair_style peri/eps command[](#pair-style-peri-eps-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style
:::
::::

- style = *peri/pmb* or *peri/lps* or *peri/ves* or *peri/eps*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style peri/pmb
    pair_coeff * * 1.6863e22 0.0015001 0.0005 0.25

    pair_style peri/lps
    pair_coeff * * 14.9e9 14.9e9 0.0015001 0.0005 0.25

    pair_style peri/ves
    pair_coeff * * 14.9e9 14.9e9 0.0015001 0.0005 0.25 0.5 0.001

    pair_style peri/eps
    pair_coeff * * 14.9e9 14.9e9 0.0015001 0.0005 0.25 118.43
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The peridynamic pair styles implement material models that can be used at the mesoscopic and macroscopic scales. See [this document](PDF/PDLammps_overview.pdf){.reference .external} for an overview of LAMMPS commands for Peridynamics modeling.

Style *peri/pmb* implements the Peridynamic bond-based prototype microelastic brittle (PMB) model.

Style *peri/lps* implements the Peridynamic state-based linear peridynamic solid (LPS) model.

Style *peri/ves* implements the Peridynamic state-based linear peridynamic viscoelastic solid (VES) model.

Style *peri/eps* implements the Peridynamic state-based elastic-plastic solid (EPS) model.

The canonical papers on Peridynamics are [[(Silling 2000)]{.std .std-ref}](#silling2000){.reference .internal} and [[(Silling 2007)]{.std .std-ref}](#silling2007){.reference .internal}. The implementation of Peridynamics in LAMMPS is described in [[(Parks)]{.std .std-ref}](#parks){.reference .internal}. Also see the [[Peridynamics Howto]{.doc}]Howto_peri.md){.reference .internal} for more details about its implementation.

The peridynamic VES and EPS models in PDLAMMPS were implemented by R. Rahman and J. T. Foster at University of Texas at San Antonio. The original VES formulation is described in "(Mitchell2011)" and the original EPS formulation is in "(Mitchell2011a)". Additional PDF docs that describe the VES and EPS implementations are include in the LAMMPS distribution in [doc/PDF/PDLammps_VES.pdf](PDF/PDLammps_VES.pdf){.reference .external} and [doc/PDF/PDLammps_EPS.pdf](PDF/PDLammps_EPS.pdf){.reference .external}. For questions regarding the VES and EPS models in LAMMPS you can contact R. Rahman (rezwanur.rahman at utsa.edu).

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below.

For the *peri/pmb* style:

- c (energy/distance/volume\^2 units)

- horizon (distance units)

- s00 (unitless)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (unitless)

C is the effectively a spring constant for Peridynamic bonds, the horizon is a cutoff distance for truncating interactions, and s00 and [\\(\\alpha\\)]{.math .notranslate .nohighlight} are used as a bond breaking criteria. The units of c are such that c/distance = stiffness/volume\^2, where stiffness is energy/distance\^2 and volume is distance\^3. See the users guide for more details.

For the *peri/lps* style:

- K (force/area units)

- G (force/area units)

- horizon (distance units)

- s00 (unitless)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (unitless)

K is the bulk modulus and G is the shear modulus. The horizon is a cutoff distance for truncating interactions, and s00 and [\\(\\alpha\\)]{.math .notranslate .nohighlight} are used as a bond breaking criteria. See the users guide for more details.

For the *peri/ves* style:

- K (force/area units)

- G (force/area units)

- horizon (distance units)

- s00 (unitless)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (unitless)

- m_lambdai (unitless)

- m_taubi (unitless)

K is the bulk modulus and G is the shear modulus. The horizon is a cutoff distance for truncating interactions, and s00 and [\\(\\alpha\\)]{.math .notranslate .nohighlight} are used as a bond breaking criteria. m_lambdai and m_taubi are the viscoelastic relaxation parameter and time constant, respectively. m_lambdai varies within zero to one. For very small values of m_lambdai the viscoelastic model responds very similar to a linear elastic model. For details please see the description in "(Mitchell2011)".

For the *peri/eps* style:

- K (force/area units)

- G (force/area units)

- horizon (distance units)

- s00 (unitless)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (unitless)

- m_yield_stress (force/area units)

K is the bulk modulus and G is the shear modulus. The horizon is a cutoff distance and s00 and [\\(\\alpha\\)]{.math .notranslate .nohighlight} are used as a bond breaking criteria. m_yield_stress is the yield stress of the material. For details please see the description in "(Mitchell2011a)".

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

These pair styles do not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table and tail options are not relevant for these pair styles.

These pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

All of these styles are part of the PERI package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Parks)** Parks, Lehoucq, Plimpton, Silling, Comp Phys Comm, 179(11), 777-783 (2008).

**(Silling 2000)** Silling, J Mech Phys Solids, 48, 175-209 (2000).

**(Silling 2007)** Silling, Epton, Weckner, Xu, Askari, J Elasticity, 88, 151-184 (2007).

**(Mitchell2011)** Mitchell. A non-local, ordinary-state-based viscoelasticity model for peridynamics. Sandia National Lab Report, 8064:1-28 (2011).

**(Mitchell2011a)** Mitchell. A Nonlocal, Ordinary, State-Based Plasticity Model for Peridynamics. Sandia National Lab Report, 3166:1-34 (2011).
:::
::::::::::::::
::::::::::::::::::
:::::::::::::::::::

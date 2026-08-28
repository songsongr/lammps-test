:::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-edpd-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style edpd command[](#pair-style-edpd-command "Link to this heading"){.headerlink}

Accelerator Variants: *edpd/gpu*
:::

::: {#pair-style-mdpd-command .section}
# pair_style mdpd command[](#pair-style-mdpd-command "Link to this heading"){.headerlink}

Accelerator Variants: *mdpd/gpu*
:::

::: {#pair-style-mdpd-rhosum-command .section}
# pair_style mdpd/rhosum command[](#pair-style-mdpd-rhosum-command "Link to this heading"){.headerlink}
:::

::::::::::::::::::::::: {#pair-style-tdpd-command .section}
# pair_style tdpd command[](#pair-style-tdpd-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *edpd* or *mdpd* or *mdpd/rhosum* or *tdpd*

- args = list of arguments for a particular style

  ``` literal-block
  edpd args = cutoff seed
    cutoff = global cutoff for eDPD interactions (distance units)
    seed = random # seed (integer) (if <= 0, eDPD will use current time as the seed)
  mdpd args = T cutoff seed
    T = temperature (temperature units)
    cutoff = global cutoff for mDPD interactions (distance units)
    seed = random # seed (integer) (if <= 0, mDPD will use current time as the seed)
  mdpd/rhosum args =
  tdpd args = T cutoff seed
    T = temperature (temperature units)
    cutoff = global cutoff for tDPD interactions (distance units)
    seed = random # seed (integer) (if <= 0, tDPD will use current time as the seed)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style edpd 1.58 9872598
    pair_coeff * * 18.75 4.5 0.41 1.58 1.42E-5 2.0 1.58
    pair_coeff 1 1 18.75 4.5 0.41 1.58 1.42E-5 2.0 1.58 power 10.54 -3.66 3.44 -4.10
    pair_coeff 1 1 18.75 4.5 0.41 1.58 1.42E-5 2.0 1.58 power 10.54 -3.66 3.44 -4.10 kappa -0.44 -3.21 5.04 0.00

    pair_style hybrid/overlay mdpd/rhosum mdpd 1.0 1.0 65689
    pair_coeff 1 1 mdpd/rhosum  0.75
    pair_coeff 1 1 mdpd -40.0 25.0 18.0 1.0 0.75

    pair_style tdpd 1.0 1.58 935662
    pair_coeff * * 18.75 4.5 0.41 1.58 1.58 1.0 1.0E-5 2.0
    pair_coeff 1 1 18.75 4.5 0.41 1.58 1.58 1.0 1.0E-5 2.0 3.0 1.0E-5 2.0
:::
::::
:::::

::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *edpd* style computes the pairwise interactions and heat fluxes for eDPD particles following the formulations in [[(Li2014_JCP)]{.std .std-ref}](#li2014-jcp){.reference .internal} and [[Li2015_CC]{.std .std-ref}](#li2015-cc){.reference .internal}. The time evolution of an eDPD particle is governed by the conservation of momentum and energy given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\frac{\\mathrm{d}\^2 \\mathbf{r}\_i}{\\mathrm{d} t\^2}= \\frac{\\mathrm{d} \\mathbf{v}\_i}{\\mathrm{d} t} =\\mathbf{F}\_{i}=\\sum\_{i\\neq j}(\\mathbf{F}\_{ij}\^{C}+\\mathbf{F}\_{ij}\^{D}+\\mathbf{F}\_{ij}\^{R}) \\\\ C_v\\frac{\\mathrm{d} T_i}{\\mathrm{d} t}= q\_{i} = \\sum\_{i\\neq j}(q\_{ij}\^{C}+q\_{ij}\^{V}+q\_{ij}\^{R}),\\end{split}\\\]
:::

where the three components of [\\(F\_{i}\\)]{.math .notranslate .nohighlight} including the conservative force [\\(F\_{ij}\^C\\)]{.math .notranslate .nohighlight}, dissipative force [\\(F\_{ij}\^D\\)]{.math .notranslate .nohighlight} and random force [\\(F\_{ij}\^R\\)]{.math .notranslate .nohighlight} are expressed as

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathbf{F}\_{ij}\^{C} & = \\alpha\_{ij}{\\omega\_{C}}(r\_{ij})\\mathbf{e}\_{ij} \\\\ \\mathbf{F}\_{ij}\^{D} & = -\\gamma {\\omega\_{D}}(r\_{ij})(\\mathbf{e}\_{ij} \\cdot \\mathbf{v}\_{ij})\\mathbf{e}\_{ij} \\\\ \\mathbf{F}\_{ij}\^{R} & = \\sigma {\\omega\_{R}}(r\_{ij}){\\xi\_{ij}}\\Delta t\^{-1/2} \\mathbf{e}\_{ij} \\\\ \\omega\_{C}(r) & = 1 - r/r_c \\\\ \\alpha\_{ij} & = A\\cdot k_B(T_i + T_j)/2 \\\\ \\omega\_{D}(r) & = \\omega\^2\_{R}(r) = (1-r/r_c)\^s \\\\ \\sigma\_{ij}\^2 & = 4\\gamma k_B T_i T_j/(T_i + T_j)\\end{split}\\\]
:::

in which the exponent of the weighting function *s* can be defined as a temperature-dependent variable. The heat flux between particles accounting for the collisional heat flux [\\(q\^C\\)]{.math .notranslate .nohighlight}, viscous heat flux [\\(q\^V\\)]{.math .notranslate .nohighlight}, and random heat flux [\\(q\^R\\)]{.math .notranslate .nohighlight} are given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}q_i\^C & = \\sum\_{j \\ne i} k\_{ij} \\omega\_{CT}(r\_{ij}) \\left( \\frac{1}{T_i} - \\frac{1}{T_j} \\right) \\\\ q_i\^V & = \\frac{1}{2 C_v}\\sum\_{j \\ne i}{ \\left\\{ \\omega_D(r\_{ij})\\left\[\\gamma\_{ij} \\left( \\mathbf{e}\_{ij} \\cdot \\mathbf{v}\_{ij} \\right)\^2 - \\frac{\\left( \\sigma \_{ij} \\right)\^2}{m}\\right\] - \\sigma \_{ij} \\omega_R(r\_{ij})\\left( \\mathbf{e}\_{ij} \\cdot \\mathbf{v}\_{ij} \\right){\\xi\_{ij}} \\right\\} } \\\\ q_i\^R & = \\sum\_{j \\ne i} \\beta \_{ij} \\omega\_{RT}(r\_{ij}) d {t\^{ - 1/2}} \\xi\_{ij}\^e \\\\ \\omega\_{CT}(r) & =\\omega\_{RT}\^2(r)=\\left(1-r/r\_{ct}\\right)\^{s_T} \\\\ k\_{ij} & =C_v\^2\\kappa(T_i + T_j)\^2/4k_B \\\\ \\beta\_{ij}\^2 & = 2k_Bk\_{ij}\\end{split}\\\]
:::

where the mesoscopic heat friction [\\(\\kappa\\)]{.math .notranslate .nohighlight} is given by

::: {.math .notranslate .nohighlight}
\\\[\\kappa = \\frac{315k_B\\upsilon }{2\\pi \\rho C_v r\_{ct}\^5}\\frac{1}{Pr},\\\]
:::

with [\\(\\upsilon\\)]{.math .notranslate .nohighlight} being the kinematic viscosity. For more details, see Eq.(15) in [[(Li2014_JCP)]{.std .std-ref}](#li2014-jcp){.reference .internal}.

The following coefficients must be defined in eDPD system for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above.

- A (force units)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

- power_f (positive real)

- cutoff (distance units)

- kappa (thermal conductivity units)

- power_T (positive real)

- cutoff_T (distance units)

- optional keyword = power or kappa

The keyword *power* or *kappa* is optional. Both "power" and "kappa" require 4 parameters [\\(c_1, c_2, c_3, c_4\\)]{.math .notranslate .nohighlight} showing the temperature dependence of the exponent [\\(s(T) = \\mathrm{power}\_f ( 1+c_1 (T-1) + c_2 (T-1)\^2 + c_3 (T-1)\^3 + c_4 (T-1)\^4 )\\)]{.math .notranslate .nohighlight} and of the mesoscopic heat friction [\\(s_T(T) = \\kappa (1 + c_1 (T-1) + c_2 (T-1)\^2 + c_3 (T-1)\^3 + c_4 (T-1)\^4)\\)]{.math .notranslate .nohighlight}. If the keyword *power* or *kappa* is not specified, the eDPD system will use constant power_f and [\\(\\kappa\\)]{.math .notranslate .nohighlight}, which is independent to temperature changes.

------------------------------------------------------------------------

The *mdpd/rhosum* style computes the local particle mass density [\\(\\rho\\)]{.math .notranslate .nohighlight} for mDPD particles by kernel function interpolation.

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above.

- cutoff (distance units)

------------------------------------------------------------------------

The *mdpd* style computes the many-body interactions between mDPD particles following the formulations in [[(Li2013_POF)]{.std .std-ref}](#li2013-pof){.reference .internal}. The dissipative and random forces are in the form same as the classical DPD, but the conservative force is local density dependent, which are given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathbf{F}\_{ij}\^C & = Aw_c(r\_{ij})\\mathbf{e}\_{ij} + B(\\rho_i+\\rho_j)w_d(r\_{ij})\\mathbf{e}\_{ij} \\\\ \\mathbf{F}\_{ij}\^{D} & = -\\gamma {\\omega\_{D}}(r\_{ij})(\\mathbf{e}\_{ij} \\cdot \\mathbf{v}\_{ij})\\mathbf{e}\_{ij} \\\\ \\mathbf{F}\_{ij}\^{R} & = \\sigma {\\omega\_{R}}(r\_{ij}){\\xi\_{ij}}\\Delta t\^{-1/2} \\mathbf{e}\_{ij}\\end{split}\\\]
:::

where the first term in [\\(F_C\\)]{.math .notranslate .nohighlight} with a negative coefficient [\\(A \< 0\\)]{.math .notranslate .nohighlight} stands for an attractive force within an interaction range [\\(r_c\\)]{.math .notranslate .nohighlight}, and the second term with [\\(B \> 0\\)]{.math .notranslate .nohighlight} is the density-dependent repulsive force within an interaction range [\\(r_d\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above.

- A (force units)

- B (force units)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

- cutoff_c (distance units)

- cutoff_d (distance units)

------------------------------------------------------------------------

The *tdpd* style computes the pairwise interactions and chemical concentration fluxes for tDPD particles following the formulations in [[(Li2015_JCP)]{.std .std-ref}](#li2015-jcp){.reference .internal}. The time evolution of a tDPD particle is governed by the conservation of momentum and concentration given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\frac{\\mathrm{d}\^2 \\mathbf{r}\_i}{\\mathrm{d} t\^2} & = \\frac{\\mathrm{d} \\mathbf{v}\_i}{\\mathrm{d} t}=\\mathbf{F}\_{i}=\\sum\_{i\\neq j}(\\mathbf{F}\_{ij}\^{C}+\\mathbf{F}\_{ij}\^{D}+\\mathbf{F}\_{ij}\^{R}) \\\\ \\frac{\\mathrm{d} C\_{i}}{\\mathrm{d} t} & = Q\_{i} = \\sum\_{i\\neq j}(Q\_{ij}\^{D}+Q\_{ij}\^{R}) + Q\_{i}\^{S}\\end{split}\\\]
:::

where the three components of [\\(F\_{i}\\)]{.math .notranslate .nohighlight} including the conservative force [\\(F\_{ij}\^C\\)]{.math .notranslate .nohighlight}, dissipative force [\\(F\_{ij}\^C\\)]{.math .notranslate .nohighlight} and random force [\\(F\_{ij}\^C\\)]{.math .notranslate .nohighlight} are expressed as

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathbf{F}\_{ij}\^{C} & = A{\\omega\_{C}}(r\_{ij})\\mathbf{e}\_{ij} \\\\ \\mathbf{F}\_{ij}\^{D} & = -\\gamma {\\omega\_{D}}(r\_{ij})(\\mathbf{e}\_{ij} \\cdot \\mathbf{v}\_{ij})\\mathbf{e}\_{ij} \\\\ \\mathbf{F}\_{ij}\^{R} & = \\sigma {\\omega\_{R}}(r\_{ij}){\\xi\_{ij}}\\Delta t\^{-1/2} \\mathbf{e}\_{ij} \\\\ \\omega\_{C}(r) & = 1 - r/r_c \\\\ \\omega\_{D}(r) & = \\omega\^2\_{R}(r) = (1-r/r_c)\^\\mathrm{power_f} \\\\ \\sigma\^2 = 2\\gamma k_B T\\end{split}\\\]
:::

The concentration flux between two tDPD particles includes the Fickian flux [\\(Q\_{ij}\^D\\)]{.math .notranslate .nohighlight} and random flux [\\(Q\_{ij}\^R\\)]{.math .notranslate .nohighlight}, which are given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}Q\_{ij}\^D & = -\\kappa\_{ij} w\_{DC}(r\_{ij}) \\left( C_i - C_j \\right) \\\\ Q\_{ij}\^R & = \\epsilon\_{ij}\\left( C_i + C_j \\right) w\_{RC}(r\_{ij}) \\xi\_{ij} \\\\ w\_{DC}(r\_{ij}) & =w\^2\_{RC}(r\_{ij}) = (1 - r/r\_{cc})\^\\mathrm{power\_{cc}} \\\\ \\epsilon\_{ij}\^2 & = m_s\^2\\kappa\_{ij}\\rho\\end{split}\\\]
:::

where the parameters kappa and epsilon determine the strength of the Fickian and random fluxes. [\\(m_s\\)]{.math .notranslate .nohighlight} is the mass of a single solute molecule. In general, [\\(m_s\\)]{.math .notranslate .nohighlight} is much smaller than the mass of a tDPD particle *m*. For more details, see [[(Li2015_JCP)]{.std .std-ref}](#li2015-jcp){.reference .internal}.

The following coefficients must be defined for each pair of atom types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above.

- A (force units)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

- power_f (positive real)

- cutoff (distance units)

- cutoff_CC (distance units)

- [\\(\\kappa_i\\)]{.math .notranslate .nohighlight} (diffusivity units)

- [\\(\\epsilon_i\\)]{.math .notranslate .nohighlight} (diffusivity units)

- power_cc_i (positive real)

The last 3 values must be repeated Nspecies times, so that values for each of the Nspecies chemical species are specified, as indicated by the "I" suffix. In the first pair_coeff example above for pair_style tdpd, Nspecies = 1. In the second example, Nspecies = 2, so 3 additional coeffs are specified (for species 2).
:::::::::::

------------------------------------------------------------------------

::: {#example-scripts .section}
## Example scripts[](#example-scripts "Link to this heading"){.headerlink}

There are example scripts for using all these pair styles in examples/PACKAGES/mesodpd. The example for an eDPD simulation models heat conduction with source terms analog of periodic Poiseuille flow problem. The setup follows Fig.12 in [[(Li2014_JCP)]{.std .std-ref}](#li2014-jcp){.reference .internal}. The output of the short eDPD simulation (about 2 minutes on a single core) gives a temperature and density profiles as

![](_images/examples_edpd.jpg){.align-center}

The example for a mDPD simulation models the oscillations of a liquid droplet started from a liquid film. The mDPD parameters are adopted from [[(Li2013_POF)]{.std .std-ref}](#li2013-pof){.reference .internal}. The short mDPD run (about 2 minutes on a single core) generates a particle trajectory which can be visualized as follows.

![](_images/examples_mdpd.gif){.align-center} ![](_images/examples_mdpd_first.jpg){.align-center} ![](_images/examples_mdpd_last.jpg){.align-center}

The first image is the initial state of the simulation. If you click it a GIF movie should play in your browser. The second image is the final state of the simulation.

The example for a tDPD simulation computes the effective diffusion coefficient of a tDPD system using a method analogous to the periodic Poiseuille flow. The tDPD system is specified with two chemical species, and the setup follows Fig.1 in [[(Li2015_JCP)]{.std .std-ref}](#li2015-jcp){.reference .internal}. The output of the short tDPD simulation (about one and a half minutes on a single core) gives the concentration profiles of the two chemical species as

![](_images/examples_tdpd.jpg){.align-center}

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

The styles *edpd*, *mdpd*, *mdpd/rhosum* and *tdpd* do not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

The styles *edpd*, *mdpd*, *mdpd/rhosum* and *tdpd* do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

The styles *edpd*, *mdpd*, *mdpd/rhosum* and *tdpd* do not write information to [[binary restart files]{.doc}]restart.md){.reference .internal}. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The pair styles *edpd*, *mdpd*, *mdpd/rhosum* and *tdpd* are part of the DPD-MESO package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix mvv/dpd]{.doc}]fix_mvv_dpd.md){.reference .internal}, [[fix mvv/edpd]{.doc}]fix_mvv_dpd.md){.reference .internal}, [[fix mvv/tdpd]{.doc}]fix_mvv_dpd.md){.reference .internal}, [[fix edpd/source]{.doc}]fix_dpd_source.md){.reference .internal}, [[fix tdpd/source]{.doc}]fix_dpd_source.md){.reference .internal}, [[compute edpd/temp/atom]{.doc}]compute_edpd_temp_atom.md){.reference .internal}, [[compute tdpd/cc/atom]{.doc}]compute_tdpd_cc_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Li2014_JCP)** Li, Tang, Lei, Caswell, Karniadakis, J Comput Phys, 265: 113-127 (2014). DOI: 10.1016/j.jcp.2014.02.003.

**(Li2015_CC)** Li, Tang, Li, Karniadakis, Chem Commun, 51: 11038-11040 (2015). DOI: 10.1039/C5CC01684C.

**(Li2013_POF)** Li, Hu, Wang, Ma, Zhou, Phys Fluids, 25: 072103 (2013). DOI: 10.1063/1.4812366.

**(Li2015_JCP)** Li, Yazdani, Tartakovsky, Karniadakis, J Chem Phys, 143: 014101 (2015). DOI: 10.1063/1.4923254.
:::
:::::::::::::::::::::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::

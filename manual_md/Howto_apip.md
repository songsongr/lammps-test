:::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::: {#adaptive-precision-interatomic-potentials-apip .section}
# [10.5.13. ]{.section-number}Adaptive-precision interatomic potentials (APIP)[](#adaptive-precision-interatomic-potentials-apip "Link to this heading"){.headerlink}

The [[PKG-APIP]{.std .std-ref}]Packages_details.md#pkg-apip){.reference .internal} enables use of adaptive-precision potentials as described in [[(Immel2025)]{.std .std-ref}](#immel2025-1){.reference .internal} and [[(Immel2026)]{.std .std-ref}](#immel2026-2){.reference .internal}. In the context of this package, precision refers to the accuracy of an interatomic potential.

Modern machine-learning (ML) potentials translate the accuracy of DFT simulations into MD simulations, i.e., ML potentials are more accurate compared to traditional empirical potentials. However, this accuracy comes at a cost: there is a considerable performance gap between the evaluation of classical and ML potentials, e.g., the force calculation of a classical EAM potential is 100-1000 times faster compared to the ML-based ACE method. The evaluation time difference results in a conflict between large time and length scales on the one hand and accuracy on the other. This conflict is resolved by an APIP model for simulations, in which the highest precision is required only locally but not globally.

An APIP model uses a precise but expensive ML potential only for a subset of atoms, while a fast potential is used for the remaining atoms. Whether the precise or the fast potential is used is determined by a continuous switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} that can be defined for each atom [\\(i\\)]{.math .notranslate .nohighlight}. The switching parameter can be adjusted dynamically during a simulation or kept constant as explained below.

The potential energy [\\(E_i\\)]{.math .notranslate .nohighlight} of an atom [\\(i\\)]{.math .notranslate .nohighlight} described by an adaptive-precision interatomic potential is given by [[(Immel2025)]{.std .std-ref}](#immel2025-1){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[E_i = \\lambda_i E_i\^\\text{(fast)} + (1-\\lambda_i) E_i\^\\text{(precise)},\\\]
:::

where [\\(E_i\^\\text{(fast)}\\)]{.math .notranslate .nohighlight} is the potential energy of atom [\\(i\\)]{.math .notranslate .nohighlight} according to a fast interatomic potential, [\\(E_i\^\\text{(precise)}\\)]{.math .notranslate .nohighlight} is the potential energy according to a precise interatomic potential and [\\(\\lambda_i\\in\[0,1\]\\)]{.math .notranslate .nohighlight} is the switching parameter that decides how the potential energies are weighted.

Adaptive-precision saves computation time when the computation of the precise potential is not required for many atoms, i.e., when [\\(\\lambda_i=1\\)]{.math .notranslate .nohighlight} applies for many atoms.

The currently implemented potentials are:

  Fast potential                                             Precise potential
  ---------------------------------------------------------- ----------------------------------------------------------
  [[ACE]{.doc}]pair_pace_apip.md){.reference .internal}   [[ACE]{.doc}]pair_pace_apip.md){.reference .internal}
  [[EAM]{.doc}]pair_eam_apip.md){.reference .internal}    

In theory, any short-range potential can be used for an adaptive-precision interatomic potential. How to implement a new (fast or precise) adaptive-precision potential is explained in [[here]{.std .std-ref}](#implementing-new-apip-styles){.reference .internal}.

The switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} that combines the two potentials can be dynamically calculated during a simulation. There are two ways to calculate dynamic switching parameters.

1\. according to [[(Immel2026)]{.std .std-ref}](#immel2026-2){.reference .internal} with a differentiable switching parameter that results in a conservative potential. Energy and momentum are (in the absence of external forces) conserved by design.

2\. according to [[(Immel2025)]{.std .std-ref}](#immel2025-1){.reference .internal} with a non-differentiable switching parameter. In this case, the implementation can be optimized for performance by using the switching parameters of the previous timestep. Thereby, one can perform most of the switching-parameter calculation within the force-calculation routine and include this calculations in the load- balancing. The potential is not conservative and energy- and momentum-conservation are achieved through a local correction.

Alternatively, one can set a constant switching parameter before the start of a simulation. Using constant switching parameters results in a conservative potential.

To run a simulation with an adaptive-precision potential, one needs the following components:

::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
conservative dynamic switching parameter

dynamic switching parameter with correction

constant switching parameter
:::

::: {#panel-0-0-0 .sphinx-tabs-panel aria-labelledby="tab-0-0-0" role="tabpanel" tabindex="0"}
1.  [[atom_style apip conservative]{.doc}]atom_style.md){.reference .internal} so that the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} can be stored.

2.  A fast potential: [[eam/apip]{.doc}]pair_eam_apip.md){.reference .internal} or [[pace/fast/apip]{.doc}]pair_pace_apip.md){.reference .internal}.

3.  A precise potential: [[pace/precise/apip]{.doc}]pair_pace_apip.md){.reference .internal}.

4.  [[fix lambda/la/csp/apip]{.doc}]fix_lambda_la_csp_apip.md){.reference .internal} to calculate a differentiable switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight}.

5.  [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} to combine the previously mentioned pair_styles.

6.  [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal} to approximate the load caused by every atom, as the computations of the pair_styles are only required for a subset of atoms.

7.  [[fix balance]{.doc}]fix_balance.md){.reference .internal} to perform dynamic load balancing with the calculated load.
:::

::: {#panel-0-0-1 .sphinx-tabs-panel aria-labelledby="tab-0-0-1" hidden="true" role="tabpanel" tabindex="0"}
1.  [[atom_style apip]{.doc}]atom_style.md){.reference .internal} so that the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} can be stored.

2.  A fast potential: [[eam/apip]{.doc}]pair_eam_apip.md){.reference .internal} or [[pace/fast/apip]{.doc}]pair_pace_apip.md){.reference .internal}.

3.  A precise potential: [[pace/precise/apip]{.doc}]pair_pace_apip.md){.reference .internal}.

4.  [[pair_style lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal} to calculate [\\(\\lambda_i\^\\text{input}\\)]{.math .notranslate .nohighlight}, from which [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} is calculated.

5.  [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal} to calculate the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight}.

6.  [[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal} to calculate the spatial transition zone of the switching parameter.

7.  [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} to combine the previously mentioned pair_styles.

8.  [[fix lambda_thermostat/apip]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal} to conserve the energy when switching parameters change.

9.  [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal} to approximate the load caused by every atom, as the computations of the pair_styles are only required for a subset of atoms.

10. [[fix balance]{.doc}]fix_balance.md){.reference .internal} to perform dynamic load balancing with the calculated load.
:::

::: {#panel-0-0-2 .sphinx-tabs-panel aria-labelledby="tab-0-0-2" hidden="true" role="tabpanel" tabindex="0"}
1.  [[atom_style apip]{.doc}]atom_style.md){.reference .internal} so that the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} can be stored.

2.  A fast potential: [[eam/apip]{.doc}]pair_eam_apip.md){.reference .internal} or [[pace/fast/apip]{.doc}]pair_pace_apip.md){.reference .internal}.

3.  A precise potential: [[pace/precise/apip]{.doc}]pair_pace_apip.md){.reference .internal}.

4.  [[set]{.doc}]set.md){.reference .internal} command to set the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight}.

5.  [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} to combine the previously mentioned pair_styles.

6.  [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal} to approximate the load caused by every atom, as the computations of the pair_styles are only required for a subset of atoms.

7.  [[fix balance]{.doc}]fix_balance.md){.reference .internal} to perform dynamic load balancing with the calculated load.
:::
:::::::

------------------------------------------------------------------------

:::::::::::::::::: {#example .section}
## Example[](#example "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

How to select the values of the parameters of an adaptive-precision interatomic potential is discussed in detail in [[(Immel2025)]{.std .std-ref}](#immel2025-1){.reference .internal} and [[(Immel2026)]{.std .std-ref}](#immel2026-2){.reference .internal}.
:::

:::::::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
conservative dynamic switching parameter

dynamic switching parameter with correction

constant switching parameter
:::

:::::: {#panel-1-1-0 .sphinx-tabs-panel aria-labelledby="tab-1-1-0" role="tabpanel" tabindex="0"}
Lines like these would appear in the input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    atom_style apip conservative
    comm_style tiled

    pair_style hybrid/overlay eam/fs/apip pace/precise/apip
    pair_coeff * * eam/fs/apip Cu.eam.fs Cu
    pair_coeff * * pace/precise/apip Cu.yace Cu

    # calculate a differentiable switching parameter to obtain
    # a conservative potential
    fix 2 all lambda/la/csp/apip 0.24 1.5 11.0 12.0 bcc

    fix 4 all atom_weight/apip 100 eam ace 0 0 all

    variable myweight atom f_4

    fix 5 all balance 100 1.1 rcb weight var myweight
:::
::::

First, the [[atom_style apip conservative]{.doc}]atom_style.md){.reference .internal} and the communication style are set.

::: {.admonition .note}
Note

Note, that [[comm_style]{.doc}]comm_style.md){.reference .internal} *tiled* is required for the style *rcb* of [[fix balance]{.doc}]fix_balance.md){.reference .internal}, but not for APIP. However, the flexibility offered by the balancing style *rcb*, compared to the balancing style *shift*, is advantageous for APIP.
:::

A conservative adaptive-precision EAM-ACE potential is defined based on the differentiable switching parameter calculated by [[fix lambda/la/csp/apip]{.doc}]fix_lambda_la_csp_apip.md){.reference .internal}, i.e., [\\(\\lambda\\)]{.math .notranslate .nohighlight} is calculated from the locally averaged CSP. The [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} combines the fast EAM and the precise ACE potential, interpolated by the corresponding switching parameter. Furthermore, the [[fix lambda/la/csp/apip]{.doc}]fix_lambda_la_csp_apip.md){.reference .internal} calculates the forces caused by the differentiation of the switching parameter. Thereby, one obtains a conservative potential ([\\(\\pmb{F}\_i = -\\nabla_i \\sum_k E_k\\)]{.math .notranslate .nohighlight}) that by design conserves energy and momentum in the absence of external forces.

The fix 4 calculates the computational weight that is used by fix 5 to balance the load between different processors.
::::::

:::::: {#panel-1-1-1 .sphinx-tabs-panel aria-labelledby="tab-1-1-1" hidden="true" role="tabpanel" tabindex="0"}
Lines like these would appear in the input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    atom_style apip
    comm_style tiled

    pair_style hybrid/overlay eam/fs/apip pace/precise/apip lambda/input/csp/apip fcc cutoff 5.0 lambda/zone/apip 12.0
    pair_coeff * * eam/fs/apip Cu.eam.fs Cu
    pair_coeff * * pace/precise/apip Cu.yace Cu
    pair_coeff * * lambda/input/csp/apip
    pair_coeff * * lambda/zone/apip

    fix 2 all lambda/apip 2.5 3.0 time_averaged_zone 4.0 12.0 110 110 min_delta_lambda 0.01
    fix 3 all lambda_thermostat/apip N_rescaling 200
    fix 4 all atom_weight/apip 100 eam ace lambda/input lambda/zone all

    variable myweight atom f_4

    fix 5 all balance 100 1.1 rcb weight var myweight
:::
::::

First, the [[atom_style apip]{.doc}]atom_style.md){.reference .internal} and the communication style are set.

::: {.admonition .note}
Note

Note, that [[comm_style]{.doc}]comm_style.md){.reference .internal} *tiled* is required for the style *rcb* of [[fix balance]{.doc}]fix_balance.md){.reference .internal}, but not for APIP. However, the flexibility offered by the balancing style *rcb*, compared to the balancing style *shift*, is advantageous for APIP.
:::

An adaptive-precision EAM-ACE potential, for which the switching parameter [\\(\\lambda\\)]{.math .notranslate .nohighlight} is calculated from the CSP, is defined via [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}. The fixes ensure that the switching parameter is calculated, the energy conserved, the weight for the load balancing calculated and the load-balancing itself is done.
::::::

:::::: {#panel-1-1-2 .sphinx-tabs-panel aria-labelledby="tab-1-1-2" hidden="true" role="tabpanel" tabindex="0"}
Lines like these would appear in the input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    atom_style apip
    comm_style tiled

    pair_style hybrid/overlay eam/fs/apip pace/precise/apip
    pair_coeff * * eam/fs/apip Cu.eam.fs Cu
    pair_coeff * * pace/precise/apip Cu.yace Cu

    # calculate lambda somehow
    variable lambda atom ...
    set group all apip/lambda v_lambda

    fix 4 all atom_weight/apip 100 eam ace lambda/input lambda/zone all

    variable myweight atom f_4

    fix 5 all balance 100 1.1 rcb weight var myweight
:::
::::

First, the [[atom_style apip]{.doc}]atom_style.md){.reference .internal} and the communication style are set.

::: {.admonition .note}
Note

Note, that [[comm_style]{.doc}]comm_style.md){.reference .internal} *tiled* is required for the style *rcb* of [[fix balance]{.doc}]fix_balance.md){.reference .internal}, but not for APIP. However, the flexibility offered by the balancing style *rcb*, compared to the balancing style *shift*, is advantageous for APIP.
:::

An adaptive-precision EAM-ACE potential is defined via [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal}. The switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} of the adaptive-precision EAM-ACE potential is set via the [[set command]{.doc}]set.md){.reference .internal}. The parameter is not updated during the simulation. Therefore, the potential is conservative. The fixes ensure that the weight for the load balancing is calculated and the load-balancing itself is done.
::::::
::::::::::::::::

------------------------------------------------------------------------
::::::::::::::::::

::: {#implementing-new-apip-pair-styles .section}
[]{#implementing-new-apip-styles}

## Implementing new APIP pair styles[](#implementing-new-apip-pair-styles "Link to this heading"){.headerlink}

One can introduce adaptive-precision to an existing pair style by modifying the original pair style. One should calculate the force [\\(F_i = - \\nabla_i \\sum_j E_j\^\\text{original}\\)]{.math .notranslate .nohighlight} for a fast potential or [\\(F_i = - (1-\\nabla_i) \\sum_j E_j\^\\text{original}\\)]{.math .notranslate .nohighlight} for a precise potential from the original potential energy [\\(E_j\^\\text{original}\\)]{.math .notranslate .nohighlight} to see where the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} needs to be introduced in the force calculation. The switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} is known for all atoms [\\(i\\)]{.math .notranslate .nohighlight} in force calculation routine. One needs to introduce an abortion criterion based on [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} to ensure that all not required calculations are skipped and compute time can be saved. Furthermore, one needs to provide the number of calculations and measure the computation time. Communication within the force calculation needs to be prevented to allow effective load-balancing. With communication, the load balancer cannot balance few calculations of the precise potential on one processor with many computations of the fast potential on another processor.

All changes in the pair_style pace/apip compared to the pair_style pace are annotated and commented. Thus, the pair_style pace/apip can serve as an example for the implementation of new adaptive-precision potentials.

------------------------------------------------------------------------

**(Immel2025)** Immel, Drautz and Sutmann, J Chem Phys, 162, 114119 (2025)

**(Immel2026)** Immel, Drautz and Sutmann, arXiv:2512.07693
:::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::

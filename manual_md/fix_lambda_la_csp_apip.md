::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::: {#fix-lambda-la-csp-apip-command .section}
[]{#index-0}

# fix lambda/la/csp/apip command[](#fix-lambda-la-csp-apip-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID lambda/la/csp/apip thr_lo thr_hi cut_lo cut_hi lattice keyword args ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- lambda/la/csp/apip = style name of this fix command

- thr_lo = value below which the differentiable CSP results in a switching parameter of 1 (squared distance units)

- thr_hi = value above which the differentiable CSP results in a switching parameter of 0 (squared distance units)

- cut_lo = radius below which the weighting function for the local averaging is 1 (distance units)

- cut_hi = radius above which the weighting function for the local averaging is 0 (distance units)

- lattice = *fcc* or *bcc* or N = \# of neighbors per atom to include in the CSP calculation

- zero or more keyword/args pairs may be appended

- keyword = *csp_cut* or *csp_mode* or *forces* or *lambda_non_group* or *store_peratom*

  ``` literal-block
  csp_cut args = float
      float = neighboring atoms outside of this cutoff radius may not be considered for the CSP calculation
  csp_mode args = dynamic or static
      dynamic = use the differentiable CSP to calculate the switching parameter
      static = use the non-differentiable CSP instead of the differentiable one
  forces args = no or yes
      yes = compute the forces caused by the differentiation of the switching parameter
      no = do not compute the forces caused by the differentiation of the switching parameter
  lambda_non_group args = precise or fast or float
      precise = assign a constant switching parameter of 0 to atoms, that are not in the group specified by group-ID
      fast = assign a constant switching parameter of 1 to atoms, that are not in the group specified by group-ID
      float = assign this constant switching parameter to atoms, that are not in the group specified by group-ID (0 <= float <= 1)
  store_peratom args = integer
      integer = provide per-atom output every this many timesteps
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix lambda_la all lambda/la/csp/apip 0.25 1.5 15.0 16.0 bcc
    fix lambda_la mobile lambda/la/csp/apip 0.24 1.5 11.0 12.0 bcc lambda_non_group fast
:::
::::
:::::

:::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 30Mar2026.]{.versionmodified .added}
:::

The potential energy [\\(E_i\\)]{.math .notranslate .nohighlight} of an atom [\\(i\\)]{.math .notranslate .nohighlight} according to an adaptive-precision potential is given by [[(Immel2025)]{.std .std-ref}](#immel2025-8){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[E_i = \\lambda_i E_i\^\\text{(fast)} + (1-\\lambda_i) E_i\^\\text{(precise)}\\,,\\\]
:::

where [\\(E_i\^\\text{(fast)}\\)]{.math .notranslate .nohighlight} is the potential energy of atom [\\(i\\)]{.math .notranslate .nohighlight} according to a fast computable interatomic potential, [\\(E_i\^\\text{(precise)}\\)]{.math .notranslate .nohighlight} is the potential energy according to a precise interatomic potential and [\\(\\lambda_i\\in\[0,1\]\\)]{.math .notranslate .nohighlight} is the switching parameter that decides which potential energy is used.

This fix calculates the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} based on local averaging of a descriptor according to [[(Immel2026)]{.std .std-ref}](#immel2026-1){.reference .internal} and parts of the conservatively calculated force as will be discussed later. The descriptor is averaged within the cutoff radius provided as *cut_hi*.

Per default, a differentiable version of the centro-symmetry parameter (CSP) is used as descriptor. This differentiable version is described in detail in [[(Immel2026)]{.std .std-ref}](#immel2026-1){.reference .internal}. The usage of a differentiable CSP results in a conservative potential, that conserves (in the absence of external forces) energy and momentum by design. The force [\\(\\pmb{F}\_i=-\\nabla_i\\sum_kE_k\\)]{.math .notranslate .nohighlight} following from the adaptive-precision potential energy is given by

::: {.math .notranslate .nohighlight}
\\\[\\pmb{F}\_i = \\sum_k \\big(- \\lambda_k \\nabla_i E_k\^\\text{(fast)} - (1 - \\lambda_k) \\nabla_i E_k\^\\text{(precise)} + (\\nabla_i\\lambda_k) (E_k\^\\text{(precise)} - E_k\^\\text{(fast)})\\big)\\,.\\\]
:::

This fix calculates the terms [\\((\\nabla_i\\lambda_k) (E_k\^\\text{(precise)} - E_k\^\\text{(fast)})\\)]{.math .notranslate .nohighlight} based on potential energies that are provided by pair styles. This force-calculation is enabled by default, but prevented by *forces = no*. Thus, one can use this fix to only calculate switching parameters.

::: {.admonition .note}
Note

The fast potential and the precise potential are combined via [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} as shown in the code example below.
:::

The original CSP [[(Kelchner)]{.std .std-ref}](#kelchner-3){.reference .internal} is used instead of the differentiable CSP with the option *csp_mode dynamic*.

::: {.admonition .warning}
Warning

Note that the original CSP is not differentiable and does not result in a conservative potential.
:::

This fix calculates the switching parameter for all atoms in the [[group]{.doc}]group.md){.reference .internal} described by group-ID, while the value of *lambda_non_group* is used as switching parameter for all other atoms.

------------------------------------------------------------------------

A code example for the usage of a conservative adaptive-precision interatomic potential is given in the following: This fix calculates the switching parameter. The [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} is used to combine the two pair styles [[pair_style eam/fs/apip]{.doc}]pair_eam_apip.md){.reference .internal} and [[pair_style pace/precise/apip]{.doc}]pair_pace_apip.md){.reference .internal}, which calculate the potential energies [\\(E_k\^\\text{(precise)}\\)]{.math .notranslate .nohighlight} and [\\(E_k\^\\text{(fast)}\\)]{.math .notranslate .nohighlight}. The conservative force is calculated by both the fix and the pair styles.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix lambda_la all lambda/la/csp/apip 0.24 1.5 11.0 12.0 bcc
    pair_style hybrid/overlay eam/fs/apip pace/apip
    pair_coeff * * eam/fs/apip W.eam.fs W
    pair_coeff * * pace/apip W.yace W
:::
::::
::::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

The CSP neighbors of the differentiable CSP are saved and written to [[binary restart files]{.doc}]restart.md){.reference .internal} to allow a smooth restart of a simulation. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix can compute the force caused by the differentiation of the switching parameters. Therefore, the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *virial* option is supported by this fix to add the contribution of these forces to both the global pressure and per-atom stress of the system via the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} and [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} commands. The former can be accessed by [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify virial yes]{.doc}]fix_modify.md){.reference .internal}.

If the (non-conservative) dynamic CSP-pairs are used, this fix returns the accumulated number of changed CSP-pairs as global scalar. The potential is conservative as long as this number of changed CSP-pairs is constant (every changed CSP pair may change the total energy of the system). The global scalar can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}.

If *store_peratom* is used, 5 quantities are provided as per-atom vector: 1.-3. the force that is caused by the differentiation of the switching parameter, 4. the differentiable CSP and 5. the locally averaged differentiable CSP that was used to calculate the switching parameter. The per-atom vector can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the APIP package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style eam/apip]{.doc}]pair_eam_apip.md){.reference .internal}, [[pair_style pace/apip]{.doc}]pair_pace_apip.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

*forces* = *yes*, *csp_cut* = 5.0, *csp_mode* = *static*, *lambda_non_group* = 1, *store_peratom* = [\\(\\infty\\)]{.math .notranslate .nohighlight}

------------------------------------------------------------------------

**(Immel2025)** Immel, Drautz and Sutmann, J Chem Phys, 162, 114119 (2025)

**(Immel2026)** Immel, Drautz and Sutmann, arXiv:2512.07693

**(Kelchner)** Kelchner, Plimpton, Hamilton, Phys Rev B, 58, 11085 (1998)
:::
:::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

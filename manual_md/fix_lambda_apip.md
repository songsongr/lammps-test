::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::: {#fix-lambda-apip-command .section}
[]{#index-0}

# fix lambda/apip command[](#fix-lambda-apip-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID lambda/apip thr_lo thr_hi keyword args ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- lambda/apip = style name of this fix command

- thr_lo = value below which [\\(\\lambda_i\^\\text{input}\\)]{.math .notranslate .nohighlight} results in a switching parameter of 1

- thr_hi = value above which [\\(\\lambda_i\^\\text{input}\\)]{.math .notranslate .nohighlight} results in a switching parameter of 0

- zero or one keyword/args pairs may be appended

- keyword = *time_averaged_zone* or *min_delta_lambda* or *lambda_non_group* or *store_atomic_stats* or *dump_atomic_history* or *group_fast* or *group_precise* or *group_ignore_lambda_input*

  ``` literal-block
  time_averaged_zone args = cut_lo cut_hi history_len_lambda_input history_len_lambda
    cut_lo = distance at which the radial function decreases from 1
    cut_hi = distance from which on the radial function is 0
    history_len_lambda_input = number of time steps for which lambda_input is averaged
    history_len_lambda = number of time steps for which the switching parameter is averaged
  min_delta_lambda args = delta
    delta = value below which changes of the switching parameter are neglected (>= 0)
  lambda_non_group args = lambda_ng
    lambda_ng = precise or fast or float
      precise = assign a constant switching parameter of 0 to atoms, that are not in the group specified by group-ID
      fast = assign a constant switching parameter of 1 to atoms, that are not in the group specified by group-ID
      float = assign this constant switching parameter to atoms, that are not in the group specified by group-ID (0 <= float <= 1)
  group_fast args = group-ID-fast
    group-ID-fast = the switching parameter of 1 is used instead of the one computed by lambda_input for atoms in the group specified by group-ID-fast
  group_precise args = group-ID-precise
    group-ID-precise = the switching parameter of 0 is used instead of the one computed by lambda_input for atoms in the group specified by group-ID-precise
  group_ignore_lambda_input args = group-ID-ignore-lambda-input
    group-ID-ignore-lambda-input = the switching parameter of lambda_ng is used instead of the one computed by lambda_input for atoms in the group specified by group-ID-ignore-lambda-input
  store_atomic_stats args = none
  dump_atomic_history args = none
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 2 all lambda/apip 3.0 3.5 time_averaged_zone 4.0 12.0 110 110 min_delta_lambda 0.01
    fix 2 mobile lambda/apip 3.0 3.5 time_averaged_zone 4.0 12.0 110 110 min_delta_lambda 0.01 group_ignore_lambda_input immobile lambda_non_group fast
:::
::::
:::::

:::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The potential energy [\\(E_i\\)]{.math .notranslate .nohighlight} of an atom [\\(i\\)]{.math .notranslate .nohighlight} of an adaptive-precision potential according to [[(Immel)]{.std .std-ref}](#immel2025-3){.reference .internal} is given by

::: {.math .notranslate .nohighlight}
\\\[E_i = \\lambda_i E_i\^\\text{(fast)} + (1-\\lambda_i) E_i\^\\text{(precise)},\\\]
:::

whereas [\\(E_i\^\\text{(fast)}\\)]{.math .notranslate .nohighlight} is the potential energy of atom [\\(i\\)]{.math .notranslate .nohighlight} according to a fast interatomic potential like EAM, [\\(E_i\^\\text{(precise)}\\)]{.math .notranslate .nohighlight} is the potential energy according to a precise interatomic potential such as ACE and [\\(\\lambda_i\\in\[0,1\]\\)]{.math .notranslate .nohighlight} is the switching parameter that decides which potential energy is used. This fix calculates the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} based on the input provided from [[pair_style lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}.

The calculation of the switching parameter is described in detail in [[(Immel)]{.std .std-ref}](#immel2025-3){.reference .internal}. This fix calculates the switching parameter for all atoms in the [[group]{.doc}]group.md){.reference .internal} described by group-ID, while the value of *lambda_non_group* is used as switching parameter for all other atoms.

First, this fix calculates per atom [\\(i\\)]{.math .notranslate .nohighlight} the time averaged input [\\(\\lambda\^\\text{input}\_{\\text{avg},i}\\)]{.math .notranslate .nohighlight} from [\\(\\lambda\^\\text{input}\_{i}\\)]{.math .notranslate .nohighlight}, whereas the number of averaged timesteps can be set via *time_averaged_zone*.

::: {.admonition .note}
Note

[\\(\\lambda\^\\text{input}\_{i}\\)]{.math .notranslate .nohighlight} is calculated by [[pair_style lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}, which needs to be included in the input script as well.
:::

The time averaged input [\\(\\lambda\^\\text{input}\_{\\text{avg},i}\\)]{.math .notranslate .nohighlight} is then used to calculate the switching parameter

::: {.math .notranslate .nohighlight}
\\\[\\lambda\_{0,i}(t) = f\^\\text{(cut)} \\left(\\frac{\\lambda\_{\\text{avg},i}\^\\text{input}(t) - \\lambda\_\\text{lo}\^\\text{input}}{\\lambda\_\\text{hi}\^\\text{input} - \\lambda\_\\text{lo}\^\\text{input}} \\right)\\,,\\\]
:::

whereas the thresholds [\\(\\lambda\_\\text{hi}\^\\text{input}\\)]{.math .notranslate .nohighlight} and [\\(\\lambda\_\\text{lo}\^\\text{input}\\)]{.math .notranslate .nohighlight} are set by the values provided as *thr_lo* and *thr_hi* and [\\(f\^\\text{(cut)}(x)\\)]{.math .notranslate .nohighlight} is a cutoff function that is 1 for [\\(x\\leq 0\\)]{.math .notranslate .nohighlight}, decays from 1 to 0 for [\\(x\\in\[0,1\]\\)]{.math .notranslate .nohighlight}, and is 0 for [\\(x\\geq 1\\)]{.math .notranslate .nohighlight}. If the *group_precise* argument is used, [\\(\\lambda\_{0,i}=0\\)]{.math .notranslate .nohighlight} is used for all atoms [\\(i\\)]{.math .notranslate .nohighlight} assigned to the corresponding [[group]{.doc}]group.md){.reference .internal}. If the *group_fast* argument is used, [\\(\\lambda\_{0,i}=1\\)]{.math .notranslate .nohighlight} is used for all atoms [\\(i\\)]{.math .notranslate .nohighlight} assigned to the corresponding [[group]{.doc}]group.md){.reference .internal}. If an atom is in the groups *group_fast* and *group_precise*, [\\(\\lambda\_{0,i}=0\\)]{.math .notranslate .nohighlight} is used. If the *group_ignore_lambda_input* argument is used, [\\(\\lambda_i\^\\text{input}\\)]{.math .notranslate .nohighlight} is not computed for all atoms [\\(i\\)]{.math .notranslate .nohighlight} assigned to the corresponding [[group]{.doc}]group.md){.reference .internal}; instead, if the value is not already set by *group_fast* or *group_precise*, the value of *lambda_non_group* is used.

::: {.admonition .note}
Note

The computation of [\\(\\lambda_i\^\\text{input}\\)]{.math .notranslate .nohighlight} is not required for atoms that are in the groups *group_fast* and *group_precise*. Thus, one should use *group_ignore_lambda_input* and prevent the computation of [\\(\\lambda_i\^\\text{input}\\)]{.math .notranslate .nohighlight} for all atoms, for which a constant input is used.
:::

A spatial transition zone between the fast and the precise potential is introduced via

::: {.math .notranslate .nohighlight}
\\\[\\lambda\_{\\text{min},i}(t) = \\text{min}\\left(\\left\\{1 - (1 -\\lambda\_{0,j}(t)) f\^\\text{(cut)}\\left(\\frac{r\_{ij}(t)-r\_{\\lambda,\\text{lo}}}{r\_{\\lambda,\\text{hi}} - r\_{\\lambda,\\text{lo}}}\\right) : j \\in \\Omega\_{\\lambda,i} \\right\\}\\right)\\,,\\\]
:::

whereas the thresholds [\\(r\_{\\lambda,\\text{lo}}\\)]{.math .notranslate .nohighlight} and [\\(r\_{\\lambda,\\text{hi}}\\)]{.math .notranslate .nohighlight} of the cutoff function are set via *time_averaged_zone* and [\\(\\Omega\_{\\lambda,i}\\)]{.math .notranslate .nohighlight} is the set of neighboring atoms of atom [\\(i\\)]{.math .notranslate .nohighlight}.

::: {.admonition .note}
Note

[\\(\\lambda\_{\\text{min},i}\\)]{.math .notranslate .nohighlight} is calculated by [[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal}, which needs to be included in the input script as well.
:::

The switching parameter is smoothed by the calculation of the time average

::: {.math .notranslate .nohighlight}
\\\[\\lambda\_{\\text{avg},i}(t) = \\frac{1}{N\_{\\lambda,\\text{avg}}} \\sum\_{n=1}\^{N\_{\\lambda,\\text{avg}}} \\lambda\_{\\text{min},i}(t - n \\Delta t)\\,,\\\]
:::

whereas [\\(\\Delta t\\)]{.math .notranslate .nohighlight} is the [[timestep]{.doc}]timestep.md){.reference .internal} and [\\(N\_{\\lambda,\\text{avg}}\\)]{.math .notranslate .nohighlight} is the number of averaged timesteps, that can be set via *time_averaged_zone*.

Finally, numerical fluctuations of the switching parameter are suppressed by the usage of

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\lambda\_{i}(t) = \\left\\{ \\begin{array}{ll} \\lambda\_{\\text{avg},i}(t) & \\text{ for } \\left\|\\lambda\_{\\text{avg},i}(t) - \\lambda\_{i}(t-\\Delta t)\\right\|\\geq \\Delta\\lambda\_\\text{min} \\text{ or } \\lambda\_{\\text{avg},i}(t)\\in\\{0,1\\}, \\\\ \\lambda\_{i}(t-\\Delta t) & \\text{ otherwise}\\,, \\end{array} \\right.\\end{split}\\\]
:::

whereas the minimum change [\\(\\Delta\\lambda\_\\text{min}\\)]{.math .notranslate .nohighlight} is set by the *min_delta_lambda* argument.

::: {.admonition .note}
Note

*group_fast* affects only [\\(\\lambda\_{0,i}(t)\\)]{.math .notranslate .nohighlight}. The switching parameter of atoms in this [[group]{.doc}]group.md){.reference .internal} may change due to the calculation of the spatial switching zone. A switching parameter of 1 can be enforced by excluding the corresponding atoms from the [[group]{.doc}]group.md){.reference .internal} described by group-ID and using *lambda_non_group* 1 as argument.
:::

------------------------------------------------------------------------

A code example for the calculation of the switching parameter for an adaptive-precision potential is given in the following: The adaptive-precision potential is created by combining [[pair_style eam/fs/apip]{.doc}]pair_eam_apip.md){.reference .internal} and [[pair_style pace/precise/apip]{.doc}]pair_pace_apip.md){.reference .internal}. The input, from which the switching parameter is calculated, is provided by [[pair lambda/input/csp/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}. The switching parameter is calculated by this fix, whereas the spatial transition zone of the switching parameter is calculated by [[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal}.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay eam/fs/apip pace/precise/apip lambda/input/csp/apip fcc cutoff 5.0 lambda/zone/apip 12.0
    pair_coeff * * eam/fs/apip Cu.eam.fs Cu
    pair_coeff * * pace/precise/apip Cu_precise.yace Cu
    pair_coeff * * lambda/input/csp/apip
    pair_coeff * * lambda/zone/apip
    fix 2 all lambda/apip 3.0 3.5 time_averaged_zone 4.0 12.0 110 110 min_delta_lambda 0.01
:::
::::
::::::::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

The saved history of the switching parameter [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} and the saved history of [\\(\\lambda_i\^\\text{input}\\)]{.math .notranslate .nohighlight} are written to [[binary restart files]{.doc}]restart.md){.reference .internal} to allow a smooth restart of a simulation. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

If the *store_atomic_stats* argument is used, basic statistics is provided as per-atom array:

> ::: {}
> 1.  [\\(\\lambda_i\^\\text{input}(t)\\)]{.math .notranslate .nohighlight}
>
> 2.  [\\(\\lambda\_{\\text{avg},i}\^\\text{input}(t)\\)]{.math .notranslate .nohighlight}
>
> 3.  [\\(\\lambda\_{0,i}(t)\\)]{.math .notranslate .nohighlight}
>
> 4.  [\\(\\lambda\_{\\text{min},i}(t)\\)]{.math .notranslate .nohighlight}
>
> 5.  [\\(\\lambda\_{i}(t)\\)]{.math .notranslate .nohighlight}
> :::

If the *dump_atomic_history* argument is used, the whole saved history of [\\(\\lambda_i\^\\text{input}(t)\\)]{.math .notranslate .nohighlight} is appended to the previously mentioned array per atom.

The per-atom vector can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the APIP package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal}, [[pair_style lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}, [[pair_style eam/apip]{.doc}]pair_eam_apip.md){.reference .internal}, [[pair_style pace/apip]{.doc}]pair_pace_apip.md){.reference .internal}, [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal} [[fix lambda_thermostat/apip]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal},
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

*min_delta_lambda* = 0, *lambda_non_group* = 1, *cut_lo* = 4.0, *cut_hi* = 12.0, *history_len_lambda_input* = 100, *history_len_lambda* = 100, *store_atomic_stats* is not used, *dump_atomic_history* is not used, *group_fast* is not used, *group_precise* is not used, *group_ignore_lambda_input* is not used

------------------------------------------------------------------------

**(Immel)** Immel, Drautz and Sutmann, J Chem Phys, 162, 114119 (2025)
:::
:::::::::::::::::::::::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::

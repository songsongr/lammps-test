:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#compute-ti-command .section}
[]{#index-0}

# compute ti command[](#compute-ti-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group ti keyword args ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- ti = style name of this compute command

- one or more attribute/arg pairs may be appended

- keyword = pair style (lj/cut, gauss, born, etc.) or *tail* or *kspace*

  ``` literal-block
  pair style args = atype v_name1 v_name2
    atype = atom type (see asterisk form below)
    v_name1 = variable with name1 that is energy scale factor and function of lambda
    v_name2 = variable with name2 that is derivative of v_name1 with respect to lambda
  tail args = atype v_name1 v_name2
    atype = atom type (see asterisk form below)
    v_name1 = variable with name1 that is energy tail correction scale factor and function of lambda
    v_name2 = variable with name2 that is derivative of v_name1 with respect to lambda
  kspace args = atype v_name1 v_name2
    atype = atom type (see asterisk form below)
    v_name1 = variable with name1 that is K-Space scale factor and function of lambda
    v_name2 = variable with name2 that is derivative of v_name1 with respect to lambda
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all ti lj/cut 1 v_lj v_dlj coul/long 2 v_c v_dc kspace 1 v_ks v_dks
    compute 1 all ti lj/cut 1*3 v_lj v_dlj coul/long * v_c v_dc kspace * v_ks v_dks
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the derivative of the interaction potential with respect to *lambda*, the coupling parameter used in a thermodynamic integration. This derivative can be used to infer a free energy difference resulting from an alchemical simulation, as described in [[Eike]{.std .std-ref}](#eike){.reference .internal}.

Typically this compute will be used in conjunction with the [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command which can perform alchemical transformations by adjusting the strength of an interaction potential as a simulation runs, as defined by one or more [[pair_style]{.doc}]pair_style.md){.reference .internal} or [[kspace_style]{.doc}]kspace_style.md){.reference .internal} commands. This scaling is done via a prefactor on the energy, forces, virial calculated by the pair or [\\(k\\)]{.math .notranslate .nohighlight}-space style. The prefactor is often a function of a *lambda* parameter which may be adjusted from 0 to 1 (or vice versa) over the course of a [[run]{.doc}]run.md){.reference .internal}. The time-dependent adjustment is what the [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command does.

Assume that the unscaled energy of a pair_style or kspace_style is given by [\\(U\\)]{.math .notranslate .nohighlight}. Then the scaled energy is

::: {.math .notranslate .nohighlight}
\\\[U_s = f(\\lambda) U\\\]
:::

where [\\(f\\)]{.math .notranslate .nohighlight} is some function of [\\(\\lambda\\)]{.math .notranslate .nohighlight}. What this compute calculates is

::: {.math .notranslate .nohighlight}
\\\[\\frac{dU_s}{d\\lambda} = U \\frac{df(\\lambda)}{d\\lambda} = \\frac{U_s}{f(\\lambda)} \\frac{df(\\lambda)}{d\\lambda},\\\]
:::

which is the derivative of the system's scaled potential energy [\\(U_s\\)]{.math .notranslate .nohighlight} with respect to [\\(\\lambda\\)]{.math .notranslate .nohighlight}.

To perform this calculation, you provide one or more atom types as *atype*. The variable *atype* can be specified in one of two ways. An explicit numeric value can be used, as in the first example above, or a wildcard asterisk can be used in place of or in conjunction with the *atype* argument to select multiple atom types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of atom types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to N (inclusive). A middle asterisk means all types from m to n (inclusive).

You also specify two functions, as [[equal-style variables]{.doc}]variable.md){.reference .internal}. The first is specified as *v_name1*, where *name1* is the name of the variable, and is [\\(f(\\lambda)\\)]{.math .notranslate .nohighlight} in the notation above. The second is specified as *v_name2*, where *name2* is the name of the variable, and is [\\(df(\\lambda)/d\\lambda\\)]{.math .notranslate .nohighlight} in the notation above (i.e., it is the analytic derivative of [\\(f\\)]{.math .notranslate .nohighlight} with respect to [\\(\\lambda\\)]{.math .notranslate .nohighlight}). Note that the *name1* variable is also typically given as an argument to the [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command.

An alchemical simulation may use several pair potentials together, invoked via the [[pair_style hybrid or hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} command. The total [\\(dU_s/d\\lambda\\)]{.math .notranslate .nohighlight} for the overall system is calculated as the sum of each contributing term as listed by the keywords in the [[compute ti]{.doc}](#){.reference .internal} command. Individual pair potentials can be listed, which will be sub-styles in the hybrid case. You can also include a [\\(k\\)]{.math .notranslate .nohighlight}-space term via the *kspace* keyword. You can also include a pairwise long-range tail correction to the energy via the *tail* keyword.

For each term, you can specify a different (or the same) scale factor by the two variables that you list. Again, these will typically correspond toe the scale factors applied to these various potentials and the [\\(k\\)]{.math .notranslate .nohighlight}-space contribution via the [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command.

More details about the exact functional forms for the computation of [\\(du/dl\\)]{.math .notranslate .nohighlight} can be found in the paper by [[Eike]{.std .std-ref}](#eike){.reference .internal}.
:::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar, namely [\\(dU_s/d\\lambda\\)]{.math .notranslate .nohighlight}. This value can be used by any command that uses a global scalar value from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "extensive".

The scalar value will be in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EXTRA-COMPUTE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix adapt]{.doc}]fix_adapt.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Eike)** Eike and Maginn, Journal of Chemical Physics, 124, 164503 (2006).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

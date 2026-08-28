::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::: {#compute-fep-command .section}
[]{#index-0}

# compute fep command[](#compute-fep-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID fep temp attribute args ... keyword value ...
:::
::::

- ID, group-ID are documented in the [[compute]{.doc}]compute.md){.reference .internal} command

- fep = name of this compute command

- temp = external temperature (as specified for constant-temperature run)

- one or more attributes with args may be appended

- attribute = *pair* or *atom*

  ``` literal-block
  pair args = pstyle pparam I J v_delta
    pstyle = pair style name (e.g., lj/cut)
    pparam = parameter to perturb
    I,J = type pair(s) to set parameter for
    v_delta = variable with perturbation to apply (in the units of the parameter)
  atom args = aparam I v_delta
    aparam = charge = parameter to perturb
    I = type to set parameter for
    v_delta = variable with perturbation to apply (in the units of the parameter)
  ```

- zero or more keyword/value pairs may be appended

- keyword = *tail* or *volume*

  ``` literal-block
  tail value = no or yes
    no = ignore tail correction to pair energies (usually small in fep)
    yes = include tail correction to pair energies
  volume value = no or yes
    no = ignore volume changes (e.g., in NVE or NVT trajectories)
    yes = include volume changes (e.g., in NPT trajectories)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all fep 298 pair lj/cut epsilon 1 * v_delta pair lj/cut sigma 1 * v_delta volume yes
    compute 1 all fep 300 atom charge 2 v_delta
:::
::::

Example input scripts available: examples/PACKAGES/fep
:::::

:::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply a perturbation to parameters of the interaction potential and recalculate the pair potential energy without changing the atomic coordinates from those of the reference, unperturbed system. This compute can be used to calculate free energy differences using several methods, such as free-energy perturbation (FEP), finite-difference thermodynamic integration (FDTI) or Bennet's acceptance ratio method (BAR).

The potential energy of the system is decomposed in three terms: a background term corresponding to interaction sites whose parameters remain constant, a reference term [\\(U_0\\)]{.math .notranslate .nohighlight} corresponding to the initial interactions of the atoms that will undergo perturbation, and a term [\\(U_1\\)]{.math .notranslate .nohighlight} corresponding to the final interactions of these atoms:

::: {.math .notranslate .nohighlight}
\\\[U(\\lambda) = U\_{\\mathrm{bg}} + U_1(\\lambda) + U_0(\\lambda)\\\]
:::

A coupling parameter [\\(\\lambda\\)]{.math .notranslate .nohighlight} varying from 0 to 1 connects the reference and perturbed systems:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\lambda &= 0 \\quad\\Rightarrow\\quad U = U\_{\\mathrm{bg}} + U_0 \\\\ \\lambda &= 1 \\quad\\Rightarrow\\quad U = U\_{\\mathrm{bg}} + U_1\\end{split}\\\]
:::

It is possible but not necessary that the coupling parameter (or a function thereof) appears as a multiplication factor of the potential energy. Therefore, this compute can apply perturbations to interaction parameters that are not directly proportional to the potential energy (e.g., [\\(\\sigma\\)]{.math .notranslate .nohighlight} in Lennard-Jones potentials).

This command can be combined with [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} to perform multistage free-energy perturbation calculations along stepwise alchemical transformations during a simulation run:

::: {.math .notranslate .nohighlight}
\\\[\\Delta_0\^1 A = \\sum\_{i=0}\^{n-1} \\Delta\_{\\lambda_i}\^{\\lambda\_{i+1}} A = - k_B T \\sum\_{i=0}\^{n-1} \\ln \\left\< \\exp \\left( - \\frac{U(\\lambda\_{i+1}) - U(\\lambda_i)}{k_B T} \\right) \\right\>\_{\\lambda_i}\\\]
:::

This compute is suitable for the finite-difference thermodynamic integration (FDTI) method [[(Mezei)]{.std .std-ref}](#mezei){.reference .internal}, which is based on an evaluation of the numerical derivative of the free energy by a perturbation method using a very small [\\(\\delta\\)]{.math .notranslate .nohighlight}:

::: {.math .notranslate .nohighlight}
\\\[\\Delta_0\^1 A = \\int\_{\\lambda=0}\^{\\lambda=1} \\left( \\frac{\\partial A(\\lambda)}{\\partial\\lambda} \\right)\_\\lambda \\mathrm{d}\\lambda \\approx \\sum\_{i=0}\^{n-1} w_i \\frac{A(\\lambda\_{i} + \\delta) - A(\\lambda_i)}{\\delta}\\\]
:::

where [\\(w_i\\)]{.math .notranslate .nohighlight} are weights of a numerical quadrature. The [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command can be used to define the stages of [\\(\\lambda\\)]{.math .notranslate .nohighlight} at which the derivative is calculated and averaged.

The compute fep calculates the exponential Boltzmann term and also the potential energy difference [\\(U_1 -U_0\\)]{.math .notranslate .nohighlight}. By choosing a very small perturbation [\\(\\delta\\)]{.math .notranslate .nohighlight} the thermodynamic integration method can be implemented using a numerical evaluation of the derivative of the potential energy with respect to [\\(\\lambda\\)]{.math .notranslate .nohighlight}:

::: {.math .notranslate .nohighlight}
\\\[\\Delta_0\^1 A = \\int\_{\\lambda=0}\^{\\lambda=1} \\left\< \\frac{\\partial U(\\lambda)}{\\partial\\lambda} \\right\>\_\\lambda \\mathrm{d}\\lambda \\approx \\sum\_{i=0}\^{n-1} w_i \\left\< \\frac{U(\\lambda\_{i} + \\delta) - U(\\lambda_i)}{\\delta} \\right\>\_{\\lambda_i}\\\]
:::

Another technique to calculate free energy differences is the acceptance ratio method [[(Bennet)]{.std .std-ref}](#bennet){.reference .internal}, which can be implemented by calculating the potential energy differences with [\\(\\delta = 1.0\\)]{.math .notranslate .nohighlight} on both the forward and reverse routes:

::: {.math .notranslate .nohighlight}
\\\[\\left\< \\frac{1}{1 + \\exp\\left\[\\left(U_1 - U_0 - \\Delta_0\^1A \\right) /k_B T \\right\]} \\right\>\_0 = \\left\< \\frac{1}{1 + \\exp\\left\[\\left(U_0 - U_1 + \\Delta_0\^1A \\right) /k_B T \\right\]} \\right\>\_1\\\]
:::

The value of the free energy difference is determined by numerical root finding to establish the equality.

Concerning the choice of how the atomic parameters are perturbed in order to setup an alchemical transformation route, several strategies are available, such as single-topology or double-topology strategies [[(Pearlman)]{.std .std-ref}](#pearlman){.reference .internal}. The latter does not require modification of bond lengths, angles or other internal coordinates.

NOTES: This compute command does not take kinetic energy into account, therefore the masses of the particles should not be modified between the reference and perturbed states, or along the alchemical transformation route. This compute command does not change bond lengths or other internal coordinates [[(Boresch, Karplus)]{.std .std-ref}](#boreschkarplus){.reference .internal}.

------------------------------------------------------------------------

The *pair* attribute enables various parameters of potentials defined by the [[pair_style]{.doc}]pair_style.md){.reference .internal} and [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} commands to be changed, if the pair style supports it.

The *pstyle* argument is the name of the pair style. For example, *pstyle* could be specified as "lj/cut". The *pparam* argument is the name of the parameter to change. This is a list of pair styles and parameters that can be used with this compute. See the doc pages for individual pair styles and their energy formulas for the meaning of these parameters:

  ----------------------------------------------------------------------------------------------------------- ------------------------- ------------
  [[born]{.doc}]pair_born.md){.reference .internal}                                                        a,b,c                     type pairs
  [[buck, buck/coul/cut, buck/coul/long, buck/coul/msm]{.doc}]pair_buck.md){.reference .internal}          a,c                       type pairs
  [[buck/mdf]{.doc}]pair_mdf.md){.reference .internal}                                                     a,c                       type pairs
  [[coul/cut]{.doc}]pair_coul.md){.reference .internal}                                                    scale                     type pairs
  [[coul/cut/soft]{.doc}]pair_fep_soft.md){.reference .internal}                                           lambda                    type pairs
  [[coul/long, coul/msm]{.doc}]pair_coul.md){.reference .internal}                                         scale                     type pairs
  [[coul/long/soft]{.doc}]pair_fep_soft.md){.reference .internal}                                          scale, lambda             type pairs
  [[eam]{.doc}]pair_eam.md){.reference .internal}                                                          scale                     type pairs
  [[gauss]{.doc}]pair_gauss.md){.reference .internal}                                                      a                         type pairs
  [[lennard/mdf]{.doc}]pair_mdf.md){.reference .internal}                                                  a,b                       type pairs
  [[lj/class2]{.doc}]pair_class2.md){.reference .internal}                                                 epsilon,sigma             type pairs
  [[lj/class2/coul/cut, lj/class2/coul/long]{.doc}]pair_class2.md){.reference .internal}                   epsilon,sigma             type pairs
  [[lj/cut]{.doc}]pair_lj.md){.reference .internal}                                                        epsilon,sigma             type pairs
  [[lj/cut/soft]{.doc}]pair_fep_soft.md){.reference .internal}                                             epsilon,sigma,lambda      type pairs
  [[lj/cut/coul/cut, lj/cut/coul/long, lj/cut/coul/msm]{.doc}]pair_lj_cut_coul.md){.reference .internal}   epsilon,sigma             type pairs
  [[lj/cut/coul/cut/soft, lj/cut/coul/long/soft]{.doc}]pair_fep_soft.md){.reference .internal}             epsilon,sigma,lambda      type pairs
  [[lj/cut/tip4p/cut, lj/cut/tip4p/long]{.doc}]pair_lj_cut_tip4p.md){.reference .internal}                 epsilon,sigma             type pairs
  [[lj/cut/tip4p/long/soft]{.doc}]pair_fep_soft.md){.reference .internal}                                  epsilon,sigma,lambda      type pairs
  [[lj/expand]{.doc}]pair_lj_expand.md){.reference .internal}                                              epsilon,sigma,delta       type pairs
  [[lj/mdf]{.doc}]pair_mdf.md){.reference .internal}                                                       epsilon,sigma             type pairs
  [[lj/sf/dipole/sf]{.doc}]pair_dipole.md){.reference .internal}                                           epsilon,sigma,scale       type pairs
  [[mie/cut]{.doc}]pair_mie.md){.reference .internal}                                                      epsilon,sigma,gamR,gamA   type pairs
  [[morse, morse/smooth/linear]{.doc}]pair_morse.md){.reference .internal}                                 d0,r0,alpha               type pairs
  [[morse/soft]{.doc}]pair_morse.md){.reference .internal}                                                 d0,r0,alpha,lambda        type pairs
  [[nm/cut]{.doc}]pair_nm.md){.reference .internal}                                                        e0,r0,nn,mm               type pairs
  [[nm/cut/coul/cut, nm/cut/coul/long]{.doc}]pair_nm.md){.reference .internal}                             e0,r0,nn,mm               type pairs
  [[ufm]{.doc}]pair_ufm.md){.reference .internal}                                                          epsilon,sigma,scale       type pairs
  [[soft]{.doc}]pair_soft.md){.reference .internal}                                                        a                         type pairs
  ----------------------------------------------------------------------------------------------------------- ------------------------- ------------

Note that it is easy to add new potentials and their parameters to this list. All it typically takes is adding an extract() method to the pair\_\*.cpp file associated with the potential.

Similar to the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command, I and J can be specified in one of two ways. Explicit numeric values can be used for each, as in the first example above. I [\\(\\le\\)]{.math .notranslate .nohighlight} J is required. LAMMPS sets the coefficients for the symmetric J,I interaction to the same values. A wild-card asterisk can be used in place of or in conjunction with the I,J arguments to set the coefficients for multiple pairs of atom types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of atom types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to N (inclusive). A middle asterisk means all types from m to n (inclusive). Note that only type pairs with I [\\(\\le\\)]{.math .notranslate .nohighlight} J are considered; if asterisks imply type pairs where J [\\(\<\\)]{.math .notranslate .nohighlight} I, they are ignored.

If [[pair_style hybrid or hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} is being used, then the *pstyle* will be a sub-style name. You must specify I,J arguments that correspond to type pair values defined (via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command) for that sub-style.

The *v_name* argument for keyword *pair* is the name of an [[equal-style variable]{.doc}]variable.md){.reference .internal} which will be evaluated each time this compute is invoked. It should be specified as v_name, where name is the variable name.

------------------------------------------------------------------------

The *atom* attribute enables atom properties to be changed. The *aparam* argument is the name of the parameter to change. This is the current list of atom parameters that can be used with this compute:

- charge = charge on particle

The *v_name* argument for keyword *pair* is the name of an [[equal-style variable]{.doc}]variable.md){.reference .internal} which will be evaluated each time this compute is invoked. It should be specified as v_name, where name is the variable name.

------------------------------------------------------------------------

The *tail* keyword controls the calculation of the tail correction to "van der Waals" pair energies beyond the cutoff, if this has been activated via the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} command. If the perturbation is small, the tail contribution to the energy difference between the reference and perturbed systems should be negligible.

If the keyword *volume* = *yes*, then the Boltzmann term is multiplied by the volume so that correct ensemble averaging can be performed over trajectories during which the volume fluctuates or changes [[(Allen and Tildesley)]{.std .std-ref}](#allentildesley){.reference .internal}:

::: {.math .notranslate .nohighlight}
\\\[\\Delta_0\^1 A = - k_B T \\sum\_{i=0}\^{n-1} \\ln \\frac{\\left\< V \\exp \\left( - \\frac{U(\\lambda\_{i+1}) - U(\\lambda_i)}{k_B T} \\right) \\right\>\_{\\lambda_i}}{\\left\< V \\right\>\_{\\lambda_i}}\\\]
:::
::::::::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector of length 3 which contains the energy difference ( [\\(U_1-U_0\\)]{.math .notranslate .nohighlight} ) as c_ID\[1\], the Boltzmann factor [\\(\\exp(-(U_1-U_0)/k_B T)\\)]{.math .notranslate .nohighlight}, or [\\(V \\exp(-(U_1-U_0)/k_B T)\\)]{.math .notranslate .nohighlight}, as c_ID\[2\] and the volume of the simulation box [\\(V\\)]{.math .notranslate .nohighlight} as c_ID\[3\]. [\\(U_1\\)]{.math .notranslate .nohighlight} is the pair potential energy obtained with the perturbed parameters and [\\(U_0\\)]{.math .notranslate .nohighlight} is the pair potential energy obtained with the unperturbed parameters. The energies include kspace terms if these are used in the simulation.

These output results can be used by any command that uses a global scalar or vector from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options. For example, the computed values can be averaged using [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}.

The values calculated by this compute are "extensive".
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is distributed as the FEP package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix adapt/fep]{.doc}]fix_adapt_fep.md){.reference .internal}, [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}, [[pair_style .../soft]{.doc}]pair_fep_soft.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *tail* = *no*, *volume* = *no*.

------------------------------------------------------------------------

**(Pearlman)** Pearlman, J Chem Phys, 98, 1487 (1994)

**(Mezei)** Mezei, J Chem Phys, 86, 7084 (1987)

**(Bennet)** Bennet, J Comput Phys, 22, 245 (1976)

**(BoreschKarplus)** Boresch and Karplus, J Phys Chem A, 103, 103 (1999)

**(AllenTildesley)** Allen and Tildesley, Computer Simulation of Liquids, Oxford University Press (1987)
:::
:::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

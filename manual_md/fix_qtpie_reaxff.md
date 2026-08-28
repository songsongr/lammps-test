:::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::: {#fix-qtpie-reaxff-command .section}
[]{#index-0}

# fix qtpie/reaxff command[](#fix-qtpie-reaxff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID qtpie/reaxff Nevery cutlo cuthi tolerance params gfile args
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- qtpie/reaxff = style name of this fix command

- Nevery = perform QTPIE every this many steps

- cutlo,cuthi = lo and hi cutoff for Taper radius

- tolerance = precision to which charges will be equilibrated

- params = reaxff or a filename

- gfile = the name of a file containing Gaussian orbital exponents

- one or more keywords or keyword/value pairs may be appended

  ``` literal-block
  keyword = scale or maxiter or nowarn
    scale beta = set value of scaling factor beta (determines strength of electric polarization)
    maxiter N = limit the number of iterations to N
    nowarn = do not print a warning message if the maximum number of iterations is reached
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all qtpie/reaxff 1 0.0 10.0 1.0e-6 reaxff exp.qtpie
    fix 1 all qtpie/reaxff 1 0.0 10.0 1.0e-6 params.qtpie exp.qtpie scale 1.5 maxiter 500 nowarn
:::
::::
:::::

::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 19Nov2024.]{.versionmodified .added}
:::

The QTPIE charge equilibration method is an extension of the QEq charge equilibration method. With QTPIE, the partial charges on individual atoms are computed by minimizing the electrostatic energy of the system in the same way as the QEq method but where the absolute electronegativity, [\\(\\chi_i\\)]{.math .notranslate .nohighlight}, of each atom in the QEq charge equilibration scheme [[(Rappe and Goddard)]{.std .std-ref}](#rappe3){.reference .internal} is replaced with an effective electronegativity given by [[(Chen)]{.std .std-ref}](#qtpie-chen){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[\\tilde{\\chi}\_{i} = \\frac{\\sum\_{j=1}\^{N} (\\chi_i - \\chi_j) S\_{ij}} {\\sum\_{m=1}\^{N}S\_{im}},\\\]
:::

which acts to penalize long-range charge transfer seen with the QEq charge equilibration scheme. In this equation, [\\(N\\)]{.math .notranslate .nohighlight} is the number of atoms in the system and [\\(S\_{ij}\\)]{.math .notranslate .nohighlight} is the overlap integral between atom [\\(i\\)]{.math .notranslate .nohighlight} and atom [\\(j\\)]{.math .notranslate .nohighlight}.

The effect of an external electric field can be incorporated into the QTPIE method by modifying the absolute or effective electronegativities of each atom [[(Chen)]{.std .std-ref}](#qtpie-chen){.reference .internal}. This fix models the effect of an external electric field by using the effective electronegativity [[(Lalli)]{.std .std-ref}](#lalli){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[\\tilde{\\chi}\_{\\mathrm{r}i} = \\frac{\\sum\_{j=1}\^{N} (\\chi_i - \\chi_j + \\beta(\\phi_i - \\phi_j)) S\_{ij}} {\\sum\_{m=1}\^{N}S\_{im}},\\\]
:::

where [\\(\\beta\\)]{.math .notranslate .nohighlight} is a scaling factor and [\\(\\phi_i\\)]{.math .notranslate .nohighlight} and [\\(\\phi_j\\)]{.math .notranslate .nohighlight} are the electric potentials at the positions of atoms [\\(i\\)]{.math .notranslate .nohighlight} and [\\(j\\)]{.math .notranslate .nohighlight} due to the external electric field. Additional details regarding the implementation and performance of this fix are provided in [[Lalli]{.std .std-ref}](#lalli){.reference .internal}.

This fix is typically used in conjunction with the ReaxFF force field model as implemented in the [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} command, but it can be used with any potential in LAMMPS, so long as it defines and uses charges on each atom. For more technical details about the charge equilibration performed by fix qtpie/reaxff, which is the same as in [[fix qeq/reaxff]{.doc}]fix_qeq_reaxff.md){.reference .internal} except for the use of [\\(\\tilde{\\chi}\_{i}\\)]{.math .notranslate .nohighlight} or [\\(\\tilde{\\chi}\_{\\mathrm{r}i}\\)]{.math .notranslate .nohighlight}, please refer to [[(Aktulga)]{.std .std-ref}](#qeq-aktulga2){.reference .internal}. To be explicit, this fix replaces [\\(\\chi_k\\)]{.math .notranslate .nohighlight} of eq. 3 in [[(Aktulga)]{.std .std-ref}](#qeq-aktulga2){.reference .internal} with [\\(\\tilde{\\chi}\_{k}\\)]{.math .notranslate .nohighlight} when no external electric field is applied and with [\\(\\tilde{\\chi}\_{\\mathrm{r}k}\\)]{.math .notranslate .nohighlight} when an external electric field is applied.

This fix requires the absolute electronegativity, [\\(\\chi\\)]{.math .notranslate .nohighlight}, in eV, the self-Coulomb potential, [\\(\\eta\\)]{.math .notranslate .nohighlight}, in eV, and the shielded Coulomb constant, [\\(\\gamma\\)]{.math .notranslate .nohighlight}, in [\\(\\AA\^{-1}\\)]{.math .notranslate .nohighlight}. If the *params* setting above is the word "reaxff", then these are extracted from the [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} command and the ReaxFF force field file it reads in. If a file name is specified for *params*, then the parameters are taken from the specified file and the file must contain one line for each atom type. The latter form must be used when performing QTPIE with a non-ReaxFF potential. Each line should be formatted as follows, ensuring that the parameters are given in units of eV, eV, and [\\(\\AA\^{-1}\\)]{.math .notranslate .nohighlight}, respectively:

:::: {.highlight-none .notranslate}
::: highlight
    itype chi eta gamma
:::
::::

where *itype* is the atom type from 1 to Ntypes. Note that eta is defined here as twice the eta value in the ReaxFF file.

The overlap integrals [\\(S\_{ij}\\)]{.math .notranslate .nohighlight} are computed by using normalized 1s Gaussian type orbitals. The Gaussian orbital exponents, [\\(\\alpha\\)]{.math .notranslate .nohighlight}, that are needed to compute the overlap integrals are taken from the file given by *gfile*. This file must contain one line for each atom type and provide the Gaussian orbital exponent for each atom type in units of inverse square Bohr radius. Each line should be formatted as follows:

:::: {.highlight-none .notranslate}
::: highlight
    itype alpha
:::
::::

Empty lines or any text following the pound sign (#) are ignored. An example *gfile* for a system with two atom types is

:::: {.highlight-none .notranslate}
::: highlight
    # An example gfile. Exponents are taken from Table 2.2 of Chen, J. (2009).
    # Theory and applications of fluctuating-charge models.
    # The units of the exponents are 1 / (Bohr radius)^2 .
    1  0.2240  # O
    2  0.5434  # H
:::
::::

The optional *scale* keyword sets the value of [\\(\\beta\\)]{.math .notranslate .nohighlight} in the equation for [\\(\\tilde{\\chi}\_{\\mathrm{r}i}\\)]{.math .notranslate .nohighlight}. This keyword only affects the computed charges when [[fix efield]{.doc}]fix_efield.md){.reference .internal} is used. The default value is 1.0.

The optional *maxiter* keyword allows changing the max number of iterations in the linear solver. The default value is 200.

The optional *nowarn* keyword silences the warning message printed when the maximum number of iterations is reached. This can be useful for comparing serial and parallel results where having the same fixed number of iterations is desired, which can be achieved by using a very small tolerance and setting *maxiter* to the desired number of iterations.

::: {.admonition .note}
Note

In order to solve the self-consistent equations for electronegativity equalization, LAMMPS imposes the additional constraint that all the charges in the fix group must add up to zero. The initial charge assignments should also satisfy this constraint. LAMMPS will print a warning if that is not the case.
:::
:::::::::::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. This fix computes a global scalar (the number of iterations) and a per-atom vector (the effective electronegativity), which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

This fix is invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the REAXFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This fix does not correctly handle interactions involving multiple periodic images of the same atom. Hence, it should not be used for periodic cell dimensions smaller than the non-bonded cutoff radius, which is typically [\\(10\~\\AA\\)]{.math .notranslate .nohighlight} for ReaxFF simulations.

This fix may be used in combination with [[fix efield]{.doc}]fix_efield.md){.reference .internal} and will apply the external electric field during charge equilibration, but there may be only one fix efield instance used and the electric field must be applied to all atoms in the system. Consequently, fix efield must be used with *group-ID* all and must not be used with the keyword *region*. Equal-style variables can be used for electric field vector components without any further settings. Atom-style variables can be used for spatially-varying electric field vector components, but the resulting electric potential must be specified as an atom-style variable using the *potential* keyword for fix efield.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal}, [[fix qeq/reaxff]{.doc}]fix_qeq_reaxff.md){.reference .internal}, [[fix acks2/reaxff]{.doc}]fix_acks2_reaxff.md){.reference .internal}, [[fix qeq/rel/reaxff]{.doc}]fix_qeq_rel_reaxff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

scale = 1.0 and maxiter = 200

------------------------------------------------------------------------

**(Rappe)** Rappe and Goddard III, Journal of Physical Chemistry, 95, 3358-3363 (1991).

**(Chen)** Chen, Jiahao. Theory and applications of fluctuating-charge models. University of Illinois at Urbana-Champaign, 2009.

**(Lalli)** Lalli and Giusti, Journal of Chemical Physics, 162, 174311 (2025).

**(Aktulga)** Aktulga, Fogarty, Pandit, Grama, Parallel Computing, 38, 245-259 (2012).
:::
::::::::::::::::::::::::
:::::::::::::::::::::::::
::::::::::::::::::::::::::

::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#fix-qeq-point-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# fix qeq/point command[](#fix-qeq-point-command "Link to this heading"){.headerlink}
:::

::: {#fix-qeq-shielded-command .section}
# fix qeq/shielded command[](#fix-qeq-shielded-command "Link to this heading"){.headerlink}
:::

::: {#fix-qeq-slater-command .section}
# fix qeq/slater command[](#fix-qeq-slater-command "Link to this heading"){.headerlink}
:::

::: {#fix-qeq-ctip-command .section}
# fix qeq/ctip command[](#fix-qeq-ctip-command "Link to this heading"){.headerlink}
:::

::: {#fix-qeq-dynamic-command .section}
# fix qeq/dynamic command[](#fix-qeq-dynamic-command "Link to this heading"){.headerlink}
:::

:::::::::::::::::::::::: {#fix-qeq-fire-command .section}
# fix qeq/fire command[](#fix-qeq-fire-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID style Nevery cutoff tolerance maxiter qfile keyword ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- style = *qeq/point* or *qeq/shielded* or *qeq/slater* or *qeq/ctip* or *qeq/dynamic* or *qeq/fire*

- Nevery = perform charge equilibration every this many steps

- cutoff = global cutoff for charge-charge interactions (distance unit)

- tolerance = precision to which charges will be equilibrated

- maxiter = maximum iterations to perform charge equilibration

- qfile = a filename with QEq parameters or *coul/streitz* or *coul/ctip* or *reaxff*

- zero or more keyword/value pairs may be appended

- keyword = *alpha* or *cdamp* or *maxrepeat* or *qdamp* or *qstep* or *warn*

  ``` literal-block
  alpha value = Slater type orbital exponent (qeq/slater only). Can be followed by optional arguments:
    wolf value = width of taper to terminate Coulomb integrals for the Wolf summation (default value is zero)
    dsf value = width of taper to terminate Coulomb integrals for the Fennell-Gezelter summation (default value is zero)
  cdamp value = damping parameter for Coulomb interactions (qeq/ctip only)
  maxrepeat value = number of equilibration cycles allowed to ensure no atoms cross charge bounds (qeq/ctip only)
  qdamp value = damping factor for damped dynamics charge solver (qeq/dynamic and qeq/fire only)
  qstep value = time step size for damped dynamics charge solver (qeq/dynamic and qeq/fire only)
  warn value = do (=yes) or do not (=no) print a warning when the maximum number of iterations is reached
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all qeq/point 1 10 1.0e-6 200 param.qeq1
    fix 1 qeq qeq/shielded 1 8 1.0e-6 100 param.qeq2
    fix 1 all qeq/slater 5 10 1.0e-6 100 params alpha 0.2
    fix 1 all qeq/slater 5 10 1.0e-6 100 params alpha 0.2 wolf
    fix 1 all qeq/slater 5 10 1.0e-6 100 params alpha 0.2 wolf 2.0
    fix 1 all qeq/slater 5 10 1.0e-6 100 params alpha 0.2 dsf
    fix 1 all qeq/slater 5 10 1.0e-6 100 params alpha 0.2 dsf 2.0
    fix 1 all qeq/ctip 1 12 1.0e-8 100 coul/ctip cdamp 0.30 maxrepeat 10
    fix 1 qeq qeq/dynamic 1 12 1.0e-3 100 my_qeq
    fix 1 all qeq/fire 1 10 1.0e-3 100 my_qeq qdamp 0.2 qstep 0.1
:::
::::
:::::

::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform the charge equilibration (QEq) method as described in [[(Rappe and Goddard)]{.std .std-ref}](#rappe1){.reference .internal} and formulated in [[(Nakano)]{.std .std-ref}](#nakano1){.reference .internal} (also known as the matrix inversion method) and in [[(Rick and Stuart)]{.std .std-ref}](#rick1){.reference .internal} (also known as the extended Lagrangian method) based on the electronegativity equilization principle.

These fixes can be used with any [[pair style]{.doc}]pair_style.md){.reference .internal} in LAMMPS, so long as per-atom charges are defined. The most typical use-case is in conjunction with a [[pair style]{.doc}]pair_style.md){.reference .internal} that performs charge equilibration periodically (e.g. every timestep), such as the ReaxFF or Streitz-Mintmire potential. But these fixes can also be used with potentials that normally assume per-atom charges are fixed, e.g. a [[Buckingham]{.doc}]pair_buck.md){.reference .internal} or [[LJ/Coulombic]{.doc}]pair_lj.md){.reference .internal} potential.

Because the charge equilibration calculation is effectively independent of the pair style, these fixes can also be used to perform a one-time assignment of charges to atoms. For example, you could define the QEq fix, perform a zero-timestep run via the [[run]{.doc}]run.md){.reference .internal} command without any pair style defined which would set per-atom charges (based on the current atom configuration), then remove the fix via the [[unfix]{.doc}]unfix.md){.reference .internal} command before performing further dynamics.

::: {.admonition .note}
Note

Computing and using charge values different from published values defined for a fixed-charge potential like Buckingham or CHARMM or AMBER, can have a strong effect on energies and forces, and produces a different model than the published versions.
:::

::: {.admonition .note}
Note

The [[fix qeq/comb]{.doc}]fix_qeq_comb.md){.reference .internal} command must still be used to perform charge equilibration with the [[COMB potential]{.doc}]pair_comb.md){.reference .internal}. The [[fix qeq/reaxff]{.doc}]fix_qeq_reaxff.md){.reference .internal} command can be used to perform charge equilibration with the [[ReaxFF force field]{.doc}]pair_reaxff.md){.reference .internal}, although fix qeq/shielded yields the same results as fix qeq/reaxff if *Nevery*, *cutoff*, and *tolerance* are the same. Eventually the fix qeq/reaxff command will be deprecated.
:::

The QEq method minimizes the electrostatic energy of the system (or equalizes the derivative of energy with respect to charge of all the atoms) by adjusting the partial charge on individual atoms based on interactions with their neighbors within *cutoff*. It requires a few parameters in the appropriate units for each atom type which are read from a file specified by *qfile*. The file has the following format:

:::: {.highlight-none .notranslate}
::: highlight
    1 chi eta gamma zeta qcore
    2 chi eta gamma zeta qcore
    ...
    Ntype chi eta gamma zeta qcore
:::
::::

except for fix style *qeq/ctip* where the format is:

:::: {.highlight-none .notranslate}
::: highlight
    1 chi eta gamma zeta qcore qmin qmax omega
    2 chi eta gamma zeta qcore qmin qmax omega
    ...
    Ntype chi eta gamma zeta qcore qmin qmax omega
:::
::::

There have to be parameters given for every atom type. Wildcard entries are possible using the same type range syntax as for "coeff" commands (i.e., n\*m, n\*, \*m, \*). Later entries will overwrite previous ones. Empty lines or any text following the pound sign (#) are ignored. Each line starts with the atom type followed by eight parameters. Only a subset of the parameters is used by each QEq style as described below, thus the others can be set to 0.0 if desired, but all eight entries per line are required.

- *chi* = electronegativity in energy units

- *eta* = self-Coulomb potential in energy units

- *gamma* = shielded Coulomb constant defined by [[ReaxFF force field]{.std .std-ref}](#vanduin){.reference .internal} in distance units

- *zeta* = Slater type orbital exponent defined by the [[Streitz-Mintmire]{.std .std-ref}](#streitz1){.reference .internal} potential in reverse distance units

- *qcore* = charge of the nucleus defined by the [[Streitz-Mintmire potential]{.std .std-ref}](#streitz1){.reference .internal} potential in charge units

- *qmin* = lower bound on the allowed charge defined by the [[CTIP]{.std .std-ref}](#ctip1){.reference .internal} potential in charge units

- *qmax* = upper bound on the allowed charge defined by the [[CTIP]{.std .std-ref}](#ctip1){.reference .internal} potential in charge units

- *omega* = penalty parameter used to enforce charge bounds defined by the [[CTIP]{.std .std-ref}](#ctip1){.reference .internal} potential in energy units

The fix qeq styles will print a warning if the charges are not equilibrated within *tolerance* by *maxiter* steps, unless the *warn* keyword is used with "no" as argument. This latter option may be useful for testing and benchmarking purposes, as it allows to use a fixed number of QEq iterations when *tolerance* is set to a small enough value to always reach the *maxiter* limit. Turning off warnings will avoid the excessive output in that case.

The *qeq/point* style describes partial charges on atoms as point charges. Interaction between a pair of charged particles is 1/r, which is the simplest description of the interaction between charges. Only the *chi* and *eta* parameters from the *qfile* file are used. Note that Coulomb catastrophe can occur if repulsion between the pair of charged particles is too weak. This style solves partial charges on atoms via the matrix inversion method. A tolerance of 1.0e-6 is usually a good number.

The *qeq/shielded* style describes partial charges on atoms also as point charges, but uses a shielded Coulomb potential to describe the interaction between a pair of charged particles. Interaction through the shielded Coulomb is given by equation (13) of the [[ReaxFF force field]{.std .std-ref}](#vanduin){.reference .internal} paper. The shielding accounts for charge overlap between charged particles at small separation. This style is the same as [[fix qeq/reaxff]{.doc}]fix_qeq_reaxff.md){.reference .internal}, and can be used with [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal}. Only the *chi*, *eta*, and *gamma* parameters from the *qfile* file are used. When using the string *reaxff* as filename, these parameters are extracted directly from an active *reaxff* pair style. This style solves partial charges on atoms via the matrix inversion method. A tolerance of 1.0e-6 is usually a good number.

The *qeq/slater* style describes partial charges on atoms as spherical charge densities centered around atoms via the Slater 1*s* orbital, so that the interaction between a pair of charged particles is the product of two Slater 1*s* orbitals. The expression for the Slater 1*s* orbital is given under equation (6) of the [[Streitz-Mintmire]{.std .std-ref}](#streitz1){.reference .internal} paper. Only the *chi*, *eta*, *zeta*, and *qcore* parameters from the *qfile* file are used. When using the string *coul/streitz* as filename, these parameters are extracted directly from an active *coul/streitz* pair style. This style solves partial charges on atoms via the matrix inversion method. A tolerance of 1.0e-6 is usually a good number. Keyword *alpha* can be used to change the Slater type orbital exponent.

::: versionadded
[Added in version 19Nov2024.]{.versionmodified .added}
:::

The *qeq/ctip* style describes partial charges on atoms in the same way as style *qeq/shielded* but also enables the definition of charge bounds. Only the *chi*, *eta*, *gamma*, *qmin*, *qmax*, and *omega* parameters from the *qfile* file are used. When using the string *coul/ctip* as filename, these parameters are extracted directly from an active *coul/ctip* pair style. This style solves partial charges on atoms via the matrix inversion method. Keyword *cdamp* can be used to change the damping parameter used to calculate Coulomb interactions. Keyword *maxrepeat* can be used to adjust the number of equilibration cycles allowed to ensure no atoms have crossed the charge bounds. A value of 10 is usually a good choice. A tolerance between 1.0e-6 and 1.0e-8 is usually a good choice but should be checked in conjunction with the timestep for adequate energy conservation during dynamic runs.

The *qeq/dynamic* style describes partial charges on atoms as point charges that interact through 1/r, but the extended Lagrangian method is used to solve partial charges on atoms. Only the *chi* and *eta* parameters from the *qfile* file are used. Note that Coulomb catastrophe can occur if repulsion between the pair of charged particles is too weak. A tolerance of 1.0e-3 is usually a good number. Keyword *qdamp* can be used to change the damping factor, while keyword *qstep* can be used to change the time step size.

The [[\*qeq/fire\*]{.std .std-ref}](#shan){.reference .internal} style describes the same charge model and charge solver as the *qeq/dynamic* style, but employs a FIRE minimization algorithm to solve for equilibrium charges. Keyword *qdamp* can be used to change the damping factor, while keyword *qstep* can be used to change the time step size.

Note that *qeq/point*, *qeq/shielded*, *qeq/slater*, and *qeq/ctip* describe different charge models, whereas the matrix inversion method and the extended Lagrangian method (*qeq/dynamic* and *qeq/fire*) are different solvers.

Note that *qeq/point*, *qeq/dynamic* and *qeq/fire* styles all describe charges as point charges that interact through 1/r relationship, but solve partial charges on atoms using different solvers. These three styles should yield comparable results if the QEq parameters and *Nevery*, *cutoff*, and *tolerance* are the same. Style *qeq/point* is typically faster, *qeq/dynamic* scales better on larger sizes, and *qeq/fire* is faster than *qeq/dynamic*.

::: {.admonition .note}
Note

In order to solve the self-consistent equations for electronegativity equalization, LAMMPS imposes the additional constraint that all the charges in the fix group must add up to zero. The initial charge assignments should also satisfy this constraint. LAMMPS will print a warning if that is not the case.
:::

::: {.admonition .note}
Note

Developing QEq parameters (chi, eta, gamma, zeta, and qcore) is non-trivial. Charges on atoms are not guaranteed to equilibrate with arbitrary choices of these parameters. We do not develop these QEq parameters. See the examples/qeq directory for some examples.
:::

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

In previous versions of LAMMPS, the real-space summations of Coulomb interactions were done by replacing *1/r* using a damped potential *erfc(alpha\*r)/r* with the parameter *alpha* controlling the rate of decay. However, any finite value of *alpha* leads to a jump at the cutoff, which interferes with equilibration if atoms move across the cutoff. The charge-neutralized potential of [[(Wolf et al.)]{.std .std-ref}](#wolf5){.reference .internal} (*wolf*) and its extension by [[(Fennell and Gezelter)]{.std .std-ref}](#fennell3){.reference .internal} (*dsf*) solve this problem. An extension was implemented to specify the width of taper (see [[(Mei et al.)]{.std .std-ref}](#mei2){.reference .internal}) to smoothly terminate the Coulomb integrals at the cutoff. This is done by specifying the optional arguments *wolf* and *dsf* with the value representing the width of taper that smoothly terminates the Coulomb integrals. For example, if the cutoff is 8 A and the taper width is 2 A, the Coulomb integrals are smoothly rescaled from their actual value at r=6 A to zero at r=8 A. For backward compatibility, the default taper width is zero.
:::::::::::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about these fixes is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. No global scalar or vector or per-atom quantities are stored by these fixes for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of these fixes can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

Thexe fixes are invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These fixes are part of the QEQ package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

These qeq fixes will ignore electric field contributions from [[fix efield]{.doc}]fix_efield.md){.reference .internal}.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix qeq/reaxff]{.doc}]fix_qeq_reaxff.md){.reference .internal}, [[fix qeq/comb]{.doc}]fix_qeq_comb.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

warn yes

------------------------------------------------------------------------

**(Rappe and Goddard)** A. K. Rappe and W. A. Goddard III, J Physical Chemistry, 95, 3358-3363 (1991).

**(Nakano)** A. Nakano, Computer Physics Communications, 104, 59-69 (1997).

**(Rick and Stuart)** S. W. Rick, S. J. Stuart, B. J. Berne, J Chemical Physics 101, 16141 (1994).

**(Streitz-Mintmire)** F. H. Streitz, J. W. Mintmire, Physical Review B, 50, 16, 11996 (1994)

**(CTIP)** G. Plummer, J. P. Tavenner, M. I. Mendelev, Z. Wu, J. W. Lawson, J Chemical Physics, 162, 054709 (2025)

**(ReaxFF)** A. C. T. van Duin, S. Dasgupta, F. Lorant, W. A. Goddard III, J Physical Chemistry, 105, 9396-9049 (2001)

**(QEq/Fire)** T.-R. Shan, A. P. Thompson, S. J. Plimpton, in preparation

**(Wolf)** D. Wolf, P. Keblinski, S. R. Phillpot, J. Eggebrecht, J. Chem. Phys. 110, 8254 (1999).

**(Fennell)** J. Fennell, J. D. Gezelter, J. Chem. Phys. 124, 234104 (2006).

**(Mei)** J. Mei, J. W. Davenport, G. W. Fernando, Phys. Rev. B 43, 4653 (1991).
:::
::::::::::::::::::::::::
::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::

::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#fix-qeq-reaxff-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# fix qeq/reaxff command[](#fix-qeq-reaxff-command "Link to this heading"){.headerlink}

Accelerator Variants: *qeq/reaxff/kk*, *qeq/reaxff/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID qeq/reaxff Nevery cutlo cuthi tolerance params args
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- qeq/reaxff = style name of this fix command

- Nevery = perform QEq every this many steps

- cutlo,cuthi = lo and hi cutoff for Taper radius

- tolerance = precision to which charges will be equilibrated

- params = reaxff or a filename

- one or more keywords or keyword/value pairs may be appended

  ``` literal-block
  keyword = dual or maxiter or nowarn or matfree
    dual = process S and T matrix in parallel (only for qeq/reaxff/omp)
    maxiter N = limit the number of iterations to N
    nowarn = do not print a warning message if the maximum number of iterations was reached
    matfree = use a matrix-free approach for applying the H matrix (only for qeq/reaxff/kk)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all qeq/reaxff 1 0.0 10.0 1.0e-6 reaxff
    fix 1 all qeq/reaxff 1 0.0 10.0 1.0e-6 param.qeq maxiter 500
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform the charge equilibration (QEq) method as described in [[(Rappe and Goddard)]{.std .std-ref}](#rappe2){.reference .internal} and formulated in [[(Nakano)]{.std .std-ref}](#nakano2){.reference .internal}. It is typically used in conjunction with the ReaxFF force field model as implemented in the [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} command, but it can be used with any potential in LAMMPS, so long as it defines and uses charges on each atom. The [[fix qeq/comb]{.doc}]fix_qeq_comb.md){.reference .internal} command should be used to perform charge equilibration with the [[COMB potential]{.doc}]pair_comb.md){.reference .internal}. For more technical details about the charge equilibration performed by fix qeq/reaxff, see the [[(Aktulga)]{.std .std-ref}](#qeq-aktulga){.reference .internal} paper.

The QEq method minimizes the electrostatic energy of the system by adjusting the partial charge on individual atoms based on interactions with their neighbors. It requires some parameters for each atom type. If the *params* setting above is the word "reaxff", then these are extracted from the [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} command and the ReaxFF force field file it reads in. If a file name is specified for *params*, then the parameters are taken from the specified file and the file must contain one line for each atom type. The latter form must be used when performing QEq with a non-ReaxFF potential. Each line should be formatted as follows:

:::: {.highlight-none .notranslate}
::: highlight
    itype chi eta gamma
:::
::::

where *itype* is the atom type from 1 to Ntypes, *chi* denotes the electronegativity in eV, *eta* denotes the self-Coulomb potential in eV, and *gamma* denotes the valence orbital exponent. Note that these 3 quantities are also in the ReaxFF potential file, except that eta is defined here as twice the eta value in the ReaxFF file. Note that unlike the rest of LAMMPS, the units of this fix are hard-coded to be A, eV, and electronic charge.

The optional *dual* keyword allows to perform the optimization of the S and T matrices in parallel. This is only supported for the *qeq/reaxff/omp* style. Otherwise they are processed separately. The *qeq/reaxff/kk* style always solves the S and T matrices in parallel.

The optional *maxiter* keyword allows changing the max number of iterations in the linear solver. The default value is 200.

The optional *nowarn* keyword silences the warning message printed when the maximum number of iterations was reached. This can be useful for comparing serial and parallel results where having the same fixed number of QEq iterations is desired, which can be achieved by using a very small tolerance and setting *maxiter* to the desired number of iterations.

The optional *matfree* keyword replaces the sequence of explicitly constructing the H matrix, then (repeatedly) applying it with a matrix-free approach where the H matrix is effectively regenerated each time it is applied. This trades performance for reduced memory requirements because it avoids the overheads of storing the matrix. This is only supported for the *qeq/reaxff/kk* style, with both full and half qeq neighbor lists supported.

::: {.admonition .note}
Note

In order to solve the self-consistent equations for electronegativity equalization, LAMMPS imposes the additional constraint that all the charges in the fix group must add up to zero. The initial charge assignments should also satisfy this constraint. LAMMPS will print a warning if that is not the case.
:::
::::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. This fix computes a global scalar (the number of iterations) for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

This fix is invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the REAXFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This fix does not correctly handle interactions involving multiple periodic images of the same atom. Hence, it should not be used for periodic cell dimensions smaller than the non-bonded cutoff radius, which is typically [\\(10\~\\AA\\)]{.math .notranslate .nohighlight} for ReaxFF simulations.

This fix may be used in combination with [[fix efield]{.doc}]fix_efield.md){.reference .internal} and will apply the external electric field during charge equilibration, but there may be only one fix efield instance used and the electric field vector may only have components in non-periodic directions. Equal-style variables can be used for electric field vector components without any further settings. Atom-style variables can be used for spatially-varying electric field vector components, but the resulting electric potential must be specified as an atom-style variable using the *potential* keyword for fix efield.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal}, [[fix qeq/shielded]{.doc}]fix_qeq.md){.reference .internal}, [[fix acks2/reaxff]{.doc}]fix_acks2_reaxff.md){.reference .internal}, [[fix qtpie/reaxff]{.doc}]fix_qtpie_reaxff.md){.reference .internal}, [[fix qeq/rel/reaxff]{.doc}]fix_qeq_rel_reaxff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

maxiter 200

------------------------------------------------------------------------

**(Rappe)** Rappe and Goddard III, Journal of Physical Chemistry, 95, 3358-3363 (1991).

**(Nakano)** Nakano, Computer Physics Communications, 104, 59-69 (1997).

**(Aktulga)** Aktulga, Fogarty, Pandit, Grama, Parallel Computing, 38, 245-259 (2012).
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

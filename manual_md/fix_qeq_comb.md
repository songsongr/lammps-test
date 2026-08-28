::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-qeq-comb-command .section}
[]{#index-1}[]{#index-0}

# fix qeq/comb command[](#fix-qeq-comb-command "Link to this heading"){.headerlink}

Accelerator Variants: *qeq/comb/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID qeq/comb Nevery precision keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- qeq/comb = style name of this fix command

- Nevery = perform charge equilibration every this many steps

- precision = convergence criterion for charge equilibration

- zero or more keyword/value pairs may be appended

- keyword = *file*

  ``` literal-block
  file value = filename
    filename = name of file to write QEQ equilibration info to
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 surface qeq/comb 10 0.0001
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform charge equilibration (QeQ) in conjunction with the COMB (Charge-Optimized Many-Body) potential as described in [[(COMB_1)]{.std .std-ref}](#comb-1){.reference .internal} and [[(COMB_2)]{.std .std-ref}](#comb-2){.reference .internal}. It performs the charge equilibration portion of the calculation using the so-called QEq method, whereby the charge on each atom is adjusted to minimize the energy of the system. This fix can only be used with the COMB potential; see the [[fix qeq/reaxff]{.doc}]fix_qeq_reaxff.md){.reference .internal} command for a QeQ calculation that can be used with any potential.

Only charges on the atoms in the specified group are equilibrated. The fix relies on the pair style (COMB in this case) to calculate the per-atom electronegativity (effective force on the charges). An electronegativity equalization calculation (or QEq) is performed in an iterative fashion, which in parallel requires communication at each iteration for processors to exchange charge information about nearby atoms with each other. See [[Rappe_and_Goddard]{.std .std-ref}](#rappe-and-goddard){.reference .internal} and [[Rick_and_Stuart]{.std .std-ref}](#rick-and-stuart){.reference .internal} for details.

During a run, charge equilibration is performed every *Nevery* time steps. Charge equilibration is also always enforced on the first step of each run. The *precision* argument controls the tolerance for the difference in electronegativity for all atoms during charge equilibration. *Precision* is a trade-off between the cost of performing charge equilibration (more iterations) and accuracy.

If the *file* keyword is used, then information about each equilibration calculation is written to the specified file.

::: {.admonition .note}
Note

In order to solve the self-consistent equations for electronegativity equalization, LAMMPS imposes the additional constraint that all the charges in the fix group must add up to zero. The initial charge assignments should also satisfy this constraint. LAMMPS will print a warning if that is not the case.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is performing charge equilibration. Default is the outermost level.

This fix produces a per-atom vector which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The vector stores the gradient of the charge on each atom. The per-atom values be accessed on any timestep.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

This fix can be invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix command currently only supports [[pair style \*comb\*]{.doc}]pair_comb.md){.reference .internal}.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style comb]{.doc}]pair_comb.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

No file output is performed.

------------------------------------------------------------------------

**(COMB_1)** J. Yu, S. B. Sinnott, S. R. Phillpot, Phys Rev B, 75, 085311 (2007),

**(COMB_2)** T.-R. Shan, B. D. Devine, T. W. Kemper, S. B. Sinnott, S. R. Phillpot, Phys Rev B, 81, 125328 (2010).

**(Rappe_and_Goddard)** A. K. Rappe, W. A. Goddard, J Phys Chem 95, 3358 (1991).

**(Rick_and_Stuart)** S. W. Rick, S. J. Stuart, B. J. Berne, J Chem Phys 101, 16141 (1994).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

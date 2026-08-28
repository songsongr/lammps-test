::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#fix-acks2-reaxff-command .section}
[]{#index-1}[]{#index-0}

# fix acks2/reaxff command[](#fix-acks2-reaxff-command "Link to this heading"){.headerlink}

Accelerator Variants: *acks2/reaxff/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID acks2/reaxff Nevery cutlo cuthi tolerance params args
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- acks2/reaxff = style name of this fix command

- Nevery = perform ACKS2 every this many steps

- cutlo,cuthi = lo and hi cutoff for Taper radius

- tolerance = precision to which charges will be equilibrated

- params = reaxff or a filename

- one or more keywords or keyword/value pairs may be appended

  ``` literal-block
  keyword = maxiter
    maxiter N = limit the number of iterations to N
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all acks2/reaxff 1 0.0 10.0 1.0e-6 reaxff
    fix 1 all acks2/reaxff 1 0.0 10.0 1.0e-6 param.acks2 maxiter 500
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform the atom-condensed Kohn--Sham DFT to second order (ACKS2) charge equilibration method as described in [[(Verstraelen)]{.std .std-ref}](#verstraelen){.reference .internal}. ACKS2 impedes unphysical long-range charge transfer sometimes seen with QEq (e.g., for dissociation of molecules), at increased computational cost. It is typically used in conjunction with the ReaxFF force field model as implemented in the [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} command, but it can be used with any potential in LAMMPS, so long as it defines and uses charges on each atom. For more technical details about the charge equilibration performed by fix acks2/reaxff, see the [[(O'Hearn)]{.std .std-ref}](#o-hearn){.reference .internal} paper.

The ACKS2 method minimizes the electrostatic energy of the system by adjusting the partial charge on individual atoms based on interactions with their neighbors. It requires some parameters for each atom type. If the *params* setting above is the word "reaxff", then these are extracted from the [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} command and the ReaxFF force field file it reads in. If a file name is specified for *params*, then the parameters are taken from the specified file and the file must contain one line for each atom type. The latter form must be used when performing QeQ with a non-ReaxFF potential. The lines should be formatted as follows:

:::: {.highlight-none .notranslate}
::: highlight
    bond_softness
    itype chi eta gamma bcut
:::
::::

where the first line is the global parameter *bond_softness*. The remaining 1 to Ntypes lines include *itype*, the atom type from 1 to Ntypes, *chi*, the electronegativity in eV, *eta*, the self-Coulomb potential in eV, *gamma*, the valence orbital exponent, and *bcut*, the bond cutoff distance. Note that these 4 quantities are also in the ReaxFF potential file, except that eta is defined here as twice the eta value in the ReaxFF file. Note that unlike the rest of LAMMPS, the units of this fix are hard-coded to be [\\(\\AA\\)]{.math .notranslate .nohighlight}, eV, and electronic charge.

The optional *maxiter* keyword allows changing the max number of iterations in the linear solver. The default value is 200.

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

This fix may be used in combination with [[fix efield]{.doc}]fix_efield.md){.reference .internal} and will apply the external electric field during charge equilibration, but there may be only one fix efield instance used, it may only use a constant electric field, and the electric field vector may only have components in non-periodic directions.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal}, [[fix qeq/reaxff]{.doc}]fix_qeq_reaxff.md){.reference .internal}, [[fix qtpie/reaxff]{.doc}]fix_qtpie_reaxff.md){.reference .internal}, [[fix qeq/rel/reaxff]{.doc}]fix_qeq_rel_reaxff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

maxiter 200

------------------------------------------------------------------------

**(O'Hearn)** O'Hearn, Alperen, Aktulga, SIAM J. Sci. Comput., 42(1), C1--C22 (2020).

**(Verstraelen)** Verstraelen, Ayers, Speybroeck, Waroquier, J. Chem. Phys. 138, 074108 (2013).
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

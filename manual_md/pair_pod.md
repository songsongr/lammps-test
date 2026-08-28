::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#pair-style-pod-command .section}
[]{#index-1}[]{#index-0}

# pair_style pod command[](#pair-style-pod-command "Link to this heading"){.headerlink}

Accelerator Variants: *pod/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style pod
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style pod
    pair_coeff * * Ta_param.pod Ta_coefficients.pod Ta
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 22Dec2022.]{.versionmodified .added}
:::

Pair style *pod* defines the proper orthogonal descriptor (POD) potential [[(Nguyen and Rohskopf)]{.std .std-ref}](#nguyen20222b){.reference .internal}, [[(Nguyen2023)]{.std .std-ref}](#nguyen20232b){.reference .internal}, [[(Nguyen2024)]{.std .std-ref}](#nguyen20242b){.reference .internal}, and [[(Nguyen and Sema)]{.std .std-ref}](#nguyen20243b){.reference .internal}. The [[fitpod]{.doc}]fitpod_command.md){.reference .internal} is used to fit the POD potential.

Only a single pair_coeff command is used with the *pod* style which specifies a POD parameter file followed by a coefficient file, a projection matrix file, and a centroid file.

The POD parameter file ([`Ta_param.pod`{.docutils .literal .notranslate}]{.pre}) can contain blank and comment lines (start with #) anywhere. Each non-blank non-comment line must contain one keyword/value pair. See [[fitpod]{.doc}]fitpod_command.md){.reference .internal} for the description of all the keywords that can be assigned in the parameter file.

The coefficient file ([`Ta_coefficients.pod`{.docutils .literal .notranslate}]{.pre}) contains coefficients for the POD potential. The top of the coefficient file can contain any number of blank and comment lines (start with #), but follows a strict format after that. The first non-blank non-comment line must contain:

- model_coefficients: *ncoeff* *nproj* *ncentroid*

This is followed by *ncoeff* coefficients, *nproj* projection matrix entries, and *ncentroid* centroid coordinates, one per line. The coefficient file is generated after training the POD potential using [[fitpod]{.doc}]fitpod_command.md){.reference .internal}.

As an example, if a LAMMPS indium phosphide simulation has 4 atoms types, with the first two being indium and the third and fourth being phophorous, the pair_coeff command would look like this:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * pod InP_param.pod InP_coefficients.pod In In P P
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The two filenames are for the parameter and coefficient files, respectively. The two trailing 'In' arguments map LAMMPS atom types 1 and 2 to the POD 'In' element. The two trailing 'P' arguments map LAMMPS atom types 3 and 4 to the POD 'P' element.

If a POD mapping value is specified as NULL, the mapping is not performed. This can be used when a *pod* potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials.

Examples about training and using POD potentials are found in the directory lammps/examples/PACKAGES/pod and the Github repo [https://github.com/cesmix-mit/pod-examples](https://github.com/cesmix-mit/pod-examples){.reference .external}.
::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, where types I and J correspond to two different element types, mixing is performed by LAMMPS with user-specifiable parameters as described above. You never need to specify a pair_coeff command with I != J arguments for this style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This style is part of the ML-POD package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fitpod]{.doc}]fitpod_command.md){.reference .internal}, [[compute pod/atom]{.doc}]compute_pod_atom.md){.reference .internal}, [[compute podd/atom]{.doc}]compute_pod_atom.md){.reference .internal}, [[compute pod/local]{.doc}]compute_pod_atom.md){.reference .internal}, [[compute pod/global]{.doc}]compute_pod_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Nguyen and Rohskopf)** Nguyen and Rohskopf, Journal of Computational Physics, 480, 112030, (2023).

**(Nguyen2023)** Nguyen, Physical Review B, 107(14), 144103, (2023).

**(Nguyen2024)** Nguyen, Journal of Computational Physics, 113102, (2024).

**(Nguyen and Sema)** Nguyen and Sema, [https://arxiv.org/abs/2405.00306](https://arxiv.org/abs/2405.00306){.reference .external}, (2024).
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#compute-pod-atom-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# compute pod/atom command[](#compute-pod-atom-command "Link to this heading"){.headerlink}
:::

::: {#compute-podd-atom-command .section}
# compute podd/atom command[](#compute-podd-atom-command "Link to this heading"){.headerlink}
:::

::: {#compute-pod-local-command .section}
# compute pod/local command[](#compute-pod-local-command "Link to this heading"){.headerlink}
:::

:::::::::::::::: {#compute-pod-global-command .section}
# compute pod/global command[](#compute-pod-global-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID pod/atom param.pod coefficients.pod
    compute ID group-ID podd/atom param.pod coefficients.pod
    compute ID group-ID pod/local param.pod coefficients.pod
    compute ID group-ID pod/global param.pod coefficients.pod
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- pod/atom = style name of this compute command

- param.pod = the parameter file specifies parameters of the POD descriptors

- coefficients.pod = the coefficient file specifies coefficients of the POD potential
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute d all pod/atom Ta_param.pod
    compute dd all podd/atom Ta_param.pod
    compute ldd all pod/local Ta_param.pod
    compute gdd all podd/global Ta_param.pod
    compute d all pod/atom Ta_param.pod Ta_coefficients.pod
    compute dd all podd/atom Ta_param.pod Ta_coefficients.pod
    compute ldd all pod/local Ta_param.pod Ta_coefficients.pod
    compute gdd all podd/global Ta_param.pod Ta_coefficients.pod
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 27June2024.]{.versionmodified .added}
:::

Define a computation that calculates a set of quantities related to the POD descriptors of the atoms in a group. These computes are used primarily for calculating the dependence of energy and force components on the linear coefficients in the [[pod pair_style]{.doc}]pair_pod.md){.reference .internal}, which is useful when training a POD potential to match target data. POD descriptors of an atom are characterized by the radial and angular distribution of neighbor atoms. The detailed mathematical definition is given in the papers by [[(Nguyen and Rohskopf)]{.std .std-ref}](#nguyen20222c){.reference .internal}, [[(Nguyen2023)]{.std .std-ref}](#nguyen20232c){.reference .internal}, [[(Nguyen2024)]{.std .std-ref}](#nguyen20242c){.reference .internal}, and [[(Nguyen and Sema)]{.std .std-ref}](#nguyen20243c){.reference .internal}.

Compute *pod/atom* calculates the per-atom POD descriptors.

Compute *podd/atom* calculates derivatives of the per-atom POD descriptors with respect to atom positions.

Compute *pod/local* calculates the per-atom POD descriptors and their derivatives with respect to atom positions.

Compute *pod/global* calculates the global POD descriptors and their derivatives with respect to atom positions.

Examples how to use Compute POD commands are found in the directory [`examples/PACKAGES/pod`{.docutils .literal .notranslate}]{.pre}.

::: {.admonition .warning}
Warning

All of these compute styles produce *very* large per-atom output arrays that scale with the total number of atoms in the system. This will result in *very* large memory consumption for systems with a large number of atoms.
:::
:::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

Compute *pod/atom* produces an 2D array of size [\\(N \\times M\\)]{.math .notranslate .nohighlight}, where [\\(N\\)]{.math .notranslate .nohighlight} is the number of atoms and [\\(M\\)]{.math .notranslate .nohighlight} is the number of descriptors. Each column corresponds to a particular POD descriptor.

Compute *podd/atom* produces an 2D array of size [\\(N \\times (M \* 3 N)\\)]{.math .notranslate .nohighlight}. Each column corresponds to a particular derivative of a POD descriptor.

Compute *pod/local* produces an 2D array of size [\\((1 + 3N) \\times (M \* N)\\)]{.math .notranslate .nohighlight}. The first row contains the per-atom descriptors, and the last 3N rows contain the derivatives of the per-atom descriptors with respect to atom positions.

Compute *pod/global* produces an 2D array of size [\\((1 + 3N) \\times (M)\\)]{.math .notranslate .nohighlight}. The first row contains the global descriptors, and the last 3N rows contain the derivatives of the global descriptors with respect to atom positions.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These computes are part of the ML-POD package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fitpod]{.doc}]fitpod_command.md){.reference .internal}, [[pair_style pod]{.doc}]pair_pod.md){.reference .internal}
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
::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

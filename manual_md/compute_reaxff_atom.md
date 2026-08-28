::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-reaxff-atom-command .section}
[]{#index-1}[]{#index-0}

# compute reaxff/atom command[](#compute-reaxff-atom-command "Link to this heading"){.headerlink}

Accelerator Variants: *reaxff/atom/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID reaxff/atom attribute args ... keyword value ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- reaxff/atom = name of this compute command

- attribute = *pair*

  ``` literal-block
  pair args = nsub
    nsub = n-instance of a sub-style, if a pair style is used multiple times in a hybrid style
  ```

- keyword = *bonds*

  ``` literal-block
  bonds value = no or yes
    no = ignore list of local bonds
    yes = include list of local bonds
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all reaxff/atom bonds yes
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 7Feb2024.]{.versionmodified .added}
:::

Define a computation that extracts bond information computed by the ReaxFF potential specified by [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal}.

By default, it produces per-atom data that includes the following columns:

- abo = atom bond order (sum of all bonds)

- nlp = number of lone pairs

- nb = number of bonds

Bonds will only be included if its atoms are in the group.

In addition, if [`bonds`{.docutils .literal .notranslate}]{.pre} is set to [`yes`{.docutils .literal .notranslate}]{.pre}, the compute will also produce a local array of all bonds on the current processor whose atoms are in the group. The columns of each entry of this local array are:

- id_i = atom i id of bond

- id_j = atom j id of bond

- bo = bond order of bond
::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom array and local array depending on the number of keywords. The number of rows in the local array is the number of bonds as described above. Both per-atom and local array have 3 columns.

The arrays can be accessed by any command that uses local and per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The compute reaxff/atom command requires that the [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} is invoked. This fix is part of the REAXFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *bonds* = *no*.
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

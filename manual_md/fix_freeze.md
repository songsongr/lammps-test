:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-freeze-command .section}
[]{#index-1}[]{#index-0}

# fix freeze command[](#fix-freeze-command "Link to this heading"){.headerlink}

Accelerator Variants: *freeze/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID freeze
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- freeze = style name of this fix command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 2 bottom freeze
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Zero out the force and torque on a granular particle. This is useful for preventing certain particles from moving in a simulation. The [[granular pair styles]{.doc}]pair_gran.md){.reference .internal} also detect if this fix has been defined and compute interactions between frozen and non-frozen particles appropriately, as if the frozen particle has infinite mass. A similar functionality for normal (point) particles can be obtained using [[fix setforce]{.doc}]fix_setforce.md){.reference .internal}.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix computes a global 3-vector of forces, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. This is the total force on the group of atoms before the forces on individual atoms are changed by the fix. The vector values calculated by this fix are "extensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the GRANULAR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

There can only be a single freeze fix defined. This is because other the [[granular pair styles]{.doc}]pair_gran.md){.reference .internal} treat frozen particles differently and need to be able to reference a single group to which this fix is applied.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[atom_style sphere]{.doc}]atom_style.md){.reference .internal}, [[fix setforce]{.doc}]fix_setforce.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#fix-momentum-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# fix momentum command[](#fix-momentum-command "Link to this heading"){.headerlink}

Accelerator Variants: *momentum/kk*
:::

:::::::::::::::: {#fix-momentum-chunk-command .section}
# fix momentum/chunk command[](#fix-momentum-chunk-command "Link to this heading"){.headerlink}

::::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID momentum N keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- momentum = style name of this fix command

- N = adjust the momentum every this many timesteps one or more keyword/value pairs may be appended

:::: {.highlight-none .notranslate}
::: highlight
    fix ID group-ID momentum/chunk N chunkID keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- momentum/chunk = style name of this fix command

- N = adjust the momentum per chunk every this many timesteps

- chunkID = ID of [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command

  one or more keyword/value settings may be appended to each of the fix commands:

- keyword = *linear* or *angular* or *rescale*

  ``` literal-block
  linear values = xflag yflag zflag
    xflag,yflag,zflag = 0/1 to exclude/include each dimension
  angular values = none
  rescale values = none
  ```
:::::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all momentum 1 linear 1 1 0
    fix 1 all momentum 1 linear 1 1 1 rescale
    fix 1 all momentum 100 linear 1 1 1 angular
    fix 1 all momentum/chunk 100 molchunk linear 1 1 1 angular
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Fix momentum zeroes the linear and/or angular momentum of the group of atoms every N timesteps by adjusting the velocities of the atoms. Fix momentum/chunk works equivalently, but operates on a per-chunk basis.

One (or both) of the *linear* or *angular* keywords **must** be specified.

If the *linear* keyword is used, the linear momentum is zeroed by subtracting the center-of-mass velocity of the group or chunk from each atom. This does not change the relative velocity of any pair of atoms. One or more dimensions can be excluded from this operation by setting the corresponding flag to 0.

If the *angular* keyword is used, the angular momentum is zeroed by subtracting a rotational component from each atom.

This command can be used to ensure the entire collection of atoms (or a subset of them) does not drift or rotate during the simulation due to random perturbations (e.g. [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} thermostatting).

The *rescale* keyword enables conserving the kinetic energy of the group or chunk of atoms by rescaling the velocities after the momentum was removed.

Note that the [[velocity]{.doc}]velocity.md){.reference .internal} command can be used to create initial velocities with zero aggregate linear and/or angular momentum.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Fix momentum/chunk is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix recenter]{.doc}]fix_recenter.md){.reference .internal}, [[velocity]{.doc}]velocity.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-reaxff-bonds-command .section}
[]{#index-1}[]{#index-0}

# fix reaxff/bonds command[](#fix-reaxff-bonds-command "Link to this heading"){.headerlink}

Accelerator Variants: *reaxff/bonds/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID reaxff/bonds Nevery filename
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- reaxff/bonds = style name of this fix command

- Nevery = output interval in timesteps

- filename = name of output file
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all reaxff/bonds 100 bonds.reaxff
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Write out the bond information computed by the ReaxFF potential specified by [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} in the exact same format as the original stand-alone ReaxFF code of Adri van Duin. The bond information is written to *filename* on timesteps that are multiples of *Nevery*, including timestep 0. For time-averaged chemical species analysis, please see the [[fix reaxff/species]{.doc}]fix_reaxff_species.md){.reference .internal} command.

The specified group-ID is ignored by this fix except for the [[dump image]{.doc}]dump_image.md){.reference .internal} related functionality (see below).

The format of the output file should be reasonably self-explanatory. The meaning of the column header abbreviations is as follows:

- id = atom id

- type = atom type

- nb = number of bonds

- id_1 = atom id of first bond

- id_nb = atom id of Nth bond

- mol = molecule id

- bo_1 = bond order of first bond

- bo_nb = bond order of Nth bond

- abo = atom bond order (sum of all bonds)

- nlp = number of lone pairs

- q = atomic charge

If the filename ends with ".gz" or some [[other supported compression format suffix]{.std .std-ref}]Build_settings.md#gzip){.reference .internal}, the output file is written in compressed format. A compressed output file can be significantly smaller than the text version, but will also take longer to write.

::: versionadded
[Added in version 2Apr2025.]{.versionmodified .added}
:::

If the filename contains the wildcard character "\*", a new file is created on every timestep where bond information is written. The "\*" character is replaced with the timestep value. Note that the [[fix_modify pad]{.doc}]fix_modify.md){.reference .internal} command can be used so that all timestep numbers have the same length by adding leading zeroes (e.g. 00010 for a pad value of 5). The default pad value is 0, i.e. no leading zeroes.

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

If the filename is "NULL", then no output is created. This can be useful when using fix *reaxff/bonds* in combination with [[dump image fix]{.doc}]dump_image.md){.reference .internal} keyword to visualize the bonds computed by the ReaxFF force field.
:::::

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

Fix *reaxff/bonds* supports the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix will pass geometry information about the bonds computed by the [[ReaxFF pair style]{.doc}]pair_reaxff.md){.reference .internal} to *dump image* so that they can be included in the rendered image. Only bonds where *both* atoms are within the fix group generate graphics objects that are displayed in the dumped images. That group may be a dynamic group.

The color of the bonds is by default that of the atoms when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

The *fflag1* setting of *dump image fix* determines whether the bonds will be capped with spheres (1) or not (0).

The *fflag2* setting allows to adjust diameter of the cylinders for the bonds. By default, a diameter of 0.5 length units will be used.
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. This fix supports the [[fix_modify pad]{.doc}]fix_modify.md){.reference .internal} option. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The fix reaxff/bonds command requires that the [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal} is invoked. This fix is part of the REAXFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

To write compressed bond files, you must compile LAMMPS with the [`-DLAMMPS_GZIP`{.docutils .literal .notranslate}]{.pre} option. See the [[Build settings]{.doc}]Build_settings.md){.reference .internal} doc page for details.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal}, [[fix reaxff/species]{.doc}]fix_reaxff_species.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

pad = 0
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

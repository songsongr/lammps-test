::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#write-dump-command .section}
[]{#index-0}

# write_dump command[](#write-dump-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    write_dump group-ID style file dump-args modify dump_modify-args
:::
::::

- group-ID = ID of the group of atoms to be dumped

- style = any of the supported [[dump styles]{.doc}]dump.md){.reference .internal}

- file = name of file to write dump info to

- dump-args = any additional args needed for a particular [[dump style]{.doc}]dump.md){.reference .internal}

- modify = all args after this keyword are passed to [[dump_modify]{.doc}]dump_modify.md){.reference .internal} (optional)

- dump-modify-args = args for [[dump_modify]{.doc}]dump_modify.md){.reference .internal} (optional)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    write_dump all atom dump.atom
    write_dump subgroup atom dump.run.bin
    write_dump all custom dump.myforce.* id type x y vx fx
    write_dump flow custom dump.%.myforce id type c_myF[3] v_ke modify sort id
    write_dump all xyz system.xyz modify sort id element O H
    write_dump all image snap*.jpg type type size 960 960 modify backcolor white
    write_dump all image snap*.jpg element element &
       bond atom 0.3 shiny 0.1 ssao yes 6345 0.2 size 1600 1600  &
       modify backcolor white element C C O H N C C C O H H S O H
    write_dump all atom/gz dump.atom.gz modify compression_level 9
    write_dump flow custom/zstd dump.%.myforce.zst &
                    id type c_myF[3] v_ke &
                    modify sort id &
                    compression_level 15
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Dump a single snapshot of atom quantities to one or more files for the current state of the system. This is a one-time immediate operation, in contrast to the [[dump]{.doc}]dump.md){.reference .internal} command which will will set up a dump style to write out snapshots periodically during a running simulation.

The syntax for this command is mostly identical to that of the [[dump]{.doc}]dump.md){.reference .internal} and [[dump_modify]{.doc}]dump_modify.md){.reference .internal} commands as if they were concatenated together, with the following exceptions: There is no need for a dump ID or dump frequency and the keyword *modify* is added. The latter is so that the full range of [[dump_modify]{.doc}]dump_modify.md){.reference .internal} options can be specified for the single snapshot, just as they can be for multiple snapshots. The *modify* keyword separates the arguments that would normally be passed to the *dump* command from those that would be given the *dump_modify*. Both support optional arguments and thus LAMMPS needs to be able to cleanly separate the two sets of args.

Note that if the specified filename uses wildcard characters "\*" or "%", as supported by the [[dump]{.doc}]dump.md){.reference .internal} command, they will operate in the same fashion to create the new filename(s). Normally, [[dump image]{.doc}]dump_image.md){.reference .internal} files require a filename with a "\*" character for the timestep. That is not the case for the write_dump command; no wildcard "\*" character is necessary.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

All restrictions for the [[dump]{.doc}]dump.md){.reference .internal} and [[dump_modify]{.doc}]dump_modify.md){.reference .internal} commands apply to this command as well, with the exception of the [[dump image]{.doc}]dump_image.md){.reference .internal} filename not requiring a wildcard "\*" character, as noted above.

Since dumps are normally written during a [[run]{.doc}]run.md){.reference .internal} or [[energy minimization]{.doc}]minimize.md){.reference .internal}, the simulation has to be ready to run before this command can be used. Similarly, if the dump requires information from a compute, fix, or variable, the information needs to have been calculated for the current timestep (e.g. by a prior run), else LAMMPS will generate an error message.

For example, it is not possible to dump per-atom energy with this command before a run has been performed, since no energies and forces have yet been calculated. See the [[variable]{.doc}]variable.md){.reference .internal} doc page section on Variable Accuracy for more information on this topic.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dump]{.doc}]dump.md){.reference .internal}, [[dump image]{.doc}]dump_image.md){.reference .internal}, [[dump_modify]{.doc}]dump_modify.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The defaults are listed on the doc pages for the [[dump]{.doc}]dump.md){.reference .internal} and [[dump image]{.doc}]dump_image.md){.reference .internal} and [[dump_modify]{.doc}]dump_modify.md){.reference .internal} commands.
:::
:::::::::::::
::::::::::::::
:::::::::::::::

::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#partition-command .section}
[]{#index-0}

# partition command[](#partition-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    partition style N command ...
:::
::::

- style = *yes* or *no*

- N = partition number (see asterisk form below)

- command = any LAMMPS command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    partition yes 1 processors 4 10 6
    partition no 5 print "Active partition"
    partition yes *5 fix all nve
    partition yes 6* fix all nvt temp 1.0 1.0 0.1
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This command invokes the specified command on a subset of the partitions of MPI processes you have defined via the [[-partition command-line switch]{.doc}]Run_options.md){.reference .internal}.

Normally, every input script command in your script is invoked by every partition. This behavior can be modified by defining world- or universe-style [[variables]{.doc}]variable.md){.reference .internal} that have different values for each partition. This mechanism can be used to cause your script to jump to different input script files on different partitions, if such a variable is used in a [[jump]{.doc}]jump.md){.reference .internal} command.

The "partition" command is another mechanism for having as input script operate differently on different partitions. It is basically a prefix on any LAMMPS command. The command will only be invoked on the partition(s) specified by the *style* and *N* arguments.

If the *style* is *yes*, the command will be invoked on any partition which matches the *N* argument. If the *style* is *no* the command will be invoked on all the partitions which do not match the *Np* argument.

Partitions are numbered from 1 to *Np*, where *Np* is the number of partitions specified by the [[-partition command-line switch]{.doc}]Run_options.md){.reference .internal}.

*N* can be specified in one of two ways. An explicit numeric value can be used, as in the first example above. Or a wild-card asterisk can be used to span a range of partition numbers. This takes the form "\*" or "\*n" or "n\*" or "m\*n". An asterisk with no numeric values means all partitions from 1 to *Np*. A leading asterisk means all partitions from 1 to n (inclusive). A trailing asterisk means all partitions from n to *Np* (inclusive). A middle asterisk means all partitions from m to n (inclusive).

This command can be useful for the "run_style verlet/split" command which imposed requirements on how the [[processors]{.doc}]processors.md){.reference .internal} command lays out a 3d grid of MPI processes in each of 2 partitions.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[run_style verlet/split]{.doc}]run_style.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

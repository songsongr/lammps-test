:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#write-restart-command .section}
[]{#index-0}

# write_restart command[](#write-restart-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    write_restart file keyword value ...
:::
::::

- file = name of file to write restart information to

- zero or more keyword/value pairs may be appended

- keyword = *fileper* or *nfile*

  ``` literal-block
  fileper arg = Np
    Np = write one file for every this many MPI processes
  nfile arg = Nf
    Nf = write this many files, one from each of Nf MPI processes
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    write_restart restart.equil
    write_restart poly.%.* nfile 10
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Write a binary restart file of the current state of the simulation.

During a long simulation, the [[restart]{.doc}]restart.md){.reference .internal} command is typically used to output restart files periodically. The write_restart command is useful after a minimization or whenever you wish to write out a single current restart file.

Similar to [[dump]{.doc}]dump.md){.reference .internal} files, the restart filename can contain two wild-card characters. If a "\*" appears in the filename, it is replaced with the current timestep value. If a "%" character appears in the filename, then one file is written by each processor and the "%" character is replaced with the MPI rank ID from 0 to *P*-1. An additional file with the "%" replaced by "base" is also written, which contains global information. For example, the files written for [`filename`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`restart.%`{.docutils .literal .notranslate}]{.pre} would be [`restart.base`{.docutils .literal .notranslate}]{.pre}, [`restart.0`{.docutils .literal .notranslate}]{.pre}, [`restart.1`{.docutils .literal .notranslate}]{.pre}, ... [`restart.P-1`{.docutils .literal .notranslate}]{.pre}. This creates smaller files and can be a fast mode of output and subsequent input on parallel machines that support parallel I/O. The optional *fileper* and *nfile* keywords discussed below can alter the number of files written.

Restart files can be read by a [[read_restart]{.doc}]read_restart.md){.reference .internal} command to restart a simulation from a particular state. Because the file is binary (to enable exact restarts), it may not be readable on another machine. In this case, you can use the [[-r command-line switch]{.doc}]Run_options.md){.reference .internal} to convert a restart file to a data file.

::: {.admonition .note}
Note

Although the purpose of restart files is to enable restarting a simulation from where it left off, not all information about a simulation is stored in the file. For example, the list of fixes that were specified during the initial run is not stored, which means the new input script must specify any fixes you want to use. Even when restart information is stored in the file, as it is for some fixes, commands may need to be re-specified in the new input script, in order to re-use that information. Details are usually given in the documentation of the respective command. Also, see the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for general information about what is stored in a restart file.
:::

------------------------------------------------------------------------

The optional *nfile* or *fileper* keywords can be used in conjunction with the "%" wildcard character in the specified restart file name. As explained above, the "%" character causes the restart file to be written in pieces, one piece for each of *P* MPI processes. By default *P* = the number of MPI processes the simulation is running on. The *nfile* or *fileper* keyword can be used to set *P* to a smaller value, which can be more efficient when running on a large number of MPI processes.

The *nfile* keyword sets *P* to the specified *Nf* value. For example, if *Nf* = 4, and the simulation is running on 100 MPI processes, 4 files will be written, by MPI ranks 0, 25, 50, and 75. Each will collect information from itself and the next 24 MPI processes and write it to a restart file.

For the *fileper* keyword, the specified value of *Np* means write one file for every *Np* MPI processes. For example, if *Np* = 4, every fourth MPI rank (0, 4, 8, 12, *etc.*) will collect information from itself and the next 3 MPI processes and write it to a restart file.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command requires inter-processor communication to migrate atoms before the restart file is written. This means that your system must be ready to perform a simulation before using this command (force fields setup, atom masses initialized, *etc.*).
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[restart]{.doc}]restart.md){.reference .internal}, [[read_restart]{.doc}]read_restart.md){.reference .internal}, [[write_data]{.doc}]write_data.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

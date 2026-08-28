:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#opt-package .section}
# [7.4.5. ]{.section-number}OPT package[](#opt-package "Link to this heading"){.headerlink}

The OPT package was developed by James Fischer (High Performance Technologies), David Richie, and Vincent Natoli (Stone Ridge Technologies). It contains a handful of pair styles whose compute() methods were rewritten in C++ templated form to reduce the overhead due to if tests and other conditional code.

::: {#required-hardware-software .section}
## Required hardware/software[](#required-hardware-software "Link to this heading"){.headerlink}

Any hardware. Any compiler.
:::

::: {#building-lammps-with-the-opt-package .section}
## Building LAMMPS with the OPT package[](#building-lammps-with-the-opt-package "Link to this heading"){.headerlink}

See the [[Build extras]{.std .std-ref}]Build_extras.md#opt){.reference .internal} page for instructions.
:::

::::: {#run-with-the-opt-package-from-the-command-line .section}
## Run with the OPT package from the command-line[](#run-with-the-opt-package-from-the-command-line "Link to this heading"){.headerlink}

:::: {.highlight-bash .notranslate}
::: highlight
    lmp_mpi -sf opt -in in.script                # run in serial
    mpirun -np 4 lmp_mpi -sf opt -in in.script   # run in parallel
:::
::::

Use the "-sf opt" [[command-line switch]{.doc}]Run_options.md){.reference .internal}, which will automatically append "opt" to styles that support it.
:::::

::::: {#or-run-with-the-opt-package-by-editing-an-input-script .section}
## Or run with the OPT package by editing an input script[](#or-run-with-the-opt-package-by-editing-an-input-script "Link to this heading"){.headerlink}

Use the [[suffix opt]{.doc}]suffix.md){.reference .internal} command, or you can explicitly add an "opt" suffix to individual styles in your input script, e.g.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/cut/opt 2.5
:::
::::
:::::

::: {#speed-up-to-expect .section}
## Speed-up to expect[](#speed-up-to-expect "Link to this heading"){.headerlink}

You should see a reduction in the "Pair time" value printed at the end of a run. On most machines for reasonable problem sizes, it will be a 5 to 20% savings.
:::

::: {#guidelines-for-best-performance .section}
## Guidelines for best performance[](#guidelines-for-best-performance "Link to this heading"){.headerlink}

Just try out an OPT pair style to see how it performs.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

None.
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

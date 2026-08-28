::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::: {#run-multiple-simulations-from-one-input-script .section}
# [10.1.5. ]{.section-number}Run multiple simulations from one input script[](#run-multiple-simulations-from-one-input-script "Link to this heading"){.headerlink}

This can be done in several ways. See the documentation for individual commands for more details on how these examples work.

If "multiple simulations" means to continue a previous simulation for more timesteps, then you simply use the [[run]{.doc}]run.md){.reference .internal} command multiple times. For example, this script

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    units lj
    atom_style atomic
    read_data data.lj
    run 10000
    run 10000
    run 10000
    run 10000
    run 10000
:::
::::

would run 5 successive simulations of the same system for a total of 50,000 timesteps.

If you wish to run totally different simulations, one after the other, the [[clear]{.doc}]clear.md){.reference .internal} command can be used in between them to re-initialize LAMMPS. For example, this script

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    units lj
    atom_style atomic
    read_data data.lj
    run 10000
    clear
    units lj
    atom_style atomic
    read_data data.lj.new
    run 10000
:::
::::

would run 2 independent simulations, one after the other.

For large numbers of independent simulations, you can use [[variables]{.doc}]variable.md){.reference .internal} and the [[next]{.doc}]next.md){.reference .internal} and [[jump]{.doc}]jump.md){.reference .internal} commands to loop over the same input script multiple times with different settings. For example, this script, named [`in.polymer`{.docutils .literal .notranslate}]{.pre}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable d index run1 run2 run3 run4 run5 run6 run7 run8
    shell cd $d
    read_data data.polymer
    run 10000
    shell cd ..
    clear
    next d
    jump in.polymer
:::
::::

would run 8 simulations in different directories, using a [`data.polymer`{.docutils .literal .notranslate}]{.pre} file in each directory. The same concept could be used to run the same system at 8 different temperatures, using a temperature variable and storing the output in different log and dump files, for example

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable a loop 8
    variable t index 0.8 0.85 0.9 0.95 1.0 1.05 1.1 1.15
    log log.$a
    read data.polymer
    velocity all create $t 352839
    fix 1 all nvt $t $t 100.0
    dump 1 all atom 1000 dump.$a
    run 100000
    clear
    next t
    next a
    jump in.polymer
:::
::::

All of the above examples work whether you are running on 1 or multiple processors, but assumed you are running LAMMPS on a single partition of processors. LAMMPS can be run on multiple partitions via the [[-partition command-line switch]{.doc}]Run_options.md){.reference .internal}.

In the last 2 examples, if LAMMPS were run on 3 partitions, the same scripts could be used if the [`index`{.docutils .literal .notranslate}]{.pre} and [`loop`{.docutils .literal .notranslate}]{.pre} variables were replaced with *universe*-style variables, as described in the [[variable]{.doc}]variable.md){.reference .internal} command. Also, the [`next `{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}[`t`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.nv .nv-Identifier} and [`next `{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}[`a`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.nv .nv-Identifier} commands would need to be replaced with a single [`next `{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}[`a`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.nv .nv-Identifier}[` `{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.w}[`t`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.n} command. With these modifications, the 8 simulations of each script would run on the 3 partitions one after the other until all were finished. Initially, 3 simulations would be started simultaneously, one on each partition. When one finished, that partition would then start the fourth simulation, and so forth, until all 8 were completed.
:::::::::::
::::::::::::
:::::::::::::

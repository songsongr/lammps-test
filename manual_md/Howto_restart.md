::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::: {#restart-a-simulation .section}
# [10.1.1. ]{.section-number}Restart a simulation[](#restart-a-simulation "Link to this heading"){.headerlink}

There are 3 ways to continue a long LAMMPS simulation. Multiple [[run]{.doc}]run.md){.reference .internal} commands can be used in the same input script. Each run will continue from where the previous run left off. Or binary restart files can be saved to disk using the [[restart]{.doc}]restart.md){.reference .internal} command. At a later time, these binary files can be read via a [[read_restart]{.doc}]read_restart.md){.reference .internal} command in a new script. Or they can be converted to text data files using the [[-r command-line switch]{.doc}]Run_options.md){.reference .internal} and read by a [[read_data]{.doc}]read_data.md){.reference .internal} command in a new script.

Here we give examples of 2 scripts that read either a binary restart file or a converted data file and then issue a new run command to continue where the previous run left off. They illustrate what settings must be made in the new script. Details are discussed in the documentation for the [[read_restart]{.doc}]read_restart.md){.reference .internal} and [[read_data]{.doc}]read_data.md){.reference .internal} commands.

Look at the *in.chain* input script provided in the *bench* directory of the LAMMPS distribution to see the original script that these 2 scripts are based on. If that script had the line

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    restart         50 tmp.restart
:::
::::

added to it, it would produce two binary restart files ([`tmp.restart.50`{.docutils .literal .notranslate}]{.pre} and [`tmp.restart.100`{.docutils .literal .notranslate}]{.pre}) as it ran.

This script could be used to read the first restart file and re-run the last 50 timesteps:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    read_restart    tmp.restart.50

    neighbor        0.4 bin
    neigh_modify    every 1 delay 1

    fix             1 all nve
    fix             2 all langevin 1.0 1.0 10.0 904297

    timestep        0.012

    run             50
:::
::::

Note that the following commands do not need to be repeated because their settings are included in the restart file: [`units`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}, [`atom_style`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}, [`special_bonds`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}, [`pair_style`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}, [`bond_style`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}. However, these commands do need to be used, since their settings are not in the restart file: [`neighbor`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}, [`fix`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}, [`timestep`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}.

If you actually use this script to perform a restarted run, you will notice that the thermodynamic data match at step 50 (if you also put a [`thermo`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k}[` `{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.w}[`50`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.m} command in the original script), but do not match at step 100. This is because the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} command uses random numbers in a way that does not allow for perfect restarts.

As an alternate approach, the restart file could be converted to a data file as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    lmp_g++ -r tmp.restart.50 tmp.restart.data
:::
::::

Then, this script could be used to re-run the last 50 steps:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    units           lj
    atom_style      bond
    pair_style      lj/cut 1.12
    pair_modify     shift yes
    bond_style      fene
    special_bonds   0.0 1.0 1.0

    read_data       tmp.restart.data

    neighbor        0.4 bin
    neigh_modify    every 1 delay 1

    fix             1 all nve
    fix             2 all langevin 1.0 1.0 10.0 904297

    timestep        0.012

    reset_timestep  50
    run             50
:::
::::

Note that nearly all the settings specified in the original [`in.chain`{.docutils .literal .notranslate}]{.pre} script must be repeated, except the [`pair_coeff`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k} and [`bond_coeff`{.code .highlight .LAMMPS .docutils .literal .highlight-LAMMPS}]{.k} commands, since the new data file lists the force field coefficients. Also, the [[reset_timestep]{.doc}]reset_timestep.md){.reference .internal} command is used to tell LAMMPS the current timestep. This value is stored in restart files, but not in data files.
:::::::::::
::::::::::::
:::::::::::::

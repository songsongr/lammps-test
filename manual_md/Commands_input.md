::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#lammps-input-scripts .section}
# [6.1. ]{.section-number}LAMMPS input scripts[](#lammps-input-scripts "Link to this heading"){.headerlink}

LAMMPS executes calculations by reading commands from a input script (text file), one line at a time. When the input script ends, LAMMPS exits. This is different from programs that read and process the entire input before starting a calculation.

Each command causes LAMMPS to take some immediate action without regard for any commands that may be processed later. Commands may set an internal variable, read in a file, or run a simulation. These actions can be grouped into three categories:

1.  commands that change a global setting (examples: [[timestep]{.doc}]timestep.md){.reference .internal}, [[newton]{.doc}]newton.md){.reference .internal}, [[echo]{.doc}]echo.md){.reference .internal}, [[log]{.doc}]log.md){.reference .internal}, [[thermo]{.doc}]thermo.md){.reference .internal}, [[restart]{.doc}]restart.md){.reference .internal}),

2.  commands that add, modify, remove, or replace "styles" that are executed during a "run" (examples: [[pair_style]{.doc}]pair_style.md){.reference .internal}, [[fix]{.doc}]fix.md){.reference .internal}, [[compute]{.doc}]compute.md){.reference .internal}, [[dump]{.doc}]dump.md){.reference .internal}, [[thermo_style]{.doc}]thermo_style.md){.reference .internal}, [[pair_modify]{.doc}]pair_modify.md){.reference .internal}), and

3.  commands that execute a "run" or perform some other computation or operation (examples: [[print]{.doc}]print.md){.reference .internal}, [[run]{.doc}]run.md){.reference .internal}, [[minimize]{.doc}]minimize.md){.reference .internal}, [[temper]{.doc}]temper.md){.reference .internal}, [[write_dump]{.doc}]write_dump.md){.reference .internal}, [[rerun]{.doc}]rerun.md){.reference .internal}, [[read_data]{.doc}]read_data.md){.reference .internal}, [[read_restart]{.doc}]read_restart.md){.reference .internal})

Commands in category a) have default settings, which means you only need to use the command if you wish to change the defaults.

In many cases, the ordering of commands in an input script is not important, but can have consequences when the global state is changed between commands in the c) category. The following rules apply:

1.  LAMMPS does not read your entire input script and then perform a simulation with all the settings. Rather, the input script is read one line at a time and each command takes effect when it is read. Thus this sequence of commands:

    :::: {.highlight-LAMMPS .notranslate}
    ::: highlight
        timestep 0.5
        run      100
        run      100
    :::
    ::::

    does something different than this sequence:

    :::: {.highlight-LAMMPS .notranslate}
    ::: highlight
        run      100
        timestep 0.5
        run      100
    :::
    ::::

    In the first case, the specified timestep (0.5 fs) is used for two simulations of 100 timesteps each. In the second case, the default timestep (1.0 fs) is used for the first 100 step simulation and a 0.5 fs timestep is used for the second one.

2.  Some commands are only valid when they follow other commands. For example you cannot set the temperature of a group of atoms until atoms have been defined and a group command is used to define which atoms belong to the group.

3.  Sometimes command B will use values that can be set by command A. This means command A must precede command B in the input script if it is to have the desired effect. For example, the [[read_data]{.doc}]read_data.md){.reference .internal} command initializes the system by setting up the simulation box and assigning atoms to processors. If default values are not desired, the [[processors]{.doc}]processors.md){.reference .internal} and [[boundary]{.doc}]boundary.md){.reference .internal} commands need to be used before [`read_data`{.docutils .literal .notranslate}]{.pre} to tell LAMMPS how to map processors to the simulation box.

Many input script errors are detected by LAMMPS and an ERROR or WARNING message is printed. The [[Errors]{.doc}]Errors.md){.reference .internal} page gives more information on what errors mean. The documentation for each command lists restrictions on how the command can be used.

You can use the [[-skiprun]{.std .std-ref}]Run_options.md#skiprun){.reference .internal} command-line flag to have LAMMPS skip the execution of any [`run`{.docutils .literal .notranslate}]{.pre}, [`minimize`{.docutils .literal .notranslate}]{.pre}, or similar commands to check the entire input for correct syntax to avoid crashes on typos or syntax errors in long runs.
:::
::::
:::::

::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#input-script-command-style .section}
# [3.10. ]{.section-number}Input script command style[](#input-script-command-style "Link to this heading"){.headerlink}

New commands can be added to LAMMPS input scripts by adding new classes that are derived from the Command class and thus must have a "command" method. For example, the [[create_atoms]{.doc}]create_atoms.md){.reference .internal}, [[read_data]{.doc}]read_data.md){.reference .internal}, [[velocity]{.doc}]velocity.md){.reference .internal}, and [[run]{.doc}]run.md){.reference .internal} commands are all implemented in this fashion. When such a command is encountered in the LAMMPS input script, LAMMPS simply creates a class instance with the corresponding name, invokes the "command" method of the class, and passes it the arguments from the input script. The command method can perform whatever operations it wishes on LAMMPS data structures. After the command method returns the class instance is deleted.

The method that your new Command class *must* define is as follows:

  --------- -----------------------------------------
  command   operations performed by the new command
  --------- -----------------------------------------

Of course, the new class can define other methods and variables as needed.
:::
::::
:::::

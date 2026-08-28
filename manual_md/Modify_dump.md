::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#dump-styles .section}
# [3.11. ]{.section-number}Dump styles[](#dump-styles "Link to this heading"){.headerlink}

Classes that dump per-atom info to files are derived from the Dump class. To dump new quantities or in a new format, a new derived dump class can be added, but it is typically simpler to modify the DumpCustom class contained in the dump_custom.cpp file.

Dump_atom.cpp is a simple example of a derived dump class.

Here is a brief description of methods you define in your new derived class. See dump.h for details.

  -------------- ---------------------------------------------------
  write_header   write the header section of a snapshot of atoms
  count          count the number of lines a processor will output
  pack           pack a proc's output data into a buffer
  write_data     write a proc's data to a file
  modify_param   called when dump_modify is executed (optional)
  extract        provide access to internal data (optional)
  -------------- ---------------------------------------------------

See the [[dump]{.doc}]dump.md){.reference .internal} command and its *custom* style for a list of keywords for atom information that can already be dumped by DumpCustom. It includes options to dump per-atom info from Compute classes, so adding a new derived Compute class is one way to calculate new quantities to dump.

Note that new keywords for atom properties are not typically added to the [[dump custom]{.doc}]dump.md){.reference .internal} command. Instead they are added to the [[compute property/atom]{.doc}]compute_property_atom.md){.reference .internal} command.
:::
::::
:::::

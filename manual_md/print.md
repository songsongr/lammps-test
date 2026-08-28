::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#print-command .section}
[]{#index-0}

# print command[](#print-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    print string keyword value
:::
::::

- string = text string to print, which may contain variables

- zero or more keyword/value pairs may be appended

- keyword = *file* or *append* or *screen* or *universe*

  ``` literal-block
  file value = filename
  append value = filename
  screen value = yes or no
  universe value = yes or no
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    print "Done with equilibration" file info.dat
    print Vol=$v append info.dat screen no
    print "The system volume is now $v"
    print 'The system volume is now $v'
    print "NEB calculation 1 complete" screen no universe yes
    print """
    System volume = $v
    System temperature = $t
    """
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Print a text string to the screen and logfile. The text string must be a single argument, so if it is one line but more than one word, it should be enclosed in single or double quotes. To generate multiple lines of output, the string can be enclosed in triple quotes, as in the last example above. If the text string contains variables, they will be evaluated and their current values printed.

::: versionadded
[Added in version 15Jun2023: ]{.versionmodified .added}support for vector style variables
:::

See the [[variable]{.doc}]variable.md){.reference .internal} command for a description of *equal* and *vector* style variables which are typically the most useful ones to use with the print command. Equal- and vector-style variables can calculate formulas involving mathematical operations, atom properties, group properties, thermodynamic properties, global values calculated by a [[compute]{.doc}]compute.md){.reference .internal} or [[fix]{.doc}]fix.md){.reference .internal}, or references to other [[variables]{.doc}]variable.md){.reference .internal}. Vector-style variables are printed in a bracketed, comma-separated format, e.g. \[1,2,3,4\] or \[12.5,2,4.6,10.1\].

::: {.admonition .note}
Note

As discussed on the [[Commands parse]{.doc}]Commands_parse.md){.reference .internal} doc page, the text string can use "immediate" variables, specified as \$(formula) with parenthesis, where the numeric formula has the same syntax as equal-style variables described on the [[variable]{.doc}]variable.md){.reference .internal} doc page. This is a convenient way to evaluate a formula immediately without using the variable command to define a named variable and then use that variable in the text string. The formula can include a trailing colon and format string which determines the precision with which the numeric value is output. This is also explained on the [[Commands parse]{.doc}]Commands_parse.md){.reference .internal} doc page.
:::

If you want the print command to be executed multiple times (with changing variable values), there are 3 options. First, consider using the [[fix print]{.doc}]fix_print.md){.reference .internal} command, which will print a string periodically during a simulation. Second, the print command can be used as an argument to the *every* option of the [[run]{.doc}]run.md){.reference .internal} command. Third, the print command could appear in a section of the input script that is looped over (see the [[jump]{.doc}]jump.md){.reference .internal} and [[next]{.doc}]next.md){.reference .internal} commands).

If the *file* or *append* keyword is used, a filename is specified to which the output will be written. If *file* is used, then the filename is overwritten if it already exists. If *append* is used, then the filename is appended to if it already exists, or created if it does not exist.

If the *screen* keyword is used, output to the screen and logfile can be turned on or off as desired.

If the *universe* keyword is used, output to the global screen and logfile can be turned on or off as desired. In multi-partition calculations, the *screen* option and the corresponding output only apply to the screen and logfile of the individual partition.
:::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix print]{.doc}]fix_print.md){.reference .internal}, [[variable]{.doc}]variable.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are no file output, screen = yes, and universe = no.
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

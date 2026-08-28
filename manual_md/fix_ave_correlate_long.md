:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-ave-correlate-long-command .section}
[]{#index-0}

# fix ave/correlate/long command[](#fix-ave-correlate-long-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID ave/correlate/long Nevery Nfreq value1 value2 ... keyword args ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- ave/correlate/long = style name of this fix command

- Nevery = use input values every this many time steps

- Nfreq = save state of the time correlation functions every this many time steps

- one or more input values can be listed

- value = c_ID, c_ID\[N\], f_ID, f_ID\[N\], v_name, v_name\[I\]

  :::: {.highlight-none .notranslate}
  ::: highlight
      c_ID = global scalar calculated by a compute with ID
      c_ID[I] = Ith component of global vector calculated by a compute with ID, I can include wildcard (see below)
      f_ID = global scalar calculated by a fix with ID
      f_ID[I] = Ith component of global vector calculated by a fix with ID, I can include wildcard (see below)
      v_name = global value calculated by an equal-style variable with name
      v_name[I] = Ith component of a vector-style variable with name, I can include wildcard (see below)
  :::
  ::::

- zero or more keyword/arg pairs may be appended

- keyword = *type* or *start* or *file* or *overwrite* or *title1* or *title2* or *ncorr* or *nlen* or *ncount*

  ``` literal-block
  type arg = auto or upper or lower or auto/upper or auto/lower or full or first
    auto = correlate each value with itself
    upper = correlate each value with each succeeding value
    lower = correlate each value with each preceding value
    auto/upper = auto + upper
    auto/lower = auto + lower
    full = correlate each value with every other value, including itself = auto + upper + lower
    first = correlate each value with the first value
  start args = Nstart
    Nstart = start accumulating correlations on this time step
  file arg = filename
    filename = name of file to output correlation data to
  overwrite arg = none = overwrite output file with only latest output
  title1 arg = string
    string = text to print as 1st line of output file
  title2 arg = string
    string = text to print as 2nd line of output file
  ncorr arg = Ncorrelators
    Ncorrelators = number of correlators to store
  nlen args = Nlen
    Nlen = length of each correlator
  ncount args = Ncount
    Ncount = number of values over which successive correlators are averaged
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all ave/correlate/long 5 1000 c_myTemp file temp.correlate
    fix 1 all ave/correlate/long 1 10000 &
              c_thermo_press[1] c_thermo_press[2] c_thermo_press[3] &
              type upper title1 "My correlation data" nlen 15 ncount 3
    fix 1 all ave/correlate/long 1 10000 c_thermo_press[*]
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix is similar in spirit and syntax to the [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal}. However, this fix allows the efficient calculation of time correlation functions on-the-fly over extremely long time windows with little additional CPU overhead, using a multiple-[\\(\\tau\\)]{.math .notranslate .nohighlight} method [[(Ramirez)]{.std .std-ref}](#ramirez){.reference .internal} that decreases the resolution of the stored correlation function with time. It is not a full drop-in replacement.

The group specified with this command is ignored. However, note that specified values may represent calculations performed by computes and fixes which store their own "group" definitions.

Each listed value can be the result of a compute or fix or the evaluation of an equal-style or vector-style variable. The specified indices can include a wildcard string. See the [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} page for details on that.

The *Nevery* and *Nfreq* arguments specify on what time steps the input values will be used to calculate correlation data and the frequency with which the time correlation functions will be output to a file, respectively. Note that there is no *Nrepeat* argument, unlike the [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} command.

The optional keywords *ncorr*, *nlen*, and *ncount* are unique to this command and determine the number of correlation points calculated and the memory and CPU overhead used by this calculation. *Nlen* and *ncount* determine the amount of averaging done at longer correlation times. The default values *nlen* = 16 and *ncount* = 2 ensure that the systematic error of the multiple-[\\(\\tau\\)]{.math .notranslate .nohighlight} correlator is always below the level of the statistical error of a typical simulation (which depends on the ensemble size and the simulation length).

The maximum correlation time (in time steps) that can be reached is given by the formula [\\((nlen-1) ncount\^{(ncorr-1)}\\)]{.math .notranslate .nohighlight}. Longer correlation times are discarded and not calculated. With the default values of the parameters ([\\(ncorr=20\\)]{.math .notranslate .nohighlight}, [\\(nlen=16\\)]{.math .notranslate .nohighlight} and [\\(ncount=2\\)]{.math .notranslate .nohighlight}), this corresponds to 7864320 time steps. If longer correlation times are needed, the value of ncorr should be increased. Using [\\(nlen=16\\)]{.math .notranslate .nohighlight} and [\\(ncount=2\\)]{.math .notranslate .nohighlight}, with [\\(ncorr=30\\)]{.math .notranslate .nohighlight}, the maximum number of steps that can be correlated is 80530636808. If [\\(ncorr=40\\)]{.math .notranslate .nohighlight}, correlation times in excess of [\\(8\\times 10\^{12}\\)]{.math .notranslate .nohighlight} time steps can be calculated.

The total memory needed for each correlation pair is roughly [\\(4 \\times ncorr\\times nlen \\times 8\\)]{.math .notranslate .nohighlight} bytes. With the default values of the parameters, this corresponds to about 10 KB.

For the meaning of the additional optional keywords, see the [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} doc page.
:::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

Contrary to [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} this fix does **not** provide access to its internal data to various output options. Since this fix in intended for the calculation of time correlation functions over very long MD simulations, the information about this fix is written automatically to binary restart files, so that the time correlation calculation can continue in subsequent simulations. None of the fix_modify options are relevant to this fix.

No parameter of this fix can be used with the start/stop keywords of the run command. This fix is not invoked during energy minimization.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

The option defaults for keywords that are also keywords for the [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} command are as follows: type = auto, start = 0, no file output, title 1,2 = strings as described on the [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} doc page.

The option defaults for keywords unique to this command are as follows: ncorr=20, nlen=16, ncount=2.

------------------------------------------------------------------------

**(Ramirez)** J. Ramirez, S.K. Sukumaran, B. Vorselaars and A.E. Likhtman, J. Chem. Phys. 133, 154103 (2010).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

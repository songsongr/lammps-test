:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#fix-ave-correlate-command .section}
[]{#index-0}

# fix ave/correlate command[](#fix-ave-correlate-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID ave/correlate Nevery Nrepeat Nfreq value1 value2 ... keyword args ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- ave/correlate = style name of this fix command

- Nevery = use input values every this many timesteps

- Nrepeat = \# of correlation time windows to accumulate

- Nfreq = calculate time window averages every this many timesteps

- one or more input values can be listed

- value = c_ID, c_ID\[N\], f_ID, f_ID\[N\], v_name

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

- keyword = *type* or *ave* or *start* or *prefactor* or *file* or *overwrite* or *title1* or *title2* or *title3*

  ``` literal-block
  type arg = auto or upper or lower or auto/upper or auto/lower or full or first
    auto = correlate each value with itself
    upper = correlate each value with each succeeding value
    lower = correlate each value with each preceding value
    auto/upper = auto + upper
    auto/lower = auto + lower
    full = correlate each value with every other value, including itself = auto + upper + lower
    first = correlate each value with the first value
  ave args = one or running
    one = zero the correlation accumulation every Nfreq steps
    running = accumulate correlations continuously
  start args = Nstart
    Nstart = start accumulating correlations on this timestep
  prefactor args = value
    value = prefactor to scale all the correlation data by
  file arg = filename
    filename = name of file to output correlation data to
  overwrite arg = none = overwrite output file with only latest output
  title1 arg = string
    string = text to print as 1st line of output file
  title2 arg = string
    string = text to print as 2nd line of output file
  title3 arg = string
    string = text to print as 3rd line of output file
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all ave/correlate 5 100 1000 c_myTemp file temp.correlate
    fix 1 all ave/correlate 1 50 10000 &
              c_thermo_press[1] c_thermo_press[2] c_thermo_press[3] &
              type upper ave running title1 "My correlation data"
    fix 1 all ave/correlate 1 50 10000 c_thermo_press[*]
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Use one or more global scalar values as inputs every few timesteps, calculate time correlations between them at varying time intervals, and average the correlation data over longer timescales. The resulting correlation values can be time integrated by [[variables]{.doc}]variable.md){.reference .internal} or used by other [[output commands]{.doc}]Howto_output.md){.reference .internal} such as [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal}, and can also be written to a file. See the [[fix ave/correlate/long]{.doc}]fix_ave_correlate_long.md){.reference .internal} command for an alternate method for computing correlation functions efficiently over very long time windows.

The group specified with this command is ignored. However, note that specified values may represent calculations performed by computes and fixes which store their own "group" definitions.

Each listed value can be the result of a [[compute]{.doc}]compute.md){.reference .internal} or [[fix]{.doc}]fix.md){.reference .internal} or the evaluation of an equal-style or vector-style [[variable]{.doc}]variable.md){.reference .internal}. In each case, the compute, fix, or variable must produce a global quantity, not a per-atom or local quantity. If you wish to spatial- or time-average or histogram per-atom quantities from a compute, fix, or variable, then see the [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal}, [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal}, or [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal} commands. If you wish to convert a per-atom quantity into a single global value, see the [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} command.

The input values must be all scalars. What kinds of correlations between input values are calculated is determined by the *type* keyword as discussed below.

[[Computes]{.doc}]compute.md){.reference .internal} that produce global quantities are those which do not have the word *atom* in their style name. Only a few [[fixes]{.doc}]fix.md){.reference .internal} produce global quantities. See the doc pages for individual fixes for info on which ones produce such values. [[Variables]{.doc}]variable.md){.reference .internal} of style *equal* and *vector* are the only ones that can be used with this fix. Variables of style *atom* cannot be used, since they produce per-atom values.

------------------------------------------------------------------------

For input values from a compute or fix or variable , the bracketed index I can be specified using a wildcard asterisk with the index to effectively specify multiple values. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the size of the vector, then an asterisk with no numeric values means all indices from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all indices from 1 to n (inclusive). A trailing asterisk means all indices from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all indices from m to n (inclusive).

Using a wildcard is the same as if the individual elements of the vector had been listed one by one. For example, the following two fix ave/correlate commands are equivalent, since the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} command creates a global vector with six values:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute myPress all pressure NULL
    fix 1 all ave/correlate 1 50 10000 c_myPress[*]
    fix 1 all ave/correlate 1 50 10000 &
              c_myPress[1] c_myPress[2] c_myPress[3] &
              c_myPress[4] c_myPress[5] c_myPress[6]
:::
::::

::: {.admonition .note}
Note

For a vector-style variable, only the wildcard forms "\*n" or "m\*n" are allowed. You must specify the upper bound, because vector-style variable lengths are not determined until the variable is evaluated. If n is specified larger than the vector length turns out to be, zeroes are output for missing vector values.
:::

------------------------------------------------------------------------

The [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight}, [\\(N\_\\text{repeat}\\)]{.math .notranslate .nohighlight}, and [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} arguments specify on what timesteps the input values will be used to calculate correlation data. The input values are sampled every [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight} time steps. The correlation data for the preceding samples is computed on time steps that are a multiple of [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight}. Consider a set of samples from some initial time up to an output timestep. The initial time could be the beginning of the simulation or the last output time; see the *ave* keyword for options. For the set of samples, the correlation value [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} is calculated as:

::: {.math .notranslate .nohighlight}
\\\[C\_{ij}(\\Delta t) = \\left\\langle V_i(t) V_j(t+\\Delta t)\\right\\rangle,\\\]
:::

which is the correlation value between input values [\\(V_i\\)]{.math .notranslate .nohighlight} and [\\(V_j\\)]{.math .notranslate .nohighlight}, separated by time [\\(\\Delta t\\)]{.math .notranslate .nohighlight}. Note that the second value [\\(V_j\\)]{.math .notranslate .nohighlight} in the pair is always the one sampled at the later time. The average is an average over every pair of samples in the set that are separated by time [\\(\\Delta t\\)]{.math .notranslate .nohighlight}. The maximum [\\(\\Delta t\\)]{.math .notranslate .nohighlight} used is of size [\\((N\_\\text{repeat} - 1) N\_\\text{every}\\)]{.math .notranslate .nohighlight}. Thus the correlation between a pair of input values yields [\\(N\_\\text{repeat}\\)]{.math .notranslate .nohighlight} correlation data:

::: {.math .notranslate .nohighlight}
\\\[C\_{ij}(0), C\_{ij}(N\_\\text{every}), C\_{ij}(2N\_\\text{every}), \\dotsc, C\_{ij}\\bigl((N\_\\text{repeat}-1) N\_\\text{every}\\bigr)\\\]
:::

For example, if [\\(N\_\\text{every}=5\\)]{.math .notranslate .nohighlight}, [\\(N\_\\text{repeat}=6\\)]{.math .notranslate .nohighlight}, and [\\(N\_\\text{freq}=100\\)]{.math .notranslate .nohighlight}, then values on time steps [\\(0, 5, 10, 15,\\dotsc,100\\)]{.math .notranslate .nohighlight} will be used to compute the final averages on time step 100. Six averages will be computed: [\\(C\_{ij}(0)\\)]{.math .notranslate .nohighlight}, [\\(C\_{ij}(5)\\)]{.math .notranslate .nohighlight}, [\\(C\_{ij}(10)\\)]{.math .notranslate .nohighlight}, [\\(C\_{ij}(15)\\)]{.math .notranslate .nohighlight}, [\\(C\_{ij}(20)\\)]{.math .notranslate .nohighlight}, and [\\(C\_{ij}(25)\\)]{.math .notranslate .nohighlight}. [\\(C\_{ij}(10)\\)]{.math .notranslate .nohighlight} on time step 100 will be the average of 19 samples, namely [\\(V_i(0) V_j(10)\\)]{.math .notranslate .nohighlight}, [\\(V_i(5) V_j(15)\\)]{.math .notranslate .nohighlight}, [\\(V_i(10) V_j(20)\\)]{.math .notranslate .nohighlight}, [\\(V_i(15) V_j(25), \\dotsc,\\)]{.math .notranslate .nohighlight} [\\(V_i(85) V_j(95)\\)]{.math .notranslate .nohighlight}, and [\\(V_i(90) V_j(100)\\)]{.math .notranslate .nohighlight}.

[\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} must be a multiple of [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight}; [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight} and [\\(N\_\\text{repeat}\\)]{.math .notranslate .nohighlight} must be non-zero. Also, if the *ave* keyword is set to *one* which is the default, then [\\(N\_\\text{freq} \\ge (N\_\\text{repeat} -1) N\_\\text{every}\\)]{.math .notranslate .nohighlight} is required.

------------------------------------------------------------------------

If a value begins with "c\_", a compute ID must follow which has been previously defined in the input script. If no bracketed term is appended, the global scalar calculated by the compute is used. If a bracketed term is appended, the [\\(I\^\\text{th}\\)]{.math .notranslate .nohighlight} element of the global vector calculated by the compute is used. See the discussion above for how [\\(I\\)]{.math .notranslate .nohighlight} can be specified with a wildcard asterisk to effectively specify multiple values.

Note that there is a [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} command that can sum per-atom quantities into a global scalar or vector which can then be accessed by fix ave/correlate. It can also be a compute defined not in your input script, but by [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} or other fixes such as [[fix nvt]{.doc}]fix_nh.md){.reference .internal} or [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal}. See the doc pages for these commands which give the IDs of these computes. Users can also write code for their own compute styles and [[add them to LAMMPS]{.doc}]Modify.md){.reference .internal}.

If a value begins with "f\_", a fix ID must follow which has been previously defined in the input script. If no bracketed term is appended, the global scalar calculated by the fix is used. If a bracketed term is appended, the [\\(I\^\\text{th}\\)]{.math .notranslate .nohighlight} element of the global vector calculated by the fix is used. See the discussion above for how [\\(I\\)]{.math .notranslate .nohighlight} can be specified with a wildcard asterisk to effectively specify multiple values.

Note that some fixes only produce their values on certain timesteps, which must be compatible with [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight}, else an error will result. Users can also write code for their own fix styles and [[add them to LAMMPS]{.doc}]Modify.md){.reference .internal}.

If a value begins with "v\_", a variable name must follow which has been previously defined in the input script. Only equal-style or vector-style variables can be referenced; the latter requires a bracketed term to specify the [\\(I\^\\text{th}\\)]{.math .notranslate .nohighlight} element of the vector calculated by the variable. See the [[variable]{.doc}]variable.md){.reference .internal} command for details. Note that variables of style *equal* or *vector* define a formula which can reference individual atom properties or thermodynamic keywords, or they can invoke other computes, fixes, or variables when they are evaluated, so this is a very general means of specifying quantities to time correlate.

------------------------------------------------------------------------

Additional optional keywords also affect the operation of this fix.

The *type* keyword determines which pairs of input values are correlated with each other. For [\\(N\\)]{.math .notranslate .nohighlight} input values [\\(V_i\\)]{.math .notranslate .nohighlight}, with [\\(i \\in \\{1,\\dotsc,N\\}\\)]{.math .notranslate .nohighlight}, let the number of pairs be [\\(N\_\\text{pair}\\)]{.math .notranslate .nohighlight}. Note that the second value in the pair, [\\(V_i(t) V_j(t+\\Delta t)\\)]{.math .notranslate .nohighlight}, is always the one sampled at the later time.

- If *type* is set to *auto* then each input value is correlated with itself (i.e., [\\(C\_{ii} = V_i\^2\\)]{.math .notranslate .nohighlight} for [\\(i \\in \\{1,\\dotsc,N\\}\\)]{.math .notranslate .nohighlight}, so [\\(N\_\\text{pair} = N\\)]{.math .notranslate .nohighlight}).

- If *type* is set to *upper* then each input value is correlated with every succeeding value (i.e., [\\(C\_{ij} = V_i V_j\\)]{.math .notranslate .nohighlight} for [\\(i \< j\\)]{.math .notranslate .nohighlight}, so [\\(N\_\\text{pair} = N (N-1)/2\\)]{.math .notranslate .nohighlight}).

- If *type* is set to *lower* then each input value is correlated with every preceding value (i.e., [\\(C\_{ij} = V_i V_j\\)]{.math .notranslate .nohighlight} for [\\(i \> j\\)]{.math .notranslate .nohighlight}, so [\\(N\_\\text{pair} = N(N-1)/2\\)]{.math .notranslate .nohighlight}).

- If *type* is set to *auto/upper* then each input value is correlated with itself and every succeeding value (i.e., [\\(C\_{ij} = V_i V_j\\)]{.math .notranslate .nohighlight} for [\\(i \\ge j\\)]{.math .notranslate .nohighlight}, so [\\(N\_\\text{pair} = N(N+1)/2\\)]{.math .notranslate .nohighlight}).

- If *type* is set to *auto/lower* then each input value is correlated with itself and every preceding value (i.e., [\\(C\_{ij} = V_i V_j\\)]{.math .notranslate .nohighlight} for [\\(i \\le j\\)]{.math .notranslate .nohighlight}, so [\\(N\_\\text{pair} = N(N+1)/2\\)]{.math .notranslate .nohighlight}).

- If *type* is set to *full* then each input value is correlated with itself and every other value (i.e., [\\(C\_{ij} = V_i V_j\\)]{.math .notranslate .nohighlight} for [\\(\\{i,j\\} = \\{1,N\\}\\)]{.math .notranslate .nohighlight}, so [\\(N\_\\text{pair} = N\^2\\)]{.math .notranslate .nohighlight}).

- If *type* is set to *first* then each input value is correlated with the first input value (i.e., [\\(C\_{ij} = V_1 V_j\\)]{.math .notranslate .nohighlight} for [\\(\\{j\\} = \\{1,N\\}\\)]{.math .notranslate .nohighlight}, so [\\(N\_\\text{pair} = N\\)]{.math .notranslate .nohighlight}).

The *ave* keyword determines what happens to the accumulation of correlation samples every [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} timesteps. If the *ave* setting is *one*, then the accumulation is restarted or zeroed every [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} timesteps. Thus the outputs on successive [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} timesteps are essentially independent of each other. The exception is that the [\\(C\_{ij}(0) = V_i(t) V_j(t)\\)]{.math .notranslate .nohighlight} value at a time step [\\(t,\\)]{.math .notranslate .nohighlight} where [\\(t\\)]{.math .notranslate .nohighlight} is a multiple of [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight}, contributes to the correlation output both at time [\\(t\\)]{.math .notranslate .nohighlight} and at time [\\(t+N\_\\text{freq}\\)]{.math .notranslate .nohighlight}.

If the *ave* setting is *running*, then the accumulation is never zeroed. Thus the output of correlation data at any timestep is the average over samples accumulated every [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight} steps since the fix was defined. It can only be restarted by deleting the fix via the [[unfix]{.doc}]unfix.md){.reference .internal} command, or by re-defining the fix by re-specifying it.

The *start* keyword specifies what time step the accumulation of correlation samples will begin on. The default is step 0. Setting it to a larger value can avoid adding non-equilibrated data to the correlation averages.

The *prefactor* keyword specifies a constant which will be used as a multiplier on the correlation data after it is averaged. It is effectively a scale factor on [\\(V_i V_j\\)]{.math .notranslate .nohighlight}, which can be used to account for the size of the time window or other unit conversions.

The *file* keyword allows a filename to be specified. Every [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} steps, an array of correlation data is written to the file. The number of rows is [\\(N\_\\text{repeat}\\)]{.math .notranslate .nohighlight}, as described above. The number of columns is [\\(N\_\\text{pair}+2\\)]{.math .notranslate .nohighlight}, also as described above. Thus the file ends up to be a series of these array sections.

The *overwrite* keyword will continuously overwrite the output file with the latest output, so that it only contains one timestep worth of output. This option can only be used with the *ave running* setting.

The *title1*, *title2*, and *title3* keywords allow specification of the strings that will be printed as the first three lines of the output file, assuming the *file* keyword was used. LAMMPS uses default values for each of these, so they do not need to be specified.

By default, these header lines are as follows:

``` literal-block
# Time-correlated data for fix ID
# TimeStep Number-of-time-windows
# Index TimeDelta Ncount valueI*valueJ valueI*valueJ ...
```

In the first line, ID is replaced with the fix-ID. The second line describes the two values that are printed at the first of each section of output. In the third line the value pairs are replaced with the appropriate fields from the fix ave/correlate command.

------------------------------------------------------------------------

Let [\\(S\_{ij}\\)]{.math .notranslate .nohighlight} be a set of time correlation data for input values [\\(I\\)]{.math .notranslate .nohighlight} and [\\(J\\)]{.math .notranslate .nohighlight}, namely the [\\(N\_\\text{repeat}\\)]{.math .notranslate .nohighlight} values:

::: {.math .notranslate .nohighlight}
\\\[S\_{ij} = C\_{ij}(0), C\_{ij}(N\_\\text{every}), C\_{ij}(2N\_\\text{every}), \\dotsc, C\_{ijI}\\bigl((N\_\\text{repeat}-1) N\_\\text{every}\\bigr)\\\]
:::

As explained below, these data are output as one column of a global array, which is effectively the correlation matrix.

The *trap* function defined for [[equal-style variables]{.doc}]variable.md){.reference .internal} can be used to perform a time integration of this vector of data, using a trapezoidal rule. This is useful for calculating various quantities which can be derived from time correlation data. If a normalization factor is needed for the time integration, it can be included in the variable formula or via the *prefactor* keyword.
:::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix computes a global array of values which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The values can only be accessed on timesteps that are multiples of [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} since that is when averaging is performed. The global array has \# of rows [\\(N\_\\text{repeat}\\)]{.math .notranslate .nohighlight} and \# of columns [\\(N\_\\text{pair}+2\\)]{.math .notranslate .nohighlight}. The first column has the time [\\(\\Delta t\\)]{.math .notranslate .nohighlight} (in time steps) between the pairs of input values used to calculate the correlation, as described above. The second column has the number of samples contributing to the correlation average, as described above. The remaining Npair columns are for [\\(I,J\\)]{.math .notranslate .nohighlight} pairs of the [\\(N\\)]{.math .notranslate .nohighlight} input values, as determined by the *type* keyword, as described above.

- For *type* = *auto*, the [\\(N\_\\text{pair} = N\\)]{.math .notranslate .nohighlight} columns are ordered: [\\(C\_{11}, C\_{22}, \\dotsc, C\_{NN}\\)]{.math .notranslate .nohighlight}

- For *type* = *upper*, the [\\(N\_\\text{pair} = N(N-1)/2\\)]{.math .notranslate .nohighlight} columns are ordered: [\\(C\_{12}, C\_{13}, \\dotsc, C\_{1N}, C\_{23}, \\dotsc, C\_{2N}, C\_{34}, \\dotsc, C\_{N-1,N}\\)]{.math .notranslate .nohighlight}

- For *type* = *lower*, the [\\(N\_\\text{pair} = N(N-1)/2\\)]{.math .notranslate .nohighlight} columns are ordered: [\\(C\_{21}, C\_{31}, C\_{32}, C\_{41}, C\_{42}, C\_{43I}, \\dotsc, C\_{N1}, C\_{N2}, \\dotsc, C\_{N,N-1}\\)]{.math .notranslate .nohighlight}

- For *type* = *auto/upper*, the [\\(N\_\\text{pair} = N(N+1)/2\\)]{.math .notranslate .nohighlight} columns are ordered: [\\(C\_{11}, C\_{12}, C\_{13}, \\dotsc, C\_{1N}, C\_{22}, C\_{23}, \\dotsc, C\_{2N}, C\_{33}, C\_{34}, \\dotsc, C\_{N-1,N}, C\_{NN}\\)]{.math .notranslate .nohighlight}

- For *type* = *auto/lower*, the [\\(N\_\\text{pair} = N(N+1)/2\\)]{.math .notranslate .nohighlight} columns are ordered: [\\(C\_{11}, C\_{21}, C\_{22}, C\_{31}, C\_{32}, C\_{33}, C\_{41}, \\dotsc, C\_{44}, C\_{N1}, C\_{N2}, \\dotsc, C\_{N,N-1}, C\_{NN}\\)]{.math .notranslate .nohighlight}

- For *type* = *full*, the [\\(N\_\\text{pair} = N\^2\\)]{.math .notranslate .nohighlight} columns are ordered: [\\(C\_{11}, C\_{12}, \\dotsc, C\_{1N}, C\_{21}, C\_{22}, \\dotsc, C\_{2N}, C\_{31}, \\dotsc, C\_{3N}, \\dotsc, C\_{N1}, \\dotsc, C\_{N,N-1}, C\_{NN}\\)]{.math .notranslate .nohighlight}

- For *type* = *first*, the [\\(N\_\\text{pair} = N\\)]{.math .notranslate .nohighlight} columns are ordered: [\\(C\_{11}, C\_{12}, \\dotsc, C\_{1N}\\)]{.math .notranslate .nohighlight}

The array values calculated by this fix are treated as extensive. If you need to divide them by the number of atoms, you must do this in a later processing step (e.g., when using them in a [[variable]{.doc}]variable.md){.reference .internal}).

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix ave/correlate/long]{.doc}]fix_ave_correlate_long.md){.reference .internal}, [[compute]{.doc}]compute.md){.reference .internal}, [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}, [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal}, [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal}, [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal}, [[variable]{.doc}]variable.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

The option defaults are ave = one, type = auto, start = 0, no file output, title 1,2,3 = strings as described above, and prefactor = 1.0.
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

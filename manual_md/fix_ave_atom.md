::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#fix-ave-atom-command .section}
[]{#index-0}

# fix ave/atom command[](#fix-ave-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID ave/atom Nevery Nrepeat Nfreq value1 value2 ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- ave/atom = style name of this fix command

- Nevery = use input values every this many timesteps

- Nrepeat = \# of times to use input values for calculating averages

- Nfreq = calculate averages every this many timesteps

- one or more input values can be listed

- value = *x*, *y*, *z*, *vx*, *vy*, *vz*, *fx*, *fy*, *fz*, c_ID, c_ID\[i\], f_ID, f_ID\[i\], v_name

  :::: {.highlight-none .notranslate}
  ::: highlight
      x,y,z,vx,vy,vz,fx,fy,fz = atom attribute (position, velocity, force component)
      c_ID = per-atom vector calculated by a compute with ID
      c_ID[I] = Ith column of per-atom array calculated by a compute with ID, I can include wildcard (see below)
      f_ID = per-atom vector calculated by a fix with ID
      f_ID[I] = Ith column of per-atom array calculated by a fix with ID, I can include wildcard (see below)
      v_name = per-atom vector calculated by an atom-style variable with name
  :::
  ::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all ave/atom 1 100 100 vx vy vz
    fix 1 all ave/atom 10 20 1000 c_my_stress[1]
    fix 1 all ave/atom 10 20 1000 c_my_stress[*]
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Use one or more per-atom vectors as inputs every few timesteps, and average them atom by atom over longer timescales. The resulting per-atom averages can be used by other [[output commands]{.doc}]Howto_output.md){.reference .internal} such as the [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} or [[dump custom]{.doc}]dump.md){.reference .internal} commands.

The group specified with the command means only atoms within the group have their averages computed. Results are set to 0.0 for atoms not in the group.

Each input value can be an atom attribute (position, velocity, force component) or can be the result of a [[compute]{.doc}]compute.md){.reference .internal} or [[fix]{.doc}]fix.md){.reference .internal} or the evaluation of an atom-style [[variable]{.doc}]variable.md){.reference .internal}. In the latter cases, the compute, fix, or variable must produce a per-atom vector, not a global quantity or local quantity. If you wish to time-average global quantities from a compute, fix, or variable, then see the [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} command.

Each per-atom value of each input vector is averaged independently.

[[Computes]{.doc}]compute.md){.reference .internal} that produce per-atom vectors or arrays are those which have the word *atom* in their style name. See the doc pages for individual [[fixes]{.doc}]fix.md){.reference .internal} to determine which ones produce per-atom vectors or arrays. [[Variables]{.doc}]variable.md){.reference .internal} of style *atom* are the only ones that can be used with this fix since they produce per-atom vectors.

Note that for values from a compute or fix, the bracketed index I can be specified using a wildcard asterisk with the index to effectively specify multiple values. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the size of the vector (for *mode* = scalar) or the number of columns in the array (for *mode* = vector), then an asterisk with no numeric values means all indices from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all indices from 1 to n (inclusive). A trailing asterisk means all indices from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all indices from m to n (inclusive).

Using a wildcard is the same as if the individual columns of the array had been listed one by one. For example, these two fix ave/atom commands are equivalent, since the [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} command creates a per-atom array with six columns:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute my_stress all stress/atom NULL
    fix 1 all ave/atom 10 20 1000 c_my_stress[*]
    fix 1 all ave/atom 10 20 1000 c_my_stress[1] c_my_stress[2] &
                                  c_my_stress[3] c_my_stress[4] &
                                  c_my_stress[5] c_my_stress[6]
:::
::::

------------------------------------------------------------------------

The [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight}, [\\(N\_\\text{repeat}\\)]{.math .notranslate .nohighlight}, and [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} arguments specify on what timesteps the input values will be used in order to contribute to the average. The final averaged quantities are generated on timesteps that are a multiple of [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight}. The average is over [\\(N\_\\text{repeat}\\)]{.math .notranslate .nohighlight} quantities, computed in the preceding portion of the simulation every [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight} timesteps. [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} must be a multiple of [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight} and [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight} must be non-zero even if [\\(N\_\\text{repeat}\\)]{.math .notranslate .nohighlight} is 1. Also, the timesteps contributing to the average value cannot overlap; that is, [\\(N\_\\text{repeat} \\times N\_\\text{every}\\)]{.math .notranslate .nohighlight} cannot exceed [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight}.

For example, if [\\(N\_\\text{every}=2\\)]{.math .notranslate .nohighlight}, [\\(N\_\\text{repeat}=6\\)]{.math .notranslate .nohighlight}, and [\\(N\_\\text{freq}=100\\)]{.math .notranslate .nohighlight}, then values on timesteps 90, 92, 94, 96, 98, and 100 will be used to compute the final average on time step 100. Similarly for timesteps 190, 192, 194, 196, 198, and 200 on time step 200, etc.

------------------------------------------------------------------------

The atom attribute values (*x*, *y*, *z*, *vx*, *vy*, *vz*, *fx*, *fy*, and *fz*) are self-explanatory. Note that other atom attributes can be used as inputs to this fix by using the [[compute property/atom]{.doc}]compute_property_atom.md){.reference .internal} command and then specifying an input value from that compute.

::: {.admonition .note}
Note

The *x*, *y*, and *z* attributes are values that are re-wrapped inside the periodic box whenever an atom crosses a periodic boundary. Thus, if you time-average an atom that spends half of its time on either side of the periodic box, you will get a value in the middle of the box. If this is not what you want, consider averaging unwrapped coordinates, which can be provided by the [[compute property/atom]{.doc}]compute_property_atom.md){.reference .internal} command via its *xu*, *yu*, and *zu* attributes.
:::

If a value begins with "c\_", a compute ID must follow which has been previously defined in the input script. If no bracketed term is appended, the per-atom vector calculated by the compute is used. If a bracketed term containing an index [\\(I\\)]{.math .notranslate .nohighlight} is appended, the [\\(I\^\\text{th}\\)]{.math .notranslate .nohighlight} column of the per-atom array calculated by the compute is used. Users can also write code for their own compute styles and [[add them to LAMMPS]{.doc}]Modify.md){.reference .internal}. See the discussion above for how [\\(I\\)]{.math .notranslate .nohighlight} can be specified with a wildcard asterisk to effectively specify multiple values.

If a value begins with "f\_", a fix ID must follow which has been previously defined in the input script. If no bracketed term is appended, the per-atom vector calculated by the fix is used. If a bracketed term containing an index [\\(I\\)]{.math .notranslate .nohighlight} is appended, the [\\(I\^\\text{th}\\)]{.math .notranslate .nohighlight} column of the per-atom array calculated by the fix is used. Note that some fixes only produce their values on certain timesteps, which must be compatible with [\\(N\_\\text{every}\\)]{.math .notranslate .nohighlight}, else an error will result. Users can also write code for their own fix styles and [[add them to LAMMPS]{.doc}]Modify.md){.reference .internal}. See the discussion above for how [\\(I\\)]{.math .notranslate .nohighlight} can be specified with a wildcard asterisk to effectively specify multiple values.

If a value begins with "v\_", a variable name must follow which has been previously defined in the input script as an [[atom-style variable]{.doc}]variable.md){.reference .internal}. Variables of style *atom* can reference thermodynamic keywords or invoke other computes, fixes, or variables when they are evaluated, so this is a very general means of generating per-atom quantities to time average.
::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global scalar or vector quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}.

This fix produces a per-atom vector or array which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. A vector is produced if only a single quantity is averaged by this fix. If two or more quantities are averaged, then an array of values is produced. The per-atom values can only be accessed on timesteps that are multiples of [\\(N\_\\text{freq}\\)]{.math .notranslate .nohighlight} since that is when averaging is performed.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute]{.doc}]compute.md){.reference .internal}, [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal}, [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal}, [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}, [[variable]{.doc}]variable.md){.reference .internal},
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

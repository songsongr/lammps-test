::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#reset-timestep-command .section}
[]{#index-0}

# reset_timestep command[](#reset-timestep-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    reset_timestep N keyword values ...
:::
::::

- N = timestep number

- zero or more keyword/value pairs may be appended

- keyword = *time*

  ``` literal-block
  time value = atime
     atime = accumulated simulation time
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    reset_timestep 0
    reset_timestep 4000000
    reset_timestep 1000 time 100.0
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set the timestep counter to the specified value. This command usually comes after the timestep has been set by reading a restart file via the [[read_restart]{.doc}]read_restart.md){.reference .internal} command, or a previous simulation run or minimization advanced the timestep.

The optional *time* keyword allows to also set the accumulated simulation time. This is usually the number of timesteps times the size of the timestep, but when using variable size timesteps with [[fix dt/reset]{.doc}]fix_dt_reset.md){.reference .internal} it can differ.

The [[read_data]{.doc}]read_data.md){.reference .internal} and [[create_box]{.doc}]create_box.md){.reference .internal} commands set the timestep to 0; the [[read_restart]{.doc}]read_restart.md){.reference .internal} command sets the timestep to the value it had when the restart file was written. The same applies to the accumulated simulation time.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command cannot be used when any fixes are defined that keep track of elapsed time to perform certain kinds of time-dependent operations. Examples are the [[fix deposit]{.doc}]fix_deposit.md){.reference .internal} and [[fix dt/reset]{.doc}]fix_dt_reset.md){.reference .internal} commands. The former adds atoms on specific timesteps. The latter keeps track of accumulated time.

Various fixes use the current timestep to calculate related quantities. If the timestep is reset, this may produce unexpected behavior, but LAMMPS allows the fixes to be defined even if the timestep is reset. For example, commands which thermostat the system, e.g. [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, allow you to specify a target temperature which ramps from Tstart to Tstop which may persist over several runs. If you change the timestep, you may induce an instantaneous change in the target temperature.

Resetting the timestep clears flags for [[computes]{.doc}]compute.md){.reference .internal} that may have calculated some quantity from a previous run. This means these quantity cannot be accessed by a variable in between runs until a new run is performed. See the [[variable]{.doc}]variable.md){.reference .internal} command for more details.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[rerun]{.doc}]rerun.md){.reference .internal}, [[timestep]{.doc}]timestep.md){.reference .internal}, [[fix dt/reset]{.doc}]fix_dt_reset.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

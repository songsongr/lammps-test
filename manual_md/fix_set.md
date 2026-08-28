::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::: {#fix-set-command .section}
[]{#index-0}

# fix set command[](#fix-set-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID set Nfreq rnflag set-args
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- set = style name of this fix command

- Nfreq = reset per-atom properties every this many timesteps

- rnflag = 1 to reneighbor on next timestep, 0 to not

- set-args = identical to args for the [[set]{.doc}]set.md){.reference .internal} command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 10 all set 1 0 group all i_dump v_new
    fix 10 all set 1 0 group all i_dump v_turnoff
:::
::::
:::::

:::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 12Jun2025.]{.versionmodified .added}
:::

Reset one or more properties of one or more atoms once every *Nfreq* steps during a simulation.

If the *rnflag* for reneighboring is set to 1, then a reneighboring will be triggered on the next timestep (since the fix set operation occurs at the end of the current timestep). This is important to do if this command changes per-atom properties that need to be communicated to ghost atoms. If this is not the case, an *rnflag* setting of 0 can be used; reneighboring will only be triggered on subsequent timesteps by the usual neighbor list criteria; see the [[neigh_modify command]{.doc}]neigh_modify.md){.reference .internal}.

Here are two examples where an *rnflag* setting of 1 are needed. If a custom per-atom property is changed and the [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal} command to create the property used the *ghost yes* keyword. Or if per-atom charges are changed, all pair styles which compute Coulombic interactions require charge values for ghost atoms. In both these examples, the re-neighboring will trigger the changes in the owned atom properties to be immediately communicated to ghost atoms.

The arguments following *Nfreq* and *rnflag* are identical to those allowed for the [[set]{.doc}]set.md){.reference .internal} command, as in the examples above and below.

Note that the group-ID setting for this command is ignored. The syntax for the [[set]{.doc}]set.md){.reference .internal} arguments allows selection of which atoms have their properties reset.

This command can only be used to reset an atom property using a per-atom variable. This option in allowed by many, but not all, of the keyword/value pairs supported by the [[set]{.doc}]set.md){.reference .internal} command. The reason for this restriction is that if a per-atom variable is not used, this command will typically not change atom properties during the simulation.

The [[set]{.doc}]set.md){.reference .internal} command can be used with similar syntax to this command to reset atom properties once before or between simulations.

------------------------------------------------------------------------

Here is an example of input script commands which will output atoms into a dump file only when their x-velocity crosses a threshold value *vthresh* for the first time. Their position and x-velocity will then be output every step for *twindow* timesteps.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable        vthresh equal 2             # threshold velocity
    variable        twindow equal 10            # dump for this many steps
    #
    # define custom property i_dump to store timestep threshold is crossed
    #
    fix             2 all property/atom i_dump
    set             group all i_dump -1
    #
    # fix set command checks for threshold crossings every step
    # resets i_dump from -1 to current timestep when crossing occurs
    #
    variable        start atom "vx > v_vthresh && i_dump == -1"
    variable        new atom ternary(v_start,step,i_dump)
    fix             3 all set 1 0 group all i_dump v_new
    #
    # dump command with thresh which enforces twindow
    #
    dump            1 all custom 1 tmp.dump id x y vx i_dump
    variable        dumpflag atom "i_dump >= 0 && (step-i_dump) < v_twindow"
    dump_modify     1 thresh v_dumpflag == 1
    #
    # run the simulation
    # final dump with all atom IDs which crossed threshold on which timestep
    #
    run             1000
    write_dump      all custom tmp.dump.final id i_dump modify thresh i_dump >= 0
:::
::::

The tmp.dump.final file lists which atoms crossed the velocity threshold. This command will print the *twindow* timesteps when a specific atom ID (104 in this case) was output in the tmp.dump file:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    % grep "^104 " tmp.dump
:::
::::

If these commands are used instead of the above, then an atom can cross the velocity threshold multiple times, and will be output for *twindow* timesteps each time. However the write_dump command is no longer useful.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable        vthresh equal 2             # threshold velocity
    variable        twindow equal 10            # dump for this many steps
    #
    # define custom property i_dump to store timestep threshold is crossed
    #
    fix             2 all property/atom i_dump
    set             group all i_dump -1
    #
    # fix set command checks for threshold crossings every step
    # resets i_dump from -1 to current timestep when crossing occurs
    #
    variable        start atom "vx > v_vthresh && i_dump == -1"
    variable        turnon atom ternary(v_start,step,i_dump)
    variable        stop atom "v_turnon >= 0 && (step-v_turnon) < v_twindow"
    variable        turnoff atom ternary(v_stop,v_turnon,-1)
    fix             3 all set 1 0 group all i_dump v_turnoff
    #
    # dump command with thresh which enforces twindow
    #
    dump            1 all custom 1 tmp.dump id x y vx i_dump
    variable        dumpflag atom "i_dump >= 0 && (step-i_dump) < v_twindow"
    dump_modify     1 thresh v_dumpflag == 1
    #
    # run the simulation
    #
    run             1000
:::
::::
::::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[set]{.doc}]set.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

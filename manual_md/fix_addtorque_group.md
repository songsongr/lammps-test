:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-addtorque-group-command .section}
[]{#index-0}

# fix addtorque/group command[](#fix-addtorque-group-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID addtorque/group Tx Ty Tz
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- addtorque/group = style name of this fix command

- Tx,Ty,Tz = torque component values (torque units)

- any of Tx,Ty,Tz can be a variable (see below)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix kick bead addtorque/group 2.0 3.0 5.0
    fix kick bead addtorque/group 0.0 0.0 v_oscillate
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 10Dec2025: ]{.versionmodified .changed}Fix *addtorque* was renamed to fix *addtorque/group*
:::

Add a set of forces to each atom in the group such that:

- the components of the total torque applied on the group (around its center of mass) are [\\(T_x\\)]{.math .notranslate .nohighlight}, [\\(T_y\\)]{.math .notranslate .nohighlight}, and [\\(T_z\\)]{.math .notranslate .nohighlight}

- the group would move as a rigid body in the absence of other forces.

This command can be used to drive a group of atoms into rotation by adding forces to the atoms. To apply a torque to individual finite-size atoms, use [[fix addtorque/atom]{.doc}]fix_addtorque_atom.md){.reference .internal} instead.

Any of the three quantities defining the torque components can be specified as an equal-style [[variable]{.doc}]variable.md){.reference .internal}, namely *Tx*, *Ty*, *Tz*. If the value is a variable, it should be specified as v_name, where name is the variable name. In this case, the variable will be evaluated each timestep, and its value used to determine the torque component.

Equal-style variables can specify formulas with various mathematical functions, and include [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command keywords for the simulation box parameters and timestep and elapsed time. Thus it is easy to specify a time-dependent torque.

::: {.admonition .note}
Note

Fix *addtorque/group* previously was known as fix *addtorque* and was renamed to clarify that the fix operates on a group of atoms as opposed to individual finite-size atoms.
:::
:::::

------------------------------------------------------------------------

::::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the potential "energy" inferred by the added torques to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}. Note that this is a fictitious quantity but is needed so that the [[minimize]{.doc}]minimize.md){.reference .internal} command can include the forces added by this fix in a consistent manner (i.e., there is a decrease in potential energy when atoms move in the direction of the added forces).

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is adding its torque. Default is the outermost level.

This fix computes a global scalar and a global 3-vector, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the potential energy discussed above. The vector is the total torque on the group of atoms before the forces on individual atoms are changed by the fix. The scalar and vector values calculated by this fix are "extensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The forces due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command.

::: {.admonition .note}
Note

If you want the fictitious potential energy associated with the added forces to be included in the total potential energy of the system (the quantity being minimized), you MUST enable the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for this fix.
:::

::: {.admonition .note}
Note

You should not specify force components with a variable that has time-dependence for use with a minimizer, since the minimizer increments the timestep as the iteration count during the minimization.
:::
:::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix addforce]{.doc}]fix_addforce.md){.reference .internal} [[fix addtorque/atom]{.doc}]fix_addtorque_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

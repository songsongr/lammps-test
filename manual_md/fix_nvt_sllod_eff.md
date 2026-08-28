:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-nvt-sllod-eff-command .section}
[]{#index-0}

# fix nvt/sllod/eff command[](#fix-nvt-sllod-eff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nvt/sllod/eff keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nvt/sllod/eff = style name of this fix command

- zero or more keyword/value pairs may be appended

  ``` literal-block
  keyword = psllod
    psllod value = no or yes = use SLLOD or p-SLLOD variant, respectively
  ```

- additional thermostat related keyword/value pairs from the [[fix nvt/eff]{.doc}]fix_nh_eff.md){.reference .internal} command may be appended, too.
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nvt/sllod/eff temp 300.0 300.0 0.1
    fix 1 all nvt/sllod/eff temp 300.0 300.0 0.1 drag 0.2
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform constant NVT integration to update positions and velocities each timestep for nuclei and electrons in the group for the [[electron force field]{.doc}]pair_eff.md){.reference .internal} model, using a Nose/Hoover temperature thermostat. V is volume; T is temperature. This creates a system trajectory consistent with the canonical ensemble.

The operation of this fix is exactly like that described by the [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal} command, except that the radius and radial velocity of electrons are also updated and thermostatted. Likewise the temperature calculated by the fix, using the compute it creates (as discussed in the [[fix nvt, npt, and nph]{.doc}]fix_nh.md){.reference .internal} doc page), is performed with a [[compute temp/deform/eff]{.doc}]compute_temp_deform_eff.md){.reference .internal} command (if *peculiar* = *no*) or a [[compute temp/eff]{.doc}]compute_temp_eff.md){.reference .internal} command (if *peculiar* = *yes*) that includes the eFF contribution to the temperature from the electron radial velocity.
:::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the state of the Nose/Hoover thermostat to [[binary restart files]{.doc}]restart.md){.reference .internal}. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* option is supported by this fix. You can use it to assign a [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its thermostatting procedure. The *kick* option is also supported as described by [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal}.

The cumulative energy change in the system imposed by this fix is included in the [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} keywords *ecouple* and *econserve*. See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} doc page for details. Note, as for [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal} this does NOT include the work done to drive the flow, so those values are expected to change with time.

This fix computes the same global scalar and global vector of quantities as does the [[fix nvt/eff]{.doc}]fix_nh_eff.md){.reference .internal} command.

This fix can ramp its target temperature over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This fix works best without Nose-Hoover chain thermostats, i.e. using tchain = 1. Setting tchain to larger values can result in poor equilibration.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nve/eff]{.doc}]fix_nve_eff.md){.reference .internal}, [[fix nvt/eff]{.doc}]fix_nh_eff.md){.reference .internal}, [[fix langevin/eff]{.doc}]fix_langevin_eff.md){.reference .internal}, [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal}, [[fix_modify]{.doc}]fix_modify.md){.reference .internal}, [[compute temp/deform/eff]{.doc}]compute_temp_deform_eff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

Same as [[fix nvt/eff]{.doc}]fix_nh_eff.md){.reference .internal}, except *tchain* = 1, *psllod* = *no*, *peculiar* = *no*, *kick* = *yes*, *integrator* = *reversible*.

------------------------------------------------------------------------

**(Tuckerman)** Tuckerman, Mundy, Balasubramanian, Klein, J Chem Phys, 106, 5615 (1997).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

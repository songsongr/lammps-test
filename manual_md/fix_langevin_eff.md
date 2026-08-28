::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-langevin-eff-command .section}
[]{#index-0}

# fix langevin/eff command[](#fix-langevin-eff-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID langevin/eff Tstart Tstop damp seed keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- langevin/eff = style name of this fix command

- Tstart,Tstop = desired temperature at start/end of run (temperature units)

- damp = damping parameter (time units)

- seed = random number seed to use for white noise (positive integer)

- zero or more keyword/value pairs may be appended

  ``` literal-block
  keyword = scale or tally or zero
    scale values = type ratio
      type = atom type (1-N)
      ratio = factor by which to scale the damping coefficient
    tally values = no or yes
      no = do not tally the energy added/subtracted to atoms
      yes = do tally the energy added/subtracted to atoms
  ```

  ``` literal-block
  zero value = no or yes
    no = do not set total random force to zero
    yes = set total random force to zero
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 3 boundary langevin/eff 1.0 1.0 10.0 699483
    fix 1 all langevin/eff 1.0 1.1 10.0 48279 scale 3 1.5
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply a Langevin thermostat as described in [[(Schneider)]{.std .std-ref}](#schneider2){.reference .internal} to a group of nuclei and electrons in the [[electron force field]{.doc}]pair_eff.md){.reference .internal} model. Used with [[fix nve/eff]{.doc}]fix_nve_eff.md){.reference .internal}, this command performs Brownian dynamics (BD), since the total force on each atom will have the form:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}F = & F_c + F_f + F_r \\\\ F_f = & - \\frac{m}{\\mathrm{damp}} v \\\\ F_r \\propto & \\sqrt{\\frac{k_B T m}{dt\~\\mathrm{damp}}}\\end{split}\\\]
:::

[\\(F_c\\)]{.math .notranslate .nohighlight} is the conservative force computed via the usual inter-particle interactions ([[pair_style]{.doc}]pair_style.md){.reference .internal}). The [\\(F_f\\)]{.math .notranslate .nohighlight} and [\\(F_r\\)]{.math .notranslate .nohighlight} terms are added by this fix on a per-particle basis.

The operation of this fix is exactly like that described by the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} command, except that the thermostatting is also applied to the radial electron velocity for electron particles.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. Because the state of the random number generator is not saved in restart files, this means you cannot do "exact" restarts with this fix, where the simulation continues on the same as if no restart had taken place. However, in a statistical sense, a restarted simulation should produce the same behavior.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* option is supported by this fix. You can use it to assign a temperature [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its thermostatting procedure, as described above. For consistency, the group used by this fix and by the compute should be the same.

The cumulative energy change in the system imposed by this fix is included in the [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} keywords *ecouple* and *econserve*, but only if the *tally* keyword to set to *yes*. See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} page for details.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the same cumulative energy change due to this fix described in the previous paragraph. The scalar value calculated by this fix is "extensive". Note that calculation of this quantity also requires setting the *tally* keyword to *yes*.

This fix can ramp its target temperature over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none

This fix is part of the EFF package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix langevin]{.doc}]fix_langevin.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are scale = 1.0 for all types and tally = no.

------------------------------------------------------------------------

**(Dunweg)** Dunweg and Paul, Int J of Modern Physics C, 2, 817-27 (1991).

**(Schneider)** Schneider and Stoll, Phys Rev B, 17, 1302 (1978).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

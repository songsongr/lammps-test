:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-append-atoms-command .section}
[]{#index-0}

# fix append/atoms command[](#fix-append-atoms-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID append/atoms face ... keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- append/atoms = style name of this fix command

- face = *zhi*

- zero or more keyword/value pairs may be appended

- keyword = *basis* or *size* or *freq* or *temp* or *random* or *units*

  ``` literal-block
  basis values = M itype
    M = which basis atom
    itype = atom type (1-N) to assign to this basis atom
  size args = Lz
    Lz = z size of lattice region appended in a single event(distance units)
  freq args = freq
    freq = the number of timesteps between append events
  temp args = target damp seed extent
    target = target temperature for the region between zhi-extent and zhi (temperature units)
    damp = damping parameter (time units)
    seed = random number seed for langevin kicks
    extent = extent of thermostatted region (distance units)
  random args = xmax ymax zmax seed
    xmax, ymax, zmax = maximum displacement in particular direction (distance units)
    seed = random number seed for random displacement
  units value = lattice or box
    lattice = the wall position is defined in lattice units
    box = the wall position is defined in simulation box units
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all append/atoms zhi size 5.0 freq 295 units lattice
    fix 4 all append/atoms zhi size 15.0 freq 5 units box
    fix A all append/atoms zhi size 1.0 freq 1000 units lattice
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix creates atoms on a lattice, appended on the zhi edge of the system box. This can be useful when a shock or wave is propagating from zlo. This allows the system to grow with time to accommodate an expanding wave. A simulation box must already exist, which is typically created via the [[create_box]{.doc}]create_box.md){.reference .internal} command. Before using this command, a lattice must also be defined using the [[lattice]{.doc}]lattice.md){.reference .internal} command.

This fix will automatically freeze atoms on the zhi edge of the system, so that overlaps are avoided when new atoms are appended.

The *basis* keyword specifies an atom type that will be assigned to specific basis atoms as they are created. See the [[lattice]{.doc}]lattice.md){.reference .internal} command for specifics on how basis atoms are defined for the unit cell of the lattice. By default, all created atoms are assigned type = 1 unless this keyword specifies differently.

The *size* keyword defines the size in [\\(z\\)]{.math .notranslate .nohighlight} of the chunk of material to be added.

The *random* keyword will give the atoms random displacements around their lattice points to simulate some initial temperature.

The *temp* keyword will cause a region to be thermostatted with a Langevin thermostat on the zhi boundary. The size of the region is measured from zhi and is set with the *extent* argument.

The *units* keyword determines the meaning of the distance units used to define a wall position, but only when a numeric constant is used. A *box* value selects standard distance units as defined by the [[units]{.doc}]units.md){.reference .internal} command (e.g., [\\(\\AA\\)]{.math .notranslate .nohighlight} for units = real or metal. A *lattice* value means the distance units are in lattice spacings. The [[lattice]{.doc}]lattice.md){.reference .internal} command must have been previously used to define the lattice spacings.
:::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix style is part of the SHOCK package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The boundary on which atoms are added with append/atoms must be shrink/minimum. The opposite boundary may be any boundary type other than periodic.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix wall/piston]{.doc}]fix_wall_piston.md){.reference .internal} command
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The keyword defaults are size = 0.0, freq = 0, units = lattice. All added atoms are of type 1 unless the basis keyword is used.
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

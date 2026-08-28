::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::: {#fix-alchemy-command .section}
[]{#index-0}

# fix alchemy command[](#fix-alchemy-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID alchemy v_name
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- alchemy = style name of this fix command

- v_name = variable with name that determines the [\\(\\lambda_R\\)]{.math .notranslate .nohighlight} value
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix trans all alchemy v_ramp
:::
::::
:::::

:::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 28Mar2023.]{.versionmodified .added}
:::

This fix command enables an "alchemical transformation" to be performed between two systems, whereby one system slowly transforms into the other over the course of a molecular dynamics run. This is useful for measuring thermodynamic differences between two different systems. It also allows transformations that are not easily possible with the [[pair style hybrid/scaled]{.doc}]pair_hybrid.md){.reference .internal}, [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} or [[fix adapt/fep]{.doc}]fix_adapt_fep.md){.reference .internal} commands.

Example inputs are included in the [`examples/PACKAGES/alchemy`{.docutils .literal .notranslate}]{.pre} directory for (a) transforming a pure copper system into a copper/aluminum bronze alloy and (b) transforming two water molecules in a box of water into a hydronium and a hydroxyl ion.

The two systems must be defined as [[separate replica]{.doc}]Howto_replica.md){.reference .internal} and run in separate partitions of processors using the [[-partition]{.doc}]Run_options.md){.reference .internal} command-line switch. Exactly two partitions must be specified, and each partition must use the same number of processors and the same domain decomposition.

Because the forces applied to the atoms are the same mix of the forces from each partition and the simulation starts with the same atom positions across both partitions, they will generate the same trajectory of coordinates for each atom, and the same simulation box size and shape. The latter two conditions are *enforced* by this fix; it exchanges coordinates and box information between the replicas. This is not strictly required, but since MD simulations are an example of a chaotic system, even the tiniest random difference will eventually grow exponentially into an unwanted divergence.

Otherwise, the properties of each atom (type, charge, bond and angle partners, etc.), as well as energy and forces between interacting atoms (pair, bond, angle styles, etc.) can be different in the two systems.

This can be initialized in the same input script by using commands which only apply to one or the other replica. The example scripts use a world-style [[variable]{.doc}]variable.md){.reference .internal} command along with [[if/then/else]{.doc}]if.md){.reference .internal} commands for this purpose. The [[partition]{.doc}]partition.md){.reference .internal} command can also be used.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    create_box 2 box
    create_atoms 1 box
    pair_style eam/alloy
    pair_coeff * * AlCu.eam.alloy Cu Al

    # replace 5% of copper with aluminum on the second partition only

    variable name world pure alloy
    if "${name} == alloy" then &
      "set type 1 type/fraction 2 0.05 6745234"
:::
::::

Both replicas must define an instance of this fix, but with a different *v_name* variable. The named variable must be an equal-style or equivalent [[variable]{.doc}]variable.md){.reference .internal}. The two variables should be defined so that one ramps *down* from 1.0 to 0.0 for the *first* replica (*R=0*) and the other ramps *up* from 0.0 to 1.0 for the *second* replica (*R=1*). A simple way is to do this is linearly, which can be done using the ramp() function of the [[variable]{.doc}]variable.md){.reference .internal} command. You could also define a variable which returns a value between 0.0 and 1.0 as a non-linear function of the timestep. Here is a linear example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    partition yes 1 variable ramp equal ramp(1.0,0.0)
    partition yes 2 variable ramp equal ramp(0.0,1.0)
    fix 2 all alchemy v_ramp
:::
::::

::: {.admonition .note}
Note

For an alchemical transformation, the two variables should sum to exactly 1.0 at any timestep. LAMMPS does *NOT* check that this is the case.
:::

If you use the [`ramp()`{.docutils .literal .notranslate}]{.pre} function to define the two variables, this fix can easily be used across successive runs in the same input script by ensuring each instance of the [[run]{.doc}]run.md){.reference .internal} command specifies the appropriate *start* or *stop* options.

At each timestep of an MD run, the two instances of this fix evaluate their respective variables as a [\\(\\lambda_R\\)]{.math .notranslate .nohighlight} factor, where *R* = 0 or 1 for each replica. The forces used by each system for the propagation of their atoms is set to the sum of the forces for the two systems, each scaled by their respective [\\(\\lambda_R\\)]{.math .notranslate .nohighlight} factor. Thus, during the MD run, the system will transform incrementally from the first system to the second system.

::: {.admonition .note}
Note

As mentioned above, the coordinates of the atoms and box size/shape must be exactly the same in the two replicas. Therefore, it is generally not a good idea to initialize the two replicas by reading different data files or creating them individually from scratch. Rather, a single system should be initialized and then desired modifications applied to the system to either replica. If your input script somehow induces the two systems to become different (e.g. by performing [[atom_modify sort]{.doc}]atom_modify.md){.reference .internal} differently, or by adding or depositing a different number of atoms), then LAMMPS will detect the mismatch and generate an error. This is done by ensuring that each step the number and ordering of atoms is identical within each pair of processors in the two replicas.
:::
::::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix stores a global scalar (the current value of [\\(\\lambda_R\\)]{.math .notranslate .nohighlight}) and a global vector of length 3 which contains the potential energy of the first partition, the second partition and the combined value, respectively. The global scalar is unitless and "intensive", the vector is in [[energy units]{.doc}]units.md){.reference .internal} and "extensive". These values can be used by any command that uses a global value from a fix as input. See the [[output howto]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the REPLICA package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

There may be only one instance of this fix in use at a time within each replica.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute pressure/alchemy]{.doc}]compute_pressure_alchemy.md){.reference .internal} command, [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command, [[fix adapt/fep]{.doc}]fix_adapt_fep.md){.reference .internal} command, [[pair_style hybrid/scaled]{.doc}]pair_hybrid.md){.reference .internal} command.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

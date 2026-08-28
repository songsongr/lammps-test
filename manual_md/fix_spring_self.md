::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-spring-self-command .section}
[]{#index-1}[]{#index-0}

# fix spring/self command[](#fix-spring-self-command "Link to this heading"){.headerlink}

Accelerator Variant: *spring/self/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID spring/self K dir
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- spring/self = style name of this fix command

- K = spring constant (force/distance units), can be a variable (see below)

- dir = xyz, xy, xz, yz, x, y, or z (optional, default: xyz)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix tether boundary-atoms spring/self 10.0
    fix var all spring/self v_kvar
    fix zrest  move spring/self 10.0 z
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply a spring force independently to each atom in the group to tether it to its initial position. The initial position for each atom is its location at the time the fix command was issued. At each timestep, the magnitude of the force on each atom is -Kr, where r is the displacement of the atom from its current position to its initial position. The distance r correctly takes into account any crossings of periodic boundary by the atom since it was in its initial position.

With the (optional) dir flag, one can select in which direction the spring force is applied. By default, the restraint is applied in all directions, but it can be limited to the xy-, xz-, yz-plane and the x-, y-, or z-direction, thus restraining the atoms to a line or a plane, respectively.

The force constant *k* can be specified as an equal-style or atom-style [[variable]{.doc}]variable.md){.reference .internal}. If the value is a variable, it should be specified as v_name, where name is the variable name. In this case, the variable will be evaluated each time step, and its value(s) will be used as force constant for the spring force.

Equal-style variables can specify formulas with various mathematical functions and include [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command keywords for the simulation box parameters, time step, and elapsed time. Thus, it is easy to specify a time-dependent force field.

Atom-style variables can specify the same formulas as equal-style variables but can also include per-atom values, such as atom coordinates. Thus, it is easy to specify a spatially-dependent force field with optional time-dependence as well.
:::

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the original coordinates of tethered atoms to [[binary restart files]{.doc}]restart.md){.reference .internal}, so that the spring effect will be the same in a restarted simulation. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the energy stored in the per-atom springs to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is adding its forces. Default is the outermost level.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is an energy which is the sum of the spring energy for each atom, where the per-atom energy is 0.5 \* K \* r\^2. The scalar value calculated by this fix is "extensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The forces due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command.

::: {.admonition .note}
Note

If you want the per-atom spring energy to be included in the total potential energy of the system (the quantity being minimized), you MUST enable the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for this fix.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The KOKKOS version, *fix spring/self/kk* may only be used with a constant value of K, not a variable.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix drag]{.doc}]fix_drag.md){.reference .internal}, [[fix spring]{.doc}]fix_spring.md){.reference .internal}, [[fix smd]{.doc}]fix_smd.md){.reference .internal}, [[fix spring/rg]{.doc}]fix_spring_rg.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

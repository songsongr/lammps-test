::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-smd-command .section}
[]{#index-0}

# fix smd command[](#fix-smd-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID smd type values keyword values
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- smd = style name of this fix command

- mode = *cvel* or *cfor* to select constant velocity or constant force SMD

  ``` literal-block
  cvel values = K vel
    K = spring constant (force/distance units)
    vel = velocity of pulling (distance/time units)
  cfor values = force
    force = pulling force (force units)
  ```

- keyword = *tether* or *couple*

  ``` literal-block
  tether values = x y z R0
    x,y,z = point to which spring is tethered
    R0 = distance of end of spring from tether point (distance units)
  couple values = group-ID2 x y z R0
    group-ID2 = 2nd group to couple to fix group with a spring
    x,y,z = direction of spring, automatically computed with 'auto'
    R0 = distance of end of spring (distance units)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix  pull    cterm smd cvel 20.0 -0.00005 tether NULL NULL 100.0 0.0
    fix  pull    cterm smd cvel 20.0 -0.0001 tether 25.0 25 25.0 0.0
    fix  stretch cterm smd cvel 20.0  0.0001 couple nterm auto auto auto 0.0
    fix  pull    cterm smd cfor  5.0 tether 25.0 25.0 25.0 0.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: {.warning .admonition}
Fix smd is unmaintained

Please note that *fix smd* is unmaintained and has multiple known issues. We recommend to use the equivalent functionality in either [[fix colvars]{.doc}]fix_colvars.md){.reference .internal} or [[fix plumed]{.doc}]fix_plumed.md){.reference .internal} instead, which are both actively maintained.
:::

This fix implements several options of steered MD (SMD) as reviewed in [[(Izrailev)]{.std .std-ref}](#izrailev){.reference .internal}, which allows to induce conformational changes in systems and to compute the potential of mean force (PMF) along the assumed reaction coordinate [[(Park)]{.std .std-ref}](#park){.reference .internal} based on Jarzynski's equality [[(Jarzynski)]{.std .std-ref}](#jarzynski){.reference .internal}. This fix borrows a lot from [[fix spring]{.doc}]fix_spring.md){.reference .internal} and [[fix setforce]{.doc}]fix_setforce.md){.reference .internal}.

You can apply a moving spring force to a group of atoms (*tether* style) or between two groups of atoms (*couple* style). The spring can then be used in either constant velocity (*cvel*) mode or in constant force (*cfor*) mode to induce transitions in your systems. When running in *tether* style, you may need some way to fix some other part of the system (e.g. via [[fix spring/self]{.doc}]fix_spring_self.md){.reference .internal})

The *tether* style attaches a spring between a point at a distance of R0 away from a fixed point *x,y,z* and the center of mass of the fix group of atoms. A restoring force of magnitude K (R - R0) Mi / M is applied to each atom in the group where *K* is the spring constant, Mi is the mass of the atom, and M is the total mass of all atoms in the group. Note that *K* thus represents the total force on the group of atoms, not a per-atom force.

In *cvel* mode the distance R is incremented or decremented monotonously according to the pulling (or pushing) velocity. In *cfor* mode a constant force is added and the actual distance in direction of the spring is recorded.

The *couple* style links two groups of atoms together. The first group is the fix group; the second is specified by group-ID2. The groups are coupled together by a spring that is at equilibrium when the two groups are displaced by a vector in direction *x,y,z* with respect to each other and at a distance R0 from that displacement. Note that *x,y,z* only provides a direction and will be internally normalized. But since it represents the *absolute* displacement of group-ID2 relative to the fix group, (1,1,0) is a different spring than (-1,-1,0). For each vector component, the displacement can be described with the *auto* parameter. In this case the direction is re-computed in every step, which can be useful for steering a local process where the whole object undergoes some other change. When the relative positions and distance between the two groups are not in equilibrium, the same spring force described above is applied to atoms in each of the two groups.

For both the *tether* and *couple* styles, any of the x,y,z values can be specified as NULL which means do not include that dimension in the distance calculation or force application.

For constant velocity pulling (*cvel* mode), the running integral over the pulling force in direction of the spring is recorded and can then later be used to compute the potential of mean force (PMF) by averaging over multiple independent trajectories along the same pulling path.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

The fix stores the direction of the spring, current pulling target distance and the running PMF to [[binary restart files]{.doc}]restart.md){.reference .internal}. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the operation of the fix continues in an uninterrupted fashion.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *virial* option is supported by this fix to add the contribution due to the added forces on atoms to both the global pressure and per-atom stress of the system via the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} and [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} commands. The former can be accessed by [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify virial no]{.doc}]fix_modify.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is adding its forces. Default is the outermost level.

This fix computes a vector list of 7 quantities, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The quantities in the vector are in this order: the x-, y-, and z-component of the pulling force, the total force in direction of the pull, the equilibrium distance of the spring, the distance between the two reference points, and finally the accumulated PMF (the sum of pulling forces times displacement).

The force is the total force on the group of atoms by the spring. In the case of the *couple* style, it is the force on the fix group (group-ID) or the negative of the force on the second group (group-ID2). The vector values calculated by this fix are "extensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix drag]{.doc}]fix_drag.md){.reference .internal}, [[fix spring]{.doc}]fix_spring.md){.reference .internal}, [[fix spring/self]{.doc}]fix_spring_self.md){.reference .internal}, [[fix spring/rg]{.doc}]fix_spring_rg.md){.reference .internal}, [[fix colvars]{.doc}]fix_colvars.md){.reference .internal}, [[fix plumed]{.doc}]fix_plumed.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Izrailev)** Izrailev, Stepaniants, Isralewitz, Kosztin, Lu, Molnar, Wriggers, Schulten. Computational Molecular Dynamics: Challenges, Methods, Ideas, volume 4 of Lecture Notes in Computational Science and Engineering, pp. 39-65. Springer-Verlag, Berlin, 1998.

**(Park)** Park, Schulten, J. Chem. Phys. 120 (13), 5946 (2004)

**(Jarzynski)** Jarzynski, Phys. Rev. Lett. 78, 2690 (1997)
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

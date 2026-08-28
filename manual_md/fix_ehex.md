:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#fix-ehex-command .section}
[]{#index-0}

# fix ehex command[](#fix-ehex-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID ehex nevery F keyword value
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- ehex = style name of this fix command

- nevery = add/subtract heat every this many timesteps

- F = energy flux into the reservoir (energy/time units)

- zero or more keyword/value pairs may be appended to args

- keyword = *region* or *constrain* or *com* or *hex*

  ``` literal-block
  region value = region-ID
    region-ID = ID of region (reservoir) atoms must be in for added thermostatting force
  constrain value = none
    apply the constraint algorithm (SHAKE or RATTLE) again at the end of the timestep
  com value = none
    rescale all sites of a constrained cluster of atom if its COM is in the reservoir
  hex value = none
    omit the coordinate correction to recover the HEX algorithm
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # Lennard-Jones, from examples/in.ehex.lj

    fix fnve all nve
    # specify regions rhot and rcold
    ...
    fix fhot all ehex 1 0.15 region rhot
    fix fcold all ehex 1 -0.15 region rcold

    # SPC/E water, from examples/in.ehex.spce
    fix fnve all nve
    # specify regions rhot and rcold
    ...
    fix fhot all ehex 1 0.075 region rhot constrain com
    fix fcold all ehex 1 -0.075 region rcold constrain com
    fix frattle all rattle 1e-10 400 0 b 1 a 1
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix implements the asymmetric version of the enhanced heat exchange algorithm [[(Wirnsberger)]{.std .std-ref}](#wirnsberger){.reference .internal}. The eHEX algorithm is an extension of the heat exchange algorithm [[(Ikeshoji)]{.std .std-ref}](#ikeshoji){.reference .internal} and adds an additional coordinate integration to account for higher-order truncation terms in the operator splitting. The original HEX algorithm (implemented as [[fix heat]{.doc}]fix_heat.md){.reference .internal}) is known to exhibit a slight energy drift limiting the accessible simulation times to a few nanoseconds. This issue is greatly improved by the new algorithm decreasing the energy drift by at least a factor of a hundred (LJ and SPC/E water) with little computational overhead.

In both algorithms (non-translational) kinetic energy is constantly swapped between regions (reservoirs) to impose a heat flux onto the system. The equations of motion are therefore modified if a particle [\\(i\\)]{.math .notranslate .nohighlight} is located inside a reservoir [\\(\\Gamma_k\\)]{.math .notranslate .nohighlight} where [\\(k\>0\\)]{.math .notranslate .nohighlight}. We use [\\(\\Gamma_0\\)]{.math .notranslate .nohighlight} to label those parts of the simulation box which are not thermostatted.) The input parameter *region-ID* of this fix corresponds to [\\(k\\)]{.math .notranslate .nohighlight}. The energy swap is modelled by introducing an additional thermostatting force to the equations of motion, such that the time evolution of coordinates and momenta of particle [\\(i\\)]{.math .notranslate .nohighlight} becomes [[(Wirnsberger)]{.std .std-ref}](#wirnsberger){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\dot{\\mathbf r}\_i &= \\mathbf v_i, \\\\ \\dot{\\mathbf v}\_i &= \\frac{\\mathbf f_i}{m_i} + \\frac{\\mathbf g_i}{m_i}.\\end{split}\\\]
:::

The thermostatting force is given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathbf g_i = \\begin{cases} \\frac{m_i}{2} \\frac{ F\_{\\Gamma\_{k(\\mathbf r_i)}}}{ K\_{\\Gamma\_{k(\\mathbf r_i)}}} \\left(\\mathbf v_i - \\mathbf v\_{\\Gamma\_{k(\\mathbf r_i)}} \\right) & \\mbox{\$k(\\mathbf r_i)\> 0\$ (inside a reservoir),} \\\\ 0 & \\mbox{otherwise, } \\end{cases}\\end{split}\\\]
:::

where [\\(m_i\\)]{.math .notranslate .nohighlight} is the mass and [\\(k(\\mathbf r_i)\\)]{.math .notranslate .nohighlight} maps the particle position to the respective reservoir. The quantity [\\(F\_{\\Gamma\_{k(\\mathbf r_i)}}\\)]{.math .notranslate .nohighlight} corresponds to the input parameter *F*, which is the energy flux into the reservoir. Furthermore, [\\(K\_{\\Gamma\_{k(\\mathbf r_i)}}\\)]{.math .notranslate .nohighlight} and [\\(v\_{\\Gamma\_{k(\\mathbf r_i)}}\\)]{.math .notranslate .nohighlight} denote the non-translational kinetic energy and the center of mass velocity of that reservoir. The thermostatting force does not affect the center of mass velocities of the individual reservoirs and the entire simulation box. A derivation of the equations and details on the numerical implementation with velocity Verlet in LAMMPS can be found in reference "(Wirnsberger)"#\_Wirnsberger.

::: {.admonition .note}
Note

This fix only integrates the thermostatting force and must be combined with another integrator, such as [[fix nve]{.doc}]fix_nve.md){.reference .internal}, to solve the full equations of motion.
:::

This fix is different from a thermostat such as [[fix nvt]{.doc}]fix_nh.md){.reference .internal} or [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal} in that energy is added/subtracted continually. Thus if there is no other mechanism in place to counterbalance this effect, the entire system will heat or cool continuously.

::: {.admonition .note}
Note

If heat is subtracted from the system too aggressively so that the group's kinetic energy would go to zero, then LAMMPS will halt with an error message. Increasing the value of *nevery* means that heat is added/subtracted less frequently but in larger portions. The resulting temperature profile will therefore be the same.
:::

This fix will default to [[fix_heat]{.doc}]fix_heat.md){.reference .internal} (HEX algorithm) if the keyword *hex* is specified.

------------------------------------------------------------------------

**Compatibility with SHAKE and RATTLE (rigid molecules)**:

This fix is compatible with [[fix shake]{.doc}]fix_shake.md){.reference .internal} and [[fix rattle]{.doc}]fix_shake.md){.reference .internal}. If either of these constraining algorithms is specified in the input script and the keyword *constrain* is set, the bond distances will be corrected a second time at the end of the integration step. It is recommended to specify the keyword *com* in addition to the keyword *constrain*. With this option all sites of a constrained cluster are rescaled, if its center of mass is located inside the region. Rescaling all sites of a cluster by the same factor does not introduce any velocity components along fixed bonds. No rescaling takes place if the center of mass lies outside the region.

::: {.admonition .note}
Note

You can only use the keyword *com* along with *constrain*.
:::

To achieve the highest accuracy it is recommended to use [[fix rattle]{.doc}]fix_shake.md){.reference .internal} with the keywords *constrain* and *com* as shown in the second example. Only if RATTLE is employed, the velocity constraints will be satisfied.

::: {.admonition .note}
Note

Even if RATTLE is used and the keywords *com* and *constrain* are both set, the coordinate constraints will not necessarily be satisfied up to the target precision. The velocity constraints are satisfied as long as all sites of a cluster are rescaled (keyword *com*) and the cluster does not span adjacent reservoirs. The current implementation of the eHEX algorithm introduces a small error in the bond distances, which goes to zero with order three in the timestep. For example, in a simulation of SPC/E water with a timestep of 2 fs the maximum relative error in the bond distances was found to be on the order of [\\(10\^{-7}\\)]{.math .notranslate .nohighlight} for relatively large temperature gradients. A higher precision can be achieved by decreasing the timestep.
:::
:::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the RIGID package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix heat]{.doc}]fix_heat.md){.reference .internal}, [[fix thermal/conductivity]{.doc}]fix_thermal_conductivity.md){.reference .internal}, [[compute temp]{.doc}]compute_temp.md){.reference .internal}, [[compute temp/region]{.doc}]compute_temp_region.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Ikeshoji)** Ikeshoji and Hafskjold, Molecular Physics, 81, 251-261 (1994).

**(Wirnsberger)** Wirnsberger, Frenkel, and Dellago, J Chem Phys, 143, 124104 (2015).
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#fix-drude-transform-direct-command .section}
[]{#index-1}[]{#index-0}

# fix drude/transform/direct command[](#fix-drude-transform-direct-command "Link to this heading"){.headerlink}
:::

:::::::::::::::::::::::::::::::: {#fix-drude-transform-inverse-command .section}
# fix drude/transform/inverse command[](#fix-drude-transform-inverse-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID style keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- style = *drude/transform/direct* or *drude/transform/inverse*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 3 all drude/transform/direct
    fix 1 all drude/transform/inverse
:::
::::

Example input scripts available: examples/PACKAGES/drude
:::::

::::::::::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Transform the coordinates of Drude oscillators from real to reduced and back for thermalizing the Drude oscillators as described in [[(Lamoureux)]{.std .std-ref}](#lamoureux1){.reference .internal} using a Nose-Hoover thermostat. This fix is designed to be used with the [[thermalized Drude oscillator model]{.doc}]Howto_drude.md){.reference .internal}. Polarizable models in LAMMPS are described on the [[Howto polarizable]{.doc}]Howto_polarizable.md){.reference .internal} doc page.

Drude oscillators are a pair of atoms representing a single polarizable atom. Ideally, the mass of Drude particles would vanish and their positions would be determined self-consistently by iterative minimization of the energy, the cores' positions being fixed. It is however more efficient and it yields comparable results, if the Drude oscillators (the motion of the Drude particle relative to the core) are thermalized at a low temperature. In that case, the Drude particles need a small mass.

The thermostats act on the reduced degrees of freedom, which are defined by the following equations. Note that in these equations upper case denotes atomic or center of mass values and lower case denotes Drude particle or dipole values. Primes denote the transformed (reduced) values, while bare letters denote the original values.

Masses:

::: {.math .notranslate .nohighlight}
\\\[M\' = M + m\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[m\' = \\frac {M\\, m } {M\'}\\\]
:::

Positions:

::: {.math .notranslate .nohighlight}
\\\[X\' = \\frac {M\\, X + m\\, x} {M\'}\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[x\' = x - X\\\]
:::

Velocities:

::: {.math .notranslate .nohighlight}
\\\[V\' = \\frac {M\\, V + m\\, v} {M\'}\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[v\' = v - V\\\]
:::

Forces:

::: {.math .notranslate .nohighlight}
\\\[F\' = F + f\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[f\' = \\frac { M\\, f - m\\, F} {M\'}\\\]
:::

This transform conserves the total kinetic energy

::: {.math .notranslate .nohighlight}
\\\[ \\frac 1 2 \\, (M\\, V\^2\\ + m\\, v\^2) = \\frac 1 2 \\, (M\'\\, V\'\^2\\ + m\'\\, v\'\^2)\\\]
:::

and the virial defined with absolute positions

::: {.math .notranslate .nohighlight}
\\\[X\\, F + x\\, f = X\'\\, F\' + x\'\\, f\'\\\]
:::

------------------------------------------------------------------------

This fix requires each atom know whether it is a Drude particle or not. You must therefore use the [[fix drude]{.doc}]fix_drude.md){.reference .internal} command to specify the Drude status of each atom type.

::: {.admonition .note}
Note

only the Drude core atoms need to be in the group specified for this fix. A Drude electron will be transformed together with its core even if it is not itself in the group. It is safe to include Drude electrons or non-polarizable atoms in the group. The non-polarizable atoms will simply not be transformed.
:::

------------------------------------------------------------------------

This fix does NOT perform time integration. It only transform masses, coordinates, velocities and forces. Thus you must use separate time integration fixes, like [[fix nve]{.doc}]fix_nve.md){.reference .internal} or [[fix npt]{.doc}]fix_nh.md){.reference .internal} to actually update the velocities and positions of atoms. In order to thermalize the reduced degrees of freedom at different temperatures, two Nose-Hoover thermostats must be defined, acting on two distinct groups.

::: {.admonition .note}
Note

The *fix drude/transform/direct* command must appear before any Nose-Hoover thermostatting fixes. The *fix drude/transform/inverse* command must appear after any Nose-Hoover thermostatting fixes.
:::

Example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix fDIRECT all drude/transform/direct
    fix fNVT gCORES nvt temp 300.0 300.0 100
    fix fNVT gDRUDES nvt temp 1.0 1.0 100
    fix fINVERSE all drude/transform/inverse
    compute TDRUDE all temp/drude
    thermo_style custom step cpu etotal ke pe ebond ecoul elong press vol temp c_TDRUDE[1] c_TDRUDE[2]
:::
::::

In this example, *gCORES* is the group of the atom cores and *gDRUDES* is the group of the Drude particles (electrons). The centers of mass of the Drude oscillators will be thermostatted at 300.0 and the internal degrees of freedom will be thermostatted at 1.0. The temperatures of cores and Drude particles, in center-of-mass and relative coordinates, are calculated using [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal}

In addition, if you want to use a barostat to simulate a system at constant pressure, only one of the Nose-Hoover fixes must be *npt*, the other one should be *nvt*. You must add a *compute temp/com* and a *fix_modify* command so that the temperature of the *npt* fix be just that of its group (the Drude cores) but the pressure be the overall pressure *thermo_press*.

Example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute cTEMP_CORE gCORES temp/com
    fix fDIRECT all drude/transform/direct
    fix fNPT gCORES npt temp 298.0 298.0 100 iso 1.0 1.0 500
    fix_modify fNPT temp cTEMP_CORE press thermo_press
    fix fNVT gDRUDES nvt temp 5.0 5.0 100
    fix fINVERSE all drude/transform/inverse
:::
::::

In this example, *gCORES* is the group of the atom cores and *gDRUDES* is the group of the Drude particles. The centers of mass of the Drude oscillators will be thermostatted at 298.0 and the internal degrees of freedom will be thermostatted at 5.0. The whole system will be barostatted at 1.0.

In order to avoid the flying ice cube problem (irreversible transfer of linear momentum to the center of mass of the system), you may need to add a *fix momentum* command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix fMOMENTUM all momentum 100 linear 1 1 1
:::
::::
:::::::::::::::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix drude]{.doc}]fix_drude.md){.reference .internal}, [[fix langevin/drude]{.doc}]fix_langevin_drude.md){.reference .internal}, [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal}, [[pair_style thole]{.doc}]pair_thole.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Lamoureux)** Lamoureux and Roux, J Chem Phys, 119, 3025-3039 (2003).
:::
::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::

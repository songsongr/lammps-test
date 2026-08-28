:::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::: {#fix-restrain-command .section}
[]{#index-0}

# fix restrain command[](#fix-restrain-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID restrain keyword args ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- restrain = style name of this fix command

- one or more keyword/arg pairs may be appended

- keyword = *bond* or *lbound* or *angle* or *dihedral*

  ``` literal-block
  bond args = atom1 atom2 Kstart Kstop r0start (r0stop)
    atom1,atom2 = IDs of two atoms in bond
    Kstart,Kstop = restraint coefficients at start/end of run (energy units)
    r0start = equilibrium bond distance at start of run (distance units)
    r0stop = equilibrium bond distance at end of run (optional) (distance units). If not
      specified it is assumed to be equal to r0start
  lbound args = atom1 atom2 Kstart Kstop r0start (r0stop)
    atom1,atom2 = IDs of two atoms in bond
    Kstart,Kstop = restraint coefficients at start/end of run (energy units)
    r0start = equilibrium bond distance at start of run (distance units)
    r0stop = equilibrium bond distance at end of run (optional) (distance units). If not
      specified it is assumed to be equal to r0start
  angle args = atom1 atom2 atom3 Kstart Kstop theta0
    atom1,atom2,atom3 = IDs of three atoms in angle, atom2 = middle atom
    Kstart,Kstop = restraint coefficients at start/end of run (energy units)
    theta0 = equilibrium angle theta (degrees)
  dihedral args = atom1 atom2 atom3 atom4 Kstart Kstop phi0 keyword/value
    atom1,atom2,atom3,atom4 = IDs of 4 atoms in dihedral in linear order
    Kstart,Kstop = restraint coefficients at start/end of run (energy units)
    phi0 = equilibrium dihedral angle phi (degrees)
    keyword/value = optional keyword value pairs. supported keyword/value pairs:
      mult n = dihedral multiplicity n (integer >= 0, default = 1)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix holdem all restrain bond 45 48 2000.0 2000.0 2.75
    fix holdem all restrain lbound 45 48 2000.0 2000.0 2.75
    fix holdem all restrain dihedral 1 2 3 4 2000.0 2000.0 120.0
    fix holdem all restrain bond 45 48 2000.0 2000.0 2.75 dihedral 1 2 3 4 2000.0 2000.0 120.0
    fix texas_holdem all restrain dihedral 1 2 3 4 0.0 2000.0 120.0 dihedral 1 2 3 5 0.0 2000.0 -120.0 dihedral 1 2 3 6 0.0 2000.0 0.0
:::
::::
:::::

:::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Restrain the motion of the specified sets of atoms by making them part of a bond or angle or dihedral interaction whose strength can vary over time during a simulation. This is functionally similar to creating a bond or angle or dihedral for the same atoms in a data file, as specified by the [[read_data]{.doc}]read_data.md){.reference .internal} command, albeit with a time-varying prefactor coefficient, and except for exclusion rules, as explained below.

For the purpose of force field parameter-fitting or mapping a molecular potential energy surface, this fix reduces the hassle and risk associated with modifying data files. In other words, use this fix to temporarily force a molecule to adopt a particular conformation. To create a permanent bond or angle or dihedral, you should modify the data file.

::: {.admonition .note}
Note

Adding a bond/angle/dihedral with this command does not apply the exclusion rules and weighting factors specified by the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command to atoms in the restraint that are now bonded (1-2,1-3,1-4 neighbors) as a result. If they are close enough to interact in a [[pair_style]{.doc}]pair_style.md){.reference .internal} sense (non-bonded interaction), then the bond/angle/dihedral restraint interaction will simply be superposed on top of that interaction.
:::

The group-ID specified by this fix is ignored.

The second example above applies a restraint to hold the dihedral angle formed by atoms 1, 2, 3, and 4 near 120 degrees using a constant restraint coefficient. The fourth example applies similar restraints to multiple dihedral angles using a restraint coefficient that increases from 0.0 to 2000.0 over the course of the run.

::: {.admonition .note}
Note

Adding a force to atoms implies a change in their potential energy as they move due to the applied force field. For dynamics via the [[run]{.doc}]run.md){.reference .internal} command, this energy can be added to the system's potential energy for thermodynamic output (see below). For energy minimization via the [[minimize]{.doc}]minimize.md){.reference .internal} command, this energy must be added to the system's potential energy to formulate a self-consistent minimization problem (see below).
:::

In order for a restraint to be effective, the restraint force must typically be significantly larger than the forces associated with conventional force field terms. If the restraint is applied during a dynamics run (as opposed to during an energy minimization), a large restraint coefficient can significantly reduce the stable timestep size, especially if the atoms are initially far from the preferred conformation. You may need to experiment to determine what value of [\\(K\\)]{.math .notranslate .nohighlight} works best for a given application.

For the case of finding a minimum energy structure for a single molecule with particular restraints (e.g. for fitting force field parameters or constructing a potential energy surface), commands such as the following may be useful:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # minimize molecule energy with restraints
    velocity all create 600.0 8675309 mom yes rot yes dist gaussian
    fix NVE all nve
    fix TFIX all langevin 600.0 0.0 100 24601
    fix REST all restrain dihedral 2 1 3 8 0.0 5000.0 ${angle1} dihedral 3 1 2 9 0.0 5000.0 ${angle2}
    fix_modify REST energy yes
    run 10000
    fix TFIX all langevin 0.0 0.0 100 24601
    fix REST all restrain dihedral 2 1 3 8 5000.0 5000.0 ${angle1} dihedral 3 1 2 9 5000.0 5000.0 ${angle2}
    fix_modify REST energy yes
    run 10000
    # sanity check for convergence
    minimize 1e-6 1e-9 1000 100000
    # report unrestrained energies
    unfix REST
    run 0
:::
::::

------------------------------------------------------------------------

The *bond* keyword applies a bond restraint to the specified atoms using the same functional form used by the [[bond_style harmonic]{.doc}]bond_harmonic.md){.reference .internal} command. The potential associated with the restraint is

::: {.math .notranslate .nohighlight}
\\\[E = K (r - r_0)\^2\\\]
:::

with the following coefficients:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)

[\\(K\\)]{.math .notranslate .nohighlight} and [\\(r_0\\)]{.math .notranslate .nohighlight} are specified with the fix. Note that the usual 1/2 factor is included in [\\(K\\)]{.math .notranslate .nohighlight}.

------------------------------------------------------------------------

The *lbound* keyword applies a lower bound bond restraint to the specified atoms using the same functional form used by the [[bond_style harmonic]{.doc}]bond_harmonic.md){.reference .internal} command if the distance between the atoms is smaller than the equilibrium bond distance and 0 otherwise. The potential associated with the restraint is

::: {.math .notranslate .nohighlight}
\\\[E = K (r - r_0)\^2 ,if\\;r \< r_0\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[E = 0 \\qquad\\quad\\quad ,if\\;r \\ge r_0\\\]
:::

with the following coefficients:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)

[\\(K\\)]{.math .notranslate .nohighlight} and [\\(r_0\\)]{.math .notranslate .nohighlight} are specified with the fix. Note that the usual 1/2 factor is included in [\\(K\\)]{.math .notranslate .nohighlight}.

------------------------------------------------------------------------

The *angle* keyword applies an angle restraint to the specified atoms using the same functional form used by the [[angle_style harmonic]{.doc}]angle_harmonic.md){.reference .internal} command. The potential associated with the restraint is

::: {.math .notranslate .nohighlight}
\\\[E = K (\\theta - \\theta_0)\^2\\\]
:::

with the following coefficients:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\theta_0\\)]{.math .notranslate .nohighlight} (degrees)

[\\(K\\)]{.math .notranslate .nohighlight} and [\\(\\theta_0\\)]{.math .notranslate .nohighlight} are specified with the fix. [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence [\\(K\\)]{.math .notranslate .nohighlight} is effectively energy per radian\^2. Note that the usual 1/2 factor is included in [\\(K\\)]{.math .notranslate .nohighlight}.

------------------------------------------------------------------------

The *dihedral* keyword applies a dihedral restraint to the specified atoms using a simplified form of the function used by the [[dihedral_style charmm]{.doc}]dihedral_charmm.md){.reference .internal} command. The potential associated with the restraint is

::: {.math .notranslate .nohighlight}
\\\[E = K \[ 1 + \\cos (n \\phi - d) \]\\\]
:::

with the following coefficients:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy)

- [\\(n\\)]{.math .notranslate .nohighlight} (multiplicity, \>= 0)

- [\\(d\\)]{.math .notranslate .nohighlight} (degrees) = [\\(\\phi_0 + 180\\)]{.math .notranslate .nohighlight}

[\\(K\\)]{.math .notranslate .nohighlight} and [\\(\\phi_0\\)]{.math .notranslate .nohighlight} are specified with the fix. Note that the value of the dihedral multiplicity [\\(n\\)]{.math .notranslate .nohighlight} is set by default to 1. You can use the optional *mult* keyword to set it to a different positive integer. Also note that the energy will be a minimum when the current dihedral angle [\\(\\phi\\)]{.math .notranslate .nohighlight} is equal to [\\(\\phi_0\\)]{.math .notranslate .nohighlight}.
::::::::::::

------------------------------------------------------------------------

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the potential energy associated with this fix to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} The default setting for this fix is [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is adding its forces. Default is the outermost level.

::: {.admonition .note}
Note

If you want the fictitious potential energy associated with the added forces to be included in the total potential energy of the system (the quantity being minimized), you MUST enable the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for this fix.
:::

This fix computes a global scalar and a global vector of length 3, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the total potential energy for *all* the restraints as discussed above. The vector values are the sum of contributions to the following individual categories:

> ::: {}
> 1.  bond energy
>
> 2.  angle energy
>
> 3.  dihedral energy
> :::

The scalar and vector values calculated by this fix are "extensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::::::::
:::::::::::::::::::::::::
::::::::::::::::::::::::::

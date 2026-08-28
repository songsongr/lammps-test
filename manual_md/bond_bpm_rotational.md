::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::: {#bond-style-bpm-rotational-command .section}
[]{#index-0}

# bond_style bpm/rotational command[](#bond-style-bpm-rotational-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style bpm/rotational keyword value attribute1 attribute2 ...
:::
::::

- optional keyword = *overlay/pair* or *store/local* or *smooth* or *break*

  ``` literal-block
  store/local values = fix_ID N attributes ...
     * fix_ID = ID of associated internal fix to store data
     * N = prepare data for output every this many timesteps
     * attributes = zero or more of the below attributes may be appended

       id1, id2 = IDs of two atoms in the bond
       time = the timestep the bond broke
       x, y, z = the center of mass position of the two atoms when the bond broke (distance units)
       x/ref, y/ref, z/ref = the initial center of mass position of the two atoms (distance units)

  overlay/pair value = yes or no
     bonded particles will still interact with pair forces

  smooth value = yes or no
     smooths bond forces near the breaking point

  normalize value = yes or no
     normalizes normal and shear forces by the reference length

  break value = yes or no
     indicates whether bonds break during a run
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style bpm/rotational
    bond_coeff 1 1.0 0.2 0.02 0.02 0.20 0.04 0.04 0.04 0.1 0.02 0.002 0.002

    bond_style bpm/rotational store/local myfix 1000 time id1 id2
    dump 1 all local 1000 dump.broken f_myfix[1] f_myfix[2] f_myfix[3]
    dump_modify 1 write_header no
:::
::::
:::::

:::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

The *bpm/rotational* bond style computes forces and torques based on deviations from the initial reference state of the two atoms. The reference state is stored by each bond when it is first computed in the setup of a run. Data is then preserved across run commands and is written to [[binary restart files]{.doc}]restart.md){.reference .internal} such that restarting the system will not reset the reference state of a bond.

Forces include a normal and tangential component. The base normal force has a magnitude of

::: {.math .notranslate .nohighlight}
\\\[f_r = k_r (r - r_0)\\\]
:::

where [\\(k_r\\)]{.math .notranslate .nohighlight} is a stiffness and [\\(r\\)]{.math .notranslate .nohighlight} is the current distance and [\\(r_0\\)]{.math .notranslate .nohighlight} is the initial distance between the two particles.

A tangential force is applied perpendicular to the normal direction which is proportional to the tangential shear displacement with a stiffness of [\\(k_s\\)]{.math .notranslate .nohighlight}. This tangential force also induces a torque. In addition, bending and twisting torques are also applied to particles which are proportional to angular bending and twisting displacements with stiffnesses of [\\(k_b\\)]{.math .notranslate .nohighlight} and [\\(k_t\\)]{.math .notranslate .nohighlight}, respectively. Details on the calculations of shear displacements and angular displacements can be found in [[(Wang)]{.std .std-ref}](#wang2009){.reference .internal} and [[(Wang and Mora)]{.std .std-ref}](#wang2009b){.reference .internal}.

Bonds will break under sufficient stress. A breaking criterion is calculated

::: {.math .notranslate .nohighlight}
\\\[B = \\mathrm{max}\\left\\{0, \\frac{f_r}{f\_{r,c}} + \\frac{\|f_s\|}{f\_{s,c}} + \\frac{\|\\tau_b\|}{\\tau\_{b,c}} + \\frac{\|\\tau_t\|}{\\tau\_{t,c}} \\right\\}\\\]
:::

where [\\(\|f_s\|\\)]{.math .notranslate .nohighlight} is the magnitude of the shear force and [\\(\|\\tau_b\|\\)]{.math .notranslate .nohighlight} and [\\(\|\\tau_t\|\\)]{.math .notranslate .nohighlight} are the magnitudes of the bending and twisting torques, respectively. The corresponding variables [\\(f\_{r,c}\\)]{.math .notranslate .nohighlight} [\\(f\_{s,c}\\)]{.math .notranslate .nohighlight}, [\\(\\tau\_{b,c}\\)]{.math .notranslate .nohighlight}, and [\\(\\tau\_{t,c}\\)]{.math .notranslate .nohighlight} are critical limits to each force or torque. If [\\(B\\)]{.math .notranslate .nohighlight} is ever equal to or exceeds one, the bond will break. This is done by setting the bond type to 0 such that forces and torques are no longer computed.

After computing the base magnitudes of the forces and torques, they can be optionally multiplied by an extra factor [\\(w\\)]{.math .notranslate .nohighlight} to smoothly interpolate forces and torques to zero as the bond breaks. This term is calculated as [\\(w = (1.0 - B\^4)\\)]{.math .notranslate .nohighlight}. This smoothing factor can be added or removed by setting the *smooth* keyword to *yes* or *no*, respectively.

Finally, additional damping forces and torques are applied to the two particles. A force is applied proportional to the difference in the normal velocity of particles using a similar construction as dissipative particle dynamics [[(Groot)]{.std .std-ref}](#groot3){.reference .internal}:

::: {.math .notranslate .nohighlight}
\\\[F_D = - \\gamma_n w (\\hat{r} \\bullet \\vec{v})\\\]
:::

where [\\(\\gamma_n\\)]{.math .notranslate .nohighlight} is the damping strength, [\\(\\hat{r}\\)]{.math .notranslate .nohighlight} is the radial normal vector, and [\\(\\vec{v}\\)]{.math .notranslate .nohighlight} is the velocity difference between the two particles. Similarly, tangential forces are applied to each atom proportional to the relative differences in sliding velocities with a constant prefactor [\\(\\gamma_s\\)]{.math .notranslate .nohighlight} [[(Wang et al.)]{.std .std-ref}](#wang20152){.reference .internal} along with their associated torques. The rolling and twisting components of the relative angular velocities of the two atoms are also damped by applying torques with prefactors of [\\(\\gamma_r\\)]{.math .notranslate .nohighlight} and [\\(\\gamma_t\\)]{.math .notranslate .nohighlight}, respectively.

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(k_r\\)]{.math .notranslate .nohighlight} (force/distance units)

- [\\(k_s\\)]{.math .notranslate .nohighlight} (force/distance units)

- [\\(k_t\\)]{.math .notranslate .nohighlight} (force\*distance/radians units)

- [\\(k_b\\)]{.math .notranslate .nohighlight} (force\*distance/radians units)

- [\\(f\_{r,c}\\)]{.math .notranslate .nohighlight} (force units)

- [\\(f\_{s,c}\\)]{.math .notranslate .nohighlight} (force units)

- [\\(\\tau\_{t,c}\\)]{.math .notranslate .nohighlight} (force\*distance units)

- [\\(\\tau\_{b,c}\\)]{.math .notranslate .nohighlight} (force\*distance units)

- [\\(\\gamma_n\\)]{.math .notranslate .nohighlight} (force/velocity units)

- [\\(\\gamma_s\\)]{.math .notranslate .nohighlight} (force/velocity units)

- [\\(\\gamma_r\\)]{.math .notranslate .nohighlight} (force\*distance/velocity units)

- [\\(\\gamma_t\\)]{.math .notranslate .nohighlight} (force\*distance/velocity units)

If the *normalize* keyword is set to *yes*, the radial and shear forces will be normalized by [\\(r_0\\)]{.math .notranslate .nohighlight} such that [\\(k_r\\)]{.math .notranslate .nohighlight} and [\\(k_s\\)]{.math .notranslate .nohighlight} must be given in force units.

By default, pair forces are not calculated between bonded particles. Pair forces can alternatively be overlaid on top of bond forces by setting the *overlay/pair* keyword to *yes*. This keyword is only necessary if bonds can break and requires specific [[special_bonds]{.doc}]special_bonds.md){.reference .internal} settings described in the restrictions. Further details can be found in the [[how to]{.doc}]Howto_bpm.md){.reference .internal} page on BPMs.

::: versionadded
[Added in version 28Mar2023.]{.versionmodified .added}
:::

If the *break* keyword is set to *no*, LAMMPS assumes bonds should not break during a simulation run. This will prevent some unnecessary calculation. The recommended bond communication distance no longer depends on bond failure coefficients (which are ignored) but instead corresponds to the typical heuristic maximum strain used by typical non-bpm bond styles. Similar behavior to *break no* can also be attained by setting arbitrarily high values for all four failure coefficients. One cannot use *break no* with *smooth yes*.

If the *store/local* keyword is used, an internal fix will track bonds that break during the simulation. Whenever a bond breaks, data is processed and transferred to an internal fix labeled *fix_ID*. This allows the local data to be accessed by other LAMMPS commands. Following this optional keyword, a list of one or more attributes is specified. These include the IDs of the two atoms in the bond. The other attributes for the two atoms include the timestep during which the bond broke and the current/initial center of mass position of the two atoms.

Data is continuously accumulated over intervals of *N* timesteps. At the end of each interval, all of the saved accumulated data is deleted to make room for new data. Individual datum may therefore persist anywhere between *1* to *N* timesteps depending on when they are saved. This data can be accessed using the *fix_ID* and a [[dump local]{.doc}]dump.md){.reference .internal} command. To ensure all data is output, the dump frequency should correspond to the same interval of *N* timesteps. A dump frequency of an integer multiple of *N* can be used to regularly output a sample of the accumulated data.

Note that when unbroken bonds are dumped to a file via the [[dump local]{.doc}]dump.md){.reference .internal} command, bonds with type 0 (broken bonds) are not included. The [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal} command can also be used to query the status of broken bonds or permanently delete them, e.g.:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    delete_bonds all stats
    delete_bonds all bond 0 remove
:::
::::
::::::::::

------------------------------------------------------------------------

::: {#restart-and-other-info .section}
## Restart and other info[](#restart-and-other-info "Link to this heading"){.headerlink}

This bond style writes the reference state of each bond to [[binary restart files]{.doc}]restart.md){.reference .internal}. Loading a restart file will properly resume bonds. However, the reference state is NOT written to data files. Therefore reading a data file will not restore bonds and will cause their reference states to be redefined.

If the *store/local* option is used, an internal fix will calculate a local vector or local array depending on the number of input values. The length of the vector or number of rows in the array is the number of recorded, broken bonds. If a single input is specified, a local vector is produced. If two or more inputs are specified, a local array is produced where the number of columns = the number of inputs. The vector or array can be accessed by any command that uses local values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The vector or array will be floating point values that correspond to the specified attribute.

Any settings with the *store/local* option are not saved to a restart file and must be redefined.

The single() function of this bond style returns 0.0 for the energy of a bonded interaction, since energy is not conserved in these dissipative potentials. It also returns only the normal component of the bonded interaction force. However, the single() function also calculates 7 extra bond quantities. The first 4 are data from the reference state of the bond including the initial distance between particles [\\(r_0\\)]{.math .notranslate .nohighlight} followed by the [\\(x\\)]{.math .notranslate .nohighlight}, [\\(y\\)]{.math .notranslate .nohighlight}, and [\\(z\\)]{.math .notranslate .nohighlight} components of the initial unit vector pointing to particle I from particle J. The next 3 quantities (5-7) are the [\\(x\\)]{.math .notranslate .nohighlight}, [\\(y\\)]{.math .notranslate .nohighlight}, and [\\(z\\)]{.math .notranslate .nohighlight} components of the total force, including normal and tangential contributions, acting on particle I.

These extra quantities can be accessed by the [[compute bond/local]{.doc}]compute_bond_local.md){.reference .internal} command, as *b1*, *b2*, ..., *b7*.
:::

::::::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style is part of the BPM package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

To handle breaking bonds, BPM bond styles have extra requirements for special bonds. If bonds cannot break (*break no*), then one can use any special bond weights. Otherwise, restrictions depend on whether pair forces are overlaid (*pair/overlay yes*). If so, then all weights must be one:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    special_bonds lj/coul 1 1 1
:::
::::

If pair forces are disabled (*pair/overlay no*), the default, then the weights must be

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    special_bonds lj 0 1 1 coul 1 1 1
:::
::::

and [[newton]{.doc}]newton.md){.reference .internal} must be set to bond off.

The *bpm/rotational* style requires [[atom style bpm/sphere]{.doc}]atom_style.md){.reference .internal}.
:::::::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[fix nve/bpm/sphere]{.doc}]fix_nve_bpm_sphere.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *overlay/pair* = *no*, *smooth* = *yes*, *normalize* = *no*, and *break* = *yes*

------------------------------------------------------------------------

**(Wang)** Wang, Acta Geotechnica, 4, p 117-127 (2009).

**(Wang and Mora)** Wang, Mora, Advances in Geocomputing, 119, p 183-228 (2009).

**(Groot)** Groot and Warren, J Chem Phys, 107, 4423-35 (1997).

**(Wang et al, 2015)** Wang, Y., Alonso-Marroquin, F., & Guo, W. W. (2015). Rolling and sliding in 3-D discrete element models. Particuology, 23, 49-55.
:::
:::::::::::::::::::::::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::

::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::: {#bond-style-bpm-spring-command .section}
[]{#index-0}

# bond_style bpm/spring command[](#bond-style-bpm-spring-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style bpm/spring keyword value attribute1 attribute2 ...
:::
::::

- optional keyword = *overlay/pair* or *store/local* or *smooth* or *normalize* or *break* or *volume/factor*

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
     normalizes bond forces by the reference length

  break value = yes or no
     indicates whether bonds break during a run

  volume/factor value = yes or no
     indicates whether forces include the volumetric contribution
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style bpm/spring
    bond_coeff 1 1.0 0.05 0.1

    bond_style bpm/spring volume/factor yes
    bond_coeff 1 1.0 0.05 0.1 0.5

    bond_style bpm/spring myfix 1000 time id1 id2
    dump 1 all local 1000 dump.broken f_myfix[1] f_myfix[2] f_myfix[3]
    dump_modify 1 write_header no
:::
::::
:::::

:::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

The *bpm/spring* bond style computes forces based on deviations from the initial reference state of the two atoms. The reference state is stored by each bond when it is first computed in the setup of a run. Data is then preserved across run commands and is written to [[binary restart files]{.doc}]restart.md){.reference .internal} such that restarting the system will not reset the reference state of a bond.

This bond style only applies central-body forces which conserve the translational and rotational degrees of freedom of a bonded set of particles based on a model described by Clemmer and Robbins [[(Clemmer)]{.std .std-ref}](#fragment-clemmer){.reference .internal}. The force has a magnitude of

::: {.math .notranslate .nohighlight}
\\\[F = k (r - r_0) w\\\]
:::

where [\\(k\\)]{.math .notranslate .nohighlight} is a stiffness, [\\(r\\)]{.math .notranslate .nohighlight} is the current distance and [\\(r_0\\)]{.math .notranslate .nohighlight} is the initial distance between the two particles, and [\\(w\\)]{.math .notranslate .nohighlight} is an optional smoothing factor discussed below. Bonds will break at a strain of [\\(\\epsilon_c\\)]{.math .notranslate .nohighlight}. This is done by setting the bond type to 0 such that forces are no longer computed.

An additional damping force is applied to the bonded particles. This forces is proportional to the difference in the normal velocity of particles using a similar construction as dissipative particle dynamics [[(Groot)]{.std .std-ref}](#groot4){.reference .internal}:

::: {.math .notranslate .nohighlight}
\\\[F_D = - \\gamma w (\\hat{r} \\bullet \\vec{v})\\\]
:::

where [\\(\\gamma\\)]{.math .notranslate .nohighlight} is the damping strength, [\\(\\hat{r}\\)]{.math .notranslate .nohighlight} is the radial normal vector, and [\\(\\vec{v}\\)]{.math .notranslate .nohighlight} is the velocity difference between the two particles.

The smoothing factor [\\(w\\)]{.math .notranslate .nohighlight} can be added or removed by setting the *smooth* keyword to *yes* or *no*, respectively. It is constructed such that forces smoothly go to zero, avoiding discontinuities, as bonds approach the critical strain

::: {.math .notranslate .nohighlight}
\\\[w = 1.0 - \\left( \\frac{r - r_0}{r_0 \\epsilon_c} \\right)\^8 .\\\]
:::

If the *normalize* keyword is set to *yes*, the elastic bond force will be normalized by [\\(r_0\\)]{.math .notranslate .nohighlight} such that [\\(k\\)]{.math .notranslate .nohighlight} must be given in force units.

By default, pair forces are not calculated between bonded particles. Pair forces can alternatively be overlaid on top of bond forces by setting the *overlay/pair* keyword to *yes*. This keyword is only necessary if bonds can break and requires specific [[special_bonds]{.doc}]special_bonds.md){.reference .internal} settings described in the restrictions. Further details can be found in the [[how to]{.doc}]Howto_bpm.md){.reference .internal} page on BPMs.

::: versionadded
[Added in version 28Mar2023.]{.versionmodified .added}
:::

If the *break* keyword is set to *no*, LAMMPS assumes bonds should not break during a simulation run. This will prevent some unnecessary calculation. The recommended bond communication distance no longer depends on the value of [\\(\\epsilon_c\\)]{.math .notranslate .nohighlight} (which is ignored) but instead corresponds to the typical heuristic maximum strain used by typical non-bpm bond styles. Similar behavior to *break no* can also be attained by setting an arbitrarily high value of [\\(\\epsilon_c\\)]{.math .notranslate .nohighlight}. One cannot use *break no* with *smooth yes*.

::: versionadded
[Added in version 4Feb2025.]{.versionmodified .added}
:::

The *volume/factor* keyword toggles whether an additional multibody contribution is added to he force using the formulation in [[(Clemmer2)]{.std .std-ref}](#multibody-clemmer){.reference .internal},

::: {.math .notranslate .nohighlight}
\\\[\\alpha_v \\left(\\left\[\\frac{V_i + V_j}{V\_{0,i} + V\_{0,j}}\\right\]\^{1/3} - \\frac{r\_{ij}}{r\_{0,ij}}\\right)\\\]
:::

where [\\(\\alpha_v\\)]{.math .notranslate .nohighlight} is a user specified coefficient and [\\(V_i\\)]{.math .notranslate .nohighlight} and [\\(V\_{0,i}\\)]{.math .notranslate .nohighlight} are estimates of the current and local volume of atom [\\(i\\)]{.math .notranslate .nohighlight}. These volumes are calculated as the sum of current or initial bond lengths cubed. In 2D, the volume is replaced with an area calculated using bond lengths squared and the cube root in the above equation is accordingly replaced with a square root. This approximation assumes bonds are evenly distributed on a spherical surface and neglects constant prefactors which are irrelevant since only the ratio of volumes matters. This term may be used to adjust the Poisson's ratio. See the simulation in the [`examples/bpm/poissons_ratio`{.docutils .literal .notranslate}]{.pre} directory for a demonstration of this effect.

If a bond is broken (or created), [\\(V\_{0,i}\\)]{.math .notranslate .nohighlight} is updated by subtracting (or adding) that bond's contribution.

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(k\\)]{.math .notranslate .nohighlight} (force/distance units)

- [\\(\\epsilon_c\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

Additionally, if *volume/factor* is set to *yes*, a fourth coefficient must be provided:

- [\\(a_v\\)]{.math .notranslate .nohighlight} (force units)

If the *store/local* keyword is used, an internal fix will track bonds that break during the simulation. Whenever a bond breaks, data is processed and transferred to an internal fix labeled *fix_ID*. This allows the local data to be accessed by other LAMMPS commands. Following this optional keyword, a list of one or more attributes is specified. These include the IDs of the two atoms in the bond. The other attributes for the two atoms include the timestep during which the bond broke and the current/initial center of mass position of the two atoms.

Data is continuously accumulated over intervals of *N* timesteps. At the end of each interval, all of the saved accumulated data is deleted to make room for new data. Individual datum may therefore persist anywhere between *1* to *N* timesteps depending on when they are saved. This data can be accessed using the *fix_ID* and a [[dump local]{.doc}]dump.md){.reference .internal} command. To ensure all data is output, the dump frequency should correspond to the same interval of *N* timesteps. A dump frequency of an integer multiple of *N* can be used to regularly output a sample of the accumulated data.

Note that when unbroken bonds are dumped to a file via the [[dump local]{.doc}]dump.md){.reference .internal} command, bonds with type 0 (broken bonds) are not included. The [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal} command can also be used to query the status of broken bonds or permanently delete them, e.g.:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    delete_bonds all stats
    delete_bonds all bond 0 remove
:::
::::
::::::::::::

------------------------------------------------------------------------

::: {#restart-and-other-info .section}
## Restart and other info[](#restart-and-other-info "Link to this heading"){.headerlink}

This bond style writes the reference state of each bond to [[binary restart files]{.doc}]restart.md){.reference .internal}. Loading a restart file will properly restore bonds. However, the reference state is NOT written to data files. Therefore reading a data file will not restore bonds and will cause their reference states to be redefined.

If the *store/local* option is used, an internal fix will calculate a local vector or local array depending on the number of input values. The length of the vector or number of rows in the array is the number of recorded, broken bonds. If a single input is specified, a local vector is produced. If two or more inputs are specified, a local array is produced where the number of columns = the number of inputs. The vector or array can be accessed by any command that uses local values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The vector or array will be floating point values that correspond to the specified attribute.

Any settings with the *store/local* option are not saved to a restart file and must be redefined.

The potential energy and the single() function of this bond style return [\\(k (r - r_0)\^2 / 2\\)]{.math .notranslate .nohighlight} as a proxy of the energy of a bonded interaction, ignoring any volumetric/smoothing factors or dissipative forces. The single() function also calculates an extra bond quantity, the initial distance [\\(r_0\\)]{.math .notranslate .nohighlight}. This extra quantity can be accessed by the [[compute bond/local]{.doc}]compute_bond_local.md){.reference .internal} command as *b1*.
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
:::::::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[pair bpm/spring]{.doc}]pair_bpm_spring.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *overlay/pair* = *no*, *smooth* = *yes*, *normalize* = *no*, *break* = *yes*, and *volume/factor* = *no*

------------------------------------------------------------------------

**(Clemmer)** Clemmer and Robbins, Phys. Rev. Lett. (2022).

**(Groot)** Groot and Warren, J Chem Phys, 107, 4423-35 (1997).

**(Clemmer2)** Clemmer, Monti, Lechman, Soft Matter, 20, 1702 (2024).
:::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::

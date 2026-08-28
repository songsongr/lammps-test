::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#bond-style-rheo-shell-command .section}
[]{#index-0}

# bond_style rheo/shell command[](#bond-style-rheo-shell-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style rheo/shell keyword value attribute1 attribute2 ...
:::
::::

- required keyword = *t/form*

- optional keyword = *store/local*

  ``` literal-block
  t/form value = formation time for a bond (time units)

  store/local values = fix_ID N attributes ...
     * fix_ID = ID of associated internal fix to store data
     * N = prepare data for output every this many timesteps
     * attributes = zero or more of the below attributes may be appended

       id1, id2 = IDs of two atoms in the bond
       time = the timestep the bond broke
       x, y, z = the center of mass position of the two atoms when the bond broke (distance units)
       x/ref, y/ref, z/ref = the initial center of mass position of the two atoms (distance units)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style rheo/shell t/form 10.0
    bond_coeff 1 1.0 0.05 0.1
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 29Aug2024.]{.versionmodified .added}
:::

The *rheo/shell* bond style is designed to work with [[fix rheo/oxidation]{.doc}]fix_rheo_oxidation.md){.reference .internal} which creates candidate bonds between eligible surface or near-surface particles. When a bond is first created, it computes no forces and starts a timer. Forces are not computed until the timer reaches the specified bond formation time, *t/form*, and the bond is enabled and applies forces. If the two particles move outside of the maximum bond distance or move into the bulk before the timer reaches *t/form*, the bond automatically deletes itself. This deletion is not recorded as a broken bond in the optional *store/local* fix.

Before bonds are enabled, they are still treated as regular bonds by all other parts of LAMMPS. This means they are written to data files and counted in computes such as [[nbond/atom]{.doc}]compute_nbond_atom.md){.reference .internal}. To only count enabled bonds, use the *nbond/shell* attribute in [[compute rheo/property/atom]{.doc}]compute_rheo_property_atom.md){.reference .internal}.

When enabled, the bond then computes forces based on deviations from the initial reference state of the two atoms much like a BPM style bond (as further discussed in the [[BPM howto page]{.doc}]Howto_bpm.md){.reference .internal}). The reference state is stored by each bond when it is first enabled. Data is then preserved across run commands and is written to [[binary restart files]{.doc}]restart.md){.reference .internal} such that restarting the system will not reset the reference state of a bond or the timer.

This bond style is based on a model described in [[(Clemmer)]{.std .std-ref}](#rheo-clemmer){.reference .internal}. The force has a magnitude of

::: {.math .notranslate .nohighlight}
\\\[F = 2 k (r - r_0) + \\frac{2 k}{r_0\^2 \\epsilon_c\^2} (r - r_0)\^3\\\]
:::

where [\\(k\\)]{.math .notranslate .nohighlight} is a stiffness, [\\(r\\)]{.math .notranslate .nohighlight} is the current distance and [\\(r_0\\)]{.math .notranslate .nohighlight} is the initial distance between the two particles, and [\\(\\epsilon_c\\)]{.math .notranslate .nohighlight} is maximum strain beyond which a bond breaks. This is done by setting the bond type to 0 such that forces are no longer computed.

A damping force proportional to the difference in the normal velocity of particles is also applied to bonded particles:

::: {.math .notranslate .nohighlight}
\\\[F_D = - \\gamma w (\\hat{r} \\bullet \\vec{v})\\\]
:::

where [\\(\\gamma\\)]{.math .notranslate .nohighlight} is the damping strength, [\\(\\hat{r}\\)]{.math .notranslate .nohighlight} is the displacement normal vector, and [\\(\\vec{v}\\)]{.math .notranslate .nohighlight} is the velocity difference between the two particles.

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(k\\)]{.math .notranslate .nohighlight} (force/distance units)

- [\\(\\epsilon_c\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

Unlike other BPM-style bonds, this bond style does not update special bond settings when bonds are created or deleted. This bond style also does not enforce specific [[special_bonds]{.doc}]special_bonds.md){.reference .internal} settings. This behavior is purposeful such [[RHEO pair]{.doc}]pair_rheo.md){.reference .internal} forces and heat flows are still calculated.

If the *store/local* keyword is used, an internal fix will track bonds that break during the simulation. Whenever a bond breaks, data is processed and transferred to an internal fix labeled *fix_ID*. This allows the local data to be accessed by other LAMMPS commands. Following this optional keyword, a list of one or more attributes is specified. These include the IDs of the two atoms in the bond. The other attributes for the two atoms include the timestep during which the bond broke and the current/initial center of mass position of the two atoms.

Data is continuously accumulated over intervals of *N* timesteps. At the end of each interval, all of the saved accumulated data is deleted to make room for new data. Individual datum may therefore persist anywhere between *1* to *N* timesteps depending on when they are saved. This data can be accessed using the *fix_ID* and a [[dump local]{.doc}]dump.md){.reference .internal} command. To ensure all data is output, the dump frequency should correspond to the same interval of *N* timesteps. A dump frequency of an integer multiple of *N* can be used to regularly output a sample of the accumulated data.

Note that when unbroken bonds are dumped to a file via the [[dump local]{.doc}]dump.md){.reference .internal} command, bonds with type 0 (broken bonds) are not included. The [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal} command can also be used to query the status of broken bonds or permanently delete them, e.g.:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    delete_bonds all stats
    delete_bonds all bond 0 remove
:::
::::
::::::::

------------------------------------------------------------------------

::: {#restart-and-other-info .section}
## Restart and other info[](#restart-and-other-info "Link to this heading"){.headerlink}

This bond style writes the reference state of each bond to [[binary restart files]{.doc}]restart.md){.reference .internal}. Loading a restart file will properly restore bonds. However, the reference state is NOT written to data files. Therefore reading a data file will not restore bonds and will cause their reference states to be redefined.

If the *store/local* option is used, an internal fix will calculate a local vector or local array depending on the number of input values. The length of the vector or number of rows in the array is the number of recorded, broken bonds. If a single input is specified, a local vector is produced. If two or more inputs are specified, a local array is produced where the number of columns = the number of inputs. The vector or array can be accessed by any command that uses local values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The vector or array will be floating point values that correspond to the specified attribute.

The single() function of this bond style returns 0.0 for the energy of a bonded interaction, since energy is not conserved in these dissipative potentials. The single() function also calculates two extra bond quantities, the initial distance [\\(r_0\\)]{.math .notranslate .nohighlight} and a time. These extra quantities can be accessed by the [[compute bond/local]{.doc}]compute_bond_local.md){.reference .internal} command as *b1* and *b2*.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style is part of the RHEO package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[fix rheo/oxidation]{.doc}]fix_rheo_oxidation.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

NA

------------------------------------------------------------------------

**(Clemmer)** Clemmer, Pierce, O'Connor, Nevins, Jones, Lechman, Tencer, Appl. Math. Model., 130, 310-326 (2024).
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

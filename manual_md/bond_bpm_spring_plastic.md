:::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::: {#bond-style-bpm-spring-plastic-command .section}
[]{#index-0}

# bond_style bpm/spring/plastic command[](#bond-style-bpm-spring-plastic-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style bpm/spring/plastic keyword value attribute1 attribute2 ...
:::
::::

- optional keyword = *overlay/pair* or *store/local* or *smooth* or *normalize* or *break*

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
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style bpm/spring/plastic
    bond_coeff 1 1.0 0.05 0.1 0.02

    bond_style bpm/spring/plastic myfix 1000 time id1 id2
    dump 1 all local 1000 dump.broken f_myfix[1] f_myfix[2] f_myfix[3]
    dump_modify 1 write_header no
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 2Apr2025.]{.versionmodified .added}
:::

The *bpm/spring/plastic* bond style computes forces based on deviations from the initial reference state of the two atoms and the strain history. The reference length of the bond [\\(r_0\\)]{.math .notranslate .nohighlight} is stored by each bond when it is first computed in the setup of a run. Initially, the equilibrium length of each bond [\\(r\_\\mathrm{eq}\\)]{.math .notranslate .nohighlight} is set equal to [\\(r_0\\)]{.math .notranslate .nohighlight} but can evolve. data is then preserved across run commands and is written to [[binary restart files]{.doc}]restart.md){.reference .internal} such that restarting the system will not modify either of these quantities.

This bond style only applies central-body forces which conserve the translational and rotational degrees of freedom of a bonded set of particles. The force has a magnitude of

::: {.math .notranslate .nohighlight}
\\\[F = -k (r\_\\mathrm{eq} - r) w\\\]
:::

where [\\(k\\)]{.math .notranslate .nohighlight} is a stiffness, [\\(r\\)]{.math .notranslate .nohighlight} is the current distance between the two particles, and [\\(w\\)]{.math .notranslate .nohighlight} is an optional smoothing factor discussed below. If the bond stretches beyond a strain of [\\(\\epsilon_p\\)]{.math .notranslate .nohighlight} in compression or extension, it will plastically activate and [\\(r\_\\mathrm{eq}\\)]{.math .notranslate .nohighlight} will evolve to ensure [\\(\|(r-r\_\\mathrm{eq})/r\_\\mathrm{eq}\|\\)]{.math .notranslate .nohighlight} never exceeds [\\(\\epsilon_p\\)]{.math .notranslate .nohighlight}. Therefore, if a bond is continually loaded in either tension or compression, the force will initially grow elastically before plateauing. See [[(Clemmer)]{.std .std-ref}](#plastic-clemmer){.reference .internal} for more details on these mechanics.

Bonds will break at a strain of [\\(\\epsilon_c\\)]{.math .notranslate .nohighlight}. This is done by setting the bond type to 0 such that forces are no longer computed.

An additional damping force is applied to the bonded particles. This forces is proportional to the difference in the normal velocity of particles:

::: {.math .notranslate .nohighlight}
\\\[F_D = - \\gamma w (\\hat{r} \\bullet \\vec{v})\\\]
:::

where [\\(\\gamma\\)]{.math .notranslate .nohighlight} is the damping strength, [\\(\\hat{r}\\)]{.math .notranslate .nohighlight} is the radial normal vector, and [\\(\\vec{v}\\)]{.math .notranslate .nohighlight} is the velocity difference between the two particles.

The smoothing factor [\\(w\\)]{.math .notranslate .nohighlight} is constructed such that forces smoothly go to zero, avoiding discontinuities, as bonds approach the critical breaking strain

::: {.math .notranslate .nohighlight}
\\\[w = 1.0 - \\left( \\frac{r - r_0}{r_0 \\epsilon_c} \\right)\^8 .\\\]
:::

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(k\\)]{.math .notranslate .nohighlight} (force/distance units)

- [\\(\\epsilon_c\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (force/velocity units)

- [\\(\\epsilon_p\\)]{.math .notranslate .nohighlight} (unitless)

See the [[bpm/spring doc page]{.doc}]bond_bpm_spring.md){.reference .internal} for information on the *smooth*, *normalize*, *break*, *overlay/pair*, and *store/local* keywords.

Note that when unbroken bonds are dumped to a file via the [[dump local]{.doc}]dump.md){.reference .internal} command, bonds with type 0 (broken bonds) are not included. The [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal} command can also be used to query the status of broken bonds or permanently delete them, e.g.:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    delete_bonds all stats
    delete_bonds all bond 0 remove
:::
::::
:::::::::

------------------------------------------------------------------------

::: {#restart-and-other-info .section}
## Restart and other info[](#restart-and-other-info "Link to this heading"){.headerlink}

This bond style writes the reference state and plastic history of each bond to [[binary restart files]{.doc}]restart.md){.reference .internal}. Loading a restart file will properly restore bonds. However, the reference state is NOT written to data files. Therefore reading a data file will not restore bonds and will cause their reference states to be redefined.

The potential energy and the single() function of this bond style returns zero. The single() function also calculates two extra bond quantities, the initial distance [\\(r_0\\)]{.math .notranslate .nohighlight} and the current equilibrium length [\\(r\_{eq}\\)]{.math .notranslate .nohighlight}. These extra quantities can be accessed by the [[compute bond/local]{.doc}]compute_bond_local.md){.reference .internal} command as *b1* and *b2*, respectively.
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

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[bond bpm/spring]{.doc}]bond_bpm_spring.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *overlay/pair* = *no*, *smooth* = *yes*, *normalize* = *no*, and *break* = *yes*

------------------------------------------------------------------------

**(Clemmer)** Clemmer and Lechman, Powder Technology (2025).
:::
::::::::::::::::::::::::
:::::::::::::::::::::::::
::::::::::::::::::::::::::

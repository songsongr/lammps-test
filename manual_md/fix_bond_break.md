:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-bond-break-command .section}
[]{#index-0}

# fix bond/break command[](#fix-bond-break-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID bond/break Nevery bondtype Rmax keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- bond/break = style name of this fix command

- Nevery = attempt bond breaking every this many steps

- bondtype = type of bonds to break (integer or type label)

- Rmax = bond longer than Rmax can break (distance units)

- zero or more keyword/value pairs may be appended

- keyword = *prob*

  ``` literal-block
  prob values = fraction seed
    fraction = break a bond with this probability if otherwise eligible
    seed = random number seed (positive integer)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 5 all bond/break 10 2 1.2
    fix 5 polymer bond/break 1 1 2.0 prob 0.5 49829
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Break bonds between pairs of atoms as a simulation runs according to specified criteria. This can be used to model the dissolution of a polymer network due to stretching of the simulation box or other deformations. In this context, a bond means an interaction between a pair of atoms computed by the [[bond_style]{.doc}]bond_style.md){.reference .internal} command. Once the bond is broken it will be permanently deleted, as will all angle, dihedral, and improper interactions that bond is part of.

This is different than a [[pair-wise]{.doc}]pair_style.md){.reference .internal} bond-order potential such as Tersoff or AIREBO which infers bonds and many-body interactions based on the current geometry of a small cluster of atoms and effectively creates and destroys bonds and higher-order many-body interactions from timestep to timestep as atoms move.

A check for possible bond breakage is performed every *Nevery* timesteps. If two bonded atoms [\\(i\\)]{.math .notranslate .nohighlight} and [\\(j\\)]{.math .notranslate .nohighlight} are farther than the distance *Rmax* from each other, the bond is of type *bondtype*, and both [\\(i\\)]{.math .notranslate .nohighlight} and [\\(j\\)]{.math .notranslate .nohighlight} are in the specified fix group, then the bond between [\\(i\\)]{.math .notranslate .nohighlight} and [\\(j\\)]{.math .notranslate .nohighlight} is labeled as a "possible" bond to break.

If several bonds involving an atom are stretched, it may have multiple possible bonds to break. Every atom checks its list of possible bonds to break and labels the longest such bond as its "sole" bond to break. After this is done, if atom [\\(i\\)]{.math .notranslate .nohighlight} is bonded to atom [\\(j\\)]{.math .notranslate .nohighlight} in its sole bond, and atom [\\(j\\)]{.math .notranslate .nohighlight} is bonded to atom [\\(j\\)]{.math .notranslate .nohighlight} in its sole bond, then the bond between [\\(i\\)]{.math .notranslate .nohighlight} and [\\(j\\)]{.math .notranslate .nohighlight} is "eligible" to be broken.

Note that these rules mean an atom will only be part of at most one broken bond on a given time step. It also means that if atom [\\(i\\)]{.math .notranslate .nohighlight} chooses atom [\\(j\\)]{.math .notranslate .nohighlight} as its sole partner, but atom [\\(j\\)]{.math .notranslate .nohighlight} chooses atom [\\(k\\)]{.math .notranslate .nohighlight} as its sole partner (because [\\(R\_{jk} \> R\_{ij}\\)]{.math .notranslate .nohighlight}), then this means atom [\\(i\\)]{.math .notranslate .nohighlight} will not be part of a broken bond on this time step, even if it has other possible bond partners.

The *prob* keyword can effect whether an eligible bond is actually broken. The *fraction* setting must be a value between 0.0 and 1.0. A uniform random number between 0.0 and 1.0 is generated and the eligible bond is only broken if the random number is less than *fraction*.

When a bond is broken, data structures within LAMMPS that store bond topologies are updated to reflect the breakage. Likewise, if the bond is part of a 3-body (angle) or 4-body (dihedral, improper) interaction, that interaction is removed as well. These changes typically affect pair-wise interactions between atoms that used to be part of bonds, angles, etc.

::: {.admonition .note}
Note

One data structure that is not updated when a bond breaks are the molecule IDs stored by each atom. Even though one molecule becomes two molecules due to the broken bond, all atoms in both new molecules retain their original molecule IDs.
:::

Computationally, each time step this fix is invoked, it loops over all the bonds in the system and computes distances between pairs of bonded atoms. It also communicates between neighboring processors to coordinate which bonds are broken. Moreover, if any bonds are broken, neighbor lists must be immediately updated on the same time step. This is to ensure that any pair-wise interactions that should be turned "on" due to a bond breaking, because they are no longer excluded by the presence of the bond and the settings of the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command, will be immediately recognized. All of these operations increase the cost of a time step. Thus, you should be cautious about invoking this fix too frequently.

You can dump out snapshots of the current bond topology via the [[dump local]{.doc}]dump.md){.reference .internal} command.

::: {.admonition .note}
Note

Breaking a bond typically alters the energy of a system. You should be careful not to choose bond breaking criteria that induce a dramatic change in energy. For example, if you define a very stiff harmonic bond and break it when two atoms are separated by a distance far from the equilibrium bond length, then the two atoms will be dramatically released when the bond is broken. More generally, you may need to thermostat your system to compensate for energy changes resulting from broken bonds (as well as angles, dihedrals, and impropers).
:::

See the [[Howto]{.doc}]Howto_broken_bonds.md){.reference .internal} page on broken bonds for more information on related features in LAMMPS.
:::::

------------------------------------------------------------------------

:::: {#dump-image-info .section}
## Dump image info[](#dump-image-info "Link to this heading"){.headerlink}

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

Fix *bond/break* supports the *fix* keyword of [[dump image]{.doc}]dump_image.md){.reference .internal}. The fix will pass geometry information about atoms involved in a broken bond to *dump image* so that these atoms can be highlighted in the visualization as additional spheres. For how long those additional spheres will be shown depends on the value of the *vizsteps* setting (default is 1000) which can be changed by using the [[fix_modify command]{.doc}]fix_modify.md){.reference .internal}. If an atom is involved in multiple broken bonds, the check on showing the additional graphics depends on the timestep of its latest broken bond.

The color of the additional spheres is by default that of the atoms when using color styles "type" or "element". With color style "const" the default value of "white" can be changed using [[dump_modify fcolor]{.doc}]dump_image.md){.reference .internal}. The transparency is by default fully opaque and can be changed with *dump_modify ftrans*.

The *fflag1* setting of *dump image fix* has no effect.

The *fflag2* setting allows you to set the radius of the added spheres, since the radius is set to zero internally.
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix computes two statistics, which it stores in a global vector of length 2. This vector can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The vector values calculated by this fix are "intensive".

The two quantities in the global vector are

> ::: {}
> 1.  number of bonds broken on the most recent breakage time step
>
> 2.  cumulative number of bonds broken
> :::

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix bond/create]{.doc}]fix_bond_create.md){.reference .internal}, [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}, [[fix bond/swap]{.doc}]fix_bond_swap.md){.reference .internal}, [[dump local]{.doc}]dump.md){.reference .internal}, [[special_bonds]{.doc}]special_bonds.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are prob = 1.0.
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

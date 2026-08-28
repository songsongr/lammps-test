::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#compute-bond-local-command .section}
[]{#index-0}

# compute bond/local command[](#compute-bond-local-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID bond/local value1 value2 ... keyword args ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- bond/local = style name of this compute command

- one or more values may be appended

- value = *dist* or *dx* or *dy* or *dz* or *engpot* or *force* or *fx* or *fy* or *fz* or *engvib* or *engrot* or *engtrans* or *omega* or *velvib* or *v_name* or *bN*

``` literal-block
dist = bond distance
engpot = bond potential energy
force = bond force
dx,dy,dz = components of pairwise distance
fx,fy,fz = components of bond force
engvib = bond kinetic energy of vibration
engrot = bond kinetic energy of rotation
engtrans = bond kinetic energy of translation
omega = magnitude of bond angular velocity
velvib = vibrational velocity along the bond length
v_name = equal-style variable with name (see below)
bN = bond style specific quantities for allowed N values
```

- zero or more keyword/args pairs may be appended

- keyword = *set*

``` literal-block
set args = dist name
  dist = only currently allowed arg
  name = name of variable to set with distance (dist)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all bond/local engpot
    compute 1 all bond/local dist engpot force
    compute 1 all bond/local dist fx fy fz b1 b2
    compute 1 all bond/local dist v_distsq set dist d
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates properties of individual bond interactions. The number of datums generated, aggregated across all processors, equals the number of bonds in the system, modified by the group parameter as explained below.

All these properties are computed for the pair of atoms in a bond, whether the two atoms represent a simple diatomic molecule, or are part of some larger molecule.

::: versionchanged
[Changed in version 12Jun2025: ]{.versionmodified .changed}The sign of *dx*, *dy*, *dz* is no longer determined by the atom IDs of the bonded atoms but by their order in the bond list to be consistent with *fx*, *fy*, and *fz*.
:::

The value *dist* is the current length of the bond. The values *dx*, *dy*, and *dz* are the [\\((x,y,z)\\)]{.math .notranslate .nohighlight} components of the distance vector [\\(\\vec{x_i} - \\vec{x_j}\\)]{.math .notranslate .nohighlight} between the atoms in the bond. The order of the atoms is determined by the bond list and the respective atom-IDs can be output with [[compute property/local]{.doc}]compute_property_local.md){.reference .internal}.

The value *engpot* is the potential energy for the bond, based on the current separation of the pair of atoms in the bond.

The value *force* is the magnitude of the force acting between the pair of atoms in the bond, which is positive for a repulsive force and negative for an attractive force.

The values *fx*, *fy*, and *fz* are the [\\((x,y,z)\\)]{.math .notranslate .nohighlight} components of the force on the first atom *i* in the bond due to the second atom *j*. Mathematically, they are obtained by multiplying the value of *force* from above with a unit vector created from the *dx*, *dy*, and *dz* components of the distance vector also described above. For bond styles that apply non-central forces, such as [[bond_style bpm/rotational]{.doc}]bond_bpm_rotational.md){.reference .internal}, these values only include the [\\((x,y,z)\\)]{.math .notranslate .nohighlight} components of the normal force component.

The remaining properties are all computed for motion of the two atoms relative to the center of mass (COM) velocity of the two atoms in the bond.

The value *engvib* is the vibrational kinetic energy of the two atoms in the bond, which is simply [\\(\\frac12 m_1 v_1\^2 + \\frac12 m_2 v_2\^2,\\)]{.math .notranslate .nohighlight} where [\\(v_1\\)]{.math .notranslate .nohighlight} and [\\(v_2\\)]{.math .notranslate .nohighlight} are the magnitude of the velocity of the two atoms along the bond direction, after the COM velocity has been subtracted from each.

The value *engrot* is the rotational kinetic energy of the two atoms in the bond, which is simply [\\(\\frac12 m_1 v_1\^2 + \\frac12 m_2 v_2\^2,\\)]{.math .notranslate .nohighlight} where [\\(v_1\\)]{.math .notranslate .nohighlight} and [\\(v_2\\)]{.math .notranslate .nohighlight} are the magnitude of the velocity of the two atoms perpendicular to the bond direction, after the COM velocity has been subtracted from each.

The value *engtrans* is the translational kinetic energy associated with the motion of the COM of the system itself, namely [\\(\\frac12(m_1+m_2) V\_{\\mathrm{cm}}\^2\\)]{.math .notranslate .nohighlight}, where Vcm = magnitude of the velocity of the COM.

Note that these three kinetic energy terms are simply a partitioning of the summed kinetic energy of the two atoms themselves. That is, the total kinetic energy is [\\(\\frac12 m_1 v_1\^2 + \\frac12 m_2 v_2\^2\\)]{.math .notranslate .nohighlight} = engvib + engrot + engtrans, where [\\(v_1\\)]{.math .notranslate .nohighlight} and [\\(v_2\\)]{.math .notranslate .nohighlight} are the magnitude of the velocities of the two atoms, without any adjustment for the COM velocity.

The value *omega* is the magnitude of the angular velocity of the two atoms around their COM position.

The value *velvib* is the magnitude of the relative velocity of the two atoms in the bond towards each other. A negative value means the two atoms are moving toward each other; a positive value means they are moving apart.

The value *v_name* can be used together with the *set* keyword to compute a user-specified function of the bond distance. The *name* specified for the *v_name* value is the name of an [[equal-style variable]{.doc}]variable.md){.reference .internal} which should evaluate a formula based on a variable which stores the bond distance. This other variable must be the [[internal-style variable]{.doc}]variable.md){.reference .internal} specified by the *set* keyword. It is an internal-style variable, because this command resets its value directly. The internal-style variable does not need to be defined in the input script (though it can be); if it is not defined, then the *set* option creates an [[internal-style variable]{.doc}]variable.md){.reference .internal} with the specified name.

As an example, these commands can be added to the bench/in.rhodo script to compute the length[\\(\^2\\)]{.math .notranslate .nohighlight} of every bond in the system and output the statistics in various ways:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable dsq equal v_d*v_d

    compute 1 all property/local batom1 batom2 btype
    compute 2 all bond/local engpot dist v_dsq set dist d
    dump 1 all local 100 tmp.dump c_1[*] c_2[*]

    compute 3 all reduce ave c_2[*] inputs local
    thermo_style custom step temp press c_3[*]

    fix 10 all ave/histo 10 10 100 0 6 20 c_2[3] mode vector file tmp.histo
:::
::::

The [[dump local]{.doc}]dump.md){.reference .internal} command will output the energy, length, and length[\\(\^2\\)]{.math .notranslate .nohighlight} for every bond in the system. The [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command will print the average of those quantities via the [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} command with thermo output, and the [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal} command will histogram the length[\\(\^2\\)]{.math .notranslate .nohighlight} values and write them to a file.

A bond style may define additional bond quantities which can be accessed as *b1* to *bN*, where N is defined by the bond style. Most bond styles do not define any additional quantities, so N = 0. An example of ones that do are the [[BPM bond styles]{.doc}]Howto_bpm.md){.reference .internal} which store the reference state between two particles. See individual bond styles for details.

When using *bN* with bond style *hybrid*, the output will be the Nth quantity from the sub-style that computes the bonded interaction (based on bond type). If that sub-style does not define a *bN*, the output will be 0.0. The maximum allowed N is the maximum number of quantities provided by any sub-style.

------------------------------------------------------------------------

The local data stored by this command is generated by looping over all the atoms owned on a processor and their bonds. A bond will only be included if both atoms in the bond are in the specified compute group. Any bonds that have been broken (see the [[bond_style]{.doc}]bond_style.md){.reference .internal} command) by setting their bond type to 0 are not included. Bonds that have been turned off (see the [[fix shake]{.doc}]fix_shake.md){.reference .internal} or [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal} commands) by setting their bond type negative are written into the file, but their energy will be 0.0.

Note that as atoms migrate from processor to processor, there will be no consistent ordering of the entries within the local vector or array from one timestep to the next. The only consistency that is guaranteed is that the ordering on a particular timestep will be the same for local vectors or arrays generated by other compute commands. For example, bond output from the [[compute property/local]{.doc}]compute_property_local.md){.reference .internal} command can be combined with data from this command and output by the [[dump local]{.doc}]dump.md){.reference .internal} command in a consistent way.

Here is an example of how to do this:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all property/local btype batom1 batom2
    compute 2 all bond/local dist engpot
    dump 1 all local 1000 tmp.dump index c_1[*] c_2[*]
:::
::::
::::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a local vector or local array depending on the number of values. The length of the vector or number of rows in the array is the number of bonds. If a single value is specified, a local vector is produced. If two or more values are specified, a local array is produced where the number of columns = the number of values. The vector or array can be accessed by any command that uses local values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The output for *dist* will be in distance [[units]{.doc}]units.md){.reference .internal}. The output for *velvib* will be in velocity [[units]{.doc}]units.md){.reference .internal}. The output for *omega* will be in velocity/distance [[units]{.doc}]units.md){.reference .internal}. The output for *engtrans*, *engvib*, *engrot*, and *engpot* will be in energy [[units]{.doc}]units.md){.reference .internal}. The output for *force* will be in force [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dump local]{.doc}]dump.md){.reference .internal}, [[compute property/local]{.doc}]compute_property_local.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

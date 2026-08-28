::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#tip4p-and-opc-water-models .section}
# [10.4.6. ]{.section-number}TIP4P and OPC water models[](#tip4p-and-opc-water-models "Link to this heading"){.headerlink}

The four-point TIP4P rigid water model extends the traditional [[three-point TIP3P]{.doc}]Howto_tip3p.md){.reference .internal} model by adding an additional site M, usually massless, where the charge associated with the oxygen atom is placed. This site M is located at a fixed distance away from the oxygen along the bisector of the HOH bond angle. A bond style of [[harmonic]{.doc}]bond_harmonic.md){.reference .internal} and an angle style of [[harmonic]{.doc}]angle_harmonic.md){.reference .internal} or [[charmm]{.doc}]angle_charmm.md){.reference .internal} should also be used. In case of rigid bonds also bond style [[zero]{.doc}]bond_zero.md){.reference .internal} and angle style [[zero]{.doc}]angle_zero.md){.reference .internal} can be used. Very similar to the TIP4P model is the OPC water model. It can be realized the same way as TIP4P but has different geometry and force field parameters.

There are two ways to implement TIP4P-like water in LAMMPS:

1.  Use a specially written pair style that uses the [[TIP3P geometry]{.std .std-ref}]Howto_tip3p.md#tip3p-molecule){.reference .internal} without the point M. The point M location is then implicitly derived from the other atoms or each water molecule and used during the force computation. The forces on M are then projected on the oxygen and the two hydrogen atoms. This is computationally very efficient, but the charge distribution in space is only correct within the tip4p labeled styles. So all other computations using charges will "see" the negative charge incorrectly located on the oxygen atom unless they are specially written for using the TIP4P geometry internally as well, e.g. [[compute dipole/tip4p]{.doc}]compute_dipole.md){.reference .internal}, [[fix efield/tip4p]{.doc}]fix_efield.md){.reference .internal}, or [[kspace_style pppm/tip4p]{.doc}]kspace_style.md){.reference .internal}.

    This can be done with the following pair styles for Coulomb with a cutoff:

    - [[pair_style tip4p/cut]{.doc}]pair_coul.md){.reference .internal}

    - [[pair_style lj/cut/tip4p/cut]{.doc}]pair_lj_cut_tip4p.md){.reference .internal}

    or these commands for a long-range Coulomb treatment:

    - [[pair_style tip4p/long]{.doc}]pair_coul.md){.reference .internal}

    - [[pair_style lj/cut/tip4p/long]{.doc}]pair_lj_cut_tip4p.md){.reference .internal}

    - [[pair_style lj/long/tip4p/long]{.doc}]pair_lj_long.md){.reference .internal}

    - [[pair_style tip4p/long/soft]{.doc}]pair_fep_soft.md){.reference .internal}

    - [[pair_style lj/cut/tip4p/long/soft]{.doc}]pair_fep_soft.md){.reference .internal}

    - [[kspace_style pppm/tip4p]{.doc}]kspace_style.md){.reference .internal}

    - [[kspace_style pppm/disp/tip4p]{.doc}]kspace_style.md){.reference .internal}

    The bond lengths and bond angles should be held fixed using the [[fix shake]{.doc}]fix_shake.md){.reference .internal} or [[fix rattle]{.doc}]fix_shake.md){.reference .internal} command, unless a parameterization for a flexible TIP4P model is used. The parameter sets listed below are all for rigid TIP4P model variants and thus the bond and angle force constants are not used and can be set to any legal value; only equilibrium length and angle are used.

2.  Use an [[explicit 4 point TIP4P geometry]{.std .std-ref}](#tip4p-molecule){.reference .internal} where the oxygen atom carries no charge and the M point no Lennard-Jones interactions. Since [[fix shake]{.doc}]fix_shake.md){.reference .internal} or [[fix rattle]{.doc}]fix_shake.md){.reference .internal} may not be applied to this kind of geometry, [[fix rigid or fix rigid/small]{.doc}]fix_rigid.md){.reference .internal} or its thermostatted variants are required to maintain a rigid geometry. This avoids some of the issues with respect to analysis and non-tip4p styles, but it is a more costly force computation (more atoms in the same volume and thus more neighbors in the neighbor lists) and requires a much shorter timestep for stable integration of the rigid body motion. Since no bonds or angles are required, they do not need to be defined and atom style charge would be sufficient for a bulk TIP4P water system. In order to avoid that LAMMPS produces an error due to the massless M site a tiny non-zero mass needs to be assigned.

The table below lists the force field parameters (in real [[units]{.doc}]units.md){.reference .internal}) to for a selection of popular variants of the TIP4P model. There is the rigid TIP4P model with a cutoff [[(Jorgensen)]{.std .std-ref}](#jorgensen5){.reference .internal}, the TIP4/Ice model [[(Abascal1)]{.std .std-ref}](#abascal1){.reference .internal}, the TIP4P/2005 model [[(Abascal2)]{.std .std-ref}](#abascal2){.reference .internal} and a version of TIP4P parameters adjusted for use with a long-range Coulombic solver (e.g. Ewald or PPPM in LAMMPS). Note that for implicit TIP4P models the OM distance is specified in the [[pair_style]{.doc}]pair_style.md){.reference .internal} command, not as part of the pair coefficients. Also parameters for the OPC model ([[Izadi]{.std .std-ref}](#izadi){.reference .internal}) are provided.

+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Parameter                                                                                                                 | TIP4P (original)                                          | TIP4P/Ice                                                 | TIP4P/2005                                                | TIP4P (Ewald)                                             | OPC                                                       |
+===========================================================================================================================+===========================================================+===========================================================+===========================================================+===========================================================+===========================================================+
| O mass (amu)                                                                                                              | 15.9994                                                   | 15.9994                                                   | 15.9994                                                   | 15.9994                                                   | 15.9994                                                   |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| H mass (amu)                                                                                                              | 1.008                                                     | 1.008                                                     | 1.008                                                     | 1.008                                                     | 1.008                                                     |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| O or M charge ([\\(e\\)]{.math .notranslate .nohighlight})                                                                | -1.040                                                    | -1.1794                                                   | -1.1128                                                   | -1.04844                                                  | -1.3582                                                   |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| H charge ([\\(e\\)]{.math .notranslate .nohighlight})                                                                     | 0.520                                                     | 0.5897                                                    | 0.5564                                                    | 0.52422                                                   | 0.6791                                                    |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\epsilon\\)]{.math .notranslate .nohighlight} of OO (kcal/mole)                                                   | 0.1550                                                    | 0.21084                                                   | 0.1852                                                    | 0.16275                                                   | 0.21280                                                   |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\sigma\\)]{.math .notranslate .nohighlight} of OO ([\\(\\AA\\)]{.math .notranslate .nohighlight})                 | 3.1536                                                    | 3.1668                                                    | 3.1589                                                    | 3.16435                                                   | 3.1660                                                    |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\epsilon\\)]{.math .notranslate .nohighlight} of HH, MM, OH, OM, HM (kcal/mole)                                   | 0.0                                                       | 0.0                                                       | 0.0                                                       | 0.0                                                       | 0.0                                                       |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\sigma\\)]{.math .notranslate .nohighlight} of HH, MM, OH, OM, HM ([\\(\\AA\\)]{.math .notranslate .nohighlight}) | 1.0                                                       | 1.0                                                       | 1.0                                                       | 1.0                                                       | 1.0                                                       |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [\\(r_0\\)]{.math .notranslate .nohighlight} of OH bond ([\\(\\AA\\)]{.math .notranslate .nohighlight})                   | 0.9572                                                    | 0.9572                                                    | 0.9572                                                    | 0.9572                                                    | 0.8724                                                    |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [\\(\\theta_0\\)]{.math .notranslate .nohighlight} of HOH angle                                                           | 104.52[\\(\^{\\circ}\\)]{.math .notranslate .nohighlight} | 104.52[\\(\^{\\circ}\\)]{.math .notranslate .nohighlight} | 104.52[\\(\^{\\circ}\\)]{.math .notranslate .nohighlight} | 104.52[\\(\^{\\circ}\\)]{.math .notranslate .nohighlight} | 103.60[\\(\^{\\circ}\\)]{.math .notranslate .nohighlight} |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| OM distance ([\\(\\AA\\)]{.math .notranslate .nohighlight})                                                               | 0.15                                                      | 0.1577                                                    | 0.1546                                                    | 0.1250                                                    | 0.1594                                                    |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

Note that the when using a TIP4P pair style, the neighbor list cutoff for Coulomb interactions is effectively extended by a distance 2 \* (OM distance), to account for the offset distance of the fictitious charges on O atoms in water molecules. Thus, it is typically best in an efficiency sense to use a LJ cutoff \>= Coulomb cutoff + 2\*(OM distance), to shrink the size of the neighbor list. This leads to slightly larger cost for the long-range calculation, so you can test the trade-off for your model. The OM distance and the LJ and Coulombic cutoffs are set in the [[pair_style lj/cut/tip4p/long]{.doc}]pair_lj_cut_tip4p.md){.reference .internal} command.

Below is the code for a LAMMPS input file using the implicit method and the [[TIP3P molecule file]{.std .std-ref}]Howto_tip3p.md#tip3p-molecule){.reference .internal}. Because the TIP4P charges are different from TIP3P they need to be reset (or the molecule file changed). For simplicity and speed the example uses a cutoff Coulomb. Most production simulations require long-range Coulomb instead.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    units real
    atom_style full
    region box block -5 5 -5 5 -5 5
    create_box 2 box bond/types 1 angle/types 1 &
                extra/bond/per/atom 2 extra/angle/per/atom 1 extra/special/per/atom 2

    mass 1 15.9994
    mass 2 1.008

    pair_style lj/cut/tip4p/cut 1 2 1 1 0.15 8.0
    pair_coeff 1 1 0.1550 3.1536
    pair_coeff 2 2 0.0    1.0

    bond_style zero
    bond_coeff 1 0.9574

    angle_style zero
    angle_coeff 1 104.52

    molecule water tip3p.mol  # this uses the TIP3P geometry
    create_atoms 0 random 33 34564 NULL mol water 25367 overlap 1.33
    # must change charges for TIP4P
    set type 1 charge -1.040
    set type 2 charge  0.520

    fix rigid all shake 0.001 10 10000 b 1 a 1
    minimize 0.0 0.0 1000 10000

    reset_timestep 0
    timestep 1.0
    velocity all create 300.0 5463576
    fix integrate all nvt temp 300 300 100.0

    thermo_style custom step temp press etotal pe

    thermo 1000
    run 20000
    write_data tip4p-implicit.data nocoeff
:::
::::

When constructing an OPC model, we cannot use the [`tip3p.mol`{.docutils .literal .notranslate}]{.pre} file due to the different geometry. Below is a molecule file providing the 3 sites of an implicit OPC geometry for use with TIP4P styles. Note, that the "Shake" and "Special" sections are missing here. Those will be auto-generated by LAMMPS when the molecule file is loaded *after* the simulation box has been created. These sections are required only when the molecule file is loaded *before*.

:::: {#opc3p-molecule .highlight-none .notranslate}
::: highlight
    # Water molecule. 3 point geometry for OPC model

    3 atoms
    2 bonds
    1 angles

    Coords

    1    0.00000  -0.06037   0.00000
    2    0.68558   0.50250   0.00000
    3   -0.68558   0.50250   0.00000

    Types

    1        1   # O
    2        2   # H
    3        2   # H

    Charges

    1       -1.3582
    2        0.6791
    3        0.6791

    Bonds

    1   1      1      2
    2   1      1      3

    Angles

    1   1      2      1      3
:::
::::

Below is a LAMMPS input file using the implicit method to implement the OPC model using the molecule file from above and including the PPPM long-range Coulomb solver.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    units real
    atom_style full
    region box block -5 5 -5 5 -5 5
    create_box 2 box bond/types 1 angle/types 1 &
                extra/bond/per/atom 2 extra/angle/per/atom 1 extra/special/per/atom 2

    mass 1 15.9994
    mass 2 1.008

    pair_style lj/cut/tip4p/long 1 2 1 1 0.1594 12.0
    pair_coeff 1 1 0.2128 3.166
    pair_coeff 2 2 0.0    1.0

    bond_style zero
    bond_coeff 1 0.8724

    angle_style zero
    angle_coeff 1 103.6

    kspace_style pppm/tip4p 1.0e-5

    molecule water opc3p.mol  # this file has the OPC geometry but is without M
    create_atoms 0 random 33 34564 NULL mol water 25367 overlap 1.33

    fix rigid all shake 0.001 10 10000 b 1 a 1
    minimize 0.0 0.0 1000 10000

    reset_timestep 0
    timestep 1.0
    velocity all create 300.0 5463576
    fix integrate all nvt temp 300 300 100.0

    thermo_style custom step temp press etotal pe

    thermo 1000
    run 20000
    write_data opc-implicit.data nocoeff
:::
::::

Below is the code for a LAMMPS input file using the explicit method and a TIP4P molecule file. Because of using [[fix rigid/small]{.doc}]fix_rigid.md){.reference .internal} no bonds need to be defined and thus no extra storage needs to be reserved for them, but we need to either switch to atom style full or use [[fix property/atom mol]{.doc}]fix_property_atom.md){.reference .internal} so that fix rigid/small can identify rigid bodies by their molecule ID. Also a [[neigh_modify exclude]{.doc}]neigh_modify.md){.reference .internal} command is added to exclude computing intramolecular non-bonded interactions, since those are removed by the rigid fix anyway:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    units real
    atom_style charge
    atom_modify map array
    region box block -5 5 -5 5 -5 5
    create_box 3 box

    mass 1 15.9994
    mass 2 1.008
    mass 3 1.0e-100

    pair_style lj/cut/coul/cut 8.0
    pair_coeff 1 1 0.1550 3.1536
    pair_coeff 2 2 0.0    1.0
    pair_coeff 3 3 0.0    1.0

    fix mol all property/atom mol ghost yes
    molecule water tip4p.mol
    create_atoms 0 random 33 34564 NULL mol water 25367 overlap 1.33
    neigh_modify exclude molecule/intra all

    timestep 0.5
    fix integrate all rigid/small molecule langevin 300.0 300.0 100.0 2345634

    thermo_style custom step temp press etotal density pe ke
    thermo 2000
    run 40000
    write_data tip4p-explicit.data nocoeff
:::
::::

:::: {#tip4p-molecule .highlight-none .notranslate}
::: highlight
    # Water molecule. Explicit TIP4P geometry for use with fix rigid

    4 atoms

    Coords

    1    0.00000  -0.06556   0.00000
    2    0.75695   0.52032   0.00000
    3   -0.75695   0.52032   0.00000
    4    0.00000   0.08444   0.00000

    Types

    1        1   # O
    2        2   # H
    3        2   # H
    4        3   # M

    Charges

    1        0.000
    2        0.520
    3        0.520
    4       -1.040
:::
::::

Wikipedia also has a nice article on [water models](https://en.wikipedia.org/wiki/Water_model){.reference .external}.

------------------------------------------------------------------------

**(Jorgensen)** Jorgensen, Chandrasekhar, Madura, Impey, Klein, J Chem Phys, 79, 926 (1983).

**(Abascal1)** Abascal, Sanz, Fernandez, Vega, J Chem Phys, 122, 234511 (2005)

:   [https://doi.org/10.1063/1.1931662](https://doi.org/10.1063/1.1931662){.reference .external}

<!-- -->

**(Abascal2)** Abascal, J Chem Phys, 123, 234505 (2005)

:   [https://doi.org/10.1063/1.2121687](https://doi.org/10.1063/1.2121687){.reference .external}

<!-- -->

**(Izadi)** Izadi, Anandakrishnan, Onufriev, J. Phys. Chem. Lett., 5, 21, 3863 (2014)

:   [https://doi.org/10.1021/jz501780a](https://doi.org/10.1021/jz501780a){.reference .external}
:::::::::::::
::::::::::::::
:::::::::::::::

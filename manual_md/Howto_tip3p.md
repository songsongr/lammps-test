::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::: {#tip3p-water-model .section}
# [10.4.5. ]{.section-number}TIP3P water model[](#tip3p-water-model "Link to this heading"){.headerlink}

The TIP3P water model as implemented in CHARMM [[(MacKerell)]{.std .std-ref}](#howto-tip3p){.reference .internal} specifies a 3-site rigid water molecule with charges and Lennard-Jones parameters assigned to each of the three atoms.

One suitable pair style with cutoff Coulomb would for instance be:

- [[pair_style lj/cut/coul/cut]{.doc}]pair_lj_cut_coul.md){.reference .internal}

These commands are examples for a long-range Coulomb model:

- [[pair_style lj/cut/coul/long]{.doc}]pair_lj_cut_coul.md){.reference .internal}

- [[pair_style lj/cut/coul/long/soft]{.doc}]pair_fep_soft.md){.reference .internal}

- [[kspace_style pppm]{.doc}]kspace_style.md){.reference .internal}

- [[pair_style lj/long/coul/long]{.doc}]pair_lj_long.md){.reference .internal}

- [[kspace_style pppm/disp]{.doc}]kspace_style.md){.reference .internal}

And these pair styles are compatible with the CHARMM force field:

- [[pair_style lj/charmm/coul/charmm]{.doc}]pair_charmm.md){.reference .internal}

- [[pair_style lj/charmm/coul/long]{.doc}]pair_charmm.md){.reference .internal}

- [[pair_style lj/charmmfsw/coul/long]{.doc}]pair_charmm.md){.reference .internal}

In LAMMPS the [[fix shake or fix rattle]{.doc}]fix_shake.md){.reference .internal} command can be used to hold the two O-H bonds and the H-O-H angle rigid. A bond style of [[harmonic]{.doc}]bond_harmonic.md){.reference .internal} and an angle style of [[harmonic]{.doc}]angle_harmonic.md){.reference .internal} or [[charmm]{.doc}]angle_charmm.md){.reference .internal} should also be used. In case of rigid bonds also bond style [[zero]{.doc}]bond_zero.md){.reference .internal} and angle style [[zero]{.doc}]angle_zero.md){.reference .internal} can be used.

The table below lists the force field parameters (in real [[units]{.doc}]units.md){.reference .internal}) to for the water molecule atoms to run a rigid or flexible TIP3P-CHARMM model with a cutoff, the original 1983 TIP3P model [[(Jorgensen)]{.std .std-ref}](#jorgensen1){.reference .internal}, or a TIP3P model with parameters optimized for a long-range Coulomb solver (e.g. Ewald or PPPM in LAMMPS) [[(Price)]{.std .std-ref}](#price1){.reference .internal}. The K values can be used if a flexible TIP3P model (without fix shake) is desired, for rigid bonds/angles they are ignored.

+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Parameter                                                                                                 | TIP3P-CHARMM                                              | TIP3P (original)                                          | TIP3P (Ewald)                                             |
+===========================================================================================================+===========================================================+===========================================================+===========================================================+
| O mass (amu)                                                                                              | 15.9994                                                   | 15.9994                                                   | 15.9994                                                   |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| H mass (amu)                                                                                              | 1.008                                                     | 1.008                                                     | 1.008                                                     |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| O charge ([\\(e\\)]{.math .notranslate .nohighlight})                                                     | -0.834                                                    | -0.834                                                    | -0.834                                                    |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| H charge ([\\(e\\)]{.math .notranslate .nohighlight})                                                     | 0.417                                                     | 0.417                                                     | 0.417                                                     |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\epsilon\\)]{.math .notranslate .nohighlight} of OO (kcal/mole)                                   | 0.1521                                                    | 0.1521                                                    | 0.1020                                                    |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\sigma\\)]{.math .notranslate .nohighlight} of OO ([\\(\\AA\\)]{.math .notranslate .nohighlight}) | 3.1507                                                    | 3.1507                                                    | 3.188                                                     |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\epsilon\\)]{.math .notranslate .nohighlight} of HH (kcal/mole)                                   | 0.0460                                                    | 0.0                                                       | 0.0                                                       |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\sigma\\)]{.math .notranslate .nohighlight} of HH ([\\(\\AA\\)]{.math .notranslate .nohighlight}) | 0.4                                                       | 1.0                                                       | 1.0                                                       |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\epsilon\\)]{.math .notranslate .nohighlight} of OH (kcal/mole)                                   | 0.0836                                                    | 0.0                                                       | 0.0                                                       |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| LJ [\\(\\sigma\\)]{.math .notranslate .nohighlight} of OH ([\\(\\AA\\)]{.math .notranslate .nohighlight}) | 1.7753                                                    | 1.0                                                       | 1.0                                                       |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| K of OH bond (kcal/mole/[\\(\\AA\^2\\)]{.math .notranslate .nohighlight})                                 | 450                                                       | 450                                                       | 450                                                       |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [\\(r_0\\)]{.math .notranslate .nohighlight} of OH bond ([\\(\\AA\\)]{.math .notranslate .nohighlight})   | 0.9572                                                    | 0.9572                                                    | 0.9572                                                    |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| K of HOH angle (kcal/mole)                                                                                | 55.0                                                      | 55.0                                                      | 55.0                                                      |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [\\(\\theta_0\\)]{.math .notranslate .nohighlight} of HOH angle                                           | 104.52[\\(\^{\\circ}\\)]{.math .notranslate .nohighlight} | 104.52[\\(\^{\\circ}\\)]{.math .notranslate .nohighlight} | 104.52[\\(\^{\\circ}\\)]{.math .notranslate .nohighlight} |
+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

Below is the code for a LAMMPS input file and a molecule file ([`tip3p.mol`{.docutils .literal .notranslate}]{.pre}) of TIP3P water for use with the [[molecule command]{.doc}]molecule.md){.reference .internal} demonstrating how to set up a small bulk water system for TIP3P with rigid bonds. For simplicity and speed the example uses a cutoff Coulomb. Most production simulations require long-range Coulomb instead.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    units real
    atom_style full
    region box block -5 5 -5 5 -5 5
    create_box 2 box bond/types 1 angle/types 1 &
                extra/bond/per/atom 2 extra/angle/per/atom 1 extra/special/per/atom 2

    mass 1 15.9994
    mass 2 1.008

    pair_style lj/cut/coul/cut 8.0
    pair_coeff 1 1 0.1521 3.1507
    pair_coeff 2 2 0.0    1.0

    bond_style zero
    bond_coeff 1 0.9574

    angle_style zero
    angle_coeff 1 104.52

    molecule water tip3p.mol
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
    write_data tip3p.data nocoeff
:::
::::

:::: {#tip3p-molecule .highlight-none .notranslate}
::: highlight
    # Water molecule. TIP3P geometry

    3 atoms
    2 bonds
    1 angles

    Coords

    1    0.00000  -0.06556   0.00000
    2    0.75695   0.52032   0.00000
    3   -0.75695   0.52032   0.00000

    Types

    1        1   # O
    2        2   # H
    3        2   # H

    Charges

    1       -0.834
    2        0.417
    3        0.417

    Bonds

    1   1      1      2
    2   1      1      3

    Angles

    1   1      2      1      3

    Shake Flags

    1 1
    2 1
    3 1

    Shake Atoms

    1 1 2 3
    2 1 2 3
    3 1 2 3

    Shake Bond Types

    1 1 1 1
    2 1 1 1
    3 1 1 1

    Special Bond Counts

    1 2 0 0
    2 1 1 0
    3 1 1 0

    Special Bonds

    1 2 3
    2 1 3
    3 1 2
:::
::::

Wikipedia also has a nice article on [water models](https://en.wikipedia.org/wiki/Water_model){.reference .external}.

------------------------------------------------------------------------

**(MacKerell)** MacKerell, Bashford, Bellott, Dunbrack, Evanseck, Field, Fischer, Gao, Guo, Ha, et al, J Phys Chem, 102, 3586 (1998).

**(Jorgensen)** Jorgensen, Chandrasekhar, Madura, Impey, Klein, J Chem Phys, 79, 926 (1983).

**(Price)** Price and Brooks, J Chem Phys, 121, 10096 (2004).
:::::::
::::::::
:::::::::

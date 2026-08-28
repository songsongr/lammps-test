::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#pair-style-command .section}
[]{#index-0}

# pair_style command[](#pair-style-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = one of the styles from the list below

- args = arguments used by a particular style
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style lj/cut 2.5
    pair_style eam/alloy
    pair_style hybrid lj/charmm/coul/long 10.0 eam
    pair_style table linear 1000
    pair_style none
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set the formula(s) LAMMPS uses to compute pairwise interactions. In LAMMPS, pair potentials are defined between pairs of atoms that are within a cutoff distance and the set of active interactions typically changes over time. See the [[bond_style]{.doc}]bond_style.md){.reference .internal} command to define potentials between pairs of bonded atoms, which typically remain in place for the duration of a simulation.

In LAMMPS, pairwise force fields encompass a variety of interactions, some of which include many-body effects, e.g. EAM, Stillinger-Weber, Tersoff, REBO potentials. They are still classified as "pairwise" potentials because the set of interacting atoms changes with time (unlike molecular bonds) and thus a neighbor list is used to find nearby interacting atoms.

Hybrid models where specified pairs of atom types interact via different pair potentials can be setup using the *hybrid* pair style.

The coefficients associated with a pair style are typically set for each pair of atom types, and are specified by the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command or read from a file by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} command sets options for mixing of type I-J interaction coefficients and adding energy offsets or tail corrections to Lennard-Jones potentials. Details on these options as they pertain to individual potentials are described on the doc page for the potential. Likewise, info on whether the potential information is stored in a [[restart file]{.doc}]write_restart.md){.reference .internal} is listed on the potential doc page.

In the formulas listed for each pair style, *E* is the energy of a pairwise interaction between two atoms separated by a distance *r*. The force between the atoms is the negative derivative of this expression.

If the pair_style command has a cutoff argument, it sets global cutoffs for all pairs of atom types. The distance(s) can be smaller or larger than the dimensions of the simulation box.

In many cases, the global cutoff value can be overridden for a specific pair of atom types by the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command.

If a new pair_style command is specified with a new style, all previous [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} and [[pair_modify]{.doc}]pair_modify.md){.reference .internal} command settings are erased; those commands must be re-specified if necessary.

If a new pair_style command is specified with the same style, then only the global settings in that command are reset. Any previous doc:pair_coeff \<pair_coeff\> and [[pair_modify]{.doc}]pair_modify.md){.reference .internal} command settings are preserved. The only exception is that if the global cutoff in the pair_style command is changed, it will override the corresponding cutoff in any of the previous [[pair_modify]{.doc}]pair_coeff.md){.reference .internal} commands.

Two pair styles which do not follow this rule are the pair_style *table* and *hybrid* commands. A new pair_style command for these styles will wipe out all previously specified [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} and [[pair_modify]{.doc}]pair_modify.md){.reference .internal} settings, including for the sub-styles of the *hybrid* command.

------------------------------------------------------------------------

Here is an alphabetic list of pair styles defined in LAMMPS. They are also listed in more compact form on the [[Commands pair]{.doc}]Commands_pair.md){.reference .internal} doc page.

Click on the style to display the formula it computes, any additional arguments specified in the pair_style command, and coefficients specified by the associated [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command.

There are also additional accelerated pair styles included in the LAMMPS distribution for faster performance on CPUs, GPUs, and KNLs. The individual style names on the [[Commands pair]{.doc}]Commands_pair.md){.reference .internal} doc page are followed by one or more of (g,i,k,o,t) to indicate which accelerated styles exist.

- [[none]{.doc}]pair_none.md){.reference .internal} - turn off pairwise interactions

- [[hybrid]{.doc}]pair_hybrid.md){.reference .internal} - multiple styles of pairwise interactions

- [[hybrid/molecular]{.doc}]pair_hybrid.md){.reference .internal} - different pair styles for intra- and inter-molecular interactions

- [[hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} - multiple styles of superposed pairwise interactions

- [[hybrid/scaled]{.doc}]pair_hybrid.md){.reference .internal} - multiple styles of scaled superposed pairwise interactions

- [[zero]{.doc}]pair_zero.md){.reference .internal} - neighbor list but no interactions

- [[adp]{.doc}]pair_adp.md){.reference .internal} - angular dependent potential (ADP) of Mishin

- [[agni]{.doc}]pair_agni.md){.reference .internal} - AGNI machine-learning potential

- [[aip/water/2dm]{.doc}]pair_aip_water_2dm.md){.reference .internal} - anisotropic interfacial potential for water in 2d geometries

- [[airebo]{.doc}]pair_airebo.md){.reference .internal} - AIREBO potential of Stuart

- [[airebo/morse]{.doc}]pair_airebo.md){.reference .internal} - AIREBO with Morse instead of LJ

- [[amoeba]{.doc}]pair_amoeba.md){.reference .internal} -

- [[atm]{.doc}]pair_atm.md){.reference .internal} - Axilrod-Teller-Muto potential

- [[beck]{.doc}]pair_beck.md){.reference .internal} - Beck potential

- [[body/nparticle]{.doc}]pair_body_nparticle.md){.reference .internal} - interactions between body particles

- [[body/rounded/polygon]{.doc}]pair_body_rounded_polygon.md){.reference .internal} - granular-style 2d polygon potential

- [[body/rounded/polyhedron]{.doc}]pair_body_rounded_polyhedron.md){.reference .internal} - granular-style 3d polyhedron potential

- [[bop]{.doc}]pair_bop.md){.reference .internal} - BOP potential of Pettifor

- [[born]{.doc}]pair_born.md){.reference .internal} - Born-Mayer-Huggins potential

- [[born/coul/dsf]{.doc}]pair_born.md){.reference .internal} - Born with damped-shifted-force model

- [[born/coul/dsf/cs]{.doc}]pair_cs.md){.reference .internal} - Born with damped-shifted-force and core/shell model

- [[born/coul/long]{.doc}]pair_born.md){.reference .internal} - Born with long-range Coulomb

- [[born/coul/long/cs]{.doc}]pair_cs.md){.reference .internal} - Born with long-range Coulomb and core/shell

- [[born/coul/msm]{.doc}]pair_born.md){.reference .internal} - Born with long-range MSM Coulomb

- [[born/coul/wolf]{.doc}]pair_born.md){.reference .internal} - Born with Wolf potential for Coulomb

- [[born/coul/wolf/cs]{.doc}]pair_cs.md){.reference .internal} - Born with Wolf potential for Coulomb and core/shell model

- [[born/gauss]{.doc}]pair_born_gauss.md){.reference .internal} - Born-Mayer / Gaussian potential

- [[bpm/spring]{.doc}]pair_bpm_spring.md){.reference .internal} - repulsive harmonic force with damping

- [[brownian]{.doc}]pair_brownian.md){.reference .internal} - Brownian potential for Fast Lubrication Dynamics

- [[brownian/poly]{.doc}]pair_brownian.md){.reference .internal} - Brownian potential for Fast Lubrication Dynamics with polydispersity

- [[buck]{.doc}]pair_buck.md){.reference .internal} - Buckingham potential

- [[buck/coul/cut]{.doc}]pair_buck.md){.reference .internal} - Buckingham with cutoff Coulomb

- [[buck/coul/long]{.doc}]pair_buck.md){.reference .internal} - Buckingham with long-range Coulomb

- [[buck/coul/long/cs]{.doc}]pair_cs.md){.reference .internal} - Buckingham with long-range Coulomb and core/shell

- [[buck/coul/msm]{.doc}]pair_buck.md){.reference .internal} - Buckingham with long-range MSM Coulomb

- [[buck/long/coul/long]{.doc}]pair_buck_long.md){.reference .internal} - long-range Buckingham with long-range Coulomb

- [[buck/mdf]{.doc}]pair_mdf.md){.reference .internal} - Buckingham with a taper function

- [[buck6d/coul/gauss/dsf]{.doc}]pair_buck6d_coul_gauss.md){.reference .internal} - dispersion-damped Buckingham with damped-shift-force model

- [[buck6d/coul/gauss/long]{.doc}]pair_buck6d_coul_gauss.md){.reference .internal} - dispersion-damped Buckingham with long-range Coulomb

- [[colloid]{.doc}]pair_colloid.md){.reference .internal} - integrated colloidal potential

- [[comb]{.doc}]pair_comb.md){.reference .internal} - charge-optimized many-body (COMB) potential

- [[comb3]{.doc}]pair_comb.md){.reference .internal} - charge-optimized many-body (COMB3) potential

- [[cosine/squared]{.doc}]pair_cosine_squared.md){.reference .internal} - Cooke-Kremer-Deserno membrane model potential

- [[coul/ctip]{.doc}]pair_coul.md){.reference .internal} - Charge Transfer Interatomic (Coulomb) Potential

- [[coul/cut]{.doc}]pair_coul.md){.reference .internal} - cutoff Coulomb potential

- [[coul/cut/dielectric]{.doc}]pair_dielectric.md){.reference .internal} -

- [[coul/cut/global]{.doc}]pair_coul.md){.reference .internal} - cutoff Coulomb potential

- [[coul/cut/soft]{.doc}]pair_fep_soft.md){.reference .internal} - Coulomb potential with a soft core

- [[coul/debye]{.doc}]pair_coul.md){.reference .internal} - cutoff Coulomb potential with Debye screening

- [[coul/diel]{.doc}]pair_coul_diel.md){.reference .internal} - Coulomb potential with dielectric permittivity

- [[coul/dsf]{.doc}]pair_coul.md){.reference .internal} - Coulomb with damped-shifted-force model

- [[coul/exclude]{.doc}]pair_coul.md){.reference .internal} - subtract Coulomb potential for excluded pairs

- [[coul/long]{.doc}]pair_coul.md){.reference .internal} - long-range Coulomb potential

- [[coul/long/cs]{.doc}]pair_cs.md){.reference .internal} - long-range Coulomb potential and core/shell

- [[coul/long/dielectric]{.doc}]pair_dielectric.md){.reference .internal} -

- [[coul/long/soft]{.doc}]pair_fep_soft.md){.reference .internal} - long-range Coulomb potential with a soft core

- [[coul/msm]{.doc}]pair_coul.md){.reference .internal} - long-range MSM Coulomb

- [[coul/slater/cut]{.doc}]pair_coul.md){.reference .internal} - smeared out Coulomb

- [[coul/slater/long]{.doc}]pair_coul.md){.reference .internal} - long-range smeared out Coulomb

- [[coul/shield]{.doc}]pair_coul_shield.md){.reference .internal} - Coulomb for boron nitride for use with [[ilp/graphene/hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal} potential

- [[coul/streitz]{.doc}]pair_coul.md){.reference .internal} - Coulomb via Streitz/Mintmire Slater orbitals

- [[coul/tt]{.doc}]pair_coul_tt.md){.reference .internal} - damped charge-dipole Coulomb for Drude dipoles

- [[coul/wolf]{.doc}]pair_coul.md){.reference .internal} - Coulomb via Wolf potential

- [[coul/wolf/cs]{.doc}]pair_cs.md){.reference .internal} - Coulomb via Wolf potential with core/shell adjustments

- [[dispersion/d3]{.doc}]pair_dispersion_d3.md){.reference .internal} - Dispersion correction for potentials derived from DFT functionals

- [[dpd]{.doc}]pair_dpd.md){.reference .internal} - dissipative particle dynamics (DPD)

- [[dpd/coul/slater/long]{.doc}]pair_dpd_coul_slater_long.md){.reference .internal} - dissipative particle dynamics (DPD) with electrostatic interactions

- [[dpd/ext]{.doc}]pair_dpd_ext.md){.reference .internal} - generalized force field for DPD

- [[dpd/ext/tstat]{.doc}]pair_dpd_ext.md){.reference .internal} - pairwise DPD thermostatting with generalized force field

- [[dpd/fdt]{.doc}]pair_dpd_fdt.md){.reference .internal} - DPD for constant temperature and pressure

- [[dpd/fdt/energy]{.doc}]pair_dpd_fdt.md){.reference .internal} - DPD for constant energy and enthalpy

- [[dpd/tstat]{.doc}]pair_dpd.md){.reference .internal} - pairwise DPD thermostatting

- [[dsmc]{.doc}]pair_dsmc.md){.reference .internal} - Direct Simulation Monte Carlo (DSMC)

- [[e3b]{.doc}]pair_e3b.md){.reference .internal} - Explicit-three body (E3B) water model

- [[drip]{.doc}]pair_drip.md){.reference .internal} - Dihedral-angle-corrected registry-dependent interlayer potential (DRIP)

- [[eam]{.doc}]pair_eam.md){.reference .internal} - embedded atom method (EAM)

- [[eam/alloy]{.doc}]pair_eam.md){.reference .internal} - alloy EAM

- [[eam/cd]{.doc}]pair_eam.md){.reference .internal} - concentration-dependent EAM

- [[eam/cd/old]{.doc}]pair_eam.md){.reference .internal} - older two-site model for concentration-dependent EAM

- [[eam/fs]{.doc}]pair_eam.md){.reference .internal} - Finnis-Sinclair EAM

- [[eam/fs/apip]{.doc}]pair_eam_apip.md){.reference .internal} - [[adaptive precision]{.doc}]Howto_apip.md){.reference .internal} version of FS EAM, used as fast potential

- [[eam/he]{.doc}]pair_eam.md){.reference .internal} - Finnis-Sinclair EAM modified for Helium in metals

- [[eam/apip]{.doc}]pair_eam_apip.md){.reference .internal} - [[adaptive-precision]{.doc}]Howto_apip.md){.reference .internal} version of EAM, used as fast potential

- [[edip]{.doc}]pair_edip.md){.reference .internal} - three-body EDIP potential

- [[edip/multi]{.doc}]pair_edip.md){.reference .internal} - multi-element EDIP potential

- [[edpd]{.doc}]pair_mesodpd.md){.reference .internal} - eDPD particle interactions

- [[eff/cut]{.doc}]pair_eff.md){.reference .internal} - electron force field with a cutoff

- [[eim]{.doc}]pair_eim.md){.reference .internal} - embedded ion method (EIM)

- [[exp6/rx]{.doc}]pair_exp6_rx.md){.reference .internal} - reactive DPD potential

- [[extep]{.doc}]pair_extep.md){.reference .internal} - extended Tersoff potential

- [[gauss]{.doc}]pair_gauss.md){.reference .internal} - Gaussian potential

- [[gauss/cut]{.doc}]pair_gauss.md){.reference .internal} - generalized Gaussian potential

- [[gayberne]{.doc}]pair_gayberne.md){.reference .internal} - Gay-Berne ellipsoidal potential

- [[granular]{.doc}]pair_granular.md){.reference .internal} - Generalized granular potential

- [[granular/superellipsoid]{.doc}]pair_granular_superellipsoid.md){.reference .internal} - Generalized granular potential for superellipsoids

- [[gran/hertz/history]{.doc}]pair_gran.md){.reference .internal} - granular potential with Hertzian interactions

- [[gran/hooke]{.doc}]pair_gran.md){.reference .internal} - granular potential without history effects

- [[gran/hooke/history]{.doc}]pair_gran.md){.reference .internal} - granular potential with history effects

- [[gw]{.doc}]pair_gw.md){.reference .internal} - Gao-Weber potential

- [[gw/zbl]{.doc}]pair_gw.md){.reference .internal} - Gao-Weber potential with a repulsive ZBL core

- [[harmonic/cut]{.doc}]pair_harmonic_cut.md){.reference .internal} - repulsive-only harmonic potential

- [[hbond/dreiding/lj]{.doc}]pair_hbond_dreiding.md){.reference .internal} - DREIDING hydrogen bonding LJ potential

- [[hbond/dreiding/lj/angleoffset]{.doc}]pair_hbond_dreiding.md){.reference .internal} - DREIDING hydrogen bonding LJ potential with offset for hbond angle

- [[hbond/dreiding/morse]{.doc}]pair_hbond_dreiding.md){.reference .internal} - DREIDING hydrogen bonding Morse potential

- [[hbond/dreiding/morse/angleoffset]{.doc}]pair_hbond_dreiding.md){.reference .internal} - DREIDING hydrogen bonding Morse potential with offset for hbond angle

- [[hdnnp]{.doc}]pair_hdnnp.md){.reference .internal} - High-dimensional neural network potential

- [[hippo]{.doc}]pair_amoeba.md){.reference .internal} -

- [[ilp/graphene/hbn]{.doc}]pair_ilp_graphene_hbn.md){.reference .internal} - registry-dependent interlayer potential (ILP)

- [[ilp/tmd]{.doc}]pair_ilp_tmd.md){.reference .internal} - interlayer potential (ILP) potential for transition metal dichalcogenides (TMD)

- [[kim]{.doc}]pair_kim.md){.reference .internal} - interface to potentials provided by KIM project

- [[kolmogorov/crespi/full]{.doc}]pair_kolmogorov_crespi_full.md){.reference .internal} - Kolmogorov-Crespi (KC) potential with no simplifications

- [[kolmogorov/crespi/z]{.doc}]pair_kolmogorov_crespi_z.md){.reference .internal} - Kolmogorov-Crespi (KC) potential with normals along z-axis

- [[lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal} - constant as input for the precision calculation of an [[adaptive-precision interatomic potential (APIP)]{.doc}]Howto_apip.md){.reference .internal}

- [[lambda/input/csp/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal} - CSP as input for the precision calculation of an [[adaptive-precision interatomic potential (APIP)]{.doc}]Howto_apip.md){.reference .internal}

- [[lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal} - transition zone of an [[adaptive-precision interatomic potential]{.doc}]Howto_apip.md){.reference .internal}

- [[lcbop]{.doc}]pair_lcbop.md){.reference .internal} - long-range bond-order potential (LCBOP)

- [[lebedeva/z]{.doc}]pair_lebedeva_z.md){.reference .internal} - Lebedeva interlayer potential for graphene with normals along z-axis

- [[lennard/mdf]{.doc}]pair_mdf.md){.reference .internal} - LJ potential in A/B form with a taper function

- [[lepton]{.doc}]pair_lepton.md){.reference .internal} - pair potential from evaluating a string

- [[lepton/coul]{.doc}]pair_lepton.md){.reference .internal} - pair potential from evaluating a string with support for charges

- [[lepton/sphere]{.doc}]pair_lepton.md){.reference .internal} - pair potential from evaluating a string with support for radii

- [[line/lj]{.doc}]pair_line_lj.md){.reference .internal} - LJ potential between line segments

- [[list]{.doc}]pair_list.md){.reference .internal} - potential between pairs of atoms explicitly listed in an input file

- [[lj/charmm/coul/charmm]{.doc}]pair_charmm.md){.reference .internal} - CHARMM potential with cutoff Coulomb

- [[lj/charmm/coul/charmm/implicit]{.doc}]pair_charmm.md){.reference .internal} - CHARMM for implicit solvent

- [[lj/charmm/coul/long]{.doc}]pair_charmm.md){.reference .internal} - CHARMM with long-range Coulomb

- [[lj/charmm/coul/long/soft]{.doc}]pair_fep_soft.md){.reference .internal} - CHARMM with long-range Coulomb and a soft core

- [[lj/charmm/coul/msm]{.doc}]pair_charmm.md){.reference .internal} - CHARMM with long-range MSM Coulomb

- [[lj/charmmfsw/coul/charmmfsh]{.doc}]pair_charmm.md){.reference .internal} - CHARMM with force switching and shifting

- [[lj/charmmfsw/coul/long]{.doc}]pair_charmm.md){.reference .internal} - CHARMM with force switching and long-rnage Coulomb

- [[lj/class2]{.doc}]pair_class2.md){.reference .internal} - COMPASS (class 2) force field without Coulomb

- [[lj/class2/coul/cut]{.doc}]pair_class2.md){.reference .internal} - COMPASS with cutoff Coulomb

- [[lj/class2/coul/cut/soft]{.doc}]pair_fep_soft.md){.reference .internal} - COMPASS with cutoff Coulomb with a soft core

- [[lj/class2/coul/long]{.doc}]pair_class2.md){.reference .internal} - COMPASS with long-range Coulomb

- [[lj/class2/coul/long/cs]{.doc}]pair_cs.md){.reference .internal} - COMPASS with long-range Coulomb with core/shell adjustments

- [[lj/class2/coul/long/soft]{.doc}]pair_fep_soft.md){.reference .internal} - COMPASS with long-range Coulomb with a soft core

- [[lj/class2/soft]{.doc}]pair_fep_soft.md){.reference .internal} - COMPASS (class 2) force field with no Coulomb with a soft core

- [[lj/cubic]{.doc}]pair_lj_cubic.md){.reference .internal} - LJ with cubic after inflection point

- [[lj/cut]{.doc}]pair_lj.md){.reference .internal} - cutoff Lennard-Jones potential without Coulomb

- [[lj/cut/coul/cut]{.doc}]pair_lj_cut_coul.md){.reference .internal} - LJ with cutoff Coulomb

- [[lj/cut/coul/cut/dielectric]{.doc}]pair_dielectric.md){.reference .internal} -

- [[lj/cut/coul/cut/soft]{.doc}]pair_fep_soft.md){.reference .internal} - LJ with cutoff Coulomb with a soft core

- [[lj/cut/coul/debye]{.doc}]pair_lj_cut_coul.md){.reference .internal} - LJ with Debye screening added to Coulomb

- [[lj/cut/coul/debye/dielectric]{.doc}]pair_dielectric.md){.reference .internal} -

- [[lj/cut/coul/dsf]{.doc}]pair_lj_cut_coul.md){.reference .internal} - LJ with Coulomb via damped shifted forces

- [[lj/cut/coul/long]{.doc}]pair_lj_cut_coul.md){.reference .internal} - LJ with long-range Coulomb

- [[lj/cut/coul/long/cs]{.doc}]pair_cs.md){.reference .internal} - LJ with long-range Coulomb with core/shell adjustments

- [[lj/cut/coul/long/dielectric]{.doc}]pair_dielectric.md){.reference .internal} -

- [[lj/cut/coul/long/soft]{.doc}]pair_fep_soft.md){.reference .internal} - LJ with long-range Coulomb with a soft core

- [[lj/cut/coul/msm]{.doc}]pair_lj_cut_coul.md){.reference .internal} - LJ with long-range MSM Coulomb

- [[lj/cut/coul/msm/dielectric]{.doc}]pair_dielectric.md){.reference .internal} -

- [[lj/cut/coul/wolf]{.doc}]pair_lj_cut_coul.md){.reference .internal} - LJ with Coulomb via Wolf potential

- [[lj/cut/dipole/cut]{.doc}]pair_dipole.md){.reference .internal} - point dipoles with cutoff

- [[lj/cut/dipole/long]{.doc}]pair_dipole.md){.reference .internal} - point dipoles with long-range Ewald

- [[lj/cut/soft]{.doc}]pair_fep_soft.md){.reference .internal} - LJ with a soft core

- [[lj/cut/sphere]{.doc}]pair_lj_cut_sphere.md){.reference .internal} - LJ where per-atom radius is used as LJ sigma

- [[lj/cut/thole/long]{.doc}]pair_thole.md){.reference .internal} - LJ with Coulomb with thole damping

- [[lj/cut/tip4p/cut]{.doc}]pair_lj_cut_tip4p.md){.reference .internal} - LJ with cutoff Coulomb for TIP4P water

- [[lj/cut/tip4p/long]{.doc}]pair_lj_cut_tip4p.md){.reference .internal} - LJ with long-range Coulomb for TIP4P water

- [[lj/cut/tip4p/long/soft]{.doc}]pair_fep_soft.md){.reference .internal} - LJ with cutoff Coulomb for TIP4P water with a soft core

- [[lj/expand]{.doc}]pair_lj_expand.md){.reference .internal} - Lennard-Jones for variable size particles

- [[lj/expand/coul/long]{.doc}]pair_lj_expand.md){.reference .internal} - Lennard-Jones for variable size particles with long-range Coulomb

- [[lj/expand/sphere]{.doc}]pair_lj_expand_sphere.md){.reference .internal} - Variable size LJ where per-atom radius is used as delta (size)

- [[lj/gromacs]{.doc}]pair_gromacs.md){.reference .internal} - GROMACS-style Lennard-Jones potential

- [[lj/gromacs/coul/gromacs]{.doc}]pair_gromacs.md){.reference .internal} - GROMACS-style LJ and Coulomb potential

- [[lj/long/coul/long]{.doc}]pair_lj_long.md){.reference .internal} - long-range LJ and long-range Coulomb

- [[lj/long/coul/long/dielectric]{.doc}]pair_dielectric.md){.reference .internal} -

- [[lj/long/dipole/long]{.doc}]pair_dipole.md){.reference .internal} - long-range LJ and long-range point dipoles

- [[lj/long/tip4p/long]{.doc}]pair_lj_long.md){.reference .internal} - long-range LJ and long-range Coulomb for TIP4P water

- [[lj/mdf]{.doc}]pair_mdf.md){.reference .internal} - LJ potential with a taper function

- [[lj/pirani]{.doc}]pair_lj_pirani.md){.reference .internal} - Improved LJ potential

- [[lj/relres]{.doc}]pair_lj_relres.md){.reference .internal} - LJ using multiscale Relative Resolution (RelRes) methodology [[(Chaimovich)]{.std .std-ref}]pair_lj_relres.md#chaimovich2){.reference .internal}.

- [[lj/spica]{.doc}]pair_spica.md){.reference .internal} - LJ for SPICA coarse-graining

- [[lj/spica/coul/long]{.doc}]pair_spica.md){.reference .internal} - LJ for SPICA coarse-graining with long-range Coulomb

- [[lj/spica/coul/msm]{.doc}]pair_spica.md){.reference .internal} - LJ for SPICA coarse-graining with long-range Coulomb via MSM

- [[lj/sf/dipole/sf]{.doc}]pair_dipole.md){.reference .internal} - LJ with dipole interaction with shifted forces

- [[lj/smooth]{.doc}]pair_lj_smooth.md){.reference .internal} - smoothed Lennard-Jones potential

- [[lj/smooth/linear]{.doc}]pair_lj_smooth_linear.md){.reference .internal} - linear smoothed LJ potential

- [[lj/switch3/coulgauss/long]{.doc}]pair_lj_switch3_coulgauss_long.md){.reference .internal} - smoothed LJ vdW potential with Gaussian electrostatics

- [[lj96/cut]{.doc}]pair_lj96.md){.reference .internal} - Lennard-Jones 9/6 potential

- [[local/density]{.doc}]pair_local_density.md){.reference .internal} - Generalized basic local density potential

- [[lubricate]{.doc}]pair_lubricate.md){.reference .internal} - Hydrodynamic lubrication forces

- [[lubricate/poly]{.doc}]pair_lubricate.md){.reference .internal} - Hydrodynamic lubrication forces with polydispersity

- [[lubricateU]{.doc}]pair_lubricateU.md){.reference .internal} - Hydrodynamic lubrication forces for Fast Lubrication Dynamics

- [[lubricateU/poly]{.doc}]pair_lubricateU.md){.reference .internal} - Hydrodynamic lubrication forces for Fast Lubrication with polydispersity

- [[mbx]{.doc}]pair_mbx.md){.reference .internal} - Many-Body eXpansion (MBX) potential

- [[mdpd]{.doc}]pair_mesodpd.md){.reference .internal} - mDPD particle interactions

- [[mdpd/rhosum]{.doc}]pair_mesodpd.md){.reference .internal} - mDPD particle interactions for mass density

- [[meam]{.doc}]pair_meam.md){.reference .internal} - Modified embedded atom method (MEAM)

- [[meam/ms]{.doc}]pair_meam.md){.reference .internal} - Multi-state modified embedded atom method (MS-MEAM)

- [[meam/spline]{.doc}]pair_meam_spline.md){.reference .internal} - Splined version of MEAM

- [[meam/sw/spline]{.doc}]pair_meam_sw_spline.md){.reference .internal} - Splined version of MEAM with a Stillinger-Weber term

- [[mesocnt]{.doc}]pair_mesocnt.md){.reference .internal} - Mesoscopic vdW potential for (carbon) nanotubes

- [[mesocnt/viscous]{.doc}]pair_mesocnt.md){.reference .internal} - Mesoscopic vdW potential for (carbon) nanotubes with friction

- [[mgpt]{.doc}]pair_mgpt.md){.reference .internal} - Simplified model generalized pseudopotential theory (MGPT) potential

- [[mie/cut]{.doc}]pair_mie.md){.reference .internal} - Mie potential

- [[mliap]{.doc}]pair_mliap.md){.reference .internal} - Multiple styles of machine-learning potential

- [[mm3/switch3/coulgauss/long]{.doc}]pair_lj_switch3_coulgauss_long.md){.reference .internal} - Smoothed MM3 vdW potential with Gaussian electrostatics

- [[momb]{.doc}]pair_momb.md){.reference .internal} - Many-Body Metal-Organic (MOMB) force field

- [[morse]{.doc}]pair_morse.md){.reference .internal} - Morse potential

- [[morse/smooth/linear]{.doc}]pair_morse.md){.reference .internal} - Linear smoothed Morse potential

- [[morse/soft]{.doc}]pair_morse.md){.reference .internal} - Morse potential with a soft core

- [[multi/lucy]{.doc}]pair_multi_lucy.md){.reference .internal} - DPD potential with density-dependent force

- [[multi/lucy/rx]{.doc}]pair_multi_lucy_rx.md){.reference .internal} - reactive DPD potential with density-dependent force

- [[nb3b/harmonic]{.doc}]pair_nb3b.md){.reference .internal} - Non-bonded 3-body harmonic potential

- [[nb3b/screened]{.doc}]pair_nb3b.md){.reference .internal} - Non-bonded 3-body screened harmonic potential

- [[nm/cut]{.doc}]pair_nm.md){.reference .internal} - N-M potential

- [[nm/cut/coul/cut]{.doc}]pair_nm.md){.reference .internal} - N-M potential with cutoff Coulomb

- [[nm/cut/coul/long]{.doc}]pair_nm.md){.reference .internal} - N-M potential with long-range Coulomb

- [[nm/cut/split]{.doc}]pair_nm.md){.reference .internal} - Split 12-6 Lennard-Jones and N-M potential

- [[oxdna/coaxstk]{.doc}]pair_oxdna.md){.reference .internal} -

- [[oxdna/excv]{.doc}]pair_oxdna.md){.reference .internal} -

- [[oxdna/hbond]{.doc}]pair_oxdna.md){.reference .internal} -

- [[oxdna/stk]{.doc}]pair_oxdna.md){.reference .internal} -

- [[oxdna/xstk]{.doc}]pair_oxdna.md){.reference .internal} -

- [[oxdna2/coaxstk]{.doc}]pair_oxdna2.md){.reference .internal} -

- [[oxdna2/dh]{.doc}]pair_oxdna2.md){.reference .internal} -

- [[oxdna2/excv]{.doc}]pair_oxdna2.md){.reference .internal} -

- [[oxdna2/hbond]{.doc}]pair_oxdna2.md){.reference .internal} -

- [[oxdna2/stk]{.doc}]pair_oxdna2.md){.reference .internal} -

- [[oxdna2/xstk]{.doc}]pair_oxdna2.md){.reference .internal} -

- [[oxrna2/coaxstk]{.doc}]pair_oxrna2.md){.reference .internal} -

- [[oxrna2/dh]{.doc}]pair_oxrna2.md){.reference .internal} -

- [[oxrna2/excv]{.doc}]pair_oxrna2.md){.reference .internal} -

- [[oxrna2/hbond]{.doc}]pair_oxrna2.md){.reference .internal} -

- [[oxrna2/stk]{.doc}]pair_oxrna2.md){.reference .internal} -

- [[oxrna2/xstk]{.doc}]pair_oxrna2.md){.reference .internal} -

- [[pace]{.doc}]pair_pace.md){.reference .internal} - Atomic Cluster Expansion (ACE) machine-learning potential

- [[pace/extrapolation]{.doc}]pair_pace.md){.reference .internal} - Atomic Cluster Expansion (ACE) machine-learning potential with extrapolation grades

- [[pace/apip]{.doc}]pair_pace_apip.md){.reference .internal} - [[adaptive-precision]{.doc}]Howto_apip.md){.reference .internal} version of ACE, used as precise potential

- [[pace/fast/apip]{.doc}]pair_pace_apip.md){.reference .internal} - [[adaptive-precision]{.doc}]Howto_apip.md){.reference .internal} version of ACE, used as fast potential

- [[pace/precise/apip]{.doc}]pair_pace_apip.md){.reference .internal} - [[adaptive-precision]{.doc}]Howto_apip.md){.reference .internal} version of ACE, used as precise potential

- [[pedone]{.doc}]pair_pedone.md){.reference .internal} - Pedone (PMMCS) potential (non-Coulomb part)

- [[pod]{.doc}]pair_pod.md){.reference .internal} - Proper orthogonal decomposition (POD) machine-learning potential

- [[peri/eps]{.doc}]pair_peri.md){.reference .internal} - Peridynamic EPS potential

- [[peri/lps]{.doc}]pair_peri.md){.reference .internal} - Peridynamic LPS potential

- [[peri/pmb]{.doc}]pair_peri.md){.reference .internal} - Peridynamic PMB potential

- [[peri/ves]{.doc}]pair_peri.md){.reference .internal} - Peridynamic VES potential

- [[polymorphic]{.doc}]pair_polymorphic.md){.reference .internal} - Polymorphic 3-body potential

- [[python]{.doc}]pair_python.md){.reference .internal} -

- [[quip]{.doc}]pair_quip.md){.reference .internal} -

- [[rann]{.doc}]pair_rann.md){.reference .internal} -

- [[reaxff]{.doc}]pair_reaxff.md){.reference .internal} - ReaxFF potential

- [[rebo]{.doc}]pair_airebo.md){.reference .internal} - Second generation REBO potential of Brenner

- [[rebomos]{.doc}]pair_rebomos.md){.reference .internal} - REBOMoS potential for MoS2

- [[rheo]{.doc}]pair_rheo.md){.reference .internal} - fluid interactions in RHEO package

- [[rheo/solid]{.doc}]pair_rheo_solid.md){.reference .internal} - solid interactions in RHEO package

- [[resquared]{.doc}]pair_resquared.md){.reference .internal} - Everaers RE-Squared ellipsoidal potential

- [[saip/metal]{.doc}]pair_saip_metal.md){.reference .internal} - Interlayer potential for hetero-junctions formed with hexagonal 2D materials and metal surfaces

- [[saip/metal/tmd]{.doc}]pair_saip_metal.md){.reference .internal} - Interlayer potential for transition-metal dichalcogenide / metal interfaces

- [[sdpd/taitwater/isothermal]{.doc}]pair_sdpd_taitwater_isothermal.md){.reference .internal} - Smoothed dissipative particle dynamics for water at isothermal conditions

- [[smatb]{.doc}]pair_smatb.md){.reference .internal} - Second Moment Approximation to the Tight Binding

- [[smatb/single]{.doc}]pair_smatb.md){.reference .internal} - Second Moment Approximation to the Tight Binding for single-element systems

- [[smd/hertz]{.doc}]pair_smd_hertz.md){.reference .internal} -

- [[smd/tlsph]{.doc}]pair_smd_tlsph.md){.reference .internal} -

- [[smd/tri_surface]{.doc}]pair_smd_triangulated_surface.md){.reference .internal} -

- [[smd/ulsph]{.doc}]pair_smd_ulsph.md){.reference .internal} -

- [[smtbq]{.doc}]pair_smtbq.md){.reference .internal} -

- [[snap]{.doc}]pair_snap.md){.reference .internal} - SNAP machine-learning potential

- [[soft]{.doc}]pair_soft.md){.reference .internal} - Soft (cosine) potential

- [[sph/heatconduction]{.doc}]pair_sph_heatconduction.md){.reference .internal} -

- [[sph/idealgas]{.doc}]pair_sph_idealgas.md){.reference .internal} -

- [[sph/lj]{.doc}]pair_sph_lj.md){.reference .internal} -

- [[sph/rhosum]{.doc}]pair_sph_rhosum.md){.reference .internal} -

- [[sph/taitwater]{.doc}]pair_sph_taitwater.md){.reference .internal} -

- [[sph/taitwater/morris]{.doc}]pair_sph_taitwater_morris.md){.reference .internal} -

- [[spin/dipole/cut]{.doc}]pair_spin_dipole.md){.reference .internal} -

- [[spin/dipole/long]{.doc}]pair_spin_dipole.md){.reference .internal} -

- [[spin/dmi]{.doc}]pair_spin_dmi.md){.reference .internal} -

- [[spin/exchange]{.doc}]pair_spin_exchange.md){.reference .internal} -

- [[spin/exchange/biquadratic]{.doc}]pair_spin_exchange.md){.reference .internal} -

- [[spin/magelec]{.doc}]pair_spin_magelec.md){.reference .internal} -

- [[spin/neel]{.doc}]pair_spin_neel.md){.reference .internal} -

- [[srp]{.doc}]pair_srp.md){.reference .internal} -

- [[srp/react]{.doc}]pair_srp.md){.reference .internal} -

- [[sw]{.doc}]pair_sw.md){.reference .internal} - Stillinger-Weber 3-body potential

- [[sw/angle/table]{.doc}]pair_sw_angle_table.md){.reference .internal} - Stillinger-Weber potential with tabulated angular term

- [[sw/mod]{.doc}]pair_sw.md){.reference .internal} - modified Stillinger-Weber 3-body potential

- [[table]{.doc}]pair_table.md){.reference .internal} - tabulated pair potential

- [[table/rx]{.doc}]pair_table_rx.md){.reference .internal} -

- [[tdpd]{.doc}]pair_mesodpd.md){.reference .internal} - tDPD particle interactions

- [[tersoff]{.doc}]pair_tersoff.md){.reference .internal} - Tersoff 3-body potential

- [[tersoff/mod]{.doc}]pair_tersoff_mod.md){.reference .internal} - modified Tersoff 3-body potential

- [[tersoff/mod/c]{.doc}]pair_tersoff_mod.md){.reference .internal} -

- [[tersoff/table]{.doc}]pair_tersoff.md){.reference .internal} -

- [[tersoff/zbl]{.doc}]pair_tersoff_zbl.md){.reference .internal} - Tersoff/ZBL 3-body potential

- [[thole]{.doc}]pair_thole.md){.reference .internal} - Coulomb interactions with thole damping

- [[threebody/table]{.doc}]pair_threebody_table.md){.reference .internal} - generic tabulated three-body potential

- [[tip4p/cut]{.doc}]pair_coul.md){.reference .internal} - Coulomb for TIP4P water w/out LJ

- [[tip4p/long]{.doc}]pair_coul.md){.reference .internal} - long-range Coulomb for TIP4P water w/out LJ

- [[tip4p/long/soft]{.doc}]pair_fep_soft.md){.reference .internal} -

- [[tracker]{.doc}]pair_tracker.md){.reference .internal} - monitor information about pairwise interactions

- [[tri/lj]{.doc}]pair_tri_lj.md){.reference .internal} - LJ potential between triangles

- [[ufm]{.doc}]pair_ufm.md){.reference .internal} -

- [[uf3]{.doc}]pair_uf3.md){.reference .internal} - UF3 machine-learning potential

- [[vashishta]{.doc}]pair_vashishta.md){.reference .internal} - Vashishta 2-body and 3-body potential

- [[vashishta/table]{.doc}]pair_vashishta.md){.reference .internal} -

- [[wf/cut]{.doc}]pair_wf_cut.md){.reference .internal} - Wang-Frenkel Potential for short-ranged interactions

- [[ylz]{.doc}]pair_ylz.md){.reference .internal} - Yuan-Li-Zhang Potential for anisotropic interactions

- [[yukawa]{.doc}]pair_yukawa.md){.reference .internal} - Yukawa potential

- [[yukawa/colloid]{.doc}]pair_yukawa_colloid.md){.reference .internal} - screened Yukawa potential for finite-size particles

- [[zbl]{.doc}]pair_zbl.md){.reference .internal} - Ziegler-Biersack-Littmark potential
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command must be used before any coefficients are set by the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[read_data]{.doc}]read_data.md){.reference .internal}, or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands.

Some pair styles are part of specific packages. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. The doc pages for individual pair potentials tell if it is part of a package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[read_data]{.doc}]read_data.md){.reference .internal}, [[pair_modify]{.doc}]pair_modify.md){.reference .internal}, [[kspace_style]{.doc}]kspace_style.md){.reference .internal}, [[dielectric]{.doc}]dielectric.md){.reference .internal}, [[pair_write]{.doc}]pair_write.md){.reference .internal}
:::

::::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style none
:::
::::
:::::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

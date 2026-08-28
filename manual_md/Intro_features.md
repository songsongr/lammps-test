:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#lammps-features .section}
# [1.3. ]{.section-number}LAMMPS features[](#lammps-features "Link to this heading"){.headerlink}

LAMMPS is a classical molecular dynamics (MD) code with these general classes of functionality:

1.  [[General features]{.std .std-ref}](#general){.reference .internal}

2.  [[Particle and model types]{.std .std-ref}](#particle){.reference .internal}

3.  [[Interatomic potentials (force fields)]{.std .std-ref}](#ff){.reference .internal}

4.  [[Atom creation]{.std .std-ref}](#create){.reference .internal}

5.  [[Ensembles, constraints, and boundary conditions]{.std .std-ref}](#ensemble){.reference .internal}

6.  [[Integrators]{.std .std-ref}](#integrate){.reference .internal}

7.  [[Diagnostics]{.std .std-ref}](#diag){.reference .internal}

8.  [[Output]{.std .std-ref}](#output){.reference .internal}

9.  [[Multi-replica models]{.std .std-ref}](#replica1){.reference .internal}

10. [[Pre- and post-processing]{.std .std-ref}](#prepost){.reference .internal}

11. [[Specialized features (beyond MD itself)]{.std .std-ref}](#special){.reference .internal}

------------------------------------------------------------------------

::: {#general-features .section}
[]{#general}

## [1.3.1. ]{.section-number}General features[](#general-features "Link to this heading"){.headerlink}

- runs on a single processor or in parallel

- distributed memory message-passing parallelism (MPI)

- shared memory multi-threading parallelism (OpenMP)

- spatial decomposition of simulation domain for MPI parallelism

- particle decomposition inside spatial decomposition for OpenMP and GPU parallelism

- GPLv2 licensed open-source distribution

- highly portable C++-17 (optional packages may require C++20)

- modular code with most functionality in optional packages

- only depends on MPI library for basic parallel functionality, MPI stub for serial compilation

- other libraries are optional and only required for specific packages

- GPU (CUDA, OpenCL, HIP, SYCL), Intel Xeon Phi, and OpenMP support for many code features

- easy to extend with new features and functionality

- runs from an input script

- syntax for defining and using variables and formulas

- syntax for looping over runs and breaking out of loops

- run one or multiple simulations simultaneously (in parallel) from one script

- build as library, invoke LAMMPS through library interface (from C, C++, Fortran) or provided Python wrapper or SWIG based wrappers

- couple with other codes: LAMMPS calls other code, other code calls LAMMPS, umbrella code calls both, MDI coupling interface

- call out to Python for computing forces, time integration, or other tasks

- plugin interface for loading external features at runtime

- large integrated collection of tests
:::

::: {#particle-and-model-types .section}
[]{#particle}

## [1.3.2. ]{.section-number}Particle and model types[](#particle-and-model-types "Link to this heading"){.headerlink}

(See [[atom style]{.doc}]atom_style.md){.reference .internal} command)

- atoms

- coarse-grained particles (e.g. bead-spring polymers)

- united-atom polymers or organic molecules

- all-atom polymers, organic molecules, proteins, DNA

- metals

- metal oxides

- granular materials

- coarse-grained mesoscale models

- finite-size spherical and ellipsoidal particles

- finite-size line segment (2d) and triangle (3d) particles

- finite-size rounded polygons (2d) and polyhedra (3d) particles

- point dipole particles

- particles with magnetic spin

- rigid collections of n particles

- hybrid combinations of these
:::

::: {#interatomic-potentials-force-fields .section}
[]{#ff}

## [1.3.3. ]{.section-number}Interatomic potentials (force fields)[](#interatomic-potentials-force-fields "Link to this heading"){.headerlink}

(See [[pair style]{.doc}]pair_style.md){.reference .internal}, [[bond style]{.doc}]bond_style.md){.reference .internal}, [[angle style]{.doc}]angle_style.md){.reference .internal}, [[dihedral style]{.doc}]dihedral_style.md){.reference .internal}, [[improper style]{.doc}]improper_style.md){.reference .internal}, [[kspace style]{.doc}]kspace_style.md){.reference .internal} commands)

- pairwise potentials: Lennard-Jones, Buckingham, Morse, Born-Mayer-Huggins, Yukawa, soft, Class II (COMPASS), hydrogen bond, harmonic, gaussian, tabulated, scripted

- charged pairwise potentials: Coulombic, point-dipole

- many-body potentials: EAM, Finnis/Sinclair, MEAM, MEAM+SW, EIM, EDIP, ADP, Stillinger-Weber, Tersoff, REBO, AIREBO, ReaxFF, COMB, Streitz-Mintmire, 3-body polymorphic, BOP, Vashishta

- machine learning potentials: ACE, AGNI, GAP, Behler-Parrinello (N2P2), POD, RANN, SNAP

- interfaces to ML potentials distributed by external groups: ANI, ChIMES, DeepPot, HIPNN, MTP

- long-range interactions for charge, point-dipoles, and LJ dispersion: Ewald, Wolf, PPPM (similar to particle-mesh Ewald), MSM, ScaFaCoS

- polarization models: [[QEq]{.doc}]fix_qeq.md){.reference .internal}, [[core/shell model]{.doc}]Howto_coreshell.md){.reference .internal}, [[Drude dipole model]{.doc}]Howto_drude.md){.reference .internal}

- charge equilibration (QEq via dynamic, point, shielded, Slater methods)

- coarse-grained potentials: DPD, GayBerne, REsquared, colloidal, DLVO, oxDNA / oxRNA, SPICA

- mesoscopic potentials: granular, Peridynamics, SPH, mesoscopic tubular potential (MESONT)

- semi-empirical potentials: multi-ion generalized pseudopotential theory (MGPT), second moment tight binding + QEq (SMTB-Q)

- electron force field (eFF)

- bond potentials: harmonic, FENE, Morse, nonlinear, Class II (COMPASS), quartic (breakable), tabulated, scripted

- angle potentials: harmonic, CHARMM, cosine, cosine/squared, cosine/periodic, Class II (COMPASS), tabulated, scripted

- dihedral potentials: harmonic, CHARMM, multi-harmonic, helix, Class II (COMPASS), OPLS, tabulated, scripted

- improper potentials: harmonic, cvff, umbrella, Class II (COMPASS), tabulated

- polymer potentials: all-atom, united-atom, bead-spring, breakable

- water potentials: TIP3P, TIP4P, SPC, SPC/E and variants

- interlayer potentials for graphene and analogues, hetero-junctions

- metal-organic framework potentials (QuickFF, MO-FF)

- implicit solvent potentials: hydrodynamic lubrication, Debye

- force-field compatibility with CHARMM, AMBER, DREIDING, OPLS, GROMACS, Class II (COMPASS), UFF, ClayFF, DREIDING, AMOEBA, INTERFACE

- access to the [OpenKIM Repository](https://openkim.org){.reference .external} of potentials via the [[kim command]{.doc}]kim_commands.md){.reference .internal}

- hybrid potentials: multiple pair, bond, angle, dihedral, improper potentials can be used in one simulation

- overlaid potentials: superposition of multiple pair potentials (including many-body) with optional scale factor
:::

::: {#atom-creation .section}
[]{#create}

## [1.3.4. ]{.section-number}Atom creation[](#atom-creation "Link to this heading"){.headerlink}

(See [[read_data]{.doc}]read_data.md){.reference .internal}, [[lattice]{.doc}]lattice.md){.reference .internal}, [[create_atoms]{.doc}]create_atoms.md){.reference .internal}, [[delete_atoms]{.doc}]delete_atoms.md){.reference .internal}, [[displace_atoms]{.doc}]displace_atoms.md){.reference .internal}, [[replicate]{.doc}]replicate.md){.reference .internal} commands)

- read in atom coordinates from files

- create atoms on one or more lattices (e.g. grain boundaries)

- delete geometric or logical groups of atoms (e.g. voids)

- replicate existing atoms multiple times

- displace atoms
:::

::: {#ensembles-constraints-and-boundary-conditions .section}
[]{#ensemble}

## [1.3.5. ]{.section-number}Ensembles, constraints, and boundary conditions[](#ensembles-constraints-and-boundary-conditions "Link to this heading"){.headerlink}

(See [[fix]{.doc}]fix.md){.reference .internal} command)

- 2d or 3d systems

- orthogonal or non-orthogonal (triclinic symmetry) simulation domains

- constant NVE, NVT, NPT, NPH, Parrinello/Rahman integrators

- thermostatting options for groups and geometric regions of atoms

- pressure control via Nose/Hoover or Berendsen barostatting in 1 to 3 dimensions

- simulation box deformation (tensile and shear)

- harmonic (umbrella) constraint forces

- rigid body constraints

- SHAKE / RATTLE bond and angle constraints

- motion constraints to manifold surfaces

- Monte Carlo bond breaking, formation, swapping, template based reaction modeling

- atom/molecule insertion and deletion

- walls of various kinds, static and moving

- non-equilibrium molecular dynamics (NEMD)

- variety of additional boundary conditions and constraints
:::

::: {#integrators .section}
[]{#integrate}

## [1.3.6. ]{.section-number}Integrators[](#integrators "Link to this heading"){.headerlink}

(See [[run]{.doc}]run.md){.reference .internal}, [[run_style]{.doc}]run_style.md){.reference .internal}, [[minimize]{.doc}]minimize.md){.reference .internal} commands)

- velocity-Verlet integrator

- Brownian dynamics

- rigid body integration

- energy minimization via conjugate gradient, steepest descent relaxation, or damped dynamics (FIRE, Quickmin)

- rRESPA hierarchical timestepping

- fixed or adaptive time step

- rerun command for post-processing of dump files
:::

::: {#diagnostics .section}
[]{#diag}

## [1.3.7. ]{.section-number}Diagnostics[](#diagnostics "Link to this heading"){.headerlink}

- see various flavors of the [[fix]{.doc}]fix.md){.reference .internal} and [[compute]{.doc}]compute.md){.reference .internal} commands

- introspection command for system, simulation, and compile time settings and configurations
:::

::: {#output .section}
[]{#id1}

## [1.3.8. ]{.section-number}Output[](#output "Link to this heading"){.headerlink}

([[dump]{.doc}]dump.md){.reference .internal}, [[restart]{.doc}]restart.md){.reference .internal} commands)

- log file of thermodynamic info

- text dump files of atom coordinates, velocities, other per-atom quantities

- dump output on fixed and variable intervals, based timestep or simulated time

- binary restart files

- parallel I/O of dump and restart files

- per-atom quantities (energy, stress, centro-symmetry parameter, CNA, etc.)

- user-defined system-wide (log file) or per-atom (dump file) calculations

- custom partitioning (chunks) for binning, and static or dynamic grouping of atoms for analysis

- spatial, time, and per-chunk averaging of per-atom quantities

- time averaging and histogramming of system-wide quantities

- atom snapshots in native, XYZ, XTC, DCD, CFG, NetCDF, HDF5, ADIOS2, YAML formats

- on-the-fly compression of output and decompression of read in files
:::

::: {#multi-replica-models .section}
[]{#replica1}

## [1.3.9. ]{.section-number}Multi-replica models[](#multi-replica-models "Link to this heading"){.headerlink}

- [[nudged elastic band]{.doc}]neb.md){.reference .internal}

- [[hyperdynamics]{.doc}]hyper.md){.reference .internal}

- [[parallel replica dynamics]{.doc}]prd.md){.reference .internal}

- [[temperature accelerated dynamics]{.doc}]tad.md){.reference .internal}

- [[parallel tempering]{.doc}]temper.md){.reference .internal}

- path-integral MD: [[first variant]{.doc}]fix_pimd.md){.reference .internal}, [[second variant]{.doc}]fix_ipi.md){.reference .internal}

- multi-walker collective variables with [[Colvars]{.doc}]fix_colvars.md){.reference .internal} and [[Plumed]{.doc}]fix_plumed.md){.reference .internal}
:::

::: {#pre-and-post-processing .section}
[]{#prepost}

## [1.3.10. ]{.section-number}Pre- and post-processing[](#pre-and-post-processing "Link to this heading"){.headerlink}

- A handful of pre- and post-processing tools are packaged with LAMMPS, some of which can convert input and output files to/from formats used by other codes; see the [[Tools]{.doc}]Tools.md){.reference .internal} page.

- Our group has also written and released a separate toolkit called [Pizza.py](https://lammps.github.io/pizza/){.reference .external} which provides tools for doing setup, analysis, plotting, and visualization for LAMMPS simulations. Pizza.py is written in [Python](https://www.python.org){.reference .external} and is available for download from [the Pizza.py WWW site](https://lammps.github.io/pizza/){.reference .external}.
:::

::: {#specialized-features .section}
[]{#special}

## [1.3.11. ]{.section-number}Specialized features[](#specialized-features "Link to this heading"){.headerlink}

LAMMPS can be built with optional packages which implement a variety of additional capabilities. See the [[Optional Packages]{.doc}]Packages.md){.reference .internal} page for details.

These are LAMMPS capabilities which you may not think of as typical classical MD options:

- [[static]{.doc}]balance.md){.reference .internal} and [[dynamic load-balancing]{.doc}]fix_balance.md){.reference .internal}, optional with recursive bisectioning decomposition

- [[generalized aspherical particles]{.doc}]Howto_body.md){.reference .internal}

- [[stochastic rotation dynamics (SRD)]{.doc}]fix_srd.md){.reference .internal}

- [[real-time visualization and interactive MD]{.doc}]fix_imd.md){.reference .internal}, [[built-in renderer for images and movies]{.doc}]dump_image.md){.reference .internal}

- calculate [[virtual diffraction patterns]{.doc}]compute_xrd.md){.reference .internal}

- calculate [[finite temperature phonon dispersion]{.doc}]fix_phonon.md){.reference .internal} and the [[dynamical matrix of minimized structures]{.doc}]dynamical_matrix.md){.reference .internal}

- [[QM/MM coupling]{.doc}]fix_qmmm.md){.reference .internal}

- Monte Carlo via [[GCMC]{.doc}]fix_gcmc.md){.reference .internal} and [[tfMC]{.doc}]fix_tfmc.md){.reference .internal} and [[atom swapping]{.doc}]fix_atom_swap.md){.reference .internal}

- [[path-integral molecular dynamics (PIMD)]{.doc}]fix_ipi.md){.reference .internal} and [[this as well]{.doc}]fix_pimd.md){.reference .internal}

- [[Direct Simulation Monte Carlo]{.doc}]pair_dsmc.md){.reference .internal} for low-density fluids

- [[Peridynamics modeling]{.doc}]pair_peri.md){.reference .internal}

- [[Lattice Boltzmann fluid]{.doc}]fix_lb_fluid.md){.reference .internal}

- [[targeted]{.doc}]fix_tmd.md){.reference .internal} and [[steered]{.doc}]fix_smd.md){.reference .internal} molecular dynamics

- [[two-temperature electron model]{.doc}]fix_ttm.md){.reference .internal}
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

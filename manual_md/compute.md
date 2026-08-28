::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-command .section}
[]{#index-0}

# compute command[](#compute-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID style args
:::
::::

- ID = user-assigned name for the computation

- group-ID = ID of the group of atoms to perform the computation on

- style = one of a list of possible style names (see below)

- args = arguments used by a particular style
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all temp
    compute newtemp flow temp/partial 1 1 0
    compute 3 all ke/atom
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a diagnostic computation that will be performed on a group of atoms. Quantities calculated by a compute are instantaneous values, meaning they are calculated from information about atoms on the current timestep or iteration, though internally a compute may store some information about a previous state of the system. Defining a compute does not perform the computation. Instead computes are invoked by other LAMMPS commands as needed (e.g., to calculate a temperature needed for a thermostat fix or to generate thermodynamic or dump file output). See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for a summary of various LAMMPS output options, many of which involve computes.

The ID of a compute can only contain alphanumeric characters and underscores.

------------------------------------------------------------------------

Computes calculate and store any of four *styles* of quantities: global, per-atom, local, or per-grid.

A global quantity is one or more system-wide values, e.g. the temperature of the system. A per-atom quantity is one or more values per atom, e.g. the kinetic energy of each atom. Per-atom values are set to 0.0 for atoms not in the specified compute group. Local quantities are calculated by each processor based on the atoms it owns, but there may be zero or more per atom, e.g. a list of bond distances. Per-grid quantities are calculated on a regular 2d or 3d grid which overlays a 2d or 3d simulation domain. The grid points and the data they store are distributed across processors; each processor owns the grid points which fall within its subdomain.

As a general rule of thumb, computes that produce per-atom quantities have the word "atom" at the end of their style, e.g. *ke/atom*. Computes that produce local quantities have the word "local" at the end of their style, e.g. *bond/local*. Computes that produce per-grid quantities have the word "grid" at the end of their style, e.g. *property/grid*. And styles with neither "atom" or "local" or "grid" at the end of their style name produce global quantities.

Global, per-atom, local, and per-grid quantities can also be of three *kinds*: a single scalar value (global only), a vector of values, or a 2d array of values. For per-atom, local, and per-grid quantities, a "vector" means a single value for each atom, each local entity (e.g. bond), or grid cell. Likewise an "array", means multiple values for each atom, each local entity, or each grid cell.

Note that a single compute can produce any combination of global, per-atom, local, or per-grid values. Likewise it can produce any combination of scalar, vector, or array output for each style. The exception is that for per-atom, local, and per-grid output, either a vector or array can be produced, but not both. The doc page for each compute explains the values it produces.

When a compute output is accessed by another input script command it is referenced via the following bracket notation, where ID is the ID of the compute:

  ---------------- --------------------------------------------
  c_ID             entire scalar, vector, or array
  c_ID\[I\]        one element of vector, one column of array
  c_ID\[I\]\[J\]   one element of array
  ---------------- --------------------------------------------

In other words, using one bracket reduces the dimension of the quantity once (vector [\\(\\to\\)]{.math .notranslate .nohighlight} scalar, array [\\(\\to\\)]{.math .notranslate .nohighlight} vector). Using two brackets reduces the dimension twice (array [\\(\\to\\)]{.math .notranslate .nohighlight} scalar). Thus, for example, a command that uses global scalar compute values as input can also process elements of a vector or array. Depending on the command, this can either be done directly using the syntax in the table, or by first defining a [[variable]{.doc}]variable.md){.reference .internal} of the appropriate style to store the quantity, then using the variable as an input to the command.

Note that commands and [[variables]{.doc}]variable.md){.reference .internal} which take compute outputs as input typically do not allow for all styles and kinds of data (e.g., a command may require global but not per-atom values, or it may require a vector of values, not a scalar). This means there is typically no ambiguity about referring to a compute output as c_ID even if it produces, for example, both a scalar and vector. The doc pages for various commands explain the details, including how any ambiguities are resolved.

------------------------------------------------------------------------

In LAMMPS, the values generated by a compute can be used in several ways:

- The results of computes that calculate a global temperature or pressure can be used by fixes that do thermostatting or barostatting or when atom velocities are created.

- Global values can be output via the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} or [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} command. Or the values can be referenced in a [[variable equal]{.doc}]variable.md){.reference .internal} or [[variable atom]{.doc}]variable.md){.reference .internal} command.

- Per-atom values can be output via the [[dump custom]{.doc}]dump.md){.reference .internal} command. Or they can be time-averaged via the [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal} command or reduced by the [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} command. Or the per-atom values can be referenced in an [[atom-style variable]{.doc}]variable.md){.reference .internal}.

- Local values can be reduced by the [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} command, or histogrammed by the [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal} command, or output by the [[dump local]{.doc}]dump.md){.reference .internal} command.

The results of computes that calculate global quantities can be either "intensive" or "extensive" values. Intensive means the value is independent of the number of atoms in the simulation (e.g., temperature). Extensive means the value scales with the number of atoms in the simulation (e.g., total rotational kinetic energy). [[Thermodynamic output]{.doc}]thermo_style.md){.reference .internal} will normalize extensive values by the number of atoms in the system, depending on the "thermo_modify norm" setting. It will not normalize intensive values. If a compute value is accessed in another way (e.g., by a [[variable]{.doc}]variable.md){.reference .internal}), you may want to know whether it is an intensive or extensive value. See the page for individual computes for further info.

------------------------------------------------------------------------

LAMMPS creates its own computes internally for thermodynamic output. Three computes are always created, named "thermo_temp", "thermo_press", and "thermo_pe", as if these commands had been invoked in the input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute thermo_temp all temp
    compute thermo_press all pressure thermo_temp
    compute thermo_pe all pe
:::
::::

Additional computes for other quantities are created if the thermo style requires it. See the documentation for the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command.

Fixes that calculate temperature or pressure, i.e. for thermostatting or barostatting, may also create computes. These are discussed in the documentation for specific [[fix]{.doc}]fix.md){.reference .internal} commands.

In all these cases, the default computes LAMMPS creates can be replaced by computes defined by the user in the input script, as described by the [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} and [[fix modify]{.doc}]fix_modify.md){.reference .internal} commands.

Properties of either a default or user-defined compute can be modified via the [[compute_modify]{.doc}]compute_modify.md){.reference .internal} command.

Computes can be deleted with the [[uncompute]{.doc}]uncompute.md){.reference .internal} command.

Code for new computes can be added to LAMMPS; see the [[Modify]{.doc}]Modify.md){.reference .internal} page for details. The results of their calculations accessed in the various ways described above.

------------------------------------------------------------------------

Each compute style has its own page which describes its arguments and what it does. Here is an alphabetic list of compute styles available in LAMMPS. They are also listed in more compact form on the [[Commands compute]{.doc}]Commands_compute.md){.reference .internal} doc page.

There are also additional accelerated compute styles included in the LAMMPS distribution for faster performance on CPUs, GPUs, and KNLs. The individual style names on the [[Commands compute]{.doc}]Commands_compute.md){.reference .internal} page are followed by one or more of (g,i,k,o,t) to indicate which accelerated styles exist.

- [[ackland/atom]{.doc}]compute_ackland_atom.md){.reference .internal} - determines the local lattice structure based on the Ackland formulation

- [[adf]{.doc}]compute_adf.md){.reference .internal} - angular distribution function of triples of atoms

- [[aggregate/atom]{.doc}]compute_cluster_atom.md){.reference .internal} - aggregate ID for each atom

- [[angle]{.doc}]compute_angle.md){.reference .internal} - energy of each angle sub-style

- [[angle/local]{.doc}]compute_angle_local.md){.reference .internal} - theta and energy of each angle

- [[angmom/chunk]{.doc}]compute_angmom_chunk.md){.reference .internal} - angular momentum for each chunk

- [[ave/sphere/atom]{.doc}]compute_ave_sphere_atom.md){.reference .internal} - compute local density and temperature around each atom

- [[basal/atom]{.doc}]compute_basal_atom.md){.reference .internal} - calculates the hexagonal close-packed "c" lattice vector of each atom

- [[body/local]{.doc}]compute_body_local.md){.reference .internal} - attributes of body sub-particles

- [[bond]{.doc}]compute_bond.md){.reference .internal} - energy of each bond sub-style

- [[bond/local]{.doc}]compute_bond_local.md){.reference .internal} - distance and energy of each bond

- [[born/matrix]{.doc}]compute_born_matrix.md){.reference .internal} - second derivative or potential with respect to strain

- [[centro/atom]{.doc}]compute_centro_atom.md){.reference .internal} - centro-symmetry parameter for each atom

- [[centroid/stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} - centroid based stress tensor for each atom

- [[chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} - assign chunk IDs to each atom

- [[chunk/spread/atom]{.doc}]compute_chunk_spread_atom.md){.reference .internal} - spreads chunk values to each atom in chunk

- [[cluster/atom]{.doc}]compute_cluster_atom.md){.reference .internal} - cluster ID for each atom

- [[cna/atom]{.doc}]compute_cna_atom.md){.reference .internal} - common neighbor analysis (CNA) for each atom

- [[cnp/atom]{.doc}]compute_cnp_atom.md){.reference .internal} - common neighborhood parameter (CNP) for each atom

- [[com]{.doc}]compute_com.md){.reference .internal} - center of mass of group of atoms

- [[com/chunk]{.doc}]compute_com_chunk.md){.reference .internal} - center of mass for each chunk

- [[composition/atom]{.doc}]compute_composition_atom.md){.reference .internal} - local composition for each atom

- [[contact/atom]{.doc}]compute_contact_atom.md){.reference .internal} - contact count for each spherical particle

- [[coord/atom]{.doc}]compute_coord_atom.md){.reference .internal} - coordination number for each atom

- [[count/type]{.doc}]compute_count_type.md){.reference .internal} - count of atoms or bonds by type

- [[damage/atom]{.doc}]compute_damage_atom.md){.reference .internal} - Peridynamic damage for each atom

- [[dihedral]{.doc}]compute_dihedral.md){.reference .internal} - energy of each dihedral sub-style

- [[dihedral/local]{.doc}]compute_dihedral_local.md){.reference .internal} - angle of each dihedral

- [[dilatation/atom]{.doc}]compute_dilatation_atom.md){.reference .internal} - Peridynamic dilatation for each atom

- [[dipole]{.doc}]compute_dipole.md){.reference .internal} - dipole vector and total dipole

- [[dipole/chunk]{.doc}]compute_dipole_chunk.md){.reference .internal} - dipole vector and total dipole for each chunk

- [[dipole/tip4p]{.doc}]compute_dipole.md){.reference .internal} - dipole vector and total dipole with TIP4P pair style

- [[dipole/tip4p/chunk]{.doc}]compute_dipole_chunk.md){.reference .internal} - dipole vector and total dipole for each chunk with TIP4P pair style

- [[displace/atom]{.doc}]compute_displace_atom.md){.reference .internal} - displacement of each atom

- [[dpd]{.doc}]compute_dpd.md){.reference .internal} - total values of internal conductive energy, internal mechanical energy, chemical energy, and harmonic average of internal temperature

- [[dpd/atom]{.doc}]compute_dpd_atom.md){.reference .internal} - per-particle values of internal conductive energy, internal mechanical energy, chemical energy, and internal temperature

- [[edpd/temp/atom]{.doc}]compute_edpd_temp_atom.md){.reference .internal} - per-atom temperature for each eDPD particle in a group

- [[efield/atom]{.doc}]compute_efield_atom.md){.reference .internal} - electric field at each atom

- [[efield/wolf/atom]{.doc}]compute_efield_wolf_atom.md){.reference .internal} - electric field at each atom

- [[entropy/atom]{.doc}]compute_entropy_atom.md){.reference .internal} - pair entropy fingerprint of each atom

- [[erotate/asphere]{.doc}]compute_erotate_asphere.md){.reference .internal} - rotational energy of aspherical particles

- [[erotate/rigid]{.doc}]compute_erotate_rigid.md){.reference .internal} - rotational energy of rigid bodies

- [[erotate/sphere]{.doc}]compute_erotate_sphere.md){.reference .internal} - rotational energy of spherical particles

- [[erotate/sphere/atom]{.doc}]compute_erotate_sphere_atom.md){.reference .internal} - rotational energy for each spherical particle

- [[event/displace]{.doc}]compute_event_displace.md){.reference .internal} - detect event on atom displacement

- [[fabric]{.doc}]compute_fabric.md){.reference .internal} - calculates fabric tensors from pair interactions

- [[fep]{.doc}]compute_fep.md){.reference .internal} - compute free energies for alchemical transformation from perturbation theory

- [[fep/ta]{.doc}]compute_fep_ta.md){.reference .internal} - compute free energies for a test area perturbation

- [[force/tally]{.doc}]compute_tally.md){.reference .internal} - force between two groups of atoms via the tally callback mechanism

- [[fragment/atom]{.doc}]compute_cluster_atom.md){.reference .internal} - fragment ID for each atom

- [[gaussian/grid/local]{.doc}]compute_gaussian_grid_local.md){.reference .internal} - local array of Gaussian atomic contributions on a regular grid

- [[global/atom]{.doc}]compute_global_atom.md){.reference .internal} - assign global values to each atom from arrays of global values

- [[group/group]{.doc}]compute_group_group.md){.reference .internal} - energy/force between two groups of atoms

- [[gyration]{.doc}]compute_gyration.md){.reference .internal} - radius of gyration of group of atoms

- [[gyration/chunk]{.doc}]compute_gyration_chunk.md){.reference .internal} - radius of gyration for each chunk

- [[gyration/shape]{.doc}]compute_gyration_shape.md){.reference .internal} - shape parameters from gyration tensor

- [[gyration/shape/chunk]{.doc}]compute_gyration_shape_chunk.md){.reference .internal} - shape parameters from gyration tensor for each chunk

- [[hbond/local]{.doc}]compute_hbond_local.md){.reference .internal} - identify hydrogen bonds

- [[heat/flux]{.doc}]compute_heat_flux.md){.reference .internal} - heat flux through a group of atoms

- [[heat/flux/tally]{.doc}]compute_tally.md){.reference .internal} - heat flux through a group of atoms via the tally callback mechanism

- [[heat/flux/virial/tally]{.doc}]compute_tally.md){.reference .internal} - virial heat flux between two groups via the tally callback mechanism

- [[hexorder/atom]{.doc}]compute_hexorder_atom.md){.reference .internal} - bond orientational order parameter q6

- [[hma]{.doc}]compute_hma.md){.reference .internal} - harmonically mapped averaging for atomic crystals

- [[improper]{.doc}]compute_improper.md){.reference .internal} - energy of each improper sub-style

- [[improper/local]{.doc}]compute_improper_local.md){.reference .internal} - angle of each improper

- [[inertia/chunk]{.doc}]compute_inertia_chunk.md){.reference .internal} - inertia tensor for each chunk

- [[ke]{.doc}]compute_ke.md){.reference .internal} - translational kinetic energy

- [[ke/atom]{.doc}]compute_ke_atom.md){.reference .internal} - kinetic energy for each atom

- [[ke/atom/eff]{.doc}]compute_ke_atom_eff.md){.reference .internal} - per-atom translational and radial kinetic energy in the electron force field model

- [[ke/eff]{.doc}]compute_ke_eff.md){.reference .internal} - kinetic energy of a group of nuclei and electrons in the electron force field model

- [[ke/rigid]{.doc}]compute_ke_rigid.md){.reference .internal} - translational kinetic energy of rigid bodies

- [[mliap]{.doc}]compute_mliap.md){.reference .internal} - gradients of energy and forces with respect to model parameters and related quantities for training machine learning interatomic potentials

- [[momentum]{.doc}]compute_momentum.md){.reference .internal} - translational momentum

- [[msd]{.doc}]compute_msd.md){.reference .internal} - mean-squared displacement of group of atoms

- [[msd/chunk]{.doc}]compute_msd_chunk.md){.reference .internal} - mean-squared displacement for each chunk

- [[msd/nongauss]{.doc}]compute_msd_nongauss.md){.reference .internal} - MSD and non-Gaussian parameter of group of atoms

- [[nbond/atom]{.doc}]compute_nbond_atom.md){.reference .internal} - calculates number of bonds per atom

- [[omega/chunk]{.doc}]compute_omega_chunk.md){.reference .internal} - angular velocity for each chunk

- [[orientorder/atom]{.doc}]compute_orientorder_atom.md){.reference .internal} - Steinhardt bond orientational order parameters Ql

- [[pace]{.doc}]compute_pace.md){.reference .internal} - atomic cluster expansion descriptors and related quantities

- [[pair]{.doc}]compute_pair.md){.reference .internal} - values computed by a pair style

- [[pair/local]{.doc}]compute_pair_local.md){.reference .internal} - distance/energy/force of each pairwise interaction

- [[pe]{.doc}]compute_pe.md){.reference .internal} - potential energy

- [[pe/atom]{.doc}]compute_pe_atom.md){.reference .internal} - potential energy for each atom

- [[pe/mol/tally]{.doc}]compute_tally.md){.reference .internal} - potential energy between two groups of atoms separated into intermolecular and intramolecular components via the tally callback mechanism

- [[pe/tally]{.doc}]compute_tally.md){.reference .internal} - potential energy between two groups of atoms via the tally callback mechanism

- [[plasticity/atom]{.doc}]compute_plasticity_atom.md){.reference .internal} - Peridynamic plasticity for each atom

- [[pod/atom]{.doc}]compute_pod_atom.md){.reference .internal} - POD descriptors for each atom

- [[podd/atom]{.doc}]compute_pod_atom.md){.reference .internal} - derivative of POD descriptors for each atom

- [[pod/local]{.doc}]compute_pod_atom.md){.reference .internal} - local POD descriptors and their derivatives

- [[pod/global]{.doc}]compute_pod_atom.md){.reference .internal} - global POD descriptors and their derivatives

- [[pressure]{.doc}]compute_pressure.md){.reference .internal} - total pressure and pressure tensor

- [[pressure/alchemy]{.doc}]compute_pressure_alchemy.md){.reference .internal} - mixed system total pressure and pressure tensor for [[fix alchemy]{.doc}]fix_alchemy.md){.reference .internal} runs

- [[pressure/uef]{.doc}]compute_pressure_uef.md){.reference .internal} - pressure tensor in the reference frame of an applied flow field

- [[property/atom]{.doc}]compute_property_atom.md){.reference .internal} - convert atom attributes to per-atom vectors/arrays

- [[property/chunk]{.doc}]compute_property_chunk.md){.reference .internal} - extract various per-chunk attributes

- [[property/grid]{.doc}]compute_property_grid.md){.reference .internal} - convert per-grid attributes to per-grid vectors/arrays

- [[property/local]{.doc}]compute_property_local.md){.reference .internal} - convert local attributes to local vectors/arrays

- [[ptm/atom]{.doc}]compute_ptm_atom.md){.reference .internal} - determines the local lattice structure based on the Polyhedral Template Matching method

- [[rattlers/atom]{.doc}]compute_rattlers_atom.md){.reference .internal} - identify under-coordinated rattler atoms

- [[rdf]{.doc}]compute_rdf.md){.reference .internal} - radial distribution function [\\(g(r)\\)]{.math .notranslate .nohighlight} histogram of group of atoms

- [[reaxff/atom]{.doc}]compute_reaxff_atom.md){.reference .internal} - extract ReaxFF bond information

- [[reduce]{.doc}]compute_reduce.md){.reference .internal} - combine per-atom quantities into a single global value

- [[reduce/chunk]{.doc}]compute_reduce_chunk.md){.reference .internal} - reduce per-atom quantities within each chunk

- [[reduce/region]{.doc}]compute_reduce.md){.reference .internal} - same as compute reduce, within a region

- [[rheo/property/atom]{.doc}]compute_rheo_property_atom.md){.reference .internal} - convert atom attributes in RHEO package to per-atom vectors/arrays

- [[rigid/local]{.doc}]compute_rigid_local.md){.reference .internal} - extract rigid body attributes

- [[saed]{.doc}]compute_saed.md){.reference .internal} - electron diffraction intensity on a mesh of reciprocal lattice nodes

- [[slcsa/atom]{.doc}]compute_slcsa_atom.md){.reference .internal} - perform Supervised Learning Crystal Structure Analysis (SL-CSA)

- [[slice]{.doc}]compute_slice.md){.reference .internal} - extract values from global vector or array

- [[smd/contact/radius]{.doc}]compute_smd_contact_radius.md){.reference .internal} - contact radius for Smooth Mach Dynamics

- [[smd/damage]{.doc}]compute_smd_damage.md){.reference .internal} - damage status of SPH particles in Smooth Mach Dynamics

- [[smd/hourglass/error]{.doc}]compute_smd_hourglass_error.md){.reference .internal} - error associated with approximated relative separation in Smooth Mach Dynamics

- [[smd/internal/energy]{.doc}]compute_smd_internal_energy.md){.reference .internal} - per-particle enthalpy in Smooth Mach Dynamics

- [[smd/plastic/strain]{.doc}]compute_smd_plastic_strain.md){.reference .internal} - equivalent plastic strain per particle in Smooth Mach Dynamics

- [[smd/plastic/strain/rate]{.doc}]compute_smd_plastic_strain_rate.md){.reference .internal} - time rate of the equivalent plastic strain in Smooth Mach Dynamics

- [[smd/rho]{.doc}]compute_smd_rho.md){.reference .internal} - per-particle mass density in Smooth Mach Dynamics

- [[smd/tlsph/defgrad]{.doc}]compute_smd_tlsph_defgrad.md){.reference .internal} - deformation gradient in Smooth Mach Dynamics

- [[smd/tlsph/dt]{.doc}]compute_smd_tlsph_dt.md){.reference .internal} - CFL-stable time increment per particle in Smooth Mach Dynamics

- [[smd/tlsph/num/neighs]{.doc}]compute_smd_tlsph_num_neighs.md){.reference .internal} - number of particles inside the smoothing kernel radius for Smooth Mach Dynamics

- [[smd/tlsph/shape]{.doc}]compute_smd_tlsph_shape.md){.reference .internal} - current shape of the volume of a particle for Smooth Mach Dynamics

- [[smd/tlsph/strain]{.doc}]compute_smd_tlsph_strain.md){.reference .internal} - Green--Lagrange strain tensor for Smooth Mach Dynamics

- [[smd/tlsph/strain/rate]{.doc}]compute_smd_tlsph_strain_rate.md){.reference .internal} - rate of strain for Smooth Mach Dynamics

- [[smd/tlsph/stress]{.doc}]compute_smd_tlsph_stress.md){.reference .internal} - per-particle Cauchy stress tensor for SPH particles

- [[smd/triangle/vertices]{.doc}]compute_smd_triangle_vertices.md){.reference .internal} - coordinates of vertices corresponding to the triangle elements of a mesh for Smooth Mach Dynamics

- [[smd/ulsph/effm]{.doc}]compute_smd_ulsph_effm.md){.reference .internal} - per-particle effective shear modulus

- [[smd/ulsph/num/neighs]{.doc}]compute_smd_ulsph_num_neighs.md){.reference .internal} - number of neighbor particles inside the smoothing kernel radius for Smooth Mach Dynamics

- [[smd/ulsph/strain]{.doc}]compute_smd_ulsph_strain.md){.reference .internal} - logarithmic strain tensor for Smooth Mach Dynamics

- [[smd/ulsph/strain/rate]{.doc}]compute_smd_ulsph_strain_rate.md){.reference .internal} - logarithmic strain rate for Smooth Mach Dynamics

- [[smd/ulsph/stress]{.doc}]compute_smd_ulsph_stress.md){.reference .internal} - per-particle Cauchy stress tensor and von Mises equivalent stress in Smooth Mach Dynamics

- [[smd/vol]{.doc}]compute_smd_vol.md){.reference .internal} - per-particle volumes and their sum in Smooth Mach Dynamics

- [[snap]{.doc}]compute_sna_atom.md){.reference .internal} - gradients of SNAP energy and forces with respect to linear coefficients and related quantities for fitting SNAP potentials

- [[sna/atom]{.doc}]compute_sna_atom.md){.reference .internal} - bispectrum components for each atom

- [[sna/grid]{.doc}]compute_sna_atom.md){.reference .internal} - global array of bispectrum components on a regular grid

- [[sna/grid/local]{.doc}]compute_sna_atom.md){.reference .internal} - local array of bispectrum components on a regular grid

- [[snad/atom]{.doc}]compute_sna_atom.md){.reference .internal} - derivative of bispectrum components for each atom

- [[snav/atom]{.doc}]compute_sna_atom.md){.reference .internal} - virial contribution from bispectrum components for each atom

- [[sph/e/atom]{.doc}]compute_sph_e_atom.md){.reference .internal} - per-atom internal energy of Smooth-Particle Hydrodynamics atoms

- [[sph/rho/atom]{.doc}]compute_sph_rho_atom.md){.reference .internal} - per-atom density of Smooth-Particle Hydrodynamics atoms

- [[sph/t/atom]{.doc}]compute_sph_t_atom.md){.reference .internal} - per-atom internal temperature of Smooth-Particle Hydrodynamics atoms

- [[spin]{.doc}]compute_spin.md){.reference .internal} - magnetic quantities for a system of atoms having spins

- [[stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} - stress tensor for each atom

- [[stress/cartesian]{.doc}]compute_stress_cartesian.md){.reference .internal} - stress tensor in cartesian coordinates

- [[stress/cylinder]{.doc}]compute_stress_curvilinear.md){.reference .internal} - stress tensor in cylindrical coordinates

- [[stress/mop]{.doc}]compute_stress_mop.md){.reference .internal} - normal components of the local stress tensor using the method of planes

- [[stress/mop/profile]{.doc}]compute_stress_mop.md){.reference .internal} - profile of the normal components of the local stress tensor using the method of planes

- [[stress/spherical]{.doc}]compute_stress_curvilinear.md){.reference .internal} - stress tensor in spherical coordinates

- [[stress/tally]{.doc}]compute_tally.md){.reference .internal} - stress between two groups of atoms via the tally callback mechanism

- [[tdpd/cc/atom]{.doc}]compute_tdpd_cc_atom.md){.reference .internal} - per-atom chemical concentration of a specified species for each tDPD particle

- [[temp]{.doc}]compute_temp.md){.reference .internal} - temperature of group of atoms

- [[temp/asphere]{.doc}]compute_temp_asphere.md){.reference .internal} - temperature of aspherical particles

- [[temp/body]{.doc}]compute_temp_body.md){.reference .internal} - temperature of body particles

- [[temp/chunk]{.doc}]compute_temp_chunk.md){.reference .internal} - temperature of each chunk

- [[temp/com]{.doc}]compute_temp_com.md){.reference .internal} - temperature after subtracting center-of-mass velocity

- [[temp/cs]{.doc}]compute_temp_cs.md){.reference .internal} - temperature based on the center-of-mass velocity of atom pairs that are bonded to each other

- [[temp/deform]{.doc}]compute_temp_deform.md){.reference .internal} - temperature excluding box deformation velocity

- [[temp/deform/eff]{.doc}]compute_temp_deform_eff.md){.reference .internal} - temperature excluding box deformation velocity in the electron force field model

- [[temp/drude]{.doc}]compute_temp_drude.md){.reference .internal} - temperature of Core--Drude pairs

- [[temp/eff]{.doc}]compute_temp_eff.md){.reference .internal} - temperature of a group of nuclei and electrons in the electron force field model

- [[temp/partial]{.doc}]compute_temp_partial.md){.reference .internal} - temperature excluding one or more dimensions of velocity

- [[temp/profile]{.doc}]compute_temp_profile.md){.reference .internal} - temperature excluding a binned velocity profile

- [[temp/ramp]{.doc}]compute_temp_ramp.md){.reference .internal} - temperature excluding ramped velocity component

- [[temp/region]{.doc}]compute_temp_region.md){.reference .internal} - temperature of a region of atoms

- [[temp/region/eff]{.doc}]compute_temp_region_eff.md){.reference .internal} - temperature of a region of nuclei and electrons in the electron force field model

- [[temp/rotate]{.doc}]compute_temp_rotate.md){.reference .internal} - temperature of a group of atoms after subtracting out their center-of-mass and angular velocities

- [[temp/sphere]{.doc}]compute_temp_sphere.md){.reference .internal} - temperature of spherical particles

- [[temp/uef]{.doc}]compute_temp_uef.md){.reference .internal} - kinetic energy tensor in the reference frame of an applied flow field

- [[ti]{.doc}]compute_ti.md){.reference .internal} - thermodynamic integration free energy values

- [[torque/chunk]{.doc}]compute_torque_chunk.md){.reference .internal} - torque applied on each chunk

- [[vacf]{.doc}]compute_vacf.md){.reference .internal} - velocity auto-correlation function of group of atoms

- [[vacf/chunk]{.doc}]compute_vacf_chunk.md){.reference .internal} - velocity auto-correlation for the center of mass velocities of chunks of atoms

- [[vcm/chunk]{.doc}]compute_vcm_chunk.md){.reference .internal} - velocity of center-of-mass for each chunk

- [[viscosity/cos]{.doc}]compute_viscosity_cos.md){.reference .internal} - velocity profile under cosine-shaped acceleration

- [[voronoi/atom]{.doc}]compute_voronoi_atom.md){.reference .internal} - Voronoi volume and neighbors for each atom

- [[xrd]{.doc}]compute_xrd.md){.reference .internal} - X-ray diffraction intensity on a mesh of reciprocal lattice nodes
:::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[uncompute]{.doc}]uncompute.md){.reference .internal}, [[compute_modify]{.doc}]compute_modify.md){.reference .internal}, [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal}, [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal}, [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

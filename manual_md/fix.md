:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-command .section}
[]{#index-0}

# fix command[](#fix-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID style args
:::
::::

- ID = user-assigned name for the fix

- group-ID = ID of the group of atoms to apply the fix to

- style = one of a long list of possible style names (see below)

- args = arguments used by a particular style
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nve
    fix 3 all nvt temp 300.0 300.0 0.01
    fix mine top setforce 0.0 NULL 0.0
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Set a fix that will be applied to a group of atoms. In LAMMPS, a "fix" is any operation that is applied to the system during timestepping or minimization. Examples include updating of atom positions and velocities due to time integration, controlling temperature, applying constraint forces to atoms, enforcing boundary conditions, computing diagnostics, etc. There are hundreds of fixes defined in LAMMPS and new ones can be added; see the [[Modify]{.doc}]Modify.md){.reference .internal} page for details.

Fixes perform their operations at different stages of the timestep. If two or more fixes operate at the same stage of the timestep, they are invoked in the order they were specified in the input script.

The ID of a fix can only contain alphanumeric characters and underscores.

Fixes can be deleted with the [[unfix]{.doc}]unfix.md){.reference .internal} command.

::: {.admonition .note}
Note

The [[unfix]{.doc}]unfix.md){.reference .internal} command is the only way to turn off a fix; simply specifying a new fix with a similar style will not turn off the first one. This is especially important to realize for integration fixes. For example, using a [[fix nve]{.doc}]fix_nve.md){.reference .internal} command for a second run after using a [[fix nvt]{.doc}]fix_nh.md){.reference .internal} command for the first run will not cancel out the NVT time integration invoked by the "fix nvt" command. Thus, two time integrators would be in place!
:::

If you specify a new fix with the same ID and style as an existing fix, the old fix is deleted and the new one is created (presumably with new settings). This is the same as if an "unfix" command were first performed on the old fix, except that the new fix is kept in the same order relative to the existing fixes as the old one originally was. Note that this operation also wipes out any additional changes made to the old fix via the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command.

The [[fix modify]{.doc}]fix_modify.md){.reference .internal} command allows settings for some fixes to be reset. See the page for individual fixes for details.

Some fixes store an internal "state" which is written to binary restart files via the [[restart]{.doc}]restart.md){.reference .internal} or [[write_restart]{.doc}]write_restart.md){.reference .internal} commands. This allows the fix to continue on with its calculations in a restarted simulation. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file. See the doc pages for individual fixes for info on which ones can be restarted.

------------------------------------------------------------------------

Some fixes calculate and store any of four *styles* of quantities: global, per-atom, local, or per-grid.

A global quantity is one or more system-wide values, e.g. the energy of a wall interacting with particles. A per-atom quantity is one or more values per atom, e.g. the original coordinates of each atom at time 0. Per-atom values are set to 0.0 for atoms not in the specified fix group. Local quantities are calculated by each processor based on the atoms it owns, but there may be zero or more per atom, e.g. values for each bond. Per-grid quantities are calculated on a regular 2d or 3d grid which overlays a 2d or 3d simulation domain. The grid points and the data they store are distributed across processors; each processor owns the grid points which fall within its subdomain.

As a general rule of thumb, fixes that produce per-atom quantities have the word "atom" at the end of their style, e.g. *ave/atom*. Fixes that produce local quantities have the word "local" at the end of their style, e.g. *store/local*. Fixes that produce per-grid quantities have the word "grid" at the end of their style, e.g. *ave/grid*.

Global, per-atom, local, and per-grid quantities can also be of three *kinds*: a single scalar value (global only), a vector of values, or a 2d array of values. For per-atom, local, and per-grid quantities, a "vector" means a single value for each atom, each local entity (e.g. bond), or grid cell. Likewise an "array", means multiple values for each atom, each local entity, or each grid cell.

Note that a single fix can produce any combination of global, per-atom, local, or per-grid values. Likewise it can produce any combination of scalar, vector, or array output for each style. The exception is that for per-atom, local, and per-grid output, either a vector or array can be produced, but not both. The doc page for each fix explains the values it produces, if any.

When a fix output is accessed by another input script command it is referenced via the following bracket notation, where ID is the ID of the fix:

  ---------------- --------------------------------------------
  f_ID             entire scalar, vector, or array
  f_ID\[I\]        one element of vector, one column of array
  f_ID\[I\]\[J\]   one element of array
  ---------------- --------------------------------------------

In other words, using one bracket reduces the dimension of the quantity once (vector [\\(\\to\\)]{.math .notranslate .nohighlight} scalar, array [\\(\\to\\)]{.math .notranslate .nohighlight} vector). Using two brackets reduces the dimension twice (array [\\(\\to\\)]{.math .notranslate .nohighlight} scalar). Thus, for example, a command that uses global scalar fix values as input can also process elements of a vector or array. Depending on the command, this can either be done directly using the syntax in the table, or by first defining a [[variable]{.doc}]variable.md){.reference .internal} of the appropriate style to store the quantity, then using the variable as an input to the command.

Note that commands and [[variables]{.doc}]variable.md){.reference .internal} which take fix outputs as input typically do not allow for all styles and kinds of data (e.g., a command may require global but not per-atom values, or it may require a vector of values, not a scalar). This means there is typically no ambiguity about referring to a fix output as c_ID even if it produces, for example, both a scalar and vector. The doc pages for various commands explain the details, including how any ambiguities are resolved.

------------------------------------------------------------------------

In LAMMPS, the values generated by a fix can be used in several ways:

- Global values can be output via the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} or [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} command. Alternatively, the values can be referenced in an [[equal-style variable]{.doc}]variable.md){.reference .internal} command.

- Per-atom values can be output via the [[dump custom]{.doc}]dump.md){.reference .internal} command, or they can be time-averaged via the [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal} command or reduced by the [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} command. Alternatively, per-atom values can be referenced in an [[atom-style variable]{.doc}]variable.md){.reference .internal}.

- Local values can be reduced by the [[compute reduce]{.doc}]compute_reduce.md){.reference .internal} command or histogrammed by the [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal} command. They can also be output by the [[dump local]{.doc}]dump.md){.reference .internal} command.

See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for a summary of various LAMMPS output options, many of which involve fixes.

The results of fixes that calculate global quantities can be either "intensive" or "extensive" values. Intensive means the value is independent of the number of atoms in the simulation (e.g., temperature). Extensive means the value scales with the number of atoms in the simulation (e.g., total rotational kinetic energy). [[Thermodynamic output]{.doc}]thermo_style.md){.reference .internal} will normalize extensive values by the number of atoms in the system, depending on the "thermo_modify norm" setting. It will not normalize intensive values. If a fix value is accessed in another way (e.g., by a [[variable]{.doc}]variable.md){.reference .internal}), you may want to know whether it is an intensive or extensive value. See the page for individual fix styles for further info.

------------------------------------------------------------------------

Each fix style has its own page that describes its arguments and what it does, as listed below. Here is an alphabetical list of fix styles available in LAMMPS. They are also listed in more compact form on the [[Commands fix]{.doc}]Commands_fix.md){.reference .internal} doc page.

There are also additional accelerated fix styles included in the LAMMPS distribution for faster performance on CPUs, GPUs, and KNLs. The individual style names on the [[Commands fix]{.doc}]Commands_fix.md){.reference .internal} doc page are followed by one or more of (g,i,k,o,t) to indicate which accelerated styles exist.

- [[accelerate/cos]{.doc}]fix_accelerate_cos.md){.reference .internal} - apply cosine-shaped acceleration to atoms

- [[acks2/reaxff]{.doc}]fix_acks2_reaxff.md){.reference .internal} - apply ACKS2 charge equilibration

- [[adapt]{.doc}]fix_adapt.md){.reference .internal} - change a simulation parameter over time

- [[adapt/fep]{.doc}]fix_adapt_fep.md){.reference .internal} - enhanced version of fix adapt

- [[addforce]{.doc}]fix_addforce.md){.reference .internal} - add a force to each atom

- [[add/heat]{.doc}]fix_add_heat.md){.reference .internal} - add a heat flux to each atom

- [[addtorque/atom]{.doc}]fix_addtorque_atom.md){.reference .internal} - add a torque to a finite-size particles

- [[addtorque/group]{.doc}]fix_addtorque_group.md){.reference .internal} - add a torque to a group of atoms

- [[alchemy]{.doc}]fix_alchemy.md){.reference .internal} - perform an "alchemical transformation" between two partitions

- [[align/self]{.doc}]fix_align_self.md){.reference .internal} - add torque to groups of atoms due to a self-alignment

- [[amoeba/bitorsion]{.doc}]fix_amoeba_bitorsion.md){.reference .internal} - torsion/torsion terms in AMOEBA force field

- [[amoeba/pitorsion]{.doc}]fix_amoeba_pitorsion.md){.reference .internal} - 6-body terms in AMOEBA force field

- [[append/atoms]{.doc}]fix_append_atoms.md){.reference .internal} - append atoms to a running simulation

- [[atom/swap]{.doc}]fix_atom_swap.md){.reference .internal} - Monte Carlo atom type swapping

- [[atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal} - compute atomic load of an [[APIP potential]{.doc}]Howto_apip.md){.reference .internal} for load balancing

- [[ave/atom]{.doc}]fix_ave_atom.md){.reference .internal} - compute per-atom time-averaged quantities

- [[ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} - compute per-chunk time-averaged quantities

- [[ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} - compute/output time correlations

- [[ave/correlate/long]{.doc}]fix_ave_correlate_long.md){.reference .internal} - alternative to [[ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} that allows efficient calculation over long time windows

- [[ave/grid]{.doc}]fix_ave_grid.md){.reference .internal} - compute per-grid time-averaged quantities

- [[ave/histo]{.doc}]fix_ave_histo.md){.reference .internal} - compute/output time-averaged histograms

- [[ave/histo/weight]{.doc}]fix_ave_histo.md){.reference .internal} - weighted version of fix ave/histo

- [[ave/moments]{.doc}]fix_ave_moments.md){.reference .internal} - compute moments of scalar quantities

- [[ave/time]{.doc}]fix_ave_time.md){.reference .internal} - compute/output global time-averaged quantities

- [[aveforce]{.doc}]fix_aveforce.md){.reference .internal} - add an averaged force to each atom

- [[balance]{.doc}]fix_balance.md){.reference .internal} - perform dynamic load-balancing

- [[brownian]{.doc}]fix_brownian.md){.reference .internal} - overdamped translational brownian motion

- [[brownian/asphere]{.doc}]fix_brownian.md){.reference .internal} - overdamped translational and rotational brownian motion for ellipsoids

- [[brownian/sphere]{.doc}]fix_brownian.md){.reference .internal} - overdamped translational and rotational brownian motion for spheres

- [[bocs]{.doc}]fix_bocs.md){.reference .internal} - NPT style time integration with pressure correction

- [[bond/break]{.doc}]fix_bond_break.md){.reference .internal} - break bonds on the fly

- [[bond/create]{.doc}]fix_bond_create.md){.reference .internal} - create bonds on the fly

- [[bond/create/angle]{.doc}]fix_bond_create.md){.reference .internal} - create bonds on the fly with angle constraints

- [[bond/react]{.doc}]fix_bond_react.md){.reference .internal} - apply topology changes to model reactions

- [[bond/swap]{.doc}]fix_bond_swap.md){.reference .internal} - Monte Carlo bond swapping

- [[box/relax]{.doc}]fix_box_relax.md){.reference .internal} - relax box size during energy minimization

- [[charge/regulation]{.doc}]fix_charge_regulation.md){.reference .internal} - Monte Carlo sampling of charge regulation

- [[cmap]{.doc}]fix_cmap.md){.reference .internal} - CMAP torsion/torsion terms in CHARMM force field

- [[colvars]{.doc}]fix_colvars.md){.reference .internal} - interface to the collective variables "Colvars" library

- [[controller]{.doc}]fix_controller.md){.reference .internal} - apply control loop feedback mechanism

- [[damping/cundall]{.doc}]fix_damping_cundall.md){.reference .internal} - Cundall non-viscous damping for granular simulations

- [[deform]{.doc}]fix_deform.md){.reference .internal} - change the simulation box size/shape

- [[deform/pressure]{.doc}]fix_deform_pressure.md){.reference .internal} - change the simulation box size/shape with additional loading conditions

- [[deposit]{.doc}]fix_deposit.md){.reference .internal} - add new atoms above a surface

- [[dpd/energy]{.doc}]fix_dpd_energy.md){.reference .internal} - constant energy dissipative particle dynamics

- [[drag]{.doc}]fix_drag.md){.reference .internal} - drag atoms towards a defined coordinate

- [[drude]{.doc}]fix_drude.md){.reference .internal} - part of Drude oscillator polarization model

- [[drude/transform/direct]{.doc}]fix_drude_transform.md){.reference .internal} - part of Drude oscillator polarization model

- [[drude/transform/inverse]{.doc}]fix_drude_transform.md){.reference .internal} - part of Drude oscillator polarization model

- [[dt/reset]{.doc}]fix_dt_reset.md){.reference .internal} - reset the timestep based on velocity, forces

- [[edpd/source]{.doc}]fix_dpd_source.md){.reference .internal} - add heat source to eDPD simulations

- [[efield]{.doc}]fix_efield.md){.reference .internal} - impose electric field on system

- [[efield/lepton]{.doc}]fix_efield_lepton.md){.reference .internal} - impose electric field on system using a Lepton expression for the potential

- [[efield/tip4p]{.doc}]fix_efield.md){.reference .internal} - impose electric field on system with TIP4P molecules

- [[ehex]{.doc}]fix_ehex.md){.reference .internal} - enhanced heat exchange algorithm

- [[electrode/conp]{.doc}]fix_electrode.md){.reference .internal} - impose electric potential

- [[electrode/conq]{.doc}]fix_electrode.md){.reference .internal} - impose total electric charge

- [[electrode/thermo]{.doc}]fix_electrode.md){.reference .internal} - apply thermo-potentiostat

- [[electron/stopping]{.doc}]fix_electron_stopping.md){.reference .internal} - electronic stopping power as a friction force

- [[electron/stopping/fit]{.doc}]fix_electron_stopping.md){.reference .internal} - electronic stopping power as a friction force

- [[enforce2d]{.doc}]fix_enforce2d.md){.reference .internal} - zero out *z*-dimension velocity and force

- [[eos/cv]{.doc}]fix_eos_cv.md){.reference .internal} - applies a mesoparticle equation of state to relate the particle internal energy to the particle internal temperature

- [[eos/table]{.doc}]fix_eos_table.md){.reference .internal} - applies a tabulated mesoparticle equation of state to relate the particle internal energy to the particle internal temperature

- [[eos/table/rx]{.doc}]fix_eos_table_rx.md){.reference .internal} - applies a tabulated mesoparticle equation of state to relate the concentration-dependent particle internal energy to the particle internal temperature

- [[evaporate]{.doc}]fix_evaporate.md){.reference .internal} - remove atoms from simulation periodically

- [[external]{.doc}]fix_external.md){.reference .internal} - callback to an external driver program

- [[ffl]{.doc}]fix_ffl.md){.reference .internal} - apply a Fast-Forward Langevin equation thermostat

- [[filter/corotate]{.doc}]fix_filter_corotate.md){.reference .internal} - implement corotation filter to allow larger timesteps with r-RESPA

- [[flow/gauss]{.doc}]fix_flow_gauss.md){.reference .internal} - Gaussian dynamics for constant mass flux

- [[freeze]{.doc}]fix_freeze.md){.reference .internal} - freeze atoms in a granular simulation

- [[gcmc]{.doc}]fix_gcmc.md){.reference .internal} - grand canonical insertions/deletions

- [[gjf]{.doc}]fix_gjf.md){.reference .internal} - statistically correct Langevin temperature control using the GJ methods

- [[gld]{.doc}]fix_gld.md){.reference .internal} - generalized Langevin dynamics integrator

- [[gle]{.doc}]fix_gle.md){.reference .internal} - generalized Langevin equation thermostat

- [[graphics/arrows]{.doc}]fix_graphics_arrows.md){.reference .internal} - add arrow graphics objects to [[dump image]{.doc}]dump_image.md){.reference .internal} output

- [[graphics/isosurface]{.doc}]fix_graphics_isosurface.md){.reference .internal} - add an isosurface for a group of atoms to [[dump image]{.doc}]dump_image.md){.reference .internal} output

- [[graphics/labels]{.doc}]fix_graphics_labels.md){.reference .internal} - add images or text as graphics objects to [[dump image]{.doc}]dump_image.md){.reference .internal} output

- [[graphics/lines]{.doc}]fix_graphics_lines.md){.reference .internal} - add a trace of atom positions to [[dump image]{.doc}]dump_image.md){.reference .internal} output

- [[graphics/objects]{.doc}]fix_graphics_objects.md){.reference .internal} - add graphics objects to [[dump image]{.doc}]dump_image.md){.reference .internal} output

- [[graphics/periodic]{.doc}]fix_graphics_periodic.md){.reference .internal} - add selected periodic images of atoms and bonds to [[dump image]{.doc}]dump_image.md){.reference .internal} output

- [[gravity]{.doc}]fix_gravity.md){.reference .internal} - add gravity to atoms in a granular simulation

- [[grem]{.doc}]fix_grem.md){.reference .internal} - implements the generalized replica exchange method

- [[halt]{.doc}]fix_halt.md){.reference .internal} - terminate a dynamics run or minimization

- [[heat]{.doc}]fix_heat.md){.reference .internal} - add/subtract momentum-conserving heat

- [[heat/flow]{.doc}]fix_heat_flow.md){.reference .internal} - plain time integration of heat flow with per-atom temperature updates

- [[hmc]{.doc}]fix_hmc.md){.reference .internal} - Hybrid/Hamiltonian Monte Carlo (HMC) particle propagation

- [[hyper/global]{.doc}]fix_hyper_global.md){.reference .internal} - global hyperdynamics

- [[hyper/local]{.doc}]fix_hyper_local.md){.reference .internal} - local hyperdynamics

- [[imd]{.doc}]fix_imd.md){.reference .internal} - implements the "Interactive MD" (IMD) protocol

- [[indent]{.doc}]fix_indent.md){.reference .internal} - impose force due to an indenter

- [[ipi]{.doc}]fix_ipi.md){.reference .internal} - enable LAMMPS to run as a client for i-PI path-integral simulations

- [[lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal} - compute switching parameter, that controls the precision of an [[APIP potential]{.doc}]Howto_apip.md){.reference .internal}

- [[lambda/la/csp/apip]{.doc}]fix_lambda_la_csp_apip.md){.reference .internal} - compute a conservative switching parameter, that controls the precision of an [[APIP potential]{.doc}]Howto_apip.md){.reference .internal}

- [[langevin]{.doc}]fix_langevin.md){.reference .internal} - Langevin temperature control

- [[langevin/drude]{.doc}]fix_langevin_drude.md){.reference .internal} - Langevin temperature control of Drude oscillators

- [[langevin/eff]{.doc}]fix_langevin_eff.md){.reference .internal} - Langevin temperature control for the electron force field model

- [[langevin/spin]{.doc}]fix_langevin_spin.md){.reference .internal} - Langevin temperature control for a spin or spin-lattice system

- [[lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal} - lattice-Boltzmann fluid on a uniform mesh

- [[lb/momentum]{.doc}]fix_lb_momentum.md){.reference .internal} - [[fix momentum]{.doc}]fix_momentum.md){.reference .internal} replacement for use with a lattice-Boltzmann fluid

- [[lb/viscous]{.doc}]fix_lb_viscous.md){.reference .internal} - [[fix viscous]{.doc}]fix_viscous.md){.reference .internal} replacement for use with a lattice-Boltzmann fluid

- [[lineforce]{.doc}]fix_lineforce.md){.reference .internal} - constrain atoms to move in a line

- [[lambda_thermostat/apip]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal} - apply energy conserving correction for an [[APIP potential]{.doc}]Howto_apip.md){.reference .internal}

- [[manifoldforce]{.doc}]fix_manifoldforce.md){.reference .internal} - restrain atoms to a manifold during minimization

- [[mdi/qm]{.doc}]fix_mdi_qm.md){.reference .internal} - LAMMPS operates as a client for a quantum code via the MolSSI Driver Interface (MDI)

- [[mdi/qmmm]{.doc}]fix_mdi_qmmm.md){.reference .internal} - LAMMPS operates as client for QM/MM simulation with a quantum code via the MolSSI Driver Interface (MDI)

- [[meso/move]{.doc}]fix_meso_move.md){.reference .internal} - move mesoscopic SPH/SDPD particles in a prescribed fashion

- [[mol/swap]{.doc}]fix_mol_swap.md){.reference .internal} - Monte Carlo atom type swapping with a molecule

- [[momentum]{.doc}]fix_momentum.md){.reference .internal} - zero the linear and/or angular momentum of a group of atoms

- [[momentum/chunk]{.doc}]fix_momentum.md){.reference .internal} - zero the linear and/or angular momentum of a chunk of atoms

- [[move]{.doc}]fix_move.md){.reference .internal} - move atoms in a prescribed fashion

- [[msst]{.doc}]fix_msst.md){.reference .internal} - multi-scale shock technique (MSST) integration

- [[mvv/dpd]{.doc}]fix_mvv_dpd.md){.reference .internal} - DPD using the modified velocity-Verlet integration algorithm

- [[mvv/edpd]{.doc}]fix_mvv_dpd.md){.reference .internal} - constant energy DPD using the modified velocity-Verlet algorithm

- [[mvv/tdpd]{.doc}]fix_mvv_dpd.md){.reference .internal} - constant temperature DPD using the modified velocity-Verlet algorithm

- [[neb]{.doc}]fix_neb.md){.reference .internal} - nudged elastic band (NEB) spring forces

- [[neb/spin]{.doc}]fix_neb_spin.md){.reference .internal} - nudged elastic band (NEB) spring forces for spins

- [[neighbor/swap]{.doc}]fix_neighbor_swap.md){.reference .internal} - kinetic Monte Carlo (kMC) atom swapping

- [[nonaffine/displacement]{.doc}]fix_nonaffine_displacement.md){.reference .internal} - calculate nonaffine displacement of atoms

- [[nph]{.doc}]fix_nh.md){.reference .internal} - constant NPH time integration via Nose/Hoover

- [[nph/asphere]{.doc}]fix_nph_asphere.md){.reference .internal} - NPH for aspherical particles

- [[nph/body]{.doc}]fix_nph_body.md){.reference .internal} - NPH for body particles

- [[nph/eff]{.doc}]fix_nh_eff.md){.reference .internal} - NPH for nuclei and electrons in the electron force field model

- [[nph/sphere]{.doc}]fix_nph_sphere.md){.reference .internal} - NPH for spherical particles

- [[nphug]{.doc}]fix_nphug.md){.reference .internal} - constant-stress Hugoniostat integration

- [[npt]{.doc}]fix_nh.md){.reference .internal} - constant NPT time integration via Nose/Hoover

- [[npt/asphere]{.doc}]fix_npt_asphere.md){.reference .internal} - NPT for aspherical particles

- [[npt/body]{.doc}]fix_npt_body.md){.reference .internal} - NPT for body particles

- [[npt/cauchy]{.doc}]fix_npt_cauchy.md){.reference .internal} - NPT with Cauchy stress

- [[npt/eff]{.doc}]fix_nh_eff.md){.reference .internal} - NPT for nuclei and electrons in the electron force field model

- [[npt/sphere]{.doc}]fix_npt_sphere.md){.reference .internal} - NPT for spherical particles

- [[npt/uef]{.doc}]fix_nh_uef.md){.reference .internal} - NPT style time integration with diagonal flow

- [[numdiff]{.doc}]fix_numdiff.md){.reference .internal} - numerically approximate atomic forces using finite energy differences

- [[numdiff/virial]{.doc}]fix_numdiff_virial.md){.reference .internal} - numerically approximate virial stress tensor using finite energy differences

- [[nve]{.doc}]fix_nve.md){.reference .internal} - constant NVE time integration

- [[nve/asphere]{.doc}]fix_nve_asphere.md){.reference .internal} - NVE for aspherical particles

- [[nve/asphere/noforce]{.doc}]fix_nve_asphere_noforce.md){.reference .internal} - NVE for aspherical particles without forces

- [[nve/body]{.doc}]fix_nve_body.md){.reference .internal} - NVE for body particles

- [[nve/dot]{.doc}]fix_nve_dot.md){.reference .internal} - rigid body constant energy time integrator for coarse grain models

- [[nve/dotc/langevin]{.doc}]fix_nve_dotc_langevin.md){.reference .internal} - Langevin style rigid body time integrator for coarse grain models

- [[nve/eff]{.doc}]fix_nve_eff.md){.reference .internal} - NVE for nuclei and electrons in the electron force field model

- [[nve/limit]{.doc}]fix_nve_limit.md){.reference .internal} - NVE with limited step length

- [[nve/line]{.doc}]fix_nve_line.md){.reference .internal} - NVE for line segments

- [[nve/manifold/rattle]{.doc}]fix_nve_manifold_rattle.md){.reference .internal} - NVE time integration for atoms constrained to a curved surface (manifold)

- [[nve/noforce]{.doc}]fix_nve_noforce.md){.reference .internal} - NVE without forces (update positions only)

- [[nve/sphere]{.doc}]fix_nve_sphere.md){.reference .internal} - NVE for spherical particles

- [[nve/bpm/sphere]{.doc}]fix_nve_bpm_sphere.md){.reference .internal} - NVE for spherical particles used in the BPM package

- [[nve/spin]{.doc}]fix_nve_spin.md){.reference .internal} - NVE for a spin or spin-lattice system

- [[nve/tri]{.doc}]fix_nve_tri.md){.reference .internal} - NVE for triangles

- [[nvk]{.doc}]fix_nvk.md){.reference .internal} - constant kinetic energy time integration

- [[nvt]{.doc}]fix_nh.md){.reference .internal} - NVT time integration via Nose/Hoover

- [[nvt/asphere]{.doc}]fix_nvt_asphere.md){.reference .internal} - NVT for aspherical particles

- [[nvt/body]{.doc}]fix_nvt_body.md){.reference .internal} - NVT for body particles

- [[nvt/eff]{.doc}]fix_nh_eff.md){.reference .internal} - NVE for nuclei and electrons in the electron force field model

- [[nvt/manifold/rattle]{.doc}]fix_nvt_manifold_rattle.md){.reference .internal} - NVT time integration for atoms constrained to a curved surface (manifold)

- [[nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal} - NVT for NEMD with SLLOD equations

- [[nvt/sllod/eff]{.doc}]fix_nvt_sllod_eff.md){.reference .internal} - NVT for NEMD with SLLOD equations for the electron force field model

- [[nvt/sphere]{.doc}]fix_nvt_sphere.md){.reference .internal} - NVT for spherical particles

- [[nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal} - NVT style time integration with diagonal flow

- [[oneway]{.doc}]fix_oneway.md){.reference .internal} - constrain particles on move in one direction

- [[orient/bcc]{.doc}]fix_orient.md){.reference .internal} - add grain boundary migration force for BCC

- [[orient/fcc]{.doc}]fix_orient.md){.reference .internal} - add grain boundary migration force for FCC

- [[orient/eco]{.doc}]fix_orient_eco.md){.reference .internal} - add generalized grain boundary migration force

- [[pafi]{.doc}]fix_pafi.md){.reference .internal} - constrained force averages on hyper-planes to compute free energies (PAFI)

- [[pair]{.doc}]fix_pair.md){.reference .internal} - access per-atom info from pair styles

- [[phonon]{.doc}]fix_phonon.md){.reference .internal} - calculate dynamical matrix from MD simulations

- [[pimd/langevin]{.doc}]fix_pimd.md){.reference .internal} - Feynman path-integral molecular dynamics with stochastic thermostat

- [[pimd/nvt]{.doc}]fix_pimd.md){.reference .internal} - Feynman path-integral molecular dynamics with Nose-Hoover thermostat

- [[pimd/langevin/bosonic]{.doc}]fix_pimd.md){.reference .internal} - Bosonic Feynman path-integral molecular dynamics for with stochastic thermostat

- [[pimd/nvt/bosonic]{.doc}]fix_pimd.md){.reference .internal} - Bosonic Feynman path-integral molecular dynamics with Nose-Hoover thermostat

- [[planeforce]{.doc}]fix_planeforce.md){.reference .internal} - constrain atoms to move in a plane

- [[plumed]{.doc}]fix_plumed.md){.reference .internal} - wrapper on PLUMED free energy library

- [[polarize/bem/gmres]{.doc}]fix_polarize.md){.reference .internal} - compute induced charges at the interface between impermeable media with different dielectric constants with generalized minimum residual (GMRES)

- [[polarize/bem/icc]{.doc}]fix_polarize.md){.reference .internal} - compute induced charges at the interface between impermeable media with different dielectric constants with the successive over-relaxation algorithm

- [[polarize/functional]{.doc}]fix_polarize.md){.reference .internal} - compute induced charges at the interface between impermeable media with different dielectric constants with the energy variational approach

- [[pour]{.doc}]fix_pour.md){.reference .internal} - pour new atoms/molecules into a granular simulation domain

- [[precession/spin]{.doc}]fix_precession_spin.md){.reference .internal} - apply a precession torque to each magnetic spin

- [[press/berendsen]{.doc}]fix_press_berendsen.md){.reference .internal} - pressure control by Berendsen barostat

- [[press/langevin]{.doc}]fix_press_langevin.md){.reference .internal} - pressure control by Langevin barostat

- [[print]{.doc}]fix_print.md){.reference .internal} - print text and variables during a simulation

- [[propel/self]{.doc}]fix_propel_self.md){.reference .internal} - model self-propelled particles

- [[property/atom]{.doc}]fix_property_atom.md){.reference .internal} - add customized per-atom values

- [[python/invoke]{.doc}]fix_python_invoke.md){.reference .internal} - call a Python function during a simulation

- [[python/move]{.doc}]fix_python_move.md){.reference .internal} - move particles using a Python function during a simulation run

- [[qbmsst]{.doc}]fix_qbmsst.md){.reference .internal} - quantum bath multi-scale shock technique time integrator

- [[qeq/comb]{.doc}]fix_qeq_comb.md){.reference .internal} - charge equilibration for COMB potential

- [[qeq/ctip]{.doc}]fix_qeq.md){.reference .internal} - charge equilibration for CTIP potential

- [[qeq/dynamic]{.doc}]fix_qeq.md){.reference .internal} - charge equilibration via dynamic method

- [[qeq/fire]{.doc}]fix_qeq.md){.reference .internal} - charge equilibration via FIRE minimizer

- [[qeq/point]{.doc}]fix_qeq.md){.reference .internal} - charge equilibration via point method

- [[qeq/reaxff]{.doc}]fix_qeq_reaxff.md){.reference .internal} - charge equilibration for ReaxFF potential

- [[qeq/rel/reaxff]{.doc}]fix_qeq_rel_reaxff.md){.reference .internal} - charge equilibration for ReaxFF potential with alternate efield implementation

- [[qeq/shielded]{.doc}]fix_qeq.md){.reference .internal} - charge equilibration via shielded method

- [[qeq/slater]{.doc}]fix_qeq.md){.reference .internal} - charge equilibration via Slater method

- [[qmmm]{.doc}]fix_qmmm.md){.reference .internal} - functionality to enable a quantum mechanics/molecular mechanics coupling

- [[qtb]{.doc}]fix_qtb.md){.reference .internal} - implement quantum thermal bath scheme

- [[qtpie/reaxff]{.doc}]fix_qtpie_reaxff.md){.reference .internal} - apply QTPIE charge equilibration

- [[rattle]{.doc}]fix_shake.md){.reference .internal} - RATTLE constraints on bonds and/or angles

- [[reaxff/bonds]{.doc}]fix_reaxff_bonds.md){.reference .internal} - write out ReaxFF bond information

- [[reaxff/species]{.doc}]fix_reaxff_species.md){.reference .internal} - write out ReaxFF molecule information

- [[recenter]{.doc}]fix_recenter.md){.reference .internal} - constrain the center-of-mass position of a group of atoms

- [[restrain]{.doc}]fix_restrain.md){.reference .internal} - constrain a bond, angle, dihedral

- [[rheo]{.doc}]fix_rheo.md){.reference .internal} - integrator for the RHEO package

- [[rheo/thermal]{.doc}]fix_rheo_thermal.md){.reference .internal} - thermal integrator for the RHEO package

- [[rheo/oxidation]{.doc}]fix_rheo_oxidation.md){.reference .internal} - create oxidation bonds for the RHEO package

- [[rheo/pressure]{.doc}]fix_rheo_pressure.md){.reference .internal} - pressure calculation for the RHEO package

- [[rheo/viscosity]{.doc}]fix_rheo_pressure.md){.reference .internal} - viscosity calculation for the RHEO package

- [[rhok]{.doc}]fix_rhok.md){.reference .internal} - add bias potential for long-range ordered systems

- [[rigid]{.doc}]fix_rigid.md){.reference .internal} - constrain one or more clusters of atoms to move as a rigid body with NVE integration

- [[rigid/meso]{.doc}]fix_rigid_meso.md){.reference .internal} - constrain clusters of mesoscopic SPH/SDPD particles to move as a rigid body

- [[rigid/nph]{.doc}]fix_rigid.md){.reference .internal} - constrain one or more clusters of atoms to move as a rigid body with NPH integration

- [[rigid/nph/small]{.doc}]fix_rigid.md){.reference .internal} - constrain many small clusters of atoms to move as a rigid body with NPH integration

- [[rigid/npt]{.doc}]fix_rigid.md){.reference .internal} - constrain one or more clusters of atoms to move as a rigid body with NPT integration

- [[rigid/npt/small]{.doc}]fix_rigid.md){.reference .internal} - constrain many small clusters of atoms to move as a rigid body with NPT integration

- [[rigid/nve]{.doc}]fix_rigid.md){.reference .internal} - constrain one or more clusters of atoms to move as a rigid body with alternate NVE integration

- [[rigid/nve/small]{.doc}]fix_rigid.md){.reference .internal} - constrain many small clusters of atoms to move as a rigid body with alternate NVE integration

- [[rigid/nvt]{.doc}]fix_rigid.md){.reference .internal} - constrain one or more clusters of atoms to move as a rigid body with NVT integration

- [[rigid/nvt/small]{.doc}]fix_rigid.md){.reference .internal} - constrain many small clusters of atoms to move as a rigid body with NVT integration

- [[rigid/small]{.doc}]fix_rigid.md){.reference .internal} - constrain many small clusters of atoms to move as a rigid body with NVE integration

- [[rx]{.doc}]fix_rx.md){.reference .internal} - solve reaction kinetic ODEs for a defined reaction set

- [[saed/vtk]{.doc}]fix_saed_vtk.md){.reference .internal} - time-average the intensities from [[compute saed]{.doc}]compute_saed.md){.reference .internal}

- [[set]{.doc}]fix_set.md){.reference .internal} - reset an atom property via an atom-style variable every N steps

- [[setforce]{.doc}]fix_setforce.md){.reference .internal} - set the force on each atom

- [[setforce/spin]{.doc}]fix_setforce.md){.reference .internal} - set magnetic precession vectors on each atom

- [[settorque/atom]{.doc}]fix_settorque_atom.md){.reference .internal} - set the torque on each finite-size atom

- [[sgcmc]{.doc}]fix_sgcmc.md){.reference .internal} - fix for hybrid semi-grand canonical MD/MC simulations

- [[shake]{.doc}]fix_shake.md){.reference .internal} - SHAKE constraints on bonds and/or angles

- [[shardlow]{.doc}]fix_shardlow.md){.reference .internal} - integration of DPD equations of motion using the Shardlow splitting

- [[smd]{.doc}]fix_smd.md){.reference .internal} - applied a steered MD force to a group

- [[smd/adjust_dt]{.doc}]fix_smd_adjust_dt.md){.reference .internal} - calculate a new stable time increment for use with SMD integrators

- [[smd/integrate_tlsph]{.doc}]fix_smd_integrate_tlsph.md){.reference .internal} - explicit time integration with total Lagrangian SPH pair style

- [[smd/integrate_ulsph]{.doc}]fix_smd_integrate_ulsph.md){.reference .internal} - explicit time integration with updated Lagrangian SPH pair style

- [[smd/move_tri_surf]{.doc}]fix_smd_move_triangulated_surface.md){.reference .internal} - update position and velocity near rigid surfaces using SPH integrators

- [[smd/setvel]{.doc}]fix_smd_setvel.md){.reference .internal} - sets each velocity component, ignoring forces, for Smooth Mach Dynamics

- [[smd/wall_surface]{.doc}]fix_smd_wall_surface.md){.reference .internal} - create a rigid wall with a triangulated surface for use in Smooth Mach Dynamics

- [[sph]{.doc}]fix_sph.md){.reference .internal} - time integration for SPH/DPDE particles

- [[sph/stationary]{.doc}]fix_sph_stationary.md){.reference .internal} - update energy and density but not position or velocity in Smooth Particle Hydrodynamics

- [[spring]{.doc}]fix_spring.md){.reference .internal} - apply harmonic spring force to group of atoms

- [[spring/chunk]{.doc}]fix_spring_chunk.md){.reference .internal} - apply harmonic spring force to each chunk of atoms

- [[spring/rg]{.doc}]fix_spring_rg.md){.reference .internal} - spring on radius of gyration of group of atoms

- [[spring/self]{.doc}]fix_spring_self.md){.reference .internal} - spring from each atom to its origin

- [[srd]{.doc}]fix_srd.md){.reference .internal} - stochastic rotation dynamics (SRD)

- [[store/force]{.doc}]fix_store_force.md){.reference .internal} - store force on each atom

- [[store/state]{.doc}]fix_store_state.md){.reference .internal} - store attributes for each atom

- [[tdpd/source]{.doc}]fix_dpd_source.md){.reference .internal} - add external concentration source

- [[temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal} - temperature control by Berendsen thermostat

- [[temp/csld]{.doc}]fix_temp_csvr.md){.reference .internal} - canonical sampling thermostat with Langevin dynamics

- [[temp/csvr]{.doc}]fix_temp_csvr.md){.reference .internal} - canonical sampling thermostat with Hamiltonian dynamics

- [[temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal} - temperature control by velocity rescaling

- [[temp/rescale/eff]{.doc}]fix_temp_rescale_eff.md){.reference .internal} - temperature control by velocity rescaling in the electron force field model

- [[tfmc]{.doc}]fix_tfmc.md){.reference .internal} - perform force-bias Monte Carlo with time-stamped method

- [[tgnvt/drude]{.doc}]fix_tgnh_drude.md){.reference .internal} - NVT time integration for Drude polarizable model via temperature-grouped Nose-Hoover

- [[tgnpt/drude]{.doc}]fix_tgnh_drude.md){.reference .internal} - NPT time integration for Drude polarizable model via temperature-grouped Nose-Hoover

- [[thermal/conductivity]{.doc}]fix_thermal_conductivity.md){.reference .internal} - Mueller-Plathe kinetic energy exchange for thermal conductivity calculation

- [[ti/spring]{.doc}]fix_ti_spring.md){.reference .internal} - perform thermodynamic integration between a solid and an Einstein crystal

- [[tmd]{.doc}]fix_tmd.md){.reference .internal} - guide a group of atoms to a new configuration

- [[ttm]{.doc}]fix_ttm.md){.reference .internal} - two-temperature model for electronic/atomic coupling (replicated grid)

- [[ttm/grid]{.doc}]fix_ttm.md){.reference .internal} - two-temperature model for electronic/atomic coupling (distributed grid)

- [[ttm/mod]{.doc}]fix_ttm.md){.reference .internal} - enhanced two-temperature model with additional options

- [[ttm/thermal]{.doc}]fix_ttm.md){.reference .internal} - a two-temperature model for thermal transport

- [[tune/kspace]{.doc}]fix_tune_kspace.md){.reference .internal} - auto-tune [\\(k\\)]{.math .notranslate .nohighlight}-space parameters

- [[vector]{.doc}]fix_vector.md){.reference .internal} - accumulate a global vector every *N* timesteps

- [[viscosity]{.doc}]fix_viscosity.md){.reference .internal} - Mueller-Plathe momentum exchange for viscosity calculation

- [[viscous]{.doc}]fix_viscous.md){.reference .internal} - viscous damping for granular simulations

- [[viscous/sphere]{.doc}]fix_viscous_sphere.md){.reference .internal} - viscous damping on angular velocity for granular simulations

- [[wall/body/polygon]{.doc}]fix_wall_body_polygon.md){.reference .internal} - time integration for body particles of style [[rounded/polygon]{.doc}]Howto_body.md){.reference .internal}

- [[wall/body/polyhedron]{.doc}]fix_wall_body_polyhedron.md){.reference .internal} - time integration for body particles of style [[rounded/polyhedron]{.doc}]Howto_body.md){.reference .internal}

- [[wall/colloid]{.doc}]fix_wall.md){.reference .internal} - Lennard-Jones wall interacting with finite-size particles

- [[wall/ees]{.doc}]fix_wall_ees.md){.reference .internal} - wall for ellipsoidal particles

- [[wall/flow]{.doc}]fix_wall_flow.md){.reference .internal} - flow boundary conditions

- [[wall/gran]{.doc}]fix_wall_gran.md){.reference .internal} - frictional wall(s) for granular simulations

- [[wall/gran/region]{.doc}]fix_wall_gran_region.md){.reference .internal} - [[fix wall/region]{.doc}]fix_wall_region.md){.reference .internal} equivalent for use with granular particles

- [[wall/harmonic]{.doc}]fix_wall.md){.reference .internal} - harmonic spring wall

- [[wall/harmonic/outside]{.doc}]fix_wall.md){.reference .internal} - harmonic spring wall for containing particles

- [[wall/lj1043]{.doc}]fix_wall.md){.reference .internal} - Lennard-Jones 10--4--3 wall

- [[wall/lj126]{.doc}]fix_wall.md){.reference .internal} - Lennard-Jones 12--6 wall

- [[wall/lj93]{.doc}]fix_wall.md){.reference .internal} - Lennard-Jones 9--3 wall

- [[wall/lepton]{.doc}]fix_wall.md){.reference .internal} - Custom Lepton expression wall

- [[wall/morse]{.doc}]fix_wall.md){.reference .internal} - Morse potential wall

- [[wall/piston]{.doc}]fix_wall_piston.md){.reference .internal} - moving reflective piston wall

- [[wall/reflect]{.doc}]fix_wall_reflect.md){.reference .internal} - reflecting wall(s)

- [[wall/reflect/stochastic]{.doc}]fix_wall_reflect_stochastic.md){.reference .internal} - reflecting wall(s) with finite temperature

- [[wall/region]{.doc}]fix_wall_region.md){.reference .internal} - use region surface as wall

- [[wall/region/ees]{.doc}]fix_wall_ees.md){.reference .internal} - use region surface as wall for ellipsoidal particles

- [[wall/srd]{.doc}]fix_wall_srd.md){.reference .internal} - slip/no-slip wall for SRD particles

- [[wall/table]{.doc}]fix_wall.md){.reference .internal} - Tabulated potential wall wall

- [[widom]{.doc}]fix_widom.md){.reference .internal} - Widom insertions of atoms or molecules
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Some fix styles are part of specific packages. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. The doc pages for individual fixes tell if it is part of a package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[unfix]{.doc}]unfix.md){.reference .internal}, [[fix_modify]{.doc}]fix_modify.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

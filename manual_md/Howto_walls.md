::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#walls .section}
# [10.2.6. ]{.section-number}Walls[](#walls "Link to this heading"){.headerlink}

Walls in an MD simulation are typically used to bound particle motion, i.e. to serve as a boundary condition.

Walls in LAMMPS can be of rough (made of particles) or idealized surfaces. Ideal walls can be smooth, generating forces only in the normal direction, or frictional, generating forces also in the tangential direction.

Rough walls, built of particles, can be created in various ways. The particles themselves can be generated like any other particle, via the [[lattice]{.doc}]lattice.md){.reference .internal} and [[create_atoms]{.doc}]create_atoms.md){.reference .internal} commands, or read in via the [[read_data]{.doc}]read_data.md){.reference .internal} command.

Their motion can be constrained by many different commands, so that they do not move at all, move together as a group at constant velocity or in response to a net force acting on them, move in a prescribed fashion (e.g. rotate around a point), etc. Note that if a time integration fix like [[fix nve]{.doc}]fix_nve.md){.reference .internal} or [[fix nvt]{.doc}]fix_nh.md){.reference .internal} is not used with the group that contains wall particles, their positions and velocities will not be updated.

- [[fix aveforce]{.doc}]fix_aveforce.md){.reference .internal} - set force on particles to average value, so they move together

- [[fix setforce]{.doc}]fix_setforce.md){.reference .internal} - set force on particles to a value, e.g. 0.0

- [[fix freeze]{.doc}]fix_freeze.md){.reference .internal} - freeze particles for use as granular walls

- [[fix nve/noforce]{.doc}]fix_nve_noforce.md){.reference .internal} - advect particles by their velocity, but without force

- [[fix move]{.doc}]fix_move.md){.reference .internal} - prescribe motion of particles by a linear velocity, oscillation, rotation, variable

The [[fix move]{.doc}]fix_move.md){.reference .internal} command offers the most generality, since the motion of individual particles can be specified with [[variable]{.doc}]variable.md){.reference .internal} formula which depends on time and/or the particle position.

For rough walls, it may be useful to turn off pairwise interactions between wall particles via the [[neigh_modify exclude]{.doc}]neigh_modify.md){.reference .internal} command.

Rough walls can also be created by specifying frozen particles that do not move and do not interact with mobile particles, and then tethering other particles to the fixed particles, via a [[bond]{.doc}]bond_style.md){.reference .internal}. The bonded particles do interact with other mobile particles.

Idealized walls can be specified via several fix commands. [[Fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal} creates frictional walls for use with granular particles; all the other commands create smooth walls.

- [[fix wall/reflect]{.doc}]fix_wall_reflect.md){.reference .internal} - reflective flat walls

- [[fix wall/lj93]{.doc}]fix_wall.md){.reference .internal} - flat walls, with Lennard-Jones 9/3 potential

- [[fix wall/lj126]{.doc}]fix_wall.md){.reference .internal} - flat walls, with Lennard-Jones 12/6 potential

- [[fix wall/colloid]{.doc}]fix_wall.md){.reference .internal} - flat walls, with [[pair_style colloid]{.doc}]pair_colloid.md){.reference .internal} potential

- [[fix wall/harmonic]{.doc}]fix_wall.md){.reference .internal} - flat walls, with repulsive harmonic spring potential

- [[fix wall/morse]{.doc}]fix_wall.md){.reference .internal} - flat walls, with Morse potential

- [[fix wall/region]{.doc}]fix_wall_region.md){.reference .internal} - use region surface as wall

- [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal} - flat or curved walls with [[pair_style granular]{.doc}]pair_gran.md){.reference .internal} potential

The *lj93*, *lj126*, *colloid*, *harmonic*, and *morse* styles all allow the flat walls to move with a constant velocity, or oscillate in time. The [[fix wall/region]{.doc}]fix_wall_region.md){.reference .internal} command offers the most generality, since the region surface is treated as a wall, and the geometry of the region can be a simple primitive volume (e.g. a sphere, or cube, or plane), or a complex volume made from the union and intersection of primitive volumes. [[Regions]{.doc}]region.md){.reference .internal} can also specify a volume "interior" or "exterior" to the specified primitive shape or *union* or *intersection*. [[Regions]{.doc}]region.md){.reference .internal} can also be "dynamic" meaning they move with constant velocity, oscillate, or rotate.

The only frictional idealized walls currently in LAMMPS are flat or curved surfaces specified by the [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal} command. At some point we plan to allow region surfaces to be used as frictional walls, as well as triangulated surfaces.
:::
::::
:::::

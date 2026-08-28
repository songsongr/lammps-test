::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::: {#atom-style-command .section}
[]{#index-0}

# atom_style command[](#atom-style-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    atom_style style args
:::
::::

- style = *amoeba* or *angle* or *apip* or *atomic* or *body* or *bond* or *charge* or *dielectric* or *dipole* or *dpd* or *edpd* or *electron* or *ellipsoid* or *full* or *line* or *mdpd* or *molecular* or *oxdna* or *peri* or *smd* or *sph* or *sphere* or *bpm/sphere* or *spin* or *tdpd* or *tri* or *template* or *hybrid*

  ``` literal-block
  args = none for any style except the following
    apip arg = conservative/thermostat (optional) for conservative APIP/lambda thermostat APIP
    body args = bstyle bstyle-args
      bstyle = style of body particles
      bstyle-args = additional arguments specific to the bstyle
                    see the Howto body doc
                    page for details
    sphere arg = 0/1 (optional) for static/dynamic particle radii
    bpm/sphere arg = 0/1 (optional) for static/dynamic particle radii
    tdpd arg = Nspecies
      Nspecies = # of chemical species
    template arg = template-ID
      template-ID = ID of molecule template specified in a separate molecule command
    hybrid args = list of one or more sub-styles, each with their args
    ellipsoid arg = superellipsoid (optional) for superellipsoids instead of ellipsoids
  ```

- accelerated styles (with same args) = *angle/kk* or *atomic/kk* or *bond/kk* or *charge/kk* or *full/kk* or *molecular/kk* or *spin/kk*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    atom_style atomic
    atom_style bond
    atom_style full
    atom_style body nparticle 2 10
    atom_style hybrid charge bond
    atom_style hybrid charge body nparticle 2 5
    atom_style spin
    atom_style template myMols
    atom_style hybrid template twomols charge
    atom_style tdpd 2
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *atom_style* command selects which per-atom attributes are associated with atoms in a LAMMPS simulation and thus stored and communicated with those atoms as well as read from and stored in data and restart files. Different models (e.g. [[pair styles]{.doc}]pair_style.md){.reference .internal}) require access to specific per-atom attributes and thus require a specific atom style. For example, to compute Coulomb interactions, the atom must have a "charge" (aka "q") attribute.

A number of distinct atom styles exist that combine attributes. Some atom styles are a superset of other atom styles. Further attributes may be added to atoms either via using a hybrid style which provides a union of the attributes of the sub-styles, or via the [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal} command. The *atom_style* command must be used before a simulation is setup via a [[read_data]{.doc}]read_data.md){.reference .internal}, [[read_restart]{.doc}]read_restart.md){.reference .internal}, or [[create_box]{.doc}]create_box.md){.reference .internal} command.

::: {.admonition .note}
Note

Many of the atom styles discussed here are only enabled if LAMMPS was built with a specific package, as listed below in the Restrictions section.
:::

Once a style is selected and the simulation box defined, it cannot be changed but only augmented with the [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal} command. So one should select an atom style general enough to encompass all attributes required. E.g. with atom style *bond*, it is not possible to define angles and use angle styles.

It is OK to use a style more general than needed, though it may be slightly inefficient because it will allocate and communicate additional unused data.
::::

:::: {#atom-style-attributes .section}
## Atom style attributes[](#atom-style-attributes "Link to this heading"){.headerlink}

The atom style *atomic* has the minimum subset of per-atom attributes and is also the default setting. It encompasses the following per-atom attributes (name of the vector or array in the [[Atom class]{.doc}]Classes_atom.md){.reference .internal} is given in parenthesis): atom-ID (tag), type (type), position (x), velocities (v), forces (f), image flags (image), group membership (mask). Since all atom styles are a superset of atom style *atomic*, they all include these attributes.

This table lists all the available atom styles, which attributes they provide, which [[package]{.doc}]Packages.md){.reference .internal} is required to use them, and what the typical applications are that use them. See the [[read_data]{.doc}]read_data.md){.reference .internal}, [[create_atoms]{.doc}]create_atoms.md){.reference .internal}, and [[set]{.doc}]set.md){.reference .internal} commands for details on how to set these various quantities. More information about many of the styles is provided in the Additional Information section below.

+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Atom style          | Attributes                                                                                                                                                                    | Required package                                                                          | Applications                                                                                                                                                                                               |
+=====================+===============================================================================================================================================================================+===========================================================================================+============================================================================================================================================================================================================+
| *amoeba*            | *full* + "1-5 special neighbor data"                                                                                                                                          | [[AMOEBA]{.std .std-ref}]Packages_details.md#pkg-amoeba){.reference .internal}         | AMOEBA/HIPPO force fields                                                                                                                                                                                  |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *angle*             | *bond* + "angle data"                                                                                                                                                         | [[MOLECULE]{.std .std-ref}]Packages_details.md#pkg-molecule){.reference .internal}     | bead-spring polymers with stiffness                                                                                                                                                                        |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *apip thermostat*   | *atomic* + apip_lambda, apip_lambda_required, apip_lambda_input, apip_lambda_const, apip_lambda_input_ta, apip_e_fast, apip_e_precise, apip_f_const_lambda, apip_f_dyn_lambda | [[APIP]{.std .std-ref}]Packages_details.md#pkg-apip){.reference .internal}             | adaptive-precision interatomic potentials(APIP) with a [[lambda thermostat]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal}, see [[APIP howto]{.doc}]Howto_apip.md){.reference .internal} |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *apip conservative* | *atomic* + apip_lambda, apip_lambda_required, apip_e_fast, apip_e_precise                                                                                                     | [[APIP]{.std .std-ref}]Packages_details.md#pkg-apip){.reference .internal}             | conservative adaptive-precision interatomic potentials(APIP), see [[APIP howto]{.doc}]Howto_apip.md){.reference .internal}                                                                              |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *atomic*            | tag, type, x, v, f, image, mask                                                                                                                                               |                                                                                           | atomic liquids, solids, metals                                                                                                                                                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *body*              | *atomic* + radius, rmass, angmom, torque, body                                                                                                                                | [[BODY]{.std .std-ref}]Packages_details.md#pkg-body){.reference .internal}             | arbitrary bodies, see [[body howto]{.doc}]Howto_body.md){.reference .internal}                                                                                                                          |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *bond*              | *atomic* + molecule, nspecial, special + "bond data"                                                                                                                          | [[MOLECULE]{.std .std-ref}]Packages_details.md#pkg-molecule){.reference .internal}     | bead-spring polymers                                                                                                                                                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *bpm/sphere*        | *bond* + radius, rmass, omega, torque, quat                                                                                                                                   | [[BPM]{.std .std-ref}]Packages_details.md#pkg-bpm){.reference .internal}               | granular bonded particle models, see [[BPM howto]{.doc}]Howto_bpm.md){.reference .internal}                                                                                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *charge*            | *atomic* + q                                                                                                                                                                  |                                                                                           | atomic systems with charges                                                                                                                                                                                |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *dielectric*        | *full* + mu, area, ed, em, epsilon, curvature, q_scaled                                                                                                                       | [[DIELECTRIC]{.std .std-ref}]Packages_details.md#pkg-dielectric){.reference .internal} | systems with surface polarization                                                                                                                                                                          |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *dipole*            | *charge* + mu                                                                                                                                                                 | [[DIPOLE]{.std .std-ref}]Packages_details.md#pkg-dipole){.reference .internal}         | atomic systems with charges and point dipoles                                                                                                                                                              |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *dpd*               | *atomic* + rho + "reactive DPD data"                                                                                                                                          | [[DPD-REACT]{.std .std-ref}]Packages_details.md#pkg-dpd-react){.reference .internal}   | reactive DPD                                                                                                                                                                                               |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *edpd*              | *atomic* + "eDPD data"                                                                                                                                                        | [[DPD-MESO]{.std .std-ref}]Packages_details.md#pkg-dpd-meso){.reference .internal}     | Energy conservative DPD (eDPD)                                                                                                                                                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *electron*          | *charge* + espin, eradius, ervel, erforce                                                                                                                                     | [[EFF]{.std .std-ref}]Packages_details.md#pkg-eff){.reference .internal}               | Electron force field systems                                                                                                                                                                               |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *ellipsoid*         | *atomic* + rmass, angmom, torque, ellipsoid                                                                                                                                   |                                                                                           | aspherical particles                                                                                                                                                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *full*              | *molecular* + q                                                                                                                                                               | [[MOLECULE]{.std .std-ref}]Packages_details.md#pkg-molecule){.reference .internal}     | molecular force fields                                                                                                                                                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *line*              | *atomic* + molecule, radius, rmass, omega, torque, line                                                                                                                       |                                                                                           | 2-d rigid body particles                                                                                                                                                                                   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *mdpd*              | *atomic* + rho, drho, vest                                                                                                                                                    | [[DPD-MESO]{.std .std-ref}]Packages_details.md#pkg-dpd-meso){.reference .internal}     | Many-body DPD (mDPD)                                                                                                                                                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *molecular*         | *angle* + "dihedral and improper data"                                                                                                                                        | [[MOLECULE]{.std .std-ref}]Packages_details.md#pkg-molecule){.reference .internal}     | apolar and uncharged molecules                                                                                                                                                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *oxdna*             | *atomic* + id5p                                                                                                                                                               | [[CG-DNA]{.std .std-ref}]Packages_details.md#pkg-cg-dna){.reference .internal}         | coarse-grained DNA and RNA models                                                                                                                                                                          |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *peri*              | *atomic* + rmass, vfrac, s0, x0                                                                                                                                               | [[PERI]{.std .std-ref}]Packages_details.md#pkg-peri){.reference .internal}             | mesoscopic Peridynamics models                                                                                                                                                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *smd*               | *atomic* + molecule, radius, rmass + "smd data"                                                                                                                               | [[MACHDYN]{.std .std-ref}]Packages_details.md#pkg-machdyn){.reference .internal}       | Smooth Mach Dynamics models                                                                                                                                                                                |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *rheo*              | *atomic* + rho, status                                                                                                                                                        | [[RHEO]{.std .std-ref}]Packages_details.md#pkg-rheo){.reference .internal}             | solid and fluid RHEO particles                                                                                                                                                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *rheo/thermal*      | *atomic* + rho, status, energy, temperature                                                                                                                                   | [[RHEO]{.std .std-ref}]Packages_details.md#pkg-rheo){.reference .internal}             | RHEO particles with temperature                                                                                                                                                                            |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *sph*               | *atomic* + "sph data"                                                                                                                                                         | [[SPH]{.std .std-ref}]Packages_details.md#pkg-sph){.reference .internal}               | Smoothed particle hydrodynamics models                                                                                                                                                                     |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *sphere*            | *atomic* + radius, rmass, omega, torque                                                                                                                                       |                                                                                           | finite size spherical particles, e.g. granular models                                                                                                                                                      |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *spin*              | *atomic* + "magnetic moment data"                                                                                                                                             | [[SPIN]{.std .std-ref}]Packages_details.md#pkg-spin){.reference .internal}             | magnetic particles                                                                                                                                                                                         |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *tdpd*              | *atomic* + cc, cc_flux, vest                                                                                                                                                  | [[DPD-MESO]{.std .std-ref}]Packages_details.md#pkg-dpd-meso){.reference .internal}     | Transport DPD (tDPD)                                                                                                                                                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *template*          | *atomic* + molecule, molindex, molatom                                                                                                                                        | [[MOLECULE]{.std .std-ref}]Packages_details.md#pkg-molecule){.reference .internal}     | molecular systems where attributes are taken from [[molecule files]{.doc}]molecule.md){.reference .internal}                                                                                            |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *tri*               | *sphere* + molecule, angmom, tri                                                                                                                                              |                                                                                           | 3-d triangulated rigid body LJ particles                                                                                                                                                                   |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

::: {.admonition .note}
Note

It is possible to add some attributes, such as a molecule ID and charge, to atom styles that do not have them built in using the [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal} command. This command also allows new custom-named attributes consisting of extra integer or floating-point values or vectors to be added to atoms. See the [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal} page for examples of cases where this is useful and details on how to initialize, access, and output these custom values.
:::
::::

------------------------------------------------------------------------

::: {#particle-size-and-mass .section}
## Particle size and mass[](#particle-size-and-mass "Link to this heading"){.headerlink}

All of the atom styles define point particles unless they (1) define finite-size spherical particles via the *radius* attribute, or (2) define finite-size aspherical particles (e.g. the *body*, *ellipsoid*, *line*, and *tri* styles). Most of these styles can also be used with mixtures of point and finite-size particles.

Note that the *radius* property may need to be provided as a *diameter* (e.g. in [[molecule files]{.doc}]molecule.md){.reference .internal} or [[data files]{.doc}]read_data.md){.reference .internal}). See the [[Howto spherical]{.doc}]Howto_spherical.md){.reference .internal} page for an overview of using finite-size spherical and aspherical particle models with LAMMPS.

Unless an atom style defines the per-atom *rmass* attribute, particle masses are defined on a per-type basis, using the [[mass]{.doc}]mass.md){.reference .internal} command. This means each particle's mass is indexed by its atom *type*.

A few styles define the per-atom *rmass* attribute which can also be added using the [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal} command. In this case each particle stores its own mass. Atom styles that have a per-atom rmass may define it indirectly through setting particle diameter and density on a per-particle basis. If both per-type mass and per-atom *rmass* are defined (e.g. in a hybrid style), the per-atom mass will take precedence in any operation which which works with both flavors of mass.
:::

------------------------------------------------------------------------

:::::: {#additional-information-about-specific-atom-styles .section}
## Additional information about specific atom styles[](#additional-information-about-specific-atom-styles "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 30Mar2026.]{.versionmodified .changed}
:::

For the *apip* style, one can choose between the style for conservative potentials and the style for the [[lambda thermostat]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal}. The [[Howto apip]{.doc}]Howto_apip.md){.reference .internal} describes the differences between both use cases.

For the *body* style, the particles are arbitrary bodies with internal attributes defined by the "style" of the bodies, which is specified by the *bstyle* argument. Body particles can represent complex entities, such as surface meshes of discrete points, collections of sub-particles, deformable objects, etc.

The [[Howto body]{.doc}]Howto_body.md){.reference .internal} page describes the body styles LAMMPS currently supports, and provides more details as to the kind of body particles they represent. For all styles, each body particle stores moments of inertia and a quaternion 4-vector, so that its orientation and position can be time integrated due to forces and torques.

Note that there may be additional arguments required along with the *bstyle* specification, in the atom_style body command. These arguments are described on the [[Howto body]{.doc}]Howto_body.md){.reference .internal} doc page.

For the *dielectric* style, each particle can be either a physical particle (e.g. an ion), or an interface particle representing a boundary element between two regions of different dielectric constant. For interface particles, in addition to the properties associated with atom_style full, each particle also should be assigned a unit dipole vector (mu) representing the direction of the induced dipole moment at each interface particle, an area (area/patch), the difference and mean of the dielectric constants of two sides of the interface along the direction of the normal vector (ed and em), the local dielectric constant at the boundary element (epsilon), and a mean local curvature (curv). Physical particles must be assigned these values, as well, but only their local dielectric constants will be used; see documentation for associated [[pair styles]{.doc}]pair_dielectric.md){.reference .internal} and [[fixes]{.doc}]fix_polarize.md){.reference .internal}. The distinction between the physical and interface particles is only meaningful when [[fix polarize]{.doc}]fix_polarize.md){.reference .internal} commands are applied to the interface particles. This style is part of the DIELECTRIC package.

For the *dipole* style, a point dipole vector mu is defined for each point particle. Note that if you wish the particles to be finite-size spheres as in a Stockmayer potential for a dipolar fluid, so that the particles can rotate due to dipole-dipole interactions, then you need to use the command atom_style hybrid sphere dipole, which will assign both a diameter and dipole moment to each particle. This also requires using an integrator with a "/sphere" suffix like [[fix nve/sphere]{.doc}]fix_nve_sphere.md){.reference .internal} or [[fix nvt/sphere]{.doc}]fix_nvt_sphere.md){.reference .internal} and the "update dipole" or "update dlm" parameters to the fix commands.

The *dpd* style is for reactive dissipative particle dynamics (DPD) particles. Note that it is part of the DPD-REACT package, and is not required for use with the [[pair_style dpd or dpd/stat]{.doc}]pair_dpd.md){.reference .internal} commands, which only require the attributes from atom_style *atomic*. Atom_style *dpd* extends DPD particle properties with internal temperature (dpdTheta), internal conductive energy (uCond), internal mechanical energy (uMech), and internal chemical energy (uChem).

The *edpd* style is for energy-conserving dissipative particle dynamics (eDPD) particles which store a temperature (edpd_temp), and heat capacity (edpd_cv).

For the *electron* style, the particles representing electrons are 3d Gaussians with a specified position and bandwidth or uncertainty in position, which is represented by the eradius = electron size.

For the *ellipsoid* style, particles can be ellipsoids which each stores a shape vector with the 3 diameters of the ellipsoid and a quaternion 4-vector with its orientation. Each particle stores a flag in the ellipsoid vector which indicates whether it is an ellipsoid (1) or a point particle (0).

::: versionadded
[Added in version 30Mar2026.]{.versionmodified .added}
:::

By adding the flag *superellipsoid* to the *ellipsoid* atom_style command, the particles can be superellipsoids, which are a generalization of ellipsoids with two additional blockiness parameters that control the shape. Superellipsoids also store the principal moments of inertia of the particle.

For the *line* style, particles can be are idealized line segments which store a per-particle mass and length and orientation (i.e. the end points of the line segment). Each particle stores a flag in the line vector which indicates whether it is a line segment (1) or a point particle (0).

The *mdpd* style is for many-body dissipative particle dynamics (mDPD) particles which store a density (rho) for considering density-dependent many-body interactions.

The *oxdna* style is for coarse-grained nucleotides and stores the 3'-to-5' polarity of the nucleotide strand, which is set through the bond topology in the data file. The first (second) atom in a bond definition is understood to point towards the 3'-end (5'-end) of the strand.

For the *peri* style, the particles are spherical and each stores a per-particle mass and volume.

The *smd* style is for Smooth Particle Mach dynamics. Both fluids and solids can be modeled. Particles store the mass and volume of an integration point, a kernel diameter used for calculating the field variables (e.g. stress and deformation) and a contact radius for calculating repulsive forces which prevent individual physical bodies from penetrating each other.

The *sph* style is for smoothed particle hydrodynamics (SPH) particles which store a density (rho), energy (esph), and heat capacity (cv).

For the *spin* style, a magnetic spin is associated with each atom. Those spins have a norm (their magnetic moment) and a direction.

The *tdpd* style is for transport dissipative particle dynamics (tDPD) particles which store a set of chemical concentration. An integer "cc_species" is required to specify the number of chemical species involved in a tDPD system.

The *wavepacket* style is similar to the *electron* style, but the electrons may consist of several Gaussian wave packets, summed up with coefficients cs= (cs_re,cs_im). Each of the wave packets is treated as a separate particle in LAMMPS, wave packets belonging to the same electron must have identical *etag* values.

The *sphere* and *bpm/sphere* styles allow particles to be either point particles or finite-size particles. If the *radius* attribute is \> 0.0, the particle is a finite-size sphere. If the diameter = 0.0, it is a point particle. Note that by using the *disc* keyword with the [[fix nve/sphere]{.doc}]fix_nve_sphere.md){.reference .internal}, [[fix nvt/sphere]{.doc}]fix_nvt_sphere.md){.reference .internal}, [[fix nph/sphere]{.doc}]fix_nph_sphere.md){.reference .internal}, [[fix npt/sphere]{.doc}]fix_npt_sphere.md){.reference .internal} commands for the *sphere* style, spheres can be effectively treated as 2d discs for a 2d simulation if desired. See also the [[set density/disc]{.doc}]set.md){.reference .internal} command. These styles also take an optional 0 or 1 argument. A value of 0 means the radius of each sphere is constant for the duration of the simulation (this is the default). A value of 1 means the radii may vary dynamically during the simulation, e.g. due to use of the [[fix adapt]{.doc}]fix_adapt.md){.reference .internal} command.

The *template* style allows molecular topology (bonds,angles,etc) to be defined via a molecule template using the [[molecule]{.doc}]molecule.md){.reference .internal} command. The template stores one or more molecules with a single copy of the topology info (bonds,angles,etc) of each. Individual atoms only store a template index and template atom to identify which molecule and which atom-within-the-molecule they represent. Using the *template* style instead of the *bond*, *angle*, *molecular* styles can save memory for systems comprised of a large number of small molecules, all of a single type (or small number of types). See the paper by Grime and Voth, in [[(Grime)]{.std .std-ref}](#grime){.reference .internal}, for examples of how this can be advantageous for large-scale coarse-grained systems. The [`examples/template`{.docutils .literal .notranslate}]{.pre} directory has a few demo inputs and examples showing the use of the *template* atom style versus *molecular*.

::: {.admonition .note}
Note

When using the *template* style with a [[molecule template]{.doc}]molecule.md){.reference .internal} that contains multiple molecules, you should ensure the atom types, bond types, angle_types, etc in all the molecules are consistent. E.g. if one molecule represents H2O and another CO2, then you probably do not want each molecule file to define two atom types and a single bond type, because they will conflict with each other when a mixture system of H2O and CO2 molecules is defined, e.g. by the [[read_data]{.doc}]read_data.md){.reference .internal} command. Rather the H2O molecule should define atom types 1 and 2, and bond type 1. And the CO2 molecule should define atom types 3 and 4 (or atom types 3 and 2 if a single oxygen type is desired), and bond type 2.
:::

For the *tri* style, particles can be planar triangles which each stores a per-particle mass and size and orientation (i.e. the corner points of the triangle). Each particle stores a flag in the tri vector which indicates whether it is a triangle (1) or a point particle (0).

------------------------------------------------------------------------

Typically, simulations require only a single (non-hybrid) atom style. If some atoms in the simulation do not have all the properties defined by a particular style, use the simplest style that defines all the needed properties by any atom. For example, if some atoms in a simulation are charged, but others are not, use the *charge* style. If some atoms have bonds, but others do not, use the *bond* style.

The only scenario where the *hybrid* style is needed is if there is no single style which defines all needed properties of all atoms. For example, as mentioned above, if you want dipolar particles which will rotate due to torque, you need to use "atom_style hybrid sphere dipole". When a hybrid style is used, atoms store and communicate the union of all quantities implied by the individual styles.

When using the *hybrid* style, you cannot combine the *template* style with another molecular style that stores bond, angle, etc info on a per-atom basis.

LAMMPS can be extended with new atom styles as well as new body styles; see the corresponding manual page on [[modifying & extending LAMMPS]{.doc}]Modify_atom.md){.reference .internal}.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command cannot be used after the simulation box is defined by a [[read_data]{.doc}]read_data.md){.reference .internal} or [[create_box]{.doc}]create_box.md){.reference .internal} command.

Many of the styles listed above are only enabled if LAMMPS was built with a specific package, as listed below. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. The table above lists which package is required for individual atom styles.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[read_data]{.doc}]read_data.md){.reference .internal}, [[pair_style]{.doc}]pair_style.md){.reference .internal}, [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal}, [[set]{.doc}]set.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default atom style is *atomic*. If atom_style *sphere* or *bpm/sphere* is used, its default argument is 0. If atom_style *apip* is used, its default argument is 'thermostat'.

------------------------------------------------------------------------

**(Grime)** Grime and Voth, to appear in J Chem Theory & Computation (2014).
:::
:::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

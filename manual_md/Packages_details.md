:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#package-details .section}
# [8.1. ]{.section-number}Package details[](#package-details "Link to this heading"){.headerlink}

Here is a brief description of all packages in LAMMPS. It lists authors (if applicable) and summarizes the package contents. It has specific instructions on how to install the package, including, if necessary, info on how to download or build any extra library it requires. It also gives links to documentation, example scripts, and pictures/movies (if available) that illustrate use of the package.

The majority of packages can be included in a LAMMPS build with a single setting ([`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`PKG_<NAME>=on`{.docutils .literal .notranslate}]{.pre} for CMake) or command ([`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`yes-<name>`{.docutils .literal .notranslate}]{.pre} for make). See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. A few packages may require additional steps; this is indicated in the descriptions below. The [[Build extras]{.doc}]Build_extras.md){.reference .internal} page gives those details.

::: {.admonition .note}
Note

To see the complete list of commands a package adds to LAMMPS, you can examine the files in its src directory, e.g. [`ls`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`src/GRANULAR`{.docutils .literal .notranslate}]{.pre}. Files with names that start with fix, compute, atom, pair, bond, angle, etc correspond to commands with the same style name as contained in the file name.
:::

  ---------------------------------------------------------------------- ---------------------------------------------------------------------------- ---------------------------------------------------------------------------- ---------------------------------------------------------------------- ------------------------------------------------------------------------ ------------------------------------------------------------------------------
  [[ADIOS]{.std .std-ref}](#pkg-adios){.reference .internal}             [[AMOEBA]{.std .std-ref}](#pkg-amoeba){.reference .internal}                 [[APIP]{.std .std-ref}](#pkg-apip){.reference .internal}                     [[ASPHERE]{.std .std-ref}](#pkg-asphere){.reference .internal}         [[BOCS]{.std .std-ref}](#pkg-bocs){.reference .internal}                 [[BODY]{.std .std-ref}](#pkg-body){.reference .internal}
  [[BPM]{.std .std-ref}](#pkg-bpm){.reference .internal}                 [[BROWNIAN]{.std .std-ref}](#pkg-brownian){.reference .internal}             [[CG-DNA]{.std .std-ref}](#pkg-cg-dna){.reference .internal}                 [[CG-SPICA]{.std .std-ref}](#pkg-cg-spica){.reference .internal}       [[CLASS2]{.std .std-ref}](#pkg-class2){.reference .internal}             [[COLLOID]{.std .std-ref}](#pkg-colloid){.reference .internal}
  [[COLVARS]{.std .std-ref}](#pkg-colvars){.reference .internal}         [[COMPRESS]{.std .std-ref}](#pkg-compress){.reference .internal}             [[CORESHELL]{.std .std-ref}](#pkg-coreshell){.reference .internal}           [[DIELECTRIC]{.std .std-ref}](#pkg-dielectric){.reference .internal}   [[DIFFRACTION]{.std .std-ref}](#pkg-diffraction){.reference .internal}   [[DIPOLE]{.std .std-ref}](#pkg-dipole){.reference .internal}
  [[DPD-BASIC]{.std .std-ref}](#pkg-dpd-basic){.reference .internal}     [[DPD-MESO]{.std .std-ref}](#pkg-dpd-meso){.reference .internal}             [[DPD-REACT]{.std .std-ref}](#pkg-dpd-react){.reference .internal}           [[DPD-SMOOTH]{.std .std-ref}](#pkg-dpd-smooth){.reference .internal}   [[DRUDE]{.std .std-ref}](#pkg-drude){.reference .internal}               [[EFF]{.std .std-ref}](#pkg-eff){.reference .internal}
  [[ELECTRODE]{.std .std-ref}](#pkg-electrode){.reference .internal}     [[EXTRA-COMMAND]{.std .std-ref}](#pkg-extra-command){.reference .internal}   [[EXTRA-COMPUTE]{.std .std-ref}](#pkg-extra-compute){.reference .internal}   [[EXTRA-DUMP]{.std .std-ref}](#pkg-extra-dump){.reference .internal}   [[EXTRA-FIX]{.std .std-ref}](#pkg-extra-fix){.reference .internal}       [[EXTRA-MOLECULE]{.std .std-ref}](#pkg-extra-molecule){.reference .internal}
  [[EXTRA-PAIR]{.std .std-ref}](#pkg-extra-pair){.reference .internal}   [[FEP]{.std .std-ref}](#pkg-fep){.reference .internal}                       [[GPU]{.std .std-ref}](#pkg-gpu){.reference .internal}                       [[GRAPHICS]{.std .std-ref}](#pkg-graphics){.reference .internal}       [[GRANULAR]{.std .std-ref}](#pkg-granular){.reference .internal}         [[H5MD]{.std .std-ref}](#pkg-h5md){.reference .internal}
  [[INTEL]{.std .std-ref}](#pkg-intel){.reference .internal}             [[INTERLAYER]{.std .std-ref}](#pkg-interlayer){.reference .internal}         [[KIM]{.std .std-ref}](#pkg-kim){.reference .internal}                       [[KOKKOS]{.std .std-ref}](#pkg-kokkos){.reference .internal}           [[KSPACE]{.std .std-ref}](#pkg-kspace){.reference .internal}             [[LATBOLTZ]{.std .std-ref}](#pkg-latboltz){.reference .internal}
  [[LEPTON]{.std .std-ref}](#pkg-lepton){.reference .internal}           [[MACHDYN]{.std .std-ref}](#pkg-machdyn){.reference .internal}               [[MANIFOLD]{.std .std-ref}](#pkg-manifold){.reference .internal}             [[MANYBODY]{.std .std-ref}](#pkg-manybody){.reference .internal}       [[MBX]{.std .std-ref}](#pkg-mbx){.reference .internal}                   [[MC]{.std .std-ref}](#pkg-mc){.reference .internal}
  [[MDI]{.std .std-ref}](#pkg-mdi){.reference .internal}                 [[MEAM]{.std .std-ref}](#pkg-meam){.reference .internal}                     [[MESONT]{.std .std-ref}](#pkg-mesont){.reference .internal}                 [[MGPT]{.std .std-ref}](#pkg-mgpt){.reference .internal}               [[MISC]{.std .std-ref}](#pkg-misc){.reference .internal}                 [[ML-HDNNP]{.std .std-ref}](#pkg-ml-hdnnp){.reference .internal}
  [[ML-IAP]{.std .std-ref}](#pkg-ml-iap){.reference .internal}           [[ML-PACE]{.std .std-ref}](#pkg-ml-pace){.reference .internal}               [[ML-POD]{.std .std-ref}](#pkg-ml-pod){.reference .internal}                 [[ML-QUIP]{.std .std-ref}](#pkg-ml-quip){.reference .internal}         [[ML-RANN]{.std .std-ref}](#pkg-ml-rann){.reference .internal}           [[ML-SNAP]{.std .std-ref}](#pkg-ml-snap){.reference .internal}
  [[ML-UF3]{.std .std-ref}](#pkg-ml-uf3){.reference .internal}           [[MOFFF]{.std .std-ref}](#pkg-mofff){.reference .internal}                   [[MOLECULE]{.std .std-ref}](#pkg-molecule){.reference .internal}             [[MOLFILE]{.std .std-ref}](#pkg-molfile){.reference .internal}         [[NETCDF]{.std .std-ref}](#pkg-netcdf){.reference .internal}             [[OPENMP]{.std .std-ref}](#pkg-openmp){.reference .internal}
  [[OPT]{.std .std-ref}](#pkg-opt){.reference .internal}                 [[ORIENT]{.std .std-ref}](#pkg-orient){.reference .internal}                 [[PERI]{.std .std-ref}](#pkg-peri){.reference .internal}                     [[PHONON]{.std .std-ref}](#pkg-phonon){.reference .internal}           [[PLUGIN]{.std .std-ref}](#pkg-plugin){.reference .internal}             [[PLUMED]{.std .std-ref}](#pkg-plumed){.reference .internal}
  [[PTM]{.std .std-ref}](#pkg-ptm){.reference .internal}                 [[PYTHON]{.std .std-ref}](#pkg-python){.reference .internal}                 [[QEQ]{.std .std-ref}](#pkg-qeq){.reference .internal}                       [[QMMM]{.std .std-ref}](#pkg-qmmm){.reference .internal}               [[QTB]{.std .std-ref}](#pkg-qtb){.reference .internal}                   [[RHEO]{.std .std-ref}](#pkg-rheo){.reference .internal}
  [[REACTION]{.std .std-ref}](#pkg-reaction){.reference .internal}       [[REAXFF]{.std .std-ref}](#pkg-reaxff){.reference .internal}                 [[REPLICA]{.std .std-ref}](#pkg-replica){.reference .internal}               [[RIGID]{.std .std-ref}](#pkg-rigid){.reference .internal}             [[SCAFACOS]{.std .std-ref}](#pkg-scafacos){.reference .internal}         [[SHOCK]{.std .std-ref}](#pkg-shock){.reference .internal}
  [[SMTBQ]{.std .std-ref}](#pkg-smtbq){.reference .internal}             [[SPH]{.std .std-ref}](#pkg-sph){.reference .internal}                       [[SPIN]{.std .std-ref}](#pkg-spin){.reference .internal}                     [[SRD]{.std .std-ref}](#pkg-srd){.reference .internal}                 [[TALLY]{.std .std-ref}](#pkg-tally){.reference .internal}               [[UEF]{.std .std-ref}](#pkg-uef){.reference .internal}
  [[VORONOI]{.std .std-ref}](#pkg-voronoi){.reference .internal}         [[VTK]{.std .std-ref}](#pkg-vtk){.reference .internal}                       [[YAFF]{.std .std-ref}](#pkg-yaff){.reference .internal}                                                                                                                                                                     
  ---------------------------------------------------------------------- ---------------------------------------------------------------------------- ---------------------------------------------------------------------------- ---------------------------------------------------------------------- ------------------------------------------------------------------------ ------------------------------------------------------------------------------

------------------------------------------------------------------------

:::: {#adios-package .section}
[]{#pkg-adios}

## [8.1.1. ]{.section-number}ADIOS package[](#adios-package "Link to this heading"){.headerlink}

**Contents:**

ADIOS is a high-performance I/O library. This package implements the [[dump atom/adios]{.doc}]dump_adios.md){.reference .internal}, [[dump custom/adios]{.doc}]dump_adios.md){.reference .internal} and [[read_dump ... format adios]{.doc}]read_dump.md){.reference .internal} commands to write and read data using the ADIOS library.

**Authors:** Norbert Podhorszki (ORNL) from the ADIOS developer team.

::: versionadded
[Added in version 28Feb2019.]{.versionmodified .added}
:::

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#adios){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/ADIOS`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/ADIOS/README`{.docutils .literal .notranslate}]{.pre}

- [`examples/PACKAGES/adios`{.docutils .literal .notranslate}]{.pre}

- [https://github.com/ornladios/ADIOS2](https://github.com/ornladios/ADIOS2){.reference .external}

- [[dump atom/adios]{.doc}]dump_adios.md){.reference .internal}

- [[dump custom/adios]{.doc}]dump_adios.md){.reference .internal}

- [[read_dump]{.doc}]read_dump.md){.reference .internal}

------------------------------------------------------------------------
::::

::: {#amoeba-package .section}
[]{#pkg-amoeba}

## [8.1.2. ]{.section-number}AMOEBA package[](#amoeba-package "Link to this heading"){.headerlink}

**Contents:**

Implementation of the AMOEBA and HIPPO polarized force fields originally developed by Jay Ponder's group at the U Washington at St Louis. The LAMMPS implementation is based on Fortran 90 code provided by the Ponder group in their [Tinker MD software](https://dasher.wustl.edu/tinker/){.reference .external}.

**Authors:** Josh Rackers and Steve Plimpton (Sandia), Trung Nguyen (U

:   Chicago)

**Supporting info:**

- [`src/AMOEBA`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[AMOEBA and HIPPO howto]{.doc}]Howto_amoeba.md){.reference .internal}

- [[pair_style amoeba]{.doc}]pair_amoeba.md){.reference .internal}

- [[pair_style hippo]{.doc}]pair_amoeba.md){.reference .internal}

- [[atom_style amoeba]{.doc}]atom_style.md){.reference .internal}

- [[angle_style amoeba]{.doc}]angle_amoeba.md){.reference .internal}

- [[improper_style amoeba]{.doc}]improper_amoeba.md){.reference .internal}

- [[fix amoeba/bitorsion]{.doc}]fix_amoeba_bitorsion.md){.reference .internal}

- [[fix amoeba/pitorsion]{.doc}]fix_amoeba_pitorsion.md){.reference .internal}

- tools/tinker/tinker2lmp.py

- [`examples/amoeba`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#apip-package .section}
[]{#pkg-apip}

## [8.1.3. ]{.section-number}APIP package[](#apip-package "Link to this heading"){.headerlink}

**Contents:**

This package provides adaptive-precision interatomic potentials (APIP) as described in:

D. Immel, R. Drautz and G. Sutmann, "Adaptive-precision potentials for large-scale atomistic simulations", J. Chem. Phys. 162, 114119 (2025) [link](https://doi.org/10.1063/5.0245877){.reference .external}

D. Immel, R. Drautz and G. Sutmann, "Conservative adaptive-precision interatomic potentials", arXiv:2512.07693 [link](https://doi.org/10.48550/arXiv.2512.07693){.reference .external}

Adaptive-precision means, that a fast interatomic potential, such as EAM, is coupled to a precise interatomic potential, such as ACE. This package provides the required pair_styles and fixes to run an efficient, energy-conserving adaptive-precision simulation.

In the context of this package, precision refers to the accuracy of an interatomic potential.

**Authors:**

This package was written by David Immel\^1, Ralf Drautz\^2 and Godehard Sutmann\^1\^2.

> ::: {}
> \^1: Forschungszentrum Juelich, Juelich, Germany
>
> \^2: Ruhr-University Bochum, Bochum, Germany
> :::

**Install:**

The APIP package requires also the installation of ML-PACE, which has [[specific installation instructions]{.std .std-ref}]Build_extras.md#ml-pace){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/APIP`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Howto APIP]{.doc}]Howto_apip.md){.reference .internal}

- [`examples/PACKAGES/apip`{.docutils .literal .notranslate}]{.pre}

- [[fix atom_weight/apip]{.doc}]fix_atom_weight_apip.md){.reference .internal}

- [[fix lambda/apip]{.doc}]fix_lambda_apip.md){.reference .internal}

- [[fix lambda/la/csp/apip]{.doc}]fix_lambda_la_csp_apip.md){.reference .internal}

- [[fix lambda_thermostat/apip]{.doc}]fix_lambda_thermostat_apip.md){.reference .internal}

- [[pair_style eam/apip]{.doc}]pair_eam_apip.md){.reference .internal}

- [[pair_style lambda/zone/apip]{.doc}]pair_lambda_zone_apip.md){.reference .internal}

- [[pair_style lambda/input/apip]{.doc}]pair_lambda_input_apip.md){.reference .internal}

- [[pair_style pace/apip]{.doc}]pair_pace_apip.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#asphere-package .section}
[]{#pkg-asphere}

## [8.1.4. ]{.section-number}ASPHERE package[](#asphere-package "Link to this heading"){.headerlink}

**Contents:**

Computes, time-integration fixes, and pair styles for aspherical particle models including ellipsoids, granular superellipsoids, 2d lines, and 3d triangles.

**Supporting info:**

- [`src/ASPHERE`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Howto spherical]{.doc}]Howto_spherical.md){.reference .internal}

- [[pair_style gayberne]{.doc}]pair_gayberne.md){.reference .internal}

- [[pair_style resquared]{.doc}]pair_resquared.md){.reference .internal}

- [[pair_style ylz]{.doc}]pair_ylz.md){.reference .internal}

- [[pair_style line/lj]{.doc}]pair_line_lj.md){.reference .internal}

- [[pair_style tri/lj]{.doc}]pair_tri_lj.md){.reference .internal}

- [[pair_style granular/superellipsoid]{.doc}]pair_granular_superellipsoid.md){.reference .internal}

- [doc/PDF/pair_gayberne_extra.pdf](PDF/pair_gayberne_extra.pdf){.reference .external}

- [doc/PDF/pair_resquared_extra.pdf](PDF/pair_resquared_extra.pdf){.reference .external}

- [`examples/ASPHERE`{.docutils .literal .notranslate}]{.pre}

- [`examples/ellipse`{.docutils .literal .notranslate}]{.pre}

- [https://www.lammps.org/movies.html#line](https://www.lammps.org/movies.html#line){.reference .external}

- [https://www.lammps.org/movies.html#tri](https://www.lammps.org/movies.html#tri){.reference .external}

------------------------------------------------------------------------
:::

::: {#bocs-package .section}
[]{#pkg-bocs}

## [8.1.5. ]{.section-number}BOCS package[](#bocs-package "Link to this heading"){.headerlink}

**Contents:**

This package provides [[fix bocs]{.doc}]fix_bocs.md){.reference .internal}, a modified version of [[fix npt]{.doc}]fix_nh.md){.reference .internal} which includes the pressure correction to the barostat as outlined in:

N. J. H. Dunn and W. G. Noid, "Bottom-up coarse-grained models that accurately describe the structure, pressure, and compressibility of molecular liquids", J. Chem. Phys. 143, 243148 (2015).

**Authors:** Nicholas J. H. Dunn and Michael R. DeLyser (The Pennsylvania State University)

**Supporting info:**

The BOCS package for LAMMPS is part of the BOCS software package: [https://github.com/noid-group/BOCS](https://github.com/noid-group/BOCS){.reference .external}

See the following reference for information about the entire package:

Dunn, NJH; Lebold, KM; DeLyser, MR; Rudzinski, JF; Noid, WG. "BOCS: Bottom-Up Open-Source Coarse-Graining Software." J. Phys. Chem. B. 122, 13, 3363-3377 (2018).

Example inputs are in the [`examples/PACKAGES/bocs`{.docutils .literal .notranslate}]{.pre} folder.

------------------------------------------------------------------------
:::

::: {#body-package .section}
[]{#pkg-body}

## [8.1.6. ]{.section-number}BODY package[](#body-package "Link to this heading"){.headerlink}

**Contents:**

Body-style particles with internal structure. Computes, time-integration fixes, pair styles, as well as the body styles themselves. See the [[Howto body]{.doc}]Howto_body.md){.reference .internal} page for an overview.

**Supporting info:**

- [`src/BODY`{.docutils .literal .notranslate}]{.pre} filenames -\> commands

- [[Howto_body]{.doc}]Howto_body.md){.reference .internal}

- [[atom_style body]{.doc}]atom_style.md){.reference .internal}

- [[fix nve/body]{.doc}]fix_nve_body.md){.reference .internal}

- [[pair_style body/nparticle]{.doc}]pair_body_nparticle.md){.reference .internal}

- [`examples/body`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

:::: {#bpm-package .section}
[]{#pkg-bpm}

## [8.1.7. ]{.section-number}BPM package[](#bpm-package "Link to this heading"){.headerlink}

**Contents:**

Pair styles, bond styles, fixes, and computes for bonded particle models for mesoscale simulations of solids and fracture. See the [[Howto bpm]{.doc}]Howto_bpm.md){.reference .internal} page for an overview.

**Authors:** Joel T. Clemmer (Sandia National Labs)

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

**Supporting info:**

- [`src/BPM`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Howto_bpm]{.doc}]Howto_bpm.md){.reference .internal}

- [[atom_style bpm/sphere]{.doc}]atom_style.md){.reference .internal}

- [[bond_style bpm/rotational]{.doc}]bond_bpm_rotational.md){.reference .internal}

- [[bond_style bpm/spring]{.doc}]bond_bpm_spring.md){.reference .internal}

- [[compute nbond/atom]{.doc}]compute_nbond_atom.md){.reference .internal}

- [[fix nve/bpm/sphere]{.doc}]fix_nve_bpm_sphere.md){.reference .internal}

- [[pair_style bpm/spring]{.doc}]pair_bpm_spring.md){.reference .internal}

- [https://www.lammps.org/movies.html#bpmpackage](https://www.lammps.org/movies.html#bpmpackage){.reference .external}

- [`examples/bpm`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

:::: {#brownian-package .section}
[]{#pkg-brownian}

## [8.1.8. ]{.section-number}BROWNIAN package[](#brownian-package "Link to this heading"){.headerlink}

**Contents:**

This package provides [[fix brownian, fix brownian/sphere, and fix brownian/asphere]{.doc}]fix_brownian.md){.reference .internal} as well as [[fix propel/self]{.doc}]fix_propel_self.md){.reference .internal} which allow performing Brownian Dynamics time integration of point, spherical and aspherical particles and also support self-propelled particles.

**Authors:** Sam Cameron (University of Bristol), Arthur Straube (Zuse Institute Berlin), Stefan Paquay (while at Brandeis University) (initial version of fix propel/self)

::: versionadded
[Added in version 14May2021.]{.versionmodified .added}
:::

Example inputs are in the [`examples/PACKAGES/brownian`{.docutils .literal .notranslate}]{.pre} folder.

------------------------------------------------------------------------
::::

::: {#cg-dna-package .section}
[]{#pkg-cg-dna}

## [8.1.9. ]{.section-number}CG-DNA package[](#cg-dna-package "Link to this heading"){.headerlink}

**Contents:**

Several pair styles, bond styles, and integration fixes for coarse-grained modelling of single- and double-stranded DNA and RNA based on the oxDNA and oxRNA model of Doye, Louis and Ouldridge. The package includes Langevin-type rigid-body integrators with improved stability.

**Author:** Oliver Henrich (University of Strathclyde, Glasgow).

**Install:**

The CG-DNA package requires that also the [[MOLECULE]{.std .std-ref}](#pkg-molecule){.reference .internal} and [[ASPHERE]{.std .std-ref}](#pkg-asphere){.reference .internal} packages are installed.

**Supporting info:**

- [`src/CG-DNA`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/CG-DNA/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style oxdna/\*]{.doc}]pair_oxdna.md){.reference .internal}

- [[pair_style oxdna2/\*]{.doc}]pair_oxdna2.md){.reference .internal}

- [[pair_style oxrna2/\*]{.doc}]pair_oxrna2.md){.reference .internal}

- [[bond_style oxdna/\*]{.doc}]bond_oxdna.md){.reference .internal}

- [[bond_style oxdna2/\*]{.doc}]bond_oxdna.md){.reference .internal}

- [[bond_style oxrna2/\*]{.doc}]bond_oxdna.md){.reference .internal}

- [[fix nve/dotc/langevin]{.doc}]fix_nve_dotc_langevin.md){.reference .internal}

- [`examples/PACKAGES/cgdna`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#cg-spica-package .section}
[]{#pkg-cg-spica}

## [8.1.10. ]{.section-number}CG-SPICA package[](#cg-spica-package "Link to this heading"){.headerlink}

**Contents:**

Several pair styles and an angle style which implement the coarse-grained SPICA (formerly called SDK) model which enables simulation of biological or soft material systems.

**Original Author:** Axel Kohlmeyer (Temple U).

**Maintainers:** Yusuke Miyazaki and Wataru Shinoda (Okayama U).

**Supporting info:**

- [`src/CG-SPICA`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/CG-SPICA/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style lj/spica/\*]{.doc}]pair_spica.md){.reference .internal}

- [[angle_style spica]{.doc}]angle_spica.md){.reference .internal}

- [`examples/PACKAGES/cgspica`{.docutils .literal .notranslate}]{.pre}

- [https://www.lammps.org/pictures.html#cg](https://www.lammps.org/pictures.html#cg){.reference .external}

- [https://www.spica-ff.org/](https://www.spica-ff.org/){.reference .external}

------------------------------------------------------------------------
:::

::: {#class2-package .section}
[]{#pkg-class2}

## [8.1.11. ]{.section-number}CLASS2 package[](#class2-package "Link to this heading"){.headerlink}

**Contents:**

Bond, angle, dihedral, improper, and pair styles for the COMPASS CLASS2 molecular force field.

**Supporting info:**

- [`src/CLASS2`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[bond_style class2]{.doc}]bond_class2.md){.reference .internal}

- [[angle_style class2]{.doc}]angle_class2.md){.reference .internal}

- [[dihedral_style class2]{.doc}]dihedral_class2.md){.reference .internal}

- [[improper_style class2]{.doc}]improper_class2.md){.reference .internal}

- [[pair_style lj/class2]{.doc}]pair_class2.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#colloid-package .section}
[]{#pkg-colloid}

## [8.1.12. ]{.section-number}COLLOID package[](#colloid-package "Link to this heading"){.headerlink}

**Contents:**

Coarse-grained finite-size colloidal particles. Pair styles and fix wall styles for colloidal interactions. Includes the Fast Lubrication Dynamics (FLD) method for hydrodynamic interactions, which is a simplified approximation to Stokesian dynamics.

**Authors:** This package includes Fast Lubrication Dynamics pair styles which were created by Amit Kumar and Michael Bybee from Jonathan Higdon's group at UIUC.

**Supporting info:**

- [`src/COLLOID`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[fix wall/colloid]{.doc}]fix_wall.md){.reference .internal}

- [[pair_style colloid]{.doc}]pair_colloid.md){.reference .internal}

- [[pair_style yukawa/colloid]{.doc}]pair_yukawa_colloid.md){.reference .internal}

- [[pair_style brownian]{.doc}]pair_brownian.md){.reference .internal}

- [[pair_style lubricate]{.doc}]pair_lubricate.md){.reference .internal}

- [[pair_style lubricateU]{.doc}]pair_lubricateU.md){.reference .internal}

- [`examples/colloid`{.docutils .literal .notranslate}]{.pre}

- [`examples/srd`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#colvars-package .section}
[]{#pkg-colvars}

## [8.1.13. ]{.section-number}COLVARS package[](#colvars-package "Link to this heading"){.headerlink}

**Contents:**

Colvars stands for collective variables, which can be used to implement various enhanced sampling methods, including Adaptive Biasing Force, Metadynamics, Steered MD, Umbrella Sampling and Restraints. A [[fix colvars]{.doc}]fix_colvars.md){.reference .internal} command is implemented which wraps a COLVARS library, which implements these methods. simulations.

**Authors:** The COLVARS library is written and maintained by Giacomo Fiorin (NIH, Bethesda, MD, USA) and Jerome Henin (CNRS, Paris, France), originally for the NAMD MD code, but with portability in mind. Axel Kohlmeyer (Temple U) provided the interface to LAMMPS.

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#colvar){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/COLVARS`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [https://colvars.github.io/master/colvars-refman-lammps.html](https://colvars.github.io/master/colvars-refman-lammps.html){.reference .external}

- [doc/PDF/colvars-refman-lammps.pdf](PDF/colvars-refman-lammps.pdf){.reference .external}

- [`src/COLVARS/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/colvars/README`{.docutils .literal .notranslate}]{.pre}

- [[fix colvars]{.doc}]fix_colvars.md){.reference .internal}

- [[group2ndx]{.doc}]group2ndx.md){.reference .internal}

- [[ndx2group]{.doc}]group2ndx.md){.reference .internal}

- [`examples/PACKAGES/colvars`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#compress-package .section}
[]{#pkg-compress}

## [8.1.14. ]{.section-number}COMPRESS package[](#compress-package "Link to this heading"){.headerlink}

**Contents:**

Compressed output of dump files via the zlib compression library, using dump styles with a "gz" in their style name.

To use this package you must have the zlib compression library available on your system.

**Author:** Axel Kohlmeyer (Temple U).

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#compress){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/COMPRESS`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/COMPRESS/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/compress/README`{.docutils .literal .notranslate}]{.pre}

- [[dump atom/gz]{.doc}]dump.md){.reference .internal}

- [[dump cfg/gz]{.doc}]dump.md){.reference .internal}

- [[dump custom/gz]{.doc}]dump.md){.reference .internal}

- [[dump xyz/gz]{.doc}]dump.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#coreshell-package .section}
[]{#pkg-coreshell}

## [8.1.15. ]{.section-number}CORESHELL package[](#coreshell-package "Link to this heading"){.headerlink}

**Contents:**

Compute and pair styles that implement the adiabatic core/shell model for polarizability. The pair styles augment Born, Buckingham, and Lennard-Jones styles with core/shell capabilities. The [[compute temp/cs]{.doc}]compute_temp_cs.md){.reference .internal} command calculates the temperature of a system with core/shell particles. See the [[Howto coreshell]{.doc}]Howto_coreshell.md){.reference .internal} page for an overview of how to use this package.

**Author:** Hendrik Heenen (Technical U of Munich).

**Supporting info:**

- [`src/CORESHELL`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Howto coreshell]{.doc}]Howto_coreshell.md){.reference .internal}

- [[Howto polarizable]{.doc}]Howto_polarizable.md){.reference .internal}

- [[compute temp/cs]{.doc}]compute_temp_cs.md){.reference .internal}

- [[pair_style born/coul/long/cs]{.doc}]pair_cs.md){.reference .internal}

- [[pair_style buck/coul/long/cs]{.doc}]pair_cs.md){.reference .internal}

- [[pair_style lj/cut/coul/long/cs]{.doc}]pair_lj.md){.reference .internal}

- [`examples/coreshell`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

:::: {#dielectric-package .section}
[]{#pkg-dielectric}

## [8.1.16. ]{.section-number}DIELECTRIC package[](#dielectric-package "Link to this heading"){.headerlink}

**Contents:**

An atom style, multiple pair styles, several fixes, Kspace styles and a compute for simulating systems using boundary element solvers for computing the induced charges at the interface between two media with different dielectric constants.

**Install:**

To use this package, also the [[KSPACE]{.std .std-ref}](#pkg-kspace){.reference .internal} and [[EXTRA-PAIR]{.std .std-ref}](#pkg-extra-pair){.reference .internal} packages need to be installed.

**Author:** Trung Nguyen and Monica Olvera de la Cruz (Northwestern U)

::: versionadded
[Added in version 2Jul2021.]{.versionmodified .added}
:::

**Supporting info:**

- [`src/DIELECTRIC`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[atom_style dielectric]{.doc}]atom_style.md){.reference .internal}

- [[pair_style coul/cut/dielectric]{.doc}]pair_dielectric.md){.reference .internal}

- [[pair_style coul/long/dielectric]{.doc}]pair_dielectric.md){.reference .internal}

- [[pair_style lj/cut/coul/cut/dielectric]{.doc}]pair_dielectric.md){.reference .internal}

- [[pair_style lj/cut/coul/debye/dielectric]{.doc}]pair_dielectric.md){.reference .internal}

- [[pair_style lj/cut/coul/long/dielectric]{.doc}]pair_dielectric.md){.reference .internal}

- [[pair_style lj/cut/coul/msm/dielectric]{.doc}]pair_dielectric.md){.reference .internal}

- [[pair_style pppm/dielectric]{.doc}]kspace_style.md){.reference .internal}

- [[pair_style pppm/disp/dielectric]{.doc}]kspace_style.md){.reference .internal}

- [[pair_style msm/dielectric]{.doc}]kspace_style.md){.reference .internal}

- [[fix_style polarize/bem/icc]{.doc}]fix_polarize.md){.reference .internal}

- [[fix_style polarize/bem/gmres]{.doc}]fix_polarize.md){.reference .internal}

- [[fix_style polarize/functional]{.doc}]fix_polarize.md){.reference .internal}

- [[compute efield/atom]{.doc}]compute_efield_atom.md){.reference .internal}

- [`examples/PACKAGES/dielectric`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

::: {#diffraction-package .section}
[]{#pkg-diffraction}

## [8.1.17. ]{.section-number}DIFFRACTION package[](#diffraction-package "Link to this heading"){.headerlink}

**Contents:**

Two computes and a fix for calculating x-ray and electron diffraction intensities based on kinematic diffraction theory.

**Author:** Shawn Coleman while at the U Arkansas.

**Supporting info:**

- [`src/DIFFRACTION`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[compute saed]{.doc}]compute_saed.md){.reference .internal}

- [[compute xrd]{.doc}]compute_xrd.md){.reference .internal}

- [[fix saed/vtk]{.doc}]fix_saed_vtk.md){.reference .internal}

- [`examples/PACKAGES/diffraction`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#dipole-package .section}
[]{#pkg-dipole}

## [8.1.18. ]{.section-number}DIPOLE package[](#dipole-package "Link to this heading"){.headerlink}

**Contents:**

An atom style and several pair styles for point dipole models with short-range or long-range interactions.

**Supporting info:**

- [`src/DIPOLE`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[atom_style dipole]{.doc}]atom_style.md){.reference .internal}

- [[pair_style lj/cut/dipole/cut]{.doc}]pair_dipole.md){.reference .internal}

- [[pair_style lj/cut/dipole/long]{.doc}]pair_dipole.md){.reference .internal}

- [[pair_style lj/long/dipole/long]{.doc}]pair_dipole.md){.reference .internal}

- [[angle_style dipole]{.doc}]angle_dipole.md){.reference .internal}

- [`examples/dipole`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#dpd-basic-package .section}
[]{#pkg-dpd-basic}

## [8.1.19. ]{.section-number}DPD-BASIC package[](#dpd-basic-package "Link to this heading"){.headerlink}

**Contents:**

Pair styles for the basic dissipative particle dynamics (DPD) method and DPD thermostatting.

Pair style [[dpd/coul/slater/long]{.doc}]pair_dpd_coul_slater_long.md){.reference .internal} also includes smeared charges for coulomb interactions and thus requires the [[KSPACE]{.std .std-ref}](#pkg-kspace){.reference .internal} package to be installed to handle the long-range Coulomb part of the interactions.

**Authors:** Kurt Smith (U Pittsburgh), Martin Svoboda, Martin Lisal (ICPF and UJEP), Eddy Barraud (IFPEN)

**Supporting info:**

- [`src/DPD-BASIC`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[pair_style dpd]{.doc}]pair_dpd.md){.reference .internal}

- [[pair_style dpd/tstat]{.doc}]pair_dpd.md){.reference .internal}

- [[pair_style dpd/ext]{.doc}]pair_dpd_ext.md){.reference .internal}

- [[pair_style dpd/ext/tstat]{.doc}]pair_dpd_ext.md){.reference .internal}

- [[pair_style dpd/coul/slater/long]{.doc}]pair_dpd_coul_slater_long.md){.reference .internal}

- [`examples/PACKAGES/dpd-basic`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#dpd-meso-package .section}
[]{#pkg-dpd-meso}

## [8.1.20. ]{.section-number}DPD-MESO package[](#dpd-meso-package "Link to this heading"){.headerlink}

**Contents:**

Several extensions of the dissipative particle dynamics (DPD) method. Specifically, energy-conserving DPD (eDPD) that can model non-isothermal processes, many-body DPD (mDPD) for simulating vapor-liquid coexistence, and transport DPD (tDPD) for modeling advection-diffusion-reaction systems. The equations of motion of these DPD extensions are integrated through a modified velocity-Verlet (MVV) algorithm.

**Author:** Zhen Li (Department of Mechanical Engineering, Clemson University)

**Supporting info:**

- [`src/DPD-MESO`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/DPD-MESO/README`{.docutils .literal .notranslate}]{.pre}

- [[atom_style edpd]{.doc}]atom_style.md){.reference .internal}

- [[pair_style edpd]{.doc}]pair_mesodpd.md){.reference .internal}

- [[pair_style mdpd]{.doc}]pair_mesodpd.md){.reference .internal}

- [[pair_style tdpd]{.doc}]pair_mesodpd.md){.reference .internal}

- [[fix mvv/dpd]{.doc}]fix_mvv_dpd.md){.reference .internal}

- [`examples/PACKAGES/mesodpd`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#dpd-react-package .section}
[]{#pkg-dpd-react}

## [8.1.21. ]{.section-number}DPD-REACT package[](#dpd-react-package "Link to this heading"){.headerlink}

**Contents:**

DPD stands for dissipative particle dynamics. This package implements coarse-grained DPD-based models for energetic, reactive molecular crystalline materials. It includes many pair styles specific to these systems, including for reactive DPD, where each particle has internal state for multiple species and a coupled set of chemical reaction ODEs are integrated each timestep. Highly accurate time integrators for isothermal, isoenergetic, isobaric and isenthalpic conditions are included. These enable long timesteps via the Shardlow splitting algorithm.

**Authors:** Jim Larentzos (ARL), Tim Mattox (Engility Corp), and John Brennan (ARL).

**Supporting info:**

- [`src/DPD-REACT`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/DPD-REACT/README`{.docutils .literal .notranslate}]{.pre}

- [[compute dpd]{.doc}]compute_dpd.md){.reference .internal}

- [[compute dpd/atom]{.doc}]compute_dpd_atom.md){.reference .internal}

- [[fix eos/cv]{.doc}]fix_eos_table.md){.reference .internal}

- [[fix eos/table]{.doc}]fix_eos_table.md){.reference .internal}

- [[fix eos/table/rx]{.doc}]fix_eos_table_rx.md){.reference .internal}

- [[fix shardlow]{.doc}]fix_shardlow.md){.reference .internal}

- [[fix rx]{.doc}]fix_rx.md){.reference .internal}

- [[pair_style table/rx]{.doc}]pair_table_rx.md){.reference .internal}

- [[pair_style dpd/fdt]{.doc}]pair_dpd_fdt.md){.reference .internal}

- [[pair_style dpd/fdt/energy]{.doc}]pair_dpd_fdt.md){.reference .internal}

- [[pair_style exp6/rx]{.doc}]pair_exp6_rx.md){.reference .internal}

- [[pair_style multi/lucy]{.doc}]pair_multi_lucy.md){.reference .internal}

- [[pair_style multi/lucy/rx]{.doc}]pair_multi_lucy_rx.md){.reference .internal}

- [`examples/PACKAGES/dpd-react`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#dpd-smooth-package .section}
[]{#pkg-dpd-smooth}

## [8.1.22. ]{.section-number}DPD-SMOOTH package[](#dpd-smooth-package "Link to this heading"){.headerlink}

**Contents:**

A pair style for smoothed dissipative particle dynamics (SDPD), which is an extension of smoothed particle hydrodynamics (SPH) to mesoscale where thermal fluctuations are important (see the [[SPH package]{.std .std-ref}](#pkg-sph){.reference .internal}). Also two fixes for moving and rigid body integration of SPH/SDPD particles (particles of atom_style meso).

**Author:** Morteza Jalalvand (Institute for Advanced Studies in Basic Sciences, Iran).

**Supporting info:**

- [`src/DPD-SMOOTH`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/DPD-SMOOTH/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style sdpd/taitwater/isothermal]{.doc}]pair_sdpd_taitwater_isothermal.md){.reference .internal}

- [[fix meso/move]{.doc}]fix_meso_move.md){.reference .internal}

- [[fix rigid/meso]{.doc}]fix_rigid_meso.md){.reference .internal}

- [`examples/PACKAGES/dpd-smooth`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#drude-package .section}
[]{#pkg-drude}

## [8.1.23. ]{.section-number}DRUDE package[](#drude-package "Link to this heading"){.headerlink}

**Contents:**

Fixes, pair styles, and a compute to simulate thermalized Drude oscillators as a model of polarization. See the [[Howto drude]{.doc}]Howto_drude.md){.reference .internal} and [[Howto drude2]{.doc}]Howto_drude2.md){.reference .internal} pages for an overview of how to use the package. There are auxiliary tools for using this package in tools/drude.

**Authors:** Alain Dequidt (U Clermont Auvergne), Julien Devemy (CNRS), and Agilio Padua (ENS de Lyon).

**Supporting info:**

- [`src/DRUDE`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Howto drude]{.doc}]Howto_drude.md){.reference .internal}

- [[Howto drude2]{.doc}]Howto_drude2.md){.reference .internal}

- [[Howto polarizable]{.doc}]Howto_polarizable.md){.reference .internal}

- [`src/DRUDE/README`{.docutils .literal .notranslate}]{.pre}

- [[fix drude]{.doc}]fix_drude.md){.reference .internal}

- [[fix drude/transform/\*]{.doc}]fix_drude_transform.md){.reference .internal}

- [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal}

- [[pair_style thole]{.doc}]pair_thole.md){.reference .internal}

- [[pair_style lj/cut/thole/long]{.doc}]pair_thole.md){.reference .internal}

- [`examples/PACKAGES/drude`{.docutils .literal .notranslate}]{.pre}

- tools/drude

------------------------------------------------------------------------
:::

::: {#eff-package .section}
[]{#pkg-eff}

## [8.1.24. ]{.section-number}EFF package[](#eff-package "Link to this heading"){.headerlink}

**Contents:**

EFF stands for electron force field which allows a classical MD code to model electrons as particles of variable radius. This package contains atom, pair, fix and compute styles which implement the eFF as described in A. Jaramillo-Botero, J. Su, Q. An, and W.A. Goddard III, JCC, 2010. The eFF potential was first introduced by Su and Goddard, in 2007. There are auxiliary tools for using this package in tools/eff; see its README file.

**Author:** Andres Jaramillo-Botero (CalTech).

**Supporting info:**

- [`src/EFF`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/EFF/README`{.docutils .literal .notranslate}]{.pre}

- [[atom_style electron]{.doc}]atom_style.md){.reference .internal}

- [[fix nve/eff]{.doc}]fix_nve_eff.md){.reference .internal}

- [[fix nvt/eff]{.doc}]fix_nh_eff.md){.reference .internal}

- [[fix npt/eff]{.doc}]fix_nh_eff.md){.reference .internal}

- [[fix langevin/eff]{.doc}]fix_langevin_eff.md){.reference .internal}

- [[compute temp/eff]{.doc}]compute_temp_eff.md){.reference .internal}

- [[pair_style eff/cut]{.doc}]pair_eff.md){.reference .internal}

- [[pair_style eff/inline]{.doc}]pair_eff.md){.reference .internal}

- [`examples/PACKAGES/eff`{.docutils .literal .notranslate}]{.pre}

- tools/eff/README

- tools/eff

- [https://www.lammps.org/movies.html#eff](https://www.lammps.org/movies.html#eff){.reference .external}

------------------------------------------------------------------------
:::

:::: {#electrode-package .section}
[]{#pkg-electrode}

## [8.1.25. ]{.section-number}ELECTRODE package[](#electrode-package "Link to this heading"){.headerlink}

**Contents:**

The ELECTRODE package allows the user to enforce a constant potential method for groups of atoms that interact with the remaining atoms as electrolyte.

**Authors:** The ELECTRODE package is written and maintained by Ludwig Ahrens-Iwers (TUHH, Hamburg, Germany), Shern Tee (UQ, Brisbane, Australia) and Robert Meissner (Helmholtz-Zentrum Hereon, Geesthacht and TUHH, Hamburg, Germany).

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#electrode){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [[fix electrode/conp]{.doc}]fix_electrode.md){.reference .internal}

- [[fix electrode/conq]{.doc}]fix_electrode.md){.reference .internal}

- [[fix electrode/thermo]{.doc}]fix_electrode.md){.reference .internal}

------------------------------------------------------------------------
::::

::: {#extra-command-package .section}
[]{#pkg-extra-command}

## [8.1.26. ]{.section-number}EXTRA-COMMAND package[](#extra-command-package "Link to this heading"){.headerlink}

**Contents:**

Additional command styles that are less commonly used.

**Supporting info:**

- [`src/EXTRA-COMMAND`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[general commands]{.doc}]Commands_all.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#extra-compute-package .section}
[]{#pkg-extra-compute}

## [8.1.27. ]{.section-number}EXTRA-COMPUTE package[](#extra-compute-package "Link to this heading"){.headerlink}

**Contents:**

Additional compute styles that are less commonly used.

**Supporting info:**

- [`src/EXTRA-COMPUTE`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[compute]{.doc}]compute.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#extra-dump-package .section}
[]{#pkg-extra-dump}

## [8.1.28. ]{.section-number}EXTRA-DUMP package[](#extra-dump-package "Link to this heading"){.headerlink}

**Contents:**

Additional dump styles that are less commonly used.

**Supporting info:**

- [`src/EXTRA-DUMP`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[dump]{.doc}]dump.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#extra-fix-package .section}
[]{#pkg-extra-fix}

## [8.1.29. ]{.section-number}EXTRA-FIX package[](#extra-fix-package "Link to this heading"){.headerlink}

**Contents:**

Additional fix styles that are less commonly used.

**Supporting info:**

- [`src/EXTRA-FIX`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[fix]{.doc}]fix.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#extra-molecule-package .section}
[]{#pkg-extra-molecule}

## [8.1.30. ]{.section-number}EXTRA-MOLECULE package[](#extra-molecule-package "Link to this heading"){.headerlink}

**Contents:**

Additional bond, angle, dihedral, and improper styles that are less commonly used.

**Install:**

To use this package, also the [[MOLECULE]{.std .std-ref}](#pkg-molecule){.reference .internal} package needs to be installed.

**Supporting info:**

- [`src/EXTRA-MOLECULE`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[molecular styles]{.doc}]Commands_bond.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#extra-pair-package .section}
[]{#pkg-extra-pair}

## [8.1.31. ]{.section-number}EXTRA-PAIR package[](#extra-pair-package "Link to this heading"){.headerlink}

**Contents:**

Additional pair styles that are less commonly used.

**Supporting info:**

- [`src/EXTRA-PAIR`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[pair_style]{.doc}]pair_style.md){.reference .internal}

- [`examples/PACKAGES/dispersion`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#fep-package .section}
[]{#pkg-fep}

## [8.1.32. ]{.section-number}FEP package[](#fep-package "Link to this heading"){.headerlink}

**Contents:**

FEP stands for free energy perturbation. This package provides methods for performing FEP simulations by using a [[fix adapt/fep]{.doc}]fix_adapt_fep.md){.reference .internal} command with soft-core pair potentials, which have a "soft" in their style name. There are auxiliary tools for using this package in [`tools/fep`{.docutils .literal .notranslate}]{.pre}; see its [`README`{.docutils .literal .notranslate}]{.pre} file.

**Author:** Agilio Padua (ENS de Lyon)

**Supporting info:**

- [`src/FEP`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/FEP/README`{.docutils .literal .notranslate}]{.pre}

- [[fix adapt/fep]{.doc}]fix_adapt_fep.md){.reference .internal}

- [[compute fep]{.doc}]compute_fep.md){.reference .internal}

- [[pair_style \*/soft]{.doc}]pair_fep_soft.md){.reference .internal}

- [`examples/PACKAGES/fep`{.docutils .literal .notranslate}]{.pre}

- tools/fep/README

- tools/fep

------------------------------------------------------------------------
:::

::: {#gpu-package .section}
[]{#pkg-gpu}

## [8.1.33. ]{.section-number}GPU package[](#gpu-package "Link to this heading"){.headerlink}

**Contents:**

Dozens of pair styles and a version of the PPPM long-range Coulombic solver optimized for GPUs. All such styles have a "gpu" as a suffix in their style name. The GPU code can be compiled with either CUDA or OpenCL, however the OpenCL variants are no longer actively maintained and only the CUDA versions are regularly tested. The [[GPU package]{.doc}]Speed_gpu.md){.reference .internal} page gives details of what hardware and GPU software is required on your system, and details on how to build and use this package. Its styles can be invoked at run time via the [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gpu`{.docutils .literal .notranslate}]{.pre} or [`-suffix`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`gpu`{.docutils .literal .notranslate}]{.pre} [[command-line switches]{.doc}]Run_options.md){.reference .internal}. See also the [[KOKKOS]{.std .std-ref}](#pkg-kokkos){.reference .internal} package, which has GPU-enabled styles.

**Authors:** Mike Brown (Intel) while at Sandia and ORNL and Trung Nguyen (Northwestern U) while at ORNL and later. AMD HIP support by Evgeny Kuznetsov, Vladimir Stegailov, and Vsevolod Nikolskiy (HSE University).

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#gpu){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/GPU`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/GPU/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/gpu/README`{.docutils .literal .notranslate}]{.pre}

- [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal}

- [[GPU package]{.doc}]Speed_gpu.md){.reference .internal}

- [[Section 4.2 -sf gpu]{.doc}]Run_options.md){.reference .internal}

- [[Section 4.2 -pk gpu]{.doc}]Run_options.md){.reference .internal}

- [[package gpu]{.doc}]package.md){.reference .internal}

- [[Commands]{.doc}]Commands_all.md){.reference .internal} pages ([[pair]{.doc}]Commands_pair.md){.reference .internal}, [[kspace]{.doc}]Commands_kspace.md){.reference .internal}) for styles followed by (g)

- [Benchmarks page](https://www.lammps.org/bench.html){.reference .external} of website

------------------------------------------------------------------------
:::

::: {#graphics-package .section}
[]{#pkg-graphics}

## [8.1.34. ]{.section-number}GRAPHICS package[](#graphics-package "Link to this heading"){.headerlink}

**Contents:**

Dump styles [[image and movie]{.doc}]dump_image.md){.reference .internal}, supporting classes for rendering images and fonts, several fixes for adding graphics objects to visualizations, and the region2vmd command for exporting visualizations of regions as scripted graphics in VMD.

**Supporting info:**

- [`src/GRAPHICS`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Visualize LAMMPS snapshots]{.doc}]Howto_viz.md){.reference .internal}

- [[dump image]{.doc}]dump_image.md){.reference .internal}

- [[dump movie]{.doc}]dump_image.md){.reference .internal}

- [[fix graphics/arrows]{.doc}]fix_graphics_arrows.md){.reference .internal}

- [[fix graphics/isosurface]{.doc}]fix_graphics_isosurface.md){.reference .internal}

- [[fix graphics/labels]{.doc}]fix_graphics_labels.md){.reference .internal},

- [[fix graphics/lines]{.doc}]fix_graphics_lines.md){.reference .internal},

- [[fix graphics/objects]{.doc}]fix_graphics_objects.md){.reference .internal},

- [[fix graphics/periodic]{.doc}]fix_graphics_periodic.md){.reference .internal},

- [[region2vmd]{.doc}]region2vmd.md){.reference .internal}

- [https://www.youtube.com/watch?v=9HEsGaOsdik](https://www.youtube.com/watch?v=9HEsGaOsdik){.reference .external}

- [https://www.youtube.com/watch?v=f4hfPs7aCmI](https://www.youtube.com/watch?v=f4hfPs7aCmI){.reference .external}

- [https://www.youtube.com/shorts/1QEjIITapwQ](https://www.youtube.com/shorts/1QEjIITapwQ){.reference .external}

- [https://www.youtube.com/shorts/OYn_VVodnIg](https://www.youtube.com/shorts/OYn_VVodnIg){.reference .external}

- [https://www.youtube.com/shorts/4Cm5p0SfgNU](https://www.youtube.com/shorts/4Cm5p0SfgNU){.reference .external}

------------------------------------------------------------------------
:::

::: {#granular-package .section}
[]{#pkg-granular}

## [8.1.35. ]{.section-number}GRANULAR package[](#granular-package "Link to this heading"){.headerlink}

**Contents:**

Pair styles and fixes for finite-size granular particles, which interact with each other and boundaries via frictional and dissipative potentials.

**Supporting info:**

- [`src/GRANULAR`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Howto granular]{.doc}]Howto_granular.md){.reference .internal}

- [[fix pour]{.doc}]fix_pour.md){.reference .internal}

- [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal}

- [[pair_style gran/hooke]{.doc}]pair_gran.md){.reference .internal}

- [[pair_style gran/hertz/history]{.doc}]pair_gran.md){.reference .internal}

- [`examples/granregion`{.docutils .literal .notranslate}]{.pre}

- [`examples/pour`{.docutils .literal .notranslate}]{.pre}

- bench/in.chute

- [https://www.lammps.org/pictures.html#jamming](https://www.lammps.org/pictures.html#jamming){.reference .external}

- [https://www.lammps.org/movies.html#hopper](https://www.lammps.org/movies.html#hopper){.reference .external}

- [https://www.lammps.org/movies.html#dem](https://www.lammps.org/movies.html#dem){.reference .external}

- [https://www.lammps.org/movies.html#brazil](https://www.lammps.org/movies.html#brazil){.reference .external}

- [https://www.lammps.org/movies.html#granregion](https://www.lammps.org/movies.html#granregion){.reference .external}

------------------------------------------------------------------------
:::

::: {#h5md-package .section}
[]{#pkg-h5md}

## [8.1.36. ]{.section-number}H5MD package[](#h5md-package "Link to this heading"){.headerlink}

**Contents:**

H5MD stands for HDF5 for MD. [HDF5](https://www.hdfgroup.org/solutions/hdf5/){.reference .external} is a portable, binary, self-describing file format, used by many scientific simulations. H5MD is a format for molecular simulations, built on top of HDF5. This package implements a [[dump h5md]{.doc}]dump_h5md.md){.reference .internal} command to output LAMMPS snapshots in this format.

To use this package you must have the HDF5 library available on your system.

**Author:** Pierre de Buyl (KU Leuven) created both the package and the H5MD format.

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#h5md){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/H5MD`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/H5MD/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/h5md/README`{.docutils .literal .notranslate}]{.pre}

- [[dump h5md]{.doc}]dump_h5md.md){.reference .internal}

------------------------------------------------------------------------
:::

:::: {#intel-package .section}
[]{#pkg-intel}

## [8.1.37. ]{.section-number}INTEL package[](#intel-package "Link to this heading"){.headerlink}

**Contents:**

Dozens of pair, fix, bond, angle, dihedral, improper, and kspace styles which are optimized for Intel CPUs and KNLs (Knights Landing). All of them have an "intel" in their style name. The [[INTEL package]{.doc}]Speed_intel.md){.reference .internal} page gives details of what hardware and compilers are required on your system, and how to build and use this package. Its styles can be invoked at run time via the [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`intel`{.docutils .literal .notranslate}]{.pre} or [`-suffix`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`intel`{.docutils .literal .notranslate}]{.pre} [[command-line switches]{.doc}]Run_options.md){.reference .internal}. Also see the [[KOKKOS]{.std .std-ref}](#pkg-kokkos){.reference .internal}, [[OPT]{.std .std-ref}](#pkg-opt){.reference .internal}, and [[OPENMP]{.std .std-ref}](#pkg-openmp){.reference .internal} packages, which have styles optimized for CPUs and KNLs.

You need to have an Intel compiler, version 14 or higher to take full advantage of this package. While compilation with GNU compilers is supported, performance will be sub-optimal.

::: {.admonition .note}
Note

the INTEL package contains styles that require using the -restrict flag, when compiling with Intel compilers.
:::

**Author:** Mike Brown (Intel).

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#intel){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/INTEL`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/INTEL/README`{.docutils .literal .notranslate}]{.pre}

- [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal}

- [[INTEL package]{.doc}]Speed_intel.md){.reference .internal}

- [[Section 4.2 -sf intel]{.doc}]Run_options.md){.reference .internal}

- [[Section 4.2 -pk intel]{.doc}]Run_options.md){.reference .internal}

- [[package intel]{.doc}]package.md){.reference .internal}

- Search the [[commands]{.doc}]Commands_all.md){.reference .internal} pages ([[fix]{.doc}]Commands_fix.md){.reference .internal}, [[compute]{.doc}]Commands_compute.md){.reference .internal}, [[pair]{.doc}]Commands_pair.md){.reference .internal}, [[bond, angle, dihedral, improper]{.doc}]Commands_bond.md){.reference .internal}, [[kspace]{.doc}]Commands_kspace.md){.reference .internal}) for styles followed by (i)

- [`src/INTEL/TEST`{.docutils .literal .notranslate}]{.pre}

- [Benchmarks page](https://www.lammps.org/bench.html){.reference .external} of website

------------------------------------------------------------------------
::::

::: {#interlayer-package .section}
[]{#pkg-interlayer}

## [8.1.38. ]{.section-number}INTERLAYER package[](#interlayer-package "Link to this heading"){.headerlink}

**Contents:**

A collection of pair styles specifically to be used for modeling layered materials, most commonly graphene sheets (or equivalents).

**Supporting info:**

- [`src/INTERLAYER`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Pair style]{.doc}]Commands_pair.md){.reference .internal} page

- [`examples/PACKAGES/interlayer`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

:::: {#kim-package .section}
[]{#pkg-kim}

## [8.1.39. ]{.section-number}KIM package[](#kim-package "Link to this heading"){.headerlink}

**Contents:**

This package contains a command with a set of sub-commands that serve as a wrapper on the [Open Knowledgebase of Interatomic Models (OpenKIM)](https://openkim.org){.reference .external} repository of interatomic models (IMs) enabling compatible ones to be used in LAMMPS simulations.

This includes [[kim init]{.doc}]kim_commands.md){.reference .internal}, and [[kim interactions]{.doc}]kim_commands.md){.reference .internal} commands to select, initialize and instantiate the IM, a [[kim query]{.doc}]kim_commands.md){.reference .internal} command to perform web queries for material property predictions of OpenKIM IMs, a [[kim param]{.doc}]kim_commands.md){.reference .internal} command to access KIM Model Parameters from LAMMPS, and a [[kim property]{.doc}]kim_commands.md){.reference .internal} command to write material properties computed in LAMMPS to standard KIM property instance format.

Support for KIM IMs that conform to the [KIM Application Programming Interface (API)](https://openkim.org/kim-api/){.reference .external} is provided by the [[pair_style kim]{.doc}]pair_kim.md){.reference .internal} command.

::: {.admonition .note}
Note

The command *pair_style kim* is called by *kim interactions* and is not recommended to be directly used in input scripts.
:::

To use this package you must have the KIM API library available on your system. The KIM API is available for download on the [OpenKIM website](https://openkim.org/kim-api/){.reference .external}. When installing LAMMPS from binary, the kim-api package is a dependency that is automatically downloaded and installed.

Information about the KIM project can be found at its website: [https://openkim.org](https://openkim.org){.reference .external}. The KIM project is led by Ellad Tadmor and Ryan Elliott (U Minnesota) and is funded by the [National Science Foundation](https://www.nsf.gov/){.reference .external}.

**Authors:** Ryan Elliott (U Minnesota) is the main developer for the KIM API and the *pair_style kim* command. Yaser Afshar (U Minnesota), Axel Kohlmeyer (Temple U), Ellad Tadmor (U Minnesota), and Daniel Karls (U Minnesota) contributed to the [[kim command]{.doc}]kim_commands.md){.reference .internal} interface in close collaboration with Ryan Elliott.

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#kim){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [[kim command]{.doc}]kim_commands.md){.reference .internal}

- [[pair_style kim]{.doc}]pair_kim.md){.reference .internal}

- [`src/KIM`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/KIM/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/kim/README`{.docutils .literal .notranslate}]{.pre}

- [`examples/kim`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

::: {#kokkos-package .section}
[]{#pkg-kokkos}

## [8.1.40. ]{.section-number}KOKKOS package[](#kokkos-package "Link to this heading"){.headerlink}

**Contents:**

Dozens of atom, pair, bond, angle, dihedral, improper, fix, compute styles adapted to compile using the Kokkos library which can convert them to OpenMP or CUDA code so that they run efficiently on multicore CPUs, KNLs, or GPUs. All the styles have a "kk" as a suffix in their style name. The [[KOKKOS package]{.doc}]Speed_kokkos.md){.reference .internal} page gives details of what hardware and software is required on your system, and how to build and use this package. Its styles can be invoked at run time via the [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kk`{.docutils .literal .notranslate}]{.pre} or [`-suffix`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kk`{.docutils .literal .notranslate}]{.pre} [[command-line switches]{.doc}]Run_options.md){.reference .internal}. Also see the [[GPU]{.std .std-ref}](#pkg-gpu){.reference .internal}, [[OPT]{.std .std-ref}](#pkg-opt){.reference .internal}, [[INTEL]{.std .std-ref}](#pkg-intel){.reference .internal}, and [[OPENMP]{.std .std-ref}](#pkg-openmp){.reference .internal} packages, which have styles optimized for CPUs, KNLs, and GPUs.

You must have a C++20 compatible compiler to use this package. KOKKOS makes extensive use of advanced C++ features, which can expose compiler bugs, especially when compiling for maximum performance at high optimization levels. Please see the file [`lib/kokkos/README`{.docutils .literal .notranslate}]{.pre} for a list of compilers and their respective platforms, that are known to work.

**Authors:** The KOKKOS package was created primarily by Christian Trott and Stan Moore (Sandia), with contributions from other folks as well. It uses the open-source [Kokkos library](https://github.com/kokkos){.reference .external} which was developed by Carter Edwards, Christian Trott, and others at Sandia, and which is included in the LAMMPS distribution in [`lib/kokkos`{.docutils .literal .notranslate}]{.pre}.

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#kokkos){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/KOKKOS`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/KOKKOS/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/kokkos/README`{.docutils .literal .notranslate}]{.pre}

- [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal}

- [[KOKKOS package]{.doc}]Speed_kokkos.md){.reference .internal}

- [[Section 4.2 -k on ...]{.doc}]Run_options.md){.reference .internal}

- [[Section 4.2 -sf kk]{.doc}]Run_options.md){.reference .internal}

- [[Section 4.2 -pk kokkos]{.doc}]Run_options.md){.reference .internal}

- [[package kokkos]{.doc}]package.md){.reference .internal}

- Search the [[commands]{.doc}]Commands_all.md){.reference .internal} pages ([[fix]{.doc}]Commands_fix.md){.reference .internal}, [[compute]{.doc}]Commands_compute.md){.reference .internal}, [[pair]{.doc}]Commands_pair.md){.reference .internal}, [[bond, angle, dihedral, improper]{.doc}]Commands_bond.md){.reference .internal}, [[kspace]{.doc}]Commands_kspace.md){.reference .internal}) for styles followed by (k)

- [Benchmarks page](https://www.lammps.org/bench.html){.reference .external} of website

------------------------------------------------------------------------
:::

::: {#kspace-package .section}
[]{#pkg-kspace}

## [8.1.41. ]{.section-number}KSPACE package[](#kspace-package "Link to this heading"){.headerlink}

**Contents:**

A variety of long-range Coulombic solvers, as well as pair styles which compute the corresponding short-range pairwise Coulombic interactions. These include Ewald, particle-particle particle-mesh (PPPM), and multilevel summation method (MSM) solvers.

**Install:**

Building with this package requires a 1d FFT library be present on your system for use by the PPPM solvers. This can be the KISS FFT library provided with LAMMPS, third party libraries like FFTW, or a vendor-supplied FFT library. See the [[Build settings]{.doc}]Build_settings.md){.reference .internal} page for details on how to select different FFT options for your LAMMPS build.

**Supporting info:**

- [`src/KSPACE`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[kspace_style]{.doc}]kspace_style.md){.reference .internal}

- [doc/PDF/kspace.pdf](PDF/kspace.pdf){.reference .external}

- [[Howto tip3p]{.doc}]Howto_tip3p.md){.reference .internal}

- [[Howto tip4p]{.doc}]Howto_tip4p.md){.reference .internal}

- [[Howto spc]{.doc}]Howto_spc.md){.reference .internal}

- [[pair_style coul]{.doc}]pair_coul.md){.reference .internal}

- Search the [[pair style]{.doc}]Commands_pair.md){.reference .internal} page for styles with "long" or "msm" in name

- [`examples/peptide`{.docutils .literal .notranslate}]{.pre}

- bench/in.rhodo

------------------------------------------------------------------------
:::

::: {#latboltz-package .section}
[]{#pkg-latboltz}

## [8.1.42. ]{.section-number}LATBOLTZ package[](#latboltz-package "Link to this heading"){.headerlink}

**Contents:**

Fixes which implement a background Lattice-Boltzmann (LB) fluid, which can be used to model MD particles influenced by hydrodynamic forces.

**Authors:** Frances Mackay and Colin Denniston (University of Western Ontario).

**Install:**

The LATBOLTZ package requires that LAMMPS is built in [[MPI parallel mode]{.std .std-ref}]Build_basics.md#serial){.reference .internal}.

**Supporting info:**

- [`src/LATBOLTZ`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/LATBOLTZ/README`{.docutils .literal .notranslate}]{.pre}

- [[fix lb/fluid]{.doc}]fix_lb_fluid.md){.reference .internal}

- [[fix lb/momentum]{.doc}]fix_lb_momentum.md){.reference .internal}

- [[fix lb/viscous]{.doc}]fix_lb_viscous.md){.reference .internal}

- [`examples/PACKAGES/latboltz`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

:::: {#lepton-package .section}
[]{#pkg-lepton}

## [8.1.43. ]{.section-number}LEPTON package[](#lepton-package "Link to this heading"){.headerlink}

**Contents:**

Styles for pair, bond, and angle forces that evaluate the potential function from a string using the [Lepton mathematical expression parser](https://simtk.org/projects/lepton){.reference .external}. Lepton is a C++ library that is bundled with [OpenMM](https://openmm.org/){.reference .external} and can be used for parsing, evaluating, differentiating, and analyzing mathematical expressions. This is a more lightweight and efficient alternative for evaluating custom potential function to an embedded Python interpreter as used in the [[PYTHON package]{.std .std-ref}](#pkg-python){.reference .internal}. On the other hand, since the potentials are evaluated form analytical expressions, they are more precise than what can be done with [[tabulated potentials]{.std .std-ref}]Tools.md#tabulate){.reference .internal}.

**Authors:** Axel Kohlmeyer (Temple U). Lepton itself is developed by Peter Eastman at Stanford University.

::: versionadded
[Added in version 8Feb2023.]{.versionmodified .added}
:::

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#lepton){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/LEPTON`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`lib/lepton/README`{.docutils .literal .notranslate}]{.pre}.md

- [[pair_style lepton]{.doc}]pair_lepton.md){.reference .internal}

- [[bond_style lepton]{.doc}]bond_lepton.md){.reference .internal}

- [[angle_style lepton]{.doc}]angle_lepton.md){.reference .internal}

- [[dihedral_style lepton]{.doc}]dihedral_lepton.md){.reference .internal}

------------------------------------------------------------------------
::::

::: {#machdyn-package .section}
[]{#pkg-machdyn}

## [8.1.44. ]{.section-number}MACHDYN package[](#machdyn-package "Link to this heading"){.headerlink}

**Contents:**

An atom style, fixes, computes, and several pair styles which implements smoothed Mach dynamics (SMD) for solids, which is a model related to smoothed particle hydrodynamics (SPH) for liquids (see the [[SPH package]{.std .std-ref}](#pkg-sph){.reference .internal}).

This package solves solids mechanics problems via a state of the art stabilized meshless method with hourglass control. It can specify hydrostatic interactions independently from material strength models, i.e. pressure and deviatoric stresses are separated. It provides many material models (Johnson-Cook, plasticity with hardening, Mie-Grueneisen, Polynomial EOS) and allows new material models to be added. It implements rigid boundary conditions (walls) which can be specified as surface geometries from \*.STL files.

**Author:** Georg Ganzenmuller (Fraunhofer-Institute for High-Speed Dynamics, Ernst Mach Institute, Germany).

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#machdyn){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/MACHDYN`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/MACHDYN/README`{.docutils .literal .notranslate}]{.pre}

- [doc/PDF/MACHDYN_LAMMPS_userguide.pdf](PDF/MACHDYN_LAMMPS_userguide.pdf){.reference .external}

- [`examples/PACKAGES/machdyn`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#manifold-package .section}
[]{#pkg-manifold}

## [8.1.45. ]{.section-number}MANIFOLD package[](#manifold-package "Link to this heading"){.headerlink}

**Contents:**

Several fixes and a "manifold" class which enable simulations of particles constrained to a manifold (a 2D surface within the 3D simulation box). This is done by applying the RATTLE constraint algorithm to formulate single-particle constraint functions g(xi,yi,zi) = 0 and their derivative (i.e. the normal of the manifold) n = grad(g).

**Author:** Stefan Paquay (until 2017: Eindhoven University of Technology (TU/e), The Netherlands; since 2017: Brandeis University, Waltham, MA, USA)

**Supporting info:**

- [`src/MANIFOLD`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/MANIFOLD/README`{.docutils .literal .notranslate}]{.pre}

- [[Howto manifold]{.doc}]Howto_manifold.md){.reference .internal}

- [[fix manifoldforce]{.doc}]fix_manifoldforce.md){.reference .internal}

- [[fix nve/manifold/rattle]{.doc}]fix_nve_manifold_rattle.md){.reference .internal}

- [[fix nvt/manifold/rattle]{.doc}]fix_nvt_manifold_rattle.md){.reference .internal}

- [`examples/PACKAGES/manifold`{.docutils .literal .notranslate}]{.pre}

- [https://www.lammps.org/movies.html#manifold](https://www.lammps.org/movies.html#manifold){.reference .external}

------------------------------------------------------------------------
:::

::: {#manybody-package .section}
[]{#pkg-manybody}

## [8.1.46. ]{.section-number}MANYBODY package[](#manybody-package "Link to this heading"){.headerlink}

**Contents:**

A variety of many-body and bond-order potentials. These include (AI)REBO, BOP, EAM, EIM, Stillinger-Weber, and Tersoff potentials.

**Supporting info:**

- [`src/MANYBODY`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Pair style]{.doc}]Commands_pair.md){.reference .internal} page

- [`examples/comb`{.docutils .literal .notranslate}]{.pre}

- [`examples/eim`{.docutils .literal .notranslate}]{.pre}

- [`examples/nb3d`{.docutils .literal .notranslate}]{.pre}

- [`examples/shear`{.docutils .literal .notranslate}]{.pre}

- [`examples/streitz`{.docutils .literal .notranslate}]{.pre}

- [`examples/vashishta`{.docutils .literal .notranslate}]{.pre}

- bench/in.eam

------------------------------------------------------------------------
:::

:::: {#mbx-package .section}
[]{#pkg-mbx}

## [8.1.47. ]{.section-number}MBX Package[](#mbx-package "Link to this heading"){.headerlink}

**Contents**

The pair_style mbx command implements the MBX library for MB-pol and MB-nrg data-driven many-body potential energy functions. MBX is called using [[pair_style mbx]{.doc}]pair_mbx.md){.reference .internal} command, which allows for MB-nrg potentials such as MB-pol to be used in LAMMPS. For more information on MBX, see the [MBX library](https://mbxsimulations.com){.reference .external} website.

**Authors:** The [MBX library](https://mbxsimulations.com){.reference .external} is developed by the Paesani group at the University of California, San Diego. Major contributors include: Marc Riera, Christopher Knight, Ethan Bull-Vulpe, and Henry Agnew.

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#mbx){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/MBX`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[pair_style mbx]{.doc}]pair_mbx.md){.reference .internal}

- [https://mbxsimulations.com/](https://mbxsimulations.com/){.reference .external}

------------------------------------------------------------------------
::::

::: {#mc-package .section}
[]{#pkg-mc}

## [8.1.48. ]{.section-number}MC package[](#mc-package "Link to this heading"){.headerlink}

**Contents:**

Several fixes and a pair style that have Monte Carlo (MC) or MC-like attributes. These include fixes for creating, breaking, and swapping bonds, for performing atomic swaps, and performing grand canonical MC (GCMC), semi-grand canonical MC (SGCMC), or similar processes in conjunction with molecular dynamics (MD).

**Supporting info:**

- [`src/MC`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[fix atom/swap]{.doc}]fix_atom_swap.md){.reference .internal}

- [[fix bond/break]{.doc}]fix_bond_break.md){.reference .internal}

- [[fix bond/create]{.doc}]fix_bond_create.md){.reference .internal}

- [[fix bond/create/angle]{.doc}]fix_bond_create.md){.reference .internal}

- [[fix bond/swap]{.doc}]fix_bond_swap.md){.reference .internal}

- [[fix charge/regulation]{.doc}]fix_charge_regulation.md){.reference .internal}

- [[fix gcmc]{.doc}]fix_gcmc.md){.reference .internal}

- [[fix hmc]{.doc}]fix_hmc.md){.reference .internal}

- [[fix mol/swap]{.doc}]fix_mol_swap.md){.reference .internal}

- [[fix neighbo/swap]{.doc}]fix_neighbor_swap.md){.reference .internal}

- [[fix sgcmc]{.doc}]fix_sgcmc.md){.reference .internal}

- [[fix tfmc]{.doc}]fix_tfmc.md){.reference .internal}

- [[fix widom]{.doc}]fix_widom.md){.reference .internal}

- [[pair_style dsmc]{.doc}]pair_dsmc.md){.reference .internal}

- [https://www.lammps.org/movies.html#gcmc](https://www.lammps.org/movies.html#gcmc){.reference .external}

------------------------------------------------------------------------
:::

:::: {#mdi-package .section}
[]{#pkg-mdi}

## [8.1.49. ]{.section-number}MDI package[](#mdi-package "Link to this heading"){.headerlink}

**Contents:**

A LAMMPS command and fixes to allow client-server coupling of LAMMPS to other atomic or molecular simulation codes or materials modeling workflows via the [MolSSI Driver Interface (MDI) library](https://molssi-mdi.github.io/MDI_Library/){.reference .external}.

**Author:** Taylor Barnes - MolSSI, taylor.a.barnes at gmail.com

::: versionadded
[Added in version 14May2021.]{.versionmodified .added}
:::

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#mdi){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/MDI/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/mdi/README`{.docutils .literal .notranslate}]{.pre}

- [[Howto MDI]{.doc}]Howto_mdi.md){.reference .internal}

- [[mdi]{.doc}]mdi.md){.reference .internal}

- [[fix mdi/qm]{.doc}]fix_mdi_qm.md){.reference .internal}

- [`examples/PACKAGES/mdi`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

::: {#meam-package .section}
[]{#pkg-meam}

## [8.1.50. ]{.section-number}MEAM package[](#meam-package "Link to this heading"){.headerlink}

**Contents:**

A pair style for the modified embedded atom (MEAM) potential translated from the Fortran version in the (obsolete) MEAM package to plain C++. The MEAM fully replaces the MEAM package, which has been removed from LAMMPS after the 12 December 2018 version.

**Author:** Sebastian Huetter, (Otto-von-Guericke University Magdeburg) based on the Fortran version of Greg Wagner (Northwestern U) while at Sandia.

**Supporting info:**

- [`src/MEAM`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/MEAM/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style meam]{.doc}]pair_meam.md){.reference .internal}

- [`examples/meam`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::::: {#mesont-package .section}
[]{#pkg-mesont}

## [8.1.51. ]{.section-number}MESONT package[](#mesont-package "Link to this heading"){.headerlink}

**Contents:**

MESONT is a LAMMPS package for simulation of nanomechanics of nanotubes (NTs). The model is based on a coarse-grained representation of NTs as "flexible cylinders" consisting of a variable number of segments. Internal interactions within a NT and the van der Waals interaction between the tubes are described by a mesoscopic force field designed and parameterized based on the results of atomic-level molecular dynamics simulations. The description of the force field is provided in the papers listed in [`src/MESONT/README`{.docutils .literal .notranslate}]{.pre}.

This package used to have two independent implementations of this model: the original implementation using a Fortran library written by the developers of the model and a second implementation written in C++ by Philipp Kloza (U Cambridge). Since the C++ implementation offers the same features as the original implementation with the addition of friction, is typically faster, and easier to compile/install, the Fortran library based implementation has since been obsoleted and removed from the distribution. You have to download and compile an older version of LAMMPS if you want to use those.

**Download of potential files:**

The potential files for these pair styles are *very* large and thus are not included in the regular downloaded packages of LAMMPS or the git repositories. Instead, they will be automatically downloaded from a web server when the package is installed for the first time.

**Authors of the obsoleted \*mesont\* styles:**

Maxim V. Shugaev (University of Virginia), Alexey N. Volkov (University of Alabama), Leonid V. Zhigilei (University of Virginia)

::: deprecated
[Deprecated since version 8Feb2023.]{.versionmodified .deprecated}
:::

**Author of the C++ styles:** Philipp Kloza (U Cambridge)

::: versionadded
[Added in version 15Jun2020.]{.versionmodified .added}
:::

**Supporting info:**

- [`src/MESONT`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/MESONT/README`{.docutils .literal .notranslate}]{.pre}

- [[bond_style mesocnt]{.doc}]bond_mesocnt.md){.reference .internal}

- [[angle_style mesocnt]{.doc}]angle_mesocnt.md){.reference .internal}

- [[pair_style mesocnt]{.doc}]pair_mesocnt.md){.reference .internal}

- [`examples/PACKAGES/mesont`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::::

::: {#mgpt-package .section}
[]{#pkg-mgpt}

## [8.1.52. ]{.section-number}MGPT package[](#mgpt-package "Link to this heading"){.headerlink}

**Contents:**

A pair style which provides a fast implementation of the quantum-based MGPT multi-ion potentials. The MGPT or model GPT method derives from first-principles DFT-based generalized pseudopotential theory (GPT) through a series of systematic approximations valid for mid-period transition metals with nearly half-filled d bands. The MGPT method was originally developed by John Moriarty at LLNL. The pair style in this package calculates forces and energies using an optimized matrix-MGPT algorithm due to Tomas Oppelstrup at LLNL.

**Authors:** Tomas Oppelstrup and John Moriarty (LLNL).

**Supporting info:**

- [`src/MGPT`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/MGPT/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style mgpt]{.doc}]pair_mgpt.md){.reference .internal}

- [`examples/PACKAGES/mgpt`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

:::: {#misc-package .section}
[]{#pkg-misc}

## [8.1.53. ]{.section-number}MISC package[](#misc-package "Link to this heading"){.headerlink}

**Contents:**

A variety of compute, fix, pair, bond styles with specialized capabilities that don't align with other packages. Do a directory listing, [`ls`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`src/MISC`{.docutils .literal .notranslate}]{.pre}, to see the list of commands.

::: {.admonition .note}
Note

the MISC package contains styles that require using the -restrict flag, when compiling with Intel compilers.
:::

**Supporting info:**

- [`src/MISC`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[bond_style special]{.doc}]bond_special.md){.reference .internal}

- [[compute viscosity/cos]{.doc}]compute_viscosity_cos.md){.reference .internal}

- [[fix accelerate/cos]{.doc}]fix_accelerate_cos.md){.reference .internal}

- [[fix imd]{.doc}]fix_imd.md){.reference .internal}

- [[fix ipi]{.doc}]fix_ipi.md){.reference .internal}

- [[pair_style agni]{.doc}]pair_agni.md){.reference .internal}

- [[pair_style list]{.doc}]pair_list.md){.reference .internal}

- [[pair_style srp]{.doc}]pair_srp.md){.reference .internal}

- [[pair_style tracker]{.doc}]pair_tracker.md){.reference .internal}

------------------------------------------------------------------------
::::

:::: {#ml-hdnnp-package .section}
[]{#pkg-ml-hdnnp}

## [8.1.54. ]{.section-number}ML-HDNNP package[](#ml-hdnnp-package "Link to this heading"){.headerlink}

**Contents:**

A [[pair_style hdnnp]{.doc}]pair_hdnnp.md){.reference .internal} command which allows the use of high-dimensional neural network potentials (HDNNPs), a form of machine learning potentials. HDNNPs must be carefully trained prior to their application in a molecular dynamics simulation.

To use this package you must have the [n2p2](https://github.com/CompPhysVienna/n2p2){.reference .external} library installed and compiled on your system.

**Author:** Andreas Singraber

::: versionadded
[Added in version 27May2021.]{.versionmodified .added}
:::

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#ml-hdnnp){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/ML-HDNNP`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/ML-HDNNP/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/hdnnp/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style hdnnp]{.doc}]pair_hdnnp.md){.reference .internal}

- [`examples/PACKAGES/hdnnp`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

:::: {#ml-iap-package .section}
[]{#pkg-ml-iap}

## [8.1.55. ]{.section-number}ML-IAP package[](#ml-iap-package "Link to this heading"){.headerlink}

**Contents:**

A general interface for machine-learning interatomic potentials, including PyTorch.

**Install:**

To use this package, also the [[ML-SNAP]{.std .std-ref}](#pkg-ml-snap){.reference .internal} package needs to be installed. To make the *mliappy* model available, also the [[PYTHON]{.std .std-ref}](#pkg-python){.reference .internal} package needs to be installed, the version of Python must be 3.6 or later, and the [cython](https://cython.org/){.reference .external} software must be installed.

**Author:** Aidan Thompson (Sandia), Nicholas Lubbers (LANL).

::: versionadded
[Added in version 30Jun2020.]{.versionmodified .added}
:::

**Supporting info:**

- [`src/ML-IAP`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/ML-IAP/README.md`{.docutils .literal .notranslate}]{.pre}

- [[pair_style mliap]{.doc}]pair_mliap.md){.reference .internal}

- [[compute_style mliap]{.doc}]compute_mliap.md){.reference .internal}

- [`examples/mliap`{.docutils .literal .notranslate}]{.pre} (see README)

When built with the *mliappy* model this package includes an extension for coupling with Python models, including PyTorch. In this case, the Python interpreter linked to LAMMPS will need the [`cython`{.docutils .literal .notranslate}]{.pre} and [`numpy`{.docutils .literal .notranslate}]{.pre} modules installed. The provided examples build models with PyTorch, which would therefore also needs to be installed to run those examples.

------------------------------------------------------------------------
::::

:::: {#ml-pace-package .section}
[]{#pkg-ml-pace}

## [8.1.56. ]{.section-number}ML-PACE package[](#ml-pace-package "Link to this heading"){.headerlink}

**Contents:**

A pair style for the Atomic Cluster Expansion potential (ACE). ACE is a methodology for deriving a highly accurate classical potential fit to a large archive of quantum mechanical (DFT) data. The ML-PACE package provides an efficient implementation for running simulations with ACE potentials.

**Authors:**

This package was written by Yury Lysogorskiy\^1, Cas van der Oord\^2, Anton Bochkarev\^1, Sarath Menon\^1, Matteo Rinaldi\^1, Thomas Hammerschmidt\^1, Matous Mrovec\^1, Aidan Thompson\^3, Gabor Csanyi\^2, Christoph Ortner\^4, Ralf Drautz\^1.

> ::: {}
> \^1: Ruhr-University Bochum, Bochum, Germany
>
> \^2: University of Cambridge, Cambridge, United Kingdom
>
> \^3: Sandia National Laboratories, Albuquerque, New Mexico, USA
>
> \^4: University of British Columbia, Vancouver, BC, Canada
> :::

::: versionadded
[Added in version 14May2021.]{.versionmodified .added}
:::

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#ml-pace){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page. This package may also be compiled as a plugin to avoid licensing conflicts when distributing binaries.

**Supporting info:**

- [`src/ML-PACE`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[pair_style pace]{.doc}]pair_pace.md){.reference .internal}

- [`examples/PACKAGES/pace`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

:::: {#ml-pod-package .section}
[]{#pkg-ml-pod}

## [8.1.57. ]{.section-number}ML-POD package[](#ml-pod-package "Link to this heading"){.headerlink}

**Contents:**

A pair style and fitpod style for Proper Orthogonal Descriptors (POD). POD is a methodology for deriving descriptors based on the proper orthogonal decomposition. The ML-POD package provides an efficient implementation for running simulations with POD potentials, along with fitting the potentials natively in LAMMPS.

**Authors:**

Ngoc Cuong Nguyen (MIT), Andrew Rohskopf (Sandia)

::: versionadded
[Added in version 22Dec2022.]{.versionmodified .added}
:::

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#ml-pod){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/ML-POD`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[pair_style pod]{.doc}]pair_pod.md){.reference .internal}

- [[command_style fitpod]{.doc}]fitpod_command.md){.reference .internal}

- [`examples/PACKAGES/pod`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

::: {#ml-quip-package .section}
[]{#pkg-ml-quip}

## [8.1.58. ]{.section-number}ML-QUIP package[](#ml-quip-package "Link to this heading"){.headerlink}

**Contents:**

A [[pair_style quip]{.doc}]pair_quip.md){.reference .internal} command which wraps the [QUIP libAtoms library](https://github.com/libAtoms/QUIP){.reference .external}, which includes a variety of interatomic potentials, including Gaussian Approximation Potential (GAP) models developed by the Cambridge University group.

To use this package you must have the QUIP libAtoms library available on your system.

**Author:** Albert Bartok (Cambridge University)

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#ml-quip){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/ML-QUIP`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/ML-QUIP/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style quip]{.doc}]pair_quip.md){.reference .internal}

- [`examples/PACKAGES/quip`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

:::: {#ml-rann-package .section}
[]{#pkg-ml-rann}

## [8.1.59. ]{.section-number}ML-RANN package[](#ml-rann-package "Link to this heading"){.headerlink}

**Contents:**

A pair style for using rapid atomistic neural network (RANN) potentials. These neural network potentials work by first generating a series of symmetry functions from the neighbor list and then using these values as the input layer of a neural network.

**Authors:**

This package was written by Christopher Barrett with contributions by Doyl Dickel, Mississippi State University.

::: versionadded
[Added in version 27May2021.]{.versionmodified .added}
:::

**Supporting info:**

- [`src/ML-RANN`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[pair_style rann]{.doc}]pair_rann.md){.reference .internal}

- [`examples/PACKAGES/rann`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

::: {#ml-snap-package .section}
[]{#pkg-ml-snap}

## [8.1.60. ]{.section-number}ML-SNAP package[](#ml-snap-package "Link to this heading"){.headerlink}

**Contents:**

A pair style for the spectral neighbor analysis potential (SNAP). SNAP is methodology for deriving a highly accurate classical potential fit to a large archive of quantum mechanical (DFT) data. Also several computes which analyze attributes of the potential.

**Author:** Aidan Thompson (Sandia).

**Supporting info:**

- [`src/ML-SNAP`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[pair_style snap]{.doc}]pair_snap.md){.reference .internal}

- [[compute sna/atom]{.doc}]compute_sna_atom.md){.reference .internal}

- [[compute sna/grid]{.doc}]compute_sna_atom.md){.reference .internal}

- [[compute sna/grid/local]{.doc}]compute_sna_atom.md){.reference .internal}

- [[compute snad/atom]{.doc}]compute_sna_atom.md){.reference .internal}

- [[compute snav/atom]{.doc}]compute_sna_atom.md){.reference .internal}

- [`examples/snap`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#ml-uf3-package .section}
[]{#pkg-ml-uf3}

## [8.1.61. ]{.section-number}ML-UF3 package[](#ml-uf3-package "Link to this heading"){.headerlink}

**Contents:**

A pair style for the ultra-fast force field potentials (UF3). UF3 is a methodology for deriving a highly accurate classical potential which is fast to evaluate and is fitted to a large archives of quantum mechanical (DFT) data. The use of b-spline basis set in UF3 enables the rapid evaluation of 2-body and 3-body interactions.

**Authors:** Ajinkya C Hire (University of Florida), Hendrik Krass (University of Constance), Matthias Rupp (Luxembourg Institute of Science and Technology), Richard Hennig (University of Florida)

**Supporting info:**

- [`src/ML-UF3`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[pair_style uf3]{.doc}]pair_uf3.md){.reference .internal}

- [`examples/uf3`{.docutils .literal .notranslate}]{.pre}

- [https://github.com/uf3/uf3](https://github.com/uf3/uf3){.reference .external}
:::

::: {#mofff-package .section}
[]{#pkg-mofff}

## [8.1.62. ]{.section-number}MOFFF package[](#mofff-package "Link to this heading"){.headerlink}

**Contents:**

Pair, angle and improper styles needed to employ the MOF-FF force field by Schmid and coworkers with LAMMPS. MOF-FF is a first principles derived force field with the primary aim to simulate MOFs and related porous framework materials, using spherical Gaussian charges. It is described in S. Bureekaew et al., Phys. Stat. Sol. B 2013, 250, 1128-1141. For the usage of MOF-FF see the example in the example directory as well as the [MOF+](https://www.mofplus.org/content/show/MOF-FF){.reference .external} website.

**Author:** Hendrik Heenen (Technical U of Munich), Rochus Schmid (Ruhr-University Bochum).

**Supporting info:**

- [`src/MOFFF`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/MOFFF/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style buck6d/coul/gauss]{.doc}]pair_buck6d_coul_gauss.md){.reference .internal}

- [[angle_style class2]{.doc}]angle_class2.md){.reference .internal}

- [[angle_style cosine/buck6d]{.doc}]angle_cosine_buck6d.md){.reference .internal}

- [[improper_style inversion/harmonic]{.doc}]improper_inversion_harmonic.md){.reference .internal}

- [`examples/PACKAGES/mofff`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#molecule-package .section}
[]{#pkg-molecule}

## [8.1.63. ]{.section-number}MOLECULE package[](#molecule-package "Link to this heading"){.headerlink}

**Contents:**

A large number of atom, pair, bond, angle, dihedral, improper styles that are used to model molecular systems with fixed covalent bonds. The pair styles include the Dreiding (hydrogen-bonding) and CHARMM force fields, and a TIP4P water model.

**Supporting info:**

- [`src/MOLECULE`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[atom_style]{.doc}]atom_style.md){.reference .internal}

- [[bond_style]{.doc}]bond_style.md){.reference .internal}

- [[angle_style]{.doc}]angle_style.md){.reference .internal}

- [[dihedral_style]{.doc}]dihedral_style.md){.reference .internal}

- [[improper_style]{.doc}]improper_style.md){.reference .internal}

- [[pair_style hbond/dreiding/lj]{.doc}]pair_hbond_dreiding.md){.reference .internal}

- [[pair_style lj/charmm/coul/charmm]{.doc}]pair_charmm.md){.reference .internal}

- [[Howto bioFF]{.doc}]Howto_bioFF.md){.reference .internal}

- [`examples/cmap`{.docutils .literal .notranslate}]{.pre}

- [`examples/dreiding`{.docutils .literal .notranslate}]{.pre}

- [`examples/micelle,`{.docutils .literal .notranslate}]{.pre}

- [`examples/peptide`{.docutils .literal .notranslate}]{.pre}

- bench/in.chain

- bench/in.rhodo

------------------------------------------------------------------------
:::

::: {#molfile-package .section}
[]{#pkg-molfile}

## [8.1.64. ]{.section-number}MOLFILE package[](#molfile-package "Link to this heading"){.headerlink}

**Contents:**

A [[dump molfile]{.doc}]dump_molfile.md){.reference .internal} command which uses molfile plugins that are bundled with the [VMD](https://www.ks.uiuc.edu/Research/vmd/){.reference .external} molecular visualization and analysis program, to enable LAMMPS to dump snapshots in formats compatible with various molecular simulation tools.

To use this package you must have the desired VMD plugins available on your system.

Note that this package only provides the interface code, not the plugins themselves, which will be accessed when requesting a specific plugin via the [[dump molfile]{.doc}]dump_molfile.md){.reference .internal} command. Plugins can be obtained from a VMD installation which has to match the platform that you are using to compile LAMMPS for. By adding plugins to VMD, support for new file formats can be added to LAMMPS (or VMD or other programs that use them) without having to re-compile the application itself. More information about the VMD molfile plugins can be found at [https://www.ks.uiuc.edu/Research/vmd/plugins/molfile](https://www.ks.uiuc.edu/Research/vmd/plugins/molfile/){.reference .external}.

**Author:** Axel Kohlmeyer (Temple U).

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#molfile){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/MOLFILE`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/MOLFILE/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/molfile/README`{.docutils .literal .notranslate}]{.pre}

- [[dump molfile]{.doc}]dump_molfile.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#netcdf-package .section}
[]{#pkg-netcdf}

## [8.1.65. ]{.section-number}NETCDF package[](#netcdf-package "Link to this heading"){.headerlink}

**Contents:**

Dump styles for writing NetCDF formatted dump files. NetCDF is a portable, binary, self-describing file format developed on top of HDF5. The file contents follow the AMBER NetCDF trajectory conventions ([https://ambermd.org/netcdf/nctraj.xhtml](https://ambermd.org/netcdf/nctraj.xhtml){.reference .external}), but include extensions.

To use this package you must have the NetCDF library available on your system.

Note that NetCDF files can be directly visualized with the following tools:

- [Ovito](https://www.ovito.org){.reference .external} (Ovito supports the AMBER convention and the extensions mentioned above)

- [VMD](https://www.ks.uiuc.edu/Research/vmd/){.reference .external}

**Author:** Lars Pastewka (Karlsruhe Institute of Technology).

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#netcdf){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/NETCDF`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/NETCDF/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/netcdf/README`{.docutils .literal .notranslate}]{.pre}

- [[dump netcdf]{.doc}]dump_netcdf.md){.reference .internal}

------------------------------------------------------------------------
:::

:::: {#openmp-package .section}
[]{#pkg-openmp}

## [8.1.66. ]{.section-number}OPENMP package[](#openmp-package "Link to this heading"){.headerlink}

**Contents:**

Hundreds of pair, fix, compute, bond, angle, dihedral, improper, and kspace styles which are altered to enable threading on many-core CPUs via OpenMP directives. All of them have an "omp" in their style name. The [[OPENMP package]{.doc}]Speed_omp.md){.reference .internal} page gives details of what hardware and compilers are required on your system, and how to build and use this package. Its styles can be invoked at run time via the [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`omp`{.docutils .literal .notranslate}]{.pre} or [`-suffix`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`omp`{.docutils .literal .notranslate}]{.pre} [[command-line switches]{.doc}]Run_options.md){.reference .internal}. Also see the [[KOKKOS]{.std .std-ref}](#pkg-kokkos){.reference .internal}, [[OPT]{.std .std-ref}](#pkg-opt){.reference .internal}, and [[INTEL]{.std .std-ref}](#pkg-intel){.reference .internal} packages, which have styles optimized for CPUs.

**Author:** Axel Kohlmeyer (Temple U).

::: {.admonition .note}
Note

To enable multi-threading support the compile flag [`-fopenmp`{.docutils .literal .notranslate}]{.pre} and the link flag [`-fopenmp`{.docutils .literal .notranslate}]{.pre} (for GNU compilers, you have to look up the equivalent flags for other compilers) must be used to build LAMMPS. When using Intel compilers, also the [`-restrict`{.docutils .literal .notranslate}]{.pre} flag is required. The OPENMP package can be compiled without enabling OpenMP; then all code will be compiled as serial and the only improvement over the regular styles are some data access optimization. These flags should be added to the CCFLAGS and LINKFLAGS lines of your Makefile.machine. See [`src/MAKE/OPTIONS/Makefile`{.docutils .literal .notranslate}]{.pre}.omp for an example.
:::

Once you have an appropriate Makefile.machine, you can install/uninstall the package and build LAMMPS in the usual manner:

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#openmp){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/OPENMP`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/OPENMP/README`{.docutils .literal .notranslate}]{.pre}

- [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal}

- [[OPENMP package]{.doc}]Speed_omp.md){.reference .internal}

- [[Command-line option -suffix/-sf omp]{.doc}]Run_options.md){.reference .internal}

- [[Command-line option -package/-pk omp]{.doc}]Run_options.md){.reference .internal}

- [[package omp]{.doc}]package.md){.reference .internal}

- Search the [[commands]{.doc}]Commands_all.md){.reference .internal} pages ([[fix]{.doc}]Commands_fix.md){.reference .internal}, [[compute]{.doc}]Commands_compute.md){.reference .internal}, [[pair]{.doc}]Commands_pair.md){.reference .internal}, [[bond, angle, dihedral, improper]{.doc}]Commands_bond.md){.reference .internal}, [[kspace]{.doc}]Commands_kspace.md){.reference .internal}) for styles followed by (o)

- [Benchmarks page](https://www.lammps.org/bench.html){.reference .external} of website

------------------------------------------------------------------------
::::

::: {#opt-package .section}
[]{#pkg-opt}

## [8.1.67. ]{.section-number}OPT package[](#opt-package "Link to this heading"){.headerlink}

**Contents:**

A handful of pair styles which are optimized for improved CPU performance on single or multiple cores. These include EAM, LJ, CHARMM, and Morse potentials. The styles have an "opt" suffix in their style name. The [[OPT package]{.doc}]Speed_opt.md){.reference .internal} page gives details of how to build and use this package. Its styles can be invoked at run time via the [`-sf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`opt`{.docutils .literal .notranslate}]{.pre} or [`-suffix`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`opt`{.docutils .literal .notranslate}]{.pre} [[command-line switches]{.doc}]Run_options.md){.reference .internal}. See also the [[KOKKOS]{.std .std-ref}](#pkg-kokkos){.reference .internal}, [[INTEL]{.std .std-ref}](#pkg-intel){.reference .internal}, and [[OPENMP]{.std .std-ref}](#pkg-openmp){.reference .internal} packages, which have styles optimized for CPU performance.

**Authors:** James Fischer (High Performance Technologies), David Richie, and Vincent Natoli (Stone Ridge Technology).

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#opt){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/OPT`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal}

- [[OPT package]{.doc}]Speed_opt.md){.reference .internal}

- [[Section 4.2 -sf opt]{.doc}]Run_options.md){.reference .internal}

- Search the [[pair style]{.doc}]Commands_pair.md){.reference .internal} page for styles followed by (t)

- [Benchmarks page](https://www.lammps.org/bench.html){.reference .external} of website
:::

::: {#orient-package .section}
[]{#pkg-orient}

## [8.1.68. ]{.section-number}ORIENT package[](#orient-package "Link to this heading"){.headerlink}

**Contents:**

A few fixes that apply orientation dependent forces for studying grain boundary migration.

**Supporting info:**

- [`src/ORIENT`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[fix orient/bcc]{.doc}]fix_orient.md){.reference .internal}

- [[fix orient/fcc]{.doc}]fix_orient.md){.reference .internal}

- [[fix orient/eco]{.doc}]fix_orient_eco.md){.reference .internal}

------------------------------------------------------------------------
:::

::: {#peri-package .section}
[]{#pkg-peri}

## [8.1.69. ]{.section-number}PERI package[](#peri-package "Link to this heading"){.headerlink}

**Contents:**

An atom style, several pair styles which implement different Peridynamics materials models, and several computes which calculate diagnostics. Peridynamics is a particle-based meshless continuum model.

**Authors:** The original package was created by Mike Parks (Sandia). Additional Peridynamics models were added by Rezwanur Rahman and John Foster (UTSA).

**Supporting info:**

- [`src/PERI`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Peridynamics Howto]{.doc}]Howto_peri.md){.reference .internal}

- [doc/PDF/PDLammps_overview.pdf](PDF/PDLammps_overview.pdf){.reference .external}

- [doc/PDF/PDLammps_EPS.pdf](PDF/PDLammps_EPS.pdf){.reference .external}

- [doc/PDF/PDLammps_VES.pdf](PDF/PDLammps_VES.pdf){.reference .external}

- [[atom_style peri]{.doc}]atom_style.md){.reference .internal}

- [[pair_style peri/\*]{.doc}]pair_peri.md){.reference .internal}

- [[compute damage/atom]{.doc}]compute_damage_atom.md){.reference .internal}

- [[compute plasticity/atom]{.doc}]compute_plasticity_atom.md){.reference .internal}

- [`examples/peri`{.docutils .literal .notranslate}]{.pre}

- [https://www.lammps.org/movies.html#impact](https://www.lammps.org/movies.html#impact){.reference .external}

------------------------------------------------------------------------
:::

::: {#phonon-package .section}
[]{#pkg-phonon}

## [8.1.70. ]{.section-number}PHONON package[](#phonon-package "Link to this heading"){.headerlink}

**Contents:**

A [[fix phonon]{.doc}]fix_phonon.md){.reference .internal} command that calculates dynamical matrices, which can then be used to compute phonon dispersion relations, directly from molecular dynamics simulations. And a [[dynamical_matrix]{.doc}]dynamical_matrix.md){.reference .internal} as well as a [[third_order]{.doc}]third_order.md){.reference .internal} command to compute the dynamical matrix and third order tensor from finite differences.

**Install:**

The fix phonon command also requires that the [[KSPACE]{.std .std-ref}](#pkg-kspace){.reference .internal} package is installed.

**Authors:** Ling-Ti Kong (Shanghai Jiao Tong University) for "fix phonon" and Charlie Sievers (UC Davis) for "dynamical_matrix" and "third_order"

**Supporting info:**

- [`src/PHONON`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/PHONON/README`{.docutils .literal .notranslate}]{.pre}

- [[fix phonon]{.doc}]fix_phonon.md){.reference .internal}

- [[dynamical_matrix]{.doc}]dynamical_matrix.md){.reference .internal}

- [[third_order]{.doc}]third_order.md){.reference .internal}

- [`examples/PACKAGES/phonon`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

:::: {#plugin-package .section}
[]{#pkg-plugin}

## [8.1.71. ]{.section-number}PLUGIN package[](#plugin-package "Link to this heading"){.headerlink}

**Contents:**

A [[plugin]{.doc}]plugin.md){.reference .internal} command that can load and unload several kind of styles in LAMMPS from shared object files at runtime without having to recompile and relink LAMMPS.

When the environment variable [`LAMMPS_PLUGIN_PATH`{.docutils .literal .notranslate}]{.pre} is set, then LAMMPS will search the directory (or directories) listed in this path for files with names that end in [`plugin.so`{.docutils .literal .notranslate}]{.pre} (e.g. [`helloplugin.so`{.docutils .literal .notranslate}]{.pre}) and will try to load the contained plugins automatically at start-up.

**Authors:** Axel Kohlmeyer (Temple U)

::: versionadded
[Added in version 8Apr2021.]{.versionmodified .added}
:::

**Supporting info:**

- [`src/PLUGIN`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[plugin command]{.doc}]plugin.md){.reference .internal}

- [[Information on writing plugins]{.doc}]Developer_plugins.md){.reference .internal}

- [`examples/plugin`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

::: {#plumed-package .section}
[]{#pkg-plumed}

## [8.1.72. ]{.section-number}PLUMED package[](#plumed-package "Link to this heading"){.headerlink}

**Contents:**

The fix plumed command allows you to use the PLUMED free energy plugin for molecular dynamics to analyze and bias your LAMMPS trajectory on the fly. The PLUMED library is called from within the LAMMPS input script by using the [[fix plumed]{.doc}]fix_plumed.md){.reference .internal} command.

**Authors:** The [PLUMED library](https://www.plumed.org){.reference .external} is written and maintained by Massimilliano Bonomi, Giovanni Bussi, Carlo Camiloni, and Gareth Tribello.

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#plumed){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page. This package may also be compiled as a plugin to avoid licensing conflicts when distributing binaries.

**Supporting info:**

- [`src/PLUMED/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/plumed/README`{.docutils .literal .notranslate}]{.pre}

- [[fix plumed]{.doc}]fix_plumed.md){.reference .internal}

- [`examples/PACKAGES/plumed`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#ptm-package .section}
[]{#pkg-ptm}

## [8.1.73. ]{.section-number}PTM package[](#ptm-package "Link to this heading"){.headerlink}

**Contents:**

A [[compute ptm/atom]{.doc}]compute_ptm_atom.md){.reference .internal} command that calculates local structure characterization using the Polyhedral Template Matching methodology.

**Author:** Peter Mahler Larsen (MIT).

**Supporting info:**

- [`src/PTM`{.docutils .literal .notranslate}]{.pre}: filenames not starting with ptm\_ -\> commands

- [`src/PTM`{.docutils .literal .notranslate}]{.pre}: filenames starting with ptm\_ -\> supporting code

- [`src/PTM/LICENSE`{.docutils .literal .notranslate}]{.pre}

- [[compute ptm/atom]{.doc}]compute_ptm_atom.md){.reference .internal}

------------------------------------------------------------------------
:::

:::: {#python-package .section}
[]{#pkg-python}

## [8.1.74. ]{.section-number}PYTHON package[](#python-package "Link to this heading"){.headerlink}

**Contents:**

A [[python]{.doc}]python.md){.reference .internal} command which allow you to execute Python code from a LAMMPS input script. The code can be in a separate file or embedded in the input script itself. See the [[Python call]{.doc}]Python_call.md){.reference .internal} page for an overview of using Python from LAMMPS in this manner and all the [[Python]{.doc}]Python_head.md){.reference .internal} manual pages for other ways to use LAMMPS and Python together.

::: {.admonition .note}
Note

Building with the PYTHON package assumes you have a Python development environment (headers and libraries) available on your system, which needs to be Python version 3.6 or later.
:::

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#python){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/PYTHON`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Python call]{.doc}]Python_head.md){.reference .internal}

- [`lib/python/README`{.docutils .literal .notranslate}]{.pre}

- [`examples/python`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

::: {#qeq-package .section}
[]{#pkg-qeq}

## [8.1.75. ]{.section-number}QEQ package[](#qeq-package "Link to this heading"){.headerlink}

**Contents:**

Several fixes for performing charge equilibration (QEq) via different algorithms. These can be used with pair styles that perform QEq as part of their formulation.

**Supporting info:**

- [`src/QEQ`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[fix qeq/\*]{.doc}]fix_qeq.md){.reference .internal}

- [`examples/qeq`{.docutils .literal .notranslate}]{.pre}

- [`examples/streitz`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#qmmm-package .section}
[]{#pkg-qmmm}

## [8.1.76. ]{.section-number}QMMM package[](#qmmm-package "Link to this heading"){.headerlink}

**Contents:**

A [[fix qmmm]{.doc}]fix_qmmm.md){.reference .internal} command which allows LAMMPS to be used as the MM code in a QM/MM simulation. This is currently only available in combination with the [Quantum ESPRESSO](https://www.quantum-espresso.org){.reference .external} package.

To use this package you must have Quantum ESPRESSO (QE) available on your system and include its coupling library in the compilation and then compile LAMMPS as a library. For QM/MM calculations you then build a custom binary with MPI support, that sets up 3 partitions with MPI sub-communicators (for inter- and intra-partition communication) and then calls the corresponding library interfaces on each partition (2x LAMMPS and 1x QE).

The current implementation supports an ONIOM style mechanical coupling and a multi-pole based electrostatic coupling to the Quantum ESPRESSO plane wave DFT package. The QM/MM interface has been written in a manner that coupling to other QM codes should be possible without changes to LAMMPS itself.

**Authors:** Axel Kohlmeyer (Temple U). Mariella Ippolito and Carlo Cavazzoni (CINECA, Italy)

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#qmmm){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/QMMM`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/QMMM/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/qmmm/README`{.docutils .literal .notranslate}]{.pre}

- [[fix phonon]{.doc}]fix_phonon.md){.reference .internal}

- [`lib/qmmm/example-ec/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/qmmm/example-mc/README`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#qtb-package .section}
[]{#pkg-qtb}

## [8.1.77. ]{.section-number}QTB package[](#qtb-package "Link to this heading"){.headerlink}

**Contents:**

Two fixes which provide a self-consistent quantum treatment of vibrational modes in a classical molecular dynamics simulation. By coupling the MD simulation to a colored thermostat, it introduces zero point energy into the system, altering the energy power spectrum and the heat capacity to account for their quantum nature. This is useful when modeling systems at temperatures lower than their classical limits or when temperatures ramp across the classical limits in a simulation.

**Author:** Yuan Shen (Stanford U).

**Supporting info:**

- [`src/QTB`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/QTB/README`{.docutils .literal .notranslate}]{.pre}

- [[fix qtb]{.doc}]fix_qtb.md){.reference .internal}

- [[fix qbmsst]{.doc}]fix_qbmsst.md){.reference .internal}

- [`examples/PACKAGES/qtb`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#reaction-package .section}
[]{#pkg-reaction}

## [8.1.78. ]{.section-number}REACTION package[](#reaction-package "Link to this heading"){.headerlink}

**Contents:**

This package implements the REACTER protocol, which allows for complex bond topology changes (reactions) during a running MD simulation when using classical force fields. Topology changes are defined in pre- and post-reaction molecule templates and can include creation and deletion of bonds, angles, dihedrals, impropers, atom types, bond types, angle types, dihedral types, improper types, and/or atomic charges. Other options currently available include reaction constraints (e.g., angle and Arrhenius constraints), deletion of reaction byproducts or other small molecules, creation of new atoms or molecules bonded to existing atoms, and using LAMMPS variables for input parameters.

**Author:** Jacob R. Gissinger (NASA Langley Research Center).

**Supporting info:**

- [`src/REACTION`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/REACTION/README`{.docutils .literal .notranslate}]{.pre}

- [[fix bond/react]{.doc}]fix_bond_react.md){.reference .internal}

- [`examples/PACKAGES/reaction`{.docutils .literal .notranslate}]{.pre}

- [2017 LAMMPS Workshop](https://www.lammps.org/workshops/Aug17/pdf/gissinger.pdf){.reference .external}

- [2019 LAMMPS Workshop](https://www.lammps.org/workshops/Aug19/talk_gissinger.pdf){.reference .external}

- [2021 LAMMPS Workshop](https://www.lammps.org/workshops/Aug21/talk/jacob-gissinger/){.reference .external}

- [REACTER website (reacter.org)](https://www.reacter.org/){.reference .external}

------------------------------------------------------------------------
:::

::: {#reaxff-package .section}
[]{#pkg-reaxff}

## [8.1.79. ]{.section-number}REAXFF package[](#reaxff-package "Link to this heading"){.headerlink}

**Contents:**

A pair style which implements the ReaxFF potential in C/C++. ReaxFF is a universal reactive force field. See the [`src/REAXFF/README`{.docutils .literal .notranslate}]{.pre} file for more info on differences between the two packages. Also two fixes for monitoring molecules as bonds are created and destroyed.

**Author:** Hasan Metin Aktulga (MSU) while at Purdue University.

**Supporting info:**

- [`src/REAXFF`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/REAXFF/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style reaxff]{.doc}]pair_reaxff.md){.reference .internal}

- [[fix reaxff/bonds]{.doc}]fix_reaxff_bonds.md){.reference .internal}

- [[fix reaxff/species]{.doc}]fix_reaxff_species.md){.reference .internal}

- [`examples/reaxff`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#replica-package .section}
[]{#pkg-replica}

## [8.1.80. ]{.section-number}REPLICA package[](#replica-package "Link to this heading"){.headerlink}

**Contents:**

A collection of multi-replica methods which can be used when running multiple LAMMPS simulations (replicas). See the [[Howto replica]{.doc}]Howto_replica.md){.reference .internal} page for an overview of how to run multi-replica simulations in LAMMPS. Methods in the package include nudged elastic band (NEB), parallel replica dynamics (PRD), temperature accelerated dynamics (TAD), parallel tempering, and a verlet/split algorithm for performing long-range Coulombics on one set of processors, and the remainder of the force field calculation on another set.

**Supporting info:**

- [`src/REPLICA`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Howto replica]{.doc}]Howto_replica.md){.reference .internal}

- [[neb]{.doc}]neb.md){.reference .internal}

- [[prd]{.doc}]prd.md){.reference .internal}

- [[tad]{.doc}]tad.md){.reference .internal}

- [[temper]{.doc}]temper.md){.reference .internal},

- [[temper/npt]{.doc}]temper_npt.md){.reference .internal},

- [[temper/grem]{.doc}]temper_grem.md){.reference .internal},

- [[run_style verlet/split]{.doc}]run_style.md){.reference .internal}

- [`examples/neb`{.docutils .literal .notranslate}]{.pre}

- [`examples/prd`{.docutils .literal .notranslate}]{.pre}

- [`examples/tad`{.docutils .literal .notranslate}]{.pre}

- [`examples/PACKAGES/grem`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

:::: {#rheo-package .section}
[]{#pkg-rheo}

## [8.1.81. ]{.section-number}RHEO package[](#rheo-package "Link to this heading"){.headerlink}

**Contents:**

Pair styles, bond styles, fixes, and computes for reproducing hydrodynamics and elastic objects. See the [[Howto rheo]{.doc}]Howto_rheo.md){.reference .internal} page for an overview.

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#rheo){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Authors:** Joel T. Clemmer (Sandia National Labs), Thomas C. O'Connor (Carnegie Mellon University)

::: versionadded
[Added in version 29Aug2024.]{.versionmodified .added}
:::

**Supporting info:**

- [`src/RHEO`{.docutils .literal .notranslate}]{.pre} filenames -\> commands

- [[Howto_rheo]{.doc}]Howto_rheo.md){.reference .internal}

- [[atom_style rheo]{.doc}]atom_style.md){.reference .internal}

- [[atom_style rheo/thermal]{.doc}]atom_style.md){.reference .internal}

- [[bond_style rheo/shell]{.doc}]bond_rheo_shell.md){.reference .internal}

- [[compute rheo/property/atom]{.doc}]compute_rheo_property_atom.md){.reference .internal}

- [[fix rheo]{.doc}]fix_rheo.md){.reference .internal}

- [[fix rheo/oxidation]{.doc}]fix_rheo_oxidation.md){.reference .internal}

- [[fix rheo/pressure]{.doc}]fix_rheo_pressure.md){.reference .internal}

- [[fix rheo/thermal]{.doc}]fix_rheo_thermal.md){.reference .internal}

- [[fix rheo/viscosity]{.doc}]fix_rheo_viscosity.md){.reference .internal}

- [[pair_style rheo]{.doc}]pair_rheo.md){.reference .internal}

- [[pair_style rheo/solid]{.doc}]pair_rheo_solid.md){.reference .internal}

- [https://www.lammps.org/movies.html#rheopackage](https://www.lammps.org/movies.html#rheopackage){.reference .external}

- [`examples/rheo`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
::::

::: {#rigid-package .section}
[]{#pkg-rigid}

## [8.1.82. ]{.section-number}RIGID package[](#rigid-package "Link to this heading"){.headerlink}

**Contents:**

Fixes which enforce rigid constraints on collections of atoms or particles. This includes SHAKE and RATTLE, as well as various rigid-body integrators for a few large bodies or many small bodies. Also several computes which calculate properties of rigid bodies.

**Supporting info:**

- [`src/RIGID`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[compute erotate/rigid]{.doc}]compute_erotate_rigid.md){.reference .internal}

- [[fix shake]{.doc}]fix_shake.md){.reference .internal}

- [[fix rattle]{.doc}]fix_shake.md){.reference .internal}

- [[fix rigid/\*]{.doc}]fix_rigid.md){.reference .internal}

- [`examples/ASPHERE`{.docutils .literal .notranslate}]{.pre}

- [`examples/rigid`{.docutils .literal .notranslate}]{.pre}

- bench/in.rhodo

- [https://www.lammps.org/movies.html#box](https://www.lammps.org/movies.html#box){.reference .external}

- [https://www.lammps.org/movies.html#star](https://www.lammps.org/movies.html#star){.reference .external}

------------------------------------------------------------------------
:::

::: {#scafacos-package .section}
[]{#pkg-scafacos}

## [8.1.83. ]{.section-number}SCAFACOS package[](#scafacos-package "Link to this heading"){.headerlink}

**Contents:**

A KSpace style which wraps the [ScaFaCoS Coulomb solver library](http://www.scafacos.de/){.reference .external} to compute long-range Coulombic interactions.

To use this package you must have the ScaFaCoS library available on your system.

**Author:** Rene Halver (JSC) wrote the scafacos LAMMPS command.

ScaFaCoS itself was developed by a consortium of German research facilities with a BMBF (German Ministry of Science and Education) funded project in 2009-2012. Participants of the consortium were the Universities of Bonn, Chemnitz, Stuttgart, and Wuppertal as well as the Forschungszentrum Juelich.

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#scafacos){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page. The SCAFACOS package requires that LAMMPS is built in [[MPI parallel mode]{.std .std-ref}]Build_basics.md#serial){.reference .internal}.

**Supporting info:**

- [`src/SCAFACOS`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/SCAFACOS/README`{.docutils .literal .notranslate}]{.pre}

- [[kspace_style scafacos]{.doc}]kspace_style.md){.reference .internal}

- [[kspace_modify]{.doc}]kspace_modify.md){.reference .internal}

- [`examples/PACKAGES/scafacos`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#shock-package .section}
[]{#pkg-shock}

## [8.1.84. ]{.section-number}SHOCK package[](#shock-package "Link to this heading"){.headerlink}

**Contents:**

Fixes for running impact simulations where a shock-wave passes through a material.

**Supporting info:**

- [`src/SHOCK`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[fix append/atoms]{.doc}]fix_append_atoms.md){.reference .internal}

- [[fix msst]{.doc}]fix_msst.md){.reference .internal}

- [[fix nphug]{.doc}]fix_nphug.md){.reference .internal}

- [[fix wall/piston]{.doc}]fix_wall_piston.md){.reference .internal}

- [`examples/hugoniostat`{.docutils .literal .notranslate}]{.pre}

- [`examples/msst`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#smtbq-package .section}
[]{#pkg-smtbq}

## [8.1.85. ]{.section-number}SMTBQ package[](#smtbq-package "Link to this heading"){.headerlink}

**Contents:**

Pair styles which implement Second Moment Tight Binding models. One with QEq charge equilibration (SMTBQ) for the description of ionocovalent bonds in oxides, and two more as plain SMATB models.

**Authors:** SMTBQ: Nicolas Salles, Emile Maras, Olivier Politano, and Robert Tetot (LAAS-CNRS, France); SMATB: Daniele Rapetti (Politecnico di Torino)

**Supporting info:**

- [`src/SMTBQ`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/SMTBQ/README`{.docutils .literal .notranslate}]{.pre}

- [[pair_style smtbq]{.doc}]pair_smtbq.md){.reference .internal}

- [[pair_style smatb]{.doc}]pair_smatb.md){.reference .internal}, [[pair_style smatb/single]{.doc}]pair_smatb.md){.reference .internal}

- [`examples/PACKAGES/smtbq`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::::: {#sph-package .section}
[]{#pkg-sph}

## [8.1.86. ]{.section-number}SPH package[](#sph-package "Link to this heading"){.headerlink}

**Contents:**

An atom style, fixes, computes, and several pair styles which implements smoothed particle hydrodynamics (SPH) for liquids. See the related [[MACHDYN package]{.std .std-ref}](#pkg-machdyn){.reference .internal} package for smooth Mach dynamics (SMD) for solids.

This package contains ideal gas, Lennard-Jones equation of states, Tait, and full support for complete (i.e. internal-energy dependent) equations of state. It allows for plain or Monaghans XSPH integration of the equations of motion. It has options for density continuity or density summation to propagate the density field. It has [[set]{.doc}]set.md){.reference .internal} command options to set the internal energy and density of particles from the input script and allows the same quantities to be output with thermodynamic output or to dump files via the [[compute property/atom]{.doc}]compute_property_atom.md){.reference .internal} command.

**Author:** Georg Ganzenmuller (Fraunhofer-Institute for High-Speed Dynamics, Ernst Mach Institute, Germany).

**Supporting info:**

- [`src/SPH`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/SPH/README`{.docutils .literal .notranslate}]{.pre}

- [doc/PDF/SPH_LAMMPS_userguide.pdf](PDF/SPH_LAMMPS_userguide.pdf){.reference .external}

- [`examples/PACKAGES/sph`{.docutils .literal .notranslate}]{.pre}

- [https://www.lammps.org/movies.html#sph](https://www.lammps.org/movies.html#sph){.reference .external}

::: {.admonition .note}
Note

Please note that the SPH PDF guide file has not been updated for many years and thus does not reflect the current *syntax* of the SPH package commands. For that please refer to the LAMMPS manual.
:::

::: {.admonition .note}
Note

Please also note, that the [[RHEO package]{.std .std-ref}](#pkg-rheo){.reference .internal} offers similar functionality in a more modern and flexible implementation.
:::

------------------------------------------------------------------------
:::::

::: {#spin-package .section}
[]{#pkg-spin}

## [8.1.87. ]{.section-number}SPIN package[](#spin-package "Link to this heading"){.headerlink}

**Contents:**

Model atomic magnetic spins classically, coupled to atoms moving in the usual manner via MD. Various pair, fix, and compute styles.

**Author:** Julien Tranchida (Sandia).

**Supporting info:**

- [`src/SPIN`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[Howto spins]{.doc}]Howto_spins.md){.reference .internal}

- [[pair_style spin/dipole/cut]{.doc}]pair_spin_dipole.md){.reference .internal}

- [[pair_style spin/dipole/long]{.doc}]pair_spin_dipole.md){.reference .internal}

- [[pair_style spin/dmi]{.doc}]pair_spin_dmi.md){.reference .internal}

- [[pair_style spin/exchange]{.doc}]pair_spin_exchange.md){.reference .internal}

- [[pair_style spin/exchange/biquadratic]{.doc}]pair_spin_exchange.md){.reference .internal}

- [[pair_style spin/magelec]{.doc}]pair_spin_magelec.md){.reference .internal}

- [[pair_style spin/neel]{.doc}]pair_spin_neel.md){.reference .internal}

- [[fix nve/spin]{.doc}]fix_nve_spin.md){.reference .internal}

- [[fix langevin/spin]{.doc}]fix_langevin_spin.md){.reference .internal}

- [[fix precession/spin]{.doc}]fix_precession_spin.md){.reference .internal}

- [[compute spin]{.doc}]compute_spin.md){.reference .internal}

- [[neb/spin]{.doc}]neb_spin.md){.reference .internal}

- [`examples/SPIN`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#srd-package .section}
[]{#pkg-srd}

## [8.1.88. ]{.section-number}SRD package[](#srd-package "Link to this heading"){.headerlink}

**Contents:**

A pair of fixes which implement the Stochastic Rotation Dynamics (SRD) method for coarse-graining of a solvent, typically around large colloidal particles.

**Supporting info:**

- [`src/SRD`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [[fix srd]{.doc}]fix_srd.md){.reference .internal}

- [[fix wall/srd]{.doc}]fix_wall_srd.md){.reference .internal}

- [`examples/srd`{.docutils .literal .notranslate}]{.pre}

- [`examples/ASPHERE`{.docutils .literal .notranslate}]{.pre}

- [https://www.lammps.org/movies.html#tri](https://www.lammps.org/movies.html#tri){.reference .external}

- [https://www.lammps.org/movies.html#line](https://www.lammps.org/movies.html#line){.reference .external}

- [https://www.lammps.org/movies.html#poly](https://www.lammps.org/movies.html#poly){.reference .external}

------------------------------------------------------------------------
:::

::: {#tally-package .section}
[]{#pkg-tally}

## [8.1.89. ]{.section-number}TALLY package[](#tally-package "Link to this heading"){.headerlink}

**Contents:**

Several compute styles that can be called when pairwise interactions are calculated to tally information (forces, heat flux, energy, stress, etc) about individual interactions.

**Author:** Axel Kohlmeyer (Temple U).

**Supporting info:**

- [`src/TALLY`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/TALLY/README`{.docutils .literal .notranslate}]{.pre}

- [[compute \*/tally]{.doc}]compute_tally.md){.reference .internal}

- [`examples/PACKAGES/tally`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#uef-package .section}
[]{#pkg-uef}

## [8.1.90. ]{.section-number}UEF package[](#uef-package "Link to this heading"){.headerlink}

**Contents:**

A fix style for the integration of the equations of motion under extensional flow with proper boundary conditions, as well as several supporting compute styles and an output option.

**Author:** David Nicholson (MIT).

**Supporting info:**

- [`src/UEF`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/UEF/README`{.docutils .literal .notranslate}]{.pre}

- [[fix nvt/uef]{.doc}]fix_nh_uef.md){.reference .internal}

- [[fix npt/uef]{.doc}]fix_nh_uef.md){.reference .internal}

- [[compute pressure/uef]{.doc}]compute_pressure_uef.md){.reference .internal}

- [[compute temp/uef]{.doc}]compute_temp_uef.md){.reference .internal}

- [[dump cfg/uef]{.doc}]dump_cfg_uef.md){.reference .internal}

- [`examples/uef`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#voronoi-package .section}
[]{#pkg-voronoi}

## [8.1.91. ]{.section-number}VORONOI package[](#voronoi-package "Link to this heading"){.headerlink}

**Contents:**

A compute command which calculates the Voronoi tesselation of a collection of atoms by wrapping the [Voro++ library](https://math.lbl.gov/voro++/){.reference .external}. This can be used to calculate the local volume of atoms or their near neighbors.

To use this package you must have the Voro++ library available on your system.

**Author:** Daniel Schwen (INL) while at LANL. The open-source Voro++ library was written by Chris Rycroft (Harvard U) while at UC Berkeley and LBNL.

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#voronoi){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/VORONOI`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/VORONOI/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/voronoi/README`{.docutils .literal .notranslate}]{.pre}

- [[compute voronoi/atom]{.doc}]compute_voronoi_atom.md){.reference .internal}

- [`examples/voronoi`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------
:::

::: {#vtk-package .section}
[]{#pkg-vtk}

## [8.1.92. ]{.section-number}VTK package[](#vtk-package "Link to this heading"){.headerlink}

**Contents:**

A [[dump vtk]{.doc}]dump_vtk.md){.reference .internal} command which outputs snapshot info in the [VTK format](https://vtk.org){.reference .external}, enabling visualization by [Paraview](https://www.paraview.org){.reference .external} or other visualization packages.

To use this package you must have VTK library available on your system.

**Authors:** Richard Berger (JKU) and Daniel Queteschiner (DCS Computing).

**Install:**

This package has [[specific installation instructions]{.std .std-ref}]Build_extras.md#vtk){.reference .internal} on the [[Build extras]{.doc}]Build_extras.md){.reference .internal} page.

**Supporting info:**

- [`src/VTK`{.docutils .literal .notranslate}]{.pre}: filenames -\> commands

- [`src/VTK/README`{.docutils .literal .notranslate}]{.pre}

- [`lib/vtk/README`{.docutils .literal .notranslate}]{.pre}

- [[dump vtk]{.doc}]dump_vtk.md){.reference .internal}

------------------------------------------------------------------------
:::

:::: {#yaff-package .section}
[]{#pkg-yaff}

## [8.1.93. ]{.section-number}YAFF package[](#yaff-package "Link to this heading"){.headerlink}

**Contents:**

Some potentials that are also implemented in the Yet Another Force Field ([YAFF](https://github.com/molmod/yaff){.reference .external}) code. The expressions and their use are discussed in the following papers

- Vanduyfhuys et al., J. Comput. Chem., 36 (13), 1015-1027 (2015) [link](https://doi.org/10.1002/jcc.23877){.reference .external}

- Vanduyfhuys et al., J. Comput. Chem., 39 (16), 999-1011 (2018) [link](https://doi.org/10.1002/jcc.25173){.reference .external}

which discuss the [QuickFF](https://molmod.github.io/QuickFF/){.reference .external} methodology.

**Author:** Steven Vandenbrande.

::: versionadded
[Added in version 1Feb2019.]{.versionmodified .added}
:::

**Supporting info:**

- [`src/YAFF/README`{.docutils .literal .notranslate}]{.pre}

- [[angle_style cross]{.doc}]angle_cross.md){.reference .internal}

- [[angle_style mm3]{.doc}]angle_mm3.md){.reference .internal}

- [[bond_style mm3]{.doc}]bond_mm3.md){.reference .internal}

- [[improper_style distharm]{.doc}]improper_distharm.md){.reference .internal}

- [[improper_style sqdistharm]{.doc}]improper_sqdistharm.md){.reference .internal}

- [[pair_style mm3/switch3/coulgauss/long]{.doc}]pair_lj_switch3_coulgauss_long.md){.reference .internal}

- [[pair_style lj/switch3/coulgauss/long]{.doc}]pair_lj_switch3_coulgauss_long.md){.reference .internal}

- [`examples/PACKAGES/yaff`{.docutils .literal .notranslate}]{.pre}
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

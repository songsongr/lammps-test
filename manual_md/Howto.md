::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#howto-discussions .section}
# [10. ]{.section-number}Howto discussions[](#howto-discussions "Link to this heading"){.headerlink}

These doc pages describe how to perform various tasks with LAMMPS, both for users and developers. The [glossary](https://www.lammps.org/glossary.html){.reference .external} website page also lists MD terminology, with links to corresponding LAMMPS manual pages. The example input scripts included in the [`examples`{.docutils .literal .notranslate}]{.pre} directory of the LAMMPS source code distribution and highlighted on the [[Example scripts]{.doc}]Examples.md){.reference .internal} page also show how to set up and run various kinds of simulations.

:::: {#general-howto .section}
## [10.1. ]{.section-number}General howto[](#general-howto "Link to this heading"){.headerlink}

::: {#id1 .toctree-wrapper .compound}
- [10.1.1. Restart a simulation]Howto_restart.md){.reference .internal}
- [10.1.2. Visualize LAMMPS snapshots]Howto_viz.md){.reference .internal}
- [10.1.3. Basic workflow for loading LAMMPS trajectories in VMD]Howto_viz.md#basic-workflow-for-loading-lammps-trajectories-in-vmd){.reference .internal}
- [10.1.4. Advanced graphics features in the *dump image* command]Howto_viz.md#advanced-graphics-features-in-the-dump-image-command){.reference .internal}
- [10.1.5. Run multiple simulations from one input script]Howto_multiple.md){.reference .internal}
- [10.1.6. Multi-replica simulations]Howto_replica.md){.reference .internal}
- [10.1.7. Library interface to LAMMPS]Howto_library.md){.reference .internal}
- [10.1.8. Coupling LAMMPS to other codes]Howto_couple.md){.reference .internal}
- [10.1.9. Using LAMMPS with the MDI library for code coupling]Howto_mdi.md){.reference .internal}
- [10.1.10. Broken Bonds]Howto_broken_bonds.md){.reference .internal}
:::
::::

:::: {#settings-howto .section}
## [10.2. ]{.section-number}Settings howto[](#settings-howto "Link to this heading"){.headerlink}

::: {#id2 .toctree-wrapper .compound}
- [10.2.1. 2d simulations]Howto_2d.md){.reference .internal}
- [10.2.2. Type labels]Howto_type_labels.md){.reference .internal}
- [10.2.3. Triclinic (non-orthogonal) simulation boxes]Howto_triclinic.md){.reference .internal}
- [10.2.4. Thermostats]Howto_thermostat.md){.reference .internal}
- [10.2.5. Barostats]Howto_barostat.md){.reference .internal}
- [10.2.6. Walls]Howto_walls.md){.reference .internal}
- [10.2.7. NEMD simulations]Howto_nemd.md){.reference .internal}
- [10.2.8. Long-range dispersion settings]Howto_dispersion.md){.reference .internal}
- [10.2.9. Convert bulk system to slab]Howto_bulk2slab.md){.reference .internal}
:::
::::

:::: {#analysis-howto .section}
## [10.3. ]{.section-number}Analysis howto[](#analysis-howto "Link to this heading"){.headerlink}

::: {#id3 .toctree-wrapper .compound}
- [10.3.1. Output from LAMMPS (thermo, dumps, computes, fixes, variables)]Howto_output.md){.reference .internal}
- [10.3.2. Use chunks to calculate system properties]Howto_chunk.md){.reference .internal}
- [10.3.3. Using distributed grids]Howto_grid.md){.reference .internal}
- [10.3.4. Calculate temperature]Howto_temperature.md){.reference .internal}
- [10.3.5. Calculate elastic constants]Howto_elastic.md){.reference .internal}
- [10.3.6. Calculate thermal conductivity]Howto_kappa.md){.reference .internal}
- [10.3.7. Calculate viscosity]Howto_viscosity.md){.reference .internal}
- [10.3.8. Calculate diffusion coefficients]Howto_diffusion.md){.reference .internal}
- [10.3.9. Output structured data from LAMMPS]Howto_structured_data.md){.reference .internal}
:::
::::

:::: {#force-fields-howto .section}
## [10.4. ]{.section-number}Force fields howto[](#force-fields-howto "Link to this heading"){.headerlink}

::: {#force-howto .toctree-wrapper .compound}
- [10.4.1. Some general force field considerations]Howto_FFgeneral.md){.reference .internal}
- [10.4.2. CHARMM, AMBER, COMPASS, ClassII-xe, DREIDING, and OPLS force fields]Howto_bioFF.md){.reference .internal}
- [10.4.3. AMBER to LAMMPS Tutorial]Howto_amber2lammps.md){.reference .internal}
- [10.4.4. AMOEBA and HIPPO force fields]Howto_amoeba.md){.reference .internal}
- [10.4.5. TIP3P water model]Howto_tip3p.md){.reference .internal}
- [10.4.6. TIP4P and OPC water models]Howto_tip4p.md){.reference .internal}
- [10.4.7. TIP5P water model]Howto_tip5p.md){.reference .internal}
- [10.4.8. SPC and SPC/E water model]Howto_spc.md){.reference .internal}
:::
::::

:::: {#packages-howto .section}
## [10.5. ]{.section-number}Packages howto[](#packages-howto "Link to this heading"){.headerlink}

::: {#id4 .toctree-wrapper .compound}
- [10.5.1. Finite-size spherical and aspherical particles]Howto_spherical.md){.reference .internal}
- [10.5.2. Granular models]Howto_granular.md){.reference .internal}
- [10.5.3. Body particles]Howto_body.md){.reference .internal}
- [10.5.4. Bonded particle models]Howto_bpm.md){.reference .internal}
- [10.5.5. Polarizable models]Howto_polarizable.md){.reference .internal}
- [10.5.6. Adiabatic core/shell model]Howto_coreshell.md){.reference .internal}
- [10.5.7. Drude induced dipoles]Howto_drude.md){.reference .internal}
- [10.5.8. Tutorial for Thermalized Drude oscillators in LAMMPS]Howto_drude2.md){.reference .internal}
- [10.5.9. Peridynamics with LAMMPS]Howto_peri.md){.reference .internal}
- [10.5.10. Manifolds (surfaces)]Howto_manifold.md){.reference .internal}
- [10.5.11. Reproducing hydrodynamics and elastic objects (RHEO)]Howto_rheo.md){.reference .internal}
- [10.5.12. Magnetic spins]Howto_spins.md){.reference .internal}
- [10.5.13. Adaptive-precision interatomic potentials (APIP)]Howto_apip.md){.reference .internal}
:::
::::

:::: {#tutorials-howto .section}
## [10.6. ]{.section-number}Tutorials howto[](#tutorials-howto "Link to this heading"){.headerlink}

::: {#tutorials .toctree-wrapper .compound}
- [10.6.1. Using CMake with LAMMPS]Howto_cmake.md){.reference .internal}
- [10.6.2. LAMMPS GitHub tutorial]Howto_github.md){.reference .internal}
- [10.6.3. Using LAMMPS-GUI]Howto_lammps_gui.md){.reference .internal}
- [10.6.4. Moltemplate Tutorial]Howto_moltemplate.md){.reference .internal}
- [10.6.5. LAMMPS Python Tutorial]Howto_python.md){.reference .internal}
- [10.6.6. Using LAMMPS on Windows 10 with WSL]Howto_wsl.md){.reference .internal}
:::
::::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

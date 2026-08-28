:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#granular-models .section}
# [10.5.2. ]{.section-number}Granular models[](#granular-models "Link to this heading"){.headerlink}

Granular systems are typically composed of spherical particles with a diameter, as opposed to point particles. This means they have an angular velocity and torque can be imparted to them to cause them to rotate.

To run a simulation of a granular model, you will typically want to use the following commands:

- [[atom_style sphere]{.doc}]atom_style.md){.reference .internal}

- [[fix nve/sphere]{.doc}]fix_nve_sphere.md){.reference .internal}

- [[fix gravity]{.doc}]fix_gravity.md){.reference .internal}

Aspherical granular particles can be simulated by creating clusters of spherical particles using either the [[rigid]{.doc}]fix_rigid.md){.reference .internal} or [[BPM]{.doc}]Howto_bpm.md){.reference .internal} package or by using [[superellipsoids]{.doc}]pair_granular_superellipsoid.md){.reference .internal}.

This compute

- [[compute erotate/sphere]{.doc}]compute_erotate_sphere.md){.reference .internal}

calculates rotational kinetic energy which can be [[output with thermodynamic info]{.doc}]Howto_output.md){.reference .internal}. The compute

- [[compute fabric]{.doc}]compute_fabric.md){.reference .internal}

calculates various versions of the fabric tensor for granular and non-granular pair styles.

Use one of these 4 pair potentials, which compute forces and torques between interacting pairs of particles:

- [[pair_style gran/history]{.doc}]pair_gran.md){.reference .internal}

- [[pair_style gran/no_history]{.doc}]pair_gran.md){.reference .internal}

- [[pair_style gran/hertzian]{.doc}]pair_gran.md){.reference .internal}

- [[pair_style granular]{.doc}]pair_granular.md){.reference .internal}

These commands implement fix options specific to granular systems:

- [[fix freeze]{.doc}]fix_freeze.md){.reference .internal}

- [[fix pour]{.doc}]fix_pour.md){.reference .internal}

- [[fix viscous]{.doc}]fix_viscous.md){.reference .internal}

- [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal}

- [[fix wall/gran/region]{.doc}]fix_wall_gran_region.md){.reference .internal}

The fix style *freeze* zeroes both the force and torque of frozen atoms, and should be used for granular system instead of the fix style *setforce*.

To model heat conduction, one must add the temperature and heatflow atom variables with:

- [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal}

a temperature integration fix

- [[fix heat/flow]{.doc}]fix_heat_flow.md){.reference .internal}

and a heat conduction option defined in both

- [[pair_style granular]{.doc}]pair_granular.md){.reference .internal}

- [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal}

For computational efficiency, you can eliminate needless pairwise computations between frozen atoms by using this command:

- [[neigh_modify]{.doc}]neigh_modify.md){.reference .internal} exclude

::: {.admonition .note}
Note

By default, for 2d systems, granular particles are still modeled as 3d spheres, not 2d discs (circles), meaning their moment of inertia will be the same as in 3d. If you wish to model granular particles in 2d as 2d discs, see the note on this topic on the [[Howto 2d]{.doc}]Howto_2d.md){.reference .internal} doc page, where 2d simulations are discussed.
:::

To add custom granular contact models, see the [[modifying granular sub-models page]{.doc}]Modify_gran_sub_mod.md){.reference .internal}.
::::
:::::
::::::

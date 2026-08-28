:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#pair-style-dsmc-command .section}
[]{#index-0}

# pair_style dsmc command[](#pair-style-dsmc-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dsmc max_cell_size seed weighting Tref Nrecompute Nsample
:::
::::

- max_cell_size = global maximum cell size for DSMC interactions (distance units)

- seed = random \# seed (positive integer)

- weighting = macroparticle weighting

- Tref = reference temperature (temperature units)

- Nrecompute = re-compute v\*sigma_max every this many timesteps (timesteps)

- Nsample = sample this many times in recomputing v\*sigma_max
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style dsmc 2.5 34387 10 1.0 100 20
    pair_coeff * * 1.0
    pair_coeff 1 1 1.0
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *dsmc* computes collisions between pairs of particles for a direct simulation Monte Carlo (DSMC) model following the exposition in [[(Bird)]{.std .std-ref}](#bird){.reference .internal}. Each collision resets the velocities of the two particles involved. The number of pairwise collisions for each pair or particle types and the length scale within which they occur are determined by the parameters of the pair_style and pair_coeff commands.

Stochastic collisions are performed using the variable hard sphere (VHS) approach, with the user-defined *max_cell_size* value used as the maximum DSMC cell size, and reference cross-sections for collisions given using the pair_coeff command.

There is no pairwise energy or virial contributions associated with this pair style.

The following coefficient must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- sigma (area units, i.e. distance-squared)

The global DSMC *max_cell_size* determines the maximum cell length used in the DSMC calculation. A structured mesh is overlayed on the simulation box such that an integer number of cells are created in each direction for each processor's subdomain. Cell lengths are adjusted up to the user-specified maximum cell size.

------------------------------------------------------------------------

To perform a DSMC simulation with LAMMPS, several additional options should be set in your input script, though LAMMPS does not check for these settings.

Since this pair style does not compute particle forces, you should use the "fix nve/noforce" time integration fix for the DSMC particles, e.g.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nve/noforce
:::
::::

This pair style assumes that all particles will communicated to neighboring processors every timestep as they move. This makes it possible to perform all collisions between pairs of particles that are on the same processor. To ensure this occurs, you should use these commands:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    neighbor 0.0 bin
    neigh_modify every 1 delay 0 check no
    atom_modify sort 0 0.0
    communicate single cutoff 0.0
:::
::::

These commands ensure that LAMMPS communicates particles to neighboring processors every timestep and that no ghost atoms are created. The output statistics for a simulation run should indicate there are no ghost particles or neighbors.

In order to get correct DSMC collision statistics, users should specify a Gaussian velocity distribution when populating the simulation domain. Note that the default velocity distribution is uniform, which will not give good DSMC collision rates. Specify "dist gaussian" when using the [[velocity]{.doc}]velocity.md){.reference .internal} command as in the following:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    velocity all create 594.6 87287 loop geom dist gaussian
:::
::::
:::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file. Note that the user-specified random number seed is stored in the restart file, so when a simulation is restarted, each processor will re-initialize its random number generator the same way it did initially. This means the random forces will be random, but will not be the same as they would have been if the original simulation had continued past the restart time.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the MC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair style requires an [[atom style]{.doc}]atom_style.md){.reference .internal} with per atom type masses.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix nve/noforce]{.doc}]fix_nve_noforce.md){.reference .internal}, [[neigh_modify]{.doc}]neigh_modify.md){.reference .internal}, [[neighbor]{.doc}]neighbor.md){.reference .internal}, [[comm_modify]{.doc}]comm_modify.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Bird)** G. A. Bird, "Molecular Gas Dynamics and the Direct Simulation of Gas Flows" (1994).
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

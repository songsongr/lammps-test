:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#fix-electron-stopping-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# fix electron/stopping command[](#fix-electron-stopping-command "Link to this heading"){.headerlink}

Accelerator Variants: *electron/stopping/kk*
:::

::::::::::::::::::: {#fix-electron-stopping-fit-command .section}
# fix electron/stopping/fit command[](#fix-electron-stopping-fit-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID style args
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- style = *electron/stopping* or *electron/stopping/fit*

  ``` literal-block
  electron/stopping args = Ecut file keyword value ...
    Ecut  = minimum kinetic energy for electronic stopping (energy units)
    file  = name of the file containing the electronic stopping power table

  electron/stopping/fit args = Ecut c1 c2 ...
    Ecut  = minimum kinetic energy for electronic stopping (energy units)
    c1 c2 = linear and quadratic coefficients for the fitted quadratic polynomial
  ```

- zero or more keyword/value pairs may be appended to args for style = *electron/stopping*

  ``` literal-block
  keyword = region or minneigh
     region value = region-ID
        region-ID = region whose atoms will be affected by this fix
     minneigh value = minneigh
        minneigh = minimum number of neighbors an atom to have stopping applied
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix el all electron/stopping 10.0 elstop-table.txt
    fix el all electron/stopping 10.0 elstop-table.txt minneigh 3
    fix el mygroup electron/stopping 1.0 elstop-table.txt region bulk
    fix 1 all electron/stopping/fit 4.63 3.3e-3 4.0e-8
    fix 1 all electron/stopping/fit 3.49 1.8e-3 9.0e-8 7.57 4.2e-3 5.0e-8
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix implements inelastic energy loss for fast projectiles in solids. It applies a friction force to fast moving atoms to slow them down due to [[electronic stopping]{.std .std-ref}](#elstopping){.reference .internal} (energy lost via electronic collisions per unit of distance). This fix should be used for simulation of irradiation damage or ion implantation, where the ions can lose noticeable amounts of energy from electron excitations. If the electronic stopping power is not considered, the simulated range of the ions can be severely overestimated ([[Nordlund98]{.std .std-ref}](#nordlund98){.reference .internal}, [[Nordlund95]{.std .std-ref}](#nordlund95){.reference .internal}).

The electronic stopping is implemented by applying a friction force to each atom as:

::: {.math .notranslate .nohighlight}
\\\[\\vec{F}\_i = \\vec{F}\^0_i - \\frac{\\vec{v}\_i}{\\\|\\vec{v}\_i\\\|} \\cdot S_e\\\]
:::

where [\\(\\vec{F}\_i\\)]{.math .notranslate .nohighlight} is the resulting total force on the atom. [\\(\\vec{F}\^0_i\\)]{.math .notranslate .nohighlight} is the original force applied to the atom, [\\(\\vec{v}\_i\\)]{.math .notranslate .nohighlight} is its velocity and [\\(S_e\\)]{.math .notranslate .nohighlight} is the stopping power of the ion.

::: {.admonition .note}
Note

In addition to electronic stopping, atomic cascades and irradiation simulations require the use of an adaptive timestep (see [[fix dt/reset]{.doc}]fix_dt_reset.md){.reference .internal}) and the repulsive ZBL potential (see [[ZBL]{.doc}]pair_zbl.md){.reference .internal} potential) or similar. Without these settings the interaction between the ion and the target atoms will be faulty. It is also common to use in such simulations a thermostat ([[fix_nvt]{.doc}]fix_nh.md){.reference .internal}) in the borders of the simulation cell.
:::

::: {.admonition .note}
Note

This fix removes energy from fast projectiles without depositing it as a heat to the simulation cell. Such implementation might lead to the unphysical results when the amount of energy deposited to the electronic system is large, e.g. simulations of Swift Heavy Ions (energy per nucleon of 100 keV/amu or higher) or multiple projectiles. You could compensate energy loss by coupling bulk atoms with some thermostat or control heat transfer between electronic and atomic subsystems with the two-temperature model ([[fix_ttm]{.doc}]fix_ttm.md){.reference .internal}).
:::

At low velocities the electronic stopping is negligible. The electronic friction is not applied to atoms whose kinetic energy is smaller than *Ecut*, or smaller than the lowest energy value given in the table in *file*. Electronic stopping should be applied only when a projectile reaches bulk material. This fix scans neighbor list and excludes atoms with fewer than *minneigh* neighbors (by default one). If the pair potential cutoff is large, minneigh should be increased, though not above the number of nearest neighbors in bulk material. An alternative is to disable the check for neighbors by setting *minneigh* to zero and using the *region* keyword. This is necessary when running simulations of cluster bombardment.

If the *region* keyword is used, the atom must also be in the specified geometric [[region]{.doc}]region.md){.reference .internal} in order to have electronic stopping applied to it. This is useful if the position of the bulk material is fixed. By default the electronic stopping is applied everywhere in the simulation cell.

------------------------------------------------------------------------

The energy ranges and stopping powers are read from the file *file*. Lines starting with *\#* and empty lines are ignored. Otherwise each line must contain exactly **N+1** numbers, where **N** is the number of atom types in the simulation.

The first column is the energy for which the stopping powers on that line apply. The energies must be sorted from the smallest to the largest. The other columns are the stopping powers [\\(S_e\\)]{.math .notranslate .nohighlight} for each atom type, in ascending order, in force [[units]{.doc}]units.md){.reference .internal}. The stopping powers for intermediate energy values are calculated with linear interpolation between 2 nearest points.

For example:

:::: {.highlight-none .notranslate}
::: highlight
    # This is a comment
    #       atom-1    atom-2
    # eV    eV/Ang    eV/Ang  # units metal
     10        0        0
    250       60       80
    750      100      150
:::
::::

If an atom which would have electronic stopping applied to it has a kinetic energy higher than the largest energy given in *file*, LAMMPS will exit with an error message.

The stopping power depends on the energy of the ion and the target material. The electronic stopping table can be obtained from scientific publications, experimental databases or by using [[SRIM]{.std .std-ref}](#srim){.reference .internal} software. Other programs such as [[CasP]{.std .std-ref}](#casp){.reference .internal} can calculate the energy deposited as a function of the impact parameter of the ion; these results can be used to derive the stopping power.

------------------------------------------------------------------------

Style *electron/stopping/fit* calculates the electronic stopping power and cumulative energy lost to the electron gas via a quadratic functional and applies a drag force to the classical equations-of-motion for all atoms moving above some minimum cutoff velocity (i.e., kinetic energy). These coefficients can be determined by fitting a quadratic polynomial to electronic stopping data predicted by, for example, SRIM or TD-DFT. Multiple 'Ecut c1 c2' values can be provided for multi-species simulations in the order of the atom types. There is an examples/PACKAGES/electron_stopping/ directory, which illustrates uses of this command. Details of this implementation are further described in [[Stewart2018]{.std .std-ref}](#stewart2018){.reference .internal} and [[Lee2020]{.std .std-ref}](#lee2020){.reference .internal}.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.

::: {.admonition .note}
Note

The region keyword is supported by Kokkos, but a Kokkos-enabled region must be used. See the region [[region]{.doc}]region.md){.reference .internal} command for more information.
:::
:::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are not supported.

This fix computes a global scalar, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the total energy loss from electronic stopping applied by this fix since the start of the latest run. It is considered "intensive".

The *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command have no effect on this fix.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default is no limitation by region, and minneigh = 1.

------------------------------------------------------------------------

**(electronic stopping)** Wikipedia - Electronic Stopping Power: [https://en.wikipedia.org/wiki/Stopping_power\_%28particle_radiation%29](https://en.wikipedia.org/wiki/Stopping_power_%28particle_radiation%29){.reference .external}

**(Nordlund98)** Nordlund, Kai, et al. Physical Review B 57.13 (1998): 7556.

**(Nordlund95)** Nordlund, Kai. Computational materials science 3.4 (1995): 448-456.

**(SRIM)** SRIM webpage: [http://www.srim.org/](http://www.srim.org/){.reference .external}

**(CasP)** CasP webpage: [https://lief.if.ufrgs.br/pub/CasP/](https://lief.if.ufrgs.br/pub/CasP/){.reference .external}

**(Stewart2018)** J.A. Stewart, et al. (2018) Journal of Applied Physics, 123(16), 165902.

**(Lee2020)** C.W. Lee, et al. (2020) Physical Review B, 102(2), 024107.
:::
:::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#calculate-thermal-conductivity .section}
# [10.3.6. ]{.section-number}Calculate thermal conductivity[](#calculate-thermal-conductivity "Link to this heading"){.headerlink}

The thermal conductivity [\\(\\kappa\\)]{.math .notranslate .nohighlight} of a material can be measured in at least 4 ways using various options in LAMMPS. See the [`examples/KAPPA`{.docutils .literal .notranslate}]{.pre} directory for scripts that implement the 4 methods discussed here for a simple Lennard-Jones fluid model. Also, see the [[Howto viscosity]{.doc}]Howto_viscosity.md){.reference .internal} page for an analogous discussion for viscosity.

The thermal conductivity tensor [\\(\\mathbf{\\kappa}\\)]{.math .notranslate .nohighlight} is a measure of the propensity of a material to transmit heat energy in a diffusive manner as given by Fourier's law

::: {.math .notranslate .nohighlight}
\\\[J = -\\kappa \\cdot \\text{grad}(T)\\\]
:::

where [\\(J\\)]{.math .notranslate .nohighlight} is the heat flux in units of energy per area per time and [\\(\\text{grad}(T)\\)]{.math .notranslate .nohighlight} is the spatial gradient of temperature. The thermal conductivity thus has units of energy per distance per time per degree K and is often approximated as an isotropic quantity, i.e. as a scalar.

The first method is to setup two thermostatted regions at opposite ends of a simulation box, or one in the middle and one at the end of a periodic box. By holding the two regions at different temperatures with a [[thermostatting fix]{.doc}]Howto_thermostat.md){.reference .internal}, the energy added to the hot region should equal the energy subtracted from the cold region and be proportional to the heat flux moving between the regions. See the papers by [[Ikeshoji and Hafskjold]{.std .std-ref}](#howto-ikeshoji){.reference .internal} and [[Wirnsberger et al]{.std .std-ref}](#howto-wirnsberger){.reference .internal} for details of this idea. Note that thermostatting fixes such as [[fix nvt]{.doc}]fix_nh.md){.reference .internal}, [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, and [[fix temp/rescale]{.doc}]fix_temp_rescale.md){.reference .internal} store the cumulative energy they add/subtract.

Alternatively, as a second method, the [[fix heat]{.doc}]fix_heat.md){.reference .internal} or [[fix ehex]{.doc}]fix_ehex.md){.reference .internal} commands can be used in place of thermostats on each of two regions to add/subtract specified amounts of energy to both regions. In both cases, the resulting temperatures of the two regions can be monitored with the "compute temp/region" command and the temperature profile of the intermediate region can be monitored with the [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} and [[compute ke/atom]{.doc}]compute_ke_atom.md){.reference .internal} commands.

The third method is to perform a reverse non-equilibrium MD simulation using the [[fix thermal/conductivity]{.doc}]fix_thermal_conductivity.md){.reference .internal} command which implements the rNEMD algorithm of Muller-Plathe. Kinetic energy is swapped between atoms in two different layers of the simulation box. This induces a temperature gradient between the two layers which can be monitored with the [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} and [[compute ke/atom]{.doc}]compute_ke_atom.md){.reference .internal} commands. The fix tallies the cumulative energy transfer that it performs. See the [[fix thermal/conductivity]{.doc}]fix_thermal_conductivity.md){.reference .internal} command for details.

The fourth method is based on the Green-Kubo (GK) formula which relates the ensemble average of the auto-correlation of the heat flux to [\\(\\kappa\\)]{.math .notranslate .nohighlight}. The heat flux can be calculated from the fluctuations of per-atom potential and kinetic energies and per-atom stress tensor in a steady-state equilibrated simulation. This is in contrast to the two preceding non-equilibrium methods, where energy flows continuously between hot and cold regions of the simulation box.

The [[compute heat/flux]{.doc}]compute_heat_flux.md){.reference .internal} command can calculate the needed heat flux and describes how to implement the Green_Kubo formalism using additional LAMMPS commands, such as the [[fix ave/correlate]{.doc}]fix_ave_correlate.md){.reference .internal} command to calculate the needed auto-correlation. See the page for the [[compute heat/flux]{.doc}]compute_heat_flux.md){.reference .internal} command for an example input script that calculates the thermal conductivity of solid Ar via the GK formalism.

------------------------------------------------------------------------

**(Ikeshoji)** Ikeshoji and Hafskjold, Molecular Physics, 81, 251-261 (1994).

**(Wirnsberger)** Wirnsberger, Frenkel, and Dellago, J Chem Phys, 143, 124104 (2015).
::::
:::::
::::::

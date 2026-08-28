::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#calculate-temperature .section}
# [10.3.4. ]{.section-number}Calculate temperature[](#calculate-temperature "Link to this heading"){.headerlink}

Temperature is computed as kinetic energy divided by some number of degrees of freedom (and the Boltzmann constant). Since kinetic energy is a function of particle velocity, there is often a need to distinguish between a particle's advection velocity (due to some aggregate motion of particles) and its thermal velocity. The sum of the two is the particle's total velocity, but the latter is often what is wanted to compute a temperature.

LAMMPS has several options for computing temperatures, any of which can be used in [[thermostatting]{.doc}]Howto_thermostat.md){.reference .internal} and [[barostatting]{.doc}]Howto_barostat.md){.reference .internal}. These [[compute commands]{.doc}]compute.md){.reference .internal} calculate temperature:

- [[compute temp]{.doc}]compute_temp.md){.reference .internal}

- [[compute temp/sphere]{.doc}]compute_temp_sphere.md){.reference .internal}

- [[compute temp/asphere]{.doc}]compute_temp_asphere.md){.reference .internal}

- [[compute temp/com]{.doc}]compute_temp_com.md){.reference .internal}

- [[compute temp/deform]{.doc}]compute_temp_deform.md){.reference .internal}

- [[compute temp/partial]{.doc}]compute_temp_partial.md){.reference .internal}

- [[compute temp/profile]{.doc}]compute_temp_profile.md){.reference .internal}

- [[compute temp/ramp]{.doc}]compute_temp_ramp.md){.reference .internal}

- [[compute temp/region]{.doc}]compute_temp_region.md){.reference .internal}

All but the first 3 calculate velocity biases directly (e.g. advection velocities) that are removed when computing the thermal temperature. [[Compute temp/sphere]{.doc}]compute_temp_sphere.md){.reference .internal} and [[compute temp/asphere]{.doc}]compute_temp_asphere.md){.reference .internal} compute kinetic energy for finite-size particles that includes rotational degrees of freedom. They both allow for velocity biases indirectly, via an optional extra argument which is another temperature compute that subtracts a velocity bias. This allows the translational velocity of spherical or aspherical particles to be adjusted in prescribed ways.
:::
::::
:::::

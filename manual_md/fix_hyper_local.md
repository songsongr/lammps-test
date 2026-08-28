::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::: {#fix-hyper-local-command .section}
[]{#index-0}

# fix hyper/local command[](#fix-hyper-local-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID hyper/local cutbond qfactor Vmax Tequil Dcut alpha Btarget
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- hyper/local = style name of this fix command

- cutbond = max distance at which a pair of atoms is considered bonded (distance units)

- qfactor = max strain at which bias potential goes to 0.0 (unitless)

- Vmax = estimated height of bias potential (energy units)

- Tequil = equilibration temperature (temperature units)

- Dcut = minimum distance between boosted bonds (distance units)

- alpha = boostostat relaxation time (time units)

- Btarget = desired time boost factor (unitless)

- zero or more keyword/value pairs may be appended

- keyword = *bound* or *reset* or *check/ghost* or *check/bias*

  ``` literal-block
  bound value = Bfrac
    Bfrac =  -1 or a value >= 0.0
  reset value = Rfreq
    Rfreq = -1 or 0 or timestep value > 0
  check/ghost values = none
  check/bias values = Nevery error/warn/ignore
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all hyper/local 1.0 0.3 0.8 300.0
    fix 1 all hyper/local 1.0 0.3 0.8 300.0 bound 0.1 reset 0
:::
::::
:::::

:::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix is meant to be used with the [[hyper]{.doc}]hyper.md){.reference .internal} command to perform a bond-boost local hyperdynamics (LHD) simulation. The role of this fix is to a select multiple pairs of atoms in the system at each timestep to add a local bias potential to, which will alter the dynamics of the system in a manner that effectively accelerates time. This is in contrast to the [[fix hyper/global]{.doc}]fix_hyper_global.md){.reference .internal} command, which can be user to perform a global hyperdynamics (GHD) simulation, by adding a global bias potential to a single pair of atoms at each timestep. GHD can time accelerate a small simulation with up to a few 100 atoms. For larger systems, LHD is needed to achieve good time acceleration.

For a system that undergoes rare transition events, where one or more atoms move over an energy barrier to a new potential energy basin, the effect of the bias potential is to induce more rapid transitions. This can lead to a dramatic speed-up in the rate at which events occurs, without altering their relative frequencies, thus leading to an overall increase in the elapsed real time of the simulation as compared to running for the same number of timesteps with normal MD. See the [[hyper]{.doc}]hyper.md){.reference .internal} page for a more general discussion of hyperdynamics and citations that explain both GHD and LHD.

The equations and logic used by this fix and described here to perform LHD follow the description given in [[(Voter2013)]{.std .std-ref}](#voter2013lhd){.reference .internal}. The bond-boost form of a bias potential for HD is due to Miron and Fichthorn as described in [[(Miron)]{.std .std-ref}](#mironlhd){.reference .internal}.

To understand this description, you should first read the description of the GHD algorithm on the [[fix hyper/global]{.doc}]fix_hyper_global.md){.reference .internal} doc page. This description of LHD builds on the GHD description.

The definition of bonds and [\\(E\_{ij}\\)]{.math .notranslate .nohighlight} are the same for GHD and LHD. The formulas for [\\(V\^{max}\_{ij}\\)]{.math .notranslate .nohighlight} and [\\(F\^{max}\_{ij}\\)]{.math .notranslate .nohighlight} are also the same except for a prefactor [\\(C\_{ij}\\)]{.math .notranslate .nohighlight}, explained below.

The bias energy [\\(V\_{ij}\\)]{.math .notranslate .nohighlight} applied to a bond *ij* with maximum strain is

::: {.math .notranslate .nohighlight}
\\\[V\^{max}\_{ij} = C\_{ij} \\cdot V\^{max} \\cdot \\left(1 - \\left(\\frac{E\_{ij}}{q}\\right)\^2\\right) \\textrm{ for } \\left\|E\_{ij}\\right\| \< qfactor \\textrm{ or } 0 \\textrm{ otherwise}\\\]
:::

The derivative of [\\(V\^{max}\_{ij}\\)]{.math .notranslate .nohighlight} with respect to the position of each atom in the *ij* bond gives a bias force [\\(F\^{max}\_{ij}\\)]{.math .notranslate .nohighlight} acting on the bond as

::: {.math .notranslate .nohighlight}
\\\[F\^{max}\_{ij} = - \\frac{dV\^{max}\_{ij}}{dE\_{ij}} = 2 C\_{ij} V\^{max} \\frac{E\_{ij}}{qfactor\^2} \\textrm{ for } \\left\|E\_{ij}\\right\| \< qfactor \\textrm{ or } 0 \\textrm{ otherwise}\\\]
:::

which can be decomposed into an equal and opposite force acting on only the two atoms *i* and *j* in the *ij* bond.

The key difference is that in GHD a bias energy and force is added (on a particular timestep) to only one bond (pair of atoms) in the system, which is the bond with maximum strain [\\(E\^{max}\\)]{.math .notranslate .nohighlight}.

In LHD, a bias energy and force can be added to multiple bonds separated by the specified *Dcut* distance or more. A bond *ij* is biased if it is the maximum strain bond within its local "neighborhood", which is defined as the bond *ij* plus any neighbor bonds within a distance *Dcut* from *ij*. The "distance" between bond *ij* and bond *kl* is the minimum distance between any of the *ik*, *il*, *jk*, and *jl* pairs of atoms.

For a large system, multiple bonds will typically meet this requirement, and thus a bias potential [\\(V\^{max}\_{ij}\\)]{.math .notranslate .nohighlight} will be applied to many bonds on the same timestep.

In LHD, all bonds store a [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} prefactor which appears in the [\\(V\^{max}\_{ij}\\)]{.math .notranslate .nohighlight} and [\\(F\^{max}\_{ij}\\)]{.math .notranslate .nohighlight} equations above. Note that the [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} factor scales the strength of the bias energy and forces whenever bond *ij* is the maximum strain bond in its neighborhood.

[\\(C\_{ij}\\)]{.math .notranslate .nohighlight} is initialized to 1.0 when a bond between the *ij* atoms is first defined. The specified *Btarget* factor is then used to adjust the [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} prefactors for each bond every timestep in the following manner.

An instantaneous boost factor [\\(B\_{ij}\\)]{.math .notranslate .nohighlight} is computed each timestep for each bond, as

::: {.math .notranslate .nohighlight}
\\\[B\_{ij} = e\^{\\beta V\^{max}\_{kl}}\\\]
:::

where [\\(V\^{max}\_{kl}\\)]{.math .notranslate .nohighlight} is the bias energy of the maxstrain bond *kl* within bond *ij*'s neighborhood, [\\(\\beta = \\frac{1}{kT\_{equil}}\\)]{.math .notranslate .nohighlight}, and [\\(T\_{equil}\\)]{.math .notranslate .nohighlight} is the temperature of the system and an argument to this fix.

::: {.admonition .note}
Note

To run an LHD simulation, the input script must also use the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} command to thermostat the atoms at the same [\\(T\_{equil}\\)]{.math .notranslate .nohighlight} as specified by this fix, so that the system is running constant-temperature (NVT) dynamics. LAMMPS does not check that this is done.
:::

Note that if *ij*== *kl*, then bond *ij* is a biased bond on that timestep, otherwise it is not. But regardless, the boost factor [\\(B\_{ij}\\)]{.math .notranslate .nohighlight} can be thought of an estimate of time boost currently being applied within a local region centered on bond *ij*. For LHD, we want this to be the specified *Btarget* value everywhere in the simulation domain.

To accomplish this, if [\\(B\_{ij} \< B\_{target}\\)]{.math .notranslate .nohighlight}, the [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} prefactor for bond *ij* is incremented on the current timestep by an amount proportional to the inverse of the specified [\\(\\alpha\\)]{.math .notranslate .nohighlight} and the difference ([\\(B\_{ij} - B\_{target}\\)]{.math .notranslate .nohighlight}). Conversely if [\\(B\_{ij} \> B\_{target}\\)]{.math .notranslate .nohighlight}, [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} is decremented by the same amount. This procedure is termed "boostostatting" in [[(Voter2013)]{.std .std-ref}](#voter2013lhd){.reference .internal}. It drives all of the individual [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} to values such that when [\\(V\^{max}\_{ij}\\)]{.math .notranslate .nohighlight} is applied as a bias to bond *ij*, the resulting boost factor [\\(B\_{ij}\\)]{.math .notranslate .nohighlight} will be close to [\\(B\_{target}\\)]{.math .notranslate .nohighlight} on average. Thus the LHD time acceleration factor for the overall system is effectively *Btarget*.

Note that in LHD, the boost factor [\\(B\_{target}\\)]{.math .notranslate .nohighlight} is specified by the user. This is in contrast to global hyperdynamics (GHD) where the boost factor varies each timestep and is computed as a function of [\\(V\_{max}\\)]{.math .notranslate .nohighlight}, [\\(E\_{max}\\)]{.math .notranslate .nohighlight}, and [\\(T\_{equil}\\)]{.math .notranslate .nohighlight}; see the [[fix hyper/global]{.doc}]fix_hyper_global.md){.reference .internal} page for details.

------------------------------------------------------------------------

Here is additional information on the input parameters for LHD.

Note that the *cutbond*, *qfactor*, and *Tequil* arguments have the same meaning as for GHD. The *Vmax* argument is slightly different. The *Dcut*, *alpha*, and *Btarget* parameters are unique to LHD.

The *cutbond* argument is the cutoff distance for defining bonds between pairs of nearby atoms. A pair of I,J atoms in their equilibrium, minimum-energy configuration, which are separated by a distance [\\(R\_{ij} \< cutbond\\)]{.math .notranslate .nohighlight}, are flagged as a bonded pair. Setting *cubond* to be \~25% larger than the nearest-neighbor distance in a crystalline lattice is a typical choice for solids, so that bonds exist only between nearest neighbor pairs.

The *qfactor* argument is the limiting strain at which the bias potential goes to 0.0. It is dimensionless, so a value of 0.3 means a bond distance can be up to 30% larger or 30% smaller than the equilibrium (quenched) [\\(R\^0\_{ij}\\)]{.math .notranslate .nohighlight} distance and the two atoms in the bond could still experience a non-zero bias force.

If *qfactor* is set too large, then transitions from one energy basin to another are affected because the bias potential is non-zero at the transition state (e.g. saddle point). If *qfactor* is set too small than little boost can be achieved because the [\\(E\_{ij}\\)]{.math .notranslate .nohighlight} strain of some bond in the system will (nearly) always exceed *qfactor*. A value of 0.3 for *qfactor* is typically a reasonable value.

The *Vmax* argument is a fixed prefactor on the bias potential. There is a also a dynamic prefactor [\\(C\_{ij}\\)]{.math .notranslate .nohighlight}, driven by the choice of *Btarget* as discussed above. The product of these should be a value less than the smallest barrier height for an event to occur. Otherwise the applied bias potential may be large enough (when added to the interatomic potential) to produce a local energy basin with a maxima in the center. This can produce artificial energy minima in the same basin that trap an atom. Or if [\\(C\_{ij} \\cdot V\^{max}\\)]{.math .notranslate .nohighlight} is even larger, it may induce an atom(s) to rapidly transition to another energy basin. Both cases are "bad dynamics" which violate the assumptions of LHD that guarantee an accelerated time-accurate trajectory of the system.

::: {.admonition .note}
Note

It may seem that [\\(V\^{max}\\)]{.math .notranslate .nohighlight} can be set to any value, and [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} will compensate to reduce the overall prefactor if necessary. However the [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} are initialized to 1.0 and the boostostatting procedure typically operates slowly enough that there can be a time period of bad dynamics if [\\(V\^{max}\\)]{.math .notranslate .nohighlight} is set too large. A better strategy is to set [\\(V\^{max}\\)]{.math .notranslate .nohighlight} to the slightly smaller than the lowest barrier height for an event (the same as for GHD), so that the [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} remain near unity.
:::

The *Tequil* argument is the temperature at which the system is simulated; see the comment above about the [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} thermostatting. It is also part of the beta term in the exponential factor that determines how much boost is achieved as a function of the bias potential. See the discussion of the *Btarget* argument below.

As discussed above, the *Dcut* argument is the distance required between two locally maxstrain bonds for them to both be selected as biased bonds on the same timestep. Computationally, the larger *Dcut* is, the more work (computation and communication) must be done each timestep within the LHD algorithm. And the fewer bonds can be simultaneously biased, which may mean the specified *Btarget* time acceleration cannot be achieved.

Physically *Dcut* should be a long enough distance that biasing two pairs of atoms that close together will not influence the dynamics of each pair. E.g. something like 2x the cutoff of the interatomic potential. In practice a *Dcut* value of \~10 Angstroms seems to work well for many solid-state systems.

::: {.admonition .note}
Note

You should ensure that ghost atom communication is performed for a distance of at least *Dcut* + *cutevent* = the distance one or more atoms move (between quenched states) to be considered an "event". It is an argument to the "compute event/displace" command used to detect events. By default the ghost communication distance is set by the pair_style cutoff, which will typically be \< *Dcut*. The [[comm_modify cutoff]{.doc}]comm_modify.md){.reference .internal} command should be used to override the ghost cutoff explicitly, e.g.
:::

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    comm_modify cutoff 12.0
:::
::::

Note that this fix does not know the *cutevent* parameter, but uses half the *cutbond* parameter as an estimate to warn if the ghost cutoff is not long enough.

As described above the *alpha* argument is a prefactor in the boostostat update equation for each bond's [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} prefactor. *Alpha* is specified in time units, similar to other thermostat or barostat damping parameters. It is roughly the physical time it will take the boostostat to adjust a [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} value from a too high (or too low) value to a correct one. An *alpha* setting of a few ps is typically good for solid-state systems. Note that the *alpha* argument here is the inverse of the alpha parameter discussed in [[(Voter2013)]{.std .std-ref}](#voter2013lhd){.reference .internal}.

The *Btarget* argument is the desired time boost factor (a value \> 1) that all the atoms in the system will experience. The elapsed time [\\(t\_{hyper}\\)]{.math .notranslate .nohighlight} for an LHD simulation running for *N* timesteps is simply

::: {.math .notranslate .nohighlight}
\\\[t\_{hyper} = B\_{target} \\cdot N \\cdot dt\\\]
:::

where *dt* is the timestep size defined by the [[timestep]{.doc}]timestep.md){.reference .internal} command. The effective time acceleration due to LHD is thus [\\(\\frac{t\_{hyper}}{N\\cdot dt} = B\_{target}\\)]{.math .notranslate .nohighlight}, where [\\(N\\cdot dt\\)]{.math .notranslate .nohighlight} is the elapsed time for a normal MD run of N timesteps.

You cannot choose an arbitrarily large setting for *Btarget*. The maximum value you should choose is

::: {.math .notranslate .nohighlight}
\\\[B\_{target} = e\^{\\beta V\_{small}}\\\]
:::

where [\\(V\_{small}\\)]{.math .notranslate .nohighlight} is the smallest event barrier height in your system, [\\(\\beta = \\frac{1}{kT\_{equil}}\\)]{.math .notranslate .nohighlight}, and [\\(T\_{equil}\\)]{.math .notranslate .nohighlight} is the specified temperature of the system (both by this fix and the Langevin thermostat).

Note that if *Btarget* is set smaller than this, the LHD simulation will run correctly. There will just be fewer events because the hyper time ([\\(t\_{hyper}\\)]{.math .notranslate .nohighlight} equation above) will be shorter.

::: {.admonition .note}
Note

If you have no physical intuition as to the smallest barrier height in your system, a reasonable strategy to determine the largest *Btarget* you can use for an LHD model, is to run a sequence of simulations with smaller and smaller *Btarget* values, until the event rate does not change (as a function of hyper time).
:::

------------------------------------------------------------------------

Here is additional information on the optional keywords for this fix.

The *bound* keyword turns on min/max bounds for bias coefficients [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} for all bonds. [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} is a prefactor for each bond on the bias potential of maximum strength [\\(V\^{max}\\)]{.math .notranslate .nohighlight}. Depending on the choice of *alpha* and *Btarget* and *Vmax*, the boostostatting can cause individual [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} values to fluctuate. If the fluctuations are too large [\\(C\_{ij} \\cdot V\^{max}\\)]{.math .notranslate .nohighlight} can exceed low barrier heights and induce bad event dynamics. Bounding the [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} values is a way to prevent this. If *Bfrac* is set to -1 or any negative value (the default) then no bounds are enforced on [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} values (except they must always be \>= 0.0). A *Bfrac* setting \>= 0.0 sets a lower bound of 1.0 - Bfrac and upper bound of 1.0 + Bfrac on each [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} value. Note that all [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} values are initialized to 1.0 when a bond is created for the first time. Thus *Bfrac* limits the bias potential height to *Vmax* +/- *Bfrac*\**Vmax*.

The *reset* keyword allow *Vmax* to be adjusted dynamically depending on the average value of all [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} prefactors. This can be useful if you are unsure what value of *Vmax* will match the *Btarget* boost for the system. The [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} values will then adjust in aggregate (up or down) so that [\\(C\_{ij} \\cdot V\^{max}\\)]{.math .notranslate .nohighlight} produces a boost of *Btarget*, but this may conflict with the *bound* keyword settings. By using *bound* and *reset* together, [\\(V\^{max}\\)]{.math .notranslate .nohighlight} itself can be reset, and desired bounds still applied to the [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} values.

A setting for *Rfreq* of -1 (the default) means *Vmax* never changes. A setting of 0 means [\\(V\^{max}\\)]{.math .notranslate .nohighlight} is adjusted every time an event occurs and bond pairs are recalculated. A setting of N \> 0 timesteps means [\\(V\^{max}\\)]{.math .notranslate .nohighlight} is adjusted on the first time an event occurs on a timestep \>= N steps after the previous adjustment. The adjustment to [\\(V\^{max}\\)]{.math .notranslate .nohighlight} is computed as follows. The current average of all [\\(C\_{ij} \\cdot V\^{max}\\)]{.math .notranslate .nohighlight} values is computed and the [\\(V\^{max}\\)]{.math .notranslate .nohighlight} is reset to that value. All [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} values are changed to new prefactors such the new [\\(C\_{ij} \\cdot V\^{max}\\)]{.math .notranslate .nohighlight} is the same as it was previously. If the *bound* keyword was used, those bounds are enforced on the new [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} values. Henceforth, new bonds are assigned a [\\(C\_{ij} = 1.0\\)]{.math .notranslate .nohighlight}, which means their bias potential magnitude is the new [\\(V\^{max}\\)]{.math .notranslate .nohighlight}.

The *check/ghost* keyword turns on extra computation each timestep to compute statistics about ghost atoms used to determine which bonds to bias. The output of these stats are the vector values 14 and 15, described below. If this keyword is not enabled, the output of the stats will be zero.

The *check/bias* keyword turns on extra computation and communication to check if any biased bonds are closer than *Dcut* to each other, which should not be the case if LHD is operating correctly. Thus it is a debugging check. The *Nevery* setting determines how often the check is made. The *error*, *warn*, or *ignore* setting determines what is done if the count of too-close bonds is not zero. Either the code will exit, or issue a warning, or silently tally the count. The count can be output as vector value 17, as described below. If this keyword is not enabled, the output of that statistic will be 0.

Note that both of these computations are costly, hence they are only enabled by these keywords.
::::::::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the energy of the bias potential to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}.

This fix computes a global scalar and global vector of length 28, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the magnitude of the bias potential (energy units) applied on the current timestep, summed over all biased bonds. The vector stores the following quantities:

> ::: {}
> 1.  average boost for all bonds on this step (unitless)
>
> 2.  \# of biased bonds on this step
>
> 3.  max strain [\\(E\_{ij}\\)]{.math .notranslate .nohighlight} of any bond on this step (absolute value, unitless)
>
> 4.  value of [\\(V\^{max}\\)]{.math .notranslate .nohighlight} on this step (energy units)
>
> 5.  average bias coeff for all bonds on this step (unitless)
>
> 6.  min bias coeff for all bonds on this step (unitless)
>
> 7.  max bias coeff for all bonds on this step (unitless)
>
> 8.  average \# of bonds/atom on this step
>
> 9.  average neighbor bonds/bond on this step within *Dcut*
>
> 10. average boost for all bonds during this run (unitless)
>
> 11. average \# of biased bonds/step during this run
>
> 12. fraction of biased bonds with no bias during this run
>
> 13. fraction of biased bonds with negative strain during this run
>
> 14. max bond length during this run (distance units)
>
> 15. average bias coeff for all bonds during this run (unitless)
>
> 16. min bias coeff for any bond during this run (unitless)
>
> 17. max bias coeff for any bond during this run (unitless)
>
> 18. max drift distance of any bond atom during this run (distance units)
>
> 19. max distance from proc subbox of any ghost atom with maxstrain \< qfactor during this run (distance units)
>
> 20. max distance outside my box of any ghost atom with any maxstrain during this run (distance units)
>
> 21. count of ghost atoms that could not be found on reneighbor steps during this run
>
> 22. count of bias overlaps (\< *Dcut*) found during this run
>
> 23. cumulative hyper time since fix created (time units)
>
> 24. cumulative count of event timesteps since fix created
>
> 25. cumulative count of atoms in events since fix created
>
> 26. cumulative \# of new bonds formed since fix created
>
> 27. average boost for biased bonds on this step (unitless)
>
> 28. \# of bonds with absolute strain \>= q on this step
> :::

Quantities 1-9 are for the current timestep. Quantities 10-22 are for the current hyper run. They are reset each time a new hyper run is performed. Quantities 23-26 are cumulative across multiple runs (since the point in the input script the fix was defined).

For value 10, each bond instantaneous boost factor is given by the equation for [\\(B\_{ij}\\)]{.math .notranslate .nohighlight} above. The total system boost (average across all bonds) fluctuates, but should average to a value close to the specified [\\(B\_{target}\\)]{.math .notranslate .nohighlight}.

For value 12, the numerator is a count of all biased bonds on each timestep whose bias energy = 0.0 due to [\\(E\_{ij} \>= qfactor\\)]{.math .notranslate .nohighlight}. The denominator is the count of all biased bonds on all timesteps.

For value 13, the numerator is a count of all biased bonds on each timestep with negative strain. The denominator is the count of all biased bonds on all timesteps.

Values 18-22 are mostly useful for debugging and diagnostic purposes.

For value 18, drift is the distance an atom moves between two quenched states when the second quench determines an event has occurred. Atoms involved in an event will typically move the greatest distance since others typically remain near their original quenched position.

For values 19-21, neighbor atoms in the full neighbor list with cutoff *Dcut* may be ghost atoms outside a processor's sub-box. Before the next event occurs they may move further than *Dcut* away from the sub-box boundary. Value 19 is the furthest (from the sub-box) any ghost atom in the neighbor list with maxstrain \< *qfactor* was accessed during the run. Value 20 is the same except that the ghost atom's maxstrain may be \>= *qfactor*, which may mean it is about to participate in an event. Value 21 is a count of how many ghost atoms could not be found on reneighbor steps, presumably because they moved too far away due to their participation in an event (which will likely be detected at the next quench).

Typical values for 19 and 20 should be slightly larger than *Dcut*, which accounts for ghost atoms initially at a *Dcut* distance moving thermally before the next event takes place.

Note that for values 19 and 20 to be computed, the optional keyword *check/ghost* must be specified. Otherwise these values will be zero. This is because computing them incurs overhead, so the values are only computed if requested.

Value 21 should be zero or small. As explained above a small count likely means some ghost atoms were participating in their own events and moved a longer distance. If the value is large, it likely means the communication cutoff for ghosts is too close to *Dcut* leading to many not-found ghost atoms before the next event. This may lead to a reduced number of bonds being selected for biasing, since the code assumes those atoms are part of highly strained bonds. As explained above, the [[comm_modify cutoff]{.doc}]comm_modify.md){.reference .internal} command can be used to set a longer cutoff.

For value 22, no two bonds should be biased if they are within a *Dcut* distance of each other. This value should be zero, indicating that no pair of biased bonds are closer than *Dcut* from each other.

Note that for value 22 to be computed, the optional keyword *check/bias* must be specified and it determines how often this check is performed. This is because performing the check incurs overhead, so if only computed as often as requested.

The result at the end of the run is the cumulative total from every timestep the check was made. Note that the value is a count of atoms in bonds which found other atoms in bonds too close, so it is almost always an over-count of the number of too-close bonds.

Value 23 is simply the specified *boost* factor times the number of timesteps times the timestep size.

For value 24, events are checked for by the [[hyper]{.doc}]hyper.md){.reference .internal} command once every *Nevent* timesteps. This value is the count of those timesteps on which one (or more) events was detected. It is NOT the number of distinct events, since more than one event may occur in the same *Nevent* time window.

For value 25, each time the [[hyper]{.doc}]hyper.md){.reference .internal} command checks for an event, it invokes a compute to flag zero or more atoms as participating in one or more events. E.g. atoms that have displaced more than some distance from the previous quench state. Value 25 is the cumulative count of the number of atoms participating in any of the events that were found.

Value 26 tallies the number of new bonds created by the bond reset operation. Bonds between a specific I,J pair of atoms may persist for the entire hyperdynamics simulation if neither I or J are involved in an event.

Value 27 computes the average boost for biased bonds only on this step.

Value 28 is the count of bonds with an absolute value of strain \>= q on this step.

The scalar value and vector values are all "intensive".

This fix also computes a local vector of length the number of bonds currently in the system. The value for each bond is its [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} prefactor (bias coefficient). These values can be can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. A particularly useful one is the [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal} command which can be used to histogram the Cij values to see if they are distributed reasonably close to 1.0, which indicates a good choice of [\\(V\^{max}\\)]{.math .notranslate .nohighlight}.

The local values calculated by this fix are unitless.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the REPLICA package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[hyper]{.doc}]hyper.md){.reference .internal}, [[fix hyper/global]{.doc}]fix_hyper_global.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default settings for optimal keywords are bounds = -1 and reset = -1. The check/ghost and check/bias keywords are not enabled by default.

------------------------------------------------------------------------

**(Voter2013)** S. Y. Kim, D. Perez, A. F. Voter, J Chem Phys, 139, 144110 (2013).

**(Miron)** R. A. Miron and K. A. Fichthorn, J Chem Phys, 119, 6210 (2003).
:::
:::::::::::::::::::::::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::

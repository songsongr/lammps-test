:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#hyper-command .section}
[]{#index-0}

# hyper command[](#hyper-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    hyper N Nevent fix-ID compute-ID keyword values ...
:::
::::

- N = \# of timesteps to run

- Nevent = check for events every this many steps

- fix-ID = ID of a fix that applies a global or local bias potential, can be NULL

- compute-ID = ID of a compute that identifies when an event has occurred

- zero or more keyword/value pairs may be appended

- keyword = *min* or *dump* or *rebond*

  ``` literal-block
  min values = etol ftol maxiter maxeval
    etol = stopping tolerance for energy, used in quenching
    ftol = stopping tolerance for force, used in quenching
    maxiter = max iterations of minimize, used in quenching
    maxeval = max number of force/energy evaluations, used in quenching
  dump value = dump-ID
    dump-ID = ID of dump to trigger whenever an event takes place
  rebond value = Nrebond
    Nrebond = frequency at which to reset bonds, even if no event has occurred
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute event all event/displace 1.0
    fix HG mobile hyper/global 3.0 0.3 0.4 800.0
    hyper 5000 100 HG event min 1.0e-6 1.0e-6 100 100 dump 1 dump 5
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Run a bond-boost hyperdynamics (HD) simulation where time is accelerated by application of a bias potential to one or more pairs of nearby atoms in the system. This command can be used to run both global and local hyperdynamics. In global HD a single bond within the system is biased on each timestep. In local HD multiple bonds (separated by a sufficient distance) can be biased simultaneously at each timestep. In the bond-boost hyperdynamics context, a "bond" is not a covalent bond between a pair of atoms in a molecule. Rather it is simply a pair of nearby atoms as discussed below.

Both global and local HD are described in [[(Voter2013)]{.std .std-ref}](#voter2013){.reference .internal} by Art Voter and collaborators. Similar to parallel replica dynamics (PRD), global and local HD are methods for performing accelerated dynamics that are suitable for infrequent-event systems that obey first-order kinetics. A good overview of accelerated dynamics methods (AMD) for such systems in given in [[(Voter2002)]{.std .std-ref}](#voter2002hd){.reference .internal} from the same group. To quote from the review paper: "The dynamical evolution is characterized by vibrational excursions within a potential basin, punctuated by occasional transitions between basins. The transition probability is characterized by p(t) = k\*exp(-kt) where k is the rate constant."

Both HD and PRD produce a time-accurate trajectory that effectively extends the timescale over which a system can be simulated, but they do it differently. HD uses a single replica of the system and accelerates time by biasing the interaction potential in a manner such that each timestep is effectively longer. PRD creates Nr replicas of the system and runs dynamics on each independently with a normal unbiased potential until an event occurs in one of the replicas. The time between events is reduced by a factor of Nr replicas. For both methods, per CPU second, more physical time elapses and more events occur. See the [[prd]{.doc}]prd.md){.reference .internal} page for more info about PRD.

An HD run has several stages, which are repeated each time an event occurs, as explained below. The logic for an HD run is as follows:

:::: {.highlight-none .notranslate}
::: highlight
    quench
    create initial list of bonds

    while (time remains):
      run dynamics for Nevent steps
      quench
      check for an event
      if event occurred: reset list of bonds
      restore pre-quench state
:::
::::

The list of bonds is the list of atom pairs of atoms that are within a short cutoff distance of each other after the system energy is minimized (quenched). This list is created and reset by a [[fix hyper/global]{.doc}]fix_hyper_global.md){.reference .internal} or [[fix hyper/local]{.doc}]fix_hyper_local.md){.reference .internal} command specified as *fix-ID*. At every dynamics timestep, the same fix selects one of more bonds to apply a bias potential to.

::: {.admonition .note}
Note

The style of fix associated with the specified *fix-ID* determines whether you are running the global versus local hyperdynamics algorithm.
:::

Dynamics (with the bias potential) is run continuously, stopping every *Nevent* steps to check if a transition event has occurred. The specified *N* for total steps must be a multiple of *Nevent*. check is performed by quenching the system and comparing the resulting atom coordinates to the coordinates from the previous basin.

A quench is an energy minimization and is performed by whichever algorithm has been defined by the [[min_style]{.doc}]min_style.md){.reference .internal} command. Minimization parameters may be set via the [[min_modify]{.doc}]min_modify.md){.reference .internal} command and by the *min* keyword of the hyper command. The latter are the settings that would be used with the [[minimize]{.doc}]minimize.md){.reference .internal} command. Note that typically, you do not need to perform a highly-converged minimization to detect a transition event, though you may need to in order to prevent a set of atoms in the system from relaxing to a saddle point.

The event check is performed by a compute with the specified *compute-ID*. Currently there is only one compute that works with the hyper command, which is the [[compute event/displace]{.doc}]compute_event_displace.md){.reference .internal} command. Other event-checking computes may be added. [[Compute event/displace]{.doc}]compute_event_displace.md){.reference .internal} checks whether any atom in the compute group has moved further than a specified threshold distance. If so, an event has occurred.

If this happens, the list of bonds is reset, since some bond pairs are likely now too far apart, and new pairs are likely close enough to be considered a bond. The pre-quenched state of the system (coordinates and velocities) is restored, and dynamics continue.

At the end of the hyper run, a variety of statistics are output to the screen and logfile. These include info relevant to both global and local hyperdynamics, such as the number of events and the elapsed hyper time (accelerated time), And it includes info specific to one or the other, depending on which style of fix was specified by *fix-ID*.

------------------------------------------------------------------------

The optional keywords operate as follows.

As explained above, the *min* keyword can be used to specify parameters for the quench. Their meaning is the same as for the [[minimize]{.doc}]minimize.md){.reference .internal} command

The *dump* keyword can be used to trigger a specific dump command with the specified *dump-ID* to output a snapshot each time an event is detected. It can be specified multiple times with different *dump-ID* values, as in the example above. These snapshots will be for the quenched state of the system on a timestep that is a multiple of *Nevent*, i.e. a timestep after the event has occurred. Note that any dump command in the input script will also output snapshots at whatever timestep interval it defines via its *N* argument; see the [[dump]{.doc}]dump.md){.reference .internal} command for details. This means if you only want a particular dump to output snapshots when events are detected, you should specify its *N* as a value larger than the length of the hyperdynamics run.

As in the code logic above, the bond list is normally only reset when an event occurs. The *rebond* keyword will force a reset of the bond list every *Nrebond* steps, even if an event has not occurred. *Nrebond* must be a multiple of *Nevent*. This can be useful to check if more frequent resets alter event statistics, perhaps because the parameters chosen for defining what is a bond and what is an event are producing bad dynamics in the presence of the bias potential.
::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command can only be used if LAMMPS was built with the REPLICA package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix hyper/global]{.doc}]fix_hyper_global.md){.reference .internal}, [[fix hyper/local]{.doc}]fix_hyper_local.md){.reference .internal}, [[compute event/displace]{.doc}]compute_event_displace.md){.reference .internal}, [[prd]{.doc}]prd.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are min = 0.1 0.1 40 50 and time = steps.

------------------------------------------------------------------------

**(Voter2013)** S. Y. Kim, D. Perez, A. F. Voter, J Chem Phys, 139, 144110 (2013).

**(Voter2002)** Voter, Montalenti, Germann, Annual Review of Materials Research 32, 321 (2002).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

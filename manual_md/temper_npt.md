::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#temper-npt-command .section}
[]{#index-0}

# temper/npt command[](#temper-npt-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    temper/npt  N M temp fix-ID seed1 seed2 pressure index
:::
::::

- N = total \# of timesteps to run

- M = attempt a tempering swap every this many steps

- temp = initial temperature for this ensemble

- fix-ID = ID of the fix that will control temperature and pressure during the run

- seed1 = random \# seed used to decide on adjacent temperature to partner with

- seed2 = random \# seed for Boltzmann factor in Metropolis swap

- pressure = setpoint pressure for the ensemble

- index = which temperature (0 to N-1) I am simulating (optional)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    temper/npt 100000 100 $t nptfix 0 58728 1
    temper/npt 2500000 1000 300 nptfix  0 32285 $p
    temper/npt 5000000 2000 $t nptfix 0 12523 1 $w
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Run a parallel tempering or replica exchange simulation using multiple replicas (ensembles) of a system in the isothermal-isobaric (NPT) ensemble. The command temper/npt works like [[temper]{.doc}]temper.md){.reference .internal} but requires running replicas in the NPT ensemble instead of the canonical (NVT) ensemble and allows for pressure to be set in the ensembles. These multiple ensembles can run in parallel at different temperatures or different pressures. The acceptance criteria for temper/npt is specific to the NPT ensemble and can be found in references [[(Okabe)]{.std .std-ref}](#okabe2){.reference .internal} and [[(Mori)]{.std .std-ref}](#mori2){.reference .internal}.

Apart from the difference in acceptance criteria and the specification of pressure, this command works much like the [[temper]{.doc}]temper.md){.reference .internal} command. See the documentation on [[temper]{.doc}]temper.md){.reference .internal} for information on how the parallel tempering is handled in general.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command can only be used if LAMMPS was built with the REPLICA package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This command should be used with a fix that maintains the isothermal-isobaric (NPT) ensemble.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[temper]{.doc}]temper.md){.reference .internal}, [[variable]{.doc}]variable.md){.reference .internal}, [[fix_npt]{.doc}]fix_nh.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

**(Okabe)** T. Okabe, M. Kawata, Y. Okamoto, M. Masuhiro, Chem. Phys. Lett., 335, 435-439 (2001).

**(Mori)** Y. Mori, Y. Okamoto, J. Phys. Soc. Jpn., 7, 074003 (2010).
:::
:::::::::::::
::::::::::::::
:::::::::::::::

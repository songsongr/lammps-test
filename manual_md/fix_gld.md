:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-gld-command .section}
[]{#index-0}

# fix gld command[](#fix-gld-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID gld Tstart Tstop N_k seed series c_1 tau_1 ... c_N_k tau_N_k keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- gld = style name of this fix command

- Tstart,Tstop = desired temperature at start/end of run (temperature units)

- N_k = number of terms in the Prony series representation of the memory kernel

- seed = random number seed to use for white noise (positive integer)

- series = *pprony* is presently the only available option

- c_k = the weight of the kth term in the Prony series (mass per time units)

- tau_k = the time constant of the kth term in the Prony series (time units)

- zero or more keyword/value pairs may be appended

  ``` literal-block
  keyword = frozen or zero
    frozen value = no or yes
      no = initialize extended variables using values drawn from equilibrium distribution at Tstart
      yes = initialize extended variables to zero (i.e., from equilibrium distribution at zero temperature)
    zero value = no or yes
      no = do not set total random force to zero
      yes = set total random force to zero
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all gld 1.0 1.0 2 82885 pprony 0.5 1.0 1.0 2.0 frozen yes zero yes
    fix 3 rouse gld 7.355 7.355 4 48823 pprony 107.1 0.02415 186.0 0.04294 428.6 0.09661 1714 0.38643
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Applies Generalized Langevin Dynamics to a group of atoms, as described in [[(Baczewski)]{.std .std-ref}](#baczewski){.reference .internal}. This is intended to model the effect of an implicit solvent with a temporally non-local dissipative force and a colored Gaussian random force, consistent with the Fluctuation-Dissipation Theorem. The functional form of the memory kernel associated with the temporally non-local force is constrained to be a Prony series.

::: {.admonition .note}
Note

While this fix bears many similarities to [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, it has one significant difference. Namely, [[fix gld]{.doc}](#){.reference .internal} performs time integration, whereas [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} does NOT. To this end, the specification of another fix to perform time integration, such as [[fix nve]{.doc}]fix_nve.md){.reference .internal}, is NOT necessary.
:::

With this fix active, the force on the *j*th atom is given as

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathbf{F}\_{j}(t) = & \\mathbf{F}\^C_j(t)-\\int \\limits\_{0}\^{t} \\Gamma_j(t-s) \\mathbf{v}\_j(s)\~\\text{d}s + \\mathbf{F}\^R_j(t) \\\\ \\Gamma_j(t-s) = & \\sum \\limits\_{k=1}\^{N_k} \\frac{c_k}{\\tau_k} e\^{-(t-s)/\\tau_k} \\\\ \\langle\\mathbf{F}\^R_j(t),\\mathbf{F}\^R_j(s)\\rangle = & \\text{k\$\_\\text{B}\$T} \~\\Gamma_j(t-s)\\end{split}\\\]
:::

Here, the first term is representative of all conservative (pairwise, bonded, etc) forces external to this fix, the second is the temporally non-local dissipative force given as a Prony series, and the third is the colored Gaussian random force.

The Prony series form of the memory kernel is chosen to enable an extended variable formalism, with a number of exemplary mathematical features discussed in [[(Baczewski)]{.std .std-ref}](#baczewski){.reference .internal}. In particular, [\\(3N_k\\)]{.math .notranslate .nohighlight} extended variables are added to each atom, which effect the action of the memory kernel without having to explicitly evaluate the integral over time in the second term of the force. This also has the benefit of requiring the generation of uncorrelated random forces, rather than correlated random forces as specified in the third term of the force.

Presently, the Prony series coefficients are limited to being greater than or equal to zero, and the time constants are limited to being greater than zero. To this end, the value of series MUST be set to *pprony*, for now. Future updates will allow for negative coefficients and other representations of the memory kernel. It is with these updates in mind that the series option was included.

The units of the Prony series coefficients are chosen to be mass per time to ensure that the numerical integration scheme stably approaches the Newtonian and Langevin limits. Details of these limits, and the associated numerical concerns are discussed in [[(Baczewski)]{.std .std-ref}](#baczewski){.reference .internal}.

The desired temperature at each timestep is ramped from *Tstart* to *Tstop* over the course of the next run.

The random \# *seed* must be a positive integer. A Marsaglia random number generator is used. Each processor uses the input seed to generate its own unique seed and its own stream of random numbers. Thus the dynamics of the system will not be identical on two runs on different numbers of processors.

------------------------------------------------------------------------

The keyword/value option pairs are used in the following ways.

The keyword *frozen* can be used to specify how the extended variables associated with the GLD memory kernel are initialized. Specifying no (the default), the initial values are drawn at random from an equilibrium distribution at *Tstart*, consistent with the Fluctuation-Dissipation Theorem. Specifying yes, initializes the extended variables to zero.

The keyword *zero* can be used to eliminate drift due to the thermostat. Because the random forces on different atoms are independent, they do not sum exactly to zero. As a result, this fix applies a small random force to the entire system, and the center-of-mass of the system undergoes a slow random walk. If the keyword *zero* is set to *yes*, the total random force is set exactly to zero by subtracting off an equal part of it from each atom in the group. As a result, the center-of-mass of a system with zero initial momentum will not drift over time.
:::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

The instantaneous values of the extended variables are written to [[binary restart files]{.doc}]restart.md){.reference .internal}. Because the state of the random number generator is not saved in restart files, this means you cannot do "exact" restarts with this fix, where the simulation continues on the same as if no restart had taken place. However, in a statistical sense, a restarted simulation should produce the same behavior.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}.

This fix can ramp its target temperature over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, [[fix viscous]{.doc}]fix_viscous.md){.reference .internal}, [[pair_style dpd/tstat]{.doc}]pair_dpd.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are frozen = no, zero = no.

------------------------------------------------------------------------

**(Baczewski)** A.D. Baczewski and S.D. Bond, J. Chem. Phys. 139, 044107 (2013).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

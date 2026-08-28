::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#fix-langevin-spin-command .section}
[]{#index-0}

# fix langevin/spin command[](#fix-langevin-spin-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID langevin/spin T Tdamp seed
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- langevin/spin = style name of this fix command

- T = desired temperature of the bath (temperature units, K in metal units)

- Tdamp = transverse magnetic damping parameter (adim)

- seed = random number seed to use for white noise (positive integer)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 2 all langevin/spin 300.0 0.01 21
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply a Langevin thermostat as described in [[(Mayergoyz)]{.std .std-ref}](#mayergoyz1){.reference .internal} to the magnetic spins associated to the atoms. Used with [[fix nve/spin]{.doc}]fix_nve_spin.md){.reference .internal}, this command performs Brownian dynamics (BD). A random torque and a transverse dissipation are applied to each spin i according to the following stochastic differential equation:

::: {.math .notranslate .nohighlight}
\\\[ \\frac{d \\vec{s}\_{i}}{dt} = \\frac{1}{\\left(1+\\lambda\^2 \\right)} \\left( \\left( \\vec{\\omega}\_{i} +\\vec{\\eta} \\right) \\times \\vec{s}\_{i} + \\lambda\\, \\vec{s}\_{i} \\times\\left( \\vec{\\omega}\_{i} \\times\\vec{s}\_{i} \\right) \\right)\\\]
:::

with [\\(\\lambda\\)]{.math .notranslate .nohighlight} the transverse damping, and [\\(\\eta\\)]{.math .notranslate .nohighlight} a random vector. This equation is referred to as the stochastic Landau-Lifshitz (sLL) equation.

The components of [\\(\\eta\\)]{.math .notranslate .nohighlight} are drawn from a Gaussian probability law. Their amplitude is defined as a proportion of the temperature of the external thermostat T (in K in metal units).

More details about this implementation are reported in [[(Tranchida)]{.std .std-ref}](#tranchida2){.reference .internal}.

Note: due to the form of the sLL equation, this fix has to be defined just before the nve/spin fix (and after all other magnetic fixes). As an example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all precession/spin zeeman 0.01 0.0 0.0 1.0
    fix 2 all langevin/spin 300.0 0.01 21
    fix 3 all nve/spin lattice moving
:::
::::

is correct, but defining a force/spin command after the langevin/spin command would give an error message.

Note: The random \# *seed* must be a positive integer. A Marsaglia random number generator is used. Each processor uses the input seed to generate its own unique seed and its own stream of random numbers. Thus the dynamics of the system will not be identical on two runs on different numbers of processors.
::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. Because the state of the random number generator is not saved in restart files, this means you cannot do "exact" restarts with this fix, where the simulation continues on the same as if no restart had taken place. However, in a statistical sense, a restarted simulation should produce the same behavior.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *langevin/spin* fix is part of the SPIN package. This style is only enabled if LAMMPS was built with this package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The numerical integration has to be performed with *fix nve/spin* when *fix langevin/spin* is enabled.

This fix has to be the last defined magnetic fix before the time integration fix (e.g. *fix nve/spin*).
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nve/spin]{.doc}]fix_nve_spin.md){.reference .internal}, [[fix precession/spin]{.doc}]fix_precession_spin.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Mayergoyz)** I.D. Mayergoyz, G. Bertotti, C. Serpico (2009). Elsevier (2009)

**(Tranchida)** Tranchida, Plimpton, Thibaudeau and Thompson, Journal of Computational Physics, 372, 406-425, (2018).
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

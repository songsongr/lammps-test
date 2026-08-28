:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-accelerate-cos-command .section}
[]{#index-0}

# fix accelerate/cos command[](#fix-accelerate-cos-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID accelerate value
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- accelerate/cos = style name of this fix command

- value = amplitude of acceleration (in unit of velocity/time)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all accelerate/cos 2.0e-7
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Give each atom a acceleration in x-direction based on its z coordinate. The acceleration is a periodic function along the z-direction:

::: {.math .notranslate .nohighlight}
\\\[a\_{x}(z) = A \\cos \\left(\\frac{2 \\pi z}{l\_{z}}\\right)\\\]
:::

where [\\(A\\)]{.math .notranslate .nohighlight} is the acceleration amplitude, [\\(l_z\\)]{.math .notranslate .nohighlight} is the [\\(z\\)]{.math .notranslate .nohighlight}-length of the simulation box. At steady state, the acceleration generates a velocity profile:

::: {.math .notranslate .nohighlight}
\\\[v\_{x}(z) = V \\cos \\left(\\frac{2 \\pi z}{l\_{z}}\\right)\\\]
:::

The generated velocity amplitude [\\(V\\)]{.math .notranslate .nohighlight} is related to the shear viscosity [\\(\\eta\\)]{.math .notranslate .nohighlight} by:

::: {.math .notranslate .nohighlight}
\\\[V = \\frac{A \\rho}{\\eta}\\left(\\frac{l\_{z}}{2 \\pi}\\right)\^{2}\\\]
:::

and it can be obtained from ensemble average of the velocity profile:

::: {.math .notranslate .nohighlight}
\\\[V = \\frac{\\sum\\limits_i 2 m\_{i} v\_{i, x} \\cos \\left(\\frac{2 \\pi z_i}{l\_{z}}\\right)}{\\sum\\limits_i m\_{i}},\\\]
:::

where [\\(m_i\\)]{.math .notranslate .nohighlight}, [\\(v\_{i,x}\\)]{.math .notranslate .nohighlight}, and [\\(z_i\\)]{.math .notranslate .nohighlight} are the mass, [\\(x\\)]{.math .notranslate .nohighlight}-component velocity, and [\\(z\\)]{.math .notranslate .nohighlight}-coordinate of a particle, respectively.

The velocity amplitude [\\(V\\)]{.math .notranslate .nohighlight} can be calculated with [[compute viscosity/cos]{.doc}]compute_viscosity_cos.md){.reference .internal}, which enables viscosity calculation with periodic perturbation method, as described by [[Hess]{.std .std-ref}](#hess2){.reference .internal}. Because the applied acceleration drives the system away from equilibration, the calculated shear viscosity is lower than the intrinsic viscosity due to the shear-thinning effect. Extrapolation to zero acceleration should generally be performed to predict the zero-shear viscosity. As the shear stress decreases, the signal-to-noise ratio decreases rapidly, and the simulation time must be extended accordingly to get converged results.

In order to get meaningful results, the group ID of this fix should be all.
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to binary restart files. None of the fix_modify options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various output commands. No parameter of this fix can be used with the start/stop keywords of the run command.

This fix is not invoked during energy minimization.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MISC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Since this fix depends on the [\\(z\\)]{.math .notranslate .nohighlight}-coordinate of atoms, it cannot be used in 2d simulations.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute viscosity/cos]{.doc}]compute_viscosity_cos.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Hess)** Hess, B. Journal of Chemical Physics 2002, 116 (1), 209--217.
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

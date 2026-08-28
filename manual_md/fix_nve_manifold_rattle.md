:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-nve-manifold-rattle-command .section}
[]{#index-0}

# fix nve/manifold/rattle command[](#fix-nve-manifold-rattle-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nve/manifold/rattle tol maxit manifold manifold-args keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nve/manifold/rattle = style name of this fix command

- tol = tolerance to which Newton iteration must converge

- maxit = maximum number of iterations to perform

- manifold = name of the manifold

- manifold-args = parameters for the manifold

- one or more keyword/value pairs may be appended

  ``` literal-block
  keyword = every
    every values = N
      N = print info about iteration every N steps. N = 0 means no output
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nve/manifold/rattle 1e-4 10 sphere 5.0
    fix step all nve/manifold/rattle 1e-8 100 ellipsoid 2.5 2.5 5.0 every 25
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform constant NVE integration to update position and velocity for atoms constrained to a curved surface (manifold) in the group each timestep. The constraint is handled by RATTLE [[(Andersen)]{.std .std-ref}](#andersen1){.reference .internal} written out for the special case of single-particle constraints as explained in [[(Paquay)]{.std .std-ref}](#paquay2){.reference .internal}. V is volume; E is energy. This way, the dynamics of particles constrained to curved surfaces can be studied. If combined with [[fix langevin]{.doc}]fix_langevin.md){.reference .internal}, this generates Brownian motion of particles constrained to a curved surface. For a list of currently supported manifolds and their parameters, see the [[Howto manifold]{.doc}]Howto_manifold.md){.reference .internal} doc page.

Note that the particles must initially be close to the manifold in question. If not, RATTLE will not be able to iterate until the constraint is satisfied, and an error is generated. For simple manifolds this can be achieved with *region* and *create_atoms* commands, but for more complex surfaces it might be more useful to write a script.

The manifold args may be equal-style variables, like so:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable R equal "ramp(5.0,3.0)"
    fix shrink_sphere all nve/manifold/rattle 1e-4 10 sphere v_R
:::
::::

In this case, the manifold parameter will change in time according to the variable. This is not a problem for the time integrator as long as the change of the manifold is slow with respect to the dynamics of the particles. Note that if the manifold has to exert work on the particles because of these changes, the total energy might not be conserved.
:::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MANIFOLD package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

------------------------------------------------------------------------

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nvt/manifold/rattle]{.doc}]fix_nvt_manifold_rattle.md){.reference .internal}, [[fix manifoldforce]{.doc}]fix_manifoldforce.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

every = 0, tchain = 3

------------------------------------------------------------------------

**(Andersen)** Andersen, J. Comp. Phys. 52, 24, (1983).

**(Paquay)** Paquay and Kusters, Biophys. J., 110, 6, (2016). preprint available at [arXiv:1411.3019](https://arxiv.org/abs/1411.3019/){.reference .external}.
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

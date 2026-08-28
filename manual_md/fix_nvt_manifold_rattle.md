::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#fix-nvt-manifold-rattle-command .section}
[]{#index-0}

# fix nvt/manifold/rattle command[](#fix-nvt-manifold-rattle-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nvt/manifold/rattle tol maxit manifold manifold-args keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nvt/manifold/rattle = style name of this fix command

- tol = tolerance to which Newton iteration must converge

- maxit = maximum number of iterations to perform

- manifold = name of the manifold

- manifold-args = parameters for the manifold

- one or more keyword/value pairs may be appended

  ``` literal-block
  keyword = temp or tchain or every
    temp values = Tstart Tstop Tdamp
      Tstart, Tstop = external temperature at start/end of run
      Tdamp = temperature damping parameter (time units)
    tchain value = N
      N = length of thermostat chain (1 = single thermostat)
    every value = N
      N = print info about iteration every N steps. N = 0 means no output
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nvt/manifold/rattle 1e-4 10 cylinder 3.0 temp 1.0 1.0 10.0
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix combines the RATTLE-based [[(Andersen)]{.std .std-ref}](#andersen2){.reference .internal} time integrator of [[fix nve/manifold/rattle]{.doc}]fix_nve_manifold_rattle.md){.reference .internal} [[(Paquay)]{.std .std-ref}](#paquay3){.reference .internal} with a Nose-Hoover-chain thermostat to sample the canonical ensemble of particles constrained to a curved surface (manifold). This sampling does suffer from discretization bias of O(dt). For a list of currently supported manifolds and their parameters, see the [[Howto manifold]{.doc}]Howto_manifold.md){.reference .internal} doc page.
:::

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

[[fix nve/manifold/rattle]{.doc}](#){.reference .internal}, [[fix manifoldforce]{.doc}]fix_manifoldforce.md){.reference .internal} **Default:** every = 0

------------------------------------------------------------------------

**(Andersen)** Andersen, J. Comp. Phys. 52, 24, (1983).

**(Paquay)** Paquay and Kusters, Biophys. J., 110, 6, (2016). preprint available at [arXiv:1411.3019](https://arxiv.org/abs/1411.3019/){.reference .external}.
:::
:::::::::::::
::::::::::::::
:::::::::::::::

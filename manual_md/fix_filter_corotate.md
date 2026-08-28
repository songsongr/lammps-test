:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-filter-corotate-command .section}
[]{#index-0}

# fix filter/corotate command[](#fix-filter-corotate-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID filter/corotate keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- one or more constraint/value pairs are appended

- constraint = *b* or *a* or *t* or *m*

  ``` literal-block
  b values = one or more bond types
  a values = one or more angle types
  t values = one or more atom types
  m value = one or more mass values
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    timestep 8
    run_style respa 3 2 8 bond 1 pair 2 kspace 3
    fix cor all filter/corotate m 1.0

    fix cor all filter/corotate b 4 19 a 3 5 2
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix implements a corotational filter for a mollified impulse method. In biomolecular simulations, it allows the usage of larger timesteps for long-range electrostatic interactions. For details, see [[(Fath)]{.std .std-ref}](#fath2017){.reference .internal}.

When using [[run_style respa]{.doc}]run_style.md){.reference .internal} for a biomolecular simulation with high-frequency covalent bonds, the outer time-step is restricted to below \~ 4fs due to resonance problems. This fix filters the outer stage of the respa and thus a larger (outer) time-step can be used. Since in large biomolecular simulations the computation of the long-range electrostatic contributions poses a major bottleneck, this can significantly accelerate the simulation.

The filter computes a cluster decomposition of the molecular structure following the criteria indicated by the options a, b, t and m. This process is similar to the approach in [[fix shake]{.doc}]fix_shake.md){.reference .internal}, however, the clusters are not kept constrained. Instead, the position is slightly modified only for the computation of long-range forces. A good cluster decomposition constitutes in building clusters which contain the fastest covalent bonds inside clusters.

If the clusters are chosen suitably, the [[run_style respa]{.doc}]run_style.md){.reference .internal} is stable for outer timesteps of at least 8fs.
:::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about these fixes is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to these fixes. No global or per-atom quantities are stored by these fixes for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of these fixes can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. These fixes are not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Currently, it does not support [[molecule templates]{.doc}]molecule.md){.reference .internal}.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Fath)** Fath, Hochbruck, Singh, J Comp Phys, 333, 180-198 (2017).
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

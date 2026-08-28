::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#fix-manifoldforce-command .section}
[]{#index-0}

# fix manifoldforce command[](#fix-manifoldforce-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID manifoldforce manifold manifold-args ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- manifold = name of the manifold

- manifold-args = parameters for the manifold
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix constrain all manifoldforce sphere 5.0
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix subtracts each time step from the force the component along the normal of the specified [[manifold]{.doc}]Howto_manifold.md){.reference .internal}. This can be used in combination with [[minimize]{.doc}]minimize.md){.reference .internal} to remove overlap between particles while keeping them (roughly) constrained to the given manifold, e.g. to set up a run with [[fix nve/manifold/rattle]{.doc}]fix_nve_manifold_rattle.md){.reference .internal}. I have found that only *hftn* and *quickmin* with a very small time step perform adequately though.
:::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the MANIFOLD package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Only use this with *min_style hftn* or *min_style quickmin*. If not, the constraints will not be satisfied very well at all. A warning is generated if the *min_style* is incompatible but no error.
:::

------------------------------------------------------------------------

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nve/manifold/rattle]{.doc}]fix_nve_manifold_rattle.md){.reference .internal}, [[fix nvt/manifold/rattle]{.doc}]fix_nvt_manifold_rattle.md){.reference .internal}
:::
:::::::::::::
::::::::::::::
:::::::::::::::

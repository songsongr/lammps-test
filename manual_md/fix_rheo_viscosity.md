::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#fix-rheo-viscosity-command .section}
[]{#index-0}

# fix rheo/viscosity command[](#fix-rheo-viscosity-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-none .notranslate}
::: highlight
    fix ID group-ID rheo/viscosity type1 pstyle1 args1 ... typeN pstyleN argsN
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- rheo/viscosity = style name of this fix command

- one or more types and viscosity styles must be appended

- types = lists of types (see below)

- vstyle = *constant* or *power*

  ``` literal-block
  constant args = eta
    eta = viscosity

  power args = eta, gd0, K, n
    eta = viscosity
    gd0 = critical strain rate
    K = consistency index
    n = power-law exponent
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all rheo/viscosity * constant 1.0
    fix 1 all rheo/viscosity 1 constant 1.0 2 power 0.1 5e-4 0.001 0.5
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 29Aug2024.]{.versionmodified .added}
:::

This fix defines a viscosity for RHEO particles. One can define different viscosities for different atom types, but a viscosity must be specified for every atom type.

One first defines the atom *types*. A wild-card asterisk can be used in place of or in conjunction with the *types* argument to set values for multiple atom types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of atom types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive).

The *types* definition is followed by the viscosity style, *vstyle*. Two options are available, *constant* and *power*. Style *constant* simply applies a constant value of the viscosity *eta* to each particle of the assigned type. Style *power* is a Hershchel-Bulkley constitutive equation for the stress [\\(\\tau\\)]{.math .notranslate .nohighlight}

::: {.math .notranslate .nohighlight}
\\\[\\tau = \\left(\\frac{\\tau_0}{\\dot{\\gamma}} + K \\dot{\\gamma}\^{n - 1}\\right) \\dot{\\gamma}, \\tau \\ge \\tau_0\\\]
:::

where [\\(\\dot{\\gamma}\\)]{.math .notranslate .nohighlight} is the strain rate and [\\(\\tau_0\\)]{.math .notranslate .nohighlight} is the critical yield stress, below which [\\(\\dot{\\gamma} = 0.0\\)]{.math .notranslate .nohighlight}. To avoid divergences, this expression is regularized by defining a critical strain rate *gd0*. If the local strain rate on a particle falls below this limit, a constant viscosity of *eta* is assigned. This implies a value of

::: {.math .notranslate .nohighlight}
\\\[\\tau_0 = \\eta \\dot{\\gamma}\_0 - K \\dot{\\gamma}\_0\^N\\\]
:::
::::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix must be used with an atom style that includes viscosity such as atom_style rheo or rheo/thermal. This fix must be used in conjunction with [[fix rheo]{.doc}]fix_rheo.md){.reference .internal}. The fix group must be set to all. Only one instance of fix rheo/viscosity can be defined.

This fix is part of the RHEO package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix rheo]{.doc}]fix_rheo.md){.reference .internal}, [[pair rheo]{.doc}]pair_rheo.md){.reference .internal}, [[compute rheo/property/atom]{.doc}]compute_rheo_property_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

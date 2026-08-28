:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#fix-rheo-pressure-command .section}
[]{#index-0}

# fix rheo/pressure command[](#fix-rheo-pressure-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-none .notranslate}
::: highlight
    fix ID group-ID rheo/pressure type1 pstyle1 args1 ... typeN pstyleN argsN
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- rheo/pressure = style name of this fix command

- one or more types and pressure styles must be appended

- types = lists of types (see below)

- pstyle = *linear* or *tait/water* or *tait/general* or *cubic* or *ideal/gas* or *background*

  ``` literal-block
  linear args = none
  tait/water args = none
  tait/general args = exponent \(gamma\) (unitless)
  cubic args = cubic prefactor \(A_3\) (pressure/density^2)
  ideal/gas args = heat capacity ratio \(gamma\) (unitless)
  background args = background pressure \(P[b]\) (pressure)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all rheo/pressure * linear
    fix 1 all rheo/pressure 1 linear 2 cubic 10.0
    fix 1 all rheo/pressure * linear * background 0.1
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 29Aug2024.]{.versionmodified .added}
:::

This fix defines a pressure equation of state for RHEO particles. One can define different equations of state for different atom types. An equation must be specified for every atom type.

One first defines the atom *types*. A wild-card asterisk can be used in place of or in conjunction with the *types* argument to set values for multiple atom types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of atom types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive).

The *types* definition is followed by the pressure style, *pstyle*. Current options *linear*, *taitwater*, and *cubic*. Style *linear* is a linear equation of state with a particle pressure [\\(P\\)]{.math .notranslate .nohighlight} calculated as

::: {.math .notranslate .nohighlight}
\\\[P = c\^2 (\\rho - \\rho_0)\\\]
:::

where [\\(c\\)]{.math .notranslate .nohighlight} is the speed of sound, [\\(\\rho_0\\)]{.math .notranslate .nohighlight} is the equilibrium density, and [\\(\\rho\\)]{.math .notranslate .nohighlight} is the current density of a particle. The numerical values of [\\(c\\)]{.math .notranslate .nohighlight} and [\\(\\rho_0\\)]{.math .notranslate .nohighlight} are set in [[fix rheo]{.doc}]fix_rheo.md){.reference .internal}. Style *cubic* is a cubic equation of state which has an extra argument [\\(A_3\\)]{.math .notranslate .nohighlight},

::: {.math .notranslate .nohighlight}
\\\[P = c\^2 ((\\rho - \\rho_0) + A_3 (\\rho - \\rho_0)\^3) .\\\]
:::

Style *tait/water* is Tait's equation of state:

::: {.math .notranslate .nohighlight}
\\\[P = \\frac{c\^2 \\rho_0}{7} \\biggl\[\\left(\\frac{\\rho}{\\rho_0}\\right)\^{7} - 1\\biggr\].\\\]
:::

Style *tait/general* generalizes this equation of state

::: {.math .notranslate .nohighlight}
\\\[P = \\frac{c\^2 \\rho_0}{\\gamma} \\biggl\[\\left(\\frac{\\rho}{\\rho_0}\\right)\^{\\gamma} - 1\\biggr\]\\\]
:::

where [\\(\\gamma\\)]{.math .notranslate .nohighlight} is an exponent.

Style *ideal/gas* is the ideal gas equation of state

::: {.math .notranslate .nohighlight}
\\\[P = (\\gamma - 1) \\rho e\\\]
:::

where [\\(\\gamma\\)]{.math .notranslate .nohighlight} is the heat capacity ratio and [\\(e\\)]{.math .notranslate .nohighlight} is the internal energy of a particle per unit mass. This style is only compatible with atom style rheo/thermal. Note that when using this style, the speed of sound is no longer constant such that the value of [\\(c\\)]{.math .notranslate .nohighlight} specified in [[fix rheo]{.doc}]fix_rheo.md){.reference .internal} is not used.

The *background* style acts differently than the rest as it only adds a constant background pressure shift [\\(P\[b\]\\)]{.math .notranslate .nohighlight} to all atoms of the designated types. Therefore, this style must be used in conjunction with another style that specifies an equation of state.
:::::::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix must be used with an atom style that includes density such as atom_style rheo or rheo/thermal. This fix must be used in conjunction with [[fix rheo]{.doc}]fix_rheo.md){.reference .internal}. The fix group must be set to all. Only one instance of fix rheo/pressure can be defined.

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
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

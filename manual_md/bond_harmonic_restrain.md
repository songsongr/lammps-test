:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#bond-style-harmonic-restrain-command .section}
[]{#index-0}

# bond_style harmonic/restrain command[](#bond-style-harmonic-restrain-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style harmonic/restrain
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style harmonic
    bond_coeff 5 80.0
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 28Mar2023.]{.versionmodified .added}
:::

The *harmonic/restrain* bond style uses the potential

::: {.math .notranslate .nohighlight}
\\\[E = K (r - r\_{t=0})\^2\\\]
:::

where [\\(r\_{t=0}\\)]{.math .notranslate .nohighlight} is the distance between the bonded atoms at the beginning of the first [[run]{.doc}]run.md){.reference .internal} or [[minimize]{.doc}]minimize.md){.reference .internal} command after the bond style has been defined (*t=0*). Note that the usual 1/2 factor is included in [\\(K\\)]{.math .notranslate .nohighlight}. This will effectively restrain bonds to their initial length, whatever that is. This is where this bond style differs from [[bond style harmonic]{.doc}]bond_harmonic.md){.reference .internal} where the bond length is set through the per bond type coefficients.

The following coefficient must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands

- [\\(K\\)]{.math .notranslate .nohighlight} (energy/distance\^2)

This bond style differs from other options to add harmonic restraints like [[fix restrain]{.doc}]fix_restrain.md){.reference .internal} or [[pair style list]{.doc}]pair_list.md){.reference .internal} or [[fix colvars]{.doc}]fix_colvars.md){.reference .internal} in that it requires a bond topology, and thus the defined bonds will trigger exclusion of special neighbors from the neighbor list according to the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} settings.
:::::

::: {#restart-info .section}
## Restart info[](#restart-info "Link to this heading"){.headerlink}

This bond style supports the [[write_restart]{.doc}]write_restart.md){.reference .internal} and [[read_restart]{.doc}]read_restart.md){.reference .internal} commands. The state of the initial bond lengths is stored with restart files and read back.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the EXTRA-MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This bond style maintains internal data to determine the original bond lengths [\\(r\_{t=0}\\)]{.math .notranslate .nohighlight}. This information will be written to [[binary restart files]{.doc}]write_restart.md){.reference .internal} but **not** to [[data files]{.doc}]write_data.md){.reference .internal}. Thus, continuing a simulation is *only* possible with [[read_restart]{.doc}]read_restart.md){.reference .internal}. When using the [[read_data command]{.doc}]read_data.md){.reference .internal}, the reference bond lengths [\\(r\_{t=0}\\)]{.math .notranslate .nohighlight} will be re-initialized from the current geometry.

This bond style cannot be used with [[fix shake or fix rattle]{.doc}]fix_shake.md){.reference .internal}, with [[fix filter/corotate]{.doc}]fix_filter_corotate.md){.reference .internal}, or any [[tip4p pair style]{.doc}]pair_lj_cut_tip4p.md){.reference .internal} since there is no specific equilibrium distance for a given bond type.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[bond_harmonic]{.doc}]bond_harmonic.md){.reference .internal}, [[fix restrain]{.doc}]fix_restrain.md){.reference .internal}, [[pair style list]{.doc}]pair_list.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

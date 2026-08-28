::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#fix-drude-command .section}
[]{#index-0}

# fix drude command[](#fix-drude-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID drude flag1 flag2 ... flagN
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- drude = style name of this fix command

- flag1 flag2 ... flagN = Drude flag for each atom type (1 to N) in the system
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all drude 1 1 0 1 0 2 2 2
    fix 1 all drude C C N C N D D D
:::
::::

Example input scripts available: examples/PACKAGES/drude
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Assign each atom type in the system to be one of 3 kinds of atoms within the Drude polarization model. This fix is designed to be used with the [[thermalized Drude oscillator model]{.doc}]Howto_drude.md){.reference .internal}. Polarizable models in LAMMPS are described on the [[Howto polarizable]{.doc}]Howto_polarizable.md){.reference .internal} doc page.

The three possible types can be designated with an integer (0,1,2) or capital letter (N,C,D):

- 0 or N = non-polarizable atom (not part of Drude model)

- 1 or C = Drude core

- 2 or D = Drude electron
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix should be invoked before any other commands that implement the Drude oscillator model, such as [[fix langevin/drude]{.doc}]fix_langevin_drude.md){.reference .internal}, [[fix tgnvt/drude]{.doc}]fix_tgnh_drude.md){.reference .internal}, [[fix drude/transform]{.doc}]fix_drude_transform.md){.reference .internal}, [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal}, [[pair_style thole]{.doc}]pair_thole.md){.reference .internal}.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix langevin/drude]{.doc}]fix_langevin_drude.md){.reference .internal}, [[fix tgnvt/drude]{.doc}]fix_tgnh_drude.md){.reference .internal}, [[fix drude/transform]{.doc}]fix_drude_transform.md){.reference .internal}, [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal}, [[pair_style thole]{.doc}]pair_thole.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::
::::::::::::::
:::::::::::::::

:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#fix-edpd-source-command .section}
[]{#index-1}[]{#index-0}

# fix edpd/source command[](#fix-edpd-source-command "Link to this heading"){.headerlink}
:::

::::::::::::::: {#fix-tdpd-source-command .section}
# fix tdpd/source command[](#fix-tdpd-source-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID edpd/source keyword values ...
    fix ID group-ID tdpd/source cc_index keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- edpd/source or tdpd/source = style name of this fix command

- index (only specified for tdpd/source) = index of chemical species (1 to Nspecies)

- keyword = *sphere* or *cuboid* or *region*

  ``` literal-block
  sphere args = cx cy cz radius source
    cx,cy,cz = x,y,z center of spherical domain (distance units)
    radius = radius of a spherical domain (distance units)
    source = heat source or concentration source (flux units, see below)
  cuboid values = cx cy cz dLx dLy dLz source
    cx,cy,cz = x,y,z center of a cuboid domain (distance units)
    dLx,dLy,dLz = x,y,z side length of a cuboid domain (distance units)
    source = heat source or concentration source (flux units, see below)
  region values = region-ID source
    region = ID of region for heat or concentration source
    source = heat source or concentration source (flux units, see below)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all edpd/source sphere 0.0 0.0 0.0 5.0 0.01
    fix 1 all edpd/source cuboid 0.0 0.0 0.0 20.0 10.0 10.0 -0.01
    fix 1 all tdpd/source 1 sphere 5.0 0.0 0.0 5.0 0.01
    fix 1 all tdpd/source 2 cuboid 0.0 0.0 0.0 20.0 10.0 10.0 0.01
    fix 1 all tdpd/source 1 region lower -0.01
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Fix *edpd/source* adds a heat source as an external heat flux to each atom in a spherical or cuboid domain, where the *source* is in units of energy/time. Fix *tdpd/source* adds an external concentration source of the chemical species specified by *index* as an external concentration flux for each atom in a spherical or cuboid domain, where the *source* is in units of mole/volume/time.

This command can be used to give an additional heat/concentration source term to atoms in a simulation, such as for a simulation of a heat conduction with a source term (see Fig.12 in [[(Li2014)]{.std .std-ref}](#li2014b){.reference .internal}) or diffusion with a source term (see Fig.1 in [[(Li2015)]{.std .std-ref}](#li2015b){.reference .internal}), as an analog of a periodic Poiseuille flow problem.

::: deprecated
[Deprecated since version 15Jun2023: ]{.versionmodified .deprecated}The *sphere* and *cuboid* keywords will be removed in a future version of LAMMPS. The same functionality and more can be achieved with a region.
:::

If the *sphere* keyword is used, the *cx, cy, cz, radius* values define a spherical domain to apply the source flux to.

If the *cuboid* keyword is used, the *cx, cy, cz, dLx, dLy, dLz* define a cuboid domain to apply the source flux to.

If the *region* keyword is used, the *region-ID* selects which [[region]{.doc}]region.md){.reference .internal} to apply the source flux to.
::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information of these fixes is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to these fixes. No global or per-atom quantities are stored by these fixes for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of these fixes can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. These fixes are not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These fixes are part of the DPD-MESO package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Fix *edpd/source* must be used with the [[pair_style edpd]{.doc}]pair_mesodpd.md){.reference .internal} command. Fix *tdpd/source* must be used with the [[pair_style tdpd]{.doc}]pair_mesodpd.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style edpd]{.doc}]pair_mesodpd.md){.reference .internal}, [[pair_style tdpd]{.doc}]pair_mesodpd.md){.reference .internal}, [[compute edpd/temp/atom]{.doc}]compute_edpd_temp_atom.md){.reference .internal}, [[compute tdpd/cc/atom]{.doc}]compute_tdpd_cc_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Li2014)** Z. Li, Y.-H. Tang, H. Lei, B. Caswell and G.E. Karniadakis, "Energy-conserving dissipative particle dynamics with temperature-dependent properties", J. Comput. Phys., 265: 113-127 (2014). DOI: 10.1016/j.jcp.2014.02.003

**(Li2015)** Z. Li, A. Yazdani, A. Tartakovsky and G.E. Karniadakis, "Transport dissipative particle dynamics model for mesoscopic advection-diffusion-reaction problems", J. Chem. Phys., 143: 014101 (2015). DOI: 10.1063/1.4923254
:::
:::::::::::::::
:::::::::::::::::
::::::::::::::::::

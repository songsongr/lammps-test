::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#region2vmd-command .section}
[]{#index-0}

# region2vmd command[](#region2vmd-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    region2vmd filename keyword arg ...
:::
::::

- filename = name of file to write VMD script commands to

- zero or more keyword/arg pairs may be appended

- keyword = *region* or *color* or *material* or *command*

  ``` literal-block
  region region-ID = name of region to translate to VMD graphics
  color color-name = set color for following visualized objects
  material material-name = set material for following visualized objects
  command string = string with custom VMD script command (in quotes)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    region2vmd regions.vmd material Opaque color red region c1 color green region c2
    region2vmd vizbox.vmd command "mol new system.lammpstrj waitfor all" region box
    region2vmd regdefs.vmd region upper region lower region hole
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 2Apr2025.]{.versionmodified .added}
:::

Write a [VMD](https://www.ks.uiuc.edu/Research/vmd/){.reference .external} Tcl script file with commands that aim to create a visualization of [[regions]{.doc}]region.md){.reference .internal}. There may be multiple region visualizations stored in a single file.

The visualization is implemented by creating a new (and empty) "VMD molecule" and then assigning a sequence of VMD graphics primitives to represent the region in VMD. Each region will be stored in a separate "VMD molecule" with the name "LAMMPS region \<region ID\>".

::: {.hint .admonition}
Visualization of regions with *dump image*

Regions can also be directly visualized within LAMMPS using the [[dump image]{.doc}]dump_image.md){.reference .internal} command. For more information, see [[Visualize LAMMPS snapshots]{.doc}]Howto_viz.md){.reference .internal}.
:::

The *region2vmd* command is followed by the filename for the resulting VMD script and an arbitrary number of keyword argument pairs to either write out a new *region* visualization, change the *color* or *material* setting, or to insert arbitrary VMD script *command*s. The keywords and arguments are processed in sequence.

The *region* keyword must be followed by a previously defined LAMMPS [[region]{.doc}]region.md){.reference .internal}. Only a limited set region styles and region settings are currently supported. See **Restrictions** below. Unsupported region styles or regions with unsupported settings will be skipped and a corresponding message is printed.

The *color* keyword must be followed by a color name that is defined in VMD. This color will be used by all following region visualizations. The default setting is 'silver'. VMD has the following colors pre-defined:

  -------- ------- ------- -------- --------- --------- ---------- --------- -------- --------- ---------
  blue     red     gray    orange   yellow    tan       silver     green     white    pink      cyan
  purple   lime    mauve   ochre    iceblue   black     yellow2    yellow3   green2   green3    cyan2
  cyan3    blue2   blue3   violet   violet2   magenta   magenta2   red2      red3     orange2   orange3
  -------- ------- ------- -------- --------- --------- ---------- --------- -------- --------- ---------

The *material* keyword must be followed by a material name that is defined in VMD. This material will be used by all following visualizations. The default setting is 'Transparent'. VMD has the following materials pre-defined:

  ---------- ------------- ---------------- --------- ------------- ------------- ----------- -----------
  Opaque     Transparent   BrushedMetal     Diffuse   Ghost         Glass1        Glass2      Glass3
  Glossy     HardPlastic   MetallicPastel   Steel     Translucent   Edgy          EdgyShiny   EdgyGlass
  Goodsell   AOShiny       AOChalky         AOEdgy    BlownGlass    GlassBubble   RTChrome    
  ---------- ------------- ---------------- --------- ------------- ------------- ----------- -----------

The *command* keyword must be followed by a VMD script command as a single string in quotes. This VMD command will be directly inserted into the created VMD script.

The created file can be loaded into VMD either from the command line with the '-e' flag, or from the command prompt with 'play \<script file\>', or from the File menu via "Load VMD visualization state".

::: {.note .admonition}
Setting the "top" molecule in VMD

It is usually desirable to have the "molecule" with the LAMMPS trajectory set at "top" molecule in VMD and not one of the "region molecules". The VMD script generated by this region2vmd assumes that this molecule is already loaded and set as the current "top" molecule. Thus at the beginning of the script the index of the top molecule is stored in the VMD variable 'oldtop' and at the end of the script, that "top" molecule is restored. If no molecule is loaded, this can be inserted into the script with a custom command. The molecule index to this new molecules should be assigned to the oldtop variable. This can be done with e.g. [`set`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`oldtop`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`[mol`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`new`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`{regions.vmd}`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`waitfor`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`all]`{.docutils .literal .notranslate}]{.pre}
:::
::::::

------------------------------------------------------------------------

:::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

::: versionchanged
[Changed in version 11Feb2026.]{.versionmodified .changed}
:::

This command is part of the GRAPHICS package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Only the following region styles are currently supported: *block*, *cone*, *cylinder*, *ellipsoid*, *prism*, and *sphere*. Regions formed from unions or intersections of other regions are not supported.

Rotating regions are currently not supported.
::::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[region]{.doc}]region.md){.reference .internal}, [[dump image]{.doc}]dump_image.md){.reference .internal}
:::

::: {#defaults .section}
## Defaults[](#defaults "Link to this heading"){.headerlink}

*color* = silver, *material* = Transparent
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

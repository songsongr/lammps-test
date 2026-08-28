::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-rheo-property-atom-command .section}
[]{#index-0}

# compute rheo/property/atom command[](#compute-rheo-property-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID rheo/property/atom input1 input2 ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- rheo/property/atom = style name of this compute command

- input = one or more atom attributes

  :::: {.highlight-none .notranslate}
  ::: highlight
      possible attributes = phase, surface, surface/r,
                            surface/divr, surface/n/a, coordination,
                            shift/v/a, energy, temperature, heatflow,
                            conductivity, cv, viscosity, pressure, rho,
                            grad/v/ab, stress/v/ab, stress/t/ab, nbond/shell
  :::
  ::::

  ``` literal-block
  phase = atom phase state
  surface = atom surface status
  surface/r = atom distance from the surface
  surface/divr = divergence of position at atom position
  surface/n/a = a-component of surface normal vector
  coordination = coordination number
  shift/v/a = a-component of atom shifting velocity
  energy = atom energy
  temperature = atom temperature
  heatflow = atom heat flow
  conductivity = atom conductivity
  cv = atom specific heat
  viscosity = atom viscosity
  pressure = atom pressure
  rho = atom density
  grad/v/ab = ab-component of atom velocity gradient tensor
  stress/v/ab = ab-component of atom viscous stress tensor
  stress/t/ab = ab-component of atom total stress tensor (pressure and viscous)
  nbond/shell = number of oxide bonds
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all rheo/property/atom phase surface/r surface/n/* pressure
    compute 2 all rheo/property/atom shift/v/x grad/v/xx stress/v/*
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 29Aug2024.]{.versionmodified .added}
:::

Define a computation that stores atom attributes specific to the RHEO package for each atom in the group. This is useful so that the values can be used by other [[output commands]{.doc}]Howto_output.md){.reference .internal} that take computes as inputs. See for example, the [[compute reduce]{.doc}]compute_reduce.md){.reference .internal}, [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal}, [[fix ave/histo]{.doc}]fix_ave_histo.md){.reference .internal}, [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal}, and [[atom-style variable]{.doc}]variable.md){.reference .internal} commands.

For vector attributes, e.g. *shift/v/*[\\(\\alpha\\)]{.math .notranslate .nohighlight}, one must specify [\\(\\alpha\\)]{.math .notranslate .nohighlight} as the *x*, *y*, or *z* component, e.g. *shift/v/x*. Alternatively, a wild card \* will include all components, *x* and *y* in 2D or *x*, *y*, and *z* in 3D.

For tensor attributes, e.g. *grad/v/*[\\(\\alpha \\beta\\)]{.math .notranslate .nohighlight}, one must specify both [\\(\\alpha\\)]{.math .notranslate .nohighlight} and [\\(\\beta\\)]{.math .notranslate .nohighlight} as *x*, *y*, or *z*, e.g. *grad/v/xy*. Alternatively, a wild card \* will include all components. In 2D, this includes *xx*, *xy*, *yx*, and *yy*. In 3D, this includes *xx*, *xy*, *xz*, *yx*, *yy*, *yz*, *zx*, *zy*, and *zz*.

Many properties require their respective fixes, listed below in related commands, be defined. For instance, the *viscosity* attribute is the viscosity of a particle calculated by [[fix rheo/viscosity]{.doc}]fix_rheo_viscosity.md){.reference .internal}. The meaning of less obvious properties is described below.

The *phase* property indicates whether the particle is in a fluid state, a value of 0, or a solid state, a value of 1.

The *surface* property indicates the surface designation produced by the *surface/detection* option of [[fix rheo]{.doc}]fix_rheo.md){.reference .internal}. Bulk particles have a value of 0, surface particles have a value of 1, and splash particles have a value of 2. The *surface/r* property is the distance from the surface, up to the kernel cutoff length. Surface particles have a value of 0. The *surface/n/*[\\(\\alpha\\)]{.math .notranslate .nohighlight} properties are the components of the surface normal vector.

The *shift/v/*[\\(\\alpha\\)]{.math .notranslate .nohighlight} properties are the components of the shifting velocity produced by the *shift* option of [[fix rheo]{.doc}]fix_rheo.md){.reference .internal}.

The *nbond/shell* property is the number of shell bonds that have been activated from [[bond style rheo/shell]{.doc}]bond_rheo_shell.md){.reference .internal}.

The values are stored in a per-atom vector or array as discussed below. Zeroes are stored for atoms not in the specified group or for quantities that are not defined for a particular particle in the group
::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom vector or per-atom array depending on the number of input values. Generally, if a single input is specified, a per-atom vector is produced. If two or more inputs are specified, a per-atom array is produced where the number of columns = the number of inputs. However, if a wild card \* is used for a vector or tensor, then the number of inputs is considered to be incremented by the dimension or the dimension squared, respectively. The vector or array can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The vector or array values will be in whatever [[units]{.doc}]units.md){.reference .internal} the corresponding attribute is in (e.g., density units for *rho*).
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute style is part of the RHEO package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dump custom]{.doc}]dump.md){.reference .internal}, [[compute reduce]{.doc}]compute_reduce.md){.reference .internal}, [[fix ave/atom]{.doc}]fix_ave_atom.md){.reference .internal}, [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal}, [[fix rheo/viscosity]{.doc}]fix_rheo_viscosity.md){.reference .internal}, [[fix rheo/pressure]{.doc}]fix_rheo_pressure.md){.reference .internal}, [[fix rheo/thermal]{.doc}]fix_rheo_thermal.md){.reference .internal}, [[fix rheo/oxdiation]{.doc}]fix_rheo_oxidation.md){.reference .internal}, [[fix rheo]{.doc}]fix_rheo.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

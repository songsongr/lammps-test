::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#dump-netcdf-command .section}
[]{#index-1}[]{#index-0}

# dump netcdf command[](#dump-netcdf-command "Link to this heading"){.headerlink}
:::

:::::::::::: {#dump-netcdf-mpiio-command .section}
# dump netcdf/mpiio command[](#dump-netcdf-mpiio-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dump ID group-ID netcdf N file args
    dump ID group-ID netcdf/mpiio N file args
:::
::::

- ID = user-assigned name for the dump

- group-ID = ID of the group of atoms to be imaged

- *netcdf* or *netcdf/mpiio* = style of dump command (other styles *atom* or *cfg* or *dcd* or *xtc* or *xyz* or *local* or *custom* are discussed on the [[dump]{.doc}]dump.md){.reference .internal} doc page)

- N = dump every this many timesteps

- file = name of file to write dump info to

- args = list of atom attributes, same as for [[dump_style custom]{.doc}]dump.md){.reference .internal}
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dump 1 all netcdf 100 traj.nc type x y z vx vy vz
    dump_modify 1 append yes at -1 thermo yes
    dump 1 all netcdf/mpiio 1000 traj.nc id type x y z
    dump 1 all netcdf 1000 traj.*.nc id type x y z
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Dump a snapshot of atom coordinates every N timesteps in AMBER-style NetCDF file format. NetCDF files are binary, portable and self-describing. This dump style will write only one file on the root node. The dump style *netcdf* uses the [standard NetCDF library](https://www.unidata.ucar.edu/software/netcdf/){.reference .external}. All data is collected on one processor and then written to the dump file. Dump style *netcdf/mpiio* uses the [parallel NetCDF library](https://parallel-netcdf.github.io/){.reference .external} and MPI-IO to write to the dump file in parallel; it has better performance on a larger number of processors. Note that style *netcdf* outputs all atoms sorted by atom tag while style *netcdf/mpiio* outputs atoms in order of their MPI rank.

NetCDF files can be directly visualized via the following tools:

- Ovito ([https://www.ovito.org/](https://www.ovito.org/){.reference .external}). Ovito supports the AMBER convention and all extensions of this dump style.

- VMD ([https://www.ks.uiuc.edu/Research/vmd/](https://www.ks.uiuc.edu/Research/vmd/){.reference .external}).

In addition to per-atom data, [[thermo]{.doc}]thermo.md){.reference .internal} data can be included in the dump file. The data included in the dump file is identical to the data specified by [[thermo_style]{.doc}]thermo_style.md){.reference .internal}.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *netcdf* and *netcdf/mpiio* dump styles are part of the NETCDF package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The *netcdf* and *netcdf/mpiio* dump styles currently cannot dump string properties or properties from variables.
:::

------------------------------------------------------------------------

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dump]{.doc}]dump.md){.reference .internal}, [[dump_modify]{.doc}]dump_modify.md){.reference .internal}, [[undump]{.doc}]undump.md){.reference .internal}
:::
::::::::::::
::::::::::::::
:::::::::::::::

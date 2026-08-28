:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-plumed-command .section}
[]{#index-0}

# fix plumed command[](#fix-plumed-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID plumed keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- plumed = style name of this fix command

- keyword = *plumedfile* or *outfile*

  ``` literal-block
  plumedfile arg = name of PLUMED input file to use (default: NULL)
  outfile arg = name of file on which to write the PLUMED log (default: NULL)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix pl all plumed plumedfile plumed.dat outfile p.log
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix instructs LAMMPS to call the [PLUMED](https://www.plumed.org/){.reference .external} library, which allows one to perform various forms of trajectory analysis on the fly and to also use methods such as umbrella sampling and metadynamics to enhance the sampling of phase space.

The documentation included here only describes the fix plumed command itself. This command is LAMMPS specific, whereas most of the functionality implemented in PLUMED will work with a range of MD codes, and when PLUMED is used as a stand alone code for analysis. The full [documentation for PLUMED](https://www.plumed.org/doc.html){.reference .external} is available online and included in the PLUMED source code. The PLUMED library development is hosted at [https://github.com/plumed/plumed2](https://github.com/plumed/plumed2){.reference .external} A detailed discussion of the code can be found in [[(Tribello)]{.std .std-ref}](#tribello){.reference .internal}.

There is an example input for using this package with LAMMPS in the examples/PACKAGES/plumed directory.

------------------------------------------------------------------------

The command to make LAMMPS call PLUMED during a run requires two keyword value pairs pointing to the PLUMED input file and an output file for the PLUMED log. The user must specify these arguments every time PLUMED is to be used. Furthermore, the fix plumed command should appear in the LAMMPS input file **after** relevant input parameters (e.g. the timestep) have been set.

The *group-ID* entry is ignored. LAMMPS will always pass all the atoms to PLUMED and there can only be one instance of the plumed fix at a time. The way the plumed fix is implemented ensures that the minimum amount of information required is communicated. Furthermore, PLUMED supports multiple, completely independent collective variables, multiple independent biases and multiple independent forms of analysis. There is thus really no restriction in functionality by only allowing only one plumed fix in the LAMMPS input.

The *plumedfile* keyword allows the user to specify the name of the PLUMED input file. Instructions as to what should be included in a plumed input file can be found in the [documentation for PLUMED](https://www.plumed.org/doc.html){.reference .external}

The *outfile* keyword allows the user to specify the name of a file in which to output the PLUMED log. This log file normally just repeats the information that is contained in the input file to confirm it was correctly read and parsed. The names of the files in which the results are stored from the various analysis options performed by PLUMED will be specified by the user in the PLUMED input file.
:::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

When performing a restart of a calculation that involves PLUMED you must include a RESTART command in the PLUMED input file as detailed in the [PLUMED documentation](https://www.plumed.org/doc.html){.reference .external}. When the restart command is found in the PLUMED input PLUMED will append to the files that were generated in the run that was performed previously. No part of the PLUMED restart data is included in the LAMMPS restart files. Furthermore, any history dependent bias potentials that were accumulated in previous calculations will be read in when the RESTART command is included in the PLUMED input.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the energy change from the biasing force added by PLUMED to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify energy yes]{.doc}]fix_modify.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *virial* option is supported by this fix to add the contribution from the biasing force to the global pressure of the system via the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} command. This can be accessed by [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify virial yes]{.doc}]fix_modify.md){.reference .internal}.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the PLUMED energy mentioned above. The scalar value calculated by this fix is "extensive".

Note that other quantities of interest can be output by commands that are native to PLUMED.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the PLUMED package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

There can only be one fix plumed command active at a time.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix smd]{.doc}]fix_smd.md){.reference .internal} [[fix colvars]{.doc}]fix_colvars.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default options are plumedfile = NULL and outfile = NULL

------------------------------------------------------------------------

**(Tribello)** G.A. Tribello, M. Bonomi, D. Branduardi, C. Camilloni and G. Bussi, Comp. Phys. Comm 185, 604 (2014)
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

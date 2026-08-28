::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#fix-bocs-command .section}
[]{#index-0}

# fix bocs command[](#fix-bocs-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID bocs keyword values ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- bocs = style name of this fix command

- two or more keyword/value pairs may be appended

- keyword = *temp* or *cgiso* or *tchain* or *pchain* or *mtk* or *tloop* or *ploop*

  ``` literal-block
  temp values = Tstart Tstop Tdamp
  cgiso values = Pstart Pstop Pdamp basis_set args
    basis_set = analytic or linear_spline or cubic_spline
      analytic args = V_avg N_particles N_coeff Coeff_1 Coeff_2 ... Coeff_N
      linear_spline args = input_filename
      cubic_spline args = input_filename
  tchain value = N = length of thermostat chain (1 = single thermostat)
  pchain value = N = length of thermostat on barostat (0 = no thermostat)
  mtk value = yes or no = add MTK adjustment term or not
  tloop value = M = number of sub-cycles to perform on thermostat
  ploop value = M = number of sub-cycles to perform on barostat
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all bocs temp 300.0 300.0 100.0 cgiso 0.986 0.986 1000.0 analytic 66476.015 968 2 245030.10 8962.20
    fix 1 all bocs temp 300.0 300.0 100.0 cgiso 0.986 0.986 1000.0 cubic_spline input_Fv.dat
    thermo_modify press 1_press
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

These commands incorporate a pressure correction as described by Dunn and Noid [[(Dunn1)]{.std .std-ref}](#bocs-dunn1){.reference .internal} to the standard MTK barostat by Martyna et al. [[(Martyna)]{.std .std-ref}](#bocs-martyna){.reference .internal}. The first half of the command mimics a standard [[fix npt]{.doc}]fix_nh.md){.reference .internal} command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all bocs temp Tstart Tstop Tcoupl cgiso Pstart Pstop Pdamp
:::
::::

The two differences are replacing *npt* with *bocs*, and replacing *iso*/*aniso*/etc. with *cgiso*. The rest of the command details what form you would like to use for the pressure correction equation. The choices are: *analytic*, *linear_spline*, or *cubic_spline*.

With either spline method, the only argument that needs to follow it is the name of a file that contains the desired pressure correction as a function of volume. The file must be formatted so each line has:

:::: {.highlight-none .notranslate}
::: highlight
    Volume_i, PressureCorrection_i
:::
::::

Note both the COMMA and the SPACE separating the volume's value and its corresponding pressure correction. The volumes in the file must be uniformly spaced. Both the volumes and the pressure corrections should be provided in the proper units (e.g., if you are using *units real*, the volumes should all be in [\\(\\mathrm{\\mathring{A}}\^3\\)]{.math .notranslate .nohighlight} and the pressure corrections should all be in atm). Furthermore, the table should start/end at a volume considerably smaller/larger than you expect your system to sample during the simulation. If the system ever reaches a volume outside of the range provided, the simulation will stop.

With the *analytic* option, the arguments are as follows:

:::: {.highlight-none .notranslate}
::: highlight
    ... analytic V_avg N_particles N_coeff Coeff_1 Coeff_2 ... Coeff_N
:::
::::

Note that *V_avg* and *Coeff_i* should all be in the proper units (e.g., if you are using *units real*, *V_avg* should be in [\\(\\mathrm{\\mathring{A}\^3}\\)]{.math .notranslate .nohighlight} and the coefficients should all be in [\\(\\mathrm{atm}\\cdot\\mathrm{\\mathring{A}\^3}\\)]{.math .notranslate .nohighlight}).
:::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the cumulative global energy change to [[binary restart files]{.doc}]restart.md){.reference .internal}. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the fix continues in an uninterrupted fashion.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *temp* option is supported by this fix. You can use it to assign a temperature [[compute]{.doc}]compute.md){.reference .internal} you have defined to this fix which will be used in its thermostatting procedure, as described above. For consistency, the group used by this fix and by the compute should be the same.

The cumulative energy change in the system imposed by this fix is included in the [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} keywords *ecouple* and *econserve*. See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} doc page for details.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the same cumulative energy change due to this fix described in the previous paragraph. The scalar value calculated by this fix is "extensive".

This fix can ramp its target temperature over multiple runs, using the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. See the [[run]{.doc}]run.md){.reference .internal} command for details of how to do this.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the BOCS package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

As this is computing a (modified) pressure, group-ID should be *all*.

The pressure correction has only been tested for use with an isotropic pressure coupling in 3 dimensions.

By default, LAMMPS will still report the normal value for the pressure if the pressure is printed via a *thermo* command, or if the pressures are written to a file every so often. In order to have LAMMPS report the modified pressure, you must include the *thermo_modify* command given in the examples. For the last argument in the command, you should put XXXX_press, where XXXX is the ID given to the fix bocs command (in the example, the ID of the fix bocs command is 1).
:::

::: {#further-information .section}
## Further information[](#further-information "Link to this heading"){.headerlink}

For more details about the pressure correction and the entire BOCS software package, visit the [BOCS package on GitHub](https://github.com/noid-group/BOCS){.reference .external} and read the release paper by Dunn et al. [[(Dunn2)]{.std .std-ref}](#bocs-dunn2){.reference .internal} .

------------------------------------------------------------------------

**(Dunn1)** Dunn and Noid, J Chem Phys, 143, 243148 (2015).

**(Martyna)** Martyna, Tobias, and Klein, J Chem Phys, 101, 4177 (1994).

**(Dunn2)** Dunn, Lebold, DeLyser, Rudzinski, and Noid, J. Phys. Chem. B, 122, 3363 (2018).
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

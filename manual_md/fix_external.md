::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::: {#fix-external-command .section}
[]{#index-1}[]{#index-0}

# fix external command[](#fix-external-command "Link to this heading"){.headerlink}

Accelerator Variants: *external/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID external mode args
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- external = style name of this fix command

- mode = *pf/callback* or *pf/array*

  ``` literal-block
  pf/callback args = Ncall Napply
    Ncall = make callback every Ncall steps
    Napply = apply callback forces every Napply steps
  pf/array args = Napply
    Napply = apply array forces every Napply steps
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all external pf/callback 1 1
    fix 1 all external pf/callback 100 1
    fix 1 all external pf/array 10
:::
::::
:::::

::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix allows external programs that are running LAMMPS through its [[library interface]{.doc}]Howto_library.md){.reference .internal} to modify certain LAMMPS properties on specific timesteps, similar to the way other fixes do. The external driver can be a [[C/C++ or Fortran program]{.doc}]Howto_library.md){.reference .internal} or a [[Python script]{.doc}]Python_head.md){.reference .internal}.

------------------------------------------------------------------------

If mode is *pf/callback* then the fix will make a callback every *Ncall* timesteps or minimization iterations to the external program. The external program computes forces on atoms by setting values in an array owned by the fix. The fix then adds these forces to each atom in the group, once every *Napply* steps, similar to the way the [[fix addforce]{.doc}]fix_addforce.md){.reference .internal} command works. Note that if *Ncall* \> *Napply*, the force values produced by one callback will persist, and be used multiple times to update atom forces.

The callback function "foo" is invoked by the fix as:

:::: {.highlight-c++ .notranslate}
::: highlight
    foo(void *ptr, bigint timestep, int nlocal, tagint *ids, double **x, double **fexternal);
:::
::::

The arguments are as follows:

- *ptr* = pointer provided by and simply passed back to external driver

- *timestep* = current LAMMPS timestep

- *nlocal* = \# of atoms on this processor

- *ids* = list of atom IDs on this processor

- *x* = coordinates of atoms on this processor

- *fexternal* = forces to add to atoms on this processor

Note that *timestep* is a "bigint" which is defined in src/lmptype.h, typically as a 64-bit integer. And *ids* is a pointer to type "tagint" which is typically a 32-bit integer unless LAMMPS is compiled with -DLAMMPS_BIGBIG. For more info please see the [[build settings]{.std .std-ref}]Build_settings.md#size){.reference .internal} section of the manual. Finally, *fexternal* are the forces returned by the driver program.

The best way to set up the callback function is to use the C-language library interface function [[`lammps_set_fix_external_callback()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv432lammps_set_fix_external_callbackPvPKc16FixExternalFnPtrPv "lammps_set_fix_external_callback"){.reference .internal}.

------------------------------------------------------------------------

If mode is *pf/array* then the fix simply stores force values in an array. The fix adds these forces to each atom in the group, once every *Napply* steps, similar to the way the [[fix addforce]{.doc}]fix_addforce.md){.reference .internal} command works.

The name of the public force array provided by the FixExternal class is

:::: {.highlight-c++ .notranslate}
::: highlight
    double **fexternal;
:::
::::

It is allocated by the FixExternal class as an (N,3) array where N is the number of atoms owned by a processor. The 3 corresponds to the fx, fy, fz components of force.

It is up to the external program to set the values in this array to the desired quantities, as often as desired. For example, the driver program might perform an MD run in stages of 1000 timesteps each. In between calls to the LAMMPS [[run]{.doc}]run.md){.reference .internal} command, it could retrieve atom coordinates from LAMMPS, compute forces, set values in fexternal, etc.

------------------------------------------------------------------------

To use this fix during energy minimization, the energy corresponding to the added forces must also be set so as to be consistent with the added forces. Otherwise the minimization will not converge correctly. Correspondingly, the global virial needs to be updated to be use this fix with variable cell calculations (e.g. [[fix box/relax]{.doc}]fix_box_relax.md){.reference .internal} or [[fix npt]{.doc}]fix_nh.md){.reference .internal}).

This can be done from the external driver by calling these public methods of the FixExternal class:

:::: {.highlight-c++ .notranslate}
::: highlight
    void set_energy_global(double eng);
    void set_virial_global(double *virial);
:::
::::

where *eng* is the potential energy, and *virial* an array of the 6 stress tensor components. Eng is an extensive quantity, meaning it should be the sum over per-atom energies of all affected atoms. It should also be provided in [[energy units]{.doc}]units.md){.reference .internal} consistent with the simulation. See the details below for how to ensure this energy setting is used appropriately in a minimization.

Additional public methods that the caller can use to update system properties are:

:::: {.highlight-c++ .notranslate}
::: highlight
    void set_energy_peratom(double *eng);
    void set_virial_peratom(double **virial);
    void set_vector_length(int n);
    void set_vector(int idx, double val);
:::
::::

These enable setting per-atom energy and per-atom stress contributions, the length and individual values of a global vector of properties that the caller code may want to communicate to LAMMPS (e.g. for use in [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal} or in [[equal-style variables]{.doc}]variable.md){.reference .internal} or for [[custom thermo output]{.doc}]thermo_style.md){.reference .internal}.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::::::

------------------------------------------------------------------------

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the potential energy set by the external driver to both the global potential energy and peratom potential energies of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal} or output by the [[compute pe/atom]{.doc}]compute_pe_atom.md){.reference .internal} command. The default setting for this fix is [[fix_modify energy yes]{.doc}]fix_modify.md){.reference .internal}. Note that this energy may be a fictitious quantity but it is needed so that the [[minimize]{.doc}]minimize.md){.reference .internal} command can include the forces added by this fix in a consistent manner. I.e. there is a decrease in potential energy when atoms move in the direction of the added force.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *virial* option is supported by this fix to add the contribution computed by the external program to both the global pressure and per-atom stress of the system via the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} and [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} commands. The former can be accessed by [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify virial yes]{.doc}]fix_modify.md){.reference .internal}.

This fix computes a global scalar, a global vector, and a per-atom array which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the potential energy discussed above. The scalar stored by this fix is "extensive". The global vector has a custom length and needs to be set by the external program using the [[`lammps_fix_external_set_vector()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv430lammps_fix_external_set_vectorPvPKcid "lammps_fix_external_set_vector"){.reference .internal} and [[`lammps_fix_external_set_vector_length()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv437lammps_fix_external_set_vector_lengthPvPKci "lammps_fix_external_set_vector_length"){.reference .internal} calls of the LAMMPS library interface or the equivalent call of the Python or Fortran modules. The per-atom array has 3 values for each atom and is the applied external force.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The forces due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command.

::: {.admonition .note}
Note

If you want the fictitious potential energy associated with the added forces to be included in the total potential energy of the system (the quantity being minimized), you MUST not disable the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for this fix.
:::
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

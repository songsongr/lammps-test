::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::: {#fix-adapt-command .section}
[]{#index-0}

# fix adapt command[](#fix-adapt-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID adapt N attribute args ... keyword value ...
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- adapt = style name of this fix command

- N = adapt simulation settings every this many timesteps

- one or more attribute/arg pairs may be appended

- attribute = *pair* or *bond* or *angle* or *dihedral* or *improper* or *kspace* or *atom*

  ``` literal-block
  pair args = pstyle pparam I J v_name
    pstyle = pair style name (e.g., lj/cut)
    pparam = parameter to adapt over time
    I,J = type pair(s) to set parameter for (integer or type label)
    v_name = variable with name that calculates value of pparam
  bond args = bstyle bparam I v_name
    bstyle = bond style name (e.g., harmonic)
    bparam = parameter to adapt over time
    I = type bond to set parameter for (integer or type label)
    v_name = variable with name that calculates value of bparam
  angle args = astyle aparam I v_name
    astyle = angle style name (e.g., harmonic)
    aparam = parameter to adapt over time
    I = type angle to set parameter for (integer or type label)
    v_name = variable with name that calculates value of aparam
  dihedral args = dstyle dparam I v_name
    dstyle = dihedral style name (e.g., quadratic)
    dparam = parameter to adapt over time
    I = type dihedral to set parameter for (integer or type label)
    v_name = variable with name that calculates value of iparam
  improper args = istyle iparam I v_name
    istyle = improper style name (e.g., cvff)
    iparam = parameter to adapt over time
    I = type improper to set parameter for (integer or type label)
    v_name = variable with name that calculates value of iparam
  kspace arg = v_name
    v_name = variable with name that calculates scale factor on \(k\)-space terms
  atom args = atomparam v_name
    atomparam = charge or diameter or diameter/disc = parameter to adapt over time
    v_name = variable with name that calculates value of atomparam
  ```

- zero or more keyword/value pairs may be appended

- keyword = *scale* or *reset* or *mass*

  ``` literal-block
  scale value = no or yes
    no = the variable value is the new setting
    yes = the variable value multiplies the original setting
  reset value = no or yes
    no = values will remain altered at the end of a run
    yes = reset altered values to their original values at the end of a run
  mass value = no or yes
    no = mass is not altered by changes in diameter
    yes = mass is altered by changes in diameter
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all adapt 1 pair soft a 1 1 v_prefactor
    fix 1 all adapt 1 pair soft a 2* 3 v_prefactor
    fix 1 all adapt 1 pair lj/cut epsilon * * v_scale1 pair coul/cut scale 3 3 v_scale2 scale yes reset yes
    fix 1 all adapt 10 atom diameter v_size

    variable ramp_up equal "ramp(0.01,0.5)"
    fix stretch all adapt 1 bond harmonic r0 1 v_ramp_up

    labelmap atom 1 c1
    fix 1 all adapt 1 pair soft a c1 c1 v_prefactor
:::
::::
:::::

:::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Change or adapt one or more specific simulation attributes or settings over time as a simulation runs. Pair potential and [\\(k\\)]{.math .notranslate .nohighlight}-space and atom attributes which can be varied by this fix are discussed below. Many other fixes can also be used to time-vary simulation parameters (e.g., the [[fix deform]{.doc}]fix_deform.md){.reference .internal} command will change the simulation box size/shape and the [[fix move]{.doc}]fix_move.md){.reference .internal} command will change atom positions and velocities in a prescribed manner). Also note that many commands allow variables as arguments for specific parameters, if described in that manner on their doc pages. An equal-style variable can calculate a time-dependent quantity, so this is another way to vary a simulation parameter over time.

If [\\(N\\)]{.math .notranslate .nohighlight} is specified as 0, the specified attributes are only changed once, before the simulation begins. This is all that is needed if the associated variables are not time-dependent. If [\\(N \> 0\\)]{.math .notranslate .nohighlight}, then changes are made every [\\(N\\)]{.math .notranslate .nohighlight} steps during the simulation, presumably with a variable that is time-dependent.

Depending on the value of the *reset* keyword, attributes changed by this fix will or will not be reset back to their original values at the end of a simulation. Even if *reset* is specified as *yes*, a restart file written during a simulation will contain the modified settings.

If the *scale* keyword is set to *no*, which is the default, then the value of the altered parameter will be whatever the variable generates. If the *scale* keyword is set to *yes*, then the value of the altered parameter will be the initial value of that parameter multiplied by whatever the variable generates (i.e., the variable is now a "scale factor" applied in (presumably) a time-varying fashion to the parameter).

Note that whether scale is *no* or *yes*, internally, the parameters themselves are actually altered by this fix. Make sure you use the *reset yes* option if you want the parameters to be restored to their initial values after the run.

------------------------------------------------------------------------

The *pair* keyword enables various parameters of potentials defined by the [[pair_style]{.doc}]pair_style.md){.reference .internal} command to be changed, if the pair style supports it. Note that the [[pair_style]{.doc}]pair_style.md){.reference .internal} and [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} commands must be used in the usual manner to specify these parameters initially; the fix adapt command simply overrides the parameters.

::: {.admonition .note}
Note

Pair_coeff settings must be made **explicitly** in order for fix adapt to be able to change them. Settings inferred from mixing are not suitable. If necessary all mixed settings can be output to a file using the [[write_coeff command]{.doc}]write_coeff.md){.reference .internal} and then the desired mixed pair_coeff settings copied from that file.
:::

The *pstyle* argument is the name of the pair style. If [[pair_style hybrid or hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} is used, *pstyle* should be a sub-style name. If there are multiple sub-styles using the same pair style, then *pstyle* should be specified as "style:N", where *N* is which instance of the pair style you wish to adapt (e.g., the first or second). For example, *pstyle* could be specified as "soft" or "lubricate" or "lj/cut:1" or "lj/cut:2". The *pparam* argument is the name of the parameter to change. This is the current list of pair styles and parameters that can be varied by this fix. See the doc pages for individual pair styles and their energy formulas for the meaning of these parameters:

  ----------------------------------------------------------------------------------------------------------- ------------------------------------------------ -------------
  [[born]{.doc}]pair_born.md){.reference .internal}                                                        a,b,c                                            type pairs
  [[born/coul/long, born/coul/msm]{.doc}]pair_born.md){.reference .internal}                               coulombic_cutoff                                 type global
  [[born/gauss]{.doc}]pair_born_gauss.md){.reference .internal}                                            biga0,biga1,r0                                   type pairs
  [[buck, buck/coul/cut]{.doc}]pair_buck.md){.reference .internal}                                         a,c                                              type pairs
  [[buck/coul/long, buck/coul/msm]{.doc}]pair_buck.md){.reference .internal}                               a,c,coulombic_cutoff                             type pairs
  [[buck/mdf]{.doc}]pair_mdf.md){.reference .internal}                                                     a,c                                              type pairs
  [[coul/cut, coul/cut/global]{.doc}]pair_coul.md){.reference .internal}                                   scale                                            type pairs
  [[coul/cut/soft]{.doc}]pair_fep_soft.md){.reference .internal}                                           lambda                                           type pairs
  [[coul/debye]{.doc}]pair_coul.md){.reference .internal}                                                  scale                                            type pairs
  [[coul/dsf]{.doc}]pair_coul.md){.reference .internal}                                                    coulombic_cutoff                                 type global
  [[coul/long, coul/msm]{.doc}]pair_coul.md){.reference .internal}                                         coulombic_cutoff, scale                          type pairs
  [[coul/long/soft]{.doc}]pair_fep_soft.md){.reference .internal}                                          scale, lambda, coulombic_cutoff                  type pairs
  [[coul/slater/long]{.doc}]pair_coul_slater.md){.reference .internal}                                     scale                                            type pairs
  [[coul/streitz]{.doc}]pair_coul.md){.reference .internal}                                                scale                                            type pairs
  [[eam, eam/alloy, eam/fs]{.doc}]pair_eam.md){.reference .internal}                                       scale                                            type pairs
  [[gauss]{.doc}]pair_gauss.md){.reference .internal}                                                      a                                                type pairs
  [[harmonic/cut]{.doc}]pair_harmonic_cut.md){.reference .internal}                                        k, cutoff                                        type pairs
  [[kim]{.doc}]pair_kim.md){.reference .internal}                                                          scale                                            type global
  [[lennard/mdf]{.doc}]pair_mdf.md){.reference .internal}                                                  A,B                                              type pairs
  [[lj96/cut]{.doc}]pair_lj96.md){.reference .internal}                                                    epsilon,sigma                                    type pairs
  [[lj/class2]{.doc}]pair_class2.md){.reference .internal}                                                 epsilon,sigma                                    type pairs
  [[lj/class2/coul/cut, lj/class2/coul/long]{.doc}]pair_class2.md){.reference .internal}                   epsilon,sigma,coulombic_cutoff                   type pairs
  [[lj/cubic]{.doc}]pair_lj_cubic.md){.reference .internal}                                                epsilon,sigma                                    type pairs
  [[lj/cut]{.doc}]pair_lj.md){.reference .internal}                                                        epsilon,sigma                                    type pairs
  [[lj/cut/coul/cut, lj/cut/coul/long, lj/cut/coul/msm]{.doc}]pair_lj_cut_coul.md){.reference .internal}   epsilon,sigma,coulombic_cutoff                   type pairs
  [[lj/cut/coul/cut/soft, lj/cut/coul/long/soft]{.doc}]pair_fep_soft.md){.reference .internal}             epsilon,sigma,lambda,coulombic_cutoff            type pairs
  [[lj/cut/coul/dsf]{.doc}]pair_lj_cut_coul.md){.reference .internal}                                      cutoff                                           type global
  [[lj/cut/tip4p/cut]{.doc}]pair_lj_cut_tip4p.md){.reference .internal}                                    epsilon,sigma,coulombic_cutoff                   type pairs
  [[lj/cut/soft]{.doc}]pair_fep_soft.md){.reference .internal}                                             epsilon,sigma,lambda                             type pairs
  [[lj/expand]{.doc}]pair_lj_expand.md){.reference .internal}                                              epsilon,sigma,delta                              type pairs
  [[lj/lj/gromacs]{.doc}]pair_gromacs.md){.reference .internal}                                            epsilon,sigma                                    type pairs
  [[lj/mdf]{.doc}]pair_mdf.md){.reference .internal}                                                       epsilon,sigma                                    type pairs
  [[lj/pirani]{.doc}]pair_lj_pirani.md){.reference .internal}                                              alpha, beta, gamma, rm, epsilon                  type pairs
  [[lj/sf/dipole/sf]{.doc}]pair_dipole.md){.reference .internal}                                           epsilon,sigma,scale                              type pairs
  [[lubricate]{.doc}]pair_lubricate.md){.reference .internal}                                              mu                                               global
  [[meam]{.doc}]pair_meam.md){.reference .internal}                                                        scale                                            type pairs
  [[mie/cut]{.doc}]pair_mie.md){.reference .internal}                                                      epsilon,sigma,gamma_repulsive,gamma_attractive   type pairs
  [[morse, morse/smooth/linear]{.doc}]pair_morse.md){.reference .internal}                                 D0,R0,alpha                                      type pairs
  [[morse/soft]{.doc}]pair_morse.md){.reference .internal}                                                 D0,R0,alpha,lambda                               type pairs
  [[nm/cut]{.doc}]pair_nm.md){.reference .internal}                                                        E0,R0,m,n                                        type pairs
  [[nm/cut/coul/cut, nm/cut/coul/long]{.doc}]pair_nm.md){.reference .internal}                             E0,R0,m,n,coulombic_cutoff                       type pairs
  [[pace, pace/extrapolation]{.doc}]pair_pace.md){.reference .internal}                                    scale                                            type pairs
  [[pedone]{.doc}]pair_pedone.md){.reference .internal}                                                    c0,d0,r0,alpha                                   type pairs
  [[quip]{.doc}]pair_quip.md){.reference .internal}                                                        scale                                            type global
  [[snap]{.doc}]pair_snap.md){.reference .internal}                                                        scale                                            type pairs
  [[spin/dmi]{.doc}]pair_spin_dmi.md){.reference .internal}                                                coulombic_cutoff                                 type global
  [[spin/exchange]{.doc}]pair_spin_exchange.md){.reference .internal}                                      coulombic_cutoff                                 type global
  [[spin/magelec]{.doc}]pair_spin_magelec.md){.reference .internal}                                        coulombic_cutoff                                 type global
  [[spin/neel]{.doc}]pair_spin_neel.md){.reference .internal}                                              coulombic_cutoff                                 type global
  [[soft]{.doc}]pair_soft.md){.reference .internal}                                                        a                                                type pairs
  [[table]{.doc}]pair_table.md){.reference .internal}                                                      table_cutoff                                     type pairs
  [[ufm]{.doc}]pair_ufm.md){.reference .internal}                                                          epsilon,sigma,scale                              type pairs
  [[wf/cut]{.doc}]pair_wf_cut.md){.reference .internal}                                                    epsilon,sigma,nu,mu                              type pairs
  [[yukawa]{.doc}]pair_yukawa.md){.reference .internal}                                                    alpha                                            type pairs
  ----------------------------------------------------------------------------------------------------------- ------------------------------------------------ -------------

::: {.admonition .note}
Note

It is easy to add new pairwise potentials and their parameters to this list. All it typically takes is adding an extract() method to the pair\_\*.cpp file associated with the potential.
:::

Some parameters are global settings for the pair style (e.g., the viscosity setting "mu" for [[pair_style lubricate]{.doc}]pair_lubricate.md){.reference .internal}). Other parameters apply to atom type pairs within the pair style (e.g., the prefactor [\\(a\\)]{.math .notranslate .nohighlight} for [[pair_style soft]{.doc}]pair_soft.md){.reference .internal}).

Note that for many of the potentials, the parameter that can be varied is effectively a prefactor on the entire energy expression for the potential (e.g., the lj/cut epsilon). The parameters listed as "scale" are exactly that, since the energy expression for the [[coul/cut]{.doc}]pair_coul.md){.reference .internal} potential (for example) has no labeled prefactor in its formula. To apply an effective prefactor to some potentials, multiple parameters need to be altered. For example, the [[Buckingham potential]{.doc}]pair_buck.md){.reference .internal} needs both the [\\(A\\)]{.math .notranslate .nohighlight} and [\\(C\\)]{.math .notranslate .nohighlight} terms altered together. To scale the Buckingham potential, you should thus list the pair style twice, once for [\\(A\\)]{.math .notranslate .nohighlight} and once for [\\(C\\)]{.math .notranslate .nohighlight}.

If a type pair parameter is specified, the [\\(I\\)]{.math .notranslate .nohighlight} and [\\(J\\)]{.math .notranslate .nohighlight} settings should be specified to indicate which type pairs to apply it to. If a global parameter is specified, the [\\(I\\)]{.math .notranslate .nohighlight} and [\\(J\\)]{.math .notranslate .nohighlight} settings still need to be specified, but are ignored.

Similar to the [[pair_coeff command]{.doc}]pair_coeff.md){.reference .internal}, [\\(I\\)]{.math .notranslate .nohighlight} and [\\(J\\)]{.math .notranslate .nohighlight} can be specified in one of several ways. Explicit numeric values can be used for each, as in the first example above. Or, one or both of the types in the I,J pair can be a [[type label]{.doc}]Howto_type_labels.md){.reference .internal}. LAMMPS sets the coefficients for the symmetric [\\(J,I\\)]{.math .notranslate .nohighlight} interaction to the same values.

A wild-card asterisk can be used in place of or in conjunction with the [\\(I,J\\)]{.math .notranslate .nohighlight} arguments to set the coefficients for multiple pairs of atom types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of atom types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive). For the asterisk syntax, note that only type pairs with [\\(I \\le J\\)]{.math .notranslate .nohighlight} are considered; if asterisks imply type pairs where [\\(J \< I\\)]{.math .notranslate .nohighlight}, they are ignored.

IMPORTANT NOTE: If [[pair_style hybrid or hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} is being used, then the *pstyle* will be a sub-style name. You must specify [\\(I,J\\)]{.math .notranslate .nohighlight} arguments that correspond to type pair values defined (via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command) for that sub-style.

The *v_name* argument for keyword *pair* is the name of an [[equal-style variable]{.doc}]variable.md){.reference .internal} which will be evaluated each time this fix is invoked to set the parameter to a new value. It should be specified as v_name, where name is the variable name. Equal-style variables can specify formulas with various mathematical functions, and include [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command keywords for the simulation box parameters and timestep and elapsed time. Thus it is easy to specify parameters that change as a function of time or span consecutive runs in a continuous fashion. For the latter, see the *start* and *stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command and the *elaplong* keyword of [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} for details.

For example, these commands would change the prefactor coefficient of the [[pair_style soft]{.doc}]pair_soft.md){.reference .internal} potential from 10.0 to 30.0 in a linear fashion over the course of a simulation:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable prefactor equal ramp(10,30)
    fix 1 all adapt 1 pair soft a * * v_prefactor
:::
::::

------------------------------------------------------------------------

The *bond* keyword uses the specified variable to change the value of a bond coefficient over time, very similar to how the *pair* keyword operates. The only difference is that now a bond coefficient for a given bond type is adapted.

A wild-card asterisk can be used in place of or in conjunction with the bond type argument to set the coefficients for multiple bond types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of bond types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive).

If [[bond_style hybrid]{.doc}]bond_hybrid.md){.reference .internal} is used, *bstyle* should be a sub-style name. The bond styles that currently work with fix adapt are:

  ---------------------------------------------------------------------------------- -------------------------- ------------
  [[class2]{.doc}]bond_class2.md){.reference .internal}                           k2,k3,k4,r0                type bonds
  [[fene]{.doc}]bond_fene.md){.reference .internal}                               k,r0                       type bonds
  [[fene/expand]{.doc}]bond_fene_expand.md){.reference .internal}                 k,r0,epsilon,sigma,shift   type bonds
  [[fene/nm]{.doc}]bond_fene.md){.reference .internal}                            k,r0                       type bonds
  [[gaussian]{.doc}]bond_gaussian.md){.reference .internal}                       alpha,width,r0             type bonds
  [[gromos]{.doc}]bond_gromos.md){.reference .internal}                           k,r0                       type bonds
  [[harmonic]{.doc}]bond_harmonic.md){.reference .internal}                       k,r0                       type bonds
  [[harmonic/restrain]{.doc}]bond_harmonic_restrain.md){.reference .internal}     k                          type bonds
  [[harmonic/shift]{.doc}]bond_harmonic_shift.md){.reference .internal}           k,r0,r1                    type bonds
  [[harmonic/shift/cut]{.doc}]bond_harmonic_shift_cut.md){.reference .internal}   k,r0,r1                    type bonds
  [[mm3]{.doc}]bond_mm3.md){.reference .internal}                                 k,r0                       type bonds
  [[morse]{.doc}]bond_morse.md){.reference .internal}                             d0,alpha,r0                type bonds
  [[nonlinear]{.doc}]bond_nonlinear.md){.reference .internal}                     lamda,epsilon,r0           type bonds
  ---------------------------------------------------------------------------------- -------------------------- ------------

------------------------------------------------------------------------

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

The *angle* keyword uses the specified variable to change the value of an angle coefficient over time, very similar to how the *pair* keyword operates. The only difference is that now an angle coefficient for a given angle type is adapted.

A wild-card asterisk can be used in place of or in conjunction with the angle type argument to set the coefficients for multiple angle types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of angle types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive).

If [[angle_style hybrid]{.doc}]angle_hybrid.md){.reference .internal} is used, *astyle* should be a sub-style name. The angle styles that currently work with fix adapt are:

  ------------------------------------------------------------------------------------------------- -------------------- -------------
  [[harmonic]{.doc}]angle_harmonic.md){.reference .internal}                                     k,theta0             type angles
  [[charmm]{.doc}]angle_charmm.md){.reference .internal}                                         k,theta0             type angles
  [[class2]{.doc}]angle_class2.md){.reference .internal}                                         k2,k3,k4,theta0      type angles
  [[cosine]{.doc}]angle_cosine.md){.reference .internal}                                         k                    type angles
  [[cosine/delta]{.doc}]angle_cosine_delta.md){.reference .internal}                             k                    type angles
  [[cosine/periodic]{.doc}]angle_cosine_periodic.md){.reference .internal}                       k,b,n                type angles
  [[cosine/squared]{.doc}]angle_cosine_squared.md){.reference .internal}                         k,theta0             type angles
  [[cosine/squared/restricted]{.doc}]angle_cosine_squared_restricted.md){.reference .internal}   k,theta0             type angles
  [[dipole]{.doc}]angle_dipole.md){.reference .internal}                                         k,gamma0             type angles
  [[fourier]{.doc}]angle_fourier.md){.reference .internal}                                       k,c0,c1,c2           type angles
  [[fourier/simple]{.doc}]angle_fourier_simple.md){.reference .internal}                         k,c,n                type angles
  [[gaussian]{.doc}]angle_gaussian.md){.reference .internal}                                     alpha,width,theta0   type angles
  [[mm3]{.doc}]angle_mm3.md){.reference .internal}                                               k,theta0             type angles
  [[mwlc]{.doc}]angle_mwlc.md){.reference .internal}                                             k1,k2,mu,T           type angles
  [[quartic]{.doc}]angle_quartic.md){.reference .internal}                                       k2,k3,k4,theta0      type angles
  [[spica]{.doc}]angle_spica.md){.reference .internal}                                           k,theta0             type angles
  ------------------------------------------------------------------------------------------------- -------------------- -------------

Note that internally, theta0 is stored in radians, so the variable this fix uses to reset theta0 needs to generate values in radians.

------------------------------------------------------------------------

::: versionadded
[Added in version 12Jun2025.]{.versionmodified .added}
:::

The *dihedral* keyword uses the specified variable to change the value of a dihedral coefficient over time, very similar to how the *angle* keyword operates. The only difference is that now a dihedral coefficient for a given dihedral type is adapted.

A wild-card asterisk can be used in place of or in conjunction with the dihedral type argument to set the coefficients for multiple dihedral types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of dihedral types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive).

If [[dihedral_style hybrid]{.doc}]dihedral_hybrid.md){.reference .internal} is used, *dstyle* should be a sub-style name. The dihedral styles that currently work with fix adapt are:

  ---------------------------------------------------------------------------------------------------- ------------------------- ----------------
  [[charmm]{.doc}]dihedral_charmm.md){.reference .internal}                                         k,n,d                     type dihedrals
  [[charmmfsw]{.doc}]dihedral_charmm.md){.reference .internal}                                      k,n,d                     type dihedrals
  [[class2]{.doc}]dihedral_class2.md){.reference .internal}                                         k1,k2,k3,phi1,phi2,phi3   type dihedrals
  [[cosine/squared/restricted]{.doc}]dihedral_cosine_squared_restricted.md){.reference .internal}   k,phi0                    type dihedrals
  [[helix]{.doc}]dihedral_helix.md){.reference .internal}                                           a,b,c                     type dihedrals
  [[multi/harmonic]{.doc}]dihedral_multi_harmonic.md){.reference .internal}                         a1,a2,a3,a4,a5            type dihedrals
  [[opls]{.doc}]dihedral_opls.md){.reference .internal}                                             k1,k2,k3,k4               type dihedrals
  [[quadratic]{.doc}]dihedral_quadratic.md){.reference .internal}                                   k,phi0                    type dihedrals
  ---------------------------------------------------------------------------------------------------- ------------------------- ----------------

Note that internally, phi0 is stored in radians, so the variable this fix use to reset phi0 needs to generate values in radians.

------------------------------------------------------------------------

::: versionadded
[Added in version 2Apr2025.]{.versionmodified .added}
:::

The *improper* keyword uses the specified variable to change the value of an improper coefficient over time, very similar to how the *angle* keyword operates. The only difference is that now an improper coefficient for a given improper type is adapted.

A wild-card asterisk can be used in place of or in conjunction with the improper type argument to set the coefficients for multiple improper types. This takes the form "\*" or "\*n" or "m\*" or "m\*n". If [\\(N\\)]{.math .notranslate .nohighlight} is the number of improper types, then an asterisk with no numeric values means all types from 1 to [\\(N\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to [\\(N\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive).

If [[improper_style hybrid]{.doc}]improper_hybrid.md){.reference .internal} is used, *istyle* should be a sub-style name. The improper styles that currently work with fix adapt are:

  -------------------------------------------------------------------------------------- ------------ ----------------
  [[amoeba]{.doc}]improper_amoeba.md){.reference .internal}                           k            type impropers
  [[class2]{.doc}]improper_class2.md){.reference .internal}                           k,chi0       type impropers
  [[cossq]{.doc}]improper_cossq.md){.reference .internal}                             k,chi0       type impropers
  [[cvff]{.doc}]improper_cvff.md){.reference .internal}                               k,d,n        type impropers
  [[distance]{.doc}]improper_distance.md){.reference .internal}                       k2,k4        type impropers
  [[distharm]{.doc}]improper_distharm.md){.reference .internal}                       k,d0         type impropers
  [[fourier]{.doc}]improper_fourier.md){.reference .internal}                         k,C0,C1,C2   type impropers
  [[harmonic]{.doc}]improper_harmonic.md){.reference .internal}                       k,chi0       type impropers
  [[inversion/harmonic]{.doc}]improper_inversion_harmonic.md){.reference .internal}   k,w0         type impropers
  [[ring]{.doc}]improper_ring.md){.reference .internal}                               k,theta0     type impropers
  [[umbrella]{.doc}]improper_umbrella.md){.reference .internal}                       k,w0         type impropers
  [[sqdistharm]{.doc}]improper_sqdistharm.md){.reference .internal}                   k            type impropers
  -------------------------------------------------------------------------------------- ------------ ----------------

Note that internally, chi0 and theta0 are stored in radians, so the variable this fix use to reset chi0 or theta0 needs to generate values in radians.

------------------------------------------------------------------------

The *kspace* keyword used the specified variable as a scale factor on the energy, forces, virial calculated by whatever [\\(k\\)]{.math .notranslate .nohighlight}-space solver is defined by the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command. If the variable has a value of 1.0, then the solver is unaltered.

The *kspace* keyword works this way whether the *scale* keyword is set to *no* or *yes*.

------------------------------------------------------------------------

The *atom* keyword enables various atom properties to be changed. The *aparam* argument is the name of the parameter to change. This is the current list of atom parameters that can be varied by this fix:

- charge = charge on particle

- diameter or diameter/disc = diameter of particle

The *v_name* argument of the *atom* keyword is the name of an [[equal-style variable]{.doc}]variable.md){.reference .internal} which will be evaluated each time this fix is invoked to set, or scale the parameter to a new value. It should be specified as v_name, where name is the variable name. See the discussion above describing the formulas associated with equal-style variables. The new value is assigned to the corresponding attribute for all atoms in the fix group.

If the atom parameter is *diameter* and per-atom density and per-atom mass are defined for particles (e.g., [[atom_style granular]{.doc}]atom_style.md){.reference .internal}), then the mass of each particle is, by default, also changed when the diameter changes. The mass is set from the particle volume for 3d systems (density is assumed to stay constant). For 2d, the default is for LAMMPS to model particles with a radius attribute as spheres. However, if the atom parameter is *diameter/disc*, then the mass is set from the particle area (the density is assumed to be in mass/distance[\\(\^2\\)]{.math .notranslate .nohighlight} units). The mass of the particle may also be kept constant if the *mass* keyword is set to *no*. This can be useful to account for diameter changes that do not involve mass changes (e.g., thermal expansion).

For example, these commands would shrink the diameter of all granular particles in the "center" group from 1.0 to 0.1 in a linear fashion over the course of a 1000-step simulation:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable size equal ramp(1.0,0.1)
    fix 1 center adapt 10 atom diameter v_size
:::
::::

------------------------------------------------------------------------

This fix can be used in long simulations which are restarted one or more times to continuously adapt simulation parameters, but it must be done carefully. There are two issues to consider. The first is how to adapt the parameters in a continuous manner from one simulation to the next. The second is how, if desired, to reset the parameters to their original values at the end of the last restarted run.

Note that all the parameters changed by this fix are written into a restart file in their current changed state. A new restarted simulation does not know the original time=0 values, unless the input script explicitly resets the parameters (after the restart file is read) to the original values.

Also note that the time-dependent variable(s) used in the restart script should typically be written as a function of time elapsed since the original simulation began.

With this in mind, if the *scale* keyword is set to *no* (the default) in a restarted simulation, original parameters are not needed. The adapted parameters should seamlessly continue their variation relative to the preceding simulation.

If the *scale* keyword is set to *yes*, then the input script should typically reset the parameters being adapted to their original values, so that the scaling formula specified by the variable will operate correctly. An exception is if the *atom* keyword is being used with *scale yes*. In this case, information is added to the restart file so that per-atom properties in the new run will automatically be scaled relative to their original values. This will only work if the fix adapt command specified in the restart script has the same ID as the one used in the original script.

In a restarted run, if the *reset* keyword is set to *yes*, and the run ends in this script (as opposed to just writing more restart files), parameters will be restored to the values they were at the beginning of the run command in the restart script, which as explained above, may or may not be the original values of the parameters. Again, an exception is if the *atom* keyword is being used with *reset yes* (in all the runs). In that case, the original per-atom parameters are stored in the restart file, and will be restored when the restarted run finally completes.
::::::::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

If the *atom* keyword is used and the *scale* or *reset* keyword is set to *yes*, then this fix writes information to a restart file so that in a restarted run scaling can continue in a seamless manner and/or the per-atom values can be restored, as explained above.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.

For [[rRESPA time integration]{.doc}]run_style.md){.reference .internal}, this fix changes parameters on the outermost rRESPA level.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute ti]{.doc}]compute_ti.md){.reference .internal}, [[fix adapt/fep]{.doc}]fix_adapt_fep.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are scale = no, reset = no, mass = yes.
:::
:::::::::::::::::::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

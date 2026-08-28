:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#pair-style-eff-cut-command .section}
[]{#index-0}

# pair_style eff/cut command[](#pair-style-eff-cut-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style eff/cut cutoff keyword args ...
:::
::::

- cutoff = global cutoff for Coulombic interactions

- zero or more keyword/value pairs may be appended

  ``` literal-block
  keyword = limit/eradius or pressure/evirials or ecp
    limit/eradius args = none
    pressure/evirials args = none
    ecp args = type element type element ...
      type = LAMMPS atom type (1 to Ntypes)
      element = element symbol (e.g. H, Si)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style eff/cut 39.7
    pair_style eff/cut 40.0 limit/eradius
    pair_style eff/cut 40.0 limit/eradius pressure/evirials
    pair_style eff/cut 40.0 ecp 1 Si 3 C
    pair_coeff * *
    pair_coeff 2 2 20.0
    pair_coeff 1 s 0.320852 2.283269 0.814857
    pair_coeff 3 p 22.721015 0.728733 1.103199 17.695345 6.693621
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This pair style contains a LAMMPS implementation of the electron Force Field (eFF) potential currently under development at Caltech, as described in [[(Jaramillo-Botero)]{.std .std-ref}](#jaramillo-botero){.reference .internal}. The eFF for Z\<6 was first introduced by [[(Su)]{.std .std-ref}](#su){.reference .internal} in 2007. It has been extended to higher Zs by using effective core potentials (ECPs) that now cover up to second and third row p-block elements of the periodic table.

eFF can be viewed as an approximation to QM wave packet dynamics and Fermionic molecular dynamics, combining the ability of electronic structure methods to describe atomic structure, bonding, and chemistry in materials, and of plasma methods to describe nonequilibrium dynamics of large systems with a large number of highly excited electrons. Yet, eFF relies on a simplification of the electronic wave function in which electrons are described as floating Gaussian wave packets whose position and size respond to the various dynamic forces between interacting classical nuclear particles and spherical Gaussian electron wave packets. The wave function is taken to be a Hartree product of the wave packets. To compensate for the lack of explicit antisymmetry in the resulting wave function, a spin-dependent Pauli potential is included in the Hamiltonian. Substituting this wave function into the time-dependent Schrodinger equation produces equations of motion that correspond - to second order - to classical Hamiltonian relations between electron position and size, and their conjugate momenta. The N-electron wave function is described as a product of one-electron Gaussian functions, whose size is a dynamical variable and whose position is not constrained to a nuclear center. This form allows for straightforward propagation of the wave function, with time, using a simple formulation from which the equations of motion are then integrated with conventional MD algorithms. In addition to this spin-dependent Pauli repulsion potential term between Gaussians, eFF includes the electron kinetic energy from the Gaussians. These two terms are based on first-principles quantum mechanics. On the other hand, nuclei are described as point charges, which interact with other nuclei and electrons through standard electrostatic potential forms.

The full Hamiltonian (shown below), contains then a standard description for electrostatic interactions between a set of delocalized point and Gaussian charges which include, nuclei-nuclei (NN), electron-electron (ee), and nuclei-electron (Ne). Thus, eFF is a mixed QM-classical mechanics method rather than a conventional force field method (in which electron motions are averaged out into ground state nuclear motions, i.e a single electronic state, and particle interactions are described via empirically parameterized interatomic potential functions). This makes eFF uniquely suited to simulate materials over a wide range of temperatures and pressures where electronically excited and ionized states of matter can occur and coexist. Furthermore, the interactions between particles -nuclei and electrons- reduce to the sum of a set of effective pairwise potentials in the eFF formulation. The *eff/cut* style computes the pairwise Coulomb interactions between nuclei and electrons (E_NN,E_Ne,E_ee), and the quantum-derived Pauli (E_PR) and Kinetic energy interactions potentials between electrons (E_KE) for a total energy expression given as,

::: {.math .notranslate .nohighlight}
\\\[U\\left(R,r,s\\right) = E\_{NN} \\left( R \\right) + E\_{Ne} \\left( {R,r,s} \\right) + E\_{ee} \\left( {r,s} \\right) + E\_{KE} \\left( {r,s} \\right) + E\_{PR} \\left( { \\uparrow \\downarrow ,S} \\right)\\\]
:::

The individual terms are defined as follows:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E\_{KE} = & \\frac{\\hbar\^2 }{{m\_{e} }}\\sum\\limits_i {\\frac{3}{{2s_i\^2 }}} \\\\ E\_{NN} = & \\frac{1}{{4\\pi \\varepsilon \_0 }}\\sum\\limits\_{i \< j} {\\frac{{Z_i Z_j }}{{R\_{ij} }}} \\\\ E\_{Ne} = & - \\frac{1}{{4\\pi \\varepsilon \_0 }}\\sum\\limits\_{i,j} {\\frac{{Z_i }}{{R\_{ij} }}Erf\\left( {\\frac{{\\sqrt 2 R\_{ij} }}{{s_j }}} \\right)} \\\\ E\_{ee} = & \\frac{1}{{4\\pi \\varepsilon \_0 }}\\sum\\limits\_{i \< j} {\\frac{1}{{r\_{ij} }}Erf\\left( {\\frac{{\\sqrt 2 r\_{ij} }}{{\\sqrt {s_i\^2 + s_j\^2 } }}} \\right)} \\\\ E\_{Pauli} = & \\sum\\limits\_{\\sigma \_i = \\sigma \_j } {E\\left( { \\uparrow \\uparrow } \\right)\_{ij}} + \\sum\\limits\_{\\sigma \_i \\ne \\sigma \_j } {E\\left( { \\uparrow \\downarrow } \\right)\_{ij}} \\\\\\end{split}\\\]
:::

where, s_i correspond to the electron sizes, the sigmas i's to the fixed spins of the electrons, Z_i to the charges on the nuclei, R_ij to the distances between the nuclei or the nuclei and electrons, and r_ij to the distances between electrons. For additional details see [[(Jaramillo-Botero)]{.std .std-ref}](#jaramillo-botero){.reference .internal}.

The overall electrostatics energy is given in Hartree units of energy by default and can be modified by an energy-conversion constant, according to the units chosen (see [[electron_units]{.doc}]units.md){.reference .internal}). The cutoff Rc, given in Bohrs (by default), truncates the interaction distance. The recommended cutoff for this pair style should follow the minimum image criterion, i.e. half of the minimum unit cell length.

This potential is designed to be used with [[atom_style electron]{.doc}]atom_style.md){.reference .internal} definitions, in order to handle the description of systems with interacting nuclei and explicit electrons.

The following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands, or by mixing as described below:

- cutoff (distance units)

For *eff/cut*, the cutoff coefficient is optional. If it is not used (as in some of the examples above), the default global value specified in the pair_style command is used.

------------------------------------------------------------------------

The *limit/eradius* and *pressure/evirials* keywords are optional. Neither or both must be specified. If not specified they are unset.

The *limit/eradius* keyword is used to restrain electron size from becoming excessively diffuse at very high temperatures were the Gaussian wave packet representation breaks down, and from expanding as free particles to infinite size. If unset, electron radius is free to increase without bounds. If set, a restraining harmonic potential of the form E = 1/2k_ss\^2 for s \> L_box/2, where k_s = 1 Hartrees/Bohr\^2, is applied on the electron radius.

The *pressure/evirials* keyword is used to control between two types of pressure computation: if unset, the computed pressure does not include the electronic radial virials contributions to the total pressure (scalar or tensor). If set, the computed pressure will include the electronic radial virial contributions to the total pressure (scalar and tensor).

The *ecp* keyword is used to associate an ECP representation for a particular atom type. The ECP captures the orbital overlap between a core pseudo particle and valence electrons within the Pauli repulsion. A list of type:element-symbol pairs may be provided for all ECP representations, after the "ecp" keyword.

::: {.admonition .note}
Note

Default ECP parameters are provided for C, N, O, Al, and Si. Users can modify these using the pair_coeff command as exemplified above. For this, the User must distinguish between two different functional forms supported, one that captures the orbital overlap assuming the s-type core interacts with an s-like valence electron (s-s) and another that assumes the interaction is s-p. For systems that exhibit significant p-character (e.g. C, N, O) the s-p form is recommended. The "s" ECP form requires 3 parameters and the "p" 5 parameters.
:::

::: {.admonition .note}
Note

There are two different pressures that can be reported for eFF when defining this pair_style, one (default) that considers electrons do not contribute radial virial components (i.e. electrons treated as incompressible 'rigid' spheres) and one that does. The radial electronic contributions to the virials are only tallied if the flexible pressure option is set, and this will affect both global and per-atom quantities. In principle, the true pressure of a system is somewhere in between the rigid and the flexible eFF pressures, but, for most cases, the difference between these two pressures will not be significant over long-term averaged runs (i.e. even though the energy partitioning changes, the total energy remains similar).
:::

------------------------------------------------------------------------

::: {.admonition .note}
Note

This implementation of eFF gives a reasonably accurate description for systems containing nuclei from Z = 1-6 in "all electron" representations. For systems with increasingly non-spherical electrons, Users should use the ECP representations. ECPs are now supported and validated for most of the second and third row elements of the p-block. Predefined parameters are provided for C, N, O, Al, and Si. The ECP captures the orbital overlap between the core and valence electrons (i.e. Pauli repulsion) with one of the functional forms:
:::

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E\_{Pauli(ECP_s)} = & p_1\\exp\\left(-\\frac{p_2r\^2}{p_3+s\^2} \\right) \\\\ E\_{Pauli(ECP_p)} = & p_1\\left( \\frac{2}{p_2/s+s/p_2} \\right)\\left( r-p_3s\\right)\^2\\exp \\left\[ -\\frac{p_4\\left( r-p_3s \\right)\^2}{p_5+s\^2} \\right\]\\end{split}\\\]
:::

Where the first form correspond to core interactions with s-type valence electrons and the second to core interactions with p-type valence electrons.

The current version adds full support for models with fixed-core and ECP definitions. to enable larger timesteps (i.e. by avoiding the high frequency vibrational modes -translational and radial- of the 2 s electrons), and in the ECP case to reduce the increased orbital complexity in higher Z elements (up to Z\<18). A fixed-core should be defined with a mass that includes the corresponding nuclear mass plus the 2 s electrons in atomic mass units (2x5.4857990943e-4), and a radius equivalent to that of minimized 1s electrons (see examples under /examples/PACKAGES/eff/fixed-core). An pseudo-core should be described with a mass that includes the corresponding nuclear mass, plus all the core electrons (i.e no outer shell electrons), and a radius equivalent to that of a corresponding minimized full-electron system. The charge for a pseudo-core atom should be given by the number of outer shell electrons.

In general, eFF excels at computing the properties of materials in extreme conditions and tracing the system dynamics over multi-picosecond timescales; this is particularly relevant where electron excitations can change significantly the nature of bonding in the system. It can capture with surprising accuracy the behavior of such systems because it describes consistently and in an unbiased manner many different kinds of bonds, including covalent, ionic, multicenter, ionic, and plasma, and how they interconvert and/or change when they become excited. eFF also excels in computing the relative thermochemistry of isodemic reactions and conformational changes, where the bonds of the reactants are of the same type as the bonds of the products. eFF assumes that kinetic energy differences dominate the overall exchange energy, which is true when the electrons present are nearly spherical and nodeless and valid for covalent compounds such as dense hydrogen, hydrocarbons, and diamond; alkali metals (e.g. lithium), alkali earth metals (e.g. beryllium) and semimetals such as boron; and various compounds containing ionic and/or multicenter bonds, such as boron dihydride.
:::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, the cutoff distance for the *eff/cut* style can be mixed. The default mix value is *geometric*. See the "pair_modify" command for details.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option is not relevant for these pair styles.

The *eff/long* (not yet available) style supports the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option for tabulation of the short-range portion of the long-range Coulombic interaction.

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

These pair styles write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so pair_style and pair_coeff commands do not need to be specified in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles will only be enabled if LAMMPS is built with the EFF package. It will only be enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

These pair styles require that particles store electron attributes such as radius, radial velocity, and radial force, as defined by the [[atom_style]{.doc}]atom_style.md){.reference .internal}. The *electron* atom style does all of this.

Thes pair styles require you to use the [[comm_modify vel yes]{.doc}]comm_modify.md){.reference .internal} command so that velocities are stored by ghost atoms.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

If not specified, limit_eradius = 0 and pressure_with_evirials = 0.

------------------------------------------------------------------------

**(Su)** Su and Goddard, Excited Electron Dynamics Modeling of Warm Dense Matter, Phys Rev Lett, 99:185003 (2007).

**(Jaramillo-Botero)** Jaramillo-Botero, Su, Qi, Goddard, Large-scale, Long-term Non-adiabatic Electron Molecular Dynamics for Describing Material Properties and Phenomena in Extreme Environments, J Comp Chem, 32, 497-512 (2011).
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

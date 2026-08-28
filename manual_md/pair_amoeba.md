:::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-amoeba-command .section}
[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style amoeba command[](#pair-style-amoeba-command "Link to this heading"){.headerlink}

Accelerator Variants: *amoeba/gpu*
:::

::::::::::::::::::::::::::: {#pair-style-hippo-command .section}
# pair_style hippo command[](#pair-style-hippo-command "Link to this heading"){.headerlink}

Accelerator Variants: *hippo/gpu*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style
:::
::::

- style = *amoeba* or *hippo*
:::::

::::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style amoeba
    pair_coeff * * protein.prm.amoeba protein.key.amoeba
:::
::::

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hippo
    pair_coeff * * water.prm.hippo water.key.hippo
:::
::::
:::::::

::: {#additional-info .section}
## Additional info[](#additional-info "Link to this heading"){.headerlink}

- [[Howto amoeba]{.doc}]Howto_amoeba.md){.reference .internal}

- examples/amoeba

- tools/amoeba

- potentials/\*.amoeba

- potentials/\*.hippo
:::

:::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *amoeba* style computes the AMOEBA polarizable field formulated by Jay Ponder's group at the U Washington at St Louis [[(Ren)]{.std .std-ref}](#amoeba-ren){.reference .internal}, [[(Shi)]{.std .std-ref}](#amoeba-shi){.reference .internal}. The *hippo* style computes the HIPPO polarizable force field, an extension to AMOEBA, formulated by Josh Rackers and collaborators in the Ponder group [[(Rackers)]{.std .std-ref}](#amoeba-rackers){.reference .internal}.

These force fields can be used when polarization effects are desired in simulations of water, organic molecules, and biomolecules including proteins, provided that parameterizations (Tinker PRM force field files) are available for the systems you are interested in. Files in the LAMMPS potentials directory with a "amoeba" or "hippo" suffix can be used. The Tinker distribution and website have additional force field files as well.

As discussed on the [[Howto amoeba]{.doc}]Howto_amoeba.md){.reference .internal} doc page, the intermolecular (non-bonded) portion of the AMOEBA force field contains these terms:

::: {.math .notranslate .nohighlight}
\\\[U\_{amoeba} = U\_{multipole} + U\_{polar} + U\_{hal}\\\]
:::

while the HIPPO force field contains these terms:

::: {.math .notranslate .nohighlight}
\\\[U\_{hippo} = U\_{multipole} + U\_{polar} + U\_{qxfer} + U\_{repulsion} + U\_{dispersion}\\\]
:::

Conceptually, these terms compute the following interactions:

- [\\(U\_{hal}\\)]{.math .notranslate .nohighlight} = buffered 14-7 van der Waals with offsets applied to hydrogen atoms

- [\\(U\_{repulsion}\\)]{.math .notranslate .nohighlight} = Pauli repulsion due to rearrangement of electron density

- [\\(U\_{dispersion}\\)]{.math .notranslate .nohighlight} = dispersion between correlated, instantaneous induced dipole moments

- [\\(U\_{multipole}\\)]{.math .notranslate .nohighlight} = electrostatics between permanent point charges, dipoles, and quadrupoles

- [\\(U\_{polar}\\)]{.math .notranslate .nohighlight} = electronic polarization between induced point dipoles

- [\\(U\_{qxfer}\\)]{.math .notranslate .nohighlight} = charge transfer effects

Note that the AMOEBA versus HIPPO force fields typically compute the same term differently using their own formulas. The references on this doc page give full details for both force fields.

The formulas for the AMOEBA energy terms are:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}U\_{hal} = & \\epsilon\_{ij} \\left( \\frac{1.07}{\\rho\_{ij} + 0.07} \\right)\^7 \\left( \\frac{1.12}{\\rho\_{ij}\^7 + 0.12} - 2 \\right) \\\\ U\_{multipole} = & \\vec{M}\_i\\boldsymbol{T\_{ij}}\\vec{M}\_j, \\quad \\mbox{with} \\quad \\vec{M} = \\left(q, \\vec{\\mu}\_{perm}, \\boldsymbol{\\Theta} \\right) \\\\ U\_{polar} = & \\frac{1}{2}\\vec{\\mu}\_i\^{ind} \\vec{E}\_i\^{perm}\\end{split}\\\]
:::

The formulas for the HIPPO energy terms are:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}U\_{multipole} = & Z_i \\frac{1}{r\_{ij}} Z_j + Z_i T\_{ij}\^{damp} \\vec{M}\_j + Z_j T\_{ji}\^{damp} \\vec{M}\_i + \\vec{M}\_i T\_{ij}\^{damp} \\vec{M}\_j, \\quad \\mbox{with} \\quad \\vec{M} = \\left(q, \\vec{\\mu}\_{perm}, \\boldsymbol{\\Theta} \\right) \\\\ U\_{polar} = & \\frac{1}{2}\\vec{\\mu}\_i\^{ind} \\vec{E}\_i\^{perm} \\\\ U\_{qxfer} = & \\epsilon_i e\^{-\\eta_j r\_{ij}} + \\epsilon_j e\^{-\\eta_i r\_{ij}} \\\\ U\_{repulsion} = & \\frac{K_i K_j}{r\_{ij}} S\^2 S\^2 = \\left( \\int{\\phi_i \\phi_j} dv \\right)\^2 = \\vec{M}\_i\\boldsymbol{T\_{ij}\^{repulsion}}\\vec{M}\_j \\\\ U\_{dispersion} = & -\\frac{C_6\^iC_6\^j}{r\_{ij}\^6} \\left( f\_{damp}\^{dispersion} \\right)\_{ij}\^2\\end{split}\\\]
:::

::: {.admonition .note}
Note

The AMOEBA and HIPPO force fields compute long-range charge, dipole, and quadrupole interactions as well as long-range dispersion effects. However, unlike other models with long-range interactions in LAMMPS, this does not require use of a KSpace style via the [[kspace_style]{.doc}]kspace_style.md){.reference .internal} command. That is because for AMOEBA and HIPPO the long-range computations are intertwined with the pairwise computations. So these pair style include both short- and long-range computations. This means the energy and virial computed by the pair style as well as the "Pair" timing reported by LAMMPS will include the long-range calculations.
:::

The implementation of the AMOEBA and HIPPO force fields in LAMMPS was done using F90 code provided by the Ponder group from their [Tinker MD code](https://dasher.wustl.edu/tinker/){.reference .external}.

The current implementation (July 2022) of AMOEBA in LAMMPS matches the version discussed in [[(Ponder)]{.std .std-ref}](#amoeba-ponder){.reference .internal}, [[(Ren)]{.std .std-ref}](#amoeba-ren){.reference .internal}, and [[(Shi)]{.std .std-ref}](#amoeba-shi){.reference .internal}. Likewise the current implementation of HIPPO in LAMMPS matches the version discussed in [[(Rackers)]{.std .std-ref}](#amoeba-rackers){.reference .internal}.

::: versionadded
[Added in version 8Feb2023.]{.versionmodified .added}
:::

Accelerator support via the GPU package is available.

------------------------------------------------------------------------

Only a single pair_coeff command is used with either the *amoeba* and *hippo* styles which specifies two Tinker files, a PRM and KEY file.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * ../potentials/protein.prm.amoeba ../potentials/protein.key.amoeba
    pair_coeff * * ../potentials/water.prm.hippo ../potentials/water.key.hippo
:::
::::

Examples of the PRM files are in the potentials directory with an \*.amoeba or \*.hippo suffix. The examples/amoeba directory has examples of both PRM and KEY files.

A Tinker PRM file is composed of sections, each of which has multiple lines. A Tinker KEY file is composed of lines, each of which has a keyword followed by zero or more parameters.

The list of PRM sections and KEY keywords which LAMMPS recognizes are listed on the [[Howto amoeba]{.doc}]Howto_amoeba.md){.reference .internal} doc page. If not recognized, the section or keyword is skipped.

Note that if the KEY file is specified as NULL, then no file is required; default values for various AMOEBA/HIPPO settings are used. The [[Howto amoeba]{.doc}]Howto_amoeba.md){.reference .internal} doc page also gives the default settings.

------------------------------------------------------------------------

::: versionadded
[Added in version 3Nov2022.]{.versionmodified .added}
:::

The *amoeba* and *hippo* pair styles support extraction of two per-atom quantities by the [[fix pair]{.doc}]fix_pair.md){.reference .internal} command. This allows the quantities to be output to files by the [[dump]{.doc}]dump.md){.reference .internal} or otherwise processed by other LAMMPS commands.

The names of the two quantities are "uind" and "uinp" for the induced dipole moments for each atom. Neither quantity needs to be triggered by the [[fix pair]{.doc}]fix_pair.md){.reference .internal} command in order for these pair styles to calculate it.
::::::::::::

------------------------------------------------------------------------

:::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} mix, shift, table, and tail options.

These pair styles do not write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.

::: {.admonition .note}
Note

Using the GPU accelerated pair styles 'amoeba/gpu' or 'hippo/gpu' when compiling the GPU package for OpenCL has a few known issues when running on integrated GPUs and the calculation may crash.

The GPU accelerated pair styles are also not (yet) compatible with single precision FFTs.
:::
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the AMOEBA package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

The AMOEBA and HIPPO potential (PRM) and KEY files provided with LAMMPS in the potentials and examples/amoeba directories are Tinker files parameterized for Tinker units. Their numeric parameters are converted by LAMMPS to its real units [[units]{.doc}]units.md){.reference .internal}. Thus you can only use these pair styles with real units.

These potentials do not yet calculate per-atom energy or virial contributions.

As explained on the [[AMOEBA and HIPPO howto]{.doc}]Howto_amoeba.md){.reference .internal} page, use of these pair styles to run a simulation with the AMOEBA or HIPPO force fields requires several things.

The first is a data file generated by the tools/tinker/tinker2lmp.py conversion script which uses Tinker file force field file input to create a data file compatible with LAMMPS.

The second is use of these commands:

- [[atom_style amoeba]{.doc}]atom_style.md){.reference .internal}

- [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal}

- [[special_bonds one/five]{.doc}]special_bonds.md){.reference .internal}

And third, depending on the model being simulated, these commands for intramolecular interactions may also be required:

- [[bond_style class2]{.doc}]bond_class2.md){.reference .internal}

- [[angle_style amoeba]{.doc}]angle_amoeba.md){.reference .internal}

- [[dihedral_style fourier]{.doc}]dihedral_fourier.md){.reference .internal}

- [[improper_style amoeba]{.doc}]improper_amoeba.md){.reference .internal}

- [[fix amoeba/pitorsion]{.doc}]fix_amoeba_pitorsion.md){.reference .internal}

- [[fix amoeba/bitorsion]{.doc}]fix_amoeba_bitorsion.md){.reference .internal}
:::

------------------------------------------------------------------------

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[atom_style amoeba]{.doc}]atom_style.md){.reference .internal}, [[bond_style class2]{.doc}]bond_class2.md){.reference .internal}, [[angle_style amoeba]{.doc}]angle_amoeba.md){.reference .internal}, [[dihedral_style fourier]{.doc}]dihedral_fourier.md){.reference .internal}, [[improper_style amoeba]{.doc}]improper_amoeba.md){.reference .internal}, [[fix amoeba/pitorsion]{.doc}]fix_amoeba_pitorsion.md){.reference .internal}, [[fix amoeba/bitorsion]{.doc}]fix_amoeba_bitorsion.md){.reference .internal}, [[special_bonds one/five]{.doc}]special_bonds.md){.reference .internal}, [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Ponder)** Ponder, Wu, Ren, Pande, Chodera, Schnieders, Haque, Mobley, Lambrecht, DiStasio Jr, M. Head-Gordon, Clark, Johnson, T. Head-Gordon, J Phys Chem B, 114, 2549-2564 (2010).

**(Rackers)** Rackers, Silva, Wang, Ponder, J Chem Theory Comput, 17, 7056-7084 (2021).

**(Ren)** Ren and Ponder, J Phys Chem B, 107, 5933 (2003).

**(Shi)** Shi, Xia, Zhang, Best, Wu, Ponder, Ren, J Chem Theory Comp, 9, 4046, 2013.
:::
:::::::::::::::::::::::::::
:::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::

::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-airebo-command .section}
[]{#index-8}[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style airebo command[](#pair-style-airebo-command "Link to this heading"){.headerlink}

Accelerator Variants: *airebo/intel*, *airebo/omp*
:::

::: {#pair-style-airebo-morse-command .section}
# pair_style airebo/morse command[](#pair-style-airebo-morse-command "Link to this heading"){.headerlink}

Accelerator Variants: *airebo/morse/intel*, *airebo/morse/omp*
:::

::::::::::::::::::: {#pair-style-rebo-command .section}
# pair_style rebo command[](#pair-style-rebo-command "Link to this heading"){.headerlink}

Accelerator Variants: *rebo/intel*, *rebo/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style cutoff LJ_flag TORSION_flag cutoff_min
:::
::::

- style = *airebo* or *airebo/morse* or *rebo*

- cutoff = LJ or Morse cutoff ([\\(\\sigma\\)]{.math .notranslate .nohighlight} scale factor) (AIREBO and AIREBO-M only)

- LJ_flag = 0/1 to turn off/on the LJ or Morse term (AIREBO and AIREBO-M only, optional)

- TORSION_flag = 0/1 to turn off/on the torsion term (AIREBO and AIREBO-M only, optional)

- cutoff_min = Start of the transition region of cutoff ([\\(\\sigma\\)]{.math .notranslate .nohighlight} scale factor) (AIREBO and AIREBO-M only, optional)
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style airebo 3.0
    pair_style airebo 2.5 1 0
    pair_coeff * * ../potentials/CH.airebo H C

    pair_style airebo/morse 3.0
    pair_coeff * * ../potentials/CH.airebo-m H C

    pair_style rebo
    pair_coeff * * ../potentials/CH.rebo H C
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *airebo* pair style computes the Adaptive Intermolecular Reactive Empirical Bond Order (AIREBO) Potential of [[(Stuart)]{.std .std-ref}](#stuart){.reference .internal} for a system of carbon and/or hydrogen atoms. Note that this is the initial formulation of AIREBO from 2000, not the later formulation.

The *airebo/morse* pair style computes the AIREBO-M potential, which is equivalent to AIREBO, but replaces the LJ term with a Morse potential. The Morse potentials are parameterized by high-quality quantum chemistry (MP2) calculations and do not diverge as quickly as particle density increases. This allows AIREBO-M to retain accuracy to much higher pressures than AIREBO (up to 40 GPa for Polyethylene). Details for this potential and its parameterization are given in [[(O'Conner)]{.std .std-ref}](#oconnor){.reference .internal}.

The *rebo* pair style computes the Reactive Empirical Bond Order (REBO) Potential of [[(Brenner)]{.std .std-ref}](#brenner){.reference .internal}. Note that this is the so-called second generation REBO from 2002, not the original REBO from 1990. As discussed below, second generation REBO is closely related to the initial AIREBO; it is just a subset of the potential energy terms with a few slightly different parameters

The AIREBO potential consists of three terms:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = \\frac{1}{2} \\sum_i \\sum\_{j \\neq i} \\left\[ E\^{\\text{REBO}}\_{ij} + E\^{\\text{LJ}}\_{ij} + \\sum\_{k \\neq i,j} \\sum\_{l \\neq i,j,k} E\^{\\text{TORSION}}\_{kijl} \\right\] \\\\\\end{split}\\\]
:::

By default, all three terms are included. For the *airebo* style, if the first two optional flag arguments to the pair_style command are included, the LJ and torsional terms can be turned off. Note that both or neither of the flags must be included. If both of the LJ an torsional terms are turned off, it becomes the second-generation REBO potential, with a small caveat on the spline fitting procedure mentioned below. This can be specified directly as pair_style *rebo* with no additional arguments.

The detailed formulas for this potential are given in [[(Stuart)]{.std .std-ref}](#stuart){.reference .internal}; here we provide only a brief description.

The [\\(E\^{\\text{REBO}}\\)]{.math .notranslate .nohighlight} term has the same functional form as the hydrocarbon REBO potential developed in [[(Brenner)]{.std .std-ref}](#brenner){.reference .internal}. The coefficients for [\\(E\^{\\text{REBO}}\\)]{.math .notranslate .nohighlight} in AIREBO are essentially the same as Brenner's potential, but a few fitted spline values are slightly different. For most cases the [\\(E\^{\\text{REBO}}\\)]{.math .notranslate .nohighlight} term in AIREBO will produce the same energies, forces and statistical averages as the original REBO potential from which it was derived. The [\\(E\^{\\text{REBO}}\\)]{.math .notranslate .nohighlight} term in the AIREBO potential gives the model its reactive capabilities and only describes short-ranged C-C, C-H and H-H interactions ([\\(r \< 2 \\AA\\)]{.math .notranslate .nohighlight}). These interactions have strong coordination-dependence through a bond order parameter, which adjusts the attraction between the I,J atoms based on the position of other nearby atoms and thus has 3- and 4-body dependence.

The [\\(E\^{\\text{LJ}}\\)]{.math .notranslate .nohighlight} term adds longer-ranged interactions ([\\(2 \< r \< \\text{cutoff}\\)]{.math .notranslate .nohighlight}) using a form similar to the standard [[Lennard Jones potential]{.doc}]pair_lj.md){.reference .internal}. The [\\(E\^{\\text{LJ}}\\)]{.math .notranslate .nohighlight} term in AIREBO contains a series of switching functions so that the short-ranged LJ repulsion ([\\(1/r\^{12}\\)]{.math .notranslate .nohighlight}) does not interfere with the energetics captured by the [\\(E\^{\\text{REBO}}\\)]{.math .notranslate .nohighlight} term. The extent of the [\\(E\^{\\text{LJ}}\\)]{.math .notranslate .nohighlight} interactions is determined by the *cutoff* argument to the pair_style command which is a scale factor. For each type pair (C-C, C-H, H-H) the cutoff is obtained by multiplying the scale factor by the sigma value defined in the potential file for that type pair. In the standard AIREBO potential, [\\(\\sigma\_{CC} = 3.4 \\AA\\)]{.math .notranslate .nohighlight}, so with a scale factor of 3.0 (the argument in pair_style), the resulting [\\(E\^{\\text{LJ}}\\)]{.math .notranslate .nohighlight} cutoff would be [\\(10.2 \\AA\\)]{.math .notranslate .nohighlight}.

By default, the longer-ranged interaction is smoothly switched off between 2.16 and 3.0 [\\(\\sigma\\)]{.math .notranslate .nohighlight}. By specifying *cutoff_min* in addition to *cutoff*, the switching can be configured to take place between *cutoff_min* and *cutoff*. *cutoff_min* can only be specified if all optional arguments are given.

The [\\(E\^{\\text{TORSION}}\\)]{.math .notranslate .nohighlight} term is an explicit 4-body potential that describes various dihedral angle preferences in hydrocarbon configurations.

------------------------------------------------------------------------

Only a single pair_coeff command is used with the *airebo*, *airebo* or *rebo* style which specifies an AIREBO, REBO, or AIREBO-M potential file with parameters for C and H. Note that as of LAMMPS version 15 May 2019 the *rebo* style in LAMMPS uses its own potential file (CH.rebo). These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- [\\(N\\)]{.math .notranslate .nohighlight} element names = mapping of AIREBO elements to atom types

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for the potential file.

As an example, if your LAMMPS simulation has 4 atom types and you want the first 3 to be C, and the fourth to be H, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * CH.airebo C C C H
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The first three C arguments map LAMMPS atom types 1,2,3 to the C element in the AIREBO file. The final H argument maps LAMMPS atom type 4 to the H element in the AIREBO file. If a mapping value is specified as NULL, the mapping is not performed. This can be used when a *airebo* potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials.

The parameters/coefficients for the AIREBO potentials are listed in the CH.airebo file to agree with the original [[(Stuart)]{.std .std-ref}](#stuart){.reference .internal} paper. Thus the parameters are specific to this potential and the way it was fit, so modifying the file should be done cautiously.

Similarly the parameters/coefficients for the AIREBO-M potentials are listed in the CH.airebo-m file to agree with the [[(O'Connor)]{.std .std-ref}](#oconnor){.reference .internal} paper. Thus the parameters are specific to this potential and the way it was fit, so modifying the file should be done cautiously. The AIREBO-M Morse potentials were parameterized using a cutoff of 3.0 ([\\(\\sigma\\)]{.math .notranslate .nohighlight}). Modifying this cutoff may impact simulation accuracy.

This pair style tallies a breakdown of the total AIREBO potential energy into sub-categories, which can be accessed via the [[compute pair]{.doc}]compute_pair.md){.reference .internal} command as a vector of values of length 3. The 3 values correspond to the following sub-categories:

1.  [\\(E\_{\\text{REBO}}\\)]{.math .notranslate .nohighlight} = REBO energy

2.  [\\(E\_{\\text{LJ}}\\)]{.math .notranslate .nohighlight} = Lennard-Jones energy

3.  [\\(E\_{\\text{TORSION}}\\)]{.math .notranslate .nohighlight} = Torsion energy

To print these quantities to the log file (with descriptive column headings) the following commands could be included in an input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 0 all pair airebo
    variable REBO     equal c_0[1]
    variable LJ       equal c_0[2]
    variable TORSION  equal c_0[3]
    thermo_style custom step temp epair v_REBO v_LJ v_TORSION
:::
::::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

These pair styles do not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} mix, shift, table, and tail options.

These pair styles do not write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. They do not support the *inner*, *middle*, *outer* keywords.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the MANYBODY package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

These pair potentials require the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

The CH.airebo and CH.airebo-m potential files provided with LAMMPS (see the potentials directory) are parameterized for metal [[units]{.doc}]units.md){.reference .internal}. You can use the pair styles with *any* LAMMPS units, but you would need to create your own AIREBO or AIREBO-M potential file with coefficients listed in the appropriate units, if your simulation does not use "metal" units.

The pair styles provided here **only** support potential files parameterized for the elements carbon and hydrogen (designated with "C" and "H" in the *pair_coeff* command. Using potential files for other elements will trigger an error.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Stuart)** Stuart, Tutein, Harrison, J Chem Phys, 112, 6472-6486 (2000).

**(Brenner)** Brenner, Shenderova, Harrison, Stuart, Ni, Sinnott, J Physics: Condensed Matter, 14, 783-802 (2002).

**(O'Connor)** O'Connor et al., J. Chem. Phys. 142, 024903 (2015).
:::
:::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

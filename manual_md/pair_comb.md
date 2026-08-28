::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-comb-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style comb command[](#pair-style-comb-command "Link to this heading"){.headerlink}

Accelerator Variants: *comb/omp*
:::

:::::::::::::::::: {#pair-style-comb3-command .section}
# pair_style comb3 command[](#pair-style-comb3-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style comb
    pair_style comb3 keyword
:::
::::

``` literal-block
keyword = polar
  polar value = polar_on or polar_off = whether or not to include atomic polarization
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style comb
    pair_coeff * * ../potentials/ffield.comb Si
    pair_coeff * * ../potentials/ffield.comb Hf Si O

    pair_style comb3 polar_off
    pair_coeff * * ../potentials/ffield.comb3 O Cu N C O
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *comb* computes the second generation variable charge COMB (Charge-Optimized Many-Body) potential. Style *comb3* computes the third-generation COMB potential. These COMB potentials are described in [[(COMB)]{.std .std-ref}](#comb){.reference .internal} and [[(COMB3)]{.std .std-ref}](#comb3){.reference .internal}. Briefly, the total energy [\\(E_T\\)]{.math .notranslate .nohighlight} of a system of atoms is given by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E_T = & \\sum_i \[ E_i\^{self} (q_i) + \\sum\_{j\>i} \[E\_{ij}\^{short} (r\_{ij}, q_i, q_j) + E\_{ij}\^{Coul} (r\_{ij}, q_i, q_j)\] + \\\\ & E\^{polar} (q_i, r\_{ij}) + E\^{vdW} (r\_{ij}) + E\^{barr} (q_i) + E\^{corr} (r\_{ij}, \\theta\_{jik})\]\\end{split}\\\]
:::

where [\\(E_i\^{self}\\)]{.math .notranslate .nohighlight} is the self-energy of atom *i* (including atomic ionization energies and electron affinities), [\\(E\_{ij}\^{short}\\)]{.math .notranslate .nohighlight} is the bond-order potential between atoms *i* and *j*, [\\(E\_{ij}\^{Coul}\\)]{.math .notranslate .nohighlight} is the Coulomb interactions, [\\(E\^{polar}\\)]{.math .notranslate .nohighlight} is the polarization term for organic systems (style *comb3* only), [\\(E\^{vdW}\\)]{.math .notranslate .nohighlight} is the van der Waals energy (style *comb3* only), [\\(E\^{barr}\\)]{.math .notranslate .nohighlight} is a charge barrier function, and [\\(E\^{corr}\\)]{.math .notranslate .nohighlight} are angular correction terms.

The COMB potentials (styles *comb* and *comb3*) are variable charge potentials. The equilibrium charge on each atom is calculated by the electronegativity equalization (QEq) method. See [[Rick]{.std .std-ref}](#rick2){.reference .internal} for further details. This is implemented by the [[fix qeq/comb]{.doc}]fix_qeq_comb.md){.reference .internal} command, which should normally be specified in the input script when running a model with the COMB potential. The [[fix qeq/comb]{.doc}]fix_qeq_comb.md){.reference .internal} command has options that determine how often charge equilibration is performed, its convergence criterion, and which atoms are included in the calculation.

Only a single pair_coeff command is used with the *comb* and *comb3* styles which specifies the COMB potential file with parameters for all needed elements. These are mapped to LAMMPS atom types by specifying N additional arguments after the potential file in the pair_coeff command, where N is the number of LAMMPS atom types.

For example, if your LAMMPS simulation of a Si/SiO2/ HfO2 interface has 4 atom types, and you want the first and last to be Si, the second to be Hf, and the third to be O, and you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * ../potentials/ffield.comb Si Hf O Si
:::
::::

The first two arguments must be \* \* so as to span all LAMMPS atom types. The first and last Si arguments map LAMMPS atom types 1 and 4 to the Si element in the *ffield.comb* file. The second Hf argument maps LAMMPS atom type 2 to the Hf element, and the third O argument maps LAMMPS atom type 3 to the O element in the potential file. If a mapping value is specified as NULL, the mapping is not performed. This can be used when a *comb* potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials.

For style *comb*, the provided potential file *ffield.comb* contains all currently-available second generation COMB parameterizations: for Si, Cu, Hf, Ti, O, their oxides and Zr, Zn and U metals. For style *comb3*, the potential file *ffield.comb3* contains all currently-available third generation COMB parameterizations: O, Cu, N, C, H, Ti, Zn and Zr. The status of the optimization of the compounds, for example Cu2O, TiN and hydrocarbons, are given in the following table:

  ---- --- ---- --- --- --- ---- ---- ----
       O   Cu   N   C   H   Ti   Zn   Zr
  O    F   F    F   F   F   F    F    F
  Cu   F   F    P   F   F   P    F    P
  N    F   P    F   M   F   P    P    P
  C    F   F    M   F   F   M    M    M
  H    F   F    F   F   F   M    M    F
  Ti   F   P    P   M   M   F    P    P
  Zn   F   F    P   M   M   P    F    P
  Zr   F   P    P   M   F   P    P    F
  ---- --- ---- --- --- --- ---- ---- ----

- F = Fully optimized

- M = Only optimized for dimer molecule

- P = in progress, but have it from mixing rule

For style *comb3*, in addition to ffield.comb3, a special parameter file, *lib.comb3*, that is exclusively used for C/O/H systems, will be automatically loaded if carbon atom is detected in LAMMPS input structure. This file must be in your working directory or in the directories listed in the environment variable [`LAMMPS_POTENTIALS`{.docutils .literal .notranslate}]{.pre}, as described on the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command doc page.

The keyword *polar* indicates whether the force field includes the atomic polarization. Since the equilibration of the polarization has not yet been implemented, it can only set polar_off at present.

::: {.admonition .note}
Note

You can not use potential file *ffield.comb* with style *comb3*, nor file *ffield.comb3* with style *comb*.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, where types I and J correspond to two different element types, mixing is performed by LAMMPS as described above from values in the potential file.

These pair styles does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

These pair styles do not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style, pair_coeff, and [[fix qeq/comb]{.doc}]fix_qeq_comb.md){.reference .internal} commands in an input script that reads a restart file.

These pair styles can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the MANYBODY package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

These pair styles requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

The COMB potentials in the *ffield.comb* and *ffield.comb3* files provided with LAMMPS (see the potentials directory) are parameterized for metal [[units]{.doc}]units.md){.reference .internal}. You can use the COMB potential with any LAMMPS units, but you would need to create your own COMB potential file with coefficients listed in the appropriate units if your simulation does not use "metal" units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style]{.doc}]pair_style.md){.reference .internal}, [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix qeq/comb]{.doc}]fix_qeq_comb.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(COMB)** T.-R. Shan, B. D. Devine, T. W. Kemper, S. B. Sinnott, and S. R. Phillpot, Phys. Rev. B 81, 125328 (2010)

**(COMB3)** T. Liang, T.-R. Shan, Y.-T. Cheng, B. D. Devine, M. Noordhoek, Y. Li, Z. Lu, S. R. Phillpot, and S. B. Sinnott, Mat. Sci. & Eng: R 74, 255-279 (2013).

**(Rick)** S. W. Rick, S. J. Stuart, B. J. Berne, J Chem Phys 101, 6141 (1994).
:::
::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

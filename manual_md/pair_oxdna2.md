:::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-oxdna2-excv-command .section}
[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style oxdna2/excv command[](#pair-style-oxdna2-excv-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-oxdna2-stk-command .section}
# pair_style oxdna2/stk command[](#pair-style-oxdna2-stk-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-oxdna2-hbond-command .section}
# pair_style oxdna2/hbond command[](#pair-style-oxdna2-hbond-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-oxdna2-xstk-command .section}
# pair_style oxdna2/xstk command[](#pair-style-oxdna2-xstk-command "Link to this heading"){.headerlink}
:::

::: {#pair-style-oxdna2-coaxstk-command .section}
# pair_style oxdna2/coaxstk command[](#pair-style-oxdna2-coaxstk-command "Link to this heading"){.headerlink}
:::

::::::::::::::::::::::: {#pair-style-oxdna2-dh-command .section}
# pair_style oxdna2/dh command[](#pair-style-oxdna2-dh-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style1

    pair_coeff * * style2 args
:::
::::

- style1 = *hybrid/overlay oxdna2/excv oxdna2/stk oxdna2/hbond oxdna2/xstk oxdna2/coaxstk oxdna2/dh*

- style2 = *oxdna2/excv* or *oxdna2/stk* or *oxdna2/hbond* or *oxdna2/xstk* or *oxdna2/coaxstk* or *oxdna2/dh*

- args = list of arguments for these particular styles

``` literal-block
oxdna2/stk args = seq T xi kappa 6.0 0.4 0.9 0.32 0.75 1.3 0 0.8 0.9 0 0.95 0.9 0 0.95 2.0 0.65 2.0 0.65
  seq = seqav (for average sequence stacking strength) or seqdep (for sequence-dependent stacking strength)
  T = temperature (LJ units: 0.1 = 300 K, real units: 300 = 300 K)
  xi = 1.3523 (LJ units) or 8.06199211612242 (real units), temperature-independent coefficient in stacking strength
  kappa = 2.6717 (LJ units) or 0.005309213 (real units), coefficient of linear temperature dependence in stacking strength
oxdna2/hbond args = seq eps 8.0 0.4 0.75 0.34 0.7 1.5 0 0.7 1.5 0 0.7 1.5 0 0.7 0.46 3.141592653589793 0.7 4.0 1.5707963267948966 0.45 4.0 1.5707963267948966 0.45
  seq = seqav (for average sequence base-pairing strength) or seqdep (for sequence-dependent base-pairing strength)
  eps = 1.0678 (LJ units) or 6.36589157849259 (real units), average hydrogen bonding strength between A-T and C-G Watson-Crick base pairs, 0 between all other pairs
oxdna2/dh args = T rhos qeff
  T = temperature (LJ units: 0.1 = 300 K, real units: 300 = 300 K)
  rhos = salt concentration (mole per litre)
  qeff = 0.815 (effective charge in elementary charges)
```
:::::

:::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # LJ units
    pair_style hybrid/overlay oxdna2/excv oxdna2/stk oxdna2/hbond oxdna2/xstk oxdna2/coaxstk oxdna2/dh
    pair_coeff * * oxdna2/excv    2.0 0.7 0.675 2.0 0.515 0.5 2.0 0.33 0.32
    pair_coeff * * oxdna2/stk     seqdep 0.1 1.3523 2.6717 6.0 0.4 0.9 0.32 0.75 1.3 0 0.8 0.9 0 0.95 0.9 0 0.95 2.0 0.65 2.0 0.65
    pair_coeff * * oxdna2/hbond   seqdep 0.0 8.0 0.4 0.75 0.34 0.7 1.5 0 0.7 1.5 0 0.7 1.5 0 0.7 0.46 3.141592653589793 0.7 4.0 1.5707963267948966 0.45 4.0 1.5707963267948966 0.45
    pair_coeff 1 4 oxdna2/hbond   seqdep 1.0678 8.0 0.4 0.75 0.34 0.7 1.5 0 0.7 1.5 0 0.7 1.5 0 0.7 0.46 3.141592653589793 0.7 4.0 1.5707963267948966 0.45 4.0 1.5707963267948966 0.45
    pair_coeff 2 3 oxdna2/hbond   seqdep 1.0678 8.0 0.4 0.75 0.34 0.7 1.5 0 0.7 1.5 0 0.7 1.5 0 0.7 0.46 3.141592653589793 0.7 4.0 1.5707963267948966 0.45 4.0 1.5707963267948966 0.45
    pair_coeff * * oxdna2/xstk    47.5 0.575 0.675 0.495 0.655 2.25 0.791592653589793 0.58 1.7 1.0 0.68 1.7 1.0 0.68 1.5 0 0.65 1.7 0.875 0.68 1.7 0.875 0.68
    pair_coeff * * oxdna2/coaxstk 58.5 0.4 0.6 0.22 0.58 2.0 2.891592653589793 0.65 1.3 0 0.8 0.9 0 0.95 0.9 0 0.95 40.0 3.116592653589793
    pair_coeff * * oxdna2/dh      0.1 0.5 0.815

    pair_style hybrid/overlay oxdna2/excv oxdna2/stk oxdna2/hbond oxdna2/xstk oxdna2/coaxstk oxdna2/dh
    pair_coeff * * oxdna2/excv    oxdna2_lj.cgdna
    pair_coeff * * oxdna2/stk     seqdep 0.1 1.3523 2.6717 oxdna2_lj.cgdna
    pair_coeff * * oxdna2/hbond   seqdep oxdna2_lj.cgdna
    pair_coeff 1 4 oxdna2/hbond   seqdep oxdna2_lj.cgdna
    pair_coeff 2 3 oxdna2/hbond   seqdep oxdna2_lj.cgdna
    pair_coeff * * oxdna2/xstk    oxdna2_lj.cgdna
    pair_coeff * * oxdna2/coaxstk oxdna2_lj.cgdna
    pair_coeff * * oxdna2/dh      0.1 0.5 oxdna2_lj.cgdna

    # Real units
    pair_style hybrid/overlay oxdna2/excv oxdna2/stk oxdna2/hbond oxdna2/xstk oxdna2/coaxstk oxdna2/dh
    pair_coeff * * oxdna2/excv    11.92337812042065 5.9626 5.74965 11.92337812042065 4.38677 4.259 11.92337812042065 2.81094 2.72576
    pair_coeff * * oxdna2/stk     seqdep 300.0 8.06199211612242 0.005309213 0.70439070204273 3.4072 7.6662 2.72576 6.3885 1.3 0.0 0.8 0.9 0.0 0.95 0.9 0.0 0.95 2.0 0.65 2.0 0.65
    pair_coeff * * oxdna2/hbond   seqdep 0.0 0.93918760272364 3.4072 6.3885 2.89612 5.9626 1.5 0.0 0.7 1.5 0.0 0.7 1.5 0.0 0.7 0.46 3.141592654 0.7 4.0 1.570796327 0.45 4.0 1.570796327 0.45
    pair_coeff 1 4 oxdna2/hbond   seqdep 6.36589157849259 0.93918760272364 3.4072 6.3885 2.89612 5.9626 1.5 0.0 0.7 1.5 0.0 0.7 1.5 0.0 0.7 0.46 3.141592654 0.7 4.0 1.570796327 0.45 4.0 1.570796327 0.45
    pair_coeff 2 3 oxdna2/hbond   seqdep 6.36589157849259 0.93918760272364 3.4072 6.3885 2.89612 5.9626 1.5 0.0 0.7 1.5 0.0 0.7 1.5 0.0 0.7 0.46 3.141592654 0.7 4.0 1.570796327 0.45 4.0 1.570796327 0.45
    pair_coeff * * oxdna2/xstk    3.9029021145006 4.89785 5.74965 4.21641 5.57929 2.25 0.791592654 0.58 1.7 1.0 0.68 1.7 1.0 0.68 1.5 0.0 0.65 1.7 0.875 0.68 1.7 0.875 0.68
    pair_coeff * * oxdna2/coaxstk 4.80673207785863 3.4072 5.1108 1.87396 4.94044 2.0 2.891592653589793 0.65 1.3 0.0 0.8 0.9 0.0 0.95 0.9 0.0 0.95 40.0 3.116592653589793
    pair_coeff * * oxdna2/dh      300.0 0.5 0.815

    pair_style hybrid/overlay oxdna2/excv oxdna2/stk oxdna2/hbond oxdna2/xstk oxdna2/coaxstk oxdna2/dh
    pair_coeff * * oxdna2/excv    oxdna2_real.cgdna
    pair_coeff * * oxdna2/stk     seqdep 300.0 8.06199211612242 0.005309213 oxdna2_real.cgdna
    pair_coeff * * oxdna2/hbond   seqdep oxdna2_real.cgdna
    pair_coeff 1 4 oxdna2/hbond   seqdep oxdna2_real.cgdna
    pair_coeff 2 3 oxdna2/hbond   seqdep oxdna2_real.cgdna
    pair_coeff * * oxdna2/xstk    oxdna2_real.cgdna
    pair_coeff * * oxdna2/coaxstk oxdna2_real.cgdna
    pair_coeff * * oxdna2/dh      300.0 0.5 oxdna2_real.cgdna
:::
::::

::: {.admonition .note}
Note

The coefficients in the above examples are provided in forms compatible with both *units lj* and *units real* (see documentation of [[units]{.doc}]units.md){.reference .internal}). These can also be read from a potential file with correct unit style by specifying the name of the file. Several potential files for each unit style are included in the [`potentials`{.docutils .literal .notranslate}]{.pre} directory of the LAMMPS distribution.
:::
::::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *oxdna2* pair styles compute the pairwise-additive parts of the oxDNA force field for coarse-grained modelling of DNA. The effective interaction between the nucleotides consists of potentials for the excluded volume interaction *oxdna2/excv*, the stacking *oxdna2/stk*, cross-stacking *oxdna2/xstk* and coaxial stacking interaction *oxdna2/coaxstk*, electrostatic Debye-Hueckel interaction *oxdna2/dh* as well as the hydrogen-bonding interaction *oxdna2/hbond* between complementary pairs of nucleotides on opposite strands. Average sequence or sequence-dependent stacking and base-pairing strengths are supported [[(Sulc)]{.std .std-ref}](#sulc2){.reference .internal}. Quasi-unique base-pairing between nucleotides can be achieved by using more complementary pairs of atom types like 5-8 and 6-7, 9-12 and 10-11, 13-16 and 14-15, etc. This prevents the hybridization of in principle complementary bases within Ntypes/4 bases up and down along the backbone.

The exact functional form of the pair styles is rather complex. The individual potentials consist of products of modulation factors, which themselves are constructed from a number of more basic potentials (Morse, Lennard-Jones, harmonic angle and distance) as well as quadratic smoothing and modulation terms. We refer to [[(Snodin)]{.std .std-ref}](#snodin2){.reference .internal} and the original oxDNA publications [[(Ouldridge-DPhil)]{.std .std-ref}](#ouldridge-dphil2){.reference .internal} and [[(Ouldridge)]{.std .std-ref}](#ouldridge2){.reference .internal} for a detailed description of the oxDNA2 force field.

::: {.admonition .note}
Note

These pair styles have to be used together with the related oxDNA2 bond style *oxdna2/fene* for the connectivity of the phosphate backbone (see also documentation of [[bond_style oxdna2/fene]{.doc}]bond_oxdna.md){.reference .internal}). Most of the coefficients in the above example have to be kept fixed and cannot be changed without reparameterizing the entire model. Exceptions are the first four coefficients after *oxdna2/stk* (seq=seqdep, T=0.1, xi=1.3523 and kappa=2.6717 and corresponding *real unit* equivalents in the above examples). the first coefficient after *oxdna2/hbond* (seq=seqdep in the above example) and the three coefficients after *oxdna2/dh* (T=0.1, rhos=0.5, qeff=0.815 in the above example). When using a Langevin thermostat e.g. through [[fix langevin]{.doc}]fix_langevin.md){.reference .internal} or [[fix nve/dotc/langevin]{.doc}]fix_nve_dotc_langevin.md){.reference .internal} the temperature coefficients have to be matched to the one used in the fix.
:::

::: {.admonition .note}
Note

These pair styles have to be used with the *atom_style hybrid bond ellipsoid oxdna* (see documentation of [[atom_style]{.doc}]atom_style.md){.reference .internal}). The *atom_style oxdna* stores the 3'-to-5' polarity of the nucleotide strand, which is set through the bond topology in the data file. The first (second) atom in a bond definition is understood to point towards the 3'-end (5'-end) of the strand.
:::

Example input and data files for DNA duplexes can be found in [`examples/PACKAGES/cgdna/examples/oxDNA/`{.docutils .literal .notranslate}]{.pre} and [`.../oxDNA2/`{.docutils .literal .notranslate}]{.pre}. A simple python setup tool which creates single straight or helical DNA strands, DNA duplexes or arrays of DNA duplexes can be found in [`examples/PACKAGES/cgdna/util/`{.docutils .literal .notranslate}]{.pre}.

Please cite [[(Henrich)]{.std .std-ref}](#henrich2){.reference .internal} in any publication that uses this implementation. An updated documentation that contains general information on the model, its implementation and performance as well as the structure of the data and input file can be found [here](PDF/CG-DNA.pdf){.reference .external}.

Please cite also the relevant oxDNA2 publications [[(Snodin)]{.std .std-ref}](#snodin2){.reference .internal} and [[(Sulc)]{.std .std-ref}](#sulc2){.reference .internal}.
:::::

------------------------------------------------------------------------

::::::::: {#potential-file-reading .section}
## Potential file reading[](#potential-file-reading "Link to this heading"){.headerlink}

For each pair style above the first non-modifiable argument can be a filename (with exception of Debye-Hueckel, for which the effective charge argument can be a filename), and if it is, no further arguments should be supplied. Therefore the following command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff 1 4 oxdna2/hbond   seqdep oxdna_real.cgdna
:::
::::

will be interpreted as a request to read the corresponding hydrogen bonding potential parameters from the file with the given name. The file can define multiple potential parameters for both bonded and pair interactions, but for the example pair interaction above there must exist in the file a line of the form:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    1 4 hbond     <coefficients>
:::
::::

If potential customization is required, the potential file reading can be mixed with the manual specification of the potential parameters. For example, the following command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay oxdna2/excv oxdna2/stk oxdna2/hbond oxdna2/xstk oxdna2/coaxstk oxdna2/dh
    pair_coeff * * oxdna2/excv    2.0 0.7 0.675 2.0 0.515 0.5 2.0 0.33 0.32
    pair_coeff * * oxdna2/stk     seqdep 0.1 1.3523 2.6717 oxdna2_lj.cgdna
    pair_coeff * * oxdna2/hbond   seqdep oxdna2_lj.cgdna
    pair_coeff 1 4 oxdna2/hbond   seqdep oxdna2_lj.cgdna
    pair_coeff 2 3 oxdna2/hbond   seqdep oxdna2_lj.cgdna
    pair_coeff * * oxdna2/xstk    oxdna2_lj.cgdna
    pair_coeff * * oxdna2/coaxstk oxdna2_lj.cgdna
    pair_coeff * * oxdna2/dh      0.1 0.5 0.815
:::
::::

will read the excluded volume and Debye-Hueckel effective charge *qeff* parameters from the manual specification and all others from the potential file *oxdna2_lj.cgdna*.

There are sample potential files for each unit style in the [`potentials`{.docutils .literal .notranslate}]{.pre} directory of the LAMMPS distribution. The potential file unit system must align with the units defined via the [[units]{.doc}]units.md){.reference .internal} command. For conversion between different *LJ* and *real* unit systems for oxDNA, the python tool *lj2real.py* located in the [`examples/PACKAGES/cgdna/util/`{.docutils .literal .notranslate}]{.pre} directory can be used. This tool assumes similar file structure to the examples found in [`examples/PACKAGES/cgdna/examples/`{.docutils .literal .notranslate}]{.pre}.
:::::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles can only be used if LAMMPS was built with the CG-DNA package and the MOLECULE and ASPHERE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_style oxdna2/fene]{.doc}]bond_oxdna.md){.reference .internal}, [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[bond_style oxdna/fene]{.doc}]bond_oxdna.md){.reference .internal}, [[pair_style oxdna/excv]{.doc}]pair_oxdna.md){.reference .internal}, [[bond_style oxrna2/fene]{.doc}]bond_oxdna.md){.reference .internal}, [[pair_style oxrna2/excv]{.doc}]pair_oxrna2.md){.reference .internal}, [[atom_style oxdna]{.doc}]atom_style.md){.reference .internal}, [[fix nve/dotc/langevin]{.doc}]fix_nve_dotc_langevin.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Henrich)** O. Henrich, Y. A. Gutierrez-Fosado, T. Curk, T. E. Ouldridge, Eur. Phys. J. E 41, 57 (2018).

**(Snodin)** B.E. Snodin, F. Randisi, M. Mosayebi, et al., J. Chem. Phys. 142, 234901 (2015).

**(Sulc)** P. Sulc, F. Romano, T.E. Ouldridge, L. Rovigatti, J.P.K. Doye, A.A. Louis, J. Chem. Phys. 137, 135101 (2012).

**(Ouldridge-DPhil)** T.E. Ouldridge, Coarse-grained modelling of DNA and DNA self-assembly, DPhil. University of Oxford (2011).

**(Ouldridge)** T.E. Ouldridge, A.A. Louis, J.P.K. Doye, J. Chem. Phys. 134, 085101 (2011).
:::
:::::::::::::::::::::::
:::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::

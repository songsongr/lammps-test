::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#bond-style-oxdna-fene-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# bond_style oxdna/fene command[](#bond-style-oxdna-fene-command "Link to this heading"){.headerlink}
:::

::: {#bond-style-oxdna2-fene-command .section}
# bond_style oxdna2/fene command[](#bond-style-oxdna2-fene-command "Link to this heading"){.headerlink}
:::

::::::::::::::::::::::: {#bond-style-oxrna2-fene-command .section}
# bond_style oxrna2/fene command[](#bond-style-oxrna2-fene-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style oxdna/fene

    bond_style oxdna2/fene

    bond_style oxrna2/fene
:::
::::
:::::

:::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # LJ units
    bond_style oxdna/fene
    bond_coeff * 2.0 0.25 0.7525

    bond_style oxdna2/fene
    bond_coeff * 2.0 0.25 0.7564

    bond_style oxrna2/fene
    bond_coeff * 2.0 0.25 0.76107

    bond_style oxdna/fene
    bond_coeff * oxdna_lj.cgdna

    # Real units
    bond_style oxdna/fene
    bond_coeff * 11.92337812042065 2.1295 6.409795

    bond_style oxdna2/fene
    bond_coeff * 11.92337812042065 2.1295 6.4430152

    bond_style oxrna2/fene
    bond_coeff * 11.92337812042065 2.1295 6.482800913

    bond_style oxrna2/fene
    bond_coeff * oxrna2_real.cgdna
:::
::::

::: {.admonition .note}
Note

The coefficients in the above examples have to be kept fixed and cannot be changed without reparameterizing the entire model. They are provided in forms compatible with both *units lj* and *units real* (see documentation of [[units]{.doc}]units.md){.reference .internal}). These can also be read from a potential file with correct unit style by specifying the name of the file. Several potential files for each unit style are included in the [`potentials`{.docutils .literal .notranslate}]{.pre} directory of the LAMMPS distribution.
:::
::::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *oxdna/fene*, *oxdna2/fene*, and *oxrna2/fene* bond styles use the potential

::: {.math .notranslate .nohighlight}
\\\[E = - \\frac{\\epsilon}{2} \\ln \\left\[ 1 - \\left(\\frac{r-r_0}{\\Delta}\\right)\^2\\right\]\\\]
:::

to define a modified finite extensible nonlinear elastic (FENE) potential [[(Ouldridge)]{.std .std-ref}](#ouldridge0){.reference .internal} to model the connectivity of the phosphate backbone in the oxDNA/oxRNA force field for coarse-grained modelling of DNA/RNA.

The following coefficients must be defined for the bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as given in the above example, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\Delta\\)]{.math .notranslate .nohighlight} (distance)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)

::: {.admonition .note}
Note

The oxDNA bond style has to be used together with the corresponding oxDNA pair styles for excluded volume interaction *oxdna/excv* , stacking *oxdna/stk* , cross-stacking *oxdna/xstk* and coaxial stacking interaction *oxdna/coaxstk* as well as hydrogen-bonding interaction *oxdna/hbond* (see also documentation of [[pair_style oxdna/excv]{.doc}]pair_oxdna.md){.reference .internal}). For the oxDNA2 [[(Snodin)]{.std .std-ref}](#snodin0){.reference .internal} bond style the analogous pair styles *oxdna2/excv* , *oxdna2/stk* , *oxdna2/xstk* , *oxdna2/coaxstk* , *oxdna2/hbond* and an additional Debye-Hueckel pair style *oxdna2/dh* have to be defined. The same applies to the oxRNA2 [[(Sulc1)]{.std .std-ref}](#sulc01){.reference .internal} styles.
:::

::: {.admonition .note}
Note

This bond style has to be used with the *atom_style hybrid bond ellipsoid oxdna* (see documentation of [[atom_style]{.doc}]atom_style.md){.reference .internal}). The *atom_style oxdna* stores the 3'-to-5' polarity of the nucleotide strand, which is set through the bond topology in the data file. The first (second) atom in a bond definition is understood to point towards the 3'-end (5'-end) of the strand.
:::

::: {.admonition .warning}
Warning

If data files are produced with [[write_data]{.doc}]write_data.md){.reference .internal}, then the [[newton]{.doc}]newton.md){.reference .internal} command should be set to *newton on* or *newton off on*. Otherwise the data files will not have the same 3'-to-5' polarity as the initial data file. This limitation does not apply to binary restart files produced with [[write_restart]{.doc}]write_restart.md){.reference .internal}.
:::

Example input and data files for DNA and RNA duplexes can be found in [`` examples/PACKAGES/cgdna/examples/oxDNA/`, ``{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`` `.../oxDNA2/ ``{.docutils .literal .notranslate}]{.pre} and [`.../oxRNA2/`{.docutils .literal .notranslate}]{.pre}. A simple python setup tool which creates single straight or helical DNA strands, DNA/RNA duplexes or arrays of DNA/RNA duplexes can be found in [`examples/PACKAGES/cgdna/util/`{.docutils .literal .notranslate}]{.pre}.

Please cite [[(Henrich)]{.std .std-ref}](#henrich0){.reference .internal} in any publication that uses this implementation. An updated documentation that contains general information on the model, its implementation and performance as well as the structure of the data and input file can be found [here](PDF/CG-DNA.pdf){.reference .external}.

Please cite also the relevant oxDNA/oxRNA publications. These are [[(Ouldridge)]{.std .std-ref}](#ouldridge0){.reference .internal} and [[(Ouldridge-DPhil)]{.std .std-ref}](#ouldridge-dphil0){.reference .internal} for oxDNA, [[(Snodin)]{.std .std-ref}](#snodin0){.reference .internal} for oxDNA2, [[(Sulc1)]{.std .std-ref}](#sulc01){.reference .internal} for oxRNA2 and for sequence-specific hydrogen-bonding and stacking interactions [[(Sulc2)]{.std .std-ref}](#sulc02){.reference .internal}.
:::::::

------------------------------------------------------------------------

::::::: {#potential-file-reading .section}
## Potential file reading[](#potential-file-reading "Link to this heading"){.headerlink}

For each style oxdna, oxdna2 and oxrna2, the first parameter argument can be a filename, and if it is, no further arguments should be supplied. Therefore the following command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style oxdna/fene
    bond_coeff * oxdna_lj.cgdna
:::
::::

will be interpreted as a request to read the (FENE) potential [[(Ouldridge)]{.std .std-ref}](#ouldridge0){.reference .internal} parameters from the file with the given name. The file can define multiple potential parameters for both bonded and pair interactions, but for the above bonded interactions there must exist in the file a line of the form:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    *   fene    epsilon delta r0
:::
::::

There are sample potential files for each unit style in the [`potentials`{.docutils .literal .notranslate}]{.pre} directory of the LAMMPS distribution. The potential file unit system must align with the units defined via the [[units]{.doc}]units.md){.reference .internal} command. For conversion between different *LJ* and *real* unit systems for oxDNA, the python tool *lj2real.py* located in the [`examples/PACKAGES/cgdna/util/`{.docutils .literal .notranslate}]{.pre} directory can be used. This tool assumes similar file structure to the examples found in [`examples/PACKAGES/cgdna/examples/`{.docutils .literal .notranslate}]{.pre}.
:::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the CG-DNA package and the MOLECULE and ASPHERE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style oxdna/excv]{.doc}]pair_oxdna.md){.reference .internal}, [[pair_style oxdna2/excv]{.doc}]pair_oxdna2.md){.reference .internal}, [[pair_style oxrna2/excv]{.doc}]pair_oxrna2.md){.reference .internal}, [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[atom_style oxdna]{.doc}]atom_style.md){.reference .internal}, [[fix nve/dotc/langevin]{.doc}]fix_nve_dotc_langevin.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Henrich)** O. Henrich, Y. A. Gutierrez-Fosado, T. Curk, T. E. Ouldridge, Eur. Phys. J. E 41, 57 (2018).

**(Ouldridge-DPhil)** T.E. Ouldridge, Coarse-grained modelling of DNA and DNA self-assembly, DPhil. University of Oxford (2011).

**(Ouldridge)** T.E. Ouldridge, A.A. Louis, J.P.K. Doye, J. Chem. Phys. 134, 085101 (2011).

**(Snodin)** B.E. Snodin, F. Randisi, M. Mosayebi, et al., J. Chem. Phys. 142, 234901 (2015).

**(Sulc1)** P. Sulc, F. Romano, T. E. Ouldridge, et al., J. Chem. Phys. 140, 235102 (2014).

**(Sulc2)** P. Sulc, F. Romano, T.E. Ouldridge, L. Rovigatti, J.P.K. Doye, A.A. Louis, J. Chem. Phys. 137, 135101 (2012).
:::
:::::::::::::::::::::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::

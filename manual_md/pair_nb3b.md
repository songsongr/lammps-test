:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-nb3b-harmonic-command .section}
[]{#index-1}[]{#index-0}

# pair_style nb3b/harmonic command[](#pair-style-nb3b-harmonic-command "Link to this heading"){.headerlink}
:::

::::::::::::::::::: {#pair-style-nb3b-screened-command .section}
# pair_style nb3b/screened command[](#pair-style-nb3b-screened-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style
:::
::::

- style = *nb3b/harmonic* or *nb3b/screened*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style nb3b/harmonic
    pair_coeff * * MgOH.nb3bharmonic Mg O H

    pair_style nb3b/screened
    pair_coeff * * PO.nb3b.screened P NULL O
    pair_coeff * * SiOH.nb3b.screened Si O H
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The pair style *nb3b/harmonic* computes a non-bonded 3-body harmonic potential for the energy E of a system of atoms as

::: {.math .notranslate .nohighlight}
\\\[E = K (\\theta - \\theta_0)\^2\\\]
:::

where [\\(\\theta_0\\)]{.math .notranslate .nohighlight} is the equilibrium value of the angle and *K* is a prefactor. Note that the usual 1/2 factor is included in *K*. The form of the potential is identical to that used in angle_style *harmonic*, but in this case, the atoms do not need to be explicitly bonded.

Style *nb3b/screened* adds an additional exponentially decaying factor to the harmonic term, given by

::: {.math .notranslate .nohighlight}
\\\[E = K (\\theta - \\theta_0)\^2 \\exp \\left(- \\frac{r\_{ij}}{\\rho\_{ij}} - \\frac{r\_{ik}}{\\rho\_{ik}} \\right)\\\]
:::

where [\\(\\rho_ij\\)]{.math .notranslate .nohighlight} and [\\(\\rho_ik\\)]{.math .notranslate .nohighlight} are the screening factors along the two bonds. Note that the usual 1/2 factor is included in *K*.

Only a single pair_coeff command is used with these styles which specifies a potential file with parameters for specified elements. These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- N element names = mapping of elements to atom types

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for the potential file.

As an example, imagine a file SiC.nb3b.harmonic has potential values for Si and C. If your LAMMPS simulation has 4 atoms types and you want the first 3 to be Si, and the fourth to be C, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * SiC.nb3b.harmonic Si Si Si C
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The first three Si arguments map LAMMPS atom types 1,2,3 to the Si element in the potential file. The final C argument maps LAMMPS atom type 4 to the C element in the potential file. If a mapping value is specified as NULL, the mapping is not performed. This can be used when the potential is used as part of the *hybrid* pair style. The NULL values are placeholders for atom types that will be used with other potentials. Two examples of pair_coeff command for use with the *hybrid* pair style are:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * nb3b/harmonic MgOH.nb3b.harmonic Mg O H
:::
::::

Three-body non-bonded harmonic files in the *potentials* directory of the LAMMPS distribution have a ".nb3b.harmonic" suffix. Lines that are not blank or comments (starting with #) define parameters for a triplet of elements.

Each entry has six arguments. The first three are atom types as referenced in the LAMMPS input file. The first argument specifies the central atom. The fourth argument indicates the *K* parameter. The fifth argument indicates [\\(\\theta_0\\)]{.math .notranslate .nohighlight}. The sixth argument indicates a separation cutoff in Angstroms.

For a given entry, if the second and third arguments are identical, then the entry is for a cutoff for the distance between types 1 and 2 (values for *K* and [\\(\\theta_0\\)]{.math .notranslate .nohighlight} are irrelevant in this case).

For a given entry, if the first three arguments are all different, then the entry is for the *K* and [\\(\\theta_0\\)]{.math .notranslate .nohighlight} parameters (the cutoff in this case is irrelevant).

It is required that the potential file contains entries for *all* permutations of the elements listed in the pair_coeff command. If certain combinations are not parameterized the corresponding parameters should be set to zero. The potential file can also contain entries for additional elements which are not used in a particular simulation; LAMMPS ignores those entries.
:::::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style can only be used if LAMMPS was built with the MANYBODY package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

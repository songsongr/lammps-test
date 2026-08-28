:::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::: {#pair-style-hdnnp-command .section}
[]{#index-0}

# pair_style hdnnp command[](#pair-style-hdnnp-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hdnnp cutoff keyword value ...
:::
::::

- cutoff = short-range cutoff of HDNNP (maximum symmetry function cutoff radius)

- zero or more keyword/value pairs may be appended

- keyword = *dir* or *showew* or *showewsum* or *maxew* or *resetew* or *cflength* or *cfenergy*

- value depends on the preceding keyword:

``` literal-block
dir value = directory
    directory = Path to HDNNP configuration files
showew value = yes or no
showewsum value = summary
          summary = Write EW summary every this many timesteps (0 turns summary off)
maxew value = threshold
      threshold = Maximum number of EWs allowed
resetew value = yes or no
cflength value = length
         length = Length unit conversion factor
cfenergy value = energy
         energy = Energy unit conversion factor
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hdnnp 6.35 showew yes showewsum 100 maxew 1000 resetew yes cflength 1.8897261328 cfenergy 0.0367493254
    pair_coeff * * H O

    pair_style hdnnp 6.01 dir "./" showewsum 10000
    pair_coeff * * S Cu NULL Cu
:::
::::
:::::

::::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This pair style adds an interaction based on the high-dimensional neural network potential (HDNNP) method as presented in [[(Behler and Parrinello 2007)]{.std .std-ref}](#behler-parrinello-2007){.reference .internal}. HDNNPs are machine learning potentials which require careful training of neural networks prior to application in MD simulations. The pair style uses an interface to the *n2p2* library [[(Singraber, Behler and Dellago 2019)]{.std .std-ref}](#singraber-behler-dellago-2019){.reference .internal} which is available on Github [here](https://github.com/CompPhysVienna/n2p2){.reference .external}. Please see the *n2p2* [documentation](https://compphysvienna.github.io/n2p2/){.reference .external} for further details. *n2p2* (and hence this pair style) is compatible with neural network potentials trained with its own tools [[(Singraber et al 2019)]{.std .std-ref}](#singraber-et-al-2019){.reference .internal} and with [RuNNer](https://www.uni-goettingen.de/de/560580.html){.reference .external}.

Only a single *pair_coeff* command with two asterisk wild-cards is used with this pair style. Its additional arguments define the mapping of LAMMPS atom types to n2p2 elements.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * H O
:::
::::

In the above example LAMMPS types 1 and 2 are mapped to the elements "H" and "O" in n2p2, respectively. Multiple types may map to the same element, or some types may not be mapped at all. For example, if the LAMMPS simulation has four atom types, the command

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * H H O NULL
:::
::::

maps atom types 1 and 2 to the element "H", type 3 to "O" and type 4 is not mapped (indicated by NULL). Atoms mapped to NULL are ignored by the HDNNP calculation, i.e. they do not contribute in any way to the evaluation of HDNNP energies and forces. This may be useful in a setup with [[hybrid pair styles]{.doc}]pair_hybrid.md){.reference .internal}.

------------------------------------------------------------------------

The mandatory pair style argument *cutoff* must match the short-range cutoff radius of the HDNNP. This corresponds to the maximum cutoff radius of all symmetry functions (the atomic environment descriptors of HDNNPs) used.

::: {.admonition .note}
Note

The cutoff must be given in LAMMPS length units, even if the neural network potential has been trained using a different unit system (see remarks about the *cflength* and *cfenergy* keywords below for details).
:::

The numeric value may be slightly larger than the actual maximum symmetry function cutoff radius (to account for rounding errors when converting units), but must not be smaller.

Use the *dir* keyword to specify the directory containing the HDNNP configuration files. The directory must contain [`input.nn`{.docutils .literal .notranslate}]{.pre} with neural network and symmetry function setup, [`scaling.data`{.docutils .literal .notranslate}]{.pre} with symmetry function scaling data and [`weights.???.data`{.docutils .literal .notranslate}]{.pre} with weight parameters for each element.

The keyword *showew* can be used to turn on/off the display of extrapolation warnings (EWs) which are issued whenever a symmetry function value is out of bounds defined by minimum/maximum values in [`scaling.data`{.docutils .literal .notranslate}]{.pre}. An extrapolation warning may look like this:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    ### NNP EXTRAPOLATION WARNING ### STRUCTURE:      0 ATOM:       119 ELEMENT: Cu SYMFUNC:   32 TYPE:  3 VALUE:  2.166E-02 MIN:  2.003E-05 MAX:  1.756E-02
:::
::::

stating that the value 2.166E-02 of symmetry function 32 of type 3 (Narrow Angular symmetry function), element Cu (see the log file for a symmetry function listing) was out of bounds (maximum in [`scaling.data`{.docutils .literal .notranslate}]{.pre} is 1.756E-02) for atom 119. Here, the atom index refers to the LAMMPS tag (global index) and the structure index is used to print out the MPI rank the atom belongs to.

::: {.admonition .note}
Note

The *showew* keyword should only be set to *yes* for debugging purposes. Extrapolation warnings may add lots of overhead as they are communicated each timestep. Also, if the simulation is run in a region where the HDNNP was not correctly trained, lots of extrapolation warnings may clog log files and the console. In a production run use *showewsum* instead.
:::

The keyword *showewsum* can be used to get an overview of extrapolation warnings occurring during an MD simulation. The argument specifies the interval at which extrapolation warning summaries are displayed and logged. An EW summary may look like this:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    ### NNP EW SUMMARY ### TS:        100 EW         11 EWPERSTEP  1.100E-01
:::
::::

Here, at timestep 100 the occurrence of 11 extrapolation warnings since the last summary is reported, which corresponds to an EW rate of 0.11 per timestep. Setting *showewsum* to 0 deactivates the EW summaries.

A maximum number of allowed extrapolation warnings can be specified with the *maxew* keyword. If the number of EWs exceeds the *maxew* argument the simulation is stopped. Note however that this is merely an approximate threshold since the check is only performed at the end of each timestep and each MPI process counts individually to minimize communication overhead.

The keyword *resetew* alters the behavior of the above mentioned *maxew* threshold. If *resetew* is set to *yes* the threshold is applied on a per-timestep basis and the internal EW counters are reset at the beginning of each timestep. With *resetew* set to *no* the counters accumulate EWs along the whole trajectory.

If the training of a neural network potential has been performed with different physical units for length and energy than those set in LAMMPS, it is still possible to use the potential when the unit conversion factors are provided via the *cflength* and *cfenergy* keywords. If for example, the HDNNP was parameterized with Bohr and Hartree training data and symmetry function parameters (i.e. distances and energies in "input.nn" are given in Bohr and Hartree) but LAMMPS is set to use *metal* units (Angstrom and eV) the correct conversion factors are:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    cflength 1.8897261328

    cfenergy 0.0367493254
:::
::::

Thus, arguments of *cflength* and *cfenergy* are the multiplicative factors required to convert lengths and energies given in LAMMPS units to respective quantities in native HDNNP units (1 Angstrom = 1.8897261328 Bohr, 1 eV = 0.0367493254 Hartree).
:::::::::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This style does not support mixing. The [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command should only be invoked with asterisk wild cards (see above).

This style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This style does not write information to [[binary restart files]{.doc}]restart.md){.reference .internal}. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

::::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the ML-HDNNP package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

Please report bugs and feature requests to the [n2p2 GitHub issue page](https://github.com/CompPhysVienna/n2p2/issues){.reference .external}.

::: {#related-commands .section}
### Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair_hybrid]{.doc}]pair_hybrid.md){.reference .internal}, [[units]{.doc}]units.md){.reference .internal}
:::

::: {#default .section}
### Default[](#default "Link to this heading"){.headerlink}

The default options are *dir* = "hdnnp/", *showew* = yes, *showewsum* = 0, *maxew* = 0, *resetew* = no, *cflength* = 1.0, *cfenergy* = 1.0.

------------------------------------------------------------------------

**(Behler and Parrinello 2007)** Behler, J.; Parrinello, M. Phys. Rev. Lett. 2007, 98 (14), 146401.

**(Singraber, Behler and Dellago 2019)** Singraber, A.; Behler, J.; Dellago, C. J., Chem. Theory Comput. 2019, 15 (3), 1827-1840

**(Singraber et al 2019)** Singraber, A.; Morawietz, T.; Behler, J.; Dellago, C., J. Chem. Theory Comput. 2019, 15 (5), 3075-3092.
:::
:::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::

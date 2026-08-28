:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-srp-command .section}
[]{#index-1}[]{#index-0}

# pair_style srp command[](#pair-style-srp-command "Link to this heading"){.headerlink}
:::

::::::::::::::::::: {#pair-style-srp-react-command .section}
# pair_style srp/react command[](#pair-style-srp-react-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style srp cutoff btype dist keyword value ...
    pair_style srp/react cutoff btype dist react-id keyword value ...
:::
::::

- cutoff = global cutoff for SRP interactions (distance units)

- btype = bond type (numeric, type label, or wildcard) to apply SRP interactions to

- distance = *min* or *mid*

- react-id = id of either fix bond/break or fix bond/create

- zero or more keyword/value pairs may be appended

- keyword = *exclude*

  ``` literal-block
  bptype value = atom type (numeric or type label) for bond particles
  exclude value = yes or no
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid dpd 1.0 1.0 12345 srp 0.8 1 mid exclude yes
    pair_coeff 1 1 dpd 60.0 4.5 1.0
    pair_coeff 1 2 none
    pair_coeff 2 2 srp 100.0 0.8

    pair_style hybrid dpd 1.0 1.0 12345 srp 0.8 * min exclude yes
    pair_coeff 1 1 dpd 60.0 50 1.0
    pair_coeff 1 2 none
    pair_coeff 2 2 srp 40.0

    fix        create all bond/create   100  1  2  1.0 1 prob  0.2  19852
    pair_style hybrid dpd 1.0 1.0 12345 srp/react 0.8 * min create exclude yes
    pair_coeff 1 1 dpd 60.0 50 1.0
    pair_coeff 1 2 none
    pair_coeff 2 2 srp/react 40.0

    pair_style hybrid srp 0.8 2 mid
    pair_coeff 1 1 none
    pair_coeff 1 2 none
    pair_coeff 2 2 srp 100.0 0.8

    labelmap bond 1 C-C
    pair_style hybrid srp 0.8 C-C mid
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Style *srp* computes a soft segmental repulsive potential (SRP) that acts between pairs of bonds. This potential is useful for preventing bonds from passing through one another when a soft non-bonded potential acts between beads in, for example, DPD polymer chains. An example input script that uses this command is provided in examples/PACKAGES/srp.

Bonds of specified type *btype* interact with one another through a bond-pairwise potential, such that the force on bond *i* due to bond *j* is as follows

::: {.math .notranslate .nohighlight}
\\\[F\^{\\mathrm{SRP}}\_{ij} = C(1-r/r_c)\\hat{r}\_{ij} \\qquad r \< r_c\\\]
:::

where *r* and [\\(\\hat{r}\_{ij}\\)]{.math .notranslate .nohighlight} are the distance and unit vector between the two bonds. Note that *btype* can be specified as an asterisk "\*", which case the interaction is applied to all bond types. The *mid* option computes *r* and [\\(\\hat{r}\_{ij}\\)]{.math .notranslate .nohighlight} from the midpoint distance between bonds. The *min* option computes *r* and [\\(\\hat{r}\_{ij}\\)]{.math .notranslate .nohighlight} from the minimum distance between bonds. The force acting on a bond is mapped onto the two bond atoms according to the lever rule,

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}F\_{i1}\^{\\mathrm{SRP}} & = F\^{\\mathrm{SRP}}\_{ij}(L) \\\\ F\_{i2}\^{\\mathrm{SRP}} & = F\^{\\mathrm{SRP}}\_{ij}(1-L)\\end{split}\\\]
:::

where *L* is the normalized distance from the atom to the point of closest approach of bond *i* and *j*. The *mid* option takes *L* as 0.5 for each interaction as described in [[(Sirk)]{.std .std-ref}](#sirk2){.reference .internal}.

The following coefficients must be defined via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart file read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- *C* (force units)

- [\\(r_c\\)]{.math .notranslate .nohighlight} (distance units)

The last coefficient is optional. If not specified, the global cutoff is used.

::: {.admonition .note}
Note

Pair style srp considers each bond of type *btype* to be a fictitious "particle" of type *bptype*, where *bptype* is either the largest atom type in the system, or the type set by the *bptype* flag. Any actual existing particles with this atom type will be deleted at the beginning of a run. This means you must specify the number of types in your system accordingly; usually to be one larger than what would normally be the case, e.g. via the [[create_box]{.doc}]create_box.md){.reference .internal} or by changing the header in your [[data file]{.doc}]read_data.md){.reference .internal}. The fictitious "bond particles" are inserted at the beginning of the run, and serve as placeholders that define the position of the bonds. This allows neighbor lists to be constructed and pairwise interactions to be computed in almost the same way as is done for actual particles. Because bonds interact only with other bonds, [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal} should be used to turn off interactions between atom type *bptype* and all other types of atoms. An error will be flagged if [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal} is not used.
:::

::: {.admonition .note}
Note

If using type labels, the type labels must be defined before calling the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command.
:::

The optional *exclude* keyword determines if forces are computed between first neighbor (directly connected) bonds. For a setting of *no*, first neighbor forces are computed; for *yes* they are not computed. A setting of *no* cannot be used with the *min* option for distance calculation because the minimum distance between directly connected bonds is zero.

Pair style *srp* turns off normalization of thermodynamic properties by particle number, as if the command [[thermo_modify norm no]{.doc}]thermo_modify.md){.reference .internal} had been issued.

The pairwise energy associated with style *srp* is shifted to be zero at the cutoff distance [\\(r_c\\)]{.math .notranslate .nohighlight}.

------------------------------------------------------------------------

::: versionadded
[Added in version 3Aug2022.]{.versionmodified .added}
:::

Pair style *srp/react* interfaces the pair style *srp* with the bond breaking and formation mechanisms provided by fix *bond/break* and fix *bond/create*, respectively. When using this pair style, whenever a bond breaking (or formation) reaction occurs, the corresponding fictitious particle is deleted (or inserted) during the same simulation time step as the reaction. This is useful in the simulation of reactive systems involving large polymeric molecules [[(Palkar)]{.std .std-ref}](#palkar){.reference .internal} where the segmental repulsive potential is necessary to minimize topological violations, and also needs to be turned on and off according to the progress of the reaction.
::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support mixing.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift option for the energy of the pair interaction. Note that as discussed above, the energy term is already shifted to be 0.0 at the cutoff distance [\\(r_c\\)]{.math .notranslate .nohighlight}.

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} table option is not relevant for this pair style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} tail option for adding long-range tail corrections to energy and pressure.

This pair style writes global and per-atom information to [[binary restart files]{.doc}]restart.md){.reference .internal}. Pair srp should be used with [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal}, thus the pair_coeff commands need to be specified in the input script when reading a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the MISC package. It is only enabled if LAMMPS was built with that package. See the Making LAMMPS section for more info.

This pair style must be used with [[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal}.

This pair style requires the [[newton]{.doc}]newton.md){.reference .internal} command to be *on* for non-bonded interactions.

This pair style is not compatible with [[rigid body integrators]{.doc}]fix_rigid.md){.reference .internal}
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style hybrid]{.doc}]pair_hybrid.md){.reference .internal}, [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[pair dpd]{.doc}]pair_dpd.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The default keyword value is exclude = yes.

------------------------------------------------------------------------

**(Sirk)** Sirk TW, Sliozberg YR, Brennan JK, Lisal M, Andzelm JW, J Chem Phys, 136 (13) 134903, 2012.

**(Palkar)** Palkar V, Kuksenok O, J. Phys. Chem. B, 126 (1), 336-346, 2022
:::
:::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

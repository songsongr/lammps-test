:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#compute-pace-command .section}
[]{#index-0}

# compute pace command[](#compute-pace-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID pace ace_potential_filename ... keyword values ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- pace = style name of this compute command

- ace_potential_filename = file name (in the .yace or .ace format from [[pace pair_style]{.doc}]pair_pace.md){.reference .internal}) including ACE hyper-parameters, bonds, and generalized coupling coefficients

- keyword = *bikflag* or *dgradflag*

  ``` literal-block
  bikflag value = 0 or 1
     0 = descriptors are summed over atoms of each type
     1 = descriptors are listed separately for each atom
  dgradflag value = 0 or 1
     0 = descriptor gradients are summed over atoms of each type
     1 = descriptor gradients are listed separately for each atom pair
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute pace all pace coupling_coefficients.yace
    compute pace all pace coupling_coefficients.yace 0 1
    compute pace all pace coupling_coefficients.yace 1 1
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 7Feb2024.]{.versionmodified .added}
:::

This compute calculates a set of quantities related to the atomic cluster expansion (ACE) descriptors of the atoms in a group. ACE descriptors are highly general atomic descriptors, encoding the radial and angular distribution of neighbor atoms, up to arbitrary bond order (rank). The detailed mathematical definition is given in the paper by [[(Drautz)]{.std .std-ref}](#drautz19){.reference .internal}. These descriptors are used in the [[pace pair_style]{.doc}]pair_pace.md){.reference .internal}. Quantities obtained from compute pace are related to those used in [[pace pair_style]{.doc}]pair_pace.md){.reference .internal} to evaluate atomic energies, forces, and stresses for linear ACE models.

For example, the energy for a linear ACE model is calculated as: [\\(E=\\sum_i\^{N\\\_atoms} \\sum\_{\\boldsymbol{\\nu}} c\_{\\boldsymbol{\\nu}} B\_{i,\\boldsymbol{\\boldsymbol{\\nu}}}\\)]{.math .notranslate .nohighlight}. The ACE descriptors for atom i [\\(B\_{i,\\boldsymbol{\\nu}}\\)]{.math .notranslate .nohighlight}, and [\\(c\_{\\nu}\\)]{.math .notranslate .nohighlight} are linear model parameters. The detailed definition and indexing convention for ACE descriptors is given in [[(Drautz)]{.std .std-ref}](#drautz19){.reference .internal}. In short, body order [\\(N\\)]{.math .notranslate .nohighlight}, angular character, radial character, and chemical elements in the *N-body* descriptor are encoded by [\\(\\nu\\)]{.math .notranslate .nohighlight}. In the [[pace pair_style]{.doc}]pair_pace.md){.reference .internal}, the linear model parameters and the ACE descriptors are combined for efficient evaluation of energies and forces. The details and benefits of this efficient implementation are given in [[(Lysogorskiy)]{.std .std-ref}](#lysogorskiy21){.reference .internal}, but the combined descriptors and linear model parameters for the purposes of compute pace may be expressed in terms of the ACE descriptors mentioned above.

[\\(c\_{\\boldsymbol{\\nu}} B\_{i,\\boldsymbol{\\nu}}= \\sum\_{\\boldsymbol{\\nu}\' \\in \\boldsymbol{\\nu} } \\big\[ c\_{\\boldsymbol{\\nu}} C(\\boldsymbol{\\nu}\') \\big\] A\_{i,\\boldsymbol{\\nu}\'}\\)]{.math .notranslate .nohighlight}

where the bracketed terms on the right-hand side are the combined functions with linear model parameters typically provided in the \<name\>.yace potential file for pace pair_style. When these bracketed terms are multiplied by the products of the atomic base from [[(Drautz)]{.std .std-ref}](#drautz19){.reference .internal}, [\\(A\_{i,\\boldsymbol{\\nu\'}}\\)]{.math .notranslate .nohighlight}, the ACE descriptors are recovered but they are also scaled by linear model parameters. The generalized coupling coefficients, written in short-hand here as [\\(C(\\boldsymbol{\\nu}\')\\)]{.math .notranslate .nohighlight}, are the generalized Clebsch-Gordan or generalized Wigner symbols. It may be desirable to reverse the combination of these descriptors and the linear model parameters so that the ACE descriptors themselves may be used. The ACE descriptors and their gradients are often used when training ACE models, performing custom data analysis, generalizing ACE model forms, and other tasks that involve direct computation of descriptors. The key utility of compute pace is that it can compute the ACE descriptors and gradients so that these tasks can be performed during a LAMMPS simulation or so that LAMMPS can be used as a driver for tasks like ACE model parameterization. To see how this command can be used within a Python workflow to train ACE potentials, see the examples in [FitSNAP](https://github.com/FitSNAP/FitSNAP){.reference .external}. Examples on using outputs from this compute to construct general ACE potential forms are demonstrated in [[(Goff)]{.std .std-ref}](#goff23){.reference .internal}. The various keywords and inputs to compute pace determine what ACE descriptors and related quantities are returned in a compute array.

The coefficient file, \<name\>.yace, ultimately defines the number of ACE descriptors to be computed, their maximum body-order, the degree of angular character they have, the degree of radial character they have, the chemical character (which element-element interactions are encoded by descriptors), and other hyper-parameters defined in [[(Drautz)]{.std .std-ref}](#drautz19){.reference .internal}. These may be modeled after the potential files in [[pace pair_style]{.doc}]pair_pace.md){.reference .internal}, and have the same format. Details on how to generate the coefficient files to train ACE models may be found in [FitSNAP](https://github.com/FitSNAP/FitSNAP){.reference .external}.

The keyword *bikflag* determines whether or not to list the descriptors of each atom separately, or sum them together and list in a single row. If *bikflag* is set to *0* then a single descriptor row is used, which contains the per-atom ACE descriptors [\\(B\_{i,\\boldsymbol{\\nu}}\\)]{.math .notranslate .nohighlight} summed over all atoms *i* to produce [\\(B\_{\\boldsymbol{\\nu}}\\)]{.math .notranslate .nohighlight}. If *bikflag* is set to *1* this is replaced by a separate per-atom ACE descriptor row for each atom. In this case, the entries in the final column for these rows are set to zero.

The keyword *dgradflag* determines whether to sum atom gradients or list them separately. If *dgradflag* is set to 0, the ACE descriptor gradients w.r.t. atom *j* are summed over all atoms *i'* of, which may be useful when training linear ACE models on atomic forces. If *dgradflag* is set to 1, gradients are listed separately for each pair of atoms. Each row corresponds to a single term [\\(\\frac{\\partial {B\_{i,\\boldsymbol{\\nu}}}}{\\partial {r}\^a_j}\\)]{.math .notranslate .nohighlight} where [\\({r}\^a_j\\)]{.math .notranslate .nohighlight} is the *a-th* position coordinate of the atom with global index *j*. This also changes the number of columns to be equal to the number of ACE descriptors, with 3 additional columns representing the indices [\\(i\\)]{.math .notranslate .nohighlight}, [\\(j\\)]{.math .notranslate .nohighlight}, and [\\(a\\)]{.math .notranslate .nohighlight}, as explained more in the Output info section below. The option *dgradflag=1* requires that *bikflag=1*.

::: {.admonition .note}
Note

It is noted here that in contrast to [[pace pair_style]{.doc}]pair_pace.md){.reference .internal}, the *.yace* file for compute pace typically should not contain linear parameters for an ACE potential. If [\\(c\_{\\nu}\\)]{.math .notranslate .nohighlight} are included, the value of the descriptor will not be returned in the compute array, but instead, the energy contribution from that descriptor will be returned. Do not do this unless it is the desired behavior. *In short, you should not plug in a '.yace' for a pace potential into this compute to evaluate descriptors.*
:::

::: {.admonition .note}
Note

*Generalized Clebsch-Gordan or Generalized Wigner symbols (with appropriate factors) must be used to evaluate ACE descriptors with this compute.* There are multiple ways to define the generalized coupling coefficients. Because of this, this compute will not revert your potential file to a coupling coefficient file. Instead this compute allows the user to supply coupling coefficients that follow any convention.
:::

::: {.admonition .note}
Note

Using *dgradflag* = 1 produces a global array with [\\(N + 3N\^2 + 1\\)]{.math .notranslate .nohighlight} rows which becomes expensive for systems with more than 1000 atoms.
:::

::: {.admonition .note}
Note

If you have a bonded system, then the settings of [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command can remove pairwise interactions between atoms in the same bond, angle, or dihedral. This is the default setting for the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command, and means those pairwise interactions do not appear in the neighbor list. Because this fix uses the neighbor list, it also means those pairs will not be included in the calculation. One way to get around this, is to write a dump file, and use the [[rerun]{.doc}]rerun.md){.reference .internal} command to compute the ACE descriptors for snapshots in the dump file. The rerun script can use a [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command that includes all pairs in the neighbor list.
:::
::::::::

------------------------------------------------------------------------

:::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

Compute *pace* evaluates a global array. The columns are arranged into *ntypes* blocks, listed in order of atom type *I*. Each block contains one column for each ACE descriptor, the same as for compute *sna/atom*in [[compute snap]{.doc}]compute_sna_atom.md){.reference .internal}. A final column contains the corresponding energy, force component on an atom, or virial stress component. The rows of the array appear in the following order:

- 1 row: *pace* average descriptor values for all atoms of type *I*

- 3\**n* force rows: quantities, with derivatives w.r.t. x, y, and z coordinate of atom *i* appearing in consecutive rows. The atoms are sorted based on atom ID and run up to the total number of atoms, *n*.

- 6 rows: *virial* quantities summed for all atoms of type *I*

For example, if [\\(\\# \\; B\_{i, \\boldsymbol{\\nu}}\\)]{.math .notranslate .nohighlight} =30 and ntypes=1, the number of columns in the The number of columns in the global array generated by *pace* are 31, and 931, respectively, while the number of rows is 1+3\**n*+6, where *n* is the total number of atoms.

If the *bik* keyword is set to 1, the structure of the pace array is expanded. The first [\\(N\\)]{.math .notranslate .nohighlight} rows of the pace array correspond to [\\(\\# \\; B\_{i,\\boldsymbol{\\nu}}\\)]{.math .notranslate .nohighlight} instead of a single row summed over atoms [\\(i\\)]{.math .notranslate .nohighlight}. In this case, the entries in the final column for these rows are set to zero. Also, each row contains only non-zero entries for the columns corresponding to the type of that atom. This is not true in the case of *dgradflag* keyword = 1 (see below).

If the *dgradflag* keyword is set to 1, this changes the structure of the global array completely. Here the per-atom quantities are replaced with rows corresponding to descriptor gradient components on single atoms:

::: {.math .notranslate .nohighlight}
\\\[\\frac{\\partial {B\_{i,\\boldsymbol{\\nu}} }}{\\partial {r}\^a_j}\\\]
:::

where [\\({r}\^a_j\\)]{.math .notranslate .nohighlight} is the *a-th* position coordinate of the atom with global index *j*. The rows are organized in chunks, where each chunk corresponds to an atom with global index [\\(j\\)]{.math .notranslate .nohighlight}. The rows in an atom [\\(j\\)]{.math .notranslate .nohighlight} chunk correspond to atoms with global index [\\(i\\)]{.math .notranslate .nohighlight}. The total number of rows for these descriptor gradients is therefore [\\(3N\^2\\)]{.math .notranslate .nohighlight}. The number of columns is equal to the number of ACE descriptors, plus 3 additional left-most columns representing the global atom indices [\\(i\\)]{.math .notranslate .nohighlight}, [\\(j\\)]{.math .notranslate .nohighlight}, and Cartesian direction [\\(a\\)]{.math .notranslate .nohighlight} (0, 1, 2, for x, y, z). The first 3 columns of the first [\\(N\\)]{.math .notranslate .nohighlight} rows belong to the reference potential force components. The remaining K columns contain the [\\(B\_{i,\\boldsymbol{\\nu}}\\)]{.math .notranslate .nohighlight} per-atom descriptors corresponding to the non-zero entries obtained when *bikflag* = 1. The first column of the last row, after the first [\\(N + 3N\^2\\)]{.math .notranslate .nohighlight} rows, contains the reference potential energy. The virial components are not used with this option. The total number of rows is therefore [\\(N + 3N\^2 + 1\\)]{.math .notranslate .nohighlight} and the number of columns is [\\(K + 3\\)]{.math .notranslate .nohighlight}.

These values can be accessed by any command that uses global values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These computes are part of the ML-PACE package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style pace]{.doc}]pair_pace.md){.reference .internal} [[pair_style snap]{.doc}]pair_snap.md){.reference .internal} [[compute snap]{.doc}]compute_sna_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The optional keyword defaults are *bikflag* = 0, *dgradflag* = 0

------------------------------------------------------------------------

**(Drautz)** Drautz, Phys Rev B, 99, 014104 (2019).

**(Lysogorskiy)** Lysogorskiy, van der Oord, Bochkarev, Menon, Rinaldi, Hammerschmidt, Mrovec, Thompson, Csanyi, Ortner, Drautz, npj Comp Mat, 7, 97 (2021).

**(Goff)** Goff, Zhang, Negre, Rohskopf, Niklasson, Journal of Chemical Theory and Computation 19, no. 13 (2023).
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

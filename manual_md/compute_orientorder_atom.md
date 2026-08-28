::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#compute-orientorder-atom-command .section}
[]{#index-1}[]{#index-0}

# compute orientorder/atom command[](#compute-orientorder-atom-command "Link to this heading"){.headerlink}

Accelerator Variants: *orientorder/atom/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID orientorder/atom keyword values ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- orientorder/atom = style name of this compute command

- one or more keyword/value pairs may be appended

  ``` literal-block
  keyword = cutoff or nnn or degrees or wl or wl/hat or components or chunksize
    cutoff value = distance cutoff
    nnn value = number of nearest neighbors
    degrees values = nlvalues, l1, l2,...
    wl value = yes or no
    wl/hat value = yes or no
    components value = ldegree
    chunksize value = number of atoms in each pass
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all orientorder/atom
    compute 1 all orientorder/atom degrees 5 4 6 8 10 12 nnn NULL cutoff 1.5
    compute 1 all orientorder/atom wl/hat yes
    compute 1 all orientorder/atom components 6
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates a set of bond-orientational order parameters [\\(Q\_\\ell\\)]{.math .notranslate .nohighlight} for each atom in a group. These order parameters were introduced by [[Steinhardt et al.]{.std .std-ref}](#steinhardt){.reference .internal} as a way to characterize the local orientational order in atomic structures. For each atom, [\\(Q\_\\ell\\)]{.math .notranslate .nohighlight} is a real number defined as follows:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\bar{Y}\_{\\ell m} = & \\frac{1}{nnn}\\sum\_{j = 1}\^{nnn} Y\_{\\ell m}\\bigl( \\theta( \\mathbf{r}\_{ij} ), \\phi( \\mathbf{r}\_{ij} ) \\bigr) \\\\ Q\_\\ell = & \\sqrt{\\frac{4 \\pi}{2 \\ell + 1} \\sum\_{m = -\\ell }\^{m = \\ell } \\bar{Y}\_{\\ell m} \\bar{Y}\^\*\_{\\ell m}}\\end{split}\\\]
:::

The first equation defines the local order parameters as averages of the spherical harmonics [\\(Y\_{\\ell m}\\)]{.math .notranslate .nohighlight} for each neighbor. These are complex number components of the 3D analog of the 2D order parameter [\\(q_n\\)]{.math .notranslate .nohighlight}, which is implemented as LAMMPS compute [[hexorder/atom]{.doc}]compute_hexorder_atom.md){.reference .internal}. The summation is over the *nnn* nearest neighbors of the central atom. The angles [\\(\\theta\\)]{.math .notranslate .nohighlight} and [\\(\\phi\\)]{.math .notranslate .nohighlight} are the standard spherical polar angles defining the direction of the bond vector [\\(r\_{ij}\\)]{.math .notranslate .nohighlight}. The phase and sign of [\\(Y\_{\\ell m}\\)]{.math .notranslate .nohighlight} follow the standard conventions, so that [\\(\\mathrm{sign}(Y\_{\\ell\\ell}(0,0)) = (-1)\^\\ell\\)]{.math .notranslate .nohighlight}. The second equation defines [\\(Q\_\\ell\\)]{.math .notranslate .nohighlight}, which is a rotationally invariant non-negative amplitude obtained by summing over all the components of degree [\\(\\ell\\)]{.math .notranslate .nohighlight}.

The optional keyword *cutoff* defines the distance cutoff used when searching for neighbors. The default value, also the maximum allowable value, is the cutoff specified by the pair style.

The optional keyword *nnn* defines the number of nearest neighbors used to calculate [\\(Q\_\\ell\\)]{.math .notranslate .nohighlight}. The default value is 12. If the value is NULL, then all neighbors up to the specified distance cutoff are used.

The optional keyword *degrees* defines the list of order parameters to be computed. The first argument *nlvalues* is the number of order parameters. This is followed by that number of non-negative integers giving the degree of each order parameter. Because [\\(Q_2\\)]{.math .notranslate .nohighlight} and all odd-degree order parameters are zero for atoms in cubic crystals (see [[Steinhardt]{.std .std-ref}](#steinhardt){.reference .internal}), the default order parameters are [\\(Q_4\\)]{.math .notranslate .nohighlight}, [\\(Q_6\\)]{.math .notranslate .nohighlight}, [\\(Q_8\\)]{.math .notranslate .nohighlight}, [\\(Q\_{10}\\)]{.math .notranslate .nohighlight}, and [\\(Q\_{12}\\)]{.math .notranslate .nohighlight}. For the FCC crystal with *nnn* =12,

::: {.math .notranslate .nohighlight}
\\\[Q_4 = \\sqrt{\\frac{7}{192}} \\approx 0.19094\\\]
:::

The numerical values of all order parameters up to [\\(Q\_{12}\\)]{.math .notranslate .nohighlight} for a range of commonly encountered high-symmetry structures are given in Table I of [[Mickel et al.]{.std .std-ref}](#mickel){.reference .internal}, and these can be reproduced with this compute.

The optional keyword *wl* will output the third-order invariants [\\(W\_\\ell\\)]{.math .notranslate .nohighlight} (see Eq. 1.4 in [[Steinhardt]{.std .std-ref}](#steinhardt){.reference .internal}) for the same degrees as for the [\\(Q\_\\ell\\)]{.math .notranslate .nohighlight} parameters. For the FCC crystal with *nnn* = 12,

::: {.math .notranslate .nohighlight}
\\\[W_4 = -\\sqrt{\\frac{14}{143}} \\left(\\frac{49}{4096}\\right) \\pi\^{-3/2} \\approx -0.0006722136\\\]
:::

The optional keyword *wl/hat* will output the normalized third-order invariants [\\(\\hat{W}\_\\ell\\)]{.math .notranslate .nohighlight} (see Eq. 2.2 in [[Steinhardt]{.std .std-ref}](#steinhardt){.reference .internal}) for the same degrees as for the [\\(Q\_\\ell\\)]{.math .notranslate .nohighlight} parameters. For the FCC crystal with *nnn* =12,

::: {.math .notranslate .nohighlight}
\\\[\\hat{W}\_4 = -\\frac{7}{3} \\sqrt{\\frac{2}{429}} \\approx -0.159317\\\]
:::

The numerical values of [\\(\\hat{W}\_\\ell\\)]{.math .notranslate .nohighlight} for a range of commonly encountered high-symmetry structures are given in Table I of [[Steinhardt]{.std .std-ref}](#steinhardt){.reference .internal}, and these can be reproduced with this keyword.

The optional keyword *components* will output the components of the *normalized* complex vector [\\(\\hat{Y}\_{\\ell m} = \\bar{Y}\_{\\ell m}/\|\\bar{Y}\_{\\ell m}\|\\)]{.math .notranslate .nohighlight} of degree *ldegree*, which must be included in the list of order parameters to be computed. This option can be used in conjunction with [[compute coord_atom]{.doc}]compute_coord_atom.md){.reference .internal} to calculate the ten Wolde's criterion to identify crystal-like particles, as discussed in [[ten Wolde]{.std .std-ref}](#tenwolde2){.reference .internal}.

The optional keyword *chunksize* is only applicable when using the the KOKKOS package and is ignored otherwise. This keyword controls the number of atoms in each pass used to compute the bond-orientational order parameters and is used to avoid running out of memory. For example if there are 32768 atoms in the simulation and the *chunksize* is set to 16384, the parameter calculation will be broken up into two passes.

The value of [\\(Q\_\\ell\\)]{.math .notranslate .nohighlight} is set to zero for atoms not in the specified compute group, as well as for atoms that have less than *nnn* neighbors within the distance cutoff, unless *nnn* is NULL.

The neighbor list needed to compute this quantity is constructed each time the calculation is performed (i.e., each time a snapshot of atoms is dumped). Thus it can be inefficient to compute/dump this quantity too frequently.

::: {.admonition .note}
Note

If you have a bonded system, then the settings of [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command can remove pairwise interactions between atoms in the same bond, angle, or dihedral. This is the default setting for the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command, and means those pairwise interactions do not appear in the neighbor list. Because this fix uses the neighbor list, it also means those pairs will not be included in the order parameter. This difficulty can be circumvented by writing a dump file, and using the [[rerun]{.doc}]rerun.md){.reference .internal} command to compute the order parameter for snapshots in the dump file. The rerun script can use a [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command that includes all pairs in the neighbor list.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom array with *nlvalues* columns, giving the [\\(Q\_\\ell\\)]{.math .notranslate .nohighlight} values for each atom, which are real numbers in the range [\\(0 \\le Q\_\\ell \\le 1\\)]{.math .notranslate .nohighlight}.

If the keyword *wl* is set to yes, then the [\\(W\_\\ell\\)]{.math .notranslate .nohighlight} values for each atom will be added to the output array, which are real numbers.

If the keyword *wl/hat* is set to yes, then the [\\(\\hat{W}\_\\ell\\)]{.math .notranslate .nohighlight} values for each atom will be added to the output array, which are real numbers.

If the keyword *components* is set, then the real and imaginary parts of each component of *normalized* [\\(\\hat{Y}\_{\\ell m}\\)]{.math .notranslate .nohighlight} will be added to the output array in the following order: [\\(\\Re(\\hat{Y}\_{-m}),\\)]{.math .notranslate .nohighlight} [\\(\\Im(\\hat{Y}\_{-m}),\\)]{.math .notranslate .nohighlight} [\\(\\Re(\\hat{Y}\_{-m+1}),\\)]{.math .notranslate .nohighlight} [\\(\\Im(\\hat{Y}\_{-m+1}), \\dotsc,\\)]{.math .notranslate .nohighlight} [\\(\\Re(\\hat{Y}\_m),\\)]{.math .notranslate .nohighlight} [\\(\\Im(\\hat{Y}\_m).\\)]{.math .notranslate .nohighlight}

In summary, the per-atom array will contain *nlvalues* columns, followed by an additional *nlvalues* columns if *wl* is set to yes, followed by an additional *nlvalues* columns if *wl/hat* is set to yes, followed by an additional 2\*(2\* *ldegree*+1) columns if the *components* keyword is set.

These values can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute coord/atom]{.doc}]compute_coord_atom.md){.reference .internal}, [[compute centro/atom]{.doc}]compute_centro_atom.md){.reference .internal}, [[compute hexorder/atom]{.doc}]compute_hexorder_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are *cutoff* = pair style cutoff, *nnn* = 12, *degrees* = 5 4 6 8 10 12 (i.e., [\\(Q_4\\)]{.math .notranslate .nohighlight}, [\\(Q_6\\)]{.math .notranslate .nohighlight}, [\\(Q_8\\)]{.math .notranslate .nohighlight}, [\\(Q\_{10}\\)]{.math .notranslate .nohighlight}, and [\\(Q\_{12}\\)]{.math .notranslate .nohighlight}), *wl* = no, *wl/hat* = no, *components* off, and *chunksize* = 16384

------------------------------------------------------------------------

**(Steinhardt)** P. Steinhardt, D. Nelson, and M. Ronchetti, Phys. Rev. B 28, 784 (1983).

**(Mickel)** W. Mickel, S. C. Kapfer, G. E. Schroeder-Turkand, K. Mecke, J. Chem. Phys. 138, 044501 (2013).

**(tenWolde)** P. R. ten Wolde, M. J. Ruiz-Montero, D. Frenkel, J. Chem. Phys. 104, 9932 (1996).
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

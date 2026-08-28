:::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#compute-sna-atom-command .section}
[]{#index-7}[]{#index-6}[]{#index-5}[]{#index-4}[]{#index-3}[]{#index-2}[]{#index-1}[]{#index-0}

# compute sna/atom command[](#compute-sna-atom-command "Link to this heading"){.headerlink}
:::

::: {#compute-snad-atom-command .section}
# compute snad/atom command[](#compute-snad-atom-command "Link to this heading"){.headerlink}
:::

::: {#compute-snav-atom-command .section}
# compute snav/atom command[](#compute-snav-atom-command "Link to this heading"){.headerlink}
:::

::: {#compute-snap-command .section}
# compute snap command[](#compute-snap-command "Link to this heading"){.headerlink}
:::

::: {#compute-sna-grid-command .section}
# compute sna/grid command[](#compute-sna-grid-command "Link to this heading"){.headerlink}
:::

::::::::::::::::::::::::::::::::: {#compute-sna-grid-local-command .section}
# compute sna/grid/local command[](#compute-sna-grid-local-command "Link to this heading"){.headerlink}

Accelerator Variants: *sna/grid/kk*, *sna/grid/local/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID sna/atom rcutfac rfac0 twojmax R_1 R_2 ... w_1 w_2 ... keyword values ...
    compute ID group-ID snad/atom rcutfac rfac0 twojmax R_1 R_2 ... w_1 w_2 ... keyword values ...
    compute ID group-ID snav/atom rcutfac rfac0 twojmax R_1 R_2 ... w_1 w_2 ... keyword values ...
    compute ID group-ID snap rcutfac rfac0 twojmax R_1 R_2 ... w_1 w_2 ... keyword values ...
    compute ID group-ID snap rcutfac rfac0 twojmax R_1 R_2 ... w_1 w_2 ... keyword values ...
    compute ID group-ID sna/grid grid nx ny nz rcutfac rfac0 twojmax R_1 R_2 ... w_1 w_2 ... keyword values ...
    compute ID group-ID sna/grid/local grid nx ny nz rcutfac rfac0 twojmax R_1 R_2 ... w_1 w_2 ... keyword values ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- sna/atom = style name of this compute command

- *rcutfac* = scale factor applied to all cutoff radii (positive real)

- *rfac0* = parameter in distance to angle conversion (0 \< rcutfac \< 1)

- *twojmax* = band limit for bispectrum components (non-negative integer)

- *R_1, R_2,...* = list of cutoff radii, one for each type (distance units)

- *w_1, w_2,...* = list of neighbor weights, one for each type

- *grid* values = nx, ny, nz, number of grid points in x, y, and z directions (positive integer)

- zero or more keyword/value pairs may be appended

- keyword = *rmin0* or *switchflag* or *bzeroflag* or *quadraticflag* or *chem* or *bnormflag* or *wselfallflag* or *bikflag* or *switchinnerflag* or *sinner* or *dinner* or *dgradflag* or *nnn* or *wmode* or *delta*

  ``` literal-block
  rmin0 value = parameter in distance to angle conversion (distance units)
  switchflag value = 0 or 1
     0 = do not use switching function
     1 = use switching function
  bzeroflag value = 0 or 1
     0 = do not subtract B0
     1 = subtract B0
  quadraticflag value = 0 or 1
     0 = do not generate quadratic terms
     1 = generate quadratic terms
  chem values = nelements elementlist
     nelements = number of SNAP elements
     elementlist = ntypes integers in range [0, nelements)
  bnormflag value = 0 or 1
     0 = do not normalize
     1 = normalize bispectrum components
  wselfallflag value = 0 or 1
     0 = self-contribution only for element of central atom
     1 = self-contribution for all elements
  switchinnerflag value = 0 or 1
     0 = do not use inner switching function
     1 = use inner switching function
  sinner values = sinnerlist
     sinnerlist = ntypes values of Sinner (distance units)
  dinner values = dinnerlist
     dinnerlist = ntypes values of Dinner (distance units)
  bikflag value = 0 or 1 (only implemented for compute snap)
     0 = descriptors are summed over atoms of each type
     1 = descriptors are listed separately for each atom
  dgradflag value = 0 or 1 (only implemented for compute snap)
     0 = descriptor gradients are summed over atoms of each type
     1 = descriptor gradients are listed separately for each atom pair
  ```

- additional keyword = *nnn* or *wmode* or *delta*

  ``` literal-block
  nnn value = number of considered nearest neighbors to compute the bispectrum over a target specific number of neighbors (only implemented for compute sna/atom)
  wmode value = weight function for finding optimal cutoff to match the target number of neighbors (required if nnn used, only implemented for compute sna/atom)
     0 = heavyside weight function
     1 = hyperbolic tangent weight function
  delta value = transition interval centered at cutoff distance for hyperbolic tangent weight function (ignored if wmode=0, required if wmode=1, only implemented for compute sna/atom)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute b all sna/atom 1.4 0.99363 6 2.0 2.4 0.75 1.0 rmin0 0.0
    compute db all sna/atom 1.4 0.95 6 2.0 1.0
    compute vb all sna/atom 1.4 0.95 6 2.0 1.0
    compute snap all snap 1.4 0.95 6 2.0 1.0
    compute snap all snap 1.0 0.99363 6 3.81 3.83 1.0 0.93 chem 2 0 1
    compute snap all snap 1.0 0.99363 6 3.81 3.83 1.0 0.93 switchinnerflag 1 sinner 1.35 1.6 dinner 0.25 0.3
    compute bgrid all sna/grid/local grid 200 200 200 1.4 0.95 6 2.0 1.0
    compute bnnn all sna/atom 9.0 0.99363 8 0.5 1.0 rmin0 0.0 nnn 24 wmode 1 delta 0.2
:::
::::
:::::

:::::::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates a set of quantities related to the bispectrum components of the atoms in a group. These computes are used primarily for calculating the dependence of energy, force, and stress components on the linear coefficients in the [[snap pair_style]{.doc}]pair_snap.md){.reference .internal}, which is useful when training a SNAP potential to match target data.

Bispectrum components of an atom are order parameters characterizing the radial and angular distribution of neighbor atoms. The detailed mathematical definition is given in the paper by Thompson et al. [[(Thompson)]{.std .std-ref}](#thompson20141){.reference .internal}

The position of a neighbor atom *i'* relative to a central atom *i* is a point within the 3D ball of radius [\\(R\_{ii\'}\\)]{.math .notranslate .nohighlight} = *rcutfac* [\\((R_i + R_i\')\\)]{.math .notranslate .nohighlight}

Bartok et al. [[(Bartok)]{.std .std-ref}](#bartok20101){.reference .internal}, proposed mapping this 3D ball onto the 3-sphere, the surface of the unit ball in a four-dimensional space. The radial distance *r* within *R_ii'* is mapped on to a third polar angle [\\(\\theta_0\\)]{.math .notranslate .nohighlight} defined by,

::: {.math .notranslate .nohighlight}
\\\[\\theta_0 = \\mathsf{rfac0} \\frac{r-r\_{min0}}{R\_{ii\'}-r\_{min0}} \\pi\\\]
:::

In this way, all possible neighbor positions are mapped on to a subset of the 3-sphere. Points south of the latitude [\\(\\theta_0 = \\mathsf{rfac0} \\pi\\)]{.math .notranslate .nohighlight} are excluded.

The natural basis for functions on the 3-sphere is formed by the representatives of *SU(2)*, the matrices [\\(U\^j\_{m,m\'}(\\theta, \\phi, \\theta_0)\\)]{.math .notranslate .nohighlight}. These functions are better known as [\\(D\^j\_{m,m\'}\\)]{.math .notranslate .nohighlight}, the elements of the Wigner *D*-matrices [[(Meremianin]{.std .std-ref}](#meremianin2006){.reference .internal}, [[Varshalovich]{.std .std-ref}](#varshalovich1987){.reference .internal}, [[Mason)]{.std .std-ref}](#mason2009){.reference .internal} The density of neighbors on the 3-sphere can be written as a sum of Dirac-delta functions, one for each neighbor, weighted by species and radial distance. Expanding this density function as a generalized Fourier series in the basis functions, we can write each Fourier coefficient as

::: {.math .notranslate .nohighlight}
\\\[u\^j\_{m,m\'} = U\^j\_{m,m\'}(0,0,0) + \\sum\_{r\_{ii\'} \< R\_{ii\'}}{f_c(r\_{ii\'}) w\_{\\mu\_{i\'}} U\^j\_{m,m\'}(\\theta_0,\\theta,\\phi)}\\\]
:::

The [\\(w\_{\\mu\_{i\'}}\\)]{.math .notranslate .nohighlight} neighbor weights are dimensionless numbers that depend on [\\(\\mu\_{i\'}\\)]{.math .notranslate .nohighlight}, the SNAP element of atom *i'*, while the central atom is arbitrarily assigned a unit weight. The function [\\(f_c(r)\\)]{.math .notranslate .nohighlight} ensures that the contribution of each neighbor atom goes smoothly to zero at [\\(R\_{ii\'}\\)]{.math .notranslate .nohighlight}:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}f_c(r) = & \\frac{1}{2}(\\cos(\\pi \\frac{r-r\_{min0}}{R\_{ii\'}-r\_{min0}}) + 1), r \\leq R\_{ii\'} \\\\ = & 0, r \> R\_{ii\'}\\end{split}\\\]
:::

The expansion coefficients [\\(u\^j\_{m,m\'}\\)]{.math .notranslate .nohighlight} are complex-valued and they are not directly useful as descriptors, because they are not invariant under rotation of the polar coordinate frame. However, the following scalar triple products of expansion coefficients can be shown to be real-valued and invariant under rotation [[(Bartok)]{.std .std-ref}](#bartok20101){.reference .internal}.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}B\_{j_1,j_2,j} = \\sum\_{m_1,m\'\_1=-j_1}\^{j_1}\\sum\_{m_2,m\'\_2=-j_2}\^{j_2}\\sum\_{m,m\'=-j}\^{j} (u\^j\_{m,m\'})\^\* H {\\scriptscriptstyle \\begin{array}{l} {j} {m} {m\'} \\\\ {j_1} {m_1} {m\'\_1} \\\\ {j_2} {m_2} {m\'\_2} \\end{array}} u\^{j_1}\_{m_1,m\'\_1} u\^{j_2}\_{m_2,m\'\_2}\\end{split}\\\]
:::

The constants [\\(H\^{jmm\'}\_{j_1 m_1 m\_{1\'},j_2 m\_ 2m\_{2\'}}\\)]{.math .notranslate .nohighlight} are coupling coefficients, analogous to Clebsch-Gordan coefficients for rotations on the 2-sphere. These invariants are the components of the bispectrum and these are the quantities calculated by the compute *sna/atom*. They characterize the strength of density correlations at three points on the 3-sphere. The j2=0 subset form the power spectrum, which characterizes the correlations of two points. The lowest-order components describe the coarsest features of the density function, while higher-order components reflect finer detail. Each bispectrum component contains terms that depend on the positions of up to 4 atoms (3 neighbors and the central atom).

Compute *snad/atom* calculates the derivative of the bispectrum components summed separately for each LAMMPS atom type:

::: {.math .notranslate .nohighlight}
\\\[-\\sum\_{i\' \\in I} \\frac{\\partial {B\^{i\'}\_{j_1,j_2,j} }}{\\partial \\mathbf{r}\_i}\\\]
:::

The sum is over all atoms *i'* of atom type *I*. For each atom *i*, this compute evaluates the above expression for each direction, each atom type, and each bispectrum component. See section below on output for a detailed explanation.

Compute *snav/atom* calculates the virial contribution due to the derivatives:

::: {.math .notranslate .nohighlight}
\\\[-\\mathbf{r}\_i \\otimes \\sum\_{i\' \\in I} \\frac{\\partial {B\^{i\'}\_{j_1,j_2,j}}}{\\partial \\mathbf{r}\_i}\\\]
:::

Again, the sum is over all atoms *i'* of atom type *I*. For each atom *i*, this compute evaluates the above expression for each of the six virial components, each atom type, and each bispectrum component. See section below on output for a detailed explanation.

Compute *snap* calculates a global array containing information related to all three of the above per-atom computes *sna/atom*, *snad/atom*, and *snav/atom*. The first row of the array contains the summation of *sna/atom* over all atoms, but broken out by type. The last six rows of the array contain the summation of *snav/atom* over all atoms, broken out by type. In between these are 3\**N* rows containing the same values computed by *snad/atom* (these are already summed over all atoms and broken out by type). The element in the last column of each row contains the potential energy, force, or stress, according to the row. These quantities correspond to the user-specified reference potential that must be subtracted from the target data when fitting SNAP. The potential energy calculation uses the built in compute *thermo_pe*. The stress calculation uses a compute called *snap_press* that is automatically created behind the scenes, according to the following command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute snap_press all pressure NULL virial
:::
::::

See section below on output for a detailed explanation of the data layout in the global array.

::: versionadded
[Added in version 3Aug2022.]{.versionmodified .added}
:::

The compute *sna/grid* and *sna/grid/local* commands calculate bispectrum components for a regular grid of points. These are calculated from the local density of nearby atoms *i'* around each grid point, as if there was a central atom *i* at the grid point. This is useful for characterizing fine-scale structure in a configuration of atoms, and it is used in the [MALA package](https://github.com/casus/mala){.reference .external} to build machine-learning surrogates for finite-temperature Kohn-Sham density functional theory ([[Ellis et al.]{.std .std-ref}](#ellis2021){.reference .internal}) Neighbor atoms not in the group do not contribute to the bispectrum components of the grid points. The distance cutoff [\\(R\_{ii\'}\\)]{.math .notranslate .nohighlight} assumes that *i* has the same type as the neighbor atom *i'*. Both computes can be hardware accelerated with Kokkos by using the *sna/grid/kk* and *sna/grid/local/kk* commands, respectively.

Compute *sna/grid* calculates a global array containing bispectrum components for a regular grid of points. The grid is aligned with the current box dimensions, with the first point at the box origin, and forming a regular 3d array with *nx*, *ny*, and *nz* points in the x, y, and z directions. For triclinic boxes, the array is congruent with the periodic lattice vectors a, b, and c. The array contains one row for each of the [\\(nx \\times ny \\times nz\\)]{.math .notranslate .nohighlight} grid points, looping over the index for *ix* fastest, then *iy*, and *iz* slowest. Each row of the array contains the *x*, *y*, and *z* coordinates of the grid point, followed by the bispectrum components. See section below on output for a detailed explanation of the data layout in the global array.

Compute *sna/grid/local* calculates bispectrum components of a regular grid of points similarly to compute *sna/grid* described above. However, because the array is local, it contains only rows for grid points that are local to the processor subdomain. The global grid of [\\(nx \\times ny \\times nz\\)]{.math .notranslate .nohighlight} points is still laid out in space the same as for *sna/grid*, but grid points are strictly partitioned, so that every grid point appears in one and only one local array. The array contains one row for each of the local grid points, looping over the global index *ix* fastest, then *iy*, and *iz* slowest. Each row of the array contains the global indexes *ix*, *iy*, and *iz* first, followed by the *x*, *y*, and *z* coordinates of the grid point, followed by the bispectrum components. See section below on output for a detailed explanation of the data layout in the global array.

The value of all bispectrum components will be zero for atoms not in the group. Neighbor atoms not in the group do not contribute to the bispectrum of atoms in the group.

The neighbor list needed to compute this quantity is constructed each time the calculation is performed (i.e. each time a snapshot of atoms is dumped). Thus it can be inefficient to compute/dump this quantity too frequently.

The argument *rcutfac* is a scale factor that controls the ratio of atomic radius to radial cutoff distance.

The argument *rfac0* and the optional keyword *rmin0* define the linear mapping from radial distance to polar angle [\\(theta_0\\)]{.math .notranslate .nohighlight} on the 3-sphere, given above.

The argument *twojmax* defines which bispectrum components are generated. See section below on output for a detailed explanation of the number of bispectrum components and the ordered in which they are listed.

The keyword *switchflag* can be used to turn off the switching function [\\(f_c(r)\\)]{.math .notranslate .nohighlight}.

The keyword *bzeroflag* determines whether or not *B0*, the bispectrum components of an atom with no neighbors, are subtracted from the calculated bispectrum components. This optional keyword normally only affects compute *sna/atom*. However, when *quadraticflag* is on, it also affects *snad/atom* and *snav/atom*.

The keyword *quadraticflag* determines whether or not the quadratic combinations of bispectrum quantities are generated. These are formed by taking the outer product of the vector of bispectrum components with itself. See section below on output for a detailed explanation of the number of quadratic terms and the ordered in which they are listed.

The keyword *chem* activates the explicit multi-element variant of the SNAP bispectrum components. The argument *nelements* specifies the number of SNAP elements that will be handled. This is followed by *elementlist*, a list of integers of length *ntypes*, with values in the range \[0, *nelements* ), which maps each LAMMPS type to one of the SNAP elements. Note that multiple LAMMPS types can be mapped to the same element, and some elements may be mapped by no LAMMPS type. However, in typical use cases (training SNAP potentials) the mapping from LAMMPS types to elements is one-to-one.

The explicit multi-element variant invoked by the *chem* keyword partitions the density of neighbors into partial densities for each chemical element. This is described in detail in the paper by [[Cusentino et al.]{.std .std-ref}](#cusentino2020){.reference .internal} The bispectrum components are indexed on ordered triplets of elements:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}B\_{j_1,j_2,j}\^{\\kappa\\lambda\\mu} = \\sum\_{m_1,m\'\_1=-j_1}\^{j_1}\\sum\_{m_2,m\'\_2=-j_2}\^{j_2}\\sum\_{m,m\'=-j}\^{j} (u\^{\\mu}\_{j,m,m\'})\^\* H {\\scriptscriptstyle \\begin{array}{l} {j} {m} {m\'} \\\\ {j_1} {m_1} {m\'\_1} \\\\ {j_2} {m_2} {m\'\_2} \\end{array}} u\^{\\kappa}\_{j_1,m_1,m\'\_1} u\^{\\lambda}\_{j_2,m_2,m\'\_2}\\end{split}\\\]
:::

where [\\(u\^{\\mu}\_{j,m,m\'}\\)]{.math .notranslate .nohighlight} is an expansion coefficient for the partial density of neighbors of element [\\(\\mu\\)]{.math .notranslate .nohighlight}

::: {.math .notranslate .nohighlight}
\\\[u\^{\\mu}\_{j,m,m\'} = w\^{self}\_{\\mu\_{i}\\mu} U\^{j,m,m\'}(0,0,0) + \\sum\_{r\_{ii\'} \< R\_{ii\'}}{\\delta\_{\\mu\\mu\_{i\'}}f_c(r\_{ii\'}) w\_{\\mu\_{i\'}} U\^{j,m,m\'}(\\theta_0,\\theta,\\phi)}\\\]
:::

where [\\(w\^{self}\_{\\mu\_{i}\\mu}\\)]{.math .notranslate .nohighlight} is the self-contribution, which is either 1 or 0 (see keyword *wselfallflag* below), [\\(\\delta\_{\\mu\\mu\_{i\'}}\\)]{.math .notranslate .nohighlight} indicates that the sum is only over neighbor atoms of element [\\(\\mu\\)]{.math .notranslate .nohighlight}, and all other quantities are the same as those appearing in the original equation for [\\(u\^j\_{m,m\'}\\)]{.math .notranslate .nohighlight} given above.

The keyword *wselfallflag* defines the rule used for the self-contribution. If *wselfallflag* is on, then [\\(w\^{self}\_{\\mu\_{i}\\mu}\\)]{.math .notranslate .nohighlight} = 1. If it is off then [\\(w\^{self}\_{\\mu\_{i}\\mu}\\)]{.math .notranslate .nohighlight} = 0, except in the case of [\\({\\mu\_{i}=\\mu}\\)]{.math .notranslate .nohighlight}, when [\\(w\^{self}\_{\\mu\_{i}\\mu}\\)]{.math .notranslate .nohighlight} = 1. When the *chem* keyword is not used, this keyword has no effect.

The keyword *bnormflag* determines whether or not the bispectrum component [\\(B\_{j_1,j_2,j}\\)]{.math .notranslate .nohighlight} is divided by a factor of [\\(2j+1\\)]{.math .notranslate .nohighlight}. This normalization simplifies force calculations because of the following symmetry relation

::: {.math .notranslate .nohighlight}
\\\[\\frac{B\_{j_1,j_2,j}}{2j+1} = \\frac{B\_{j,j_2,j_1}}{2j_1+1} = \\frac{B\_{j_1,j,j_2}}{2j_2+1}\\\]
:::

This option is typically used in conjunction with the *chem* keyword, and LAMMPS will generate a warning if both *chem* and *bnormflag* are not both set or not both unset.

The keyword *switchinnerflag* with value 1 activates an additional radial switching function similar to [\\(f_c(r)\\)]{.math .notranslate .nohighlight} above, but acting to switch off smoothly contributions from neighbor atoms at short separation distances. This is useful when SNAP is used in combination with a simple repulsive potential. For a neighbor atom at distance [\\(r\\)]{.math .notranslate .nohighlight}, its contribution is scaled by a multiplicative factor [\\(f\_{inner}(r)\\)]{.math .notranslate .nohighlight} defined as follows:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split} = & 0, r \\leq S\_{inner} - D\_{inner} \\\\ f\_{inner}(r) = & \\frac{1}{2}(1 - \\cos(\\frac{\\pi}{2} (1 + \\frac{r-S\_{inner}}{D\_{inner}})), S\_{inner} - D\_{inner} \< r \\leq S\_{inner} + D\_{inner} \\\\ = & 1, r \> S\_{inner} + D\_{inner}\\end{split}\\\]
:::

where the switching region is centered at [\\(S\_{inner}\\)]{.math .notranslate .nohighlight} and it extends a distance [\\(D\_{inner}\\)]{.math .notranslate .nohighlight} to the left and to the right of this. With this option, additional keywords *sinner* and *dinner* must be used, each followed by *ntypes* values for [\\(S\_{inner}\\)]{.math .notranslate .nohighlight} and [\\(D\_{inner}\\)]{.math .notranslate .nohighlight}, respectively. When the central atom and the neighbor atom have different types, the values of [\\(S\_{inner}\\)]{.math .notranslate .nohighlight} and [\\(D\_{inner}\\)]{.math .notranslate .nohighlight} are the arithmetic means of the values for both types.

The keywords *bikflag* and *dgradflag* are only used by compute *snap*. The keyword *bikflag* determines whether or not to list the descriptors of each atom separately, or sum them together and list in a single row. If *bikflag* is set to *0* then a single bispectrum row is used, which contains the per-atom bispectrum descriptors [\\(B\_{i,k}\\)]{.math .notranslate .nohighlight} summed over all atoms *i* to produce [\\(B_k\\)]{.math .notranslate .nohighlight}. If *bikflag* is set to *1* this is replaced by a separate per-atom bispectrum row for each atom. In this case, the entries in the final column for these rows are set to zero.

The keyword *dgradflag* determines whether to sum atom gradients or list them separately. If *dgradflag* is set to 0, the bispectrum descriptor gradients w.r.t. atom *j* are summed over all atoms *i'* of type *I* (similar to *snad/atom* above). If *dgradflag* is set to 1, gradients are listed separately for each pair of atoms. Each row corresponds to a single term [\\(\\frac{\\partial {B\_{i,k} }}{\\partial {r}\^a_j}\\)]{.math .notranslate .nohighlight} where [\\({r}\^a_j\\)]{.math .notranslate .nohighlight} is the *a-th* position coordinate of the atom with global index *j*. This also changes the number of columns to be equal to the number of bispectrum components, with 3 additional columns representing the indices [\\(i\\)]{.math .notranslate .nohighlight}, [\\(j\\)]{.math .notranslate .nohighlight}, and [\\(a\\)]{.math .notranslate .nohighlight}, as explained more in the Output info section below. The option *dgradflag=1* requires that *bikflag=1*.

::: {.admonition .note}
Note

Using *dgradflag* = 1 produces a global array with [\\(N + 3N\^2 + 1\\)]{.math .notranslate .nohighlight} rows which becomes expensive for systems with more than 1000 atoms.
:::

::: {.admonition .note}
Note

If you have a bonded system, then the settings of [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command can remove pairwise interactions between atoms in the same bond, angle, or dihedral. This is the default setting for the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command, and means those pairwise interactions do not appear in the neighbor list. Because this fix uses the neighbor list, it also means those pairs will not be included in the calculation. One way to get around this, is to write a dump file, and use the [[rerun]{.doc}]rerun.md){.reference .internal} command to compute the bispectrum components for snapshots in the dump file. The rerun script can use a [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command that includes all pairs in the neighbor list.
:::

The keyword *nnn* allows for the calculation of the bispectrum over a specific target number of neighbors. This option is only implemented for the compute *sna/atom*. An optimal cutoff radius for defining the neighborhood of the central atom is calculated by means of a dichotomy algorithm. This iterative process allows to assign weights to neighboring atoms in order to match the total sum of weights with the target number of neighbors. Depending on the radial weight function used in that process, the cutoff radius can fluctuate a lot in the presence of thermal noise. Therefore, in addition to the *nnn* keyword, the keyword *wmode* allows to choose whether a Heaviside (*wmode* = 0) function or a Hyperbolic tangent function (*wmode* = 1) should be used. If the Heaviside function is used, the cutoff radius exactly matches the distance between the central atom an its *nnn*'th neighbor. However, in the case of the hyperbolic tangent function, the dichotomy algorithm allows to span the weights over a distance *delta* in order to reduce fluctuations in the resulting local atomic environment fingerprint. The detailed formalism is given in the paper by Lafourcade et al. [[(Lafourcade)]{.std .std-ref}](#lafourcade2023-2){.reference .internal}.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::::::::::::::::

------------------------------------------------------------------------

::::::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

Compute *sna/atom* calculates a per-atom array, each column corresponding to a particular bispectrum component. The total number of columns and the identity of the bispectrum component contained in each column depend of the value of *twojmax*, as described by the following piece of python code:

:::: {.highlight-none .notranslate}
::: highlight
    for j1 in range(0,twojmax+1):
        for j2 in range(0,j1+1):
            for j in range(j1-j2,min(twojmax,j1+j2)+1,2):
                if (j>=j1): print j1/2.,j2/2.,j/2.
:::
::::

There are [\\(m(m+1)/2\\)]{.math .notranslate .nohighlight} descriptors with last index *j*, where *m* = [\\(\\lfloor j \\rfloor + 1\\)]{.math .notranslate .nohighlight}. Hence, for even *twojmax* = 2(*m*-1), [\\(K = m(m+1)(2m+1)/6\\)]{.math .notranslate .nohighlight}, the *m*-th pyramidal number, and for odd *twojmax* = 2 *m*-1, [\\(K = m(m+1)(m+2)/3\\)]{.math .notranslate .nohighlight}, twice the *m*-th tetrahedral number.

::: {.admonition .note}
Note

the *diagonal* keyword allowing other possible choices for the number of bispectrum components was removed in 2019, since all potentials use the value of 3, corresponding to the above set of bispectrum components.
:::

Compute *snad/atom* evaluates a per-atom array. The columns are arranged into *ntypes* blocks, listed in order of atom type *I*. Each block contains three sub-blocks corresponding to the *x*, *y*, and *z* components of the atom position. Each of these sub-blocks contains *K* columns for the *K* bispectrum components, the same as for compute *sna/atom*

Compute *snav/atom* evaluates a per-atom array. The columns are arranged into *ntypes* blocks, listed in order of atom type *I*. Each block contains six sub-blocks corresponding to the *xx*, *yy*, *zz*, *yz*, *xz*, and *xy* components of the virial tensor in Voigt notation. Each of these sub-blocks contains *K* columns for the *K* bispectrum components, the same as for compute *sna/atom*

Compute *snap* evaluates a global array. The columns are arranged into *ntypes* blocks, listed in order of atom type *I*. Each block contains one column for each bispectrum component, the same as for compute *sna/atom*. A final column contains the corresponding energy, force component on an atom, or virial stress component. The rows of the array appear in the following order:

- 1 row: *sna/atom* quantities summed for all atoms of type *I*

- 3\**N* rows: *snad/atom* quantities, with derivatives w.r.t. x, y, and z coordinate of atom *i* appearing in consecutive rows. The atoms are sorted based on atom ID.

- 6 rows: *snav/atom* quantities summed for all atoms of type *I*

For example, if *K* =30 and ntypes=1, the number of columns in the per-atom arrays generated by *sna/atom*, *snad/atom*, and *snav/atom* are 30, 90, and 180, respectively. With *quadratic* value=1, the numbers of columns are 930, 2790, and 5580, respectively. The number of columns in the global array generated by *snap* are 31, and 931, respectively, while the number of rows is 1+3\**N*+6, where *N* is the total number of atoms.

Compute *sna/grid* evaluates a global array. The array contains one row for each of the [\\(nx \\times ny \\times nz\\)]{.math .notranslate .nohighlight} grid points, looping over the index for *ix* fastest, then *iy*, and *iz* slowest. Each row of the array contains the *x*, *y*, and *z* coordinates of the grid point, followed by the bispectrum components.

Compute *sna/grid/local* evaluates a local array. The array contains one row for each of the local grid points, looping over the global index *ix* fastest, then *iy*, and *iz* slowest. Each row of the array contains the global indexes *ix*, *iy*, and *iz* first, followed by the *x*, *y*, and *z* coordinates of the grid point, followed by the bispectrum components.

If the *quadratic* keyword value is set to 1, then additional columns are generated, corresponding to the products of all distinct pairs of bispectrum components. If the number of bispectrum components is *K*, then the number of distinct pairs is *K*(*K*+1)/2. For compute *sna/atom* these columns are appended to existing *K* columns. The ordering of quadratic terms is upper-triangular, (1,1),(1,2)...(1,*K*),(2,1)...(*K*-1,*K*-1),(*K*-1,*K*),(*K*,*K*). For computes *snad/atom* and *snav/atom* each set of *K*(*K*+1)/2 additional columns is inserted directly after each of sub-block of linear terms i.e. linear and quadratic terms are contiguous. So the nesting order from inside to outside is bispectrum component, linear then quadratic, vector/tensor component, type.

If the *chem* keyword is used, then the data is arranged into [\\(N\_{elem}\^3\\)]{.math .notranslate .nohighlight} sub-blocks, each sub-block corresponding to a particular chemical labeling [\\(\\kappa\\lambda\\mu\\)]{.math .notranslate .nohighlight} with the last label changing fastest. Each sub-block contains *K* bispectrum components. For the purposes of handling contributions to force, virial, and quadratic combinations, these [\\(N\_{elem}\^3\\)]{.math .notranslate .nohighlight} sub-blocks are treated as a single block of [\\(K N\_{elem}\^3\\)]{.math .notranslate .nohighlight} columns.

If the *bik* keyword is set to 1, the structure of the snap array is expanded. The first [\\(N\\)]{.math .notranslate .nohighlight} rows of the snap array correspond to [\\(B\_{i,k}\\)]{.math .notranslate .nohighlight} instead of a single row summed over atoms [\\(i\\)]{.math .notranslate .nohighlight}. In this case, the entries in the final column for these rows are set to zero. Also, each row contains only non-zero entries for the columns corresponding to the type of that atom. This is not true in the case of *dgradflag* keyword = 1 (see below).

If the *dgradflag* keyword is set to 1, this changes the structure of the global array completely. Here the *snad/atom* quantities are replaced with rows corresponding to descriptor gradient components on single atoms:

::: {.math .notranslate .nohighlight}
\\\[\\frac{\\partial {B\_{i,k} }}{\\partial {r}\^a_j}\\\]
:::

where [\\({r}\^a_j\\)]{.math .notranslate .nohighlight} is the *a-th* position coordinate of the atom with global index *j*. The rows are organized in chunks, where each chunk corresponds to an atom with global index [\\(j\\)]{.math .notranslate .nohighlight}. The rows in an atom [\\(j\\)]{.math .notranslate .nohighlight} chunk correspond to atoms with global index [\\(i\\)]{.math .notranslate .nohighlight}. The total number of rows for these descriptor gradients is therefore [\\(3N\^2\\)]{.math .notranslate .nohighlight}. The number of columns is equal to the number of bispectrum components, plus 3 additional left-most columns representing the global atom indices [\\(i\\)]{.math .notranslate .nohighlight}, [\\(j\\)]{.math .notranslate .nohighlight}, and Cartesian direction [\\(a\\)]{.math .notranslate .nohighlight} (0, 1, 2, for x, y, z). The first 3 columns of the first [\\(N\\)]{.math .notranslate .nohighlight} rows belong to the reference potential force components. The remaining K columns contain the [\\(B\_{i,k}\\)]{.math .notranslate .nohighlight} per-atom descriptors corresponding to the non-zero entries obtained when *bikflag* = 1. The first column of the last row, after the first [\\(N + 3N\^2\\)]{.math .notranslate .nohighlight} rows, contains the reference potential energy. The virial components are not used with this option. The total number of rows is therefore [\\(N + 3N\^2 + 1\\)]{.math .notranslate .nohighlight} and the number of columns is [\\(K + 3\\)]{.math .notranslate .nohighlight}.

These values can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options. To see how this command can be used within a Python workflow to train SNAP potentials, see the examples in [FitSNAP](https://github.com/FitSNAP/FitSNAP){.reference .external}.
:::::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These computes are part of the ML-SNAP package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style snap]{.doc}]pair_snap.md){.reference .internal} [[compute slcsa/atom]{.doc}]compute_slcsa_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The optional keyword defaults are *rmin0* = 0, *switchflag* = 1, *bzeroflag* = 1, *quadraticflag* = 0, *bnormflag* = 0, *wselfallflag* = 0, *switchinnerflag* = 0, *nnn* = -1, *wmode* = 0, *delta* = 1.e-3

------------------------------------------------------------------------

**(Thompson)** Thompson, Swiler, Trott, Foiles, Tucker, J Comp Phys, 285, 316, (2015).

**(Bartok)** Bartok, Payne, Risi, Csanyi, Phys Rev Lett, 104, 136403 (2010).

**(Meremianin)** Meremianin, J. Phys. A, 39, 3099 (2006).

**(Varshalovich)** Varshalovich, Moskalev, Khersonskii, Quantum Theory of Angular Momentum, World Scientific, Singapore (1987).

**(Mason)** J. K. Mason, Acta Cryst A65, 259 (2009).

**(Cusentino)** Cusentino, Wood, Thompson, J Phys Chem A, 124, 5456, (2020)

**(Ellis)** Ellis, Fiedler, Popoola, Modine, Stephens, Thompson, Cangi, Rajamanickam, [Phys. Rev. B, 104, 035120, (2021)](https://doi.org/10.1103/PhysRevB.104.035120){.reference .external}

**(Lafourcade)** Lafourcade, Maillet, Denoual, Duval, Allera, Goryaeva, and Marinica, [Comp. Mat. Science, 230, 112534 (2023)](https://doi.org/10.1016/j.commatsci.2023.112534){.reference .external}
:::
:::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

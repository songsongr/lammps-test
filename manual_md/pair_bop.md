:::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::: {#pair-style-bop-command .section}
[]{#index-0}

# pair_style bop command[](#pair-style-bop-command "Link to this heading"){.headerlink}

::::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style bop keyword ...
:::
::::

- zero or more keywords may be appended

- keyword = *save*

:::: {.highlight-none .notranslate}
::: highlight
    save = pre-compute and save some values
:::
::::
:::::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style bop
    pair_coeff * * ../potentials/CdTe_bop Cd Te
    pair_style bop save
    pair_coeff * * ../potentials/CdTe.bop.table Cd Te Te
    comm_modify cutoff 14.70
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *bop* pair style computes Bond-Order Potentials (BOP) based on quantum mechanical theory incorporating both [\\(\\sigma\\)]{.math .notranslate .nohighlight} and [\\(\\pi\\)]{.math .notranslate .nohighlight} bonding. By analytically deriving the BOP from quantum mechanical theory its transferability to different phases can approach that of quantum mechanical methods. This potential is similar to the original BOP developed by Pettifor ([[Pettifor_1]{.std .std-ref}](#pettifor-1){.reference .internal}, [[Pettifor_2]{.std .std-ref}](#pettifor-2){.reference .internal}, [[Pettifor_3]{.std .std-ref}](#pettifor-3){.reference .internal}) and later updated by Murdick, Zhou, and Ward ([[Murdick]{.std .std-ref}](#murdick){.reference .internal}, [[Ward]{.std .std-ref}](#ward){.reference .internal}). Currently, BOP potential files for these systems are provided with LAMMPS: AlCu, CCu, CdTe, CdTeSe, CdZnTe, CuH, GaAs. A system with only a subset of these elements, including a single element (e.g. C or Cu or Al or Ga or Zn or CdZn), can also be modeled by using the appropriate alloy file and assigning all atom types to the single element or subset of elements via the [[pair_coeff command]{.doc}]pair_coeff.md){.reference .internal}, as discussed below.

The BOP potential consists of three terms:

::: {.math .notranslate .nohighlight}
\\\[E = \\frac{1}{2} \\sum\_{i=1}\^{N} \\sum\_{j=i_1}\^{i_N} \\phi\_{ij} \\left( r\_{ij} \\right) - \\sum\_{i=1}\^{N} \\sum\_{j=i_1}\^{i_N} \\beta\_{\\sigma,ij} \\left( r\_{ij} \\right) \\cdot \\Theta\_{\\sigma,ij} - \\sum\_{i=1}\^{N} \\sum\_{j=i_1}\^{i_N} \\beta\_{\\pi,ij} \\left( r\_{ij} \\right) \\cdot \\Theta\_{\\pi,ij} + U\_{prom}\\\]
:::

where [\\(\\phi\_{ij}(r\_{ij})\\)]{.math .notranslate .nohighlight} is a short-range two-body function representing the repulsion between a pair of ion cores, [\\(\\beta\_{\\sigma,ij}(r\_{ij})\\)]{.math .notranslate .nohighlight} and [\\(\\beta\_{\\sigma,ij}(r\_{ij})\\)]{.math .notranslate .nohighlight} are respectively sigma and [\\(\\pi\\)]{.math .notranslate .nohighlight} bond integrals, [\\(\\Theta\_{\\sigma,ij}\\)]{.math .notranslate .nohighlight} and [\\(\\Theta\_{\\pi,ij}\\)]{.math .notranslate .nohighlight} are [\\(\\sigma\\)]{.math .notranslate .nohighlight} and [\\(\\pi\\)]{.math .notranslate .nohighlight} bond-orders, and U_prom is the promotion energy for sp-valent systems.

The detailed formulas for this potential are given in Ward ([[Ward]{.std .std-ref}](#ward){.reference .internal}); here we provide only a brief description.

The repulsive energy [\\(\\phi\_{ij}(r\_{ij})\\)]{.math .notranslate .nohighlight} and the bond integrals [\\(\\beta\_{\\sigma,ij}(r\_{ij})\\)]{.math .notranslate .nohighlight} and [\\(\\beta\_{\\phi,ij}(r\_{ij})\\)]{.math .notranslate .nohighlight} are functions of the interatomic distance [\\(r\_{ij}\\)]{.math .notranslate .nohighlight} between atom *i* and *j*. Each of these potentials has a smooth cutoff at a radius of [\\(r\_{cut,ij}\\)]{.math .notranslate .nohighlight}. These smooth cutoffs ensure stable behavior at situations with high sampling near the cutoff such as melts and surfaces.

The bond-orders can be viewed as environment-dependent local variables that are ij bond specific. The maximum value of the [\\(\\sigma\\)]{.math .notranslate .nohighlight} bond-order ([\\(\\Theta\_{\\sigma}\\)]{.math .notranslate .nohighlight} is 1, while that of the [\\(\\pi\\)]{.math .notranslate .nohighlight} bond-order ([\\(\\Theta\_{\\pi}\\)]{.math .notranslate .nohighlight}) is 2, attributing to a maximum value of the total bond-order ([\\(\\Theta\_{\\sigma}+\\Theta\_{\\pi}\\)]{.math .notranslate .nohighlight}) of 3. The [\\(\\sigma\\)]{.math .notranslate .nohighlight} and [\\(\\pi\\)]{.math .notranslate .nohighlight} bond-orders reflect the ubiquitous single-, double-, and triple- bond behavior of chemistry. Their analytical expressions can be derived from tight- binding theory by recursively expanding an inter-site Green's function as a continued fraction. To accurately represent the bonding with a computationally efficient potential formulation suitable for MD simulations, the derived BOP only takes (and retains) the first two levels of the recursive representations for both the [\\(\\sigma\\)]{.math .notranslate .nohighlight} and the [\\(\\pi\\)]{.math .notranslate .nohighlight} bond-orders. Bond-order terms can be understood in terms of molecular orbital hopping paths based upon the Cyrot-Lackmann theorem ([[Pettifor_1]{.std .std-ref}](#pettifor-1){.reference .internal}). The [\\(\\sigma\\)]{.math .notranslate .nohighlight} bond-order with a half-full valence shell is used to interpolate the bond-order expression that incorporated explicit valance band filling. This [\\(\\pi\\)]{.math .notranslate .nohighlight} bond-order expression also contains also contains a three-member ring term that allows implementation of an asymmetric density of states, which helps to either stabilize or destabilize close-packed structures. The [\\(\\pi\\)]{.math .notranslate .nohighlight} bond-order includes hopping paths of length 4. This enables the incorporation of dihedral angles effects.

::: {.admonition .note}
Note

Note that unlike for other potentials, cutoffs for BOP potentials are not set in the pair_style or pair_coeff command; they are specified in the BOP potential files themselves. Likewise, the BOP potential files list atomic masses; thus you do not need to use the [[mass]{.doc}]mass.md){.reference .internal} command to specify them. Note that for BOP potentials with hydrogen, you will likely want to set the mass of H atoms to be 10x or 20x larger to avoid having to use a tiny timestep. You can do this by using the [[mass]{.doc}]mass.md){.reference .internal} command after using the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command to read the BOP potential file.
:::

One option can be specified as a keyword with the pair_style command.

The *save* keyword gives you the option to calculate in advance and store a set of distances, angles, and derivatives of angles. The default is to not do this, but to calculate them on-the-fly each time they are needed. The former may be faster, but takes more memory. The latter requires less memory, but may be slower. It is best to test this option to optimize the speed of BOP for your particular system configuration.

------------------------------------------------------------------------

Only a single pair_coeff command is used with the *bop* style which specifies a BOP potential file, with parameters for all needed elements. These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- N element names = mapping of BOP elements to atom types

As an example, imagine the CdTe.bop file has BOP values for Cd and Te. If your LAMMPS simulation has 4 atoms types and you want the first 3 to be Cd, and the fourth to be Te, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * CdTe Cd Cd Cd Te
:::
::::

The first 2 arguments must be \* \* so as to span all LAMMPS atom types. The first three Cd arguments map LAMMPS atom types 1,2,3 to the Cd element in the BOP file. The final Te argument maps LAMMPS atom type 4 to the Te element in the BOP file.

BOP files in the *potentials* directory of the LAMMPS distribution have a ".bop" suffix. The potentials are in tabulated form containing pre-tabulated pair functions for phi_ij(r_ij), beta\_(sigma,ij)(r_ij), and beta_pi,ij)(r_ij).

The parameters/coefficients format for the different kinds of BOP files are given below with variables matching the formulation of Ward ([[Ward]{.std .std-ref}](#ward){.reference .internal}) and Zhou ([[Zhou]{.std .std-ref}](#zhou1){.reference .internal}). Each header line containing a ":" is preceded by a blank line.

------------------------------------------------------------------------

**No angular table file format**:

The parameters/coefficients format for the BOP potentials input file containing pre-tabulated functions of g is given below with variables matching the formulation of Ward ([[Ward]{.std .std-ref}](#ward){.reference .internal}). This format also assumes the angular functions have the formulation of ([[Ward]{.std .std-ref}](#ward){.reference .internal}).

- Line 1: \# elements N

The first line is followed by N lines containing the atomic number, mass, and element symbol of each element.

Following the definition of the elements several global variables for the tabulated functions are given.

- Line 1: nr, nBOt (nr is the number of divisions the radius is broken into for function tables and MUST be a factor of 5; nBOt is the number of divisions for the tabulated values of THETA\_(S,ij)

- Line 2: delta_1-delta_7 (if all are not used in the particular

- formulation, set unused values to 0.0)

Following this N lines for e_1-e_N containing p_pi.

- Line 3: p_pi (for e_1)

- Line 4: p_pi (for e_2 and continues to e_N)

The next section contains several pair constants for the number of interaction types e_i-e_j, with i=1-\>N, j=i-\>N

- Line 1: r_cut (for e_1-e_1 interactions)

- Line 2: c_sigma, a_sigma, c_pi, a_pi

- Line 3: delta_sigma, delta_pi

- Line 4: f_sigma, k_sigma, delta_3 (This delta_3 is similar to that of the previous section but is interaction type dependent)

The next section contains a line for each three body interaction type e_j-e_i-e_k with i=0-\>N, j=0-\>N, k=j-\>N

- Line 1: g\_(sigma0), g\_(sigma1), g\_(sigma2) (These are coefficients for g\_(sigma,jik)(THETA_ijk) for e_1-e_1-e_1 interaction. [[Ward]{.std .std-ref}](#ward){.reference .internal} contains the full expressions for the constants as functions of b\_(sigma,ijk), p\_(sigma,ijk), u\_(sigma,ijk))

- Line 2: g\_(sigma0), g\_(sigma1), g\_(sigma2) (for e_1-e_1-e_2)

The next section contains a block for each interaction type for the phi_ij(r_ij). Each block has nr entries with 5 entries per line.

- Line 1: phi(r1), phi(r2), phi(r3), phi(r4), phi(r5) (for the e_1-e_1 interaction type)

- Line 2: phi(r6), phi(r7), phi(r8), phi(r9), phi(r10) (this continues until nr)

- ...

- Line nr/5_1: phi(r1), phi(r2), phi(r3), phi(r4), phi(r5), (for the e_1-e_1 interaction type)

The next section contains a block for each interaction type for the beta\_(sigma,ij)(r_ij). Each block has nr entries with 5 entries per line.

- Line 1: beta_sigma(r1), beta_sigma(r2), beta_sigma(r3), beta_sigma(r4), beta_sigma(r5) (for the e_1-e_1 interaction type)

- Line 2: beta_sigma(r6), beta_sigma(r7), beta_sigma(r8), beta_sigma(r9), beta_sigma(r10) (this continues until nr)

- ...

- Line nr/5+1: beta_sigma(r1), beta_sigma(r2), beta_sigma(r3), beta_sigma(r4), beta_sigma(r5) (for the e_1-e_2 interaction type)

The next section contains a block for each interaction type for beta\_(pi,ij)(r_ij). Each block has nr entries with 5 entries per line.

- Line 1: beta_pi(r1), beta_pi(r2), beta_pi(r3), beta_pi(r4), beta_pi(r5) (for the e_1-e_1 interaction type)

- Line 2: beta_pi(r6), beta_pi(r7), beta_pi(r8), beta_pi(r9), beta_pi(r10) (this continues until nr)

- ...

- Line nr/5+1: beta_pi(r1), beta_pi(r2), beta_pi(r3), beta_pi(r4), beta_pi(r5) (for the e_1-e_2 interaction type)

The next section contains a block for each interaction type for the THETA\_(S,ij)((THETA\_(sigma,ij))\^(1/2), f\_(sigma,ij)). Each block has nBOt entries with 5 entries per line.

- Line 1: THETA\_(S,ij)(r1), THETA\_(S,ij)(r2), THETA\_(S,ij)(r3), THETA\_(S,ij)(r4), THETA\_(S,ij)(r5) (for the e_1-e_2 interaction type)

- Line 2: THETA\_(S,ij)(r6), THETA\_(S,ij)(r7), THETA\_(S,ij)(r8), THETA\_(S,ij)(r9), THETA\_(S,ij)(r10) (this continues until nBOt)

- ...

- Line nBOt/5+1: THETA\_(S,ij)(r1), THETA\_(S,ij)(r2), THETA\_(S,ij)(r3), THETA\_(S,ij)(r4), THETA\_(S,ij)(r5) (for the e_1-e_2 interaction type)

The next section contains a block of N lines for e_1-e_N

- Line 1: delta\^mu (for e_1)

- Line 2: delta\^mu (for e_2 and repeats to e_N)

The last section contains more constants for e_i-e_j interactions with i=0-\>N, j=i-\>N

- Line 1: (A_ij)\^(mu\*nu) (for e1-e1)

- Line 2: (A_ij)\^(mu\*nu) (for e1-e2 and repeats as above)

------------------------------------------------------------------------

**Angular spline table file format**:

The parameters/coefficients format for the BOP potentials input file containing pre-tabulated functions of g is given below with variables matching the formulation of Ward ([[Ward]{.std .std-ref}](#ward){.reference .internal}). This format also assumes the angular functions have the formulation of ([[Zhou]{.std .std-ref}](#zhou1){.reference .internal}).

- Line 1: \# elements N

The first line is followed by N lines containing the atomic number, mass, and element symbol of each element.

Following the definition of the elements several global variables for the tabulated functions are given.

- Line 1: nr, ntheta, nBOt (nr is the number of divisions the radius is broken into for function tables and MUST be a factor of 5; ntheta is the power of the power of the spline used to fit the angular function; nBOt is the number of divisions for the tabulated values of THETA\_(S,ij)

- Line 2: delta_1-delta_7 (if all are not used in the particular

- formulation, set unused values to 0.0)

Following this N lines for e_1-e_N containing p_pi.

- Line 3: p_pi (for e_1)

- Line 4: p_pi (for e_2 and continues to e_N)

The next section contains several pair constants for the number of interaction types e_i-e_j, with i=1-\>N, j=i-\>N

- Line 1: r_cut (for e_1-e_1 interactions)

- Line 2: c_sigma, a_sigma, c_pi, a_pi

- Line 3: delta_sigma, delta_pi

- Line 4: f_sigma, k_sigma, delta_3 (This delta_3 is similar to that of the previous section but is interaction type dependent)

The next section contains a line for each three body interaction type e_j-e_i-e_k with i=0-\>N, j=0-\>N, k=j-\>N

- Line 1: g0, g1, g2... (These are coefficients for the angular spline of the g\_(sigma,jik)(THETA_ijk) for e_1-e_1-e_1 interaction. The function can contain up to 10 term thus 10 constants. The first line can contain up to five constants. If the spline has more than five terms the second line will contain the remaining constants The following lines will then contain the constants for the remaining g0, g1, g2... (for e_1-e_1-e_2) and the other three body interactions

The rest of the table has the same structure as the previous section (see above).

------------------------------------------------------------------------

**Angular no-spline table file format**:

The parameters/coefficients format for the BOP potentials input file containing pre-tabulated functions of g is given below with variables matching the formulation of Ward ([[Ward]{.std .std-ref}](#ward){.reference .internal}). This format also assumes the angular functions have the formulation of ([[Zhou]{.std .std-ref}](#zhou1){.reference .internal}).

- Line 1: \# elements N

The first two lines are followed by N lines containing the atomic number, mass, and element symbol of each element.

Following the definition of the elements several global variables for the tabulated functions are given.

- Line 1: nr, ntheta, nBOt (nr is the number of divisions the radius is broken into for function tables and MUST be a factor of 5; ntheta is the number of divisions for the tabulated values of the g angular function; nBOt is the number of divisions for the tabulated values of THETA\_(S,ij)

- Line 2: delta_1-delta_7 (if all are not used in the particular

- formulation, set unused values to 0.0)

Following this N lines for e_1-e_N containing p_pi.

- Line 3: p_pi (for e_1)

- Line 4: p_pi (for e_2 and continues to e_N)

The next section contains several pair constants for the number of interaction types e_i-e_j, with i=1-\>N, j=i-\>N

- Line 1: r_cut (for e_1-e_1 interactions)

- Line 2: c_sigma, a_sigma, c_pi, a_pi

- Line 3: delta_sigma, delta_pi

- Line 4: f_sigma, k_sigma, delta_3 (This delta_3 is similar to that of the previous section but is interaction type dependent)

The next section contains a line for each three body interaction type e_j-e_i-e_k with i=0-\>N, j=0-\>N, k=j-\>N

- Line 1: g(theta1), g(theta2), g(theta3), g(theta4), g(theta5) (for the e_1-e_1-e_1 interaction type)

- Line 2: g(theta6), g(theta7), g(theta8), g(theta9), g(theta10) (this continues until ntheta)

- ...

- Line ntheta/5+1: g(theta1), g(theta2), g(theta3), g(theta4), g(theta5), (for the e_1-e_1-e_2 interaction type)

The rest of the table has the same structure as the previous section (see above).
:::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} mix, shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the MANYBODY package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

These pair potentials require the [[newtion]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

Pair style bop is not compatible with being used as a sub-style with doc:hybrid pair styles \<pair_hybrid\>. Pair style bop is also not compatible with [[multi-cutoff neighbor lists]{.doc}]neighbor.md){.reference .internal} or [[multi-cutoff communitcation]{.doc}]comm_modify.md){.reference .internal}.

The .bop.table potential files provided with LAMMPS (see the potentials directory) are parameterized for metal [[units]{.doc}]units.md){.reference .internal}. You can use the BOP potential with any LAMMPS units, but you would need to create your own BOP potential file with coefficients listed in the appropriate units if your simulation does not use "metal" units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

non-tabulated potential file, a_0 is non-zero.

------------------------------------------------------------------------

**(Pettifor_1)** D.G. Pettifor and I.I. Oleinik, Phys. Rev. B, 59, 8487 (1999).

**(Pettifor_2)** D.G. Pettifor and I.I. Oleinik, Phys. Rev. Lett., 84, 4124 (2000).

**(Pettifor_3)** D.G. Pettifor and I.I. Oleinik, Phys. Rev. B, 65, 172103 (2002).

**(Murdick)** D.A. Murdick, X.W. Zhou, H.N.G. Wadley, D. Nguyen-Manh, R. Drautz, and D.G. Pettifor, Phys. Rev. B, 73, 45206 (2006).

**(Ward)** D.K. Ward, X.W. Zhou, B.M. Wong, F.P. Doty, and J.A. Zimmerman, Phys. Rev. B, 85,115206 (2012).

**(Zhou)** X.W. Zhou, D.K. Ward, M. Foster (TBP).
:::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::

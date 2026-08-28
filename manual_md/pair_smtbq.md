::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#pair-style-smtbq-command .section}
[]{#index-0}

# pair_style smtbq command[](#pair-style-smtbq-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style smtbq
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style smtbq
    pair_coeff * * ffield.smtbq.Al2O3 O Al
:::
::::
:::::

::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This pair style computes a variable charge SMTB-Q (Second-Moment tight-Binding QEq) potential as described in [[SMTB-Q_1]{.std .std-ref}](#smtb-q-1){.reference .internal} and [[SMTB-Q_2]{.std .std-ref}](#smtb-q-2){.reference .internal}. This potential was first proposed in [[SMTB-Q_0]{.std .std-ref}](#smtb-q-0){.reference .internal}. Briefly, the energy of metallic-oxygen systems is given by three contributions:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E\_{tot} & = E\_{ES} + E\_{OO} + E\_{MO} \\\\ E\_{ES} & = \\sum_i{\\biggl\[ \\chi\_{i}\^{0}Q_i + \\frac{1}{2}J\_{i}\^{0}Q\_{i}\^{2} + \\frac{1}{2} \\sum\_{j\\neq i}{ J\_{ij}(r\_{ij})f\_{cut}\^{R\_{coul}}(r\_{ij})Q_i Q_j } \\biggr\] } \\\\ E\_{OO} & = \\sum\_{i,j}\^{i,j = O}{\\biggl\[Cexp( -\\frac{r\_{ij}}{\\rho} ) - Df\_{cut}\^{r_1\^{OO}r_2\^{OO}}(r\_{ij}) exp(Br\_{ij})\\biggr\]} \\\\ E\_{MO} & = \\sum_i{E\_{cov}\^{i} + \\sum\_{j\\neq i}{ Af\_{cut}\^{r\_{c1}r\_{c2}}(r\_{ij})exp\\bigl\[-p(\\frac{r\_{ij}}{r_0} -1) \\bigr\] } }\\end{split}\\\]
:::

where [\\(E\_{tot}\\)]{.math .notranslate .nohighlight} is the total potential energy of the system, [\\(E\_{ES}\\)]{.math .notranslate .nohighlight} is the electrostatic part of the total energy, [\\(E\_{OO}\\)]{.math .notranslate .nohighlight} is the interaction between oxygen atoms and [\\(E\_{MO}\\)]{.math .notranslate .nohighlight} is a short-range interaction between metal and oxygen atoms. This interactions depend on interatomic distance [\\(r\_{ij}\\)]{.math .notranslate .nohighlight} and/or the charge [\\(Q\_{i}\\)]{.math .notranslate .nohighlight} of atoms *i*. Cut-off function enables smooth convergence to zero interaction.

The parameters appearing in the upper expressions are set in the ffield.SMTBQ.Syst file where Syst corresponds to the selected system (e.g. field.SMTBQ.Al2O3). Examples for [\\(\\mathrm{TiO_2}\\)]{.math .notranslate .nohighlight}, [\\(\\mathrm{Al_2O_3}\\)]{.math .notranslate .nohighlight} are provided. A single pair_coeff command is used with the SMTBQ styles which provides the path to the potential file with parameters for needed elements. These are mapped to LAMMPS atom types by specifying additional arguments after the potential filename in the pair_coeff command. Note that atom type 1 must always correspond to oxygen atoms. As an example, to simulate a [\\(\\mathrm{TiO_2}\\)]{.math .notranslate .nohighlight} system, atom type 1 has to be oxygen and atom type 2 Ti. The following pair_coeff command should then be used:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * PathToLammps/potentials/ffield.smtbq.TiO2 O Ti
:::
::::

The electrostatic part of the energy consists of two components

self-energy of atom *i* in the form of a second order charge dependent polynomial and a long-range Coulombic electrostatic interaction. The latter uses the wolf summation method described in [[Wolf]{.std .std-ref}](#wolf2){.reference .internal}, spherically truncated at a longer cutoff, [\\(R\_{coul}\\)]{.math .notranslate .nohighlight}. The charge of each ion is modeled by an orbital Slater which depends on the principal quantum number (*n*) of the outer orbital shared by the ion.

Interaction between oxygen, [\\(E\_{OO}\\)]{.math .notranslate .nohighlight}, consists of two parts, an attractive and a repulsive part. The attractive part is effective only at short range (\< [\\(r_2\^{OO}\\)]{.math .notranslate .nohighlight}). The attractive contribution was optimized to study surfaces reconstruction (e.g. [[SMTB-Q_2]{.std .std-ref}](#smtb-q-2){.reference .internal} in [\\(\\mathrm{TiO_2}\\)]{.math .notranslate .nohighlight}) and is not necessary for oxide bulk modeling. The repulsive part is the Pauli interaction between the electron clouds of oxygen. The Pauli repulsion and the coulombic electrostatic interaction have same cut off value. In the ffield.SMTBQ.Syst, the keyword *'buck'* allows to consider only the repulsive O-O interactions. The keyword *'buckPlusAttr'* allows to consider the repulsive and the attractive O-O interactions.

The short-range interaction between metal-oxygen, [\\(E\_{MO}\\)]{.math .notranslate .nohighlight} is based on the second moment approximation of the density of states with a N-body potential for the band energy term, [\\(E\^i\_{cov}\\)]{.math .notranslate .nohighlight}, and a Born-Mayer type repulsive terms as indicated by the keyword *'second_moment'* in the ffield.SMTBQ.Syst. The energy band term is given by:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E\_{cov}\^{i(i=M,O)} & = - \\biggl\\{\\eta_i(\\mu \\xi\^{0})\^2 f\_{cut}\^{r\_{c1}r\_{c2}}(r\_{ij}) \\biggl( \\sum\_{j(j=O,M)}{ exp\[ -2q(\\frac{r\_{ij}}{r_0} - 1)\] } \\biggr) \\delta Q_i \\bigl( 2\\frac{n_0}{\\eta_i} - \\delta Q_i \\bigr) \\biggr\\}\^{1/2} \\\\ \\delta Q_i & = \| Q_i\^{F} \| - \| Q_i \|\\end{split}\\\]
:::

where [\\(\\eta_i\\)]{.math .notranslate .nohighlight} is the stoichiometry of atom *i*, [\\(\\delta Q_i\\)]{.math .notranslate .nohighlight} is the charge delocalization of atom *i*, compared to its formal charge [\\(Q\^F_i\\)]{.math .notranslate .nohighlight}. [\\(n_0\\)]{.math .notranslate .nohighlight}, the number of hybridized orbitals, is calculated with to the atomic orbitals shared [\\(d_i\\)]{.math .notranslate .nohighlight} and the stoichiometry [\\(\\eta_i\\)]{.math .notranslate .nohighlight}. [\\(r\_{c1}\\)]{.math .notranslate .nohighlight} and [\\(r\_{c2}\\)]{.math .notranslate .nohighlight} are the two cutoff radius around the fourth neighbors in the cutoff function.

In the formalism used here, [\\(\\xi\^0\\)]{.math .notranslate .nohighlight} is the energy parameter. [\\(\\xi\^0\\)]{.math .notranslate .nohighlight} is in tight-binding approximation the hopping integral between the hybridized orbitals of the cation and the anion. In the literature we find many ways to write the hopping integral depending on whether one takes the point of view of the anion or cation. These are equivalent vision. The correspondence between the two visions is explained in appendix A of the article in the SrTiO3 [[SMTB-Q_3]{.std .std-ref}](#smtb-q-3){.reference .internal} (parameter [\\(\\beta\\)]{.math .notranslate .nohighlight} shown in this article is in fact the [\\(\\beta_O\\)]{.math .notranslate .nohighlight}). To summarize the relationship between the hopping integral [\\(\\xi\^O\\)]{.math .notranslate .nohighlight} and the others, we have in an oxide [\\(\\mathrm{C_n O_m}\\)]{.math .notranslate .nohighlight} the following relationship:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\xi\^0 & = \\frac{\\xi_O}{m} = \\frac{\\xi_C}{n} \\\\ \\frac{\\beta_O}{\\sqrt{m}} & = \\frac{\\beta_C}{\\sqrt{n}} = \\xi\^0 \\frac{\\sqrt{m}+\\sqrt{n}}{2}\\end{split}\\\]
:::

Thus parameter [\\(\\mu\\)]{.math .notranslate .nohighlight}, indicated above, is given by [\\(\\mu = \\frac{1}{2}(\\sqrt{n}+\\sqrt{m})\\)]{.math .notranslate .nohighlight}

The potential offers the possibility to consider the polarizability of the electron clouds of oxygen by changing the slater radius of the charge density around the oxygen atoms through the parameters *rBB, rB and rS* in the ffield.SMTBQ.Syst. This change in radius is performed according to the method developed by E. Maras [[SMTB-Q_2]{.std .std-ref}](#smtb-q-2){.reference .internal}. This method needs to determine the number of nearest neighbors around the oxygen. This calculation is based on first ([\\(r\_{1n}\\)]{.math .notranslate .nohighlight}) and second ([\\(r\_{2n}\\)]{.math .notranslate .nohighlight}) distances neighbors.

The SMTB-Q potential is a variable charge potential. The equilibrium charge on each atom is calculated by the electronegativity equalization (QEq) method. See [[Rick]{.std .std-ref}](#rick3){.reference .internal} for further detail. One can adjust the frequency, the maximum number of iterative loop and the convergence of the equilibrium charge calculation. To obtain the energy conservation in NVE thermodynamic ensemble, we recommend to use a convergence parameter in the interval 10e-5 - 10e-6 eV.

The ffield.SMTBQ.Syst files are provided for few systems. They consist of nine parts and the lines beginning with '#' are comments (note that the number of comment lines matter). The first sections are on the potential parameters and others are on the simulation options and might be modified. Keywords are character type and must be enclosed in quotation marks ('').

1.  Number of different element in the oxide:

- N_elem= 2 or 3

- Divider line

2.  Atomic parameters

For the anion (oxygen)

- Name of element (char) and stoichiometry in oxide

- Formal charge and mass of element

- Principal quantum number of outer orbital n), electronegativity ([\\(\\chi\^0_i\\)]{.math .notranslate .nohighlight}) and hardness ([\\(J\^0_i\\)]{.math .notranslate .nohighlight})

- Ionic radius parameters : max coordination number (*coordBB* = 6 by default), bulk coordination number *(coordB)*, surface coordination number *(coordS)* and *rBB, rB and rS* the slater radius for each coordination number. (**note : If you don't want to change the slater radius, use three identical radius values**)

- Number of orbital shared by the element in the oxide ([\\(d_i\\)]{.math .notranslate .nohighlight})

- Divider line

For each cations (metal):

- Name of element (char) and stoichiometry in oxide

- Formal charge and mass of element

- Number of electron in outer orbital *(ne)*, electronegativity ([\\(\\chi\^0_i\\)]{.math .notranslate .nohighlight}), hardness ([\\(J\^0_i\\)]{.math .notranslate .nohighlight}) and [\\(r\_{Slater}\\)]{.math .notranslate .nohighlight} the slater radius for the cation.

- Number of orbitals shared by the elements in the oxide ([\\(d_i\\)]{.math .notranslate .nohighlight})

- Divider line

3.  Potential parameters:

- Keyword for element1, element2 and interaction potential ('second_moment' or 'buck' or 'buckPlusAttr') between element 1 and 2. If the potential is 'second_moment', specify 'oxide' or 'metal' for metal-oxygen or metal-metal interactions respectively.

- Potential parameter:

  - If type of potential is 'second_moment' : A (eV), *p*, [\\(\\zeta\^0\\)]{.math .notranslate .nohighlight} (eV) and *q*, [\\(r\_{c1} (\\AA)\\)]{.math .notranslate .nohighlight}, [\\(r\_{c2} (\\AA)\\)]{.math .notranslate .nohighlight} and [\\(r_0 (\\AA)\\)]{.math .notranslate .nohighlight}

  - If type of potential is 'buck' : *C* (eV) and [\\(\\rho (\\AA)\\)]{.math .notranslate .nohighlight}

  - If type of potential is 'buckPlusAttr' : *C* (eV) and [\\(\\rho (\\AA)\\)]{.math .notranslate .nohighlight} *D* (eV), *B* [\\((\\AA\^{-1})\\)]{.math .notranslate .nohighlight}, [\\(r\^{OO}\_1 (\\AA)\\)]{.math .notranslate .nohighlight} and [\\(r\^{OO}\_2 (\\AA)\\)]{.math .notranslate .nohighlight}

- Divider line

4.  Tables parameters:

- Cutoff radius for the Coulomb interaction ([\\(R\_{coul}\\)]{.math .notranslate .nohighlight})

- Starting radius ([\\(r\_{min} = 1,18845 \\AA\\)]{.math .notranslate .nohighlight}) and increments ([\\(dr = 0.001 \\AA\\)]{.math .notranslate .nohighlight}) for creating the potential table.

- Divider line

5.  Rick model parameter:

- *Nevery* : parameter to set the frequency of the charge resolution. The charges are evaluated each *Nevery* time steps.

- Max number of iterative loop (*loopmax*) and convergence criterion (*prec*) in eV of the charge resolution

- Divider line

6.  Coordination parameter:

- First ([\\(r\_{1n}\\)]{.math .notranslate .nohighlight}) and second ([\\(r\_{2n}\\)]{.math .notranslate .nohighlight}) neighbor distances in angstroms

- Divider line

7.  Charge initialization mode:

- Keyword (*QInitMode*) and initial oxygen charge ([\\(Q\_{init}\\)]{.math .notranslate .nohighlight}). If keyword = 'true', all oxygen charges are initially set equal to [\\(Q\_{init}\\)]{.math .notranslate .nohighlight}. The charges on the cations are initially set in order to respect the neutrality of the box. If keyword = 'false', all atom charges are initially set equal to 0 if you use the [[create_atoms]{.doc}]create_atoms.md){.reference .internal} command or the charge specified in the file structure using [[read_data]{.doc}]read_data.md){.reference .internal} command.

- Divider line

8.  Mode for the electronegativity equalization (Qeq)

- Keyword (*mode*) followed by:

  - QEqAll (one QEq group) \| no parameters

  - QEqAllParallel (several QEq groups) \| no parameters

  - Surface \| zlim (QEq only for z\>zlim)

- Parameter if necessary

- Divider line

9.  Verbose

- If you want the code to work in verbose mode or not : 'true' or 'false'

- If you want to print or not in the file 'Energy_component.txt' the three main contributions to the energy of the system according to the description presented above : 'true' or 'false' and [\\(N\_{Energy}\\)]{.math .notranslate .nohighlight}. This option writes to the file every [\\(N\_{Energy}\\)]{.math .notranslate .nohighlight} time steps. If the value is 'false' then [\\(N\_{Energy} = 0\\)]{.math .notranslate .nohighlight}. The file takes into account the possibility to have several QEq groups *g* then it writes: time step, number of atoms in group *g*, electrostatic part of energy, [\\(E\_{ES}\\)]{.math .notranslate .nohighlight}, the interaction between oxygen, [\\(E\_{OO}\\)]{.math .notranslate .nohighlight}, and short range metal-oxygen interaction, [\\(E\_{MO}\\)]{.math .notranslate .nohighlight}.

- If you want to print to the file 'Electroneg_component.txt' the electronegativity component ([\\(\\frac{\\partial E\_{tot}}{\\partial Q_i}\\)]{.math .notranslate .nohighlight}) or not: 'true' or 'false' and [\\(N\_{Electroneg}\\)]{.math .notranslate .nohighlight}. This option writes to the file every [\\(N\_{Electroneg}\\)]{.math .notranslate .nohighlight} time steps. If the value is 'false' then [\\(N\_{Electroneg} = 0\\)]{.math .notranslate .nohighlight}. The file consist of atom number *i*, atom type (1 for oxygen and \# higher than 1 for metal), atom position: *x*, *y* and *z*, atomic charge of atom *i*, electrostatic part of atom *i* electronegativity, covalent part of atom *i* electronegativity, the hopping integral of atom *i* [\\((Z\\beta\^2)\_i\\)]{.math .notranslate .nohighlight} and box electronegativity.

::: {.admonition .note}
Note

This last option slows down the calculation dramatically. Use only with a single processor simulation.
:::
:::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} mix, shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you needs to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the SMTBQ package and is only enabled if LAMMPS is built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This potential requires using atom type 1 for oxygen and atom type higher than 1 for metal atoms.

This pair style requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

The SMTB-Q potential files provided with LAMMPS (see the potentials directory) are parameterized for metal [[units]{.doc}]units.md){.reference .internal}.
:::

------------------------------------------------------------------------

::: {#citing-this-work .section}
## Citing this work[](#citing-this-work "Link to this heading"){.headerlink}

Please cite related publication: N. Salles, O. Politano, E. Amzallag and R. Tetot, Comput. Mater. Sci. 111 (2016) 181-189

------------------------------------------------------------------------

**(SMTB-Q_0)** A. Hallil, E. Amzallag, S. Landron, R. Tetot, Surface Science 605 738-745 (2011); R. Tetot, A. Hallil, J. Creuze and I. Braems, EPL, 83 40001 (2008)

**(SMTB-Q_1)** N. Salles, O. Politano, E. Amzallag, R. Tetot, Comput. Mater. Sci. 111 (2016) 181-189

**(SMTB-Q_2)** E. Maras, N. Salles, R. Tetot, T. Ala-Nissila, H. Jonsson, J. Phys. Chem. C 2015, 119, 10391-10399

**(SMTB-Q_3)** R. Tetot, N. Salles, S. Landron, E. Amzallag, Surface Science 616, 19-8722 28 (2013)

**(Wolf)** D. Wolf, P. Keblinski, S. R. Phillpot, J. Eggebrecht, J Chem Phys, 110, 8254 (1999).

**(Rick)** S. W. Rick, S. J. Stuart, B. J. Berne, J Chem Phys 101, 6141 (1994).
:::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

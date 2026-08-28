::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#compute-stress-atom-command .section}
[]{#index-1}[]{#index-0}

# compute stress/atom command[](#compute-stress-atom-command "Link to this heading"){.headerlink}
:::

:::::::::::::::::::::: {#compute-centroid-stress-atom-command .section}
# compute centroid/stress/atom command[](#compute-centroid-stress-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID style temp-ID keyword ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- style = *stress/atom* or *centroid/stress/atom*

- temp-ID = ID of compute that calculates temperature, can be NULL if not needed

- zero or more keywords may be appended

- keyword = *ke* or *pair* or *bond* or *angle* or *dihedral* or *improper* or *kspace* or *fix* or *virial*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 mobile stress/atom NULL
    compute 1 mobile stress/atom myRamp
    compute 1 all stress/atom NULL pair bond
    compute 1 all centroid/stress/atom NULL bond dihedral improper
:::
::::
:::::

::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that computes per-atom stress tensor for each atom in a group. In case of compute *stress/atom*, the tensor for each atom is symmetric with 6 components and is stored as a 6-element vector in the following order: [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}. In case of compute *centroid/stress/atom*, the tensor for each atom is asymmetric with 9 components and is stored as a 9-element vector in the following order: [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight}, [\\(yx\\)]{.math .notranslate .nohighlight}, [\\(zx\\)]{.math .notranslate .nohighlight}, [\\(zy\\)]{.math .notranslate .nohighlight}. See the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} command if you want the stress tensor (pressure) of the entire system.

The stress tensor for atom [\\(I\\)]{.math .notranslate .nohighlight} is given by the following formula, where [\\(a\\)]{.math .notranslate .nohighlight} and [\\(b\\)]{.math .notranslate .nohighlight} take on values [\\(x\\)]{.math .notranslate .nohighlight}, [\\(y\\)]{.math .notranslate .nohighlight}, [\\(z\\)]{.math .notranslate .nohighlight} to generate the components of the tensor:

::: {.math .notranslate .nohighlight}
\\\[S\_{ab} = - m v_a v_b - W\_{ab}\\\]
:::

The first term is a kinetic energy contribution for atom [\\(I\\)]{.math .notranslate .nohighlight}. See details below on how the specified *temp-ID* can affect the velocities used in this calculation. The second term is the virial contribution due to intra and intermolecular interactions, where the exact computation details are determined by the compute style.

In case of compute *stress/atom*, the virial contribution is:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split} W\_{ab} & = \\frac{1}{2} \\sum\_{n = 1}\^{N_p} (r\_{1_a} F\_{1_b} + r\_{2_a} F\_{2_b}) + \\frac{1}{2} \\sum\_{n = 1}\^{N_b} (r\_{1_a} F\_{1_b} + r\_{2_a} F\_{2_b}) \\\\ & + \\frac{1}{3} \\sum\_{n = 1}\^{N_a} (r\_{1_a} F\_{1_b} + r\_{2_a} F\_{2_b} + r\_{3_a} F\_{3_b}) + \\frac{1}{4} \\sum\_{n = 1}\^{N_d} (r\_{1_a} F\_{1_b} + r\_{2_a} F\_{2_b} + r\_{3_a} F\_{3_b} + r\_{4_a} F\_{4_b}) \\\\ & + \\frac{1}{4} \\sum\_{n = 1}\^{N_i} (r\_{1_a} F\_{1_b} + r\_{2_a} F\_{2_b} + r\_{3_a} F\_{3_b} + r\_{4_a} F\_{4_b}) + \\mathrm{Kspace}(r\_{i_a},F\_{i_b}) + \\sum\_{n = 1}\^{N_f} r\_{i_a} F\_{i_b}\\end{split}\\\]
:::

The first term is a pairwise energy contribution where [\\(n\\)]{.math .notranslate .nohighlight} loops over the [\\(N_p\\)]{.math .notranslate .nohighlight} neighbors of atom [\\(I\\)]{.math .notranslate .nohighlight}, [\\(\\mathbf{r}\_1\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{r}\_2\\)]{.math .notranslate .nohighlight} are the positions of the two atoms in the pairwise interaction, and [\\(\\mathbf{F}\_1\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{F}\_2\\)]{.math .notranslate .nohighlight} are the forces on the two atoms resulting from the pairwise interaction. The second term is a bond contribution of similar form for the [\\(N_b\\)]{.math .notranslate .nohighlight} bonds which atom [\\(I\\)]{.math .notranslate .nohighlight} is part of. There are similar terms for the [\\(N_a\\)]{.math .notranslate .nohighlight} angle, [\\(N_d\\)]{.math .notranslate .nohighlight} dihedral, and [\\(N_i\\)]{.math .notranslate .nohighlight} improper interactions atom [\\(I\\)]{.math .notranslate .nohighlight} is part of. There is also a term for the KSpace contribution from long-range Coulombic interactions, if defined. Finally, there is a term for the [\\(N_f\\)]{.math .notranslate .nohighlight} [[fixes]{.doc}]fix.md){.reference .internal} that apply internal constraint forces to atom [\\(I\\)]{.math .notranslate .nohighlight}. Currently, only the [[fix shake]{.doc}]fix_shake.md){.reference .internal} and [[fix rigid]{.doc}]fix_rigid.md){.reference .internal} commands contribute to this term. As the coefficients in the formula imply, a virial contribution produced by a small set of atoms (e.g. 4 atoms in a dihedral or 3 atoms in a Tersoff 3-body interaction) is assigned in equal portions to each atom in the set. E.g. 1/4 of the dihedral virial to each of the 4 atoms, or 1/3 of the fix virial due to SHAKE constraints applied to atoms in a water molecule via the [[fix shake]{.doc}]fix_shake.md){.reference .internal} command. As an exception, the virial contribution from constraint forces in [[fix rigid]{.doc}]fix_rigid.md){.reference .internal} on each atom is computed from the constraint force acting on the corresponding atom and its position, i.e. the total virial is not equally distributed.

In case of compute *centroid/stress/atom*, the virial contribution is:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split} W\_{ab} & = \\sum\_{n = 1}\^{N_p} r\_{I0_a} F\_{I_b} + \\sum\_{n = 1}\^{N_b} r\_{I0_a} F\_{I_b} + \\sum\_{n = 1}\^{N_a} r\_{I0_a} F\_{I_b} + \\sum\_{n = 1}\^{N_d} r\_{I0_a} F\_{I_b} + \\sum\_{n = 1}\^{N_i} r\_{I0_a} F\_{I_b} \\\\ & + \\mathrm{Kspace}(r\_{i_a},F\_{i_b}) + \\sum\_{n = 1}\^{N_f} r\_{i_a} F\_{i_b}\\end{split}\\\]
:::

As with compute *stress/atom*, the first, second, third, fourth and fifth terms are pairwise, bond, angle, dihedral and improper contributions, but instead of assigning the virial contribution equally to each atom, only the force [\\(\\mathbf{F}\_I\\)]{.math .notranslate .nohighlight} acting on atom [\\(I\\)]{.math .notranslate .nohighlight} due to the interaction and the relative position [\\(\\mathbf{r}\_{I0}\\)]{.math .notranslate .nohighlight} of the atom [\\(I\\)]{.math .notranslate .nohighlight} to the geometric center of the interacting atoms, i.e. centroid, is used. As the geometric center is different for each interaction, the [\\(\\mathbf{r}\_{I0}\\)]{.math .notranslate .nohighlight} also differs. The sixth term, Kspace contribution, is computed identically to compute *stress/atom*. The seventh term is handed differently depending on if the constraint forces are due to [[fix shake]{.doc}]fix_shake.md){.reference .internal} or [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}. In case of SHAKE constraints, each distance constraint is handed as a pairwise interaction. E.g. in case of a water molecule, two OH and one HH distance constraints are treated as three pairwise interactions. In case of [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}, all constraint forces in the molecule are treated as a single many-body interaction with a single centroid position. In case of water molecule, the formula expression would become identical to that of the three-body angle interaction. Although the total system virial is the same as compute *stress/atom*, compute *centroid/stress/atom* is know to result in more consistent heat flux values for angle, dihedrals, improper and constraint force contributions when computed via [[compute heat/flux]{.doc}]compute_heat_flux.md){.reference .internal}.

If no extra keywords are listed, the kinetic contribution *and* all of the virial contribution terms are included in the per-atom stress tensor. If any extra keywords are listed, only those terms are summed to compute the tensor. The *virial* keyword means include all terms except the kinetic energy *ke*.

Note that the stress for each atom is due to its interaction with all other atoms in the simulation, not just with other atoms in the group.

Details of how compute *stress/atom* obtains the virial for individual atoms for either pairwise or many-body potentials, and including the effects of periodic boundary conditions is discussed in [[(Thompson)]{.std .std-ref}](#thompson2){.reference .internal}. The basic idea for many-body potentials is to treat each component of the force computation between a small cluster of atoms in the same manner as in the formula above for bond, angle, dihedral, etc interactions. Namely the quantity [\\(\\mathbf{r} \\cdot \\mathbf{F}\\)]{.math .notranslate .nohighlight} is summed over the atoms in the interaction, with the [\\(r\\)]{.math .notranslate .nohighlight} vectors unwrapped by periodic boundaries so that the cluster of atoms is close together. The total contribution for the cluster interaction is divided evenly among those atoms.

Details of how compute *centroid/stress/atom* obtains the virial for individual atoms are given in [[(Surblys2019)]{.std .std-ref}](#surblys1){.reference .internal} and [[(Surblys2021)]{.std .std-ref}](#surblys2){.reference .internal}, where the idea is that the virial of the atom [\\(I\\)]{.math .notranslate .nohighlight} is the result of only the force [\\(\\mathbf{F}\_I\\)]{.math .notranslate .nohighlight} on the atom due to the interaction and its positional vector [\\(\\mathbf{r}\_{I0}\\)]{.math .notranslate .nohighlight}, relative to the geometric center of the interacting atoms, regardless of the number of participating atoms. The periodic boundary treatment is identical to that of compute *stress/atom*, and both of them reduce to identical expressions for two-body interactions, i.e. computed values for contributions from bonds and two-body pair styles, such as [[Lennard-Jones]{.doc}]pair_lj.md){.reference .internal}, will be the same, while contributions from angles, dihedrals and impropers will be different.

The [[dihedral_style charmm]{.doc}]dihedral_charmm.md){.reference .internal} style calculates pairwise interactions between 1-4 atoms. The virial contribution of these terms is included in the pair virial, not the dihedral virial.

The KSpace contribution is calculated using the method in [[(Heyes)]{.std .std-ref}](#heyes2){.reference .internal} for the Ewald method and by the methodology described in [[(Sirk)]{.std .std-ref}](#sirk1){.reference .internal} for PPPM. The choice of KSpace solver is specified by the [[kspace_style pppm]{.doc}]kspace_style.md){.reference .internal} command. Note that for PPPM, the calculation requires 6 extra FFTs each timestep that per-atom stress is calculated. Thus it can significantly increase the cost of the PPPM calculation if it is needed on a large fraction of the simulation timesteps.

The *temp-ID* argument can be used to affect the per-atom velocities used in the kinetic energy contribution to the total stress. If the kinetic energy is not included in the stress, than the temperature compute is not used and can be specified as NULL. If the kinetic energy is included and you wish to use atom velocities as-is, then *temp-ID* can also be specified as NULL. If desired, the specified temperature compute can be one that subtracts off a bias to leave each atom with only a thermal velocity to use in the formula above, e.g. by subtracting a background streaming velocity. See the doc pages for individual [[compute commands]{.doc}]compute.md){.reference .internal} to determine which ones include a bias.

------------------------------------------------------------------------

Note that as defined in the formula, per-atom stress is the negative of the per-atom pressure tensor. It is also really a stress\*volume formulation, meaning the computed quantity is in units of pressure\*volume. It would need to be divided by a per-atom volume to have units of stress (pressure), but an individual atom's volume is not well defined or easy to compute in a deformed solid or a liquid. See the [[compute voronoi/atom]{.doc}]compute_voronoi_atom.md){.reference .internal} command for one possible way to estimate a per-atom volume.

Thus, if the diagonal components of the per-atom stress tensor are summed for all atoms in the system and the sum is divided by [\\(dV\\)]{.math .notranslate .nohighlight}, where [\\(d\\)]{.math .notranslate .nohighlight} = dimension and [\\(V\\)]{.math .notranslate .nohighlight} is the volume of the system, the result should be [\\(-P\\)]{.math .notranslate .nohighlight}, where [\\(P\\)]{.math .notranslate .nohighlight} is the total pressure of the system.

These lines in an input script for a 3d system should yield that result. I.e. the last 2 columns of thermo output will be the same:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute        peratom all stress/atom NULL
    compute        p all reduce sum c_peratom[1] c_peratom[2] c_peratom[3]
    variable       press equal -(c_p[1]+c_p[2]+c_p[3])/(3*vol)
    thermo_style   custom step temp etotal press v_press
:::
::::

::: {.admonition .note}
Note

The per-atom stress does not include any Lennard-Jones tail corrections to the pressure added by the [[pair_modify tail yes]{.doc}]pair_modify.md){.reference .internal} command, since those are contributions to the global system pressure.
:::

The compute stress/atom can be used in a number of ways. Here is an example to compute a 1-d pressure profile in x-direction across the complete simulation box. You will need to adjust the number of bins and the selections for time averaging to your specific simulation. This assumes that the dimensions of the simulation cell does not change.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    # set number of bins
    variable nbins index 20
    variable fraction equal 1.0/v_nbins
    # define bins as chunks
    compute cchunk all chunk/atom bin/1d x lower ${fraction} units reduced
    compute stress all stress/atom NULL
    # apply conversion to pressure early since we have no variable style for processing chunks
    variable press atom -(c_stress[1]+c_stress[2]+c_stress[3])/(3.0*vol*${fraction})
    compute binpress all reduce/chunk cchunk sum v_press
    fix avg all ave/time 10 40 400 c_binpress mode vector file ave_stress.txt
:::
::::
:::::::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

Compute *stress/atom* calculates a per-atom array with 6 columns, which can be accessed by indices 1-6 by any command that uses per-atom values from a compute as input. Compute *centroid/stress/atom* produces a per-atom array with 9 columns, but otherwise can be used in an identical manner to compute *stress/atom*. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The ordering of the 6 columns for *stress/atom* is as follows: xx, yy, zz, xy, xz, yz. The ordering of the 9 columns for *centroid/stress/atom* is as follows: xx, yy, zz, xy, xz, yz, yx, zx, zy.

The per-atom array values will be in pressure\*volume [[units]{.doc}]units.md){.reference .internal} as discussed above.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Currently, compute *centroid/stress/atom* does not support pair styles with many-body interactions ([[EAM]{.doc}]pair_eam.md){.reference .internal} is an exception, since its computations are performed pairwise), nor granular pair styles with pairwise forces which are not aligned with the vector between the pair of particles. All bond styles are supported. All angle, dihedral, improper styles are supported with the exception of INTEL and KOKKOS variants of specific styles. It also does not support models with long-range Coulombic or dispersion forces, i.e. the kspace_style command in LAMMPS. It also does not implement the following fixes which add rigid-body constraints: [[fix rigid/\*]{.doc}]fix_rigid.md){.reference .internal} and the OpenMP accelerated version of [[fix rigid/small]{.doc}]fix_rigid.md){.reference .internal}, while all other [[fix rigid/\*/small]{.doc}]fix_rigid.md){.reference .internal} are implemented.

LAMMPS will generate an error if one of these options is included in your model. Extension of centroid stress calculations to these force and fix styles is planned for the future.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute pe]{.doc}]compute_pe.md){.reference .internal}, [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

By default the compute includes contributions from the keywords: [`ke`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`pair`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`bond`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`angle`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`dihedral`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`improper`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`kspace`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`fix`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

**(Heyes)** Heyes, Phys Rev B, 49, 755 (1994).

**(Sirk)** Sirk, Moore, Brown, J Chem Phys, 138, 064505 (2013).

**(Thompson)** Thompson, Plimpton, Mattson, J Chem Phys, 131, 154107 (2009).

**(Surblys2019)** Surblys, Matsubara, Kikugawa, Ohara, Phys Rev E, 99, 051301(R) (2019).

**(Surblys2021)** Surblys, Matsubara, Kikugawa, Ohara, J Appl Phys 130, 215104 (2021).
:::
::::::::::::::::::::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

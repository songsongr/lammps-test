:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-orient-eco-command .section}
[]{#index-0}

# fix orient/eco command[](#fix-orient-eco-command "Link to this heading"){.headerlink}

:::: {.highlight-none .notranslate}
::: highlight
    fix ID group-ID orient/eco u0 eta cutoff orientationsFile
:::
::::

- ID, group-ID are documented in fix command

- u0 = energy added to each atom (energy units)

- eta = cutoff value (usually 0.25)

- cutoff = cutoff radius for orientation parameter calculation

- orientationsFile = file that specifies orientation of each grain

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix gb all orient/eco 0.08 0.25 3.524 sigma5.ori
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The fix applies a synthetic driving force to a grain boundary which can be used for the investigation of grain boundary motion. The affiliation of atoms to either of the two grains forming the grain boundary is determined from an orientation-dependent order parameter as described in [[(Ulomek)]{.std .std-ref}](#ulomek){.reference .internal}. The potential energy of atoms is either increased by an amount of 0.5\**u0* or -0.5\**u0* according to the orientation of the surrounding crystal. This creates a potential energy gradient which pushes atoms near the grain boundary to orient according to the energetically favorable grain orientation. This fix is designed for applications in bicrystal system with one grain boundary and open ends, or two opposite grain boundaries in a periodic system. In either case, the entire system can experience a displacement during the simulation which needs to be accounted for in the evaluation of the grain boundary velocity. While the basic method is described in [[(Ulomek)]{.std .std-ref}](#ulomek){.reference .internal}, the implementation follows the efficient implementation from [[(Schratt & Mohles)]{.std .std-ref}](#schratt){.reference .internal}. The synthetic potential energy added to an atom j is given by the following formulas

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}w(\|\\vec{r}\_{jk}\|) = w\_{jk} & = \\left\\{\\begin{array}{lc} \\frac{\|\\vec{r}\_{jk}\|\^{4}}{r\_{\\mathrm{cut}}\^{4}} -2\\frac{\|\\vec{r}\_{jk}\|\^{2}}{r\_{\\mathrm{cut}}\^{2}}+1, & \|\\vec{r}\_{jk}\|\<r\_{\\mathrm{cut}} \\\\ 0, & \|\\vec{r}\_{jk}\|\\ge r\_{\\mathrm{cut}} \\end{array}\\right. \\\\ \\chi\_{j} & = \\frac{1}{N}\\sum\_{l=1}\^{3}\\left\\lbrack\\left\\vert\\psi\_{l}\^{\\mathrm{I}}(\\vec{r}\_{j})\\right\\vert\^{2}-\\left\\vert\\psi\_{l}\^{\\mathrm{II}}(\\vec{r}\_{j})\\right\\vert\^{2}\\right\\rbrack \\\\ \\psi\_{l}\^{\\mathrm{X}}(\\vec{r}\_{j}) & = \\sum\_{k\\in\\mathit{\\Gamma}\_{j}}w\_{jk}\\exp\\left(\\mathrm{i}\\vec{r}\_{jk}\\cdot\\vec{q}\_{l}\^{\\mathrm{X}}\\right) \\\\ u(\\chi\_{j}) & = \\frac{u\_{0}}{2}\\left\\{\\begin{array}{lc} 1, & \\chi\_{j}\\ge\\eta\\\\ \\sin\\left(\\frac{\\pi\\chi\_{j}}{2\\eta}\\right), & -\\eta\<\\chi\_{j}\<\\eta\\\\ -1, & \\chi\_{j}\\le-\\eta \\end{array}\\right.\\end{split}\\\]
:::

which are fully explained in [[(Ulomek)]{.std .std-ref}](#ulomek){.reference .internal} and [[(Schratt & Mohles)]{.std .std-ref}](#schratt){.reference .internal}.

The force on each atom is the negative gradient of the synthetic potential energy. It depends on the surrounding of this atom. An atom far from the grain boundary does not experience a synthetic force as its surrounding is that of an oriented single crystal and thermal fluctuations are masked by the parameter *eta*. Near the grain boundary however, the gradient is nonzero and synthetic force terms are computed. The orientationsFile specifies the perfect oriented crystal basis vectors for the two adjoining crystals. The first three lines (line=row vector) for the energetically penalized and the last three lines for the energetically favored grain assuming *u0* is positive. For negative *u0*, this is reversed. With the *cutoff* parameter, the size of the region around each atom which is used in the order parameter computation is defined. The cutoff must be smaller than the interaction range of the MD potential. It should at least include the nearest neighbor shell. For high temperatures or low angle grain boundaries, it might be beneficial to increase the cutoff in order to get a more precise identification of the atoms surrounding. However, computation time will increase as more atoms are considered in the order parameter and force computation. It is also worth noting that the cutoff radius must not exceed the communication distance for ghost atoms in LAMMPS. With orientationsFile, the 6 oriented crystal basis vectors is specified. Each line of the input file contains the three components of a primitive lattice vector oriented according to the grain orientation in the simulation box. The first (last) three lines correspond to the primitive lattice vectors of the first (second) grain. An example for a [\\(\\Sigma\\langle001\\rangle\\)]{.math .notranslate .nohighlight} mis-orientation is given at the end.

If no synthetic energy difference between the grains is created, [\\(u0=0\\)]{.math .notranslate .nohighlight}, the force computation is omitted. In this case, still, the order parameter of the driving force is computed and can be used to track the grain boundary motion throughout the simulation.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the potential energy of atom interactions with the grain boundary driving force to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}.

This fix calculates a per-atom array with 2 columns, which can be accessed by indices 1-1 by any command that uses per-atom values from a fix as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The first column is the order parameter for each atom; the second is the thermal masking value for each atom. Both are described above.

No parameter of this fix can be used with the start/stop keywords of the run command. This fix is not invoked during energy minimization.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the ORIENT package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix_modify]{.doc}]fix_modify.md){.reference .internal}

[[fix_orient]{.doc}]fix_orient.md){.reference .internal}
:::

::::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Ulomek)** Ulomek, Brien, Foiles, Mohles, Modelling Simul. Mater. Sci. Eng. 23 (2015) 025007

**(Schratt & Mohles)** Schratt, Mohles. Comp. Mat. Sci. 182 (2020) 109774

------------------------------------------------------------------------

For illustration purposes, here is an example file that specifies a [\\(\\Sigma=5 \\langle 001 \\rangle\\)]{.math .notranslate .nohighlight} tilt grain boundary. This is for a lattice constant of 3.52 Angstrom:

:::: {.highlight-none .notranslate}
::: highlight
    sigma5.ori:

    1.671685  0.557228  1.76212
    0.557228 -1.671685  1.76212
    2.228913 -1.114456  0.00000
    0.557228  1.671685  1.76212
    1.671685 -0.557228  1.76212
    2.228913  1.114456  0.00000
:::
::::
:::::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

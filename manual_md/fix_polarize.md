::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#fix-polarize-bem-gmres-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# fix polarize/bem/gmres command[](#fix-polarize-bem-gmres-command "Link to this heading"){.headerlink}
:::

::: {#fix-polarize-bem-icc-command .section}
# fix polarize/bem/icc command[](#fix-polarize-bem-icc-command "Link to this heading"){.headerlink}
:::

::::::::::::::::: {#fix-polarize-functional-command .section}
# fix polarize/functional command[](#fix-polarize-functional-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID style nevery tolerance
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- style = *polarize/bem/gmres* or *polarize/bem/icc* or *polarize/functional*

- nevery = this fixed is invoked every this many timesteps

- tolerance = the relative tolerance for the iterative solver to stop
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 2 interface polarize/bem/gmres 5 0.0001
    fix 1 interface polarize/bem/icc 1 0.0001
    fix 3 interface polarize/functional 1 0.0001
:::
::::

Used in input scripts:

> ::::: {}
> :::: {.highlight-none .notranslate}
> ::: highlight
>     examples/PACKAGES/dielectric/in.confined
>     examples/PACKAGES/dielectric/in.nopbc
> :::
> ::::
> :::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

These fixes compute induced charges at the interface between two impermeable media with different dielectric constants. The interfaces need to be discretized into vertices, each representing a boundary element. The vertices are treated as if they were regular atoms or particles. [[atom_style dielectric]{.doc}]atom_style.md){.reference .internal} should be used since it defines the additional properties of each interface particle such as interface normal vectors, element areas, and local dielectric mismatch. These fixes also require the use of [[pair_style]{.doc}]pair_style.md){.reference .internal} and [[kspace_style]{.doc}]kspace_style.md){.reference .internal} with the *dielectric* suffix. At every time step, given a configuration of the physical charges in the system (such as atoms and charged particles) these fixes compute and update the charge of the interface particles. The interfaces are allowed to move during the simulation if the appropriate time integrators are also set (for example, with [[fix_rigid]{.doc}]fix_rigid.md){.reference .internal}).

Consider an interface between two media: one with dielectric constant of 78 (water), the other of 4 (silica). The interface is discretized into 2000 boundary elements, each represented by an interface particle. Suppose that each interface particle has a normal unit vector pointing from the silica medium to water. The dielectric difference along the normal vector is then 78 - 4 = 74, the mean dielectric value is (78 + 4) / 2 = 41. Each boundary element also has its area and the local mean curvature, which is used by these fixes for computing a correction term in the local electric field. To model charged interfaces, an interface particle will have a non-zero charge value, coming from its area and surface charge density, and its local dielectric constant set to the mean dielectric value.

For non-interface particles such as atoms and charged particles, the interface normal vectors, element area, and dielectric mismatch are irrelevant and unused. Their local dielectric value is used internally to rescale their given charge when computing the Coulombic interactions. For instance, to simulate a cation carrying a charge of +2 (in simulation charge units) in an implicit solvent with a dielectric constant of 40, the cation's charge should be set to +2 and its local dielectric constant property (defined in the [[atom_style dielectric]{.doc}]atom_style.md){.reference .internal}) should be set to 40; there is no need to manually rescale charge. This will produce the proper force for any [[pair_style]{.doc}]pair_style.md){.reference .internal} with the dielectric suffix. It is assumed that the particles cannot pass through the interface during the simulation because the value of the local dielectric constant property does not change.

There are some example scripts for using these fixes with LAMMPS in the [`examples/PACKAGES/dielectric`{.docutils .literal .notranslate}]{.pre} directory. The README file therein contains specific details on the system setup. Note that the example data files show the additional fields (columns) needed for [[atom_style dielectric]{.doc}]atom_style.md){.reference .internal} beyond the conventional fields *id*, *mol*, *type*, *q*, *x*, *y*, and *z*.

------------------------------------------------------------------------

For fix *polarize/bem/gmres* and fix *polarize/bem/icc* the induced charges of the atoms in the specified group, which are the vertices on the interface, are computed using the equation:

::: {.math .notranslate .nohighlight}
\\\[\\sigma_b(\\mathbf{s}) = \\dfrac{1 - \\bar{\\epsilon}}{\\bar{\\epsilon}} \\sigma_f(\\mathbf{s}) - \\epsilon_0 \\dfrac{\\Delta \\epsilon}{\\bar{\\epsilon}} \\mathbf{E}(\\mathbf{s}) \\cdot \\mathbf{n}(\\mathbf{s})\\\]
:::

- [\\(\\sigma_b\\)]{.math .notranslate .nohighlight} is the induced charge density at the interface vertex [\\(\\mathbf{s}\\)]{.math .notranslate .nohighlight}.

- [\\(\\bar{\\epsilon}\\)]{.math .notranslate .nohighlight} is the mean dielectric constant at the interface vertex: [\\(\\bar{\\epsilon} = (\\epsilon_1 + \\epsilon_2)/2\\)]{.math .notranslate .nohighlight}.

- [\\(\\Delta \\epsilon\\)]{.math .notranslate .nohighlight} is the dielectric constant difference at the interface vertex: [\\(\\Delta \\epsilon = \\epsilon_1 - \\epsilon_2\\)]{.math .notranslate .nohighlight}

- [\\(\\sigma_f\\)]{.math .notranslate .nohighlight} is the free charge density at the interface vertex

- [\\(\\mathbf{E}(\\mathbf{s})\\)]{.math .notranslate .nohighlight} is the electrical field at the vertex

- [\\(\\mathbf{n}(\\mathbf{s})\\)]{.math .notranslate .nohighlight} is the unit normal vector at the vertex pointing from medium with [\\(\\epsilon_2\\)]{.math .notranslate .nohighlight} to that with [\\(\\epsilon_1\\)]{.math .notranslate .nohighlight}

Fix *polarize/bem/gmres* employs the Generalized Minimum Residual (GMRES) as described in [[(Barros)]{.std .std-ref}](#barros){.reference .internal} to solve [\\(\\sigma_b\\)]{.math .notranslate .nohighlight}.

Fix *polarize/bem/icc* employs the successive over-relaxation algorithm as described in [[(Tyagi)]{.std .std-ref}](#tyagi){.reference .internal} to solve [\\(\\sigma_b\\)]{.math .notranslate .nohighlight}.

The iterative solvers would terminate either when the maximum relative change in the induced charges in consecutive iterations is below the set tolerance, or when the number of iterations reaches *iter_max* (see below).

Fix *polarize/functional* employs the energy functional variation approach as described in [[(Jadhao)]{.std .std-ref}](#jadhao){.reference .internal} to solve [\\(\\sigma_b\\)]{.math .notranslate .nohighlight}.

The induced charges computed by these fixes are stored in the *q_scaled* field, and can be accessed as in the following example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute qs all property/atom q_scaled
    dump 1 all custom 1000 all.txt id type q x y z c_qs
:::
::::

Note that the *q* field is the regular atom charges, which do not change during the simulation. For interface particles, *q_scaled* is the sum of the real charge, divided by the local dielectric constant *epsilon*, and their induced charges. For non-interface particles, *q_scaled* is the real charge, divided by the local dielectric constant *epsilon*.

More details on the implementation of these fixes and their recommended use are described in [[(NguyenTD)]{.std .std-ref}](#nguyentd){.reference .internal}.
::::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} command provides the ability to modify certain settings:

> ::: {}
> ``` literal-block
> itr_max arg
>    arg = maximum number of iterations for convergence
> dielectrics ediff emean epsilon area charge
>    ediff = dielectric difference or NULL
>    emean = dielectric mean or NULL
>    epsilon = local dielectric value or NULL
>    area = element area or NULL
>    charge = real interface charge or NULL
> kspace arg = yes or no
> rand max seed
>    max = range of random induced charges to be generated
>    seed = random number seed to use when generating random charge
> mr arg
>    arg = maximum number of q-vectors to use when solving (GMRES only)
> omega arg
>    arg = relaxation parameter to use when iterating (ICC only)
> ```
> :::

The *itr_max* keyword sets the max number of iterations to be used for solving each step.

The *dielectrics* keyword allows properties of the atoms in group *group-ID* to be modified. Values passed to any of the arguments (*ediff*, *emean*, *epsilon*, *area*, *charge*) will override existing values for all atoms in the group *group-ID*. Passing NULL to any of these arguments will preserve the existing value. Note that setting the properties of the interface this way will change the properties of all atoms associated with the fix (all atoms in *group-ID*), so multiple fix and fix_modify commands would be needed to change the properties of two different interfaces to different values (one fix and fix_modify for each interface group).

The *kspace* keyword turns on long range interactions.

If the arguments of the *rand* keyword are set, then the atoms subject to this fix will be assigned a random initial charge in a uniform distribution from -*max*/2 to *max*/2, using random number seed *seed*.

The *mr* keyword only applies to *style* = *polarize/bem/gmres*. It is the maximum number of q-vectors to use when solving for the surface charge.

The *omega* keyword only applies when using *style* = *polarize/bem/icc*. It is a relaxation parameter defined in [[(Tyagi)]{.std .std-ref}](#tyagi){.reference .internal} that should generally be set between 0 and 2.

Note that the local dielectric constant (epsilon) can also be set independently using the [[set]{.doc}]set.md){.reference .internal} command.

------------------------------------------------------------------------

*polarize/bem/gmres* or *polarize/bem/icc* compute a global 2-element vector which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The first element is the number of iterations when the solver terminates (of which the upper bound is set by *iter_max*). The second element is the RMS error.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These fixes are part of the DIELECTRIC package. They are only enabled if LAMMPS was built with that package, which requires that also the KSPACE package is installed. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Note that the *polarize/bem/gmres* and *polarize/bem/icc* fixes only support [[units]{.doc}]units.md){.reference .internal} *lj*, *real*, *metal*, *si* and *nano* at the moment.

Note that *polarize/functional* does not yet support charged interfaces.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}, [[fix polarize]{.doc}](#){.reference .internal}, [[read_data]{.doc}]read_data.md){.reference .internal}, [[pair_style lj/cut/coul/long/dielectric]{.doc}]pair_dielectric.md){.reference .internal}, [[kspace_style pppm/dielectric]{.doc}]kspace_style.md){.reference .internal}, [[compute efield/atom]{.doc}]compute_efield_atom.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

*iter_max* = 50

*kspace* = yes

*omega* = 0.7 (ICC only)

*mr* = \# atoms in group *group-ID* minus 1 (GMRES only)

No random charge initialization happens by default.

------------------------------------------------------------------------

**(Barros)** Barros, Sinkovits, Luijten, J. Chem. Phys, 140, 064903 (2014)

**(Tyagi)** Tyagi, Suzen, Sega, Barbosa, Kantorovich, Holm, J Chem Phys, 132, 154112 (2010)

**(Jadhao)** Jadhao, Solis, Olvera de la Cruz, J Chem Phys, 138, 054119 (2013)

**(NguyenTD)** Nguyen, Li, Bagchi, Solis, Olvera de la Cruz, Comput Phys Commun 241, 80-19 (2019)
:::
:::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-thole-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style thole command[](#pair-style-thole-command "Link to this heading"){.headerlink}
:::

::::::::::::::::: {#pair-style-lj-cut-thole-long-command .section}
# pair_style lj/cut/thole/long command[](#pair-style-lj-cut-thole-long-command "Link to this heading"){.headerlink}

Accelerator Variants: *lj/cut/thole/long/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style args
:::
::::

- style = *thole* or *lj/cut/thole/long*

- args = list of arguments for a particular style

``` literal-block
thole args = damp cutoff
  damp = global damping parameter
  cutoff = global cutoff (distance units)
lj/cut/thole/long args = damp cutoff (cutoff2)
  damp = global damping parameter
  cutoff = global cutoff for LJ (and Thole if only 1 arg) (distance units)
  cutoff2 = global cutoff for Thole (optional) (distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style hybrid/overlay ... thole 2.6 12.0
    pair_coeff 1 1 thole 1.0
    pair_coeff 1 2 thole 1.0 2.6 10.0
    pair_coeff * 2 thole 1.0 2.6

    pair_style lj/cut/thole/long 2.6 12.0
:::
::::

Example input scripts available: examples/PACKAGES/drude
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *thole* pair styles are meant to be used with force fields that include explicit polarization through Drude dipoles. This link describes how to use the [[thermalized Drude oscillator model]{.doc}]Howto_drude.md){.reference .internal} in LAMMPS and polarizable models in LAMMPS are discussed on the [[Howto polarizable]{.doc}]Howto_polarizable.md){.reference .internal} doc page.

The *thole* pair style should be used as a sub-style within in the [[pair_style hybrid/overlay]{.doc}]pair_hybrid.md){.reference .internal} command, in conjunction with a main pair style including Coulomb interactions, i.e. any pair style containing *coul/cut* or *coul/long* in its style name.

The *lj/cut/thole/long* pair style is equivalent to, but more convenient that the frequent combination *hybrid/overlay lj/cut/coul/long cutoff thole damp cutoff2*. It is not only a shorthand for this pair_style combination, but it also allows for mixing pair coefficients instead of listing them all. The *lj/cut/thole/long* pair style is also a bit faster because it avoids an overlay and can benefit from OMP acceleration. Moreover, it uses a more precise approximation of the direct Coulomb interaction at short range similar to [[coul/long/cs]{.doc}]pair_cs.md){.reference .internal}, which stabilizes the temperature of Drude particles.

The *thole* pair styles compute the Coulomb interaction damped at short distances by a function

::: {.math .notranslate .nohighlight}
\\\[T\_{ij}(r\_{ij}) = 1 - \\left( 1 + \\frac{s\_{ij} r\_{ij} }{2} \\right) \\exp \\left( - s\_{ij} r\_{ij} \\right)\\\]
:::

This function results from an adaptation to point charges [[(Noskov)]{.std .std-ref}](#noskov1){.reference .internal} of the dipole screening scheme originally proposed by [[Thole]{.std .std-ref}](#thole1){.reference .internal}. The scaling coefficient [\\(s\_{ij}\\)]{.math .notranslate .nohighlight} is determined by the polarizability of the atoms, [\\(\\alpha_i\\)]{.math .notranslate .nohighlight}, and by a Thole damping parameter [\\(a\\)]{.math .notranslate .nohighlight}. This Thole damping parameter usually takes a value of 2.6, but in certain force fields the value can depend upon the atom types. The mixing rule for Thole damping parameters is the arithmetic average, and for polarizabilities the geometric average between the atom-specific values.

::: {.math .notranslate .nohighlight}
\\\[s\_{ij} = \\frac{ a\_{ij} }{ (\\alpha\_{ij})\^{1/3} } = \\frac{ (a_i + a_j)/2 }{ \[(\\alpha_i\\alpha_j)\^{1/2}\]\^{1/3} }\\\]
:::

The damping function is only applied to the interactions between the point charges representing the induced dipoles on polarizable sites, that is, charges on Drude particles, [\\(q\_{D,i}\\)]{.math .notranslate .nohighlight}, and opposite charges, [\\(-q\_{D,i}\\)]{.math .notranslate .nohighlight}, located on the respective core particles (to which each Drude particle is bonded). Therefore, Thole screening is not applied to the full charge of the core particle [\\(q_i\\)]{.math .notranslate .nohighlight}, but only to the [\\(-q\_{D,i}\\)]{.math .notranslate .nohighlight} part of it.

The interactions between core charges are subject to the weighting factors set by the [[special_bonds]{.doc}]special_bonds.md){.reference .internal} command. The interactions between Drude particles and core charges or non-polarizable atoms are also subject to these weighting factors. The Drude particles inherit the 1-2, 1-3 and 1-4 neighbor relations from their respective cores.

For pair_style *thole*, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command as in the example above.

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (distance units\^3)

- damp

- cutoff (distance units)

The last two coefficients are optional. If not specified the global Thole damping parameter or global cutoff specified in the pair_style command are used. In order to specify a cutoff (third argument) a damp parameter (second argument) must also be specified.

For pair style *lj/cut/thole/long*, the following coefficients must be defined for each pair of atoms types via the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command.

- [\\(\\epsilon\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (length units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight} (distance units\^3)

- damp

- LJ cutoff (distance units)

The last two coefficients are optional and default to the global values from the *pair_style* command.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::

:::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

The *thole* pair style does not support mixing. Thus, coefficients for all I,J pairs must be specified explicitly.

The *lj/cut/thole/long* pair style does support mixing. Mixed coefficients are defined using

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\alpha\_{ij} = & \\sqrt{\\alpha_i\\alpha_j} \\\\ & \\\\ a\_{ij} = & \\frac 1 2 (a_i + a_j)\\end{split}\\\]
:::
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles are part of the DRUDE package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair_style should currently not be used with the [[charmm dihedral style]{.doc}]dihedral_charmm.md){.reference .internal} if the latter has non-zero 1-4 weighting factors. This is because the *thole* pair style does not know which pairs are 1-4 partners of which dihedrals.

The *lj/cut/thole/long* pair style should be used with a [[Kspace solver]{.doc}]kspace_style.md){.reference .internal} like PPPM or Ewald, which is only enabled if LAMMPS was built with the kspace package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix drude]{.doc}]fix_drude.md){.reference .internal}, [[fix langevin/drude]{.doc}]fix_langevin_drude.md){.reference .internal}, [[fix drude/transform]{.doc}]fix_drude_transform.md){.reference .internal}, [[compute temp/drude]{.doc}]compute_temp_drude.md){.reference .internal} [[pair_style lj/cut/coul/long]{.doc}]pair_lj_cut_coul.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Noskov)** Noskov, Lamoureux and Roux, J Phys Chem B, 109, 6705 (2005).

**(Thole)** Chem Phys, 59, 341 (1981).
:::
:::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

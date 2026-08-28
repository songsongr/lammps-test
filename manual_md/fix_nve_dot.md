::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::: {#fix-nve-dot-command .section}
[]{#index-0}

# fix nve/dot command[](#fix-nve-dot-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nve/dot
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nve/dot = style name of this fix command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nve/dot
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply a rigid-body integrator as described in [[(Davidchack)]{.std .std-ref}](#davidchack4){.reference .internal} to a group of atoms, but without Langevin dynamics. This command performs Molecular dynamics (MD) via a velocity-Verlet algorithm and an evolution operator that rotates the quaternion degrees of freedom, similar to the scheme outlined in [[(Miller)]{.std .std-ref}](#miller4){.reference .internal}.

This command is the equivalent of the [[fix nve/dotc/langevin]{.doc}]fix_nve_dotc_langevin.md){.reference .internal} without damping and noise and can be used to determine the stability range in a NVE ensemble prior to using the Langevin-type DOTC-integrator (see also [[fix nve/dotc/langevin]{.doc}]fix_nve_dotc_langevin.md){.reference .internal}). The command is equivalent to the [[fix nve]{.doc}]fix_nve.md){.reference .internal}. The particles are always considered to have a finite size.

An example input file can be found in /examples/PACKAGES/cgdna/examples/duplex1/. Further details of the implementation and stability of the integrator are contained in [[(Henrich)]{.std .std-ref}](#henrich4){.reference .internal}. The preprint version of the article can be found [here](PDF/CG-DNA.pdf){.reference .external}.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These pair styles can only be used if LAMMPS was built with the [[CG-DNA]{.std .std-ref}]Packages_details.md#pkg-cg-dna){.reference .internal} package and the MOLECULE and ASPHERE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nve/dotc/langevin]{.doc}]fix_nve_dotc_langevin.md){.reference .internal}, [[fix nve]{.doc}]fix_nve.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Davidchack)** R.L Davidchack, T.E. Ouldridge, and M.V. Tretyakov. J. Chem. Phys. 142, 144114 (2015).

**(Miller)** T. F. Miller III, M. Eleftheriou, P. Pattnaik, A. Ndirango, G. J. Martyna, J. Chem. Phys., 116, 8649-8659 (2002).

**(Henrich)** O. Henrich, Y. A. Gutierrez-Fosado, T. Curk, T. E. Ouldridge, Eur. Phys. J. E 41, 57 (2018).
:::
:::::::::::::
::::::::::::::
:::::::::::::::

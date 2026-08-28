::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-nve-spin-command .section}
[]{#index-0}

# fix nve/spin command[](#fix-nve-spin-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID nve/spin keyword values
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nve/spin = style name of this fix command

- keyword = *lattice*

  ``` literal-block
  lattice value = moving or frozen
    moving = integrate both spin and atomic degress of freedom
    frozen = integrate spins on a fixed lattice
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 3 all nve/spin lattice moving
    fix 1 all nve/spin lattice frozen
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Perform a symplectic integration for the spin or spin-lattice system.

The *lattice* keyword defines if the spins are integrated on a lattice of fixed atoms (lattice = frozen), or if atoms are moving (lattice = moving). The first case corresponds to a spin dynamics calculation, and the second to a spin-lattice calculation. By default a spin-lattice integration is performed (lattice = moving).

The *nve/spin* fix applies a Suzuki-Trotter decomposition to the equations of motion of the spin lattice system, following the scheme:

![](_images/fix_integration_spin_stdecomposition.jpg){.align-center}

according to the implementation reported in [[(Omelyan)]{.std .std-ref}](#omelyan1){.reference .internal}.

A sectoring method enables this scheme for parallel calculations. The implementation of this sectoring algorithm is reported in [[(Tranchida)]{.std .std-ref}](#tranchida1){.reference .internal}.
:::

------------------------------------------------------------------------

::::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix style can only be used if LAMMPS was built with the SPIN package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

To use the spin algorithm, it is necessary to define a map with the atom_modify command. Typically, by adding the command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    atom_modify map array
:::
::::

before you create the simulation box. Note that the keyword "hash" instead of "array" is also valid.
:::::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[atom_style spin]{.doc}]atom_style.md){.reference .internal}, [[fix nve]{.doc}]fix_nve.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option default is lattice = moving.

------------------------------------------------------------------------

**(Omelyan)** Omelyan, Mryglod, and Folk. Phys. Rev. Lett. 86(5), 898. (2001).

**(Tranchida)** Tranchida, Plimpton, Thibaudeau and Thompson, Journal of Computational Physics, 372, 406-425, (2018).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

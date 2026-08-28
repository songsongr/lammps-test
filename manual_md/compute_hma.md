:::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::: {#compute-hma-command .section}
[]{#index-0}

# compute hma command[](#compute-hma-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID hma temp-ID keyword ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- hma = style name of this compute command

- temp-ID = ID of fix that specifies the set temperature during canonical simulation

- one or more keywords or keyword/argument pairs must be appended

- keyword = *anharmonic* or *u* or *p* or *cv*

``` literal-block
anharmonic = compute will return anharmonic property values
u = compute will return potential energy
p value = Pharm = compute will return pressure
   Pharm = difference between the harmonic pressure and lattice pressure
           as described below
cv = compute will return the heat capacity
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 2 all hma 1 u
    compute 2 all hma 1 anharmonic u p 0.9
    compute 2 all hma 1 u cv
:::
::::
:::::

::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the properties of a solid (potential energy, pressure or heat capacity), using the harmonically-mapped averaging (HMA) method. This command yields much higher precision than the equivalent compute commands ([[compute pe]{.doc}]compute_pe.md){.reference .internal}, [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}, etc.) commands during a canonical simulation of an atomic crystal. Specifically, near melting HMA can yield averages of a given precision an order of magnitude faster than conventional methods, and this only improves as the temperatures is lowered. This is particularly important for evaluating the free energy by thermodynamic integration, where the low-temperature contributions are the greatest source of statistical uncertainty. Moreover, HMA has other advantages, including smaller potential-truncation effects, finite-size effects, smaller timestep inaccuracy, faster equilibration and shorter decorrelation time.

HMA should not be used if atoms are expected to diffuse. It is also restricted to simulations in the NVT ensemble. While this compute may be used with any potential in LAMMPS, it will provide inaccurate results for potentials that do not go to 0 at the truncation distance; [[pair_style lj/smooth/linear]{.doc}]pair_lj_smooth_linear.md){.reference .internal} and Ewald summation should work fine, while [[pair_style lj/cut]{.doc}]pair_lj.md){.reference .internal} will perform poorly unless the potential is shifted (via [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift) or the cutoff is large. Furthermore, computation of the heat capacity with this compute is restricted to those that implement the *single_hessian* method in Pair. Implementing *single_hessian* in additional pair styles is simple. Please contact Andrew Schultz (ajs42 at buffalo.edu) and David Kofke (kofke at buffalo.edu) if your desired pair style does not have this method. This is the list of pair styles that currently implement *single_hessian*:

- [[pair_style lj/smooth/linear]{.doc}]pair_lj_smooth_linear.md){.reference .internal}

In this method, the analytically known harmonic behavior of a crystal is removed from the traditional ensemble averages, which leads to an accurate and precise measurement of the anharmonic contributions without contamination by noise produced by the already-known harmonic behavior. A detailed description of this method can be found in ([[Moustafa]{.std .std-ref}](#hma-moustafa){.reference .internal}). The potential energy is computed by the formula:

::: {.math .notranslate .nohighlight}
\\\[\\left\< U\\right\>\_\\text{HMA} = \\frac{d}{2} (N-1) k_B T + \\left\< U + \\frac{1}{2} \\vec F\\cdot\\Delta \\vec r \\right\>\\\]
:::

where [\\(N\\)]{.math .notranslate .nohighlight} is the number of atoms in the system, [\\(k_B\\)]{.math .notranslate .nohighlight} is Boltzmann's constant, [\\(T\\)]{.math .notranslate .nohighlight} is the temperature, [\\(d\\)]{.math .notranslate .nohighlight} is the dimensionality of the system (2 or 3 for 2d/3d), [\\(\\vec F\\cdot\\Delta\\vec r\\)]{.math .notranslate .nohighlight} is the sum of dot products of the atomic force vectors and displacement (from lattice sites) vectors, and [\\(U\\)]{.math .notranslate .nohighlight} is the sum of pair, bond, angle, dihedral, improper, kspace (long-range), and fix energies.

The pressure is computed by the formula:

::: {.math .notranslate .nohighlight}
\\\[\\left\< P\\right\>\_{HMA} = \\Delta \\hat P + \\left\< P\_\\text{vir} + \\frac{\\beta \\Delta \\hat P - \\rho}{d(N-1)} \\vec F\\cdot\\Delta \\vec r \\right\>\\\]
:::

where [\\(\\rho\\)]{.math .notranslate .nohighlight} is the number density of the system, [\\(\\Delta \\hat P\\)]{.math .notranslate .nohighlight} is the difference between the harmonic and lattice pressure, [\\(P\_\\text{vir}\\)]{.math .notranslate .nohighlight} is the virial pressure computed as the sum of pair, bond, angle, dihedral, improper, kspace (long-range), and fix contributions to the force on each atom, and [\\(k_B=1/k_B T\\)]{.math .notranslate .nohighlight}. Although the method will work for any value of [\\(\\Delta \\hat P\\)]{.math .notranslate .nohighlight} specified (use pressure [[units]{.doc}]units.md){.reference .internal}), the precision of the resultant pressure is sensitive to [\\(\\Delta \\hat P\\)]{.math .notranslate .nohighlight}; the precision tends to be best when [\\(\\Delta \\hat P\\)]{.math .notranslate .nohighlight} is the actual the difference between the lattice pressure and harmonic pressure.

::: {.math .notranslate .nohighlight}
\\\[\\left\<C_V \\right\>\_\\text{HMA} = \\frac{d}{2} (N-1) k_B + \\frac{1}{k_B T\^2} \\left( \\left\<U\_\\text{HMA}\^2 \\right\> - \\left\<U\_\\text{HMA}\\right\>\^2 \\right) + \\frac{1}{4 T} \\left\<\\vec F\\cdot\\Delta\\vec r + \\Delta r \\cdot\\Phi\\cdot \\Delta\\vec r\\right\>\\\]
:::

where [\\(\\Phi\\)]{.math .notranslate .nohighlight} is the Hessian matrix. The compute hma command computes the full expression for [\\(C_V\\)]{.math .notranslate .nohighlight} except for the [\\(\\left\<U\_\\text{HMA}\\right\>\^2\\)]{.math .notranslate .nohighlight} in the variance term, which can be obtained by passing the *u* keyword; you must add this extra contribution to the [\\(C_V\\)]{.math .notranslate .nohighlight} value reported by this compute. The variance term can cause significant round-off error when computing [\\(C_V\\)]{.math .notranslate .nohighlight}. To address this, the *anharmonic* keyword can be passed and/or the output format can be specified with more digits.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    thermo_modify format float '%22.15e'
:::
::::

The *anharmonic* keyword will instruct the compute to return anharmonic properties rather than the full properties, which include lattice, harmonic and anharmonic contributions. When using this keyword, the compute must be first active (it must be included via a [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command) while the atoms are still at their lattice sites (before equilibration).

The temp-ID specified with compute hma command should be same as the fix-ID of the Nose--Hoover ([[fix nvt]{.doc}]fix_nh.md){.reference .internal}) or Berendsen ([[fix temp/berendsen]{.doc}]fix_temp_berendsen.md){.reference .internal}) thermostat used for the simulation. While using this command, the Langevin thermostat ([[fix langevin]{.doc}]fix_langevin.md){.reference .internal}) should be avoided as its extra forces interfere with the HMA implementation.

::: {.admonition .note}
Note

Compute hma command should be used right after the energy minimization, when the atoms are at their lattice sites. The simulation should not be started before this command has been used in the input script.
:::

The following example illustrates the placement of this command in the input script:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    min_style cg
    minimize 1e-35 1e-15 50000 500000
    compute 1 all hma thermostatid u
    fix thermostatid all nvt temp 600.0 600.0 100.0
:::
::::

::: {.admonition .note}
Note

Compute hma should be used when the atoms of the solid do not diffuse. Diffusion will reduce the precision in the potential energy computation.
:::

::: {.admonition .note}
Note

The [[fix_modify energy yes]{.doc}]fix_modify.md){.reference .internal} command must also be specified if a fix is to contribute potential energy to this command.
:::

An example input script that uses this compute is included in examples/PACKAGES/hma/ along with corresponding LAMMPS output showing that the HMA properties fluctuate less than the corresponding conventional properties.
:::::::::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector that includes the n properties requested as arguments to the command (the potential energy, pressure and/or heat capacity). The elements of the vector can be accessed by indices 1--n by any command that uses global vector values as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The vector values calculated by this compute are "extensive". The scalar value will be in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EXTRA-COMPUTE package. It is enabled only if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Usage restricted to canonical (NVT) ensemble simulation only.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute pe]{.doc}]compute_pe.md){.reference .internal}, [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}

[[dynamical matrix]{.doc}]dynamical_matrix.md){.reference .internal} provides a finite difference formulation of the Hessian provided by Pair's single_hessian, which is used by this compute.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Moustafa)** Sabry G. Moustafa, Andrew J. Schultz, and David A. Kofke, *Very fast averaging of thermal properties of crystals by molecular simulation*, [Phys. Rev. E \[92\], 043303 (2015)](https://link.aps.org/doi/10.1103/PhysRevE.92.043303){.reference .external}
:::
::::::::::::::::::::::::
:::::::::::::::::::::::::
::::::::::::::::::::::::::

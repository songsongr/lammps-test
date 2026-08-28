::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#compute-stress-cylinder-command .section}
[]{#index-1}[]{#index-0}

# compute stress/cylinder command[](#compute-stress-cylinder-command "Link to this heading"){.headerlink}
:::

:::::::::::::::: {#compute-stress-spherical-command .section}
# compute stress/spherical command[](#compute-stress-spherical-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID style args
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- style = stress/spherical or stress/cylinder

- args = argument specific to the compute style

``` literal-block
stress/cylinder args = zlo zh Rmax bin_width keyword
  zlo = minimum z-boundary for cylinder
  zhi = maximum z-boundary for cylinder
  Rmax = maximum radius to perform calculation to
  bin_width = width of radial bins to use for calculation
  keyword = ke (zero or one can be specified)
    ke = yes or no
stress/spherical
  x0, y0, z0 = origin of the spherical coordinate system
  bin_width = width of spherical shells
  Rmax = maximum radius of spherical shells
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all stress/cylinder -10.0 10.0 15.0 0.25
    compute 1 all stress/cylinder -10.0 10.0 15.0 0.25 ke no
    compute 1 all stress/spherical 0 0 0 0.1 10
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Compute *stress/cylinder*, and compute *stress/spherical* define computations that calculate profiles of the diagonal components of the local stress tensor in the specified coordinate system. The stress tensor is split into a kinetic contribution [\\(P\^k\\)]{.math .notranslate .nohighlight} and a virial contribution [\\(P\^v\\)]{.math .notranslate .nohighlight}. The sum gives the total stress tensor [\\(P = P\^k+P\^v\\)]{.math .notranslate .nohighlight}. These computes can for example be used to calculate the diagonal components of the local stress tensor of surfaces with cylindrical or spherical symmetry. These computes obeys momentum balance through fluid interfaces. They use the Irving--Kirkwood contour, which is the straight line between particle pairs.

The compute *stress/cylinder* computes the stress profile along the radial direction in cylindrical coordinates, as described in [[(Addington)]{.std .std-ref}](#addington1){.reference .internal}. The compute *stress/spherical* computes the stress profile along the radial direction in spherical coordinates, as described in [[(Ikeshoji)]{.std .std-ref}](#ikeshoji4){.reference .internal}.
:::

::::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

The default output columns for *stress/cylinder* are the radius to the center of the cylindrical shell, number density, [\\(P\^k\_{rr}\\)]{.math .notranslate .nohighlight}, [\\(P\^k\_{\\phi\\phi}\\)]{.math .notranslate .nohighlight}, [\\(P\^k\_{zz}\\)]{.math .notranslate .nohighlight}, [\\(P\^v\_{rr}\\)]{.math .notranslate .nohighlight}, [\\(P\^v\_{\\phi\\phi}\\)]{.math .notranslate .nohighlight}, and [\\(P\^v\_{zz}\\)]{.math .notranslate .nohighlight}. When the keyword *ke* is set to *no*, the kinetic contributions are not calculated, and consequently there are only 5 columns: the position of the center of the cylindrical shell, the number density, [\\(P\^v\_{rr}\\)]{.math .notranslate .nohighlight}, [\\(P\^v\_{\\phi\\phi}\\)]{.math .notranslate .nohighlight}, and [\\(P\^v\_{zz}\\)]{.math .notranslate .nohighlight}. The number of bins (rows) is [\\(R\_\\text{max}/b\\)]{.math .notranslate .nohighlight}, where [\\(b\\)]{.math .notranslate .nohighlight} is the specified bin width.

The output columns for *stress/spherical* are the position of the center of the spherical shell, the number density, [\\(P\^k\_{rr}\\)]{.math .notranslate .nohighlight}, [\\(P\^k\_{\\theta\\theta}\\)]{.math .notranslate .nohighlight}, [\\(P\^k\_{\\phi\\phi}\\)]{.math .notranslate .nohighlight}, [\\(P\^v\_{rr}\\)]{.math .notranslate .nohighlight}, [\\(P\^v\_{\\theta\\theta}\\)]{.math .notranslate .nohighlight}, and [\\(P\^v\_{\\phi\\phi}\\)]{.math .notranslate .nohighlight}. There are 8 columns and the number of bins (rows) is [\\(R\_\\text{max}/b\\)]{.math .notranslate .nohighlight}, where [\\(b\\)]{.math .notranslate .nohighlight} is the specified bin width.

This array can be output with [[fix ave/time]{.doc}]fix_ave_time.md){.reference .internal},

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute p all stress/spherical 0 0 0 0.1 10
    fix 2 all ave/time 100 1 100 c_p[*] file dump_p.out mode vector
:::
::::

The values calculated by this compute are "intensive". The stress values will be in pressure [[units]{.doc}]units.md){.reference .internal}. The number density values are in inverse volume [[units]{.doc}]units.md){.reference .internal}.

NOTE 1: The local stress does not include any Lennard-Jones tail corrections to the stress added by the [[pair_modify tail yes]{.doc}]pair_modify.md){.reference .internal} command, since those are contributions to the global system pressure.
:::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

These computes calculate the stress tensor contributions for pair styles only (i.e., no bond, angle, dihedral, etc. contributions, and in the presence of bonded interactions, the result may be incorrect due to exclusions for [[special bonds]{.doc}]special_bonds.md){.reference .internal} excluding pairs of atoms completely). It requires pairwise force calculations not available for most many-body pair styles. Note that [\\(k\\)]{.math .notranslate .nohighlight}-space calculations are also excluded.

These computes are part of the EXTRA-COMPUTE package. They are only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal}, [[compute pressure]{.doc}]compute_pressure.md){.reference .internal}, [[compute stress/mop/profile]{.doc}]compute_stress_mop.md){.reference .internal}, [[compute stress/cartesian]{.doc}]compute_stress_cartesian.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The keyword default for ke in style *stress/cylinder* is yes.

------------------------------------------------------------------------

**(Ikeshoji)** Ikeshoji, Hafskjold, Furuholt, Mol Sim, 29, 101-109, (2003).

**(Addington)** Addington, Long, Gubbins, J Chem Phys, 149, 084109 (2018).
:::
::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

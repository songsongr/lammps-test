::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-erotate-asphere-command .section}
[]{#index-1}[]{#index-0}

# compute erotate/asphere command[](#compute-erotate-asphere-command "Link to this heading"){.headerlink}

Accelerator Variants: *erotate/asphere/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID erotate/asphere
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- erotate/asphere = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all erotate/asphere
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the rotational kinetic energy of a group of aspherical particles. The aspherical particles can be ellipsoids, or line segments, or triangles. See the [[atom_style]{.doc}]atom_style.md){.reference .internal} and [[read_data]{.doc}]read_data.md){.reference .internal} commands for descriptions of these options.

For all 3 types of particles, the rotational kinetic energy is computed as [\\(\\frac12 I \\omega\^2\\)]{.math .notranslate .nohighlight}, where [\\(I\\)]{.math .notranslate .nohighlight} is the inertia tensor for the aspherical particle and [\\(\\omega\\)]{.math .notranslate .nohighlight} is its angular velocity, which is computed from its angular momentum if needed.

::: {.admonition .note}
Note

For [[2d models]{.doc}]dimension.md){.reference .internal}, ellipsoidal particles are treated as ellipsoids, not ellipses, meaning their moments of inertia will be the same as in 3d.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global scalar (the KE). This value can be used by any command that uses a global scalar value from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The scalar value calculated by this compute is "extensive". The scalar value will be in energy [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute requires that ellipsoidal particles atoms store a shape and quaternion orientation and angular momentum as defined by the [[atom_style ellipsoid]{.doc}]atom_style.md){.reference .internal} command.

This compute requires that line segment particles atoms store a length and orientation and angular velocity as defined by the [[atom_style line]{.doc}]atom_style.md){.reference .internal} command.

This compute requires that triangular particles atoms store a size and shape and quaternion orientation and angular momentum as defined by the [[atom_style tri]{.doc}]atom_style.md){.reference .internal} command.

All particles in the group must be of finite size. They cannot be point particles.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none

[[compute erotate/sphere]{.doc}]compute_erotate_sphere.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

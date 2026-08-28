:::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::: {#compute-fabric-command .section}
[]{#index-0}

# compute fabric command[](#compute-fabric-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID fabric cutoff attribute ... keyword values ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- fabric = style name of this compute command

- cutoff = *type* or *radius*

  ``` literal-block
  type = cutoffs determined based on atom types
  radius = cutoffs determined based on atom diameters (atom style sphere)
  ```

- one or more attributes may be appended

- attribute = *contact* or *branch* or *force/normal* or *force/tangential*

  ``` literal-block
  contact = contact tensor
  branch = branch tensor
  force/normal = normal force tensor
  force/tangential = tangential force tensor
  ```

- zero or more keyword/value pairs may be appended

- keyword = *type/include*

  ``` literal-block
  type/include value = arg1 arg2
    arg = separate lists of types (see below)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all fabric type contact force/normal type/include 1,2 3*4
    compute 1 all fabric radius force/normal force/tangential
:::
::::
:::::

::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a compute that calculates various fabric tensors for pairwise interaction [[(Ouadfel)]{.std .std-ref}](#ouadfel){.reference .internal}. Fabric tensors are commonly used to quantify the anisotropy or orientation of granular contacts but can also be used to characterize the direction of pairwise interactions in general systems. The *type* and *radius* settings are used to select whether interactions cutoffs are determined by atom types or by the sum of atomic radii (atom style sphere), respectively. Calling this compute is roughly the cost of a pair style invocation as it involves a loop over the neighbor list. If the normal or tangential force tensors are requested, it will be more expensive than a pair style invocation as it will also recalculate all pair forces.

Four fabric tensors are available: the contact, branch, normal force, or tangential force tensor. The contact tensor is calculated as

::: {.math .notranslate .nohighlight}
\\\[C\_{ab} = \\frac{15}{2} (\\phi\_{ab} - \\frac{1}{3} \\mathrm{Tr}(\\phi) \\delta\_{ab})\\\]
:::

where [\\(a\\)]{.math .notranslate .nohighlight} and [\\(b\\)]{.math .notranslate .nohighlight} are the [\\(x\\)]{.math .notranslate .nohighlight}, [\\(y\\)]{.math .notranslate .nohighlight}, [\\(z\\)]{.math .notranslate .nohighlight} directions, [\\(\\delta\_{ab}\\)]{.math .notranslate .nohighlight} is the Kronecker delta function, and the tensor [\\(\\phi\\)]{.math .notranslate .nohighlight} is defined as

::: {.math .notranslate .nohighlight}
\\\[\\phi\_{ab} = \\sum\_{n = 1}\^{N_p} \\frac{r\_{a} r\_{b}}{r\^2}\\\]
:::

where [\\(n\\)]{.math .notranslate .nohighlight} loops over the [\\(N_p\\)]{.math .notranslate .nohighlight} pair interactions in the simulation, [\\(r\_{a}\\)]{.math .notranslate .nohighlight} is the [\\(a\\)]{.math .notranslate .nohighlight} component of the radial vector between the two pairwise interacting particles, and [\\(r\\)]{.math .notranslate .nohighlight} is the magnitude of the radial vector.

The branch tensor is calculated as

::: {.math .notranslate .nohighlight}
\\\[B\_{ab} = \\frac{15}{2\\, \\mathrm{Tr}(D)} (D\_{ab} - \\frac{1}{3} \\mathrm{Tr}(D) \\delta\_{ab})\\\]
:::

where the tensor [\\(D\\)]{.math .notranslate .nohighlight} is defined as

::: {.math .notranslate .nohighlight}
\\\[D\_{ab} = \\sum\_{n = 1}\^{N_p} \\frac{1}{N_c (r\^2 + C\_{cd} r_c r_d)} \\frac{r\_{a} r\_{b}}{r}\\\]
:::

where [\\(N_c\\)]{.math .notranslate .nohighlight} is the total number of contacts in the system and the subscripts [\\(c\\)]{.math .notranslate .nohighlight} and [\\(d\\)]{.math .notranslate .nohighlight} indices are summed according to Einstein notation.

The normal force fabric tensor is calculated as

::: {.math .notranslate .nohighlight}
\\\[F\^n\_{ab} = \\frac{15}{2\\, \\mathrm{Tr}(N)} (N\_{ab} - \\frac{1}{3} \\mathrm{Tr}(N) \\delta\_{ab})\\\]
:::

where the tensor [\\(N\\)]{.math .notranslate .nohighlight} is defined as

::: {.math .notranslate .nohighlight}
\\\[N\_{ab} = \\sum\_{n = 1}\^{N_p} \\frac{1}{N_c (r\^2 + C\_{cd} r_c r_d)} \\frac{r\_{a} r\_{b}}{r\^2} f_n\\\]
:::

and [\\(f_n\\)]{.math .notranslate .nohighlight} is the magnitude of the normal, central-body force between the two atoms.

Finally, the tangential force fabric tensor is only defined for pair styles that apply tangential forces to particles, namely granular pair styles. It is calculated as

::: {.math .notranslate .nohighlight}
\\\[F\^t\_{ab} = \\frac{5}{\\mathrm{Tr}(N)} (T\_{ab} - \\frac{1}{3} \\mathrm{Tr}(T) \\delta\_{ab})\\\]
:::

where the tensor [\\(T\\)]{.math .notranslate .nohighlight} is defined as

::: {.math .notranslate .nohighlight}
\\\[T\_{ab} = \\sum\_{n = 1}\^{N_p} \\frac{1}{N_c (r\^2 + C\_{cd} r_c r_d)} \\frac{r\_{a} r\_{b}}{r\^2} f_t\\\]
:::

and [\\(f_t\\)]{.math .notranslate .nohighlight} is the magnitude of the tangential force between the two atoms.

The *type/include* keyword filters interactions based on the types of the two atoms. Interactions between two atoms are only included in calculations if the atom types are in the two lists. Each list consists of a series of type ranges separated by commas. The range can be specified as a single numeric value, or a wildcard asterisk can be used to specify a range of values. This takes the form "\*" or "\*n" or "m\*" or "m\*n". For example, if [\\(M\\)]{.math .notranslate .nohighlight} is the number of atom types, then an asterisk with no numeric values means all types from 1 to [\\(M\\)]{.math .notranslate .nohighlight}. A leading asterisk means all types from 1 to n (inclusive). A trailing asterisk means all types from m to [\\(M\\)]{.math .notranslate .nohighlight} (inclusive). A middle asterisk means all types from m to n (inclusive). Multiple *type/include* keywords may be added.
:::::::::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector of doubles and a global scalar. The vector stores the unique components of the first requested tensor in the order [\\(xx\\)]{.math .notranslate .nohighlight}, [\\(yy\\)]{.math .notranslate .nohighlight}, [\\(zz\\)]{.math .notranslate .nohighlight}, [\\(xy\\)]{.math .notranslate .nohighlight}, [\\(xz\\)]{.math .notranslate .nohighlight}, [\\(yz\\)]{.math .notranslate .nohighlight} followed by the same components for all subsequent tensors. The length of the vector is therefore six times the number of requested tensors. The scalar output is the number of pairwise interactions included in the calculation of the fabric tensor.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the GRANULAR package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

Currently, compute *fabric* does not support pair styles with many-body interactions. It also does not support models with long-range Coulombic or dispersion forces, i.e. the kspace_style command in LAMMPS. It also does not support the following fixes which add rigid-body constraints: [[fix shake]{.doc}]fix_shake.md){.reference .internal}, [[fix rattle]{.doc}]fix_shake.md){.reference .internal}, [[fix rigid]{.doc}]fix_rigid.md){.reference .internal}, [[fix rigid/small]{.doc}]fix_rigid.md){.reference .internal}. It does not support granular pair styles that extend beyond the contact of atomic radii (e.g., JKR and DMT).
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Ouadfel)** Ouadfel and Rothenburg "Stress-force-fabric relationship for assemblies of ellipsoids", Mechanics of Materials (2001). ([link to paper](https://doi.org/10.1016/S0167-6636(00)00057-0){.reference .external})
:::
::::::::::::::::::::::
:::::::::::::::::::::::
::::::::::::::::::::::::

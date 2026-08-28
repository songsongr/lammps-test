:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#compute-efield-atom-command .section}
[]{#index-0}

# compute efield/atom command[](#compute-efield-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID efield/atom keyword val
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- efield/atom = style name of this compute command

- zero or more keyword/value pairs may be appended

- keyword = *pair* or *kspace*

  ``` literal-block
  pair args = yes or no
  kspace args = yes or no
  ```
:::::

::::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all efield/atom
    compute 1 all efield/atom pair yes kspace no
:::
::::

Used in input scripts:

:::: {.highlight-none .notranslate}
::: highlight
    examples/PACKAGES/dielectric/in.confined
    examples/PACKAGES/dielectric/in.nopbc
:::
::::
:::::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the electric field at each atom in a group. The compute should only enabled with pair and kspace styles that are provided by the DIELECTRIC package because only these styles compute the per-atom electric field at every time step.

The electric field is a 3-component vector. The value of the electric field components will be 0.0 for atoms not in the specified compute group.

------------------------------------------------------------------------

The keyword/value option pairs are used in the following ways.

For the *pair* and *kspace* keywords, the real-space and reciprocal-space contributions to the electric field can be turned off and on.
:::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom vector, which can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The per-atom vector values will be in electric field [[units]{.doc}]units.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the DIELECTRIC package. It is only enabled if LAMMPS was built with that package.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dump custom]{.doc}]dump.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are pair = yes and kspace = yes.
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

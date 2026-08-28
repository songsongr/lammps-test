::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-msd-nongauss-command .section}
[]{#index-0}

# compute msd/nongauss command[](#compute-msd-nongauss-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID msd/nongauss keyword values ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- msd/nongauss = style name of this compute command

- zero or more keyword/value pairs may be appended

- keyword = *com*

  ``` literal-block
  com value = yes or no
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all msd/nongauss
    compute 1 upper msd/nongauss com yes
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the mean-squared displacement (MSD) and non-Gaussian parameter (NGP) of the group of atoms, including all effects due to atoms passing through periodic boundaries.

A vector of three quantities is calculated by this compute. The first element of the vector is the total squared displacement, [\\(dr\^2 = dx\^2 + dy\^2 + dz\^2\\)]{.math .notranslate .nohighlight}, of the atoms, and the second is the fourth power of these displacements, [\\(dr\^4 = (dx\^2 + dy\^2 + dz\^2)\^2\\)]{.math .notranslate .nohighlight}, summed and averaged over atoms in the group. The third component is the non-Gaussian diffusion parameter NGP,

::: {.math .notranslate .nohighlight}
\\\[\\text{NGP}(t) = \\frac{3\\left\\langle(r(t)-r(0))\^4\\right\\rangle} {5\\left\\langle(r(t)-r(0))\^2\\right\\rangle\^2} - 1.\\\]
:::

The NGP is a commonly used quantity in studies of dynamical heterogeneity. Its minimum theoretical value [\\((-0.4)\\)]{.math .notranslate .nohighlight} occurs when all atoms have the same displacement magnitude. [\\(\\text{NGP}=0\\)]{.math .notranslate .nohighlight} for Brownian diffusion, while [\\(\\text{NGP} \> 0\\)]{.math .notranslate .nohighlight} when some mobile atoms move faster than others.

If the *com* option is set to *yes* then the effect of any drift in the center-of-mass of the group of atoms is subtracted out before the displacement of each atom is calculated.

See the [[compute msd]{.doc}]compute_msd.md){.reference .internal} page for further important NOTEs, which also apply to this compute.
::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector of length 3, which can be accessed by indices 1--3 by any command that uses global vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The vector values are "intensive". The first vector value will be in distance[\\(\^2\\)]{.math .notranslate .nohighlight} [[units]{.doc}]units.md){.reference .internal}, the second is in distance[\\(\^4\\)]{.math .notranslate .nohighlight} units, and the third is dimensionless.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Compute *msd/nongauss* cannot be used with a dynamic group.

This compute is part of the EXTRA-COMPUTE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute msd]{.doc}]compute_msd.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option default is com = no.
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

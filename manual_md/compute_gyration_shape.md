:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#compute-gyration-shape-command .section}
[]{#index-0}

# compute gyration/shape command[](#compute-gyration-shape-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID gyration/shape compute-ID
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- gyration/shape = style name of this compute command

- compute-ID = ID of [[compute gyration]{.doc}]compute_gyration.md){.reference .internal} command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 molecule gyration/shape pe
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates the eigenvalues of the gyration tensor of a group of atoms and three shape parameters. The computation includes all effects due to atoms passing through periodic boundaries.

The three computed shape parameters are the asphericity, [\\(b\\)]{.math .notranslate .nohighlight}, the acylindricity, [\\(c\\)]{.math .notranslate .nohighlight}, and the relative shape anisotropy, [\\(k\\)]{.math .notranslate .nohighlight}, viz.,

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}b &= l_z - \\frac12(l_y+l_x) \\\\ c &= l_y - l_x \\\\ k &= \\frac{3}{2} \\frac{l_x\^2+l_y\^2+l_z\^2}{(l_x+l_y+l_z)\^2} - \\frac{1}{2}\\end{split}\\\]
:::

where [\\(l_x \\le l_y \\le l_z\\)]{.math .notranslate .nohighlight} are the three eigenvalues of the gyration tensor. A general description of these parameters is provided in [[(Mattice)]{.std .std-ref}](#mattice1){.reference .internal} while an application to polymer systems can be found in [[(Theodorou)]{.std .std-ref}](#theodorou1){.reference .internal}. The asphericity is always non-negative and zero only when the three principal moments are equal. This zero condition is met when the distribution of particles is spherically symmetric (hence the name asphericity) but also whenever the particle distribution is symmetric with respect to the three coordinate axes (e.g., when the particles are distributed uniformly on a cube, tetrahedron or other Platonic solid). The acylindricity is always non-negative and zero only when the two principal moments are equal. This zero condition is met when the distribution of particles is cylindrically symmetric (hence the name, acylindricity), but also whenever the particle distribution is symmetric with respect to the two coordinate axes (e.g., when the particles are distributed uniformly on a regular prism). The relative shape anisotropy is bounded between zero (if all points are spherically symmetric) and one (if all points lie on a line).

::: {.admonition .note}
Note

The coordinates of an atom contribute to the gyration tensor in "unwrapped" form, by using the image flags associated with each atom. See the [[dump custom]{.doc}]dump.md){.reference .internal} command for a discussion of "unwrapped" coordinates. See the Atoms section of the [[read_data]{.doc}]read_data.md){.reference .internal} command for a discussion of image flags and how they are set for each atom. You can reset the image flags (e.g., to 0) before invoking this compute by using the [[set image]{.doc}]set.md){.reference .internal} command.
:::
:::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector of length 6, which can be accessed by indices 1--6. The first three values are the eigenvalues of the gyration tensor followed by the asphericity, the acylindricity and the relative shape anisotropy. The computed values can be used by any command that uses global vector values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The vector values calculated by this compute are "intensive". The first five vector values will be in distance[\\(2\\)]{.math .notranslate .nohighlight} [[units]{.doc}]units.md){.reference .internal} while the sixth one is dimensionless.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EXTRA-COMPUTE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute gyration]{.doc}]compute_gyration.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Mattice)** Mattice, Suter, Conformational Theory of Large Molecules, Wiley, New York, 1994.

**(Theodorou)** Theodorou, Suter, Macromolecules, 18, 1206 (1985).
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

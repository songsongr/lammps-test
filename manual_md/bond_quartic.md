::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#bond-style-quartic-command .section}
[]{#index-1}[]{#index-0}

# bond_style quartic command[](#bond-style-quartic-command "Link to this heading"){.headerlink}

Accelerator Variants: *quartic/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style quartic
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    bond_style quartic
    bond_coeff 2 1200 -0.55 0.25 1.3 34.6878
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *quartic* bond style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = E_q + E\_{LJ} \\\\ E_q & = K (r - R_c)\^ 2 (r - R_c - B_1) (r - R_c - B_2) + U_0 \\\\ E\_{LJ} & = \\left\\{ \\begin{array} {l@{\\quad:\\quad}l} 4 \\epsilon \\left\[ \\left(\\frac{\\sigma}{r}\\right)\^{12} - \\left(\\frac{\\sigma}{r}\\right)\^6 \\right\] + \\epsilon & r \< 2\^{\\frac{1}{6}}, \\epsilon = 1, \\sigma = 1 \\\\ 0 & r \>= 2\^{\\frac{1}{6}} \\end{array} \\right.\\end{split}\\\]
:::

to define a bond that can be broken as the simulation proceeds (e.g. due to a polymer being stretched). The [\\(\\sigma\\)]{.math .notranslate .nohighlight} and [\\(\\epsilon\\)]{.math .notranslate .nohighlight} used in the LJ portion of the formula are both set equal to 1.0 by LAMMPS and the LJ portion is cut off at its minimum, i.e. at [\\(r_c = 2\^{\\frac{1}{6}}\\)]{.math .notranslate .nohighlight}.

The following coefficients must be defined for each bond type via the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- [\\(K\\)]{.math .notranslate .nohighlight} (energy/distance\^4)

- [\\(B_1\\)]{.math .notranslate .nohighlight} (distance)

- [\\(B_2\\)]{.math .notranslate .nohighlight} (distance)

- [\\(R_c\\)]{.math .notranslate .nohighlight} (distance)

- [\\(U_0\\)]{.math .notranslate .nohighlight} (energy)

This potential was constructed to mimic the FENE bond potential for coarse-grained polymer chains. When monomers with [\\(\\sigma = \\epsilon = 1.0\\)]{.math .notranslate .nohighlight} are used, the following choice of parameters gives a quartic potential that looks nearly like the FENE potential:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}K &= 1200 \\\\ B_1 &= -0.55 \\\\ B_2 &= 0.25 \\\\ R_c &= 1.3 \\\\ U_0 &= 34.6878\\end{split}\\\]
:::

Different parameters can be specified using the [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal} command, but you will need to choose them carefully so they form a suitable bond potential.

[\\(R_c\\)]{.math .notranslate .nohighlight} is the cutoff length at which the bond potential goes smoothly to a local maximum. If a bond length ever becomes [\\(\> R_c\\)]{.math .notranslate .nohighlight}, LAMMPS "breaks" the bond, which means two things. First, the bond potential is turned off by setting its type to 0, and is no longer computed. Second, a pairwise interaction between the two atoms is turned on, since they are no longer bonded. See the [[Howto]{.doc}]Howto_broken_bonds.md){.reference .internal} page on broken bonds for more information.

LAMMPS does the second task via a computational sleight-of-hand. It subtracts the pairwise interaction as part of the bond computation. When the bond breaks, the subtraction stops. For this to work, the pairwise interaction must always be computed by the [[pair_style]{.doc}]pair_style.md){.reference .internal} command, whether the bond is broken or not. This means that [[special_bonds]{.doc}]special_bonds.md){.reference .internal} must be set to 1,1,1, as indicated as a restriction below.

Note that when bonds are dumped to a file via the [[dump local]{.doc}]dump.md){.reference .internal} command, bonds with type 0 are not included. The [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal} command can also be used to query the status of broken bonds or permanently delete them, e.g.:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    delete_bonds all stats
    delete_bonds all bond 0 remove
:::
::::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This bond style can only be used if LAMMPS was built with the MOLECULE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The *quartic* style requires that [[special_bonds]{.doc}]special_bonds.md){.reference .internal} parameters be set to 1,1,1. Three- and four-body interactions (angle, dihedral, etc) cannot be used with *quartic* bonds.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}, [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

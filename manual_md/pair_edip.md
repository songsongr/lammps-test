:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#pair-style-edip-command .section}
[]{#index-2}[]{#index-1}[]{#index-0}

# pair_style edip command[](#pair-style-edip-command "Link to this heading"){.headerlink}

Accelerator Variants: *edip/omp*
:::

::::::::::::::: {#pair-style-edip-multi-command .section}
# pair_style edip/multi command[](#pair-style-edip-multi-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style style
:::
::::

- style = *edip* or *edip/multi*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style edip
    pair_coeff * * Si.edip Si
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *edip* and *edip/multi* styles compute a 3-body [[EDIP]{.std .std-ref}](#edip){.reference .internal} potential which is popular for modeling silicon materials where it can have advantages over other models such as the [[Stillinger-Weber]{.doc}]pair_sw.md){.reference .internal} or [[Tersoff]{.doc}]pair_tersoff.md){.reference .internal} potentials. The *edip* style has been programmed for single element potentials, while *edip/multi* supports multi-element EDIP runs.

In EDIP, the energy E of a system of atoms is

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = & \\sum\_{j \\ne i} \\phi\_{2}(R\_{ij}, Z\_{i}) + \\sum\_{j \\ne i} \\sum\_{k \\ne i,k \> j} \\phi\_{3}(R\_{ij}, R\_{ik}, Z\_{i}) \\\\ \\phi\_{2}(r, Z) = & A\\left\[\\left(\\frac{B}{r}\\right)\^{\\rho} - e\^{-\\beta Z\^2}\\right\]exp{\\left(\\frac{\\sigma}{r-a}\\right)} \\\\ \\phi\_{3}(R\_{ij}, R\_{ik}, Z_i) = & exp{\\left(\\frac{\\gamma}{R\_{ij}-a}\\right)}exp{\\left(\\frac{\\gamma}{R\_{ik}-a}\\right)}h(cos\\theta\_{ijk},Z_i) \\\\ Z_i = & \\sum\_{m \\ne i} f(R\_{im}) \\qquad f(r) = \\begin{cases} 1 & \\quad r\<c \\\\ \\exp\\left(\\frac{\\alpha}{1-x\^{-3}}\\right) & \\quad c\<r\<a \\\\ 0 & \\quad r\>a \\end{cases} \\\\ h(l,Z) = & \\lambda \[(1-e\^{-Q(Z)(l+\\tau(Z))\^2}) + \\eta Q(Z)(l+\\tau(Z))\^2 \] \\\\ Q(Z) = & Q_0 e\^{-\\mu Z} \\qquad \\tau(Z) = u_1 + u_2 (u_3 e\^{-u_4 Z} - e\^{-2u_4 Z})\\end{split}\\\]
:::

where [\\(\\phi_2\\)]{.math .notranslate .nohighlight} is a two-body term and [\\(\\phi_3\\)]{.math .notranslate .nohighlight} is a three-body term. The summations in the formula are over all neighbors J and K of atom I within a cutoff distance = a. Both terms depend on the local environment of atom I through its effective coordination number defined by Z, which is unity for a cutoff distance \< c and gently goes to 0 at distance = a.

Only a single pair_coeff command is used with the *edip* style which specifies a EDIP potential file with parameters for all needed elements. These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- N element names = mapping of EDIP elements to atom types

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for the potential file.

As an example, imagine a file Si.edip has EDIP values for Si.

EDIP files in the *potentials* directory of the LAMMPS distribution have a ".edip" suffix. Lines that are not blank or comments (starting with #) define parameters for a triplet of elements. The parameters in a single entry correspond to the two-body and three-body coefficients in the formula above:

- element 1 (the center atom in a 3-body interaction)

- element 2

- element 3

- A (energy units)

- B (distance units)

- cutoffA (distance units)

- cutoffC (distance units)

- [\\(\\alpha\\)]{.math .notranslate .nohighlight}

- [\\(\\beta\\)]{.math .notranslate .nohighlight}

- [\\(\\eta\\)]{.math .notranslate .nohighlight}

- [\\(\\gamma\\)]{.math .notranslate .nohighlight} (distance units)

- [\\(lambda\\)]{.math .notranslate .nohighlight} (energy units)

- [\\(\\mu\\)]{.math .notranslate .nohighlight}

- [\\(\\tau\\)]{.math .notranslate .nohighlight}

- [\\(\\sigma\\)]{.math .notranslate .nohighlight} (distance units)

- Q0

- u1

- u2

- u3

- u4

The A, B, beta, sigma parameters are used only for two-body interactions. The eta, gamma, lambda, mu, Q0 and all u1 to u4 parameters are used only for three-body interactions. The alpha and cutoffC parameters are used for the coordination environment function only.

The EDIP potential file must contain entries for all the elements listed in the pair_coeff command. It can also contain entries for additional elements not being used in a particular simulation; LAMMPS ignores those entries.

For a single-element simulation, only a single entry is required (e.g. SiSiSi). For a two-element simulation, the file must contain 8 entries (for SiSiSi, SiSiC, SiCSi, SiCC, CSiSi, CSiC, CCSi, CCC), that specify EDIP parameters for all permutations of the two elements interacting in three-body configurations. Thus for 3 elements, 27 entries would be required, etc.

At the moment, only a single element parameterization is implemented. However, the author is not aware of other multi-element EDIP parameterization. If you know any and you are interest in that, please contact the author of the EDIP package.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style can only be used if LAMMPS was built with the MANYBODY package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

This pair style requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

The EDIP potential files provided with LAMMPS (see the potentials directory) are parameterized for metal [[units]{.doc}]units.md){.reference .internal}. You can use the EDIP potential with any LAMMPS units, but you would need to create your own EDIP potential file with coefficients listed in the appropriate units if your simulation does not use "metal" units.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(EDIP)** J F Justo et al, Phys Rev B 58, 2539 (1998).
:::
:::::::::::::::
:::::::::::::::::
::::::::::::::::::

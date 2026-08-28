:::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::: {#pair-style-polymorphic-command .section}
[]{#index-0}

# pair_style polymorphic command[](#pair-style-polymorphic-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style polymorphic
:::
::::

style = *polymorphic*
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style polymorphic
    pair_coeff * * FeCH_BOP_I.poly Fe C H
    pair_coeff * * TlBr_msw.poly Tl Br
    pair_coeff * * CuTa_eam.poly Cu Ta
    pair_coeff * * GaN_tersoff.poly Ga N
    pair_coeff * * GaN_sw.poly Ga N
:::
::::
:::::

:::::::::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The *polymorphic* pair style computes a 3-body free-form potential ([[Zhou3]{.std .std-ref}](#zhou3){.reference .internal}) for the energy E of a system of atoms as

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E & = \\frac{1}{2}\\sum\_{i=1}\^{i=N}\\sum\_{j=1}\^{j=N}\\left\[\\left(1-\\delta\_{ij}\\right)\\cdot U\_{IJ}\\left(r\_{ij}\\right)-\\left(1-\\eta\_{ij}\\right)\\cdot F\_{IJ}\\left(X\_{ij}\\right)\\cdot V\_{IJ}\\left(r\_{ij}\\right)\\right\] \\\\ X\_{ij} & = \\sum\_{k=i_1,k\\neq j}\^{i_N}W\_{IK}\\left(r\_{ik}\\right)\\cdot G\_{JIK}\\left(\\cos\\theta\_{jik}\\right)\\cdot P\_{JIK}\\left(\\Delta r\_{jik}\\right) \\\\ \\Delta r\_{jik} & = r\_{ij}-\\xi\_{IJ}\\cdot r\_{ik}\\end{split}\\\]
:::

where I, J, K represent species of atoms i, j, and k, [\\(i_1, \..., i_N\\)]{.math .notranslate .nohighlight} represents a list of *i*'s neighbors, [\\(\\delta\_{ij}\\)]{.math .notranslate .nohighlight} is a Dirac constant (i.e., [\\(\\delta\_{ij} = 1\\)]{.math .notranslate .nohighlight} when [\\(i = j\\)]{.math .notranslate .nohighlight}, and [\\(\\delta\_{ij} = 0\\)]{.math .notranslate .nohighlight} otherwise), [\\(\\eta\_{ij}\\)]{.math .notranslate .nohighlight} is similar constant that can be set either to [\\(\\eta\_{ij} = \\delta\_{ij}\\)]{.math .notranslate .nohighlight} or [\\(\\eta\_{ij} = 1 - \\delta\_{ij}\\)]{.math .notranslate .nohighlight} depending on the potential type, [\\(U\_{IJ}(r\_{ij})\\)]{.math .notranslate .nohighlight}, [\\(V\_{IJ}(r\_{ij})\\)]{.math .notranslate .nohighlight}, [\\(W\_{IK}(r\_{ik})\\)]{.math .notranslate .nohighlight} are pair functions, [\\(G\_{JIK}(\\cos\\theta\_{jik})\\)]{.math .notranslate .nohighlight} is an angular function, [\\(P\_{JIK}(\\Delta r\_{jik})\\)]{.math .notranslate .nohighlight} is a function of atomic spacing differential [\\(\\Delta r\_{jik} = r\_{ij} - \\xi\_{IJ} \\cdot r\_{ik}\\)]{.math .notranslate .nohighlight} with [\\(\\xi\_{IJ}\\)]{.math .notranslate .nohighlight} being a pair-dependent parameter, and [\\(F\_{IJ}(X\_{ij})\\)]{.math .notranslate .nohighlight} is a function of the local environment variable [\\(X\_{ij}\\)]{.math .notranslate .nohighlight}. This generic potential is fully defined once the constants [\\(\\eta\_{ij}\\)]{.math .notranslate .nohighlight} and [\\(\\xi\_{IJ}\\)]{.math .notranslate .nohighlight}, and the six functions [\\(U\_{IJ}(r\_{ij})\\)]{.math .notranslate .nohighlight}, [\\(V\_{IJ}(r\_{ij})\\)]{.math .notranslate .nohighlight}, [\\(W\_{IK}(r\_{ik})\\)]{.math .notranslate .nohighlight}, [\\(G\_{JIK}(\\cos\\theta\_{jik})\\)]{.math .notranslate .nohighlight}, [\\(P\_{JIK}(\\Delta r\_{jik})\\)]{.math .notranslate .nohighlight}, and [\\(F\_{IJ}(X\_{ij})\\)]{.math .notranslate .nohighlight} are given. Here LAMMPS uses a global parameter [\\(\\eta\\)]{.math .notranslate .nohighlight} to represent [\\(\\eta\_{ij}\\)]{.math .notranslate .nohighlight}. When [\\(\\eta = 1\\)]{.math .notranslate .nohighlight}, [\\(\\eta\_{ij} = 1 - \\delta\_{ij}\\)]{.math .notranslate .nohighlight}, otherwise [\\(\\eta\_{ij} = \\delta\_{ij}\\)]{.math .notranslate .nohighlight}. Additionally, [\\(\\eta = 3\\)]{.math .notranslate .nohighlight} indicates that the function [\\(P\_{JIK}(\\Delta r)\\)]{.math .notranslate .nohighlight} depends on species I, J and K, otherwise [\\(P\_{JIK}(\\Delta r) = P\_{IK}(\\Delta r)\\)]{.math .notranslate .nohighlight} only depends on species I and K. Note that these six functions are all one dimensional, and hence can be provided in a tabular form. This allows users to design different potentials solely based on a manipulation of these functions. For instance, the potential reduces to a Stillinger-Weber potential ([[SW]{.std .std-ref}](#sw){.reference .internal}) if we set

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\eta\_{ij} & = \\delta\_{ij} (\\eta = 2\~or\~\\eta = 0),\\xi\_{IJ}=0 \\\\ U\_{IJ}\\left(r\\right) & = A\_{IJ}\\cdot\\epsilon\_{IJ}\\cdot \\left(\\frac{\\sigma\_{IJ}}{r}\\right)\^q\\cdot \\left\[B\_{IJ}\\cdot \\left(\\frac{\\sigma\_{IJ}}{r}\\right)\^{p-q}-1\\right\]\\cdot exp\\left(\\frac{\\sigma\_{IJ}}{r-a\_{IJ}\\cdot \\sigma\_{IJ}}\\right) \\\\ V\_{IJ}\\left(r\\right) & = \\sqrt{\\lambda\_{IJ}\\cdot \\epsilon\_{IJ}}\\cdot exp\\left(\\frac{\\gamma\_{IJ}\\cdot \\sigma\_{IJ}}{r-a\_{IJ}\\cdot \\sigma\_{IJ}}\\right) \\\\ F\_{IJ}\\left(X\\right) & = -X \\\\ P\_{JIK}\\left(\\Delta r\\right) & = P\_{IK}\\left(\\Delta r\\right) = 1 \\\\ W\_{IJ}\\left(r\\right) & = \\sqrt{\\lambda\_{IJ}\\cdot \\epsilon\_{IJ}}\\cdot exp\\left(\\frac{\\gamma\_{IJ}\\cdot \\sigma\_{IJ}}{r-a\_{IJ}\\cdot \\sigma\_{IJ}}\\right) \\\\ G\_{JIK}\\left(\\cos\\theta\\right) & = \\left(\\cos\\theta+\\frac{1}{3}\\right)\^2\\end{split}\\\]
:::

The potential reduces to a Tersoff potential ([[Tersoff]{.std .std-ref}](#tersoff){.reference .internal} or [[Albe1]{.std .std-ref}](#poly-albe){.reference .internal}) if we set

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\eta\_{ij} & = \\delta\_{ij} (\\eta = 2\~or\~\\eta = 0),\\xi\_{IJ}=1 \\\\ U\_{IJ}\\left(r\\right) & = \\frac{D\_{e,IJ}}{S\_{IJ}-1}\\cdot exp\\left\[-\\beta\_{IJ}\\sqrt{2S\_{IJ}}\\left(r-r\_{e,IJ}\\right)\\right\]\\cdot f\_{c,IJ}\\left(r\\right) \\\\ V\_{IJ}\\left(r\\right) & = \\frac{S\_{IJ}\\cdot D\_{e,IJ}}{S\_{IJ}-1}\\cdot exp\\left\[-\\beta\_{IJ}\\sqrt{\\frac{2}{S\_{IJ}}}\\left(r-r\_{e,IJ}\\right)\\right\]\\cdot f\_{c,IJ}\\left(r\\right) \\\\ F\_{IJ}\\left(X\\right) & = \\left(1+X\\right)\^{-\\frac{1}{2}} \\\\ P\_{JIK}\\left(\\Delta r\\right) & = P\_{IK}\\left(\\Delta r\\right) = exp\\left(2\\mu\_{IK}\\cdot \\Delta r\\right) \\\\ W\_{IJ}\\left(r\\right) & = f\_{c,IJ}\\left(r\\right) \\\\ G\_{JIK}\\left(\\cos\\theta\\right) & = \\gamma\_{IK}\\left\[1+\\frac{c\_{IK}\^2}{d\_{IK}\^2}-\\frac{c\_{IK}\^2}{d\_{IK}\^2+\\left(h\_{IK}+\\cos\\theta\\right)\^2}\\right\]\\end{split}\\\]
:::

where

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}f\_{c,IJ}\\left(r\\right)=\\left\\{\\begin{array}{l} 1, r\\leq R\_{IJ}-D\_{IJ} \\\\ \\frac{1}{2}+\\frac{1}{2}cos\\left\[\\frac{\\pi\\left(r+D\_{IJ}-R\_{IJ}\\right)}{2D\_{IJ}}\\right\], R\_{IJ}-D\_{IJ} \< r \< R\_{IJ}+D\_{IJ} \\\\ 0, r \\geq R\_{IJ}+D\_{IJ} \\end{array}\\right.\\end{split}\\\]
:::

The potential reduces to a modified Stillinger-Weber potential ([[Zhou3]{.std .std-ref}](#zhou3){.reference .internal}) if we set

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\eta\_{ij} & = \\delta\_{ij} (\\eta = 2\~or\~\\eta = 0),\\xi\_{IJ}=0 \\\\ U\_{IJ}\\left(r\\right) & = \\varphi\_{R,IJ}\\left(r\\right)-\\varphi\_{A,IJ}\\left(r\\right) \\\\ V\_{IJ}\\left(r\\right) & = u\_{IJ}\\left(r\\right) \\\\ F\_{IJ}\\left(X\\right) & = -X \\\\ P\_{JIK}\\left(\\Delta r\\right) & = P\_{IK}\\left(\\Delta r\\right) = 1 \\\\ W\_{IJ}\\left(r\\right) & = u\_{IJ}\\left(r\\right) \\\\ G\_{JIK}\\left(\\cos\\theta\\right) & = g\_{JIK}\\left(\\cos\\theta\\right)\\end{split}\\\]
:::

The potential reduces to a Rockett-Tersoff potential ([[Wang3]{.std .std-ref}](#wang3){.reference .internal}) if we set

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\eta\_{ij} & = \\delta\_{ij} (\\eta = 2\~or\~\\eta = 0),\\xi\_{IJ}=1 \\\\ U\_{IJ}\\left(r\\right) & = A\_{IJ}exp\\left(-\\lambda\_{1,IJ}\\cdot r\\right)f\_{c,IJ}\\left(r\\right)f\_{ca,IJ}\\left(r\\right) \\\\ V\_{IJ}\\left(r\\right) & = \\left\\{\\begin{array}{l}B\_{IJ}exp\\left(-\\lambda\_{2,IJ}\\cdot r\\right)f\_{c,IJ}\\left(r\\right)+ \\\\ A\_{IJ}exp\\left(-\\lambda\_{1,IJ}\\cdot r\\right)f\_{c,IJ}\\left(r\\right) \\left\[1-f\_{ca,IJ}\\left(r\\right)\\right\]\\end{array} \\right\\} \\\\ F\_{IJ}\\left(X\\right) & = \\left\[1+\\left(\\beta\_{IJ}X\\right)\^{n\_{IJ}}\\right\]\^{-\\frac{1}{2n\_{IJ}}} \\\\ P\_{JIK}\\left(\\Delta r\\right) & = P\_{IK}\\left(\\Delta r\\right) = exp\\left(\\lambda\_{3,IK}\\cdot \\Delta r\^3\\right) \\\\ W\_{IJ}\\left(r\\right) & = f\_{c,IJ}\\left(r\\right) \\\\ G\_{JIK}\\left(\\cos\\theta\\right) & = 1+\\frac{c\_{IK}\^2}{d\_{IK}\^2}-\\frac{c\_{IK}\^2}{d\_{IK}\^2+\\left(h\_{IK}+\\cos\\theta\\right)\^2}\\end{split}\\\]
:::

where [\\(f\_{ca,IJ}(r)\\)]{.math .notranslate .nohighlight} is similar to the [\\(f\_{c,IJ}(r)\\)]{.math .notranslate .nohighlight} defined above:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}f\_{ca,IJ}\\left(r\\right)=\\left\\{\\begin{array}{l} 1, r\\leq R\_{a,IJ}-D\_{a,IJ} \\\\ \\frac{1}{2}+\\frac{1}{2}cos\\left\[\\frac{\\pi\\left(r+D\_{a,IJ}-R\_{a,IJ}\\right)}{2D\_{a,IJ}}\\right\], R\_{a,IJ}-D\_{a,IJ} \< r \< R\_{a,IJ}+D\_{a,IJ} \\\\ 0, r \\geq R\_{a,IJ}+D\_{a,IJ} \\end{array}\\right.\\end{split}\\\]
:::

The potential becomes the embedded atom method ([[Daw]{.std .std-ref}](#poly-daw){.reference .internal}) if we set

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\eta\_{ij} & = 1-\\delta\_{ij} (\\eta = 1),\\xi\_{IJ}=0 \\\\ U\_{IJ}\\left(r\\right) & = \\phi\_{IJ}\\left(r\\right) \\\\ V\_{IJ}\\left(r\\right) & = 1 \\\\ F\_{II}\\left(X\\right) & = -2F_I\\left(X\\right) \\\\ P\_{JIK}\\left(\\Delta r\\right) & = P\_{IK}\\left(\\Delta r\\right) = 1 \\\\ W\_{IJ}\\left(r\\right) & = f\_{J}\\left(r\\right) \\\\ G\_{JIK}\\left(\\cos\\theta\\right) & = 1\\end{split}\\\]
:::

In the embedded atom method case, [\\(\\phi\_{IJ}(r)\\)]{.math .notranslate .nohighlight} is the pair energy, [\\(F_I(X)\\)]{.math .notranslate .nohighlight} is the embedding energy, *X* is the local electron density, and [\\(f_J(r)\\)]{.math .notranslate .nohighlight} is the atomic electron density function.

The potential reduces to another type of Tersoff potential ([[Zhou4]{.std .std-ref}](#zhou4){.reference .internal}) if we set

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\eta\_{ij} & = \\delta\_{ij} (\\eta = 3),\\xi\_{IJ}=1 \\\\ U\_{IJ}\\left(r\\right) & = \\frac{D\_{e,IJ}}{S\_{IJ}-1}\\cdot exp\\left\[-\\beta\_{IJ}\\sqrt{2S\_{IJ}}\\left(r-r\_{e,IJ}\\right)\\right\]\\cdot f\_{c,IJ}\\left(r\\right) \\cdot T\_{IJ}\\left(r\\right)+V\_{ZBL,IJ}\\left(r\\right)\\left\[1-T\_{IJ}\\left(r\\right)\\right\] \\\\ V\_{IJ}\\left(r\\right) & = \\frac{S\_{IJ}\\cdot D\_{e,IJ}}{S\_{IJ}-1}\\cdot exp\\left\[-\\beta\_{IJ}\\sqrt{\\frac{2}{S\_{IJ}}}\\left(r-r\_{e,IJ}\\right)\\right\]\\cdot f\_{c,IJ}\\left(r\\right) \\cdot T\_{IJ}\\left(r\\right) \\\\ F\_{IJ}\\left(X\\right) & = \\left(1+X\\right)\^{-\\frac{1}{2}} \\\\ P\_{JIK}\\left(\\Delta r\\right) & = \\omega\_{JIK} \\cdot exp\\left(\\alpha\_{JIK}\\cdot \\Delta r\\right) \\\\ W\_{IJ}\\left(r\\right) & = f\_{c,IJ}\\left(r\\right) \\\\ G\_{JIK}\\left(\\cos\\theta\\right) & = \\gamma\_{JIK}\\left\[1+\\frac{c\_{JIK}\^2}{d\_{JIK}\^2}-\\frac{c\_{JIK}\^2}{d\_{JIK}\^2+\\left(h\_{JIK}+\\cos\\theta\\right)\^2}\\right\] \\\\ T\_{IJ}\\left(r\\right) & = \\frac{1}{1+exp\\left\[-b\_{f,IJ}\\left(r-r\_{f,IJ}\\right)\\right\]} \\\\ V\_{ZBL,IJ}\\left(r\\right) & = 14.4 \\cdot \\frac{Z_I \\cdot Z_J}{r}\\sum\_{k=1}\^{4}\\mu_k \\cdot exp\\left\[-\\nu_k \\left(Z_I\^{0.23}+Z_J\^{0.23}\\right) r\\right\]\\end{split}\\\]
:::

where [\\(f\_{c,IJ}(r)\\)]{.math .notranslate .nohighlight} is the same as defined above. This Tersoff potential differs from the one above because the [\\(P\_{JIK}(\\Delta r)\\)]{.math .notranslate .nohighlight} function is now dependent on all three species I, J, and K.

If the tabulated functions are created using the parameters of Stillinger-Weber, Tersoff, and EAM potentials, the polymorphic pair style will produce the same global properties (energies and stresses) and the same forces as the [[sw]{.doc}]pair_sw.md){.reference .internal}, [[tersoff]{.doc}]pair_tersoff.md){.reference .internal}, and [[eam]{.doc}]pair_eam.md){.reference .internal} pair styles. The polymorphic pair style also produces the same per-atom properties (energies and stresses) as the corresponding [[tersoff]{.doc}]pair_tersoff.md){.reference .internal} and [[eam]{.doc}]pair_eam.md){.reference .internal} pair styles. However, due to a different partitioning of global properties to per-atom properties, the polymorphic pair style will produce different per-atom properties (energies and stresses) as the [[sw]{.doc}]pair_sw.md){.reference .internal} pair style. This does not mean that polymorphic pair style is different from the sw pair style. It just means that the definitions of the atom energies and atom stresses are different.

Only a single pair_coeff command is used with the polymorphic pair style which specifies a potential file for all needed elements. These are mapped to LAMMPS atom types by specifying N additional arguments after the filename in the pair_coeff command, where N is the number of LAMMPS atom types:

- filename

- N element names = mapping of polymorphic potential elements to atom types

See the pair_coeff page for alternate ways to specify the path for the potential file. Several files for polymorphic potentials are included in the potentials directory of the LAMMPS distribution. They have a "poly" suffix.

As an example, imagine the GaN_tersoff.poly file has tabulated functions for Ga-N tersoff potential. If your LAMMPS simulation has 4 atom types and you want the first 3 to be Ga, and the fourth to be N, you would use the following pair_coeff command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_coeff * * GaN_tersoff.poly Ga Ga Ga N
:::
::::

The first two arguments must be \* \* to span all pairs of LAMMPS atom types. The first three Ga arguments map LAMMPS atom types 1,2,3 to the Ga element in the polymorphic file. The final N argument maps LAMMPS atom type 4 to the N element in the polymorphic file. If a mapping value is specified as NULL, the mapping is not performed. This can be used when an polymorphic potential is used as part of the hybrid pair style. The NULL values are placeholders for atom types that will be used with other potentials.

Potential files in the potentials directory of the LAMMPS distribution have a ".poly" suffix. At the beginning of the files, an unlimited number of lines starting with '#' are used to describe the potential and are ignored by LAMMPS. The next line lists two numbers:

:::: {.highlight-none .notranslate}
::: highlight
    ntypes eta
:::
::::

Here *ntypes* represent total number of species defined in the potential file, [\\(\\eta = 1\\)]{.math .notranslate .nohighlight} reduces to embedded atom method, [\\(\\eta = 3\\)]{.math .notranslate .nohighlight} assumes a three species dependent [\\(P\_{JIK}(\\Delta r)\\)]{.math .notranslate .nohighlight} function, and all other values of [\\(\\eta\\)]{.math .notranslate .nohighlight} assume a two species dependent [\\(P\_{JK}(\\Delta r)\\)]{.math .notranslate .nohighlight} function. The value of *ntypes* must equal the total number of different species defined in the pair_coeff command. The next *ntypes* lines each lists two numbers and a character string representing atomic number, atomic mass, and name of the species of the ntypes elements:

:::: {.highlight-none .notranslate}
::: highlight
    atomic-number atomic-mass element-name(1)
    atomic-number atomic-mass element-name(2)
    ...
    atomic-number atomic-mass element-name(ntypes)
:::
::::

The next line contains four numbers:

:::: {.highlight-none .notranslate}
::: highlight
    nr ntheta nx xmax
:::
::::

Here nr is total number of tabular points for radial functions U, V, W, P, ntheta is total number of tabular points for the angular function G, nx is total number of tabular points for the function F, xmax is a maximum value of the argument of function F. Note that the pair functions [\\(U\_{IJ}(r)\\)]{.math .notranslate .nohighlight}, [\\(V\_{IJ}(r)\\)]{.math .notranslate .nohighlight}, [\\(W\_{IJ}(r)\\)]{.math .notranslate .nohighlight} are uniformly tabulated between 0 and cutoff distance of the IJ pair, [\\(G\_{JIK}(\\cos\\theta)\\)]{.math .notranslate .nohighlight} is uniformly tabulated between -1 and 1, [\\(P\_{JIK}(\\Delta r)\\)]{.math .notranslate .nohighlight} is uniformly tabulated between -rcmax and rcmax where rcmax is the maximum cutoff distance of all pairs, and [\\(F\_{IJ}(X)\\)]{.math .notranslate .nohighlight} is uniformly tabulated between 0 and xmax. Linear extrapolation is assumed if actual simulations exceed these ranges.

The next ntypes\*(ntypes+1)/2 lines contain two numbers:

``` literal-block
cut xi(1)
cut xi(2)
...
cut xi(ntypes*(ntypes+1)/2)
```

Here cut means the cutoff distance of the pair functions, "xi" is [\\(\\xi\\)]{.math .notranslate .nohighlight} as defined in the potential functions above. The ntypes\*(ntypes+1)/2 lines are related to the pairs according to the sequence of first ii (self) pairs, i = 1, 2, ..., ntypes, and then ij (cross) pairs, i = 1, 2, ..., ntypes-1, and j = i+1, i+2, ..., ntypes (i.e., the sequence of the ij pairs follows 11, 22, ..., 12, 13, 14, ..., 23, 24, ...).

In the final blocks of the potential file, U, V, W, P, G, and F functions are listed sequentially. First, U functions are given for each of the ntypes\*(ntypes+1)/2 pairs according to the sequence described above. For each of the pairs, nr values are listed. Next, similar arrays are given for V and W functions. If P functions depend only on pair species, i.e., [\\(\\eta \\neq 3\\)]{.math .notranslate .nohighlight}, then P functions are also listed the same way the next. If P functions depend on three species, i.e., [\\(\\eta = 3\\)]{.math .notranslate .nohighlight}, then P functions are listed for all the ntypes\*ntypes\*ntypes IJK triplets in a natural sequence I from 1 to ntypes, J from 1 to ntypes, and K from 1 to ntypes (i.e., IJK = 111, 112, 113, ..., 121, 122, 123 ..., 211, 212, ...). Next, G functions are listed for all the ntypes\*ntypes\*ntypes IJK triplets similarly. For each of the G functions, ntheta values are listed. Finally, F functions are listed for all the ntypes\*(ntypes+1)/2 pairs in the same sequence as described above. For each of the F functions, nx values are listed.
::::::::::::::::::::

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style does not write their information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

If using create_atoms command, atomic masses must be defined in the input script. If using read_data, atomic masses must be defined in the atomic structure data file.

This pair style is part of the MANYBODY package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair potential requires the [[newton]{.doc}]newton.md){.reference .internal} setting to be "on" for pair interactions.

The potential files provided with LAMMPS (see the potentials directory) are parameterized for metal [[units]{.doc}]units.md){.reference .internal}. You can use any LAMMPS units, but you would need to create your own potential files.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}

------------------------------------------------------------------------

**(Zhou3)** X. W. Zhou, M. E. Foster, R. E. Jones, P. Yang, H. Fan, and F. P. Doty, J. Mater. Sci. Res., 4, 15 (2015).

**(Zhou4)** X. W. Zhou, M. E. Foster, J. A. Ronevich, and C. W. San Marchi, J. Comp. Chem., 41, 1299 (2020).

**(SW)** F. H. Stillinger, and T. A. Weber, Phys. Rev. B, 31, 5262 (1985).

**(Tersoff)** J. Tersoff, Phys. Rev. B, 39, 5566 (1989).

**(Albe1)** K. Albe, K. Nordlund, J. Nord, and A. Kuronen, Phys. Rev. B, 66, 035205 (2002).

**(Wang)** J. Wang, and A. Rockett, Phys. Rev. B, 43, 12571 (1991).

**(Daw)** M. S. Daw, and M. I. Baskes, Phys. Rev. B, 29, 6443 (1984).
:::
::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::

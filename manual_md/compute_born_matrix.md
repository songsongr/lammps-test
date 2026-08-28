::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::: {#compute-born-matrix-command .section}
[]{#index-0}

# compute born/matrix command[](#compute-born-matrix-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID born/matrix keyword value ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- born/matrix = style name of this compute command

- zero or more keywords or keyword/value pairs may be appended

  ``` literal-block
  keyword = numdiff or pair or bond or angle or dihedral or improper
    numdiff values = delta virial-ID
      delta = magnitude of strain (dimensionless)
      virial-ID = ID of pressure compute for virial (string)
      (numdiff cannot be used with any other keyword)
    pair = compute pair-wise contributions
    bond = compute bonding contributions
    angle = compute angle contributions
    dihedral = compute dihedral contributions
    improper = compute improper contributions
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all born/matrix
    compute 1 all born/matrix bond angle
    compute 1 all born/matrix numdiff 1.0e-4 myvirial
:::
::::
:::::

:::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

Define a compute that calculates [\\(\\frac{\\partial{}\^2U}{\\partial\\varepsilon\_{i}\\partial\\varepsilon\_{j}},\\)]{.math .notranslate .nohighlight} the second derivatives of the potential energy [\\(U\\)]{.math .notranslate .nohighlight} with respect to the strain tensor [\\(\\varepsilon\\)]{.math .notranslate .nohighlight} elements. These values are related to:

::: {.math .notranslate .nohighlight}
\\\[C\^{B}\_{i,j}=\\frac{1}{V}\\frac{\\partial{}\^2U}{\\partial{}\\varepsilon\_{i}\\partial\\varepsilon\_{j}}\\\]
:::

also called the Born term of elastic constants in the stress-stress fluctuation formalism. This quantity can be used to compute the elastic constant tensor. Using the symmetric Voigt notation, the elastic constant tensor can be written as a 6x6 symmetric matrix:

::: {.math .notranslate .nohighlight}
\\\[C\_{i,j} = \\langle{}C\^{B}\_{i,j}\\rangle + \\frac{V}{k\_{B}T}\\left(\\langle\\sigma\_{i}\\sigma\_{j}\\rangle\\right. \\left.- \\langle\\sigma\_{i}\\rangle\\langle\\sigma\_{j}\\rangle\\right) + \\frac{Nk\_{B}T}{V} \\left(\\delta\_{i,j}+(\\delta\_{1,i}+\\delta\_{2,i}+\\delta\_{3,i})\\right. \\left.\*(\\delta\_{1,j}+\\delta\_{2,j}+\\delta\_{3,j})\\right)\\\]
:::

In the above expression, [\\(\\sigma\\)]{.math .notranslate .nohighlight} stands for the virial stress tensor, [\\(\\delta\\)]{.math .notranslate .nohighlight} is the Kronecker delta and the usual notation apply for the number of particle, the temperature and volume respectively [\\(N\\)]{.math .notranslate .nohighlight}, [\\(T\\)]{.math .notranslate .nohighlight} and [\\(V\\)]{.math .notranslate .nohighlight}. [\\(k\_{B}\\)]{.math .notranslate .nohighlight} is the Boltzmann constant. For a more detailed explanation of the terms appearing in the above equation, see [[(Lutsko)]{.std .std-ref}](#lutsko){.reference .internal}.

The Born term is a symmetric 6x6 matrix, as is the matrix of second derivatives of potential energy w.r.t strain, whose 21 independent elements are output in this order:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\begin{bmatrix} C\_{1} & C\_{7} & C\_{8} & C\_{9} & C\_{10} & C\_{11} \\\\ C\_{7} & C\_{2} & C\_{12} & C\_{13} & C\_{14} & C\_{15} \\\\ \\vdots & C\_{12} & C\_{3} & C\_{16} & C\_{17} & C\_{18} \\\\ \\vdots & C\_{13} & C\_{16} & C\_{4} & C\_{19} & C\_{20} \\\\ \\vdots & \\vdots & \\vdots & C\_{19} & C\_{5} & C\_{21} \\\\ \\vdots & \\vdots & \\vdots & \\vdots & C\_{21} & C\_{6} \\end{bmatrix}\\end{split}\\\]
:::

in this matrix the indices of [\\(C\_{k}\\)]{.math .notranslate .nohighlight} value are the corresponding element [\\(k\\)]{.math .notranslate .nohighlight} in the global vector output by this compute. Each term comes from the sum of the derivatives of every contribution to the potential energy in the system as explained in [[(VanWorkum)]{.std .std-ref}](#vanworkum){.reference .internal}.

The output can be accessed using the usual LAMMPS routines:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all born/matrix
    compute 2 all pressure NULL virial
    variable S1 equal -c_2[1]
    variable S2 equal -c_2[2]
    variable S3 equal -c_2[3]
    variable S4 equal -c_2[6]
    variable S5 equal -c_2[5]
    variable S6 equal -c_2[4]
    fix 1 all ave/time 1 1 1 v_S1 v_S2 v_S3 v_S4 v_S5 v_S6 c_1[*] file born.out
:::
::::

Note interchange of 4th and 6th stress values to satisfy Voigt notation. In this example, the file *born.out* will contain the information needed to compute the first and second terms of the elastic constant matrix in a post processing procedure. The third term depends only on *T*, which can be specified directly or estimated by sampling the atom velocities. Several examples of this method are provided in the examples/ELASTIC_T/BORN_MATRIX directory described on the [[Examples]{.doc}]Examples.md){.reference .internal} doc page.

NOTE: In the above [\\(C\_{i,j}\\)]{.math .notranslate .nohighlight} computation, the fluctuation term involving the virial stress tensor [\\(\\sigma\\)]{.math .notranslate .nohighlight} is the covariance between each elements. In a solid the stress fluctuations can vary rapidly, while average fluctuations can be slow to converge. A detailed analysis of the convergence rate of all the terms in the elastic tensor is provided in the paper by Clavier et al. [[(Clavier)]{.std .std-ref}](#clavier2){.reference .internal}.

Two different computation methods for the Born matrix are implemented in this compute and are mutually exclusive.

The first one is a direct computation from the analytical formula from the different terms of the potential used for the simulations [[(VanWorkum)]{.std .std-ref}](#vanworkum){.reference .internal}. However, the implementation of such derivations must be done for every potential form. This has not been done yet and can be very complicated for complex potentials. At the moment a warning message is displayed for every term that is not supporting the compute at the moment. This method is the default for now.

The second method uses finite differences of energy to numerically approximate the second derivatives [[(Zhen)]{.std .std-ref}](#zhen){.reference .internal}. This is useful when using interaction styles for which the analytical second derivatives have not been implemented. In this cases, the compute applies linear strain fields of magnitude *delta* to all the atoms relative to a point at the center of the box. The strain fields are in six different directions, corresponding to the six Cartesian components of the stress tensor defined by LAMMPS. For each direction it applies the strain field in both the positive and negative senses, and the new stress virial tensor of the entire system is calculated after each. The difference in these two virials divided by two times *delta*, approximates the corresponding components of the second derivative, after applying a suitable unit conversion.

::: {.admonition .note}
Note

It is important to choose a suitable value for delta, the magnitude of strains that are used to generate finite difference approximations to the exact virial stress. For typical systems, a value in the range of 1 part in 1e5 to 1e6 will be sufficient. However, the best value will depend on a multitude of factors including the stiffness of the interatomic potential, the thermodynamic state of the material being probed, and so on. The only way to be sure that you have made a good choice is to do a sensitivity study on a representative atomic configuration, sweeping over a wide range of values of delta. If delta is too small, the output values will vary erratically due to truncation effects. If delta is increased beyond a certain point, the output values will start to vary smoothly with delta, due to growing contributions from higher order derivatives. In between these two limits, the numerical virial values should be largely independent of delta.
:::

The keyword requires the additional arguments *delta* and *virial-ID*. *delta* gives the size of the applied strains. *virial-ID* gives the ID string of the pressure compute that provides the virial stress tensor, requiring that it use the virial keyword e.g.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute myvirial all pressure NULL virial
    compute 1 all born/matrix numdiff 1.0e-4 myvirial
:::
::::

**Output info:**

This compute calculates a global vector with 21 values that are the second derivatives of the potential energy with respect to strain. The values are in energy units. The values are ordered as explained above. These values can be used by any command that uses global values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.

The array values calculated by this compute are all "extensive".
::::::::::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EXTRA-COMPUTE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

The Born term can be decomposed as a product of two terms. The first one is a general term which depends on the configuration. The second one is specific to every interaction composing your force field (non-bonded, bonds, angle, ...). Currently not all LAMMPS interaction styles implement the *born_matrix* method giving first and second order derivatives and LAMMPS will exit with an error if this compute is used with such interactions unless the *numdiff* option is also used. The *numdiff* option cannot be used with any other keyword. In this situation, LAMMPS will also exit with an error.
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Van Workum)** K. Van Workum et al., J Chem Phys, 125, 144506 (2006).

**(Clavier)** G. Clavier, N. Desbiens, E. Bourasseau, V. Lachet, N. Brusselle-Dupend and B. Rousseau, Mol Sim, 43, 1413 (2017).

**(Zhen)** Y. Zhen, C. Chu, Comp Phys Comm, 183, 261-265 (2012).

**(Lutsko)** J. F. Lutsko, J Appl Phys, 65, 2991-2997 (1989).
:::
:::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::

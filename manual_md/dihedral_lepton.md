:::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::: {#dihedral-style-lepton-command .section}
[]{#index-1}[]{#index-0}

# dihedral_style lepton command[](#dihedral-style-lepton-command "Link to this heading"){.headerlink}

Accelerator Variants: *lepton/omp*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style lepton
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dihedral_style lepton

    dihedral_coeff  1 "k*(1 + d*cos(n*phi)); k=75.0; d=1; n=2"
    dihedral_coeff  2 "45*(1-cos(4*phi))"
    dihedral_coeff  2 "k2*cos(phi) + k3*cos(phi)^2; k2=100.0"
    dihedral_coeff  3 "k*(phi-phi0)^2; k=85.0; phi0=120.0"
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 8Feb2023.]{.versionmodified .added}
:::

Dihedral style *lepton* computes dihedral interactions between four atoms forming a dihedral angle with a custom potential function. The potential function must be provided as an expression string using "phi" as the dihedral angle variable. For example "200.0\*(phi-120.0)\^2" represents a [[quadratic dihedral]{.doc}]dihedral_quadratic.md){.reference .internal} potential around a 120 degree dihedral angle with a force constant *K* of 200.0 energy units:

::: {.math .notranslate .nohighlight}
\\\[U\_{dihedral,i} = K (\\phi_i - \\phi_0)\^2\\\]
:::

The [Lepton library](https://simtk.org/projects/lepton){.reference .external}, that the *lepton* dihedral style interfaces with, evaluates this expression string at run time to compute the pairwise energy. It also creates an analytical representation of the first derivative of this expression with respect to "phi" and then uses that to compute the force between the dihedral atoms as defined by the topology data.

The potential function expression for each dihedral type is provided via the [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal} command as in the example above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands. The expression is in energy units.

The Lepton expression must be either enclosed in quotes or must not contain any whitespace so that LAMMPS recognizes it as a single keyword. More on valid Lepton expressions below. Dihedral angles are internally computed in radians and thus the expression must assume "phi" is in radians.
:::::

------------------------------------------------------------------------

::::::::: {#lepton-expression-syntax-and-features .section}
## Lepton expression syntax and features[](#lepton-expression-syntax-and-features "Link to this heading"){.headerlink}

Lepton supports the following operators in expressions:

  ---- ----- -- ---- ---------- -- ---- ---------- -- --- -------- -- ---- -------
  \+   Add      \-   Subtract      \*   Multiply      /   Divide      \^   Power
  ---- ----- -- ---- ---------- -- ---- ---------- -- --- -------- -- ---- -------

The following mathematical functions are available:

  ---------- -------------------------------------- ---------- --------------------------------------
  sqrt(x)    Square root                            exp(x)     Exponential
  log(x)     Natural logarithm                      sin(x)     Sine (angle in radians)
  cos(x)     Cosine (angle in radians)              sec(x)     Secant (angle in radians)
  csc(x)     Cosecant (angle in radians)            tan(x)     Tangent (angle in radians)
  cot(x)     Cotangent (angle in radians)           asin(x)    Inverse sine (in radians)
  acos(x)    Inverse cosine (in radians)            atan(x)    Inverse tangent (in radians)
  sinh(x)    Hyperbolic sine                        cosh(x)    Hyperbolic cosine
  tanh(x)    Hyperbolic tangent                     erf(x)     Error function
  erfc(x)    Complementary Error function           abs(x)     Absolute value
  min(x,y)   Minimum of two values                  max(x,y)   Maximum of two values
  delta(x)   delta(x) is 1 for x = 0, otherwise 0   step(x)    step(x) is 0 for x \< 0, otherwise 1
  ---------- -------------------------------------- ---------- --------------------------------------

Numbers may be given in either decimal or exponential form. All of the following are valid numbers: 5, -3.1, 1e6, and 3.12e-2.

As an extension to the standard Lepton syntax, it is also possible to use LAMMPS [[variables]{.doc}]variable.md){.reference .internal} in the format "v_name". Before evaluating the expression, "v_name" will be replaced with the value of the variable "name". This is compatible with all kinds of scalar variables, but not with vectors, arrays, local, or per-atom variables. If necessary, a custom scalar variable needs to be defined that can access the desired (single) item from a non-scalar variable. As an example, the following lines will instruct LAMMPS to ramp the force constant for a harmonic bond from 100.0 to 200.0 during the next run:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable fconst equal ramp(100.0, 200)
    bond_style lepton
    bond_coeff 1 1.5 "v_fconst * (r^2)"
:::
::::

An expression may be followed by definitions for intermediate values that appear in the expression. A semicolon ";" is used as a delimiter between value definitions. For example, the expression:

:::: {.highlight-C .notranslate}
::: highlight
    a^2+a*b+b^2; a=a1+a2; b=b1+b2
:::
::::

is exactly equivalent to

:::: {.highlight-C .notranslate}
::: highlight
    (a1+a2)^2+(a1+a2)*(b1+b2)+(b1+b2)^2
:::
::::

The definition of an intermediate value may itself involve other intermediate values. Whitespace and quotation characters ('\'' and '"') are ignored. All uses of a value must appear *before* that value's definition. For efficiency reasons, the expression string is parsed, optimized, and then stored in an internal, pre-parsed representation for evaluation.

Evaluating a Lepton expression is typically between 2.5 and 5 times slower than the corresponding compiled and optimized C++ code. If additional speed or GPU acceleration (via GPU or KOKKOS) is required, the interaction can be represented as a table. Suitable table files can be created either internally using the [[pair_write]{.doc}]pair_write.md){.reference .internal} or [[bond_write]{.doc}]bond_write.md){.reference .internal} command or through the Python scripts in the [[tools/tabulate]{.std .std-ref}]Tools.md#tabulate){.reference .internal} folder.

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This dihedral style is part of the LEPTON package and only enabled if LAMMPS was built with this package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}, [[dihedral_style table]{.doc}]dihedral_table.md){.reference .internal}, [[bond_style lepton]{.doc}]bond_lepton.md){.reference .internal}, [[angle_style lepton]{.doc}]angle_lepton.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::::::::::
:::::::::::::::::::::::
::::::::::::::::::::::::

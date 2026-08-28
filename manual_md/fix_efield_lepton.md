::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::: {#fix-efield-lepton-command .section}
[]{#index-0}

# fix efield/lepton command[](#fix-efield-lepton-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID efield/lepton V ...
:::
::::

- ID, group-ID are documented in the [[fix]{.doc}]fix.md){.reference .internal} command

- style = *efield/lepton*

- V = electric potential (electric field \* distance units)

- V must be a Lepton expression (see below)

- zero or more keyword/value pairs may be appended to args

- keyword = *region* or *step*

  ``` literal-block
  region value = region-ID
    region-ID = ID of region atoms must be in to have effect
  step value = h
    h = step size for numerical differentiation (distance units)
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ex all efield/lepton "-E*x; E=1"
    fix dexx all efield/lepton "-0.5*x^2" step 1
    fix yukawa all efield/lepton "A*exp(-B*r)/r; r=abs(sqrt(x^2+y^2+z^2)); A=1; B=1" step 1e-6
    fix infp all efield/lepton "-abs(x)" step 1

    variable th equal 2*PI*ramp(0,1)
    fix erot all efield/lepton "-(x*cos(v_th)+y*sin(v_th))"
:::
::::
:::::

:::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4Feb2025.]{.versionmodified .added}
:::

Add an electric potential [\\(V\\)]{.math .notranslate .nohighlight} that applies to a group of charged atoms a force [\\(\\vec{F} = q \\vec{E}\\)]{.math .notranslate .nohighlight}, and to dipoles a force [\\(\\vec{F} = (\\vec{p} \\cdot \\nabla) \\vec{E}\\)]{.math .notranslate .nohighlight} and torque [\\(\\vec{T} = \\vec{p} \\times \\vec{E}\\)]{.math .notranslate .nohighlight}, where [\\(\\vec{E} = - \\nabla V\\)]{.math .notranslate .nohighlight}. The fix also evaluates the electrostatic energy ([\\(U\_{q} = q V\\)]{.math .notranslate .nohighlight} and [\\(U\_{p} = - \\vec{p} \\cdot \\vec{E}\\)]{.math .notranslate .nohighlight}) due to this potential when the [[fix_modify energy yes]{.doc}]fix_modify.md){.reference .internal} command is specified (see below).

::: {.admonition .note}
Note

This command should be used instead of [[fix efield]{.doc}]fix_efield.md){.reference .internal} if you want to impose a non-uniform electric field on a system with dipoles since the latter does not include the dipole force term. If you only have charges or if the electric field gradient is negligible, [[fix efield]{.doc}]fix_efield.md){.reference .internal} should be used since it is faster.
:::

The [Lepton library](https://simtk.org/projects/lepton){.reference .external}, that the *efield/lepton* fix style interfaces with, evaluates the expression string at run time to compute the energy, forces, and torques. It creates an analytical representation of [\\(V\\)]{.math .notranslate .nohighlight} and [\\(\\vec{E}\\)]{.math .notranslate .nohighlight}, while the gradient force is computed using a central difference scheme

::: {.math .notranslate .nohighlight}
\\\[\\vec{F} = \\frac{\|\\vec{p}\|}{2h} \\left\[ \\vec{E}(\\vec{x} + h \\hat{p}) - \\vec{E}(\\vec{x} - h \\hat{p}) \\right\] .\\\]
:::

The Lepton expression must be either enclosed in quotes or must not contain any whitespace so that LAMMPS recognizes it as a single keyword. More on valid Lepton expressions below. The final Lepton expression must be a function of only [\\(x, y, z\\)]{.math .notranslate .nohighlight}, which refer to the current *unwrapped* coordinates of the atoms to ensure continuity. Special care must be taken when using this fix with periodic boundary conditions or box-changing commands.
::::::

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

If the *region* keyword is used, the atom must also be in the specified geometric [[region]{.doc}]region.md){.reference .internal} in order to be affected by the potential.

The *step* keyword is required when [[atom_style dipole]{.doc}]atom_style.md){.reference .internal} is used and the electric field is non-uniform.
:::::::::

------------------------------------------------------------------------

:::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the potential energy defined above to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *virial* option is supported by this fix to add the contribution due to the added **\*forces\*** on charges and dipoles to both the global pressure and per-atom stress of the system via the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} and [[compute stress/atom]{.doc}]compute_stress_atom.md){.reference .internal} commands. The former can be accessed by [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify virial no]{.doc}]fix_modify.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix adding its forces. Default is the outermost level.

This fix computes a global scalar and a global 3-vector of forces, which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the potential energy discussed above. The vector is the total force added to the group of atoms. The scalar and vector values calculated by this fix are "extensive".

This fix cannot be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The forces due to this fix are imposed during an energy minimization, invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command. You should not specify force components with a variable that has time-dependence for use with a minimizer, since the minimizer increments the timestep as the iteration count during the minimization.

::: {.admonition .note}
Note

If you want the electric potential energy to be included in the total potential energy of the system (the quantity being minimized), you MUST enable the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option for this fix.
:::
::::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Fix style *efield/lepton* is part of the LEPTON package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix efield]{.doc}]fix_efield.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::::::::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::

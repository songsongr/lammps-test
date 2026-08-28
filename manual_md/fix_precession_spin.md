:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-precession-spin-command .section}
[]{#index-0}

# fix precession/spin command[](#fix-precession-spin-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group precession/spin style args
:::
::::

- ID, group are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- precession/spin = style name of this fix command

- style = *zeeman* or *anisotropy* or *cubic* or *stt*

  ``` literal-block
  zeeman args = H x y z
    H = intensity of the magnetic field (in Tesla)
    x y z = vector direction of the field
  anisotropy args = K x y z
    K = intensity of the magnetic anisotropy (in eV)
    x y z = vector direction of the anisotropy
  cubic args = K1 K2c n1x n1y n1x n2x n2y n2z n3x n3y n3z
    K1 and K2c = intensity of the magnetic anisotropy (in eV)
    n1x to n3z = three direction vectors of the cubic anisotropy
  stt args = J x y z
    J = intensity of the spin-transfer torque field
    x y z = vector direction of the field
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all precession/spin zeeman 0.1 0.0 0.0 1.0
    fix 1 3 precession/spin anisotropy 0.001 0.0 0.0 1.0
    fix 1 iron precession/spin cubic 0.001 0.0005 1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0
    fix 1 all precession/spin zeeman 0.1 0.0 0.0 1.0 anisotropy 0.001 0.0 0.0 1.0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix applies a precession torque to each magnetic spin in the group.

Style *zeeman* is used for the simulation of the interaction between the magnetic spins in the defined group and an external magnetic field:

::: {.math .notranslate .nohighlight}
\\\[H\_{Zeeman} = -g \\sum\_{i=0}\^{N}\\mu\_{i}\\, \\vec{s}\_{i} \\cdot\\vec{B}\_{ext}\\\]
:::

with:

- [\\(\\vec{B}\_{ext}\\)]{.math .notranslate .nohighlight} the external magnetic field (in T)

- [\\(g\\)]{.math .notranslate .nohighlight} the Lande factor (hard-coded as [\\(g=2.0\\)]{.math .notranslate .nohighlight})

- [\\(\\vec{s}\_i\\)]{.math .notranslate .nohighlight} the unitary vector describing the orientation of spin [\\(i\\)]{.math .notranslate .nohighlight}

- [\\(\\mu_i\\)]{.math .notranslate .nohighlight} the atomic moment of spin [\\(i\\)]{.math .notranslate .nohighlight} given as a multiple of the Bohr magneton [\\(\\mu_B\\)]{.math .notranslate .nohighlight} (for example, [\\(\\mu_i \\approx 2.2\\)]{.math .notranslate .nohighlight} in bulk iron).

The field value in Tesla is multiplied by the gyromagnetic ratio, [\\(g \\cdot \\mu_B/\\hbar\\)]{.math .notranslate .nohighlight}, converting it into a precession frequency in rad.THz (in metal units and with [\\(\\mu_B = 5.788\\cdot 10\^{-5}\\)]{.math .notranslate .nohighlight} eV/T).

As a comparison, the figure below displays the simulation of a single spin (of norm [\\(\\mu_i = 1.0\\)]{.math .notranslate .nohighlight}) submitted to an external magnetic field of [\\(\\vert B\_{ext}\\vert = 10.0\\; \\mathrm{Tesla}\\)]{.math .notranslate .nohighlight} (and oriented along the z axis). The upper plot shows the average magnetization along the external magnetic field axis and the lower plot the Zeeman energy, both as a function of temperature. The reference result is provided by the plot of the Langevin function for the same parameters.

[![](_images/zeeman_langevin.jpg){.align-center style="width: 600px;"}](_images/zeeman_langevin.jpg){.reference .internal .image-reference}

The temperature effects are accounted for by connecting the spin [\\(i\\)]{.math .notranslate .nohighlight} to a thermal bath using a Langevin thermostat (see [[fix langevin/spin]{.doc}]fix_langevin_spin.md){.reference .internal} for the definition of this thermostat).

Style *anisotropy* is used to simulate an easy axis or an easy plane for the magnetic spins in the defined group:

::: {.math .notranslate .nohighlight}
\\\[H\_{aniso} = -\\sum\_{{ i}=1}\^{N} K\_{an}(\\mathbf{r}\_{i})\\, \\left( \\vec{s}\_{i} \\cdot \\vec{n}\_{i} \\right)\^2\\\]
:::

with [\\(n\\)]{.math .notranslate .nohighlight} defining the direction of the anisotropy, and [\\(K\\)]{.math .notranslate .nohighlight} (in eV) its intensity. If [\\(K \> 0\\)]{.math .notranslate .nohighlight}, an easy axis is defined, and if [\\(K \< 0\\)]{.math .notranslate .nohighlight}, an easy plane is defined.

Style *cubic* is used to simulate a cubic anisotropy, with three possible easy axis for the magnetic spins in the defined group:

::: {.math .notranslate .nohighlight}
\\\[H\_{cubic} = -\\sum\_{{ i}=1}\^{N} K\_{1} \\Big\[ \\left(\\vec{s}\_{i} \\cdot \\vec{n}\_1 \\right)\^2 \\left(\\vec{s}\_{i} \\cdot \\vec{n}\_2 \\right)\^2 + \\left(\\vec{s}\_{i} \\cdot \\vec{n}\_2 \\right)\^2 \\left(\\vec{s}\_{i} \\cdot \\vec{n}\_3 \\right)\^2 + \\left(\\vec{s}\_{i} \\cdot \\vec{n}\_1 \\right)\^2 \\left(\\vec{s}\_{i} \\cdot \\vec{n}\_3 \\right)\^2 \\Big\] +K\_{2}\^{(c)} \\left(\\vec{s}\_{i} \\cdot \\vec{n}\_1 \\right)\^2 \\left(\\vec{s}\_{i} \\cdot \\vec{n}\_2 \\right)\^2 \\left(\\vec{s}\_{i} \\cdot \\vec{n}\_3 \\right)\^2\\\]
:::

with [\\(K_1\\)]{.math .notranslate .nohighlight} and [\\(K\_{2c}\\)]{.math .notranslate .nohighlight} (in eV) the intensity coefficients and [\\(\\vec{n}\_1\\)]{.math .notranslate .nohighlight}, [\\(\\vec{n}\_2\\)]{.math .notranslate .nohighlight} and [\\(\\vec{n}\_3\\)]{.math .notranslate .nohighlight} defining the three anisotropic directions defined by the command (from *n1x* to *n3z*). For [\\(\\vec{n}\_1 = (1 0 0)\\)]{.math .notranslate .nohighlight}, [\\(\\vec{n}\_2 = (0 1 0)\\)]{.math .notranslate .nohighlight}, and [\\(\\vec{n}\_3 = (0 0 1)\\)]{.math .notranslate .nohighlight}, [\\(K_1 \< 0\\)]{.math .notranslate .nohighlight} defines an iron type anisotropy (easy axis along the [\\((0 0 1)\\)]{.math .notranslate .nohighlight}-type cube edges), and [\\(K_1 \> 0\\)]{.math .notranslate .nohighlight} defines a nickel type anisotropy (easy axis along the [\\((1 1 1)\\)]{.math .notranslate .nohighlight}-type cube diagonals). [\\(K_2\^c \> 0\\)]{.math .notranslate .nohighlight} also defines easy axis along the [\\((1 1 1)\\)]{.math .notranslate .nohighlight}-type cube diagonals. See chapter 2 of [[(Skomski)]{.std .std-ref}](#skomski1){.reference .internal} for more details on cubic anisotropies.

Style *stt* is used to simulate the interaction between the spins and a spin-transfer torque. See equation (7) of [[(Chirac)]{.std .std-ref}](#chirac1){.reference .internal} for more details about the implemented spin-transfer torque term.

In all cases, the choice of [\\((x y z)\\)]{.math .notranslate .nohighlight} only imposes the vector directions for the forces. Only the direction of the vector is important; its length is ignored (the entered vectors are normalized).

Those styles can be combined within one single command.

::: {.admonition .note}
Note

The norm of all vectors defined with the precession/spin command have to be non-zero. For example, defining "fix 1 all precession/spin zeeman 0.1 0.0 0.0 0.0" would result in an error message. Since those vector components are used to compute the inverse of the field (or anisotropy) vector norm, setting a zero-vector would result in a division by zero.
:::
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the energy associated with the spin precession torque to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the potential energy (in energy units) discussed in the previous paragraph. The scalar value is an "extensive" quantity.

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *precession/spin* style is part of the SPIN package. This style is only enabled if LAMMPS was built with this package, and if the atom_style "spin" was declared. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[atom_style spin]{.doc}]atom_style.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Skomski)** Skomski, R. (2008). Simple models of magnetism. Oxford University Press.

**(Chirac)** Chirac, Theophile, et al. Ultrafast antiferromagnetic switching in NiO induced by spin transfer torques. Physical Review B 102.13 (2020): 134415.
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

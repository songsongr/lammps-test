:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#angle-style-mesocnt-command .section}
[]{#index-0}

# angle_style mesocnt command[](#angle-style-mesocnt-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style mesocnt
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style mesocnt
    angle_coeff 1 buckling C 10 10 20.0
    angle_coeff 4 harmonic C 8 4 10.0
    angle_coeff 2 buckling custom 400.0 50.0 5.0
    angle_coeff 1 harmonic custom 300.0
:::
::::
:::::

:::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 15Sep2022.]{.versionmodified .added}
:::

The *mesocnt* angle style uses the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}E = K\_\\text{H} \\Delta \\theta\^2, \\qquad \|\\Delta \\theta\| \< \\Delta \\theta\_\\text{B} \\\\ E = K\_\\text{H} \\Delta \\theta\_\\text{B}\^2 + K\_\\text{B} (\\Delta \\theta - \\Delta \\theta\_\\text{B}), \\qquad \|\\Delta \\theta\| \\geq \\Delta \\theta\_\\text{B}\\end{split}\\\]
:::

where [\\(\\Delta \\theta = \\theta - \\pi\\)]{.math .notranslate .nohighlight} is the bending angle of the nanotube, [\\(K\_\\text{H}\\)]{.math .notranslate .nohighlight} and [\\(K\_\\text{B}\\)]{.math .notranslate .nohighlight} are prefactors for the harmonic and linear regime respectively and [\\(\\Delta \\theta\_\\text{B}\\)]{.math .notranslate .nohighlight} is the buckling angle. Note that the usual 1/2 factor for the harmonic potential is included in [\\(K\_\\text{H}\\)]{.math .notranslate .nohighlight}.

The style implements parameterization presets of [\\(K\_\\text{H}\\)]{.math .notranslate .nohighlight}, [\\(K\_\\text{B}\\)]{.math .notranslate .nohighlight} and [\\(\\Delta \\theta\_\\text{B}\\)]{.math .notranslate .nohighlight} for mesoscopic simulations of carbon nanotubes based on the atomistic simulations of [[(Srivastava)]{.std .std-ref}](#srivastava-2){.reference .internal} and buckling considerations of [[(Zhigilei)]{.std .std-ref}](#zhigilei1-1){.reference .internal}.

The following coefficients must be defined for each angle type via the [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal} command as in the examples above, or in the data file or restart files read by the [[read_data]{.doc}]read_data.md){.reference .internal} or [[read_restart]{.doc}]read_restart.md){.reference .internal} commands:

- mode = *buckling* or *harmonic*

- preset = *C* or *custom*

- additional parameters depending on preset

If mode *harmonic* is chosen, the potential is simply harmonic and does not switch to the linear term when the buckling angle is reached. In *buckling* mode, the full piecewise potential is used.

Preset *C* is for carbon nanotubes, and the additional parameters are:

- chiral index [\\(n\\)]{.math .notranslate .nohighlight} (unitless)

- chiral index [\\(m\\)]{.math .notranslate .nohighlight} (unitless)

- [\\(r_0\\)]{.math .notranslate .nohighlight} (distance)

Here, [\\(r_0\\)]{.math .notranslate .nohighlight} is the equilibrium distance of the bonds included in the angle, see [[bond_style mesocnt]{.doc}]bond_mesocnt.md){.reference .internal}.

In harmonic mode with preset *custom*, the additional parameter is:

- [\\(K\_\\text{H}\\)]{.math .notranslate .nohighlight} (energy)

Hence, this setting is simply a wrapper for [[bond_style harmonic]{.doc}]bond_harmonic.md){.reference .internal} with an equilibrium angle of 180 degrees.

In harmonic mode with preset *custom*, the additional parameters are:

- [\\(K\_\\text{H}\\)]{.math .notranslate .nohighlight} (energy)

- [\\(K\_\\text{B}\\)]{.math .notranslate .nohighlight} (energy)

- [\\(\\Delta \\theta\_\\text{B}\\)]{.math .notranslate .nohighlight} (degrees)

[\\(\\Delta \\theta\_\\text{B}\\)]{.math .notranslate .nohighlight} is specified in degrees, but LAMMPS converts it to radians internally; hence [\\(K\_\\text{H}\\)]{.math .notranslate .nohighlight} is effectively energy per radian\^2 and [\\(K\_\\text{B}\\)]{.math .notranslate .nohighlight} is energy per radian.

------------------------------------------------------------------------

In *buckling* mode, this angle style adds the *buckled* property to all atoms in the simulation, which is an integer flag indicating whether the bending angle at a given atom has exceeded [\\(\\Delta \\theta\_\\text{B}\\)]{.math .notranslate .nohighlight}. It can be accessed as an atomic variable, e.g. for custom dump commands, as *i_buckled*.

::: {.admonition .note}
Note

If the initial state of the simulation contains buckled nanotubes and [[pair_style mesocnt]{.doc}]pair_mesocnt.md){.reference .internal} is used, the *i_buckled* atomic variable needs to be initialized before the pair_style is defined by doing a *run 0* command straight after the angle_style command. See below for an example.
:::

If CNTs are already buckled at the start of the simulation, this script will correctly initialize *i_buckled*:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    angle_style mesocnt
    angle_coeff 1 buckling C 10 10 20.0

    run 0

    pair_style mesocnt 60.0
    pair_coeff * * C_10_10.mesocnt 1
:::
::::
::::::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This angle style can only be used if LAMMPS was built with the MOLECULE and MESONT packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Srivastava)** Zhigilei, Wei, Srivastava, Phys. Rev. B 71, 165417 (2005).

**(Zhigilei)** Volkov and Zhigilei, ACS Nano 4, 6187 (2010).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

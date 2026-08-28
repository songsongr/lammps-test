:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#nemd-simulations .section}
# [10.2.7. ]{.section-number}NEMD simulations[](#nemd-simulations "Link to this heading"){.headerlink}

Non-equilibrium molecular dynamics or NEMD simulations are typically used to measure a fluid's rheological properties such as viscosity. In LAMMPS, such simulations can be performed by first setting up a non-orthogonal simulation box (see the preceding Howto section).

A shear strain can be applied to the simulation box at a desired strain rate by using the [[fix deform]{.doc}]fix_deform.md){.reference .internal} command. The [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal} command can be used to thermostat the sheared fluid and integrate the SLLOD equations of motion for the system. Fix nvt/sllod uses [[compute temp/deform]{.doc}]compute_temp_deform.md){.reference .internal} to compute a thermal temperature by subtracting out the streaming velocity of the shearing atoms. The velocity profile or other properties of the fluid can be monitored via the [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal} command.

::: {.admonition .note}
Note

A recent (2017) book by [[(Daivis and Todd)]{.std .std-ref}](#daivis-nemd){.reference .internal} discusses use of the SLLOD method and non-equilibrium MD (NEMD) thermostatting generally, for both simple and complex fluids, e.g. molecular systems. The latter can be tricky to do correctly.
:::

As discussed in the previous section on non-orthogonal simulation boxes, the amount of tilt or skew that can be applied is limited by LAMMPS for computational efficiency to be 1/2 of the parallel box length. However, [[fix deform]{.doc}]fix_deform.md){.reference .internal} can continuously strain a box by an arbitrary amount. As discussed in the [[fix deform]{.doc}]fix_deform.md){.reference .internal} command, when the tilt value reaches a limit, the box is flipped to the opposite limit which is an equivalent tiling of periodic space. The strain rate can then continue to change as before. In a long NEMD simulation these box re-shaping events may occur many times.

In a NEMD simulation, the "remap" option of [[fix deform]{.doc}]fix_deform.md){.reference .internal} should be set to "remap v", since that is what [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal} assumes to generate a velocity profile consistent with the applied shear strain rate. Alternatively, if the laboratory-frame velocity is not required (e.g. if only calculating viscosity), atom velocities can be stored in the peculiar frame using the "peculiar yes" flag of [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal}, which will typically give better performance. In this case, the velocity reported by LAMMPS is the velocity relative to the flow, the "remap" option of [[fix deform]{.doc}]fix_deform.md){.reference .internal} should be set to "remap none", and [[fix nvt/sllod]{.doc}]fix_nvt_sllod.md){.reference .internal} calculates temperature using [[compute temp]{.doc}]compute_temp.md){.reference .internal}.

An alternative method for calculating viscosities is provided via the [[fix viscosity]{.doc}]fix_viscosity.md){.reference .internal} command.

NEMD simulations can also be used to measure transport properties of a fluid through a pore or channel. Simulations of steady-state flow can be performed using the [[fix flow/gauss]{.doc}]fix_flow_gauss.md){.reference .internal} command.

------------------------------------------------------------------------

**(Daivis and Todd)** Daivis and Todd, Nonequilibrium Molecular Dynamics (book), Cambridge University Press, [https://doi.org/10.1017/9781139017848](https://doi.org/10.1017/9781139017848){.reference .external}, (2017).
::::
:::::
::::::

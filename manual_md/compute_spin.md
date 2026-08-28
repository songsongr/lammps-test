::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-spin-command .section}
[]{#index-0}

# compute spin command[](#compute-spin-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID spin
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- spin = style name of this compute command
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute out_mag all spin
:::
::::
:::::

::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a computation that calculates magnetic quantities for a system of atoms having spins.

This compute calculates the following 6 magnetic quantities:

- the three first quantities are the x,y and z coordinates of the total magnetization,

- the fourth quantity is the norm of the total magnetization,

- The fifth quantity is the magnetic energy (in eV),

- The sixth one is referred to as the spin temperature, according to the work of [[(Nurdin)]{.std .std-ref}](#nurdin1){.reference .internal}.

The simplest way to output the results of the compute spin calculation is to define some of the quantities as variables, and to use the thermo and thermo_style commands, for example:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute out_mag         all spin

    variable mag_z          equal c_out_mag[3]
    variable mag_norm       equal c_out_mag[4]
    variable temp_mag       equal c_out_mag[6]

    thermo                  10
    thermo_style            custom step v_mag_z v_mag_norm v_temp_mag
:::
::::

This series of commands evaluates the total magnetization along z, the norm of the total magnetization, and the magnetic temperature. Three variables are assigned to those quantities. The thermo and thermo_style commands print them every 10 timesteps.
:::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

The array values are "intensive". The array values will be in metal units ([[units]{.doc}]units.md){.reference .internal}).
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *spin* compute is part of the SPIN package. This compute is only enabled if LAMMPS was built with this package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. The atom_style has to be "spin" for this compute to be valid.

**Related commands:**

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Nurdin)** Nurdin and Schotte Phys Rev E, 61(4), 3579 (2000)
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-propel-self-command .section}
[]{#index-0}

# fix propel/self command[](#fix-propel-self-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID propel/self mode magnitude keyword values
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- propel/self = style name of this fix command

- mode = *dipole* or *velocity* or *quat*

- magnitude = magnitude of self-propulsion force

- zero or one keyword/value pairs may be appended

- keyword = *qvector*

  ``` literal-block
  qvector value = direction of force in ellipsoid frame
   sx, sy, sz = components of qvector
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix active all propel/self dipole 40.0
    fix active all propel/self velocity 10.0
    fix active all propel/self quat 15.7 qvector 1.0 0.0 0.0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Add a force to each atom in the group due to a self-propulsion force. The force is given by

::: {.math .notranslate .nohighlight}
\\\[F_i = f_P e_i\\\]
:::

where *i* is the particle the force is being applied to, [\\(f_P\\)]{.math .notranslate .nohighlight} is the magnitude of the force, and [\\(e_i\\)]{.math .notranslate .nohighlight} is the vector direction of the force. The specification of [\\(e_i\\)]{.math .notranslate .nohighlight} is based on which of the three keywords (*dipole* or *velocity* or *quat*) one selects.

For mode *dipole*, [\\(e_i\\)]{.math .notranslate .nohighlight} is just equal to the dipole vectors of the atoms in the group. Therefore, if the dipoles are not unit vectors, the [\\(e_i\\)]{.math .notranslate .nohighlight} will not be unit vectors.

::: {.admonition .note}
Note

If another command changes the magnitude of the dipole, this force will change accordingly (since [\\(\|e_i\|\\)]{.math .notranslate .nohighlight} will change, which is physically equivalent to re-scaling [\\(f_P\\)]{.math .notranslate .nohighlight} while keeping [\\(\|e_i\|\\)]{.math .notranslate .nohighlight} constant), and no warning will be provided by LAMMPS. This is almost never what you want, so ensure you are not changing dipole magnitudes with another LAMMPS fix or pair style. Furthermore, self-propulsion forces (almost) always set [\\(e_i\\)]{.math .notranslate .nohighlight} to be a unit vector for all times, so it's best to set all the dipole magnitudes to 1.0 unless you have a good reason not to (see the [[set]{.doc}]set.md){.reference .internal} command on how to do this).
:::

For mode *velocity*, [\\(e_i\\)]{.math .notranslate .nohighlight} points in the direction of the current velocity (a unit-vector). This can be interpreted as a velocity-dependent friction, as proposed by e.g. [[(Erdmann)]{.std .std-ref}](#erdmann1){.reference .internal}.

For mode *quat*, [\\(e_i\\)]{.math .notranslate .nohighlight} points in the direction of a unit vector, oriented in the coordinate frame of the ellipsoidal particles, which defaults to point along the x-direction. This default behavior can be changed by via the *quatvec* keyword.

The optional *quatvec* keyword specifies the direction of self-propulsion via a unit vector (sx,sy,sz). The arguments *sx*, *sy*, and *sz*, are defined within the coordinate frame of the atom's ellipsoid. For instance, for an ellipsoid with long axis along its x-direction, if one wanted the self-propulsion force to also be along this axis, set *sx* equal to 1 and *sy*, *sz* both equal to zero. This keyword may only be specified for mode *quat*.

::: {.admonition .note}
Note

In using keyword *quatvec*, the three arguments *sx*, *sy*, and *sz* will be automatically normalized to components of a unit vector internally to avoid users having to explicitly do so themselves. Therefore, in mode *quat*, the vectors [\\(e_i\\)]{.math .notranslate .nohighlight} will always be of unit length.
:::

Along with adding a force contribution, this fix can also contribute to the virial (pressure) of the system, defined as [\\(f_P \\sum_i \<e_i . r_i\>/(d V)\\)]{.math .notranslate .nohighlight}, where [\\(r_i\\)]{.math .notranslate .nohighlight} is the *unwrapped* coordinate of particle i in the case of periodic boundary conditions. See [[(Winkler)]{.std .std-ref}](#winkler1){.reference .internal} for a discussion of this active pressure contribution.

For modes *dipole* and *quat*, this fix is by default included in pressure computations.

For mode *velocity*, this fix is by default not included in pressure computations.

::: {.admonition .note}
Note

In contrast to equilibrium systems, pressure of active systems in general depends on the geometry of the container. The active pressure contribution as calculated in this fix is only valid for certain boundary conditions (spherical walls, rectangular walls, or periodic boundary conditions). For other geometries, the pressure must be measured via explicit calculation of the force per unit area on a wall, and so one must not calculate it using this fix. (Use [[fix_modify]{.doc}]fix_modify.md){.reference .internal} as described below to turn off the virial contribution of this fix). Again, see [[(Winkler)]{.std .std-ref}](#winkler1){.reference .internal} for discussion of why this is the case.

Furthermore, when dealing with active systems, the temperature is no longer well defined. Therefore, one should ensure that the *virial* flag is used in the [[compute pressure]{.doc}]compute_pressure.md){.reference .internal} command (turning off temperature contributions).
:::
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *virial* option is supported by this fix to add the contribution due to the added forces on atoms to the system's virial as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default is *virial yes* for keywords *dipole* and *quat*. The default is *virial no* for keyword *velocity*.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the BROWNIAN package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

With keyword *dipole*, this fix only works when the DIPOLE package is also enabled. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix align/self]{.doc}]fix_align_self.md){.reference .internal}, [[fix efield]{.doc}]fix_efield.md){.reference .internal}, [[fix setforce]{.doc}]fix_setforce.md){.reference .internal}, [[fix addforce]{.doc}]fix_addforce.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Erdmann)** U. Erdmann , W. Ebeling, L. Schimansky-Geier, and F. Schweitzer, Eur. Phys. J. B 15, 105-113, 2000.

**(Winkler)** Winkler, Wysocki, and Gompper, Soft Matter, 11, 6680 (2015).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

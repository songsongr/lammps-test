:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-align-self-command .section}
[]{#index-0}

# fix align/self command[](#fix-align-self-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID align/self mode magnitude keyword values
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- align/self = style name of this fix command

- mode = *dipole* or *quat*

- magnitude = magnitude of self-alignment torque

- zero or one keyword/value pairs may be appended

- keyword = *qvector*

  ``` literal-block
  qvector value = direction of self-propulsion force in ellipsoid frame
   sx, sy, sz = components of qvector
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix active all align/self dipole 40.0
    fix active all align/self quat 15.7 qvector 1.0 0.0 0.0
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 10Dec2025.]{.versionmodified .added}
:::

Add a torque to each atom in the group which accounts for the reorientation of each particle toward its own velocity, a generic phenomenon called self-alignment (see [[(Baconnier2025)]{.std .std-ref}](#baconnier2025){.reference .internal}). The torque is given by :

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{\\tau}\_i = \\zeta(\\mathbf{e}\_i \\times \\mathbf{v}\_i)\\\]
:::

where *i* is the particle the torque is being applied to, [\\(\\zeta\\)]{.math .notranslate .nohighlight} is the magnitude of the torque, [\\(\\mathbf{e}\_i\\)]{.math .notranslate .nohighlight} is the orientation of the particle, and [\\(\\mathbf{v}\_i\\)]{.math .notranslate .nohighlight} is its velocity. The self-alignment term, introduced in [[(Shimoyama1996)]{.std .std-ref}](#shimoyama1996){.reference .internal} with the study of collective motion in systems of self-propelled particles, is an effective torque arising from differential drag in asymmetric rigid bodies.

For mode *dipole*, [\\(e_i\\)]{.math .notranslate .nohighlight} is just equal to the dipole vectors of the atoms in the group. Therefore, if the dipoles are not unit vectors, the [\\(e_i\\)]{.math .notranslate .nohighlight} will not be unit vectors.

::: {.admonition .note}
Note

If another command changes the magnitude of the dipole, the applied torque will change accordingly and no warning will be provided by LAMMPS. This is almost never what you want, so ensure you are not changing dipole magnitudes with another LAMMPS fix or pair style. Furthermore, self-propulsion forces (almost) always set [\\(e_i\\)]{.math .notranslate .nohighlight} to be a unit vector for all times, so it's best to set all the dipole magnitudes to 1.0 unless you have a good reason not to (see the [[set]{.doc}]set.md){.reference .internal} command on how to do this).
:::

For mode *quat*, [\\(e_i\\)]{.math .notranslate .nohighlight} points in the direction of a unit vector, oriented in the coordinate frame of the ellipsoidal particles, which defaults to point along the x-direction. This default behavior can be changed by via the *qvector* keyword.

The optional *qvector* keyword specifies the direction of self-propulsion via a unit vector (sx,sy,sz). The arguments *sx*, *sy*, and *sz*, are defined within the coordinate frame of the atom's ellipsoid. For instance, for an ellipsoid with long axis along its x-direction, if one wanted the self-propulsion force to also be along this axis, set *sx* equal to 1 and *sy*, *sz* both equal to zero. This keyword may only be specified for mode *quat*.

::: {.admonition .note}
Note

In using keyword *qvector*, the three arguments *sx*, *sy*, and *sz* will be automatically normalized to components of a unit vector internally to avoid users having to explicitly do so themselves. Therefore, in mode *quat*, the vectors [\\(e_i\\)]{.math .notranslate .nohighlight} will always be of unit length.
:::
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}.

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the BROWNIAN package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.

The keyword *dipole* requires that atoms store torque as defined by the [[atom_style sphere]{.doc}]atom_style.md){.reference .internal} command, as well as a dipole moment as defined by the [[atom_style dipole]{.doc}]atom_style.md){.reference .internal} command which is part of the DIPOLE package. The keyword *quat* requires that atoms store torque and quaternions as defined by the [[atom_style ellipsoid]{.doc}]atom_style.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix propel/self]{.doc}]fix_propel_self.md){.reference .internal}, [[fix brownian]{.doc}]fix_brownian.md){.reference .internal}, [[fix addtorque/group]{.doc}]fix_addtorque_group.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Baconnier2025)** P. Baconnier, O. Dauchot, V. Demery, G. Duering, S. Henkes, C. Huepe, and A. Shee, Self-aligning polar active matter, Rev. Mod. Phys. 97, 015007 (2025).

**(Shimoyama1996)** N. Shimoyama, K. Sugawara, T. Mizuguchi, Y. Hayakawa, and M. Sano, Collective Motion in a System of Motile Elements, Phys. Rev. Lett. 76, 3870 (1996).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#fix-spring-rg-command .section}
[]{#index-0}

# fix spring/rg command[](#fix-spring-rg-command "Link to this heading"){.headerlink}

::::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID spring/rg K RG0
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- spring/rg = style name of this fix command

- K = harmonic force constant (force/distance units)

- RG0 = target radius of gyration to constrain to (distance units)

:::: {.highlight-none .notranslate}
::: highlight
    if RG0 = NULL, use the current RG as the target value
:::
::::
:::::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 protein spring/rg 5.0 10.0
    fix 2 micelle spring/rg 5.0 NULL
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Apply a harmonic restraining force to atoms in the group to affect their central moment about the center of mass (radius of gyration). This fix is useful to encourage a protein or polymer to fold/unfold and also when sampling along the radius of gyration as a reaction coordinate (i.e. for protein folding).

The radius of gyration is defined as RG in the first formula. The energy of the constraint and associated force on each atom is given by the second and third formulas, when the group is at a different RG than the target value RG0.

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}{R_G}\^2 & = \\frac{1}{M}\\sum\_{i}\^{N}{m\_{i}\\left( x\_{i} - \\frac{1}{M}\\sum\_{j}\^{N}{m\_{j}x\_{j}} \\right)\^{2}} \\\\ E & = K\\left( R_G - R\_{G0} \\right)\^{2} \\\\ F\_{i} & = 2K\\frac{m\_{i}}{M}\\left( 1-\\frac{R\_{G0}}{R_G} \\right)\\left( x\_{i} - \\frac{1}{M}\\sum\_{j}\^{N}{m\_{j}x\_{j}} \\right)\\end{split}\\\]
:::

The ([\\(x_i\\)]{.math .notranslate .nohighlight} - center-of-mass) term is computed taking into account periodic boundary conditions, [\\(m_i\\)]{.math .notranslate .nohighlight} is the mass of the atom, and *M* is the mass of the entire group. Note that K is thus a force constant for the aggregate force on the group of atoms, not a per-atom force.

If [\\(R\_{G0}\\)]{.math .notranslate .nohighlight} is specified as NULL, then the RG of the group is computed at the time the fix is specified, and that value is used as the target.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

This fix writes the currently used reference RG ([\\(R\_{G0}\\)]{.math .notranslate .nohighlight}) to [[binary restart files]{.doc}]restart.md){.reference .internal}. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for info on how to re-specify a fix in an input script that reads a restart file, so that the fix continues in an uninterrupted fashion.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the reference radius of gyration [\\(R\_{G0}\\)]{.math .notranslate .nohighlight} used by the fix. energy change due to this fix. The scalar value calculated by this fix is "intensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *respa* option is supported by this fix. This allows to set at which level of the [[r-RESPA]{.doc}]run_style.md){.reference .internal} integrator the fix is adding its forces. Default is the outermost level.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix spring]{.doc}]fix_spring.md){.reference .internal}, [[fix spring/self]{.doc}]fix_spring_self.md){.reference .internal} [[fix drag]{.doc}]fix_drag.md){.reference .internal}, [[fix smd]{.doc}]fix_smd.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

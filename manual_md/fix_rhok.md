::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#fix-rhok-command .section}
[]{#index-0}

# fix rhok command[](#fix-rhok-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID rhok nx ny nz K a
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nx, ny, nz = k-vector of collective density field

- K = spring constant of bias potential

- a = anchor point of bias potential
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix bias all rhok 16 0 0 4.0 16.0
    fix 1 all npt temp 0.8 0.8 4.0 z 2.2 2.2 8.0
    # output of 4 values from fix rhok: U_bias rho_k_RE  rho_k_IM  \|rho_k\|
    thermo_style custom step temp pzz lz f_bias f_bias[1] f_bias[2] f_bias[3]
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The fix applies a force to atoms given by the potential

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}U = & \\frac{1}{2} K (\|\\rho\_{\\vec{k}}\| - a)\^2 \\\\ \\rho\_{\\vec{k}} = & \\sum_j\^N \\exp(-i\\vec{k} \\cdot \\vec{r}\_j )/\\sqrt{N} \\\\ \\vec{k} = & (2\\pi n_x /L_x , 2\\pi n_y /L_y , 2\\pi n_z/L_z )\\end{split}\\\]
:::

as described in [[(Pedersen)]{.std .std-ref}](#pedersen){.reference .internal}.

This field, which biases configurations with long-range order, can be used to study crystal-liquid interfaces and determine melting temperatures [[(Pedersen)]{.std .std-ref}](#pedersen){.reference .internal}.

An example of using the interface pinning method is located in the *examples/PACKAGES/rhok* directory.
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}.

The [[fix_modify]{.doc}]fix_modify.md){.reference .internal} *energy* option is supported by this fix to add the potential energy calculated by the fix to the global potential energy of the system as part of [[thermodynamic output]{.doc}]thermo_style.md){.reference .internal}. The default setting for this fix is [[fix_modify energy no]{.doc}]fix_modify.md){.reference .internal}.

This fix computes a global scalar which can be accessed by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. The scalar is the potential energy discussed in the preceding paragraph. The scalar stored by this fix is "extensive".

No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[thermo_style]{.doc}]thermo_style.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Pedersen)** Pedersen, J. Chem. Phys., 139, 104102 (2013).
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

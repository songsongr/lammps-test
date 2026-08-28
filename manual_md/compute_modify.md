:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-modify-command .section}
[]{#index-0}

# compute_modify command[](#compute-modify-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute_modify compute-ID keyword value ...
:::
::::

- compute-ID = ID of the compute to modify

- one or more keyword/value pairs may be listed

- keyword = *extra/dof* or *dynamic/dof* or *temp*

  ``` literal-block
  extra/dof value = N
    N = # of extra degrees of freedom to subtract
  dynamic/dof value = yes or no
    yes/no = do or do not re-compute the number of degrees of freedom (DOF) contributing to the temperature
  temp value = compute ID that calculates a temperature
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute_modify myTemp extra/dof 0
    compute_modify newtemp dynamic/dof yes extra/dof 600
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Modify one or more parameters of a previously defined compute. Not all compute styles support all parameters.

The *extra/dof* keyword refers to how many degrees of freedom are subtracted (typically from [\\(3N\\)]{.math .notranslate .nohighlight}) as a normalizing factor in a temperature computation. Only computes that compute a temperature use this option. The default is 2 or 3 for [[2d or 3d systems]{.doc}]dimension.md){.reference .internal} which is a correction factor for an ensemble of velocities with zero total linear momentum. For compute temp/partial, if one or more velocity components are excluded, the value used for *extra/dof* is scaled accordingly. You can use a negative number for the *extra/dof* parameter if you need to add degrees-of-freedom. See the [[compute temp/asphere]{.doc}]compute_temp_asphere.md){.reference .internal} command for an example.

The *dynamic/dof* keyword determines whether the number of atoms [\\(N\\)]{.math .notranslate .nohighlight} in the compute group and their associated degrees of freedom (DOF) are re-computed each time a temperature is computed. Only compute styles that calculate a temperature use this option. By default, [\\(N\\)]{.math .notranslate .nohighlight} and their DOF are assumed to be constant. If you are adding atoms or molecules to the system (see the [[fix pour]{.doc}]fix_pour.md){.reference .internal}, [[fix deposit]{.doc}]fix_deposit.md){.reference .internal}, and [[fix gcmc]{.doc}]fix_gcmc.md){.reference .internal} commands) or expect atoms or molecules to be lost (e.g. due to exiting the simulation box or via [[fix evaporate]{.doc}]fix_evaporate.md){.reference .internal}), then this option should be used to ensure the temperature is correctly normalized.

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

The *temp* keyword is used with [[compute temp/deform]{.doc}]compute_temp_deform.md){.reference .internal} to change the internal temperature compute.
::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute]{.doc}]compute.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are extra/dof = 2 or 3 for 2d or 3d systems, respectively, and dynamic/dof = *no*.
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

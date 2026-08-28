::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::: {#compute-nbond-atom-command .section}
[]{#index-0}

# compute nbond/atom command[](#compute-nbond-atom-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID nbond/atom keyword value
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- nbond/atom = style name of this compute command

- zero or more keyword/value pairs may be appended

- keyword = *bond/type*

  ``` literal-block
  bond/type value = btype
    btype = bond type included in count
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all nbond/atom
    compute 1 all nbond/atom bond/type 2
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

Define a computation that computes the number of bonds each atom is part of. Bonds which are broken are not counted in the tally. See the [[Howto broken bonds]{.doc}]Howto_bpm.md){.reference .internal} page for more information. The number of bonds will be zero for atoms not in the specified compute group. This compute does not depend on Newton bond settings.

If the keyword *bond/type* is specified, only bonds of *btype* are counted.
::::

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a per-atom vector, which can be accessed by any command that uses per-atom values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} doc page for an overview of LAMMPS output options.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the BPM package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::
::::::::::::::::
:::::::::::::::::

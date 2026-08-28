:::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::: {#fix-nonaffine-displacement-command .section}
[]{#index-0}

# fix nonaffine/displacement command[](#fix-nonaffine-displacement-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-none .notranslate}
::: highlight
    fix ID group nonaffine/displacement nevery style args reference/style nstep keyword values
:::
::::

- ID, group are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- nonaffine/displacement = style name of this fix command

- nevery = calculate nonaffine displacement every this many timesteps

- style = *d2min* or *integrated*

  ``` literal-block
  d2min args = cutoff args
    cutoff = type or radius or custom
      type args = none, cutoffs determined by atom types
      radius args = none, cutoffs determined based on atom diameters (atom style sphere)
      custom args = rmax, cutoff set by a constant numeric value rmax (distance units)
  integrated args = none
  ```

- reference/style = *fixed* or *update* or *offset*

  ``` literal-block
  fixed = use a fixed reference frame at nstep
  update = update the reference frame every nstep timesteps
  offset = update the reference frame nstep timesteps before calculating the nonaffine displacement
  ```

- zero or more keyword/value pairs may be appended

  ``` literal-block
  z/min values = zmin
    zmin = minimum coordination number to calculate D2min
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all nonaffine/displacement 100 integrated update 100
    fix 1 all nonaffine/displacement 1000 d2min type fixed 0
    fix 1 all nonaffine/displacement 1000 d2min custom 2.0 offset 100
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 7Feb2024.]{.versionmodified .added}
:::

This fix computes different metrics of the nonaffine displacement of particles. The first metric, *d2min* calculates the [\\(D\^2\_\\mathrm{min}\\)]{.math .notranslate .nohighlight} nonaffine displacement by Falk and Langer in [[(Falk)]{.std .std-ref}](#d2min-falk){.reference .internal}. For each atom, the fix computes the two tensors

::: {.math .notranslate .nohighlight}
\\\[X = \\sum\_{\\mathrm{neighbors}} \\vec{r} \\left(\\vec{r}\_{0} \\right)\^T\\\]
:::

and

::: {.math .notranslate .nohighlight}
\\\[Y = \\sum\_{\\mathrm{neighbors}} \\vec{r}\_0 \\left(\\vec{r}\_{0} \\right)\^T\\\]
:::

where the neighbors include all other atoms within the distance criterion set by the cutoff option, discussed below, [\\(\\vec{r}\\)]{.math .notranslate .nohighlight} is the current displacement between particles, and [\\(\\vec{r}\_0\\)]{.math .notranslate .nohighlight} is the reference displacement. A deformation gradient tensor is then calculated as [\\(F = X Y\^{-1}\\)]{.math .notranslate .nohighlight} from which

::: {.math .notranslate .nohighlight}
\\\[D\^2\_\\mathrm{min} = \\sum\_{\\mathrm{neighbors}} \\left\| \\vec{r} - F \\vec{r}\_0 \\right\|\^2\\\]
:::

and a strain tensor is calculated [\\(E = F F\^{T} - I\\)]{.math .notranslate .nohighlight} where [\\(I\\)]{.math .notranslate .nohighlight} is the identity tensor. This calculation is only performed on timesteps that are a multiple of *nevery* (including timestep zero). Data accessed before this occurs will simply be zeroed.

For particles with low coordination numbers, calculations of [\\(D\^2\_\\mathrm{min}\\)]{.math .notranslate .nohighlight} may not be accurate. An optional minimum coordination number can be defined using the *z/min* keyword. If any particle has fewer than the specified number of particles in the cutoff distance or in contact, the above calculations will be skipped and the corresponding peratom array entries will be zero.

The *integrated* style simply integrates the velocity of particles every timestep to calculate a displacement. This style only works if used in conjunction with another fix that deforms the box and displaces atom positions such as [[fix deform]{.doc}]fix_deform.md){.reference .internal} with remap x, [[fix press/berendsen]{.doc}]fix_press_berendsen.md){.reference .internal}, or [[fix nh]{.doc}]fix_nh.md){.reference .internal}.

Both of these methods require defining a reference state. With the *fixed* reference style, the user picks a specific timestep *nstep* at which particle positions are saved. If peratom data is accessed from this compute prior to this timestep, it will simply be zeroed. The *update* reference style implies the reference state will be updated every *nstep* timesteps. The *offset* reference will update the reference state *nstep* timesteps before a multiple of *nevery* timesteps.
:::::::

------------------------------------------------------------------------

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

The reference state is saved to [[binary restart files]{.doc}]restart.md){.reference .internal}.

None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix.

This fix computes a peratom array with either 3 or 9 columns, which can be accessed by indices 1-9 using any command that uses per-atom values from a fix as input.

For the *integrated* style, the three columns are the nonaffine displacements in the x, y, and z directions. For the *d2min* style, the first three columns are the calculated [\\(\\sqrt{D\^2\_\\mathrm{min}}\\)]{.math .notranslate .nohighlight}, the volumetric strain, and the deviatoric strain. The following 6 columns are the xx, yy, zz, xy, xz, and yz components of the calculated strain tensor.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This compute is part of the EXTRA-FIX package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

As this fix depends on a run including specific reference timesteps, it currently does not update peratom values if used in conjunction with the [[rerun command]{.doc}]rerun.md){.reference .internal} since it cannot ensure the necessary reference timesteps are included.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Falk)** Falk and Langer PRE, 57, 7192 (1998).
:::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::

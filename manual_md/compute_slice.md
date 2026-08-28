:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#compute-slice-command .section}
[]{#index-0}

# compute slice command[](#compute-slice-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute ID group-ID slice Nstart Nstop Nskip input1 input2 ...
:::
::::

- ID, group-ID are documented in [[compute]{.doc}]compute.md){.reference .internal} command

- slice = style name of this compute command

- Nstart = starting index within input vector(s)

- Nstop = stopping index within input vector(s)

- Nskip = extract every Nskip elements from input vector(s)

- input = c_ID, c_ID\[N\], f_ID, f_ID\[N\]

  :::: {.highlight-none .notranslate}
  ::: highlight
      c_ID = global vector calculated by a compute with ID
      c_ID[I] = Ith column of global array calculated by a compute with ID
      f_ID = global vector calculated by a fix with ID
      f_ID[I] = Ith column of global array calculated by a fix with ID
      v_name = vector calculated by an vector-style variable with name
  :::
  ::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    compute 1 all slice 1 100 10 c_msdmol[4]
    compute 1 all slice 301 400 1 c_msdmol[4] v_myVec
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Define a calculation that "slices" one or more vector inputs into smaller vectors, one per listed input. The inputs can be global quantities; they cannot be per-atom or local quantities. [[Computes]{.doc}]compute.md){.reference .internal} and [[fixes]{.doc}]fix.md){.reference .internal} and vector-style [[variables]{.doc}]variable.md){.reference .internal} can generate such global quantities. The group specified with this command is ignored.

The values extracted from the input vector(s) are determined by the *Nstart*, *Nstop*, and *Nskip* parameters. The elements of an input vector of length N are indexed from 1 to N. Starting at element *Nstart*, every Mth element is extracted, where M = *Nskip*, until element *Nstop* is reached. The extracted quantities are stored as a vector, which is typically shorter than the input vector.

Each listed input is operated on independently to produce one output vector. Each listed input must be a global vector or column of a global array calculated by another [[compute]{.doc}]compute.md){.reference .internal} or [[fix]{.doc}]fix.md){.reference .internal}.

If an input value begins with "c\_", a compute ID must follow which has been previously defined in the input script and which generates a global vector or array. See the individual [[compute]{.doc}]compute.md){.reference .internal} doc page for details. If no bracketed integer is appended, the vector calculated by the compute is used. If a bracketed integer is appended, the Ith column of the array calculated by the compute is used. Users can also write code for their own compute styles and [[add them to LAMMPS]{.doc}]Modify.md){.reference .internal}.

If a value begins with "f\_", a fix ID must follow which has been previously defined in the input script and which generates a global vector or array. See the individual [[fix]{.doc}]fix.md){.reference .internal} page for details. Note that some fixes only produce their values on certain timesteps, which must be compatible with when compute slice references the values, else an error results. If no bracketed integer is appended, the vector calculated by the fix is used. If a bracketed integer is appended, the Ith column of the array calculated by the fix is used. Users can also write code for their own fix style and [[add them to LAMMPS]{.doc}]Modify.md){.reference .internal}.

If an input value begins with "v\_", a variable name must follow which has been previously defined in the input script. Only vector-style variables can be referenced. See the [[variable]{.doc}]variable.md){.reference .internal} command for details. Note that variables of style *vector* define a formula which can reference individual atom properties or thermodynamic keywords, or they can invoke other computes, fixes, or variables when they are evaluated, so this is a very general means of specifying quantities to slice.

If a single input is specified this compute produces a global vector, even if the length of the vector is 1. If multiple inputs are specified, then a global array of values is produced, with the number of columns equal to the number of inputs specified.
:::

------------------------------------------------------------------------

::: {#output-info .section}
## Output info[](#output-info "Link to this heading"){.headerlink}

This compute calculates a global vector if a single input value is specified or a global array with N columns where N is the number of inputs. The length of the vector or the number of rows in the array is equal to the number of values extracted from each input vector. These values can be used by any command that uses global vector or array values from a compute as input. See the [[Howto output]{.doc}]Howto_output.md){.reference .internal} page for an overview of LAMMPS output options.

The vector or array values calculated by this compute are simply copies of values generated by computes or fixes or variables that are input vectors to this compute. If there is a single input vector of intensive and/or extensive values, then each value in the vector of values calculated by this compute will be "intensive" or "extensive", depending on the corresponding input value. If there are multiple input vectors, and all the values in them are intensive, then the array values calculated by this compute are "intensive". If there are multiple input vectors, and any value in them is extensive, then the array values calculated by this compute are "extensive". Values produced by a variable are treated as intensive.

The vector or array values will be in whatever [[units]{.doc}]units.md){.reference .internal} the input quantities are in.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

none
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[compute]{.doc}]compute.md){.reference .internal}, [[fix]{.doc}]fix.md){.reference .internal}, [[compute reduce]{.doc}]compute_reduce.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

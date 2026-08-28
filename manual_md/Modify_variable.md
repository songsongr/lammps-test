::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#variable-options .section}
# [3.18. ]{.section-number}Variable options[](#variable-options "Link to this heading"){.headerlink}

The [`Variable`{.docutils .literal .notranslate}]{.pre} class computes and stores [[variable]{.doc}]variable.md){.reference .internal} information in LAMMPS; see the file [`variable.cpp`{.docutils .literal .notranslate}]{.pre}. The value associated with a variable can be periodically printed to the screen via the [[print]{.doc}]print.md){.reference .internal}, [[fix print]{.doc}]fix_print.md){.reference .internal}, or [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} commands. Variables of style "equal" can compute complex equations that involve the following types of arguments:

:::: {.highlight-none .notranslate}
::: highlight
    thermo keywords = ke, vol, atoms, ...
    other variables = v_a, v_myvar, ...
    math functions = div(x,y), mult(x,y), add(x,y), ...
    group functions = mass(group), xcm(group,x), ...
    atom values = x[123], y[3], vx[34], ...
    compute values = c_mytemp[0], c_thermo_press[3], ...
:::
::::

Adding keywords for the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command (which can then be accessed by variables) is discussed in the [[Modify thermo]{.doc}]Modify_thermo.md){.reference .internal} documentation.

Adding a new math function of one or two arguments can be done by editing one section of the [`Variable::evaluate()`{.docutils .literal .notranslate}]{.pre} method. Search for the word "customize" to find the appropriate location.

Adding a new group function can be done by editing one section of the [`Variable::evaluate()`{.docutils .literal .notranslate}]{.pre} method. Search for the word "customize" to find the appropriate location. You may need to add a new method to the Group class as well (see the [`group.cpp`{.docutils .literal .notranslate}]{.pre} file).

Accessing a new atom-based vector can be done by editing one section of the Variable::evaluate() method. Search for the word "customize" to find the appropriate location.

Adding new [[compute styles]{.doc}]compute.md){.reference .internal} (whose calculated values can then be accessed by variables) is discussed in the [[Modify compute]{.doc}]Modify_compute.md){.reference .internal} documentation.
:::::
::::::
:::::::

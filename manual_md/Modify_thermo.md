:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#thermodynamic-output-options .section}
# [3.17. ]{.section-number}Thermodynamic output options[](#thermodynamic-output-options "Link to this heading"){.headerlink}

The [`Thermo`{.docutils .literal .notranslate}]{.pre} class computes and prints thermodynamic information to the screen and log file; see the files [`thermo.cpp`{.docutils .literal .notranslate}]{.pre} and [`thermo.h`{.docutils .literal .notranslate}]{.pre}.

There are four styles defined in [`thermo.cpp`{.docutils .literal .notranslate}]{.pre}: "one", "multi", "yaml", and "custom". The "custom" style allows the user to explicitly list keywords for individual quantities to print when thermodynamic output is generated. The others have a fixed list of keywords. See the [[thermo_style]{.doc}]thermo_style.md){.reference .internal} command for a list of available quantities. The formatting of the "custom" style defaults to the "one" style, but can be adapted using [[thermo_modify line]{.doc}]thermo_modify.md){.reference .internal}.

The thermo styles (one, multi, etc) are defined by lists of keywords with associated formats for integer and floating point numbers and identified by an enumerator constant. Adding a new style thus mostly requires defining a new list of keywords and the associated formats and then inserting the required output processing where the enumerators are identified. Search for the word "CUSTOMIZATION" with references to "thermo style" in the [`thermo.cpp`{.docutils .literal .notranslate}]{.pre} file to see the locations where code will need to be added. The member function [`Thermo::header()`{.docutils .literal .notranslate}]{.pre} prints output at the very beginning of a thermodynamic output block and can be used to print column headers or other front matter. The member function [`Thermo::footer()`{.docutils .literal .notranslate}]{.pre} prints output at the end of a thermodynamic output block. The formatting of the output is done by assembling a "line" (which may span multiple lines if the style inserts newline characters ("n" as in the "multi" style).

New thermodynamic keywords can also be added to [`thermo.cpp`{.docutils .literal .notranslate}]{.pre} to compute new quantities for output. Search for the word "CUSTOMIZATION" with references to "keyword" in [`thermo.cpp`{.docutils .literal .notranslate}]{.pre} to see the several locations where code will need to be added. Effectively, you need to define a member function that computes the property, add an if statement in [`Thermo::parse_fields()`{.docutils .literal .notranslate}]{.pre} where the corresponding header string for the keyword and the function pointer is registered by calling the [`Thermo::addfield()`{.docutils .literal .notranslate}]{.pre} method, and add an if statement in [`Thermo::evaluate_keyword()`{.docutils .literal .notranslate}]{.pre} which is called from the [`Variable`{.docutils .literal .notranslate}]{.pre} class when a thermo keyword is encountered.

::: {.admonition .note}
Note

The third argument to [`Thermo::addfield()`{.docutils .literal .notranslate}]{.pre} is a flag indicating whether the function for the keyword computes a floating point (FLOAT), regular integer (INT), or big integer (BIGINT) value. This information is used for formatting the thermodynamic output. Inside the function the result must then be stored either in the [`dvalue`{.docutils .literal .notranslate}]{.pre}, [`ivalue`{.docutils .literal .notranslate}]{.pre} or [`bivalue`{.docutils .literal .notranslate}]{.pre} member variable, respectively.
:::

Since the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command allows to use output of quantities calculated by [[fixes]{.doc}]fix.md){.reference .internal}, [[computes]{.doc}]compute.md){.reference .internal}, and [[variables]{.doc}]variable.md){.reference .internal}, it may often be simpler to compute what you wish via one of those constructs, rather than by adding a new keyword to the thermo_style command.
::::
:::::
::::::

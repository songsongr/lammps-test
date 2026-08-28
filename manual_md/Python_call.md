::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#calling-python-from-lammps .section}
# [2.6. ]{.section-number}Calling Python from LAMMPS[](#calling-python-from-lammps "Link to this heading"){.headerlink}

LAMMPS has several commands which can be used to invoke Python code directly from an input script:

- [[python]{.doc}]python.md){.reference .internal}

- [[python-style variables]{.doc}]variable.md){.reference .internal}

- [[equal-style and atom-style variables with formulas containing Python function wrappers]{.doc}]variable.md){.reference .internal}

- [[fix python/invoke]{.doc}]fix_python_invoke.md){.reference .internal}

- [[pair_style python]{.doc}]pair_python.md){.reference .internal}

The [[python]{.doc}]python.md){.reference .internal} command can be used to define and execute a Python function that you write the code for. The Python function can also be assigned to a LAMMPS python-style variable via the [[variable]{.doc}]variable.md){.reference .internal} command. Each time the variable is evaluated, either in the LAMMPS input script itself, or by another LAMMPS command that uses the variable, this will trigger the Python function to be invoked.

The Python function can also be referenced in the formula used to define an [[equal-style or atom-style variable]{.doc}]variable.md){.reference .internal}, using the syntax for a [[Python function wrapper]{.doc}]variable.md){.reference .internal}. This make it easy to pass LAMMPS-related arguments to the Python function, as well as to invoke it whenever the equal- or atom-style variable is evaluated. For an atom-style variable it means the Python function can be invoked once per atom, using per-atom properties as arguments to the function.

The Python code for the function can be included directly in the input script or in an auxiliary file. The function can have arguments which are mapped to LAMMPS variables (also defined in the input script) and it can return a value to a LAMMPS variable. This is thus a mechanism for your input script to pass information to a piece of Python code, ask Python to execute the code, and return information to your input script.

Note that a Python function can be arbitrarily complex. It can import other Python modules, instantiate Python classes, call other Python functions, etc. The Python code that you provide can contain more code than the single function. It can contain other functions or Python classes, as well as global variables or other mechanisms for storing state between calls from LAMMPS to the function.

The Python function you provide can consist of "pure" Python code that only performs operations provided by standard Python. However, the Python function can also "call back" to LAMMPS through its Python-wrapped library interface, in the manner described in the [[Python run]{.doc}]Python_run.md){.reference .internal} doc page. This means it can issue LAMMPS input script commands or query and set internal LAMMPS state. As an example, this can be useful in an input script to create a more complex loop with branching logic, than can be created using the simple looping and branching logic enabled by the [[next]{.doc}]next.md){.reference .internal} and [[if]{.doc}]if.md){.reference .internal} commands.

See the [[python]{.doc}]python.md){.reference .internal} page and the [[variable]{.doc}]variable.md){.reference .internal} doc page for its python-style variables for more info, including examples of Python code you can write for both pure Python operations and callbacks to LAMMPS.
:::
::::
:::::

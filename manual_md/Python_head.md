:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#use-python-with-lammps .section}
# [2. ]{.section-number}Use Python with LAMMPS[](#use-python-with-lammps "Link to this heading"){.headerlink}

These pages describe various ways that LAMMPS and Python can be used together.

::: {.toctree-wrapper .compound}
- [2.1. Overview]Python_overview.md){.reference .internal}
- [2.2. Installation]Python_install.md){.reference .internal}
- [2.3. Run LAMMPS from Python]Python_run.md){.reference .internal}
- [2.4. The [`lammps`{.docutils .literal .notranslate}]{.pre} Python module]Python_module.md){.reference .internal}
- [2.5. Extending the Python interface]Python_ext.md){.reference .internal}
- [2.6. Calling Python from LAMMPS]Python_call.md){.reference .internal}
- [2.7. Output Readers]Python_formats.md){.reference .internal}
- [2.8. Example Python scripts]Python_examples.md){.reference .internal}
- [2.9. Using LAMMPS in IPython notebooks and Jupyter]Python_jupyter.md){.reference .internal}
- [2.10. Handling LAMMPS errors]Python_error.md){.reference .internal}
- [2.11. Troubleshooting]Python_trouble.md){.reference .internal}
:::

If you are not familiar with [Python](https://www.python.org){.reference .external}, it is a powerful scripting and programming language which can do almost everything that compiled languages like C, C++, or Fortran can do in fewer lines of code. It also comes with a large collection of add-on modules for many purposes (either bundled or easily installed from Python code repositories). The major drawback is slower execution speed of the script code compared to compiled programming languages. But when the script code is interfaced to optimized compiled code, performance can be on par with a standalone executable, for as long as the scripting is restricted to high-level operations. Thus Python is also convenient to use as a "glue" language to "drive" a program through its library interface, or to hook multiple pieces of software together, such as a simulation code and a visualization tool, or to run a coupled multi-scale or multi-physics model.

See the [[Coupling LAMMPS to other codes]{.doc}]Howto_couple.md){.reference .internal} page for more ideas about coupling LAMMPS to other codes. See the [[LAMMPS Library Interfaces]{.doc}]Library.md){.reference .internal} page for a description of the LAMMPS library interfaces. That interface is exposed to Python either when calling LAMMPS from Python or when calling Python from a LAMMPS input script and then calling back to LAMMPS from Python code. The C-library interface is designed to be easy to add functionality to, thus the Python interface to LAMMPS is easy to extend as well.

If you create interesting Python scripts that run LAMMPS or interesting Python functions that can be called from a LAMMPS input script, that you think would be generally useful, please post them as a pull request to our [GitHub site](https://github.com/lammps/lammps){.reference .external}, and they can be added to the LAMMPS distribution or web page.
::::
:::::
::::::

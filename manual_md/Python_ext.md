::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#extending-the-python-interface .section}
# [2.5. ]{.section-number}Extending the Python interface[](#extending-the-python-interface "Link to this heading"){.headerlink}

As noted previously, most of the [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}]Python_module.md#lammps.lammps "lammps.lammps"){.reference .internal} Python class methods correspond one-to-one with the functions in the LAMMPS library interface in [`src/library.cpp`{.docutils .literal .notranslate}]{.pre} and [`library.h`{.docutils .literal .notranslate}]{.pre}. This means you can extend the Python wrapper by following these steps:

- Add a new interface function to [`src/library.cpp`{.docutils .literal .notranslate}]{.pre} and [`src/library.h`{.docutils .literal .notranslate}]{.pre}.

- Rebuild LAMMPS as a shared library.

- Add a wrapper method to [`python/lammps/core.py`{.docutils .literal .notranslate}]{.pre} for this interface function.

- Define the corresponding [`argtypes`{.docutils .literal .notranslate}]{.pre} list and [`restype`{.docutils .literal .notranslate}]{.pre} in the [`lammps.__init__()`{.docutils .literal .notranslate}]{.pre} function.

- Re-install the shared library and the python module, if needed

- You should now be able to invoke the new interface function from a Python script.
:::
::::
:::::

::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::: {#using-lammps-in-ipython-notebooks-and-jupyter .section}
# [2.9. ]{.section-number}Using LAMMPS in IPython notebooks and Jupyter[](#using-lammps-in-ipython-notebooks-and-jupyter "Link to this heading"){.headerlink}

If the LAMMPS Python package is installed for the same Python interpreter as [IPython](https://ipython.org/){.reference .external}, you can use LAMMPS directly inside of an IPython notebook inside of Jupyter. [Jupyter](https://jupyter.org/){.reference .external} is a powerful integrated development environment (IDE) for many dynamic languages like [Python](https://www.python.org/){.reference .external}, [Julia](https://julialang.org/){.reference .external} and others, which operates inside of any web browser. Besides auto-completion and syntax highlighting it allows you to create formatted documents using Markup, mathematical formulas, graphics and animations intermixed with executable Python code. It is a great format for tutorials and showcasing your latest research.

The easiest way to install it is via [`pip`{.docutils .literal .notranslate}]{.pre} from [https://pypi.org/](https://pypi.org/){.reference .external}:

:::: {.highlight-bash .notranslate}
::: highlight
    pip install --user jupyter
:::
::::

To launch an instance of Jupyter simply run the following command inside your Python environment:

:::: {.highlight-bash .notranslate}
::: highlight
    jupyter notebook
:::
::::

:::: {#interactive-python-examples .section}
## [2.9.1. ]{.section-number}Interactive Python Examples[](#interactive-python-examples "Link to this heading"){.headerlink}

Examples of IPython notebooks can be found in the [`python/examples/ipython`{.docutils .literal .notranslate}]{.pre} subdirectory. They require LAMMPS to be compiled as shared library with PYTHON, PNG, JPEG and FFMPEG support.

To open these notebooks launch [`jupyter`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`notebook`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`index.ipynb`{.docutils .literal .notranslate}]{.pre} inside this directory. The opened file provides an overview of the available examples.

- Example 1: Using LAMMPS with Python ([`simple.ipynb`{.docutils .literal .notranslate}]{.pre})

- Example 2: Analyzing LAMMPS thermodynamic data ([`thermo.ipynb`{.docutils .literal .notranslate}]{.pre})

- Example 3: Working with Per-Atom Data ([`atoms.ipynb`{.docutils .literal .notranslate}]{.pre})

- Example 4: Working with LAMMPS variables ([`variables.ipynb`{.docutils .literal .notranslate}]{.pre})

- Example 5: Validating a dihedral potential ([`dihedrals/dihedral.ipynb`{.docutils .literal .notranslate}]{.pre})

- Example 6: Running a Monte Carlo relaxation ([`montecarlo/mc.ipynb`{.docutils .literal .notranslate}]{.pre})

::: {.admonition .note}
Note

Typically clicking a link in Jupyter will open a new tab, which might be blocked by your pop-up blocker.
:::
::::
:::::::::
::::::::::
:::::::::::

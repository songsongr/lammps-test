:::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::: {#troubleshooting .section}
# [2.11. ]{.section-number}Troubleshooting[](#troubleshooting "Link to this heading"){.headerlink}

::::::::::: {#testing-if-python-can-launch-lammps .section}
## [2.11.1. ]{.section-number}Testing if Python can launch LAMMPS[](#testing-if-python-can-launch-lammps "Link to this heading"){.headerlink}

To test if LAMMPS is callable from Python, launch Python interactively and type:

:::: {.highlight-python .notranslate}
::: highlight
    >>> from lammps import lammps
    >>> lmp = lammps()
:::
::::

If you get no errors, you're ready to use LAMMPS from Python. If the second command fails, the most common error to see is

:::: {.highlight-bash .notranslate}
::: highlight
    OSError: Could not load LAMMPS dynamic library
:::
::::

which means Python was unable to load the LAMMPS shared library. This typically occurs if the system can't find the LAMMPS shared library or one of the auxiliary shared libraries it depends on, or if something about the library is incompatible with your Python. The error message should give you an indication of what went wrong.

If your shared library uses a suffix, such as [`liblammps_mpi.so`{.docutils .literal .notranslate}]{.pre}, change the constructor call as follows (see [[Creating or deleting a LAMMPS object]{.std .std-ref}]Python_create.md#python-create-lammps){.reference .internal} for more details):

:::: {.highlight-python .notranslate}
::: highlight
    >>> lmp = lammps(name='mpi')
:::
::::

You can also test the load directly in Python as follows, without first importing from the [`lammps`{.docutils .literal .notranslate}]{.pre} module:

:::: {.highlight-python .notranslate}
::: highlight
    >>> from ctypes import CDLL
    >>> CDLL("liblammps.so")
:::
::::

If an error occurs, carefully go through the steps in [[Installing the LAMMPS Python Module and Shared Library]{.std .std-ref}]Python_install.md#python-install-guides){.reference .internal} and on the [[Build_basics]{.doc}]Build_basics.md){.reference .internal} page about building a shared library.
:::::::::::
::::::::::::
:::::::::::::
::::::::::::::

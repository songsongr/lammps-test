::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#example-python-scripts .section}
# [2.8. ]{.section-number}Example Python scripts[](#example-python-scripts "Link to this heading"){.headerlink}

The [`python/examples`{.docutils .literal .notranslate}]{.pre} directory has Python scripts which show how Python can run LAMMPS, grab data, change it, and put it back into LAMMPS.

These are the Python scripts included as demos in the [`python/examples`{.docutils .literal .notranslate}]{.pre} directory of the LAMMPS distribution, to illustrate the kinds of things that are possible when Python wraps LAMMPS. If you create your own scripts, send them to us and we can include them in the LAMMPS distribution.

  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`trivial.py`{.docutils .literal .notranslate}]{.pre}           read/run a LAMMPS input script through Python
  [`demo.py`{.docutils .literal .notranslate}]{.pre}              invoke various LAMMPS library interface routines
  [`simple.py`{.docutils .literal .notranslate}]{.pre}            run in parallel, similar to [`examples/COUPLE/simple/simple.cpp`{.docutils .literal .notranslate}]{.pre}
  [`split.py`{.docutils .literal .notranslate}]{.pre}             same as [`simple.py`{.docutils .literal .notranslate}]{.pre} but running in parallel on a subset of procs
  [`gui.py`{.docutils .literal .notranslate}]{.pre}               GUI go/stop/temperature-slider to control LAMMPS
  [`plot.py`{.docutils .literal .notranslate}]{.pre}              real-time temperature plot with GnuPlot via Pizza.py
  [`viz_TOOL.py`{.docutils .literal .notranslate}]{.pre}          real-time viz via some viz package
  [`vizplotgui_TOOL.py`{.docutils .literal .notranslate}]{.pre}   combination of [`viz_TOOL.py`{.docutils .literal .notranslate}]{.pre} and [`plot.py`{.docutils .literal .notranslate}]{.pre} and [`gui.py`{.docutils .literal .notranslate}]{.pre}
  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For the [`viz_TOOL.py`{.docutils .literal .notranslate}]{.pre} and [`vizplotgui_TOOL.py`{.docutils .literal .notranslate}]{.pre} commands, replace [`TOOL`{.docutils .literal .notranslate}]{.pre} with [`gl`{.docutils .literal .notranslate}]{.pre} or [`atomeye`{.docutils .literal .notranslate}]{.pre} or [`pymol`{.docutils .literal .notranslate}]{.pre} or [`vmd`{.docutils .literal .notranslate}]{.pre}, depending on what visualization package you have installed.

Note that for GL, you need to be able to run the Pizza.py GL tool, which is included in the pizza subdirectory. See the Pizza.py doc pages for more info:

- [https://lammps.github.io/pizza/](https://lammps.github.io/pizza/){.reference .external}

Note that for AtomEye, you need version 3, and there is a line in the scripts that specifies the path and name of the executable. See the AtomEye web pages for more details:

- [http://li.mit.edu/Archive/Graphics/A/](http://li.mit.edu/Archive/Graphics/A/){.reference .external}

- [http://li.mit.edu/Archive/Graphics/A3/A3.html](http://li.mit.edu/Archive/Graphics/A3/A3.html){.reference .external}

The latter link is to AtomEye 3 which has the scripting capability needed by these Python scripts.

Note that for PyMol, you need to have built and installed the open-source version of PyMol in your Python, so that you can import it from a Python script. See the PyMol web pages for more details:

> ::: {}
> - [https://www.pymol.org](https://www.pymol.org){.reference .external}
>
> - [https://github.com/schrodinger/pymol-open-source](https://github.com/schrodinger/pymol-open-source){.reference .external}
> :::

The latter link is to the open-source version.

Note that for VMD, you need a fairly current version (1.8.7 works for me) and there are some lines in the [`pizza/vmd.py`{.docutils .literal .notranslate}]{.pre} script for 4 PIZZA variables that have to match the VMD installation on your system.

------------------------------------------------------------------------

See the [`python/README`{.docutils .literal .notranslate}]{.pre} file for instructions on how to run them and the source code for individual scripts for comments about what they do.

Here are screenshots of the [`vizplotgui_tool.py`{.docutils .literal .notranslate}]{.pre} script in action for different visualization package options:

[![pyex1](_images/screenshot_gl.jpg){style="width: 24%;"}](_images/screenshot_gl.jpg){.reference .internal} [![pyex2](_images/screenshot_atomeye.jpg){style="width: 24%;"}](_images/screenshot_atomeye.jpg){.reference .internal} [![pyex3](_images/screenshot_pymol.jpg){style="width: 24%;"}](_images/screenshot_pymol.jpg){.reference .internal} [![pyex4](_images/screenshot_vmd.jpg){style="width: 24%;"}](_images/screenshot_vmd.jpg){.reference .internal}

Click to see larger versions of the images.
:::
::::
:::::

::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#lammps-non-features .section}
# [1.4. ]{.section-number}LAMMPS non-features[](#lammps-non-features "Link to this heading"){.headerlink}

LAMMPS is designed to be a fast, parallel engine for molecular dynamics (MD) simulations. It provides only a modest amount of functionality for setting up simulations and analyzing their output.

Originally, LAMMPS was not conceived and designed for:

- being run through a GUI

- building molecular systems, or building molecular topologies

- assign force-field coefficients automagically

- perform sophisticated analysis of your MD simulation

- visualize your MD simulation interactively

- plot your output data

Over the years many of these limitations have been reduced or removed. In part through features added to LAMMPS and in part through external tools that either closely interface with LAMMPS or extend LAMMPS.

Here are suggestions on how to perform these tasks:

- **GUI:** LAMMPS can be built as a library and a Python module that wraps the library interface is provided. Thus, GUI interfaces can be written in Python or C/C++ that run LAMMPS and visualize or plot its output. Examples of this are provided in the python directory and described on the [[Python]{.doc}]Python_head.md){.reference .internal} doc page. Since version 2 August 2023 [the LAMMPS-GUI application](https://lammps-gui.lammps.org){.reference .external} is available and can be compiled together with LAMMPS and linked to the LAMMPS library for running and visualizing LAMMPS simulation inputs. As of August 2025, LAMMPS-GUI is maintained in its own [repository on GitHub](https://github.com/akohlmey/lammps-gui/){.reference .external}. Also, there are several external wrappers or GUI front ends that are mentioned on the [Pre-/post-processing tools page](https://www.lammps.org/prepost.html){.reference .external} of the LAMMPS homepage.

- **Builder:** Several pre-processing tools are packaged with LAMMPS. Some of them convert input files in formats produced by other MD codes such as CHARMM, AMBER, or Insight into LAMMPS input formats. Some of them are simple programs that will build simple molecular systems, such as linear bead-spring polymer chains. The moltemplate program is a true molecular builder that will generate complex molecular models. See the [[Tools]{.doc}]Tools.md){.reference .internal} page for details on tools packaged with LAMMPS. The [Pre-/post-processing tools page](https://www.lammps.org/prepost.html){.reference .external} of the LAMMPS homepage describes a variety of third party tools for this task. Furthermore, some internal LAMMPS commands allow reconstructing, or selectively adding topology information, as well as provide the option to insert molecule templates instead of atoms for building bulk molecular systems.

- **Force-field assignment:** The conversion tools described in the previous bullet for CHARMM, AMBER, and Insight will also assign force field coefficients in the LAMMPS format, assuming you provide CHARMM, AMBER, or BIOVIA (formerly Accelrys) force field files. The tools [ParmEd](https://parmed.github.io/ParmEd/html/index.html){.reference .external} and [InterMol](https://github.com/shirtsgroup/InterMol){.reference .external} are particularly powerful and flexible in converting force field and topology data between various MD simulation programs.

- **Simulation analysis:** If you want to perform analysis on-the-fly as your simulation runs, see the [[compute]{.doc}]compute.md){.reference .internal} and [[fix]{.doc}]fix.md){.reference .internal} doc pages, which list commands that can be used in a LAMMPS input script. Also see the [[Modify]{.doc}]Modify.md){.reference .internal} page for info on how to add your own analysis code or algorithms to LAMMPS. For post-processing, LAMMPS output such as [[dump file snapshots]{.doc}]dump.md){.reference .internal} can be converted into formats used by other MD or post-processing codes. To some degree, that conversion can be done directly inside LAMMPS by interfacing to the VMD molfile plugins. The [[rerun]{.doc}]rerun.md){.reference .internal} command also allows post-processing of existing trajectories, and through being able to read a variety of file formats, this can also be used for analyzing trajectories from other MD codes. Some post-processing tools packaged with LAMMPS will do these conversions. Scripts provided in the tools/python directory can extract and massage data in dump files to make it easier to import into other programs. See the [[Tools]{.doc}]Tools.md){.reference .internal} page for details on these various options.

  The [Pre-/post-processing page](https://www.lammps.org/prepost.html){.reference .external} on the LAMMPS homepage lists some external packages for analysis of MD simulation data, including data produced by LAMMPS.

- **Visualization:** LAMMPS can produce NETPBM, TGA, JPG, or PNG format snapshot images on-the-fly via its [[dump image]{.doc}]dump_image.md){.reference .internal} command and pass them to an external program, [FFmpeg](https://ffmpeg.org/){.reference .external}, to generate movies from them. The [[LAMMPS-GUI tool]{.std .std-ref}]Tools.md#lammps-gui){.reference .internal} has a *Snapshot Image Viewer* which uses [[dump image]{.doc}]dump_image.md){.reference .internal} and allows to modify the visualization settings interactively. It also has a *Slide Show* feature where images created by [[dump image]{.doc}]dump_image.md){.reference .internal} are collected during a simulation and can be animated interactively or exported to a movie with FFmpeg or ImageMagick.

  For high-quality, interactive visualization, there are many excellent and free tools available. See the [Visualization Tools](https://www.lammps.org/viz.html){.reference .external} page of the LAMMPS website for visualization packages that can process LAMMPS output data.

- **Plotting:** See the next bullet about Pizza.py as well as the [[Python]{.doc}]Python_head.md){.reference .internal} page for examples of plotting LAMMPS output. Scripts provided with the *python* tool in the [`tools`{.docutils .literal .notranslate}]{.pre} directory will extract and process data in log and dump files to make it easier to analyze and plot. See the [[Tools]{.doc}]Tools.md){.reference .internal} doc page for more discussion of the various tools.

  The [[LAMMPS-GUI tool]{.std .std-ref}]Tools.md#lammps-gui){.reference .internal} has a *Chart Viewer* where [[thermodynamic data]{.doc}]thermo_style.md){.reference .internal} computed by LAMMPS is collected during the simulation and plotted immediately.

- **Pizza.py:** Our group has also written a separate toolkit called [Pizza.py](https://lammps.github.io/pizza/){.reference .external} which can do certain kinds of setup, analysis, plotting, and visualization (via OpenGL) for LAMMPS simulations. It thus provides some functionality for several of the above bullets. Pizza.py is written in [Python](https://www.python.org){.reference .external} and is available for download from [https://lammps.github.io/pizza/](https://lammps.github.io/pizza/){.reference .external}.
:::
::::
:::::

::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#kspace-styles .section}
# [3.12. ]{.section-number}Kspace styles[](#kspace-styles "Link to this heading"){.headerlink}

Classes that compute long-range Coulombic interactions via K-space representations (Ewald, PPPM) are derived from the KSpace class. New styles can be created to add new K-space options to LAMMPS.

Ewald.cpp is an example of computing K-space interactions.

Here is a brief description of methods you define in your new derived class. See kspace.h for details.

  -------------- ------------------------------------------------
  init           initialize the calculation before a run
  setup          computation before the first timestep of a run
  compute        every-timestep computation
  memory_usage   tally of memory usage
  -------------- ------------------------------------------------
:::
::::
:::::

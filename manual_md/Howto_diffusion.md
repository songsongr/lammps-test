::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#calculate-diffusion-coefficients .section}
# [10.3.8. ]{.section-number}Calculate diffusion coefficients[](#calculate-diffusion-coefficients "Link to this heading"){.headerlink}

The diffusion coefficient [\\(D\\)]{.math .notranslate .nohighlight} of a material can be measured in at least 2 ways using various options in LAMMPS. See the [`examples/DIFFUSE`{.docutils .literal .notranslate}]{.pre} directory for scripts that implement the 2 methods discussed here for a simple Lennard-Jones fluid model.

The first method is to measure the mean-squared displacement (MSD) of the system, via the [[compute msd]{.doc}]compute_msd.md){.reference .internal} command. The slope of the MSD versus time is proportional to the diffusion coefficient. The instantaneous MSD values can be accumulated in a vector via the [[fix vector]{.doc}]fix_vector.md){.reference .internal} command, and a line fit to the vector to compute its slope via the [[variable slope]{.doc}]variable.md){.reference .internal} function, and thus extract [\\(D\\)]{.math .notranslate .nohighlight}.

The second method is to measure the velocity auto-correlation function (VACF) of the system, via the [[compute vacf]{.doc}]compute_vacf.md){.reference .internal} command. The time-integral of the VACF is proportional to the diffusion coefficient. The instantaneous VACF values can be accumulated in a vector via the [[fix vector]{.doc}]fix_vector.md){.reference .internal} command, and time integrated via the [[variable trap]{.doc}]variable.md){.reference .internal} function, and thus extract [\\(D\\)]{.math .notranslate .nohighlight}.
:::
::::
:::::

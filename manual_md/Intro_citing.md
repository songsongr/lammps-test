::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::: {#citing-lammps .section}
# [1.8. ]{.section-number}Citing LAMMPS[](#citing-lammps "Link to this heading"){.headerlink}

::: {#core-algorithms .section}
## [1.8.1. ]{.section-number}Core Algorithms[](#core-algorithms "Link to this heading"){.headerlink}

The paper mentioned below is the best overview of LAMMPS, but there are also publications describing particular models or algorithms implemented in LAMMPS or complementary software that it has interfaces to. Please see below for how to cite contributions to LAMMPS.

The latest canonical publication that describes the basic features, the source code design, the program structure, the spatial decomposition approach, the neighbor finding, basic communications algorithms, and how users and developers have contributed to LAMMPS is:

> ::: {}
> [LAMMPS - A flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales, Comp. Phys. Comm. 271, 108171 (2022)](https://doi.org/10.1016/j.cpc.2021.108171){.reference .external}
> :::

So a project using LAMMPS or a derivative application that uses LAMMPS as a simulation engine should cite this paper. The paper is expected to be published in its final form under the same DOI in the first half of 2022. Please also give the URL of the LAMMPS website in your paper, namely [https://www.lammps.org](https://www.lammps.org){.reference .external}.

The original publication describing the parallel algorithms used in the initial versions of LAMMPS is:

> ::: {}
> [S. Plimpton, Fast Parallel Algorithms for Short-Range Molecular Dynamics, J Comp Phys, 117, 1-19 (1995).](https://doi.org/10.1006/jcph.1995.1039){.reference .external}
> :::
:::

::: {#doi-for-the-lammps-source-code .section}
## [1.8.2. ]{.section-number}DOI for the LAMMPS source code[](#doi-for-the-lammps-source-code "Link to this heading"){.headerlink}

The LAMMPS developers use the [Zenodo service at CERN](https://zenodo.org/){.reference .external} to create digital object identifiers (DOI) for stable releases of the LAMMPS source code. There are two types of DOIs for the LAMMPS source code.

The canonical DOI for **all** versions of LAMMPS, which will always point to the **latest** stable release version, is:

- DOI: [10.5281/zenodo.3726416](https://dx.doi.org/10.5281/zenodo.3726416){.reference .external}

In addition there are DOIs generated for individual stable releases:

- 3 March 2020 version: [DOI:10.5281/zenodo.3726417](https://dx.doi.org/10.5281/zenodo.3726417){.reference .external}

- 29 October 2020 version: [DOI:10.5281/zenodo.4157471](https://dx.doi.org/10.5281/zenodo.4157471){.reference .external}

- 29 September 2021 version: [DOI:10.5281/zenodo.6386596](https://dx.doi.org/10.5281/zenodo.6386596){.reference .external}

- 23 June 2022 version: [DOI:10.5281/zenodo.10806836](https://doi.org/10.5281/zenodo.10806836){.reference .external}

- 2 August 2023 version: [DOI:10.5281/zenodo.10806852](https://doi.org/10.5281/zenodo.10806852){.reference .external}
:::

::: {#home-page .section}
## [1.8.3. ]{.section-number}Home page[](#home-page "Link to this heading"){.headerlink}

The LAMMPS website at [https://www.lammps.org/](https://www.lammps.org){.reference .external} is the canonical location for information about LAMMPS and its features.
:::

::: {#citing-contributions .section}
## [1.8.4. ]{.section-number}Citing contributions[](#citing-contributions "Link to this heading"){.headerlink}

LAMMPS has many features that use either previously published methods and algorithms or novel features. It also includes potential parameter files for specific models. Where available, a reminder about references for optional features used in a specific run is printed to the screen and log file. Style and output location can be selected with the [[-cite command-line switch]{.std .std-ref}]Run_options.md#cite){.reference .internal}. Additional references are given in the documentation of the [[corresponding commands]{.doc}]Commands_all.md){.reference .internal} or in the [[Howto tutorials]{.doc}]Howto.md){.reference .internal}. Please make certain, that you provide the proper acknowledgments and citations in any published works using LAMMPS.
:::
:::::::
::::::::
:::::::::

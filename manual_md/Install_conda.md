:::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::: {#download-an-executable-for-linux-or-macos-via-conda .section}
# [2.4. ]{.section-number}Download an executable for Linux or macOS via Conda[](#download-an-executable-for-linux-or-macos-via-conda "Link to this heading"){.headerlink}

Pre-compiled LAMMPS binaries are available for macOS and Linux via the [Conda](https://docs.conda.io/en/latest/index.html){.reference .external} package management system.

First, one must set up the Conda package manager on your system. Follow the instructions to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html){.reference .external}, then create a conda environment (named my-lammps-env or whatever you prefer) for your LAMMPS install:

:::: {.highlight-bash .notranslate}
::: highlight
    conda config --add channels conda-forge
    conda create -n my-lammps-env
:::
::::

Then, you can install LAMMPS on your system with the following command:

:::: {.highlight-bash .notranslate}
::: highlight
    conda activate my-lammps-env
    conda install lammps
:::
::::

The LAMMPS binary is built with the [[KIM package]{.std .std-ref}]Build_extras.md#kim){.reference .internal}, which results in Conda also installing the kim-api binaries when LAMMPS is installed. In order to use potentials from [openkim.org](https://openkim.org){.reference .external}, you can install the openkim-models package

:::: {.highlight-bash .notranslate}
::: highlight
    conda install openkim-models
:::
::::

If you have problems with the installation, you can post issues to [this link](https://github.com/conda-forge/lammps-feedstock/issues){.reference .external}. Thanks to Jan Janssen (Max-Planck-Institut fuer Eisenforschung) for setting up the Conda capability.

::: {.admonition .note}
Note

If you have questions about these pre-compiled LAMMPS executables, you need to contact the people preparing those packages. The LAMMPS developers have no control over their choices of how they configure and build their packages and when they update them.
:::
::::::::::
:::::::::::
::::::::::::

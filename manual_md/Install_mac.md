::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::: {#download-an-executable-for-macos .section}
# [2.2. ]{.section-number}Download an executable for macOS[](#download-an-executable-for-macos "Link to this heading"){.headerlink}

LAMMPS can be downloaded, built, and configured for macOS with [Homebrew](https://brew.sh){.reference .external}. (Alternatively, see the installation instructions for [[downloading an executable via Conda]{.doc}]Install_conda.md){.reference .internal}.) The following LAMMPS packages are unavailable at this time because of additional requirements not yet met: GPU, KOKKOS.

After installing Homebrew, you can install LAMMPS on your system with the following commands:

:::: {.highlight-bash .notranslate}
::: highlight
    brew install lammps
:::
::::

This will install the executables "lammps_serial" and "lammps_mpi", as well as the LAMMPS "doc", "potentials", "tools", "bench", and "examples" directories.

Once LAMMPS is installed, you can test the installation with the Lennard-Jones benchmark file:

:::: {.highlight-bash .notranslate}
::: highlight
    brew test lammps -v
:::
::::

The LAMMPS binary is built with the [[KIM package]{.std .std-ref}]Build_extras.md#kim){.reference .internal}, which results in Homebrew also installing the kim-api binaries when LAMMPS is installed. In order to use potentials from [openkim.org](https://openkim.org){.reference .external}, you can install the openkim-models package

:::: {.highlight-bash .notranslate}
::: highlight
    brew install openkim-models
:::
::::

If you have problems with the installation, you can post issues to [this link](https://github.com/Homebrew/homebrew-core/issues){.reference .external}.

Thanks to Derek Thomas (derekt at cello.t.u-tokyo.ac.jp) for setting up the Homebrew capability.
:::::::::
::::::::::
:::::::::::

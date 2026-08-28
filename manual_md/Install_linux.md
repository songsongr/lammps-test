::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::::::::::::::: {#download-an-executable-for-linux .section}
# [2.1. ]{.section-number}Download an executable for Linux[](#download-an-executable-for-linux "Link to this heading"){.headerlink}

Binaries are available for different versions of Linux:

- [[Pre-built static Linux x86_64 executables]{.std .std-ref}](#static){.reference .internal}

- [[Pre-built Ubuntu and Debian Linux executables]{.std .std-ref}](#ubuntu){.reference .internal}

- [[Pre-built Fedora Linux executables]{.std .std-ref}](#fedora){.reference .internal}

- [[Pre-built EPEL Linux executables (RHEL, CentOS)]{.std .std-ref}](#epel){.reference .internal}

- [[Pre-built OpenSuse Linux executables]{.std .std-ref}](#opensuse){.reference .internal}

- [[Gentoo Linux executable]{.std .std-ref}](#gentoo){.reference .internal}

- [[Arch Linux build-script]{.std .std-ref}](#arch){.reference .internal}

::: {.admonition .note}
Note

If you have questions about these pre-compiled LAMMPS executables, you need to contact the people preparing those packages. The LAMMPS developers have no control over how they configure and build their packages and when they update them. They may only provide packages for stable release versions and not always update the packages in a timely fashion after a new LAMMPS release is made.
:::

------------------------------------------------------------------------

::: {#pre-built-static-linux-x86-64-executables .section}
[]{#static}

## [2.1.1. ]{.section-number}Pre-built static Linux x86_64 executables[](#pre-built-static-linux-x86-64-executables "Link to this heading"){.headerlink}

Pre-built LAMMPS executables for Linux, that are statically linked and compiled for 64-bit x86 CPUs (x86_64 or AMD64) are available for download at [https://download.lammps.org/static/](https://download.lammps.org/static/){.reference .external}. Because of that static linkage (and unlike the Linux distribution specific packages listed below), they do not depend on any installed software and thus should run on *any* 64-bit x86 machine with *any* Linux version.

These executable include most of the available packages and multi-thread parallelization (via INTEL, KOKKOS, or OPENMP package). They are **not** compatible with MPI. Several of the LAMMPS tools executables (e.g. [`msi2lmp`{.docutils .literal .notranslate}]{.pre}) are included as well. Because of the static linkage, there is no [`liblammps.so`{.docutils .literal .notranslate}]{.pre} library file and thus also the LAMMPS python module, which depends on it, is not included.

The compressed tar archives available for download have names following the pattern [`lammps-linux-x86_64-<version>.tar.gz`{.docutils .literal .notranslate}]{.pre} and will all unpack into a [`lammps-static`{.docutils .literal .notranslate}]{.pre} folder. The executables are then in the [`lammps-static/bin/`{.docutils .literal .notranslate}]{.pre} folder. Since they do not depend on any other software, they may be freely moved or copied around.

------------------------------------------------------------------------
:::

::::::::::::: {#pre-built-ubuntu-and-debian-linux-executables .section}
[]{#ubuntu}

## [2.1.2. ]{.section-number}Pre-built Ubuntu and Debian Linux executables[](#pre-built-ubuntu-and-debian-linux-executables "Link to this heading"){.headerlink}

A pre-built LAMMPS executable, suitable for running on the latest Ubuntu and Debian Linux versions, can be downloaded as a Debian package. This allows you to install LAMMPS with a single command, and stay (mostly) up-to-date with the current stable version of LAMMPS by simply updating your operating system.

To install LAMMPS do the following once:

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt-get install lammps
:::
::::

This downloads an executable named [`lmp`{.docutils .literal .notranslate}]{.pre} to your box and multiple packages with supporting data, examples and libraries as well as any missing dependencies. For example, the LAMMPS binary in this package is built with the [[KIM package]{.std .std-ref}]Build_extras.md#kim){.reference .internal} enabled, which results in the above command also installing the [`kim-api`{.docutils .literal .notranslate}]{.pre} binaries when LAMMPS is installed, unless they were installed already. In order to use potentials from [openkim.org](https://openkim.org){.reference .external}, you can also install the [`openkim-models`{.docutils .literal .notranslate}]{.pre} package:

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt-get install openkim-models
:::
::::

Or use the [KIM-API commands](https://openkim.org/doc/usage/obtaining-models/#source_install){.reference .external} to download and install individual models.

This LAMMPS executable can then be used in the usual way to run input scripts:

:::: {.highlight-bash .notranslate}
::: highlight
    lmp -in in.lj
:::
::::

To update LAMMPS to the latest packaged version, do the following:

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt-get update
:::
::::

This will also update other packages on your system.

To uninstall LAMMPS, do the following:

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt-get remove lammps
:::
::::

Please use [`lmp`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-help`{.docutils .literal .notranslate}]{.pre} to see which compilation options, packages, and styles are included in the binary.

Thanks to Anton Gladky (gladky.anton at gmail.com) for setting up this Ubuntu package capability.

------------------------------------------------------------------------
:::::::::::::

::::::: {#pre-built-fedora-linux-executables .section}
[]{#fedora}

## [2.1.3. ]{.section-number}Pre-built Fedora Linux executables[](#pre-built-fedora-linux-executables "Link to this heading"){.headerlink}

Pre-built [LAMMPS packages for stable releases](https://packages.fedoraproject.org/pkgs/lammps/){.reference .external} are available in the Fedora Linux distribution since Fedora version 28. The packages can be installed via the dnf package manager. There are 3 basic varieties (lammps = no MPI, lammps-mpich = MPICH MPI library, lammps-openmpi = OpenMPI MPI library) and for each support for linking to the C library interface (lammps-devel, lammps-mpich-devel, lammps-openmpi-devel), the header for compiling programs using the C library interface (lammps-headers), and the LAMMPS python module for Python 3. All packages can be installed at the same time and the name of the LAMMPS executable is [`lmp`{.docutils .literal .notranslate}]{.pre} and [`lmp_openmpi`{.docutils .literal .notranslate}]{.pre} or [`lmp_mpich`{.docutils .literal .notranslate}]{.pre} respectively. By default, [`lmp`{.docutils .literal .notranslate}]{.pre} will refer to the serial executable, unless one of the MPI environment modules is loaded ([`module`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`load`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`mpi/mpich-x86_64`{.docutils .literal .notranslate}]{.pre} or [`module`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`load`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`mpi/openmpi-x86_64`{.docutils .literal .notranslate}]{.pre}). Then the corresponding parallel LAMMPS executable can be used. The same mechanism applies when loading the LAMMPS python module.

To install LAMMPS with OpenMPI and run an input [`in.lj`{.docutils .literal .notranslate}]{.pre} with 2 CPUs do:

:::: {.highlight-bash .notranslate}
::: highlight
    dnf install lammps-openmpi
    module load mpi/openmpi-x86_64
    mpirun -np 2 lmp -in in.lj
:::
::::

The [`dnf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre} command is needed only once. In case of a new LAMMPS stable release, [`dnf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`update`{.docutils .literal .notranslate}]{.pre} will automatically update to the newer version as soon as the RPM files are built and uploaded to the download mirrors. The [`module`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`load`{.docutils .literal .notranslate}]{.pre} command is needed once per (shell) session or shell terminal instance, unless it is automatically loaded from the shell profile.

The LAMMPS binary is built with the [[KIM package]{.std .std-ref}]Build_extras.md#kim){.reference .internal} which results in the above command also installing the kim-api binaries when LAMMPS is installed. In order to use potentials from [openkim.org](https://openkim.org){.reference .external}, you can install the openkim-models package

:::: {.highlight-bash .notranslate}
::: highlight
    dnf install openkim-models
:::
::::

Please use [`lmp`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-help`{.docutils .literal .notranslate}]{.pre} to see which compilation options, packages, and styles are included in the binary.

Thanks to Christoph Junghans (LANL) for making LAMMPS available in Fedora.

------------------------------------------------------------------------
:::::::

::: {#pre-built-epel-linux-executable .section}
[]{#epel}

## [2.1.4. ]{.section-number}Pre-built EPEL Linux executable[](#pre-built-epel-linux-executable "Link to this heading"){.headerlink}

Pre-built LAMMPS (and KIM) packages for stable releases are available in the [Extra Packages for Enterprise Linux (EPEL) repository](https://docs.fedoraproject.org/en-US/epel/){.reference .external} for use with Red Hat Enterprise Linux (RHEL) or CentOS version 7.x and compatible Linux distributions. Names of packages, executable, and content are the same as described above for Fedora Linux. But RHEL/CentOS 7.x uses the [`yum`{.docutils .literal .notranslate}]{.pre} package manager instead of [`dnf`{.docutils .literal .notranslate}]{.pre} in Fedora 28.

Please use [`lmp`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-help`{.docutils .literal .notranslate}]{.pre} to see which compilation options, packages, and styles are included in the binary.

Thanks to Christoph Junghans (LANL) for making LAMMPS available in EPEL.

------------------------------------------------------------------------
:::

::::::::: {#pre-built-opensuse-linux-executable .section}
[]{#opensuse}

## [2.1.5. ]{.section-number}Pre-built OpenSuse Linux executable[](#pre-built-opensuse-linux-executable "Link to this heading"){.headerlink}

A pre-built LAMMPS package for stable releases is available in OpenSuse as of Leap 15.0. You can install the package with:

:::: {.highlight-bash .notranslate}
::: highlight
    zypper install lammps
:::
::::

This includes support for OpenMPI. The name of the LAMMPS executable is [`lmp`{.docutils .literal .notranslate}]{.pre}. To run an input in parallel on 2 CPUs you would do:

:::: {.highlight-bash .notranslate}
::: highlight
    mpirun -np 2 lmp -in in.lj
:::
::::

Please use [`lmp`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-help`{.docutils .literal .notranslate}]{.pre} to see which compilation options, packages, and styles are included in the binary.

The LAMMPS binary is built with the [[KIM package]{.std .std-ref}]Build_extras.md#kim){.reference .internal} which results in the above command also installing the kim-api binaries when LAMMPS is installed. In order to use potentials from [openkim.org](https://openkim.org){.reference .external}, you can install the openkim-models package

:::: {.highlight-bash .notranslate}
::: highlight
    zypper install openkim-models
:::
::::

Thanks to Christoph Junghans (LANL) for making LAMMPS available in OpenSuse.

------------------------------------------------------------------------
:::::::::

::::::: {#gentoo-linux-executable .section}
[]{#gentoo}

## [2.1.6. ]{.section-number}Gentoo Linux executable[](#gentoo-linux-executable "Link to this heading"){.headerlink}

LAMMPS is part of [Gentoo's main package tree](https://packages.gentoo.org/packages/sci-physics/lammps){.reference .external} and can be installed by typing:

:::: {.highlight-bash .notranslate}
::: highlight
    emerge --ask lammps
:::
::::

Note that in Gentoo the LAMMPS source code is downloaded and the package is then compiled and installed on your machine.

Certain LAMMPS packages can be enabled via USE flags, type

:::: {.highlight-bash .notranslate}
::: highlight
    equery uses lammps
:::
::::

for details.

Thanks to Nicolas Bock and Christoph Junghans (LANL) for setting up this Gentoo capability.

------------------------------------------------------------------------
:::::::

::::::: {#archlinux-build-script .section}
[]{#arch}

## [2.1.7. ]{.section-number}Archlinux build-script[](#archlinux-build-script "Link to this heading"){.headerlink}

LAMMPS is available via Arch's unofficial Arch User repository (AUR). There are three scripts available, named [lammps](https://aur.archlinux.org/packages/lammps){.reference .external}, [lammps-beta](https://aur.archlinux.org/packages/lammps){.reference .external} and [lammps-git](https://aur.archlinux.org/packages/lammps){.reference .external}. They respectively package the stable, feature, and git releases.

To install, you will need to have the git package installed. You may use any of the above names in-place of lammps.

:::: {.highlight-bash .notranslate}
::: highlight
    git clone https://aur.archlinux.org/lammps.git
    cd lammps
    makepkg -s
    makepkg -i
:::
::::

To update LAMMPS, you may repeat the above, or change into the cloned directory, and execute the following, after which, if there are any changes, you may use makepkg as above.

:::: {.highlight-bash .notranslate}
::: highlight
    git pull
:::
::::

Alternatively, you may use an AUR helper to install these packages.

Note that the AUR provides build-scripts that download the source code and then build and install the package on your machine.
:::::::
:::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::

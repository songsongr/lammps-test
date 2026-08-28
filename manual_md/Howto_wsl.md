:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#using-lammps-on-windows-10-with-wsl .section}
# [10.6.6. ]{.section-number}Using LAMMPS on Windows 10 with WSL[](#using-lammps-on-windows-10-with-wsl "Link to this heading"){.headerlink}

**written by Richard Berger**

------------------------------------------------------------------------

It's always been tricky for us to have LAMMPS users and developers work on Windows. We primarily develop LAMMPS to run on Linux clusters. To teach LAMMPS in workshop settings, we had to redirect Windows users to Linux Virtual Machines such as VirtualBox or Unix-like compilation with Cygwin.

With the latest updates in Windows 10 (Version 2004, Build 19041 or higher), Microsoft has added a new way to work on Linux-based code. The [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/){.reference .external}. With WSL Version 2, you now get a Linux Virtual Machine that transparently integrates into Windows. All you need is to ensure you have the latest Windows updates installed and enable this new feature. Linux VMs are then easily installed using the Microsoft Store.

In this tutorial, I'll show you how to set up and compile LAMMPS for both serial and MPI usage in WSL2.

::::::::::::::: {#installation .section}
## Installation[](#installation "Link to this heading"){.headerlink}

::: {#upgrade-to-the-latest-windows-10 .section}
### Upgrade to the latest Windows 10[](#upgrade-to-the-latest-windows-10 "Link to this heading"){.headerlink}

Type "Updates" in Windows Start and select "Check for Updates".

[![](_images/updates.png){style="width: 441.5px; height: 317.5px;"}](_images/updates.png){.reference .internal .image-reference}

Install all pending updates and reboot your system as many times as necessary. Continue until your Windows installation is updated.

[![](_images/windows_update.png){style="width: 601.0px; height: 467.0px;"}](_images/windows_update.png){.reference .internal .image-reference}

Verify your system has at least **version 2004 and build 19041 or later**. You can find this information by clicking on "OS build info".

[![](_images/osinfo.png){style="width: 601.0px; height: 467.0px;"}](_images/osinfo.png){.reference .internal .image-reference}
:::

::::::: {#enable-wsl .section}
### Enable WSL[](#enable-wsl "Link to this heading"){.headerlink}

Next, we must install two additional Windows features to enable WSL support. Open a PowerShell window as an administrator. Type "PowerShell" in Windows Start and select "Run as Administrator".

[![](_images/powershell.png){style="width: 422.0px; height: 315.5px;"}](_images/powershell.png){.reference .internal .image-reference}

Windows will ask you for administrator access. After you accept a new command line window will appear. Type in the following command to install WSL:

:::: {.highlight-none .notranslate}
::: highlight
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
:::
::::

![](_images/wsl_install1.png)

Next, enable the VirtualMachinePlatform feature using the following command:

:::: {.highlight-none .notranslate}
::: highlight
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
:::
::::

![](_images/wsl_install2.png)

Finally, reboot your system.
:::::::

::: {#update-wsl-kernel-component .section}
### Update WSL kernel component[](#update-wsl-kernel-component "Link to this heading"){.headerlink}

Download and install the [[`WSL`{.xref .download .docutils .literal .notranslate}]{.pre}` `{.xref .download .docutils .literal .notranslate}[`Kernel`{.xref .download .docutils .literal .notranslate}]{.pre}` `{.xref .download .docutils .literal .notranslate}[`Component`{.xref .download .docutils .literal .notranslate}]{.pre}` `{.xref .download .docutils .literal .notranslate}[`Update`{.xref .download .docutils .literal .notranslate}]{.pre}](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi){.reference .download .external download=""}. Afterwards, reboot your system.
:::

::::: {#set-wsl2-as-default .section}
### Set WSL2 as default[](#set-wsl2-as-default "Link to this heading"){.headerlink}

Again, open PowerShell as administrator and run the following command:

:::: {.highlight-powershell .notranslate}
::: highlight
    wsl --set-default-version 2
:::
::::

This command ensures that all future Linux installations will use WSL version 2.

![](_images/wsl_install3.png)
:::::

:::: {#install-a-linux-distribution .section}
### Install a Linux Distribution[](#install-a-linux-distribution "Link to this heading"){.headerlink}

Next, we need to install a Linux distribution via the Microsoft Store. Install [Ubuntu 20.04 LTS](ms-windows-store://pdp/?ProductId=9n6svws3rx71){.reference .external}. Once installed, you can launch it like any other application from the Start Menu.

[![](_images/ubuntu_in_store.png){style="width: 572.0px; height: 400.0px;"}](_images/ubuntu_in_store.png){.reference .internal .image-reference}

::: {#initial-setup .section}
#### Initial Setup[](#initial-setup "Link to this heading"){.headerlink}

The first time you launch the Ubuntu Linux console, it will prompt you for a UNIX username and password. You will need this password to perform [`sudo`{.code .docutils .literal .notranslate}]{.pre} commands later. Once completed, your Linux shell is ready for use. All your actions and commands will run as the Linux user you specified.

[![](_images/first_login.png){style="width: 489.5px; height: 256.0px;"}](_images/first_login.png){.reference .internal .image-reference}
:::
::::
:::::::::::::::

::: {#windows-explorer-wsl-integration .section}
## Windows Explorer / WSL integration[](#windows-explorer-wsl-integration "Link to this heading"){.headerlink}

Your Linux installation will have its own Linux filesystem, which contains the Ubuntu files. Your Linux user will have a regular Linux home directory in [`/home/<USERNAME>`{.code .docutils .literal .notranslate}]{.pre}. This directory is different from your Windows User directory. Windows and Linux filesystems are connected through WSL.

All hard drives in Windows are accessible in the [`/mnt`{.code .docutils .literal .notranslate}]{.pre} directory in Linux. E.g., WSL maps the [`C`{.code .docutils .literal .notranslate}]{.pre} hard drive to the [`/mnt/c`{.code .docutils .literal .notranslate}]{.pre} directory. That means you can access your Windows User directory in [`/mnt/c/Users/<WINDOWS_USERNAME>`{.code .docutils .literal .notranslate}]{.pre}.

The Windows Explorer can also access the Linux filesystem. To illustrate this integration, open an Ubuntu console and navigate to a directory of your choice. To view this location in Windows Explorer, use the [`explorer.exe`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`.`{.code .docutils .literal .notranslate}]{.pre} command (do not forget the final dot!).

[![](_images/wsl_integration.png){style="width: 496.5px; height: 262.0px;"}](_images/wsl_integration.png){.reference .internal .image-reference}
:::

------------------------------------------------------------------------

:::::::::::::::::::::::::: {#compiling-lammps .section}
## Compiling LAMMPS[](#compiling-lammps "Link to this heading"){.headerlink}

You now have a fully functioning Ubuntu installation and can follow most guides to install LAMMPS on a Linux system. Here are some of the essential steps to follow:

::::::: {#install-prerequisite-packages .section}
### Install prerequisite packages[](#install-prerequisite-packages "Link to this heading"){.headerlink}

Before we can begin, we need to download the necessary compiler toolchain and libraries to compile LAMMPS. In our Ubuntu-based Linux installation, we will use the [`apt`{.code .docutils .literal .notranslate}]{.pre} package manager to install additional packages.

First, upgrade all existing packages using [`apt`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`update`{.code .docutils .literal .notranslate}]{.pre} and [`apt`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`upgrade`{.code .docutils .literal .notranslate}]{.pre}.

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt update
    sudo apt upgrade -y
:::
::::

Next, install the following packages with [`apt`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`install`{.code .docutils .literal .notranslate}]{.pre}:

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt install -y cmake build-essential ccache gfortran openmpi-bin libopenmpi-dev \
                        libfftw3-dev libjpeg-dev libpng-dev python3-dev python3-pip \
                        python3-virtualenv libblas-dev liblapack-dev libhdf5-serial-dev \
                        hdf5-tools
:::
::::
:::::::

::::::::: {#download-lammps .section}
### Download LAMMPS[](#download-lammps "Link to this heading"){.headerlink}

Obtain a copy of the LAMMPS source code and go into it using the [`cd`{.code .docutils .literal .notranslate}]{.pre} command.

::::: {#option-1-download-a-lammps-tarball-using-wget .section}
#### Option 1: Download a LAMMPS tarball using wget[](#option-1-download-a-lammps-tarball-using-wget "Link to this heading"){.headerlink}

:::: {.highlight-bash .notranslate}
::: highlight
    wget https://github.com/lammps/lammps/archive/stable_3Mar2020.tar.gz
    tar xvzf stable_3Mar2020.tar.gz
    cd lammps
:::
::::
:::::

::::: {#option-2-download-a-lammps-development-version-from-github .section}
#### Option 2: Download a LAMMPS development version from GitHub[](#option-2-download-a-lammps-development-version-from-github "Link to this heading"){.headerlink}

:::: {.highlight-bash .notranslate}
::: highlight
    git clone --depth=1 https://github.com/lammps/lammps.git
    cd lammps
:::
::::
:::::
:::::::::

::::::::::::: {#configure-and-compile-lammps-with-cmake .section}
### Configure and Compile LAMMPS with CMake[](#configure-and-compile-lammps-with-cmake "Link to this heading"){.headerlink}

A beginner-friendly way to compile LAMMPS is to use CMake. Create a [`build`{.code .docutils .literal .notranslate}]{.pre} directory to compile LAMMPS and move into it. This directory will store the build configuration and any binaries generated during compilation.

:::: {.highlight-bash .notranslate}
::: highlight
    mkdir build
    cd build
:::
::::

There are countless ways to compile LAMMPS. It is beyond the scope of this tutorial. If you want to find out more about what can be enabled, please consult the extensive [documentation](https://docs.lammps.org/Build_cmake.html){.reference .external}.

To compile a minimal version of LAMMPS, we're going to use a preset. Presets are a way to specify a collection of CMake options using a file.

:::: {.highlight-bash .notranslate}
::: highlight
    cmake ../cmake/presets/basic.cmake ../cmake
:::
::::

This command configures the build and generates the necessary Makefiles. To compile the binary, run the make command.

:::: {.highlight-bash .notranslate}
::: highlight
    make -j 4
:::
::::

The [`-j`{.code .docutils .literal .notranslate}]{.pre} option specifies how many parallel processes will perform the compilation. This option can significantly speed up compilation times. Use a number that corresponds to the number of processors in your system.

After the compilation completes successfully, you will have an executable called [`lmp`{.code .docutils .literal .notranslate}]{.pre} in the [`build`{.code .docutils .literal .notranslate}]{.pre} directory.

[![](_images/compilation_result.png){style="width: 489.5px; height: 145.5px;"}](_images/compilation_result.png){.reference .internal .image-reference}

Please take note of the absolute path of your [`build`{.code .docutils .literal .notranslate}]{.pre} directory. You will need to know the location to execute the LAMMPS binary later.

One way of getting the absolute path of the current directory is through the [`$PWD`{.code .docutils .literal .notranslate}]{.pre} variable:

:::: {.highlight-bash .notranslate}
::: highlight
    # prints out the current value of the PWD variable
    echo $PWD
:::
::::

Let us save this value in a temporary variable [`LAMMPS_BUILD_DIR`{.code .docutils .literal .notranslate}]{.pre} for future use:

:::: {.highlight-bash .notranslate}
::: highlight
    LAMMPS_BUILD_DIR=$PWD
:::
::::

The full path of the LAMMPS binary then is [`$LAMMPS_BUILD_DIR/lmp`{.code .docutils .literal .notranslate}]{.pre}.
:::::::::::::
::::::::::::::::::::::::::

------------------------------------------------------------------------

::::::::::: {#running-an-example-script .section}
## Running an example script[](#running-an-example-script "Link to this heading"){.headerlink}

Now that we have a LAMMPS binary, we will run a script from the examples folder.

Switch into the [`examples/melt`{.code .docutils .literal .notranslate}]{.pre} folder:

:::: {.highlight-none .notranslate}
::: highlight
    cd ../examples/melt
:::
::::

To run this example in serial, use the following command:

:::: {.highlight-none .notranslate}
::: highlight
    $LAMMPS_BUILD_DIR/lmp -in in.melt
:::
::::

To run the same script in parallel using MPI with 4 processes, do the following:

:::: {.highlight-bash .notranslate}
::: highlight
    mpirun -np 4 $LAMMPS_BUILD_DIR/lmp -in in.melt
:::
::::

If you run LAMMPS for the first time, the Windows Firewall might prompt you to confirm access. LAMMPS is accessing the network stack to enable parallel computation. Allow the access.

[![](_images/windows_firewall.png){style="width: 807.0px; height: 284.25px;"}](_images/windows_firewall.png){.reference .internal .image-reference}

In either serial or MPI case, LAMMPS executes and will output something similar to this:

:::: {.highlight-none .notranslate}
::: highlight
    LAMMPS (30 Jun 2020)
    ...
    ...
    ...
    Total # of neighbors = 151513
    Ave neighs/atom = 37.878250
    Neighbor list builds = 12
    Dangerous builds not checked
    Total wall time: 0:00:00
:::
::::

**Congratulations! You've successfully compiled and executed LAMMPS on WSL!**
:::::::::::

:::::::::::::::: {#final-steps .section}
## Final steps[](#final-steps "Link to this heading"){.headerlink}

It is cumbersome to always specify the path of your LAMMPS binary. You can avoid this by adding the absolute path of your [`build`{.code .docutils .literal .notranslate}]{.pre} directory to your PATH environment variable.

:::: {.highlight-bash .notranslate}
::: highlight
    export PATH=$LAMMPS_BUILD_DIR:$PATH
:::
::::

You can then run LAMMPS input scripts like this:

:::: {.highlight-bash .notranslate}
::: highlight
    lmp -in in.melt
:::
::::

or

:::: {.highlight-bash .notranslate}
::: highlight
    mpirun -np 4 lmp -in in.melt
:::
::::

::::::::: {.admonition .note}
Note

The value of this [`PATH`{.code .docutils .literal .notranslate}]{.pre} variable will disappear once you close your console window. To persist this setting edit the [`$HOME/.bashrc`{.code .docutils .literal .notranslate}]{.pre} file using your favorite text editor and add this line:

:::: {.highlight-bash .notranslate}
::: highlight
    export PATH=/full/path/to/your/lammps/build:$PATH
:::
::::

**Example:** If the LAMMPS executable lmp has the following absolute path:

:::: {.highlight-bash .notranslate}
::: highlight
    /home/<USERNAME>/lammps/build/lmp
:::
::::

the [`PATH`{.code .docutils .literal .notranslate}]{.pre} variable should be:

:::: {.highlight-bash .notranslate}
::: highlight
    export PATH=/home/<USERNAME>/lammps/build:$PATH
:::
::::

Once set up, all your Ubuntu consoles will always have access to your [`lmp`{.code .docutils .literal .notranslate}]{.pre} binary without having to specify its location.
:::::::::
::::::::::::::::

:::: {#conclusion .section}
## Conclusion[](#conclusion "Link to this heading"){.headerlink}

I hope this gives you good overview on how to start compiling and running LAMMPS on Windows. WSL makes preparing and running scripts on Windows a much better experience.

If you are completely new to Linux, I highly recommend investing some time in studying Linux online tutorials. E.g., tutorials about Bash Shell and Basic Unix commands (e.g., [Linux Journey](https://linuxjourney.com/){.reference .external}). Acquiring these skills will make you much more productive in this environment.

::: {.admonition .seealso}
See also

- [Windows Subsystem for Linux Documentation](https://learn.microsoft.com/en-us/windows/wsl/){.reference .external}
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::: {#installation .section}
# [2.2. ]{.section-number}Installation[](#installation "Link to this heading"){.headerlink}

The LAMMPS Python module enables calling the [[LAMMPS C library API]{.std .std-ref}]Library.md#lammps-c-api){.reference .internal} from Python by dynamically loading functions in the LAMMPS shared library through the Python [ctypes](https://docs.python.org/3/library/ctypes.html){.reference .external} module. Because of the dynamic loading, it is required that LAMMPS is compiled in [["shared" mode]{.std .std-ref}]Build_basics.md#exe){.reference .internal}.

::: versionchanged
[Changed in version 2Apr2025.]{.versionmodified .changed}
:::

LAMMPS currently only supports Python version 3.6 or later.

Two components are necessary for Python to be able to invoke LAMMPS code:

- The LAMMPS Python Package ([`lammps`{.docutils .literal .notranslate}]{.pre}) from the [`python`{.docutils .literal .notranslate}]{.pre} folder

- The LAMMPS Shared Library ([`liblammps.so`{.docutils .literal .notranslate}]{.pre}, [`liblammps.dylib`{.docutils .literal .notranslate}]{.pre} or [`liblammps.dll`{.docutils .literal .notranslate}]{.pre}) from the folder where you compiled LAMMPS.

::::::::::::::::::::::::::: {#installing-the-lammps-python-module-and-shared-library .section}
[]{#python-install-guides}

## [2.2.1. ]{.section-number}Installing the LAMMPS Python Module and Shared Library[](#installing-the-lammps-python-module-and-shared-library "Link to this heading"){.headerlink}

Making LAMMPS usable within Python and vice versa requires putting the LAMMPS Python package ([`lammps`{.docutils .literal .notranslate}]{.pre}) into a location where the Python interpreter can find it and installing the LAMMPS shared library into a folder that the dynamic loader searches or inside of the installed [`lammps`{.docutils .literal .notranslate}]{.pre} package folder. There are multiple ways to achieve this.

1.  Install both components into a Python [`site-packages`{.docutils .literal .notranslate}]{.pre} folder, either system-wide or in the corresponding user-specific folder. This way no additional environment variables need to be set, but the shared library is otherwise not accessible.

2.  Do an installation into a virtual environment.

3.  Leave the files where they are in the source/development tree and adjust some environment variables.

:::::::::::::::::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
Python package

Virtual environment

In place usage
:::

::::::::::: {#panel-0-0-0 .sphinx-tabs-panel aria-labelledby="tab-0-0-0" role="tabpanel" tabindex="0"}
Compile LAMMPS with either [[CMake]{.doc}]Build_cmake.md){.reference .internal} or the [[traditional make]{.doc}]Build_make.md){.reference .internal} procedure in [[shared mode]{.std .std-ref}]Build_basics.md#exe){.reference .internal}. After compilation has finished, type (in the compilation folder):

:::: {.highlight-bash .notranslate}
::: highlight
    make install-python
:::
::::

This will try to build a so-called (binary) wheel file, a compressed binary python package and then install it with the python package manager 'pip'. Installation will be attempted into a system-wide [`site-packages`{.docutils .literal .notranslate}]{.pre} folder and if that fails into the corresponding folder in the user's home directory. For a system-wide installation you usually would have to gain superuser privilege first, e.g. though [`sudo`{.docutils .literal .notranslate}]{.pre}

+-----------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| File                  | Location                                                                                     | Notes                                                                                  |
+=======================+==============================================================================================+========================================================================================+
| LAMMPS Python package | - [`$HOME/.local/lib/pythonX.Y/site-packages/lammps`{.docutils .literal .notranslate}]{.pre} | [`X.Y`{.docutils .literal .notranslate}]{.pre} depends on the installed Python version |
+-----------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| LAMMPS shared library | - [`$HOME/.local/lib/pythonX.Y/site-packages/lammps`{.docutils .literal .notranslate}]{.pre} | [`X.Y`{.docutils .literal .notranslate}]{.pre} depends on the installed Python version |
+-----------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

For a system-wide installation those folders would then become.

+-----------------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| File                  | Location                                                                             | Notes                                                                                  |
+=======================+======================================================================================+========================================================================================+
| LAMMPS Python package | - [`/usr/lib/pythonX.Y/site-packages/lammps`{.docutils .literal .notranslate}]{.pre} | [`X.Y`{.docutils .literal .notranslate}]{.pre} depends on the installed Python version |
+-----------------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| LAMMPS shared library | - [`/usr/lib/pythonX.Y/site-packages/lammps`{.docutils .literal .notranslate}]{.pre} | [`X.Y`{.docutils .literal .notranslate}]{.pre} depends on the installed Python version |
+-----------------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

No environment variables need to be set for those, as those folders are searched by default by Python or the LAMMPS Python package.

::: versionchanged
[Changed in version 24Mar2022.]{.versionmodified .changed}
:::

::: {.admonition .note}
Note

If there is an existing installation of the LAMMPS python module, [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install-python`{.docutils .literal .notranslate}]{.pre} will try to update it. However, that will fail if the older version of the module was installed by LAMMPS versions until 17Feb2022. Those were using the distutils package, which does not create a "manifest" that allows a clean uninstall. The [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install-python`{.docutils .literal .notranslate}]{.pre} command will always produce a lammps-\<version\>-\<python\>-\<abi\>-\<os\>-\<arch\>.whl file (the 'wheel'). And this file can be later installed directly with [`python`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-m`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`pip`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`<wheel`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`file>.whl`{.docutils .literal .notranslate}]{.pre} without having to type [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install-python`{.docutils .literal .notranslate}]{.pre} again and repeating the build step, too.
:::

For the traditional make process you can override the python version to version x.y when calling [`make`{.docutils .literal .notranslate}]{.pre} with [`PYTHON=pythonX.Y`{.docutils .literal .notranslate}]{.pre}. For a CMake based compilation this choice has to be made during the CMake configuration step.

If the default settings of [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install-python`{.docutils .literal .notranslate}]{.pre} are not what you want, you can invoke [`install.py`{.docutils .literal .notranslate}]{.pre} from the [`python`{.docutils .literal .notranslate}]{.pre} directory manually as

:::: {.highlight-bash .notranslate}
::: highlight
    python3 install.py -p <python package> -l <shared library> -v <version.h file> [-n] [-f]
:::
::::

- The [`-p`{.docutils .literal .notranslate}]{.pre} flag argument is the full path to the [`python/lammps`{.docutils .literal .notranslate}]{.pre} folder to be installed,

- the [`-l`{.docutils .literal .notranslate}]{.pre} flag argument is the full path to the LAMMPS shared library file to be installed,

- the [`-v`{.docutils .literal .notranslate}]{.pre} flag argument is the full path to the [`src/version.h`{.docutils .literal .notranslate}]{.pre} file

- the optional [`-n`{.docutils .literal .notranslate}]{.pre} flag instructs the script to only build a wheel file but not attempt to install it (default is to try installing),

- the optional [`-w`{.docutils .literal .notranslate}]{.pre} flag argument is the path to a folder where to store the resulting wheel file (default is the current folder)

- and the optional [`-f`{.docutils .literal .notranslate}]{.pre} argument instructs the script to force installation even if pip would otherwise refuse installation with an [[error about externally managed environments]{.std .std-ref}]Howto_python.md#externally-managed){.reference .internal}. The Python developers recommend to not augment a Python installation with custom packages, both at the user and the system level, and advise to use virtual environments instead. Some recent Linux distributions enforce that recommendation by default.

Example command line for building only the wheel after building LAMMPS with [`cmake`{.docutils .literal .notranslate}]{.pre} in the folder [`build`{.docutils .literal .notranslate}]{.pre}:

:::: {.highlight-bash .notranslate}
::: highlight
    python3 python/install.py -n -p python/lammps -l build/liblammps.so -v src/version.h -w build
:::
::::
:::::::::::

::::::: {#panel-0-0-1 .sphinx-tabs-panel aria-labelledby="tab-0-0-1" hidden="true" role="tabpanel" tabindex="0"}
A virtual environment is a minimal Python installation inside of a folder. It allows isolating and customizing a Python environment that is mostly independent from a user or system installation. For the core Python environment, it uses symbolic links to the system installation and thus it can be set up quickly and will not take up much disk space. This gives you the flexibility to install (newer/different) versions of Python packages that would potentially conflict with already installed system packages. It also does not requite any superuser privileges. See [PEP 405: Python Virtual Environments](https://peps.python.org/pep-0405/){.reference .external} for more information.

To create a virtual environment in the folder [`$HOME/myenv`{.docutils .literal .notranslate}]{.pre}, use the [venv](https://docs.python.org/3/library/venv.html){.reference .external} module as follows.

:::: {.highlight-bash .notranslate}
::: highlight
    # create virtual environment in folder $HOME/myenv
    python3 -m venv $HOME/myenv
:::
::::

To activate the virtual environment type:

:::: {.highlight-bash .notranslate}
::: highlight
    source $HOME/myenv/bin/activate
:::
::::

This has to be done every time you log in or open a new terminal window and after you turn off the virtual environment with the [`deactivate`{.docutils .literal .notranslate}]{.pre} command.

When using CMake to build LAMMPS, you need to set [`CMAKE_INSTALL_PREFIX`{.docutils .literal .notranslate}]{.pre} to the value of the [`$VIRTUAL_ENV`{.docutils .literal .notranslate}]{.pre} environment variable during the configuration step. For the traditional make procedure, no additional steps are needed. After compiling LAMMPS you can do a "Python package only" installation with [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install-python`{.docutils .literal .notranslate}]{.pre} and the LAMMPS Python package and the shared library file are installed into the following locations:

+-----------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| File                  | Location                                                                                     | Notes                                                                                  |
+=======================+==============================================================================================+========================================================================================+
| LAMMPS Python Module  | - [`$VIRTUAL_ENV/lib/pythonX.Y/site-packages/lammps`{.docutils .literal .notranslate}]{.pre} | [`X.Y`{.docutils .literal .notranslate}]{.pre} depends on the installed Python version |
+-----------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| LAMMPS shared library | - [`$VIRTUAL_ENV/lib/pythonX.Y/site-packages/lammps`{.docutils .literal .notranslate}]{.pre} | [`X.Y`{.docutils .literal .notranslate}]{.pre} depends on the installed Python version |
+-----------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
:::::::

:::::::: {#panel-0-0-2 .sphinx-tabs-panel aria-labelledby="tab-0-0-2" hidden="true" role="tabpanel" tabindex="0"}
You can also [[compile LAMMPS]{.doc}]Build.md){.reference .internal} as usual in [["shared" mode]{.std .std-ref}]Build_basics.md#exe){.reference .internal} leave the shared library and Python package inside the source/compilation folders. Instead of copying the files where they can be found, you need to set the environment variables [`PYTHONPATH`{.docutils .literal .notranslate}]{.pre} (for the Python package) and [`LD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre} (or [`DYLD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre} on macOS

For Bourne shells (bash, ksh and similar) the commands are:

:::: {.highlight-bash .notranslate}
::: highlight
    export PYTHONPATH=${PYTHONPATH}:${HOME}/lammps/python
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${HOME}/lammps/src
:::
::::

For the C-shells like csh or tcsh the commands are:

:::: {.highlight-csh .notranslate}
::: highlight
    setenv PYTHONPATH ${PYTHONPATH}:${HOME}/lammps/python
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:${HOME}/lammps/src
:::
::::

On macOS you may also need to set [`DYLD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre} accordingly. You can make those changes permanent by editing your [`$HOME/.bashrc`{.docutils .literal .notranslate}]{.pre} or [`$HOME/.login`{.docutils .literal .notranslate}]{.pre} files, respectively.

::: {.admonition .note}
Note

The [`PYTHONPATH`{.docutils .literal .notranslate}]{.pre} needs to point to the parent folder that contains the [`lammps`{.docutils .literal .notranslate}]{.pre} package!
:::
::::::::
::::::::::::::::::::::::

In case you run into an "externally-managed-environment" error when trying to install the LAMMPS Python module, please refer to [[corresponding paragraph]{.std .std-ref}]Howto_python.md#externally-managed){.reference .internal} in the Python HOWTO page to learn about options for handling this error.

To verify if LAMMPS can be successfully started from Python, start the Python interpreter, load the [`lammps`{.docutils .literal .notranslate}]{.pre} Python module and create a LAMMPS instance. This should not generate an error message and produce output similar to the following:

> ::::: {}
> :::: {.highlight-console .notranslate}
> ::: highlight
>     $ python
>     Python 3.8.5 (default, Sep  5 2020, 10:50:12)
>     [GCC 10.2.0] on linux
>     Type "help", "copyright", "credits" or "license" for more information.
>     >>> import lammps
>     >>> lmp = lammps.lammps()
>     LAMMPS (18 Sep 2020)
>     using 1 OpenMP thread(s) per MPI task
>     >>>
> :::
> ::::
> :::::

::: {.admonition .note}
Note

Unless you opted for "In place use", you will have to rerun the installation any time you recompile LAMMPS to ensure the latest Python package and shared library are installed and used.
:::

::: {.admonition .note}
Note

If you want Python to be able to load different versions of the LAMMPS shared library with different settings, you will need to manually copy the files under different names (e.g. [`liblammps_mpi.so`{.docutils .literal .notranslate}]{.pre} or [`liblammps_gpu.so`{.docutils .literal .notranslate}]{.pre}) into the appropriate folder as indicated above. You can then select the desired library through the *name* argument of the LAMMPS object constructor (see [[Creating or deleting a LAMMPS object]{.std .std-ref}]Python_create.md#python-create-lammps){.reference .internal}).
:::
:::::::::::::::::::::::::::

::::::::::: {#extending-python-to-run-in-parallel .section}
[]{#python-install-mpi4py}

## [2.2.2. ]{.section-number}Extending Python to run in parallel[](#extending-python-to-run-in-parallel "Link to this heading"){.headerlink}

If you wish to run LAMMPS in parallel from Python, you need to extend your Python with an interface to MPI. This also allows you to make MPI calls directly from Python in your script, if you desire.

We have tested this with [MPI for Python](https://mpi4py.readthedocs.io/){.reference .external} (aka mpi4py) and you will find installation instruction for it below.

Installation of mpi4py (version 4.0.1 as of Feb 2025) can be done as follows:

- Via [`pip`{.docutils .literal .notranslate}]{.pre} into a local user folder with:

  :::: {.highlight-bash .notranslate}
  ::: highlight
      python3 -m pip install --user mpi4py
  :::
  ::::

- Via [`dnf`{.docutils .literal .notranslate}]{.pre} into a system folder for RedHat/Fedora systems:

  :::: {.highlight-bash .notranslate}
  ::: highlight
      # for use with OpenMPI
      sudo dnf install python3-mpi4py-openmpi
      # for use with MPICH
      sudo dnf install python3-mpi4py-mpich
  :::
  ::::

- Via [`pip`{.docutils .literal .notranslate}]{.pre} into a virtual environment (see above):

  :::: {.highlight-console .notranslate}
  ::: highlight
      $ source $HOME/myenv/activate
      (myenv)$ python -m pip install mpi4py
  :::
  ::::

- Via [`pip`{.docutils .literal .notranslate}]{.pre} into a system folder (not recommended):

  :::: {.highlight-bash .notranslate}
  ::: highlight
      sudo python3 -m pip install mpi4py
  :::
  ::::

For more detailed installation instructions and additional options, please see the [mpi4py installation](https://mpi4py.readthedocs.io/en/stable/install.html){.reference .external} page.

To use [`mpi4py`{.docutils .literal .notranslate}]{.pre} and LAMMPS in parallel from Python, you **must** make certain that **both** are using the **same** implementation and version of MPI library. If you only have one MPI library installed on your system this is not an issue, but it can be if you have multiple MPI installations (e.g. on an HPC cluster to be selected through environment modules). Your LAMMPS build is explicit about which MPI it is using, since it is either detected during CMake configuration or in the traditional make build system you specify the details in your low-level [`src/MAKE/Makefile.foo`{.docutils .literal .notranslate}]{.pre} file. The installation process of [`mpi4py`{.docutils .literal .notranslate}]{.pre} uses the [`mpicc`{.docutils .literal .notranslate}]{.pre} command to find information about the MPI it uses to build against. And it tries to load "libmpi.so" from the [`LD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre}. This may or may not find the MPI library that LAMMPS is using. If you have problems running both mpi4py and LAMMPS together, this is an issue you may need to address, e.g. by loading the module for different MPI installation so that mpi4py finds the right one.

If you have successfully installed mpi4py, you should be able to run Python and type

:::: {.highlight-python .notranslate}
::: highlight
    from mpi4py import MPI
:::
::::

without error. You should also be able to run Python in parallel on a simple test script

:::: {.highlight-bash .notranslate}
::: highlight
    mpirun -np 4 python3 test.py
:::
::::

where [`test.py`{.docutils .literal .notranslate}]{.pre} contains the lines

:::: {.highlight-python .notranslate}
::: highlight
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    print("Proc %d out of %d procs" % (comm.Get_rank(),comm.Get_size()))
:::
::::

and see one line of output for each processor you run on. Please note that the order of the lines is not deterministic

:::: {.highlight-console .notranslate}
::: highlight
    $ mpirun -np 4 python3 test.py
    Proc 0 out of 4 procs
    Proc 1 out of 4 procs
    Proc 2 out of 4 procs
    Proc 3 out of 4 procs
:::
::::
:::::::::::
::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#lammps-python-tutorial .section}
# [10.6.5. ]{.section-number}LAMMPS Python Tutorial[](#lammps-python-tutorial "Link to this heading"){.headerlink}

- [Overview](#overview){#id1 .reference .internal}

- [Quick Start](#quick-start){#id2 .reference .internal}

  - [System-wide or User Installation](#system-wide-or-user-installation){#id3 .reference .internal}

    - [Step 1: Building LAMMPS as a shared library](#step-1-building-lammps-as-a-shared-library){#id4 .reference .internal}

    - [Step 2: Installing the LAMMPS Python module](#step-2-installing-the-lammps-python-module){#id5 .reference .internal}

  - [Installation inside of a virtual environment](#installation-inside-of-a-virtual-environment){#id6 .reference .internal}

    - [Benefits of using a virtualenv](#benefits-of-using-a-virtualenv){#id7 .reference .internal}

    - [Creating a virtualenv with lammps installed](#creating-a-virtualenv-with-lammps-installed){#id8 .reference .internal}

- [Creating a new lammps instance](#creating-a-new-lammps-instance){#id9 .reference .internal}

- [Commands](#commands){#id10 .reference .internal}

- [Accessing atom data](#accessing-atom-data){#id11 .reference .internal}

- [Retrieving the values of thermodynamic data and variables](#retrieving-the-values-of-thermodynamic-data-and-variables){#id12 .reference .internal}

- [Error handling](#error-handling){#id13 .reference .internal}

- [Using LAMMPS in IPython notebooks and Jupyter](#using-lammps-in-ipython-notebooks-and-jupyter){#id14 .reference .internal}

- [Interactive Python Examples](#interactive-python-examples){#id15 .reference .internal}

  - [Validating a dihedral potential](#validating-a-dihedral-potential){#id16 .reference .internal}

  - [Running a Monte Carlo relaxation](#running-a-monte-carlo-relaxation){#id17 .reference .internal}

------------------------------------------------------------------------

::: {#overview .section}
## [Overview](#id1){.toc-backref role="doc-backlink"}[](#overview "Link to this heading"){.headerlink}

The [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}]Python_module.md#lammps.lammps "lammps.lammps"){.reference .internal} Python module is a wrapper class for the LAMMPS [[C language library interface API]{.std .std-ref}]Library.md#lammps-c-api){.reference .internal} which is written using [Python ctypes](https://docs.python.org/3/library/ctypes.html){.reference .external}. The design choice of this wrapper class is to follow the C language API closely with only small changes related to Python specific requirements and to better accommodate object oriented programming.

In addition to this flat [ctypes](https://docs.python.org/3/library/ctypes.html){.reference .external} interface, the [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}]Python_module.md#lammps.lammps "lammps.lammps"){.reference .internal} wrapper class exposes a discoverable API that doesn't require as much knowledge of the underlying C language library interface or LAMMPS C++ code implementation.

Finally, the API exposes some additional features for [IPython integration](https://ipython.org/){.reference .external} into [Jupyter notebooks](https://jupyter.org/){.reference .external}, e.g. for embedded visualization output from [[dump style image]{.doc}]dump_image.md){.reference .internal}.
:::

------------------------------------------------------------------------

::::::::::::::::::::::::::: {#quick-start .section}
## [Quick Start](#id2){.toc-backref role="doc-backlink"}[](#quick-start "Link to this heading"){.headerlink}

::::::::::::::::: {#system-wide-or-user-installation .section}
### [System-wide or User Installation](#id3){.toc-backref role="doc-backlink"}[](#system-wide-or-user-installation "Link to this heading"){.headerlink}

::::::::::: {#step-1-building-lammps-as-a-shared-library .section}
#### [Step 1: Building LAMMPS as a shared library](#id4){.toc-backref role="doc-backlink"}[](#step-1-building-lammps-as-a-shared-library "Link to this heading"){.headerlink}

To use LAMMPS inside of Python it has to be compiled as shared library. This library is then loaded by the Python interface. In this example we enable the [[MOLECULE package]{.std .std-ref}]Packages_details.md#pkg-molecule){.reference .internal} and compile LAMMPS with [[PNG, JPEG and FFMPEG output support]{.std .std-ref}]Build_extras.md#graphics){.reference .internal} enabled.

:::::::::: {.sphinx-tabs .docutils .container}
::: {.closeable aria-label="Tabbed content" role="tablist"}
CMake build

Traditional make
:::

::::: {#panel-0-0-0 .sphinx-tabs-panel aria-labelledby="tab-0-0-0" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    mkdir $LAMMPS_DIR/build-shared
    cd  $LAMMPS_DIR/build-shared

    # MPI, PNG, Jpeg, FFMPEG are auto-detected
    cmake ../cmake -DPKG_MOLECULE=yes -DPKG_PYTHON=on -DBUILD_SHARED_LIBS=yes
    make
:::
::::
:::::

::::: {#panel-0-0-1 .sphinx-tabs-panel aria-labelledby="tab-0-0-1" hidden="true" role="tabpanel" tabindex="0"}
:::: {.highlight-bash .notranslate}
::: highlight
    cd $LAMMPS_DIR/src

    # add LAMMPS packages if necessary
    make yes-MOLECULE
    make yes-PYTHON

    # compile shared library using Makefile
    make mpi mode=shlib LMP_INC="-DLAMMPS_PNG -DLAMMPS_JPEG -DLAMMPS_FFMPEG" JPG_LIB="-lpng -ljpeg"
:::
::::
:::::
::::::::::
:::::::::::

::::::: {#step-2-installing-the-lammps-python-module .section}
#### [Step 2: Installing the LAMMPS Python module](#id5){.toc-backref role="doc-backlink"}[](#step-2-installing-the-lammps-python-module "Link to this heading"){.headerlink}

Next install the LAMMPS Python module into your current Python installation with:

:::: {.highlight-bash .notranslate}
::: highlight
    make install-python
:::
::::

This will create a so-called ["wheel"](https://packaging.python.org/en/latest/discussions/package-formats/#what-is-a-wheel){.reference .external} and then install the LAMMPS Python module from that "wheel" into either into a system folder (provided the command is executed with root privileges) or into your personal Python module folder.

::: {.admonition .note}
Note

Recompiling the shared library requires re-installing the Python package.
:::

::: {#externally-managed .hint .admonition}
Handling an "externally-managed-environment" Error

Some Python installations made through Linux distributions (e.g. Ubuntu 24.04LTS or later) will prevent installing the LAMMPS Python module into a system folder or a corresponding folder of the individual user as attempted by [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`install-python`{.docutils .literal .notranslate}]{.pre} with an error stating that an *externally managed* python installation must be only managed by the same package package management tool. This is an optional setting, so not all Linux distributions follow it currently (Spring 2025). The reasoning and explanations for this error can be found in the [Python Packaging User Guide](https://packaging.python.org/en/latest/specifications/externally-managed-environments/){.reference .external}

These guidelines suggest to create a virtual environment and install the LAMMPS Python module there (see below). This is generally a good idea and the LAMMPS developers recommend this, too. If, however, you want to proceed and install the LAMMPS Python module regardless, you can install the "wheel" file (see above) manually with the [`pip`{.docutils .literal .notranslate}]{.pre} command by adding the [`--break-system-packages`{.docutils .literal .notranslate}]{.pre} flag.
:::
:::::::
:::::::::::::::::

::::::::::: {#installation-inside-of-a-virtual-environment .section}
### [Installation inside of a virtual environment](#id6){.toc-backref role="doc-backlink"}[](#installation-inside-of-a-virtual-environment "Link to this heading"){.headerlink}

You can use virtual environments to create a custom Python environment specifically tuned for your workflow.

::::: {#benefits-of-using-a-virtualenv .section}
#### [Benefits of using a virtualenv](#id7){.toc-backref role="doc-backlink"}[](#benefits-of-using-a-virtualenv "Link to this heading"){.headerlink}

- isolation of your system Python installation from your development installation

- installation can happen in your user directory without root access (useful for HPC clusters)

- installing packages through pip allows you to get newer versions of packages than e.g., through apt-get or yum package managers (and without root access)

- you can even install specific old versions of a package if necessary

**Prerequisite (e.g. on Ubuntu)**

:::: {.highlight-bash .notranslate}
::: highlight
    apt-get install python-venv
:::
::::
:::::

::::::: {#creating-a-virtualenv-with-lammps-installed .section}
#### [Creating a virtualenv with lammps installed](#id8){.toc-backref role="doc-backlink"}[](#creating-a-virtualenv-with-lammps-installed "Link to this heading"){.headerlink}

:::: {.highlight-bash .notranslate}
::: highlight
    # create virtual envrionment named 'testing'
    python3 -m venv $HOME/python/testing

    # activate 'testing' environment
    source $HOME/python/testing/bin/activate
:::
::::

Now configure and compile the LAMMPS shared library as outlined above. When using CMake and the shared library has already been build, you need to re-run CMake to update the location of the python executable to the location in the virtual environment with:

:::: {.highlight-bash .notranslate}
::: highlight
    cmake . -DPython_EXECUTABLE=$(which python)

    # install LAMMPS package in virtualenv
    (testing) make install-python

    # install other useful packages
    (testing) pip install matplotlib jupyter mpi4py pandas

    ...

    # return to original shell
    (testing) deactivate
:::
::::
:::::::
:::::::::::
:::::::::::::::::::::::::::

------------------------------------------------------------------------

::::: {#creating-a-new-lammps-instance .section}
## [Creating a new lammps instance](#id9){.toc-backref role="doc-backlink"}[](#creating-a-new-lammps-instance "Link to this heading"){.headerlink}

To create a lammps object you need to first import the class from the lammps module. By using the default constructor, a new [[`lammps`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}]Python_module.md#lammps.lammps "lammps.lammps"){.reference .internal} instance is created.

:::: {.highlight-python .notranslate}
::: highlight
    from lammps import lammps
    L = lammps()
:::
::::

See the [[LAMMPS Python documentation]{.doc}]Python_create.md){.reference .internal} for how to customize the instance creation with optional arguments.
:::::

------------------------------------------------------------------------

:::::::::::::: {#commands .section}
## [Commands](#id10){.toc-backref role="doc-backlink"}[](#commands "Link to this heading"){.headerlink}

Sending a LAMMPS command with the library interface is done using the [`command`{.docutils .literal .notranslate}]{.pre} method of the lammps object.

For instance, let's take the following LAMMPS command:

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    region box block 0 10 0 5 -0.5 0.5
:::
::::

This command can be executed with the following Python code if [`L`{.docutils .literal .notranslate}]{.pre} is a [`lammps`{.docutils .literal .notranslate}]{.pre} instance:

:::: {.highlight-python .notranslate}
::: highlight
    L.command("region box block 0 10 0 5 -0.5 0.5")
:::
::::

For convenience, the [`lammps`{.docutils .literal .notranslate}]{.pre} class also provides a command wrapper [`cmd`{.docutils .literal .notranslate}]{.pre} that turns any LAMMPS command into a regular function call:

:::: {.highlight-python .notranslate}
::: highlight
    L.cmd.region("box block", 0, 10, 0, 5, -0.5, 0.5)
:::
::::

Note that each parameter is set as Python number literal. With the wrapper each command takes an arbitrary parameter list and transparently merges it to a single command string, separating individual parameters by white-space.

The benefit of this approach is avoiding redundant command calls and easier parameterization. With the [`command`{.docutils .literal .notranslate}]{.pre} function each call needs to be assembled manually using formatted strings.

:::: {.highlight-python .notranslate}
::: highlight
    L.command(f"region box block {xlo} {xhi} {ylo} {yhi} {zlo} {zhi}")
:::
::::

The wrapper accepts parameters directly and will convert them automatically to a final command string.

:::: {.highlight-python .notranslate}
::: highlight
    L.cmd.region("box block", xlo, xhi, ylo, yhi, zlo, zhi)
:::
::::

::: {.admonition .note}
Note

When running in IPython you can use Tab-completion after [`L.cmd.`{.docutils .literal .notranslate}]{.pre} to see all available LAMMPS commands.
:::
::::::::::::::

------------------------------------------------------------------------

::::::: {#accessing-atom-data .section}
## [Accessing atom data](#id11){.toc-backref role="doc-backlink"}[](#accessing-atom-data "Link to this heading"){.headerlink}

All per-atom properties that are part of the [[atom style]{.doc}]atom_style.md){.reference .internal} in the current simulation can be accessed using the [`extract_atoms()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre} method. This can be retrieved as ctypes objects or as NumPy arrays through the lammps.numpy module. Those represent the *local* atoms of the individual sub-domain for the current MPI process and may contain information for the local ghost atoms or not depending on the property. Both can be accessed as lists, but for the ctypes list object the size is not known and hast to be retrieved first to avoid out-of-bounds accesses.

:::: {.highlight-python .notranslate}
::: highlight
    nlocal = L.extract_setting("nlocal")
    nall = L.extract_setting("nall")
    print("Number of local atoms ", nlocal, "  Number of local and ghost atoms ", nall);

    # access via ctypes directly
    atom_id = L.extract_atom("id")
    print("Atom IDs", atom_id[0:nlocal])

    # access through numpy wrapper
    atom_type = L.numpy.extract_atom("type")
    print("Atom types", atom_type)

    x = L.numpy.extract_atom("x")
    v = L.numpy.extract_atom("v")
    print("positions array shape", x.shape)
    print("velocity array shape", v.shape)
    # turn on communicating velocities to ghost atoms
    L.cmd.comm_modify("vel", "yes")
    v = L.numpy.extract_atom('v')
    print("velocity array shape", v.shape)
:::
::::

Some properties can also be set from Python since internally the data of the C++ code is accessed directly:

:::: {.highlight-python .notranslate}
::: highlight
    # set position in 2D simulation
    x[0] = (1.0, 0.0)

    # set position in 3D simulation
    x[0] = (1.0, 0.0, 1.)
:::
::::
:::::::

------------------------------------------------------------------------

::::: {#retrieving-the-values-of-thermodynamic-data-and-variables .section}
## [Retrieving the values of thermodynamic data and variables](#id12){.toc-backref role="doc-backlink"}[](#retrieving-the-values-of-thermodynamic-data-and-variables "Link to this heading"){.headerlink}

To access thermodynamic data from the last completed timestep, you can use the [[`get_thermo()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}]Python_module.md#lammps.lammps.get_thermo "lammps.lammps.get_thermo"){.reference .internal} method, and to extract the value of (compatible) variables, you can use the [[`extract_variable()`{.xref .py .py-meth .docutils .literal .notranslate}]{.pre}]Python_module.md#lammps.lammps.extract_variable "lammps.lammps.extract_variable"){.reference .internal} method.

:::: {.highlight-python .notranslate}
::: highlight
    result = L.get_thermo("ke") # kinetic energy
    result = L.get_thermo("pe") # potential energy

    result = L.extract_variable("t") / 2.0
:::
::::
:::::

:::: {#error-handling .section}
## [Error handling](#id13){.toc-backref role="doc-backlink"}[](#error-handling "Link to this heading"){.headerlink}

We are using C++ exceptions in LAMMPS for errors and the C language library interface captures and records them. This allows checking whether errors have happened in Python during a call into LAMMPS and then re-throw the error as a Python exception. This way you can handle LAMMPS errors in the conventional way through the Python exception handling mechanism.

::: {.admonition .warning}
Warning

Capturing a LAMMPS exception in Python can still mean that the current LAMMPS process is in an illegal state and must be terminated. It is advised to save your data and terminate the Python instance as quickly as possible.
:::
::::

::::: {#using-lammps-in-ipython-notebooks-and-jupyter .section}
## [Using LAMMPS in IPython notebooks and Jupyter](#id14){.toc-backref role="doc-backlink"}[](#using-lammps-in-ipython-notebooks-and-jupyter "Link to this heading"){.headerlink}

If the LAMMPS Python package is installed for the same Python interpreter as IPython, you can use LAMMPS directly inside of an IPython notebook inside of Jupyter. Jupyter is a powerful integrated development environment (IDE) for many dynamic languages like Python, Julia and others, which operates inside of any web browser. Besides auto-completion and syntax highlighting it allows you to create formatted documents using Markup, mathematical formulas, graphics and animations intermixed with executable Python code. It is a great format for tutorials and showcasing your latest research.

To launch an instance of Jupyter simply run the following command inside your Python environment (this assumes you followed the Quick Start instructions):

:::: {.highlight-bash .notranslate}
::: highlight
    jupyter notebook
:::
::::
:::::

::::::::::: {#interactive-python-examples .section}
## [Interactive Python Examples](#id15){.toc-backref role="doc-backlink"}[](#interactive-python-examples "Link to this heading"){.headerlink}

Examples of IPython notebooks can be found in the [`python/examples/ipython`{.docutils .literal .notranslate}]{.pre} subdirectory. To open these notebooks launch [`jupyter`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`notebook`{.docutils .literal .notranslate}]{.pre} inside this directory and navigate to one of them. If you compiled and installed a LAMMPS shared library with PNG, JPEG and FFMPEG support you should be able to rerun all of these notebooks.

::::: {#validating-a-dihedral-potential .section}
### [Validating a dihedral potential](#id16){.toc-backref role="doc-backlink"}[](#validating-a-dihedral-potential "Link to this heading"){.headerlink}

This example showcases how an IPython Notebook can be used to compare a simple LAMMPS simulation of a harmonic dihedral potential to its analytical solution. Four atoms are placed in the simulation and the dihedral potential is applied on them using a datafile. Then one of the atoms is rotated along the central axis by setting its position from Python, which changes the dihedral angle.

:::: {.highlight-python .notranslate}
::: highlight
    phi = [d \* math.pi / 180 for d in range(360)]

    pos = [(1.0, math.cos(p), math.sin(p)) for p in phi]

    x = L.numpy.extract_atom("x")

    pe = []
    for p in pos:
        x[3] = p
        L.cmd.run(0, "post", "no")
        pe.append(L.get_thermo("pe"))
:::
::::

By evaluating the potential energy for each position we can verify that trajectory with the analytical formula. To compare both solutions, we plot both trajectories over each other using matplotlib, which embeds the generated plot inside the IPython notebook.

![](_images/python_dihedral.jpg){.align-center}
:::::

::::::: {#running-a-monte-carlo-relaxation .section}
### [Running a Monte Carlo relaxation](#id17){.toc-backref role="doc-backlink"}[](#running-a-monte-carlo-relaxation "Link to this heading"){.headerlink}

This second example shows how to use the lammps Python interface to create a 2D Monte Carlo Relaxation simulation, computing and plotting energy terms and even embedding video output.

Initially, a 2D system is created in a state with minimal energy.

![](_images/python_mc_minimum.jpg){.align-center}

It is then disordered by moving each atom by a random delta.

:::: {.highlight-python .notranslate}
::: highlight
    random.seed(27848)
    deltaperturb = 0.2
    x = L.numpy.extract_atom("x")
    natoms = x.shape[0]

    for i in range(natoms):
        dx = deltaperturb \* random.uniform(-1, 1)
        dy = deltaperturb \* random.uniform(-1, 1)
        x[i][0] += dx
        x[i][1] += dy

    L.cmd.run(0, "post", "no")
:::
::::

![](_images/python_mc_disordered.jpg){.align-center}

Finally, the Monte Carlo algorithm is implemented in Python. It continuously moves random atoms by a random delta and only accepts certain moves.

:::: {.highlight-python .notranslate}
::: highlight
    estart = L.get_thermo("pe")
    elast = estart

    naccept = 0
    energies = [estart]

    niterations = 3000
    deltamove = 0.1
    kT = 0.05

    for i in range(niterations):
        x = L.numpy.extract_atom("x")
        natoms = x.shape[0]
        iatom = random.randrange(0, natoms)
        current_atom = x[iatom]

        x0 = current_atom[0]
        y0 = current_atom[1]

        dx = deltamove \* random.uniform(-1, 1)
        dy = deltamove \* random.uniform(-1, 1)

        current_atom[0] = x0 + dx
        current_atom[1] = y0 + dy

        L.cmd.run(1, "pre no post no")

        e = L.get_thermo("pe")
        energies.append(e)

        if e <= elast:
            naccept += 1
            elast = e
        elif random.random() <= math.exp(natoms\*(elast-e)/kT):
            naccept += 1
            elast = e
        else:
            current_atom[0] = x0
            current_atom[1] = y0
:::
::::

The energies of each iteration are collected in a Python list and finally plotted using matplotlib.

![](_images/python_mc_energies_plot.jpg){.align-center}

The IPython notebook also shows how to use dump commands and embed video files inside of the IPython notebook.
:::::::
:::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

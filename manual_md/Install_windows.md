::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#download-an-executable-for-windows .section}
# [2.3. ]{.section-number}Download an executable for Windows[](#download-an-executable-for-windows "Link to this heading"){.headerlink}

Pre-compiled Windows installers which install LAMMPS executables on a Windows system can be downloaded from this site:

``` literal-block
https://packages.lammps.org/windows.html
```

Note that each installer package has a date in its name, which corresponds to the LAMMPS version of the same date. Installers for current and older versions of LAMMPS are available. 32-bit and 64-bit installers are available, and each installer contains both a serial and parallel executable. The installer website also explains how to install the Windows MPI package (MPICH2 from Argonne National Labs), needed to run in parallel with MPI.

The LAMMPS binaries contain *all* [[optional packages]{.doc}]Packages.md){.reference .internal} included in the source distribution except: ADIOS, H5MD, KIM, ML-PACE, ML-QUIP, MSCG, NETCDF, QMMM, SCAFACOS, and VTK. The serial version also does not include the LATBOLTZ package. The PYTHON package is only available in the Python installers that bundle a Python runtime. The GPU package is compiled for OpenCL with mixed precision kernels.

The LAMMPS library is compiled as a shared library and the [[LAMMPS Python module]{.doc}]Python_module.md){.reference .internal} is installed, so that it is possible to load LAMMPS into a Python interpreter.

The installer site also has instructions on how to run LAMMPS under Windows, once it is installed, in both serial and parallel.

When you download the installer package, you run it on your Windows machine. It will then prompt you with a dialog, where you can choose the installation directory, unpack and copy several executables, potential files, documentation PDFs, selected example files, etc. It will then update a few system settings (e.g. [`PATH`{.docutils .literal .notranslate}]{.pre}, [`LAMMPS_POTENTIALS`{.docutils .literal .notranslate}]{.pre}) and add an entry into the Start Menu (with references to the documentation, LAMMPS homepage and more). From that menu, there is also a link to an uninstaller that removes the files and undoes the environment manipulations.

Note that to update to a newer version of LAMMPS, you should typically uninstall the version you currently have, download a new installer, and go through the installation procedure described above. I.e. the same procedure for installing/updating most Windows programs. You can install multiple versions of LAMMPS (in different directories), but only the executable for the last-installed package will be found automatically, so this should only be done for debugging purposes.
:::
::::
:::::

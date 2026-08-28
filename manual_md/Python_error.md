:::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::: {#handling-lammps-errors .section}
# [2.10. ]{.section-number}Handling LAMMPS errors[](#handling-lammps-errors "Link to this heading"){.headerlink}

LAMMPS and the LAMMPS library are compiled with [[C++ exception support]{.std .std-ref}]Build_settings.md#exceptions){.reference .internal} to provide a better error handling experience. LAMMPS errors trigger throwing a C++ exception. These exceptions allow capturing errors on the C++ side and rethrowing them on the Python side. This way LAMMPS errors can be handled through the Python exception handling mechanism.

:::: {.highlight-python .notranslate}
::: highlight
    from lammps import lammps, MPIAbortException

    lmp = lammps()

    try:
       # LAMMPS will normally terminate itself and the running process if an error
       # occurs. This would kill the Python interpreter.  The library wrapper will
       # detect that an error has occurred and throw a Python exception

       lmp.command('unknown')
    except MPIAbortException as ae:
       # Single MPI process got killed. This would normally be handled by an MPI abort
       pass
    except Exception as e:
       # All (MPI) processes have reached this error
       pass
:::
::::

::: {.admonition .warning}
Warning

Capturing a LAMMPS exception in Python can still mean that the current LAMMPS process is in an illegal state and must be terminated. It is advised to save your data and terminate the Python instance as quickly as possible when running in parallel with MPI.
:::
::::::
:::::::
::::::::

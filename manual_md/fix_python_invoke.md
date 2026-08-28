:::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::: {#fix-python-invoke-command .section}
[]{#index-0}

# fix python/invoke command[](#fix-python-invoke-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID python/invoke N callback function_name
:::
::::

- ID, group-ID are ignored by this fix

- python/invoke = style name of this fix command

- N = execute every N steps

- callback = *post_force* or *end_of_step*

  ``` literal-block
  post_force = callback after force computations on atoms every N time steps
  end_of_step = callback after every N time steps
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    python post_force_callback here """
    from lammps import lammps

    def post_force_callback(lammps_ptr, vflag):
        lmp = lammps(ptr=lammps_ptr)
        # access LAMMPS state using Python interface
    """

    python end_of_step_callback here """
    def end_of_step_callback(lammps_ptr):
        lmp = lammps(ptr=lammps_ptr)
        # access LAMMPS state using Python interface
    """

    fix pf  all python/invoke 50 post_force post_force_callback
    fix eos all python/invoke 50 end_of_step end_of_step_callback
:::
::::
:::::

:::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix allows you to call a Python function during a simulation run. The callback is either executed after forces have been applied to atoms or at the end of every N time steps.

Callback functions must be declared in the global scope of the active Python interpreter. This can either be done by defining it inline using the python command or by importing functions from other Python modules. If LAMMPS is driven using the library interface from Python, functions defined in the driving Python interpreter can also be executed.

Each callback is given a pointer object as first argument. This can be used to initialize an instance of the lammps Python interface, which gives access to the LAMMPS state from Python.

::: {.admonition .warning}
Warning

While you can access the state of LAMMPS via library functions from these callbacks, trying to execute input script commands will in the best case not work or in the worst case result in undefined behavior.
:::
::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command. This fix is not invoked during [[energy minimization]{.doc}]minimize.md){.reference .internal}.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This fix is part of the PYTHON package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

Building LAMMPS with the PYTHON package will link LAMMPS with the Python library on your system. Settings to enable this are in the lib/python/Makefile.lammps file. See the lib/python/README file for information on those settings.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[python command]{.doc}]python.md){.reference .internal}
:::
::::::::::::::
:::::::::::::::
::::::::::::::::

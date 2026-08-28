::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::: {#plugin-command .section}
[]{#index-0}

# plugin command[](#plugin-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    plugin command args
:::
::::

- command = *load* or *unload* or *list* or *clear* or *restore*

- args = list of arguments for a particular plugin command

  ``` literal-block
  load file = load plugin(s) from shared object in file
  unload style name = unload plugin name of style style
      style = pair or bond or angle or dihedral or improper or kspace or compute or fix or region or command or run or min
  list = print a list of currently loaded plugins
  clear = unload all currently loaded plugins
  restore = restore all loaded plugins
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    plugin load morse2plugin.so
    plugin unload pair morse2/omp
    plugin unload command hello
    plugin list
    plugin clear
    plugin restore
:::
::::
:::::

::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

The plugin command allows to load (and unload) additional styles and commands into a LAMMPS binary from so-called dynamic shared object (DSO) files. This enables to add new functionality to an existing LAMMPS binary without having to recompile and link the entire executable.

::: {.hint .admonition}
Plugins are a global, per-executable property

Unlike most settings in LAMMPS, plugins are a per-executable global property. Loading a plugin means that it is not only available for the current LAMMPS instance but for all *future* LAMMPS instances.

After a [[clear]{.doc}]clear.md){.reference .internal} command, all currently loaded plugins will be restored and do not need to be loaded again.

When using the library interface or the Python or Fortran module to create multiple concurrent LAMMPS instances, all plugins should be loaded by the first created LAMMPS instance as all future instances will inherit them. To import plugins that were loaded by a different LAMMPS instance, use the *restore* command.
:::

The *load* command will load and initialize all plugins contained in the plugin DSO with the given filename. A message with information about the plugin style and name and more will be printed. Individual DSO files may contain multiple plugins. If a plugin is already loaded it will be skipped. More details about how to write and compile the plugin DSO is given in programmer's guide part of the manual under [[Writing plugins]{.doc}]Developer_plugins.md){.reference .internal}.

The *unload* command will remove the given style or the given name from the list of available styles. If the plugin style is currently in use, that style instance will be deleted and replaced by the default setting for that style.

The *list* command will print a list of the loaded plugins and their styles and names.

The *clear* command will unload all currently loaded plugins.

::: versionadded
[Added in version 12Jun2025.]{.versionmodified .added}
:::

The *restore* command will restore all currently loaded plugins. This allows to "import" plugins into a different LAMMPS instance.

:::: {.note .admonition}
Automatic loading of plugins

::: versionadded
[Added in version 4May2022.]{.versionmodified .added}
:::

When the environment variable [`LAMMPS_PLUGIN_PATH`{.docutils .literal .notranslate}]{.pre} is set, then LAMMPS will search the directory (or directories) listed in this path for files with names that end in [`plugin.so`{.docutils .literal .notranslate}]{.pre} (e.g. [`helloplugin.so`{.docutils .literal .notranslate}]{.pre}) and will try to load the contained plugins automatically at start-up.
::::
:::::::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *plugin* command is part of the PLUGIN package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

If plugins access functions or classes from a package, LAMMPS must have been compiled with that package included.

Plugins are dependent on the LAMMPS binary interface (ABI) and particularly the MPI library used. So they are not guaranteed to work when the plugin was compiled with a different MPI library or different compilation settings or a different LAMMPS version. There are no checks, so if there is a mismatch the plugin object will either not load or data corruption and crashes may happen.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

none
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none
:::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::

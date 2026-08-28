:::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::: {#fix-ipi-command .section}
[]{#index-0}

# fix ipi command[](#fix-ipi-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID ipi address port [unix] [reset]
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- ipi = style name of this fix command

- address = internet address (FQDN or IP), or UNIX socket name

- port = port number (ignored for UNIX sockets)

- zero or more keywords may be appended

- keyword = *unix* or *reset*

  ``` literal-block
  unix args = none = use a unix socket
  reset args = none = reset electrostatics at each call
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 all ipi my.server.com 12345
    fix 1 all ipi mysocket 666 unix reset
:::
::::
:::::

::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

This fix enables LAMMPS to be run as a client for the i-PI Python wrapper [[(IPI)]{.std .std-ref}](#ipihome){.reference .internal}. i-PI is a universal force engine, designed to perform advanced molecular simulations, with a special focus on path integral molecular dynamics (PIMD) simulation. The philosophy behind i-PI is to separate the evaluation of the energy and forces, which is delegated to the client, and the evolution of the dynamics, that is the responsibility of i-PI. This approach also simplifies combining energies computed from different codes, which can for instance be useful to mix first-principles calculations, empirical force fields or machine-learning potentials. The following publication [[(IPI-CPC-2014)]{.std .std-ref}](#ipicpc){.reference .internal} discusses the overall implementation of i-PI, and focuses on path-integral techniques, while a later release [[(IPI-CPC-2019)]{.std .std-ref}](#ipicpc2){.reference .internal} introduces several additional features and simulation schemes.

The communication between i-PI and LAMMPS takes place using sockets, and is reduced to the bare minimum. All the parameters of the dynamics are specified in the input of i-PI, and all the parameters of the force field must be specified as LAMMPS inputs, preceding the *fix ipi* command.

The server address must be specified by the *address* argument, and can be either the IP address, the fully-qualified name of the server, or the name of a UNIX socket for local, faster communication. In the case of internet sockets, the *port* argument specifies the port number on which i-PI is listening, while the *unix* optional switch specifies that the socket is a UNIX socket.

Note that there is no check of data integrity, or that the atomic configurations make sense. It is assumed that the species in the i-PI input are listed in the same order as in the data file of LAMMPS. The initial configuration is ignored, as it will be substituted with the coordinates received from i-PI before forces are ever evaluated.

A note of caution when using potentials that contain long-range electrostatics, or that contain parameters that depend on box size: all of these options will be initialized based on the cell size in the LAMMPS-side initial configuration and kept constant during the run. This is required to e.g. obtain reproducible and conserved forces. If the cell varies too wildly, it may be advisable to re-initialize these interactions at each call. This behavior can be requested by setting the *reset* switch.
:::

::::: {#obtaining-i-pi .section}
## Obtaining i-PI[](#obtaining-i-pi "Link to this heading"){.headerlink}

Here are the commands to set up a virtual environment and install i-PI into it with all its dependencies via the PyPI repository and the pip package manager.

:::: {.highlight-sh .notranslate}
::: highlight
    python -m venv ipienv
    source ipienv/bin/activate
    pip install --upgrade pip
    pip install ipi
:::
::::
:::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

There is no restart information associated with this fix, since all the dynamical parameters are dealt with by i-PI.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

Using this fix on anything other than all atoms requires particular care, since i-PI will know nothing on atoms that are not those whose coordinates are transferred. However, one could use this strategy to define an external potential acting on the atoms that are moved by i-PI.

Since the i-PI code uses atomic units internally, this fix needs to convert LAMMPS data to and from its [[specified units]{.doc}]units.md){.reference .internal} accordingly when communicating with i-PI. This is not possible for reduced units ("units lj") and thus *fix ipi* will stop with an error in this case.

This fix is part of the MISC package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. Because of the use of UNIX domain sockets, this fix will only work in a UNIX environment.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[fix nve]{.doc}]fix_nve.md){.reference .internal}

------------------------------------------------------------------------

**(IPI-CPC-2014)** Ceriotti, More and Manolopoulos, Comp Phys Comm 185, 1019-1026 (2014).

**(IPI-CPC-2019)** Kapil et al., Comp Phys Comm 236, 214-223 (2019).

**(IPI)** [https://ipi-code.org](https://ipi-code.org){.reference .external}
:::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::

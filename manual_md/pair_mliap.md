:::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::: {#pair-style-mliap-command .section}
[]{#index-1}[]{#index-0}

# pair_style mliap command[](#pair-style-mliap-command "Link to this heading"){.headerlink}

Accelerator Variants: *mliap/kk*

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style mliap ... keyword values ...
:::
::::

- one or two keyword/value pairs must be appended

- keyword = *model* or *descriptor* or *unified*

  ``` literal-block
  model values = style filename
    style = linear or quadratic or nn or mliappy
    filename = name of file containing model definitions
  descriptor values = style filename
    style = sna or so3 or ace
    filename = name of file containing descriptor definitions
  unified values = filename ghostneigh_flag
    filename = name of file containing serialized unified Python object
    ghostneigh_flag = 0/1 to turn off/on inclusion of ghost neighbors in neighbors list
  ```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style mliap model linear InP.mliap.model descriptor sna InP.mliap.descriptor
    pair_style mliap model quadratic W.mliap.model descriptor sna W.mliap.descriptor
    pair_style mliap model nn Si.nn.mliap.model descriptor so3 Si.nn.mliap.descriptor
    pair_style mliap model mliappy ACE_NN_Pytorch.pt descriptor ace ccs_single_element.yace
    pair_style mliap unified mliap_unified_lj_Ar.pkl 0
    pair_coeff * * In P
:::
::::
:::::

::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Pair style *mliap* provides a general interface to families of machine-learning interatomic potentials. It allows separate definitions of the interatomic potential functional form (*model*) and the geometric quantities that characterize the atomic positions (*descriptor*).

By defining *model* and *descriptor* separately, it is possible to use many different models with a given descriptor, or many different descriptors with a given model. The pair style currently supports *sna*, *so3* and *ace* descriptor styles, but it is straightforward to add new descriptor styles. By using the *unified* keyword, it is possible to define a Python model that combines functionalities of both *model* and *descriptor*.

The SNAP descriptor style *sna* is the same as that used by [[pair_style snap]{.doc}]pair_snap.md){.reference .internal}, including the linear, quadratic, and chem variants. The available models are *linear*, *quadratic*, *nn*, and *mliappy*. The *mliappy* style can be used to couple python models, e.g. PyTorch neural network energy models, and requires building LAMMPS with the PYTHON package (see below). In order to train a model, it is useful to know the gradient or derivative of energy, force, and stress w.r.t. model parameters. This information can be accessed using the related [[compute mliap]{.doc}]compute_mliap.md){.reference .internal} command.

::: versionadded
[Added in version 2Jun2022.]{.versionmodified .added}
:::

The descriptor style *so3* is a descriptor that is derived from the the smooth SO(3) power spectrum with the explicit inclusion of a radial basis [[(Bartok)]{.std .std-ref}](#bartok2013){.reference .internal} and [[(Zagaceta)]{.std .std-ref}](#zagaceta2020){.reference .internal}. The available models are *linear* and *nn*.

::: versionadded
[Added in version 17Apr2024.]{.versionmodified .added}
:::

The descriptor style *ace* is a class of highly general atomic descriptors, atomic cluster expansion descriptors (ACE) from [[(Drautz)]{.std .std-ref}]compute_pace.md#drautz19){.reference .internal}, that include a radial basis, an angular basis, and bases for other variables (such as chemical species) if relevant. In descriptor style *ace*, the *ace* descriptors may be defined up to an arbitrary body order. This descriptor style is the same as that used in [[pair_style pace]{.doc}]pair_pace.md){.reference .internal} and [[compute pace]{.doc}]compute_pace.md){.reference .internal}. The available models with *ace* in ML-IAP are *linear* and *mliappy*. The *ace* descriptors and models require building LAMMPS with the ML-PACE package (see below). The *mliappy* model style may be used with *ace* descriptors, but it requires that LAMMPS is also built with the PYTHON package. As with other model styles, the *mliappy* model style can be used to couple arbitrary python models that use the *ace* descriptors such as Pytorch NNs. Note that *ALL* mliap model styles with *ace* descriptors require that descriptors and hyperparameters are supplied in a .yace or .ace file, similar to [[compute pace]{.doc}]compute_pace.md){.reference .internal}.

The pair_style *mliap* command must be followed by two keywords *model* and *descriptor* in either order, or the one keyword *unified*. A single *pair_coeff* command is also required. The first 2 arguments must be \* \* so as to span all LAMMPS atom types. This is followed by a list of N arguments that specify the mapping of MLIAP element names to LAMMPS atom types, where N is the number of LAMMPS atom types.

The *model* keyword is followed by the model style. This is followed by a single argument specifying the model filename containing the parameters for a set of elements. The model filename usually ends in the *.mliap.model* extension. It may contain parameters for many elements. The only requirement is that it contain at least those element names appearing in the *pair_coeff* command.

The top of the model file can contain any number of blank and comment lines (start with #), but follows a strict format after that. The first non-blank non-comment line must contain two integers:

- nelems = Number of elements

- nparams = Number of parameters

When the *model* keyword is *linear* or *quadratic*, this is followed by one block for each of the *nelem* elements. Each block consists of *nparams* parameters, one per line. Note that this format is similar, but not identical to that used for the [[pair_style snap]{.doc}]pair_snap.md){.reference .internal} coefficient file. Specifically, the line containing the element weight and radius is omitted, since these are handled by the *descriptor*.

When the *model* keyword is *nn* (neural networks), the model file can contain blank and comment lines (start with #) anywhere. The second non-blank non-comment line must contain the string NET, followed by two integers:

- ndescriptors = Number of descriptors

- nlayers = Number of layers (including the hidden layers and the output layer)

and followed by a sequence of a string and an integer for each layer:

- Activation function (linear, sigmoid, tanh or relu)

- nnodes = Number of nodes

This is followed by one block for each of the *nelem* elements. Each block consists of *scale0* minimum value, *scale1* (maximum - minimum) value, in order to normalize the descriptors, followed by *nparams* parameters, including *bias* and *weights* of the model, starting with the first node of the first layer and so on, with a maximum of 30 values per line.

The detail of *nn* module implementation can be found at [[(Yanxon)]{.std .std-ref}](#yanxon2020){.reference .internal}.

::: {.note .admonition}
Notes on mliappy models

When the *model* keyword is *mliappy*, if the filename ends in '.pt', or '.pth', it will be loaded using pytorch; otherwise, it will be loaded as a pickle file. To load a model from memory (i.e. an existing python object), specify the filename as "LATER", and then call lammps.mliap.load_model(model) from python before using the pair style. When using LAMMPS via the library mode, you will need to call lammps.mliappy.activate_mliappy(lmp) on the active LAMMPS object before the pair style is defined. This call locates and loads the mliap-specific python module that is built into LAMMPS.
:::

The *descriptor* keyword is followed by a descriptor style, and additional arguments. Currently three descriptor styles are available: *sna*, *so3*, and *ace*.

- *sna* indicates the bispectrum component descriptors used by the Spectral Neighbor Analysis Potential (SNAP) potentials of [[pair_style snap]{.doc}]pair_snap.md){.reference .internal}. A single additional argument specifies the descriptor filename containing the parameters and setting used by the SNAP descriptor. The descriptor filename usually ends in the *.mliap.descriptor* extension.

- *so3* indicated the power spectrum component descriptors. A single additional argument specifies the descriptor filename containing the parameters and setting.

- *ace* indicates the atomic cluster expansion (ACE) descriptors. A single additional argument specifies the filename containing parameters, settings, and definitions of the ace descriptors (through tabulated basis function indices and corresponding generalized Clebsch-Gordan coefficients) in the ctilde file format, e.g. in the potential file format with \*.ace or \*.yace extensions from [[pair_style pace]{.doc}]pair_pace.md){.reference .internal}. Note that unlike the potential file, the Clebsch-Gordan coefficients in the descriptor file supplied should *NOT* be multiplied by linear or square root embedding terms.

The SNAP descriptor file closely follows the format of the [[pair_style snap]{.doc}]pair_snap.md){.reference .internal} parameter file. The file can contain blank and comment lines (start with #) anywhere. Each non-blank non-comment line must contain one keyword/value pair. The required keywords are *rcutfac* and *twojmax*. There are many optional keywords that are described on the [[pair_style snap]{.doc}]pair_snap.md){.reference .internal} doc page. In addition, the SNAP descriptor file must contain the *nelems*, *elems*, *radelems*, and *welems* keywords. The *nelems* keyword specifies the number of elements provided in the other three keywords. The *elems* keyword is followed by a list of *nelems* element names that must include the element names appearing in the *pair_coeff* command, but can contain other names too. Similarly, the *radelems* and *welems* keywords are followed by lists of *nelems* numbers giving the element radius and element weight of each element. Obviously, the order in which the elements are listed must be consistent for all three keywords.

The SO3 descriptor file is similar to the SNAP descriptor except that it contains a few more arguments (e.g., *nmax* and *alpha*). The preparation of SO3 descriptor and model files can be done with the [PyXtal_FF](https://github.com/MaterSim/PyXtal_FF){.reference .external} package.

The ACE descriptor file differs from the SNAP and SO3 files. It more closely resembles the potential file format for linear or square-root embedding ACE potentials used in the [[pair_style pace]{.doc}]pair_pace.md){.reference .internal}. As noted above, the key difference is that the Clebsch-Gordan coefficients in the descriptor file with *mliap descriptor ace* are *NOT* multiplied by linear or square root embedding terms. In other words,the model is separated from the descriptor definitions and hyperparameters. In [[pair_style pace]{.doc}]pair_pace.md){.reference .internal}, they are combined. The ACE descriptor files required by *mliap* are generated automatically in [FitSNAP](https://github.com/FitSNAP/FitSNAP){.reference .external} during linear, pytorch, etc. ACE model fitting. Additional tools are provided there to prepare *ace* descriptor files and hyperparameters before model fitting. The *ace* descriptor files can also be extracted from ACE model fits in [python-ace.](https://github.com/ICAMS/python-ace){.reference .external}. It is important to note that order of the types listed in [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} must match the order of the elements/types listed in the ACE descriptor file for all *mliap* styles when using *ace* descriptors.

See the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} page for alternate ways to specify the path for these *model* and *descriptor* files.

::: {.admonition .note}
Note

To significantly reduce SO3 descriptor/force calculation time, some properties are pre-computed and reused during the calculation. These can consume a significant amount of RAM for simulations of larger systems since their size depends on the total number of neighbors per MPI process.
:::

::: versionadded
[Added in version 3Nov2022.]{.versionmodified .added}
:::

The *unified* keyword is followed by an argument specifying the filename containing the serialized unified Python object and the "ghostneigh" toggle (0/1) to disable/enable the construction of neighbors lists including neighbors of ghost atoms. If the filename ends in '.pt', or '.pth', it will be loaded using pytorch; otherwise, it will be loaded as a pickle file. If ghostneigh is enabled, it is recommended to set [[comm_modify]{.doc}]comm_modify.md){.reference .internal} cutoff manually, such as in the following example.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    variable ninteractions equal 2
    variable cutdist equal 7.5
    variable skin equal 1.0
    variable commcut equal (${ninteractions}*${cutdist})+${skin}
    neighbor ${skin} bin
    comm_modify cutoff ${commcut}
:::
::::

::: {.admonition .note}
Note

To load a model from memory (i.e. an existing python object), call lammps.mliap.load_unified(unified) from python, and then specify the filename as "EXISTS". When using LAMMPS via the library mode, you will need to call lammps.mliappy.activate_mliappy(lmp) on the active LAMMPS object before the pair style is defined. This call locates and loads the mliap-specific python module that is built into LAMMPS.
:::

------------------------------------------------------------------------

Styles with a *gpu*, *intel*, *kk*, *omp*, or *opt* suffix are functionally the same as the corresponding style without the suffix. They have been optimized to run faster, depending on your available hardware, as discussed on the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page. The accelerated styles take the same arguments and should produce the same results, except for round-off and precision issues.

These accelerated styles are part of the GPU, INTEL, KOKKOS, OPENMP, and OPT packages, respectively. They are only enabled if LAMMPS was built with those packages. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

You can specify the accelerated styles explicitly in your input script by including their suffix, or you can use the [[-suffix command-line switch]{.doc}]Run_options.md){.reference .internal} when you invoke LAMMPS, or you can use the [[suffix]{.doc}]suffix.md){.reference .internal} command in your input script.

See the [[Accelerator packages]{.doc}]Speed_packages.md){.reference .internal} page for more instructions on how to use the accelerated styles effectively.
:::::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

For atom type pairs I,J and I != J, where types I and J correspond to two different element types, mixing is performed by LAMMPS with user-specifiable parameters as described above. You never need to specify a pair_coeff command with I != J arguments for this style.

This pair style does not support the [[pair_modify]{.doc}]pair_modify.md){.reference .internal} shift, table, and tail options.

This pair style does not write its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, since it is stored in potential files. Thus, you need to re-specify the pair_style and pair_coeff commands in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This pair style is part of the ML-IAP package. It is only enabled if LAMMPS was built with that package. In addition, building LAMMPS with the ML-IAP package requires building LAMMPS with the ML-SNAP package. The *mliappy* model requires building LAMMPS with the PYTHON package. The *ace* descriptor requires building LAMMPS with the ML-PACE package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info. Note that pair_mliap/kk acceleration will *not* invoke the kk accelerated variants of SNAP or ACE descriptors.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_style snap]{.doc}]pair_snap.md){.reference .internal}, [[compute mliap]{.doc}]compute_mliap.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

none

------------------------------------------------------------------------

**(Bartok2013)** Bartok, Kondor, Csanyi, Phys Rev B, 87, 184115 (2013).

**(Zagaceta2020)** Zagaceta, Yanxon, Zhu, J Appl Phys, 128, 045113 (2020).

**(Yanxon2020)** Yanxon, Zagaceta, Tang, Matteson, Zhu, Mach. Learn.: Sci. Technol. 2, 027001 (2020).
:::
::::::::::::::::::::::
:::::::::::::::::::::::
::::::::::::::::::::::::

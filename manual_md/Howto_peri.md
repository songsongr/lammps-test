::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#peridynamics-with-lammps .section}
# [10.5.9. ]{.section-number}Peridynamics with LAMMPS[](#peridynamics-with-lammps "Link to this heading"){.headerlink}

This Howto is based on the Sandia report 2010-5549 by Michael L. Parks, Pablo Seleson, Steven J. Plimpton, Richard B. Lehoucq, and Stewart A. Silling.

::: {#overview .section}
## Overview[](#overview "Link to this heading"){.headerlink}

Peridynamics is a nonlocal extension of classical continuum mechanics. The discrete peridynamic model has the same computational structure as a molecular dynamics model. This Howto provides a brief overview of the peridynamic model of a continuum, then discusses how the peridynamic model is discretized within LAMMPS as described in the original article [[(Parks)]{.std .std-ref}](#parks2){.reference .internal}. An example problem with comments is also included.
:::

::::: {#quick-start .section}
## Quick Start[](#quick-start "Link to this heading"){.headerlink}

The peridynamics styles are included in the optional [[PERI package]{.std .std-ref}]Packages_details.md#pkg-peri){.reference .internal}. If your LAMMPS executable does not already include the PERI package, you can see the [[build instructions for packages]{.doc}]Build_package.md){.reference .internal} for how to enable the package when compiling a custom version of LAMMPS from source.

Here is a minimal example for setting up a peridynamics simulation.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    units         si
    boundary      s s s
    lattice       sc 0.0005
    atom_style    peri
    atom_modify   map array
    neighbor      0.0010 bin
    region        target cylinder y 0.0 0.0 0.0050 -0.0050 0.0 units box
    create_box    1 target
    create_atoms  1 region target

    pair_style    peri/pmb
    pair_coeff    * * 1.6863e22 0.0015001 0.0005 0.25
    set           group all density 2200
    set           group all volume 1.25e-10
    velocity      all set 0.0 0.0 0.0 sum no units box
    fix           1 all nve
    compute       1 all damage/atom
    timestep      1.0e-7
:::
::::

Some notes on this input example:

- peridynamics simulations typically use SI [[units]{.doc}]units.md){.reference .internal}

- particles must be created on a [[simple cubic lattice]{.doc}]lattice.md){.reference .internal}

- using the [[atom style peri]{.doc}]atom_style.md){.reference .internal} is required

- an [[atom map]{.doc}]atom_modify.md){.reference .internal} is required for indexing particles

- The [[skin distance]{.doc}]neighbor.md){.reference .internal} used when computing neighbor lists should be defined appropriately for your choice of simulation parameters. The *skin* should be set to a value such that the peridynamic horizon plus the skin distance is larger than the maximum possible distance between two bonded particles (before their bond breaks). Here it is set to 0.001 meters.

- a [[peridynamics pair style]{.doc}]pair_peri.md){.reference .internal} is required. Available choices are currently: *peri/eps*, *peri/lps*, *peri/pmb*, and *peri/ves*. The model parameters are set with a [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command.

- the mass density and volume fraction for each particle must be defined. This is done with the two [[set]{.doc}]set.md){.reference .internal} commands for *density* and *volume*. For a simple cubic lattice, the volume of a particle should be equal to the cube of the lattice constant, here [\\(V_i = \\Delta x \^3\\)]{.math .notranslate .nohighlight}.

- with the [[velocity]{.doc}]velocity.md){.reference .internal} command all particles are initially at rest

- a plain [[velocity-Verlet time integrator]{.doc}]fix_nve.md){.reference .internal} is used, which is algebraically equivalent to a centered difference in time, but numerically more stable

- you can compute the damage at the location of each particle with [[compute damage/atom]{.doc}]compute_damage_atom.md){.reference .internal}

- finally, the timestep is set to 0.1 microseconds with the [[timestep]{.doc}]timestep.md){.reference .internal} command.
:::::

::::::::::::::::::::::::::: {#peridynamic-model-of-a-continuum .section}
## Peridynamic Model of a Continuum[](#peridynamic-model-of-a-continuum "Link to this heading"){.headerlink}

The following is not a complete overview of peridynamics, but a discussion of only those details specific to the model we have implemented within LAMMPS. For more on the peridynamic theory, the reader is referred to [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}. To begin, we define the notation we will use.

:::::: {#basic-notation .section}
### Basic Notation[](#basic-notation "Link to this heading"){.headerlink}

Within the peridynamic literature, the following notational conventions are generally used. The position of a given point in the reference configuration is [\\(\\textbf{x}\\)]{.math .notranslate .nohighlight}. Let [\\(\\mathbf{u}(\\mathbf{x},t)\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{y}(\\mathbf{x},t)\\)]{.math .notranslate .nohighlight} denote the displacement and position, respectively, of the point [\\(\\mathbf{x}\\)]{.math .notranslate .nohighlight} at time [\\(t\\)]{.math .notranslate .nohighlight}. Define the relative position and displacement vectors of two bonded points [\\(\\textbf{x}\\)]{.math .notranslate .nohighlight} and [\\(\\textbf{x}\^\\prime\\)]{.math .notranslate .nohighlight} as [\\(\\mathbf{\\xi} = \\textbf{x}\^\\prime - \\textbf{x}\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{\\eta} = \\textbf{u}(\\textbf{x}\^\\prime,t) - \\textbf{u}(\\textbf{x},t)\\)]{.math .notranslate .nohighlight}, respectively. We note here that [\\(\\mathbf{\\eta}\\)]{.math .notranslate .nohighlight} is time-dependent, and that [\\(\\mathbf{\\xi}\\)]{.math .notranslate .nohighlight} is not. It follows that the relative position of the two bonded points in the current configuration can be written as [\\(\\boldsymbol{\\xi} + \\boldsymbol{\\eta} = \\mathbf{y}(\\mathbf{x}\^{\\prime},t)-\\mathbf{y}(\\mathbf{x},t)\\)]{.math .notranslate .nohighlight}.

Peridynamic models are frequently written using *states*, which we briefly describe here. For the purposes of our discussion, all states are operators that act on vectors in [\\(\\mathbb{R}\^3\\)]{.math .notranslate .nohighlight}. For a more complete discussion of states, see [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}. A *vector state* is an operator whose image is a vector, and may be viewed as a generalization of a second-rank tensor. Similarly, a *scalar state* is an operator whose image is a scalar. Of particular interest is the vector force state [\\(\\underline{\\mathbf{T}}\\left\[ \\mathbf{x},t \\right\]\\left\< \\mathbf{x}\^{\\prime}-\\mathbf{x} \\right\>\\)]{.math .notranslate .nohighlight}, which is a mapping, having units of force per volume squared, of the vector [\\(\\mathbf{x}\^{\\prime}-\\mathbf{x}\\)]{.math .notranslate .nohighlight} to the force vector state field. The vector state operator [\\(\\underline{\\mathbf{T}}\\)]{.math .notranslate .nohighlight} may itself be a function of [\\(\\mathbf{x}\\)]{.math .notranslate .nohighlight} and [\\(t\\)]{.math .notranslate .nohighlight}. The constitutive model is completely contained within [\\(\\underline{\\mathbf{T}}\\)]{.math .notranslate .nohighlight}.

In the peridynamic theory, the deformation at a point depends collectively on all points interacting with that point. Using the notation of [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}, we write the peridynamic equation of motion as

::: {#perinewtonii .math .notranslate .nohighlight}
\\\[\\rho(\\mathbf{x}) \\ddot{\\mathbf{u}}(\\mathbf{x},t) = \\int\_{\\mathcal{H}\_{\\mathbf{x}}} \\left\\{ \\underline{\\mathbf{T}}\\left\[\\mathbf{x},t \\right\]\\left\<\\mathbf{x}\^{\\prime}-\\mathbf{x} \\right\> - \\underline{\\mathbf{T}}\\left\[\\mathbf{x}\^{\\prime},t \\right\]\\left\<\\mathbf{x}-\\mathbf{x}\^{\\prime} \\right\> \\right\\} {d}V\_{\\mathbf{x}\^\\prime} + \\mathbf{b}(\\mathbf{x},t), \\qquad\\qquad\\textrm{(1)}\\\]
:::

where [\\(\\rho\\)]{.math .notranslate .nohighlight} represents the mass density, [\\(\\underline{\\mathbf{T}}\\)]{.math .notranslate .nohighlight} the force vector state, and [\\(\\mathbf{b}\\)]{.math .notranslate .nohighlight} an external body force density. A point [\\(\\mathbf{x}\\)]{.math .notranslate .nohighlight} interacts with all the points [\\(\\mathbf{x}\^{\\prime}\\)]{.math .notranslate .nohighlight} within the neighborhood [\\(\\mathcal{H}\_{\\mathbf{x}}\\)]{.math .notranslate .nohighlight}, assumed to be a spherical region of radius [\\(\\delta\>0\\)]{.math .notranslate .nohighlight} centered at [\\(\\mathbf{x}\\)]{.math .notranslate .nohighlight}. [\\(\\delta\\)]{.math .notranslate .nohighlight} is called the *horizon*, and is analogous to the cutoff radius used in molecular dynamics. Conditions on [\\(\\underline{\\mathbf{T}}\\)]{.math .notranslate .nohighlight} for which [[(1)]{.std .std-ref}](#perinewtonii){.reference .internal} satisfies the balance of linear and angular momentum are given in [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}.

We consider only force vector states that can be written as

::: {.math .notranslate .nohighlight}
\\\[\\underline{\\mathbf{T}} = \\underline{t}\\,\\underline{\\mathbf{M}},\\\]
:::

with [\\(\\underline{t}\\)]{.math .notranslate .nohighlight} a *scalar force state* and [\\(\\underline{\\mathbf{M}}\\)]{.math .notranslate .nohighlight} the *deformed direction vector state*, defined by

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\underline{\\mathbf{M}}\\left\< \\boldsymbol{\\xi} \\right\> = \\left\\{ \\begin{array}{cl} \\frac{\\boldsymbol{\\xi} + \\boldsymbol{\\eta}}{ \\left\\Vert \\boldsymbol{\\xi} + \\boldsymbol{\\eta} \\right\\Vert } & \\left\\Vert \\boldsymbol{\\xi} + \\boldsymbol{\\eta} \\right\\Vert \\neq 0 \\\\ \\boldsymbol{0} & \\textrm{otherwise} \\end{array} \\right. . \\qquad\\qquad\\textrm{(2)}\\end{split}\\\]
:::

Such force states correspond to so-called *ordinary* materials [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}. These are the materials for which the force between any two interacting points [\\(\\textbf{x}\\)]{.math .notranslate .nohighlight} and [\\(\\textbf{x}\^\\prime\\)]{.math .notranslate .nohighlight} acts along the line between the points.
::::::

::::::::::: {#linear-peridynamic-solid-lps-model .section}
### Linear Peridynamic Solid (LPS) Model[](#linear-peridynamic-solid-lps-model "Link to this heading"){.headerlink}

We summarize the linear peridynamic solid (LPS) material model. For more on this model, the reader is referred to [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}. This model is a nonlocal analogue to a classical linear elastic isotropic material. The elastic properties of a classical linear elastic isotropic material are determined by (for example) the bulk and shear moduli. For the LPS model, the elastic properties are analogously determined by the bulk and shear moduli, along with the horizon [\\(\\delta\\)]{.math .notranslate .nohighlight}.

The LPS model has a force scalar state

::: {.math .notranslate .nohighlight}
\\\[\\underline{t} = \\frac{3K\\theta}{m}\\underline{\\omega}\\,\\underline{x} + \\alpha \\underline{\\omega}\\,\\underline{e}\^\\mathrm{d}, \\qquad\\qquad\\textrm{(3)}\\\]
:::

with [\\(K\\)]{.math .notranslate .nohighlight} the bulk modulus and [\\(\\alpha\\)]{.math .notranslate .nohighlight} related to the shear modulus [\\(G\\)]{.math .notranslate .nohighlight} as

::: {.math .notranslate .nohighlight}
\\\[\\alpha = \\frac{15 G}{m}.\\\]
:::

The remaining components of the model are described as follows. Define the reference position scalar state [\\(\\underline{x}\\)]{.math .notranslate .nohighlight} so that [\\(\\underline{x}\\left\<\\boldsymbol{\\xi} \\right\> = \\left\\Vert \\boldsymbol{\\xi} \\right\\Vert\\)]{.math .notranslate .nohighlight}. Then, the weighted volume [\\(m\\)]{.math .notranslate .nohighlight} is defined as

::: {.math .notranslate .nohighlight}
\\\[m\\left\[ \\mathbf{x} \\right\] = \\int\_{\\mathcal{H}\_\\mathbf{x}} \\underline{\\omega} \\left\<\\boldsymbol{\\xi}\\right\> \\underline{x}\\left\<\\boldsymbol{\\xi} \\right\> \\underline{x}\\left\<\\boldsymbol{\\xi} \\right\>{d}V\_{\\boldsymbol{\\xi} }. \\qquad\\qquad\\textrm{(4)}\\\]
:::

Let

::: {.math .notranslate .nohighlight}
\\\[\\underline{e}\\left\[ \\mathbf{x},t \\right\] \\left\<\\boldsymbol{\\xi} \\right\> = \\left\\Vert \\boldsymbol{\\xi} + \\boldsymbol{\\eta} \\right\\Vert - \\left\\Vert \\boldsymbol{\\xi} \\right\\Vert\\\]
:::

be the extension scalar state, and

::: {.math .notranslate .nohighlight}
\\\[\\theta\\left\[ \\mathbf{x}, t \\right\] = \\frac{3}{m\\left\[ \\mathbf{x} \\right\]}\\int\_{\\mathcal{H}\_\\mathbf{x}} \\underline{\\omega} \\left\<\\boldsymbol{\\xi}\\right\> \\underline{x}\\left\<\\boldsymbol{\\xi} \\right\> \\underline{e}\\left\[ \\mathbf{x},t \\right\]\\left\<\\boldsymbol{\\xi} \\right\>{d}V\_{\\boldsymbol{\\xi}}\\\]
:::

be the dilatation. The isotropic and deviatoric parts of the extension scalar state are defined, respectively, as

::: {.math .notranslate .nohighlight}
\\\[\\underline{e}\^\\mathrm{i}=\\frac{\\theta \\underline{x}}{3}, \\qquad \\underline{e}\^\\mathrm{d} = \\underline{e}- \\underline{e}\^\\mathrm{i},\\\]
:::

where the arguments of the state functions and the vectors on which they operate are omitted for simplicity. We note that the LPS model is linear in the dilatation [\\(\\theta\\)]{.math .notranslate .nohighlight}, and in the deviatoric part of the extension [\\(\\underline{e}\^\\mathrm{d}\\)]{.math .notranslate .nohighlight}.

::: {.admonition .note}
Note

The weighted volume [\\(m\\)]{.math .notranslate .nohighlight} is time-independent, and does not change as bonds break. It is computed with respect to the bond family defined at the reference (initial) configuration.
:::

The non-negative scalar state [\\(\\underline{\\omega}\\)]{.math .notranslate .nohighlight} is an *influence function* [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}. For more on influence functions, see [[(Seleson 2010)]{.std .std-ref}](#seleson2010){.reference .internal}. If an influence function [\\(\\underline{\\omega}\\)]{.math .notranslate .nohighlight} depends only upon the scalar [\\(\\left\\Vert \\boldsymbol{\\xi} \\right\\Vert\\)]{.math .notranslate .nohighlight}, (i.e., [\\(\\underline{\\omega}\\left\<\\boldsymbol{\\xi}\\right\> = \\underline{\\omega}\\left\<\\left\\Vert \\boldsymbol{\\xi} \\right\\Vert\\right\>\\)]{.math .notranslate .nohighlight}), then [\\(\\underline{\\omega}\\)]{.math .notranslate .nohighlight} is a spherical influence function. For a spherical influence function, the LPS model is isotropic [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}.

::: {.admonition .note}
Note

In the LAMMPS implementation of the LPS model, the influence function [\\(\\underline{\\omega}\\left\<\\left\\Vert \\boldsymbol{\\xi} \\right\\Vert\\right\> = 1 / \\left\\Vert \\boldsymbol{\\xi} \\right\\Vert\\)]{.math .notranslate .nohighlight} is used. However, the user can define their own influence function by altering the method "influence_function" in the file [`pair_peri_lps.cpp`{.docutils .literal .notranslate}]{.pre}. The LAMMPS peridynamics code permits both spherical and non-spherical influence functions (e.g., isotropic and non-isotropic materials).
:::
:::::::::::

::::::::: {#prototype-microelastic-brittle-pmb-model .section}
### Prototype Microelastic Brittle (PMB) Model[](#prototype-microelastic-brittle-pmb-model "Link to this heading"){.headerlink}

We summarize the prototype microelastic brittle (PMB) material model. For more on this model, the reader is referred to [[(Silling 2000)]{.std .std-ref}](#silling2000-2){.reference .internal} and [[(Silling 2005)]{.std .std-ref}](#silling2005){.reference .internal}. This model is a special case of the LPS model; see [[(Seleson 2010)]{.std .std-ref}](#seleson2010){.reference .internal} for the derivation. The elastic properties of the PMB model are determined by the bulk modulus [\\(K\\)]{.math .notranslate .nohighlight} and the horizon [\\(\\delta\\)]{.math .notranslate .nohighlight}.

The PMB model is expressed using the scalar force state field

::: {#peripmbstate .math .notranslate .nohighlight}
\\\[\\underline{t}\\left\[ \\mathbf{x},t \\right\]\\left\< \\boldsymbol{\\xi} \\right\> = \\frac{1}{2} f\\left( \\boldsymbol{\\eta} ,\\boldsymbol{\\xi} \\right), \\qquad\\qquad\\textrm{(5)}\\\]
:::

with [\\(f\\)]{.math .notranslate .nohighlight} a scalar-valued function. We assume that [\\(f\\)]{.math .notranslate .nohighlight} takes the form

::: {.math .notranslate .nohighlight}
\\\[f = c s,\\\]
:::

where

::: {#peric .math .notranslate .nohighlight}
\\\[c = \\frac{18K}{\\pi \\delta\^4}, \\qquad\\qquad\\textrm{(6)}\\\]
:::

with [\\(K\\)]{.math .notranslate .nohighlight} the bulk modulus and [\\(\\delta\\)]{.math .notranslate .nohighlight} the horizon, and [\\(s\\)]{.math .notranslate .nohighlight} the bond stretch, defined as

::: {.math .notranslate .nohighlight}
\\\[s(t,\\mathbf{\\eta},\\mathbf{\\xi}) = \\frac{ \\left\\Vert {\\mathbf{\\eta}+\\mathbf{\\xi}} \\right\\Vert - \\left\\Vert {\\mathbf{\\xi}} \\right\\Vert }{\\left\\Vert {\\mathbf{\\xi}} \\right\\Vert}.\\\]
:::

Bond stretch is a unitless quantity, and identical to a one-dimensional definition of strain. As such, we see that a bond at its equilibrium length has stretch [\\(s=0\\)]{.math .notranslate .nohighlight}, and a bond at twice its equilibrium length has stretch [\\(s=1\\)]{.math .notranslate .nohighlight}. The constant [\\(c\\)]{.math .notranslate .nohighlight} given above is appropriate for 3D models only. For more on the origins of the constant [\\(c\\)]{.math .notranslate .nohighlight}, see [[(Silling 2005)]{.std .std-ref}](#silling2005){.reference .internal}. For the derivation of [\\(c\\)]{.math .notranslate .nohighlight} for 1D and 2D models, see [[(Emmrich)]{.std .std-ref}](#emmrich2007){.reference .internal}.

Given [[(5)]{.std .std-ref}](#peripmbstate){.reference .internal}, [[(1)]{.std .std-ref}](#perinewtonii){.reference .internal} reduces to

::: {.math .notranslate .nohighlight}
\\\[\\rho(\\mathbf{x}) \\ddot{\\mathbf{u}}(\\mathbf{x},t) = \\int\_{\\mathcal{H}\_\\mathbf{x}} \\mathbf{f} \\left( \\boldsymbol{\\eta},\\boldsymbol{\\xi} \\right){d}V\_{\\boldsymbol{\\xi}} + \\mathbf{b}(\\mathbf{x},t), \\qquad\\qquad\\textrm{(7)}\\\]
:::

with

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{f} \\left( \\boldsymbol{\\eta}, \\boldsymbol{\\xi}\\right) =f \\left( \\boldsymbol{\\eta}, \\boldsymbol{\\xi}\\right) \\frac{\\boldsymbol{\\xi}+ \\boldsymbol{\\eta}}{ \\left\\Vert {\\boldsymbol{\\xi} + \\boldsymbol{\\eta}} \\right\\Vert}.\\\]
:::

Unlike the LPS model, the PMB model has a Poisson ratio of [\\(\\nu=1/4\\)]{.math .notranslate .nohighlight} in 3D, and [\\(\\nu=1/3\\)]{.math .notranslate .nohighlight} in 2D. This is reflected in the input for the PMB model, which requires only the bulk modulus of the material, whereas the LPS model requires both the bulk and shear moduli.
:::::::::

:::::: {#damage .section}
[]{#peridamage}

### Damage[](#damage "Link to this heading"){.headerlink}

Bonds are made to break when they are stretched beyond a given limit. Once a bond fails, it is failed forever [[(Silling)]{.std .std-ref}](#silling2005){.reference .internal}. Further, new bonds are never created during the course of a simulation. We discuss only one criterion for bond breaking, called the *critical stretch* criterion.

Define [\\(\\mu\\)]{.math .notranslate .nohighlight} to be the history-dependent scalar boolean function

::: {#perimu .math .notranslate .nohighlight}
\\\[\\begin{split}\\mu(t,\\mathbf{\\eta},\\mathbf{\\xi}) = \\left\\{ \\begin{array}{cl} 1 & \\mbox{if \$s(t\^\\prime,\\mathbf{\\eta},\\mathbf{\\xi})\< \\min \\left(s_0(t\^\\prime,\\mathbf{\\eta},\\mathbf{\\xi}) , s_0(t\^\\prime,\\mathbf{\\eta}\^\\prime,\\mathbf{\\xi}\^\\prime) \\right)\$ for all \$0 \\leq t\^\\prime \\leq t\$} \\\\ 0 & \\mbox{otherwise} \\end{array}\\right\\}. \\qquad\\qquad\\textrm{(8)}\\end{split}\\\]
:::

where [\\(\\mathbf{\\eta}\^\\prime = \\textbf{u}(\\textbf{x}\^{\\prime \\prime},t) - \\textbf{u}(\\textbf{x}\^\\prime,t)\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{\\xi}\^\\prime = \\textbf{x}\^{\\prime \\prime} - \\textbf{x}\^\\prime\\)]{.math .notranslate .nohighlight}. Here, [\\(s_0(t,\\mathbf{\\eta},\\mathbf{\\xi})\\)]{.math .notranslate .nohighlight} is a critical stretch defined as

::: {#peris0 .math .notranslate .nohighlight}
\\\[s_0(t,\\mathbf{\\eta},\\mathbf{\\xi}) = s\_{00} - \\alpha s\_{\\min}(t,\\mathbf{\\eta},\\mathbf{\\xi}), \\qquad s\_{\\min}(t) = \\min\_{\\mathbf{\\xi}} s(t,\\mathbf{\\eta},\\mathbf{\\xi}), \\qquad\\qquad\\textrm{(9)}\\\]
:::

where [\\(s\_{00}\\)]{.math .notranslate .nohighlight} and [\\(\\alpha\\)]{.math .notranslate .nohighlight} are material-dependent constants. The history function [\\(\\mu\\)]{.math .notranslate .nohighlight} breaks bonds when the stretch [\\(s\\)]{.math .notranslate .nohighlight} exceeds the critical stretch [\\(s_0\\)]{.math .notranslate .nohighlight}.

Although [\\(s_0(t,\\mathbf{\\eta},\\mathbf{\\xi})\\)]{.math .notranslate .nohighlight} is expressed as a property of a particle, bond breaking must be a symmetric operation for all particle pairs sharing a bond. That is, particles [\\(\\textbf{x}\\)]{.math .notranslate .nohighlight} and [\\(\\textbf{x}\^\\prime\\)]{.math .notranslate .nohighlight} must utilize the same test when deciding to break their common bond. This can be done by any method that treats the particles symmetrically. In the definition of [\\(\\mu\\)]{.math .notranslate .nohighlight} above, we have chosen to take the minimum of the two [\\(s_0\\)]{.math .notranslate .nohighlight} values for particles [\\(\\textbf{x}\\)]{.math .notranslate .nohighlight} and [\\(\\textbf{x}\^\\prime\\)]{.math .notranslate .nohighlight} when determining if the [\\(\\textbf{x}\\)]{.math .notranslate .nohighlight}--[\\(\\textbf{x}\^\\prime\\)]{.math .notranslate .nohighlight} bond should be broken.

Following [[(Silling)]{.std .std-ref}](#silling2005){.reference .internal}, we can define the damage at a point [\\(\\textbf{x}\\)]{.math .notranslate .nohighlight} as

::: {#peridamageeq .math .notranslate .nohighlight}
\\\[\\varphi(\\textbf{x}, t) = 1 - \\frac{\\int\_{\\mathcal{H}\_{\\textbf{x}}} \\mu(t,\\mathbf{\\eta},\\mathbf{\\xi}) dV\_{\\textbf{x}\^\\prime} }{ \\int\_{\\mathcal{H}\_{\\textbf{x}}} dV\_{\\textbf{x}\^\\prime} }. \\qquad\\qquad\\textrm{(10)}\\\]
:::
::::::
:::::::::::::::::::::::::::

::::::::::::::::::::::::::: {#discrete-peridynamic-model-and-lammps-implementation .section}
## Discrete Peridynamic Model and LAMMPS Implementation[](#discrete-peridynamic-model-and-lammps-implementation "Link to this heading"){.headerlink}

In LAMMPS, instead of [[(1)]{.std .std-ref}](#perinewtonii){.reference .internal}, we model this equation of motion:

::: {.math .notranslate .nohighlight}
\\\[\\rho(\\mathbf{x}) \\ddot{\\textbf{y}}(\\mathbf{x},t) = \\int\_{\\mathcal{H}\_{\\mathbf{x}}} \\left\\{ \\underline{\\mathbf{T}}\\left\[ \\mathbf{x},t \\right\]\\left\<\\mathbf{x}\^{\\prime}-\\mathbf{x} \\right\> - \\underline{\\mathbf{T}}\\left\[\\mathbf{x}\^{\\prime},t \\right\]\\left\<\\mathbf{x}-\\mathbf{x}\^{\\prime} \\right\> \\right\\} {d}V\_{\\mathbf{x}\^\\prime} + \\mathbf{b}(\\mathbf{x},t),\\\]
:::

where we explicitly track and store at each timestep the positions and not the displacements of the particles. We observe that [\\(\\ddot{\\textbf{y}}(\\textbf{x}, t) = \\ddot{\\textbf{x}} + \\ddot{\\textbf{u}}(\\textbf{x}, t) = \\ddot{\\textbf{u}}(\\textbf{x}, t)\\)]{.math .notranslate .nohighlight}, so that this is equivalent to [[(1)]{.std .std-ref}](#perinewtonii){.reference .internal}.

::::: {#spatial-discretization .section}
### Spatial Discretization[](#spatial-discretization "Link to this heading"){.headerlink}

The region defining a peridynamic material is discretized into particles forming a simple cubic lattice with lattice constant [\\(\\Delta x\\)]{.math .notranslate .nohighlight}, where each particle [\\(i\\)]{.math .notranslate .nohighlight} is associated with some volume fraction [\\(V_i\\)]{.math .notranslate .nohighlight}. For any particle [\\(i\\)]{.math .notranslate .nohighlight}, let [\\(\\mathcal{F}\_i\\)]{.math .notranslate .nohighlight} denote the family of particles for which particle [\\(i\\)]{.math .notranslate .nohighlight} shares a bond in the reference configuration. That is,

::: {#peribondfamily .math .notranslate .nohighlight}
\\\[\\mathcal{F}\_i = \\{ p \~ \| \~ \\left\\Vert {\\textbf{x}\_p - \\textbf{x}\_i} \\right\\Vert \\leq \\delta \\}. \\qquad\\qquad\\textrm{(11)}\\\]
:::

The discretized equation of motion replaces [[(1)]{.std .std-ref}](#perinewtonii){.reference .internal} with

::: {#peridiscretenewtonii .math .notranslate .nohighlight}
\\\[\\rho \\ddot{\\textbf{y}}\_i\^n = \\sum\_{p \\in \\mathcal{F}\_i} \\left\\{ \\underline{\\mathbf{T}}\\left\[ \\textbf{x}\_i,t \\right\]\\left\<\\textbf{x}\_p\^{\\prime}-\\textbf{x}\_i \\right\> - \\underline{\\mathbf{T}}\\left\[\\textbf{x}\_p,t \\right\]\\left\<\\textbf{x}\_i-\\textbf{x}\_p \\right\> \\right\\} V\_{p} + \\textbf{b}\_i\^n, \\qquad\\qquad\\textrm{(12)}\\\]
:::

where [\\(n\\)]{.math .notranslate .nohighlight} is the timestep number and subscripts denote the particle number.
:::::

:::::::: {#short-range-forces .section}
### Short-Range Forces[](#short-range-forces "Link to this heading"){.headerlink}

In the model discussed so far, particles interact only through their bond forces. A particle with no bonds becomes a free non-interacting particle. To account for contact forces, short-range forces are introduced [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}. We add to the force in [[(12)]{.std .std-ref}](#peridiscretenewtonii){.reference .internal} the following force

::: {.math .notranslate .nohighlight}
\\\[\\textbf{f}\_S(\\textbf{y}\_p,\\textbf{y}\_i) = \\min \\left\\{ 0, \\frac{c_S}{\\delta}(\\left\\Vert {\\textbf{y}\_p-\\textbf{y}\_i} \\right\\Vert - d\_{pi}) \\right\\} \\frac{\\textbf{y}\_p-\\textbf{y}\_i}{\\left\\Vert {\\textbf{y}\_p-\\textbf{y}\_i} \\right\\Vert}, \\qquad\\qquad\\textrm{(13)}\\\]
:::

where [\\(d\_{pi}\\)]{.math .notranslate .nohighlight} is the short-range interaction distance between particles [\\(p\\)]{.math .notranslate .nohighlight} and [\\(i\\)]{.math .notranslate .nohighlight}, and [\\(c_S\\)]{.math .notranslate .nohighlight} is a multiple of the constant [\\(c\\)]{.math .notranslate .nohighlight} from [[(6)]{.std .std-ref}](#peric){.reference .internal}. Note that the short-range force is always repulsive, never attractive. In practice, we choose

::: {#perics .math .notranslate .nohighlight}
\\\[c_S = 15 \\frac{18K}{\\pi \\delta\^4}. \\qquad\\qquad\\textrm{(14)}\\\]
:::

For the short-range interaction distance, we choose [[(Silling 2007)]{.std .std-ref}](#silling2007-2){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[d\_{pi} = \\min \\left\\{ 0.9 \\left\\Vert {\\textbf{x}\_p - \\textbf{x}\_i} \\right\\Vert, 1.35 (r_p + r_i) \\right\\}, \\qquad\\qquad\\textrm{(15)}\\\]
:::

where [\\(r_i\\)]{.math .notranslate .nohighlight} is called the *node radius* of particle [\\(i\\)]{.math .notranslate .nohighlight}. Given a discrete lattice, we choose [\\(r_i\\)]{.math .notranslate .nohighlight} to be half the lattice constant.

::: {.admonition .note}
Note

For a simple cubic lattice, [\\(\\Delta x = \\Delta y = \\Delta z\\)]{.math .notranslate .nohighlight}.
:::

Given this definition of [\\(d\_{pi}\\)]{.math .notranslate .nohighlight}, contact forces appear only when particles are under compression.

When accounting for short-range forces, it is convenient to define the short-range family of particles

::: {.math .notranslate .nohighlight}
\\\[\\mathcal{F}\^S_i = \\{ p \~ \| \~ \\left\\Vert {\\textbf{y}\_p - \\textbf{y}\_i} \\right\\Vert \\leq d\_{pi} \\}.\\\]
:::
::::::::

:::: {#modification-to-the-particle-volume .section}
### Modification to the Particle Volume[](#modification-to-the-particle-volume "Link to this heading"){.headerlink}

The right-hand side of [[(12)]{.std .std-ref}](#peridiscretenewtonii){.reference .internal} may be thought of as a midpoint quadrature of [[(1)]{.std .std-ref}](#perinewtonii){.reference .internal}. To slightly improve the accuracy of this quadrature, we discuss a modification to the particle volume used in [[(12)]{.std .std-ref}](#peridiscretenewtonii){.reference .internal}. In a situation where two particles share a bond with [\\(\\left\\Vert { \\textbf{x}\_p - \\textbf{x}\_i }\\right\\Vert = \\delta\\)]{.math .notranslate .nohighlight}, for example, we suppose that only approximately half the volume of each particle is "seen" by the other [[(Silling 2007)]{.std .std-ref}]pair_peri.md#silling2007){.reference .internal}. When computing the force of each particle on the other we use [\\(V_p / 2\\)]{.math .notranslate .nohighlight} rather than [\\(V_p\\)]{.math .notranslate .nohighlight} in [[(12)]{.std .std-ref}](#peridiscretenewtonii){.reference .internal}. As such, we introduce a nodal volume scaling function for all bonded particles where [\\(\\delta - r_i \\leq \\left\\Vert { \\textbf{x}\_p - \\textbf{x}\_i } \\right\\Vert \\leq \\delta\\)]{.math .notranslate .nohighlight} (see the Figure below).

We choose to use a linear unitless nodal volume scaling function

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\nu(\\textbf{x}\_p - \\textbf{x}\_i) = \\left\\{ \\begin{array}{cl} -\\frac{1}{2 r_i} \\left\\Vert {\\textbf{x}\_p - \\textbf{x}\_i} \\right\\Vert + \\left( \\frac{\\delta}{2 r_i} + \\frac{1}{2} \\right) & \\mbox{if } \\delta - r_i \\leq \\left\\Vert {\\textbf{x}\_p - \\textbf{x}\_i } \\right\\Vert \\leq \\delta \\\\ 1 & \\mbox{if } \\left\\Vert {\\textbf{x}\_p - \\textbf{x}\_i } \\right\\Vert \\leq \\delta - r_i \\\\ 0 & \\mbox{otherwise} \\end{array} \\right\\}\\end{split}\\\]
:::

If [\\(\\left\\Vert {\\textbf{x}\_p - \\textbf{x}\_i} \\right\\Vert = \\delta\\)]{.math .notranslate .nohighlight}, [\\(\\nu = 0.5\\)]{.math .notranslate .nohighlight}, and if [\\(\\left\\Vert {\\textbf{x}\_p - \\textbf{x}\_i} \\right\\Vert = \\delta - r_i\\)]{.math .notranslate .nohighlight}, [\\(\\nu = 1.0\\)]{.math .notranslate .nohighlight}, for example.

<figure id="id2" class="align-center align-default" style="width: 80%">
<img src="_images/pdlammps_fig1.png" alt="_images/pdlammps_fig1.png" />
<figcaption><p><span class="caption-text">Diagram showing horizon of a particular particle, demonstrating that the volume associated with particles near the boundary of the horizon is not completely contained within the horizon.</span><a href="#id2" class="headerlink" title="Link to this image"></a></p></figcaption>
</figure>
::::

::: {#temporal-discretization .section}
### Temporal Discretization[](#temporal-discretization "Link to this heading"){.headerlink}

When discretizing time in LAMMPS, we use a velocity-Verlet scheme, where both the position and velocity of the particle are stored explicitly. The velocity-Verlet scheme is generally expressed in three steps. In [[Algorithm 1]{.std .std-ref}](#algvelverlet){.reference .internal}, [\\(\\rho_i\\)]{.math .notranslate .nohighlight} denotes the mass density of a particle and [\\(\\widetilde{\\textbf{f}}\_i\^n\\)]{.math .notranslate .nohighlight} denotes the net force density on particle [\\(i\\)]{.math .notranslate .nohighlight} at timestep [\\(n\\)]{.math .notranslate .nohighlight}. The LAMMPS command [[fix nve]{.doc}]fix_nve.md){.reference .internal} performs a velocity-Verlet integration.

> ::::::: {}
> :::::: {#algvelverlet .tip .admonition}
> Algorithm 1: Velocity Verlet
>
> ::: line
> 1: [\\(\\textbf{v}\_i\^{n + 1/2} = \\textbf{v}\_i\^n + \\frac{\\Delta t}{2 \\rho_i} \\widetilde{\\textbf{f}}\_i\^n\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> 2: [\\(\\textbf{y}\_i\^{n+1} = \\textbf{y}\_i\^n + \\Delta t \\textbf{v}\_i\^{n + 1/2}\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> 3: [\\(\\textbf{v}\_i\^{n+1} = \\textbf{v}\_i\^{n+1/2} + \\frac{\\Delta t}{2 \\rho_i} \\widetilde{\\textbf{f}}\_i\^{n+1}\\)]{.math .notranslate .nohighlight}
> :::
> ::::::
> :::::::
:::

:::: {#breaking-bonds .section}
### Breaking Bonds[](#breaking-bonds "Link to this heading"){.headerlink}

During the course of simulation, it may be necessary to break bonds, as described in the [[Damage section]{.std .std-ref}](#peridamage){.reference .internal}. Bonds are recorded as broken in a simulation by removing them from the bond family [\\(\\mathcal{F}\_i\\)]{.math .notranslate .nohighlight} (see [[(11)]{.std .std-ref}](#peribondfamily){.reference .internal}).

A naive implementation would have us first loop over all bonds and compute [\\(s\_{min}\\)]{.math .notranslate .nohighlight} in [[(9)]{.std .std-ref}](#peris0){.reference .internal}, then loop over all bonds again and break bonds with a stretch [\\(s \> s0\\)]{.math .notranslate .nohighlight} as in [[(8)]{.std .std-ref}](#perimu){.reference .internal}, and finally loop over all particles and compute forces for the next step of [[Algorithm 1]{.std .std-ref}](#algvelverlet){.reference .internal}. For reasons of computational efficiency, we will utilize the values of [\\(s_0\\)]{.math .notranslate .nohighlight} from the *previous* timestep when deciding to break a bond.

::: {.admonition .note}
Note

For the first timestep, [\\(s_0\\)]{.math .notranslate .nohighlight} is initialized to [\\(\\mathbf{\\infty}\\)]{.math .notranslate .nohighlight} for all nodes. This means that no bonds may be broken until the second timestep. As such, it is recommended that the first few timesteps of the peridynamic simulation not involve any actions that might result in the breaking of bonds. As a practical example, the projectile in the [[commented example below]{.std .std-ref}](#periexample){.reference .internal} is placed such that it does not impact the target brittle plate until several timesteps into the simulation.
:::
::::

::: {#lps-pseudocode .section}
### LPS Pseudocode[](#lps-pseudocode "Link to this heading"){.headerlink}

A sketch of the LPS model implementation in the PERI package appears in [[Algorithm 2]{.std .std-ref}](#algperilps){.reference .internal}. This algorithm makes use of the routines in [[Algorithm 3]{.std .std-ref}](#algperilpsm){.reference .internal} and [[Algorithm 4]{.std .std-ref}](#algperilpstheta){.reference .internal}.

> :::::::::::::::::::: {}
> :::::::::::::::::: {#algperilps .tip .admonition}
> Algorithm 2: LPS Peridynamic Model Pseudocode
>
> ::: line
> Fix [\\(s\_{00}\\)]{.math .notranslate .nohighlight}, [\\(\\alpha\\)]{.math .notranslate .nohighlight}, horizon [\\(\\delta\\)]{.math .notranslate .nohighlight}, bulk modulus [\\(K\\)]{.math .notranslate .nohighlight}, shear modulus [\\(G\\)]{.math .notranslate .nohighlight}, timestep [\\(\\Delta t\\)]{.math .notranslate .nohighlight}, and generate initial lattice of particles with lattice constant [\\(\\Delta x\\)]{.math .notranslate .nohighlight}. Let there be [\\(N\\)]{.math .notranslate .nohighlight} particles. Define constant [\\(c_S\\)]{.math .notranslate .nohighlight} for repulsive short-range forces.
> :::
>
> ::: line
> Initialize bonds between all particles [\\(i \\neq j\\)]{.math .notranslate .nohighlight} where [\\(\\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert \\leq \\delta\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> Initialize weighted volume [\\(m\\)]{.math .notranslate .nohighlight} for all particles using [[Algorithm 3]{.std .std-ref}](#algperilpsm){.reference .internal}
> :::
>
> ::: line
> Initialize [\\(s_0 = \\mathbf{\\infty}\\)]{.math .notranslate .nohighlight} {*Initialize each entry to MAX_DOUBLE*}
> :::
>
> ::: line
> **while** not done **do**
> :::
>
> ::: line
> Perform step 1 of [[Algorithm 1]{.std .std-ref}](#algvelverlet){.reference .internal}, updating velocities of all particles
> :::
>
> ::: line
> Perform step 2 of [[Algorithm 1]{.std .std-ref}](#algvelverlet){.reference .internal}, updating positions of all particles
> :::
>
> ::: line
> [\\(\\tilde{s}\_0 = \\mathbf{\\infty}\\)]{.math .notranslate .nohighlight} {*Initialize each entry to MAX_DOUBLE*}
> :::
>
> ::: line
> **for** [\\(i=1\\)]{.math .notranslate .nohighlight} to [\\(N\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> {Compute short-range forces}
> :::
>
> ::: line
> **for all** particles [\\(j \\in \\mathcal{F}\^S_i\\)]{.math .notranslate .nohighlight} (the short-range family of nodes for particle [\\(i\\)]{.math .notranslate .nohighlight}) **do**
> :::
>
> ::: line
> [\\(r = \\left\\Vert {\\textbf{y}\_j - \\textbf{y}\_i} \\right\\Vert\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> [\\(dr = \\min \\{ 0, r - d \\}\\)]{.math .notranslate .nohighlight} {*Short-range forces are only repulsive, never attractive*}
> :::
>
> ::: line
> [\\(k = \\frac{c_S}{\\delta} V_k dr\\)]{.math .notranslate .nohighlight} {[\\(c_S\\)]{.math .notranslate .nohighlight} *defined in :ref:\`(14) \<pericS\>\`*}
> :::
>
> ::: line
> [\\(\\textbf{f} = \\textbf{f} + k \\frac{\\textbf{y}\_j-\\textbf{y}\_i}{\\left\\Vert {\\textbf{y}\_j-\\textbf{y}\_i} \\right\\Vert}\\)]{.math .notranslate .nohighlight}
> :::
> ::::::::::::::::::
>
> ::: line
> **end for**
> :::
> ::::::::::::::::::::
>
> ::: line
> **end for**
> :::
>
> ::: line
> Compute the dilatation for each particle using [[Algorithm 4]{.std .std-ref}](#algperilpstheta){.reference .internal}
> :::
>
> ::: line
> **for** [\\(i=1\\)]{.math .notranslate .nohighlight} to [\\(N\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> {Compute bond forces}
> :::
>
> ::: line
> **for all** particles [\\(j\\)]{.math .notranslate .nohighlight} sharing an unbroken bond with particle [\\(i\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> [\\(e = \\left\\Vert {\\textbf{y}\_j - \\textbf{y}\_i} \\right\\Vert - \\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> [\\(\\omega\_+ = \\underline{\\omega}\\left\<\\textbf{x}\_j - \\textbf{x}\_i\\right\>\\)]{.math .notranslate .nohighlight} {*Influence function evaluation*}
> :::
>
> ::: line
> [\\(\\omega\_- = \\underline{\\omega}\\left\<\\textbf{x}\_i - \\textbf{x}\_j\\right\>\\)]{.math .notranslate .nohighlight} {*Influence function evaluation*}
> :::
>
> ::: line
> [\\(\\hat{f} = \\left\[ (3K-5G)\\left( \\frac{\\theta(i)}{m(i)}\\omega\_+ + \\frac{\\theta(j)}{m(j)}\\omega\_- \\right) \\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert + 15G \\left( \\frac{\\omega\_+}{m(i)} + \\frac{\\omega\_-}{m(j)} \\right) e \\right\] \\nu(\\textbf{x}\_j - \\textbf{x}\_i) V_j\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> [\\(\\textbf{f} = \\textbf{f} + \\hat{f} \\frac{\\textbf{y}\_j-\\textbf{y}\_i}{\\left\\Vert {\\textbf{y}\_j-\\textbf{y}\_i} \\right\\Vert}\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> **if** [\\((dr / \\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert) \> \\min(s_0(i), s_0(j))\\)]{.math .notranslate .nohighlight} **then**
> :::
>
> ::: line
> Break [\\(i\\)]{.math .notranslate .nohighlight}'s bond with [\\(j\\)]{.math .notranslate .nohighlight} {[\\(j\\)]{.math .notranslate .nohighlight} *'s bond with* [\\(i\\)]{.math .notranslate .nohighlight} *will be broken when this loop iterates on* [\\(j\\)]{.math .notranslate .nohighlight}}
> :::
>
> ::: line
> **end if**
> :::
>
> ::: line
> [\\(\\tilde{s}\_0(i) = \\min (\\tilde{s}\_0(i),s\_{00}-\\alpha(dr / \\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert))\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> **end for**
> :::
>
> ::: line
> **end for**
> :::
>
> ::: line
> [\\(s_0 = \\tilde{s}\_0\\)]{.math .notranslate .nohighlight} {*Store for use in next timestep*}
> :::
>
> ::: line
> Perform step 3 of [[Algorithm 1]{.std .std-ref}](#algvelverlet){.reference .internal}, updating velocities of all particles
> :::
>
> ::: line
> **end while**
> :::
>
> ::::::: {#algperilpsm .tip .admonition}
> Algorithm 3: Computation of Weighted Volume *m*
>
> ::: line
> **for** [\\(i=1\\)]{.math .notranslate .nohighlight} to [\\(N\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> [\\(m(i) = 0.0\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> **for all** particles [\\(j\\)]{.math .notranslate .nohighlight} sharing a bond with particle [\\(i\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> [\\(m(i) = m(i) + \\underline{\\omega}\\left\<\\textbf{x}\_j - \\textbf{x}\_i\\right\> \\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert\^2 \\nu(\\textbf{x}\_j - \\textbf{x}\_i) V_j\\)]{.math .notranslate .nohighlight}
> :::
> :::::::
>
> ::: line
> **end for**
> :::
>
> ::: line
> **end for**
> :::
>
> :::::::: {#algperilpstheta .tip .admonition}
> Algorithm 4: Computation of Dilatation [\\(\\theta\\)]{.math .notranslate .nohighlight}
>
> ::: line
> **for** [\\(i=1\\)]{.math .notranslate .nohighlight} to [\\(N\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> [\\(\\theta(i) = 0.0\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> **for all** particles [\\(j\\)]{.math .notranslate .nohighlight} sharing an unbroken bond with particle [\\(i\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> [\\(e = \\left\\Vert {\\textbf{y}\_i - \\textbf{y}\_j} \\right\\Vert - \\left\\Vert {\\textbf{x}\_i - \\textbf{x}\_j} \\right\\Vert\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> [\\(\\theta(i) = \\theta(i) + \\underline{\\omega}\\left\<\\textbf{x}\_j - \\textbf{x}\_i\\right\> \\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert e \\nu(\\textbf{x}\_j - \\textbf{x}\_i) V_j\\)]{.math .notranslate .nohighlight}
> :::
> ::::::::
>
> ::: line
> **end for**
> :::
>
> ::: line
> [\\(\\theta(i) = \\frac{3}{m(i)}\\theta(i)\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> **end for**
> :::
:::

::: {#pmb-pseudocode .section}
### PMB Pseudocode[](#pmb-pseudocode "Link to this heading"){.headerlink}

A sketch of the PMB model implementation in the PERI package appears in [[Algorithm 5]{.std .std-ref}](#algperipmb){.reference .internal}.

> ::::::::::::::::::: {}
> ::::::::::::::::: {#algperipmb .tip .admonition}
> Algorithm 5: PMB Peridynamic Model Pseudocode
>
> ::: line
> Fix [\\(s\_{00}\\)]{.math .notranslate .nohighlight}, [\\(\\alpha\\)]{.math .notranslate .nohighlight}, horizon [\\(\\delta\\)]{.math .notranslate .nohighlight}, spring constant [\\(c\\)]{.math .notranslate .nohighlight}, timestep [\\(\\Delta t\\)]{.math .notranslate .nohighlight}, and generate initial lattice of particles with lattice constant [\\(\\Delta x\\)]{.math .notranslate .nohighlight}. Let there be [\\(N\\)]{.math .notranslate .nohighlight} particles.
> :::
>
> ::: line
> Initialize bonds between all particles [\\(i \\neq j\\)]{.math .notranslate .nohighlight} where [\\(\\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert \\leq \\delta\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> Initialize [\\(s_0 = \\mathbf{\\infty}\\)]{.math .notranslate .nohighlight} {*Initialize each entry to MAX_DOUBLE*}
> :::
>
> ::: line
> **while** not done **do**
> :::
>
> ::: line
> Perform step 1 of [[Algorithm 1]{.std .std-ref}](#algvelverlet){.reference .internal}, updating velocities of all particles
> :::
>
> ::: line
> Perform step 2 of [[Algorithm 1]{.std .std-ref}](#algvelverlet){.reference .internal}, updating positions of all particles
> :::
>
> ::: line
> [\\(\\tilde{s}\_0 = \\mathbf{\\infty}\\)]{.math .notranslate .nohighlight} {*Initialize each entry to MAX_DOUBLE*}
> :::
>
> ::: line
> **for** [\\(i=1\\)]{.math .notranslate .nohighlight} to [\\(N\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> {Compute short-range forces}
> :::
>
> ::: line
> **for all** particles [\\(j \\in \\mathcal{F}\^S_i\\)]{.math .notranslate .nohighlight} (the short-range family of nodes for particle [\\(i\\)]{.math .notranslate .nohighlight}) **do**
> :::
>
> ::: line
> [\\(r = \\left\\Vert {\\textbf{y}\_j - \\textbf{y}\_i} \\right\\Vert\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> [\\(dr = \\min \\{ 0, r - d \\}\\)]{.math .notranslate .nohighlight} {*Short-range forces are only repulsive, never attractive*}
> :::
>
> ::: line
> [\\(k = \\frac{c_S}{\\delta} V_k dr\\)]{.math .notranslate .nohighlight} {[\\(c_S\\)]{.math .notranslate .nohighlight} *defined in :ref:\`(14) \<pericS\>\`*}
> :::
>
> ::: line
> [\\(\\textbf{f} = \\textbf{f} + k \\frac{\\textbf{y}\_j-\\textbf{y}\_i}{\\left\\Vert {\\textbf{y}\_j-\\textbf{y}\_i} \\right\\Vert}\\)]{.math .notranslate .nohighlight}
> :::
> :::::::::::::::::
>
> ::: line
> **end for**
> :::
> :::::::::::::::::::
>
> ::: line
> **end for**
> :::
>
> ::: line
> **for** [\\(i=1\\)]{.math .notranslate .nohighlight} to [\\(N\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> {Compute bond forces}
> :::
>
> ::: line
> **for all** particles [\\(j\\)]{.math .notranslate .nohighlight} sharing an unbroken bond with particle [\\(i\\)]{.math .notranslate .nohighlight} **do**
> :::
>
> ::: line
> [\\(r = \\left\\Vert {\\textbf{y}\_j - \\textbf{y}\_i} \\right\\Vert\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> [\\(dr = r - \\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> [\\(k = \\frac{c}{\\left\\Vert {\\textbf{x}\_i - \\textbf{x}\_j} \\right\\Vert} \\nu(\\textbf{x}\_i - \\textbf{x}\_j) V_j dr\\)]{.math .notranslate .nohighlight} {[\\(c\\)]{.math .notranslate .nohighlight} *defined in :ref:\`(6) \<peric\>\`*}
> :::
>
> ::: line
> [\\(\\textbf{f} = \\textbf{f} + k \\frac{\\textbf{y}\_j-\\textbf{y}\_i}{\\left\\Vert {\\textbf{y}\_j-\\textbf{y}\_i} \\right\\Vert}\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> **if** [\\((dr / \\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert) \> \\min(s_0(i), s_0(j))\\)]{.math .notranslate .nohighlight} **then**
> :::
>
> ::: line
> Break [\\(i\\)]{.math .notranslate .nohighlight}'s bond with [\\(j\\)]{.math .notranslate .nohighlight} {[\\(j\\)]{.math .notranslate .nohighlight}*'s bond with* [\\(i\\)]{.math .notranslate .nohighlight} *will be broken when this loop iterates on* [\\(j\\)]{.math .notranslate .nohighlight}}
> :::
>
> ::: line
> **end if**
> :::
>
> ::: line
> [\\(\\tilde{s}\_0(i) = \\min (\\tilde{s}\_0(i),s\_{00}-\\alpha(dr / \\left\\Vert {\\textbf{x}\_j - \\textbf{x}\_i} \\right\\Vert))\\)]{.math .notranslate .nohighlight}
> :::
>
> ::: line
> **end for**
> :::
>
> ::: line
> **end for**
> :::
>
> ::: line
> [\\(s_0 = \\tilde{s}\_0\\)]{.math .notranslate .nohighlight} {*Store for use in next timestep*}
> :::
>
> ::: line
> Perform step 3 of [[Algorithm 1]{.std .std-ref}](#algvelverlet){.reference .internal}, updating velocities of all particles
> :::
>
> ::: line
> **end while**
> :::
:::

::: {#id1 .section}
### Damage[](#id1 "Link to this heading"){.headerlink}

The damage associated with every particle (see [[(10)]{.std .std-ref}](#peridamageeq){.reference .internal}) can optionally be computed and output with a LAMMPS data dump. To do this, your input script must contain the command [[compute damage/atom]{.doc}]compute_damage_atom.md){.reference .internal} This enables a LAMMPS per-atom compute to calculate the damage associated with each particle every time a LAMMPS [[data dump]{.doc}]dump.md){.reference .internal} frame is written.
:::

::::: {#visualizing-simulation-results .section}
### Visualizing Simulation Results[](#visualizing-simulation-results "Link to this heading"){.headerlink}

There are multiple ways to visualize the simulation results. Typically, you want to display the particles and color code them by the value computed with the [[compute damage/atom]{.doc}]compute_damage_atom.md){.reference .internal} command.

This can be done, for example, by using the built-in visualizer of the [[dump image or dump movie]{.doc}]dump_image.md){.reference .internal} command to create snapshot images or a movie. Below are example command for using dump image with the [[example listed below]{.std .std-ref}](#periexample){.reference .internal} and a set of images created for steps 300, 600, and 2000 this way.

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    dump            D2 all image 100 dump.peri.*.png c_C1 type box no 0.0 view 30 60 zoom 1.5 up 0 0 -1  ssao yes 4539 0.6
    dump_modify     D2 pad 5 adiam * 0.001 amap 0.0 1.0 ca 0.1 3 min blue 0.5 yellow max red
:::
::::

[![periimage1](_images/dump.peri.300.png){style="width: 32%;"}](_images/dump.peri.300.png){.reference .internal} [![periimage2](_images/dump.peri.600.png){style="width: 32%;"}](_images/dump.peri.600.png){.reference .internal} [![periimage3](_images/dump.peri.2000.png){style="width: 32%;"}](_images/dump.peri.2000.png){.reference .internal}

For interactive visualization, the [Ovito](https://ovito.org){.reference .external} is very convenient to use. Below are steps to create a visualization of the [[same example from below]{.std .std-ref}](#periexample){.reference .internal} now using the generated trajectory in the [`dump.peri`{.docutils .literal .notranslate}]{.pre} file.

- Launch Ovito

- File -\> Load File -\> [`dump.peri`{.docutils .literal .notranslate}]{.pre}

- Select "-\> Particle types" and under "Appearance" set "Display radius:" to 0.0005

- From the "Add modification:" drop down list select "Color coding"

- Under "Color coding" select from the "Color gradient" drop down list "Jet"

- Also under "Color coding" set "Start value:" to 0 and "End value:" to 1

- You can improve the image quality by adding the "Ambient occlusion" modification

<figure id="id3" class="align-center align-default" style="width: 80%">
<img src="_images/ovito-peri-snap.png" alt="_images/ovito-peri-snap.png" />
<figcaption><p><span class="caption-text">Screenshot of visualizing a trajectory with Ovito</span><a href="#id3" class="headerlink" title="Link to this image"></a></p></figcaption>
</figure>
:::::

::: {#pitfalls .section}
### Pitfalls[](#pitfalls "Link to this heading"){.headerlink}

**Parallel Scalability**

LAMMPS operates in parallel in a [[spatial-decomposition mode]{.doc}]Developer_par_part.md){.reference .internal}, where each processor owns a spatial subdomain of the overall simulation domain and communicates with its neighboring processors via distributed-memory message passing (MPI) to acquire ghost atom information to allow forces on the atoms it owns to be computed. LAMMPS also uses Verlet neighbor lists which are recomputed every few timesteps as particles move. On these timesteps, particles also migrate to new processors as needed. LAMMPS decomposes the overall simulation domain so that spatial subdomains of nearly equal volume are assigned to each processor. When each subdomain contains nearly the same number of particles, this results in a reasonable load balance among all processors. As is more typical with some peridynamic simulations, some subdomains may contain many particles while other subdomains contain few particles, resulting in a load imbalance that impacts parallel scalability.

**Setting the "skin" distance**

The [[neighbor]{.doc}]neighbor.md){.reference .internal} command with LAMMPS is used to set the so-called "skin" distance used when building neighbor lists. All atom pairs within a cutoff distance equal to the horizon [\\(\\delta\\)]{.math .notranslate .nohighlight} plus the skin distance are stored in the list. Unexpected crashes in LAMMPS may be due to too small a skin distance. The skin should be set to a value such that [\\(\\delta\\)]{.math .notranslate .nohighlight} plus the skin distance is larger than the maximum possible distance between two bonded particles. For example, if [\\(s\_{00}\\)]{.math .notranslate .nohighlight} is increased, the skin distance may also need to be increased.

**"Lost" particles**

All particles are contained within the "simulation box" of LAMMPS. The boundaries of this box may change with time, or not, depending on how the LAMMPS [[boundary]{.doc}]boundary.md){.reference .internal} command has been set. If a particle drifts outside the simulation box during the course of a simulation, it is called *lost*.

As an option of the [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal} command of LAMMPS, the lost keyword determines whether LAMMPS checks for lost atoms each time it computes thermodynamics and what it does if atoms are lost. If the value is *ignore*, LAMMPS does not check for lost atoms. If the value is *error* or *warn*, LAMMPS checks and either issues an error or warning. The code will exit with an error and continue with a warning. This can be a useful debugging option. The default behavior of LAMMPS is to exit with an error if a particle is lost.

The peridynamic module within LAMMPS does not check for lost atoms. If a particle with unbroken bonds is lost, those bonds are marked as broken by the remaining particles.

**Defining the peridynamic horizon** [\\(\\mathbf{\\delta}\\)]{.math .notranslate .nohighlight}

In the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command, the user must specify the horizon [\\(\\delta\\)]{.math .notranslate .nohighlight}. This argument determines which particles are bonded when the simulation is initialized. It is recommended that [\\(\\delta\\)]{.math .notranslate .nohighlight} be set to a small fraction of a lattice constant larger than desired.

For example, if the lattice constant is 0.0005 and you wish to set the horizon to three times the lattice constant, then set [\\(\\delta\\)]{.math .notranslate .nohighlight} to be 0.0015001, a value slightly larger than three times the lattice constant. This guarantees that particles three lattice constants away from each other are still bonded. If [\\(\\delta\\)]{.math .notranslate .nohighlight} is set to 0.0015, for example, floating point error may result in some pairs of particles three lattice constants apart not being bonded.

**Breaking bonds too early**

For technical reasons, the bonds in the simulation are not created until the end of the first timestep of the simulation. Therefore, one should not attempt to break bonds until at least the second step of the simulation.
:::

::: {#bugs .section}
### Bugs[](#bugs "Link to this heading"){.headerlink}

The user is cautioned that this code is a beta release. If you are confident that you have found a bug in the peridynamic module, please report it in a GitHub Issue \<https://github.com/lammps/lammps/issues\> or send an email to the LAMMPS developers. First, check the [New features and bug fixes](https://www.lammps.org/bug.html){.reference .external} section of the LAMMPS website site to see if the bug has already been reported or fixed. If not, the most useful thing you can do for us is to isolate the problem. Run it on the smallest number of atoms and fewest number of processors and with the simplest input script that reproduces the bug. In your message, describe the problem and any ideas you have as to what is causing it or where in the code the problem might be. We'll request your input script and data files if necessary.
:::

::: {#modifying-and-extending-the-peridynamic-module .section}
### Modifying and Extending the Peridynamic Module[](#modifying-and-extending-the-peridynamic-module "Link to this heading"){.headerlink}

To add new features or peridynamic potentials to the peridynamic module, the user is referred to the [[Modifying & extending LAMMPS]{.doc}]Modify.md){.reference .internal} section. To develop a new bond-based material, start with the *peri/pmb* pair style as a template. To develop a new state-based material, start with the *peri/lps* pair style as a template.
:::
:::::::::::::::::::::::::::

:::::::::::::: {#a-numerical-example .section}
## A Numerical Example[](#a-numerical-example "Link to this heading"){.headerlink}

To introduce the peridynamic implementation within LAMMPS, we replicate a numerical experiment taken from section 6 of [[(Silling 2005)]{.std .std-ref}](#silling2005){.reference .internal}.

:::: {#problem-description-and-setup .section}
### Problem Description and Setup[](#problem-description-and-setup "Link to this heading"){.headerlink}

We consider the impact of a rigid sphere on a homogeneous disk of brittle material. The sphere has diameter [\\(0.01\\)]{.math .notranslate .nohighlight} m and velocity 100 m/s directed normal to the surface of the target. The target material has density [\\(\\rho = 2200\\)]{.math .notranslate .nohighlight} kg/m:math:\^3. A PMB material model is used with [\\(K = 14.9\\)]{.math .notranslate .nohighlight} GPa and critical bond stretch parameters given by [\\(s\_{00} = 0.0005\\)]{.math .notranslate .nohighlight} and [\\(\\alpha = 0.25\\)]{.math .notranslate .nohighlight}. A three-dimensional simple cubic lattice is constructed with lattice constant [\\(0.0005\\)]{.math .notranslate .nohighlight} m and horizon [\\(0.0015\\)]{.math .notranslate .nohighlight} m. (The horizon is three times the lattice constant.) The target is a cylinder of diameter [\\(0.074\\)]{.math .notranslate .nohighlight} m and thickness [\\(0.0025\\)]{.math .notranslate .nohighlight} m, and the associated lattice contains 103,110 particles. Each particle [\\(i\\)]{.math .notranslate .nohighlight} has volume fraction [\\(V_i = 1.25 \\times 10\^{-10} \\textrm{m}\^3\\)]{.math .notranslate .nohighlight}.

The spring constant in the PMB material model is (see [[(6)]{.std .std-ref}](#peric){.reference .internal})

::: {.math .notranslate .nohighlight}
\\\[c = \\frac{18k}{\\pi \\delta\^4} = \\frac{18 (14.9 \\times 10\^9)}{ \\pi (1.5 \\times 10\^{-3})\^4} \\approx 1.6863 \\times 10\^{22}.\\\]
:::

The CFL analysis from [[(Silling2005)]{.std .std-ref}](#silling2005){.reference .internal} shows that a timestep of [\\(1.0 \\times 10\^{-7}\\)]{.math .notranslate .nohighlight} is safe.

We observe here that in IEEE double-precision floating point arithmetic when computing the bond stretch [\\(s(t,\\mathbf{\\eta},\\mathbf{\\xi})\\)]{.math .notranslate .nohighlight} at each iteration where [\\(\\left\\Vert {\\mathbf{\\eta}+\\mathbf{\\xi}} \\right\\Vert\\)]{.math .notranslate .nohighlight} is computed during the iteration and [\\(\\left\\Vert {\\mathbf{\\xi}} \\right\\Vert\\)]{.math .notranslate .nohighlight} was computed and stored for the initial lattice, it may be that [\\(fl(s) = \\varepsilon\\)]{.math .notranslate .nohighlight} with [\\(\\left\| \\varepsilon \\right\| \\leq \\varepsilon\_{machine}\\)]{.math .notranslate .nohighlight} for an unstretched bond. Taking [\\(\\varepsilon = 2.220446049250313 \\times 10\^{-16}\\)]{.math .notranslate .nohighlight}, we see that the value [\\(c s V_i \\approx 4.68 \\times 10\^{-4}\\)]{.math .notranslate .nohighlight}, computed when determining [\\(f\\)]{.math .notranslate .nohighlight}, is perhaps larger than we would like, especially when the true force should be zero. One simple way to avoid this issue is to insert the following instructions in Algorithm [[Algorithm 5]{.std .std-ref}](#algperipmb){.reference .internal} after instruction 21 (and similarly for Algorithm [[Algorithm 2]{.std .std-ref}](#algperilps){.reference .internal}):

> ::::: {}
> ::: line
> **if** [\\(\\left\| dr \\right\| \< \\varepsilon\_{machine}\\)]{.math .notranslate .nohighlight} **then**
> :::
>
> ::: line
> [\\(dr = 0\\)]{.math .notranslate .nohighlight}
> :::
> :::::
>
> ::: line
> **end if**
> :::

Qualitatively, this says that displacements from equilibrium on the order of [\\(10\^{-16}\\)]{.math .notranslate .nohighlight}m are taken to be exactly zero, a seemingly reasonable assumption.
::::

:::: {#the-projectile .section}
### The Projectile[](#the-projectile "Link to this heading"){.headerlink}

The projectile used in the following experiments is not the one used in [[(Silling 2005)]{.std .std-ref}](#silling2005){.reference .internal}. The projectile used here exerts a force

::: {.math .notranslate .nohighlight}
\\\[F(r) = - k_s (r - R)\^2\\\]
:::

on each atom where [\\(k_s\\)]{.math .notranslate .nohighlight} is a specified force constant, [\\(r\\)]{.math .notranslate .nohighlight} is the distance from the atom to the center of the indenter, and [\\(R\\)]{.math .notranslate .nohighlight} is the radius of the projectile. The force is repulsive and [\\(F(r) = 0\\)]{.math .notranslate .nohighlight} for [\\(r \> R\\)]{.math .notranslate .nohighlight}. For our problem, the projectile radius [\\(R = 0.05\\)]{.math .notranslate .nohighlight} m, and we have chosen [\\(k_s = 1.0 \\times 10\^{17}\\)]{.math .notranslate .nohighlight} (compare with [[(6)]{.std .std-ref}](#peric){.reference .internal} above).
::::

:::::::: {#writing-the-lammps-input-file .section}
### Writing the LAMMPS Input File[](#writing-the-lammps-input-file "Link to this heading"){.headerlink}

We discuss the example input script [[listed below]{.std .std-ref}](#periexample){.reference .internal}. In line 2 we specify that SI units are to be used. We specify the dimension (3) and boundary conditions ("shrink-wrapped") for the computational domain in lines 3 and 4. In line 5 we specify that peridynamic particles are to be used for this simulation. In line 7, we set the "skin" distance used in building the LAMMPS neighbor list. In line 8 we set the lattice constant (in meters) and in line 10 we define the spatial region where the target will be placed. In line 12 we specify a rectangular box enclosing the target region that defines the simulation domain. Line 14 fills the target region with atoms. Lines 15 and 17 define the peridynamic material model, and lines 19 and 21 set the particle density and particle volume, respectively. The particle volume should be set to the cube of the lattice constant for a simple cubic lattice. Line 23 sets the initial velocity of all particles to zero. Line 25 instructs LAMMPS to integrate time with velocity-Verlet, and lines 27-30 create the spherical projectile, sending it with a velocity of 100 m/s towards the target. Line 32 declares a compute style for the damage (percentage of broken bonds) associated with each particle. Line 33 sets the timestep, line 34 instructs LAMMPS to provide a screen dump of thermodynamic quantities every 200 timesteps, and line 35 instructs LAMMPS to create a data file ([`dump.peri`{.docutils .literal .notranslate}]{.pre}) with a complete snapshot of the system every 100 timesteps. This file can be used to create still images or movies. Finally, line 36 instructs LAMMPS to run for 2000 timesteps.

:::::: {#id4 .literal-block-wrapper .docutils .container}
[]{#periexample}

::: code-block-caption
[Peridynamics Example LAMMPS Input Script]{.caption-text}[](#id4 "Link to this code"){.headerlink}
:::

:::: {.highlight-LAMMPS .notranslate}
::: highlight
     1# 3D Peridynamic simulation with projectile"
     2units           si
     3dimension       3
     4boundary        s s s
     5atom_style      peri
     6atom_modify     map array
     7neighbor        0.0010 bin
     8lattice         sc 0.0005
     9# Create desired target
    10region          target cylinder y 0.0 0.0 0.037 -0.0025 0.0 units box
    11# Make 1 atom type
    12create_box      1 target
    13# Create the atoms in the simulation region
    14create_atoms    1 region target
    15pair_style      peri/pmb
    16#               <type1> <type2>    <c>    <horizon>  <s00> <alpha>
    17pair_coeff         *       *    1.6863e22 0.0015001 0.0005  0.25
    18# Set mass density
    19set             group all density 2200
    20# volume = lattice constant^3
    21set             group all volume 1.25e-10
    22# Zero out velocities of particles
    23velocity        all set 0.0 0.0 0.0 sum no units box
    24# Use velocity-Verlet time integrator
    25fix             F1 all nve
    26# Construct spherical indenter to shatter target
    27variable        y0 equal 0.00510
    28variable        vy equal -100
    29variable        y equal "v_y0 + step*dt*v_vy"
    30fix             F2 all indent 1e17 sphere 0.0000 v_y 0.0000 0.0050 units box
    31# Compute damage for each particle
    32compute         C1 all damage/atom
    33timestep        1.0e-7
    34thermo          200
    35dump            D1 all custom 100 dump.peri id type x y z c_C1
    36run             2000
:::
::::
::::::

::: {.admonition .note}
Note

To use the LPS model, replace line 15 with [[pair_style peri/lps]{.doc}]pair_peri.md){.reference .internal} and modify line 16 accordingly.
:::
::::::::

::: {#numerical-results-and-discussion .section}
### Numerical Results and Discussion[](#numerical-results-and-discussion "Link to this heading"){.headerlink}

We ran the [[input script from above]{.std .std-ref}](#periexample){.reference .internal}. Images of the disk (projectile not shown) appear in Figure below. The plot of damage on the top monolayer was created by coloring each particle according to its damage.

The symmetry in the computed solution arises because a "perfect" lattice was used, and a because a perfectly spherical projectile impacted the lattice at its geometric center. To break the symmetry in the solution, the nodes in the peridynamic body may be perturbed slightly from the lattice sites. To do this, the lattice of points can be slightly perturbed using the [[displace_atoms]{.doc}]displace_atoms.md){.reference .internal} command.

<figure id="id5" class="align-center align-default" style="width: 80%">
<span id="figperitarget"></span><img src="_images/pdlammps_fig2.png" alt="_images/pdlammps_fig2.png" />
<figcaption><p><span class="caption-text">Target during (a) and after (b,c) impact</span><a href="#id5" class="headerlink" title="Link to this image"></a></p></figcaption>
</figure>

------------------------------------------------------------------------

**(Emmrich)** Emmrich, Weckner, Commun. Math. Sci., 5, 851-864 (2007),

**(Parks)** Parks, Lehoucq, Plimpton, Silling, Comp Phys Comm, 179(11), 777-783 (2008).

**(Silling 2000)** Silling, J Mech Phys Solids, 48, 175-209 (2000).

**(Silling 2005)** Silling Askari, Computer and Structures, 83, 1526-1535 (2005).

**(Silling 2007)** Silling, Epton, Weckner, Xu, Askari, J Elasticity, 88, 151-184 (2007).

**(Seleson 2010)** Seleson, Parks, Int J Mult Comp Eng 9(6), pp. 689-706, 2011.
:::
::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::: {#pair-style-granular-superellipsoid-command .section}
[]{#index-0}

# pair_style granular/superellipsoid command[](#pair-style-granular-superellipsoid-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style granular/superellipsoid cutoff no_bounding_box curvature_gaussian

    Optional settings, see discussion below.
    * cutoff = global cutoff value
    * no_bounding_box = skip oriented bounding box check
    * curvature_gaussian = gaussian curvature coeff approximation for contact patch
:::
::::
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    pair_style granular/superellipsoid
    pair_coeff * * hooke 1000.0 50.0 tangential linear_history 1000.0 1.0 0.5 damping mass_velocity

    pair_style granular/superellipsoid 10.0 curvature_gaussian
    pair_coeff 1 1 hertz 1000.0 50.0 tangential linear_history 500.0 1.0 0.4 damping viscoelastic
    pair_coeff 2 2 hertz 500.0 50.0 tangential linear_history 250.0 1.0 0.1 damping viscoelastic
:::
::::
:::::

:::::::::::::::::::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

::: versionadded
[Added in version 30Mar2026.]{.versionmodified .added}
:::

The *granular/superellipsoid* style calculates granular contact forces between superellipsoidal particles (see [[atom style ellipsoid]{.doc}]atom_style.md){.reference .internal}). Similar to the [[granular pairstyle]{.doc}]pair_granular.md){.reference .internal} which is designed for spherical particles, various normal, damping, and tangential contact models are available (rolling and twisting may be added later). The total computed forces and torques are the sum of various models selected.

All model choices and parameters are entered in the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command, as described below. Coefficient values are not global, but can be set to different values for different combinations of particle types, as determined by the [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} command. If the contact model choice is the same for two particle types, the mixing for the cross-coefficients can be carried out automatically. This is shown in the last example, where model choices are the same for type 1 - type 1 as for type 2 - type2 interactions, but coefficients are different. In this case, the mixed coefficients for type 1 - type 2 interactions can be determined from mixing rules discussed below. For additional flexibility, coefficients as well as model forms can vary between particle types.

------------------------------------------------------------------------

This pair_style allows granular contact between two superellipsoid particles whose surface is implicitly defined as:

::: {.math .notranslate .nohighlight}
\\\[f(\\mathbf{x}) = \\left( \\left\|\\frac{x}{a}\\right\|\^{n_2} + \\left\|\\frac{y}{b}\\right\|\^{n_2} \\right)\^{n_1 / n_2} + \\left\|\\frac{z}{c}\\right\|\^{n_1} - 1 = 0\\\]
:::

for a point [\\(\\mathbf{x} = (x, y, z)\\)]{.math .notranslate .nohighlight} where the coordinates are given in the reference of the principal directions of inertia of the particle. The half-diameters [\\(a\\)]{.math .notranslate .nohighlight}, [\\(b\\)]{.math .notranslate .nohighlight}, and [\\(c\\)]{.math .notranslate .nohighlight} correspond to the *shape* property, and the exponents [\\(n_1\\)]{.math .notranslate .nohighlight} and [\\(n_2\\)]{.math .notranslate .nohighlight} to the *block* property of the ellipsoid atom. See the doc page for the [[set]{.doc}]set.md){.reference .internal} command for more details.

::: {.admonition .note}
Note

The contact solver strictly requires convex particle shapes to ensure a mathematically unique point of deepest penetration. Therefore, the blockiness parameters must be [\\(n_1 \\ge 2.0\\)]{.math .notranslate .nohighlight} and [\\(n_2 \\ge 2.0\\)]{.math .notranslate .nohighlight}. Attempting to simulate concave or "pointy" particles ([\\(n \< 2.0\\)]{.math .notranslate .nohighlight}) will result in an error.
:::

::: {.admonition .note}
Note

For particles with high blockiness exponents ([\\(n \> 4.0\\)]{.math .notranslate .nohighlight}) involved in edge-to-edge or corner-to-corner contacts, the surface normal vector varies rapidly over small distances. The Newton solver may occasionally fail to converge to the strict gradient alignment tolerance (typically [\\(10\^{-10}\\)]{.math .notranslate .nohighlight}). You may see warning messages in the log indicating that the solver returned a sub-optimal solution, but the simulation will proceed using this best-effort contact point.
:::

Contact detection for these aspherical particles uses the so-called "midway" minimization approach from [[(Houlsby)]{.std .std-ref}](#houlsby){.reference .internal}. Considering two particles with shape functions, [\\(F_i\\)]{.math .notranslate .nohighlight} and [\\(F_j\\)]{.math .notranslate .nohighlight}, the contact point [\\(\\mathbf{X}\_0\\)]{.math .notranslate .nohighlight} in the global frame is obtained as:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{X}\_0 = \\underset{\\mathbf{X}}{\\text{argmin}} \\ F_i(\\mathbf{X}) + F_j(\\mathbf{X}) \\text{, subject to } F_i(\\mathbf{X}) = F_j(\\mathbf{X})\\\]
:::

where the shape function is given by [\\(F_i(\\mathbf{X}) = f_i(\\mathbf{R}\_i\^T (\\mathbf{X} - \\mathbf{X}\_i))\\)]{.math .notranslate .nohighlight} and where [\\(\\mathbf{X}\_i\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{R}\_i\\)]{.math .notranslate .nohighlight} are the center of mass and rotation matrix of the particle, respectively. The constrained minimization problem is solved using Lagrange multipliers and Newton's method with a line search as described by [[(Podlozhnyuk)]{.std .std-ref}](#podlozhnyuk){.reference .internal}.

::: {.admonition .note}
Note

The shape function [\\(F\\)]{.math .notranslate .nohighlight} is not a signed distance function and does not have unit gradient [\\(\\\|\\nabla F \\\| \\neq 1\\)]{.math .notranslate .nohighlight} so that the so-called "midway" point is not actually located at an equal distance from the surface of both particles. For contact between non-identical particles, the contact point tends to be closer to the surface of the smaller and blockier particle.
:::

::: {.admonition .note}
Note

This formulation leads to a 4x4 system of non-linear equations. Tikhonov regularization and step clumping is used to ensure robustness of the direct solver and high convergence rate, even for blocky particles with near flat faces.
:::

The particles overlap if both shape functions are negative at the contact point. The contact normal is obtained as: [\\(\\mathbf{n}\_{ij} = \\nabla F_i(\\mathbf{X}\_0) / \\\| \\nabla F_i(\\mathbf{X}\_0)\\\| = - \\nabla F_j(\\mathbf{X}\_0) / \\\| \\nabla F_j(\\mathbf{X}\_0)\\\|\\)]{.math .notranslate .nohighlight} and the overlap [\\(\\delta = \\\|\\mathbf{X}\_j\^{\\mathrm{surf}} - \\mathbf{X}\_i\^{\\mathrm{surf}}\\\|\\)]{.math .notranslate .nohighlight} is computed as the distance between the points on the particles surfaces that are closest to the contact point in the direction of the contact normal: [\\(F_i(\\mathbf{X}\_i\^{\\mathrm{surf}} = \\mathbf{X}\_0 + \\lambda_i \\mathbf{n}\_{ij}) = 0\\)]{.math .notranslate .nohighlight} and [\\(F_j(\\mathbf{X}\_j\^{\\mathrm{surf}} = \\mathbf{X}\_0 + \\lambda_j \\mathbf{n}\_{ij}) = 0\\)]{.math .notranslate .nohighlight}. Newton's method is used to solve this equation for the scalars [\\(\\lambda_i\\)]{.math .notranslate .nohighlight} and [\\(\\lambda_j\\)]{.math .notranslate .nohighlight} and find the surface points [\\(\\mathbf{X}\_i\^{\\mathrm{surf}}\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{X}\_j\^{\\mathrm{surf}}\\)]{.math .notranslate .nohighlight}.

::: {.admonition .note}
Note

A modified representation of the particle surface is defined as [\\(G(\\mathbf{X}) = (F(\\mathbf{X})+1)\^{1/n_1}-1\\)]{.math .notranslate .nohighlight} which is a quasi-radial distance function formulation. This formulation is used to compute the surface points once the "midway" contact point is found. This formulation is also used when the *geometric* keyword is specified in the pair_style command and the following optimization problem is solved instead for the contact point: [\\(\\mathbf{X}\_0 = \\underset{\\mathbf{X}}{\\text{argmin}} \\, \\left( r_i G_i(\\mathbf{X}) + r_j G_j(\\mathbf{X}) \\right) \\text{, subject to } r_i G_i(\\mathbf{X}) = r_j G_j(\\mathbf{X})\\)]{.math .notranslate .nohighlight}, where [\\(r_i\\)]{.math .notranslate .nohighlight} and [\\(r_j\\)]{.math .notranslate .nohighlight} are the average radii of the two particles. The geometric formulation thus yields a better approximation of the contact point for particles with different sizes, and it is slightly more robust for particles with high *block* exponents, albeit more computationally expensive.
:::

A hierarchical approach is used to limit the cost of contact detection. First, intersection of the bounding spheres of the two particles of bounding radii [\\(r_i\\)]{.math .notranslate .nohighlight} and [\\(r_j\\)]{.math .notranslate .nohighlight} is checked. If the distance between the particles center is more than the sum of the radii [\\(\\\|\\mathbf{X}\_j - \\mathbf{X}\_j\\\| \> r_i + r_j\\)]{.math .notranslate .nohighlight}, the particles do not intersect. Then, if the bounding spheres intersect, intersection of the oriented bounding box is checked. This is done following the equations of [[(Eberly)]{.std .std-ref}](#geometrictools){.reference .internal}. This check is always performed, unless the *no_bounding_box* keyword is used. This is advantageous for all particle shapes except for superellipses with aspect ratio close to one and both blockiness indexes close to 2.

::: {.admonition .warning}
Warning

The Newton-Raphson minimization used to find the midway contact point can fail to converge if the initial starting guess is too far from the true physical surface. This typically occurs if a user specifies a manual global *cutoff* that is significantly larger than the particles **and** enables the *no_bounding_box* keyword. Under these conditions, the solver attempts to resolve contacts between widely separated particles, which might cause the math to diverge and instantly crashing the simulation. It is strongly recommended to keep bounding box checks enabled if a large cutoff is specified.
:::

------------------------------------------------------------------------

This section provides an overview of the various normal, tangential, and damping contact models available. For additional context, see the discussion in the [[granular pairstyle]{.doc}]pair_granular.md){.reference .internal} doc page which includes all of these options.

The first required keyword for the *pair_coeff* command is the normal contact model. Currently supported options for normal contact models and their required arguments are:

1.  *hooke* : [\\(k_n\\)]{.math .notranslate .nohighlight}, [\\(\\eta\_{n0}\\)]{.math .notranslate .nohighlight} (or [\\(e\\)]{.math .notranslate .nohighlight})

2.  *hertz* : [\\(k_n\\)]{.math .notranslate .nohighlight}, [\\(\\eta\_{n0}\\)]{.math .notranslate .nohighlight} (or [\\(e\\)]{.math .notranslate .nohighlight})

Here, [\\(k_n\\)]{.math .notranslate .nohighlight} is spring stiffness (with units that depend on model choice, see below); [\\(\\eta\_{n0}\\)]{.math .notranslate .nohighlight} is a damping prefactor (or, in its place a coefficient of restitution [\\(e\\)]{.math .notranslate .nohighlight}, depending on the choice of damping mode, see below).

For the *hooke* model, the normal, elastic component of force acting on particle *i* due to contact with particle *j* is given by:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{F}\_{ne, Hooke} = k_n \\delta\_{ij} \\mathbf{n}\\\]
:::

Where [\\(\\delta\_{ij}\\)]{.math .notranslate .nohighlight} is the particle overlap, (note the i-j ordering so that [\\(\\mathbf{F}\_{ne}\\)]{.math .notranslate .nohighlight} is positive for repulsion), and [\\(\\mathbf{n}\\)]{.math .notranslate .nohighlight} is the contact normal vector at the contact point. Therefore, for *hooke*, the units of the spring constant [\\(k_n\\)]{.math .notranslate .nohighlight} are *force*/*distance*, or equivalently *mass*/*time\^2*.

For the *hertz* model, the normal component of force is given by:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{F}\_{ne, Hertz} = k_n R\_{eff}\^{1/2}\\delta\_{ij}\^{3/2} \\mathbf{n}\\\]
:::

Here, [\\(R\_{eff} = R = \\frac{R_i R_j}{R_i + R_j}\\)]{.math .notranslate .nohighlight} is the effective radius, and [\\(R_i\\)]{.math .notranslate .nohighlight} is the equivalent radius of the i-th particle at the surface contact point with the j-th particle. This radius is either the inverse of the mean curvature coefficient, [\\(R_i = 2 / (\\kappa_1 + \\kappa_2)\\)]{.math .notranslate .nohighlight}, or the gaussian curvature coefficient [\\(R_i = 1 / \\sqrt{\\kappa_1 \\kappa_2}\\)]{.math .notranslate .nohighlight}, where [\\(\\kappa\_{1,2}\\)]{.math .notranslate .nohighlight} are the principal curvatures of the particle surface at the contact point. For *hertz*, the units of the spring constant [\\(k_n\\)]{.math .notranslate .nohighlight} are *force*/*length*\^2, or equivalently *pressure*.

::: {.admonition .note}
Note

To ensure numerical stability and preserve physical realism, the computed contact radius is mathematically capped. For highly blocky particles undergoing flat-on-flat contact, the theoretical curvature approaches zero, which would yield an infinite contact radius and cause a force explosion. To prevent this, the maximum contact radius is capped at the physical bounding radius of the smallest interacting particle. Conversely, for sharp corner contacts where curvature approaches infinity, the calculated radius would drop to zero, eliminating the repulsive force entirely. The contact radius is therefore lower-bounded by a minimum fraction of the physical radius ([\\(10\^{-4} \\min(r_i, r_j)\\)]{.math .notranslate .nohighlight}) to prevent particles from unphysically interpenetrating.
:::

In addition, the normal force is augmented by a damping term of the following general form:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{F}\_{n,damp} = -\\eta_n \\mathbf{v}\_{n,rel}\\\]
:::

Here, [\\(\\mathbf{v}\_{n,rel} = (\\mathbf{v}\_j - \\mathbf{v}\_i) \\cdot \\mathbf{n}\\ \\mathbf{n}\\)]{.math .notranslate .nohighlight} is the component of relative velocity along [\\(\\mathbf{n}\\)]{.math .notranslate .nohighlight}.

The optional *damping* keyword to the *pair_coeff* command followed by a keyword determines the model form of the damping factor [\\(\\eta_n\\)]{.math .notranslate .nohighlight}, and the interpretation of the [\\(\\eta\_{n0}\\)]{.math .notranslate .nohighlight} or [\\(e\\)]{.math .notranslate .nohighlight} coefficients specified as part of the normal contact model settings. The *damping* keyword and corresponding model form selection may be appended anywhere in the *pair coeff* command. Note that the choice of damping model affects both the normal and tangential damping. The options for the damping model currently supported are:

1.  *mass_velocity*

2.  *viscoelastic*

If the *damping* keyword is not specified, the *viscoelastic* model is used by default.

For *damping mass_velocity*, the normal damping is given by:

::: {.math .notranslate .nohighlight}
\\\[\\eta_n = \\eta\_{n0} m\_{eff}\\\]
:::

Here, [\\(\\eta\_{n0}\\)]{.math .notranslate .nohighlight} is the damping coefficient specified for the normal contact model, in units of 1/*time* and [\\(m\_{eff} = m_i m_j/(m_i + m_j)\\)]{.math .notranslate .nohighlight} is the effective mass. Use *damping mass_velocity* to reproduce the damping behavior of *pair gran/hooke/\**.

The *damping viscoelastic* model is based on the viscoelastic treatment of [[(Brilliantov et al)]{.std .std-ref}](#brill1996-2){.reference .internal}, where the normal damping is given by:

::: {.math .notranslate .nohighlight}
\\\[\\eta_n = \\eta\_{n0}\\ a m\_{eff}\\\]
:::

Here, *a* is the contact radius, given by [\\(a =\\sqrt{R\\delta}\\)]{.math .notranslate .nohighlight} for all models. For *damping viscoelastic*, [\\(\\eta\_{n0}\\)]{.math .notranslate .nohighlight} is in units of 1/(*time*\**distance*).

The total normal force is computed as the sum of the elastic and damping components:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{F}\_n = \\mathbf{F}\_{ne} + \\mathbf{F}\_{n,damp}\\\]
:::

------------------------------------------------------------------------

The *pair_coeff* command also requires specification of the tangential contact model. The required keyword *tangential* is expected, followed by the model choice and associated parameters. Currently there is only one supported tangential model with expected parameters as follows:

1.  *linear_history* : [\\(k_t\\)]{.math .notranslate .nohighlight}, [\\(x\_{\\gamma,t}\\)]{.math .notranslate .nohighlight}, [\\(\\mu_s\\)]{.math .notranslate .nohighlight}

Here, [\\(x\_{\\gamma,t}\\)]{.math .notranslate .nohighlight} is a dimensionless multiplier for the normal damping [\\(\\eta_n\\)]{.math .notranslate .nohighlight} that determines the magnitude of the tangential damping, [\\(\\mu_t\\)]{.math .notranslate .nohighlight} is the tangential (or sliding) friction coefficient, and [\\(k_t\\)]{.math .notranslate .nohighlight} is the tangential stiffness coefficient.

The tangential damping force [\\(\\mathbf{F}\_\\mathrm{t,damp}\\)]{.math .notranslate .nohighlight} is given by:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{F}\_\\mathrm{t,damp} = -\\eta_t \\mathbf{v}\_{t,rel}\\\]
:::

The tangential damping prefactor [\\(\\eta_t\\)]{.math .notranslate .nohighlight} is calculated by scaling the normal damping [\\(\\eta_n\\)]{.math .notranslate .nohighlight} (see above):

::: {.math .notranslate .nohighlight}
\\\[\\eta_t = -x\_{\\gamma,t} \\eta_n\\\]
:::

The normal damping prefactor [\\(\\eta_n\\)]{.math .notranslate .nohighlight} is determined by the choice of the *damping* keyword, as discussed above. Thus, the *damping* keyword also affects the tangential damping. The parameter [\\(x\_{\\gamma,t}\\)]{.math .notranslate .nohighlight} is a scaling coefficient. Several works in the literature use [\\(x\_{\\gamma,t} = 1\\)]{.math .notranslate .nohighlight} ([[Marshall]{.std .std-ref}](#marshall2009-2){.reference .internal}, [[Tsuji et al]{.std .std-ref}](#tsuji1992-2){.reference .internal}, [[Silbert et al]{.std .std-ref}](#silbert2001-2){.reference .internal}). The relative tangential velocity at the point of contact is given by [\\(\\mathbf{v}\_{t, rel} = \\mathbf{v}\_{t} - (R_i\\boldsymbol{\\Omega}\_i + R_j\\boldsymbol{\\Omega}\_j) \\times \\mathbf{n}\\)]{.math .notranslate .nohighlight}, where [\\(\\mathbf{v}\_{t} = \\mathbf{v}\_r - \\mathbf{v}\_r\\cdot\\mathbf{n}\\ \\mathbf{n}\\)]{.math .notranslate .nohighlight}, [\\(\\mathbf{v}\_r = \\mathbf{v}\_j - \\mathbf{v}\_i\\)]{.math .notranslate .nohighlight} . The direction of the applied force is [\\(\\mathbf{t} = \\mathbf{v\_{t,rel}}/\\\|\\mathbf{v\_{t,rel}}\\\|\\)]{.math .notranslate .nohighlight} .

The normal force value [\\(F\_{n0}\\)]{.math .notranslate .nohighlight} used to compute the critical force depends on the form of the contact model. It is given by the magnitude of the normal force:

::: {.math .notranslate .nohighlight}
\\\[F\_{n0} = \\\|\\mathbf{F}\_n\\\|\\\]
:::

The remaining tangential options all use accumulated tangential displacement (i.e. contact history). The accumulated tangential displacement is discussed in details below in the context of the *linear_history* option. The same treatment of the accumulated displacement will apply to other (future) options as well.

For *tangential linear_history*, the tangential force is given by:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{F}\_t = -\\min(\\mu_t F\_{n0}, \\\|-k_t\\mathbf{\\xi} + \\mathbf{F}\_\\mathrm{t,damp}\\\|) \\mathbf{t}\\\]
:::

Here, [\\(\\mathbf{\\xi}\\)]{.math .notranslate .nohighlight} is the tangential displacement accumulated during the entire duration of the contact:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{\\xi} = \\int\_{t0}\^t \\mathbf{v}\_{t,rel}(\\tau) \\mathrm{d}\\tau\\\]
:::

This accumulated tangential displacement must be adjusted to account for changes in the frame of reference of the contacting pair of particles during contact. This occurs due to the overall motion of the contacting particles in a rigid-body-like fashion during the duration of the contact. There are two modes of motion that are relevant: the 'tumbling' rotation of the contacting pair, which changes the orientation of the plane in which tangential displacement occurs; and 'spinning' rotation of the contacting pair about the vector connecting their centers of mass ([\\(\\mathbf{n}\\)]{.math .notranslate .nohighlight}). Corrections due to the former mode of motion are made by rotating the accumulated displacement into the plane that is tangential to the contact vector at each step, or equivalently removing any component of the tangential displacement that lies along [\\(\\mathbf{n}\\)]{.math .notranslate .nohighlight}, and rescaling to preserve the magnitude. This follows the discussion in [[Luding]{.std .std-ref}](#luding2008-2){.reference .internal}, see equation 17 and relevant discussion in that work:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{\\xi} = \\left(\\mathbf{\\xi\'} - (\\mathbf{n} \\cdot \\mathbf{\\xi\'})\\mathbf{n}\\right) \\frac{\\\|\\mathbf{\\xi\'}\\\|}{\\\|\\mathbf{\\xi\'} - (\\mathbf{n}\\cdot\\mathbf{\\xi\'})\\mathbf{n}\\\|}\\\]
:::

Here, [\\(\\mathbf{\\xi\'}\\)]{.math .notranslate .nohighlight} is the accumulated displacement prior to the current time step and [\\(\\mathbf{\\xi}\\)]{.math .notranslate .nohighlight} is the corrected displacement. Corrections to the displacement due to the second mode of motion described above (rotations about [\\(\\mathbf{n}\\)]{.math .notranslate .nohighlight}) are not currently implemented, but are expected to be minor for most simulations.

Furthermore, when the tangential force exceeds the critical force, the tangential displacement is re-scaled to match the value for the critical force (see [[Luding]{.std .std-ref}](#luding2008-2){.reference .internal}, equation 20 and related discussion):

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{\\xi} = -\\frac{1}{k_t}\\left(\\mu_t F\_{n0}\\mathbf{t} - \\mathbf{F}\_{t,damp}\\right)\\\]
:::

The tangential force is added to the total normal force (elastic plus damping) to produce the total force on the particle.

Unlike perfect spheres, the surface normal at the contact point of a superellipsoid does not generally pass through the particle's center of mass. Therefore, both the normal and tangential forces act at the contact point to induce a torque on each particle.

Using the exact contact point [\\(\\mathbf{X}\_0\\)]{.math .notranslate .nohighlight} determined by the geometric solver, the branch vectors from the particle centers of mass to the contact point are defined as [\\(\\mathbf{r}\_{ci} = \\mathbf{X}\_0 - \\mathbf{x}\_i\\)]{.math .notranslate .nohighlight} and [\\(\\mathbf{r}\_{cj} = \\mathbf{X}\_0 - \\mathbf{x}\_j\\)]{.math .notranslate .nohighlight}. The resulting torques are calculated as:

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{\\tau}\_i = \\mathbf{r}\_{ci} \\times \\mathbf{F}\_{tot}\\\]
:::

::: {.math .notranslate .nohighlight}
\\\[\\mathbf{\\tau}\_j = -\\mathbf{r}\_{cj} \\times \\mathbf{F}\_{tot}\\\]
:::

------------------------------------------------------------------------

If two particles are moving away from each other while in contact, there is a possibility that the particles could experience an effective attractive force due to damping. If the optional *limit_damping* keyword is used, this option will zero out the normal component of the force if there is an effective attractive force.

------------------------------------------------------------------------

LAMMPS automatically sets pairwise cutoff values for *pair_style granular/superellipsoid* based on particle radii. In the vast majority of situations, this is adequate. However, a cutoff value can optionally be appended to the *pair_style granular/superellipsoid* command to specify a global cutoff (i.e. a cutoff for all atom types). This option may be useful in some rare cases where the automatic cutoff determination is not sufficient.
::::::::::::::::::::::::::::

------------------------------------------------------------------------

::: {#mixing-shift-table-tail-correction-restart-rrespa-info .section}
## Mixing, shift, table, tail correction, restart, rRESPA info[](#mixing-shift-table-tail-correction-restart-rrespa-info "Link to this heading"){.headerlink}

The [[pair_modify]{.doc}]pair_modify.md){.reference .internal} mix, shift, table, and tail options are not relevant for granular pair styles.

Mixing of coefficients is carried out using geometric averaging for most quantities, e.g. if friction coefficient for type 1-type 1 interactions is set to [\\(\\mu_1\\)]{.math .notranslate .nohighlight}, and friction coefficient for type 2-type 2 interactions is set to [\\(\\mu_2\\)]{.math .notranslate .nohighlight}, the friction coefficient for type1-type2 interactions is computed as [\\(\\sqrt{\\mu_1\\mu_2}\\)]{.math .notranslate .nohighlight} (unless explicitly specified to a different value by a *pair_coeff 1 2 ...* command).

This pair style writes its information to [[binary restart files]{.doc}]restart.md){.reference .internal}, so a pair_style command does not need to be specified in an input script that reads a restart file.

This pair style can only be used via the *pair* keyword of the [[run_style respa]{.doc}]run_style.md){.reference .internal} command. It does not support the *inner*, *middle*, *outer* keywords.

The [`single()`{.docutils .literal .notranslate}]{.pre} function of these pair styles returns 0.0 for the energy of a pairwise interaction, since energy is not conserved in these dissipative potentials. It also returns only the normal component of the pairwise interaction force.
:::

------------------------------------------------------------------------

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

The *atom_style* must be set to *ellipsoid superellipsoid* to enable superellipsoid particles' shape parameters (3 lengths and two blockiness parameters), see [[atom_style]{.doc}]atom_style.md){.reference .internal} for more details.

This pair style require Newton's third law be set to *off* for pair interactions.

There are currently no versions of *fix wall/gran* or *fix wall/gran/region* that are compatible with superellipsoid particles.

This pair style is part of the ASPHERE package. It is only enabled if LAMMPS was built with that package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} page for more info.

This pair style requires that atoms store per-particle bounding radius, shapes, blockiness, inertia, torque, and angular momentum (omega) as defined by the [[atom_style ellipsoid superellipsoid]{.doc}]atom_style.md){.reference .internal}.

This pair style requires you to use the [[comm_modify vel yes]{.doc}]comm_modify.md){.reference .internal} command so that velocities are stored by ghost atoms.

This pair style will not restart exactly when using the [[read_restart]{.doc}]read_restart.md){.reference .internal} command, though it should provide statistically similar results. This is because the forces it computes depend on atom velocities and the atom velocities have been propagated half a timestep between the force computation and when the restart is written, due to using Velocity Verlet time integration. See the [[read_restart]{.doc}]read_restart.md){.reference .internal} command for more details.

Accumulated values for individual contacts are saved to restart files but are not saved to data files. Therefore, forces may differ significantly when a system is reloaded using the [[read_data]{.doc}]read_data.md){.reference .internal} command.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[pair_coeff]{.doc}]pair_coeff.md){.reference .internal} [[pair granular]{.doc}]pair_granular.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

For the *pair_coeff* settings: *damping viscoelastic*
:::

::: {#references .section}
## References[](#references "Link to this heading"){.headerlink}

**(Brilliantov et al, 1996)** Brilliantov, N. V., Spahn, F., Hertzsch, J. M., & Poschel, T. (1996). Model for collisions in granular gases. Physical review E, 53(5), 5382.

**(Tsuji et al, 1992)** Tsuji, Y., Tanaka, T., & Ishida, T. (1992). Lagrangian numerical simulation of plug flow of cohesionless particles in a horizontal pipe. Powder technology, 71(3), 239-250.

**(Luding, 2008)** Luding, S. (2008). Cohesive, frictional powders: contact models for tension. Granular matter, 10(4), 235.

**(Marshall, 2009)** Marshall, J. S. (2009). Discrete-element modeling of particulate aerosol flows. Journal of Computational Physics, 228(5), 1541-1561.

**(Silbert, 2001)** Silbert, L. E., Ertas, D., Grest, G. S., Halsey, T. C., Levine, D., & Plimpton, S. J. (2001). Granular flow down an inclined plane: Bagnold scaling and rheology. Physical Review E, 64(5), 051302.

**(Thornton, 1991)** Thornton, C. (1991). Interparticle sliding in the presence of adhesion. J. Phys. D: Appl. Phys. 24 1942

**(Thornton et al, 2013)** Thornton, C., Cummins, S. J., & Cleary, P. W. (2013). An investigation of the comparative behavior of alternative contact force models during inelastic collisions. Powder Technology, 233, 30-46.

**(Otis R. Walton)** Walton, O.R., Personal Communication

**(Podlozhnyuk)** Podlozhnyuk, Pirker, Kloss, Comp. Part. Mech., 4:101-118 (2017).

**(Houlsby)** Houlsby, Computers and Geotechnics, 36, 953-959 (2009).

**(Eberly)** Eberly, Geometric Tools: Dynamic Collision Detection Using Oriented Bounding Boxes (2008).
:::
::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::

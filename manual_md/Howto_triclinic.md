::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::::::::::::: {#triclinic-non-orthogonal-simulation-boxes .section}
# [10.2.3. ]{.section-number}Triclinic (non-orthogonal) simulation boxes[](#triclinic-non-orthogonal-simulation-boxes "Link to this heading"){.headerlink}

By default, LAMMPS uses an orthogonal simulation box to encompass the particles. The orthogonal box has its "origin" at (xlo,ylo,zlo) and extends to (xhi,yhi,zhi). Conceptually it is defined by 3 edge vectors starting from the origin given by **A** = (xhi-xlo,0,0); **B** = (0,yhi-ylo,0); **C** = (0,0,zhi-zlo). The [[boundary]{.doc}]boundary.md){.reference .internal} command sets the boundary conditions for the 6 faces of the box (periodic, non-periodic, etc). The 6 parameters (xlo,xhi,ylo,yhi,zlo,zhi) are defined at the time the simulation box is created by one of these commands:

- [[create_box]{.doc}]create_box.md){.reference .internal}

- [[read_data]{.doc}]read_data.md){.reference .internal}

- [[read_restart]{.doc}]read_restart.md){.reference .internal}

- [[read_dump]{.doc}]read_dump.md){.reference .internal}

Internally, LAMMPS defines box size parameters lx,ly,lz where lx = xhi-xlo, and similarly in the y and z dimensions. The 6 parameters, as well as lx,ly,lz, can be output via the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command. See the [[Howto 2d]{.doc}]Howto_2d.md){.reference .internal} doc page for info on how zlo and zhi are defined for 2d simulations.

------------------------------------------------------------------------

:::: {#triclinic-simulation-boxes .section}
## Triclinic simulation boxes[](#triclinic-simulation-boxes "Link to this heading"){.headerlink}

LAMMPS also allows simulations to be performed using triclinic (non-orthogonal) simulation boxes shaped as a 3d parallelepiped with triclinic symmetry. For 2d simulations a triclinic simulation box is effectively a parallelogram; see the [[Howto 2d]{.doc}]Howto_2d.md){.reference .internal} doc page for details.

One use of triclinic simulation boxes is to model solid-state crystals with triclinic symmetry. The [[lattice]{.doc}]lattice.md){.reference .internal} command can be used with non-orthogonal basis vectors to define a lattice that will tile a triclinic simulation box via the [[create_atoms]{.doc}]create_atoms.md){.reference .internal} command.

A second use is to run Parrinello-Rahman dynamics via the [[fix npt]{.doc}]fix_nh.md){.reference .internal} command, which will adjust the xy, xz, yz tilt factors to compensate for off-diagonal components of the pressure tensor. The analog for an [[energy minimization]{.doc}]minimize.md){.reference .internal} is the [[fix box/relax]{.doc}]fix_box_relax.md){.reference .internal} command.

A third use is to shear a bulk solid to study the response of the material. The [[fix deform]{.doc}]fix_deform.md){.reference .internal} command can be used for this purpose. It allows dynamic control of the xy, xz, yz tilt factors as a simulation runs. This is discussed in the [[Howto NEMD]{.doc}]Howto_nemd.md){.reference .internal} doc page on non-equilibrium MD (NEMD) simulations.

Conceptually, a triclinic parallelepiped is defined with an "origin" at (xlo,ylo,zhi) and 3 edge vectors **A** = (ax,ay,az), **B** = (bx,by,bz), **C** = (cx,cy,cz) which can be arbitrary vectors, so long as they are non-zero, distinct, and not co-planar. In addition, they must define a right-handed system, such that (**A** cross **B**) points in the direction of **C**. Note that a left-handed system can be converted to a right-handed system by simply swapping the order of any pair of the **A**, **B**, **C** vectors.

The 4 commands listed above for defining orthogonal simulation boxes have triclinic options which allow for specification of the origin and edge vectors **A**, **B**, **C**. For each command, this can be done in one of two ways, for what LAMMPS calls a *general* triclinic box or a *restricted* triclinic box.

A *general* triclinic box is specified by an origin (xlo, ylo, zlo) and arbitrary edge vectors **A** = (ax,ay,az), **B** = (bx,by,bz), and **C** = (cx,cy,cz). So there are 12 parameters in total.

A *restricted* triclinic box also has an origin (xlo,ylo,zlo), but its edge vectors are of the following restricted form: **A** = (xhi-xlo,0,0), **B** = (xy,yhi-ylo,0), **C** = (xz,yz,zhi-zlo). So there are 9 parameters in total. Note that the restricted form requires **A** to be along the x-axis, **B** to be in the xy plane with a y-component in the +y direction, and **C** to have its z-component in the +z direction. Note that a restricted triclinic box is *right-handed* by construction since (**A** cross **B**) points in the direction of **C**.

The *xy,xz,yz* values can be zero or positive or negative. They are called "tilt factors" because they are the amount of displacement applied to edges of faces of an orthogonal box to change it into a restricted triclinic parallelepiped.

::: {.admonition .note}
Note

Any right-handed general triclinic box (i.e. solid-state crystal basis vectors) can be rotated in 3d around its origin in order to conform to the LAMMPS definition of a restricted triclinic box. See the discussion in the next sub-section about general triclinic simulation boxes in LAMMPS.
:::

Note that the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} command has keywords for outputting the various parameters that define the size and shape of orthogonal, restricted triclinic, and general triclinic simulation boxes.

For orthogonal boxes there are 6 thermo keywords (xlo,ylo,zlo) and (xhi,yhi,zhi).

For restricted triclinic boxes there are 9 thermo keywords for (xlo,ylo,zlo), (xhi,yhi,zhi), and the (xy,xz,yz) tilt factors.

For general triclinic boxes there are 12 thermo keywords for (xlo,ylo,zhi) and the components of the **A**, **B**, **C** edge vectors, namely (avecx,avecy,avecz), (bvecx,bvecy,bvecz), and (cvecx,cvecy,cvecz),

The remainder of this doc page explains (a) how LAMMPS operates with general triclinic simulation boxes, (b) mathematical transformations between general and restricted triclinic boxes which may be useful when creating LAMMPS inputs or interpreting outputs for triclinic simulations, and (c) how LAMMPS uses tilt factors for restricted triclinic simulation boxes.
::::

------------------------------------------------------------------------

::: {#general-triclinic-simulation-boxes-in-lammps .section}
## General triclinic simulation boxes in LAMMPS[](#general-triclinic-simulation-boxes-in-lammps "Link to this heading"){.headerlink}

LAMMPS allows specification of general triclinic simulation boxes with their atoms as a convenience for users who may be converting data from solid-state crystallographic representations or from DFT codes for input to LAMMPS. Likewise it allows output of dump files, data files, and thermodynamic data (e.g. pressure tensor) in a general triclinic format.

However internally, LAMMPS only uses restricted triclinic simulation boxes. This is for parallel efficiency and to formulate partitioning of the simulation box across processors, neighbor list building, and inter-processor communication of per-atom data with methods similar to those used for orthogonal boxes.

This means 4 things which are important to understand:

- Input of a general triclinic system is immediately converted to a restricted triclinic system.

- If output of per-atom data for a general triclinic system is requested (e.g. for atom coordinates in a dump file), conversion from a restricted to general triclinic system is done at the time of output.

- The conversion of the simulation box and per-atom data from general triclinic to restricted triclinic (and vice versa) is a 3d rotation operation around an origin, which is the lower left corner of the simulation box. This means an input data file for a general triclinic system should specify all per-atom quantities consistent with the general triclinic box and its orientation relative to the standard x,y,z coordinate axes. For example, atom coordinates should be inside the general triclinic simulation box defined by the edge vectors **A**, **B**, **C** and its origin. Likewise per-atom velocities should be in directions consistent with the general triclinic box orientation. E.g. a velocity vector which will be in the +x direction once LAMMPS converts from a general to restricted triclinic box, should be specified in the data file in the direction of the **A** edge vector. See the [[read_data]{.doc}]read_data.md){.reference .internal} doc page for info on all the per-atom vector quantities to which this rule applies when a data file for a general triclinic box is input.

- If commands such as [[write_data]{.doc}]write_data.md){.reference .internal} or [[dump custom]{.doc}]dump.md){.reference .internal} are used to output general triclinic information, it is effectively the inverse of the operation described in the preceding bullet.

- Other LAMMPS commands such as [[region]{.doc}]region.md){.reference .internal} or [[velocity]{.doc}]velocity.md){.reference .internal} or [[set]{.doc}]set.md){.reference .internal}, operate on a restricted triclinic system even if a general triclinic system was defined initially.

This is the list of commands which have general triclinic options:

- [[create_box]{.doc}]create_box.md){.reference .internal} - define a general triclinic box

- [[create_atoms]{.doc}]create_atoms.md){.reference .internal} - add atoms to a general triclinic box

- [[lattice]{.doc}]lattice.md){.reference .internal} - define a custom lattice consistent with the **A**, **B**, **C** edge vectors of a general triclinic box

- [[read_data]{.doc}]read_data.md){.reference .internal} - read a data file for a general triclinic system

- [[write_data]{.doc}]write_data.md){.reference .internal} - write a data file for a general triclinic system

- [[dump atom, dump custom]{.doc}]dump.md){.reference .internal} - output dump snapshots in general triclinic format

- [[dump_modify triclinic/general]{.doc}]dump_modify.md){.reference .internal} - select general triclinic format for dump output

- [[thermo_style]{.doc}]thermo_style.md){.reference .internal} - output the pressure tensor in general triclinic format

- [[thermo_modify triclinic/general]{.doc}]thermo_modify.md){.reference .internal} - select general triclinic format for thermo output

- [[read_restart]{.doc}]read_restart.md){.reference .internal} - read a restart file for a general triclinic system

- [[write_restart]{.doc}]read_restart.md){.reference .internal} - write a restart file for a general triclinic system
:::

------------------------------------------------------------------------

::::: {#transformation-from-general-to-restricted-triclinic-boxes .section}
## Transformation from general to restricted triclinic boxes[](#transformation-from-general-to-restricted-triclinic-boxes "Link to this heading"){.headerlink}

Let **A**,**B**,**C** be the right-handed edge vectors of a general triclinic simulation box. The equivalent LAMMPS **a**,**b**,**c** for a restricted triclinic box are a 3d rotation of **A**, **B**, and **C** and can be computed as follows:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\begin{pmatrix} \\mathbf{a} & \\mathbf{b} & \\mathbf{c} \\end{pmatrix} = & \\begin{pmatrix} a_x & b_x & c_x \\\\ 0 & b_y & c_y \\\\ 0 & 0 & c_z \\\\ \\end{pmatrix} \\\\ a_x = & A \\\\ b_x = & \\mathbf{B} \\cdot \\mathbf{\\hat{A}} \\quad = \\quad B \\cos{\\gamma} \\\\ b_y = & \|\\mathbf{\\hat{A}} \\times \\mathbf{B}\| \\quad = \\quad B \\sin{\\gamma} \\quad = \\quad \\sqrt{B\^2 - {b_x}\^2} \\\\ c_x = & \\mathbf{C} \\cdot \\mathbf{\\hat{A}} \\quad = \\quad C \\cos{\\beta} \\\\ c_y = & \\mathbf{C} \\cdot \\widehat{(\\mathbf{A} \\times \\mathbf{B})} \\times \\mathbf{\\hat{A}} \\quad = \\quad \\frac{\\mathbf{B} \\cdot \\mathbf{C} - b_x c_x}{b_y} \\\\ c_z = & \|\\mathbf{C} \\cdot \\widehat{(\\mathbf{A} \\times \\mathbf{B})}\|\\quad = \\quad \\sqrt{C\^2 - {c_x}\^2 - {c_y}\^2}\\end{split}\\\]
:::

where A = \| **A** \| indicates the scalar length of **A**. The hat symbol (\^) indicates the corresponding unit vector. [\\(\\beta\\)]{.math .notranslate .nohighlight} and [\\(\\gamma\\)]{.math .notranslate .nohighlight} are angles between the **A**, **B**, **C** vectors as described below.

For consistency, the same rotation applied to the triclinic box edge vectors can also be applied to atom positions, velocities, and other vector quantities. This can be conveniently achieved by first converting to fractional coordinates in the general triclinic coordinates and then converting to coordinates in the restricted triclinic basis. The transformation is given by the following equation:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathbf{x} = & \\begin{pmatrix} \\mathbf{a} & \\mathbf{b} & \\mathbf{c} \\end{pmatrix} \\cdot \\frac{1}{V} \\begin{pmatrix} \\mathbf{B \\times C} \\\\ \\mathbf{C \\times A} \\\\ \\mathbf{A \\times B} \\end{pmatrix} \\cdot \\mathbf{X}\\end{split}\\\]
:::

where *V* is the volume of the box (same in either basis), **X** is the fractional vector in the general triclinic basis and **x** is the resulting vector in the restricted triclinic basis.
:::::

------------------------------------------------------------------------

::::: {#crystallographic-general-triclinic-representation-of-a-simulation-box .section}
## Crystallographic general triclinic representation of a simulation box[](#crystallographic-general-triclinic-representation-of-a-simulation-box "Link to this heading"){.headerlink}

General triclinic crystal structures are often defined using three lattice constants *a*, *b*, and *c*, and three angles [\\(\\alpha\\)]{.math .notranslate .nohighlight}, [\\(\\beta\\)]{.math .notranslate .nohighlight}, and [\\(\\gamma\\)]{.math .notranslate .nohighlight}. Note that in this nomenclature, the a, b, and c lattice constants are the scalar lengths of the edge vectors **a**, **b**, and **c** defined above. The relationship between these 6 quantities (a, b, c, [\\(\\alpha\\)]{.math .notranslate .nohighlight}, [\\(\\beta\\)]{.math .notranslate .nohighlight}, [\\(\\gamma\\)]{.math .notranslate .nohighlight}) and the LAMMPS restricted triclinic box sizes (lx,ly,lz) = (xhi-xlo,yhi-ylo,zhi-zlo) and tilt factors (xy,xz,yz) is as follows:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}a = & \\mathrm{lx} \\\\ b\^2 = & \\mathrm{ly}\^2 + \\mathrm{xy}\^2 \\\\ c\^2 = & \\mathrm{lz}\^2 + \\mathrm{xz}\^2 + \\mathrm{yz}\^2 \\\\ \\cos{\\alpha} = & \\frac{\\mathrm{xy}\*\\mathrm{xz} + \\mathrm{ly}\*\\mathrm{yz}}{b\*c} \\\\ \\cos{\\beta} = & \\frac{\\mathrm{xz}}{c} \\\\ \\cos{\\gamma} = & \\frac{\\mathrm{xy}}{b} \\\\\\end{split}\\\]
:::

The inverse relationship can be written as follows:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}\\mathrm{lx} = & a \\\\ \\mathrm{xy} = & b \\cos{\\gamma} \\\\ \\mathrm{xz} = & c \\cos{\\beta}\\\\ \\mathrm{ly}\^2 = & b\^2 - \\mathrm{xy}\^2 \\\\ \\mathrm{yz} = & \\frac{b\*c \\cos{\\alpha} - \\mathrm{xy}\*\\mathrm{xz}}{\\mathrm{ly}} \\\\ \\mathrm{lz}\^2 = & c\^2 - \\mathrm{xz}\^2 - \\mathrm{yz}\^2 \\\\\\end{split}\\\]
:::

The values of *a*, *b*, *c*, [\\(\\alpha\\)]{.math .notranslate .nohighlight} , [\\(\\beta\\)]{.math .notranslate .nohighlight}, and [\\(\\gamma\\)]{.math .notranslate .nohighlight} can be printed out or accessed by computes using the [[thermo_style custom]{.doc}]thermo_style.md){.reference .internal} keywords *cella*, *cellb*, *cellc*, *cellalpha*, *cellbeta*, *cellgamma*, respectively.
:::::

------------------------------------------------------------------------

::::::: {#output-of-restricted-and-general-triclinic-boxes-in-a-dump-file .section}
## Output of restricted and general triclinic boxes in a dump file[](#output-of-restricted-and-general-triclinic-boxes-in-a-dump-file "Link to this heading"){.headerlink}

As discussed on the [[dump]{.doc}]dump.md){.reference .internal} command doc page, when the BOX BOUNDS for a snapshot is written to a dump file for a restricted triclinic box, an orthogonal bounding box which encloses the triclinic simulation box is output, along with the 3 tilt factors (xy, xz, yz) of the restricted triclinic box, formatted as follows:

:::: {.highlight-none .notranslate}
::: highlight
    ITEM: BOX BOUNDS xy xz yz
    xlo_bound xhi_bound xy
    ylo_bound yhi_bound xz
    zlo_bound zhi_bound yz
:::
::::

This bounding box is convenient for many visualization programs and is calculated from the 9 restricted triclinic box parameters (xlo,xhi,ylo,yhi,zlo,zhi,xy,xz,yz) as follows:

:::: {.highlight-none .notranslate}
::: highlight
    xlo_bound = xlo + MIN(0.0,xy,xz,xy+xz)
    xhi_bound = xhi + MAX(0.0,xy,xz,xy+xz)
    ylo_bound = ylo + MIN(0.0,yz)
    yhi_bound = yhi + MAX(0.0,yz)
    zlo_bound = zlo
    zhi_bound = zhi
:::
::::

These formulas can be inverted if you need to convert the bounding box back into the restricted triclinic box parameters, e.g. xlo = xlo_bound - MIN(0.0,xy,xz,xy+xz).
:::::::

------------------------------------------------------------------------

:::: {#periodicity-and-tilt-factors-for-triclinic-simulation-boxes .section}
## Periodicity and tilt factors for triclinic simulation boxes[](#periodicity-and-tilt-factors-for-triclinic-simulation-boxes "Link to this heading"){.headerlink}

There is no requirement that a triclinic box be periodic in any dimension, though it typically should be in y or z if you wish to enforce a shift in coordinates due to periodic boundary conditions across the y or z boundaries. See the doc page for the [[boundary]{.doc}]boundary.md){.reference .internal} command for an explanation of shifted coordinates for restricted triclinic boxes which are periodic.

Some commands that work with triclinic boxes, e.g. the [[fix deform]{.doc}]fix_deform.md){.reference .internal} and [[fix npt]{.doc}]fix_nh.md){.reference .internal} commands, require periodicity or non-shrink-wrap boundary conditions in specific dimensions. See the command doc pages for details.

A restricted triclinic box can be defined with all 3 tilt factors = 0.0, so that it is initially orthogonal. This is necessary if the box will become non-orthogonal, e.g. due to use of the [[fix npt]{.doc}]fix_nh.md){.reference .internal} or [[fix deform]{.doc}]fix_deform.md){.reference .internal} commands. Alternatively, you can use the [[change_box]{.doc}]change_box.md){.reference .internal} command to convert a simulation box from orthogonal to restricted triclinic and vice versa.

::: {.admonition .note}
Note

Highly tilted restricted triclinic simulation boxes can be computationally inefficient. This is due to the large volume of communication needed to acquire ghost atoms around a processor's irregular-shaped subdomain. For extreme values of tilt, LAMMPS may also lose atoms and generate an error.
:::

LAMMPS will issue a warning if you define a restricted triclinic box with a tilt factor which skews the box more than half the distance of the parallel box length, which is the first dimension in the tilt factor (e.g. x for xz).

For example, if xlo = 2 and xhi = 12, then the x box length is 10 and the xy tilt factor should be between -5 and 5 to avoid the warning. Similarly, both xz and yz should be between -(xhi-xlo)/2 and +(yhi-ylo)/2. Note that these are not limitations, since if the maximum tilt factor is 5 (as in this example), then simulations boxes and atom configurations with tilt = ..., -15, -5, 5, 15, 25, ... are all geometrically equivalent.

If the box tilt exceeds this limit during a dynamics run (e.g. due to the [[fix deform]{.doc}]fix_deform.md){.reference .internal} command), then by default the box is "flipped" to an equivalent shape with a tilt factor within the warning bounds, and the run continues. See the [[fix deform]{.doc}]fix_deform.md){.reference .internal} page for further details. Box flips that would normally occur using the [[fix deform]{.doc}]fix_deform.md){.reference .internal} or [[fix npt]{.doc}]fix_nh.md){.reference .internal} commands can be suppressed using the *flip no* option with either of the commands.

One exception to box flipping is if the first dimension in the tilt factor (e.g. x for xy) is non-periodic. In that case, the limits on the tilt factor are not enforced, since flipping the box in that dimension would not change the atom positions due to non-periodicity. In this mode, if the system tilts to large angles, the simulation will simply become inefficient, due to the highly skewed simulation box.
::::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::

:::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::: {#fix-neb-command .section}
[]{#index-0}

# fix neb command[](#fix-neb-command "Link to this heading"){.headerlink}

::::: {#syntax .section}
## Syntax[](#syntax "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix ID group-ID neb Kspring keyword value
:::
::::

- ID, group-ID are documented in [[fix]{.doc}]fix.md){.reference .internal} command

- neb = style name of this fix command

- Kspring = spring constant for parallel nudging force (force/distance units or force units, see parallel keyword)

- zero or more keyword/value pairs may be appended

- keyword = *parallel* or *perp* or *end*

``` literal-block
parallel value = neigh or ideal or equal
  neigh = parallel nudging force based on distance to neighbor replicas (Kspring = force/distance units)
  ideal = parallel nudging force based on interpolated ideal position (Kspring = force units)
  equal = parallel nudging force based on interpolated ideal position before climbing, then interpolated ideal energy whilst climbing (Kspring = force units)
perp value = Kspring2
  Kspring2 = spring constant for perpendicular nudging force (force/distance units)
end values = estyle Kspring3
  estyle = first or last or last/efirst or last/efirst/middle
    first = apply force to first replica
    last = apply force to last replica
    last/efirst = apply force to last replica and set its target energy to that of first replica
    last/efirst/middle = same as last/efirst plus prevent middle replicas having lower energy than first replica
  Kspring3 = spring constant for target energy term (1/distance units)
```
:::::

::::: {#examples .section}
## Examples[](#examples "Link to this heading"){.headerlink}

:::: {.highlight-LAMMPS .notranslate}
::: highlight
    fix 1 active neb 10.0
    fix 2 all neb 1.0 perp 1.0 end last
    fix 2 all neb 1.0 perp 1.0 end first 1.0 end last 1.0
    fix 1 all neb 1.0 parallel ideal end last/efirst 1
:::
::::
:::::

::::::::::: {#description .section}
## Description[](#description "Link to this heading"){.headerlink}

Add nudging forces to atoms in the group for a multi-replica simulation run via the [[neb]{.doc}]neb.md){.reference .internal} command to perform a nudged elastic band (NEB) calculation for finding the transition state. Hi-level explanations of NEB are given with the [[neb]{.doc}]neb.md){.reference .internal} command and on the [[Howto replica]{.doc}]Howto_replica.md){.reference .internal} doc page. The fix neb command must be used with the "neb" command and defines how inter-replica nudging forces are computed. A NEB calculation is divided in two stages. In the first stage n replicas are relaxed toward a MEP until convergence. In the second stage, the climbing image scheme (see [[(Henkelman2)]{.std .std-ref}](#henkelman2){.reference .internal}) is enabled, so that the replica having the highest energy relaxes toward the saddle point (i.e. the point of highest energy along the MEP), and a second relaxation is performed.

A key purpose of the nudging forces is to keep the replicas equally spaced. During the NEB calculation, the [\\(3N\\)]{.math .notranslate .nohighlight}-length vector of interatomic force [\\(F_i = -\\nabla V\\)]{.math .notranslate .nohighlight} for each replica *i* is altered. For all intermediate replicas (i.e. for [\\(1 \< i \< N\\)]{.math .notranslate .nohighlight}, except the climbing replica) the force vector becomes:

::: {.math .notranslate .nohighlight}
\\\[F_i = -\\nabla V + (\\nabla V \\cdot T\') T\' + F\_\\parallel + F\_\\perp\\\]
:::

T' is the unit "tangent" vector for replica *i* and is a function of [\\(R_i, R\_{i-1}, R\_{i+1}\\)]{.math .notranslate .nohighlight}, and the potential energy of the 3 replicas; it points roughly in the direction of [\\(R\_{i+i} - R\_{i-1}\\)]{.math .notranslate .nohighlight}; see the [[(Henkelman1)]{.std .std-ref}](#henkelman1){.reference .internal} paper for details. [\\(R_i\\)]{.math .notranslate .nohighlight} are the atomic coordinates of replica *i*; [\\(R\_{i-1}\\)]{.math .notranslate .nohighlight} and [\\(R\_{i+1}\\)]{.math .notranslate .nohighlight} are the coordinates of its neighbor replicas. The term [\\(\\nabla V \\cdot T\'\\)]{.math .notranslate .nohighlight} is used to remove the component of the gradient parallel to the path which would tend to distribute the replica unevenly along the path. [\\(F\_\\parallel\\)]{.math .notranslate .nohighlight} is an artificial nudging force which is applied only in the tangent direction and which maintains the equal spacing between replicas (see below for more information). [\\(F\_\\perp\\)]{.math .notranslate .nohighlight} is an optional artificial spring which is applied in a direction perpendicular to the tangent direction and which prevent the paths from forming acute kinks (see below for more information).

In the second stage of the NEB calculation, the interatomic force [\\(F_i\\)]{.math .notranslate .nohighlight} for the climbing replica (the replica of highest energy after the first stage) is changed to:

::: {.math .notranslate .nohighlight}
\\\[F_i = -\\nabla V + 2 (\\nabla V \\cdot T\') T\' + F\_\\perp\\\]
:::

and the relaxation procedure is continued to a new converged MEP.

------------------------------------------------------------------------

The keyword *parallel* specifies how the parallel nudging force is computed. With a value of *neigh*, the parallel nudging force is computed as in [[(Henkelman1)]{.std .std-ref}](#henkelman1){.reference .internal} by connecting each intermediate replica with the previous and the next image:

::: {.math .notranslate .nohighlight}
\\\[F\_\\parallel = Kspring \\cdot \\left(\\left\|R\_{i+1} - R_i\\right\| - \\left\|R_i - R\_{i-1}\\right\|\\right)\\\]
:::

Note that in this case the specified *Kspring* is in force/distance units.

With a value of *ideal*, the spring force is computed as suggested in [[(WeinanE)]{.std .std-ref}](#weinane){.reference .internal}

::: {.math .notranslate .nohighlight}
\\\[F\_\\parallel = -Kspring \\cdot (RD - RD\_{ideal}) / (2 \\cdot meanDist)\\\]
:::

where *RD* is the "reaction coordinate" see [[neb]{.doc}]neb.md){.reference .internal} section, and [\\(RD\_{ideal}\\)]{.math .notranslate .nohighlight} is the ideal *RD* for which all the images are equally spaced. I.e. [\\(RD\_{ideal} = (i-1) \\cdot meanDist\\)]{.math .notranslate .nohighlight} when the climbing replica is off, where *i* is the replica number). The *meanDist* is the average distance between replicas. Note that in this case the specified *Kspring* is in force units. When the climbing replica is on, [\\(RD\_{ideal}\\)]{.math .notranslate .nohighlight} and [\\(meanDist\\)]{.math .notranslate .nohighlight} are calculated separately each side of the climbing image. Note that the *ideal* form of nudging can often be more effective at keeping the replicas equally spaced before climbing, then equally spaced either side of the climbing image whilst climbing.

With a value of *equal* the spring force is computed as for *ideal* when the climbing replica is off, promoting equidistance. When the climbing replica is on, the spring force is computed to promote equidistant absolute differences in energy, rather than distance, each side of the climbing image:

::: {.math .notranslate .nohighlight}
\\\[F\_\\parallel = -Kspring \\cdot (ED - ED\_{ideal}) / (2 \\cdot meanEDist)\\\]
:::

where *ED* is the cumulative sum of absolute energy differences:

::: {.math .notranslate .nohighlight}
\\\[ED = \\sum\_{i\<N} \\left\|E(R\_{i+1}) - E(R_i)\\right\|,\\\]
:::

*meanEdist* is the average absolute energy difference between replicas up to the climbing image or from the climbing image to the final image, for images before or after the climbing image respectively. [\\(ED\_{ideal}\\)]{.math .notranslate .nohighlight} is the corresponding cumulative sum of average absolute energy differences in each case, in close analogy to *ideal*. This form of nudging is to aid schemes which integrate forces along, or near to, NEB pathways such as [[fix_pafi]{.doc}]fix_pafi.md){.reference .internal}.

------------------------------------------------------------------------

The keyword *perp* specifies if and how a perpendicular nudging force is computed. It adds a spring force perpendicular to the path in order to prevent the path from becoming too strongly kinked. It can significantly improve the convergence of the NEB calculation when the resolution is poor. I.e. when few replicas are used; see [[(Maras)]{.std .std-ref}](#maras1){.reference .internal} for details.

The perpendicular spring force is given by

::: {.math .notranslate .nohighlight}
\\\[F\_\\perp = K\_{spring2} \\cdot F(R\_{i-1},R_i,R\_{i+1}) (R\_{i+1} + R\_{i-1} - 2 R_i)\\\]
:::

where *Kspring2* is the specified value. [\\(F(R\_{i-1}, R_i, R\_{i+1})\\)]{.math .notranslate .nohighlight} is a smooth scalar function of the angle [\\(R\_{i-1} R_i R\_{i+1}\\)]{.math .notranslate .nohighlight}. It is equal to 0.0 when the path is straight and is equal to 1 when the angle [\\(R\_{i-1} R_i R\_{i+1}\\)]{.math .notranslate .nohighlight} is acute. [\\(F(R\_{i-1}, R_i, R\_{i+1})\\)]{.math .notranslate .nohighlight} is defined in [[(Jonsson)]{.std .std-ref}](#jonsson){.reference .internal}.

If *Kspring2* is set to 0.0 (the default) then no perpendicular spring force is added.

------------------------------------------------------------------------

By default, no additional forces act on the first and last replicas during the NEB relaxation, so these replicas simply relax toward their respective local minima. By using the keyword *end*, additional forces can be applied to the first and/or last replicas, to enable them to relax toward a MEP while constraining their energy E to the target energy ETarget.

If [\\(E\_{Target} \> E\\)]{.math .notranslate .nohighlight}, the interatomic force [\\(F_i\\)]{.math .notranslate .nohighlight} for the specified replica becomes:

::: {.math .notranslate .nohighlight}
\\\[\\begin{split}F_i & = -\\nabla V + (\\nabla V \\cdot T\' + (E - E\_{Target}) \\cdot K\_{spring3}) T\', \\qquad \\textrm{when} \\quad \\nabla V \\cdot T\' \< 0 \\\\ F_i & = -\\nabla V + (\\nabla V \\cdot T\' + (E\_{Target} - E) \\cdot K\_{spring3}) T\', \\qquad \\textrm{when} \\quad \\nabla V \\cdot T\' \> 0\\end{split}\\\]
:::

The "spring" constant on the difference in energies is the specified *Kspring3* value.

When *estyle* is specified as *first*, the force is applied to the first replica. When *estyle* is specified as *last*, the force is applied to the last replica. Note that the *end* keyword can be used twice to add forces to both the first and last replicas.

For both these *estyle* settings, the target energy *ETarget* is set to the initial energy of the replica (at the start of the NEB calculation).

If the *estyle* is specified as *last/efirst* or *last/efirst/middle*, force is applied to the last replica, but the target energy *ETarget* is continuously set to the energy of the first replica, as it evolves during the NEB relaxation.

The difference between these two *estyle* options is as follows. When *estyle* is specified as *last/efirst*, no change is made to the inter-replica force applied to the intermediate replicas (neither first or last). If the initial path is too far from the MEP, an intermediate replica may relax "faster" and reach a lower energy than the last replica. In this case the intermediate replica will be relaxing toward its own local minima. This behavior can be prevented by specifying *estyle* as *last/efirst/middle* which will alter the inter-replica force applied to intermediate replicas by removing the contribution of the gradient to the inter-replica force. This will only be done if a particular intermediate replica has a lower energy than the first replica. This should effectively prevent the intermediate replicas from over-relaxing.

After converging a NEB calculation using an *estyle* of *last/efirst/middle*, you should check that all intermediate replicas have a larger energy than the first replica. If this is not the case, the path is probably not a MEP.

Finally, note that the last replica may never reach the target energy if it is stuck in a local minima which has a larger energy than the target energy.
:::::::::::

::: {#restart-fix-modify-output-run-start-stop-minimize-info .section}
## Restart, fix_modify, output, run start/stop, minimize info[](#restart-fix-modify-output-run-start-stop-minimize-info "Link to this heading"){.headerlink}

No information about this fix is written to [[binary restart files]{.doc}]restart.md){.reference .internal}. None of the [[fix_modify]{.doc}]fix_modify.md){.reference .internal} options are relevant to this fix. No global or per-atom quantities are stored by this fix for access by various [[output commands]{.doc}]Howto_output.md){.reference .internal}. No parameter of this fix can be used with the *start/stop* keywords of the [[run]{.doc}]run.md){.reference .internal} command.

The forces due to this fix are imposed during an energy minimization, as invoked by the [[minimize]{.doc}]minimize.md){.reference .internal} command via the [[neb]{.doc}]neb.md){.reference .internal} command.
:::

::: {#restrictions .section}
## Restrictions[](#restrictions "Link to this heading"){.headerlink}

This command can only be used if LAMMPS was built with the REPLICA package. See the [[Build package]{.doc}]Build_package.md){.reference .internal} doc page for more info.
:::

::: {#related-commands .section}
## Related commands[](#related-commands "Link to this heading"){.headerlink}

[[neb]{.doc}]neb.md){.reference .internal}
:::

::: {#default .section}
## Default[](#default "Link to this heading"){.headerlink}

The option defaults are parallel = neigh, perp = 0.0, ends is not specified (no inter-replica force on the end replicas).

------------------------------------------------------------------------

**(Henkelman1)** Henkelman and Jonsson, J Chem Phys, 113, 9978-9985 (2000).

**(Henkelman2)** Henkelman, Uberuaga, Jonsson, J Chem Phys, 113, 9901-9904 (2000).

**(WeinanE)** E, Ren, Vanden-Eijnden, Phys Rev B, 66, 052301 (2002).

**(Jonsson)** Jonsson, Mills and Jacobsen, in Classical and Quantum Dynamics in Condensed Phase Simulations, edited by Berne, Ciccotti, and Coker World Scientific, Singapore, 1998, p 385.

**(Maras)** Maras, Trushin, Stukowski, Ala-Nissila, Jonsson, Comp Phys Comm, 205, 13-21 (2016).
:::
::::::::::::::::::::::
:::::::::::::::::::::::
::::::::::::::::::::::::

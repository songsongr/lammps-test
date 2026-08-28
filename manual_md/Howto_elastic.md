:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#calculate-elastic-constants .section}
# [10.3.5. ]{.section-number}Calculate elastic constants[](#calculate-elastic-constants "Link to this heading"){.headerlink}

Elastic constants characterize the stiffness of a material. The formal definition is provided by the linear relation that holds between the stress and strain tensors in the limit of infinitesimal deformation. In tensor notation, this is expressed as

::: {.math .notranslate .nohighlight}
\\\[s\_{ij} = C\_{ijkl} e\_{kl}\\\]
:::

where the repeated indices imply summation. [\\(s\_{ij}\\)]{.math .notranslate .nohighlight} are the elements of the symmetric stress tensor. [\\(e\_{kl}\\)]{.math .notranslate .nohighlight} are the elements of the symmetric strain tensor. [\\(C\_{ijkl}\\)]{.math .notranslate .nohighlight} are the elements of the fourth rank tensor of elastic constants. In three dimensions, this tensor has [\\(3\^4=81\\)]{.math .notranslate .nohighlight} elements. Using Voigt notation, the tensor can be written as a 6x6 matrix, where [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} is now the derivative of [\\(s_i\\)]{.math .notranslate .nohighlight} w.r.t. [\\(e_j\\)]{.math .notranslate .nohighlight}. Because [\\(s_i\\)]{.math .notranslate .nohighlight} is itself a derivative w.r.t. [\\(e_i\\)]{.math .notranslate .nohighlight}, it follows that [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} is also symmetric, with at most [\\(\\frac{7 \\times 6}{2}\\)]{.math .notranslate .nohighlight} = 21 distinct elements.

At zero temperature, it is easy to estimate these derivatives by deforming the simulation box in one of the six directions using the [[change_box]{.doc}]change_box.md){.reference .internal} command and measuring the change in the stress tensor. A general-purpose script that does this is given in the [`examples/ELASTIC`{.docutils .literal .notranslate}]{.pre} directory described on the [[Examples]{.doc}]Examples.md){.reference .internal} doc page.

Calculating elastic constants at finite temperature is more challenging, because it is necessary to run a simulation that performs time averages of differential properties. There are at least 3 ways to do this in LAMMPS. The most reliable way to do this is by exploiting the relationship between elastic constants, stress fluctuations, and the Born matrix, the second derivatives of energy w.r.t. strain [[(Ray)]{.std .std-ref}](#ray){.reference .internal}. The Born matrix calculation has been enabled by the [[compute born/matrix]{.doc}]compute_born_matrix.md){.reference .internal} command, which works for any bonded or non-bonded potential in LAMMPS. The most expensive part of the calculation is the sampling of the stress fluctuations. Several examples of this method are provided in the [`examples/ELASTIC_T/BORN_MATRIX`{.docutils .literal .notranslate}]{.pre} directory described on the [[Examples]{.doc}]Examples.md){.reference .internal} doc page.

A second way is to measure the change in average stress tensor in an NVT simulations when the cell volume undergoes a finite deformation. In order to balance the systematic and statistical errors in this method, the magnitude of the deformation must be chosen judiciously, and care must be taken to fully equilibrate the deformed cell before sampling the stress tensor. An example of this method is provided in the [`examples/ELASTIC_T/DEFORMATION`{.docutils .literal .notranslate}]{.pre} directory described on the [[Examples]{.doc}]Examples.md){.reference .internal} doc page.

Another approach is to sample the triclinic cell fluctuations that occur in an NPT simulation. This method can also be slow to converge and requires careful post-processing [[(Shinoda)]{.std .std-ref}](#shinoda1){.reference .internal}. We do not provide an example of this method.

A nice review of the advantages and disadvantages of all of these methods is provided in the paper by Clavier et al. [[(Clavier)]{.std .std-ref}](#clavier){.reference .internal}.

------------------------------------------------------------------------

**(Ray)** J. R. Ray and A. Rahman, J Chem Phys, 80, 4423 (1984).

**(Shinoda)** Shinoda, Shiga, and Mikami, Phys Rev B, 69, 134103 (2004).

**(Clavier)** G. Clavier, N. Desbiens, E. Bourasseau, V. Lachet, N. Brusselle-Dupend and B. Rousseau, Mol Sim, 43, 1413 (2017).
::::
:::::
::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::: {#removed-commands-and-packages .section}
# [6.15. ]{.section-number}Removed commands and packages[](#removed-commands-and-packages "Link to this heading"){.headerlink}

- [amber2lmp tools](#amber2lmp-tools){#id1 .reference .internal}

- [ATC, AWPMD, and POEMS packages](#atc-awpmd-and-poems-packages){#id2 .reference .internal}

- [Neighbor style and comm mode multi/old](#neighbor-style-and-comm-mode-multi-old){#id3 .reference .internal}

- [LAMMPS-GUI source code](#lammps-gui-source-code){#id4 .reference .internal}

- [GJF formulation in fix langevin](#gjf-formulation-in-fix-langevin){#id5 .reference .internal}

- [LAMMPS shell](#lammps-shell){#id6 .reference .internal}

- [i-PI tool](#i-pi-tool){#id7 .reference .internal}

- [USER-REAXC package](#user-reaxc-package){#id8 .reference .internal}

- [MPIIO package](#mpiio-package){#id9 .reference .internal}

- [MSCG package](#mscg-package){#id10 .reference .internal}

- [LATTE package](#latte-package){#id11 .reference .internal}

- [Minimize style fire/old](#minimize-style-fire-old){#id12 .reference .internal}

- [Pair style mesont/tpm, compute style mesont, atom style mesont](#pair-style-mesont-tpm-compute-style-mesont-atom-style-mesont){#id13 .reference .internal}

- [Box command](#box-command){#id14 .reference .internal}

- [Reset_ids, reset_atom_ids, reset_mol_ids commands](#reset-ids-reset-atom-ids-reset-mol-ids-commands){#id15 .reference .internal}

- [MESSAGE package](#message-package){#id16 .reference .internal}

- [REAX package](#reax-package){#id17 .reference .internal}

- [MEAM package](#meam-package){#id18 .reference .internal}

- [USER-CUDA package](#user-cuda-package){#id19 .reference .internal}

- [Compute atom/molecule](#compute-atom-molecule){#id20 .reference .internal}

- [Fix ave/spatial and fix ave/spatial/sphere](#fix-ave-spatial-and-fix-ave-spatial-sphere){#id21 .reference .internal}

- [restart2data tool](#restart2data-tool){#id22 .reference .internal}

------------------------------------------------------------------------

This page lists LAMMPS commands and packages that have been removed from the distribution and provides suggestions for alternatives or replacements. LAMMPS has special dummy styles implemented, that will stop LAMMPS and print a suitable error message in most cases, when a style/command is used that has been removed or will replace the command with the direct alternative (if available) and print a warning.

:::: {#amber2lmp-tools .section}
## [[6.15.1. ]{.section-number}amber2lmp tools](#id1){.toc-backref role="doc-backlink"}[](#amber2lmp-tools "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 11Feb2026.]{.versionmodified .deprecated}
:::

The tools in the [`tools/amber2lmp`{.docutils .literal .notranslate}]{.pre} folder have been removed because they were unmaintained for a long time and required Python 2 which has been obsolete for a long time. Instead the external [AMBER2LAMMPS tool](https://github.com/askforarun/AMBER2LAMMPS){.reference .external} can be used for the same purpose. There is an Howto_amber2lammps included in this manual.
::::

::::: {#atc-awpmd-and-poems-packages .section}
## [[6.15.2. ]{.section-number}ATC, AWPMD, and POEMS packages](#id2){.toc-backref role="doc-backlink"}[](#atc-awpmd-and-poems-packages "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 10Sep2025.]{.versionmodified .deprecated}
:::

The ATC, AWPMD, and POEMS packages are removed because they were unmaintained for a long time and their legacy C++ programming style started to create problems with modern C++ compilers. LAMMPS version 22 July 2025 is the last version that contains them. You have to download and compile this version, if you want to use any of these packages.

::: {.toctree-wrapper .compound}
:::
:::::

:::: {#neighbor-style-and-comm-mode-multi-old .section}
## [[6.15.3. ]{.section-number}Neighbor style and comm mode multi/old](#id3){.toc-backref role="doc-backlink"}[](#neighbor-style-and-comm-mode-multi-old "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 10Sep2025.]{.versionmodified .deprecated}
:::

The original implementation of neighbor style multi and comm mode multi, most recently available under "multi/old" has been removed. The new implementation should be used instead.
::::

:::: {#lammps-gui-source-code .section}
## [[6.15.4. ]{.section-number}LAMMPS-GUI source code](#id4){.toc-backref role="doc-backlink"}[](#lammps-gui-source-code "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 10Sep2025.]{.versionmodified .deprecated}
:::

The LAMMPS-GUI sources used to be included in LAMMPS but they are now hosted in their own git repository at [https://github.com/akohlmey/lammps-gui/](https://github.com/akohlmey/lammps-gui/){.reference .external} and the corresponding online documentation is at [https://lammps-gui.lammps.org/](https://lammps-gui.lammps.org/){.reference .external}
::::

:::: {#gjf-formulation-in-fix-langevin .section}
## [[6.15.5. ]{.section-number}GJF formulation in fix langevin](#id5){.toc-backref role="doc-backlink"}[](#gjf-formulation-in-fix-langevin "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 22Jul2025.]{.versionmodified .deprecated}
:::

The *gjf* keyword in fix langevin has been removed. The GJF functionality has been moved to its own fix style [[fix gjf]{.doc}]fix_gjf.md){.reference .internal}.
::::

:::: {#lammps-shell .section}
## [[6.15.6. ]{.section-number}LAMMPS shell](#id6){.toc-backref role="doc-backlink"}[](#lammps-shell "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 29Aug2024.]{.versionmodified .deprecated}
:::

The LAMMPS shell has been removed from the LAMMPS distribution. Users are encouraged to use the [[LAMMPS-GUI]{.std .std-ref}]Tools.md#lammps-gui){.reference .internal} tool instead.
::::

:::: {#i-pi-tool .section}
## [[6.15.7. ]{.section-number}i-PI tool](#id7){.toc-backref role="doc-backlink"}[](#i-pi-tool "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 27Jun2024.]{.versionmodified .deprecated}
:::

The i-PI tool has been removed from the LAMMPS distribution. Instead, instructions to install i-PI from PyPI via pip are provided.
::::

:::: {#user-reaxc-package .section}
## [[6.15.8. ]{.section-number}USER-REAXC package](#id8){.toc-backref role="doc-backlink"}[](#user-reaxc-package "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 7Feb2024.]{.versionmodified .deprecated}
:::

The USER-REAXC package has been renamed to [[REAXFF]{.std .std-ref}]Packages_details.md#pkg-reaxff){.reference .internal}. In the process also the pair style and related fixes were renamed to use the "reaxff" string instead of "reax/c". For a while LAMMPS was maintaining backward compatibility by providing aliases for the styles. These have been removed, so using "reaxff" is now *required*.
::::

:::: {#mpiio-package .section}
## [[6.15.9. ]{.section-number}MPIIO package](#id9){.toc-backref role="doc-backlink"}[](#mpiio-package "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 21Nov2023.]{.versionmodified .deprecated}
:::

The MPIIO package has been removed from LAMMPS since it was unmaintained for many years and thus not updated to incorporate required changes that had been applied to the corresponding non-MPIIO commands. As a consequence the MPIIO commands had become unreliable and sometimes crashing LAMMPS or corrupting data. Similar functionality is available through the [[ADIOS package]{.std .std-ref}]Packages_details.md#pkg-adios){.reference .internal} and the [[NETCDF package]{.std .std-ref}]Packages_details.md#pkg-netcdf){.reference .internal}. Also, the [[dump_modify nfile or dump_modify fileper]{.doc}]dump_modify.md){.reference .internal} keywords may be used for an efficient way of writing out dump files when running on large numbers of processors. Similarly, the "nfile" and "fileper" keywords exist for restarts: see [[restart]{.doc}]restart.md){.reference .internal}, [[read_restart]{.doc}]read_restart.md){.reference .internal}, [[write_restart]{.doc}]write_restart.md){.reference .internal}.
::::

:::: {#mscg-package .section}
## [[6.15.10. ]{.section-number}MSCG package](#id10){.toc-backref role="doc-backlink"}[](#mscg-package "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 21Nov2023.]{.versionmodified .deprecated}
:::

The MSCG package has been removed from LAMMPS since it was unmaintained for many years and instead superseded by the [OpenMSCG software](https://software.rcc.uchicago.edu/mscg/){.reference .external} of the Voth group at the University of Chicago, which can be used independent from LAMMPS.
::::

:::: {#latte-package .section}
## [[6.15.11. ]{.section-number}LATTE package](#id11){.toc-backref role="doc-backlink"}[](#latte-package "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 15Jun2023.]{.versionmodified .deprecated}
:::

The LATTE package with the fix latte command was removed from LAMMPS. This functionality has been superseded by [[fix mdi/qm]{.doc}]fix_mdi_qm.md){.reference .internal} and [[fix mdi/qmmm]{.doc}]fix_mdi_qmmm.md){.reference .internal} from the [[MDI package]{.std .std-ref}]Packages_details.md#pkg-mdi){.reference .internal}. These fixes are compatible with several quantum software packages, including LATTE. See the [`examples/QUANTUM`{.docutils .literal .notranslate}]{.pre} dir and the [[MDI coupling HOWTO]{.doc}]Howto_mdi.md){.reference .internal} page. MDI supports running LAMMPS with LATTE as a plugin library (similar to the way fix latte worked), as well as on a different set of MPI processors.
::::

:::: {#minimize-style-fire-old .section}
## [[6.15.12. ]{.section-number}Minimize style fire/old](#id12){.toc-backref role="doc-backlink"}[](#minimize-style-fire-old "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 8Feb2023.]{.versionmodified .deprecated}
:::

Minimize style *fire/old* has been removed. Its functionality can be reproduced with style *fire* with specific options. Please see the [[min_modify command]{.doc}]min_modify.md){.reference .internal} documentation for details.
::::

:::: {#pair-style-mesont-tpm-compute-style-mesont-atom-style-mesont .section}
## [[6.15.13. ]{.section-number}Pair style mesont/tpm, compute style mesont, atom style mesont](#id13){.toc-backref role="doc-backlink"}[](#pair-style-mesont-tpm-compute-style-mesont-atom-style-mesont "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 8Feb2023.]{.versionmodified .deprecated}
:::

Pair style *mesont/tpm*, compute style *mesont*, and atom style *mesont* have been removed from the [[MESONT package]{.std .std-ref}]Packages_details.md#pkg-mesont){.reference .internal}. The same functionality is available through [[pair style mesocnt]{.doc}]pair_mesocnt.md){.reference .internal}, [[bond style mesocnt]{.doc}]bond_mesocnt.md){.reference .internal} and [[angle style mesocnt]{.doc}]angle_mesocnt.md){.reference .internal}.
::::

:::: {#box-command .section}
## [[6.15.14. ]{.section-number}Box command](#id14){.toc-backref role="doc-backlink"}[](#box-command "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 22Dec2022.]{.versionmodified .deprecated}
:::

The *box* command has been removed and the LAMMPS code changed so it won't be needed. If present, LAMMPS will ignore the command and print a warning.
::::

:::: {#reset-ids-reset-atom-ids-reset-mol-ids-commands .section}
## [[6.15.15. ]{.section-number}Reset_ids, reset_atom_ids, reset_mol_ids commands](#id15){.toc-backref role="doc-backlink"}[](#reset-ids-reset-atom-ids-reset-mol-ids-commands "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 22Dec2022.]{.versionmodified .deprecated}
:::

The *reset_ids*, *reset_atom_ids*, and *reset_mol_ids* commands have been folded into the [[reset_atoms]{.doc}]reset_atoms.md){.reference .internal} command. If present, LAMMPS will replace the commands accordingly and print a warning.
::::

:::: {#message-package .section}
## [[6.15.16. ]{.section-number}MESSAGE package](#id16){.toc-backref role="doc-backlink"}[](#message-package "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 4May2022.]{.versionmodified .deprecated}
:::

The MESSAGE package has been removed since it was superseded by the [[MDI package]{.std .std-ref}]Packages_details.md#pkg-mdi){.reference .internal}. MDI implements the same functionality and in a more general way with direct support for more applications.
::::

:::: {#reax-package .section}
## [[6.15.17. ]{.section-number}REAX package](#id17){.toc-backref role="doc-backlink"}[](#reax-package "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 4Jan2019.]{.versionmodified .deprecated}
:::

The REAX package has been removed since it was superseded by the [[REAXFF package]{.std .std-ref}]Packages_details.md#pkg-reaxff){.reference .internal}. The REAXFF package has been tested to yield equivalent results to the REAX package, offers better performance, supports OpenMP multi-threading via OPENMP, and GPU and threading parallelization through KOKKOS. The new pair styles are not syntax compatible with the removed reax pair style, so input files will have to be adapted. The REAXFF package was originally called USER-REAXC.
::::

:::: {#meam-package .section}
## [[6.15.18. ]{.section-number}MEAM package](#id18){.toc-backref role="doc-backlink"}[](#meam-package "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 4Jan2019.]{.versionmodified .deprecated}
:::

The MEAM package in Fortran has been replaced by a C++ implementation. The code in the [[MEAM package]{.std .std-ref}]Packages_details.md#pkg-meam){.reference .internal} is a translation of the Fortran code of MEAM into C++, which removes several restrictions (e.g. there can be multiple instances in hybrid pair styles) and allows for some optimizations leading to better performance. The pair style [[meam]{.doc}]pair_meam.md){.reference .internal} has the exact same syntax. For a transition period the C++ version of MEAM was called USER-MEAMC so it could coexist with the Fortran version.
::::

:::: {#user-cuda-package .section}
## [[6.15.19. ]{.section-number}USER-CUDA package](#id19){.toc-backref role="doc-backlink"}[](#user-cuda-package "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 31May2016.]{.versionmodified .deprecated}
:::

The USER-CUDA package had been removed, since it had been unmaintained for a long time and had known bugs and problems. Significant parts of the design were transferred to the [[KOKKOS package]{.std .std-ref}]Packages_details.md#pkg-kokkos){.reference .internal}, which has similar performance characteristics on NVIDIA GPUs. Both, the KOKKOS and the [[GPU package]{.std .std-ref}]Packages_details.md#pkg-gpu){.reference .internal} are maintained and allow running LAMMPS with GPU acceleration.
::::

:::: {#compute-atom-molecule .section}
## [[6.15.20. ]{.section-number}Compute atom/molecule](#id20){.toc-backref role="doc-backlink"}[](#compute-atom-molecule "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 11: ]{.versionmodified .deprecated}Dec2015
:::

The atom/molecule command has been removed from LAMMPS since it was superseded by the more general and extensible "chunk infrastructure". Here the system is partitioned in one of many possible ways - including using molecule IDs - through the [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command and then summing is done using [[compute reduce/chunk]{.doc}]compute_reduce_chunk.md){.reference .internal} Please refer to the [[chunk HOWTO]{.doc}]Howto_chunk.md){.reference .internal} section for an overview.
::::

:::: {#fix-ave-spatial-and-fix-ave-spatial-sphere .section}
## [[6.15.21. ]{.section-number}Fix ave/spatial and fix ave/spatial/sphere](#id21){.toc-backref role="doc-backlink"}[](#fix-ave-spatial-and-fix-ave-spatial-sphere "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 11Dec2015.]{.versionmodified .deprecated}
:::

The fixes ave/spatial and ave/spatial/sphere have been removed from LAMMPS since they were superseded by the more general and extensible "chunk infrastructure". Here the system is partitioned in one of many possible ways through the [[compute chunk/atom]{.doc}]compute_chunk_atom.md){.reference .internal} command and then averaging is done using [[fix ave/chunk]{.doc}]fix_ave_chunk.md){.reference .internal}. Please refer to the [[chunk HOWTO]{.doc}]Howto_chunk.md){.reference .internal} section for an overview.
::::

:::: {#restart2data-tool .section}
## [[6.15.22. ]{.section-number}restart2data tool](#id22){.toc-backref role="doc-backlink"}[](#restart2data-tool "Link to this heading"){.headerlink}

::: deprecated
[Deprecated since version 23Nov2013.]{.versionmodified .deprecated}
:::

The functionality of the restart2data tool has been folded into the LAMMPS executable directly instead of having a separate tool. A combination of the commands [[read_restart]{.doc}]read_restart.md){.reference .internal} and [[write_data]{.doc}]write_data.md){.reference .internal} can be used to the same effect. For added convenience this conversion can also be triggered by [[command-line flags]{.doc}]Run_options.md){.reference .internal}
::::
::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::

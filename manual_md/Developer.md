:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#information-for-developers .section}
# [4. ]{.section-number}Information for Developers[](#information-for-developers "Link to this heading"){.headerlink}

This section describes the internal structure and basic algorithms of the LAMMPS code. This is a work in progress and additional information will be added incrementally depending on availability of time and requests from the LAMMPS user community.

A discussion of software engineering methods applied to LAMMPS over time and a general outline of the design and maintenance approach by the LAMMPS developers can be found in the paper LAMMPS: A Case Study For Applying Modern Software Engineering to an Established Research Software Package, \<https://doi.org/10.5281/zenodo.17117558\> in USRSE'25 conference proceedings.

::: {.toctree-wrapper .compound}
- [4.1. Source files]Developer_org.md){.reference .internal}
- [4.2. Class topology]Developer_org.md#class-topology){.reference .internal}
- [4.3. Code design]Developer_code_design.md){.reference .internal}
- [4.4. Parallel algorithms]Developer_parallel.md){.reference .internal}
- [4.5. Accessing per-atom data]Developer_atom.md){.reference .internal}
- [4.6. Communication patterns]Developer_comm_ops.md){.reference .internal}
- [4.7. How a timestep works]Developer_flow.md){.reference .internal}
- [4.8. Writing new styles]Developer_write.md){.reference .internal}
- [4.9. Notes for developers and code maintainers]Developer_notes.md){.reference .internal}
- [4.10. Notes for updating code written for older LAMMPS versions]Developer_updating.md){.reference .internal}
- [4.11. Writing plugins]Developer_plugins.md){.reference .internal}
- [4.12. Adding tests for unit testing]Developer_unittest.md){.reference .internal}
- [4.13. C++ base classes]Classes.md){.reference .internal}
- [4.14. Platform abstraction functions]Developer_platform.md){.reference .internal}
- [4.15. Utility functions]Developer_utils.md){.reference .internal}
- [4.16. Special Math functions]Developer_utils.md#special-math-functions){.reference .internal}
- [4.17. Tokenizer classes]Developer_utils.md#tokenizer-classes){.reference .internal}
- [4.18. Argument parsing classes]Developer_utils.md#argument-parsing-classes){.reference .internal}
- [4.19. Safe pointer classes]Developer_utils.md#safe-pointer-classes){.reference .internal}
- [4.20. File reader classes]Developer_utils.md#file-reader-classes){.reference .internal}
- [4.21. Type label support]Developer_utils.md#type-label-support){.reference .internal}
- [4.22. Memory pool classes]Developer_utils.md#memory-pool-classes){.reference .internal}
- [4.23. Eigensolver functions]Developer_utils.md#eigensolver-functions){.reference .internal}
- [4.24. Communication buffer coding with *ubuf*]Developer_utils.md#communication-buffer-coding-with-ubuf){.reference .internal}
- [4.25. Internal Styles]Developer_internal.md){.reference .internal}
- [4.26. Use of distributed grids within style classes]Developer_grid.md){.reference .internal}
:::
::::
:::::
::::::

:::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::: {#writing-new-styles .section}
# [4.8. ]{.section-number}Writing new styles[](#writing-new-styles "Link to this heading"){.headerlink}

The [[Modifying & extending LAMMPS]{.doc}]Modify.md){.reference .internal} section of the manual gives an overview of how LAMMPS can be extended by writing new classes that derive from existing parent classes in LAMMPS. Here, some specific coding details are provided for writing code for LAMMPS.

::: {.toctree-wrapper .compound}
- [4.8.1. Writing new pair styles]Developer_write_pair.md){.reference .internal}
- [4.8.2. Package and build system considerations]Developer_write_pair.md#package-and-build-system-considerations){.reference .internal}
- [4.8.3. Case 1: a pairwise additive model]Developer_write_pair.md#case-1-a-pairwise-additive-model){.reference .internal}
- [4.8.4. Case 2: a many-body potential]Developer_write_pair.md#case-2-a-many-body-potential){.reference .internal}
- [4.8.5. Case 3: a potential requiring communication]Developer_write_pair.md#case-3-a-potential-requiring-communication){.reference .internal}
- [4.8.6. Case 4: potentials without a compute() function]Developer_write_pair.md#case-4-potentials-without-a-compute-function){.reference .internal}
- [4.8.7. Writing a new fix style]Developer_write_fix.md){.reference .internal}
- [4.8.8. Writing a new command style]Developer_write_command.md){.reference .internal}
- [4.8.9. Case 1: Implementing the geturl command]Developer_write_command.md#case-1-implementing-the-geturl-command){.reference .internal}
:::
::::
:::::
::::::

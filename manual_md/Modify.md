::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#modifying-extending-lammps .section}
# [3. ]{.section-number}Modifying & extending LAMMPS[](#modifying-extending-lammps "Link to this heading"){.headerlink}

LAMMPS has a modular design, so that it is easy to modify or extend with new functionality. In fact, about 95% of its source code is optional. The following pages give basic instructions on adding new features to LAMMPS. More in-depth explanations and documentation of individual functions and classes are given in [[Information for Developers]{.doc}]Developer.md){.reference .internal}.

If you add a new feature to LAMMPS and think it will be of general interest to other users, we encourage you to submit it for inclusion in LAMMPS. This process is explained in the following three pages:

- [[how to prepare and submit your code]{.doc}]Modify_contribute.md){.reference .internal}

- [[requirements for submissions]{.doc}]Modify_requirements.md){.reference .internal}

- [[style guidelines]{.doc}]Modify_style.md){.reference .internal}

A summary description of various types of styles in LAMMPS follows. A discussion of implementing specific styles from scratch is given in [[writing new styles]{.doc}]Developer_write.md){.reference .internal}.

::: {.toctree-wrapper .compound}
- [3.1. Overview]Modify_overview.md){.reference .internal}
- [3.2. Submitting new features for inclusion in LAMMPS]Modify_contribute.md){.reference .internal}
- [3.3. Requirements for contributions to LAMMPS]Modify_requirements.md){.reference .internal}
- [3.4. LAMMPS programming style]Modify_style.md){.reference .internal}
:::

::: {.toctree-wrapper .compound}
- [3.5. Atom styles]Modify_atom.md){.reference .internal}
- [3.6. Pair styles]Modify_pair.md){.reference .internal}
- [3.7. Bond, angle, dihedral, improper styles]Modify_bond.md){.reference .internal}
- [3.8. Compute styles]Modify_compute.md){.reference .internal}
- [3.9. Fix styles]Modify_fix.md){.reference .internal}
- [3.10. Input script command style]Modify_command.md){.reference .internal}
- [3.11. Dump styles]Modify_dump.md){.reference .internal}
- [3.12. Kspace styles]Modify_kspace.md){.reference .internal}
- [3.13. Minimization styles]Modify_min.md){.reference .internal}
- [3.14. Region styles]Modify_region.md){.reference .internal}
- [3.15. Body styles]Modify_body.md){.reference .internal}
- [3.16. Granular Sub-Model styles]Modify_gran_sub_mod.md){.reference .internal}
- [3.17. Thermodynamic output options]Modify_thermo.md){.reference .internal}
- [3.18. Variable options]Modify_variable.md){.reference .internal}
:::
:::::
::::::
:::::::

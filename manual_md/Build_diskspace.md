::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#notes-for-saving-disk-space-when-building-lammps-from-source .section}
# [3.11. ]{.section-number}Notes for saving disk space when building LAMMPS from source[](#notes-for-saving-disk-space-when-building-lammps-from-source "Link to this heading"){.headerlink}

LAMMPS is a large software project with a large number of source files, extensive documentation, and a large collection of example files. When downloading LAMMPS by cloning the [git repository from GitHub](https://github.com/lammps/lammps){.reference .external} this will by default also download the entire commit history since September 2006. Compiling LAMMPS will add the storage requirements of the compiled object files and libraries to the tally.

In a user account on an HPC cluster with filesystem quotas or in other environments with restricted disk space capacity it may be needed to reduce the storage requirements. Here are some suggestions:

- Create a so-called shallow repository by cloning only the last commit instead of the full project history by using [`git`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`clone`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`git@github.com:lammps/lammps`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--depth=1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--branch=develop`{.docutils .literal .notranslate}]{.pre}. This reduces the downloaded size to about half. With [`--depth=1`{.docutils .literal .notranslate}]{.pre} it is not possible to check out different versions/branches of LAMMPS, using [`--depth=1000`{.docutils .literal .notranslate}]{.pre} will make multiple recent versions available at little extra storage needs (the entire git history had nearly 30,000 commits in fall 2021).

- Download a tar archive from either the [download section on the LAMMPS homepage](https://www.lammps.org/download.html){.reference .external} or from the [LAMMPS releases page on GitHub](https://github.com/lammps/lammps/releases){.reference .external} these will not contain the git history at all.

- Build LAMMPS without the debug flag (remove [`-g`{.docutils .literal .notranslate}]{.pre} from the machine makefile or use [`-DCMAKE_BUILD_TYPE=Release`{.docutils .literal .notranslate}]{.pre}) or use the [`strip`{.docutils .literal .notranslate}]{.pre} command on the LAMMPS executable when no more debugging would be needed. The strip command may also be applied to the LAMMPS shared library. The static library may be deleted entirely.

- Delete compiled object files and libraries after copying the LAMMPS executable to a permanent location. When using the traditional build process, one may use [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`clean-<machine>`{.docutils .literal .notranslate}]{.pre} or [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`clean-all`{.docutils .literal .notranslate}]{.pre} to delete object files in the src folder. For CMake based builds, one may use [`make`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`clean`{.docutils .literal .notranslate}]{.pre} or just delete the entire build folder.

- The folders containing the documentation tree (doc), the examples (examples) are not needed to build and run LAMMPS and can be safely deleted. Some files in the potentials folder are large and may be deleted, if not needed. The largest of those files (occupying about 120 MBytes combined) will only be downloaded on demand, when the corresponding package is installed.

- When using the CMake build procedure, the compilation can be done on a (local) scratch storage that will not count toward the quota. A local scratch file system may offer the additional benefit of speeding up creating object files and linking with libraries compared to a networked file system. Also with CMake (and unlike with the traditional make) it is possible to compile LAMMPS executables with different settings and packages included from the same source tree since all the configuration information is stored in the build folder. So it is not necessary to have multiple copies of LAMMPS.
:::
::::
:::::

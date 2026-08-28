::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::::: {#submitting-new-features-for-inclusion-in-lammps .section}
# [3.2. ]{.section-number}Submitting new features for inclusion in LAMMPS[](#submitting-new-features-for-inclusion-in-lammps "Link to this heading"){.headerlink}

We encourage LAMMPS users to submit new features they write for LAMMPS to be included in the LAMMPS distribution and thus become easily accessible to all LAMMPS users. The LAMMPS source code is managed with git and public development is hosted on [GitHub](https://github.com/lammps/lammps){.reference .external}. You can monitor the repository to be notified of releases, follow the ongoing development, and comment on topics of interest to you.

This section contains general information regarding the preparation and submission of new features to LAMMPS. If you are new to development in LAMMPS, we recommend you read one of the tutorials on developing a new [[pair style]{.doc}]Developer_write_pair.md){.reference .internal} or [[fix style]{.doc}]Developer_write_fix.md){.reference .internal} which provide a friendly introduction to what LAMMPS development entails and common vocabulary used on this section.

::: {#communication-with-the-lammps-developers .section}
## [3.2.1. ]{.section-number}Communication with the LAMMPS developers[](#communication-with-the-lammps-developers "Link to this heading"){.headerlink}

For any larger modifications or programming project, you are encouraged to contact the LAMMPS developers ahead of time to discuss implementation strategies. That will make it easier to integrate your contribution and typically results in less work for everyone involved. You are also encouraged to search through the list of [open issues on GitHub](https://github.com/lammps/lammps/issues){.reference .external} and submit a new issue for a planned feature, to avoid duplicating work (and possibly being scooped).

For informal communication with the LAMMPS developers, you may ask to join the [LAMMPS developers on Slack](https://lammps.slack.com){.reference .external}. This slack work space is by invitation only. For access, please send an e-mail to [`slack@lammps.org`{.docutils .literal .notranslate}]{.pre} explaining what part of LAMMPS you are working on. Only discussions related to LAMMPS development are tolerated in that work space, so this is **NOT** for people looking for help with compiling, installing, or using LAMMPS. Please post a message to the [LAMMPS forum](https://www.lammps.org/forum.html){.reference .external} for those purposes.
:::

::: {#time-and-effort-required .section}
## [3.2.2. ]{.section-number}Time and effort required[](#time-and-effort-required "Link to this heading"){.headerlink}

How quickly your contribution will be integrated can vary widely. It depends largely on how much effort is required by the LAMMPS developers to integrate and test it, if any and what kind of changes to the core code are required, how quickly you can address them, and how much interest the contribution is to the larger LAMMPS community. This process can be streamlined by following the [[requirements]{.doc}]Modify_requirements.md){.reference .internal} and [[style guidelines]{.doc}]Modify_style.md){.reference .internal}. A small, modular, well written contribution may be integrated within hours, but a complex change that requires a re-design of a core functionality in LAMMPS can take months before inclusion (though this is rare).
:::

::: {#submission-procedure .section}
## [3.2.3. ]{.section-number}Submission procedure[](#submission-procedure "Link to this heading"){.headerlink}

All changes to LAMMPS (including those from LAMMPS developers) are integrated via pull requests on GitHub and cannot be merged without passing the automated testing and an approving review by a LAMMPS core developer. Before submitting your contribution, you should therefore first ensure that your added or modified code compiles and works correctly with the latest development version of LAMMPS and contains all bug fixes from it.

Once you have prepared everything, see the [[LAMMPS GitHub Tutorial]{.doc}]Howto_github.md){.reference .internal} page for instructions on how to submit your changes or new files through a GitHub pull request. If you are unable or unwilling to submit via GitHub yourself, you may also send patch files or full files to the [LAMMPS developers](https://www.lammps.org/authors.html){.reference .external} and ask them to submit a pull request on GitHub on your behalf. If this is the case, create a gzipped tar file of all new or changed files or a corresponding patch file using 'diff -u' or 'diff -c' format and compress it with gzip. Please only use gzip compression, as this works well and is available on all platforms. This mode of submission may delay the integration as it depends more on the LAMMPS developers.
:::

::: {#external-contributions .section}
## [3.2.4. ]{.section-number}External contributions[](#external-contributions "Link to this heading"){.headerlink}

If you prefer to do so, you can also develop and support your add-on feature **without** having it included in the LAMMPS distribution, for example as a download from a website of your own. See the [External LAMMPS packages and tools](https://www.lammps.org/external.html){.reference .external} page of the LAMMPS website for examples of groups that do this. We are happy to advertise your package and website from that page. Simply email the [developers](https://www.lammps.org/authors.html){.reference .external} with info about your package, and we will post it there. We recommend naming external packages USER-\<name\> so they can be easily distinguished from packages in the LAMMPS distribution which do not have the USER- prefix.
:::

::: {#location-of-files-individual-files-and-packages .section}
## [3.2.5. ]{.section-number}Location of files: individual files and packages[](#location-of-files-individual-files-and-packages "Link to this heading"){.headerlink}

We rarely accept new styles in the core src folder. Thus, please review the list of [[available Packages]{.doc}]Packages_details.md){.reference .internal} to see if your contribution should be added to one of them. It should fit into the general purpose of that package. If it does not fit well, it may be added to one of the EXTRA- packages or the MISC package.

However, if your project includes many related features that are not covered by one of the existing packages or is dependent on a library (bundled or external), it is best to create a new package with its own directory (with a name like FOO). In addition to your new files, the directory should contain a README text file containing your name and contact information and a brief description of what your new package does.
:::

::: {#changes-to-core-lammps-files .section}
## [3.2.6. ]{.section-number}Changes to core LAMMPS files[](#changes-to-core-lammps-files "Link to this heading"){.headerlink}

If designed correctly, most additions do not require any changes to the core code of LAMMPS; they are simply add-on files that are compiled with the rest of LAMMPS. To make those styles work, you may need some trivial changes to the core code. An example of a trivial change is making a parent-class method "virtual" when you derive a new child class from it. If your features involve more substantive changes to the core LAMMPS files, it is particularly encouraged that you communicate with the LAMMPS developers early in development.
:::
:::::::::
::::::::::
:::::::::::

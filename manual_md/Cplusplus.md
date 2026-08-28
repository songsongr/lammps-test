::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#using-the-c-api-directly .section}
# [1.4.1. ]{.section-number}Using the C++ API directly[](#using-the-c-api-directly "Link to this heading"){.headerlink}

Using the C++ classes of the LAMMPS library is lacking some of the convenience of the C library API, but it allows a more direct access to simulation data and thus more low-level manipulations and tighter integration of LAMMPS into another code. While for the complete C library API is provided in the [`library.h`{.docutils .literal .notranslate}]{.pre} header file, for using the C++ API it is required to include the individual header files defining the individual classes in use. Typically the name of the class and the name of the header follow some simple rule. Examples are given below.
:::

::::: {#creating-or-deleting-a-lammps-object .section}
# [1.4.2. ]{.section-number}Creating or deleting a LAMMPS object[](#creating-or-deleting-a-lammps-object "Link to this heading"){.headerlink}

When using the LAMMPS library interfaces, the core task is to create an instance of the [[`LAMMPS_NS::LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} class. In C++ this can be done directly through the [`new`{.docutils .literal .notranslate}]{.pre} operator. All further operations are then initiated through calling member functions of some of the components of the LAMMPS class or accessing their data members. The destruction of the LAMMPS instance is correspondingly initiated by using the [`delete`{.docutils .literal .notranslate}]{.pre} operator. Here is a simple example:

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "lammps.h"

    #include <mpi.h>
    #include <iostream>

    int main(int argc, char **argv)
    {
        LAMMPS_NS::LAMMPS *lmp;
        // custom argument vector for LAMMPS library
        const char *lmpargv[] {"liblammps", "-log", "none"};
        int lmpargc = sizeof(lmpargv)/sizeof(const char *);

        // explicitly initialize MPI
        MPI_Init(&argc, &argv);

        // create LAMMPS instance
        lmp = new LAMMPS_NS::LAMMPS(lmpargc, (char **)lmpargv, MPI_COMM_WORLD);
        // output numerical version string
        std::cout << "LAMMPS version ID: " << lmp->num_ver << std::endl;
        // delete LAMMPS instance
        delete lmp;

        // stop MPI environment
        MPI_Finalize();
        return 0;
    }
:::
::::

This minimal example only requires to include the [`lammps.h`{.docutils .literal .notranslate}]{.pre} header file since it only accesses a non-pointer member of the LAMMPS class.
:::::

::::: {#executing-lammps-commands .section}
# [1.4.3. ]{.section-number}Executing LAMMPS commands[](#executing-lammps-commands "Link to this heading"){.headerlink}

Once a LAMMPS instance is created by your C++ code, you need to set up a simulation and that is most conveniently done by "driving" it through issuing commands like you would do when running a LAMMPS simulation from an input script. Processing of input in LAMMPS is handled by the [[`Input`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_input.md#_CPPv4N9LAMMPS_NS5InputE "LAMMPS_NS::Input"){.reference .internal} class an instance of which is a member of the [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} class. You have two options: reading commands from a file, or executing a single command from a string. See below for a small example:

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "lammps.h"
    #include "input.h"
    #include <mpi.h>

    using namespace LAMMPS_NS;

    int main(int argc, char **argv)
    {
        const char *lmpargv[] {"liblammps", "-log", "none"};
        int lmpargc = sizeof(lmpargv)/sizeof(const char *);

        MPI_Init(&argc, &argv);
        LAMMPS *lmp = new LAMMPS(lmpargc, (char **)lmpargv, MPI_COMM_WORLD);
        lmp->input->file("in.melt");
        lmp->input->one("run 100 post no");
        delete lmp;
        return 0;
    }
:::
::::
:::::
::::::::::
:::::::::::

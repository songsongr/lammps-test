:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#amber-to-lammps-tutorial .section}
# [10.4.3. ]{.section-number}AMBER to LAMMPS Tutorial[](#amber-to-lammps-tutorial "Link to this heading"){.headerlink}

**written by Arun Srikanth Sridhar**

::: versionadded
[Added in version 11Feb2026.]{.versionmodified .added}
:::

[AMBER2LAMMPS](https://github.com/askforarun/AMBER2LAMMPS){.reference .external} is a Python utility that converts AMBER topology ([`.prmtop`{.docutils .literal .notranslate}]{.pre}) and coordinate/charge ([`.crd`{.docutils .literal .notranslate}]{.pre}) files into LAMMPS data and parameter files. It provides both a command-line interface and a Python API with built-in validation. This tutorial provides a detailed workflow with examples using the [AMBER2LAMMPS](https://github.com/askforarun/AMBER2LAMMPS){.reference .external} python utility. The legacy scripts previously distributed in [`tools/amber2lmp`{.docutils .literal .notranslate}]{.pre} have been removed due to their reliance on Python 2 and lack of maintenance.

This tutorial assumes familiarity with molecular dynamics simulations and molecular mechanics force fields, including atom typing, bond topologies, partial charge assignment, and different force field families (AMBER, CHARMM, GROMOS, OPLS/AA). For an introduction to force field concepts, see [[Some general force field considerations]{.doc}]Howto_FFgeneral.md){.reference .internal} before starting this tutorial. AMBER offers various force fields for different biomolecules, including ff19SB/ff14SB (proteins), Bsc1/OL3 (DNA/RNA), GLYCAM06 (carbohydrates), and Lipid17 (lipids), alongside the General AMBER Force Field (GAFF/GAFF2) for small organic molecules (see [https://ambermd.org/AmberModels.php](https://ambermd.org/AmberModels.php){.reference .external} and Wang, J., et al., J. Comput. Chem., 25, 1157-1174 (2004) for GAFF force field development).

::: {.warning .admonition}
Important Force Field Compatibility Warning:

Different force field families (AMBER, CHARMM, GROMOS, OPLS/AA) use distinct atom typing schemes, charge assignment methods, and parameterization strategies. **Never mix and match parameters from different force field families; this leads to unphysical results and simulation failures.** Always use a consistent force field family throughout your system.
:::

------------------------------------------------------------------------

- [What the AMBER2LAMMPS tool does](#what-the-amber2lammps-tool-does){#id1 .reference .internal}

- [AMBER2LAMMPS homepage and download](#amber2lammps-homepage-and-download){#id2 .reference .internal}

- [Requirements](#requirements){#id3 .reference .internal}

- [Installing dependencies](#installing-dependencies){#id4 .reference .internal}

  - [AmberTools](#ambertools){#id5 .reference .internal}

  - [Python packages](#python-packages){#id6 .reference .internal}

  - [Open Babel (optional, for SMILES to PDB conversion)](#open-babel-optional-for-smiles-to-pdb-conversion){#id7 .reference .internal}

- [Command Reference](#command-reference){#id8 .reference .internal}

- [Conversion Process](#conversion-process){#id9 .reference .internal}

  - [Charge normalization](#charge-normalization){#id10 .reference .internal}

- [Workflow Examples](#workflow-examples){#id11 .reference .internal}

- [Prepare input files (ethanol example)](#prepare-input-files-ethanol-example){#id12 .reference .internal}

  - [Convert SMILES to PDB (optional)](#convert-smiles-to-pdb-optional){#id13 .reference .internal}

  - [Generate AMBER topology and coordinates](#generate-amber-topology-and-coordinates){#id14 .reference .internal}

- [Basic conversion workflow](#basic-conversion-workflow){#id15 .reference .internal}

  - [LAMMPS input script](#lammps-input-script){#id16 .reference .internal}

  - [CLI usage with LAMMPS execution](#cli-usage-with-lammps-execution){#id17 .reference .internal}

    - [Additional CLI examples](#additional-cli-examples){#id18 .reference .internal}

  - [Python API usage with LAMMPS execution](#python-api-usage-with-lammps-execution){#id19 .reference .internal}

    - [Additional API examples](#additional-api-examples){#id20 .reference .internal}

- [Validation of AMBER2LAMMPS](#validation-of-amber2lammps){#id21 .reference .internal}

- [Getting Help](#getting-help){#id22 .reference .internal}

- [Citation](#citation){#id23 .reference .internal}

------------------------------------------------------------------------

::: {#what-the-amber2lammps-tool-does .section}
## [What the AMBER2LAMMPS tool does](#id1){.toc-backref role="doc-backlink"}[](#what-the-amber2lammps-tool-does "Link to this heading"){.headerlink}

This tool helps you run molecular dynamics simulations in **LAMMPS** when you have your molecular system set up in **AMBER** format. AMBER2LAMMPS uses AmberTools utilities (antechamber and tleap) to perform the conversion.

**Typical workflow:**

1.  Start with a molecular structure (PDB file or SMILES string to be converted to PDB)

2.  Use AMBER tools to create AMBER files ([`.prmtop`{.docutils .literal .notranslate}]{.pre}, [`.crd`{.docutils .literal .notranslate}]{.pre})

3.  **Convert AMBER files to LAMMPS format** using this tool

4.  Run your simulation in LAMMPS

**What gets converted:**

- **\`\`.prmtop\`\`** (topology file): Contains bonds, angles, atom types, and force field parameters -\> LAMMPS data and parameter files

- **\`\`.crd\`\`** (coordinates file): Contains atomic positions -\> LAMMPS coordinates

**What you get as output:**

- **LAMMPS data file** (e.g., [`data.lammps`{.docutils .literal .notranslate}]{.pre}): Contains atomic coordinates, box dimensions, and molecular topology

- **LAMMPS parameter file** (e.g., [`parm.lammps`{.docutils .literal .notranslate}]{.pre}): Contains force field parameters for bonds, angles, and non-bonded interactions
:::

------------------------------------------------------------------------

::::: {#amber2lammps-homepage-and-download .section}
## [AMBER2LAMMPS homepage and download](#id2){.toc-backref role="doc-backlink"}[](#amber2lammps-homepage-and-download "Link to this heading"){.headerlink}

AMBER2LAMMPS is developed and maintained outside the LAMMPS repository. Download its source code from its GitHub project page or clone its repository from GitHub:

:::: {.highlight-bash .notranslate}
::: highlight
    # direct download
    curl -L -o AMBER2LAMMPS-main.tar.gz https://github.com/askforarun/AMBER2LAMMPS/archive/refs/heads/main.tar.gz
    tar -xzvvf AMBER2LAMMPS-main.tar.gz
    cd AMBER2LAMMPS-main

    # clone repository
    git clone https://github.com/askforarun/AMBER2LAMMPS.git
    cd AMBER2LAMMPS
:::
::::
:::::

------------------------------------------------------------------------

::: {#requirements .section}
## [Requirements](#id3){.toc-backref role="doc-backlink"}[](#requirements "Link to this heading"){.headerlink}

**Platform Compatibility**

AMBER2LAMMPS works on all major platforms:

- **Linux**: Full support (Ubuntu, CentOS, Fedora, etc.)

- **macOS**: Full support (Intel and Apple Silicon)

- **Windows**: Support via WSL2 or Git Bash

**System Requirements**

- **Structure**: PDB file (or a SMILES string that you can convert to PDB).

- **AmberTools utilities**: [`antechamber`{.docutils .literal .notranslate}]{.pre} and [`tleap`{.docutils .literal .notranslate}]{.pre} to build [`.prmtop`{.docutils .literal .notranslate}]{.pre} and [`.crd`{.docutils .literal .notranslate}]{.pre}.

- **Python packages**: [`parmed`{.docutils .literal .notranslate}]{.pre} and [`numpy`{.docutils .literal .notranslate}]{.pre}.

- **LAMMPS**: On your [`PATH`{.docutils .literal .notranslate}]{.pre} ([`which`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`lmp`{.docutils .literal .notranslate}]{.pre} or [`lmp`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-help`{.docutils .literal .notranslate}]{.pre}) and built with [`MOLECULE`{.docutils .literal .notranslate}]{.pre}, [`KSPACE`{.docutils .literal .notranslate}]{.pre}, and [`EXTRA-MOLECULE`{.docutils .literal .notranslate}]{.pre} packages.

- **Optional**: Open Babel ([`obabel`{.docutils .literal .notranslate}]{.pre}) if starting from SMILES.
:::

:::::::::::::::::: {#installing-dependencies .section}
## [Installing dependencies](#id4){.toc-backref role="doc-backlink"}[](#installing-dependencies "Link to this heading"){.headerlink}

::::: {#ambertools .section}
### [AmberTools](#id5){.toc-backref role="doc-backlink"}[](#ambertools "Link to this heading"){.headerlink}

Install from [https://ambermd.org/GetAmber.php#ambertools](https://ambermd.org/GetAmber.php#ambertools){.reference .external} and activate the environment:

:::: {.highlight-bash .notranslate}
::: highlight
    conda activate Ambertools23  # or your AmberTools environment
:::
::::

To see the available force fields, run antechamber -h
:::::

::::::: {#python-packages .section}
### [Python packages](#id6){.toc-backref role="doc-backlink"}[](#python-packages "Link to this heading"){.headerlink}

Using conda (recommended):

:::: {.highlight-bash .notranslate}
::: highlight
    conda install -c conda-forge parmed numpy
:::
::::

Using pip:

:::: {.highlight-bash .notranslate}
::: highlight
    pip install --user parmed numpy
:::
::::
:::::::

::::::::: {#open-babel-optional-for-smiles-to-pdb-conversion .section}
### [Open Babel (optional, for SMILES to PDB conversion)](#id7){.toc-backref role="doc-backlink"}[](#open-babel-optional-for-smiles-to-pdb-conversion "Link to this heading"){.headerlink}

Using conda (recommended):

:::: {.highlight-bash .notranslate}
::: highlight
    conda install -c conda-forge openbabel
:::
::::

Using pip:

:::: {.highlight-bash .notranslate}
::: highlight
    pip install --user openbabel
:::
::::

Using system package manager:

:::: {.highlight-bash .notranslate}
::: highlight
    # Ubuntu/Debian
    sudo apt-get install openbabel

    # Fedora/Red Hat
    sudo dnf install openbabel

    # macOS
    brew install open-babel
:::
::::
:::::::::
::::::::::::::::::

------------------------------------------------------------------------

::: {#command-reference .section}
## [Command Reference](#id8){.toc-backref role="doc-backlink"}[](#command-reference "Link to this heading"){.headerlink}

+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Argument                                                                                                                              | Required? | Description                                                                                                                                         |
+=======================================================================================================================================+===========+=====================================================================================================================================================+
| **Input Files**                                                                                                                       |           |                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [`topology`{.docutils .literal .notranslate}]{.pre}                                                                                   | yes       | AMBER topology file ([`.prmtop`{.docutils .literal .notranslate}]{.pre})                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [`crd`{.docutils .literal .notranslate}]{.pre}                                                                                        | yes       | AMBER coordinate file ([`.crd`{.docutils .literal .notranslate}]{.pre})                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Output Files**                                                                                                                      |           |                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [`data_file`{.docutils .literal .notranslate}]{.pre}                                                                                  | yes       | Output LAMMPS data filename                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [`param_file`{.docutils .literal .notranslate}]{.pre}                                                                                 | yes       | Output LAMMPS parameter filename                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Options**                                                                                                                           |           |                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [`-b,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--buffer`{.docutils .literal .notranslate}]{.pre} | optional  | Vacuum padding (Angstrom) for the simulation box. Default: [`3.8`{.docutils .literal .notranslate}]{.pre}.                                          |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [`--charge`{.docutils .literal .notranslate}]{.pre}                                                                                   | yes       | Target net charge (integer). Applies a uniform offset to every atom to reach this charge (1e-6 tolerance).                                          |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                       |           | Does not add counterions; add those with the AMBER tools before conversion.                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [`--keep-temp`{.docutils .literal .notranslate}]{.pre}                                                                                | optional  | Keep temporary files (bonds.txt, angles.txt, dihedrals.txt, pairs.txt) after conversion. Default: [`False`{.docutils .literal .notranslate}]{.pre}. |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [`--verbose`{.docutils .literal .notranslate}]{.pre}                                                                                  | optional  | Print step-by-step progress, counts, and box size. Default: [`False`{.docutils .literal .notranslate}]{.pre}.                                       |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| [`-h,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--help`{.docutils .literal .notranslate}]{.pre}   | optional  | Show help message.                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
:::

:::: {#conversion-process .section}
## [Conversion Process](#id9){.toc-backref role="doc-backlink"}[](#conversion-process "Link to this heading"){.headerlink}

The converter implements the following sequence (see [`amber_to_lammps.py`{.docutils .literal .notranslate}]{.pre}):

1.  **Input validation**: [`validate_files`{.docutils .literal .notranslate}]{.pre} checks that [`topology`{.docutils .literal .notranslate}]{.pre} and [`crd`{.docutils .literal .notranslate}]{.pre} exist and are readable. The CLI performs this validation automatically, while the Python API requires manual validation if desired.

2.  **AMBER topology load**: ParmEd reads atoms, bonds, angles, and dihedrals from [`.prmtop`{.docutils .literal .notranslate}]{.pre}; counts are printed with [`--verbose`{.docutils .literal .notranslate}]{.pre}.

3.  **Atom typing and masses**: Atom types and masses are extracted from the topology file.

4.  **Coordinates and charges**: Coordinates are read from the CRD file and charges from the topology file.

5.  **Box creation (\`\`--buffer\`\`)**: A bounding box around the coordinates is expanded by the buffer on all sides.

6.  **Charge normalization**: Charges are shifted uniformly to achieve the target net charge specified by [`--charge`{.docutils .literal .notranslate}]{.pre}.

7.  **Non-bonded parameters**: Lennard-Jones parameters are extracted from the topology and become [`pair_coeff`{.docutils .literal .notranslate}]{.pre} entries in the parameter file.

8.  **Topology terms**: Bonds, angles, and dihedrals are exported via ParmEd to temporary files and written to the LAMMPS data/parameter files.

9.  **Cleanup**: Temporary helper files ([`bonds.txt`{.docutils .literal .notranslate}]{.pre}, [`angles.txt`{.docutils .literal .notranslate}]{.pre}, [`dihedrals.txt`{.docutils .literal .notranslate}]{.pre}, [`pairs.txt`{.docutils .literal .notranslate}]{.pre}) are removed unless [`--keep-temp`{.docutils .literal .notranslate}]{.pre} is specified.

10. **Verbose diagnostics**: With [`--verbose`{.docutils .literal .notranslate}]{.pre}, the script reports counts, box extents after buffering, and the final total charge.

::: {#charge-normalization .section}
### [Charge normalization](#id10){.toc-backref role="doc-backlink"}[](#charge-normalization "Link to this heading"){.headerlink}

**AMBER Charge Schemes:** AMBER uses various charge methods including:

- **RESP** (Restrained Electrostatic Potential): Derived from quantum mechanical electrostatic potential

- **AM1-BCC**: Semi-empirical charges with bond charge corrections

- **CM5** or **CM1A**: Charge models based on atomic charges

In this tutorial, we will use AM1-BCC charges.

**Charge Normalization in AMBER2LAMMPS:**

- Most systems should be overall neutral for PME to converge; small residual charges (+/-0.003) from AM1-BCC (or other methods) calculated from antechamber are common.

- For neutral molecules, run with [`--charge`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0`{.docutils .literal .notranslate}]{.pre} so AMBER2LAMMPS applies a uniform offset that removes the residual charge; this prevents the error from scaling up when the system is replicated in LAMMPS.

- For intentionally charged species (e.g., protonated or deprotonated), add counterions in tleap/packmol before conversion. AMBER2LAMMPS never adds ions; it only shifts existing charges to your requested total.

- How the flag works: - [`--charge`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0`{.docutils .literal .notranslate}]{.pre}: uniform shift makes the summed charge 0 within 1e-6. - [`--charge`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+1`{.docutils .literal .notranslate}]{.pre} (or any integer): uniform shift makes the total that integer within 1e-6. - The same constant is added to every atom, so relative charge differences are preserved.

**Example:** If your system has net charge +0.003 and you specify

:   [`--charge`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0`{.docutils .literal .notranslate}]{.pre}, each atom's charge will be reduced by [`(0.003`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`number_of_atoms)`{.docutils .literal .notranslate}]{.pre} to reach neutrality.
:::
::::

------------------------------------------------------------------------

::: {#workflow-examples .section}
## [Workflow Examples](#id11){.toc-backref role="doc-backlink"}[](#workflow-examples "Link to this heading"){.headerlink}
:::

::::::: {#prepare-input-files-ethanol-example .section}
## [Prepare input files (ethanol example)](#id12){.toc-backref role="doc-backlink"}[](#prepare-input-files-ethanol-example "Link to this heading"){.headerlink}

::::: {#convert-smiles-to-pdb-optional .section}
### [Convert SMILES to PDB (optional)](#id13){.toc-backref role="doc-backlink"}[](#convert-smiles-to-pdb-optional "Link to this heading"){.headerlink}

If you start from a SMILES string, generate a PDB with [`obabel`{.docutils .literal .notranslate}]{.pre}:

:::: {.highlight-bash .notranslate}
::: highlight
    obabel -:CCO -h -opdb -O ethanol.pdb --gen3d  # adds hydrogens, recommended
    obabel -:c1ccccc1 -h -opdb -O benzene.pdb --gen3d
    obabel -:"CC(=O)OC1=CC=CC=C1C(=O)O" -h -opdb -O aspirin.pdb --gen3d
:::
::::
:::::

::: {#generate-amber-topology-and-coordinates .section}
### [Generate AMBER topology and coordinates](#id14){.toc-backref role="doc-backlink"}[](#generate-amber-topology-and-coordinates "Link to this heading"){.headerlink}

Assuming [`ethanol.pdb`{.docutils .literal .notranslate}]{.pre} is your structure:

1.  Generate a MOL2 file with charges:

    :::: {.highlight-bash .notranslate}
    ::: highlight
        antechamber -j 4 -at gaff2 -dr yes -fi pdb -fo mol2 \
           -i ethanol.pdb -o ethanol.mol2 -c bcc
    :::
    ::::

    The [`-c`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`bcc`{.docutils .literal .notranslate}]{.pre} assigns AM1-BCC charges; use the [`-at`{.docutils .literal .notranslate}]{.pre} option to choose the force field.

2.  Create [`tleap.in`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-text .notranslate}
    ::: highlight
        source leaprc.gaff2
        ETH = loadmol2 ethanol.mol2
        check ETH
        saveamberparm SUS ethanol.prmtop ethanol.crd
        quit
    :::
    ::::

    leaprc.gaff2 loads the gaff2 force field parameters that were used in step 1

3.  Run tleap and inspect [`leap.log`{.docutils .literal .notranslate}]{.pre} for errors:

    :::: {.highlight-bash .notranslate}
    ::: highlight
        tleap -f tleap.in
    :::
    ::::

    Outputs: [`ethanol.prmtop`{.docutils .literal .notranslate}]{.pre} and [`ethanol.crd`{.docutils .literal .notranslate}]{.pre}.
:::
:::::::

------------------------------------------------------------------------

:::::::::::::::::::: {#basic-conversion-workflow .section}
## [Basic conversion workflow](#id15){.toc-backref role="doc-backlink"}[](#basic-conversion-workflow "Link to this heading"){.headerlink}

::::: {#lammps-input-script .section}
### [LAMMPS input script](#id16){.toc-backref role="doc-backlink"}[](#lammps-input-script "Link to this heading"){.headerlink}

Save the following LAMMPS commands in a file called [`example_lammps_input.lmp`{.docutils .literal .notranslate}]{.pre}:

:::: {.highlight-text .notranslate}
::: highlight
    # LAMMPS Input Script for Converted AMBER System

    units real
    dimension 3
    boundary p p p
    atom_style full

    read_data data.lammps

    pair_style      lj/cut/coul/long 9 9
    bond_style      harmonic
    angle_style     harmonic
    dihedral_style  fourier
    special_bonds lj 0.0 0.0 0.5 coul 0.0 0.0 0.83333333

    include parm.lammps

    thermo_style custom ebond eangle edihed eimp epair evdwl ecoul elong etail pe
    run 0
:::
::::

The above script includes the parameter file via [`include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`parm.lammps`{.docutils .literal .notranslate}]{.pre} and loads the coordinate data via [`read_data`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`data.lammps`{.docutils .literal .notranslate}]{.pre}.
:::::

:::::::::: {#cli-usage-with-lammps-execution .section}
### [CLI usage with LAMMPS execution](#id17){.toc-backref role="doc-backlink"}[](#cli-usage-with-lammps-execution "Link to this heading"){.headerlink}

Ensure amber_to_lammps.py is executable and the input files are accessible.

Run the converter:

:::: {.highlight-bash .notranslate}
::: highlight
    python3 amber_to_lammps.py data.lammps parm.lammps \
       ethanol.prmtop ethanol.crd --charge 0 --verbose -b 4.5
:::
::::

Outputs: [`data.lammps`{.docutils .literal .notranslate}]{.pre} (coordinates/topology) and [`parm.lammps`{.docutils .literal .notranslate}]{.pre}

Run with LAMMPS:

:::: {.highlight-bash .notranslate}
::: highlight
    lmp -in example_lammps_input.lmp
:::
::::

::::: {#additional-cli-examples .section}
#### [Additional CLI examples](#id18){.toc-backref role="doc-backlink"}[](#additional-cli-examples "Link to this heading"){.headerlink}

:::: {.highlight-bash .notranslate}
::: highlight
    # Custom buffer and verbose logging (adds 5 Angstroms of padding)
    python3 amber_to_lammps.py my_data.lammps my_params.lammps \
       ethanol.prmtop ethanol.crd --charge 0 --verbose -b 5.0

    # Custom output names
    python3 amber_to_lammps.py system.data system.parm system.prmtop \
       system.crd --charge 0

    # Minimal output without verbose logging
    python3 amber_to_lammps.py small.data small.parm \
       ethanol.prmtop ethanol.crd --charge 0 -b 3.0

    # Using absolute paths with custom buffer
    python3 amber_to_lammps.py /home/user/lammps/output/data.lammps /home/user/lammps/output/param.lammps /home/user/amber/topology.prmtop /home/user/amber/coords.crd --charge 0 -b 4.5

    # Keep temporary files for debugging
    python3 amber_to_lammps.py debug_data.lammps debug_parm.lammps molecule.prmtop molecule.crd --charge 0 --keep-temp --verbose
:::
::::

Make sure to rename the files in example_lammps_input.lmp to match the names of the files generated by the conversion when custom file names are used.
:::::
::::::::::

:::::::: {#python-api-usage-with-lammps-execution .section}
### [Python API usage with LAMMPS execution](#id19){.toc-backref role="doc-backlink"}[](#python-api-usage-with-lammps-execution "Link to this heading"){.headerlink}

This example script uses the [[LAMMPS Python module]{.doc}]Python_head.md){.reference .internal} to execute LAMMPS directly from Python.

:::: {.highlight-python .notranslate}
::: highlight
    from amber_to_lammps import amber2lammps, validate_files
    from lammps import lammps

    validate_files('ethanol.prmtop', 'ethanol.crd')

    amber2lammps(
        data_file='data.lammps',
        param_file='parm.lammps',
        topology='ethanol.prmtop',
        crd='ethanol.crd',
        charge=0,
        buffer=3.8,
        verbose=True,
    )

    lmp = lammps()
    lmp.file('example_lammps_input.lmp')
    lmp.close()
:::
::::

::::: {#additional-api-examples .section}
#### [Additional API examples](#id20){.toc-backref role="doc-backlink"}[](#additional-api-examples "Link to this heading"){.headerlink}

:::: {.highlight-python .notranslate}
::: highlight
    # Example 1: Basic conversion without validation
    from amber_to_lammps import amber2lammps

    amber2lammps(
        data_file='benzene.data',
        param_file='benzene.parm',
        topology='benzene.prmtop',
        crd='benzene.crd',
        charge=0
    )

    # Example 2: Custom buffer and verbose output
    amber2lammps(
        data_file='ethanol.data',
        param_file='ethanol.parm',
        topology='ethanol.prmtop',
        crd='ethanol.crd',
        charge=0,
        buffer=5.0,
        verbose=True,
        keep_temp=True  # Keep temporary files for inspection
    )

    # Example 3: Batch processing multiple molecules
    from amber_to_lammps import amber2lammps, validate_files

    molecules = ['ethanol', 'benzene', 'aspirin']

    for mol in molecules:
        validate_files(f'{mol}.prmtop', f'{mol}.crd')
        amber2lammps(
            data_file=f'{mol}.data',
            param_file=f'{mol}.parm',
            topology=f'{mol}.prmtop',
            crd=f'{mol}.crd',
            charge=0,
            verbose=True
        )
:::
::::
:::::
::::::::
::::::::::::::::::::

::: {#validation-of-amber2lammps .section}
## [Validation of AMBER2LAMMPS](#id21){.toc-backref role="doc-backlink"}[](#validation-of-amber2lammps "Link to this heading"){.headerlink}

AMBER2LAMMPS has been validated against InterMol output. See the project page for details: [https://github.com/askforarun/AMBER2LAMMPS](https://github.com/askforarun/AMBER2LAMMPS){.reference .external}
:::

::: {#getting-help .section}
## [Getting Help](#id22){.toc-backref role="doc-backlink"}[](#getting-help "Link to this heading"){.headerlink}

- **Submit Issues:** [https://github.com/askforarun/AMBER2LAMMPS/issues](https://github.com/askforarun/AMBER2LAMMPS/issues){.reference .external}

- **Feature Requests:** Use GitHub Issues or Discussions

- **Questions:** Use GitHub Discussions or Issues
:::

::: {#citation .section}
## [Citation](#id23){.toc-backref role="doc-backlink"}[](#citation "Link to this heading"){.headerlink}

If you use the AMBER2LAMMPS tool in your research, please cite it as:

**DOI:** [10.5281/zenodo.18114886](https://doi.org/10.5281/zenodo.18114886){.reference .external}
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

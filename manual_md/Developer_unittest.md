:::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::::::::::::::::::::::::::::::::::::::::: {#adding-tests-for-unit-testing .section}
# [4.12. ]{.section-number}Adding tests for unit testing[](#adding-tests-for-unit-testing "Link to this heading"){.headerlink}

This section discusses adding or expanding tests for the unit test infrastructure included into the LAMMPS source code distribution. Unlike example inputs, unit tests focus on testing the "local" behavior of individual features, tend to run fast, and should be set up to cover as much of the added code as possible. When contributing code to the distribution, the LAMMPS developers will appreciate if additions to the integrated unit test facility are included.

Given the complex nature of MD simulations where many operations can only be performed when suitable "real" simulation environment has been set up, not all tests will be unit tests in the strict definition of the term. They are rather executed on a more abstract level by issuing LAMMPS script commands and then inspecting the changes to the internal data. For some classes of tests, generic test programs have been written that can be applied to parts of LAMMPS that use the same interface (via polymorphism) and those are driven by input files, so tests can be added by simply adding more of those input files. Those tests should be seen more as a hybrid between unit and regression tests.

When adding tests it is recommended to also [[enable support for code coverage reporting]{.std .std-ref}]Build_development.md#testing){.reference .internal}, and study the coverage reports so that it is possible to monitor which parts of the code of a given file are executed during the tests and which tests would need to be added to increase the coverage.

The tests are grouped into categories and corresponding folders. The following sections describe how the tests are implemented and executed in those categories with increasing complexity of tests and implementation.

::::::::::::::: {#tests-for-utility-functions .section}
## [4.12.1. ]{.section-number}Tests for utility functions[](#tests-for-utility-functions "Link to this heading"){.headerlink}

These tests are driven by programs in the [`unittest/utils`{.docutils .literal .notranslate}]{.pre} folder and most closely resemble conventional unit tests. There is one test program for each namespace or group of classes or file. The naming convention for the sources and executables is that they start with with [`test_`{.docutils .literal .notranslate}]{.pre}. The following sources and groups of tests are currently available:

+---------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| File name:                                                          | Test name:  | Description:                                                                                                                                                                                                                                                                                                                                                                            |
+=====================================================================+=============+=========================================================================================================================================================================================================================================================================================================================================================================================+
| [`test_argutils.cpp`{.docutils .literal .notranslate}]{.pre}        | ArgInfo     | Tests for [`ArgInfo`{.docutils .literal .notranslate}]{.pre} class used by LAMMPS                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`test_fmtlib.cpp`{.docutils .literal .notranslate}]{.pre}          | FmtLib      | Tests for [`{fmt}`{.docutils .literal .notranslate}]{.pre} or [`std::format`{.docutils .literal .notranslate}]{.pre} functions used by LAMMPS                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`test_math_eigen_impl.cpp`{.docutils .literal .notranslate}]{.pre} | MathEigen   | Tests for [`MathEigen::`{.docutils .literal .notranslate}]{.pre} classes and functions                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`test_mempool.cpp`{.docutils .literal .notranslate}]{.pre}         | MemPool     | Tests for [[`MyPage`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4I0EN9LAMMPS_NS6MyPageE "LAMMPS_NS::MyPage"){.reference .internal} and [[`MyPoolChunk`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4I0EN9LAMMPS_NS11MyPoolChunkE "LAMMPS_NS::MyPoolChunk"){.reference .internal}             |
+---------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`test_tokenizer.cpp`{.docutils .literal .notranslate}]{.pre}       | Tokenizer   | Tests for [[`Tokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS9TokenizerE "LAMMPS_NS::Tokenizer"){.reference .internal} and [[`ValueTokenizer`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Developer_utils.md#_CPPv4N9LAMMPS_NS14ValueTokenizerE "LAMMPS_NS::ValueTokenizer"){.reference .internal} |
+---------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`test_utils.cpp`{.docutils .literal .notranslate}]{.pre}           | Utils       | Tests for [`utils::`{.docutils .literal .notranslate}]{.pre} [[functions]{.doc}]Developer_utils.md){.reference .internal}                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`test_fft3d.cpp`{.docutils .literal .notranslate}]{.pre}           | FFT3D       | Tests for standard FFT3d wrapper (KISS, FFTW3, MKL, NVPL)                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`test_fft3d_kokkos.cpp`{.docutils .literal .notranslate}]{.pre}    | FFT3DKokkos | Tests for KOKKOS FFT3d wrapper (CPU and GPU back ends)                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

To add tests either an existing source file needs to be modified or a new source file needs to be added to the distribution and enabled for testing. To add a new file suitable CMake script code needs to be added to the [`CMakeLists.txt`{.docutils .literal .notranslate}]{.pre} file in the [`unittest/utils`{.docutils .literal .notranslate}]{.pre} folder. Example:

:::: {.highlight-cmake .notranslate}
::: highlight
    add_executable(test_tokenizer test_tokenizer.cpp)
    target_link_libraries(test_tokenizer PRIVATE lammps GTest::GMockMain GTest::GMock GTest::GTest)
    add_test(Tokenizer test_tokenizer)
:::
::::

This adds instructions to build the [`test_tokenizer`{.docutils .literal .notranslate}]{.pre} executable from [`test_tokenizer.cpp`{.docutils .literal .notranslate}]{.pre} and links it with the GoogleTest libraries and the LAMMPS library as well as it uses the [`main()`{.docutils .literal .notranslate}]{.pre} function from the GoogleMock library of GoogleTest. The third line registers the executable as a test program to be run from [`ctest`{.docutils .literal .notranslate}]{.pre} under the name [`Tokenizer`{.docutils .literal .notranslate}]{.pre}.

The test executable itself will execute multiple individual tests through the GoogleTest framework. In this case each test consists of creating a tokenizer class instance with a given string and explicit or default separator choice, and then executing member functions of the class and comparing their results with expected values. A few examples:

:::: {.highlight-c++ .notranslate}
::: highlight
    TEST(Tokenizer, empty_string)
    {
        Tokenizer t("", " ");
        ASSERT_EQ(t.count(), 0);
    }

    TEST(Tokenizer, two_words)
    {
        Tokenizer t("test word", " ");
        ASSERT_EQ(t.count(), 2);
    }

    TEST(Tokenizer, default_separators)
    {
        Tokenizer t(" \r\n test \t word \f");
        ASSERT_THAT(t.next(), Eq("test"));
        ASSERT_THAT(t.next(), Eq("word"));
        ASSERT_EQ(t.count(), 2);
    }
:::
::::

Each of these TEST functions will become an individual test run by the test program. When using the [`ctest`{.docutils .literal .notranslate}]{.pre} command as a front end to run the tests, their output will be suppressed and only a summary printed, but adding the '-V' option will then produce output from the tests above like the following:

:::: {.highlight-console .notranslate}
::: highlight
    [...]
    1: [ RUN      ] Tokenizer.empty_string
    1: [       OK ] Tokenizer.empty_string (0 ms)
    1: [ RUN      ] Tokenizer.two_words
    1: [       OK ] Tokenizer.two_words (0 ms)
    1: [ RUN      ] Tokenizer.default_separators
    1: [       OK ] Tokenizer.default_separators (0 ms)
    [...]
:::
::::

The MathEigen test collection has been adapted from a standalone test and does not use the GoogleTest framework and thus not representative. The other test sources, however, can serve as guiding examples for additional tests.

:::::::: {#fft-testing-infrastructure .section}
### FFT Testing Infrastructure[](#fft-testing-infrastructure "Link to this heading"){.headerlink}

::: versionadded
[Added in version 10Dec2025.]{.versionmodified .added}
:::

The FFT tests ([`test_fft3d.cpp`{.docutils .literal .notranslate}]{.pre} and [`test_fft3d_kokkos.cpp`{.docutils .literal .notranslate}]{.pre}) validate the LAMMPS FFT wrapper implementations for both standard (CPU) and KOKKOS (CPU/GPU) back ends. These tests require the KSPACE package and use specialized helper utilities to ensure FFT correctness across different library back ends (KISS FFT, FFTW3, MKL, NVPL, cuFFT, hipFFT, etc.).

**Building and Running FFT Tests:**

The FFT tests are automatically enabled when [`ENABLE_TESTING=ON`{.docutils .literal .notranslate}]{.pre} and [`PKG_KSPACE=ON`{.docutils .literal .notranslate}]{.pre} are set during CMake configuration. For KOKKOS FFT tests, [`PKG_KOKKOS=ON`{.docutils .literal .notranslate}]{.pre} is also required.

Run only FFT tests using the [`ctest`{.docutils .literal .notranslate}]{.pre} command of the CMake software:

:::: {.highlight-bash .notranslate}
::: highlight
    ctest -R FFT3D          # Run all tests with FFT3D in their name
    ctest -R FFT3D -V       # Same as above but with verbose output
    ctest -L fft            # Run all tests labeled with 'fft'
:::
::::

Tests automatically skip configurations requiring libraries or back ends not available in the current build (e.g., FFTW3, MPI, CUDA).

**FFT Test Helper Header:**

The testing infrastructure uses [`fft_test_helpers.h`{.docutils .literal .notranslate}]{.pre} which contains test data generators, validators, and utilities.

For runtime configuration detection, tests use the existing [`Info`{.docutils .literal .notranslate}]{.pre} class API ([`Info::has_package()`{.docutils .literal .notranslate}]{.pre}, [`Info::has_accelerator_feature()`{.docutils .literal .notranslate}]{.pre}, etc.).

The [`fft_test_helpers.h`{.docutils .literal .notranslate}]{.pre} header provides three main namespaces:

1.  **FFTTestHelpers** - utility functions: [`FFTBuffer`{.docutils .literal .notranslate}]{.pre} (RAII wrapper), [`idx3d()`{.docutils .literal .notranslate}]{.pre} (index conversion), [`scaled_tolerance()`{.docutils .literal .notranslate}]{.pre} (grid-size-dependent precision)

2.  **FFTTestData** - test data generators: [`DeltaFunctionGenerator`{.docutils .literal .notranslate}]{.pre}, [`ConstantGenerator`{.docutils .literal .notranslate}]{.pre}, [`SineWaveGenerator`{.docutils .literal .notranslate}]{.pre}, [`GaussianGenerator`{.docutils .literal .notranslate}]{.pre}, [`RandomComplexGenerator`{.docutils .literal .notranslate}]{.pre}, [`MixedModesGenerator`{.docutils .literal .notranslate}]{.pre}

3.  **FFTValidation** - validators: [`RoundTripValidator`{.docutils .literal .notranslate}]{.pre}, [`KnownAnswerValidator`{.docutils .literal .notranslate}]{.pre}, [`ParsevalValidator`{.docutils .literal .notranslate}]{.pre}, [`HermitianSymmetryValidator`{.docutils .literal .notranslate}]{.pre}, [`LinearityValidator`{.docutils .literal .notranslate}]{.pre}

**Example Test:**

:::: {.highlight-c++ .notranslate}
::: highlight
    TEST_F(FFT3DTest, RoundTrip_32x32x32) {
        FFTBuffer original(32, 32, 32), fft_result(32, 32, 32), recovered(32, 32, 32);

        GaussianGenerator generator(2.0);
        generator.generate(original.data(), 32, 32, 32);

        fft->compute(original.data(), fft_result.data(), FFT3d::FORWARD);
        fft->compute(fft_result.data(), recovered.data(), FFT3d::BACKWARD);

        RoundTripValidator validator(original.data(), recovered.data(), 32, 32, 32,
                                      scaled_tolerance(ROUNDTRIP_TOLERANCE, 32, 32, 32));
        EXPECT_TRUE(validator.validate());
    }
:::
::::

**Precision and Tolerances:**

FFT tests use precision-aware tolerances that automatically adjust based on floating-point precision ([`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`FFT_SINGLE=ON`{.docutils .literal .notranslate}]{.pre} vs [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`FFT_SINGLE=off`{.docutils .literal .notranslate}]{.pre}), grid size, and accelerator back end. Base tolerances ([`ROUNDTRIP_TOLERANCE`{.docutils .literal .notranslate}]{.pre}, [`PARSEVAL_TOLERANCE`{.docutils .literal .notranslate}]{.pre}, etc.) are defined in [`fft_test_helpers.h`{.docutils .literal .notranslate}]{.pre}. Use [`scaled_tolerance()`{.docutils .literal .notranslate}]{.pre} to adjust for grid size effects.
::::::::
:::::::::::::::

::::::: {#tests-for-individual-lammps-commands .section}
## [4.12.2. ]{.section-number}Tests for individual LAMMPS commands[](#tests-for-individual-lammps-commands "Link to this heading"){.headerlink}

The tests [`unittest/commands`{.docutils .literal .notranslate}]{.pre} are a bit more complex as they require to first create a [[`LAMMPS`{.xref .cpp .cpp-class .docutils .literal .notranslate}]{.pre}]Classes_lammps.md#_CPPv4N9LAMMPS_NS6LAMMPSE "LAMMPS_NS::LAMMPS"){.reference .internal} class instance and then use the [[C++ API]{.doc}]Cplusplus.md){.reference .internal} to pass individual commands to that LAMMPS instance. For that reason these tests use a GoogleTest "test fixture", i.e. a class derived from [`testing::Test`{.docutils .literal .notranslate}]{.pre} that will create (and delete) the required LAMMPS class instance for each set of tests in a [`TEST_F()`{.docutils .literal .notranslate}]{.pre} function. Please see the individual source files for different examples of setting up suitable test fixtures. Here is an example for implementing a test using a fixture by first checking the default value and then issuing LAMMPS commands and checking whether they have the desired effect:

:::: {.highlight-c++ .notranslate}
::: highlight
    TEST_F(SimpleCommandsTest, ResetTimestep)
    {
        ASSERT_EQ(lmp->update->ntimestep, 0);

        BEGIN_HIDE_OUTPUT();
        command("reset_timestep 10");
        END_HIDE_OUTPUT();
        ASSERT_EQ(lmp->update->ntimestep, 10);

        BEGIN_HIDE_OUTPUT();
        command("reset_timestep 0");
        END_HIDE_OUTPUT();
        ASSERT_EQ(lmp->update->ntimestep, 0);

        TEST_FAILURE(".*ERROR: Timestep must be >= 0.*", command("reset_timestep -10"););
        TEST_FAILURE(".*ERROR: Illegal reset_timestep .*", command("reset_timestep"););
        TEST_FAILURE(".*ERROR: Illegal reset_timestep .*", command("reset_timestep 10 10"););
        TEST_FAILURE(".*ERROR: Expected integer .*", command("reset_timestep xxx"););
    }
:::
::::

Please note the use of the [`BEGIN_HIDE_OUTPUT`{.docutils .literal .notranslate}]{.pre} and [`END_HIDE_OUTPUT`{.docutils .literal .notranslate}]{.pre} functions that will capture output from running LAMMPS. This is normally discarded but by setting the verbose flag (via setting the [`TEST_ARGS`{.docutils .literal .notranslate}]{.pre} environment variable, [`TEST_ARGS=-v`{.docutils .literal .notranslate}]{.pre}) it can be printed and used to understand why tests fail unexpectedly.

The specifics of so-called "death tests", i.e. conditions where LAMMPS should fail and throw an exception, are implemented in the [`TEST_FAILURE()`{.docutils .literal .notranslate}]{.pre} macro. These tests operate by capturing the screen output when executing the failing command and then comparing that with a provided regular expression string pattern. Example:

:::: {.highlight-c++ .notranslate}
::: highlight
    TEST_F(SimpleCommandsTest, UnknownCommand)
    {
        TEST_FAILURE(".*ERROR: Unknown command.*", lmp->input->one("XXX one two"););
    }
:::
::::

The following test programs are currently available:

  File name:                                                            Test name:       Description:
  --------------------------------------------------------------------- ---------------- ----------------------------------------------------------------------------------------------------------------------------------------------
  [`test_simple_commands.cpp`{.docutils .literal .notranslate}]{.pre}   SimpleCommands   Tests for LAMMPS commands that do not require a box
  [`test_lattice_region.cpp`{.docutils .literal .notranslate}]{.pre}    LatticeRegion    Tests to validate the [[lattice]{.doc}]lattice.md){.reference .internal} and [[region]{.doc}]region.md){.reference .internal} commands
  [`test_groups.cpp`{.docutils .literal .notranslate}]{.pre}            GroupTest        Tests to validate the [[group]{.doc}]group.md){.reference .internal} command
  [`test_variables.cpp`{.docutils .literal .notranslate}]{.pre}         VariableTest     Tests to validate the [[variable]{.doc}]variable.md){.reference .internal} command
  [`test_kim_commands.cpp`{.docutils .literal .notranslate}]{.pre}      KimCommands      Tests for several commands from the [[KIM package]{.std .std-ref}]Packages_details.md#pkg-kim){.reference .internal}
  [`test_reset_atoms.cpp`{.docutils .literal .notranslate}]{.pre}       ResetAtoms       Tests to validate the [[reset_atoms]{.doc}]reset_atoms.md){.reference .internal} sub-commands
:::::::

::::: {#tests-for-the-c-style-library-interface .section}
## [4.12.3. ]{.section-number}Tests for the C-style library interface[](#tests-for-the-c-style-library-interface "Link to this heading"){.headerlink}

Tests for validating the LAMMPS C-style library interface are in the [`unittest/c-library`{.docutils .literal .notranslate}]{.pre} folder. They text either utility functions or LAMMPS commands, but use the functions implemented in [`src/library.cpp`{.docutils .literal .notranslate}]{.pre} as much as possible. There may be some overlap with other tests as far as the LAMMPS functionality is concerned, but the focus is on testing the C-style library API. The tests are distributed over multiple test programs which try to match the grouping of the functions in the source code and [[in the manual]{.std .std-ref}]Library.md#lammps-c-api){.reference .internal}.

This group of tests also includes tests invoking LAMMPS in parallel through the library interface, provided that LAMMPS was compiled with MPI support. These include tests where LAMMPS is run in multi-partition mode or only on a subset of the MPI world communicator. The CMake script code for adding this kind of test looks like this:

:::: {.highlight-cmake .notranslate}
::: highlight
    if (BUILD_MPI)
      add_executable(test_library_mpi test_library_mpi.cpp)
      target_link_libraries(test_library_mpi PRIVATE lammps GTest::GTest GTest::GMock)
      target_compile_definitions(test_library_mpi PRIVATE ${TEST_CONFIG_DEFS})
      add_mpi_test(NAME LibraryMPI NUM_PROCS 4 COMMAND $<TARGET_FILE:test_library_mpi>)
    endif()
:::
::::

Note the custom function [`add_mpi_test()`{.docutils .literal .notranslate}]{.pre} which adapts how [`ctest`{.docutils .literal .notranslate}]{.pre} will execute the test so it is launched in parallel (with 4 MPI ranks).
:::::

::: {#tests-for-the-python-module-and-package .section}
## [4.12.4. ]{.section-number}Tests for the Python module and package[](#tests-for-the-python-module-and-package "Link to this heading"){.headerlink}

The [`unittest/python`{.docutils .literal .notranslate}]{.pre} folder contains primarily tests for classes and functions in the LAMMPS python module but also for commands in the PYTHON package. These tests are only enabled, if the necessary prerequisites are detected or enabled during configuration and compilation of LAMMPS (shared library build enabled, Python interpreter found, Python development files found).

The Python tests are implemented using the [`unittest`{.docutils .literal .notranslate}]{.pre} standard Python module and split into multiple files with similar categories as the tests for the C-style library interface.
:::

::: {#tests-for-the-fortran-interface .section}
## [4.12.5. ]{.section-number}Tests for the Fortran interface[](#tests-for-the-fortran-interface "Link to this heading"){.headerlink}

Tests for using the Fortran module are in the [`unittest/fortran`{.docutils .literal .notranslate}]{.pre} folder. Since they are also using the GoogleTest library, they require test wrappers written in C++ that will call fortran functions with a C function interface through ISO_C_BINDINGS which will in turn call the functions in the LAMMPS Fortran module.
:::

::: {#id1 .section}
## [4.12.6. ]{.section-number}Tests for the C++-style library interface[](#id1 "Link to this heading"){.headerlink}

The tests in the [`unittest/cplusplus`{.docutils .literal .notranslate}]{.pre} folder are somewhat similar to the tests for the C-style library interface, but do not need to test the convenience and utility functions that are only available through the C-style library interface. Instead they focus on the more generic features that are used in LAMMPS internally. This part of the unit tests is currently still mostly in the planning stage.
:::

::: {#tests-for-reading-and-writing-file-formats .section}
## [4.12.7. ]{.section-number}Tests for reading and writing file formats[](#tests-for-reading-and-writing-file-formats "Link to this heading"){.headerlink}

The [`unittest/formats`{.docutils .literal .notranslate}]{.pre} folder contains test programs for reading and writing files like data files, restart files, potential files or dump files. This covers simple things like the file i/o convenience functions in the [`utils::`{.docutils .literal .notranslate}]{.pre} namespace to complex tests of atom styles where creating and deleting of atoms with different properties is tested in different ways and through script commands or reading and writing of data or restart files.
:::

:::::::::::::::: {#tests-for-styles-computing-or-modifying-forces .section}
## [4.12.8. ]{.section-number}Tests for styles computing or modifying forces[](#tests-for-styles-computing-or-modifying-forces "Link to this heading"){.headerlink}

These are tests common configurations for pair styles, bond styles, angle styles, kspace styles and certain fix styles. Those are tests driven by some test executables build from sources in the [`unittest/force-styles`{.docutils .literal .notranslate}]{.pre} folder and use LAMMPS input template and data files as well as input files in YAML format from the [`unittest/force-styles/tests`{.docutils .literal .notranslate}]{.pre} folder. The YAML file names have to follow some naming conventions so they get associated with the test programs and categorized and listed with canonical names in the list of tests as displayed by [`ctest`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-N`{.docutils .literal .notranslate}]{.pre}. If you add a new YAML file, you need to re-run CMake to update the corresponding list of tests.

A minimal YAML file for a (molecular) pair style test will looks something like the following (see [`mol-pair-zero.yaml`{.docutils .literal .notranslate}]{.pre}):

:::: {.highlight-yaml .notranslate}
::: highlight
    ---
    lammps_version: 24 Aug 2020
    date_generated: Tue Sep 15 09:44:21 202
    epsilon: 1e-14
    prerequisites: ! |
      atom full
      pair zero
    pre_commands: ! ""
    post_commands: ! ""
    input_file: in.fourmol
    pair_style: zero 8.0
    pair_coeff: ! |
      * *
    extract: ! ""
    natoms: 29
    init_vdwl: 0
    init_coul: 0

    [...]
:::
::::

The following table describes the available keys and their purpose for testing pair styles:

  Key:             Description:
  ---------------- --------------------------------------------------------------------------------------------------------------
  lammps_version   LAMMPS version used to last update the reference data
  date_generated   date when the file was last updated
  epsilon          base value for the relative precision required for tests to pass
  prerequisites    list of style kind / style name pairs required to run the test
  pre_commands     LAMMPS commands to be executed before the input template file is read
  post_commands    LAMMPS commands to be executed right before the actual tests
  input_file       LAMMPS input file template based on pair style zero
  pair_style       arguments to the pair_style command to be tested
  pair_coeff       list of pair_coeff arguments to set parameters for the input template
  extract          list of keywords supported by [`Pair::extract()`{.docutils .literal .notranslate}]{.pre} and their dimension
  natoms           number of atoms in the input file template
  init_vdwl        non-Coulomb pair energy after "run 0"
  init_coul        Coulomb pair energy after "run 0"
  init_stress      stress tensor after "run 0"
  init_forces      forces on atoms after "run 0"
  run_vdwl         non-Coulomb pair energy after "run 4"
  run_coul         Coulomb pair energy after "run 4"
  run_stress       stress tensor after "run 4"
  run_forces       forces on atoms after "run 4"

The test program will read all this data from the YAML file and then create a LAMMPS instance, apply the settings/commands from the YAML file as needed and then issue a "run 0" command, write out a restart file, a data file and a coeff file. The actual test will then compare computed energies, stresses, and forces with the reference data, issue a "run 4" command and compare to the second set of reference data. This will be run with both the newton_pair setting enabled and disabled and is expected to generate the same results (allowing for some numerical noise). Then it will restart from the previously generated restart and compare with the reference and also start from the data file. A final check will use multi-cutoff r-RESPA (if supported by the pair style) at a 1:1 split and compare to the Verlet results. These sets of tests are run with multiple test fixtures for accelerated styles (OPT, OPENMP, INTEL, KOKKOS (OpenMP only)) and for the latter three with 4 OpenMP threads enabled. For these tests the relative error (epsilon) is lowered by a common factor due to the additional numerical noise, but the tests are still comparing to the same reference data.

Additional tests will check whether all listed extract keywords are supported and have the correct dimensionality and the final set of tests will set up a few pairs of atoms explicitly and in such a fashion that the forces on the atoms computed from [`Pair::compute()`{.docutils .literal .notranslate}]{.pre} will match individually with the results from [`Pair::single()`{.docutils .literal .notranslate}]{.pre}, if the pair style does support that functionality.

With this scheme a large fraction of the code of any tested pair style will be executed and consistent results are required for different settings and between different accelerated pair style variants and the base class, as well as for computing individual pairs through the [`Pair::single()`{.docutils .literal .notranslate}]{.pre} method where supported.

The [`test_pair_style`{.docutils .literal .notranslate}]{.pre} tester is used with 4 categories of test inputs:

- pair styles compatible with molecular systems using bonded interactions and exclusions. For pair styles requiring a KSpace style the KSpace computations are disabled. The YAML files match the pattern "mol-pair-\*.yaml" and the tests are correspondingly labeled with "MolPairStyle:\*"

- pair styles not compatible with the previous input template. The YAML files match the pattern "atomic-pair-\*.yaml" and the tests are correspondingly labeled with "AtomicPairStyle:\*"

- manybody pair styles. The YAML files match the pattern "atomic-pair-\*.yaml" and the tests are correspondingly labeled with "AtomicPairStyle:\*"

- kspace styles. The YAML files match the pattern "kspace-\*.yaml" and the tests are correspondingly labeled with "KSpaceStyle:\*". In these cases a compatible pair style is defined, but the computation of the pair style contributions is disabled.

The [`test_bond_style`{.docutils .literal .notranslate}]{.pre}, [`test_angle_style`{.docutils .literal .notranslate}]{.pre}, [`test_dihedral_style`{.docutils .literal .notranslate}]{.pre}, and [`test_improper_style`{.docutils .literal .notranslate}]{.pre} tester programs are set up in a similar fashion and share support functions with the pair style tester. The final group of tests in this section is for fix styles that add/manipulate forces and velocities, e.g. for time integration, thermostats and more.

Adding a new test is easiest done by copying and modifying an existing YAML file for a style that is similar to one to be tested. The file name should follow the naming conventions described above and after copying the file, the first step is to replace the style names where needed. The coefficient values do not have to be meaningful, just in a reasonable range for the given system. It does not matter if some forces are large, for as long as they do not diverge.

The template input files define a large number of index variables at the top that can be modified inside the YAML file to control the behavior. For example, if a pair style requires a "newton on" setting, the following can be used in as the "pre_commands" section:

:::: {.highlight-yaml .notranslate}
::: highlight
    pre_commands: ! |
      variable newton_pair delete
      variable newton_pair index on
:::
::::

And for a pair style requiring a kspace solver the following would be used as the "post_commands" section:

:::: {.highlight-yaml .notranslate}
::: highlight
    post_commands: ! |
      pair_modify table 0
      kspace_style pppm/tip4p 1.0e-6
      kspace_modify gewald 0.3
      kspace_modify compute no
:::
::::

Note that this disables computing the kspace contribution, but still will run the setup. The "gewald" parameter should be set explicitly to speed up the run. For styles with long-range electrostatics, typically two tests are added one using the (slower) analytic approximation of the erfc() function and the other using the tabulated coulomb, to test both code paths. The reference results in the YAML files then should be compared manually, if they agree well enough within the limits of those two approximations.

The [`test_pair_style`{.docutils .literal .notranslate}]{.pre} and equivalent programs have special command-line options to update the YAML files. Running a command like

:::: {.highlight-bash .notranslate}
::: highlight
    test_pair_style mol-pair-lennard_mdf.yaml -g new.yaml
:::
::::

will read the settings from the [`mol-pair-lennard_mdf.yaml`{.docutils .literal .notranslate}]{.pre} file and then compute the reference data and write a new file with to [`new.yaml`{.docutils .literal .notranslate}]{.pre}. If this step fails, there are likely some (LAMMPS or YAML) syntax issues in the YAML file that need to be resolved and then one can compare the two files to see if the output is as expected.

It is also possible to do an update in place with:

:::: {.highlight-bash .notranslate}
::: highlight
    test_pair_style mol-pair-lennard_mdf.yaml -u
:::
::::

And one can finally run the full set of tests with:

:::: {.highlight-bash .notranslate}
::: highlight
    test_pair_style mol-pair-lennard_mdf.yaml
:::
::::

This will just print a summary of the groups of tests. When using the "-v" flag the test will also keep any LAMMPS output and when using the "-s" flag, there will be some statistics reported on the relative errors for the individual checks which can help to figure out what would be a good choice of the epsilon parameter. It should be as small as possible to catch any unintended side effects from changes elsewhere, but large enough to accommodate the numerical noise due to the implementation of the potentials and differences in compilers.

::: {.admonition .note}
Note

These kinds of tests can be very sensitive to compiler optimization and thus the expectation is that they pass with compiler optimization turned off. When compiler optimization is enabled, there may be some failures, but one has to carefully check whether those are acceptable due to the enhanced numerical noise from reordering floating-point math operations or due to the compiler mis-compiling the code. That is not always obvious.
:::
::::::::::::::::

::: {#tests-for-programs-in-the-tools-folder .section}
## [4.12.9. ]{.section-number}Tests for programs in the tools folder[](#tests-for-programs-in-the-tools-folder "Link to this heading"){.headerlink}

The [`unittest/tools`{.docutils .literal .notranslate}]{.pre} folder contains tests for programs in the [`tools`{.docutils .literal .notranslate}]{.pre} folder. This currently only contains tests for the LAMMPS shell, which are implemented as a python scripts using the [`unittest`{.docutils .literal .notranslate}]{.pre} Python module and launching the tool commands through the [`subprocess`{.docutils .literal .notranslate}]{.pre} Python module.
:::

::::::::: {#troubleshooting-failed-unit-tests .section}
## [4.12.10. ]{.section-number}Troubleshooting failed unit tests[](#troubleshooting-failed-unit-tests "Link to this heading"){.headerlink}

There are by default no unit tests for newly added features (e.g. pair, fix, or compute styles) unless your pull request also includes tests for these added features. If you are modifying some existing LAMMPS features, you may see failures for existing tests, if your modifications have some unexpected side effects or your changes render the existing test invalid. If you are adding an accelerated version of an existing style, then only tests for INTEL, KOKKOS (with OpenMP only), OPENMP, and OPT will be run automatically. Tests for the GPU package are time consuming and thus are only run *after* a merge, or when a special label, [`gpu_unit_tests`{.docutils .literal .notranslate}]{.pre} is added to the pull request. After the test has started, it is often best to remove the label since every PR activity will re-trigger the test (that is a limitation of triggering a test with a label). Support for unit tests using KOKKOS with GPU acceleration is currently not supported.

When you see a failed build on GitHub, click on [`Details`{.docutils .literal .notranslate}]{.pre} to be taken to the corresponding LAMMPS Jenkins CI web page. Click on the "Exit" symbol near the [`Logout`{.docutils .literal .notranslate}]{.pre} button on the top right of that page to go to the "classic view". In the classic view, there is a list of the individual runs that make up this test run (they are shown but cannot be inspected in the default view). You can click on any of those. Clicking on [`Test`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Result`{.docutils .literal .notranslate}]{.pre} will display the list of failed tests. Click on the "Status" column to sort the tests based on their Failed or Passed status. Then click on the failed test to expand its output.

For example, the following output snippet shows the failed unit test

:::: {.highlight-console .notranslate}
::: highlight
    [ RUN      ] PairStyle.gpu
    /home/builder/workspace/dev/pull_requests/ubuntu_gpu/unit_tests/cmake_gpu_opencl_mixed_smallbig_clang_static/unittest/force-styles/test_main.cpp:63: Failure
    Expected: (err) <= (epsilon)
    Actual: 0.00018957912910606503 vs 0.0001
    Google Test trace:
    /home/builder/workspace/dev/pull_requests/ubuntu_gpu/unit_tests/cmake_gpu_opencl_mixed_smallbig_clang_static/unittest/force-styles/test_main.cpp:56: EXPECT_FORCES: init_forces (newton off)
    /home/builder/workspace/dev/pull_requests/ubuntu_gpu/unit_tests/cmake_gpu_opencl_mixed_smallbig_clang_static/unittest/force-styles/test_main.cpp:64: Failure
    Expected: (err) <= (epsilon)
    Actual: 0.00022892713393549854 vs 0.0001
:::
::::

The failed assertions provide line numbers in the test source (e.g. [`test_main.cpp:56`{.docutils .literal .notranslate}]{.pre}), from which one can understand what specific assertion failed.

Note that the force style engine runs one of a small number of systems in a rather off-equilibrium configuration with a few atoms for a few steps, writes data and restart files, uses [[the clear command]{.doc}]clear.md){.reference .internal} to reset LAMMPS, and then runs from those files with different settings (e.g. newton on/off) and integrators (e.g. verlet vs. respa). Beyond potential issues/bugs in the source code, the mismatch between the expected and actual values could be that force arrays are not properly cleared between multiple run commands or that class members are not correctly initialized or written to or read from a data or restart file.

While the epsilon (relative precision) for a single, [IEEE 754 compliant](https://en.wikipedia.org/wiki/IEEE_754){.reference .external}, double precision floating point operation is at about 2.2e-16, the achievable precision for the tests is lower due to most numbers being sums over intermediate results for which the non-associativity of floating point math leads to larger errors. As a rule of thumb, the test epsilon can often be in the range 5.0e-14 to 1.0e-13. But for "noisy" force kernels, e.g. those a larger amount of arithmetic operations involving exp(), log() or sin() functions, and also due to the effect of compiler optimization or differences between compilers or platforms, epsilon may need to be further relaxed, sometimes epsilon can be relaxed to 1.0e-12. If interpolation or lookup tables are used, epsilon may need to be set to 1.0e-10 or even higher. For tests of accelerated styles, the per-test epsilon is multiplied by empirical factors that take into account the differences in the order of floating point operations or that some or most intermediate operations may be done using approximations or with single precision floating point math.

To rerun a failed unit test individually, change to the [`build`{.docutils .literal .notranslate}]{.pre} directory and run the test with verbose output. For example,

:::: {.highlight-bash .notranslate}
::: highlight
    env TEST_ARGS=-v ctest -R ^MolPairStyle:lj_cut_coul_long -V
:::
::::

[`ctest`{.docutils .literal .notranslate}]{.pre} with the [`-V`{.docutils .literal .notranslate}]{.pre} flag also shows the exact command of the test. One can then use [`gdb`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`--args`{.docutils .literal .notranslate}]{.pre} to further debug and catch exceptions with the test command, for example,

:::: {.highlight-bash .notranslate}
::: highlight
    gdb --args /path/to/lammps/build/test_pair_style /path/to/lammps/unittest/force-styles/tests/mol-pair-lj_cut_coul_long.yaml
:::
::::

It is recommended to configure the build with [`-D`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`BUILD_SHARED_LIBS=on`{.docutils .literal .notranslate}]{.pre} and use a custom linker to shorten the build time during recompilation. Installing ccache in your development environment helps speed up recompilation by caching previous compilations and detecting when the same compilation is being done again. Please see [[Development build options]{.doc}]Build_development.md){.reference .internal} for further details.
:::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::

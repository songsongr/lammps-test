::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::: {#executing-commands .section}
# [1.1.2. ]{.section-number}Executing commands[](#executing-commands "Link to this heading"){.headerlink}

This section documents the following functions:

- [[`lammps_file()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv411lammps_filePvPKc "lammps_file"){.reference .internal}

- [[`lammps_command()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv414lammps_commandPvPKc "lammps_command"){.reference .internal}

- [[`lammps_commands_list()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv420lammps_commands_listPviPPKc "lammps_commands_list"){.reference .internal}

- [[`lammps_commands_string()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_commands_stringPvPKc "lammps_commands_string"){.reference .internal}

- [[`lammps_expand()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv413lammps_expandPvPKc "lammps_expand"){.reference .internal}

------------------------------------------------------------------------

Once a LAMMPS instance is created, there are multiple ways to "drive" a simulation. In most cases it is easiest to process single or multiple LAMMPS commands like in an input file. This can be done through reading a file or passing single commands or lists of commands or blocks of commands with the following functions.

Via these functions, the calling code can have LAMMPS act on a series of [[input file commands]{.doc}]Commands_all.md){.reference .internal} that are either read from a file or passed as strings. For example, this allows setup of a problem from an input script, and then running it in stages while performing other operations in between or concurrently. The caller can interleave the LAMMPS function calls with operations it performs, such as calls to extract information from or set information within LAMMPS, or calls to another code's library.

Just as with [[input script parsing]{.doc}]Commands_parse.md){.reference .internal} comments can be included in the file or strings, and expansion of variables with [`${name}`{.docutils .literal .notranslate}]{.pre} or [`$(expression)`{.docutils .literal .notranslate}]{.pre} syntax is performed. Below is a short example using some of these functions.

:::: {.highlight-c .notranslate}
::: highlight
    /* define to make the otherwise hidden prototype for "lammps_open()" visible */
    #define LAMMPS_LIB_MPI
    #include "library.h"

    #include <mpi.h>
    #include <stdio.h>

    int main(int argc, char **argv)
    {
      void *handle;
      int i;

      MPI_Init(&argc, &argv);
      handle = lammps_open(0, NULL, MPI_COMM_WORLD, NULL);
      lammps_file(handle,"in.sysinit");
      lammps_command(handle,"run 1000 post no");

      for (i=0; i < 100; ++i) {
        lammps_commands_string(handle,"run 100 pre no post no\n"
                                      "print 'PE = $(pe)'\n"
                                      "print 'KE = $(ke)'\n");
      }
      lammps_close(handle);
      MPI_Finalize();
      return 0;
    }
:::
::::

------------------------------------------------------------------------

[]{#_CPPv311lammps_filePvPKc}[]{#_CPPv211lammps_filePvPKc}[]{#lammps_file__voidP.cCP}[]{#library_8h_1a76c1ce1af98c09978578c7a94d778c0b .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_file]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[file]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv411lammps_filePvPKc "Link to this definition"){.headerlink}\

:   Process [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} input from a file.

    This function processes commands in the file pointed to by *filename* line by line and thus functions very similar to the [[include]{.doc}]include.md){.reference .internal} command. The function returns when the end of the file is reached and the commands have completed.

    The actual work is done by the functions [[`Input::file(const`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`char`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}` `{.xref .cpp .cpp-func .docutils .literal .notranslate}[`*)`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Classes_input.md#_CPPv4N9LAMMPS_NS5Input4fileEPKc "void LAMMPS_NS::Input::file(const char*)"){.reference .internal} and [[`Input::file()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Classes_input.md#_CPPv4N9LAMMPS_NS5Input4fileEv "void LAMMPS_NS::Input::file()"){.reference .internal}.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **filename** -- name of a file with [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} input

------------------------------------------------------------------------

[]{#_CPPv314lammps_commandPvPKc}[]{#_CPPv214lammps_commandPvPKc}[]{#lammps_command__voidP.cCP}[]{#library_8h_1a48721b1903a79541cb680dabea9b84d5 .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_command]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[cmd]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv414lammps_commandPvPKc "Link to this definition"){.headerlink}\

:   Process a single [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} input command from a string.

    This function tells LAMMPS to execute the single command in the string *cmd*. The entire string is considered as command and need not have a (final) newline character. Newline characters in the body of the string, however, will be treated as part of the command and will **not** start a second command. The function [[`lammps_commands_string()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_commands_stringPvPKc "lammps_commands_string"){.reference .internal} processes a string with multiple command-lines.

    The function returns the name of the command on success or [`NULL`{.docutils .literal .notranslate}]{.pre} when passing a string without a command.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **cmd** -- string with a single [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} command

    Returns[:]{.colon}

    :   string with parsed command name or [`NULL`{.docutils .literal .notranslate}]{.pre}

------------------------------------------------------------------------

[]{#_CPPv320lammps_commands_listPviPPKc}[]{#_CPPv220lammps_commands_listPviPPKc}[]{#lammps_commands_list__voidP.i.cCPP}[]{#library_8h_1ab542f51c42bcf8e39b64722ffa426890 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_commands_list]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[ncmd]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[cmds]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420lammps_commands_listPviPPKc "Link to this definition"){.headerlink}\

:   Process multiple [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} input commands from list of strings.

    This function processes multiple commands from a list of strings by first concatenating the individual strings in *cmds* into a single string, inserting newline characters as needed. The combined string is passed to [[`lammps_commands_string()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv422lammps_commands_stringPvPKc "lammps_commands_string"){.reference .internal} for processing.

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **ncmd** -- number of lines in *cmds*

        - **cmds** -- list of strings with [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} commands

------------------------------------------------------------------------

[]{#_CPPv322lammps_commands_stringPvPKc}[]{#_CPPv222lammps_commands_stringPvPKc}[]{#lammps_commands_string__voidP.cCP}[]{#library_8h_1a82b8d3fb9db7e0a834f6da0996e61d6b .target}[[void]{.pre}]{.kt}[ ]{.w}[[[lammps_commands_string]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[str]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422lammps_commands_stringPvPKc "Link to this definition"){.headerlink}\

:   Process a block of [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} input commands from a single string.

    This function processes a multi-line string similar to a block of commands from a file. The string may have multiple lines (separated by newline characters) and also single commands may be distributed over multiple lines with continuation characters ('&'). Those lines are combined by removing the '&' and the following newline character. After this processing the string is handed to LAMMPS for parsing and executing.

    ::: versionadded
    [Added in version 21Nov2023: ]{.versionmodified .added}The command is now able to process long strings with triple quotes and loops using [[jump SELF \<label\>]{.doc}]jump.md){.reference .internal}.
    :::

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **str** -- string with block of [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} input commands

------------------------------------------------------------------------

[]{#_CPPv313lammps_expandPvPKc}[]{#_CPPv213lammps_expandPvPKc}[]{#lammps_expand__voidP.cCP}[]{#library_8h_1aeff3ea554b2e172d2caa63304c222f8c .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[[lammps_expand]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[handle]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[line]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv413lammps_expandPvPKc "Link to this definition"){.headerlink}\

:   expand a single [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} input line from a string.

    This function tells LAMMPS to expand the string in *cmd* like it would process an input line fed to [[`lammps_command()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](#_CPPv414lammps_commandPvPKc "lammps_command"){.reference .internal} **without** executing it. The *entire* string is considered as input and need not have a (final) newline character. Newline characters in the body of the string, however, will be treated as part of the command and will **not** start a second command.

    The function returns the expanded string in a new string buffer that must be freed with [[`lammps_free()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_utility.md#_CPPv411lammps_freePv "lammps_free"){.reference .internal} after use to avoid a memory leak.

    *See also*

    :   [[`lammps_eval()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}]Library_objects.md#_CPPv411lammps_evalPvPKc "lammps_eval"){.reference .internal}

    Parameters[:]{.colon}

    :   - **handle** -- pointer to a previously created [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} instance

        - **line** -- string with a single [[LAMMPS]{.std .std-ref}]Classes_lammps.md#classLAMMPS__NS_1_1LAMMPS){.reference .internal} input line

    Returns[:]{.colon}

    :   string with expanded line
:::::
::::::
:::::::

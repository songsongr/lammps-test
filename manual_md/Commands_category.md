:::::::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

:::::::::::: {#commands-by-category .section}
# [6.4. ]{.section-number}Commands by category[](#commands-by-category "Link to this heading"){.headerlink}

This page lists most of the LAMMPS commands, grouped by category. The [[General commands]{.doc}]Commands_all.md){.reference .internal} page lists all general commands alphabetically. Style options for entries like fix, compute, pair etc. have their own pages where they are listed alphabetically.

::: {#initialization .section}
## [6.4.1. ]{.section-number}Initialization[](#initialization "Link to this heading"){.headerlink}

  ----------------------------------------------------- ------------------------------------------------------- ------------------------------------------------------------- ----------------------------------------------------- ---------------------------------------------------
  [[newton]{.doc}]newton.md){.reference .internal}   [[package]{.doc}]package.md){.reference .internal}   [[processors]{.doc}]processors.md){.reference .internal}   [[suffix]{.doc}]suffix.md){.reference .internal}   [[units]{.doc}]units.md){.reference .internal}
  ----------------------------------------------------- ------------------------------------------------------- ------------------------------------------------------------- ----------------------------------------------------- ---------------------------------------------------
:::

::: {#setup-simulation-box .section}
## [6.4.2. ]{.section-number}Setup simulation box[](#setup-simulation-box "Link to this heading"){.headerlink}

  --------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------------------------- -----------------------------------------------------------
  [[boundary]{.doc}]boundary.md){.reference .internal}   [[change_box]{.doc}]change_box.md){.reference .internal}   [[create_box]{.doc}]create_box.md){.reference .internal}   [[dimension]{.doc}]dimension.md){.reference .internal}
  [[lattice]{.doc}]lattice.md){.reference .internal}     [[region]{.doc}]region.md){.reference .internal}                                                                         
  --------------------------------------------------------- ------------------------------------------------------------- ------------------------------------------------------------- -----------------------------------------------------------
:::

::: {#setup-atoms .section}
## [6.4.3. ]{.section-number}Setup atoms[](#setup-atoms "Link to this heading"){.headerlink}

  ----------------------------------------------------------------- ----------------------------------------------------------------- ----------------------------------------------------------------- ---------------------------------------------------------------------
  [[atom_modify]{.doc}]atom_modify.md){.reference .internal}     [[atom_style]{.doc}]atom_style.md){.reference .internal}       [[balance]{.doc}]balance.md){.reference .internal}             [[create_atoms]{.doc}]create_atoms.md){.reference .internal}
  [[create_bonds]{.doc}]create_bonds.md){.reference .internal}   [[delete_atoms]{.doc}]delete_atoms.md){.reference .internal}   [[delete_bonds]{.doc}]delete_bonds.md){.reference .internal}   [[displace_atoms]{.doc}]displace_atoms.md){.reference .internal}
  [[group]{.doc}]group.md){.reference .internal}                 [[mass]{.doc}]mass.md){.reference .internal}                   [[molecule]{.doc}]molecule.md){.reference .internal}           [[read_data]{.doc}]read_data.md){.reference .internal}
  [[read_dump]{.doc}]read_dump.md){.reference .internal}         [[read_restart]{.doc}]read_restart.md){.reference .internal}   [[replicate]{.doc}]replicate.md){.reference .internal}         [[set]{.doc}]set.md){.reference .internal}
  [[velocity]{.doc}]velocity.md){.reference .internal}                                                                                                                                               
  ----------------------------------------------------------------- ----------------------------------------------------------------- ----------------------------------------------------------------- ---------------------------------------------------------------------
:::

::: {#force-fields .section}
## [6.4.4. ]{.section-number}Force fields[](#force-fields "Link to this heading"){.headerlink}

  --------------------------------------------------------------------- --------------------------------------------------------------------- --------------------------------------------------------------------- ---------------------------------------------------------------------
  [[angle_coeff]{.doc}]angle_coeff.md){.reference .internal}         [[angle_style]{.doc}]angle_style.md){.reference .internal}         [[bond_coeff]{.doc}]bond_coeff.md){.reference .internal}           [[bond_style]{.doc}]bond_style.md){.reference .internal}
  [[bond_write]{.doc}]bond_write.md){.reference .internal}           [[dielectric]{.doc}]dielectric.md){.reference .internal}           [[dihedral_coeff]{.doc}]dihedral_coeff.md){.reference .internal}   [[dihedral_style]{.doc}]dihedral_style.md){.reference .internal}
  [[improper_coeff]{.doc}]improper_coeff.md){.reference .internal}   [[improper_style]{.doc}]improper_style.md){.reference .internal}   [[kspace_modify]{.doc}]kspace_modify.md){.reference .internal}     [[kspace_style]{.doc}]kspace_style.md){.reference .internal}
  [[pair_coeff]{.doc}]pair_coeff.md){.reference .internal}           [[pair_modify]{.doc}]pair_modify.md){.reference .internal}         [[pair_style]{.doc}]pair_style.md){.reference .internal}           [[pair_write]{.doc}]pair_write.md){.reference .internal}
  [[special_bonds]{.doc}]special_bonds.md){.reference .internal}                                                                                                                                                 
  --------------------------------------------------------------------- --------------------------------------------------------------------- --------------------------------------------------------------------- ---------------------------------------------------------------------
:::

::: {#settings .section}
## [6.4.5. ]{.section-number}Settings[](#settings "Link to this heading"){.headerlink}

  --------------------------------------------------------------------- ----------------------------------------------------------------- --------------------------------------------------------- -------------------------------------------------------------
  [[comm_modify]{.doc}]comm_modify.md){.reference .internal}         [[comm_style]{.doc}]comm_style.md){.reference .internal}       [[info]{.doc}]info.md){.reference .internal}           [[min_modify]{.doc}]min_modify.md){.reference .internal}
  [[min_style]{.doc}]min_style.md){.reference .internal}             [[neigh_modify]{.doc}]neigh_modify.md){.reference .internal}   [[neighbor]{.doc}]neighbor.md){.reference .internal}   [[partition]{.doc}]partition.md){.reference .internal}
  [[reset_timestep]{.doc}]reset_timestep.md){.reference .internal}   [[run_style]{.doc}]run_style.md){.reference .internal}         [[timer]{.doc}]timer.md){.reference .internal}         [[timestep]{.doc}]timestep.md){.reference .internal}
  --------------------------------------------------------------------- ----------------------------------------------------------------- --------------------------------------------------------- -------------------------------------------------------------
:::

::: {#operations-within-timestepping-fixes-and-diagnostics-computes .section}
## [6.4.6. ]{.section-number}Operations within timestepping (fixes) and diagnostics (computes)[](#operations-within-timestepping-fixes-and-diagnostics-computes "Link to this heading"){.headerlink}

  ----------------------------------------------------------- --------------------------------------------------------------------- ----------------------------------------------- -------------------------------------------------------------
  [[compute]{.doc}]compute.md){.reference .internal}       [[compute_modify]{.doc}]compute_modify.md){.reference .internal}   [[fix]{.doc}]fix.md){.reference .internal}   [[fix_modify]{.doc}]fix_modify.md){.reference .internal}
  [[uncompute]{.doc}]uncompute.md){.reference .internal}   [[unfix]{.doc}]unfix.md){.reference .internal}                                                                     
  ----------------------------------------------------------- --------------------------------------------------------------------- ----------------------------------------------- -------------------------------------------------------------
:::

::: {#output .section}
## [6.4.7. ]{.section-number}Output[](#output "Link to this heading"){.headerlink}

  ------------------------------------------------------------------- --------------------------------------------------------------- ------------------------------------------------------------------- -----------------------------------------------------------------
  [[dump image]{.doc}]dump_image.md){.reference .internal}         [[dump movie]{.doc}]dump_image.md){.reference .internal}     [[dump]{.doc}]dump.md){.reference .internal}                     [[dump_modify]{.doc}]dump_modify.md){.reference .internal}
  [[restart]{.doc}]restart.md){.reference .internal}               [[thermo]{.doc}]thermo.md){.reference .internal}             [[thermo_modify]{.doc}]thermo_modify.md){.reference .internal}   [[thermo_style]{.doc}]thermo_style.md){.reference .internal}
  [[undump]{.doc}]undump.md){.reference .internal}                 [[write_coeff]{.doc}]write_coeff.md){.reference .internal}   [[write_data]{.doc}]write_data.md){.reference .internal}         [[write_dump]{.doc}]write_dump.md){.reference .internal}
  [[write_restart]{.doc}]write_restart.md){.reference .internal}                                                                                                                                       
  ------------------------------------------------------------------- --------------------------------------------------------------- ------------------------------------------------------------------- -----------------------------------------------------------------
:::

::: {#actions .section}
## [6.4.8. ]{.section-number}Actions[](#actions "Link to this heading"){.headerlink}

  --------------------------------------------------------- ----------------------------------------------------- --------------------------------------------------------- ----------------------------------------------- --------------------------------------------------- -----------------------------------------------
  [[minimize]{.doc}]minimize.md){.reference .internal}   [[neb]{.doc}]neb.md){.reference .internal}         [[neb_spin]{.doc}]neb_spin.md){.reference .internal}   [[prd]{.doc}]prd.md){.reference .internal}   [[rerun]{.doc}]rerun.md){.reference .internal}   [[run]{.doc}]run.md){.reference .internal}
  [[tad]{.doc}]tad.md){.reference .internal}             [[temper]{.doc}]temper.md){.reference .internal}                                                                                                                                                                 
  --------------------------------------------------------- ----------------------------------------------------- --------------------------------------------------------- ----------------------------------------------- --------------------------------------------------- -----------------------------------------------
:::

::: {#input-script-control .section}
## [6.4.9. ]{.section-number}Input script control[](#input-script-control "Link to this heading"){.headerlink}

  --------------------------------------------------- ------------------------------------------------- --------------------------------------------------- ------------------------------------------------------- ------------------------------------------------- --------------------------------------------------- ---------------------------------------------------------
  [[clear]{.doc}]clear.md){.reference .internal}   [[echo]{.doc}]echo.md){.reference .internal}   [[if]{.doc}]if.md){.reference .internal}         [[include]{.doc}]include.md){.reference .internal}   [[info]{.doc}]info.md){.reference .internal}   [[jump]{.doc}]jump.md){.reference .internal}     [[label]{.doc}]label.md){.reference .internal}
  [[log]{.doc}]log.md){.reference .internal}       [[next]{.doc}]next.md){.reference .internal}   [[print]{.doc}]print.md){.reference .internal}   [[python]{.doc}]python.md){.reference .internal}     [[quit]{.doc}]quit.md){.reference .internal}   [[shell]{.doc}]shell.md){.reference .internal}   [[variable]{.doc}]variable.md){.reference .internal}
  --------------------------------------------------- ------------------------------------------------- --------------------------------------------------- ------------------------------------------------------- ------------------------------------------------- --------------------------------------------------- ---------------------------------------------------------
:::
::::::::::::
:::::::::::::
::::::::::::::

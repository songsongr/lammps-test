:::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#bond-styles .section}
[]{#bond}

# [6.9. ]{.section-number}Bond styles[](#bond-styles "Link to this heading"){.headerlink}

All LAMMPS [[bond_style]{.doc}]bond_style.md){.reference .internal} commands. Some styles have accelerated versions. This is indicated by additional letters in parenthesis: g = GPU, i = INTEL, k = KOKKOS, o = OPENMP, t = OPT.

  -------------------------------------------------------------------------------- ------------------------------------------------------------------------------ -------------------------------------------------------------------------------------- --------------------------------------------------------------- --------------------------------------------------------------------
  [[none]{.doc}]bond_none.md){.reference .internal}                             [[zero]{.doc}]bond_zero.md){.reference .internal}                           [[hybrid (k)]{.doc}]bond_hybrid.md){.reference .internal}                                                                                           
                                                                                                                                                                                                                                                                                                                         
  [[bpm/rotational]{.doc}]bond_bpm_rotational.md){.reference .internal}         [[bpm/spring]{.doc}]bond_bpm_spring.md){.reference .internal}               [[bpm/spring/plastic]{.doc}]bond_bpm_spring_plastic.md){.reference .internal}       [[class2 (ko)]{.doc}]bond_class2.md){.reference .internal}   [[fene (iko)]{.doc}]bond_fene.md){.reference .internal}
  [[fene/expand (o)]{.doc}]bond_fene_expand.md){.reference .internal}           [[fene/nm]{.doc}]bond_fene.md){.reference .internal}                        [[gaussian]{.doc}]bond_gaussian.md){.reference .internal}                           [[gromos (o)]{.doc}]bond_gromos.md){.reference .internal}    [[harmonic (iko)]{.doc}]bond_harmonic.md){.reference .internal}
  [[harmonic/restrain]{.doc}]bond_harmonic_restrain.md){.reference .internal}   [[harmonic/shift (o)]{.doc}]bond_harmonic_shift.md){.reference .internal}   [[harmonic/shift/cut (o)]{.doc}]bond_harmonic_shift_cut.md){.reference .internal}   [[lepton (o)]{.doc}]bond_lepton.md){.reference .internal}    [[mesocnt]{.doc}]bond_mesocnt.md){.reference .internal}
  [[mm3]{.doc}]bond_mm3.md){.reference .internal}                               [[morse (o)]{.doc}]bond_morse.md){.reference .internal}                     [[nonlinear (o)]{.doc}]bond_nonlinear.md){.reference .internal}                     [[oxdna/fene]{.doc}]bond_oxdna.md){.reference .internal}     [[oxdna2/fene]{.doc}]bond_oxdna.md){.reference .internal}
  [[oxrna2/fene]{.doc}]bond_oxdna.md){.reference .internal}                     [[quartic (o)]{.doc}]bond_quartic.md){.reference .internal}                 [[rheo/shell]{.doc}]bond_rheo_shell.md){.reference .internal}                       [[special]{.doc}]bond_special.md){.reference .internal}      [[table (o)]{.doc}]bond_table.md){.reference .internal}
  -------------------------------------------------------------------------------- ------------------------------------------------------------------------------ -------------------------------------------------------------------------------------- --------------------------------------------------------------- --------------------------------------------------------------------
:::

::: {#angle-styles .section}
[]{#angle}

# [6.10. ]{.section-number}Angle styles[](#angle-styles "Link to this heading"){.headerlink}

All LAMMPS [[angle_style]{.doc}]angle_style.md){.reference .internal} commands. Some styles have accelerated versions. This is indicated by additional letters in parenthesis: g = GPU, i = INTEL, k = KOKKOS, o = OPENMP, t = OPT.

  ----------------------------------------------------------------------------------- ------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------------------------------------------------------------
  [[none]{.doc}]angle_none.md){.reference .internal}                               [[zero]{.doc}]angle_zero.md){.reference .internal}                           [[hybrid (k)]{.doc}]angle_hybrid.md){.reference .internal}                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                              
  [[amoeba]{.doc}]angle_amoeba.md){.reference .internal}                           [[charmm (iko)]{.doc}]angle_charmm.md){.reference .internal}                 [[class2 (ko)]{.doc}]angle_class2.md){.reference .internal}                                        [[class2/p6]{.doc}]angle_class2.md){.reference .internal}                      [[class2xe]{.doc}]angle_class2.md){.reference .internal}
  [[cosine (ko)]{.doc}]angle_cosine.md){.reference .internal}                      [[cosine/buck6d]{.doc}]angle_cosine_buck6d.md){.reference .internal}         [[cosine/delta (o)]{.doc}]angle_cosine_delta.md){.reference .internal}                             [[cosine/periodic (o)]{.doc}]angle_cosine_periodic.md){.reference .internal}   [[cosine/shift (o)]{.doc}]angle_cosine_shift.md){.reference .internal}
  [[cosine/shift/exp (o)]{.doc}]angle_cosine_shift_exp.md){.reference .internal}   [[cosine/squared (o)]{.doc}]angle_cosine_squared.md){.reference .internal}   [[cosine/squared/restricted (o)]{.doc}]angle_cosine_squared_restricted.md){.reference .internal}   [[cross]{.doc}]angle_cross.md){.reference .internal}                           [[dipole (o)]{.doc}]angle_dipole.md){.reference .internal}
  [[fourier (o)]{.doc}]angle_fourier.md){.reference .internal}                     [[fourier/simple (o)]{.doc}]angle_fourier_simple.md){.reference .internal}   [[gaussian]{.doc}]angle_gaussian.md){.reference .internal}                                         [[harmonic (iko)]{.doc}]angle_harmonic.md){.reference .internal}               [[lepton (o)]{.doc}]angle_lepton.md){.reference .internal}
  [[mesocnt]{.doc}]angle_mesocnt.md){.reference .internal}                         [[mm3]{.doc}]angle_mm3.md){.reference .internal}                             [[mwlc]{.doc}]angle_mwlc.md){.reference .internal}                                                 [[quartic (o)]{.doc}]angle_quartic.md){.reference .internal}                   [[spica (ko)]{.doc}]angle_spica.md){.reference .internal}
  [[table (o)]{.doc}]angle_table.md){.reference .internal}                                                                                                                                                                                                                                                                                                 
  ----------------------------------------------------------------------------------- ------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------------------------------------------------------------
:::

::: {#dihedral-styles .section}
[]{#dihedral}

# [6.11. ]{.section-number}Dihedral styles[](#dihedral-styles "Link to this heading"){.headerlink}

All LAMMPS [[dihedral_style]{.doc}]dihedral_style.md){.reference .internal} commands. Some styles have accelerated versions. This is indicated by additional letters in parenthesis: g = GPU, i = INTEL, k = KOKKOS, o = OPENMP, t = OPT.

  ---------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------- ------------------------------------------------------------------------ ------------------------------------------------------------------------ --------------------------------------------------------------------------------------
  [[none]{.doc}]dihedral_none.md){.reference .internal}                                             [[zero]{.doc}]dihedral_zero.md){.reference .internal}                  [[hybrid (k)]{.doc}]dihedral_hybrid.md){.reference .internal}                                                                                  
                                                                                                                                                                                                                                                                                                                                   
  [[charmm (iko)]{.doc}]dihedral_charmm.md){.reference .internal}                                   [[charmmfsw (k)]{.doc}]dihedral_charmm.md){.reference .internal}       [[class2 (ko)]{.doc}]dihedral_class2.md){.reference .internal}        [[class2xe]{.doc}]dihedral_class2.md){.reference .internal}           [[cosine/shift/exp (o)]{.doc}]dihedral_cosine_shift_exp.md){.reference .internal}
  [[cosine/squared/restricted]{.doc}]dihedral_cosine_squared_restricted.md){.reference .internal}   [[fourier (iko)]{.doc}]dihedral_fourier.md){.reference .internal}      [[harmonic (iko)]{.doc}]dihedral_harmonic.md){.reference .internal}   [[helix (o)]{.doc}]dihedral_helix.md){.reference .internal}           [[lepton (o)]{.doc}]dihedral_lepton.md){.reference .internal}
  [[multi/harmonic (ko)]{.doc}]dihedral_multi_harmonic.md){.reference .internal}                    [[nharmonic (ko)]{.doc}]dihedral_nharmonic.md){.reference .internal}   [[opls (iko)]{.doc}]dihedral_opls.md){.reference .internal}           [[quadratic (o)]{.doc}]dihedral_quadratic.md){.reference .internal}   [[spherical]{.doc}]dihedral_spherical.md){.reference .internal}
  [[table (o)]{.doc}]dihedral_table.md){.reference .internal}                                       [[table/cut]{.doc}]dihedral_table.md){.reference .internal}                                                                                                                                                              
  ---------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------- ------------------------------------------------------------------------ ------------------------------------------------------------------------ --------------------------------------------------------------------------------------
:::

::: {#improper-styles .section}
[]{#improper}

# [6.12. ]{.section-number}Improper styles[](#improper-styles "Link to this heading"){.headerlink}

All LAMMPS [[improper_style]{.doc}]improper_style.md){.reference .internal} commands. Some styles have accelerated versions. This is indicated by additional letters in parenthesis: g = GPU, i = INTEL, k = KOKKOS, o = OPENMP, t = OPT.

  ---------------------------------------------------------------------- ---------------------------------------------------------------------- ------------------------------------------------------------------------ -------------------------------------------------------------------------------------- ------------------------------------------------------------------
  [[none]{.doc}]improper_none.md){.reference .internal}               [[zero]{.doc}]improper_zero.md){.reference .internal}               [[hybrid (k)]{.doc}]improper_hybrid.md){.reference .internal}                                                                                                
                                                                                                                                                                                                                                                                                                                
  [[amoeba]{.doc}]improper_amoeba.md){.reference .internal}           [[class2 (ko)]{.doc}]improper_class2.md){.reference .internal}      [[cossq (o)]{.doc}]improper_cossq.md){.reference .internal}           [[cvff (iko)]{.doc}]improper_cvff.md){.reference .internal}                         [[distance]{.doc}]improper_distance.md){.reference .internal}
  [[distharm]{.doc}]improper_distharm.md){.reference .internal}       [[fourier (o)]{.doc}]improper_fourier.md){.reference .internal}     [[harmonic (iko)]{.doc}]improper_harmonic.md){.reference .internal}   [[inversion/harmonic]{.doc}]improper_inversion_harmonic.md){.reference .internal}   [[ring (o)]{.doc}]improper_ring.md){.reference .internal}
  [[sqdistharm]{.doc}]improper_sqdistharm.md){.reference .internal}   [[umbrella (o)]{.doc}]improper_umbrella.md){.reference .internal}                                                                                                                                                                   
  ---------------------------------------------------------------------- ---------------------------------------------------------------------- ------------------------------------------------------------------------ -------------------------------------------------------------------------------------- ------------------------------------------------------------------
:::
:::::::
::::::::

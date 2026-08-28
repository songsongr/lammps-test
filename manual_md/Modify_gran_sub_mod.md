::::::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::::::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::::::: {#granular-sub-model-styles .section}
# [3.16. ]{.section-number}Granular Sub-Model styles[](#granular-sub-model-styles "Link to this heading"){.headerlink}

In granular models, particles are spheres with a finite radius and rotational degrees of freedom as further described in the [[Howto granular page]{.doc}]Howto_granular.md){.reference .internal}. Interactions between pair of particles or particles and walls may therefore depend on many different modes of motion as described in [[pair granular]{.doc}]pair_granular.md){.reference .internal} and [[fix wall/gran]{.doc}]fix_wall_gran.md){.reference .internal}. In both cases, the exchange of forces, torques, and heat flow between two types of bodies is defined using a GranularModel class. The GranularModel class organizes the details of an interaction using a series of granular sub-models each of which describe a particular interaction mode (e.g. normal forces or rolling friction). From a parent GranSubMod class, several types of sub-model classes are derived:

- GranSubModNormal: normal force sub-model

- GranSubModDamping: normal damping sub-model

- GranSubModTangential: tangential forces and sliding friction sub-model

- GranSubModRolling: rolling friction sub-model

- GranSubModTwisting: twisting friction sub-model

- GranSubModHeat: heat conduction sub-model

For each type of sub-model, more classes are further derived, each describing a specific implementation. For instance, from the GranSubModNormal class the GranSubModNormalHooke, GranSubModNormalHertz, and GranSubModNormalJKR classes are derived which calculate Hookean, Hertzian, or JKR normal forces, respectively. This modular structure simplifies the addition of new granular contact models as one only needs to create a new GranSubMod class without having to modify the more complex PairGranular, FixGranWall, and GranularModel classes. Most GranSubMod methods are also already defined by the parent classes so new contact models typically only require edits to a few relevant methods (e.g. methods that define coefficients and calculate forces).

Each GranSubMod class has a pointer to both the LAMMPS class and the GranularModel class which owns it, [`lmp`{.docutils .literal .notranslate}]{.pre} and [`gm`{.docutils .literal .notranslate}]{.pre}, respectively. The GranularModel class includes several public variables that describe the geometry/dynamics of the contact such as

+---------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [`xi`{.docutils .literal .notranslate}]{.pre} and [`xj`{.docutils .literal .notranslate}]{.pre}                                                   | Positions of the two contacting bodies                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [`vi`{.docutils .literal .notranslate}]{.pre} and [`vj`{.docutils .literal .notranslate}]{.pre}                                                   | Velocities of the two contacting bodies                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [`omegai`{.docutils .literal .notranslate}]{.pre} and [`omegaj`{.docutils .literal .notranslate}]{.pre}                                           | Angular velocities of the two contacting bodies                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [`dx`{.docutils .literal .notranslate}]{.pre} and [`nx`{.docutils .literal .notranslate}]{.pre}                                                   | The displacement and normalized displacement vectors                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [`r`{.docutils .literal .notranslate}]{.pre}, [`rsq`{.docutils .literal .notranslate}]{.pre}, and [`rinv`{.docutils .literal .notranslate}]{.pre} | The distance, distance squared, and inverse distance                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [`radsum`{.docutils .literal .notranslate}]{.pre}                                                                                                 | The sum of particle radii                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [`vr`{.docutils .literal .notranslate}]{.pre}, [`vn`{.docutils .literal .notranslate}]{.pre}, and [`vt`{.docutils .literal .notranslate}]{.pre}   | The relative velocity vector and its normal and tangential components |
+---------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| [`wr`{.docutils .literal .notranslate}]{.pre}                                                                                                     | The relative rotational velocity                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

These quantities, among others, are calculated in the [`GranularModel->check_contact()`{.docutils .literal .notranslate}]{.pre} and [`GranularModel->calculate_forces()`{.docutils .literal .notranslate}]{.pre} methods which can be referred to for more details.

To create a new GranSubMod class, it is recommended that one first looks at similar GranSubMod classes. All GranSubMod classes share several general methods which may need to be defined

+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`mix_coeff()`{.docutils .literal .notranslate}]{.pre}       | Optional method to define how coefficients are mixed for different atom types. By default, coefficients are mixed using a geometric mean.                                                       |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`coeffs_to_local()`{.docutils .literal .notranslate}]{.pre} | Parses coefficients to define local variables. Run once at model construction.                                                                                                                  |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`init()`{.docutils .literal .notranslate}]{.pre}            | Optional method to define local variables after other GranSubMod types were created. For instance, this method may be used by a tangential model that derives parameters from the normal model. |
+--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The Normal, Damping, Tangential, Twisting, and Rolling sub-models also have a [`calculate_forces()`{.docutils .literal .notranslate}]{.pre} method which calculate the respective forces/torques. Correspondingly, the Heat sub-model has a [`calculate_heat()`{.docutils .literal .notranslate}]{.pre} method. Lastly, the Normal sub-model has a few extra optional methods:

+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`touch()`{.docutils .literal .notranslate}]{.pre}            | Tests whether particles are in contact. By default, when particles overlap.                                                                                              |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`pulloff_distance()`{.docutils .literal .notranslate}]{.pre} | Returns the distance at which particles stop interacting. By default, when particles no longer overlap.                                                                  |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`calculate_radius()`{.docutils .literal .notranslate}]{.pre} | Returns the radius of the contact. By default, the radius of the geometric cross section.                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [`set_fncrit()`{.docutils .literal .notranslate}]{.pre}       | Defines the critical force to break the contact used by some tangential, rolling, and twisting sub-models. By default, the current total normal force including damping. |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

As an example, say one wanted to create a new normal force option that consisted of a Hookean force with a piecewise stiffness. This could be done by adding a new set of files [`gran_sub_mod_custom.h`{.docutils .literal .notranslate}]{.pre}:

:::: {.highlight-c++ .notranslate}
::: highlight
    #ifdef GRAN_SUB_MOD_CLASS
    // clang-format off
    GranSubModStyle(hooke/piecewise,GranSubModNormalHookePiecewise,NORMAL);
    // clang-format on
    #else

    #ifndef GRAN_SUB_MOD_CUSTOM_H
    #define GRAN_SUB_MOD_CUSTOM_H

    #include "gran_sub_mod.h"
    #include "gran_sub_mod_normal.h"

    namespace LAMMPS_NS {
    namespace Granular_NS {
      class GranSubModNormalHookePiecewise : public GranSubModNormal {
       public:
        GranSubModNormalHookePiecewise(class GranularModel *, class LAMMPS *);
        void coeffs_to_local() override;
        double calculate_forces() override;
       protected:
        double k1, k2, delta_switch;
      };
    }    // namespace Granular_NS
    }    // namespace LAMMPS_NS

    #endif /*GRAN_SUB_MOD_CUSTOM_H */
    #endif /*GRAN_SUB_MOD_CLASS_H */
:::
::::

and [`gran_sub_mod_custom.cpp`{.docutils .literal .notranslate}]{.pre}

:::: {.highlight-c++ .notranslate}
::: highlight
    #include "gran_sub_mod_custom.h"
    #include "gran_sub_mod_normal.h"
    #include "granular_model.h"

    using namespace LAMMPS_NS;
    using namespace Granular_NS;

    GranSubModNormalHookePiecewise::GranSubModNormalHookePiecewise(GranularModel *gm, LAMMPS *lmp) :
        GranSubModNormal(gm, lmp)
    {
      num_coeffs = 4;
    }

    /* ---------------------------------------------------------------------- */

    void GranSubModNormalHookePiecewise::coeffs_to_local()
    {
      k1 = coeffs[0];
      k2 = coeffs[1];
      damp = coeffs[2];
      delta_switch = coeffs[3];
    }

    /* ---------------------------------------------------------------------- */

    double GranSubModNormalHookePiecewise::calculate_forces()
    {
      double Fne;
      if (gm->delta >= delta_switch) {
        Fne = k1 * delta_switch + k2 * (gm->delta - delta_switch);
      } else {
        Fne = k1 * gm->delta;
      }
      return Fne;
    }
:::
::::
:::::::
::::::::
:::::::::

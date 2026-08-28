::::: {.document role="main" itemscope="itemscope" itemtype="https://schema.org/Article"}
:::: {itemprop="articleBody"}
[\\(\\renewcommand{\\AA}{\\text{Å}}\\)]{.math .notranslate .nohighlight}

::: {#atom-styles .section}
# [3.5. ]{.section-number}Atom styles[](#atom-styles "Link to this heading"){.headerlink}

Classes that define an [[atom style]{.doc}]atom_style.md){.reference .internal} are derived from the AtomVec class and managed by the Atom class. The atom style determines what attributes are associated with an atom and communicated when it is a ghost atom or migrates to a new processor. A new atom style can be created if one of the existing atom styles does not define all the attributes you need to store and communicate with atoms.

The file [`atom_vec_atomic.cpp`{.docutils .literal .notranslate}]{.pre} is the simplest example of an atom style. Examining the code for others will make these instructions more clear.

Note that the [[atom style hybrid]{.doc}]atom_style.md){.reference .internal} command can be used to define atoms or particles which have the union of properties of individual styles. Also the [[fix property/atom]{.doc}]fix_property_atom.md){.reference .internal} command can be used to add a single property (e.g. charge or a molecule ID) to a style that does not have it. It can also be used to add custom properties to an atom, with options to communicate them with ghost atoms or read them from a data file. Other LAMMPS commands can access these custom properties, as can new pair, fix, compute styles that are written to work with these properties. For example, the [[set]{.doc}]set.md){.reference .internal} command can be used to set the values of custom per-atom properties from an input script. All of these methods are less work than writing and testing(!) code for a new atom style.

If you follow these directions your new style will automatically work in tandem with others via the [[atom_style hybrid]{.doc}]atom_style.md){.reference .internal} command.

The first step is to define a set of string lists in the constructor of the new derived class. Each list will have zero or more comma-separated strings that correspond to the variable names used in the [`atom.h`{.docutils .literal .notranslate}]{.pre} header file for per-atom properties. Note that some represent per-atom vectors (q, molecule) while other are per-atom arrays (x,v). For all but the last two lists you do not need to specify any of (id,type,x,v,f). Those are included automatically as needed in the other lists.

  ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------
  fields_grow         full list of properties which is allocated and stored
  fields_copy         list of properties to copy atoms are rearranged on-processor
  fields_comm         list of properties communicated to ghost atoms every step
  fields_comm_vel     additional properties communicated if [[comm_modify vel]{.doc}]comm_modify.md){.reference .internal} is used
  fields_reverse      list of properties summed from ghost atoms every step
  fields_border       list of properties communicated with ghost atoms every reneighboring step
  fields_border_vel   additional properties communicated if [[comm_modify vel]{.doc}]comm_modify.md){.reference .internal} is used
  fields_exchange     list of properties communicated when an atom migrates to another processor
  fields_restart      list of properties written/read to/from a restart file
  fields_create       list of properties defined when an atom is created by [[create_atoms]{.doc}]create_atoms.md){.reference .internal}
  fields_data_atom    list of properties (in order) in the Atoms section of a data file, as read by [[read_data]{.doc}]read_data.md){.reference .internal}
  fields_data_vel     list of properties (in order) in the Velocities section of a data file, as read by [[read_data]{.doc}]read_data.md){.reference .internal}
  ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------

In these lists you can list variable names which LAMMPS already defines (in some other atom style), or you can create new variable names. You should not re-use a LAMMPS variable in your atom style that is used for something with a different meaning in another atom style. If the meaning is related, but interpreted differently by your atom style, then using the same variable name means a user must not use your style and the other style together in a [[atom_style hybrid]{.doc}]atom_style.md){.reference .internal} command. Because there will only be one value of the variable and different parts of LAMMPS will then likely use it differently. LAMMPS has no way of checking for this.

If you are defining new variable names then make them descriptive and unique to your new atom style. For example choosing "e" for energy is a bad choice; it is too generic. A better choice would be "e_foo", where "foo" is specific to your style.

If any of the variable names in your new atom style do not exist in LAMMPS, you need to add them to the src/atom.h and atom.cpp files.

Search for the word "customize" or "customization" in these 2 files to see where to add your variable. Adding a flag to the 2nd customization section in [`atom.h`{.docutils .literal .notranslate}]{.pre} is only necessary if your code (e.g. a pair style) needs to check that a per-atom property is defined. These flags should also be set in the constructor of the atom style child class.

In [`atom.cpp`{.docutils .literal .notranslate}]{.pre}, aside from the constructor and destructor, there are 3 methods that a new variable name or flag needs to be added to.

In [`Atom::peratom_create()`{.docutils .literal .notranslate}]{.pre} when using the [`Atom::add_peratom()`{.docutils .literal .notranslate}]{.pre} method, a cols argument of 0 is for per-atom vectors, a length \> 1 is for per-atom arrays. Note the use of the extra per-thread flag and the add_peratom_vary() method when the last dimension of the array is variable-length.

Adding the variable name to Atom::extract() enables the per-atom data to be accessed through the [[LAMMPS library interface]{.doc}]Howto_library.md){.reference .internal} by a calling code, including from [[Python]{.doc}]Python_head.md){.reference .internal}.

The constructor of the new atom style will also typically set a few flags which are defined at the top of [`atom_vec.h`{.docutils .literal .notranslate}]{.pre}. If these are unclear, see how other atom styles use them.

The grow_pointers() method is also required to make a copy of peratom data pointers, as explained in the code.

There are a number of other optional methods which your atom style can implement. These are only needed if you need to do something out-of-the-ordinary which the default operation of the AtomVec parent class does not take care of. The best way to figure out why they are sometimes useful is to look at how other atom styles use them.

- process_args = use if the atom style has arguments

- init = called before each run

- force_clear = called before force computations each timestep

A few atom styles define "bonus" data associated with some or all of their particles, such as [[atom_style ellipsoid or tri]{.doc}]atom_style.md){.reference .internal}. These methods work with that data:

- copy_bonus

- clear_bonus

- pack_comm_bonus

- unpack_comm_bonus

- pack_border_bonus

- unpack_border_bonus

- pack_exchange_bonus

- unpack_exchange_bonus

- size_restart_bonus

- pack_restart_bonus

- unpack_restart_bonus

- data_atom_bonus

- memory_usage_bonus

The [[atom_style body]{.doc}]atom_style.md){.reference .internal} command can define a particle geometry with an arbitrary number of values. This method reads it from a data file:

- data_body

These methods are called before or after operations handled by the parent AtomVec class. They allow an atom style to do customized operations on the per-atom values. For example [[atom_style sphere]{.doc}]atom_style.md){.reference .internal} reads a diameter and density of each particle from a data file. But these need to be converted internally to a radius and mass. That operation is done in the data_atom_post() method.

- pack_restart_pre

- pack_restart_post

- unpack_restart_init

- create_atom_post

- data_atom_post

- pack_data_pre

- pack_data_post

These methods enable the [[compute property/atom]{.doc}]compute_property_atom.md){.reference .internal} command to access per-atom variables it does not already define as arguments, so that they can be written to a dump file or used by other LAMMPS commands.

- property_atom

- pack_property_atom
:::
::::
:::::

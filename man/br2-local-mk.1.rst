===============
br2-local-mk
===============

-------------------------
Manage Buildroot local.mk
-------------------------

:Author: Eric Le Bihan <eric.le.bihan.dev@free.fr>
:Copyright: 2015-2017 Eric Le Bihan
:Manual section: 1

SYNOPSIS
========

br2-local-mk [OPTIONS] <command> [<argument>, ...]

DESCRIPTION
===========

`br2-local-mk(1)` allows the Buildroot user to easily manage a
local Makefile for compiling custom versions of packages, through a
set of commands:

- edit: edit or create a ``local.mk`` preset.
- list: list the available presets.
- import: import an existing ``local.mk`` from a Buildroot build directory into
  preset.
- install: install a ``local.mk`` from a preset into a Buildroot build
  directory.
- clean: remove ``local.mk`` from a directory.
- remove: remove ``local.mk`` preset.
- scaffold: create a ``local.mk`` preset for a given list of packages.

OPTIONS
=======

-v, --version   display program version and exit

COMMANDS
========

The following commands are available:

list
~~~~

List the available presets.

edit <preset>
~~~~~~~~~~~~~

Edit an existing ``local.mk`` *preset* or create one if it does not
exists. The text editor specified in the *$EDITOR* environment
variable will be used.

import <preset> <source>
~~~~~~~~~~~~~~~~~~~~~~~~

Install an existing ``local.mk`` from the *source* directory into *preset*.

install <preset> <destination>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install an existing ``local.mk`` *preset* into the *destination*
directory. As the ``local.mk`` file is just a symbolic link, simply
delete it to uninstall.

clean <directory>
~~~~~~~~~~~~~~~~~

Remove ``local.mk`` from *directory*.

remove <preset>
~~~~~~~~~~~~~~~

Remove preset.
Make sure you also *clean* or remove the ``local.mk`` file from the Buildroot
build directory.

scaffold <preset> <pkgdir> <srcdir> [<package>, ...]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a ``local.mk`` *preset* for a given list of packages. The packages are
declared in *pkgdir*. The root directory containing the source code of the
packages to override is *srcdir*. If no package is given, all packages found in
*pkgdir* are selected.

EXAMPLES
========

To create a new preset named "foobar", execute::

  $ br2-local-mk edit foobar

To install it into the Buildroot build directory, execute::

  $ br2-local-mk install foobar /path/to/buildroot/output

To uninstall::

  $ rm /path/to/buildroot/output/local.mk

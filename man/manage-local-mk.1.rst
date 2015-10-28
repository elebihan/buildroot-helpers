===============
manage-local-mk
===============

---------------
Manage local.mk
---------------

:Author: Eric Le Bihan <eric.le.bihan.dev@free.fr>
:Copyright: 2015 Eric Le Bihan
:Manual section: 1

SYNOPSIS
========

manage-local-mk [OPTIONS] <command> [<argument>, ...]

DESCRIPTION
===========

`manage-local-mk(1)` allows the Buildroot user to easily manage a
local Makefile for compiling custom versions of packages, through a
set of commands:

- edit: edit or create a ``local.mk`` preset.
- list: list the available presets.
- install: install a ``local.mk`` from a preset into a Buildroot build
  directory.
- clean: remove ``local.mk`` from a directory.
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

install <preset> <destination>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install an existing ``local.mk`` *preset* into the *destination*
directory. As the ``local.mk`` file is just a symbolic link, simply
delete it to uninstall.

clean <directory>
~~~~~~~~~~~~~~~~~

Remove ``local.mk`` from *directory*.

scaffold <preset> <pkgdir> <srcdir> [<package>, ...]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a ``local.mk`` *preset* for a given list of packages. The packages are
declared in *pkgdir*. The root directory containing the source code of the
packages to override is *srcdir*. If no package is given, all packages found in
*pkgdir* are selected.

EXAMPLES
========

To create a new preset named "foobar", execute::

  $ manage-local-mk edit foobar

To install it into the Buildroot build directory, execute::

  $ manage-local-mk install foobar /path/to/buildroot/output

To uninstall::

  $ rm /path/to/buildroot/output/local.mk

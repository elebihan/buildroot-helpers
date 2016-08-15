# -*- coding: utf-8 -*-
#
# This file is part of buildroot-helpers
#
# Copyright (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
   br2helpers.cli
   ``````````````

   Command line interpreter helpers

   :copyright: (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""

import os
import argparse
from gettext import gettext as _
from br2helpers import __version__
from .mk import LocalMkManager
from .utils import setup_i18n


def parse_cmd_list(args):
    mgr = LocalMkManager()
    for preset in mgr.presets:
        print(preset)


def parse_cmd_edit(args):
    mgr = LocalMkManager()
    mgr.edit(args.preset)


def parse_cmd_install(args):
    mgr = LocalMkManager()
    mgr.install(args.preset, args.destination)


def parse_cmd_new(args):
    mgr = LocalMkManager()
    mgr.create(args.preset, args.src_dir, args.packages)


def manage_local_mk():

    setup_i18n()

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version',
                        action='version',
                        version=__version__)

    subparsers = parser.add_subparsers(dest='command')
    p = subparsers.add_parser('list',
                              help=_('list available presets'))
    p.set_defaults(func=parse_cmd_list)

    p = subparsers.add_parser('edit',
                              help=_('edit a local.mk preset'))
    p.add_argument('preset',
                   help=_('name of the local.mk preset'))
    p.set_defaults(func=parse_cmd_edit)

    p = subparsers.add_parser('install',
                              help=_('install a local.mk preset'))
    p.add_argument('preset',
                   help=_('name of the local.mk preset'))
    p.add_argument('destination',
                   help=_('destination directory'))
    p.set_defaults(func=parse_cmd_install)

    p = subparsers.add_parser('new',
                              help=_('create a new local.mk preset'))
    p.add_argument('-s', '--source',
                   dest='src_dir',
                   metavar=_('DIRECTORY'),
                   default=os.getcwd(),
                   help=_('path to packages base directory'))
    p.add_argument('preset',
                   help=_('name of the local.mk preset'))
    p.add_argument('packages',
                   nargs='+',
                   metavar=_('PACKAGE'),
                   help=_('package to override'))
    p.set_defaults(func=parse_cmd_new)

    args = parser.parse_args()

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.error(_('Missing command'))
    else:
        args.func(args)

# vim: ts=4 sw=4 sts=4 et ai

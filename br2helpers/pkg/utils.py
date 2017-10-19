# -*- coding: utf-8 -*-
#
# This file is part of buildroot-helpers
#
# Copyright (C) 2015-2017 Eric Le Bihan <eric.le.bihan.dev@free.fr>
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
   br2helpers.pkg.utils
   ``̀``````````````````

   Package utilities

   :copyright: (C) 2015-2017 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""


import os
from ..mk.utils import extract_variables
from collections import namedtuple

PackageInfo = namedtuple('PackageInfo', ['name', 'site', 'source', 'version'])


def create_package_info(filename):
    """Collect package information from Makefile.

    :param filename: path to the Makefile
    :type filename: string

    :return: a :class:`PackageInfo`
    """
    name, ext = os.path.splitext(os.path.basename(filename))
    prefix = name.replace('-', '_').upper()
    vars = extract_variables(filename, prefix)
    info = PackageInfo(name,
                       vars.get(prefix + '_SITE'),
                       vars.get(prefix + '_SOURCE'),
                       vars.get(prefix + '_VERSION'))
    return info


def collect(directory):
    """Collect information about the packages in a directory.

    :param directory: path to the directory containing packages
    :type directory: string

    :returns: a list of :class:`PackageInfo`
    """
    packages = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.mk'):
                path = os.path.join(root, filename)
                packages.append(create_package_info(path))
    return packages


# vim: ts=4 sw=4 sts=4 et ai

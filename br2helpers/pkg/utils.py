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
   br2helpers.pkg.utils
   ``̀``````````````````

   Package utilities

   :copyright: (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""


import os
from ..common import download_file
from ..mk.utils import extract_variables
from ..vcs.base import RepoObjectType
from ..vcs.utils import checkout_vcs, is_vcs_url
from collections import namedtuple
from gettext import gettext as _

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


def check_package_use_vcs(pkginfo):
    return is_vcs_url(pkginfo.site)


def download_package(pkginfo, path):
    if not pkginfo.site or not pkginfo.source:
        raise RuntimeError(_('Invalid URL for package'))
    url = pkginfo.site + '/' + pkginfo.source
    download_file(url, path)


def checkout_package(pkginfo, path):
    checkout_vcs(pkginfo.site, path, RepoObjectType.tag, pkginfo.version)

# vim: ts=4 sw=4 sts=4 et ai

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
   br2helpers.pkg.helpers
   ``````````````````````

   Package helpers

   :copyright: (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""

import os
from .utils import collect, check_package_use_vcs
from .utils import download_package, checkout_package
from ..common import uncompress_archive
from fnmatch import fnmatch
from gettext import gettext as _


class PackageFetcher:
    """Fetch the source code of a package.

    :param pkgdir: location of packages
    :type pkgdir: strchr

    :param cachedir: location of archives
    :type cachedir: str
    """

    def __init__(self, pkgdir, cachedir):
        self._pkgdir = pkgdir
        self._cachedir = cachedir or os.path.expanduser('~/dl')
        self._pkgs = []
        self.use_vcs = False

    def _find_package(self, pkgname):
        self._pkgs = self._pkgs or collect(self._pkgdir)
        for pkg in self._pkgs:
            if pkg.name == pkgname:
                return pkg
        raise RuntimeError(_("can not find '{}'".format(pkgname)))

    def _find_file(self, pattern):
        for fn in os.listdir(self._cachedir):
            if fnmatch(fn, pattern):
                return os.path.join(self._cachedir, fn)
        msg = _("can not find files matching '{}'".format(pattern))
        raise FileNotFoundError(msg)

    def fetch(self, pkgname, path):
        """Fetch the source code and drop it into a directory.

        :param pkgname: name of the packages
        :type pkgname: strchr

        :param path: path of the destination directory
        :type path: str
        """
        pkg = self._find_package(pkgname)
        if check_package_use_vcs(pkg):
            checkout_package(pkg, path)
        else:
            try:
                basename = pkg.source or pkg.name + '-' + pkg.version + '*'
                filename = self._find_file(basename)
            except FileNotFoundError:
                filename = download_package(pkg, self._cachedir)
            uncompress_archive(filename, path)


# vim: ts=4 sw=4 sts=4 et ai

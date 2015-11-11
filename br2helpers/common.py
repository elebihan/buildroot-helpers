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
   br2helpers.common
   `````````````````

   Common helpers and functions

   :copyright: (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""

import tarfile


def uncompress_archive(filename, path):
    """Uncompress an archive file.

    :param filename: path to the archive file
    :type filename: str

    :param path: path to destination directory
    :type path: str
    """
    tarball = tarfile.open(filename)
    tarball.extractall(path)


def download_file(url, path):
    """Download a file.

    :param url: URL of the file to download.
    :type url: str

    :param path: path ot destination directory
    :type path: str
    """
    raise NotImplementedError


# vim: ts=4 sw=4 sts=4 et ai

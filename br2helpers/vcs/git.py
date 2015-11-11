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
   br2helpers.vcs.git
   ``````````````````

   Git version control system

   :copyright: (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""

import re
from .base import Repository
from subprocess import check_call

_URL_PATTERNS = (
    r'^git://.+',
    r'^http[s]?://github.com/.+',
)


class GitRepository(Repository):
    """Git repository"""

    def __init__(self, url, path):
        self._url = url
        self._path = path

    def clone(url, path):
        args = ['git', 'clone', url, path]
        check_call(args)
        return GitRepository(url, path)

    def is_supported_url(url):
        for pattern in _URL_PATTERNS:
            if re.match(pattern, url):
                return True
        return False

    def checkout_branch(self, name):
        args = ['git', '-C', self._path, 'checkout', '--track', name]
        check_call(args)

    def checkout_tag(self, name):
        args = ['git', '-C', self._path, 'checkout', '-b', 'tmp/' + name, name]
        check_call(args)


# vim: ts=4 sw=4 sts=4 et ai

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
   br2helpers.vcs.utils
   ````````````````````

   Version Control System utilities

   :copyright: (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""

import os
from .base import RepoObjectType
from .git import GitRepository
from gettext import gettext as _

_REPO_KLASSES = (GitRepository, )


def clone_repository(url, path):
    path = os.path.abspath(path)
    for klass in _REPO_KLASSES:
        if klass.is_supported_url(url):
            return klass.clone(url, path)
    raise RuntimeError(_('unsupported URL scheme'))


def checkout_vcs(url, path, what, which):
    repo = clone_repository(url, path)
    if what == RepoObjectType.branch:
        repo.checkout_branch(which)
    elif what == RepoObjectType.tag:
        repo.checkout_tag(which)


def is_vcs_url(url):
    for klass in _REPO_KLASSES:
        if klass.is_supported_url(url):
            return True
    return False


# vim: ts=4 sw=4 sts=4 et ai

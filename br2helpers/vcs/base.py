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
   br2helpers.vcs.base
   ```````````````````

   Version Control System base classes

   :copyright: (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""

import abc
from enum import Enum


RepoObjectType = Enum('RepoObjectType', 'branch tag')


class Repository(metaclass=abc.ABCMeta):
    """Abstract base class for a VCS repository"""

    @abc.abstractstaticmethod
    def clone(url, path):
        pass

    @abc.abstractstaticmethod
    def is_supported_url(url):
        pass

    @abc.abstractmethod
    def checkout_branch(self, name):
        pass

    @abc.abstractmethod
    def checkout_tag(self, name):
        pass


# vim: ts=4 sw=4 sts=4 et ai

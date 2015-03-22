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
   br2helpers.mk
   `````````````

   Makefile helpers

   :copyright: (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""

import os
from subprocess import check_call
from gettext import gettext as _

class LocalMkManager:
    def __init__(self):
        self._registry = os.path.expanduser('~/.config/buildroot.org/Makefiles')

    @property
    def presets(self):
        presets = []
        try:
            for entry in os.listdir(self._registry):
                if not os.path.isdir(entry):
                    root, ext = os.path.splitext(entry)
                    if ext == '.mk':
                        presets.append(root)
        except OSError:
            pass
        return presets

    def _create(self, preset):
        os.makedirs(self._registry, exist_ok=True)
        with open(self._expand(preset), 'w') as f:
            f.write('# Buildroot local.mk\n')

    def _expand(self, preset):
        return os.path.join(self._registry, preset + '.mk')

    def install(self, preset, destination):
        if preset in self.presets:
            if not os.path.isdir(destination):
                os.makedirs(destination)
            target = os.path.join(destination, 'local.mk')
            os.symlink(self._expand(preset), target)
        else:
            raise RuntimeError(_('no such preset'))

    def edit(self, preset):
        if preset not in self.presets:
            self._create(preset)
        check_call([os.environ.get('EDITOR', 'vi'), self._expand(preset)])


# vim: ts=4 sw=4 sts=4 et ai

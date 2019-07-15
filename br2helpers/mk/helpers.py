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
   br2helpers.mk.helpers
   ``````````````̀`̀̀``̀`̀̀```

   Makefile helpers

   :copyright: (C) 2015-2017 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""

import os
from ..pkg.utils import collect
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

    def imprt(self, preset, source):
        if preset in self.presets:
            raise RuntimeError(_('preset already exists'))
        else:
            if not os.path.isdir(source):
                raise RuntimeError(_('source folder does not exist'))
            target = os.path.join(source, 'local.mk')
            os.makedirs(self._registry, exist_ok=True)
            os.rename(target, self._expand(preset))
            os.symlink(self._expand(preset), target)

    def install(self, preset, destination):
        if preset in self.presets:
            if not os.path.isdir(destination):
                os.makedirs(destination)
            target = os.path.join(destination, 'local.mk')
            os.symlink(self._expand(preset), target)
        else:
            raise RuntimeError(_('no such preset'))

    def clean(self, path):
        target = os.path.join(path, 'local.mk')
        if os.path.exists(target):
            os.unlink(target)

    def edit(self, preset):
        if preset not in self.presets:
            self._create(preset)
        check_call([os.environ.get('EDITOR', 'vi'), self._expand(preset)])

    def scaffold(self, preset, pkgdir, srcdir, selection=[]):
        os.makedirs(self._registry, exist_ok=True)
        packages = collect(pkgdir)
        if selection:
            names = [pkg.name for pkg in packages]
            for entry in selection:
                if entry not in names:
                    raise RuntimeError(_("can not find '{}'".format(entry)))
            packages = [pkg for pkg in packages if pkg.name in selection]
        with open(self._expand(preset), 'w') as f:
            for pkg in packages:
                name = pkg.name.upper().replace('-', '_')
                path = os.path.join(srcdir, pkg.name)
                line = "{}_OVERRIDE_SRCDIR = {}\n".format(name, path)
                f.write(line)

# vim: ts=4 sw=4 sts=4 et ai

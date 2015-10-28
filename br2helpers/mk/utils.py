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
   br2helpers.mk.utils
   ``````````````̀`̀̀``̀`̀̀`

   Makefile utilities

   :copyright: (C) 2015 Eric Le Bihan <eric.le.bihan.dev@free.fr>
   :license: GPLv2+
"""

import re


def _topological_sort(graph_unsorted):
    """Perform a topological sort on a mapping between an item and its
    dependencies.

    :param graph_unsorted: the unsorted graph
    :type graph: dict of str to str

    :return: the sorted graph
    """

    graph_sorted = []

    while graph_unsorted:
        acyclic = False
        for node, edges in list(graph_unsorted.items()):
            for edge in edges:
                if edge in graph_unsorted:
                    break
            else:
                acyclic = True
                del graph_unsorted[node]
                graph_sorted.append((node, edges))
        if not acyclic:
            raise RuntimeError("Not an acyclic graph")

    return graph_sorted


def _expand_variables(variables):
    """"Expand the variables of a Makefile;

    :param variables: a mapping of strings to strings

    :return: a mapping of strings to strings.
    """

    graph_unsorted = {}

    for n, v in variables.items():
        deps = re.findall(r'\$\(([A-Z_0-9]+)\)', v)
        graph_unsorted[n] = deps

    graph_sorted = _topological_sort(graph_unsorted)

    for node, edges in graph_sorted:
        if edges:
            value = variables[node]
            for edge in edges:
                try:
                    value = value.replace("$({})".format(edge), variables[edge])
                except KeyError:
                    pass
            variables[node] = value


def extract_variables(filename, prefix):
    """Extract the variables from a Makefile.

    :param filename: path to the Makefile
    :type filename: str

    :param prefix: prefix of the variables
    :type prefix: str

    :return: a dictionary of variables with their associated values
    :rtype: dict of str to str
    """
    vars = {}
    expr = re.compile(r"^({}_[A-Z0-9_]+)\s*[:]?=\s*(.*)".format(prefix))
    with open(filename, 'r') as makefile:
        for line in makefile:
            match = expr.search(line)
            if match:
                vars[match.group(1)] = match.group(2).strip()

    _expand_variables(vars)
    return vars

# vim: ts=4 sw=4 sts=4 et ai

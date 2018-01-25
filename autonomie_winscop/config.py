# -*- coding: utf-8 -*-
# * Copyright (C) 2012-2014 Croissance Commune
# * Authors:
#       * Arezki Feth <f.a@majerti.fr>;
#       * Miotte Julien <j.m@majerti.fr>;
#       * TJEBBES Gaston <g.t@majerti.fr>
#
# This file is part of Autonomie : Progiciel de gestion de CAE.
#
#    Autonomie is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Autonomie is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Autonomie.  If not, see <http://www.gnu.org/licenses/>.
"""
Configuration handlers

Base config + spec config loader
"""
import importlib

from autonomie_winscop import models
from autonomie_winscop import formatters

EXPORTS = {
    'porteurs_1':{
        'filename': 'porteurs.csv',
        'model': models.Porteur,
        'format': formatters.format_porteurs,
    },
    'porteurs_2':{
        'filename': 'porteurs_critere.csv',
        'model': models.PorteursCritere,
    },
    'porteurs_3':{
        'filename': 'porteurs_rsa.csv',
        'model': models.PorteursRsa,
    },
    'porteurs_4':{
        'filename': 'porteurs_infos.csv',
        'model': models.PorteursInfo,
        'format': formatters.format_porteurs_infos,
    },
    'porteurs_5': {
        'filename': 'porteurs_exp.csv',
        'model': models.PorteursExp,
    },
}


def load_config(setting_file=None):
    """
    Return the final config object
    """
    exports = {}
    if setting_file is not None:
        settings = importlib.import_module(setting_file)
        exports = settings.EXPORTS

    EXPORTS.update(exports)
    return EXPORTS

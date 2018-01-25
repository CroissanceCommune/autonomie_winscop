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
Entry point of the project
"""
from sqlalchemy import engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declared_attr

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class ORMClass(object):
    """
        BASE class for our models providing usefull query and get methods
    """
    @classmethod
    def query(cls):
        """
            return a query
        """
        return DBSession().query(cls)

    @classmethod
    def get(cls, id_):
        """
            Return a query
        """
        return DBSession().query(cls).get(id_)


BASE = declarative_base(cls=ORMClass)
metadata = BASE.metadata

def initialize(settings):
    """
    Return an engine pointing to the database
    """
    engine = engine_from_config(settings, prefix="sqlalchemy.")

    DBSession.configure(bind=engine)
    BASE.metadata.bind = engine

    return DBSession

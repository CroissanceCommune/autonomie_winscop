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
Script that should be launched to write output files
"""

import os
import logging
from logging.config import fileConfig

from docopt import docopt
from sqla_inspect.csv import SqlaCsvExporter

from autonomie_winscop import initialize

try: # pragma: no cover
    import configparser
except ImportError: # pragma: no cover
    import ConfigParser as configparser


def parse_inifile(path):
    parser = configparser.ConfigParser()
    parser.read([path])
    return parser


def setup_logging(parser, inifile_path):
    """
    Setup the logging module
    """
    if parser.has_section('loggers'):
        return fileConfig(
            inifile_path,
            dict(__file__=inifile_path, here=os.path.dirname(inifile_path))
        )


def setup_formatters():
    """
    Tune sqla_inspect in order to get appropriate formatters
    """
#    import sqlalchemy
    from sqla_inspect.export import FORMATTERS_REGISTRY
#    FORMATTERS_REGISTRY.add_formatter(
#        sqlalchemy.Date,
#        lambda d: d.strftime('%d/%m/%Y'),
#    )


def cmd(func, doc):
    logging.basicConfig()
    args = docopt(doc)

    inifile_path = os.path.abspath(args['<config_uri>'])
    parser = parse_inifile(inifile_path)

    main_config_dict = dict(parser.items('main'))

    setup_formatters()
    setup_logging(parser, inifile_path)
    initialize(main_config_dict)

    try:
        func(args)
    finally:
        print("Done")
    return 0


def writefiles(args):
    """
    Write csv files to the specified filepath

    --c : export_config_file containing the list of files to generate
    for each file, a dict describes:

        filename

            The name of the file to generate

        model

            the model to use for the export

        query

            the query to use in order to fetch all the datas we want to import

        format

            A python callable that takes the csv file buffer resulting from the
            export
    """
    logger = logging.getLogger(__name__)
    logger.info("******** Writing files *********")

    dest_directory = args.get(
        '--d',
        '/tmp/',
    )
    export_config_file = args.get('--c')

    if export_config_file is not None:
        logger.info(
            " + Getting additionnal configuration elements from {0}".format(
                export_config_file
            )
        )

    # L'import doit être fait ici (après initialize)
    from autonomie_winscop.config import load_config

    export_dict = load_config(export_config_file)

    logger.info(u"We loaded the config dict")
    logger.debug(export_dict)

    for value in export_dict.values():
        filename = value['filename']
        model = value['model']
        query = value.get('query', model.query)
        post_format = value.get('format')

        filepath = os.path.join(dest_directory, filename)

        logger.info("Writing {0}".format(filepath))
        with open(filepath, 'w') as f_buf:
            exporter = SqlaCsvExporter(model)
            for entry in query():
                exporter.add_row(entry)
            exporter.render(f_buf)

        if post_format is not None:
            post_format(filepath)

    logger.debug("Done")


def write(directory='/tmp', settings=None):
    """Write csv files from the winscop database
    Usage:
        writefiles <config_uri> write [--d=dest_directory] [--c=export_config_file]


    Options:
        -h --help     Show this screen.
    """
    try:
        return cmd(writefiles, write.__doc__)
    except:
        import traceback
        traceback.print_exc()

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
import csv
from sqla_inspect.csv import get_csv_reader, CsvWriter


FAMILY_STATUS_MATCH = dict((
    ("Marié(e)", 'maried'),
    ("Divorcé(e)", "single"),
    ("Célibataire", "single"),
    ('', "single"),
    ("Veuf(ve)", 'single',),
    ("Concubinage", "free_union",),
    ("Pacsé(e)", "pacsed",),
))

PORTEUR_STATUS_MATCH = dict((
    ("En convention", "En convention",),
    ("Entrepreneur salarié", "Intégré",),
    ("Candidat", "Candidat",),
    ("Sortie", "Sortie",),
    ("Associé", "Intégré"),
))


ENTRANCE_STATUS_MATCH = dict((
    ("de1", "DE > 1 an",),
    ("sal", "Salarié",),
    ("rsa", "Bénéficiaire du RSA",),
    ("de", "DE",),
    ("autre", "Autre"),
    ("inde", "Travailleur indépendant"),
))

def get_header_rows(filepath):
    """
    Get the headers and the rows from the given file
    """
    with open(filepath, 'r') as f_buf:
        reader = get_csv_reader(f_buf)
        fieldnames = reader.fieldnames
        rows = [row for row in reader]
    return fieldnames, rows


def write_csv_file(filepath, fieldnames, rows):
    """
    Write the output csv file after formatting
    """
    headers = [{'label': field} for field in fieldnames]
    with open(filepath, 'w') as f_buf:
        outfile = CsvWriter()
        outfile.set_headers(headers)
        outfile._datas = rows
        outfile.render(f_buf)


def format_porteurs(filepath):
    """
    Formatter used to manage the porteurs.csv file content

    :param str filepath: The path to the file to read/write
    """
    fieldnames, rows = get_header_rows(filepath)

    if "statut" in fieldnames:
        fieldnames.append("situation_societariat_entrance")
        fieldnames.append("situation_situation")
        for row in rows:
            statut = row['statut']
            row['situation_societariat_entrance'] = ""
            if statut == "Associé":
                row['situation_societariat_entrance'] = "01/01/2015"
            row['situation_situation'] = PORTEUR_STATUS_MATCH.get(statut)


    if 'coordonnees_address1' in fieldnames and 'coordonnees_address2' in fieldnames:
        fieldnames.append('coordonnees_address')
        for row in rows:
            row['coordonnees_address'] = row['coordonnees_address1'] + \
                    '\n' + row['coordonnees_address2']

    if "coordonnees_civilite" in fieldnames:
        fieldnames.append('coordonnees_sex')
        for row in rows:
            if row['coordonnees_civilite'].lower() == u"mademoiselle":
                row['coordonnees_civilite'] = u"Madame"

            if row['coordonnees_civilite'] == u'Madame':
                row['coordonnees_sex'] = 'F'
            else:
                row['coordonnees_sex'] = 'M'

    if "zus" in fieldnames:
        fieldnames.append("coordonnees_zone_qual")
        for row in rows:
            if row['zus'] == '1':
                row['coordonnees_zone_qual'] = 'zus'

    write_csv_file(filepath, fieldnames, rows)


def format_porteurs_infos(filepath):
    fieldnames, rows = get_header_rows(filepath)

    if '_coordonnees_family_status' in fieldnames:
        for row in rows:
            row['coordonnees_family_status'] = FAMILY_STATUS_MATCH.get(row['_coordonnees_family_status'])
            if row.get('femme_isolee') == 1:
                row['coordonnees_family_status'] = 'isolated'

    write_csv_file(filepath, fieldnames, rows)

def format_porteurs_exp(filepath):
    fieldnames, rows = get_header_rows(filepath)

    if '_statut_social_status' in fieldnames:
        fieldnames.append('statut_social_status')
        for row in rows:
            row['statut_social_status'] = ENTRANCE_STATUS_MATCH.get(
                row['_statut_social_status']
            )

    write_csv_file(filepath, fieldnames, rows)


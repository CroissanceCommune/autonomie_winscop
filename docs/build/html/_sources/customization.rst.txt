Personnalisation de la génération CSV
=====================================


Dans le répertoire /tmp/winscop_datas/, ajouter un fichier custom.py et fournir
un dictionnaire EXPORTS personnalisé :

.. code-block:: python

    # -*- coding:utf-8 -*-
    from autonomie_winscop.models import MyModel

    def format_mymodel_datas(csv_filepath):
        """
        Fonction permettant le post-formattage des données dans le fichier csv

        Il est possible de lire le fichier, modifier les valeurs et le réécrire
        ou effectuer toute autre opération (envoi de mail si on veut changer des
        mots de passe à la volée ...)

        :param str csv_filepath: Le chemin sur disque vers le fichier csv
        """
        pass


    EXPORTS = {
        'porteurcustom': {
            'file': 'porteurs_custom.csv',
            'model': MyModel,
            ['query': MyModel.query().filter(...)],
            'formatters':
        }
    }

Vous pouvez vous inspirer de la configuration dans autonomie_winscop/config.py.

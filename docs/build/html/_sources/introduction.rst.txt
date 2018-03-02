Introduction
=============

Ce package fournit l'outillage nécessaire pour générer des fichiers CSV
depuis les données de gestion sociale d'une base de données Winscop.

Les fichiers csv générés sont ensuite importable dans la gestion sociale
Autonomie.

Les outils suivants sont utilisés

    sqlautogen

        Utilisé pour la génération des modèles SQLAlchemy depuis une base de
        données existantes.

    SQLAlchemy

        Pour la description des modèles de données Winscop

    sqla_inspect

        Pour la génération des fichiers csv depuis les modèles, permet la
        translation et le formattage des données

    docker

        Pour la génération automatique des fichiers csv depuis le fichier
        sql

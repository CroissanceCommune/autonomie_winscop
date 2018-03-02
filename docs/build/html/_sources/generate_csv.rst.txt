Génération des fichiers CSV
============================

Une fois vos données préparées, vous pouvez générer les fichiers csv.

Téléchargement de autonomie_winscop
------------------------------------

On va télécharger le logiciel à la racine du home de l'utilisateur courant

.. code-block:: console

    cd ~/
    git clone https://github.com/CroissanceCommune/autonomie_winscop

Installation de docker
-----------------------

Sur les distributions basées sur Debian (Ubuntu, Linux Mint ...)

.. code-block:: console

    apt-get install docker-io

Sur les distributions utilisant dnf (CentOS, Fedora, RedHat)

.. code-block:: console

    dnf install docker-io

Générer l'image docker
----------------------

.. code-block:: console

    docker build -t winautonomie ~/autonomie_winscop/docker/

Générer les fichiers csv
-------------------------

.. code-block:: console

    docker run -t -i -v ~/autonomie_winscop:/mnt/winautonomie \
    -v /tmp/winscop_datas:/mnt/autonomie winautonomie

Les fichiers csv sont alors disponibles dans le répertoire
/tmp/winscop_datas/processed.

Quelques commandes Docker
-------------------------

Lister les containers (instances qui tournent)

.. code-block:: console

    docker ps -a

Lister les images docker

.. code-block:: console

    docker images

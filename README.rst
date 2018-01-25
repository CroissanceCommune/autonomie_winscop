Winscop to Autonomie migration tool
===================================

Generate csv files with Autonomie model attribute headers that can be imported
with the help of sqla_inspect toolbox.

Prepare the sql datas
----------------------

Generated models are generated with the help of sqlautogen

* Take the appropriate sql dump file
* Clean it (remove the unnecessary databases, especially mysql)
* Rename the database to restore as 'winscop'

Place the sql file in a directory, for example : ~/test

Generation customization
------------------------

In a ~/test/custom.py file customize the csv file generation by writing a EXPORTS dict
of the form :

.. code-block:: python

    EXPORTS = {
        'porteurcustom': {
            'file': 'porteurs_custom.csv',
            'model': Model,
            ['query': Model.query().filter(...)],
        }
    }

Clone the repository in ~/autonomie_winscop

.. code-block:: console

    apt-get install docker-io

Launch the import
-----------------

Build the docker image (to clear the cache, modify/add a comment on the line
from which you want it to be cleared)

.. code-block:: console

    # docker build -t autonomie_winscop ~/autonomie_winscop/docker/
    docker build -t autonomie_winscop ~/autonomie/autonomie_winscop/docker/

Launch the csv file generation

.. code-block:: console

    # docker run -t -i -v ~/autonomie_winscop:/mnt/autonomie_winscop \
    -v /tmp/autonomie:/mnt/autonomie autonomie_winscop
    docker run -t -i -v ~/autonomie/autonomie_winscop:/mnt/autonomie_winscop -v \
    ~/test:/mnt/autonomie autonomie_winscop


Usefull docker commands
------------------------

List all containers :

.. code-block:: console

    docker ps -a

List images :

.. code-block:: console

    docker images

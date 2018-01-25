# -*- coding: utf-8 -*-
import os
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='autonomie_winscop',
    version='0.1',
    packages=['autonomie_winscop'],
    include_package_data=True,
    license='GPLv3',
    description='Outils de migration de Winscop vers Autonomie',
    author='Gaston Tjebbes - Majerti',
    author_email='tech@majerti.fr',
    install_requires=['oursql', 'sqla_inspect', 'SQLAlchemy', 'zope.sqlalchemy', 'docopt'],
    extra_requires={'docs': ['sphinx'], 'test': ['pytest']},
    entry_points={
        'console_scripts': [
            "autonomie_winscop = autonomie_winscop.script:write",
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
    ],
)

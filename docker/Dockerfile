FROM debian
# Installation des paquets
RUN apt-get update

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y -q install mysql-server
RUN apt-get -y -q install libmysqlclient-dev python-pip python-dev libxml2-dev libxslt-dev 
RUN pip install sqla_inspect oursql SQLAlchemy zope.sqlalchemy 
# Installation de autonomie_winscop
ENTRYPOINT python /mnt/autonomie_winscop/setup.py install &&  cp /mnt/autonomie_winscop/app.ini /etc/autonomie_winscop.ini && /mnt/autonomie_winscop/bin/gen_migration_files.sh && /bin/bash

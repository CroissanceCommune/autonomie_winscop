#!/bin/bash
####################################################################################
# Script générant des fichiers d'import autonomie sur la base de données sql
# winscop
#
# Créer le container docker depuis l'image approprié et placer un fichier .sql
# winscop dans /mnt/autonomie/ sur le container démarré
#
####################################################################################

ROOT_DIR=/mnt/autonomie/
CUSTOM_CONFIG=${ROOT_DIR}/custom.py
PROCESSED_DIR=${ROOT_DIR}/processed/
LOGFILE=${ROOT_DIR}/script.log

NAME="winscop"

if [ ! -d ${ROOT_DIR} ]
then
    echo "Please add the missing the mount point (${ROOT_DIR}) to your docker container"
    exit 1
fi

echo "Creating the PROCESSED_DIR"
echo "Creating the PROCESSED_DIR" >> $LOGFILE
mkdir -p ${PROCESSED_DIR}

echo "Checking the number of sql files provided (should be 1)"
echo "Checking the number of sql files provided (should be 1)" >> $LOGFILE
num_sql_files=`ls -l ${ROOT_DIR}*.sql | wc -l`
if [ "o${num_sql_files}o" != "o1o" ]
then
    echo "There should be only one .sql file in ${ROOT_DIR}"
    exit 1
fi

/etc/init.d/mysql start

echo "Initializing the database"
echo "Initializing the database" >> $LOGFILE

echo "Inserting the datas"
echo "Inserting the datas" >> $LOGFILE
mysql -uroot < ${ROOT_DIR}*.sql

echo "Creating user and granting permissions"
echo "Creating user and granting permissions" >> $LOGFILE
echo "CREATE USER ${NAME};" | mysql -uroot
echo "GRANT ALL PRIVILEGES on ${NAME}.* to ${NAME}@localhost IDENTIFIED BY '${NAME}';" | mysql -uroot
echo "FLUSH PRIVILEGES;" | mysql -uroot

echo "Launching the file generation"
echo "Launching the file generation" >> $LOGFILE

if [ -f ${CUSTOM_CONFIG} ]
then
    autonomie_winscop /etc/autonomie_winscop.ini write --d=${PROCESSED_DIR} --c=${CUSTOM_CONFIG}
else
    autonomie_winscop /etc/autonomie_winscop.ini write --d=${PROCESSED_DIR}
fi

exit 0

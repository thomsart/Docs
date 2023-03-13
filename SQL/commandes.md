# Installation

    sudo apt update
    sudo apt install postgresql


Une fois que PostgreSQL est installé, on s'assure que les services de postgres soientt acif et disponible sous systemd on tappant les commandes suivantes:

    sudo systemctl is-active postgresql
    sudo systemctl is-enabled postgresql
    sudo systemctl status postgresql

On s'assure aussi qu'il est prêt à recevoir la connection d'un client:

    sudo pg_isready

Pour créer une nouvelle base de données sur PostgreSQL, on doit accéder au shell (psql). Premièrement on switch sur l'administrateur (le big boss) de postgresql qui est 'postgres' et on tape 'psql':

    sudo su - postgres
    psql

S'ouvre ensuite:

    postgres=#

Ensuite on fait notre créaton:

    postgres=# CREATE USER jack WITH PASSWORD 'thepaswordofjack';
    postgres=# CREATE DATABASE thedatabase;
    postgres=# GRANT ALL PRIVILEGES ON DATABASE thedatabase to jack;
    postgres=# \q

PostgreSQL uses client authentication to decide which user accounts can connect to which databases from which hosts and this is controlled by settings in the client authentication configuration file, which on Ubuntu is located at /etc/postgresql/12/main/pg_hba.conf.

Open this file using your favorite text editor as shown.

    sudo vim /etc/postgresql/12/main/pg_hba.conf

PostgreSQL uses many types of client authentication methods including peer, ident, password, and md5 (read the PostgreSQL 12 documentation for a detailed explanation of each method).  
md5 is the most secure and recommended because it requires the client to supply a double-MD5-hashed password for authentication. So, ensure that the entries below have md5 as the under method:

    host    all             all             127.0.0.1/32            md5
    # IPv6 local connections:
    host    all             all             ::1/128                	md5


Une fois finis redémarrer les services de PostgreSQL an tappant:

    sudo systemctl restart postgresql

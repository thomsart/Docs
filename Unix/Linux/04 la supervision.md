#################################################################################################
#################################################################################################
# Analysez les principaux fichiers de traces

Unix est un système d'exploitation conçu dès le départ pour accueillir plusieurs utilisateurs simultanément. Linux a bien évidemment hérité de cette propriété. Il est donc tout à fait possible que plusieurs comptes exécutent plusieurs tâches simultanément sur un serveur Linux (service web, service FTP, service mail, etc.).
Du coup, l'exercice d'analyse de l'activité du système pourrait paraître un peu compliqué mais en réalité c'est assez simple : Linux vous fournit tous les outils nécessaires pour auditer l'activité des utilisateurs ou des processus.
Les audits systèmes sont très utiles notamment dans le cadre de supervision de service: l’exemple le plus commun est le service de messagerie, qui est souvent très sensible !

Si vous souhaitez vous pencher sur l'activité passée sur le système, alors vous allez consulter les fichiers de traces, comme nous allons le voir dans la première section de ce chapitre avec les fichiers contenus dans le répertoire **/var/log**. 
Mais si vous vous demandez qui fait quoi à l'instant T sur le système, alors vous pourrez également profiter des nombreuses commandes à votre disposition, comme **w**, ou encore **who**.

## Consultez les répertoires des fichiers de traces de  rsyslog

Comme nous avons pu l'évoquer dans le chapitre "Adoptez l'arborescence des systèmes Linux", le répertoire **/var** contient toutes les données variables du système et notamment les fichiers de traces dans le sous-répertoire **/var/log**. 

Ce comportement est normalisé et sera commun aux distributions RedHat ou Debian et leurs dérivées. Cependant quelques différences mineures apparaîssent dans la gestion des fichiers de traces entre ces deux familles.
Chacun des processus du système proposant au noyau Linux de tracer ses activités déclenche le traitement de ses informations par un service particulier :**rsyslog**.
Ce dernier centralise la configuration des fichiers de traces et regroupe dans les fichiers concernés les informations de même nature.

Par exemple :

* toutes les traces émises par le noyau Linux : les **"kernel ring buffer"**, seront stockées dans un fichier particulier,
* toutes les traces concernant l'authentification des utilisateurs seront dans un autre fichier.

Par ailleurs, **rsyslog** dispose également de fonctionnalités supplémentaires intéressantes comme :

* envoyer ces traces sur le réseau afin de centraliser toutes celles d'un parc de machines sur un même serveur de logs,
* gérer la rotation automatique des fichiers,
* utiliser des formats de dates très précis (jusqu'au millième de seconde).

Comme tout bon processus système sous Linux, **rsyslog** se paramètre dans **/etc/rsyslog.conf**.
Nous allons parcourir ce fichier pour comprendre la gestion des fichiers de traces. Vous verrez notamment quelques différences entre Debian et CentOS (pour RedHat). Du coup je vous propose d’utiliser ce fichier pour transférer les traces d’un serveur à un autre.
C’est une opération qui est très recommandée dans tous les bons guides d’administration sécurisée des serveurs Linux (celui de **l’ANSSI** en premier !)
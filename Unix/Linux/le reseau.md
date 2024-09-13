#################################################################################################
#################################################################################################
# Configurez les cartes réseaux

La plupart du temps, votre serveur Linux sera installé au fin fond d'une salle blanche avec nombreux de ses cousins, et son administration s'effectuera à distance via un terminal. Mais ce mode opératoire n'est rendu possible qu'à la condition que votre serveur soit lui-même connecté sur un réseau.  

Je vous propose de voir tout ce qui concerne la configuration réseau d'un serveur Linux, que ce soit :

* le nom réseau de la machine
* la détection des périphériques interfaces par le noyau
* l'emplacement des fichiers de configuration
* les différents modes d'adresse IP
* les routes et passerelles
* et les services de noms (DNS)

La configuration du réseau sous Linux est un aspect qui varie fortement entre les distributions. En effet, chaque distribution aura tendance à installer les outils qui lui sont propres pour gérer le réseau. Vous pourrez notamment trouver **NetworkManager**, **Connection-Manager**, ou encore **dhcpcd**.  

Nous faire abstraction de ces différents outils et passer en revue la configuration manuelle du réseau via un processus démon. Ce processus gère :

* le montage ou le démontage des interfaces,
* les fichiers de configuration sur les distributions majoritaires en entreprise : **RedHat** (et ses dérivés) et **Debian** (et ses dérivés).

Normalement, avec cette méthode, vous serez en mesure de configurer le réseau sur toutes les distributions.

Je vous expliquerai les différences qu’il y a entre les branches **RedHat** et **Debian** lorsque ce sera nécessaire.

#################################################################################################
#################################################################################################
# Configurez le nom du réseau de votre serveur

Premier élément de configuration réseau du serveur : **son nom réseau**. 

Le nom réseau d'un serveur Linux (aussi appelé "system hostname") sert d'identifiant par défaut de la machine pour tous les services et applications qui s'exécutent en local et pour beaucoup de services et d'applications lorsque ceux-ci communiquent sur le réseau.  

Prenez l'exemple d'un serveur de fichiers logs centralisés sur un réseau interne : toutes les communications logs des serveurs du réseau seront préfixées de leur nom réseau, ce qui permettra au service de centralisation des logs de savoir d'où viennent tels ou tels fichiers.  

Si tous les serveurs de logs ont le même nom réseau (par exemple localhost qui est proposé pendant le processus d'installation), difficile de reconnaître l'origine des fichiers communiqués.  

Nous allons voir :

1. le fichier/proc/sys/kernel/hostname qui contient la valeur courante du nom réseau du serveur,
2. la commande hostnamectl qui permet de la modifier,
3. le fichier/etc/hostname qui permet d’initialiser le nom réseau au démarrage.
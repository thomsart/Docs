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

Nous allons faire abstraction de ces différents outils et passer en revue la configuration manuelle du réseau via un processus démon. Ce processus gère :

* le montage ou le démontage des interfaces,
* les fichiers de configuration sur les distributions majoritaires en entreprise : **RedHat** (et ses dérivés) et **Debian** (et ses dérivés).

Normalement, avec cette méthode, vous serez en mesure de configurer le réseau sur toutes les distributions.
Je vous expliquerai les différences qu’il y a entre les branches **RedHat** et **Debian** lorsque ce sera nécessaire.

## Configurez le nom du réseau de votre serveur

Premier élément de configuration réseau du serveur : **son nom réseau**.  

Le nom réseau d'un serveur Linux (aussi appelé "system hostname") sert d'identifiant par défaut de la machine pour tous les services et applications qui s'exécutent en local et pour beaucoup de services et d'applications lorsque ceux-ci communiquent sur le réseau.  
Prenez l'exemple d'un serveur de fichiers logs centralisés sur un réseau interne : toutes les communications logs des serveurs du réseau seront préfixées de leur nom réseau, ce qui permettra au service de centralisation des logs de savoir d'où viennent tels ou tels fichiers. On peut l;obtenir de differentes facon:

    1. cat /proc/sys/kernel/hostname
    2. sysctl kernel.hostname
    3. hostnamectl status (qui renvois plus d'info)

Du coup on pourrait modifier ce nom grace a la commnande:

    hostnamectl set-hostname nouveau_nom

Ou manuelement en modifant le fichier se situant dans /etc/hostname  

Si tous les serveurs de logs ont le même nom réseau (par exemple localhost qui est proposé pendant le processus d'installation), difficile de reconnaître l'origine des fichiers communiqués.  

Il est de coutume de le garder sous un format très simple, le plus souvent, un mot, représentant un champ lexical commun entre plusieurs serveurs.
Si on utilise par exemple "vega", pour l'étoile principale de la constellation de la Lyre. Ainsi, mes différents serveurs pourraient se nommer également avec des noms d'étoile (deneb,  altair,  procyon,  sirius, etc.). 
J'ai rencontré beaucoup de nomenclatures de nom réseau en entreprise, allant de :
la reprise de noms célèbres de villes du monde (sydney,  beijing,  bamako, etc.),
en passant par des noms de personnages mythologiques diverses (heimdall,  zeus,  osiris, etc.),
à des noms réseaux purement analytiques reprenant par exemple leur localisation ou leurs objectifs en termes de services (srv10s40,  web10front,  mailintra, etc.).
Bon, une fois le nom d’hôte positionné, il est ensuite nécessaire de passer à la configuration de la carte réseau.

## Détectez les interfaces réseaux de votre système



## Configurez les cartes réseaux de manière dynamique

## Configurez des interfaces reseaux..

## Configurez les routes et les passerelles

## Configurez les resolutions de noms


#################################################################################################
#################################################################################################
# Connectez vous a distancve avec SSH


#################################################################################################
#################################################################################################
# Transferez des fichiers par le reseau
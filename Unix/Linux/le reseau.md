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

Avant toute configuration, il est nécessaire de s'assurer que le noyau Linux a bien détecté les cartes réseaux connectées d'une manière ou d'une autre sur la machine.
La commande **dmesg**(pour "display message") permet d'afficher les messages du noyau :

* pendant le processus de démarrage,
* et notamment lorsque ce dernier charge les pilotes des périphériques qui vérifient si un matériel connecté leur est compatible.

La commande **dmesg** détecte les cartes réseaux reconnues par le noyau lors du démarrage.
On peut aussi consulter le système de fichier virtuel/sys pour lister les interfaces réseaux.
Constate d'ailleurs une évolution liée à Systemd dans le nommage par défaut de ces interfaces. 

## Configurez les cartes réseaux de manière dynamique

Avant etait utilise le paquet **net-tools** mais il n'est plus maintenus depuis 2009. Les commandes **ifconfig** ou encore **netstat** ont du coup disparus. Maintenant il y a le paquet **iproute2** qui s'en charge a la place.  
Pour configurer les cartes reseaux on a maintenant la commande **ip**.  

Si on tape:

    thomas@hp-pavillon:~$ ip link (suivit de deux fois la tabulation)

On obtiens les differentes options associees:

    add  delete  help  set  show

On peut par exemple lister les cartes:

    thomas@hp-pavillon:~$ ip link show

On pourrait par exemple eteindre ou remonter une carte reseau du nom de enp0s8:

    thomas@hp-pavillon:~$ ip link set enp0s8 down (ou up)

Ceci de maniere dynamique car au rebootage de l'ordi (ou du serveur) la conf d'origine reprend.
On peut aller plus loin que **ip link show** et avoir toutes les configuration plus detaille avec la commande:

    thomas@hp-pavillon:~$ ip a

Il est possible de creer une nouvelle adresse IP on faisant:

    thomas@hp-pavillon:~$ ip addr add 192.128.1.24/24
et
    thomas@hp-pavillon:~$ ip addr del 192.128.1.24/24

pour la supprimer.

## Configurez des interfaces reseaux...

Toutes les configurations de réseau sur les cartes gérées par la commande **ip** sont dynamiques. Elles seront donc perdues entre chaque "reboot" du serveur.
Pour configurer de manière statique les cartes réseaux de Linux, il est nécessaire de saisir les informations dans des fichiers de configuration qui vont être lus pendant le boot du serveur. On utilise donc pour ca le système de configuration **Netplan**.
Netplan est un système de configuration YAML qui remplace le fichier **/etc/network/interfaces** traditionnel. Il offre un moyen plus flexible et évolutif de configurer les interfaces réseau. Les fichiers de configuration sont stockés dans le répertoire **/etc/netplan**, et ils utilisent une syntaxe YAML pour définir les interfaces réseau et leurs paramètres.  

Par conséquent, vous ne trouverez pas de fichier **/interfaces** dans Ubuntu 24.04. Au lieu de cela, vous devrez utiliser **Netplan** pour configurer vos interfaces réseau. Vous pouvez le faire en créant un fichier de configuration YAML dans le répertoire **/etc/netplan** et en redémarrant le service Netplan.

Par exemple, si vous voulez configurer une adresse IP statique pour une interface réseau, vous créez un **fichier.yaml** comme ceci :

    network:
        version: 2
        ethernets:
            enx00e04c68425d:
                addresses:
                    - 192.168.1.100/24
                gateway4: 192.168.1.1
                nameservers:
                    addresses:
                        - 8.8.8.8
                        - 8.8.4.4

Ensuite, vous exécuteriez la commande **netplan apply** pour appliquer la configuration.

## Configurez les routes et les passerelles

À ce stade, les cartes réseaux sont configurées, mais il est encore nécessaire d'indiquer les configurations pour les paquets qui en sortent. On parle de :  

* routes pour désigner les chemins suivis par les paquets réseaux lors d'une communication,
* passerelles (ou "gateway") pour indiquer les équipements (serveurs ou routeurs) permettant d'interconnecter des réseaux différents. 

Pour gérer de manière dynamique les routes et passerelles sur le serveur Linux, encore une fois, le package **iproute2** est votre outil de préférence.

En tapant **ip route list** on obtient:

    default via 192.168.1.254 dev eno1 proto dhcp src 192.168.1.34 metric 100 
    192.168.1.0/24 dev eno1 proto kernel scope link src 192.168.1.34 metric 100

On pourrait vouloir changer la route default on faisant:

    thomas@hp-pavillon:~$ ip route del default via 192.168.1.254
    thomas@hp-pavillon:~$ ip route add default via 192.168.1.1 dev eno1 (on precise sur quelle interface, ici eno1)

Sachant bien entendu que ces modifications dans le terminal ne persistent pas, si nous voulions qu'elles le soient il faudrait reconfigurer manuellement les fichiers qui s'en chargent, a savoir le rep **/etc/netplan**.

## Configurez les resolutions de noms

Dernier point de configuration réseau du serveur: les services de résolutions de noms de domaine, ou **DNS** pour **Domain Name System**. Ce service permet au serveur d'effectuer la résolution des noms de domaines en adresse IP, afin d'envoyer des requêtes selon le protocole du service destinataire.  

Coome sur un navigateur web lorsque vous saisissez une URL dans la barre d’adresse afin d'accéder à un site web. Votre navigateur, par l'intermédiaire d'un service de résolution de nom, émet une requête pour demander la résolution de l'URL en une adresse IP identifiant de manière unique le serveur qui héberge le site web.  

Sur un serveur Linux, il est nécessaire de configurer les services de résolutions de noms de domaine. En règle générale, il s'agit simplement d'indiquer dans un fichier de configuration les adresses IP des serveurs hébergeant les services de résolution de noms de domaine.  

Cette configuration est identique entre les distributions **DEBIAN** et les distributions dérivées **REDHAT**. Cela se passe dans les fichiers **/etc/hosts** et **/etc/resolv.conf**.  

C'est dans **/etc/nsswitch.conf** que se trouve la configuration qui permet au serveur(le Software comme par exemple Nginx) en tant que client de chercher les machines(dons le PC ou le VPS) autour de lui.

Cette partie n'est pas finis car les concepts ici sont trop abstraits pour moi pour le moment...

#################################################################################################
#################################################################################################
# Connectez vous a distancve avec SSH


#################################################################################################
#################################################################################################
# Transferez des fichiers par le reseau





thomas@hp-pavillon:~$
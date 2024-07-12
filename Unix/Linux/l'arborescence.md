############################################################################################################
############################################################################################################
# L'arborescence Linux

La fondation Linux est l'organisme responsable du maintien de la norme définissant l'arborescence des systèmes Unix|Linux. Cette norme est appelée FHS pour Filesystem Hierarchy Standard et est disponible sous plusieurs formats.  

Le respect de ce standard permet aux administrateurs d'anticiper les répertoires contenant les informations recherchées, quelle que soit la distribution utilisée. 
aux développeurs système d'utiliser une arborescence commune et connue pour déployer, installer ou configurer les programmes qu'ils éditent. Pratique lorsque l'on exploite des milliers de fichiers.  

Le document va donc recenser les répertoires identifiables qui proposent un usage clair et défini,
puis indiquer éventuellement la liste minimale des répertoires, sous-répertoires et fichiers attendus pour chacun.  

Les répertoires contenant des informations stockées sur un équipement mais utilisées par d'autres équipements seront identifiés par le mot-clé "shareable" (partageables). Par exemple, le répertoire **/home** contient traditionnellement les répertoires personnels des comptes utilisateurs du système, et ces données peuvent être partagées entre utilisateurs sur le même serveur, voire entre utilisateurs sur un serveur différent.  

Les répertoires contenant des fichiers qui ne peuvent pas ou ne doivent pas être partagés entre plusieurs équipements seront marqués "unshareable". Nous pouvons citer ici **/boot** qui contient notamment le noyau Linux exploité sur l'équipement.  

Les répertoires contenant des données qui ne peuvent pas changer d'elles-mêmes, ou sans l'intervention de l'administrateur, avec nécessité d'une élévation de privilèges sont marqués "static". On peut à nouveau citer ici **/boot** bien entendu, mais également **/etc**, par exemple, qui contient traditionnellement les fichiers de configuration du système et des services.  

Les répertoires qui ne sont pas marqués statiques sont marqués "variable" (variables). On peut retrouver ici le répertoire  **/home**  évidemment, mais également **/var/www** pour les sources d'un site web par exemple.  

Tous les exemples de répertoires cités ici sont adressés de manière absolue, c'est-à-dire à partir de la racine du système **/**. 

La norme FHS adresse ces recommandations à partir d'un système monté sur la racine **/**.  
L'administrateur peut quant à lui adresser les répertoires et les fichiers de manière relative à un emplacement courant. Pour cela, chaque répertoire sous la racine **/** possède deux fichiers spéciaux nommés '.' pour se  désigner soi-même, et '..' pour désigner son parent dans l'arborescence.

Selon FHS, voici la liste minimale de tous les éléments devant être présents
directement sous la racine **/** :  

**bin** => répertoire contenant les commandes pouvant être utilisées à la fois par le système et par un administrateur ;  
**boot** => répertoire contenant tout le nécessaire pour démarrer le système => la configuration du bootloader, le noyau, les fichiers ramfs… ;  
**dev** => répertoire contenant traditionnellement tous les points d'accès aux périphériques, terminaux, disques, supports amovibles etc. ;  
**etc** => répertoire contenant les fichiers de configuration des programmes et services exploités sur le système ;  
**lib** => répertoire contenant les librairies partagées par les différentes commandes de /bin ou /sbin ;  
**media** => répertoire contenant les points de montage des périphériques amovibles (clé USB, disques externes, etc.) ;  
**mnt** => répertoire contenant les points de montage temporaires de systèmes de fichiers requis à un instant donné par l'administrateur ;  
**opt** => répertoire contenant les applications installées par-dessus le système d'exploitation minimal ;  
**run** => répertoire contenant les données gérées par le système depuis le démarrage, ce répertoire est ré-initialisé entre chaque démarrage ;  
**sbin** => répertoire contenant les commandes utilisées uniquement par l'administrateur (pas par le système) ;  
**srv** => répertoire contenant les données gérées par les services exploités sur le système ;  
**tmp** => répertoire servant de dépôt de fichiers temporaires pour le système, les utilisateurs et les administrateurs ;  
**usr** => répertoire complexe détaillé un peu plus loin.
**var** => répertoire contenant toutes les données variables du système, qu'elles soient produites par les utilisateurs, les administrateurs ou le système lui-même (comme les fichiers de traces).  

## Root

La norme ne stipule pas de répertoire /root. Or celui-ci est présent sur quasiment toutes les distributions Linux !  
Le répertoire/root est créé pour stocker “les données personnelles de l'administrateur”, mais il n'est pas indispensable pour faire démarrer le système et l'exploiter. Et stocker dans ce répertoire des données critiques pour le système est effectivement une erreur.  
Le compte root est le compte privilégié de Linux, il doit être réservé exclusivement aux tâches administratives sur le système. En aucun cas le compte root ne doit s'apparenter à un utilisateur “humain”. Ne jamais y stocker une boite de messagerie ou un env de travail.  

## Home

En fait, il l'est, mais de manière facultative également, et à y réfléchir, c'est assez normal : la FHS tend à normaliser l'emplacement des ressources exploitées par le système.  
Le répertoire /home est, par définition, très contextuel, ce qui le rend impossible à normaliser. Ainsi, sur tel serveur, vous n'aurez peut-être tout simplement pas de compte utilisateur… Du moins pas de compte nécessitant un répertoire personnel de stockage de données. Sur tel autre serveur à objectif de partage de fichier, au contraire, vous en aurez une multitude.  
FHS précise néanmoins que les fichiers de configuration nécessaires aux utilisateurs qui souhaitent exploiter des applications et des programmes doivent être stockés dans un sous-répertoire de/home désigné par le login du compte utilisateur, préfixé d'un point'.'.  

## Usr

Ce répertoire est devenu avec le temps une arborescence majeure des distributions Linux. Il contient lui-même des répertoires bin et sbin dans lesquels se situent également des commandes !  
Résumons un peu la logique de tous ces répertoires contenant des commandes :  

**/bin**: ce sont les commandes critiques pour le bon fonctionnement du système, quel que soit son objectif. Elles sont lancées par le système et par l'administrateur ;  
**/sbin**: ce sont les commandes uniquement à destination de l'administrateur pour la gestion du système.  
**/usr/bin**: ce répertoire contient majoritairement les commandes à destination de tous les utilisateurs du système, privilégiés ou non.  
**/usr/sbin**: ce sont des commandes à nouveau à destination unique de l'administrateur, mais non critiques pour le bon fonctionnement du système.  

Maintenant il existe aussi un répertoire /usr/local/bin! Ce dernier de la famille va contenir tous les binaires qui sont compilés manuellement par l'administrateur après l'installation du système.  
Le répertoire **/usr** est très important, il est marqué "shareable" et "static", ce qui implique que d'un système à l'autre, les éléments contenus dans ce répertoire sont censés fonctionner exactement de la même manière.  

## Var

L'objectif de ce répertoire est simple : stocker toutes les informations utilisateurs, administrateurs et systèmes variables.  
Normalement, avec une utilisation classique de **/var**, **/usr** devrait pouvoir être utilisé en lecture seule ! Ce qui est un gage de sécurité très important.  

Il y a quelques sous-répertoires de **/var** qu'il est important de mentionner :  

**/var/log** => répertoire contenant l'arborescence de toutes les traces systèmes et applicatives. C'est dans ce répertoire qu'il est possible de consulter les traces des historiques de démarrage du système, de connexion des comptes utilisateurs, d'activité des services réseaux (SSH, HTTPD, SMTP, etc.) ainsi que les traces du noyau. Généralement les applications installées sur le système disposent de leur propre sous-répertoire (/var/log/apache2par exemple).  
**/var/run** => répertoire contenant toutes les données relatives aux processus en cours d'exécution, les sémaphores, les données applicatives, les fichiers numéro de processus, etc.  
**/var/spool** => répertoire contenant des données stockées de manière temporaire entre processus. Souvent, ce répertoire est utilisé pour stocker des données relatives à des actions ou tâches à effectuer dans un futur proche par les processus en cours d'exécution.  
**/var/mail** => c'est le répertoire de stockage des messageries électroniques locales des comptes utilisateurs du système.  

Certains programmes vont stocker par défaut leurs données temporaires dans l'arborescence **/var**. Ainsi, le serveur web Apache HTTPD par exemple, lorsqu'il est installé via les packages des distributions majeures est configuré avec un docroot (répertoire contenant par défaut les sources des sites web) pointant vers **/var/www**.
Ce qui fait que :  
* certains sous-répertoires de/var seront marqués **variablesunshareable** (exemple /var/log)
* alors que d'autres seront marqués **variablesshareable** (comme /var/mail ou /var/www).  

# Identifiez le rôle des systèmes de fichiers virtuels de Linux

Traditionnellement, il existe aussi sur les systèmes Linux des arborescences un peu particulières. Elles correspondent à une organisation des informations maintenues en temps réel par le noyau Linux, sous la forme d'une arborescence.  
Imaginez la vitrine d'un magasin, le noyau met à disposition beaucoup d'informations, elles sont visibles (certaines accessibles uniquement en lecture seule). Mais pour certaines d'entre elles, il est possible de rentrer dans la boutique pour les manipuler.  
Il est ainsi possible de changer certaines variables du noyau, et donc certains comportements du système global en modifiant le contenu de ces fichiers “virtuels” placés dans ces arborescences.  
Ces arborescences n'existent pas sur périphérique physique de type bloc, et l'analyse indépendante du disque d'un système Linux ne les fera pas apparaître. Elles existent uniquement parce que le noyau vous les propose gracieusement.

## Le répertoire /proc

Cette arborescence contient toutes les informations concernant le processus ! Et il y en a beaucoup…
Pour lister le contenu de cette arborescence, lancez la commande suivante : `ls /proc`  
Vous pouvez remarquer que **/proc** présente aussi des fichiers et des répertoires. Je vous propose d'observer un peu plus dans le détail quelques fichiers intéressants.  
Par exemple, **/proc/cpuinfo** contient les informations sur le(s) processeur(s) maintenues par le noyau. Pour consulter ce fichier, utilisez la commande `cat` telle que:

    seb@thor:~$ cat /proc/cpuinfo
    processor : 0
    vendor_id : GenuineIntel
    cpu family : 6
    model : 94
    model name : Intel(R) Xeon(R) CPU E3-1220 v5 @ 3.00GHz
    ...

Et pourtant, lorsque vous lancez la commande `file` sur ce même fichier :

    seb@thor:~$ file /proc/cpuinfo
    /proc/cpuinfo: empty

Ces fichiers étant virtuels, ils ont une taille de 0.
D'autres fichiers sont intéressants à relever dans cette arborescence :  

**/proc/version** contient la version exacte du noyau en exécution,  
**/proc/meminfo** les informations détaillés sur la mémoire vive gérée par le noyau,  
**/proc/uptime** le temps d'exécution cumulé,  
**/proc/cmdline** les paramètres passés au démarrage du noyau, etc.  
**/proc** contient également beaucoup de répertoires, dont la grande majorité porte des noms à base de chiffres.En effet, tous les processus en exécution sur le système sont identifiés par un numéro unique géré par le noyau.
Ainsi ce dernier met à disposition les informations concernant chaque processus dans le répertoire portant son numéro associé.  

Observons par exemple le contenu du répertoire **/proc/1** qui est le premier processus du noyau :

    seb@thor:~$ cat /proc/1/cmdline
    /lib/systemd/systemd--system--deserialize18

Vous obtenez ici le premier processus lancé par le noyau => **systemd**, le programme d'initialisation principal de Linux (le résultat de cette commande peut varier en fonction des distributions).  
**/sys**: cette seconde arborescence fonctionne sur le même principe que sa petite sœur **/proc**. Elle présente des informations maintenues en temps réel par le noyau. À une différence fondamentale près :  
certains éléments de cette arborescence sont accessibles en écriture aux comptes privilégiés du système et notamment les variables systèmes du noyau dans le répertoire **kernel**.  

Cette arborescence contient les informations sur les périphériques gérés par le noyau, notamment :  
* les périphériques de type bloc ou caractères dans les répertoires **/sys/block** ou **/sys/dev**,
* les drivers dans **/sys/devices**,
* les différents systèmes de fichiers dans **/sys/fs**,
* les modules du noyau dans **/sys/module**.

Le répertoire **/sys/kernel** contient une arborescence de fichiers représentant des variables du noyau accessibles en écriture et permettant de modifier le comportement à chaud du système. Par exemple, le répertoire **/sys/kernel/debug** contient des fichiers permettant d'activer des fonctions de traces et de débogage du noyau.  

Sur les distributions principales de Linux, le répertoire **/proc/sys** est également accessible en écriture sur certains paramètres. En effet, d'un point de vue historique, seule l'arborescence **/proc** existait. **/sys** a été ajoutée à partir des versions 2.6 du noyau, notamment pour différencier la gestion des informations concernant les périphériques.  

############################################################################################################
############################################################################################################
# Visualisez des fichiers

Etant donné que Linux est un système d'exploitation orientée fichier, vous allez passer votre temps à consulter ces fichiers pour administrer votre serveur. Linux fournit des outils permettant de visualiser le contenu de ces fichiers.

## Affichez le contenu des fichiers

J'ai utilisé le mot-clé “sortie” pour évoquer les données transmises à l'écran sur le terminal par une commande.  Sous Linux, cette notion est conceptualisée avec des canaux (streams).

Dans la majorité des cas, tous les programmes exécutés sous Linux disposent de 3 canaux de données :

* stdin(pour standard input) : c'est le canal de l'entrée standard, et par défaut, lorsque vous lancez une commande, c'est votre clavier. La commande sera éventuellement capable de lire les informations saisies avec le clavier via ce canal. Il porte le descripteur de fichier numéro 0 ;

* stdout(pour standard output) : c'est le canal de la sortie standard, et lorsque vous lancez une commande depuis un terminal, c'est l'écran par défaut. Le résultat et les données affichées par la commande sont diffusés sur l'écran. Il porte le descripteur de fichier numéro 1 ;

* stderr(pour standard error) : c'est le canal du flux concernant les erreurs, et par défaut, lorsque vous lancez une commande, c'est aussi l'écran. La commande va différencier les données “normales” des données “erreur” et peut changer de canal pour diffuser ces informations.

stdin (0) ------> Programme ------> stdout (1)  
                      |-----------> stderr (2)

Pour manipuler ces canaux on utilise les chevrons:  
simples **>** et **<**,  
ou doubles **>>** et **<<**.  

En fait `cat /dossier/fichier` revient a taper `cat < /dossier/fichier` et meme pour etre plus precis `cat 0< /dossier/fichier` (l'argument **/dossier/fichier** est en realite ici le canal d'entree '0').
Ce qui sort de cette commande (le canal de sortie '1') s'affiche par defaut dans le terminal mais on pourrait decider de l'envoyer dans un fichier comme suit: `cat /dossier/fichier 1> /dossier/fichier sortie` et la rien ne s'affichera dans le terminal car on a redirige la sortie dans un fichier et pour en voir le contenu il nous faudrait faire `cat /dossier/fichier sortie`. Nous pourrions meme decider de prendre en compte les erreurs en faisant `cat /dossier/fichier 1> /dossier/fichier sortie 2> /dossier/fichier sortie erreur`. Il est possible bien evidement d'afficher deux fichiers le contenu de deux fichiers la suite avec `cat /dossier/fichier1 /dossier/fichier2`. Imaginons maintenant que nous voulions envoyer le contenus de ces deux fichiers dans un seul fichier. On pourrait se dire qu'il faudrait faire `cat /dossier/fichier1 > /dossier/fichier sauvegarde` et ensuite `cat /dossier/fichier2 > /dossier/fichier sauvegarde`, si on l'affiche maintenant patatra on s'appercoit qu'il n'y a que le contenue du fichier2 dans le fichier de sauvegarde car la deuxieme commande a ecrasee la premiere. Pour pallier a ca il faut faire `cat /dossier/fichier1 > /dossier/fichier sauvegarde` **puis** `cat /dossier/fichier2 >> /dossier/fichier sauvegarde`, ici lors de la deuxieme commande l'emplois des doubles chevrons indique que la sortie doit etre ajoutee a la suite et non depuis le debut en ecrasant ce qui pourrait se trouver avant>.

## Filtrer le contenu des fichiers

Très souvent vous n'aurez besoin que d'une partie de l'information affichée à l'écran suite à l'exécution d'une commande.  
Par exemple sur la commande suivante :

    seb@thor:~$ cat /etc/os-release
    PRETTY_NAME="Debian GNU/Linux 9 (stretch)"
    NAME="Debian GNU/Linux"
    VERSION_ID="9"
    VERSION="9 (stretch)"
    ID=debian
    HOME_URL="https://www.debian.org/"
    SUPPORT_URL="https://www.debian.org/support"
    BUG_REPORT_URL="https://bugs.debian.org/"

Vous pourriez souhaiter récupérer uniquement la ligne contenant le champ **NAME** pour simplement connaître la distribution que vous exploitez. Pour cela, vous allez utiliser la commande `grep`. Cette commande permet de filtrer le flux de données selon un motif passé en paramètre, exemple:

`grep -n debian /etc/os-release` va afficher:

    6:ID=debian
    7:HOME_URL="https://www.debian.org/"
    8:SUPPORT_URL="https://www.debian.org/support"
    9:BUG_REPORT_URL="https://bugs.debian.org/"

ici '-n' est une option qui affiche le numero de ligne ou se trouve 'debian'.  
`grep -ni debian /etc/os-release` => 'i' pour insensible a la case, 'debian' ou 'Debian'  
`grep -nio debian /etc/os-release` => 'o' pour isoler juste le pattern 'debian' sans avoir ce qu'il y a autour  
`grep -rnio debian /etc/*` => 'r' pour filter de maniere recurssive sur tout les fichiers dans le rep **/etc**  

Pour les deux commandes suivantes, il existe une petite bataille de geeks entre :  

les administrateurs pro commande sed;  
et les administrateurs pro commande awk.  
Souvent les utilisateurs de sed s'appliqueront à tout faire avec cette commande. Ce qui est vrai également pour les utilisateurs de awk.  

Ces deux commandes sont très appréciées des administrateurs car elles permettent de réaliser des opérations sur les flux de données, fichiers, entrée et sortie de manière non interactive. Les deux s'appuyant sur les expressions régulières, qu'il est intéressant de rappeler ici.

Une expression régulière est la modélisation d'un motif dans un flux de données à l'aide de méta-caractères, c'est-à-dire de caractères particuliers auxquels on ajoute une expression ou un opérateur.

Parmi les méta-caractères les plus couramment utilisés on peut retrouver :

`.` => Le point remplace n'importe quel caractère (hors retour chariot), par exemple l'expression régulière suivante : S.B, pourrait modéliser SEB ou SAB ou encore SSB, etc.  

`?` => Le point d'interrogation indique que l'expression modélisée peut être présente 0 ou 1 fois. Par exemple, S.?B, pourrait correspondre à SB ouSEB, mais pas SEEB  

`*`  => L'étoile fonctionne comme le ?, mais autorise 0 ou n fois l'expression, par exemple S.* pourrait modéliser S.*B, mais aussi SEB, mais aussi SAEIOUYB  

`+` => Petit dernier de la famille, il permet de modéliser au moins une fois (1 ou n).  

`^` => Nous l'avons vu précédemment en exemple, il permet de modéliser la première position, le début.  

`$` => À l'inverse, ici, permet de modéliser la dernière position, la fin.  

`[]` => Les crochets, accompagnés souvent de `-` permettent de modéliser un jeu de caractères, par exemple [a-z] pour modéliser l'ensemble des caractères minuscules de l'alphabet.  
Il est possible également d'utiliser le caractère `^` avec les crochets, qui a alors une autre signification et permet d'omettre une expression. Par exemple [^abc], modélise tous les caractères sauf a, b et c.  

La commande sed peut utiliser ces expressions régulières pour transformer un flux de données à la volée de manière non interactive (sed signifie Stream EDitor). Très pratique pour les traitements automatiques.  


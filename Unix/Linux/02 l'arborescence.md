#################################################################################################
#################################################################################################
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

#################################################################################################
#################################################################################################
# Visualisez des fichiers

Etant donné que Linux est un système d'exploitation orientée fichier, vous allez passer votre temps à consulter ces fichiers pour administrer votre serveur. Linux fournit des outils permettant de visualiser le contenu de ces fichiers.

## Affichez le contenu des fichiers

J'ai utilisé le mot-clé “sortie” pour évoquer les données transmises à l'écran sur le terminal par une commande.  Sous Linux, cette notion est conceptualisée avec des canaux (streams).

Dans la majorité des cas, tous les programmes exécutés sous Linux disposent de 3 canaux de données :

* stdin(pour standard input) : c'est le canal de l'entrée standard, et par défaut, lorsque vous lancez une commande, c'est votre clavier. La commande sera éventuellement capable de lire les informations saisies avec le clavier via ce canal. Il porte le descripteur de fichier numéro 0 ;

* stdout(pour standard output) : c'est le canal de la sortie standard, et lorsque vous lancez une commande depuis un terminal, c'est l'écran par défaut. Le résultat et les données affichées par la commande sont diffusés sur l'écran. Il porte le descripteur de fichier numéro 1 ;

* stderr(pour standard error) : c'est le canal du flux concernant les erreurs, et par défaut, lorsque vous lancez une commande, c'est aussi l'écran. La commande va différencier les données “normales” des données “erreur” et peut changer de canal pour diffuser ces informations.

![alt text](./png/image-1.png)

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

`?` => Le point d'interrogation indique que l'expression modélisée peut être présente 0 ou 1 fois. Par exemple, S.?B, pourrait correspondre à SB ou SEB, mais pas SEEB  

`*`  => L'étoile fonctionne comme le ?, mais autorise 0 ou n fois l'expression, par exemple S.* pourrait modéliser S.*B, mais aussi SEB, mais aussi SAEIOUYB  

`+` => Petit dernier de la famille, il permet de modéliser au moins une fois (1 ou n).  

`^` => Nous l'avons vu précédemment en exemple, il permet de modéliser la première position, le début.  

`$` => À l'inverse, ici, permet de modéliser la dernière position, la fin.  

`[]` => Les crochets, accompagnés souvent de `-` permettent de modéliser un jeu de caractères, par exemple [a-z] pour modéliser l'ensemble des caractères minuscules de l'alphabet.  
Il est possible également d'utiliser le caractère `^` avec les crochets, qui a alors une autre signification et permet d'omettre une expression. Par exemple [^abc], modélise tous les caractères sauf a, b et c.  

La commande `sed` peut utiliser ces expressions régulières pour transformer un flux de données à la volée de manière non interactive (sed signifie Stream EDitor). Très pratique pour les traitements automatiques.  

exemple de transformation de flux:  
`sed 's/Debian/Ubuntu/' /dossier/fichier`  
Cette commande va remplacer tout les paterns 'Debian' par 'Ubuntu' dans le fichier 'fichier'  
`sed 's/[D|d]ebian/Ubuntu/' /dossier/fichier`  
cas meme prendre les 'Debian' ou les 'debian'  
Si on veut reellement l'executer dans un fichier on peux faire:  
`sed 's/[D|d]ebian/Ubuntu/' /dossier/fichier > /dossier/fichier sauvergarde`  
Il est meme possible avec l'option **-i** de modifier directement dans le fichier:  
`sed -i 's/[D|d]ebian/Ubuntu/' /dossier/fichier`  
On peux aussi recuperer seulement une partie du fichier avec l'option '-n' comme suit:  
`sed -n 2,6p /dossier/fichier`  
'2,6p' veut dire print la ligne 2 a 6  

## enchainer les commandes

Maintenant que vous maîtrisez les différents canaux de données, entrée et sortie standard et erreur, ainsi que les différentes commandes permettant de filtrer un flux selon un motif, il est temps de passer à la vitesse supérieure et d'utiliser toutes ces notions en même temps.  

Pour cela, Linux met à votre disposition une fonction permettant de lier entre eux les canaux de données des différentes commandes : **le pipe** (ou tube / tuyau).  
Le principe est simple : il s'agit ici de rediriger un flux, en sortie d'une commande, vers le canal d'entrée de la commande suivante. Et ainsi de suite.  
Pour lier ces commandes entres elles, on utilise le caractère **|** (prononcé pipe). Il correspond à la séquence de touches `ALTGR+6` sur les claviers standards français.

Ainsi il est possible d'écrire quelque chose comme :  

    commande options arguments | commande options arguments | commande options arguments | ...

par exemple:  
`cat /dossier/fichier | grep thomas`  
Cette commande va rediriger la sortie std de `cat` vers l'entree de `grep`. Ne va s'afficher du coup que les lignes de 'fichier' contenant 'thomas'  
On pourrait se dire quel est l'interet ? Pourquoi ne pas utiliser directement `grep` ? Et bien l'avantage c'est qu'on peut faire des traitements avec `cat` avant ou meme cumuler du coup un certain nombre de commande, exemple:  
`cat /dossier/fichier | grep nologin | grep -E "[0-9][0-9]"`  
Ici on filtre deux fois a la suite du coup. On pourrait meme trier:  
`cat /dossier/fichier | grep nologin | grep -E "[0-9][0-9]" | sort`  

#################################################################################################
#################################################################################################
# Copiez, déplacez et supprimez des fichiers sous Linux

Vous voilà équipé pour éditer un fichier sous Linux. Il est temps de se pencher sur la manipulation des fichiers, c'est-à-dire :  
* la copie
* le déplacement
* la suppression  

Pour bien comprendre ces manipulations et les commandes associées, une petite introduction sur le concept de fichier sous Linux me paraît nécessaire.   
Linux est construit autour de la philosophie de fichier, si vous comprenez cette philosophie, vous aurez tout compris à Linux !  

Sans entrer trop dans le détail, un fichier est une structure du langage C définie directement au niveau du code noyau de Linux. Oui ! Ne soyez pas choqué, ce lien pointe vers le code C officiel du noyau Linux !
Cette structure est nommée inode. Elle peut se représenter par une liste de champs illustrée généralement sous la forme d’un tableau, que l'on va étudier par dézooms successifs.  

Regardons de près l'inode, le fichier donc. On y voit ses informations (sa taille, son propriétaire et groupe propriétaire, ses permissions, la date de ses derniers accès (lecture, modification), etc.) :  

![alt text](./png/image.png)

L’adresse contenue dans la ligne 14 renvoie à un nouvel inode ou bloc de pointeurs de 128 lignes.  Chacune des adresses contenues dans ces lignes renvoient vers un nouvel inode contenant à nouveau 128 lignes (oui c’est énorme !) Et chaque adresse contenue dans chaque ligne renvoie vers un bloc de données. On dit que ces blocs de donnés sont doublement indirects :  

![alt text](./png/image-2.png)

Je vous laisse déduire pour la ligne 15... on parle ici de triple redirection !  
Très simplement, on pourrait résumer la chose comme ça :  

![alt text](./png/image-3.png)

En fait, il faut se rendre compte que toutes ces différentes vues sont des niveaux de zoom sur un même fichier, qui grossit au fur et à mesure qu’on va loin dans les redirections.  

Cette commande affiche les inodes dans ce repertoire:  

    thomas@hp-pavillon:~/Bureau/projets/Docs/Unix/Linux$ ls -li
    total 44
    25586161 -rw-rw-r-- 1 thomas thomas 25988 juil. 13 15:13 "l'arborescence.md"
    25590258 -rw-rw-r-- 1 thomas thomas     0 juil.  6 14:46 'la supervision.md'
    25590252 -rw-rw-r-- 1 thomas thomas     0 juil.  6 14:45 'le reseau.md'
    25194250 -rw-rw-r-- 1 thomas thomas  4748 juil. 12 11:17 'le terminal.md'
    25694243 drwxrwxr-x 2 thomas thomas  4096 juil. 13 15:10  png
    25186062 -rw-rw-r-- 1 thomas thomas  1493 mai    3 14:34  vi.md

Tout a gauche se trouvent les inodes le premier => '25586161' par exemple.

Il faut differencier les liens des liens symboliques:  
* `ln fichier1 fichier2` va produire un lien, c a d que les deux fichiers aurons le meme inodes et si on modifie **fichier2**, **fichier1** sera impacte et du coup modifie aussi.  
* `ln -s fichier1 fichier2` va quant a elle produire un lien symbolique comme suit:  

    25586161 -rw-rw-r-- 1 thomas thomas 25988 juil. 12 15:13 "fichier1"  
    ...  
    25694256 lrwxrwxrwx 1 thomas thomas  4096 juil. 13 15:10  fichier2 -> fichier1

Comme on peut le voir la pour le coup l'inode est different. Le lien symbolique est un peu comme un raccourcit et du coup dans l'inode du lien symbolique on a pas les donnees de fichier1 mais juste son adresse vers laquelle il pointe.  

En resume les liens augmentent les occurences d'un fichier avec le meme inode alors que les liens symboliques sont des objets a part entiere et crees des references supplementaires a un meme fichier.

#################################################################################################
#################################################################################################
# Les Droits

Sous Linux, tout est fichier.  
Bien entendu, les données sont stockées dans des fichiers, mais les périphériques sont aussi des fichiers, les disques, les cartes réseau, les répertoires, la représentation des processus, etc. Il est donc primordial de comprendre la gestion des droits associée à ces fichiers.  
Le principe fondamental de la gestion des droits sous Linux est le **Discretionary Access Control** dit **DAC**.  

## Appréhendez le principe régissant les droits sous Linux

Le contrôle d'accès sous les systèmes Unix, et par héritage sous Linux, est dit “discrétionnaire“ : tous les objets (répertoires, fichiers, processus, etc.) sont la propriété d'un compte utilisateur ou système, ainsi que d'un groupe de comptes utilisateurs et/ou système.  

Les droits associés à ces objets sont donc définis pour :

* Le propriétaire de l'objet
* Le groupe propriétaire de l'objet
* Tous les autres soit comptes utilisateurs et/ou système qui ne sont pas le compte et le groupe propriétaire.  

L'aspect discrétionnaire de la gestion de ces droits réside dans le fait que le propriétaire de l'objet (ainsi que le super utilisateur root) peut directement gérer les droits associés à cet objet.  

Selon cette norme, un utilisateur peut donc créer, modifier ou supprimer ses propres objets, et définir quels autres comptes utilisateurs peuvent accéder en lecture ou modification à cet objet.  

Associée à la présence d'un compte super utilisateur, généralement root, cette gestion de droits reste finalement assez simple. Mais on peut alors lui reprocher son manque de granularité. Par exemple, un processus lancé par un utilisateur hérite de ses droits même si ce processus n'en a pas forcément besoin.  

## Maîtrisez le triplets des droits sous Linux

Les droits sous Linux sont définis à l'aide de 3 bits :

1. Un bit à la position 2, le droit "read" => r
2. Un bit à la position 1, le droit "write" => w
3. Un bit à la position 0, le droit "execute" => x

Et nous avons vu ci-dessus que les droits étaient exprimés :

* pour le propriétaire noté u (pour "user") ;
* pour le groupe propriétaire noté g (pour "group") ;
* et enfin pour tous les autres, notés eux o (pour "others" comme un très bon film d’ailleurs).

Vous pouvez en déduire une expression générale des droits sur un objet à l'aide de 9 bits, répartis en 3 groupes de 3 dans l'ordre suivant :

1. rwx pour u
2. rwx pour g
3. rwx pour o 

soit apres un "ls" dans le terminal on obtient par exemple:

    25586161 -rw-rw-r-- 1 thomas thomas 25988 juil. 12 15:13 "fichier1"

Ici "fichier1" appartient a thomas (u) et le groupe thomas (g) avec les droits "read" et "write" desssus et que les autres (o) quant a eux ne peuvent que le lire "read". Si je voulais accorder le droit en execution a thomas je devrais faire la commande **chmod**:

    thomas@hp-pavillon:~$ chmod u+rwx fichier1

Attention ceci n'est possible que parceque je me suis connecte en tant que "thomas" et que je suis le proprietaite de ce fichier, si le fichier1 avait ete la propriete de l'utilisateur "root" une erreur de droit aurrai ete levee.

## Simplifiez la gestion des droits avec leur valeur numérique

Une autre facon plus rapide de proceder au lieu de taper 3 fois la commande pour gerer les troi utilisateurs different est de proceder ainsi grace a cette norme:

    - - -  ->  000  ->  0+0+0  ->  0
    - - x  ->  001  ->  0+0+1  ->  1
    - w -  ->  010  ->  0+2+0  ->  2
    - w x  ->  011  ->  0+2+1  ->  3
    r - -  ->  100  ->  4+0+0  ->  4
    r - x  ->  101  ->  4+0+1  ->  5
    r w -  ->  110  ->  4+2+0  ->  6
    r w x  ->  111  ->  4+2+1  ->  7

du coup on peut faire maintenant:

    thomas@hp-pavillon:~$ chmod 644 fichier1

chaque chiffre representant un user soit : Root-User-Other  

## Changez le propriétaire d’un fichier sous Linux

La seconde commande importante concernant la gestion des droits sous Linux est **chown** "change owner", pour modifier le proprietaire du fichier. Le seul a pouvoir faire cette manipulation est d'etre **Root**.

    root@hp-pavillon:/home/thomas# chown jean:thomas fichier1

Il faut comprendre le proprio "jean" a la place de "thomas"

On peut de la meme maniere changer le **groupe** proprietaire en faisant:

    root@hp-pavillon:/home/thomas# chgrp thomas fichier1

On peut meme changer les proprios de tout les fichiers d'un rep avec l'argument -R:

    root@hp-pavillon:/home/thomas# chown -R jean:thomas *

Attention tout les fichiers du rep "thomas" vont devenir la propriete de l'utilisateur "jean" mais aussi les fichiers de repertoire sous-jacent... A manipuler donc avec precaution.  

## Manipulez les droits spéciaux sous Linux

Vous connaissez désormais les droits standard sous Linux, mais il existe deux droits spéciaux supplémentaires que je vous propose d'analyser :

1. Le premier de ces droits particuliers se nomme le **SetUID bit**, et son petit frère le **SetGID bit**. Ce droit permet notamment d’exécuter un fichier avec les droits de son propriétaire ! C’est très important, car de nombreux aspects de la gestion des droits sous Linux utilisent cette propriété fondamentale.

2. Le second est le **Sticky Bit**(le "bit collant"). Ce droit est une tentative de gestion d'espaces collaboratifs, proposé par la branche BSD de Unix au milieu des années 80 (même si une version antérieure de cette fonctionnalité existait déjà sur Unix dès les années 70, mais pas du tout avec le même objectif).

et je vous propose d’illustrer le Sticky Bit avec son plus fervent représentant : le répertoire /tmp!

Par exemple lorsque l'on change son mot de passe avec la commande **passwd** c'est le **SetUID bit** qui est a l'oeuvre:

    thomas@hp-pavillon:~$ passwd

Il permet momentanement d'executer une ecriture dans un fichier normalement ferme d'acces en ecriture a un utilisateur autre que root. Lorsque l'on vas voir le fichier de cette commande on a dailleur:

    -rwsr-xr-x 1 root root 63960 7 fevr. 2020 /bin/passwd

On voit ici que tout le monde peut executer cette commande (le dernier 'x' en temoigne) et que lorsqu'on le lance grace au bit 's', en lieu et place de 'x' de root, on vas heriter des droits du compte proprietaire 'root'. Pour donner cette fonctionnalite a une commande, on procede comme suit:

    chmod 4755 fichier_de_ma_commande

C'est le chiffre des milliers '4' qui le permet. En fait cette fonctionalite permet d'executer une modification momentanement par le biais ici de 'fichier_de_ma_commande' qui vas permettre cette modification (definit dans le script du fichier) sur un fichier sensible qui serait la propriete du user et du groupe 'root' par exemple.  

Le **Sticky Bit** sert a partager un fichier propriete du user et groupe 'thomas' par exemple en laisant le droit de lecture d'ecriture aux autres sans qu'ils puissent pour autant le supprimer car habituellement le droit en ecriture 'w' le permet.
Pour appliquer a un fichier cette propriete tapper la commande:

    chmod 1744 fichier_de_ma_commande

C'est le chiffre des milliers '1' qui permet cette modification. Si on regade maintenant ce fichier on verra apparaitre un 'T' en lieu et place du 'x' des autres utilisateurs:

    -rwxr--r-T 1 thomas thomas 63961 7 fevr. 2020 fichier_de_ma_commande

# Le Terminal

## Les terminaux
Linux propose 7 terminaux physiques accessibles lorsque l'on est en presence du serveur. Ils sont geres via sa console avec les combinaisons de touches CTRL+ALT+F1 a F7.
En presence du serveur on utilise donc les 7 et en s'y connectant a distance via le reseau on utilise un emulateur de terminal, un programme que l'on lance sur son OS, tel que BASH, ZSH, Powershell, etc...
Le rôle principal du shell est d'exécuter les commandes saisies par l'administrateur lui permettant d'effectuer des appels systèmes vers le noyau.
Par exemple, la possibilité de traiter de manière automatique les résultats des commandes saisies, ou encore de rediriger ces informations dans des fichiers ou vers d'autres commandes.
Le shell exécuté lors de la connexion d'un utilisateur sur un terminal est configuré dans le fichier  /etc/passwd.

Taper cette commande pour afficher le shell utilise par thomas: 
    grep thomas /etc/passwd
Qui donne:
"thomas:x:1000:1000:thomas,,,:/home/thomas:/bin/bash"
Le shell exécuté à la connexion de l'utilisateur est indiqué dans le dernier champ (les champs sont séparés par des :).

thomas@hp-pavillon:~$
'thomas' est l'utilisateur
'@' est un separateur
connecte a l'hote 'hp-pavillon'
'~' indique qu'on se situe dans le repertoire personnel de thomas.
'$' en tant qu'utilisateur non root (root -> '#')
Toute cette configuration est stockée dans un fichier **.bashrc** et dans une variable **$PS1** gérée par le shell.
Si on fait **echo $PS1** on obtient donc:
    \[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$
La commande echo ici affiche le contenu de deux variable  $PS1

## Les commandes de base

Il y a deux types de commandes, celles integrees a Linux qui possedent leur fichier executable et celles integrees au shell:
    thomas@hp-pavillon:~$ type echo
    echo est une primitive du shell
    thomas@hp-pavillon:~$ type bash
    bash est /usr/bin/bash

Afficher une variable `echo $SHELL` (afficher le shell utilise apres authentification)<br>
Afficher le dossier dans lequel on se trouve `pwd`<br>
Lister tout les fichers du dossier `ls`<br>
Afficher toutes les infos des fichiers `ls -l`<br>
Afficher touts les fichiers dont les masqués `ls -a`<br>
Afficher touts les fichiers dont les masqués en mode path `l -a`<br>
Créer un fichier `touch fichier.txt`<br>
Pour le copier `cp fichier.txt fichier_copie.txt`<br>
Pour le deplacer `mv fichier.txt new/path/`<br>
Pour le renomer `mv fichier.txt new_name.txt`<br>
Pour le vider `truncate -s0 fichier.txt`<br>
Pour le supprimer `rm fichier.txt`<br><br>
Créer un dossier `mkdir dossier`<br>
Pour le supprimer `rm -r dossier`<br>

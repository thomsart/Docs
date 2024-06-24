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
La commande echo ici affiche le contenu de de la variable $PS1
La variable **$PATH** contient tout les path des binaires donc des fichiers de commandes.
En faisant **export PATH=$PATH:/home/thomas/Bureau/projets/Tetris/** on rajoute tout les binaires executables qui se trouvent dans le repertoire 'Tetris' comme le 'main.py', du coup on pourra lancer de n'importe ou **Tetris** dans l'OS. en faisant **main**, a savoir que ce n'est pas un nom de commande tres pertinant bien sur. Sachant que cette commande la est rajoutee juste pour la session en cours, si on veut qu'elle soit persistante il faudra modifier le '.bashrc'

## Les commandes de base

Il y a deux types de commandes, celles integrees a Linux qui possedent leur fichier executable et celles integrees au shell:
    thomas@hp-pavillon:~$ type echo
    echo est une primitive du shell
    thomas@hp-pavillon:~$ type bash
    bash est /usr/bin/bash
**type** par exemple qui est une primitive du shell permet justement de s'en assurer.
Pour avoir des infos sur une commande integree au shell on fait:
    help la_commande
Pour celles qui sont integree a l'OS on fait:
    la_commande --help
Et si on desire plus d'info on peut aussi taper:
    man la_commande

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
Pour le supprimer `rm fichier.txt`<br>
Pour avoir les infos dessus `file /usr/bin/bash`<br>
Créer un dossier `mkdir dossier`<br>
Pour le supprimer `rm -r dossier`<br>

Il est possible d'executer plusieur commandes a la fois grace a **&&**, ex:
    cd /home/thomas/Bureau/projets && file *
Nous enmenera dans le dossier 'projets' et ensuite affichera tout les fichiers qui s'y trouvent.
La commande **id** affiche les informations du compte utilisteur connecte.

La commande **history** sert a afficher l'historique des commandes executees dans le shell.
Une fonctionnalite bien utile consiste a tapper **CTRL+r** et commencer a taper le debut d'une commande dont on se souvient vaguement le nom en utilisant **TAB**.
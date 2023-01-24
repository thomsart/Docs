## Manuel pour déployer sur Unix
>On présume ici que le projet à été cloné et que les dépendances sont installées sur notre espace serveur.

## 1.Diriger le trafic entrant:

Nginx est le serveur du VPS qui reçois tout le trafic entrant, en gros toutes les requêtes sont envoyées à l'adresse IP publique du serveur.  
Sa configuration par défaut se situe dans 'etc/nginx/sites-enabled/default'.
Nginx peut sur un même serveur gérer le trafic entrant/sortant de plusieurs sites.  
C'est pourquoi on créer un fichier de configuration par site dans le répertoire 'sites-available', on s'y rend et on le crée comme suit :

	sudo touch sites-available/mon_site

Une fois le fichier crée il faut ajouter le lien symbolique dans le répertoire 'sites-enabled' grâce à la commande 'ln' suivante:
>U+26A0 le chemin doit partir de la racine.

	sudo ln -s etc/nginx/sites-available/le_nom_du_fichier etc/nginx/sites-enabled 

Une fois le fichier et le lien crées, ne pas oublier de relancer le serveur pour qu'il prenne en compte les modifications:

	'sudo service nginx reload'.

## Servir du script Python:

Nginx n'étant pas fait pour interpreter le Python il nous faut maintenant un serveur Python afin de dialoguer avec lui: Gunicorn.  
Ce serveur (fait pour les projets Python déployés sur Unix comme Ubuntu) utilise les spécifications WSGI (Web Server Gateway Interface). Il est déjà dans le requirements de Django nativement.  
On peut le démarrer en tapant:

	gunicorn mon_projet.wsgi:application

Blabla...
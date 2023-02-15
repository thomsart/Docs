# Architecture d'un Projet

Ici est expliqué comment fonctionne un projet du point de vu de son architeture => les paquets et modules.  
Il est recommandé à la racine d'un projet de structurer par thematique.  
Un dossier (paquet) pour la base de donnée par exemple "data_base" dans lequel on y mettrai un *__init__.py* et d'autre modules comme *create_db.py* ou encore *populate_db.py*.  

Attention, seuls les paquets d'espace de nom ne doivent pas contenir ce fameux *__init__.py* car ils sont destinés à distribuer plusieurs projets comme django-rest pour le back par exemple et react pour le front pour le même espace (ici on dit espace mais en réalité ce serait le projet dans son ensemble qui en contiendrai d'autres plus petits).

## A la racine on a...

    env
    LICENCE.txt
    readme.md
    requirements.txt
    setup.cfg
    .gitignore
    app
        | __init__.py
        | classes.py
        | launch.py
        | model.py
        | tools.py
        manager
            | __init__.py
            | command.py
        db
            | __init__.py
            | create.py
            | model.py
            | populate.py
    tests
        | __init__.py
        app
            | __init__.py
            | test_classes.py
            | test_launch.py
            | test_model.py
            | test_tools.py
            manager
                | __init__.py
                | test_command.py
            db
                | __init__.py
                | test_create.py
                | test_model.py
                | test_populate.py


## Le .gitignore
> Voici un exemple d'un .gitignore de base

    env
    __pycache__/

## Comment importe-on ?

Voici la règle pour les imports dans les modules.  
`import module`  
ou  
`from module import function`  
ou  
`from package.souspackage.module import function`  
A éviter  
`from module import *`  
> La PEP8 interdit ce genre d'import tant pour des raisons de clarté que de probleme de résolution d'import.

Il est important de stipuler que dès lors que l'on importe un package, le code qui se trouve dans le *__init__.py* est éxécuté. De ce fait il peut être une bonne idée d'y mettre certaines variables ou autre script. A savoir que ce code n'est éxécuter qu'une seul et unique fois lors du runtime de l'appli, et ne s'éxécute pas 10 fois si il est importé 10 fois au total dans toute l'appli.

## Lancer un module

Comme vu précédement il est mieux d'oganiser son projet par paquet et d'y mettre les modules associés. On constate du coup que depuis la racine nous ne disposons pas nécessairement à porté de main de module de lancement tel que le fameux 'main.py' qui du coup peut être niché dans le souspaquet d'un paquet.  
On a du coup le réflexe de faire  
`python3 paquet/souspaquet/module.py`  
ce qui bien évidement génère une erreur d'import car le contexte de lancement n'est pas le même.  
La bonne pratique consiste donc à préciser à python qu'on le lance comme un module en faisant  
`python3 -m paquet.souspaquet.module`.  
>Ici c'est '-m' qui indique à python que c'est un module.

Du coup en faisant comme ceci on indique à python l'endroit de référence qui est l'endroit ou on éxécute la commande donc la racine du projet idéalement. Ce qui crée une total symétrie avec la référence des imports dans les modules et le répertoire courant 'cwd' (curent work directory) qui est la racine du projet.
# Architecture d'un Projet

Ici est expliqué comment fonctionne un projet du point de vu de son architeture => les paquets et modules.  
Il est recommandé à la racine d'un projet de structurer par thematique.  
Un dossier (paquet) pour la base de donnée par exemple "data_base" dans lequel on y mettrai un *__init__.py* et d'autre modules comme *create_db.py* ou encore *populate_db.py*.  

Attention, seuls les paquets d'espace de nom ne doivent pas contenir ce fameux *__init__.py* car ils sont destinés à distribuer plusieurs projets comme django-rest pour le back par exemple et react pour le front pour le même espace (ici on dit espace mais en réalité ce serait le projet dans son ensemble qui en contiendrai d'autres plus petits).

## A la racine on a...

    env
    .gitignore
    readme.md
    LICENCE.txt
    setup.cfg
    app
        | __init__.py
        | classes.py
        | launch.py
        | model.py
        | test.py
        | tools.py
        db
            | __init__.py
            | create.py
            | model.py
            | populate.py
            | test.py

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
on évite de faire  
`from module import *`  
>à éviter pour des raisons de lisibilité (PEP8)

Il est important de stipuler que dès lors que l'on importe un package, le code qui se trouve dans le *__init__.py* est éxécuté. De ce fait il peut être une bonne idée d'y mettre certaines variables ou autre script.
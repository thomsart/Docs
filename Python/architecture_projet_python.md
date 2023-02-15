# Architecture d'un Projet

Ici est expliqué comment fonctionne un projet du point de vu de son architeture => les paquets et modules.  
Il est recommandé à la racine d'un projet de structurer par thematique.  
Un dossier (paquet) pour la base de donnée par exemple "data_base" dans lequel on y mettrai un *__init__.py* et d'autre modules comme *create_db.py* etc.  

## Comment importe-on ?

`import module`  
ou  
`from module import function`  
on évite de faire  
`from module import *`  
>à éviter pour des raisons de lisibilité (PEP8)


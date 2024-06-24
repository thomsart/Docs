# Editeur de texte Vim  
> Ouvrir un fichier
    `vi fichier.txt`  

## Mode Saisie en tapant 'i'  
>Le mode saisie permet d'inserer des caracteres en faisant entree pour passer d'une ligne a l'autre. Si je veux modifier il faut que je sorte de ce mode. Attention dans ce mode on ne peut se deplacer avec les touches directionnelles habituelles.
    `i` y entrer
    `a` y entrer en mode append...
    `enter` pour sauter de ligne
    `esc` sortir du mode Saisie

## Mode Commande  
>En generale on passe du mode Saisie au mode Commande  

###### Les deplacement:
>Mot en mot
    `w` et `b`
>Debut ou fin
    `g g` et `G`

###### Les lettres et mots:
>Supprimer
    `x`
>Remplacer
    `r`
>Changer un mot depuis sa 1ere lettre
    `c w`

###### Les lignes:
>Ajouter une ligne au dessus
    `O`
>Ajouter une ligne au dessous
    `o`
>Supprimer la ligne sur laquelle on est
    `d d`
>Supprimer X lignes à partir de celle sous le curseur
    `X d d`
>Copier la ligne sur laquelle on est
    `y y`
>Copier plusieurs lignes a partir d'elle avec X le nombre de lignes a copier
    `X y y`
>Pour la ou les coller se mettre sur la ligne qui sera au dessus
    `p`

###### Les options du mode commande en tapant ':' puis:
>Numeroter les lignes
    `:set number`
>Aller directement sur une ligne X
    `:X`
>Aller des mots XXX en XXX
    `:/XXX` puis `n`
>Remplacer les XXX par YYY
    `:%s/XXX/YYY/g` le g ici mentionnent toutes les occurences

>Quitter vi
    `:q! enter`
    `:wq! enter` en sauvant
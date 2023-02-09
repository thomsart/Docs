""" Le but de ce module est de bien comprendre le mecanisme des decorateurs
"""

# Quand je declare une fonction je fais :
def mult(x, y):
    return x * y

# Je peux l'appeler comme suit :
resultat = mult(2, 5)
print(resultat)
# >> 10

# Maintenant si je l'appelle comme ca :
print(mult)
# >> <function mult at 0x00000246A9572B90>

# En realite mult n'est autre qu'une variable de la classe function à cette adresse précise.
# C'est un point qu'il ne faut pas oublier.

# Donc si je fais
x_by_y = mult
print(x_by_y)
# j'obtient >> <function mult at 0x00000246A9572B90>

# Maintenant si je fais
print(x_by_y(3, 10))
# >> 30

# Ca veut dire quoi ?
# Comme tout est objet en Python en rélité "x_by_y" tout comme
# "mult" sont les étiquettes (au même titre) du code "return x * y"

# Pour illustrer tout ça...
def mon_super_print(text):
    return print(text)
mon_super_print('hello world !')
# >> hello world !

# En conclusion, le nom d'une fonction n'est rien d'autre qu'une variable,
# et c'est important de garder ça en tête pour aborder les décorateurs.

# à partir de 29 min
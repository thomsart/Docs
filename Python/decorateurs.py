""" Le but de ce module est de bien comprendre le mecanisme des decorateurs
"""

from functools import wraps

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

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################


# Ce premier niveau sert à personnaliser le décorateur
# On prend l'exemple de messages à afficher ici
# mais ca peut être ce qu'on veut, une condition, une liste,
# un dictionnaire, un type d'erreurs à gérer etc
def decorator(pre_mess=None, then_mess=None):
    # Ce deuxième niveau prend notre fonction à décorer
    def internal_decorator(function):
        # Ce dernier niveau se charge de prendre les arguments passés à notre fonction décorée
        # Le décorateur @wraps sert à récuper le __name__ et __doc__ de notre fonction décorée
        @wraps(function)
        def wrapper(*args, **kwargs):

            print(pre_mess)

            returned_value = function(*args, **kwargs)

            print(then_mess)

            return returned_value

        return wrapper

    return internal_decorator



@decorator(pre_mess="Avant la fonction !!!", then_mess="Apres la fonction !!!")
def a_function():
    """La doc de ma fonction decorée."""
    return print("Ma fonction est réalisée.")


help(a_function)

print("#########################")

a_function()
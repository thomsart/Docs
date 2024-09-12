# Mise en place dans l'ordre

On ouvre un terminal et on se place à l'endroit ou on veut importer son projet avec la commande suivante :<br>
`git clone https://github.com/thomsart/monrepo.git`<br>
On créer ensuite son environement virtuel grâce à la commande :<br>
`python3 -m venv env`<br>
Maintenant on créer notre '.gitignore' pour ignorer ce qu'on souhaite lors des push :

    env
    __pycahe__/
    local.py

Si le requirements est déjà en place on peut importer les libs en tapant :<br>
`pip install -r requiremnts.txt`<br>
Lorsque l'on importe des libs on tape derrière :<br>
`pip freeze > requirements.txt`<br>
...


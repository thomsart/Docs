""" Dans ce module nous traiterons de toutes les choses importantes a savoir sur les classes ."""

import datetime


###############################################################################
###############################################################################
###############################################################################

class Vehicle:
    """ This class is used to represent a vehicle in a general form. """


    """ Les attributs statiques sont des attributs qui peuvent être utilisés 
    même si aucune instance de la classe où ils sont définis n'a été créée.
    Ces attributs sont partagés par toutes les instances. ex: """

    country = "England"
    total_vehicle = 0

    """ Les méthodes statiques sont des méthodes qui peuvent être appelées 
    même si aucune instance de la classe où elles sont définies n'a été 
    créée. Les méthodes statiques sont souvent employées pour créer des 
    instances spécifiques d'une classe. ex: """

    @staticmethod
    def in_wich_country():
        """ This static method allows to know the country where all cars 
        came from. """
        return print(f"All vehicle here came from {Vehicle.country}.")

    @staticmethod
    def nb_vehicles_in_circulation():
        """ This static method allows to know how many cars there is. """
        return print(f"There is {Vehicle.total_vehicle} vehicle in circulation.")

    def __init__(self):
        self.__class__.total_vehicle += 1
        self.build_year = datetime.date.today()
        self.driving_licence_required = True
        self.driving_licence_type = "B"
        self.energy = None
        self.color = None # can be "red"
        self.weight_kg = 1200
        self.seat_nb = 1
        self.nb_weels = None
        self.price = 0
        self.second_hand = False
        self.owner = None
        self.immatriculation = None
        self.kilometrage_counter = 0
        self.in_circulation = True
        self._private = "attribut privé"
                # en déclarant ce genre d'attribut en previens le developpeur
                # que cet attribut est privé et que l'on ne doit pas y acceder
                # directement par l'objet mais par une methode comme un getter
                # ou setter.

    @property
    def age(self):
        """ Les property servent à créer des attributs dynamique sous la forme
        de methode ayant le fonctionnement d'un attribut dans l'utilisation.
        On l'utilise lorsque un attribut évolue dans le temps. """
        return self.build_year

    @property
    def private(self):
        """ Le getter de l'attribut privé '_private'. """
        return self._private
    
    @private.setter
    def private(self, new_value):
        """ Le setter de l'attribut privé '_private'. """
        # traitement possible de 'new_value'
        self._private = new_value

    def sale_vehicle(self, new_owner):
        if self.owner != None:
            self.second_hand = True
        self.owner = new_owner

    def drive(self, km):
        self.kilometrage_counter + km

    def get_owner(self):
        if self.owner == None:
            if self.in_circulation == False:
                return print("This vehicle is now destroyed.")
            else:
                return print("This vehicle doesn't belongs to someone yet.")
        return print(f"This vehicle belongs to {self.owner}.")

    def sale(self, new_owner):
        self.owner = new_owner

    def destroy(self):
        """ Même si un attribut est statique, il peut être utilisé avec la 
        syntaxe self.attribut_statique dans une méthode non statique à 
        condition qu'un attribut non statique ne porte pas le même nom. """

        self.in_circulation = False
        self.owner = None
        self.__class__.total_vehicle -= 1

    def _private_methode(self):
        ...

    def __super_private_methode(self):
        ...


###############################################################################
###############################################################################
###############################################################################

class Car(Vehicle):
    """ Represent a car. """

    def __init__(self, constructor, type):
        super().__init__()
        self.constructor = None # "renault"
        self.type = None # "clio"


###############################################################################
###############################################################################
###############################################################################

class Bicycle(Vehicle):
    """ Represent a bicycle. """

    def __init__(self, constructor, type):
        Vehicle.__init__(self)
        self.constructor = None # "peugeot"
        self.type = None # "course"


###############################################################################
###############################################################################
###############################################################################


Vehicle.nb_vehicles_in_circulation()
first_vehicle = Car("peugeot", "3008")
first_vehicle.get_owner()
print(first_vehicle.age)
Vehicle.nb_vehicles_in_circulation()
second_vehicle = Vehicle()
Vehicle.nb_vehicles_in_circulation()
second_vehicle.get_owner()
second_vehicle.sale("George")
second_vehicle.get_owner()
second_vehicle.destroy()
second_vehicle.get_owner()
Vehicle.nb_vehicles_in_circulation()
Vehicle.in_wich_country()




"""

clio = Car()
dir(clio)
donne toutes les methodes spéciales de clio qui est un objet de ma classe Car() héritant de Vehicle()

__module__
Contient le nom du module dans lequel est incluse la classe (voir chapitre Modules).

__class__
Contient le nom de la classe de l’instance. Ce nom est précédé du nom du module suivi d’un point.

    L’attribut __class__ contient lui même d’autres d’attributs :

    __doc__
    Contient un commentaire associé à la classe (voir paragraphe Commentaires, aide.

    __dict__
    Contient la liste des attributs statiques (définis hors d’une méthode) et des méthodes (voir paragraphe Attributs statiques.

    __name__
    Contient le nom de l’instance.

    __bases__
    Contient les classes dont la classe de l’instance hérite (voir paragraphe Héritage.

__dict__
Contient la liste des attributs de l’instance (voir paragraphe Liste des attributs.

__doc__
Contient un commentaire associé à la classe (voir paragraphe Commentaires, aide.

"""
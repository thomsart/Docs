""" Dans ce module nous traiterons de toutes les choses importantes a savoir sur les classes ."""

import datetime
import random

###############################################################################
###############################################################################
###############################################################################

class Vehicle:
    """ Doc: This class is used to represent a vehicle in a general form. """



    """ Les attributs statiques sont des attributs qui peuvent être utilisés 
    même si aucune instance de la classe où ils sont définis n'a été créée.
    Ces attributs sont partagés par toutes les instances. ex: """
    country = "England"
    total_vehicle = 0



    """ Les méthodes statiques sont des méthodes qui peuvent être appelées 
    même si aucune instance de la classe où elles sont définies n'a été 
    créée. Ces méthodes ont une connexion logique avec la classe, 
    mais n'utilisent pas l'état de la classe ou de l'objet.
    On les utilise donc lorsque nous avons besoin de fonctionnalités non pas
    par rapport à un objet mais par rapport à la classe.
    C'est assez avantageux lorsque nous devons créer des méthodes utiles 
    car elles ne sont généralement pas liées au cycle de vie d'un objet.
    ex: """
    @staticmethod
    def stc_country_vehicles():
        """ This static method allows to know the country where all cars 
        come from. """
        return print(f"All vehicles come from {Vehicle.country}.")
    @staticmethod
    def stc_nb_vehicles():
        """ This class method allows to know how many cars there is. """
        return print(f"There is {Vehicle.total_vehicle} vehicles in circulation.")



    """ Les méthodes de classe sont souvent utilisées comme constructeurs 
    alternatifs ou comme méthodes de construction, c'est-à-dire pour créer 
    des instances basées sur différents cas d'utilisation. """
    @classmethod
    def cls_country_vehicles(cls):
        return print(f"All vehicles come from {cls.country}.")
    @classmethod
    def cls_nb_vehicles(cls):
        return print(f"There is {cls.total_vehicle} vehicles in circulation.")



    def __init__(self):
        # à chaque instance de classe créée héritant de Vehicle, on implèmente 'total_vehicle'
        Vehicle.total_vehicle += 1
        self.build_year = datetime.date.today()
        self.in_circulation = True
        self.driving_licence_type = [None, "A", "B", "AM", "C", "D", "E"]
        self.energy_type = ["muscular", "electric", "gasoil", "kerosene"]
        self.kilometrage_counter = 0
        self.second_hand = False
        self.owner = None
        self.price = 0
        self._immatriculation = "undefined"
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
    def immatriculation(self):
        """ Le getter de l'attribut privé '_immatriculation'. """
        return self._immatriculation

    @immatriculation.setter
    def immatriculation(self, new_immatriculation):
        """ Le setter de l'attribut privé '_immatriculation'. """
        # traitement possible de 'new_immatriculation' afin de s'assurer par
        # exemple que le numéro soit aux normes.
        self._immatriculation = new_immatriculation

    def sale(self, new_owner: str, price: int):
        if self.owner != None:
            self.second_hand = True
        self.owner = new_owner
        if self.immatriculation == "undefined":
            self.immatriculation = self.owner[0].lower() + self.owner[-1] + str(self.build_year)[4:] + "-" + str(random.randint(1, 99))
        self.price = price

    def drive(self, km: int):
        self.kilometrage_counter + km

    def get_owner(self):
        name = self.__class__.__name__
        if self.owner == None:
            if self.in_circulation == False:
                return print(f"This {name} is now destroyed.")
            else:
                return print(f"This {name} doesn't belongs to someone yet.")
        return print(f"This {name} belongs to {self.owner}.")

    def destroy(self):
        """ Même si un attribut est statique, il peut être utilisé avec la 
        syntaxe self.attribut_statique dans une méthode non statique à 
        condition qu'un attribut non statique ne porte pas le même nom. """

        self.in_circulation = False
        self.owner = None
        Vehicle.total_vehicle -= 1

    def _private_methode(self):
        ...

    def __superprivate_methode__(self):
        ...


###############################################################################
###############################################################################
###############################################################################

class Car(Vehicle):
    """ Represent a car. """

    def __init__(self, brand: str, model: str, color: str):
        super().__init__()
        self.constructor = brand # "ex: renault"
        self.type = model # "ex: clio"
        self.driving_licence = self.driving_licence_type[2] # "B"
        self.energy = self.energy_type[2] # "gasoil"
        self.color = color

###############################################################################
###############################################################################
###############################################################################

class Bicycle(Vehicle):
    """ Represent a bicycle. """

    def __init__(self, brand: str, model: str, color: str):
        Vehicle.__init__(self)
        self.constructor = brand # "ex: peugeot"
        self.type = model # "ex: course"
        self.driving_licence = self.driving_licence_type[0] # "None"
        self.energy = self.energy_type[0] # "muscular"
        self.color = color

###############################################################################
###############################################################################
###############################################################################

print("############################################")
Vehicle.stc_nb_vehicles()
print("############################################")
car_01 = Car("peugeot", "3008", "red")
car_01.get_owner()
print(car_01.age)
print("############################################")
Vehicle.cls_nb_vehicles()
bicycle_01 = Bicycle("peaugeot", "vtt", "white")
print("############################################")
Vehicle.stc_nb_vehicles()
print("############################################")
bicycle_01.get_owner()
print(bicycle_01.immatriculation)
bicycle_01.sale("George", 1000)
print(bicycle_01.immatriculation)
bicycle_01.get_owner()
bicycle_01.destroy()
bicycle_01.get_owner()
print("############################################")
Vehicle.cls_nb_vehicles()
print("############################################")
Vehicle.stc_country_vehicles()
print("############################################")
Vehicle.cls_country_vehicles()




"""

clio = Car()
dir(clio)
donne toutes les methodes spéciales de clio qui est un objet de ma classe Car() héritant de Vehicle()

__module__
Contient le nom du module dans lequel est incluse la classe (voir chapitre Modules).

__class__
Contient le nom de la classe de l'instance. Ce nom est précédé du nom du module suivi d'un point.

    L'attribut __class__ contient lui même d'autres d'attributs :

    __doc__
    Contient un commentaire associé à la classe (voir paragraphe Commentaires, aide.

    __dict__
    Contient la liste des attributs statiques (définis hors d'une méthode) et des méthodes (voir paragraphe Attributs statiques.

    __name__
    Contient le nom de l'instance.

    __bases__
    Contient les classes dont la classe de l'instance hérite (voir paragraphe Héritage.

__dict__
Contient la liste des attributs de l'instance (voir paragraphe Liste des attributs.

__doc__
Contient un commentaire associé à la classe (voir paragraphe Commentaires, aide.

"""
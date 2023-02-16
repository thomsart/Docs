""" Dans ce module nous traiterons de toutes les choses importantes a savoir sur les classes ."""

import datetime



class Vehicle:
    
    def __init__(self):
        self.build_year = datetime.date.today()
        self.driving_licence_required = True
        self.driving_licence_type = "B"
        self.color = None # can be "red"
        self.weight_kg = 1200
        self.seat_nb = 1
        self.price = 0
        self.kilometrage_counter = 0
        self.second_hand = False


class Car(Vehicle):

    def __init__(self, constructor, type):
        self.constructor = None # "renault"
        self.type = None # "clio"
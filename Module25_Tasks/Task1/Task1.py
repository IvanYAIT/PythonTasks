class Property:
    def __init__(self, worth):
        self.worth = worth

    def count_tax(self):
        pass

class Car(Property):
    def count_tax(self):
        return self.worth * 0.02
    
class Appartment(Property):
    def count_tax(self):
        return self.worth * 0.001

class CountryHouse(Property):
    def count_tax(self):
        return self.worth * 0.05
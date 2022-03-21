from sympy import *

class Formula:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def set_formula(self, formula):
        """
        accept the latex string and store it by Sympy's equation type
        """
        pass

    

if __name__ =='__main__':
    print('Formula test')
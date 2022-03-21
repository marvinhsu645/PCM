from Circuit import Circuit
from Formula import Formula

class PCM:
    def __init__(self, name):
        self.circuit = Circuit()
        self.formula = Formula()
    
    def set_circuit(self, circuit):
        pass

    def set_formula(self, formula):
        pass

    def get_derived_value(self, value):
        """
        return the derived value by provided formulas
        """
        pass

    def check_restriction(self, **conditions):
        """
        check if the conditions violate the restriction
        """
        pass

linear_ramp = PCM('Linear Ramp')

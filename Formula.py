from sympy import latex
from sympy.parsing.latex import parse_latex
import sympy_latex as SL

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

    def get_derrived_value(self, **sources):
        """
        accept the sources using dictionary and calculate the derrived value by sympy
        """
        pass

    def check_constraint(self, **conditions):
        """
        accept the conditions using dictionary and check the constraint by constraint solver
        """
        pass

if __name__ =='__main__':
    print('Formula test')

    formula = Formula('Formula_test')
    formula.set_formula(r"I_C=\frac{V_{\CC}-V_E}{R_E}")
    formula.get_derrived_value()


    # parse_eq = parse_latex(r"I_C=\frac{V_{\CC}-V_E}{R_E}")

    # for i in parse_eq.args:
    #     SL.check_symbol(i)
        
    # print(latex(SL.formula_dict('I_{C}', {'V_{E}':20, 'V_{C*C}':30})))
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

    

if __name__ =='__main__':
    print('Formula test')
    parse_eq = parse_latex(r"I_C=\frac{V_{\CC}-V_E}{R_E}")

    for i in parse_eq.args:
        SL.check_symbol(i)
        
    print(latex(SL.formula_dict('I_{C}', {'V_{E}':20, 'V_{C*C}':30})))
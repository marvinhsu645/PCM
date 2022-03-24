from sympy.parsing.latex import parse_latex
from sympy import I, symbols, Eq, solve
from sympy import *
from sympy.physics.units import convert_to

all_symbols = {}

def check_symbol(expr):
    if isinstance(expr, Symbol):
        globals()[str(expr)] = expr
        all_symbols[str(expr)] = expr
        return
    elif isinstance(expr, (Mul, Add)):
        for i in expr.args:
            check_symbol(i)
    elif isinstance(expr, Pow):
        globals()[str(expr.base)] = expr.base
        all_symbols[str(expr.base)] = expr.base
    # else:
    #     print(expr)
    #     print(type(expr))

def eq_subs(target, eq):
    for target_symbol, target_expr in target.items():
        eq = eq.subs(target_symbol, target_expr)
    return eq

# test eq_subs
# print(eq_subs({'I_{C}':20, 'V_{C*C}':30}, parse_eq))

def formula_dict(target_unit, source):
    eq = parse_eq
    solve(eq, all_symbols[target_unit])[0]
    for source_new_symbol, source_expr in source.items():
        eq = eq.subs(source_new_symbol, source_expr)
    return eq    


if __name__=='__main__':
    # Eq(I_{C}, (V_{C*C} - V_{E})/R_{E})
    # Eq(I_{C}, (V_{C*C} - V_{E})/R_{E})
    parse_eq = parse_latex(r"I_C=\frac{V_{\CC}-V_E}{R_E}")

    for i in parse_eq.args:
        check_symbol(i)
        
    print(latex(formula_dict('I_{C}', {'V_{E}':20, 'V_{C*C}':30})))
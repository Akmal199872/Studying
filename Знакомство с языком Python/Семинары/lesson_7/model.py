import sympy


def evaluate_expression(exp):
    x = sympy.Symbol('x')
    return sympy.solve(exp, x)

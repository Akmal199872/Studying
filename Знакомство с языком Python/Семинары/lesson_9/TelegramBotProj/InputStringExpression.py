import ast
import operator as op
import cmath as cm

# print(dir(cm))
# print("Выбран расчёт комплексных чисел:")
#
# print(cm.sqrt(-9))
# j = -1
# z = 5 + 7j
# print(abs(z))
# phi = cm.phase(z)
# print(phi)
# qphi = m.degrees(phi)
# print(qphi)
# print(m.radians(qphi))
# print(cm.polar(z))
# print(cm.rect((cm.polar(z)[0]), (cm.polar(z)[1])))
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}


def eval(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval(node.left), eval(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval(node.operand))
    else:
        raise TypeError(node)


def calculate_plus():
    expr = input("Введите уравнение: ")
    return eval(ast.parse(expr, mode='eval').body)



# print(cm.sqrt(calculate_plus()))

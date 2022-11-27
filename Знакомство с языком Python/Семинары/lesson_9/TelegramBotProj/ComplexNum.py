import InputStringExpression as ise
import cmath as cm


def choose_func():
    list_activities = dir(cm)
    result = 0
    for i, j in enumerate(list_activities, start=1):
        print(f'№{i} = Функция: "{j}"')
    function_number = int(input("Выберите необходимую функцию: "))
    match function_number:
        case 1:
            result = cm.__doc__(ise.calculate_plus())
        case 2:
            result = cm.__loader__(ise.calculate_plus())
        case 3:
            result = cm.__name__(ise.calculate_plus())
        case 4:
            result = cm.__package(ise.calculate_plus())
        case 5:
            result = cm.__spec__(ise.calculate_plus())
        case 6:
            result = cm.acos(ise.calculate_plus())
        case 7:
            result = cm.acosh(ise.calculate_plus())
        case 8:
            result = cm.asin(ise.calculate_plus())
        case 9:
            result = cm.asinh(ise.calculate_plus())
        case 10:
            result = cm.atan(ise.calculate_plus())
        case 11:
            result = cm.atanh(ise.calculate_plus())
        case 12:
            result = cm.cos(ise.calculate_plus())
        case 13:
            result = cm.cosh(ise.calculate_plus())
        case 14:
            result = cm.e(ise.calculate_plus())
        case 15:
            result = cm.exp(ise.calculate_plus())
        case 16:
            result = cm.inf(ise.calculate_plus())
        case 17:
            result = cm.infj(ise.calculate_plus())
        case 18:
            result = cm.isclose(ise.calculate_plus())
        case 19:
            result = cm.isinfinite(ise.calculate_plus())
        case 20:
            result = cm.isinf(ise.calculate_plus())
        case 21:
            result = cm.isnan(ise.calculate_plus())
        case 22:
            result = cm.log(ise.calculate_plus())
        case 23:
            result = cm.log10(ise.calculate_plus())
        case 24:
            result = cm.nan(ise.calculate_plus())
        case 25:
            result = cm.nanj(ise.calculate_plus())
        case 26:
            result = cm.phase(ise.calculate_plus())
        case 27:
            result = cm.pi(ise.calculate_plus())
        case 28:
            result = cm.polar(ise.calculate_plus())
        case 29:
            result = cm.rect(ise.calculate_plus())
        case 30:
            result = cm.sin(ise.calculate_plus())
        case 31:
            result = cm.sinh(ise.calculate_plus())
        case 32:
            result = cm.sqrt(ise.calculate_plus())
        case 33:
            result = cm.tan(ise.calculate_plus())
        case 34:
            result = cm.tanh(ise.calculate_plus())
        case 35:
            result = cm.tau(ise.calculate_plus())
    return result

# print(choose_func())


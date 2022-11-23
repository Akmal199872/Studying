import model
# from logger import log_expression, log_ans
import logger

def get_expression():
    return input()


def show_res(a):
    print(a)


exp = get_expression()
logger.log_expression(exp)
answer = model.evaluate_expression(exp)
logger.log_ans(answer)
show_res(answer)

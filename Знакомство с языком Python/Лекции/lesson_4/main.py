import random
import controller
import htmlCreator
import xmlGenerator

def IntroTask(number):
    print(f"\nЗадача №{number}\n")


IntroTask(1)


def attempt_first():
    listArray = [random.randint(1, 9) for i in range(2)]
    print(sum(listArray))


attempt_first()


def attempt_second():
    sum = lambda a, b: a + b
    print(sum(6, 8))


attempt_second()

controller.button_click()


IntroTask(2)

print(htmlCreator.create())
print(xmlGenerator.create())
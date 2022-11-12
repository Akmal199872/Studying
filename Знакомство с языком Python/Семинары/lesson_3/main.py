def IntroTask(number):
    print("\nЗадача №", number, "\n")


IntroTask(1)

from datetime import datetime


def rand(seed):
    now = datetime.now()
    return int(now.microsecond) % 10


print(rand(3))

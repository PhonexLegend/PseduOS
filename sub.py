from calc import calc
from env import env
import time

def sub(num1, num2):
    s = num1 - num2
    print("The difference of", num1, "and", num2, "is", s )
    print("_________________________________________")
    time.sleep(3)
    print("Choose from the following: ")
    a = print("a. Return to calculator")
    b = print("b. Return to Desktop environment")

    u = input("Your Choice: ")

    if u == 'a':
        print("Returning to calculator... ")
        time.sleep(3)
        print("____________________________________")
        return calc()

    elif u == 'b':
        print("Returning to desktop environment... ")
        time.sleep(3)
        print("_____________________________________")
        return env(nn)

    else:
        exit()



nn = (" ")


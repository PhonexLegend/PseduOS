import time
from env import env

def calc():
    print("-------------------------------------------------------------------------------")
    time.sleep(3)
    print("Welcome to Calculator!")
    time.sleep(3)
    print("Loading Calculator... ")
    time.sleep(2)
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Choose from the following opertations: ")

    a = print("a. Add")
    b = print("b. Subtract")
    c = print("c. Multiply")
    d = print("d. Divide")
    e = print("e. All listed operations at once")

    u = input("Your Choice: ")

    if u == 'a':
        from add import add
        print(add(num1, num2))

    elif u == 'b':
        from sub import sub
        print(sub(num1, num2))

    elif u == 'c':
        from multy import multy
        print(multy(num1, num2))

    elif u == 'd':
        from div import div
        print(div(num1, num2))

    elif u == 'e':


        print("Sum is: ", num1 + num2)
        time.sleep(2)
        print("Difference is: ", num1 - num2)
        time.sleep(2)
        print("Product is: ", num1 * num2 )
        time.sleep(2)
        print("Division is: ", num1/num2)

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
        return env



nn = (" ")

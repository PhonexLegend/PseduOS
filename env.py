import time
import sys

def env(nn):
    print('welcome to the desktop tty ')
    a = print("a. Load applications: ")
    b = print("b. Shutdown")
    u = input("Your choice: ")

    if u == 'a':
        print("Loading App manager... ")
        time.sleep(2)
        a = print("a. Utilities")
        b = print("b. Games")
        u = input("Your Choice: ")

        if u == 'a' or 'A':
            from calc import calc
            print("Loading Utilities...")
            time.sleep(3)
            print("Choose from the following utilities: ")
            a = print("a. Calculator")

            u = input('Your choice: ')

            if u == 'a':
                print(calc())

            else:
                return env(nn)




    elif u == 'b':
        print("Shutting down...")
        time.sleep(3)
    return exit()

enn = print("  ")

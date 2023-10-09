import pyfiglet
import time
from login import login
from boot import boot
from env import env

splash_scrn = pyfiglet.figlet_format("PseduOS", font = "doh" )
print(splash_scrn)
time.sleep(3)

print("Choose from the following:  ")

a = print("a. Boot PseduOS")
b = print("b. Exit")

u = input("Your choice: ")

if u == 'a' or 'A':
    n1 = print("Welcome to PseduOS...")
    print(boot(n1))
    time.sleep(2)

    n = print("Loading login Screen... ")
    time.sleep(1)
    print(login(n))
    print("Logging in... ")
    time.sleep(1)

    nn = print("Loading Environment... ")
    time.sleep(2)
    print(env(nn))


else:
    exit()

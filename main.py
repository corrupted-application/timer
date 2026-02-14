from win11toast import toast
import time
import os
from rich import print
from rich.prompt import Prompt

def cls():
    os.system('cls')

def title(title):
    os.system('title ' + title)

while True:
 cls()
 title("CorruptedApplication Timer")
 print("[yellow]Welcome to Corrupted Application Timer!\n")
 wait = Prompt.ask("[blue]Type when to ring (in seconds)")
 cls()
 print("Idle. Will ring in " + str(wait) + " seconds.")
 time.sleep(int(wait))
 cls()
 print("Ring ring ring")
 toast('The timer is up!')
 time.sleep(3)
 quitting = Prompt.ask("[blue]Do you want to quit? (y/n)")
 if quitting == "y":
     break
     cls()
     exit()
 elif quitting == "n":
     cls()
cls()
exit()

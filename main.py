from win11toast import toast
import time
import os
from rich import print
from rich.prompt import Prompt

def cls():
    os.system('cls')

def title(window_title):
    os.system('title ' + window_title)

while True:
 cls()
 title("CorruptedApplication Timer")
 print("[yellow]Welcome to Corrupted Application Timer!\n")
 while True:  
     wait = Prompt.ask("[blue]Type when to ring (in seconds)")
     if wait.isdigit():
         wait = int(wait)
         break
     else:
         print("[red]Please enter a valid number")
 cls()
 print("Idle. Will ring in " + str(wait) + " seconds.")
 time.sleep(wait)
 cls()
 print("Ring ring ring🔔")
 toast('The timer is up!')
 time.sleep(3)
 quitting = Prompt.ask("[blue]Do you want to quit? (y/n)")
 if quitting == "y":
     break
 elif quitting == "n":
     cls()
cls()
exit()

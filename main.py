from win11toast import toast
import time
import os
from rich import print
from rich.prompt import Prompt

def cls():
    os.system('cls')

def title(title):
    os.system('title ' + title)

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
print("Quitting in 5 seconds...")
time.sleep(5)
cls()
exit()

import os
import time

def cls():
    os.system('cls')

def title(title):
    os.system('title ' + title)

cls()
title("CorruptedApplication Timer Configure")
print("Starting dependency install process...")
time.sleep(3)
cls()
title("CorruptedApplication Timer Configure Installing Dependencies")
os.system("pip install rich win11toast")
cls()
print("Done. Quitting in 3 seconds...")
time.sleep(3)
exit()

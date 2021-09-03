import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import pyautogui as pag

import config
import dark_castle
import infernal

pag.FAILSAFE = config.PAG_FAILSAFE
game_counter = 0

if config.PAG_FAILSAFE:
    print("Drag your mouse to the top left corner of the screen to activate the Failsafe")
else:
    print("Warning: Failsafe is turned off!")

# Check if MelonLoader is installed
if Path(config.MELON_LOADER_C_DRIVE).is_file():
    btd6_directory = config.BTD6_DIRECTORY_C_DRIVE

elif Path(config.MELON_LOADER_D_DRIVE).is_file():
    btd6_directory = config.BTD6_DIRECTORY_D_DRIVE

# And if MelonLoader isn't in default install locations, tell the user to input the directory
else:
    print("Couldn't find MelonLoader")
    btd6_directory = input("Type in the path to your BTD6 directory where MelonLoader is installed (include BloonsTD6.exe in the end)")
    if Path(btd6_directory).is_file():
        pass

print("MelonLoader is installed\nLaunching...")
print("Make sure you have Speedhack mod in your Mods folder!")

# Launch BTD6
subprocess.Popen(btd6_directory)
time.sleep(17.5) # Wait just to make sure they in da menu

pag.click(962, 1000)
time.sleep(5)
pag.click(961, 733)

# XP, Monkey Money and Time Calculator
counter = pag.prompt(text="How many times would you like to complete this map? (Must type a whole number)", title="bruh")
extra_mm_unlocked = pag.confirm(text="Have you unlocked the Mo' Monkey Money Knowledge?", buttons=["Yes", "No"], title="MONKE")
map = pag.confirm("What map do you want to farm on?", buttons=["Infernal", "Dark Castle"], title="this game is ridiculous")
if extra_mm_unlocked == "Yes":
    mk_m = int(counter) * 66
else:
    mk_m = int(counter) * 60
xp = int(counter) * float(59731)

# HMTDIT = How Much Time Does It Takes
hmtdit = 14.89 * float(counter)

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

print(f"Monkey Money: {mk_m}\nXP: {xp}")
usure = pag.confirm(text=f"Do you want to start farming? (Pressing no will terminate the process)\nEstimated Time: {convert(hmtdit)}\nMonkey Money: {mk_m} | XP: {xp}", buttons=["Yes", "No"])
if usure == "Yes":
    pass

elif usure == "No":
    print("Terminating Python process! (BloonsTD6 will not be terminated)")
    sys.exit()

def delay():
    return np.random.uniform(0.5, 0.75)

time.sleep(1)
while True:
    if game_counter == int(counter):
        break
    game_counter += 1
    pag.click(841, 929)
    time.sleep(delay())
    pag.click(1319, 978)
    time.sleep(delay())
    if map == "Infernal":
        infernal.launch()
        infernal.main()
    elif map == "Dark Castle":
        dark_castle.launch()
        dark_castle.main()

pag.alert(text=f"Done!\nYou earned {xp} XP and {mk_m} Monkey Money in {counter} run(s)!", title="Autofarm is done!", button="Let's GOOOOO!")
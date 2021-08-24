import subprocess
import time
from pathlib import Path
import pyautogui as pag
import sys
import numpy
import config

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

def delay():
    if config.FAST_MODE == True:
        return numpy.random.uniform(0.075, 0.125)
    else:
        return numpy.random.uniform(0.1, 0.2)

# Launch BTD6
subprocess.Popen(btd6_directory)
time.sleep(17.5) # Wait just to make sure they in da menu

pag.click(962, 1000)
time.sleep(5)
pag.click(961, 733)

# XP, Monkey Money and Time Calculator
counter = pag.prompt(text="How many times would you like to complete this map? (Must type a whole number)", title="bruh")
extra_mm_unlocked = pag.confirm(text="Have you unlocked the Mo' Monkey Money Knowledge?", buttons=["Yes", "No"])
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
    print("Launching Infernal | Deflation Mode")

elif usure == "No":
    print("Terminating Python process! (BloonsTD6 will not be terminated)")
    sys.exit()

time.sleep(1)
while True:
    if game_counter == int(counter):
        break
    game_counter += 1
    pag.click(841, 929)
    time.sleep(0.5)
    pag.click(1319, 978)
    time.sleep(0.5)
    # In-case golden bloon wants to mess with OpenCV which happened to me :(
    pag.click(544, 557)
    time.sleep(0.5)
    pag.click(615, 403)
    time.sleep(0.5)
    pag.click(1281, 441)
    time.sleep(0.5)
    pag.click(1137, 717)
    time.sleep(5)
    pag.click(968, 762)
    time.sleep(1)

    # Deflation strat + loop
    pag.press(config.NINJA_MONKEY)
    pag.moveTo(837, 366, duration=delay())
    pag.click(clicks=2, interval=delay())
    pag.press(config.UPGRADE_1, presses=4, interval=delay())
    pag.press(config.UPGRADE_3, presses=2, interval=delay())
    time.sleep(delay())
    pag.press("esc")
    time.sleep(delay())
    pag.press(config.NINJA_MONKEY)
    pag.moveTo(832, 699, duration=delay())
    pag.click(clicks=2, interval=delay())
    pag.press(config.UPGRADE_1, presses=4, interval=delay())
    pag.press(config.UPGRADE_3, presses=2, interval=delay())
    pag.press("esc")
    time.sleep(delay())
    pag.press(config.ALCHEMIST_MONKEY)
    pag.moveTo(832, 766, duration=delay())
    pag.click(clicks=2, interval=delay())
    pag.press(config.UPGRADE_1, presses=4, interval=delay())
    pag.press("esc")
    time.sleep(delay())
    pag.press(config.ALCHEMIST_MONKEY)
    pag.moveTo(833, 290, duration=delay())
    pag.click(clicks=2, interval=delay())
    pag.press(config.UPGRADE_1, presses=4, interval=delay())
    pag.press("esc")
    time.sleep(delay())
    pag.press(config.FAST_FORWARD, presses=2, interval=delay())
    pag.press("9")
    time.sleep(10)
    pag.click(944, 900)
    time.sleep(0.5)
    pag.click(796, 857)
    time.sleep(3)

pag.alert(text=f"Done!\nYou earned {xp} XP and {mk_m} Monkey Money in {counter} run(s)!", title="Autofarm is done!", button="Let's GOOOOO!")
import subprocess
import time
from pathlib import Path
import pyautogui
import sys
import numpy

pyautogui.FAILSAFE = True

print("You can drag your mouse to the top left corner of your screen if you want to")
print("terminate the Python process or press Ctrl+C in the commandline")

# MelonLoader Locations
cDriveModLibrary = "C:/Program Files (x86)/Steam/steamapps/common/BloonsTD6/version.dll"
dDriveModLibrary = "D:/SteamLibrary/steamapps/common/BloonsTD6/version.dll"

# BTD6 Locations
cDriveLibrary = "C:/Program Files (x86)/Steam/steamapps/common/BloonsTD6/BloonsTD6.exe"
dDriveLibrary = "D:/SteamLibrary/steamapps/common/BloonsTD6/BloonsTD6.exe"

# Check if MelonLoader is installed
if Path(cDriveModLibrary).is_file():
    btd6_directory = cDriveLibrary
    print("MelonLoader is installed\nLaunching...")
    print("Make sure you have Speedhack mod in your Mods folder!")

elif Path(dDriveModLibrary).is_file():
    btd6_directory = dDriveLibrary
    print("MelonLoader is installed\nLaunching...")
    print("Make sure you have Speedhack mod in your Mods folder!")

# And if MelonLoader isn't in default install locations, tell the user to input the directory
else:
    print("Couldn't find MelonLoader")
    btd6_directory = input("Type in the path to your BTD6 directory where MelonLoader is installed (include BloonsTD6.exe in the end)")
    if Path(btd6_directory).is_file():
        print("MelonLoader is installed\nLaunching...")
        print("Make sure you have Speedhack mod in your Mods folder!")

# Launch BTD6 with Mods and wait 12.5 cause that's around how long it will take to launch
# BTD6 on an average PC
subprocess.Popen(btd6_directory)
time.sleep(14.25)

#BTD6 Automatic Map Launch
start_button = None
print("Looking for Start Button...")
while start_button == None:
    if start_button != None:
        print("Found Start Button")
        break
    start_button = pyautogui.locateCenterOnScreen("./resources/start_button.png", confidence=0.8)

pyautogui.click(start_button)
time.sleep(5)
pyautogui.click(955, 716)

# XP, Monkey Money and Time Calculator
counter = pyautogui.prompt(text="How many times would you like to complete this map? (Must type a whole number)", title="bruh")
extra_mm_unlocked = pyautogui.confirm(text="Have you unlocked the Mo' Monkey Money Knowledge?", buttons=["Yes", "No"])
if extra_mm_unlocked == "Yes":
    mk_m = int(counter) * 66
else:
    mk_m = int(counter) * 60
xp = int(counter) * float(59731)

# HMTIT = How Much Time It Takes
hmtit = 17.89 * float(counter)

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

print(f"Monkey Money: {mk_m}\nXP: {xp}")
usure = pyautogui.confirm(text=f"Do you want to start farming? (Pressing no will terminate the process)\nEstimated Time: {convert(hmtit)}\nMonkey Money: {mk_m} | XP: {xp}", buttons=["Yes", "No"])
if usure == "Yes":
    print("Launching Infernal | Deflation Mode")

elif usure == "No":
    print("Terminating Python process! (BloonsTD6 will not be terminated)")
    sys.exit()

# Random delay between 0.1 and 0.3 seconds
delay = numpy.random.uniform(0.1, 0.3)

n = 0
while True:
    if n == int(counter):
        break
    n += 1
    pyautogui.click(837, 938)
    time.sleep(delay)

    pyautogui.click(1340, 970)
    time.sleep(delay)

    pyautogui.click(517, 562)
    time.sleep(delay)

    pyautogui.click(618, 414)
    time.sleep(delay)

    pyautogui.click(1280, 466)
    time.sleep(5)

    pyautogui.click(952, 765)
    time.sleep(1)

    # Deflation strat + loop
    pyautogui.press("D")
    pyautogui.moveTo(837, 366)
    pyautogui.click(clicks=2, interval=0.2)
    pyautogui.click(323, 490, clicks=4, interval=0.2)
    pyautogui.click(340, 788, clicks=2, interval=0.2)
    time.sleep(delay)
    pyautogui.press("esc")
    time.sleep(delay)
    pyautogui.press("D")
    pyautogui.moveTo(832, 699)
    pyautogui.click(clicks=2, interval=0.2)
    pyautogui.click(1585, 483, clicks=4, interval=0.2)
    pyautogui.click(1542, 784, clicks=2, interval=0.2)
    pyautogui.press("esc")
    time.sleep(delay)
    pyautogui.press("F")
    pyautogui.moveTo(832, 766)
    pyautogui.click(clicks=2, interval=0.2)
    pyautogui.click(1585, 483, clicks=4, interval=0.2)
    pyautogui.press("esc")
    time.sleep(delay)
    pyautogui.press("F")
    pyautogui.moveTo(833, 290)
    pyautogui.click(clicks=2, interval=0.2)
    pyautogui.click(1585, 483, clicks=4, interval=0.2)
    pyautogui.press("esc")
    time.sleep(delay)
    pyautogui.press("space")
    time.sleep(delay)
    pyautogui.press("space")
    time.sleep(delay)
    pyautogui.press("9")
    time.sleep(10)
    pyautogui.click(945, 917)
    time.sleep(1)
    pyautogui.click(796, 857)
    time.sleep(3)

# Alert the user in-case they didn't check the commandline and see if the program has finished
pyautogui.alert(text=f"Done!\nYou earned {xp} XP and {mk_m} Monkey Money in {counter} run(s)!", title="Autofarm is done!", button="Let's GOOOOO!")
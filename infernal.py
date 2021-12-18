import time

import numpy as np
import pyautogui as pag
import pydirectinput as pagg

import config


def delay():
    if config.FAST_MODE == True:
        return np.random.uniform(0.075, 0.125)
    else:
        return np.random.uniform(0.125, 0.2)


def launch_delay():
    return np.random.uniform(0.5, 1)
        

def launch():
    pag.click(512, 566)
    time.sleep(launch_delay())
    pag.click(637, 558)
    time.sleep(launch_delay())
    pag.click(1276, 442)
    time.sleep(launch_delay())
    pag.click(1122, 720)
    time.sleep(3)
    pag.click(942, 757)
    time.sleep(3)


def level_detection():
    img = config.LEVEL_UP_BUTTON
    counter = 0
    while True:
        if counter == 10:
            break
        x = pag.locateCenterOnScreen(img, confidence=0.9)
        if x == None:
            counter += 1
            pass
        elif x != None:
            time.sleep(0.5)
            pag.click(x, clicks=2, interval=delay())
            time.sleep(0.5)
            pagg.press("space")
            if counter < 3:
                counter += 7
            elif counter > 5:
                counter += 3
            else:
                pass
            time.sleep(counter)
            break
        time.sleep(1)


def map_completed():
    hb = config.HOME_BUTTON
    nb = config.NEXT_BUTTON
    counter = 0
    while True:
        if counter == 10:
            break
        x = pag.locateCenterOnScreen(nb, confidence=0.9)
        if x == None:
            counter += 1
            pass
        elif x != None:
            time.sleep(0.5)
            pag.click(x)
            time.sleep(1)
            y = pag.locateCenterOnScreen(hb, confidence=0.9)
            time.sleep(0.5)
            pag.click(y)
            time.sleep(3)
            break
    time.sleep(1)


def main():
    pagg.press(config.NINJA_MONKEY)
    pag.moveTo(837, 366, duration=delay())
    pag.click(clicks=2, interval=delay())
    pagg.press(config.UPGRADE_1, presses=4, interval=delay())
    pagg.press(config.UPGRADE_3, presses=2, interval=delay())
    time.sleep(delay())
    pagg.press("esc")
    time.sleep(delay())
    pagg.press(config.NINJA_MONKEY)
    pag.moveTo(832, 699, duration=delay())
    pag.click(clicks=2, interval=delay())
    pagg.press(config.UPGRADE_1, presses=4, interval=delay())
    pagg.press(config.UPGRADE_3, presses=2, interval=delay())
    pagg.press("esc")
    time.sleep(delay())
    pagg.press(config.ALCHEMIST_MONKEY)
    pag.moveTo(832, 766, duration=delay())
    pag.click(clicks=2, interval=delay())
    pagg.press(config.UPGRADE_1, presses=4, interval=delay())
    pagg.press("esc")
    time.sleep(delay())
    pagg.press(config.ALCHEMIST_MONKEY)
    pag.moveTo(833, 290, duration=delay())
    pag.click(clicks=2, interval=delay())
    pagg.press(config.UPGRADE_1, presses=4, interval=delay())
    pagg.press("esc")
    time.sleep(delay())
    pagg.press(config.FAST_FORWARD, presses=2, interval=delay())
    pagg.press("9")
    level_detection()
    map_completed()
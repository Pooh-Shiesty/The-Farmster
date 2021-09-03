import pyautogui as pag
import time
import numpy as np
import config

def delay():
    if config.FAST_MODE == True:
        return np.random.uniform(0.075, 0.125)
    else:
        return np.random.uniform(0.125, 0.2)
        
def launch():
    pag.click(1650, 439)
    time.sleep(delay())
    pag.click(956, 265)
    time.sleep(delay())
    pag.click(637, 558)
    time.sleep(delay())
    pag.click(1276, 442)
    time.sleep(delay())
    pag.click(1122, 720)
    time.sleep(5)
    pag.click(942, 757)
    time.sleep(delay())


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
            pag.press("space")
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
    pag.press(config.NINJA_MONKEY)
    pag.moveTo(709, 427, duration=delay())
    pag.click(clicks=2, interval=delay())
    pag.press(config.UPGRADE_1, presses=4, interval=delay())
    pag.press(config.UPGRADE_3, presses=2, interval=delay())
    time.sleep(delay())
    pag.press("esc")
    time.sleep(delay())
    pag.press(config.NINJA_MONKEY)
    pag.moveTo(797, 433, duration=delay())
    pag.click(clicks=2, interval=delay())
    pag.press(config.UPGRADE_1, presses=4, interval=delay())
    pag.press(config.UPGRADE_3, presses=2, interval=delay())
    pag.press("esc")
    time.sleep(delay())
    pag.press(config.NINJA_MONKEY)
    pag.moveTo(852, 444, duration=delay())
    pag.click(clicks=2, interval=delay())
    pag.press(config.UPGRADE_1, presses=4, interval=delay())
    pag.press(config.UPGRADE_3, presses=2, interval=delay())
    pag.press("esc")
    time.sleep(delay())
    pag.press(config.ALCHEMIST_MONKEY)
    pag.moveTo(747, 379, duration=delay())
    pag.click(clicks=2, interval=delay())
    pag.press(config.UPGRADE_1, presses=4, interval=delay())
    pag.press(config.UPGRADE_3, interval=delay())
    pag.press("esc")
    time.sleep(delay())
    pag.press(config.HERO_MONKEY)
    pag.moveTo(921, 435, duration=delay())
    pag.click()
    time.sleep(delay())
    pag.press(config.SNIPER_MONKEY)
    pag.moveTo(1477, 524, duration=delay())
    pag.click(config.SNIPER_MONKEY, clicks=2, interval=delay())
    pag.click(91, 382)
    pag.press("esc")
    time.sleep(delay())
    pag.press(config.FAST_FORWARD, presses=2, interval=delay())
    pag.press("9")
    level_detection()
    map_completed()
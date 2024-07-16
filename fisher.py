import os
import time

import cv2
import mss
import numpy as np
import pyautogui
from termcolor import colored

LAST_HIT_TIMEOUT = 60
MATCH_THRESHOLD = 0.9

def get_time_string(current_time):
    return time.strftime("%H:%M:%S", time.localtime(current_time))

def main():
    if not os.path.exists("image.png"):
        print(colored("Did not create image.png. Make sure to take screenshot and save in this folder.", "red"))
        return

    screen_width, screen_height = pyautogui.size()
    monitor = (screen_width // 2, screen_height // 2, screen_width, screen_height)
    indicate = True
    with mss.mss() as sct:
        needle = cv2.imread("image.png")
        last_hit = time.time()
        while (current_time := time.time()) - last_hit < LAST_HIT_TIMEOUT:
            screenshot = np.array(sct.grab(monitor))
            haystack = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
            result = cv2.matchTemplate(needle, haystack, cv2.TM_CCOEFF_NORMED)
            if np.any(result > MATCH_THRESHOLD):
                pyautogui.rightClick()
                time.sleep(0.1)
                pyautogui.rightClick()
                print(get_time_string(current_time), colored("Detected", "green"))
                time.sleep(2)
                last_hit = current_time
                indicate = True
            else:
                if indicate:
                    print(get_time_string(current_time), colored("Not detected", "light_yellow"))
                indicate = False
    print(get_time_string(current_time), colored("Have not fished for a long time. Stopping now.", "red"))

if __name__ == "__main__":
    main()

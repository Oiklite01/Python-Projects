import pyautogui as pt
import time
while True:
    start_time = time.time()
    while time.time() - start_time < 5:
            pt.press('down')
    time.sleep(1)

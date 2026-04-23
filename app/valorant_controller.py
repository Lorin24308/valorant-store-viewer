import pyautogui
import time


def click_store_button() -> None:
    time.sleep(2)
    pyautogui.moveTo(1645, 33, duration=0.5)
    pyautogui.click()
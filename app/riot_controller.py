import pyautogui
import time


def click_valorant_icon() -> None:
    time.sleep(1)
    pyautogui.moveTo(369, 716, duration=0.5)
    pyautogui.click()


def click_play_button() -> None:
    time.sleep(2)
    pyautogui.moveTo(641, 551, duration=0.5)
    pyautogui.click()
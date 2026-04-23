import pyautogui
from pathlib import Path
import time


def take_store_screenshot() -> Path:
    time.sleep(2)

    output_dir = Path("data/screenshots")
    output_dir.mkdir(parents=True, exist_ok=True)

    path = output_dir / "store.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(path)

    return path
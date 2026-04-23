from pywinauto import Application
import time


def connect_to_valorant(timeout: int = 60):
    """
    Tenta encontrar e conectar na janela do VALORANT.
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            app = Application(backend="uia").connect(title_re=".*VALORANT.*")
            window = app.window(title_re=".*VALORANT.*")
            return window
        except Exception:
            time.sleep(2)

    return None


def focus_valorant_window(window) -> None:
    try:
        window.set_focus()
        window.restore()
    except Exception:
        pass